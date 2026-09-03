#!/usr/bin/env python3
"""全星系體檢：把 /note-check §1 指標與 §2 可機檢的項目一次跑完全部 75 站。

    notes-core/tools/galaxy-checkup.py                 # 全星系，逐站列 findings
    notes-core/tools/galaxy-checkup.py --station <name>
    notes-core/tools/galaxy-checkup.py --json          # 給後續腳本吃

**它不取代 `/note-check`**：這支只做機器判得準的那半（下方清單），
`/note-check` §2.5 的「抽驗防杜撰」（具名事實回源 grep）與 §3 的落差 backlog
仍要進站做——那是判斷，不是掃描。首跑 2026-08-26：75 站 blocker 0、
warn 61（全數當場修掉）、nit 332。

用法：galaxy-checkup.py [--station <name>] [--json] [--only <check>]

檢查項（對應 note-check.md 的節次）：
  2.1 core 版本落後、site.config 良構、首頁契約、content.config factory、
      divergence（站上自建 layouts/components/styles/pages/lib）、分類三者一致、導覽時效
  2.2 roadmap/mastery 覆蓋、roadmap 死指、孤兒頁、mastery slug 死指
  2.4 schema（importance 1-5、status enum、lastReviewed 格式、category 存在）
  2.5 書本位（每頁 ≥1 book、slug 對得到書庫、anchor 實存、label 分隔號）
  2.6 :::response 存在（只適用 concepts／problems，guide 不需要）、跳脫實體殘留
  2.7 related 雙向與死指、seeAlso 合法、**內文相對連結指得到頁**（見下）
  2.8 深度與連結度的地板（2026-09-03 加，三條都是 nit）：
      guide-unlinked  頁沒被任何導覽章連到——導覽是讀者入口，走不到的頁等於不存在
      related-thin    related 少於 2 條——checkup 原本只查死指與單向，`related: []` 一路綠燈
      body-thin       正文（去空白）不到 1000 字——技術站體裁短，但 1000 以下連 intuition 都撐不起
      這三條是「夠不夠」的定義，契約層（2.1–2.7）全綠時它們才有意義；門檻寫死在 THIN_* 常數
"""
import json
import re
import subprocess
import sys
from pathlib import Path

NOTES = Path("/home/andrew/workspace/andrew/notes")
BOOKS = Path("/home/andrew/workspace/andrew/books-management/books-done")
CORE = NOTES / "notes-core"

STATUS_OK = {"draft", "studied", "reviewed"}
THIN_RELATED = 2      # related 少於這個數就報
THIN_BODY = 1000      # 正文去空白字元數少於這個數就報


def guide_linked_pages(st):
    """導覽五章連到的 cat/slug 集合。兩種寫法都認：../concepts/… 與 /<站>/concepts/…。"""
    out = set()
    guide = st / "src" / "content" / "guide"
    if not guide.exists():
        return out
    pat = re.compile(rf"\]\((?:\.\./|/{re.escape(st.name)}/)concepts/([a-z0-9-]+)/([a-z0-9-]+)/?[#)]")
    for g in guide.glob("*.md"):
        out |= {f"{c}/{sl}" for c, sl in pat.findall(g.read_text(encoding="utf8"))}
    return out


def body_len(raw):
    """去掉 frontmatter 與所有空白後的字元數。"""
    body = raw.split("---", 2)[2] if raw.startswith("---") else raw
    return len(re.sub(r"\s", "", body))
SEP = re.compile(r"[—–]|\s-\s")


def book_index():
    idx = {}
    for p in BOOKS.rglob("site/content"):
        idx.setdefault(p.parent.parent.name, p.parent.parent)
    return idx


BOOKS_IDX = book_index()


def latest_core_tag():
    try:
        out = subprocess.run(
            ["gh", "api", "repos/nplus-father/notes-core/tags", "--jq", ".[0].name"],
            capture_output=True, text=True, timeout=25)
        tag = out.stdout.strip()
        return tag.lstrip("v") if tag else None
    except Exception:
        return None


