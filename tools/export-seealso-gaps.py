#!/usr/bin/env python3
"""匯出「同書同章、卻沒有互相 seeAlso」的跨站連結缺口（docs/SEEALSO-GAPS.md）。

用法：
    notes-core/tools/export-seealso-gaps.py            # 寫進 notes-core/docs/SEEALSO-GAPS.md
    notes-core/tools/export-seealso-gaps.py -          # markdown 印到 stdout
    notes-core/tools/export-seealso-gaps.py --json     # 給 apply-seealso.py 吃的決策 JSON（stdout）
    notes-core/tools/export-seealso-gaps.py --station <name>   # 只看一站（當來源）

星系根目錄預設推導成 tools/../..；佈局不同時用 NOTES_ROOT= 覆寫，與其他 export-*.py 同慣例。

**為什麼要有這份**：契約層（溯源、判層、related 雙向、roadmap／mastery）全綠之後，星系的
下一個薄處是「站與站之間」。2026-11-06 盤點：2233 個概念頁只有 225 頁（10%）有任何 `seeAlso`，
四十多站一條跨站連結都沒有——79 個站各自封閉，首頁 schools 卡的跨站門是唯一的通道。
同一本書的同一章，常常同時撐著主題站的一頁與人物站的一頁（leadership 的 level-5 頁與 collins
的 level-5 頁都掛《從 A 到 A+》同一章），讀者在任一邊都看不到另一邊。

**判準（只報 strong）**：兩頁的 `furtherReading` 有**同一本書的同一個 anchor**，且來源頁還沒有
任何 `seeAlso` 指到目標站。「同書不同章」只算 weak，列數字不開單——同一本書的不同章可能講
完全不同的事，掛上去是雜訊。

**選目標頁**：同一個目標站裡，候選頁同屬一個分類且 ≥3 頁 → 連分類頁（`concepts/<cat>/`，
label 用該分類的 `name`）；否則依共用章節數排序，最多連 2 頁，label 用目標頁的 `title`。
label 不另寫文案——那是頁面自己的標題，不會過期成第二份事實。

**不自動雙向**：A→B 與 B→A 各自獨立判斷（B 可能早就連到 A 的站），兩邊都缺就兩邊都列。

**strict 站的 enum**：技術站群（sites.ts `seeAlsoMode: "strict"`）的 `seeAlso.site` 走 `siteKeys` enum，而那個
enum 只含技術站自己的 key——clean-code 連不到 uncle-bob、kent-beck、fowler 這些作者站，build 會直接紅
（2026-11-06 首跑踩到）。這類缺口**另列「被 schema 擋住」**，不進決策 JSON；要放行得改 notes-core 的 enum。

套用走 `tools/apply-seealso.py`，不要讓模型逐頁改 frontmatter。
"""

import datetime as _dt
import json
import os
import re
import sys
from collections import Counter, defaultdict
from io import StringIO
from pathlib import Path

from _stamp import stamp

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("NOTES_ROOT", HERE.parent.parent))
OUT = HERE.parent / "docs" / "SEEALSO-GAPS.md"
CAT_LINK_MIN = 3
MAX_PAGES_PER_TARGET = 2

FM_RE = re.compile(r"^---\n(.*?)\n---", re.S)
FR_RE = re.compile(
    r"-\s*book:\s*\"?([\w.-]+)\"?\s*\n(?:\s+label:[^\n]*\n)?(?:\s+anchor:\s*\"?([^\"\n]+)\"?)?"
)


def site_keys() -> dict[str, str]:
    """key → axis，來自 sites.ts（星系成員的 SSOT）。"""
    src = (ROOT / "notes-core" / "src" / "lib" / "sites.ts").read_text(encoding="utf-8")
    return {m.group(1): m.group(2) for m in re.finditer(r'key:\s*"([^"]+)".*?axis:\s*"(\w+)"', src)}


def strict_keys() -> set[str]:
    """seeAlsoMode: "strict" 的站——它們的 seeAlso.site 只能是這個集合裡的 key（content.ts 的 siteKeys enum）。"""
    src = (ROOT / "notes-core" / "src" / "lib" / "sites.ts").read_text(encoding="utf-8")
    return {m.group(1) for m in re.finditer(r'key:\s*"([^"]+)".*?seeAlsoMode:\s*"strict"', src)}


