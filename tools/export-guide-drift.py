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

**判法（2026-09-03 起：逐一試讀法，不靠句型分級）**：

每個「站上 N 頁」的 N 逐一試過所有合法讀法，**沒有任何讀法成立的才報**：
  - 整站總數（概念頁，或概念頁＋題型頁）
  - N = 0：缺口陳述（「三本書都有料，站上零頁」），整站總數不可能是 0
  - 句內／段內列舉的概念頁連結數（「站上三頁以它為主引：[A]、[B]、[C]」）
  - 句內／段內點名的書的被引頁數，或多本書被引頁的聯集（「四本，站上七頁陪跑」）
  - 段內連結所在分類的頁數，或那些分類的頁數和
  - 整個 `##` 小節的連結數、小節連到的分類頁數和
  - 「頁」後面那個詞是站台自己命名的分組（出現在某章小節標題裡）且那節的大小等於 N
只靠「等於某本未點名的書的被引頁數」放行的另列**低信心通過**。

**驗證**：`--validate "<時間>"` 拿各站在那個時間點的導覽配現在的頁數回放——那之後被人改掉的
數字＝真債、沒改的＝正確，算漏報與誤報。2026-09-03 用四個基準（08-27、08-30、09-02、09-03 15:00）
跑：**漏報 0／177 筆真債，誤報 3／79**，那三筆是同一句（philosophy「十九頁收心術」——四個分類
的和，但那節連到五個分類，機器無法知道作者的分組）。

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
     等於「工具說沒事」。那一輪人工從弱訊號撈出 22 筆真債（18 站）。**修法不是繼續加句型**——
     自然語言分不完；改成逐一試讀法（見上）。
  6. **讀法只能收緊不能放寬**：「分類的部分和」曾經讓誤報歸零，但 08-27 基準回放時它把
     philosophy「十八→十九」那筆真債放行了（18 也是那五個分類的某個部分和）。凡是在猜作者心裡
     分組的讀法都不能要——對不上就留給人看。改讀法後一定跑四個基準，漏報必須維持 0。

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


# ── 站台事實 ─────────────────────────────────────────────────────────────
LINK = re.compile(r"\]\(\.\./(?:\.\./)?concepts/([a-z0-9-]+)/([a-z0-9-]+)/?\)")


def station_facts(st):
    """該站的實際規模：概念頁、題型頁、各分類頁數、owned 本數、每本書被哪些頁引用、書名表。"""
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
        if (root / kind).is_dir():
            flat = len([p for p in (root / kind).glob("*.md") if p.name != "_index.md"])
            if kind == "concepts":
                concepts += flat
            else:
                problems += flat
    bib = NOTES / st / "src" / "data" / "bibliography.ts"
    bib_text = bib.read_text(encoding="utf-8") if bib.exists() else ""
    owned = len(re.findall(r'status:\s*"owned"', bib_text))
    facts = {
        "concepts": concepts,
        "problems": problems,
        "cats": cats,
        "owned": owned,
        "pages_by_book": pages_by_book(st),
        "titles": book_titles(bib_text),
    }
    facts["named_groups"] = named_groups(st, facts)
    return facts


def named_groups(st, f):
    """站台自己命名的分組：每個導覽 `## ` 小節標題 → 該小節連到的分類頁數和。

    「站上十九頁收心術」——「收心術」是 02 章一個小節標題裡的詞（「收心術的四種方言」），
    那一節連到四個分類、頁數和十九。別章再提「十九頁收心術」時，拿這張表對。
    """
    groups = []
    for p in (NOTES / st / "src" / "content" / "guide").glob("*.md"):
        text = p.read_text(encoding="utf-8")
        for m in re.finditer(r"^## +(.+)$", text, re.M):
            sec = section_of(text, m.end())
            cats = {l.split("/")[0] for l in links_in(sec)}
            if cats:
                counts = [f["cats"].get(c, 0) for c in cats]
                groups.append((m.group(1), {sum(counts), len(links_in(sec))}))
    return groups


