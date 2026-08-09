#!/usr/bin/env python3
"""盤點全星系哪些 note 站「書收齊了、可以開始深化」（docs/DEEPEN-READY.md）。

用法：
    notes-core/tools/export-deepen-ready.py       # 寫進 notes-core/docs/DEEPEN-READY.md
    notes-core/tools/export-deepen-ready.py -     # 印到 stdout

星系根目錄預設推導成 tools/../..；佈局不同時用 NOTES_ROOT= 覆寫（與其他 tools/ 腳本同慣例）。

**為什麼是生成物而不是手寫清單**：ENRICH-BACKLOG.md 用的是同一個指標（頁數 vs owned
書數），但它是手維護的，掃描日一停就過期——2026-08-09 那份還停在 07-31，中間 68 站
的 bibliography 已經翻過好幾輪。所以排序表改成每次重跑；ENRICH-BACKLOG 專心當
「做過什麼」的工作日誌，兩者分工。

**判準**（三分類，看的是「現在的瓶頸是什麼」）：

  可深化   待收 ≤ 2 且 頁/書 < 1.5 —— 書在架上、還沒挖。這批是 /note-check --enrich 的目標。
  已深化   頁/書 ≥ 1.5 —— 相對於手上的書已經挖得夠深，缺的多半是廣度（收書）或
           使用者困惑驅動的補強（/note-master），不是再叫 enrich 產頁。
  先收書   待收 > 2 —— 瓶頸在採購不在寫作，先走 /note-wanted。

  「頁/書」是粗指標（ENRICH-BACKLOG 原本就這樣註明），精確落差要進站跑 /note-check。
  它只回答「該不該進場」，不回答「該寫哪幾頁」。

**溯源債獨立列**：沒有任何 `anchor` 的頁 = 主張沒被原文驗證過。這欄不參與三分類，
因為它是**任何**狀態的站都該先清的債——/note-check 會把它排在 backlog 最前面。
"""

import os
import re
import sys
from io import StringIO
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("NOTES_ROOT", HERE.parent.parent))
OUT = HERE.parent / "docs" / "DEEPEN-READY.md"

MINED = 1.5  # 頁/書 ≥ 此值視為「已深化」
NEAR = 2  # 待收 ≤ 此值視為「書單實質收齊」


def entries_of(src: str) -> list[str]:
    """抓 defineBibliography([...]) 裡 depth-1 的物件字面值（字串內的括號不算）。"""
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


def status_of(entry: str) -> str:
    m = re.search(r'\bstatus\s*:\s*"([^"]*)"', entry)
    return m.group(1) if m else "?"


def scan(station_dir: Path) -> dict | None:
    bib = station_dir / "src" / "data" / "bibliography.ts"
    if not bib.exists():
        return None
    es = entries_of(bib.read_text(encoding="utf-8"))
    owned = sum(1 for e in es if status_of(e) == "owned")
    wanted = sum(1 for e in es if status_of(e) == "wanted")

    pages, no_anchor, cats, cats_with_mastery = [], 0, 0, 0
    for coll in ("concepts", "problems"):
        d = station_dir / "src" / "content" / coll
        if not d.is_dir():
            continue
        for p in sorted(d.rglob("*.md")):
            if p.name == "_index.md":
                if coll == "concepts":
                    cats += 1
                    if re.search(r"^\s*mastery\s*:", p.read_text(encoding="utf-8"), re.M):
                        cats_with_mastery += 1
                continue
            pages.append(p)
            if not re.search(r"^\s*anchor\s*:", p.read_text(encoding="utf-8"), re.M):
                no_anchor += 1

    n = len(pages)
    return {
        "station": station_dir.name,
        "owned": owned,
        "wanted": wanted,
        "pages": n,
        "ratio": n / owned if owned else 0.0,
        "no_anchor": no_anchor,
        "sourced_pct": (n - no_anchor) / n * 100 if n else 0.0,
        "cats": cats,
        "mastery_cats": cats_with_mastery,
    }


def verdict(r: dict) -> str:
    if r["wanted"] > NEAR:
        return "先收書"
    if r["ratio"] >= MINED:
        return "已深化"
    return "可深化"