CORE_TAG = latest_core_tag()


def fm_of(raw):
    if not raw.startswith("---"):
        return ""
    return raw.split("---", 2)[1]


def related_of(text):
    m = re.search(r"^related:\s*\[([^\]]*)\]", text, re.M | re.S)
    if m:
        return [s.strip().strip('"\'') for s in m.group(1).split(",") if s.strip()]
    m = re.search(r"^related:\s*\n((?:\s+-\s+\S+\n)+)", text, re.M)
    if m:
        return [s.strip('"\'') for s in re.findall(r"-\s+(\S+)", m.group(1))]
    return []


# seeAlso.site 有 sites.ts 的 enum 擋拼字（strict 站群），但 **path 從來沒有人驗**——
# 它是一個自由字串，指到別站的 URL 路徑，寫錯就是靜默 404。2026-08-26 首次驗證 239 條
# 全部有效，但那是運氣不是保證：這份 docstring 早就宣稱檢查「seeAlso 合法」，實作卻不存在。
SITE_DIRS = {d.name[:-5]: d for d in NOTES.glob("*-note")}

# 這些 path 不對應內容檔，而是 notes-core 產生的站級路由（見 core src/routes/）。
INDEX_ROUTES = {"", "concepts", "guide", "library", "search", "problems"}


def see_also_of(fm):
    """[(site, path)]；四種寫法只出現過 `- site:` / `path:` 這一種，故只解這種。"""
    m = re.search(r"^seeAlso:\s*\n((?:\s+-.*\n|\s{4,}.*\n)+)", fm, re.M)
    if not m:
        return []
    return [
        (s.strip().strip("\"'"), p.strip())
        for s, p in re.findall(r'-\s+site:\s*(\S+)\s*\n\s+path:\s*"?([^"\n]*)"?', m.group(1))
    ]


# 內文相對連結（`](../x/y/)`）從來沒有人驗過，而它是 seeAlso 之外的第二種靜默 404。
# 2026-08-28 首掃：112 條死鏈散在 26 站，全部躲過既有檢查——checkup 只驗 seeAlso 與
# related 這兩個 **frontmatter 欄位**，內文連結不在任何一份盤點裡。
#
# 解析規則（踩過兩次 off-by-one，寫在這裡免得下次再踩）：
#   * 概念頁 `concepts/<cat>/<slug>.md` 的 URL 是 `/concepts/<cat>/<slug>/`——
#     **頁面自己就是一層目錄**，所以相對連結要從「頁面 URL 之下」起算，
#     同站跨分類的正確寫法是 `../../<cat>/<slug>/`（不是 `../<cat>/<slug>/`）。
#   * `guide/NN-*.md` 全部渲染進**單頁** `/guide/`（notes-core ≥ v0.30.0），
#     所以各章的 URL 一律是 `/guide`，連概念頁要寫 `../concepts/<cat>/<slug>/`。
#   * 分類 `_index.md` 的 URL 是 `/concepts/<cat>/`。
#   * `/concepts/`、`/problems/`、`/guide/`、`/check/`、`/library/`、`/books/` 這些
#     **區段路由由 core 產生**，不對應任何 content 檔，要當成合法目標白名單。
# 校準方式（改這段前務必重跑）：拿剛 build 過、`dist` 逐條驗過的站當對照組，
# 掃描結果必須是 0；2026-08-28 用 cloud／gardner／fengtang／pastoral 四站校準過。
SECTION_ROUTES = {"/concepts", "/problems", "/guide", "/check", "/library", "/books", "/"}


def page_url(rel_no_ext):
    """content 相對路徑（去副檔名）→ 站上的 URL 路徑。"""
    parts = rel_no_ext.split("/")
    if parts[0] == "guide":
        return "/guide"
    if parts[-1] == "_index":
        return "/" + "/".join(parts[:-1])
    return "/" + rel_no_ext


