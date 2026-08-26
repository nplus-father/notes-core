#!/usr/bin/env python3
"""盤點「延伸閱讀 anchor 覆蓋不足」——頁面用了書裡的事實，卻掛到不含該事實的章。

做法：把概念頁裡的**具名數字**（金額、百分比、年份、人次⋯⋯）抽出來，回查它
`furtherReading` 掛出去的章節。數字在同一本書裡找得到、卻不在任何一個掛出去的
anchor 底下 → 這頁的 anchor 太窄或指錯章，讀者點「延伸閱讀」會落在找不到內容的地方。
報告同時算出這些數字**實際落在哪幾章**，直接給可用的 anchor 候選。

只驗數字，不驗引文：書 repo 是中文密集摘要，頁面裡的引號多半是筆記自創的標籤
（「生存迴路＋情感＋概念歸類」）而非逐字引用，字面比對必然失準。數字不同——
「51%」「2,500 萬美元」「1962 年」是可判定的事實宣稱。

另有一類 `書摘查無`：數字在整本書摘裡都找不到。**這不等於錯**——books-done 是摘要
不是全文，全書才有的細節（Webvan 花 1,800 萬美元開發軟體）本來就不會進摘要。
這類只列數量供抽查，不當違規。

**2026-08-27 首輪結案**：開工時證據充分 73 頁，逐頁對書核完全部修掉，收在 0。
修法幾乎都是「另加一條」而非「擴大母章」（70:2）——因為既有 anchor 多半是精確的
子章、指的也是對的主題，問題出在頁面**還用了同一本書別章的材料**卻沒掛出去。
最典型的一種：頁面 label 自己就寫著「⋯⋯與策略性聯盟」，anchor 卻只有可分享內容那章。

核對時學到的兩件事，下一輪別重犯：
  1. **建議章的排名不可盡信**。工具按命中數排序，但排第一的可能是撞號——睡眠那頁
     的「40%」在書裡是「食物渴望提高 40%」、在頁面是「晨型人佔 40%」。加語境比對
     之後好很多（73 頁裡只剩少數要人工推翻），但掛上去前仍要看一眼那章在講什麼。
  2. **查不到不代表沒有**。用 grep 找「1300萬」找不到，是因為書裡寫「1,300 萬」有
     逗號——這害我一度誤判 1929 那頁不用補。要查就用工具的正規化比對，別手打 grep。

用法：
    python3 tools/export-anchor-gaps.py            # 全星系，寫 docs/ANCHOR-GAPS.md
    python3 tools/export-anchor-gaps.py <station>  # 只看一站，印到畫面
"""
import datetime as _dt
import re
import sys
import unicodedata

from _stamp import stamp
from collections import Counter, defaultdict
from pathlib import Path

CORE = Path(__file__).resolve().parents[1]
NOTES = CORE.parent
BOOKS = NOTES.parent / "books-management" / "books-done"
OUT = CORE / "docs" / "ANCHOR-GAPS.md"

REPOS = {d.name: d for d in BOOKS.glob("*/*/*/*") if (d / "site" / "content").is_dir()}

UNIT = r"%|％|億|萬|美元|英尺|英里|公里|磅|公斤|公分|歲|次|倍|人|本|卷|條|項|種|個|家|天|週|年|小時|分鐘"
# 小數字沒有鑑別力：「3 個步驟」「2 種」在任何一本書裡都找得到，比中了也不算證據
MIN_MEANINGFUL = 11
# 一頁掛的 anchor 太多時本來就覆蓋得廣，剩下的落空多半是別本書的事實
MAX_SUGGEST = 3

# 已裁決「不是缺口」的（頁面, 數字）。這些數字在該書裡到處都是，撞上不代表出處。
# 新增前先確認是「同一個比例被反覆引用」，而不是「頁面真的在講那一章的事」。
KNOWN_FALSE_POSITIVES = {
    # 80/20 是這本書從頭到尾的骨架（銷售章講前 20% 業務員賺 80% 傭金、時間管理章
    # 講 20% 的事產生 80% 價值⋯⋯）。頁面講的是「集中法則」，撞號不代表出處在那些章。
    ("tracy-note", "business/100-absolutely-unbreakable-laws-of-business.md"): {"80%", "20%"},
}


YEAR = re.compile(r"(1[89]|20)\d\d年$")


def norm(s: str) -> str:
    return re.sub(r"[\s,，]", "", unicodedata.normalize("NFKC", s))


