#!/usr/bin/env python3
"""判層履約稽核：檢查每本書的 tier 承諾有沒有兌現。

判層不是貼標籤，四層各自是一個承諾：

  spine      該有專屬概念頁        違約 → 真欠債
  support    guide 要一句帶到      違約 → 空頭支票
  tool       列進盤點表即可        恆真（體裁對不對只能人工看）
  delegated  深挖歸姊妹站          違約 → 漏接

**真欠債是「知道要做還沒做」，空頭支票與漏接是「以為做過了其實沒有」。**
後兩者才是會靜靜把缺口藏起來的那種——判錯一本脊梁只是多寫一頁，
判錯一本豁免，那個洞就再也不會有人看見。所以稽核的重點在豁免那一邊：
一個站豁免掉愈多書，愈該被檢查，而不是愈健康。

用法（在星系根目錄或任何地方都可以）：
    notes-core/tools/tier-audit.py                # 全星系總表
    notes-core/tools/tier-audit.py --detail       # 附逐本違約清單
    notes-core/tools/tier-audit.py leadership-note writing-note
    notes-core/tools/tier-audit.py --json         # 給程式吃

NOTES_ROOT 可覆寫星系根目錄（預設＝本檔往上兩層）。
"""
import json
import os
import re
import sys

ROOT = os.environ.get("NOTES_ROOT") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CORE = os.path.join(ROOT, "notes-core", "src", "lib", "sites.ts")
TIERS = ("spine", "support", "tool", "delegated")


def stations():
    return sorted(d for d in os.listdir(ROOT) if d.endswith("-note") and os.path.isdir(os.path.join(ROOT, d)))


def site_registry():
    """{slug: key} 與 {key: slug}——delegatedTo 填的是 key，目錄名是 slug。"""
    if not os.path.exists(CORE):
        return {}, {}
    src = open(CORE, encoding="utf-8").read()
    pairs = re.findall(r'\{\s*key:\s*"([^"]+)",\s*slug:\s*"([^"]+)"', src)
    return {s: k for k, s in pairs}, {k: s for k, s in pairs}


def bibliography(station):
    """{slug: {title, original, status, tier, delegatedTo}}。"""
    p = os.path.join(ROOT, station, "src", "data", "bibliography.ts")
    if not os.path.exists(p):
        return {}
    src = open(p, encoding="utf-8").read()
    out = {}
    for m in re.finditer(r"\{[^{}]*?\btitle:[^{}]*?\}", src, re.S):
        blk = m.group(0)

        def f(k):
            mm = re.search(r'\b%s:\s*"([^"]*)"' % k, blk)
            return mm.group(1) if mm else None

        slug = f("slug")
        if slug:
            out[slug] = {k: f(k) for k in ("title", "original", "status", "tier", "delegatedTo")}
    return out


def citations(station):
    """每本書被 concepts／problems 引用幾次，以及**散在幾個不同的頁**。
    回傳 {slug: (次數, 頁數)}。guide 不計——脊梁的債要用概念頁還，導覽提再多次都不算。

    **頁數才是判「載重」的指標，次數不是。** 同一頁掛四個 anchor 就是四次，
    但那本書仍然只撐著一頁。2026-08-24 用「次數 ≥3」當既成事實門檻，12 筆警報裡
    有 9 筆是這種假象（covey 的語錄 7 次全在同一頁、taleb 的動態避險 3 次全在同一頁）。
    改看頁數之後，剩下的才是真的在跨頁承重。
    """
    n, pages = {}, {}
    for sub in ("concepts", "problems"):
        base = os.path.join(ROOT, station, "src", "content", sub)
        for dirpath, _, files in os.walk(base):
            for fn in files:
                if not fn.endswith(".md") or fn == "_index.md":
                    continue
                path = os.path.join(dirpath, fn)
                txt = open(path, encoding="utf-8").read()
                for b in re.findall(r"^\s*-\s*book:\s*([\w\-.]+)", txt, re.M):
                    n[b] = n.get(b, 0) + 1
                    pages.setdefault(b, set()).add(path)
    return {b: (c, len(pages.get(b, ()))) for b, c in n.items()}


