#!/usr/bin/env python3
"""盤點「導覽的數字宣稱跟不上站台現況」——導覽說十二頁，站上已經十五頁。

**這一類以前沒有工具看得見。** `tier-audit.py` 的「導覽落後」欄只比日期
（`enrichedAt` 比所有 guide 章節的 `writtenAt` 新），抓的是「內容補過、策展層還沒回頭看」；
但站台成長時**日期可以完全不動而內容照樣說謊**——2026-08-27 收《飛輪效應》那輪就是：
collins-note 的導覽寫著「書單列為 wanted，未收」「站上十二頁概念頁」「六本 owned」，
三句都被當天的現況打臉，而 `enrichedAt` 當時還沒推，所以那一欄是乾淨的。

判準：導覽正文（`src/content/guide/*.md`）與首頁總覽（`src/data/overview.ts`）裡
**指向站台自身規模的數字**，回去數實際檔案：

  1. 站台總頁數    「站上十二頁概念頁」「寫完站上六十七頁」「站上六十五頁互相連結之後」
  2. 分類頁數      「scrum 分類十二頁」「randomness 分類四頁」
  3. owned 本數    「收完這二十本」「六本 owned」

**三級證據**（2026-09-03 由兩級改成三級，原因見坑 5）：

- **強訊號**＝數字後面接得住「總數」語境（`概念頁`／`分N區`／`分在`／`互相連結`／
  前面是`寫完`、`讀完`、`收完`）。這種句子在講整站規模，數字錯就是錯。
- **待判**＝句型看不出是不是總數，而且這個數字**對不上該站任何一本書的被引頁數**。
  子集宣稱（「站上三頁以它為主引」）的數字必然等於某本書的被引頁數；對不上就代表
  它在講別的東西，而「別的東西」多半就是整站規模。**這一節要人逐筆看**。
- **弱訊號**＝數字剛好等於某本書的被引頁數，幾乎確定是子集宣稱，寫的是對的。供抽查。

計數口徑同時接受兩種，只有兩個都對不上才報：
  - 只算 `concepts/`（多數站）
  - `concepts/` ＋ `problems/`（behaviour-interview、system-design、design-patterns…
    這類站的導覽會寫「站上五十頁（三十六頁概念、十四種題型）」，50 = 36 + 14）

踩過的坑，別重犯：
  1. **子集宣稱是這裡的主要假陽性來源**，不是漏報。第一版沒有分級，48 筆裡有一半是
     「站上三頁以它為主引」這種——照著改會把對的句子改成錯的。
  2. **中文數字要換算**（十二、六十七），只認阿拉伯數字會漏掉導覽裡的絕大多數。
  3. 這支只**指出數字對不上**，不判斷該改哪一邊：頁數少了可能是導覽舊了，也可能是
     頁被合併／除役而導覽才是對的。改之前看一眼那句話在講什麼。
  4. **已知盲區**：同一個數字在同段落無前綴地再出現（「把十四頁一口氣讀完」「讀這十四頁」）
     抓不到——放寬前綴會把所有「N 頁」都炸成假陽性。所以修強訊號時要把那一段整段讀完，
     別只改工具指到的那一行（2026-08-27 collins 02-threads 就漏了兩處，隔輪人工撞到）。
  5. **句型分級會漏真債**（2026-09-03 B 類輪實證）：「站上十五頁一口氣讀完」「站上三十頁裡」
     「站上二十五頁裡」都是整站宣稱，但句型不符強訊號的白名單，全被丟進弱訊號那堆 47 筆裡，
     等於「工具說沒事」。那一輪人工從弱訊號撈出 22 筆真債（18 站）。
     **修法不是繼續加句型**——自然語言分不完；改成「兩種讀法都驗」：子集宣稱的數字一定等於
     某本書的被引頁數，兩種讀法都對不上的就進待判。這條把 47 筆縮到十幾筆要人看的。

用法：
    python3 tools/export-guide-drift.py            # 全星系，寫 docs/GUIDE-DRIFT.md
    python3 tools/export-guide-drift.py <station>  # 只看一站，印到畫面
"""
import collections
import datetime as _dt
import io
import re
import sys