def dead_inline_links(content_dir):
    """回傳 [(檔案相對路徑, 連結原文, 解析後路徑)]——指不到任何頁的內文相對連結。"""
    import posixpath

    files = [p for p in content_dir.rglob("*.md")]
    urls = {page_url(str(p.relative_to(content_dir))[:-3]) for p in files}
    urls |= SECTION_ROUTES
    out = []
    for p in files:
        rel = str(p.relative_to(content_dir))
        u = page_url(rel[:-3])
        for href in re.findall(r"\]\((\.\.?/[^)#]*)\)", p.read_text(encoding="utf8")):
            target = posixpath.normpath(posixpath.join(u + "/", href.rstrip("/")))
            if target not in urls:
                out.append((rel, href, target))
    return out


def see_also_bad(site, path):
    """回傳壞掉的原因；合法回 None。"""
    d = SITE_DIRS.get(site)
    if d is None:
        return f"site「{site}」不是星系裡的站"
    seg = path.strip("/").split("/") if path.strip("/") else []
    if not seg or seg[0] in INDEX_ROUTES and len(seg) == 1:
        return None                                   # 站首頁／總覽路由
    if seg[0] not in ("concepts", "problems"):
        return f"路徑前綴不認得（{seg[0]}）"
    rest = seg[1:]
    if not rest:
        return None
    c = d / "src" / "content" / seg[0]
    c = c.joinpath(*rest)
    if c.with_suffix(".md").exists() or (c / "_index.md").exists():
        return None
    return "目標頁不存在"


