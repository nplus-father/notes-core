#!/usr/bin/env python3
"""判層證據包：把「證據躺在 repo 裡」的那些書自動判掉，只留有爭議的給人（或高階模型）看。

**為什麼要有這支**：判層的依據多半本來就在資料裡，不需要模型讀完整本書才判得出來——
被幾個不同的頁引用、姊妹站有沒有收、盤點表的 group／note 怎麼寫。2026-08-24 首輪實測：
261 本「未挖」裡有 192 本是判過的決定，真正拿不準的大約五分之一。把 1031 本原封丟給
高階模型，是拿最貴的額度做查表。

**輸出兩份**：
  1. 自動判定（附證據與信心）——直接套進 bibliography.ts
  2. 爭議清單——證據不足或互相矛盾的，交給人裁決

**規則（順序有意義，第一個命中就停）**：
  A. 被 ≥3 個不同的頁引用            → spine  ：既成事實，站上自己的頁面已經投過票
  B. 被 1–2 頁引用                    → spine  ：已經在用了，只是還沒用開
  C. 姊妹站收了同一本且判 spine       → delegated：那站在挖，深挖歸它
  D. note／group 明講查閱體裁         → tool   ：合集、辭典、題庫、手冊
  E. 其餘                             → 爭議   ：零引用、沒人接、體裁不明

**這支不會自己改檔**——它只產 JSON 與報表。套用要另外跑，因為判層是決策紀錄，
要留得下「當時憑什麼這樣判」。

用法：
    tools/tier-evidence.py                    # 全部未判層的站
    tools/tier-evidence.py theology-note      # 指定站
    tools/tier-evidence.py --json             # 給程式吃
"""
import json
import os
import re
import sys

ROOT = os.environ.get("NOTES_ROOT") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CORE = os.path.join(ROOT, "notes-core", "src", "lib", "sites.ts")

# 查閱體裁的訊號詞。**只認「不可能是論說書」的那幾個**。
#
# 2026-08-24 實測：把「手冊」放進來，17 筆自動判定裡有 13 筆是誤判——
# 《今天很重要》《讓錢為你工作》《Obviously Awesome》都因為 note 寫了「操作手冊」
# 「實踐手冊」而被判成查閱型，但它們是不折不扣的論說書。
# **「手冊」在中文書名與行銷語裡是修辭，不是體裁**；「指南」「入門」同理。
#
# 判錯一本豁免，那個缺口就再也不會有人看見——所以這裡寧可少判、把書丟去爭議清單，
# 讓人看一眼。少判的成本是多一本要人看，誤判的成本是永久失去一本。
TOOL_WORDS = ("辭典", "字典", "詞典", "百科", "題庫", "圖鑑", "年鑑", "速查")


def sites_registry():
    """{key: slug}。delegatedTo 填的是 key，目錄名是 slug。"""
    if not os.path.exists(CORE):
        return {}
    src = open(CORE, encoding="utf-8").read()
    return {k: s for k, s in re.findall(r'\{\s*key:\s*"([^"]+)",\s*slug:\s*"([^"]+)"', src)}


def bibliography(station):
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
            out[slug] = {k: f(k) for k in ("title", "author", "status", "tier", "note", "group")}
    return out


def citations(station):
    """{slug: 散在幾個不同的頁}。頁數才是載重指標，次數不是——同一頁掛四個錨仍只撐一頁。"""
    pages = {}
    for sub in ("concepts", "problems"):
        base = os.path.join(ROOT, station, "src", "content", sub)
        for dirpath, _, files in os.walk(base):
            for fn in files:
                if not fn.endswith(".md") or fn == "_index.md":
                    continue
                path = os.path.join(dirpath, fn)
                txt = open(path, encoding="utf-8").read()
                for b in set(re.findall(r"^\s*-\s*book:\s*([\w\-.]+)", txt, re.M)):
                    pages.setdefault(b, set()).add(path)
    return {b: len(v) for b, v in pages.items()}


def build_index(stations):
    """全星系索引：每本書被哪些站收了、各判什麼層、被引幾頁。判 delegated 要靠它。"""
    idx = {}
    for st in stations:
        bib = bibliography(st)
        cit = citations(st)
        for slug, e in bib.items():
            idx.setdefault(slug, []).append(
                {"station": st, "tier": e.get("tier"), "pages": cit.get(slug, 0), "status": e.get("status")}
            )
    return idx


