#!/usr/bin/env python3
"""反向盤點：書庫的書有沒有站在管，站上的 slug 是不是死鏈（docs/ORPHAN-BOOKS.md）。

用法：
    notes-core/tools/export-orphan-books.py            # 寫進 notes-core/docs/ORPHAN-BOOKS.md
    notes-core/tools/export-orphan-books.py -          # 印到 stdout

星系根目錄（放所有 -note 站的容器目錄）預設推導成 tools/../..；佈局不同時用
NOTES_ROOT= 覆寫，與 new-note.sh / bump-notes-core.sh / export-wanted.py 同慣例。

**為什麼要有這一支**：既有的四個軸全是「**站**說它缺什麼」的正向視角——WANTED-BOOKS
問「標 wanted 的書是不是其實已經建好站了」，DEEPEN-READY 問「這站的書單收齊沒」。
反過來的問題「**書庫裡這本書，有沒有任何站在管**」在此之前只存在於 COVERAGE-GAPS.md
的一段 heredoc 裡：沒有腳本、要人手貼、而且吃站台 `repos.json` 快照。掃描日停在
2026-08-03（當時 1391 本、413 本沒站碰），之後書庫又長了兩百多個 repo，而**新建的書站
沒有任何機制會提醒「這本沒人認領」**——正向的工具永遠看不到它，因為沒有站提過它。
這一支把那段 heredoc 腳本化，並補上另外三類只在 SOURCING-DEBT.md 留過一次性紀錄的破口。

四節產出：
  一、**孤兒書**——`nplus-kind-book` 的 repo，沒有任何站的 bibliography 用 `slug` 指到它。
      缺口靠開新站、或讓既有站認領補。其中「內容頁的 `furtherReading` 已經 anchor 到它、
      bibliography 卻沒登記」的另外抓出來——那類只要補一筆盤點，不必開站，最該先補。
  二、**死鏈 slug**——bibliography 指到不存在的 repo。首頁書架的封面會 404
      （2026-08-04 抓到 8 個、08-05 結清，此後沒有任何機制在看）。
  三、**`owned` 沒有 slug**——`owned` 的語意是「已建成 `nplus.wiki/<slug>/` 書站」，
      slug 是必要條件；沒填就不會出現在首頁書架，等於登記了卻看不到。
  四、**死鏈 anchor**——內容頁 `furtherReading` 的 `book:` 指到不存在的書 repo，
      延伸閱讀連結直接 404。SOURCING-DEBT 只驗過「有沒有 anchor」，沒驗過「anchor 到的
      書在不在」。

另外讀 docs/EXCLUDED-BOOKS.md（手維護的裁決紀錄）：裁定「不進任何站」的書從盤點分母
整個拿掉，摘要留一行計數——不然練習冊、機構教材這類永遠不會被認領的書會在孤兒清單裡
一直提醒，把真正該認領的淹掉。被排除卻仍有站在引＝裁決衝突，輸出裡吵。

**資料源紀律**（這條被違反過，代價是整張清單失真）：權威是 GitHub 現況，不是站台的
`repos.json`。那份快照是 build 時打 API 存下來 commit 進去的，落後好幾天很正常——
2026-08-07 就是拿 08-05 的快照去對 08-07 建的書站，回報「0 本已收錄」，實際上 20 本裡
16 本已經有站。問不到 `gh` 才退回快照，且**一定在輸出頂端標警語**；看到警語就先
`gh auth status`，別拿快照的結論下判斷。

**比對鍵用 repo name，不是書名**——這點與 export-wanted.py 相反，別把那邊的教訓
套過來。那邊是拿「書名」去猜 repo（因為 `wanted` 的書還沒有 slug，只能靠 description
的書名欄模糊比對，於是需要 ALIASES／NAME_COLLISIONS 那一整套）。這邊比的是
bibliography 已經寫死的 `slug` 對 repo name，兩者本來就該**逐字相同**——slug 就是
`nplus.wiki/<slug>/` 的路徑，不同就是死鏈。所以這支不需要模糊比對，也不會有它的偽陽性。
"""