def pages_by_book(st):
    """每本書 → 引用它的頁面集合（用頁面路徑當 key，聯集時才不會重複算）。"""
    out = collections.defaultdict(set)
    for kind in ("concepts", "problems"):
        root = NOTES / st / "src" / "content" / kind
        if not root.is_dir():
            continue
        for f in root.rglob("*.md"):
            if f.name == "_index.md":
                continue
            for b in set(re.findall(r"^\s*- book:\s*(\S+)", f.read_text(encoding="utf-8"), re.M)):
                out[b.strip("\"'")].add(f"{f.parent.name}/{f.stem}")
    return out


def book_titles(bib_text):
    """slug → 可拿來在導覽正文裡比對的書名片段（原題、中譯、《》內的名字）。"""
    titles = {}
    for m in re.finditer(r"\{[^{}]*?\}", bib_text, re.S):
        blk = m.group(0)
        slug = re.search(r'slug:\s*"([^"]+)"', blk)
        title = re.search(r'title:\s*"([^"]+)"', blk)
        if not slug or not title:
            continue
        parts = set()
        t = title.group(1)
        parts.add(t)
        # 「The Little Book of Common Sense Investing 投資常識」→ 兩半都可獨立出現
        for piece in re.split(r"\s+(?=[一-鿿《])|(?<=[一-鿿》])\s+", t):
            piece = piece.strip(" 《》:：")
            if len(piece) >= 4 or re.fullmatch(r"[一-鿿]{2,}", piece):
                parts.add(piece)
        # 冒號副題前的主題
        main = re.split(r"[:：]", t)[0].strip()
        if len(main) >= 4:
            parts.add(main)
        titles[slug.group(1)] = parts
    return titles


# ── 讀法解析 ─────────────────────────────────────────────────────────────
def sentence_of(text, pos):
    a = max(text.rfind(ch, 0, pos) for ch in "。！？\n")
    ends = [text.find(ch, pos) for ch in "。！？\n"]
    b = min([e for e in ends if e >= 0] or [len(text)])
    return text[a + 1:b]


def paragraph_of(text, pos):
    a = text.rfind("\n\n", 0, pos)
    b = text.find("\n\n", pos)
    return text[(a + 2 if a >= 0 else 0):(b if b >= 0 else len(text))]


def section_of(text, pos):
    """所在的 `## ` 小節（到下一個同級或更高級標題為止）。"""
    a = text.rfind("\n## ", 0, pos)
    b = text.find("\n## ", pos)
    return text[(a if a >= 0 else 0):(b if b >= 0 else len(text))]




def links_in(seg):
    return {f"{c}/{s}" for c, s in LINK.findall(seg)}


def named_books(seg, titles):
    hits = set()
    for slug, parts in titles.items():
        if any(p in seg for p in parts):
            hits.add(slug)
    return hits