def chapter_title(book: str, ch: str) -> str:
    """讀該章 `_index.md` 的 title，讓建議可以直接當 label 用。"""
    repo = REPOS.get(book)
    if not repo:
        return ""
    f = repo / "site" / "content" / ch.strip("/") / "_index.md"
    if not f.is_file():
        return ""
    m = re.search(r'^title:\s*"?([^"\n]+?)"?\s*$', f.read_text(encoding="utf8", errors="ignore"), re.M)
    return m.group(1) if m else ""


CJK = re.compile(r"[一-鿿]{2,}")
CTX_WINDOW = 14      # 頁面裡取數字前後幾個字當語境
BOOK_WINDOW = 160    # 書裡數字附近多遠算「講同一件事」


def numbers_of(body: str) -> list[tuple[str, str, set[str]]]:
    """回傳 (顯示字串, 比對用數字, 語境詞)。

    語境詞是數字前後的中文詞——沒有它，「40%」在書裡撞到「食物渴望提高 40%」
    就會被當成頁面裡「晨型人佔 40%」的出處。數字要對，講的事也要對。
    """
    body = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", body)   # 連結文字留下、URL 拿掉
    body = re.sub(r"`[^`]*`", "", body)
    out = []
    for m in re.finditer(rf"(\d[\d,，]*(?:\.\d+)?)\s*({UNIT})", body):
        num, unit = norm(m.group(1)), m.group(2)
        val = float(num) if num.replace(".", "", 1).isdigit() else 0.0
        if not (unit in ("%", "％") or val >= MIN_MEANINGFUL):
            continue
        lo, hi = max(0, m.start() - CTX_WINDOW), m.end() + CTX_WINDOW
        ctx = {w for w in CJK.findall(body[lo:hi]) if len(w) >= 2}
        out.append((f"{num}{unit}", num, ctx))
    return out


def hit_with_context(text: str, needle: str, ctx: set[str]) -> bool:
    """數字要在文中出現，且附近要有頁面那句話的語境詞，才算真的對上。"""
    if not ctx:
        return needle in text
    start = 0
    while (i := text.find(needle, start)) != -1:
        window = text[max(0, i - BOOK_WINDOW) : i + BOOK_WINDOW]
        if any(w in window for w in ctx):
            return True
        start = i + 1
    return False


def anchors_of(fm: str) -> list[tuple[str, str]]:
    return re.findall(
        r'book:\s*([\w-]+)\s*\n\s*label:[^\n]*\n\s*anchor:\s*"?([^"\n]+?)"?\s*$', fm, re.M
    )


_chapters: dict[str, dict[str, str]] = {}


def chapters_of(book: str) -> dict[str, str]:
    """book → {章節相對路徑: 正規化全文}。鍵是 docs/NN-xxx/ 這一層。"""
    if book in _chapters:
        return _chapters[book]
    repo = REPOS.get(book)
    out: dict[str, str] = {}
    if repo:
        root = repo / "site" / "content"
        for f in root.rglob("*.md"):
            parts = f.relative_to(root).parts
            if len(parts) < 2 or parts[0] != "docs":
                continue        # 站根的 _index.md 不是可掛的章
            key = f"docs/{parts[1]}/"
            out[key] = out.get(key, "") + norm(f.read_text(encoding="utf8", errors="ignore"))
    return _chapters.setdefault(book, out)


def text_under(book: str, anchor: str) -> str:
    """掛出去的 anchor 可能比章更深（docs/03-x/02-y/），要把底下全收。"""
    a = anchor.strip().strip('"').rstrip("/")
    repo = REPOS.get(book)
    if not repo:
        return ""
    root = repo / "site" / "content"
    d = root / a
    if d.is_dir():
        return norm("".join(f.read_text(encoding="utf8", errors="ignore") for f in d.rglob("*.md")))
    f = d.with_suffix(".md")
    return norm(f.read_text(encoding="utf8", errors="ignore")) if f.is_file() else ""


