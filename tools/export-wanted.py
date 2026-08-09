#!/usr/bin/env python3
"""把全星系 bibliography 的 `wanted` 匯出成一張採購清單（docs/WANTED-BOOKS.md）。

用法：
    notes-core/tools/export-wanted.py            # 寫進 notes-core/docs/WANTED-BOOKS.md
    notes-core/tools/export-wanted.py -          # 印到 stdout

星系根目錄（放所有 -note 站的容器目錄）預設推導成 tools/../..；佈局不同時用
NOTES_ROOT= 覆寫，與 new-note.sh / bump-notes-core.sh 同慣例。

**英文書名怎麼來的**（各站的欄位慣例不統一，這裡歸一）：
  1. `original` 若含 3 個以上拉丁字母就用它——但 `original` 有時放的是簡中書名
     （吳軍）、日文原名（ロジカル・シンキング）或說明文字（萬維鋼那筆寫「簡中版；
     繁中版書名《高手量子力學》」），那些不算英文名。
  2. 否則看 `title`：整串無 CJK 就整串用；「English 中文」混寫就取 CJK 前的前綴。
  3. 都不成立＝華文／日文原著，照原書名列，另立一節。

**去重**用「主標」（冒號前）比對，因為同一本書各站寫法長短不一（Flow 有站寫
`Flow`、有站寫 `Flow: The Psychology of Optimal Experience`）。已核對過合併結果
不會誤併不同的書。

  漏併的坑（2026-08-09）：`title` 的「English 中文」慣例假設中文那半有 CJK 字，
  但**中譯書名本身是拉丁字母時就漏了**——《EQ》寫成 `Emotional Intelligence EQ`，
  latin_of 砍不掉 `EQ`，於是與另一站的 `Emotional Intelligence` 併不起來，
  「多站共等」少報一本。修法在資料側：那筆補 `original` 放純英文書名（thinking-note
  本來就這樣寫）。看到某書「應該多站都要卻只出現一次」時，先查這個。

  同一個坑的另一種形狀（2026-08-09）：`original` 放的是**拉丁／希臘原名**
  （spiritual-formation 的 `Confessiones`、`De Imitatione Christi`，philosophy 的
  `Politeia`、`Ethika Nikomacheia`），規則 1 照收，於是英文名整個對不上——兩個後果：
  跨站併不起來（《效法基督》theology 用英文名、spiritual-formation 用拉丁名，被算成
  兩本，「多站共等」漏報），portal 比對也對不上（《懺悔錄》早就有 `augustine-confessions`
  書站，卻在 wanted 躺到 2026-08-09 才發現，「先扣掉」那節一直回報 0 本）。
  拿 `original` 當英文名之前，先確認它真的是英文；覺得可疑就再拿 `title` 的拉丁前綴
  對一次 portal。

**「其實已經有書站」怎麼比對**（2026-08-07 全面改寫；舊版用 repo name 精確比對，
20 本裡漏報 16 本，兩個獨立故障各自都足以讓它全盲）：

  1. **資料源要現況，不要快照。** 站台的 `repos.json` 是 build 時打 GitHub API 存
     下來 commit 進去的，落後好幾天很正常（漏報那次快照是 08-05、書是 08-07 建的）。
     所以預設 `gh repo list` 直接問 GitHub；問不到才退回快照，並在輸出頂端標明
     資料源與落後天數——**證據過期就要吵**，不能安靜地回報「0 本已收錄」。
  2. **比對鍵用 description 的書名欄，不是 repo name。** 這些 repo 的描述是結構化的
     `書名 | 作者 | 簡介`；書名是書的身分，repo name 只是命名慣例，會砍冠詞
     （`the-war-of-art` → `war-of-art`）、加作者前綴（`minto-pyramid-principle`）。
     兩邊都正規化（小寫、砍冒號後副標、砍冠詞、去標點）之後，只認**完全相同**，
     外加一條「作者前綴」例外，且**只能拿書名欄套**——repo name 的作者前綴反而是
     反指標（`kostolany-confessions` 這樣命名，正是為了跟奧古斯丁的《懺悔錄》區隔）。
  3. **同名不同書列 NAME_COLLISIONS**：《Biblical Theology》Vos ≠ Goldingay、
     《Christian Theology》麥葛福 ≠ Erickson、《Servant Leadership》Greenleaf 1977
     原典 ≠ Larry W. Boone 的同名教科書（2026-08-08 加）——命中也不算已收錄。
     這類撞名在「原典很有名、後人拿同一個書名寫教科書」時特別容易發生，回填前
     務必逐筆核對 description 的作者欄。
  4. **改名／轉寫沒有演算法可解，列 ALIASES**：英美版書名不同（Between Two Worlds
     ＝ I Believe in Preaching）、華文書 repo 用英文轉寫（浪潮之巔 ＝ on-top-of-tides）。
"""

