#!/usr/bin/env python3
"""一次性遷移：把作者寫進各站 bibliography 的 `author` 欄（notes-core v0.27.0 起）。

用法：
    notes-core/tools/migrate-authors.py --dry-run   # 只報告，不改檔
    notes-core/tools/migrate-authors.py             # 實際寫入

**這支是一次性的，跑完就可以刪。** 留著是為了記錄兩個資料來源怎麼分工——
之後新書進 bibliography 時直接手填 `author`，不會再需要它。

作者從哪裡來（兩個來源，都不是憑空生成）：
  1. **`owned` 條目 → 書 repo 的 description 作者欄**（權威）。那些 description 是
     `書名 | 作者 | 簡介`，建 repo 時查過版權頁、三方核對過（見 book-import-to-queue
     skill 的 A2）。所以 owned 這批等於把已經驗證過的事實搬進盤點，不是重新輸入。
  2. **其餘（wanted／unavailable／skipped）→ `export-wanted.py` 的 `AUTHORS` 側表**。
     那張表本來就是為了採購清單防買錯而養的，只是住錯地方——它服務的是「這本書是誰
     寫的」，那屬於資料，不屬於產生器。

搬完之後 `AUTHORS` 就只剩「還沒進資料」的殘留，可以逐步清空。

**欄位位置**：插在 `original` 之後（沒有 original 就插在 `title` 之後），與
`BibliographyEntry` 的欄位宣告順序一致。
"""

import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTES_ROOT = Path(os.environ.get("NOTES_ROOT") or HERE.parent.parent)
DRY = "--dry-run" in sys.argv

spec = importlib.util.spec_from_file_location("ew", HERE / "export-wanted.py")
ew = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ew)


def portal_authors():
    """repo name → description 的作者欄。權威來源是 GitHub 現況，不是站台快照。"""
    out = {}
    for owner in ew.PORTAL_OWNERS:
        raw = subprocess.run(
            ["gh", "repo", "list", owner, "--limit", "2000", "--json", "name,description"],
            capture_output=True, text=True, timeout=120, check=True,
        ).stdout
        for r in json.loads(raw):
            parts = [p.strip() for p in (r.get("description") or "").split("|")]
            if len(parts) >= 2 and parts[1]:
                out[r["name"]] = parts[1]
    return out


def main():
    authors_by_repo = portal_authors()
    print(f"portal 作者欄：{len(authors_by_repo)} 個 repo 有作者")

    total = filled_portal = filled_table = missing = already = 0
    per_station = {}

    for bib in sorted(NOTES_ROOT.glob("*-note/src/data/bibliography.ts")):
        station = bib.parts[len(NOTES_ROOT.parts)]
        src = bib.read_text(encoding="utf-8")
        out, n = [], 0

        # 逐 `status:` 行回推整個條目——不必真的解析 TS，欄位都在同一個物件字面值裡。
        for m in re.finditer(r'^( *)status: "([a-z]+)",$', src, re.M):
            total += 1
            indent, status = m.group(1), m.group(2)
            head = src.rfind("\n  {\n", 0, m.start())
            tail = src.index("\n  },", m.start())
            block = src[head:tail]
            if re.search(r"^\s*author:", block, re.M):
                already += 1
                continue

            slug = (re.search(r'slug: "([^"]+)"', block) or [None, None])[1]
            author = None
            if status == "owned" and slug:
                author = authors_by_repo.get(slug)
            if not author:
                title = (re.search(r'title: "((?:[^"\\]|\\.)*)"', block) or [None, None])[1]
                original = (re.search(r'original: "((?:[^"\\]|\\.)*)"', block) or [None, None])[1]
                if (original or "").strip() in ew.NON_ENGLISH_ORIGINALS:
                    en = ew.latin_of(title) or ew.latin_of(original)
                else:
                    en = ew.latin_of(original) or ew.latin_of(title)
                key = ew.slugify(en.split(":")[0]) if en else "cjk::" + (title or "")
                author = ew.AUTHORS.get(key)
                if author:
                    filled_table += 1
            elif author:
                filled_portal += 1

            if not author:
                missing += 1
                continue

            # 插在 original 之後；沒有 original 就插在 title 之後。
            anchor = re.search(r"^ *original: .*,$", block, re.M) or re.search(
                r"^ *title: .*,$", block, re.M
            )
            if not anchor:
                missing += 1
                continue
            pos = head + anchor.end()
            line = f'\n{indent}author: "{author}",'
            out.append((pos, line))
            n += 1

        if n:
            per_station[station] = n
        if out and not DRY:
            for pos, line in sorted(out, reverse=True):
                src = src[:pos] + line + src[pos:]
            bib.write_text(src, encoding="utf-8")

    print(f"條目總數 {total}｜已有 author {already}｜"
          f"這次填入 {filled_portal + filled_table}"
          f"（portal {filled_portal} ＋ AUTHORS 表 {filled_table}）｜仍缺 {missing}")
    print(f"涉及 {len(per_station)} 站：")
    for st, n in sorted(per_station.items(), key=lambda x: -x[1]):
        print(f"  {st:28} {n:4}")
    if DRY:
        print("\n（--dry-run，沒有寫入任何檔案）")


if __name__ == "__main__":
    main()
