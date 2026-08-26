#!/usr/bin/env python3
"""跨站比對同一本書的 `year`，把矛盾與可補的缺口匯出（docs/YEAR-CONFLICTS.md）。

用法：
    notes-core/tools/export-year-conflicts.py       # 寫進 notes-core/docs/YEAR-CONFLICTS.md
    notes-core/tools/export-year-conflicts.py -     # 印到 stdout

星系根目錄預設推導成 tools/../..，用 NOTES_ROOT= 覆寫（與其他 export-*.py 同慣例）。

**為什麼要有這支**：既有四份盤點都是「一站之內」的視角——MISSING-YEARS 只問「這一格
空不空」，答不出「這一格填的跟隔壁站不一樣」。而一本書被 N 個站收錄是常態（跨站分工
本來就允許），於是同一個 slug 在不同站有不同 `year` 完全不會被任何檢查攔下來：
tier-audit 看 tier、orphan-books 看 slug 存不存在、missing-years 看有沒有填。
**填錯不會被抓，只有沒填會。**

後果不是美觀問題：`year` 是首頁年代分佈圖的軸，兩個站畫同一本書會落在不同年代；而
讀者（跟 AI）沒有辦法從單一站看出哪一格才對。2026-08-26 首跑抓到 23 本矛盾。

這支同時回答第二個問題：**缺 year 的條目，別站有沒有現成答案**。有的話那是零判斷的
補漏——直接抄，不必查書。首跑 123 個缺口裡有 15 個可以這樣補掉。

**兩種矛盾要分開看，工具不替人判**：

1. **初版 vs 改版**（Refactoring 1999／2018、非暴力溝通 1999／2003）——schema 要的是
   初版年，所以較晚那個通常是後來的版次，但**不能無腦取小**：有些書的早期年份指的是
   同名的錄音課程或講座，書本身晚很多年才出（Tracy 的 Psychology of Selling 就是）。
2. **系列列 vs 單卷列**——一個 slug 被拿來當「一整套書」的代表列。biblical-studies-note
   的「聖經信息系列（全 52 冊）」就掛在 message-of-romans 這個 slug 上，year 填 1968
   （系列起始年），而 stott-note 的《羅馬書的信息》填 1994（該卷初版年）。**兩邊都對**，
   這不是債。工具會把 title 一起印出來，就是為了讓這種情況一眼看得出來。

所以輸出只做分類與陳列，**不自動改資料**。

**解析方式**：與 export-missing-years.py 相同——直接讀 `defineBibliography([...])` 的
原始碼抓 depth-1 物件字面值，不 import TS。
"""

import os
import re
import sys
import datetime as _dt

from _stamp import stamp
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("NOTES_ROOT", HERE.parent.parent))
OUT = HERE.parent / "docs" / "YEAR-CONFLICTS.md"


def entries_of(src: str) -> list[str]:
    """抓 defineBibliography([...]) 裡 depth-1 的物件字面值。

    與 export-missing-years.py 同一份實作。刻意不抽成共用模組：tools/ 底下的
    export-*.py 各自可獨立執行、互不 import，複製這 30 行比長出一個內部套件便宜。
    """
    start = src.find("defineBibliography(")
    if start < 0:
        return []
    out: list[str] = []
    depth, buf, quote, esc = 0, [], None, False
    for ch in src[src.index("[", start) + 1 :]:
        if quote:
            buf.append(ch)
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
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


def field(entry: str, name: str) -> str | None:
    m = re.search(rf'\b{name}\s*:\s*"([^"]*)"', entry)
    if m:
        return m.group(1)
    m = re.search(rf"\b{name}\s*:\s*(-?\d+)", entry)
    return m.group(1) if m else None


def collect() -> tuple[dict, list, int]:
    """slug → {year: [(station, title)]}、缺 year 的 (station, slug, title)、總條目數。"""
    have: dict[str, dict[int, list[tuple[str, str]]]] = {}
    missing: list[tuple[str, str, str]] = []
    total = 0
    for f in sorted(ROOT.glob("*/src/data/bibliography.ts")):
        station = f.parts[-4]
        for e in entries_of(f.read_text(encoding="utf-8")):
            slug = field(e, "slug")
            if not slug:
                continue
            total += 1
            title = field(e, "title") or "(無 title)"
            y = field(e, "year")
            if y is None:
                missing.append((station, slug, title))
            else:
                have.setdefault(slug, {}).setdefault(int(y), []).append((station, title))
    return have, missing, total


