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
  2.7 related 雙向與死指、seeAlso 合法
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