import collections
import io
import json
import os
import re
import subprocess
import sys
from pathlib import Path

# ── 手選 Top 20：全檔唯一的人工區塊 ──────────────────────────────
# 366 筆太長，這是從裡面挑出來的採購順序。挑選準則，依序：
#   1. **歸零槓桿（2026-08-09 起升為準則①）**——優先收「還差 1–2 本就收齊」的站所缺的書。
#      理由：一個站的書單歸零，缺書就不再是它進 note-check --enrich 深化的瓶頸；把採購火力集中在
#      快到終點的站，換到的是「多一個站可以開始深化」，而不是「多一本好書躺在清單上」。
#      腳本自動算（見 near_zero / leverage 與輸出的「快歸零的站」那節），不必手數。
#   2. 多站共等——收一本補多站（下面「優先收」那節自動算出來的那批）
#   3. 站主自己在該筆的 `note` 裡標了「最大／頭號缺口」
#   4. portal 驗證的 anchor 深度——nplus.wiki 上**已經建成幾本**回指它的書站
#      （同作者的書櫃已有幾本／同一條線的衍生書有幾本），收了既有概念頁才掛得上
#      anchor（見 SOURCING-DEBT.md）。書櫃愈深、原典愈缺，排愈前面
#   5. 同等重要時，薄的、有繁中在版的排前面——排序即建議消化順序
# 下面「為何排這裡」的 portal 數字是實查 nplus-father／Andrewnplus 的書 repo 得到的
# （作者書櫃本數、同一條線的衍生書數、各站概念頁引用處數）；portal 長大之後數字會漂，
# 改這裡時順手重查一次——`/note-wanted` 每次重挑都會重查。
# key = 該書英文主標（冒號前）的 slug，也就是 by_main 的鍵；華文原著用 "cjk::原書名"。
# 不必手動維護「收到了沒」：key 對不上 wanted 時腳本會自己在表裡標出來。
TOP20 = [
    ("emotional-intelligence", "**多站共等**（準則①）——life-meaning 與 thinking 兩站都掛著它，也是腳本自己算得出來的那一本；portal 的 Goleman **只有 1 本、還是合著的** Primal Leadership，1995 年那本把 EQ 帶進大眾語彙的原典不在；「情緒智商」站內 11 處跨 5 站、「情緒智力」4 處跨 2 站；繁中《EQ》在版"),
    ("the-imitation-of-christ", "**另一本多站共等**（準則①）：theology 與 spiritual-formation 兩站都掛著它——腳本沒併起來，因為 sf 那筆的 `original` 放的是拉丁原名 `De Imitatione Christi`（見檔頭 2026-08-09 的漏併坑），下方完整清單可見兩筆；portal 的**中世紀靈修原典整片掛零**——金碧士、大德蘭、十架約翰、不知之雲、勞倫斯弟兄一本都沒有，只有 Foster《Celebration of Discipline》這類當代轉述；willard 站的 profile 明列「Thomas à Kempis 與古典靈修傳統」是他的素材庫，源頭卻不在；薄、繁中多種在版"),
    ("market-sense-and-nonsense", "schwager 站 owned 9／wanted 1——**收了就歸零**；portal 的 9 個 Schwager repo 全是 Market Wizards 訪談線（外加一本技術分析入門），缺的是他唯一一本正面清算投資圈流行謬誤的實證之作；「效率市場」站內 16 處、10 個檔案、跨 3 站（investing 5、schwager 3、bogle 2），三站都在談卻沒有原典可掛；有繁中《市場真相》"),
    ("cjk::你有你的計劃，世界另有計劃", "wan-weigang 站 owned 10／wanted 1——**收了就歸零**；portal 已有 11 個萬維鋼 repo，而站主自註這本「原列在建議閱讀路徑卻沒有對應書站」——閱讀路徑現在是斷的，收它是把既有的路走通，不是開新路"),
    ("servant-leadership", "leadership 站 owned 95／wanted 1——**全星系最深的站書櫃，只差這一本就歸零**；portal 的 Greenleaf **只有 1 本**（晚年文集 The Power of Servant-Leadership），1977 原典不在，而下游整片（Maxwell 14 本、Kouzes、Bennis、Kotter）全掛在它上面。注意 portal 的 `servant-leadership` repo 是 Larry W. Boone 的同名教科書，不是本書（見 NAME_COLLISIONS）"),
    ("the-everlasting-man", "portal 只有 2 本切斯特頓（Orthodoxy、What's Wrong with the World）；「切斯特頓」站內 11 處、6 個檔案、跨 3 站（lewis、theology、design），而 portal 13 本路易斯那整個書櫃的歸信轉捩點正是這一本——收了才接得起來；薄、有繁中《永恆的人》"),
    ("insight", "「自我覺察」站內 40 處、**跨 11 站**（behaviour-interview 6、fromm 4、startup 3、growth 3、tools、science、maxwell、life-meaning、leadership、image-style、covey），而 portal **沒有任何一本以自我覺察為主題的書**、Eurich 本人也掛零——橫跨最廣卻完全沒有原典可掛的概念；薄、有繁中《洞察》"),
    ("principle-centered-leadership", "covey 站 owned 8／wanted 2（80%，是幾個小而緊的站之一）；portal 的柯維本人著作 6 本全是個人層次（七個習慣、第 8 個習慣、與時間有約…），缺的正是把原則中心從個人推到**組織**層次的這一本——「原則中心」站內 4 處跨 2 站，轉折點沒有出處"),
    ("trading-in-the-zone", "portal 的 Mark Douglas **只有前作** The Disciplined Trader，缺這本被當成交易心理標準讀物的成熟之作；「交易心理」站內 12 處、7 個檔案，橫跨 investing 與 schwager 兩站，兩站的概念頁都指著它"),
    ("advanced-selling-strategies", "portal 已有 34 本 Brian Tracy——**全星系最深的作者書櫃**，而 tracy 站 owned 34／wanted 2；銷售線上已有 The Psychology of Selling、Sales Management、Negotiation 三本，缺的正是大客戶與關係銷售這一層進階正典"),
    ("the-divine-conspiracy-continued", "portal 已有 7 本魏樂德，《神聖的密謀》本傳在、續篇不在（注意兩者是不同書，別讓比對誤併）；天國福音延伸到職場與公共領域"),
    ("after-you-believe-virtue-reborn", "nt-wright 是**第二淺的站**（owned 8／wanted 7，53%）；portal 的 8 本賴特裡，普及三部曲已有 Simply Christian 與 Surprised by Hope，**就缺這本收尾的**——系列缺一本，補起來最划算；有繁中《信主了，然後呢？》"),
    ("being-mortal", "「臨終」站內 48 處、19 個檔案、**跨 13 站**（nouwen、theology、peck、design、de-botton、willard、spiritual-formation、relationships、personal-finance、life-meaning、growth、covey、biblical-studies），另有「善終」12 處跨 4 站；portal 的 Gawande **只有 The Checklist Manifesto**，善終這條線一本都沒有；有繁中《凝視死亡》"),
    ("kanban", "portal 只有衍生的 Kanban in Action，沒有 Anderson 2010 的原典；「看板」站內 67 處、22 個檔案、跨 8 站，「限制在製品」21 處、WIP 86 處——理論來源全靠二手轉述"),
    ("release-it", "portal 的 Nygard **掛零**，而「circuit breaker／斷路器」站內 22 處、16 個檔案、跨 4 站（cloud-infra 10、system-design 8、design-patterns 3、data-systems 1；covey 那 1 處是同名零件，已剔除），bulkhead 另 5 處跨 2 站——data-systems 的失效偵測頁甚至直接連到 system-design 的 `concepts/reliability/circuit-breaker/`，整套穩定性模式的命名來源沒有原典可掛；system-design 站 owned 21／wanted 4，cloud-infra 只有 65%"),
    ("out-of-the-crisis", "portal 的 Deming **掛零**；「戴明」6 處＋「Deming」5 處、各跨 4 站，品質管理與系統觀的源頭完全沒有出處；management 站 owned 44／wanted 3，是深站裡少數還缺源頭的一條線；有繁中《轉危為安》"),
    ("the-data-warehouse-toolkit", "data-systems 是**全星系最淺的站**（owned 9／wanted 10，僅 47%）；portal 的 Kimball **掛零**，「維度建模」站內只有 1 處——星型結構的正典不在，整個資料倉儲線沒有源頭可掛"),
    ("the-four-steps-to-the-epiphany", "startup 站 wanted 11 本、是缺口最深的主題站之一；portal 的 Steve Blank **掛零**（唯一命中 Blank 的是 Blank-Edelman 的 Seeking SRE，不是他），而下游（Running Lean／Scaling Lean、精實創業線）全從顧客開發長出來——源頭不在，「顧客開發」站內只剩 2 處孤證"),
    ("the-body-keeps-the-score", "「創傷」是全星系橫跨最廣的概念之一——38 處、20 個檔案、**跨 10 站**（growth、history、life-meaning、navarro、peterson、relationships、taleb、theology、thinking、wellness），而 portal 的 van der Kolk **掛零**，這片引用沒有任何原典可掛；有繁中《心靈的傷，身體會記住》，厚，排後段"),
    ("the-chronicles-of-narnia", "lewis 站 owned 13／wanted 1——**收了就歸零**；portal 已有 13 本路易斯而納尼亞掛零，「納尼亞」站內 4 處跨 3 站（lewis、keller、biblical-studies）卻無處可掛；七部曲，最厚，壓軸慢啃"),
]