import collections
import json
import os
import re
import subprocess
import sys
import datetime as _dt

from _stamp import stamp
from io import StringIO
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTES_ROOT = Path(os.environ.get("NOTES_ROOT") or HERE.parent.parent)
PORTAL_REPOS = NOTES_ROOT / ".." / "sites" / "nplus-father.github.io" / "src" / "data" / "repos.json"
OUT = HERE.parent / "docs" / "ORPHAN-BOOKS.md"
EXCLUDED_DOC = HERE.parent / "docs" / "EXCLUDED-BOOKS.md"  # 刻意排除的裁決紀錄（手維護）

PORTAL_OWNERS = ("nplus-father", "Andrewnplus")
BOOK_TOPIC = "nplus-kind-book"
SNAPSHOT_STALE_DAYS = 2  # 退回快照時，超過這個天數就在輸出裡吵

# 「該開新站」的判準，沿用 COVERAGE-GAPS.md 2026-08-03 那輪掃描定下來的門檻：
# 藏書夠多（少於這個數字開站撐不起一個站）且大多沒人碰（比例低＝已經有站在管、
# 只是還沒寫完，那是 ENRICH-BACKLOG 的事，不是這裡的事）。
NEW_STATION_MIN_BOOKS = 8
NEW_STATION_MIN_UNCOVERED_PCT = 60

# 「該開作者站／讓既有站認領」的判準：同一作者累積這麼多本沒人認領。
# COVERAGE-GAPS 的人物缺口 A 類就是這樣抓出 covey／templar／navarro 三站的。
AUTHOR_MIN_ORPHANS = 3

# leaf 覆蓋率表列到幾名為止（全部 leaf 太長，尾巴都是 1–2 本的零頭）。
# 全部孤兒書仍會在「全部孤兒書」那節逐本列出，不會因為這個上限漏掉。
LEAF_TABLE_LIMIT = 30


def esc(s):
    """表格欄位裡的管線與換行會把 Markdown 表格打斷。"""
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


def load_excluded():
    """docs/EXCLUDED-BOOKS.md 表格裡的 repo slug——裁定「不進任何站」的書。

    抓的是表格列開頭的 `` | `slug` `` 樣式；沒有這份檔就當空集合，行為與加這個
    機制之前完全相同。排除≠刪 repo：書庫照舊，只是孤兒盤點不再提醒。
    """
    if not EXCLUDED_DOC.is_file():
        return set()
    return set(re.findall(r"^\|\s*`([A-Za-z0-9._-]+)`", EXCLUDED_DOC.read_text(encoding="utf-8"), re.M))


def entries_of(src):
    """抓 defineBibliography([...]) 裡 depth-1 的物件字面值（字串內的括號不算）。

    與 export-deepen-ready.py 同一份實作。不用 `\\{[^{}]*\\}` 那種天真正則——
    條目裡只要出現巢狀物件就會被切壞。
    """
    start = src.find("defineBibliography(")
    if start < 0:
        return []
    out = []
    depth, buf, quote, esc_next = 0, [], None, False
    for ch in src[src.index("[", start) + 1 :]:
        if quote:
            buf.append(ch)
            if esc_next:
                esc_next = False
            elif ch == "\\":
                esc_next = True
            elif ch == quote:
                quote = None
            continue
        if ch in "\"'`":
            quote = ch
            buf.append(ch)
            continue
        if ch == "{":
            depth += 1
            if depth == 1:
                buf = []
                continue
        elif ch == "}":
            depth -= 1
            if depth == 0:
                out.append("".join(buf))
                continue
        elif ch == "]" and depth == 0:
            break
        if depth >= 1:
            buf.append(ch)
    return out


def field(entry, name):
    m = re.search(rf'\b{name}\s*:\s*"((?:[^"\\]|\\.)*)"', entry)
    return m.group(1) if m else None


