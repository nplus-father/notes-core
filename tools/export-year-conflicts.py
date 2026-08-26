#!/usr/bin/env python3
"""跨站比對同一本書的欄位（year／author／original），把矛盾匯出（docs/YEAR-CONFLICTS.md）。

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

**2026-08-26 擴充**：同一套跨站視角也套用到另外兩個欄位。
- **slug 撞號**（最嚴重）：同一個 `slug` 在不同站被填成不同作者（比**姓氏鍵**，與
  `src/lib/library.ts` 的 `authorKey` 同規則）——多半代表兩站指到**不同的書**，
  而封面與延伸連結會全部指錯。首跑 0 本。
- **`original` 語言不一致**：schema 說它是**原文書名**，但有站填了英譯（《懺悔錄》
  被填成 `Confessions` 而非 `Confessiones`）。**只報「一邊不是另一邊前綴」的組**——
  短標題 vs 帶副標題兩者都對，不算債（17 組差異裡只有 3 組是真的）。
`title` 刻意不檢查：259 組差異全是同一本書的不同寫法（有的站寫中譯、有的寫中英合併），
而作者姓氏鍵全部一致，證明沒有指錯書——那是設計，不是債。

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


# 已裁決「不是債」的 slug：同一個 slug 被一站當「整套書的代表列」、另一站當「單卷」用，
# 於是 year 與 original 天生就會不一致，而**兩邊都對**。列在這裡的不再報進矛盾節，
# 但會在檔尾的「已知例外」節列出來，免得下一輪重新判斷一次。
# 新增前先確認是這一類；「初版 vs 改版」不屬於此，那要挑一個年份。
KNOWN_SERIES_ROWS = {
    # biblical-studies-note 拿它當「聖經信息系列（全 52 冊）」的代表列（1968＝系列起始年），
    # stott-note 則是《羅馬書的信息》單卷（1994＝該卷初版年）。
    "message-of-romans",
}

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("NOTES_ROOT", HERE.parent.parent))
OUT = HERE.parent / "docs" / "YEAR-CONFLICTS.md"


BOOKS = Path("/home/andrew/workspace/andrew/books-management/books-done")

# 第五節「早於書 repo 的 published」已逐本查證、裁定**我們的 year 才對**的 slug。
# published 欄位是「做摘要時手上那一版」，早於初版是常態（預告上架），所以會有假陽性。
SETTLED_AGAINST_PUBLISHED = {
    "knowing-doing-gap",                    # HBS 初版 2000-01；repo 的 1999 是預告年
    "hbr-guide-to-managing-stress-at-work",  # HBR 初版 2014-01；repo 的 2013 是預告年
    "hbr-guide-to-managing-stress",         # 同一本書的短標題寫法，也是 2014
    "hbr-guide-to-beating-burnout",         # HBR 出版 2021（版權頁 2020）
    "j-i-packer-his-life-and-thought",      # McGrath，IVP 2020-11
    "journey-of-modern-theology",           # Olson，IVP Academic 2013（1992 那本是前身《20 世紀神學評論》）
}


def published_years() -> dict[str, int]:
    """書 repo `site/content/_index.md` frontmatter 的 `published`。1777 本 100% 都有。

    **它不是初版年**，是做摘要時手上那一版（High Performance MySQL 標第 3 版 2012、
    Release It! 標第 2 版 2017）。所以它不能拿來直接覆蓋 `year`——但當我們的 `year`
    **晚於**它時必錯：初版年不可能晚於一個已經存在的印次。當偵測器用，別當答案用。
    """
    out: dict[str, int] = {}
    for d in BOOKS.glob("*/*/*/*"):
        f = d / "site" / "content" / "_index.md"
        if not f.is_file():
            continue
        m = re.search(r'^\s*published:\s*"?([^"\n]+)', f.read_text(encoding="utf-8", errors="ignore")[:2000], re.M)
        if m and (y := re.search(r"(1[5-9]\d\d|20\d\d)", m.group(1))):
            out[d.name] = int(y.group(1))
    return out


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


def author_key(author: str) -> str:
    """姓氏 token 當識別鍵——與 notes-core src/lib/library.ts 的 authorKey 同一套規則。

    不能拿整串作者字串比對：同一位作者的寫法本來就不統一（schema 明說「寫法不必統一」），
    也不能拿 token 集合比對（會把三個 David 併成一人）。姓氏才是識別鍵。
    """
    primary = re.split(r"\s+with\s+|\s*&\s*|\s*\(|\s*（|,", author)[0].strip()
    if not primary:
        return ""
    if not re.search(r"[A-Za-z]", primary):
        return primary
    toks = re.findall(r"[A-Za-z][A-Za-z'’-]*", primary)
    return toks[-1].lower() if toks else ""


# `original` 的差異多半**不是債**：一站寫短標題、另一站連副標題一起寫，兩者都對。
# 真正要報的只有「同一本書被填成不同語言」——schema 說 original 是**原文書名**，
# 所以《懺悔錄》該是 Confessiones 而非 Confessions（英譯）。判準：一邊不是另一邊的前綴。
def original_conflict(vals: list[str]) -> bool:
    norm = [re.sub(r"[\s:：,，.。'’\"-]", "", v).lower() for v in vals]
    for i, a in enumerate(norm):
        for b in norm[i + 1 :]:
            if not (a.startswith(b) or b.startswith(a)):
                return True
    return False


def collect() -> tuple[dict, list, int, dict, dict]:
    """slug → {year: [(station, title)]}、缺 year 的 (station, slug, title)、總條目數、
    slug → {author: [station]}、slug → {original: [station]}。"""
    have: dict[str, dict[int, list[tuple[str, str]]]] = {}
    missing: list[tuple[str, str, str]] = []
    authors: dict[str, dict[str, list[str]]] = {}
    originals: dict[str, dict[str, list[str]]] = {}
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
            au = field(e, "author")
            if au:
                authors.setdefault(slug, {}).setdefault(au, []).append(station)
            og = field(e, "original")
            if og:
                originals.setdefault(slug, {}).setdefault(og, []).append(station)
    return have, missing, total, authors, originals


def main() -> None:
    have, missing, total, authors, originals = collect()
    conflicts = {
        s: d for s, d in have.items() if len(d) > 1 and s not in KNOWN_SERIES_ROWS
    }
    fillable = [(st, sl, ti, have[sl]) for st, sl, ti in missing if sl in have]
    # slug 撞號：同一個 slug 在不同站被填成不同作者（姓氏鍵不同）＝多半指到不同的書
    collisions = {
        s: d for s, d in authors.items() if len({author_key(a) for a in d} - {""}) > 1
    }
    # original 語言不一致（前綴關係不算）
    orig_bad = {
        s: d
        for s, d in originals.items()
        if len(d) > 1 and s not in KNOWN_SERIES_ROWS and original_conflict(list(d))
    }

    # `have` 是 slug → {year: [(station, title)]}；這一節只看書，不看它被幾站收
    pub = published_years()
    later = sorted(
        {
            (sl, sts[0][1], y, pub[sl])
            for sl, years in have.items()
            if sl in pub and sl not in SETTLED_AGAINST_PUBLISHED
            for y, sts in years.items()
            if y > pub[sl]
        }
    )

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
    w(f"| **slug 撞號嫌疑** | **{len(collisions)}** | 兩站可能指到不同的書，封面與連結全指錯 |")
    w(f"| `original` 語言不一致 | **{len(orig_bad)}** | 原文書名欄填了譯名 |")
    w(f"| **year 晚於書 repo 的 published** | **{len(later)}** | 填的是某個改版年，不是初版年 |")
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

    w(f"## 三、slug 撞號嫌疑：{len(collisions)} 本\n")
    if not collisions:
        w("無——被多站收錄的書，作者姓氏鍵都一致。\n")
    else:
        w(
            "同一個 `slug` 在不同站被填成不同作者（**姓氏鍵**不同）。這是最嚴重的一類——"
            "多半代表兩站其實指到**不同的書**，而封面與延伸連結會全部指錯。\n"
        )
        for slug in sorted(collisions):
            w(f"- `{slug}`：" + "；".join(
                f"「{a}」（{'、'.join(sts)}）" for a, sts in collisions[slug].items()))
        w("")

    w(f"## 四、`original` 語言不一致：{len(orig_bad)} 本\n")
    if not orig_bad:
        w("無。\n")
    else:
        w(
            "schema 說 `original` 是**原文書名**，所以《懺悔錄》該是 `Confessiones` 而非英譯 "
            "`Confessions`。**只報「一邊不是另一邊前綴」的組**——短標題 vs 帶副標題兩者都對，"
            "不列入。\n"
        )
        for slug in sorted(orig_bad):
            w(f"- `{slug}`：" + "；".join(
                f"「{o}」（{'、'.join(sts)}）" for o, sts in orig_bad[slug].items()))
        w("")

    w(f"## 五、`year` 晚於書 repo 的 `published`：{len(later)} 本\n")
    w(
        "書 repo 的 `_index.md` frontmatter 有 `published` 欄位（1777 本 **100% 都有**），"
        "是做摘要時手上那一版的出版日。**我們的 `year` 晚於它就必錯**——初版年不可能晚於"
        "一個已經存在的印次，代表這格填的是某次改版的年份。\n"
    )
    w(
        "**但 `published` 也不是初版年**（High Performance MySQL 標的是第 3 版 2012、"
        "Release It! 標的是第 2 版 2017），所以**不能直接抄過來**——要查真初版。反向也有"
        "假陽性：`published` 偶爾是預告上架年而早於實際出版（HBR 那批），查證後把 slug "
        "加進 `SETTLED_AGAINST_PUBLISHED` 就不會再報。\n"
    )
    if not later:
        w("無。\n")
    else:
        w("| slug | 書名 | 我們填的 | repo published |")
        w("| --- | --- | ---: | ---: |")
        for sl, ti, y, p in later:
            w(f"| `{sl}` | {ti} | {y} | {p} |")
        w("")

    w(f"## 已知例外（不報進上面各節）：{len(KNOWN_SERIES_ROWS)} 本\n")
    w(
        "同一個 slug 被一站當「整套書的代表列」、另一站當「單卷」用，於是 `year` 與 "
        "`original` 天生不一致，而**兩邊都對**。清單寫在 `export-year-conflicts.py` 的 "
        "`KNOWN_SERIES_ROWS`；要加新的，先確認它是這一類——「初版 vs 改版」不屬於此。\n"
    )
    for s in sorted(KNOWN_SERIES_ROWS):
        w(f"- `{s}`")
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
        print(
            f"→ {OUT}（year 矛盾 {len(conflicts)}、可補 {len(fillable)}、"
            f"slug 撞號 {len(collisions)}、original 語言不一致 {len(orig_bad)}）"
        )


if __name__ == "__main__":
    main()