def resolve_total(text, m, n, f):
    """一個「站上 N 頁」宣稱有沒有任何一種合法讀法成立。回 (verdict, reason)。

    verdict：ok（具體讀法成立）／weak（只有泛讀法成立）／drift（都不成立）。
    讀法由具體到寬鬆排，第一個成立的就是理由——報表要看的是「它為什麼被放行」。
    """
    if n in {f["concepts"], f["concepts"] + f["problems"]}:
        return "ok", "整站總數"
    if n == 0:
        # 「三本書都有料，站上零頁」是缺口陳述；整站總數不可能是 0，放行沒有風險
        return "ok", "零頁＝缺口陳述"
    if demoted(text, m):
        return "ok", "子集後綴／歷史敘述"
    sent = sentence_of(text, m.start())
    para = paragraph_of(text, m.start())
    sl, pl = links_in(sent), links_in(para)
    if n and len(sl) == n:
        return "ok", f"句內列舉 {n} 頁"
    if n and len(pl) == n:
        return "ok", f"段內列舉 {n} 頁"
    pb = f["pages_by_book"]
    for scope, seg in (("句內", sent), ("段內", para)):
        books = named_books(seg, f["titles"])
        if not books:
            continue
        for b in books:
            if len(pb.get(b, ())) == n:
                return "ok", f"{scope}點名的書被引 {n} 頁"
        union = set().union(*(pb.get(b, set()) for b in books))
        if len(union) == n:
            return "ok", f"{scope}點名 {len(books)} 本書的被引頁聯集 = {n}"
    # 段內連結落在哪些分類，那些分類的頁數和
    cats = {l.split("/")[0] for l in pl}
    if cats and sum(f["cats"].get(c, 0) for c in cats) == n:
        return "ok", f"段內 {len(cats)} 個分類的頁數和 = {n}"
    for c in cats:
        if f["cats"].get(c) == n:
            return "ok", f"段內連結所在分類 {c} 有 {n} 頁"
    # 整個 ## 小節：「問題三……站上十頁裡」——那一節剛好連了十頁；
    # 「四張卡片合起來撐起站上十九頁」——那一節連到的四個分類頁數和是十九
    sec = section_of(text, m.start())
    secl = links_in(sec)
    if n and len(secl) == n:
        return "ok", f"小節內列舉 {n} 頁"
    sec_cats = {l.split("/")[0] for l in secl}
    counts = [f["cats"].get(c, 0) for c in sec_cats]
    if counts and sum(counts) == n:
        return "ok", f"小節內 {len(sec_cats)} 個分類的頁數和 = {n}"
    # 不做「分類的部分和」：它在猜作者心裡的分組。philosophy 的「十九頁收心術」是四個分類的和，
    # 但那一節連到五個分類，部分和同時包含 18 與 19——2026-08-27 基準回放時它把「十八→十九」
    # 那筆真債放行了。分組的大小只有作者知道，對不上就交給人看。
    # 「頁」後面的那個詞是不是站台自己命名的分組（出現在某章小節標題裡）
    tail = re.sub(r"[「」『』《》（）()，。：；、\s*_]", "", text[m.end():m.end() + 8])
    for k in (4, 3, 2):
        label = tail[:k]
        if len(label) < 2 or not re.fullmatch(r"[一-鿿]+", label):
            continue
        for heading, sizes in f["named_groups"]:
            if label in heading and n in sizes:
                return "ok", f"「{label}」是小節「{heading[:12]}」命名的分組，頁數 {n}"
    if n in {len(v) for v in pb.values()}:
        return "weak", "等於某本未點名的書的被引頁數"
    return "drift", "沒有任何讀法成立"


def scan_text(st, f, fname, text):
    """對一份導覽或總覽的文字做判定。回 [(fname, kind, said, actual, verdict, reason, ctx)]。"""
    rows = []
    actual_total = f"{f['concepts']}（＋題型 {f['problems']}）" if f["problems"] else str(f["concepts"])
    for m in TOTAL_STRONG.finditer(text):
        n = cn2int(m.group(1))
        if n is None:
            continue
        verdict, reason = resolve_total(text, m, n, f)
        if verdict != "ok" and is_strong(text, m):
            verdict, reason = "drift", "句型即整站宣稱，" + reason
        rows.append((fname, "站台總頁", n, actual_total, verdict, reason, ctx(text, m)))
    for m in CAT_CLAIM.finditer(text):
        cat, n = m.group(1), cn2int(m.group(2))
        if cat in f["cats"] and n is not None:
            if n == f["cats"][cat]:
                rows.append((fname, f"{cat} 分類", n, str(f["cats"][cat]), "ok", "分類頁數", ctx(text, m)))
            elif demoted(text, m):
                rows.append((fname, f"{cat} 分類", n, str(f["cats"][cat]), "ok", "歷史敘述", ctx(text, m)))
            else:
                rows.append((fname, f"{cat} 分類", n, str(f["cats"][cat]), "drift", "分類頁數不符", ctx(text, m)))
    for m in OWNED_CLAIM.finditer(text):
        n = cn2int(m.group(1))
        if n is None:
            continue
        if n == f["owned"]:
            rows.append((fname, "owned 本數", n, str(f["owned"]), "ok", "owned 本數", ctx(text, m)))
        elif demoted(text, m):
            rows.append((fname, "owned 本數", n, str(f["owned"]), "ok", "歷史敘述", ctx(text, m)))
        else:
            rows.append((fname, "owned 本數", n, str(f["owned"]), "drift", "owned 本數不符", ctx(text, m)))
    return rows