def guide_lag(station):
    """導覽是不是落後於內容：curation.enrichedAt 比所有 guide 章節的 writtenAt 都新。

    還債會把導覽寫過時——第三章白紙黑字寫著「這本還沒挖」，而那本書昨天剛開了頁。
    2026-08-24 那輪 enrich 三個站獨立回報同一件事，所以把它變成常駐檢查：
    兩邊都是日期，這是少數機器判得準的內容一致性訊號。

    **限制：同日打平就抓不到。** 導覽若在同一天因為別的原因被動過（改一個標籤、修一個
    計數），writtenAt 會跟 enrichedAt 一樣新，這裡就報「—」，但正文可能還寫著那本書
    「未挖」。所以「—」只代表日期沒落後，不代表內容同步過——動過 tier 或補過頁之後，
    導覽第三章仍然要人眼讀一遍。
    """
    cfg = os.path.join(ROOT, station, "src", "site.config.ts")
    if not os.path.exists(cfg):
        return None
    m = re.search(r'enrichedAt:\s*"(\d{4}-\d{2}-\d{2})"', open(cfg, encoding="utf-8").read())
    if not m:
        return None
    enriched = m.group(1)
    base = os.path.join(ROOT, station, "src", "content", "guide")
    written = []
    for dirpath, _, files in os.walk(base):
        for fn in files:
            if fn.endswith(".md"):
                w = re.search(r'^writtenAt:\s*"?(\d{4}-\d{2}-\d{2})', open(os.path.join(dirpath, fn), encoding="utf-8").read(), re.M)
                if w:
                    written.append(w.group(1))
    if not written:
        return None
    newest = max(written)
    return (newest, enriched) if newest < enriched else None


def guide_reach(station):
    """guide 碰過哪些書：furtherReading 的 slug（強訊號）＋內文（弱訊號）。

    也收 overview.ts——首頁總覽是讀者最先看到的導覽文字，同樣會帶著過期的分層說法。
    2026-08-24 那輪只改第三章，結果 bogle／collins／damodaran 的首頁還寫著舊的
    「兩根脊梁、兩根支架」，跟改好的第三章互相打架。
    """
    base = os.path.join(ROOT, station, "src", "content", "guide")
    slugs, prose = set(), []
    ov = os.path.join(ROOT, station, "src", "data", "overview.ts")
    if os.path.exists(ov):
        prose.append(open(ov, encoding="utf-8").read())
    for dirpath, _, files in os.walk(base):
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            txt = open(os.path.join(dirpath, fn), encoding="utf-8").read()
            slugs.update(re.findall(r"^\s*-\s*book:\s*([\w\-.]+)", txt, re.M))
            parts = txt.split("---", 2)
            prose.append(parts[2] if len(parts) >= 3 else txt)
    return slugs, "\n".join(prose)


def name_candidates(entry):
    """書名在導覽裡可能長什麼樣。

    盤點表的 title 常把中英名串在一起（「Head First Design Patterns 深入淺出設計模式」），
    導覽行文卻只用其中一半——拿整串去比對會漏掉，把談了整段的書誤判成空頭支票。
    所以要把雙語名拆成可獨立辨識的片段。長度下限是防誤命中：太短的片段
    （「重構」「高手」「Design」）會在散文裡到處撞到，反而把真的空頭支票蓋掉。
    """
    out = set()
    for key in ("title", "original"):
        t = (entry.get(key) or "").strip()
        if not t:
            continue
        out.add(t)
        out.add(re.split(r"[:：（(]", t)[0].strip())  # 去副標
        out.update(r.strip(" ,.:-—") for r in re.findall(r"[A-Za-z][A-Za-z0-9 '’&.,:!?\-]{9,}", t))
        out.update(re.findall(r"[一-鿿]{4,}", t))
    return {c for c in out if len(c) >= 4}