def judge(slug, entry, pages, index, self_station, key_by_slug):
    """回傳 (tier or None, 信心, 證據字串)。None＝有爭議，交給人。"""
    if pages >= 3:
        return "spine", "high", "站上 %d 個不同的頁引用它——既成事實" % pages
    if pages > 0:
        # 1–2 頁也判 spine，但要知道這代表什麼：**它只保證「這本書在站上有位置」，
        # 不保證它是領域正典。** 2026-08-24 全隊實測，577 筆 spine 裡有 449 筆只被 1 頁引用。
        # 這仍是安全的判定——spine 的承諾是「該有專屬概念頁」，而它已經被引用過，
        # 所以不會產生欠債（欠債＝判 spine 卻零引用）。誤判的方向是「多寫一頁」，
        # 不是「永久失去一本」，這正是判層紀律要的那個方向。
        return "spine", "high", "站上 %d 頁引用它，已經在用" % pages

    # 姊妹站在挖同一本 → 深挖歸它。要求那站判 spine **且真的有頁在引**，
    # 否則只是把債推給一個同樣沒動的站（那正是「漏接」的成因）。
    for other in index.get(slug, []):
        if other["station"] == self_station or other["status"] != "owned":
            continue
        if other["tier"] == "spine" and other["pages"] > 0:
            key = key_by_slug.get(other["station"])
            if key:
                return (
                    "delegated:" + key,
                    "high",
                    "%s 判 spine 且已開採 %d 頁" % (other["station"], other["pages"]),
                )

    blob = " ".join(filter(None, [entry.get("note"), entry.get("group"), entry.get("title")]))
    hit = [w for w in TOOL_WORDS if w in blob]
    if hit:
        return "tool", "medium", "體裁詞「%s」出現在 title/group/note" % "、".join(hit)

    return None, "low", "零引用、無姊妹站接手、體裁不明"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    reg = sites_registry()
    key_by_slug = {v: k for k, v in reg.items()}
    all_st = sorted(d for d in os.listdir(ROOT) if d.endswith("-note") and os.path.isdir(os.path.join(ROOT, d)))
    index = build_index(all_st)

    targets = args or [
        st
        for st in all_st
        if any(e.get("status") == "owned" and not e.get("tier") for e in bibliography(st).values())
    ]

    result = {}
    for st in targets:
        bib = bibliography(st)
        cit = citations(st)
        auto, contested = [], []
        for slug, e in sorted(bib.items()):
            if e.get("status") != "owned" or e.get("tier"):
                continue
            tier, conf, why = judge(slug, e, cit.get(slug, 0), index, st, key_by_slug)
            row = {"slug": slug, "title": e.get("title"), "author": e.get("author"),
                   "pages": cit.get(slug, 0), "note": e.get("note"), "group": e.get("group"),
                   "why": why, "confidence": conf}
            if tier:
                row["tier"] = tier
                auto.append(row)
            else:
                contested.append(row)
        if auto or contested:
            result[st] = {"auto": auto, "contested": contested}

    if "--json" in sys.argv:
        json.dump(result, sys.stdout, ensure_ascii=False, indent=1)
        return

    ta = sum(len(v["auto"]) for v in result.values())
    tc = sum(len(v["contested"]) for v in result.values())
    print("%-28s%8s%8s%8s" % ("station", "未判層", "可自動", "待裁決"))
    for st, v in sorted(result.items(), key=lambda kv: -len(kv[1]["contested"])):
        print("%-28s%8d%8d%8d" % (st, len(v["auto"]) + len(v["contested"]), len(v["auto"]), len(v["contested"])))
    print("%-28s%8d%8d%8d" % ("TOTAL", ta + tc, ta, tc))
    print()
    print("可自動判掉 %.0f%%；其餘 %d 本要人裁決（見 --json 的 contested）。" % (ta / max(ta + tc, 1) * 100, tc))
    if "--detail" in sys.argv:
        for st, v in sorted(result.items()):
            if not v["contested"]:
                continue
            print("\n=== %s 待裁決 %d 本 ===" % (st, len(v["contested"])))
            for r in v["contested"]:
                print("   %-42s %s" % (r["title"][:40] if r["title"] else r["slug"], r["note"] or "（無 note）"))


if __name__ == "__main__":
    main()
