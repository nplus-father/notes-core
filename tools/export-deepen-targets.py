#!/usr/bin/env python3
"""挑出「大部頭正典卻只被挖了一鏟」的書，匯出深挖對象清單（docs/DEEPEN-TARGETS.md）。

用法：
    notes-core/tools/export-deepen-targets.py       # 寫進 notes-core/docs/DEEPEN-TARGETS.md
    notes-core/tools/export-deepen-targets.py -     # 印到 stdout

星系根目錄預設推導成 tools/../..，用 NOTES_ROOT= 覆寫（與其他 export-*.py 同慣例）。

**與 DEEPEN-READY.md 的分工**：那份回答「**該進哪一站**」（站的層級：書收齊了沒、頁/書
多少）；這份回答「**進站之後該挖哪本書**」（書的層級）。兩份都是排序表，不是工作日誌
（那是 ENRICH-BACKLOG）。

**為什麼需要書的層級**：判層債歸零之後，「哪裡還薄」這個問題失去了現成訊號——
tier-audit 只抓「spine 且零引用」（真欠債），但**被引 1 次的 spine 它一律放行**，
而那正是大部頭最常見的狀態。2026-08-26 實測：theology-note 49 本 spine **每本恰好 1 頁**、
management-note 42 本裡 37 本只有 1 頁——健康，但薄得看不出來。

**訊號＝書的分量 vs 站給它的頁數**。分量用書 repo `site/content/docs` 底下的
`_index.md` 數（章節與次章節），頁數用站上 `book:` 欄實際引到它的**不同頁數**。
`章節數 ÷ 頁數` 越大，代表這本書被挖到的比例越低。

**這份只排序，不開單。** 每頁該切哪個概念、跟既有頁怎麼分工、anchor 落哪幾章，
仍是 `/note-check --enrich` 進站後的判斷（依 MODEL-ROUTING 留給 Fable 開單）。

**排除清單（EXCLUDED_KINDS）**：有些書天生就不該被挖成多頁——工具書／辭典（按條目查，
不是按論證讀）、小說與文學（本站不是文評站）、條目式合輯。它們章節數必然很高，
不排除的話會永遠霸佔排行前段。判準是**體裁**，不是「我暫時不想挖」；後者屬於選題，
不該寫進工具。
"""

import os
import re
import sys
import datetime as _dt

from _stamp import stamp
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("NOTES_ROOT", HERE.parent.parent))
BOOKS = ROOT.parent / "books-management" / "books-done"
OUT = HERE.parent / "docs" / "DEEPEN-TARGETS.md"

# 章節數 ≥ 此值才算「大部頭」。書庫 1776 本的章節數中位數是 18、90 百分位是 48，
# 取 30 約當前三成——低於這個的書，一頁挖完是誠實的。
HEAVY = 30

# 體裁上就不該挖成多頁的書（見 docstring）。加新的要說明體裁理由。
EXCLUDED_KINDS = {
    # 工具書／辭典：按條目查，不是按論證讀
    "new-dictionary-of-theology": "神學辭典，按條目查閱",
    "5-min-mba-tools": "工具條目合輯，每條各自獨立",
    # 文學作品：本站收的是它的思想，不做文本細讀
    "chronicles-of-narnia": "小說七部曲",
    "gulag-archipelago": "文學性紀實巨著",
}


def entries_of(src: str) -> list[str]:
    """抓 defineBibliography([...]) 裡 depth-1 的物件字面值（與其他 export-*.py 同實作）。"""
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
    return m.group(1) if m else None


def book_depth() -> dict[str, int]:
    """書 repo slug → 章節數（docs 底下 _index.md 的數量）。"""
    out: dict[str, int] = {}
    if not BOOKS.is_dir():
        return out
    for cdir in BOOKS.glob("*/*/*/*/site/content/docs"):
        out[cdir.parent.parent.parent.name] = sum(1 for _ in cdir.rglob("_index.md"))
    return out