from _stamp import stamp
from pathlib import Path

CORE = Path(__file__).resolve().parents[1]
NOTES = CORE.parent
OUT = CORE / "docs" / "GUIDE-DRIFT.md"

CN = "零一二三四五六七八九十"
NUM = rf"(\d+|[{CN}]{{1,3}})"
# 強訊號：數字兩側有「這是整站規模」的語境
TOTAL_BEFORE = r"(?:寫完|讀完|收完)\s*"
TOTAL_AFTER = r"(?:概念頁|分在|分\S{1,3}區|互相連結|讀下來)"
TOTAL_STRONG = re.compile(rf"(?:{TOTAL_BEFORE})?(?:站上|全站|共)\s*{NUM}\s*頁\s*(?:（[^）]*）)?\s*(?:{TOTAL_AFTER})?")
CAT_CLAIM = re.compile(rf"([a-z][a-z0-9-]{{2,}})\s*分類\s*{NUM}\s*頁")
# 只認「收完這 N 本」這種講整站書架的句式。裸的「N 本 owned」幾乎都在講**某一組**
# （「測試優先（三本 owned＋一本 skipped）」「企業應用那一翼六本 owned」），拿站台總數
# 去對必然全錯——第一版就是這樣多報了 5 筆。
OWNED_CLAIM = re.compile(rf"收完\s*這?\s*{NUM}\s*本")


def cn2int(s):
    if s.isdigit():
        return int(s)
    d = {c: i for i, c in enumerate("零一二三四五六七八九")}
    if s == "十":
        return 10
    if len(s) == 2 and s[0] == "十":
        return 10 + d.get(s[1], 0)
    if len(s) == 2 and s[1] == "十":
        return d.get(s[0], 0) * 10
    if len(s) == 3 and s[1] == "十":
        return d.get(s[0], 0) * 10 + d.get(s[2], 0)
    return d.get(s) if len(s) == 1 else None


# 「站上七頁概念頁的母體」「站上四頁的骨架」——接了這些詞就不是站台總數，而是
# 「某本書撐起幾頁」的子集宣稱，即使前面剛好有「概念頁」也一樣。
SUBSET_AFTER = re.compile(r"^\s*(?:概念頁)?\s*(?:的)?\s*(?:母體|骨架|來源|由它|以它|都掛|陪跑|對應|全靠)")


# 導覽會**講歷史**：「2026-08-21 之前 infrastructure 分類四頁全靠 X 撐著⋯⋯因此從四頁長到
# 六頁」——那個「四頁」講的是當時，句子本身是對的。首跑就被這種時態騙報一筆（cloud-infra）。
HISTORY = ("之前", "原本", "當時", "曾經", "長到", "增到", "從此")


def demoted(text, m):
    """這個數字是不是根本不在講「現在有幾頁」——子集宣稱或歷史敘述。兩種都不是債。"""
    if SUBSET_AFTER.match(text[m.end():m.end() + 14]):
        return True
    return any(h in text[max(0, m.start() - 30):m.end() + 30] for h in HISTORY)


def is_strong(text, m):
    """數字附近有沒有「整站規模」的語境詞。

    只有**總頁數**宣稱需要這一關：「站上三頁」多半在講子集，要有語境詞才算總數。
    分類與 owned 宣稱（「product 分類五頁」「收完這二十本」）本身就是規模宣稱，
    只過 `demoted()` 那一關就好——否則整條檢查會被這裡的門檻誤殺（首跑踩過）。
    """
    if demoted(text, m):
        return False
    # 「寫完／讀完／收完」可能落在 match 之外（前文），也可能被 TOTAL_BEFORE 吃進 match 裡
    # ——兩邊都要看。只看前文的話，「收完這二十五本、寫完站上六十七頁（…）之後」會被誤判成
    # 弱訊號（2026-08-27 首跑踩到，system-design 與 thinking 的第一章各漏一筆真債）。
    head = text[max(0, m.start() - 6):m.start()] + m.group(0)[:6]
    tail = text[m.end():m.end() + 12]
    return bool(re.search(r"(寫完|讀完|收完)", head) or re.match(rf"\s*{TOTAL_AFTER}", tail) or re.search(TOTAL_AFTER, m.group(0)))