def frontmatter(path: Path) -> str:
    m = FM_RE.match(path.read_text(encoding="utf-8"))
    return m.group(1) if m else ""


def title_of(fm: str, fallback: str) -> str:
    m = re.search(r'^title:\s*(.*?)\s*$', fm, re.M)
    if not m:
        return fallback
    t = m.group(1).strip()
    if len(t) >= 2 and t[0] == t[-1] and t[0] in "\"'":
        t = t[1:-1]
    return t.replace('\\"', '"')


def scan():
    keys = site_keys()
    pages = {}  # (station, cat/slug) → {"title", "anchors": set[(book, anchor)], "seealso_sites": set}
    cat_names = {}  # (station, cat) → name
    for d in sorted(ROOT.glob("*-note")):
        station = d.name[: -len("-note")]
        if station not in keys:
            continue
        cdir = d / "src" / "content" / "concepts"
        if not cdir.is_dir():
            continue
        for idx in cdir.glob("*/_index.md"):
            cat_names[(station, idx.parent.name)] = title_of(
                re.sub(r"^title:", "x:", frontmatter(idx), flags=re.M).replace("name:", "title:", 1),
                idx.parent.name,
            )
        for p in cdir.glob("*/*.md"):
            if p.name == "_index.md":
                continue
            fm = frontmatter(p)
            rel = f"{p.parent.name}/{p.stem}"
            anchors = {(b, (a or "").strip().strip("/")) for b, a in FR_RE.findall(fm) if a}
            sites = set(re.findall(r"^\s*-\s*site:\s*\"?([\w-]+)\"?", fm, re.M))
            pages[(station, rel)] = {"title": title_of(fm, p.stem), "anchors": anchors, "seealso": sites}

    by_anchor = defaultdict(set)
    by_book = defaultdict(set)
    for pid, info in pages.items():
        for b, a in info["anchors"]:
            by_anchor[(b, a)].add(pid)
            by_book[b].add(pid)

    # strong：(src page, dst station) → Counter(dst page → 共用章節數)
    strong = defaultdict(Counter)
    for (b, a), pids in by_anchor.items():
        by_station = defaultdict(list)
        for pid in pids:
            by_station[pid[0]].append(pid)
        if len(by_station) < 2:
            continue
        for sx, px in by_station.items():
            for sy, py in by_station.items():
                if sx == sy:
                    continue
                for pa in px:
                    if sy in pages[pa]["seealso"]:
                        continue
                    for pb in py:
                        strong[(pa, sy)][pb] += 1

    weak_pairs = 0
    for b, pids in by_book.items():
        by_station = defaultdict(list)
        for pid in pids:
            by_station[pid[0]].append(pid)
        if len(by_station) < 2:
            continue
        for sx, px in by_station.items():
            for sy in by_station:
                if sx == sy:
                    continue
                for pa in px:
                    if sy not in pages[pa]["seealso"] and (pa, sy) not in strong:
                        weak_pairs += 1

    strict = strict_keys()
    decisions = defaultdict(list)  # station → [{page, add:[{site,path,label}]}]
    rows = []  # (src station, src page, src title, dst station, [(path,label,shared)])
    blocked = []  # strict 站指向非技術站：schema 不收，只列不開單
    for (pa, sy), counter in sorted(strong.items()):
        if pa[0] in strict and sy not in strict:
            blocked.append((pa[0], pa[1], pages[pa]["title"], sy, len(counter)))
            continue
        by_cat = defaultdict(list)
        for pb, n in counter.items():
            by_cat[pb[1].split("/")[0]].append((pb, n))
        adds = []
        for cat, items in sorted(by_cat.items()):
            if len(items) >= CAT_LINK_MIN:
                adds.append((f"concepts/{cat}/", cat_names.get((sy, cat), cat), sum(n for _, n in items), True))
            else:
                for pb, n in sorted(items, key=lambda x: (-x[1], pages[x[0]]["title"])):
                    adds.append((f"concepts/{pb[1]}/", pages[pb]["title"], n, False))
        cats = [x for x in adds if x[3]]
        singles = sorted([x for x in adds if not x[3]], key=lambda x: (-x[2], x[1]))[:MAX_PAGES_PER_TARGET]
        chosen = cats + singles
        rows.append((pa[0], pa[1], pages[pa]["title"], sy, chosen))
        decisions[f"{pa[0]}-note"].append(
            {"page": pa[1], "add": [{"site": sy, "path": path, "label": label} for path, label, _, _ in chosen]}
        )
    return keys, pages, rows, decisions, weak_pairs, blocked