# 導覽第三章寫判層的句式很固定：「**書名（作者，年）**判**工具書層，不排隊**」，
# 可以拿來跟 tier 資料對帳——散文與資料不一致，讀者會看到兩個互相矛盾的說法。
#
# **只認「工具書」與「姊妹站分工」兩個詞。** 「支架」「脊梁」看起來也能用，實際上不行：
# 那批導覽寫在判層體系定案之前，各站的用法不一樣。cloud-infra 的第三章把「支架」
# 當結構承重件用（「借來的支架換自己的柱子」＝那本書該撐起一頁），語意接近 spine，
# 和判層裡「支架＝一句帶到就好」正好相反。拿它對帳會整站誤報。
PROSE_TIER = [
    ("tool", ("工具書層", "工具書", "查閱型")),
    ("delegated", ("姊妹站分工", "姊妹站")),
]


def prose_tier(entry, prose, cands):
    """導覽散文替這本書標的層（找不到或含糊就回 None）。

    只認「**書名（作者，年）**判**支架待挖**」這個句式：書名後緊接著「判」，
    標籤詞就在那個「判」的後面十幾個字內。放寬一點就會把比喻吃進來——
    「Kubernetes in Action 仍在待挖區——借來的支架換自己的柱子」裡的「支架」
    不是在標這本書的層，而寬鬆版把它當成了判層句。

    **它仍會因為鄰近而誤報**：一句話裡連續列出幾本不同層的書，或在書名後緊接
    「判給姊妹站」的子句，都可能讓標籤黏到錯的書上。2026-08-24 有代理為了讓這欄歸零
    而去拆句子——**那是本末倒置**。這一欄報出來的東西要人眼確認；確認是誤報就留著，
    不要為了配合檢查改寫文風。
    """
    found = set()
    for cand in cands:
        start = 0
        while True:
            i = prose.find(cand, start)
            if i < 0:
                break
            start = i + len(cand)
            head = prose[start:start + 25]
            j = head.find("判")
            if j < 0:
                continue
            seg = prose[start + j:start + j + 16]
            for tier, words in PROSE_TIER:
                if any(w in seg for w in words):
                    found.add(tier)
    return found.pop() if len(found) == 1 else None


def touched(slug, entry, gslugs, prose):
    if slug in gslugs:
        return "furtherReading"
    if "/%s/" % slug in prose:
        return "連結"
    for cand in name_candidates(entry):
        if cand in prose:
            return "內文"
    return None