def load_portal():
    """回傳 (items, source, age_note)。先問 GitHub（權威），失敗才退回站台快照。

    快照是站台 build 時存下來 commit 進去的，落後幾天很正常——退回去用就一定要在
    輸出裡標明，否則「0 本孤兒書」會被當成事實。與 export-wanted.py 同一套紀律。
    """
    items = []
    for owner in PORTAL_OWNERS:
        try:
            out = subprocess.run(
                ["gh", "repo", "list", owner, "--limit", "2000", "--json", "name,description,repositoryTopics"],
                capture_output=True, text=True, timeout=120, check=True,
            ).stdout
        except (OSError, subprocess.SubprocessError):
            items = []
            break
        for r in json.loads(out):
            items.append(
                {
                    "name": r["name"],
                    "description": r.get("description") or "",
                    "topics": [t["name"] for t in (r.get("repositoryTopics") or [])],
                }
            )
    if items:
        return items, f"GitHub 現況（`gh repo list` {'／'.join(PORTAL_OWNERS)}，{len(items)} 個 repo）", ""

    snap = json.loads(PORTAL_REPOS.read_text(encoding="utf-8"))
    fetched = snap.get("fetchedAt", "")
    age = ""
    try:
        import datetime as _dt

        days = (_dt.datetime.now(_dt.timezone.utc) - _dt.datetime.fromisoformat(fetched.replace("Z", "+00:00"))).days
        if days >= SNAPSHOT_STALE_DAYS:
            age = f"⚠ **快照已經 {days} 天沒更新，孤兒書那節會把剛建好的書站全當成孤兒**——`gh auth login` 後重跑才準。"
    except ValueError:
        age = "⚠ **快照時間戳讀不出來，無法判斷新舊。**"
    return (
        [{"name": i["name"], "description": i.get("description") or "", "topics": i.get("topics") or []} for i in snap["items"]],
        f"站台快照 `repos.json`（fetchedAt {fetched}，{len(snap['items'])} 個 repo）",
        age,
    )


def topic_of(book, prefix):
    return next((t[len(prefix) :] for t in book["topics"] if t.startswith(prefix)), "")


def scan_stations():
    """掃全星系，回傳 (cited, owned_no_slug, anchors)。

    cited: slug -> [站…]（bibliography 寫了 slug 的，不分 status——寫了 slug 就是認領）
    owned_no_slug: (站, title) 清單
    anchors: slug -> [「站/相對路徑」…]（內容頁 furtherReading 的 book:）
    """
    cited = collections.defaultdict(list)
    owned_no_slug = []
    anchors = collections.defaultdict(list)

    for bib in sorted(NOTES_ROOT.glob("*-note/src/data/bibliography.ts")):
        station = bib.parts[len(NOTES_ROOT.parts)]
        for e in entries_of(bib.read_text(encoding="utf-8")):
            slug, status = field(e, "slug"), field(e, "status")
            if slug:
                cited[slug].append(station)
            elif status == "owned":
                owned_no_slug.append((station, field(e, "title") or "（無 title）"))

    for station_dir in sorted(NOTES_ROOT.glob("*-note")):
        content = station_dir / "src" / "content"
        if not content.is_dir():
            continue
        for page in sorted(content.rglob("*.md")):
            # 一頁可以錨同一本書的好幾章（`furtherReading` 每章一筆），
            # 這裡數的是「幾頁在引」不是「幾個 anchor」，所以逐頁去重。
            for slug in dict.fromkeys(
                re.findall(
                    r'^\s*-\s*book:\s*"?([A-Za-z0-9][A-Za-z0-9._-]*)"?\s*$',
                    page.read_text(encoding="utf-8"),
                    re.M,
                )
            ):
                anchors[slug].append(f"{station_dir.name}/{page.relative_to(station_dir / 'src' / 'content')}")

    return cited, owned_no_slug, anchors