def check(st):
    f = []          # findings: (level, code, msg)
    add = lambda lv, code, msg: f.append((lv, code, msg))
    src = st / "src"

    # ---- 2.1 版本 currency ----
    pkg = st / "package.json"
    pinned = None
    if pkg.exists():
        m = re.search(r'"@nplus-father/notes-core":\s*"([^"]+)"', pkg.read_text(encoding="utf8"))
        if m:
            pinned = m.group(1)
            if CORE_TAG and CORE_TAG not in pinned:
                add("warn", "core-version", f"釘 {pinned}，最新 v{CORE_TAG}")

    # ---- 2.1 site.config ----
    cfg_p = src / "site.config.ts"
    cfg = cfg_p.read_text(encoding="utf8") if cfg_p.exists() else ""
    if not cfg:
        add("blocker", "no-site-config", "缺 src/site.config.ts")
    else:
        for key in ("brand", "titleBase"):
            if f"{key}:" not in cfg:
                add("warn", "site-config", f"缺 {key}")
        bm = re.search(r'brand:\s*"([^"]*)"', cfg)
        if bm and re.search(r"[一-鿿]", bm.group(1)):
            add("warn", "brand-cjk", f'brand 含中文："{bm.group(1)}"（中文短名歸 sites.ts）')
        if re.search(r"^\s*ns:", cfg, re.M):
            add("nit", "ns-residue", "site.config 殘留已廢除的 ns")

    # ---- 2.1 首頁契約 ----
    has_schools = (src / "data" / "schools.ts").exists()
    has_profile = (src / "data" / "profile.ts").exists()
    if not (has_schools or has_profile):
        add("blocker", "home-contract", "既無 schools.ts 也無 profile.ts")
    if not (src / "data" / "bibliography.ts").exists():
        add("blocker", "no-bibliography", "缺 bibliography.ts")

    # ---- 2.1 content.config 是 factory ----
    cc = src / "content.config.ts"
    if cc.exists():
        body = cc.read_text(encoding="utf8")
        if "defineNoteCollections" not in body:
            add("warn", "content-config", "沒有用 notes-core 的 defineNoteCollections factory")
        if re.search(r"\bz\.object\(|defineCollection\(", body):
            add("warn", "content-config", "站上自寫 schema（z.object / defineCollection）")

    # ---- 2.1 divergence ----
    for d in ("layouts", "components", "styles", "pages", "lib"):
        p = src / d
        if p.exists() and any(p.rglob("*")):
            n = sum(1 for _ in p.rglob("*") if _.is_file())
            add("blocker", "divergence", f"站上自建 src/{d}/（{n} 檔）——設計系統分岔")

    # ---- 掃內容 ----
    concepts = src / "content" / "concepts"
    if not concepts.exists():
        add("blocker", "no-concepts", "缺 src/content/concepts")
        return f, {}

    cats = {}
    for idx in concepts.glob("*/_index.md"):
        raw = idx.read_text(encoding="utf8")
        fm = fm_of(raw)
        cat = idx.parent.name
        cats[cat] = {
            "roadmap": re.findall(r"slug:\s*([a-z0-9-]+)", fm.split("mastery:")[0] if "mastery:" in fm else fm),
            "mastery_slugs": re.findall(r"slug:\s*([a-z0-9-]+)", fm.split("mastery:")[1]) if "mastery:" in fm else [],
            "has_roadmap": "roadmap:" in fm,
            "has_mastery": "mastery:" in fm,
        }
        for key in ("name", "icon", "order"):
            if not re.search(rf"^{key}:", fm, re.M):
                add("warn", "cat-index", f"{cat}/_index.md 缺 {key}")

    pages = {}
    for p in concepts.rglob("*.md"):
        if p.name == "_index.md":
            continue
        pages[p.stem] = p

    all_slugs = set(pages)
    guide_linked = guide_linked_pages(st)
    sourced = 0
    for slug, p in sorted(pages.items()):
        raw = p.read_text(encoding="utf8")
        fm = fm_of(raw)
        rel = f"{p.parent.name}/{p.name}"

        # 2.6 entity + response
        for ent in ("&gt;", "&lt;", "&amp;"):
            if ent in raw:
                add("warn", "entity", f"{rel}: 殘留 {ent}")
        if ":::response" not in raw:
            add("warn", "no-response", f"{rel}: 缺 :::response 區塊")

        # 2.4 schema
        m = re.search(r"^importance:\s*(\d+)", fm, re.M)
        if m and not (1 <= int(m.group(1)) <= 5):
            add("warn", "schema", f"{rel}: importance={m.group(1)} 超出 1–5")
        m = re.search(r"^status:\s*(\S+)", fm, re.M)
        if m and m.group(1).strip('"') not in STATUS_OK:
            add("warn", "schema", f"{rel}: status={m.group(1)}")
        m = re.search(r"^lastReviewed:\s*(\S+)", fm, re.M)
        if m and not re.fullmatch(r'"?\d{4}-\d{2}-\d{2}"?', m.group(1)):
            add("warn", "schema", f"{rel}: lastReviewed={m.group(1)} 格式不合")
        m = re.search(r"^category:\s*(\S+)", fm, re.M)
        if m and m.group(1).strip('"') != p.parent.name:
            add("warn", "cat-mismatch", f"{rel}: category={m.group(1)} 與目錄不符")

        # 2.5 書本位
        fr = re.findall(r"- book:\s*(\S+)\s*\n\s*label:\s*\"([^\"]*)\"\s*\n\s*anchor:\s*\"?([^\"\n]+)\"?", fm)
        if not fr:
            add("warn", "unsourced", f"{rel}: furtherReading 沒有任何 anchor")
        else:
            sourced += 1
        for bslug, label, anchor in fr:
            repo = BOOKS_IDX.get(bslug)
            if repo is None:
                add("warn", "dead-book", f"{rel}: 書庫查無 {bslug}")
            elif not (repo / "site" / "content" / anchor.strip().strip('"').rstrip("/")).is_dir():
                add("warn", "dead-anchor", f"{rel}: {bslug} → {anchor}")
            if not SEP.search(label):
                add("nit", "label-sep", f"{rel}: label 缺分隔號 → {label[:40]}")

        # 2.7 related
        for t in related_of(fm):
            if t not in all_slugs:
                add("warn", "dead-related", f"{rel}: related → {t} 不存在")
            elif slug not in related_of(fm_of(pages[t].read_text(encoding="utf8"))):
                add("nit", "oneway-related", f"{rel} → {t}（未指回）")

        # 2.8 地板：related 條數、正文長度、導覽有沒有連到
        n_rel = len(related_of(fm))
        if n_rel < THIN_RELATED:
            add("nit", "related-thin", f"{rel}: related 只有 {n_rel} 條")
        bl = body_len(raw)
        if bl < THIN_BODY:
            add("nit", "body-thin", f"{rel}: 正文 {bl} 字")
        if guide_linked and f"{p.parent.name}/{slug}" not in guide_linked:
            add("nit", "guide-unlinked", f"{rel}: 沒被任何導覽章連到")

        # 2.7 seeAlso：site 走 registry、path 要指得到真的頁（寫錯是靜默 404）
        for site, path in see_also_of(fm):
            why = see_also_bad(site, path)
            if why:
                add("warn", "dead-seealso", f"{rel}: seeAlso → {site}/{path}（{why}）")

    # ---- 2.7 內文相對連結（seeAlso 之外的第二種靜默 404）----
    content_dir = src / "content"
    if content_dir.is_dir():
        for rel, href, target in dead_inline_links(content_dir):
            add("warn", "dead-inline-link", f"{rel}: {href} → {target}（指不到頁）")

    # ---- 2.2 roadmap / mastery ----
    in_roadmap = {s for c in cats.values() for s in c["roadmap"]}
    for slug in sorted(all_slugs - in_roadmap):
        add("warn", "orphan-page", f"{pages[slug].parent.name}/{slug}: 不在任何 roadmap")
    for cat, c in sorted(cats.items()):
        if not c["has_roadmap"]:
            add("warn", "no-roadmap", f"{cat}/_index.md 沒有 roadmap")
        if not c["has_mastery"]:
            add("warn", "no-mastery", f"{cat}/_index.md 沒有 mastery")
        for s in c["roadmap"]:
            if s not in all_slugs:
                add("nit", "roadmap-planned", f"{cat}: roadmap → {s}（未寫，若非 planned 意圖要報）")
        for s in c["mastery_slugs"]:
            if s not in all_slugs:
                add("warn", "mastery-slug", f"{cat}: mastery slug → {s} 不存在")

    # ---- 2.1 導覽時效 ----
    guide = src / "content" / "guide"
    if guide.exists():
        wr = sorted(re.search(r"writtenAt:\s*(\S+)", g.read_text(encoding="utf8")).group(1)
                    for g in guide.glob("*.md")
                    if re.search(r"writtenAt:\s*(\S+)", g.read_text(encoding="utf8")))
        en = re.search(r'enrichedAt:\s*"([^"]+)"', cfg)
        if wr and en and wr[-1] < en.group(1):
            add("warn", "guide-stale", f"導覽最新 {wr[-1]} < enrichedAt {en.group(1)}")

    # ---- 2.1 首頁總覽（DESIGN §4.2：每一站都要有，主題站與人物站共同的第一區）----
    # 2026-09-03 加：theology／biblical-studies／startup 三站是 08-27 導覽輪的前三站，
    # 總覽那一步輪到第四站才接上，之後沒人發現——因為這裡從來沒查過 overview 存不存在。
    ov_p = src / "data" / "overview.ts"
    astro_p = st / "astro.config.mjs"
    astro = astro_p.read_text(encoding="utf8") if astro_p.exists() else ""
    if not ov_p.exists():
        add("warn", "no-overview", "缺 src/data/overview.ts（首頁 Overview 區）")
    else:
        if "overview" not in astro:
            add("warn", "overview-unwired", "overview.ts 在，但 astro.config.mjs 沒 import／傳入 overview")
        ov = ov_p.read_text(encoding="utf8")
        allowed = {"Landscape", "Threads", "Verdict", "Background", "Contributions", "Claims"}
        for h in re.findall(r'heading:\s*"([^"]+)"', ov):
            if h not in allowed:
                add("nit", "overview-heading", f'overview heading "{h}" 不在標準英文詞彙裡（chrome 一律簡短英文，v0.34.0）')
        if "（待寫）" in ov:
            add("nit", "overview-placeholder", "overview.ts 還是 template 的佔位稿（含「（待寫）」）")
        wm = re.search(r'writtenAt:\s*"([^"]+)"', ov)
        en2 = re.search(r'enrichedAt:\s*"([^"]+)"', cfg)
        if wm and en2 and wm.group(1) < en2.group(1):
            add("warn", "overview-stale", f"overview writtenAt {wm.group(1)} < enrichedAt {en2.group(1)}")

    # ---- §1 指標 ----
    bib = (src / "data" / "bibliography.ts").read_text(encoding="utf8")
    spine = len(re.findall(r'tier:\s*"spine"', bib))
    owned = len(re.findall(r'status:\s*"owned"', bib))
    wanted = len(re.findall(r'status:\s*"wanted"', bib))
    metrics = {
        "pages": len(pages),
        "spine": spine,
        "pages_per_spine": round(len(pages) / spine, 2) if spine else None,
        "sourced_pct": round(100 * sourced / len(pages)) if pages else 0,
        "mastery_pct": round(100 * sum(1 for c in cats.values() if c["has_mastery"]) / len(cats)) if cats else 0,
        "roadmap_pct": round(100 * len(all_slugs & in_roadmap) / len(pages)) if pages else 0,
        "booklist_pct": round(100 * owned / (owned + wanted)) if (owned + wanted) else 100,
    }
    return f, metrics