NOTES_ROOT = Path(os.environ.get("NOTES_ROOT") or Path(__file__).resolve().parents[2])
PORTAL_REPOS = NOTES_ROOT / ".." / "sites" / "nplus-father.github.io" / "src" / "data" / "repos.json"
OUT = Path(__file__).resolve().parents[1] / "docs" / "WANTED-BOOKS.md"
PORTAL_OWNERS = ("nplus-father", "Andrewnplus")
SNAPSHOT_STALE_DAYS = 2  # 退回快照時，超過這個天數就在輸出裡吵

# 書名對不上 repo 的例外：英美版書名不同、華文書 repo 用英文轉寫。
# key = wanted 的 main slug（華文原著用 "cjk::原書名"），value = repo name。
ALIASES = {
    "between-two-worlds": "i-believe-in-preaching",
    "cjk::浪潮之巔": "on-top-of-tides",
}

# CJK 統一漢字、日文假名、CJK 標點與全形符號
NONLAT = re.compile(r"[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\u3000-\u303f\uff00-\uffef]")


def parse_bibliography(path):
    """各站的 bibliography.ts 是單層物件陣列，逐 block 抓欄位即可（不必真的解析 TS）。"""
    txt = path.read_text(encoding="utf-8")
    out = []
    for blk in re.findall(r"\{[^{}]*\}", txt):
        st = re.search(r'status:\s*"([^"]+)"', blk)
        if not st:
            continue
        field = lambda k: (re.search(rf'{k}:\s*"((?:[^"\\]|\\.)*)"', blk) or [None, None])[1]
        year = re.search(r"year:\s*(\d+)", blk)
        out.append(
            {
                "status": st.group(1),
                "title": field("title"),
                "original": field("original"),
                "note": field("note"),
                "slug": field("slug"),
                "year": int(year.group(1)) if year else None,
            }
        )
    return out