def ctx(text, m, before=44, after=26):
    return text[max(0, m.start() - before):m.end() + after].replace("\n", " ").strip()


def station_facts(st):
    """該站的實際規模：概念頁、題型頁、各分類頁數、owned 本數。"""
    root = NOTES / st / "src" / "content"
    cats, concepts, problems = {}, 0, 0
    for kind in ("concepts", "problems"):
        for d in sorted((root / kind).glob("*/")) if (root / kind).is_dir() else []:
            n = len([p for p in d.glob("*.md") if p.name != "_index.md"])
            cats[d.name] = n
            if kind == "concepts":
                concepts += n
            else:
                problems += n
        # 有些站的 problems 是平鋪的 .md，不分子目錄
        if (root / kind).is_dir():
            flat = len([p for p in (root / kind).glob("*.md") if p.name != "_index.md"])
            if kind == "concepts":
                concepts += flat
            else:
                problems += flat
    bib = NOTES / st / "src" / "data" / "bibliography.ts"
    owned = len(re.findall(r'status:\s*"owned"', bib.read_text(encoding="utf-8"))) if bib.exists() else 0
    return {
        "concepts": concepts,
        "problems": problems,
        "cats": cats,
        "owned": owned,
        "citing": citing_counts(st),
    }


def citing_counts(st):
    """該站每一本書「被幾頁引用」的所有值。

    子集宣稱（「站上三頁以它為主引」「站上四頁都掛它」）的那個數字，必然是某本書的
    被引頁數。所以這個集合就是「數字的第二種合法讀法」——用它把待判與弱訊號分開。
    """
    per_book = collections.Counter()
    for kind in ("concepts", "problems"):
        root = NOTES / st / "src" / "content" / kind
        if not root.is_dir():
            continue
        for f in root.rglob("*.md"):
            if f.name == "_index.md":
                continue
            for b in set(re.findall(r"^\s*- book:\s*(\S+)", f.read_text(encoding="utf-8"), re.M)):
                per_book[b.strip("\"'")] += 1
    return set(per_book.values())


def scan(st):
    f = station_facts(st)
    accepted_totals = {f["concepts"], f["concepts"] + f["problems"]}
    strong, unsure, weak = [], [], []
    files = sorted((NOTES / st / "src" / "content" / "guide").glob("*.md"))
    ov = NOTES / st / "src" / "data" / "overview.ts"
    if ov.exists():
        files.append(ov)
    for p in files:
        text = p.read_text(encoding="utf-8")
        for m in TOTAL_STRONG.finditer(text):
            n = cn2int(m.group(1))
            if n is None or n in accepted_totals:
                continue
            row = (p.name, "站台總頁", n, f"{f['concepts']}（＋題型 {f['problems']}）" if f["problems"] else str(f["concepts"]), ctx(text, m))
            if is_strong(text, m):
                strong.append(row)
            elif n in f["citing"]:
                # 對得上某本書的被引頁數 → 幾乎確定是子集宣稱，寫的是對的
                weak.append(row)
            else:
                # 兩種讀法都對不上 → 這個數字在講別的東西，要人看
                unsure.append(row)
        for m in CAT_CLAIM.finditer(text):
            cat, n = m.group(1), cn2int(m.group(2))
            if cat in f["cats"] and n is not None and n != f["cats"][cat]:
                row = (p.name, f"{cat} 分類", n, str(f["cats"][cat]), ctx(text, m))
                # 分類宣稱同樣會講歷史（「之前四頁⋯⋯因此從四頁長到六頁」），走同一道護欄
                (weak if demoted(text, m) else strong).append(row)
        for m in OWNED_CLAIM.finditer(text):
            n = cn2int(m.group(1))
            if n is not None and n != f["owned"]:
                row = (p.name, "owned 本數", n, str(f["owned"]), ctx(text, m))
                (weak if demoted(text, m) else strong).append(row)
    return strong, unsure, weak


def table(o, rows):
    o.write("| 站 | 檔 | 宣稱的是 | 導覽說 | 實際 | 上下文 |\n| --- | --- | --- | ---: | ---: | --- |\n")
    for st, (fn, kind, said, actual, c) in rows:
        c = c.replace("|", "｜")
        o.write(f"| `{st}` | {fn} | {kind} | **{said}** | {actual} | …{c}… |\n")