def guide_files(st):
    files = sorted((NOTES / st / "src" / "content" / "guide").glob("*.md"))
    ov = NOTES / st / "src" / "data" / "overview.ts"
    if ov.exists():
        files.append(ov)
    return files


def scan(st):
    f = station_facts(st)
    rows = []
    for p in guide_files(st):
        rows += scan_text(st, f, p.name, p.read_text(encoding="utf-8"))
    return rows


def stations_all():
    return sorted(p.parts[len(NOTES.parts)] for p in NOTES.glob("*-note/src/data/bibliography.ts"))


# ── 報表 ─────────────────────────────────────────────────────────────────
def table(o, rows, with_reason=True):
    o.write("| 站 | 檔 | 宣稱的是 | 導覽說 | 實際 | 判定理由 | 上下文 |\n| --- | --- | --- | ---: | ---: | --- | --- |\n")
    for st, (fn, kind, said, actual, verdict, reason, c) in rows:
        c = c.replace("|", "｜")
        o.write(f"| `{st}` | {fn} | {kind} | **{said}** | {actual} | {reason} | …{c}… |\n")


def report(stations, only):
    drift, weak, ok = [], [], []
    for st in stations:
        for r in scan(st):
            {"drift": drift, "weak": weak, "ok": ok}[r[4]].append((st, r))
    o = io.StringIO()
    o.write("# 導覽數字與現況不符\n\n")
    o.write(
        "由 `tools/export-guide-drift.py` 產生。判準：導覽（`guide/*.md`）與首頁總覽"
        "（`overview.ts`）裡**指向站台自身規模的數字**——總頁數、某分類幾頁、收了幾本"
        "——回去數實際檔案對不對得上。\n\n"
        "**為什麼另立一支**：`tier-audit.py` 的「導覽落後」欄只比日期（`enrichedAt` vs "
        "`writtenAt`），抓的是「內容補過、策展層還沒回頭看」；但站台長大時**日期可以完全"
        "不動而內容照樣說謊**。2026-08-27 收《飛輪效應》那輪就是這樣被手動抓到的。\n\n"
        "**判法（2026-09-03 起）**：每個數字逐一試過所有合法讀法——整站總數、句內／段內列舉的"
        "連結數、句內／段內點名的書被引頁數（含聯集）、段內連結所在分類的頁數（含加總）——"
        "**沒有任何讀法成立的才報**。這取代了先前靠句型分「強／弱訊號」的做法（句型分不完，"
        "2026-09-03 那輪從弱訊號裡人工撈出 22 筆真債）。\n\n"
        f"- **要改：{len(drift)} 筆**——沒有任何讀法能解釋這個數字。\n"
        f"- 低信心通過：{len(weak)} 筆——只靠「等於某本未點名的書的被引頁數」放行，抽查用。\n"
        f"- 通過：{len(ok)} 筆——具體讀法成立，理由列在表裡。\n\n"
        "計數口徑同時接受「只算概念頁」與「概念頁＋題型頁」兩種。\n\n"
    )
    o.write(f"## 要改：{len(drift)} 筆\n\n")
    table(o, drift) if drift else o.write("無——導覽的規模數字都對得上現況。\n")
    o.write(f"\n## 低信心通過：{len(weak)} 筆\n\n")
    table(o, weak) if weak else o.write("無。\n")
    o.write(f"\n## 通過：{len(ok)} 筆\n\n")
    o.write("<details><summary>展開</summary>\n\n")
    table(o, ok) if ok else o.write("無。\n")
    o.write("\n</details>\n")
    o.write(
        "\n## 修法\n\n"
        "**保語氣、只改被現況打臉的數字**（MODEL-ROUTING §二最後一列：導覽過期多數不必重寫，"
        "只要對帳）。改完把該章的 `writtenAt` 推到當天；如果是 `overview.ts`，順手看一眼"
        "`lede`／`Verdict` 有沒有一起過期。\n\n"
        "數字對不上時**不預設是導覽錯**：頁被合併或除役時，導覽反而可能是對的——先看那句話在講什麼。\n\n"
        "## 驗證\n\n```bash\nnotes-core/tools/export-guide-drift.py --validate \"2026-09-03 15:00\"\n```\n"
        "拿各站在那個時間點的導覽文字配**現在**的頁數重跑：那之後被人改掉的數字＝真債、沒改的＝正確；"
        "算分類器在這套標籤上的漏報與誤報。\n\n"
        "## 重跑\n\n```bash\nnotes-core/tools/export-guide-drift.py\n```\n"
    )
    text = stamp(o.getvalue(), "tools/export-guide-drift.py", _dt.datetime.now().astimezone().isoformat(timespec="seconds"))
    if only:
        sys.stdout.write(text)
    else:
        OUT.write_text(text, encoding="utf-8")
        print(
            f"{OUT}: 要改 {len(drift)} 筆、低信心通過 {len(weak)} 筆、通過 {len(ok)} 筆，"
            f"要動的涉及 {len({s for s, _ in drift})} 站"
        )