def latin_of(s):
    """取出可當英文書名的部分；拉丁字母少於 3 個就當作沒有。"""
    if not s:
        return None
    s = s.strip()
    if not NONLAT.search(s):
        return s if len(re.findall(r"[A-Za-z]", s)) >= 3 else None
    head = s[: NONLAT.search(s).start()].strip(" －—-（(:：,，")
    return head if len(re.findall(r"[A-Za-z]", head)) >= 3 else None


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")


def norm_title(s):
    """書名正規化：砍副標與冠詞、去標點——兩邊都過這關才能比。"""
    s = re.sub(r"[:：].*", "", s or "").lower()
    s = re.sub(r"[^a-z0-9一-鿿]+", " ", s).strip()
    return re.sub(r"^(the|a|an) ", "", s)


def load_portal():
    """回傳 (items, source, age_note)。先問 GitHub（權威），失敗才退回站台快照。

    快照是站台 build 時存下來 commit 進去的，落後幾天很正常——退回去用就一定要
    在輸出裡標明，否則「0 本已收錄」會被當成事實。
    """
    items = []
    for owner in PORTAL_OWNERS:
        try:
            out = subprocess.run(
                ["gh", "repo", "list", owner, "--limit", "2000", "--json", "name,description,repositoryTopics"],
                capture_output=True, text=True, timeout=120, check=True,
            ).stdout
        except (OSError, subprocess.SubprocessError):
            items = []
            break
        for r in json.loads(out):
            items.append(
                {
                    "name": r["name"],
                    "description": r.get("description") or "",
                    "topics": [t["name"] for t in (r.get("repositoryTopics") or [])],
                }
            )
    if items:
        return items, f"GitHub 現況（`gh repo list` {'／'.join(PORTAL_OWNERS)}，{len(items)} 個 repo）", ""

    snap = json.loads(PORTAL_REPOS.read_text(encoding="utf-8"))
    fetched = snap.get("fetchedAt", "")
    age = ""
    try:
        import datetime as _dt

        days = (_dt.datetime.now(_dt.timezone.utc) - _dt.datetime.fromisoformat(fetched.replace("Z", "+00:00"))).days
        if days >= SNAPSHOT_STALE_DAYS:
            age = f"⚠ **快照已經 {days} 天沒更新，這節可能漏報剛建好的書站**——`gh auth login` 後重跑才準。"
    except ValueError:
        age = "⚠ **快照時間戳讀不出來，無法判斷新舊。**"
    return (
        [{"name": i["name"], "description": i.get("description") or "", "topics": i.get("topics") or []} for i in snap["items"]],
        f"站台快照 `repos.json`（fetchedAt {fetched}，{len(snap['items'])} 個 repo）",
        age,
    )