def audit(only=None):
    slug2key, key2slug = site_registry()
    all_st = stations()
    cite_cache, bib_cache = {}, {}

    def cites(st):
        if st not in cite_cache:
            cite_cache[st] = citations(st)
        return cite_cache[st]

    def bib(st):
        if st not in bib_cache:
            bib_cache[st] = bibliography(st)
        return bib_cache[st]

    rows = []
    for st in all_st:
        if only and st not in only:
            continue
        entries = bib(st)
        owned = {s: e for s, e in entries.items() if e.get("status") == "owned"}
        if not owned:
            continue
        gslugs, prose = guide_reach(st)
        has_guide = bool(gslugs or prose.strip())
        n = cites(st)
        counts = dict.fromkeys(TIERS, 0)
        untiered, debt, empty, dropped, conflict, mismatch = [], [], [], [], [], []
        for slug, e in owned.items():
            t = e.get("tier")
            title = e.get("title") or slug
            c, npages = n.get(slug, (0, 0))
            if t not in TIERS:
                untiered.append((slug, title))
                continue
            counts[t] += 1
            if t == "spine" and c == 0:
                debt.append((slug, title))
            # 載重看「散在幾頁」，不看次數——同頁多 anchor 不代表跨頁承重。
            if t != "spine" and npages >= 3:
                conflict.append((slug, title, npages, t))
            if has_guide:
                pt = prose_tier(e, prose, name_candidates(e))
                if pt and pt != t:
                    mismatch.append((slug, title, pt, t))
            if t == "support" and has_guide and not touched(slug, e, gslugs, prose):
                # 完全隱形＝guide 沒提、概念頁也沒引：這本書在站上只剩盤點表那一行
                empty.append((slug, title, "完全隱形" if c == 0 else "概念頁引用 %d 次" % c))
            if t == "delegated":
                to = e.get("delegatedTo")
                tgt = key2slug.get(to)
                te = bib(tgt).get(slug) if tgt and tgt in all_st else None
                tc = cites(tgt).get(slug, (0, 0))[0] if tgt and tgt in all_st else 0
                tt = (te or {}).get("tier")
                if not tgt or tgt not in all_st:
                    dropped.append((slug, title, to, "姊妹站不存在", "壞標籤"))
                elif not te or te.get("status") != "owned":
                    dropped.append((slug, title, to, "該站根本沒收這本", "真漏接"))
                elif tc == 0 and tt != "spine":
                    if tt in ("tool", "support"):
                        # 兩站都判「不深挖」——本站不該說「歸那站」，該直接標成同一層
                        dropped.append((slug, title, to, "該站也判 %s，兩邊都不會挖" % tt, "標籤下錯"))
                    elif not tt:
                        # 姊妹站還沒判層（多半是還沒寫導覽）——承諾未到期，不是違約，
                        # 但要記著：那站判層時如果也判非 spine，這裡就會翻成標籤下錯。
                        dropped.append((slug, title, to, "該站尚未判層，承諾未到期", "待姊妹站"))
                    else:
                        dropped.append((slug, title, to, "該站判 %s 但零引用" % tt, "真漏接"))
        lag = guide_lag(st) if has_guide else None
        tot = len(owned)
        rows.append(
            {
                "station": st, "hasGuide": has_guide, "owned": tot, "counts": counts,
                "excused": tot - counts["spine"] - len(untiered),
                "untiered": untiered, "debt": debt, "empty": empty,
                "dropped": dropped, "conflict": conflict, "mismatch": mismatch, "lag": lag,
            }
        )
    return rows


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    detail = "--detail" in sys.argv
    rows = audit(args or None)
    if "--json" in sys.argv:
        json.dump(rows, sys.stdout, ensure_ascii=False, indent=1)
        return

    def missed(r):
        """真漏接：不含「待姊妹站」。

        姊妹站還沒寫導覽＝還沒判層，那本書的承諾根本還沒到期。把它算進違約
        欄，等於要求一個尚未開始的站先還債——那個數字會永遠掛在那裡，讀者
        看久了就不看了。--detail 仍會把它列出來，只是不計入。
        """
        return [d for d in r["dropped"] if d[4] != "待姊妹站"]

    def viol(r):
        return len(r["empty"]) + len(missed(r)) + len(r["untiered"]) + len(r["mismatch"])

    # 判層是 guide 帶出來的動作——沒寫過導覽的站還沒輪到，別讓它們稀釋數字。
    pending = [r for r in rows if not r["hasGuide"]]
    if "--all" not in sys.argv:
        rows = [r for r in rows if r["hasGuide"]]

    rows.sort(key=lambda r: -viol(r))
    hdr = ("station", "藏書", "豁免", "豁免率", "真欠債", "空頭支票", "漏接", "文資不符", "衝突", "未判層", "導覽落後")
    print("%-26s%5s%5s%7s%7s%9s%6s%9s%6s%7s%9s" % hdr)
    t = dict.fromkeys(("owned", "excused", "debt", "empty", "dropped", "conflict", "untiered", "mismatch"), 0)
    for r in rows:
        ratio = r["excused"] / r["owned"] * 100 if r["owned"] else 0
        print(
            "%-26s%5d%5d%6.0f%%%7d%9d%6d%9d%6d%7d%s%s"
            % (r["station"], r["owned"], r["excused"], ratio, len(r["debt"]), len(r["empty"]),
               len(missed(r)), len(r["mismatch"]), len(r["conflict"]), len(r["untiered"]),
               "  是" if r["lag"] else "   —", " ⚠" if viol(r) else "")
        )
        t["owned"] += r["owned"]; t["excused"] += r["excused"]
        for k in ("debt", "empty", "conflict", "untiered", "mismatch"):
            t[k] += len(r[k])
        t["dropped"] += len(missed(r))
    print(
        "%-26s%5d%5d%6.0f%%%7d%9d%6d%9d%6d%7d"
        % ("TOTAL", t["owned"], t["excused"], t["excused"] / max(t["owned"], 1) * 100,
           t["debt"], t["empty"], t["dropped"], t["mismatch"], t["conflict"], t["untiered"])
    )

    if pending and "--all" not in sys.argv:
        print(
            "\n另有 %d 站尚無導覽、共 %d 本未判層（判層跟著 /note-guide 走，還沒輪到）——加 --all 一併列出。"
            % (len(pending), sum(r["owned"] for r in pending))
        )

    if not detail:
        print("\n（加 --detail 看逐本違約清單）")
        return

    def section(title, note, pick, fmt):
        print("\n\n=== %s ===" % title)
        print(note)
        for r in rows:
            items = pick(r)
            if items:
                print("\n[%s]" % r["station"])
                for it in items:
                    print("  - " + fmt(it))

    section(
        "空頭支票：判 support，卻連 guide 都沒提到",
        "support 的承諾是「導覽一句帶到」。沒提＝這本書判了不挖、也沒人介紹過它，等於默默消失。",
        lambda r: r["empty"], lambda it: "%s  [%s]  (%s)" % (it[1], it[2], it[0]),
    )
    section(
        "漏接：判 delegated，姊妹站卻沒接住",
        "標籤下錯＝兩站都判不深挖，本站該把它改成同一層而不是說「歸那站」；真漏接＝那站根本沒收。",
        lambda r: r["dropped"], lambda it: "[%s] %s → %s 站：%s" % (it[4], it[1], it[2], it[3]),
    )
    print("\n導覽落後＝enrichedAt 比所有 guide 章節的 writtenAt 都新：內容補過了，策展層還在講舊帳。"
          "不是 gate（補內容本來就會領先），但那是 /note-guide 的待辦。")

    section(
        "文資不符：導覽散文寫的層，和 tier 資料不一樣",
        "讀者會看到兩個互相矛盾的說法。改資料還是改散文都行，但要一致。",
        lambda r: r["mismatch"], lambda it: "%s：導覽說 %s，資料是 %s" % (it[1], it[2], it[3]),
    )
    section(
        "既成事實衝突：被 ≥3 個不同的頁引用，卻判成非脊梁",
        "散在多頁＝它在跨頁承重，站上自己的頁面已經投過票了。集中在一兩頁的書不算——"
        "那是那一頁的素材，判查閱型完全誠實。",
        lambda r: r["conflict"], lambda it: "%s（散在 %d 頁 → 判 %s）" % (it[1], it[2], it[3]),
    )
    section(
        "未判層：owned 但沒有 tier 欄",
        "判層是決策紀錄，缺一本就是缺一個決定。",
        lambda r: r["untiered"], lambda it: "%s  (%s)" % (it[1], it[0]),
    )
    section(
        "真欠債：判 spine 卻零引用",
        "唯一「知道要做還沒做」的一類——下一輪 enrich 的現成材料。",
        lambda r: r["debt"], lambda it: "%s  (%s)" % (it[1], it[0]),
    )


if __name__ == "__main__":
    main()
