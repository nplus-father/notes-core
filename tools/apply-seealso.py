#!/usr/bin/env python3
"""把 export-seealso-gaps.py --json 的決策寫進各站概念頁的 frontmatter `seeAlso`。

用法：
    tools/apply-seealso.py <decisions.json>            # 乾跑，印每站筆數
    tools/apply-seealso.py <decisions.json> --apply    # 實際寫入

決策 JSON 格式（與 export-seealso-gaps.py --json 同形）：
    {"<station>-note": [{"page": "<cat>/<slug>", "add": [{"site": "collins", "path": "concepts/greatness/flywheel/", "label": "…"}]}]}

**用腳本改而不是讓模型手改**：同 apply-tiers.py 的教訓——幾百筆 frontmatter 讓模型逐頁改必出錯。
這裡只做三件純文字操作：`seeAlso: []` 換成區塊；既有區塊尾端追加；frontmatter 沒有 seeAlso 就在
結尾 `---` 前補一個區塊。同 (site, path) 已存在就跳過。寫完各站要 `npm run format`，
prettier 會把引號與縮排整齊化。
"""
import json
import os
import re
import sys

NOTES = os.environ.get("NOTES_ROOT") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
args = [a for a in sys.argv[1:] if not a.startswith("--")]
if not args:
    sys.exit("用法: tools/apply-seealso.py <decisions.json> [--apply]")
decisions = json.load(open(args[0], encoding="utf-8"))
apply = "--apply" in sys.argv

FM_RE = re.compile(r"^(---\n)(.*?)(\n---\n)", re.S)


def q(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def entry(site: str, path: str, label: str) -> str:
    return f"  - site: {site}\n    path: {q(path)}\n    label: {q(label)}"


total = 0
touched_files = 0
for station, items in sorted(decisions.items()):
    n = 0
    for it in items:
        p = os.path.join(NOTES, station, "src", "content", "concepts", it["page"] + ".md")
        if not os.path.exists(p):
            print(f"  ✘ {station}: 找不到 {it['page']}")
            continue
        src = open(p, encoding="utf-8").read()
        m = FM_RE.match(src)
        if not m:
            print(f"  ✘ {station}: {it['page']} 沒有 frontmatter")
            continue
        head, fm, tail = m.groups()
        existing = set(re.findall(r"-\s*site:\s*\"?([\w-]+)\"?\s*\n\s+path:\s*\"?([^\"\n]+)\"?", fm))
        new = [a for a in it["add"] if (a["site"], a["path"]) not in existing]
        if not new:
            continue
        block = "\n".join(entry(a["site"], a["path"], a["label"]) for a in new)
        if re.search(r"^seeAlso:\s*\[\s*\]\s*$", fm, re.M):
            fm2 = re.sub(r"^seeAlso:\s*\[\s*\]\s*$", "seeAlso:\n" + block, fm, count=1, flags=re.M)
        elif re.search(r"^seeAlso:\s*$", fm, re.M):
            # 既有區塊：找到 seeAlso: 之後、下一個頂層 key 之前，追加在區塊尾
            bm = re.search(r"^seeAlso:\s*\n((?:[ \t]+[^\n]*\n?)+)", fm, re.M)
            if not bm:
                print(f"  ✘ {station}: {it['page']} 的 seeAlso 區塊形狀看不懂，跳過")
                continue
            blk = bm.group(0).rstrip("\n")
            fm2 = fm[: bm.start()] + blk + "\n" + block + fm[bm.start() + len(bm.group(0).rstrip("\n")):]
        elif re.search(r"^seeAlso:", fm, re.M):
            print(f"  ✘ {station}: {it['page']} 的 seeAlso 不是 [] 也不是區塊，跳過")
            continue
        else:
            fm2 = fm.rstrip("\n") + "\nseeAlso:\n" + block
        out = head + fm2 + tail + src[m.end():]
        if apply:
            open(p, "w", encoding="utf-8").write(out)
        n += len(new)
        touched_files += 1
    if n:
        print("%-28s %3d 筆%s" % (station, n, "（已寫入）" if apply else ""))
    total += n
print("\n合計 %d 筆、%d 個檔%s" % (total, touched_files, "" if apply else "（乾跑；加 --apply 才寫入）"))
