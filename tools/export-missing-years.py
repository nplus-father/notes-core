#!/usr/bin/env python3
"""把全星系 bibliography 裡缺 `year` 的條目匯出成補漏清單（docs/MISSING-YEARS.md）。

用法：
    notes-core/tools/export-missing-years.py       # 寫進 notes-core/docs/MISSING-YEARS.md
    notes-core/tools/export-missing-years.py -     # 印到 stdout

星系根目錄（放所有 -note 站的容器目錄）預設推導成 tools/../..；佈局不同時用
NOTES_ROOT= 覆寫，與 new-note.sh / bump-notes-core.sh / export-wanted.py 同慣例。

**為什麼要有這份**：notes-core v0.20.0 起 `year` 從「可有可無的補充」升格成盤點表的
**排序鍵**與**年代分佈圖的軸**。缺 year 的條目會沉到該分組最底、也不進圖表——書還在
表上、只是從時間軸上消失了。這份就是那批「在架上但不在時間軸上」的書。

**為什麼不自動填**：書 repo 的 book-cover `date=` 是**手上這一版的出版日**，不是
schema 要的**初版年**（清單革命 repo 記 2011 年平裝版，初版是 2009；同一本書的
繁中版更晚）。照抄會把整條時間軸系統性往後推，而那正是這張圖要講的事。所以這裡只把
版次日當**線索**列出來，補哪個年份由人決定。

**解析方式**：直接讀 `defineBibliography([...])` 的原始碼，抓 depth-1 的物件字面值
（字串裡的括號不算）。不 import TS——那需要一整套 Astro/Vite 解析鏈，而這裡只要欄位。
"""

import os
import re
import sys
from io import StringIO
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("NOTES_ROOT", HERE.parent.parent))
BOOKS = ROOT.parent / "books-management" / "books-done"
OUT = HERE.parent / "docs" / "MISSING-YEARS.md"


def entries_of(src: str) -> list[str]:
    """抓 defineBibliography([...]) 裡 depth-1 的物件字面值。"""
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


def cover_dates() -> dict[str, str]:
    """slug → 書 repo 的 book-cover date=（手上那一版的出版日，僅供對照）。"""
    out: dict[str, str] = {}
    if not BOOKS.is_dir():
        return out
    for toml in BOOKS.glob("*/*/*/*/site/hugo.toml"):
        m = re.search(
            r'baseURL\s*=\s*"https://nplus\.wiki/([^/"]+)/?"',
            toml.read_text(encoding="utf-8"),
        )
        idx = toml.parent / "content" / "_index.md"
        if not m or not idx.exists():
            continue
        d = re.search(r'date="([^"]+)"', idx.read_text(encoding="utf-8"))
        if d:
            out[m.group(1)] = d.group(1)
    return out