def scan_page(p: Path, station: str, rel: str):
    parts = p.read_text(encoding="utf8").split("---", 2)
    if len(parts) < 3:
        return None
    fm, body = parts[1], parts[2]
    pairs = anchors_of(fm)
    if not pairs:
        return None

    covered = "".join(text_under(b, a) for b, a in pairs)
    books = {b for b, _ in pairs}
    if not any(chapters_of(b) for b in books):
        return None

    # 判「有沒有缺口」用寬鬆比對（數字在 anchor 底下就算數），寧可少報；
    # 判「該掛哪一章」才要求語境相符，寧可準。
    skip = KNOWN_FALSE_POSITIVES.get((station, rel), set())
    gaps, unfound = [], []
    for shown, needle, ctx in numbers_of(body):
        if needle in covered or shown in skip:
            continue
        where = [
            (b, ch)
            for b in books
            for ch, txt in chapters_of(b).items()
            if hit_with_context(txt, needle, ctx)
        ]
        if where:
            gaps.append((shown, where))
        elif not any(needle in t for b in books for t in chapters_of(b).values()):
            unfound.append((shown, []))
        # 數字在書裡有、但語境對不上：可能是同號不同事，也可能是換句話說——存疑，不報
    if not gaps:
        return ([], unfound, pairs)

    # 計分兩條規矩：
    #   裸年份不計——「1990年」在任何一章都可能碰巧出現
    #   同一個數字只計一次——「21 個秘訣」在一頁裡出現十遍不代表十個證據
    hits: dict = defaultdict(set)
    for shown, where in gaps:
        if YEAR.match(shown):
            continue
        for b, ch in where:
            hits[(b, ch)].add(shown)
    score = Counter({k: len(v) for k, v in hits.items()})
    return ([(s, w) for s, w in gaps], unfound, pairs, score)


def main() -> None:
    only = sys.argv[1] if len(sys.argv) > 1 else None
    stations = [NOTES / only] if only else sorted(NOTES.glob("*-note"))

    rows = []
    unfound_n = 0
    for st in stations:
        cdir = st / "src/content/concepts"
        if not cdir.is_dir():
            continue
        for p in sorted(cdir.rglob("*.md")):
            if p.stem == "_index":
                continue
            r = scan_page(p, st.name, str(p.relative_to(cdir)))
            if not r:
                continue
            unfound_n += len(r[1])
            if len(r) == 4 and r[0]:
                rows.append((st.name, p, r[0], r[2], r[3]))

    # 分層：建議章被 ≥2 個不同的非年份數字命中才算證據充分
    strong = [r for r in rows if r[4] and r[4].most_common(1)[0][1] >= 2]
    weak = [r for r in rows if r not in strong]
    strong.sort(key=lambda r: -r[4].most_common(1)[0][1])

    lines = [
        "# ANCHOR 覆蓋不足",
        "",
        "由 `tools/export-anchor-gaps.py` 產生。判準：頁面正文用到的**具名數字**"
        "（金額、百分比、年份、人次⋯⋯）在它 `furtherReading` 掛的那本書裡找得到，"
        "卻不在掛出去的 anchor 章節底下——讀者點「延伸閱讀」會落在找不到內容的章。",
        "",
        f"- 證據充分（同一章被 ≥2 個非年份數字命中）：**{len(strong)}** 頁",
        f"- 證據單薄（只有一個數字，或全靠裸年份）：{len(weak)} 頁——裸年份如「1990年」"
        "在任何一章都可能碰巧出現，不足以當證據，列在後面備查。",
        f"- 另有 {unfound_n} 筆數字在整本書摘裡查無。books-done 是摘要不是全文，"
        "全書才有的細節本來就不會進摘要，**這類不算違規**，只供抽查。",
        "",
        "修法兩種：建議章是現掛 anchor 的**祖章**→ 直接擴大；是別的子樹 → 另加一條"
        "`furtherReading`。「建議 anchor」附的標題取自該章 `_index.md`，可直接當 label。",
        "",
    ]

    def render(group: list) -> None:
        for st, p, gaps, pairs, score in group:
            rel = p.relative_to(NOTES / st / "src/content/concepts")
            lines.append(f"## {st} / {rel}")
            lines.append("")
            lines.append("- 現掛：" + "、".join(f"`{b}` → `{a}`" for b, a in pairs))
            sug = []
            for (b, ch), n in score.most_common(MAX_SUGGEST):
                t = chapter_title(b, ch)
                widen = any(cb == b and ca.strip("/").startswith(ch.strip("/")) for cb, ca in pairs)
                sug.append(
                    f"`{b}` → `{ch}`"
                    + (f"「{t}」" if t else "")
                    + f"（{n} 個數字{'、擴大' if widen else ''}）"
                )
            if sug:
                lines.append("- 建議 anchor：" + "、".join(sug))
            lines.append("- 落空數字：" + "、".join(sorted({g[0] for g in gaps})))
            lines.append("")

    render(strong)
    if weak:
        lines += ["---", "", "# 證據單薄（備查，先不動）", ""]
        render(weak)

    text = stamp(
        "\n".join(lines),
        "tools/export-anchor-gaps.py",
        _dt.datetime.now().astimezone().isoformat(timespec="seconds"),
    )
    if only:
        print(text)
    else:
        OUT.write_text(text + "\n", encoding="utf8")
        print(
            f"→ {OUT}（證據充分 {len(strong)} 頁、證據單薄 {len(weak)} 頁、"
            f"書摘查無 {unfound_n} 筆）"
        )


main()