def main() -> None:
    args = sys.argv[1:]
    only = args[args.index("--station") + 1] if "--station" in args else None
    if only and only.endswith("-note"):
        only = only[: -len("-note")]
    keys, pages, rows, decisions, weak_pairs, blocked = scan()
    if only:
        rows = [r for r in rows if r[0] == only]
        blocked = [b for b in blocked if b[0] == only]
        decisions = {k: v for k, v in decisions.items() if k == f"{only}-note"}

    if "--json" in args:
        json.dump(decisions, sys.stdout, ensure_ascii=False, indent=1)
        sys.stdout.write("\n")
        return

    total_pages = len(pages)
    linked_now = sum(1 for p in pages.values() if p["seealso"])
    src_pages = {(r[0], r[1]) for r in rows}
    linked_after = len({pid for pid, p in pages.items() if p["seealso"]} | src_pages)
    per_src = Counter(r[0] for r in rows)
    per_pair = Counter((r[0], r[3]) for r in rows)
    no_seealso_stations = sorted(
        {s for s, _ in pages} - {s for (s, _), p in pages.items() if p["seealso"]}
    )

    o = StringIO()
    o.write("# 跨站連結缺口（同書同章、卻沒有互相 seeAlso）\n\n")
    o.write(
        "**這份是什麼**：兩個站的概念頁掛了**同一本書的同一章**，來源頁卻沒有任何 `seeAlso` 指到對方那一站。\n"
        "由 `notes-core/tools/export-seealso-gaps.py` 生成，**不要手改**——補各站的 seeAlso 再重跑。\n\n"
        "**為什麼要補**：契約層全綠之後，星系最薄的是站與站之間。同一章同時撐著主題站的一頁與人物站的一頁，\n"
        "讀者在任一邊都看不到另一邊——79 個站各自封閉，首頁 schools 卡的跨站門是唯一通道。\n"
        "頁級的「Dive Deeper」就是為這件事存在的，它的使用率卻只有一成。\n\n"
        "**判準只收 strong**：同書**同章**。同書不同章只列數字（weak），不開單——不同章可能講完全不同的事。\n\n"
    )
    o.write(
        f"目前：{total_pages} 個概念頁，有 seeAlso 的 **{linked_now} 頁（{linked_now / total_pages * 100:.0f}%）**；"
        f"一條跨站連結都沒有的站 **{len(no_seealso_stations)}**。\n"
        f"strong 缺口 **{len(rows)} 筆**（來源頁 {len(src_pages)}，分佈在 {len(per_src)} 站）；"
        f"全部補上後有 seeAlso 的頁變成 **{linked_after}（{linked_after / total_pages * 100:.0f}%）**。"
        f"weak（同書不同章）另有 {weak_pairs} 筆，只供參考。\n"
        f"另有 **{len(blocked)} 筆被 schema 擋住**（strict 站指向非技術站，見下節）。\n\n"
    )
    if no_seealso_stations:
        o.write("> [!NOTE]\n> 目前零跨站連結的站：" + "、".join(f"`{s}`" for s in no_seealso_stations) + "\n\n")

    o.write("## 各站缺口（當來源）\n\n")
    o.write("缺越多排越前；缺 0 的站略去。軸別來自 sites.ts。\n\n")
    o.write("| 站 | 軸 | 缺口 | 主要去向 |\n| --- | --- | ---: | --- |\n")
    for s, n in per_src.most_common():
        dests = Counter({sy: c for (sx, sy), c in per_pair.items() if sx == s})
        o.write(f"| `{s}` | {keys.get(s, '?')} | {n} | " + "、".join(f"{sy} {c}" for sy, c in dests.most_common(4)) + " |\n")

    tp = sum(c for (sx, sy), c in per_pair.items() if keys.get(sx) == "topic" and keys.get(sy) == "person")
    pt = sum(c for (sx, sy), c in per_pair.items() if keys.get(sx) == "person" and keys.get(sy) == "topic")
    tt = sum(c for (sx, sy), c in per_pair.items() if keys.get(sx) == "topic" and keys.get(sy) == "topic")
    pp = sum(c for (sx, sy), c in per_pair.items() if keys.get(sx) == "person" and keys.get(sy) == "person")
    o.write(f"\n軸向：主題→人物 {tp}、人物→主題 {pt}、主題→主題 {tt}、人物→人物 {pp}。\n")

    o.write("\n## 逐筆清單\n\n")
    o.write("格式：來源頁 → 目標站：要掛的 path（label）。分類頁＝該分類 ≥3 頁同時命中，連分類不連單頁。\n")
    cur = None
    for sx, page, title, sy, chosen in rows:
        if sx != cur:
            cur = sx
            o.write(f"\n### {cur}（{per_src[cur]} 筆）\n\n")
        targets = "；".join(f"`{path}`（{label}）" for path, label, _, _ in chosen)
        o.write(f"- `{page}`「{title}」 → **{sy}**：{targets}\n")

    o.write("\n## 被 schema 擋住的缺口（strict 站 → 非技術站）\n\n")
    o.write(
        "技術站群的 `seeAlso.site` 走 `siteKeys` enum，目前只含技術站自己的 key。這些缺口**真實存在**\n"
        "（同書同章），但寫進 frontmatter build 會紅。要放行得改 notes-core：讓 enum 涵蓋全部 79 個 key\n"
        "（仍是封閉集合，拼錯照樣抓得到），升版後重跑本工具它們就會進決策 JSON。\n\n"
    )
    if blocked:
        bc = Counter((b[0], b[3]) for b in blocked)
        o.write("| 來源站 | 目標站 | 筆數 |\n| --- | --- | ---: |\n")
        for (sx, sy), n in bc.most_common():
            o.write(f"| `{sx}` | `{sy}` | {n} |\n")
        o.write("\n<details><summary>逐筆</summary>\n\n")
        for sx, page, title, sy, n in blocked:
            o.write(f"- `{sx}` `{page}`「{title}」 → **{sy}**（共用 {n} 章）\n")
        o.write("\n</details>\n")
    else:
        o.write("無。\n")
    o.write(
        "\n## 套用\n\n"
        "```bash\n"
        "notes-core/tools/export-seealso-gaps.py --json > /tmp/seealso.json\n"
        "notes-core/tools/apply-seealso.py /tmp/seealso.json            # 乾跑\n"
        "notes-core/tools/apply-seealso.py /tmp/seealso.json --apply    # 寫入各站 frontmatter\n"
        "```\n\n"
        "寫入後各站 `npm run format`，抽幾站 build（strict 站的 `seeAlso.site` 走 siteKeys enum，拼錯 build 會紅），\n"
        "`galaxy-checkup.py` 的 dead-seealso 必須維持 0。補完重跑本工具，該站就會從這裡消失。\n"
    )

    text = stamp(
        o.getvalue(),
        "tools/export-seealso-gaps.py",
        _dt.datetime.now().astimezone().isoformat(timespec="seconds"),
    )
    if "-" in args:
        sys.stdout.write(text)
    else:
        OUT.write_text(text, encoding="utf-8")
        print(
            f"{OUT}: strong 缺口 {len(rows)} 筆（來源頁 {len(src_pages)}，{len(per_src)} 站）；"
            f"有 seeAlso 的頁 {linked_now} → {linked_after} / {total_pages}；weak {weak_pairs}；被 schema 擋住 {len(blocked)}"
        )


if __name__ == "__main__":
    main()