def main() -> None:
    have, missing, total = collect()
    conflicts = {s: d for s, d in have.items() if len(d) > 1}
    fillable = [(st, sl, ti, have[sl]) for st, sl, ti in missing if sl in have]

    buf: list[str] = []
    w = buf.append
    w("# 出版年跨站矛盾（同一本書、兩個年份）\n")
    w(
        "**這份是什麼**：全星系 bibliography 的**跨站**一致性檢查。既有四份盤點都是一站"
        "之內的視角，答不出「這一格填的跟隔壁站不一樣」——而一本書被多站收錄是常態，"
        "所以填錯永遠不會被抓，只有沒填會。`year` 是首頁年代分佈圖的軸，兩站對同一本書"
        "填不同年，圖上就會落在不同年代。\n"
    )
    w(
        "**工具不替人判**：矛盾至少有兩種，處理方式相反——(1) **初版 vs 改版**，schema 要"
        "初版年，但不能無腦取小（有些早年份指的是同名錄音課程，書晚很多年才出）；"
        "(2) **系列列 vs 單卷列**，一個 slug 被當成一整套書的代表列，兩邊都對、不是債。"
        "下面把 title 一起列出來，就是為了讓第二種一眼看得出來。\n"
    )

    w("## 摘要\n")
    w("| 檢查 | 數 | 後果 |")
    w("| --- | ---: | --- |")
    w(f"| 有 slug 的條目 | {total} | — |")
    w(f"| **跨站 year 矛盾** | **{len(conflicts)}** | 同一本書在年代圖上出現在兩個年代 |")
    w(f"| 缺 year、但別站已填 | **{len(fillable)}** | 零判斷可補（直接抄，不必查書） |")
    w("")

    w(f"## 一、跨站矛盾：{len(conflicts)} 本\n")
    if not conflicts:
        w("無——所有被多站收錄的書，`year` 都一致。\n")
    else:
        w("每組列出各年份及主張它的站；`title` 不同時多半是「系列列 vs 單卷列」，不是債。\n")
        for slug in sorted(conflicts):
            w(f"### `{slug}`\n")
            for y in sorted(conflicts[slug]):
                who = "、".join(f"{st}（{ti}）" for st, ti in conflicts[slug][y])
                w(f"- **{y}** — {who}")
            w("")

    w(f"## 二、缺 year、別站有現成答案：{len(fillable)} 筆\n")
    if not fillable:
        w("無。\n")
    else:
        w(
            "這批不必查書：同一個 slug 別站已經填了。**來源本身也在第一節出現的先別抄**"
            "——那表示答案自己就有兩個版本。\n"
        )
        w("| 缺的站 | slug | 書名 | 別站填的 |")
        w("| --- | --- | --- | --- |")
        for st, sl, ti, ys in sorted(fillable):
            src = "；".join(
                f"{y}（{'、'.join(s for s, _ in v)}）" for y, v in sorted(ys.items())
            )
            flag = " ⚠︎ 來源自身矛盾" if len(ys) > 1 else ""
            w(f"| `{st}` | `{sl}` | {ti} | {src}{flag} |")
        w("")

    w("## 重跑\n")
    w("```bash")
    w("notes-core/tools/export-year-conflicts.py")
    w("```\n")
    w(
        "補完之後重跑，該筆就會從這裡消失。與 [MISSING-YEARS.md](./MISSING-YEARS.md) 的"
        "分工：那份問「空不空」，這份問「一不一致」。"
    )

    text = stamp(
        "\n".join(buf), "tools/export-year-conflicts.py", _dt.datetime.now().astimezone().isoformat(timespec="seconds")
    )
    if len(sys.argv) > 1 and sys.argv[1] == "-":
        print(text)
    else:
        OUT.write_text(text + "\n", encoding="utf-8")
        print(f"→ {OUT}（矛盾 {len(conflicts)}、可補 {len(fillable)}）")


if __name__ == "__main__":
    main()