def main():
    args = sys.argv[1:]
    only = args[args.index("--station") + 1] if "--station" in args else None
    stations = [NOTES / only] if only else sorted(
        p.parent.parent for p in NOTES.glob("*-note/src/site.config.ts"))

    report = {}
    for st in stations:
        fs, mx = check(st)
        report[st.name] = {"findings": fs, "metrics": mx}

    if "--json" in args:
        print(json.dumps(report, ensure_ascii=False, indent=1))
        return

    tot = {"blocker": 0, "warn": 0, "nit": 0}
    for name, r in report.items():
        lv = {"blocker": 0, "warn": 0, "nit": 0}
        for level, _, _ in r["findings"]:
            lv[level] += 1
            tot[level] += 1
        m = r["metrics"]
        if sum(lv.values()) == 0:
            print(f"✅ {name:28s} 乾淨   頁/spine={m.get('pages_per_spine')} 溯源={m.get('sourced_pct')}%")
            continue
        print(f"\n=== {name}  blocker={lv['blocker']} warn={lv['warn']} nit={lv['nit']}"
              f"  頁/spine={m.get('pages_per_spine')} 溯源={m.get('sourced_pct')}%"
              f" mastery={m.get('mastery_pct')}% roadmap={m.get('roadmap_pct')}%")
        codes = {}
        for level, code, msg in r["findings"]:
            codes.setdefault((level, code), []).append(msg)
        for (level, code), msgs in sorted(codes.items()):
            tag = {"blocker": "🛑", "warn": "⚠️ ", "nit": "·"}[level]
            print(f"  {tag} [{code}] {len(msgs)}")
            for msg in msgs[:4]:
                print(f"       {msg}")
            if len(msgs) > 4:
                print(f"       …另外 {len(msgs)-4} 筆")
    print(f"\n=== 全星系 {len(report)} 站：blocker {tot['blocker']}／warn {tot['warn']}／nit {tot['nit']}")


main()