def main() -> None:
    dates = cover_dates()
    rows, totals = [], []
    for f in sorted(ROOT.glob("*/src/data/bibliography.ts")):
        station = f.parts[-4]
        es = entries_of(f.read_text(encoding="utf-8"))
        missing = [e for e in es if field(e, "year") is None]
        totals.append((station, len(es), len(es) - len(missing), len(missing)))
        for e in missing:
            slug = field(e, "slug") or ""
            rows.append(
                {
                    "station": station,
                    "title": field(e, "title") or "(無 title)",
                    "original": field(e, "original") or "",
                    "status": field(e, "status") or "?",
                    "group": field(e, "group") or "",
                    "hint": dates.get(slug, ""),
                }
            )

    totals.sort(key=lambda t: (-t[3], t[0]))
    grand = sum(t[1] for t in totals)
    gap = sum(t[3] for t in totals)
    stations = sum(1 for t in totals if t[3])
    hinted = sum(1 for r in rows if r["hint"])
    thin = [t for t in totals if t[2] < 4]

    o = StringIO()
    o.write("# 缺出版年清單（bibliography `year` 全星系匯出）\n\n")
    o.write(
        "**這份是什麼**：各 note 站 `src/data/bibliography.ts` 裡**沒填 `year`** 的條目。由\n"
        "`notes-core/tools/export-missing-years.py` 生成，**不要手改**——補各站的 bibliography 再重跑。\n\n"
        "**為什麼要補**：notes-core v0.20.0 起 `year` 是盤點表的**排序鍵**與首頁**年代分佈圖的軸**。\n"
        "缺 year 的條目會沉到該分組最底、也不進圖表——書還在表上，只是從時間軸上消失了。\n\n"
        "**填哪一個年份**：schema 要的是**初版年**（原文首次出版），不是手上這一版、更不是中譯版。\n"
        "下面的 📕 是該書 repo `book-cover` 記的版次日，只能當**線索**——照抄會把時間軸整條往後推。\n\n"
    )
    o.write(
        f"目前：{len(totals)} 站 / {grand} 筆，缺 year **{gap} 筆**（{gap / grand * 100:.1f}%），"
        f"分佈在 {stations} 站；其中 {hinted} 筆查得到版次日線索。\n\n"
    )
    if thin:
        o.write(
            "> [!WARNING]\n> 有年份的條目少於 4 筆、畫不出年代分佈圖的站："
            + "、".join(f"`{t[0]}`（{t[2]} 筆）" for t in thin)
            + "\n\n"
        )
    else:
        o.write("每一站「有 year」的條目都 ≥ 4 筆，所以年代分佈圖全都畫得出來，只是少了這些點。\n\n")

    o.write("## 各站缺口\n\n")
    o.write("缺越多排越前；缺 0 的站略去。\n\n")
    o.write("| 站 | 總筆數 | 有 year | 缺 year |\n| --- | ---: | ---: | ---: |\n")
    for st, tot, wy, ms in totals:
        if ms:
            o.write(f"| {st} | {tot} | {wy} | {ms} |\n")

    o.write("\n## 逐筆清單\n\n")
    o.write("格式：`[status]` 書名 / 原文 · 分組 — 📕 書 repo 記的版次日（若有）\n")
    cur = None
    for r in rows:
        if r["station"] != cur:
            cur = r["station"]
            n = sum(1 for x in rows if x["station"] == cur)
            o.write(f"\n### {cur}（{n} 筆）\n\n")
        orig = f" / {r['original']}" if r["original"] else ""
        group = f" · {r['group']}" if r["group"] else ""
        hint = f" — 📕 {r['hint']}" if r["hint"] else ""
        o.write(f"- [{r['status']}] {r['title']}{orig}{group}{hint}\n")

    o.write(
        "\n## 補不上來的那幾筆\n\n"
        "有些條目**本來就不該有單一年份**，補不上是對的，不是欠債：\n\n"
        "- **上古典籍**（論語、道德經、孫子兵法、理想國、尼各馬可倫理學…）：成書年本身是區間。\n"
        "  真要上時間軸就填約略的負數年（`year: -500`），圖表標籤會顯示成 `500 BC`。\n"
        "- **`skipped` 的彙總列**（「勵志小品群 / Kiss That Frog! / Crunch Point …」）：\n"
        "  一列代表一整批書，沒有單一出版年。留白即可。\n"
        "- **系列代表卷**（NICNT／NICOT 系列）：指的是一套書而非一本。\n\n"
        "## 重跑\n\n"
        "```bash\nnotes-core/tools/export-missing-years.py\n```\n\n"
        "補完某站的 `year` 之後重跑，該站就會從這裡消失。\n"
    )

    text = o.getvalue()
    if len(sys.argv) > 1 and sys.argv[1] == "-":
        sys.stdout.write(text)
    else:
        OUT.write_text(text, encoding="utf-8")
        print(f"{OUT}: 缺 year {gap} 筆 / {grand} 筆，分佈在 {stations} 站，{hinted} 筆有版次日線索")


if __name__ == "__main__":
    main()