def portal_index(items):
    """建書名索引：主鍵是 description 的書名欄（`書名 | 作者 | 簡介`），repo name 當備援。"""
    idx = {}
    for it in items:
        parts = [p.strip() for p in it["description"].split("|")]
        it["book_title"] = parts[0] if parts and parts[0] else it["name"]
        it["book_author"] = parts[1] if len(parts) >= 2 else ""
        for k in (norm_title(it["book_title"]), norm_title(it["name"].replace("-", " "))):
            if k:
                idx.setdefault(k, it)
    # 作者前綴只准拿「書名欄」套（見模組 docstring 第 2 點）
    title_idx = {norm_title(it["book_title"]): it for it in items if norm_title(it["book_title"])}
    return idx, title_idx


def main():
    rows = []
    counts = collections.Counter()
    for f in sorted(NOTES_ROOT.glob("*-note/src/data/bibliography.ts")):
        station = f.parts[len(NOTES_ROOT.parts)]
        for e in parse_bibliography(f):
            counts[e["status"]] += 1
            if e["status"] != "wanted":
                continue
            en = latin_of(e["original"]) or latin_of(e["title"])
            rows.append(
                {
                    **e,
                    "station": station,
                    "en": en,
                    # full = 完整書名的 slug（比對書 repo 用）；main = 主標（跨站去重用）
                    "full": slugify(en) if en else "cjk::" + (e["title"] or ""),
                    "main": slugify(en.split(":")[0]) if en else "cjk::" + (e["title"] or ""),
                }
            )

    owned_unique = len(
        {
            e["slug"]
            for f in NOTES_ROOT.glob("*-note/src/data/bibliography.ts")
            for e in parse_bibliography(f)
            if e["status"] == "owned" and e["slug"]
        }
    )

    portal_items, portal_source, portal_age = load_portal()
    repo_desc = {i["name"]: i["description"].strip() for i in portal_items}
    by_name = {i["name"]: i for i in portal_items}
    idx, title_idx = portal_index(portal_items)

    by_main = collections.defaultdict(list)
    for r in rows:
        by_main[r["main"]].append(r)
    by_station = collections.defaultdict(list)
    for r in rows:
        by_station[r["station"]].append(r)

    # 已核對過「同名但不同書」的撞名——比對命中也不算已有書站（想收的那本仍是 wanted）：
    #   change-your-thinking-change-your-life：repo 是 Joseph Murphy 的書，
    #   tracy-note 想收的是 Brian Tracy 2003 年的同名書（站上 note 亦註明）。
    #   how-to-be-a-high-school-superstar：repo 內容實為 How to Win at College
    #   （建站時譯名對應錯誤，見 SOURCING-DEBT.md），newport-note 想收的
    #   才是真正的 2010 年 Superstar。
    #   biblical-theology-goldingay：repo 是 Goldingay 的同名書，
    #   biblical-studies-note 想收的是 Vos 1948 年那本奠基之作。
    #   erickson-christian-theology：repo 是 Millard Erickson 的，
    #   theology-note 想收的是麥葛福（McGrath）的同名教科書。
    #   servant-leadership：repo 是 Larry W. Boone 的教科書式拆解，
    #   leadership-note 想收的是 Greenleaf 1977 年的原典（portal 只有他的晚年
    #   文集 power-of-servant-leadership，源頭本身仍缺）。
    NAME_COLLISIONS = {
        ("change-your-thinking-change-your-life", "tracy-note"),
        ("how-to-be-a-high-school-superstar", "newport-note"),
        ("biblical-theology-goldingay", "biblical-studies-note"),
        ("erickson-christian-theology", "theology-note"),
        ("servant-leadership", "leadership-note"),
    }

    def match_repo(r):
        """一筆 wanted 對得上哪個書 repo？對不上回 None——那才是真缺口。

        只認兩種命中，其餘一律當沒有：
          a. 正規化後**完全相同**（砍副標與冠詞之後，真的是同一個書名）。
          b. **作者前綴**：portal 書名 ＝ 作者姓氏 ＋ 想收的書名，且那個姓氏確實出現在
             description 的作者欄（`The Minto Pyramid Principle` ＝ `Pyramid Principle`）。
        曾經試過「token 連續包含」，結果 `Action` 吃掉 `Kubernetes in Action`、
        `Boundaries` 吃掉 `Boundaries with Kids`、`The Divine Conspiracy` 吃掉它的續集
        `Continued`——48 筆命中裡三十幾筆是假的。寧可漏報留在 wanted，也不要把還沒收的
        書從採購清單裡誤刪；漏掉的用 ALIASES 補。
        """
        alias = ALIASES.get(r["main"])
        if alias and alias in by_name:
            return by_name[alias]
        for key in (r["en"], r["title"]):
            k = norm_title(key)
            if not k:
                continue
            if k in idx:
                return idx[k]
            toks = k.split()
            for pk, it in title_idx.items():
                ptoks = pk.split()
                if len(ptoks) == len(toks) + 1 and ptoks[1:] == toks:
                    if ptoks[0] in norm_title(it["book_author"]).split():
                        return it
        return None

    existing = {}
    for r in rows:
        hit = match_repo(r)
        if hit and (hit["name"], r["station"]) not in NAME_COLLISIONS:
            r["repo"] = hit["name"]
            existing.setdefault(hit["name"], []).append(r)

    multi = sorted(
        (k for k, v in by_main.items() if len({r["station"] for r in v}) > 1),
        key=lambda k: (-len({r["station"] for r in by_main[k]}), k),
    )
    cjk_only = [r for r in rows if not r["en"]]

    # ── 歸零槓桿（2026-08-09 起是 TOP20 的準則①）
    # 「這本書收了，某個站的書單就收齊了」比「這本書很重要」更能決定採購順序：
    # 站書單歸零 → 該站可以進 note-check --enrich 深化，缺書不再是它的瓶頸。
    # 分母只算 owned + wanted——unavailable（絕版無中譯）與 skipped（刻意略過）
    # 是永久不可收，把它們算進去會讓永遠歸不了零的站看起來像差一點點。
    station_left = {}  # 站 → 還差幾本 wanted
    station_owned = {}
    for f in sorted(NOTES_ROOT.glob("*-note/src/data/bibliography.ts")):
        st = f.parts[len(NOTES_ROOT.parts)]
        es = parse_bibliography(f)
        station_left[st] = sum(1 for e in es if e["status"] == "wanted")
        station_owned[st] = sum(1 for e in es if e["status"] == "owned")

    def leverage(key):
        """這本書能讓「還差最少本」的那個站前進多少——回 (最小剩餘, 等它的站數)。"""
        v = by_main.get(key) or []
        lefts = [station_left.get(r["station"], 99) for r in v]
        return (min(lefts) if lefts else 99, len({r["station"] for r in v}))

    # 只差 1–2 本就歸零的站（採購清單的第一梯隊）
    near_zero = sorted(
        (st for st, n in station_left.items() if 0 < n <= 2),
        key=lambda st: (station_left[st], -station_owned[st], st),
    )

    esc = lambda s: (s or "").replace("|", "\\|").replace("\n", " ")

    def zh(r):
        """中譯／別名欄：title 與英文名重複的部分砍掉，只留中文那半。"""
        t = (r["title"] or "").strip()
        if r["en"] and t.lower().startswith(r["en"].lower()[:12]):
            return t[len(r["en"]) :].strip(" －—-（(:：")
        return "" if t == r["en"] else t

    o = io.StringIO()
    w = o.write
    w(f"""# 待收書單（bibliography `wanted` 全星系匯出）

**這份是什麼**：各 note 站 `src/data/bibliography.ts` 裡標成 `status: "wanted"` 的書，
全部匯出成一張採購清單。書名以**英文原名**為主，中譯附在後面。由
`notes-core/tools/export-wanted.py` 生成，**不要手改**——改各站的 bibliography 再重跑。

**已收錄比對的資料源**：{portal_source}。{portal_age}

""")

    w("## 先收這 20 本\n\n")
    w(
        f"整份 {len(rows)} 筆太長，這是從裡面挑出來的採購順序，也是建議的消化順序（薄的、"
        "起手容易的排前面）。**這節是全檔唯一的人工區塊**——要改請編 `export-wanted.py` 的 "
        "`TOP20`，不要改這裡。挑選準則依序：**①歸零槓桿——優先收「還差 1–2 本就收齊」"
        "的站所缺的書**（見下面「快歸零的站」那節，腳本自動算；站書單一歸零，缺書就不再是"
        "它進 `note-check --enrich` 深化的瓶頸） ②多站共等，收一本補多站 "
        "③站主自己在 `note` 裡標了「最大／頭號缺口」 ④portal 驗證的 anchor 深度——"
        "nplus.wiki 上已經建成幾本回指它的書站（同作者書櫃、同一條線的衍生書），"
        "書櫃愈深、原典愈缺就排愈前面（見 [SOURCING-DEBT.md](./SOURCING-DEBT.md)） "
        "⑤同等重要時，薄的、有繁中在版的排前面。\n\n"
        "「站」欄的 `(n)` ＝**收了這本之後該站還剩幾本**；`(0)` 就是這一本收了該站即歸零。\n\n"
        "「為何排這裡」的 portal 數字都是實查出來的（作者書櫃本數、同一條線的衍生書數、"
        "各站概念頁引用處數）；`/note-wanted` 每次重挑會一併重查。\n\n"
    )
    built = sum(1 for key, _ in TOP20 if any(r.get("repo") for r in by_main.get(key, [])))
    if built:
        w(
            f"> ⚠ **這 20 本裡有 {built} 本已經建好書站了**（下表標 ✅），代表這張採購清單該重挑——"
            "跑 `/note-wanted` 把 bibliography 回填成 `owned` 之後重排。\n\n"
        )
    w("| # | 英文書名 | 中譯 | 年 | 站 | 為何排這裡 |\n| --- | --- | --- | --- | --- | --- |\n")
    for i, (key, why) in enumerate(TOP20, 1):
        v = by_main.get(key)
        if not v:
            w(f"| {i} | ⚠ `{key}` 已不在 wanted（收到了或書名改了，請更新 `TOP20`） | | | | {esc(why)} |\n")
            continue
        best = max(v, key=lambda r: len(r["en"] or ""))
        name = best["en"] or f"（{best['title']}）"
        year = best["year"] or next((r["year"] for r in v if r["year"]), "")
        # 站欄帶「收了之後還剩幾本」，讓歸零槓桿在表上直接看得出來，不必翻下面那節。
        stations = sorted(
            f"{r['station'].replace('-note', '')}({max(0, station_left.get(r['station'], 0) - 1)})"
            for r in {r["station"]: r for r in v}.values()
        )
        repo = next((r["repo"] for r in v if r.get("repo")), None)
        flag = f"✅ 已建站 `{repo}`——" if repo else ""
        w(
            f"| {i} | **{esc(name)}** | {esc(zh(best)) if best['en'] else ''} | {year} "
            f"| {', '.join(stations)} | {flag}{esc(why)} |\n"
        )

    w(f"""
**這是第四個軸**，與 docs/ 既有三份不同：

| 文件 | 缺口是什麼 | 靠什麼補 |
| --- | --- | --- |
| [COVERAGE-GAPS.md](./COVERAGE-GAPS.md) | 還沒有**站** | 開新站 |
| [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md) | 站在、**內容**沒寫完 | `note-check --enrich` |
| [SOURCING-DEBT.md](./SOURCING-DEBT.md) | 內容寫了、查不到**出處** | 掛 anchor |
| **本檔** | **書本身還沒有** | **去收書** |

## bibliography 的四個 status

`library.ts` 的 `BibliographyStatus`，語意是「**這本書在書庫裡的狀態**」，不是「讀過沒有」：

| status | 意思 | 判準 | 筆數 |
| --- | --- | --- | --- |
| `owned` | **已收錄**——書已經做成 `nplus.wiki/<slug>/` 的書站 | 必須有 `slug`；首頁書架的封面列就是取這批，概念頁的 `furtherReading.anchor` 也是連到這裡 | {counts['owned']} 筆（去重 {owned_unique} 本） |
| `wanted` | **待收錄**——想收、還沒有 | 買得到，只是還沒買／還沒做站 | **{counts['wanted']} 筆（去重 {len(by_main)} 本）** |
| `unavailable` | **暫無來源**——想收但收不到 | 絕版、無中譯、或只有機構授權（如 Scrum Guide、Vanguard 內部傳記） | {counts['unavailable']} 筆 |
| `skipped` | **刻意略過**——不打算收 | 內容重複、練習冊、合輯、不合站主軸；`note` 欄寫明為何略過 | {counts['skipped']} 筆 |

> `owned` 去重後的 {owned_unique} 是**已建成書站的書**（{counts['owned']} 是含跨站重複的登錄筆數，
> 一本書被三站列進盤點就算三筆）。它代表「書站存在、封面抓得到、概念頁 anchor 回得去」，
> 不等於實體書在書架上。

""")

    w(f"## 先扣掉：{len(existing)} 本其實已經有書站了\n\n")
    w(
        "這些 `wanted` 的書名對得上**已存在的書 repo**——不必再收，是各站 bibliography 的 "
        "status 沒跟上。**買書前先扣掉這批**，並把該筆改成 `status: \"owned\"` ＋ 補上 "
        "`slug`（＝下表的 repo slug）再重跑；`/note-wanted` 會代勞。\n\n"
    )
    w("| 書 repo slug | 書名 | 登記在 | portal 上的描述（核對用） |\n| --- | --- | --- | --- |\n")
    for k in sorted(existing):
        v = existing[k]
        desc = repo_desc[k]
        shown = esc(desc[:60]) if desc else "**（repo 無描述，需人工確認是不是同一本）**"
        w(f"| `{k}` | {esc(v[0]['en'] or v[0]['title'])} | {', '.join(sorted({r['station'] for r in v}))} | {shown} |\n")

    w(f"\n## 快歸零的站：{len(near_zero)} 站只差 1–2 本\n\n")
    w(
        "**TOP20 的準則①就看這一節。** 這些站的書單已經接近收齊，剩下的一兩本收到，"
        "整站的採購缺口就歸零——缺書不再是它進 `note-check --enrich` 深化的瓶頸。"
        "分母只算 `owned + wanted`（`unavailable` / `skipped` 是永久不可收，不算欠）。\n\n"
    )
    if near_zero:
        w("| 站 | 已收 | 還差 | 差哪幾本 |\n| --- | ---: | ---: | --- |\n")
        for st in near_zero:
            need = ", ".join(
                esc(r["en"] or r["title"]) for r in sorted(by_station[st], key=lambda r: r["title"])
            )
            w(f"| `{st}` | {station_owned[st]} | **{station_left[st]}** | {need} |\n")
    else:
        w("（目前沒有只差 1–2 本的站。）\n")

    w(f"\n## 優先收：{len(multi)} 本有兩個以上的站在等\n\n")
    w("同一本書被多站列為 `wanted`——收一本補多站的缺口，投資報酬率最高。\n\n")
    w("| 英文書名 | 中譯 | 年 | 等它的站 |\n| --- | --- | --- | --- |\n")
    for k in multi:
        v = by_main[k]
        best = max(v, key=lambda r: len(r["en"] or ""))
        stations = sorted({r["station"].replace("-note", "") for r in v})
        year = best["year"] or next((r["year"] for r in v if r["year"]), "")
        w(f"| **{esc(best['en'] or best['title'])}** | {esc(zh(best))} | {year} | {len(stations)}: {', '.join(stations)} |\n")

    w(f"\n## 完整清單（依站，共 {len(rows)} 筆）\n\n")
    for st in sorted(by_station, key=lambda s: (-len(by_station[s]), s)):
        entries = by_station[st]
        w(f"### {st} — {len(entries)} 本\n\n")
        w("| 英文書名 | 中譯 | 年 | 為何想收 |\n| --- | --- | --- | --- |\n")
        for r in entries:
            name = r["en"] or f"（{esc(r['title'])}）"
            mark = f" ⟵ 已有書站 `{r['repo']}`" if r.get("repo") else ""
            w(f"| {esc(name)}{mark} | {esc(zh(r))} | {r['year'] or ''} | {esc(r['note'])} |\n")
        w("\n")

    w(f"## 沒有英文書名的 {len(cjk_only)} 本（華文／日文原著）\n\n")
    w("這些本來就沒有英文版，照原書名收。\n\n| 原書名 | 站 | 為何想收 |\n| --- | --- | --- |\n")
    for r in sorted(cjk_only, key=lambda r: (r["station"], r["title"] or "")):
        w(f"| {esc(r['title'])} | {r['station']} | {esc(r['note'])} |\n")

    w("""
## 重跑

```bash
notes-core/tools/export-wanted.py
```

收到書、建好書站之後，把該站 bibliography 那筆改成 `status: "owned"` 並補 `slug`，
重跑就會從這裡消失。
""")

    text = o.getvalue()
    if len(sys.argv) > 1 and sys.argv[1] == "-":
        sys.stdout.write(text)
    else:
        OUT.write_text(text, encoding="utf-8")
        print(f"{OUT}: {len(rows)} wanted 筆 / {len(by_main)} 本、{len(existing)} 本已有書站、{len(multi)} 本多站共同")


if __name__ == "__main__":
    main()