# ── 驗證：拿歷史版本的導覽配現在的事實回放 ────────────────────────────────
def git_text(st, path, before):
    import subprocess
    repo = NOTES / st
    rel = str(path.relative_to(repo))
    rev = subprocess.run(["git", "-C", str(repo), "log", "-1", f"--before={before}", "--format=%H", "--", rel],
                         capture_output=True, text=True).stdout.strip()
    if not rev:
        return None
    r = subprocess.run(["git", "-C", str(repo), "show", f"{rev}:{rel}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def label_against_current(old_text, new_text, m):
    """舊文裡這個數字，在現在的文裡變了沒。回 'drift'／'ok'／None（整段被重寫，無法對）。"""
    before = re.escape(old_text[max(0, m.start(1) - 18):m.start(1)])
    after = re.escape(old_text[m.end(1):m.end(1) + 10])
    hit = re.search(before + NUM + after, new_text)
    if not hit:
        return None
    return "ok" if hit.group(1) == m.group(1) else "drift"


def validate(before, stations):
    tp = fn = fp = tn = 0
    misses, false_alarms = [], []
    for st in stations:
        f = station_facts(st)
        for p in guide_files(st):
            old = git_text(st, p, before)
            if old is None:
                continue
            new = p.read_text(encoding="utf-8")
            rows = scan_text(st, f, p.name, old)
            # rows 與 TOTAL_STRONG 的 match 順序一致，重新掃一次拿 match 物件來標籤
            matches = [m for m in TOTAL_STRONG.finditer(old) if cn2int(m.group(1)) is not None]
            for m, row in zip(matches, [r for r in rows if r[1] == "站台總頁"]):
                truth = label_against_current(old, new, m)
                if truth is None:
                    continue
                flagged = row[4] == "drift"
                if truth == "drift" and flagged:
                    tp += 1
                elif truth == "drift" and not flagged:
                    fn += 1
                    misses.append((st, row))
                elif truth == "ok" and flagged:
                    fp += 1
                    false_alarms.append((st, row))
                else:
                    tn += 1
    total = tp + fn + fp + tn
    print(f"基準時間 {before}｜可標籤的宣稱 {total} 筆：真債 {tp + fn}、正確 {fp + tn}")
    print(f"  抓到真債 {tp}／{tp + fn}（漏報 {fn}）　誤報 {fp}／{fp + tn}　準確率 {(tp + tn) / total:.1%}" if total else "  無資料")
    if misses:
        print("\n漏報（真債卻放行）——這是危險的那一種：")
        for st, r in misses:
            print(f"  {st:24} {r[0]:30} 說 {r[2]:>3} 實 {r[3]:<8} 放行理由：{r[5]}｜…{r[6][:60]}…")
    if false_alarms:
        print("\n誤報（正確卻被報）——要人看一眼的成本：")
        for st, r in false_alarms:
            print(f"  {st:24} {r[0]:30} 說 {r[2]:>3} 實 {r[3]:<8} …{r[6][:70]}…")


def main():
    args = [a for a in sys.argv[1:]]
    if args and args[0] == "--validate":
        before = args[1] if len(args) > 1 else "2026-09-03 15:00"
        validate(before, args[2:] or stations_all())
        return
    only = args[0] if args and not args[0].startswith("-") else None
    report([only] if only else stations_all(), only)


if __name__ == "__main__":
    main()
