#!/usr/bin/env python3
"""把「孤兒書認領」的決策 JSON 套進各站的 bibliography.ts。

存在的理由：2026-08-28 一次認領 328 本孤兒書，橫跨三十幾個站。讓模型逐筆去改
TS entry 必壞語法（2026-08-24 判層輪實測，90 筆就壞），所以沿用 `apply-tiers.py`
的分工：**模型只交 JSON 決策，TS 由這支腳本產生**。

安全的插入點：`Bibliography.astro` 是**依 `group` 欄位的值**分組（首次出現決定組序），
組內再依 `year` 由早到晚排序——**實體順序不影響呈現**。所以新條目一律附加在陣列
末尾（`]);` 之前），不必在檔案中間動刀，也就沒有插錯位置的風險。

決策 JSON 的每一筆：

    {"slug": "...", "station": "investing-note", "group": "（該站已存在的組名）",
     "title": "...", "original": "（選填）", "author": "...", "year": 2017,
     "status": "owned", "tier": "tool", "note": "..."}

用法:
    apply-claims.py <決策.json> [<決策.json> ...]            乾跑，只驗證與統計
    apply-claims.py <決策.json> ... --apply                  寫入
    apply-claims.py <決策.json> ... --notes-root <path>      指定 notes 星系根目錄

寫入後**必跑**：各站 `npm run format`（prettier 解析失敗＝語法壞了，是最便宜的
語法閘）、`notes-core/tools/tier-audit.py --all`、`export-orphan-books.py`。
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

FIELD_ORDER = ["group", "title", "original", "author", "year", "slug", "status", "tier", "note"]
REQUIRED = ["slug", "station", "group", "title", "author", "status", "tier"]


def ts_string(value: str) -> str:
    """挑不需要跳脫的引號；兩種都出現才跳脫。書名裡有 " 的不少（12 "Christian" Beliefs）。"""
    if '"' not in value:
        return '"' + value.replace("\\", "\\\\") + '"'
    if "'" not in value:
        return "'" + value.replace("\\", "\\\\") + "'"
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def render(entry: dict) -> str:
    lines = ["  {"]
    for key in FIELD_ORDER:
        if key not in entry or entry[key] in (None, ""):
            continue
        value = entry[key]
        rendered = str(value) if isinstance(value, (int, float)) else ts_string(str(value))
        lines.append(f"    {key}: {rendered},")
    lines.append("  },")
    return "\n".join(lines)


def existing_slugs(source: str) -> set:
    return set(re.findall(r'slug:\s*"([^"]+)"', source))


def existing_groups(source: str) -> set:
    return set(re.findall(r'group:\s*"([^"]+)"', source))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("decisions", nargs="+", help="決策 JSON 檔（可多個）")
    ap.add_argument("--apply", action="store_true", help="真的寫入；預設只乾跑")
    ap.add_argument(
        "--notes-root",
        default="/home/andrew/workspace/andrew/notes",
        help="notes 星系根目錄",
    )
    args = ap.parse_args()
    root = Path(args.notes_root)

    entries = []
    for path in args.decisions:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        if not isinstance(data, list):
            print(f"✗ {path} 不是 JSON 陣列", file=sys.stderr)
            return 2
        entries.extend(data)

    problems = []
    seen = {}
    for entry in entries:
        slug = entry.get("slug", "（無 slug）")
        for key in REQUIRED:
            if not entry.get(key):
                problems.append(f"{slug}: 缺 {key}")
        if entry.get("tier") != "tool":
            problems.append(f"{slug}: tier 是 {entry.get('tier')}，這一輪只准 tool")
        if slug in seen:
            problems.append(f"{slug}: 重複出現（{seen[slug]} 與 {entry.get('station')}）")
        seen[slug] = entry.get("station")

    by_station = defaultdict(list)
    for entry in entries:
        by_station[entry.get("station", "")].append(entry)

    plans = []
    for station, items in sorted(by_station.items()):
        path = root / station / "src" / "data" / "bibliography.ts"
        if not path.is_file():
            problems.append(f"{station}: 找不到 {path}")
            continue
        source = path.read_text(encoding="utf-8")
        have_slugs, have_groups = existing_slugs(source), existing_groups(source)
        new_groups = set()
        for entry in items:
            if entry["slug"] in have_slugs:
                problems.append(f"{entry['slug']}: {station} 已經有這個 slug")
            if entry["group"] not in have_groups:
                new_groups.add(entry["group"])
        marker = source.rfind("]);")
        if marker == -1:
            problems.append(f"{station}: 找不到陣列結尾 `]);`")
            continue
        plans.append((station, path, source, marker, items, sorted(new_groups)))

    for station, _, _, _, items, new_groups in plans:
        note = f"  ⚠ 新增組別：{'、'.join(new_groups)}" if new_groups else ""
        print(f"{station:30s} +{len(items):3d} 本{note}")
    print(f"\n合計 {len(entries)} 本，{len(plans)} 個站")

    if problems:
        print(f"\n✗ {len(problems)} 個問題，未寫入：", file=sys.stderr)
        for problem in problems[:40]:
            print("   " + problem, file=sys.stderr)
        if len(problems) > 40:
            print(f"   …另有 {len(problems) - 40} 筆", file=sys.stderr)
        return 1

    if not args.apply:
        print("\n（乾跑；加 --apply 才寫入）")
        return 0

    for station, path, source, marker, items, _ in plans:
        block = "\n".join(render(entry) for entry in items)
        path.write_text(source[:marker] + block + "\n" + source[marker:], encoding="utf-8")
        print(f"✓ {station} 寫入 {len(items)} 本")
    print("\n收尾必跑：各站 npm run format、tier-audit.py --all、export-orphan-books.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