def main() -> None:
    rows = [s for d in sorted(ROOT.glob("*-note")) if (s := scan(d))]
    ready = sorted(
        (r for r in rows if verdict(r) == "可深化"), key=lambda r: (r["ratio"], -r["owned"])
    )
    mined = sorted((r for r in rows if verdict(r) == "已深化"), key=lambda r: -r["ratio"])
    blocked = sorted((r for r in rows if verdict(r) == "先收書"), key=lambda r: -r["wanted"])
    debt = sorted((r for r in rows if r["no_anchor"]), key=lambda r: -r["no_anchor"])

    o = StringIO()
    w = o.write
    w("# 可深化的站（哪些 note repo 的書收齊了）\n\n")
    w(
        "**這份是什麼**：全星系每一站「書單收齊了沒、手上的書挖了多少」的盤點，用來回答"
        "**現在該進哪一站做深化**。由 `notes-core/tools/export-deepen-ready.py` 生成，"
        "**不要手改**——改各站的 bibliography／內容再重跑。\n\n"
        "**與 [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md) 的分工**：那份是**做過什麼**的工作日誌"
        "（抽查輪次、契約債結案），手維護；這份是**現在該做什麼**的排序表，每次重算。\n\n"
    )
    w(
        f"**判準**：`待收 > {NEAR}` → 瓶頸在採購（先走 `/note-wanted`）｜"
        f"`頁/書 ≥ {MINED}` → 相對手上的書已挖得夠深（要的是廣度或 `/note-master`）｜"
        "其餘 → **可深化**，書在架上還沒挖。\n\n"
        "「頁/書」是粗指標，只回答「該不該進場」，不回答「該寫哪幾頁」——"
        "精確落差進站跑 `/note-check`（它會先給五個指標再給 backlog）。\n\n"
    )
    w(f"共 {len(rows)} 站：**可深化 {len(ready)}**、已深化 {len(mined)}、先收書 {len(blocked)}。\n\n")

    def table(title: str, items: list[dict], lead: str) -> None:
        w(f"## {title}（{len(items)} 站）\n\n{lead}\n\n")
        if not items:
            w("（無）\n\n")
            return
        w("| 站 | 已收 | 待收 | 頁數 | 頁/書 | 溯源 | mastery |\n")
        w("| --- | ---: | ---: | ---: | ---: | ---: | ---: |\n")
        for r in items:
            w(
                f"| `{r['station']}` | {r['owned']} | {r['wanted']} | {r['pages']} "
                f"| **{r['ratio']:.1f}** | {r['sourced_pct']:.0f}% "
                f"| {r['mastery_cats']}/{r['cats']} |\n"
            )
        w("\n")

    table(
        "可深化",
        ready,
        "書單實質收齊、手上的書還沒挖完。**由上而下就是建議的開工順序**（頁/書 愈低＝"
        "架上材料愈沒被用到）。進站跑 `/note-check` 看落差，確認後 `--enrich`。",
    )
    table(
        "已深化",
        mined,
        "相對於手上的書已經挖得夠深。再叫 `--enrich` 產頁容易變成灌水——"
        "這批要的是**廣度**（收更多書，走 `/note-wanted`）或**使用者困惑驅動**的補強"
        "（`/note-master`）。",
    )
    table(
        "先收書",
        blocked,
        f"待收超過 {NEAR} 本，瓶頸在採購不在寫作。先走 `/note-wanted`——"
        "而且它的準則①正是「優先讓快收齊的站歸零」，這批裡差 1–2 本的會被排進前 20。",
    )

    w("## 溯源債（獨立於上面三類）\n\n")
    w(
        "沒有任何 `anchor` 的頁 ＝ **主張沒被原文驗證過**。這欄不參與三分類，因為它是"
        "任何狀態的站都該先清的債——`/note-check` 會把它排在 backlog 最前面，且"
        "**必改不是選改**（回原文逐段核對後改寫，不是補一個 anchor 上去了事）。\n\n"
    )
    if debt:
        w("| 站 | 未溯源頁 | 總頁數 | 溯源率 |\n| --- | ---: | ---: | ---: |\n")
        for r in debt:
            w(f"| `{r['station']}` | **{r['no_anchor']}** | {r['pages']} | {r['sourced_pct']:.0f}% |\n")
    else:
        w("（全星系溯源率 100%。）\n")

    w("\n## 重跑\n\n```bash\nnotes-core/tools/export-deepen-ready.py\n```\n")

    text = o.getvalue()
    if len(sys.argv) > 1 and sys.argv[1] == "-":
        sys.stdout.write(text)
    else:
        OUT.write_text(text, encoding="utf-8")
        print(
            f"{OUT}: {len(rows)} 站 — 可深化 {len(ready)}、已深化 {len(mined)}、"
            f"先收書 {len(blocked)}、有溯源債 {len(debt)}"
        )


if __name__ == "__main__":
    main()