def main():
    only = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else None
    stations = [only] if only else sorted(p.parts[len(NOTES.parts)] for p in NOTES.glob("*-note/src/data/bibliography.ts"))
    strong, unsure, weak = [], [], []
    for st in stations:
        s, u, w = scan(st)
        strong += [(st, r) for r in s]
        unsure += [(st, r) for r in u]
        weak += [(st, r) for r in w]

    o = io.StringIO()
    o.write("# 導覽數字與現況不符\n\n")
    o.write(
        "由 `tools/export-guide-drift.py` 產生。判準：導覽（`guide/*.md`）與首頁總覽"
        "（`overview.ts`）裡**指向站台自身規模的數字**——總頁數、某分類幾頁、收了幾本"
        "——回去數實際檔案對不對得上。\n\n"
        "**為什麼另立一支**：`tier-audit.py` 的「導覽落後」欄只比日期（`enrichedAt` vs "
        "`writtenAt`），抓的是「內容補過、策展層還沒回頭看」；但站台長大時**日期可以完全"
        "不動而內容照樣說謊**。2026-08-27 收《飛輪效應》那輪就是這樣被手動抓到的。\n\n"
        f"- **強訊號（數字在講整站規模）：{len(strong)} 筆**——句子接得住「概念頁」「分 N 區」"
        "「互相連結」，或前面是「寫完／讀完／收完」。這種數字錯就是錯，逐筆對現況改。\n"
        f"- **待判：{len(unsure)} 筆**——句型看不出是不是總數，而且這個數字**對不上該站任何一本書的"
        "被引頁數**。子集宣稱的數字必然等於某本書的被引頁數；對不上就代表它在講別的東西，"
        "而那多半就是整站規模。**這一節要逐筆看**，2026-09-03 那輪從這裡撈出 22 筆真債。\n"
        f"- 弱訊號：{len(weak)} 筆——數字剛好等於某本書的被引頁數（「站上三頁以它為主引」＝有三頁"
        "引用這本書），幾乎確定是子集宣稱，寫的是對的。供抽查，不是判決。\n\n"
        "計數口徑同時接受「只算概念頁」與「概念頁＋題型頁」兩種，兩個都對不上才報。\n\n"
    )
    o.write(f"## 強訊號：{len(strong)} 筆\n\n")
    if strong:
        table(o, strong)
    else:
        o.write("無——導覽的規模數字都對得上現況。\n")
    o.write(f"\n## 待判（兩種讀法都對不上，要人看）：{len(unsure)} 筆\n\n")
    if unsure:
        table(o, unsure)
    else:
        o.write("無。\n")
    o.write(f"\n## 弱訊號（數字等於某本書的被引頁數，是子集宣稱）：{len(weak)} 筆\n\n")
    if weak:
        table(o, weak)
    else:
        o.write("無。\n")
    o.write(
        "\n## 修法\n\n"
        "**保語氣、只改被現況打臉的數字**（MODEL-ROUTING §二最後一列：導覽過期多數不必重寫，"
        "只要對帳）。改完把該章的 `writtenAt` 推到當天；如果是 `overview.ts`，順手看一眼"
        "`lede`／`Verdict` 有沒有一起過期。\n\n"
        "數字對不上時**不預設是導覽錯**：頁被合併或除役時，導覽反而可能是對的——先看那句話在講什麼。\n\n"
        "## 重跑\n\n```bash\nnotes-core/tools/export-guide-drift.py\n```\n"
    )
    text = stamp(o.getvalue(), "tools/export-guide-drift.py", _dt.datetime.now().astimezone().isoformat(timespec="seconds"))
    if only:
        sys.stdout.write(text)
    else:
        OUT.write_text(text, encoding="utf-8")
        print(
            f"{OUT}: 強訊號 {len(strong)} 筆、待判 {len(unsure)} 筆、弱訊號 {len(weak)} 筆，"
            f"要動的涉及 {len({s for s, _ in strong + unsure})} 站"
        )


if __name__ == "__main__":
    main()