def main():
    items, source, age_note = load_portal()
    books = [b for b in items if BOOK_TOPIC in b["topics"]]
    by_name = {b["name"]: b for b in books}
    repo_names = {i["name"] for i in items}

    for b in books:
        parts = [p.strip() for p in b["description"].split("|")]
        b["book_title"] = parts[0] if parts and parts[0] else b["name"]
        b["book_author"] = parts[1] if len(parts) >= 2 else ""
        b["leaf"] = topic_of(b, "leaf-") or "（無 leaf）"
        b["sub"] = topic_of(b, "sub-") or "（無 sub）"

    cited, owned_no_slug, anchors = scan_stations()

    # 刻意排除的書（EXCLUDED-BOOKS.md 裁決）：從盤點分母整個拿掉——孤兒、leaf 覆蓋率、
    # 作者統計都不算它，只在摘要留一行計數。被排除卻仍有站在引的是裁決衝突，要吵；
    # 這種情況下那本書照常留在盤點裡（引用是現實，裁決只是主張）。
    excluded = load_excluded()
    raw_book_count = len(books)
    excluded_claimed = sorted(n for n in excluded if n in cited)
    excluded_books = [b for b in books if b["name"] in excluded and b["name"] not in cited]
    books = [b for b in books if b["name"] not in excluded or b["name"] in cited]

    orphans = [b for b in books if b["name"] not in cited]
    # 內容頁已經 anchor 到、bibliography 卻沒登記——補一筆盤點就好，不必開站。
    unlisted = [b for b in orphans if b["name"] in anchors]
    dead_slugs = sorted(s for s in cited if s not in repo_names)
    dead_anchors = sorted(s for s in anchors if s not in repo_names)

    # 每個 leaf 目前是誰在管：該 leaf 已覆蓋的書，是被哪些站引用的。
    # 這欄回答「孤兒該歸誰認領」——比「該不該開新站」更常用的那個答案。
    leaf_total = collections.Counter(b["leaf"] for b in books)
    leaf_orphan = collections.Counter(b["leaf"] for b in orphans)
    leaf_owners = collections.defaultdict(collections.Counter)
    for b in books:
        for st in cited.get(b["name"], []):
            leaf_owners[b["leaf"]][st.replace("-note", "")] += 1

    o = StringIO()
    w = o.write

    w("# 孤兒書與死鏈（反向盤點）\n\n")
    w(
        "**這份是什麼**：從**書庫那一側**反過來問的四個問題——書庫的書有沒有站在管、"
        "站上的 slug 指得到書嗎。由 `notes-core/tools/export-orphan-books.py` 生成，"
        "**不要手改**——改各站的 bibliography／內容再重跑。\n\n"
    )
    w(
        "**為什麼需要反向**：另外幾份都是「站說它缺什麼」的正向視角，看不到「**沒有任何站提過**」"
        "的書——新建的書站如果沒人認領，正向工具永遠不會提醒你，因為沒有站提過它。\n\n"
    )
    w(f"**資料源**：{source}，其中 `{BOOK_TOPIC}` 的書 repo {raw_book_count} 本")
    if excluded_books:
        w(f"（{len(excluded_books)} 本經 [EXCLUDED-BOOKS.md](./EXCLUDED-BOOKS.md) 裁決排除，不入盤點）")
    w("。\n\n")
    if age_note:
        w(f"> {age_note}\n\n")

    w("| 文件 | 缺口是什麼 | 靠什麼補 |\n| --- | --- | --- |\n")
    w("| [COVERAGE-GAPS.md](./COVERAGE-GAPS.md) | 還沒有**站** | 開新站 |\n")
    w("| [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md) | 站在、**內容**沒寫完 | `note-check --enrich` |\n")
    w("| [SOURCING-DEBT.md](./SOURCING-DEBT.md) | 內容寫了、查不到**出處** | 掛 anchor |\n")
    w("| [WANTED-BOOKS.md](./WANTED-BOOKS.md) | **書本身**還沒有 | 去收書 |\n")
    w("| **本檔** | **書有了、沒有站在管**（或指到的書不存在） | 認領／開站／修 slug |\n\n")

    w("## 摘要\n\n")
    w("| 檢查 | 數 | 後果 |\n| --- | ---: | --- |\n")
    w(f"| 孤兒書（沒有任何站的 bibliography 指到） | **{len(orphans)}** | 書站建了但沒有筆記在用，等於白建 |\n")
    w(f"| ↳ 其中內容頁已經 anchor 到、盤點沒登記 | **{len(unlisted)}** | 補一筆 bibliography 就好，不必開站 |\n")
    w(f"| 刻意排除（[EXCLUDED-BOOKS.md](./EXCLUDED-BOOKS.md) 裁決不進任何站） | **{len(excluded_books)}** | 不列孤兒、不再提醒 |\n")
    w(f"| 死鏈 slug（bibliography 指到不存在的 repo） | **{len(dead_slugs)}** | 首頁書架封面 404 |\n")
    w(f"| `owned` 沒有 slug | **{len(owned_no_slug)}** | 不會出現在首頁書架，登記了卻看不到 |\n")
    w(f"| 死鏈 anchor（內容頁 `book:` 指到不存在的 repo） | **{len(dead_anchors)}** | 延伸閱讀連結 404 |\n\n")

    if excluded_claimed:
        w(
            "> ⚠ **裁決衝突**：下列 slug 在 [EXCLUDED-BOOKS.md](./EXCLUDED-BOOKS.md) 被排除，"
            "卻有站的 bibliography 用 `slug` 指到它——去掉那筆引用，或刪掉排除那行重跑："
            + "、".join(f"`{s}`" for s in excluded_claimed)
            + "\n\n"
        )

    # ── 一、孤兒書 ────────────────────────────────────────────────
    w(f"## 一、孤兒書：{len(orphans)} 本沒有任何站認領\n\n")
    w(
        "判準＝這本書的 repo name 沒有出現在**任何**站 `bibliography.ts` 的 `slug` 欄。"
        "用 slug 而不是站數對書數，是因為它抓得到跨站分工——一本書被別站認領也算覆蓋。\n\n"
    )

    w(f"### 1a. 內容已經引了、盤點沒登記：{len(unlisted)} 本\n\n")
    if unlisted:
        w(
            "**這批最該先補。** 站內已經有頁 `furtherReading` 錨到這本書，代表書確實在被用，"
            "只是那一站的 bibliography 漏登記——補一筆 `status: \"owned\"` ＋ `slug` 即可，"
            "不必開新站、也不必判斷歸誰。\n\n"
        )
        w("| 書 repo | 書名 | 作者 | 哪些頁在引 |\n| --- | --- | --- | --- |\n")
        for b in sorted(unlisted, key=lambda b: b["name"]):
            pages = anchors[b["name"]]
            shown = "、".join(f"`{p}`" for p in pages[:3]) + (f" 等 {len(pages)} 處" if len(pages) > 3 else "")
            w(f"| `{b['name']}` | {esc(b['book_title'])} | {esc(b['book_author'])} | {shown} |\n")
        w("\n")
    else:
        w("無——內容引用到的書都已經登記在盤點裡。\n\n")

    flagged = [
        (leaf, leaf_orphan[leaf], leaf_total[leaf])
        for leaf in leaf_orphan
        if leaf_total[leaf] >= NEW_STATION_MIN_BOOKS
        and leaf_orphan[leaf] / leaf_total[leaf] * 100 >= NEW_STATION_MIN_UNCOVERED_PCT
    ]
    w(f"### 1b. 開新站候選：{len(flagged)} 個 leaf\n\n")
    w(
        f"判準沿用 COVERAGE-GAPS 那輪：**藏書 ≥{NEW_STATION_MIN_BOOKS} 本且未覆蓋 "
        f"≥{NEW_STATION_MIN_UNCOVERED_PCT}%**。低於這個比例的 leaf 表示已經有站在管、"
        "只是還沒寫完——那是 [ENRICH-BACKLOG](./ENRICH-BACKLOG.md) 的事，不是這裡的。\n\n"
    )
    if flagged:
        w("| leaf | 未覆蓋/總數 | 未覆蓋率 | 沒人認領的是哪幾本 |\n| --- | ---: | ---: | --- |\n")
        for leaf, n, tot in sorted(flagged, key=lambda x: (-x[1] / x[2], -x[1])):
            titles = "、".join(esc(b["book_title"]) for b in orphans if b["leaf"] == leaf)
            w(f"| `{leaf}` | {n}/{tot} | **{n / tot * 100:.0f}%** | {titles} |\n")
        w("\n")
    else:
        w("無——沒有任何 leaf 同時滿足「書夠多」與「大多沒人碰」。\n\n")

    w("### 1c. 各 leaf 覆蓋率與目前誰在管\n\n")
    w(
        "**看比例不是看絕對數。** 未覆蓋比例高＝沒站在管（開新站）；絕對數高但比例低＝有站在管、"
        "只是還沒寫完。「目前誰在管」是該 leaf **已覆蓋**的書被哪些站引用——"
        "孤兒通常就該歸這幾站認領，不必另外開站。\n\n"
    )
    w("| leaf | sub | 未覆蓋/總數 | 未覆蓋率 | 目前誰在管 |\n| --- | --- | ---: | ---: | --- |\n")
    leaf_sub = {b["leaf"]: b["sub"] for b in books}
    for leaf, n in leaf_orphan.most_common(LEAF_TABLE_LIMIT):
        tot = leaf_total[leaf]
        owners = "、".join(f"{s}({c})" for s, c in leaf_owners[leaf].most_common(3)) or "**沒有站在管**"
        w(f"| `{leaf}` | {leaf_sub.get(leaf, '')} | {n}/{tot} | {n / tot * 100:.0f}% | {owners} |\n")
    if len(leaf_orphan) > LEAF_TABLE_LIMIT:
        w(f"\n> 另有 {len(leaf_orphan) - LEAF_TABLE_LIMIT} 個 leaf 各有 1–{leaf_orphan.most_common(LEAF_TABLE_LIMIT)[-1][1]} 本孤兒，逐本列在下面「全部孤兒書」那節。\n")
    w("\n")

    author_orphans = collections.defaultdict(list)
    for b in orphans:
        if b["book_author"]:
            author_orphans[b["book_author"]].append(b)
    hot_authors = sorted(
        ((a, bs) for a, bs in author_orphans.items() if len(bs) >= AUTHOR_MIN_ORPHANS),
        key=lambda x: (-len(x[1]), x[0]),
    )
    w(f"### 1d. 同一作者 ≥{AUTHOR_MIN_ORPHANS} 本沒人認領：{len(hot_authors)} 位\n\n")
    w(
        "作者站的線索。**有同名站就是該站漏收**（回去補 bibliography），"
        "沒有站才是開站候選——COVERAGE-GAPS 的人物缺口就是這樣抓出 covey／templar／navarro 三站的。\n\n"
    )
    if hot_authors:
        w("| 作者 | 孤兒本數 | 已有作者站？ | 書 |\n| --- | ---: | --- | --- |\n")
        stations = {p.name for p in NOTES_ROOT.glob("*-note")}
        for author, bs in hot_authors:
            # 作者站的 key 沒有規則可推（Henri J. M. Nouwen → nouwen-note），拿姓氏碰碰看；
            # 碰不到只是沒印出提示，不影響清單本身。
            surname = re.sub(r"[^a-z]", "", author.split()[-1].lower()) if author.split() else ""
            has = f"`{surname}-note`" if surname and f"{surname}-note" in stations else "—"
            w(
                f"| {esc(author)} | {len(bs)} | {has} | "
                + "、".join(esc(b["book_title"]) for b in sorted(bs, key=lambda b: b["name"]))
                + " |\n"
            )
        w("\n")
    else:
        w("無。\n\n")

    w(f"### 1e. 全部 {len(orphans)} 本（依 leaf 分組）\n\n")
    for leaf, n in leaf_orphan.most_common():
        owners = "、".join(f"{s}({c})" for s, c in leaf_owners[leaf].most_common(3)) or "**沒有站在管**"
        w(f"#### `{leaf}` — {n}/{leaf_total[leaf]} 沒人認領（目前：{owners}）\n\n")
        w("| 書 repo | 書名 | 作者 |\n| --- | --- | --- |\n")
        for b in sorted((b for b in orphans if b["leaf"] == leaf), key=lambda b: b["name"]):
            w(f"| `{b['name']}` | {esc(b['book_title'])} | {esc(b['book_author']) or '⚠ 描述沒有作者欄'} |\n")
        w("\n")

    # ── 二、死鏈 slug ─────────────────────────────────────────────
    w(f"## 二、死鏈 slug：{len(dead_slugs)} 個\n\n")
    w(
        "bibliography 的 `slug` 在書庫裡找不到對應 repo——**首頁書架的封面會 404**。"
        "兩種收法（2026-08-04 那批 8 個就是這樣分的）：書其實該有就**補建書 repo**，"
        "書根本不存在就**撤掉這筆 `slug`**，不要掛死鏈。\n\n"
    )
    if dead_slugs:
        w("| slug | 登記在 |\n| --- | --- |\n")
        for s in dead_slugs:
            w(f"| `{s}` | {'、'.join(cited[s])} |\n")
        w("\n")
    else:
        w("無——所有 `slug` 都指得到真的 repo。\n\n")

    # ── 三、owned 沒有 slug ───────────────────────────────────────
    w(f"## 三、`owned` 沒有 slug：{len(owned_no_slug)} 筆\n\n")
    w(
        "`owned` 的語意是「已經做成 `nplus.wiki/<slug>/` 書站」，slug 是必要條件。"
        "沒填 slug 的 `owned` **不會出現在首頁書架的封面列**，概念頁的 "
        "`furtherReading.anchor` 也無處可指——書登記了卻看不到。"
        "書真的有就補 slug；其實還沒收就改回 `wanted`。\n\n"
    )
    if owned_no_slug:
        w("| 站 | 書名 |\n| --- | --- |\n")
        for station, title in sorted(owned_no_slug):
            w(f"| `{station}` | {esc(title)} |\n")
        w("\n")
    else:
        w("無——每一筆 `owned` 都有 slug。\n\n")

    # ── 四、死鏈 anchor ───────────────────────────────────────────
    w(f"## 四、死鏈 anchor：{len(dead_anchors)} 個 slug\n\n")
    w(
        "內容頁 `furtherReading` 的 `book:` 指到不存在的書 repo——延伸閱讀連結 404。"
        "[SOURCING-DEBT](./SOURCING-DEBT.md) 只驗過「頁有沒有 anchor」，"
        "沒驗過「anchor 到的書在不在」。\n\n"
    )
    if dead_anchors:
        w("| book slug | 出現在哪些頁 |\n| --- | --- |\n")
        for s in dead_anchors:
            pages = anchors[s]
            shown = "、".join(f"`{p}`" for p in pages[:5]) + (f" 等 {len(pages)} 處" if len(pages) > 5 else "")
            w(f"| `{s}` | {shown} |\n")
        w("\n")
    else:
        w("無——所有 anchor 都指得到真的 repo。\n\n")

    w(
        """## 重跑

```bash
notes-core/tools/export-orphan-books.py
```

認領一本孤兒＝在該站 `bibliography.ts` 加一筆 `status: "owned"` ＋ `slug: "<repo name>"`，
重跑就會從這裡消失。整個 leaf 都沒站在管就走 `/note-new-station`。
裁定**永遠不進任何站**＝在 [EXCLUDED-BOOKS.md](./EXCLUDED-BOOKS.md) 加一行，重跑後不再提醒。
"""
    )

    # 新鮮度戳記：生成物看起來永遠跟剛跑完一樣，不寫上去就沒人分得出今天算的還是三週前算的。
    text = stamp(o.getvalue(), "tools/export-orphan-books.py", _dt.datetime.now().astimezone().isoformat(timespec="seconds"))
    if len(sys.argv) > 1 and sys.argv[1] == "-":
        sys.stdout.write(text)
    else:
        OUT.write_text(text, encoding="utf-8")
        print(
            f"{OUT}: 孤兒 {len(orphans)} 本（其中 {len(unlisted)} 本內容已引）、"
            f"刻意排除 {len(excluded_books)} 本、"
            f"死鏈 slug {len(dead_slugs)}、owned 缺 slug {len(owned_no_slug)}、"
            f"死鏈 anchor {len(dead_anchors)}"
        )


if __name__ == "__main__":
    main()