def main() -> None:
    depth = book_depth()
    rows: list[tuple[float, int, int, str, str, str]] = []
    excluded_hits: list[tuple[str, str, str]] = []
    stations = 0
    for f in sorted(ROOT.glob("*/src/data/bibliography.ts")):
        station = f.parts[-4]
        cdir = f.parent.parent / "content" / "concepts"
        if not cdir.is_dir():
            continue
        stations += 1
        cites: dict[str, set[str]] = {}
        for p in cdir.rglob("*.md"):
            if p.stem == "_index":
                continue
            for b in re.findall(r"book: ([\w-]+)", p.read_text(encoding="utf-8")):
                cites.setdefault(b, set()).add(p.stem)
        for e in entries_of(f.read_text(encoding="utf-8")):
            if 'tier: "spine"' not in e:
                continue
            slug = field(e, "slug")
            if not slug:
                continue
            ch = depth.get(slug, 0)
            pg = len(cites.get(slug, ()))
            if ch < HEAVY or pg > 1:
                continue
            title = field(e, "title") or slug
            if slug in EXCLUDED_KINDS:
                excluded_hits.append((station, title, EXCLUDED_KINDS[slug]))
                continue
            rows.append((ch / max(pg, 1), ch, pg, station, title, slug))
    rows.sort(reverse=True)

    per_station: dict[str, list] = {}
    for r in rows:
        per_station.setdefault(r[3], []).append(r)

    buf: list[str] = []
    w = buf.append
    w("# 深挖對象：大部頭卻只有一鏟的正典\n")
    w(
        "**這份是什麼**：書的層級的排序表——**進站之後該挖哪本書**。與 "
        "[DEEPEN-READY.md](./DEEPEN-READY.md) 的分工：那份回答「該進哪一站」（站的層級），"
        "這份回答「進站之後挖哪一本」。兩份都是排序表，工作日誌在 "
        "[ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md)。\n"
    )
    w(
        "**為什麼需要它**：判層債歸零後，「哪裡還薄」失去了現成訊號——`tier-audit` 只抓"
        "「spine 且**零**引用」，**被引 1 次的 spine 一律放行**，而那正是大部頭最常見的"
        "狀態。theology-note 49 本 spine 每本恰好 1 頁、management-note 42 本裡 37 本只有 "
        "1 頁：健康，但薄得看不出來。\n"
    )
    w(
        f"**判準**：`tier: spine`、書 repo 章節數 ≥ **{HEAVY}**（書庫 1776 本的中位數是 18、"
        "90 百分位是 48）、且站上引到它的**不同頁數 ≤ 1**。排序鍵是 `章節數 ÷ 頁數`。\n"
    )
    w(
        "**這份只排序，不開單。** 每頁該切哪個概念、跟既有頁怎麼分工、anchor 落哪幾章，"
        "仍是進站跑 `/note-check --enrich` 時的判斷（依 MODEL-ROUTING 留給 Fable 開單）。\n"
    )

    w("## 摘要\n")
    w("| 項目 | 數 |")
    w("| --- | ---: |")
    w(f"| 掃過的站 | {stations} |")
    w(f"| **候選（大部頭 × ≤1 頁）** | **{len(rows)}** |")
    w(f"| 涉及的站 | {len(per_station)} |")
    w(f"| 依體裁排除 | {len(excluded_hits)} |")
    w("")

    w("## 一、前 30 名（跨站總排序）\n")
    w("| # | 章節 | 頁 | 站 | 書 |")
    w("| ---: | ---: | ---: | --- | --- |")
    for i, (_, ch, pg, st, ti, slug) in enumerate(rows[:30], 1):
        w(f"| {i} | {ch} | {pg} | `{st}` | {ti} |")
    w("")

    w("## 二、依站分組\n")
    w("開單時整站一起看比較省力——同一站的候選常常共享脈絡。\n")
    for st in sorted(per_station, key=lambda s: -len(per_station[s])):
        items = per_station[st]
        w(f"### `{st}`（{len(items)} 本）\n")
        for _, ch, pg, _, ti, slug in items:
            w(f"- **{ti}** — {ch} 章 / {pg} 頁（`{slug}`）")
        w("")

    w(f"## 三、依體裁排除：{len(excluded_hits)} 本\n")
    if not excluded_hits:
        w("無。\n")
    else:
        w(
            "這些書章節數必然很高，但體裁上就不該挖成多頁——不排除會永遠霸佔排行前段。"
            "清單在 `export-deepen-targets.py` 的 `EXCLUDED_KINDS`；加新的要寫**體裁**理由，"
            "「暫時不想挖」屬於選題，不該寫進工具。\n"
        )
        for st, ti, why in sorted(excluded_hits):
            w(f"- `{st}` — {ti}：{why}")
        w("")

    w("## 重跑\n")
    w("```bash")
    w("notes-core/tools/export-deepen-targets.py")
    w("```\n")
    w("補完某本書的第二頁之後重跑，該筆就會從這裡消失。")

    text = stamp(
        "\n".join(buf),
        "tools/export-deepen-targets.py",
        _dt.datetime.now().astimezone().isoformat(timespec="seconds"),
    )
    if len(sys.argv) > 1 and sys.argv[1] == "-":
        print(text)
    else:
        OUT.write_text(text + "\n", encoding="utf-8")
        print(f"→ {OUT}（候選 {len(rows)} 本、涉及 {len(per_station)} 站）")


if __name__ == "__main__":
    main()
