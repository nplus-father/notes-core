#!/usr/bin/env python3
"""把判層決策套進各站 bibliography.ts（純文字插入，不動其他欄位）。

兩種輸入都吃：
  - `tier-evidence.py --json` 的自動判定（`auto` 那半）
  - 高階模型交回的裁決 JSON——同樣的形狀即可，見下方「決策 JSON 格式」

用法：
    tools/apply-tiers.py <decisions.json>            # 乾跑，印每站筆數
    tools/apply-tiers.py <decisions.json> --apply    # 實際寫入
套用後**必跑** `tools/tier-audit.py`，再逐站 `npm run build:nosearch` 驗語法。

決策 JSON 格式（`auto` 陣列裡每筆只有 slug 與 tier 是必要的）：
    {"<station>": {"auto": [{"slug": "book-slug", "tier": "spine"},
                            {"slug": "other", "tier": "delegated:drucker"}]}}
`delegated` 用 `delegated:<sites.ts 的 key>`，腳本會拆成 tier ＋ delegatedTo 兩欄。


**用腳本改而不是讓 AI 手改**：2026-08-24 首輪的教訓——讓模型逐筆改 90 個 TS entry 必壞語法。
這裡走「找到那一筆的 slug 行 → 在同一個物件裡插入 tier」，純文字操作、可驗證。

規則：
  - 只碰 status: "owned" 且**還沒有 tier** 的 entry
  - tier 插在 status 那一行之後（跟既有慣例一致）
  - delegated 同時插 delegatedTo
不改任何其他東西；改完印每站筆數，另外跑 build 驗語法。
"""
import json
import os
import re
import sys

NOTES = os.environ.get("NOTES_ROOT") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
args = [a for a in sys.argv[1:] if not a.startswith("--")]
if not args:
    sys.exit("用法: tools/apply-tiers.py <decisions.json> [--apply]")
ev = json.load(open(args[0], encoding="utf-8"))
apply = "--apply" in sys.argv

total = 0
for st, v in sorted(ev.items()):
    if not v["auto"]:
        continue
    p = os.path.join(NOTES, st, "src", "data", "bibliography.ts")
    src = open(p, encoding="utf-8").read()
    n = 0
    for r in v["auto"]:
        slug, tier = r["slug"], r["tier"]
        # 找出含這個 slug 的物件區塊
        m = re.search(r"\{[^{}]*?\bslug:\s*\"%s\"[^{}]*?\}" % re.escape(slug), src, re.S)
        if not m:
            print("  ✘ %s: 找不到 %s" % (st, slug))
            continue
        blk = m.group(0)
        if re.search(r"\btier:\s*\"", blk):
            continue  # 已判過，跳過
        sm = re.search(r"^(\s*)status:\s*\"owned\",\s*$", blk, re.M)
        if not sm:
            print("  ✘ %s: %s 沒有標準的 status 行" % (st, slug))
            continue
        indent = sm.group(1)
        if tier.startswith("delegated:"):
            key = tier.split(":", 1)[1]
            ins = '%stier: "delegated",\n%sdelegatedTo: "%s",' % (indent, indent, key)
        else:
            ins = '%stier: "%s",' % (indent, tier)
        new_blk = blk[: sm.end()] + "\n" + ins + blk[sm.end():]
        src = src[: m.start()] + new_blk + src[m.end():]
        n += 1
    if apply and n:
        open(p, "w", encoding="utf-8").write(src)
    print("%-28s %3d 筆%s" % (st, n, "（已寫入）" if apply and n else ""))
    total += n
print("\n合計 %d 筆%s" % (total, "" if apply else "（乾跑；加 --apply 才寫入）"))
