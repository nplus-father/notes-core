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

  第三種形狀（2026-08-11）：**中譯書名以 ASCII 數字開頭**，latin_of 的「砍 CJK 之後」
  切不乾淨——startup 的 `The $100 Startup 3000元開始的自主人生`，英文名被抓成
  `The $100 Startup 3000`，於是 portal 早就有的 `100-startup` 對不上，那本在 wanted
  躺著沒被扣掉。career 的 `The Defining Decade 20 世代…` 是同一個形狀（暫時沒 repo
  所以沒出事）。兩筆都已在資料側補 `original` 放純英文書名。掃法：`title` 含 CJK 時，
  取 CJK 之前的前綴，**前綴結尾是數字或冠詞／介係詞就是可疑**。

  同一個坑的另一種形狀（2026-08-09）：`original` 放的是**拉丁／希臘原名**
  （spiritual-formation 的 `Confessiones`、`De Imitatione Christi`，philosophy 的
  `Politeia`、`Ethika Nikomacheia`），規則 1 照收，於是英文名整個對不上——兩個後果：
  跨站併不起來（《效法基督》theology 用英文名、spiritual-formation 用拉丁名，被算成
  兩本，「多站共等」漏報），portal 比對也對不上（《懺悔錄》早就有 `augustine-confessions`
  書站，卻在 wanted 躺到 2026-08-09 才發現，「先扣掉」那節一直回報 0 本）。
  拿 `original` 當英文名之前，先確認它真的是英文；覺得可疑就再拿 `title` 的拉丁前綴
  對一次 portal。

  **修法（2026-08-09 第二輪補上）**：`NON_ENGLISH_ORIGINALS` 列出這些非英文原名，命中就
  改用 `title` 的拉丁前綴當英文名。沒有演算法能判斷「這串拉丁字母是不是英文」——
  `De Imitatione Christi` 與 `The Divine Conspiracy` 在字元層級長得一樣——所以照
  ALIASES 的辦法列白名單。`title` 沒有拉丁前綴時（`神學大全`／`思想錄` 這種純中文
  title）仍退回用 `original`，否則它們會掉進「華文／日文原著」那節，那更不對。

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
  3. **書名對上還不夠，作者也要對上**（2026-08-10 起的第二因子，見 `author_ok`）。
     在那之前 matcher **只比書名**，作者純粹拿來顯示——於是 `understanding-the-bible`
     （Dorothy L. Johns 的函授查經課程）被判成 stott-note 想收的斯托得《認識聖經》，
     而那筆的 `AUTHORS` 早就寫著 "John Stott"：**要擋這個錯的資料一直都在檔案裡，
     只是沒接上比對**。接上之後，「原典很有名、後人拿同一個書名寫教科書」這一整類
     （《Christian Theology》麥葛福 ≠ Erickson、《Servant Leadership》Greenleaf ≠ Boone、
     《Biblical Theology》Vos ≠ Goldingay）都自動擋下並列進報告的「作者這一關擋下的」。
     作者只在**雙方都登錄**時裁決，缺一邊就棄權——缺資料不該變成拒絕。
  4. **NAME_COLLISIONS 剩下的職責**：作者相同、但 repo 內容掛錯書的那種——
     `how-to-be-a-high-school-superstar` 的 repo 內容實為《How to Win at College》
     （見 SOURCING-DEBT.md），作者同樣是 Cal Newport，所以第二因子救不了，只能人工列。
     其餘幾筆是歷史紀錄（那些書已不在 wanted），留著當決策存檔。
  5. **改名／轉寫沒有演算法可解，列 ALIASES**：英美版書名不同（Between Two Worlds
     ＝ I Believe in Preaching）、華文書 repo 用英文轉寫（浪潮之巔 ＝ on-top-of-tides）。
     「該對上卻沒對上」現在會自己浮出來——報告的「疑似漏報」那節用雙向 Jaccard
     提名候選（**只提名不採用**：門檻放寬到能抓改名，就一定混進續集與同系列，
     而誤刪一本還沒收的書比漏報嚴重得多）。確認過的寫進 ALIASES 走精確路徑。

**為什麼不預先把 slug 填進 wanted 條目**（2026-08-10 討論後的決定）：猜出來的 slug 會
**無聲地**爛掉——命名慣例會砍冠詞（`the-war-of-art` → `war-of-art`）、加作者前綴
（`minto-pyramid-principle`），猜錯就永遠對不上，而且沒有任何東西會報錯。這不是假想：
pastoral-psychology 的四個概念頁就是拿 wanted 的書名猜 slug 去 `anchor`，四個全是
死鏈（見 ORPHAN-BOOKS.md 第四節）。所以預測不存進資料，改成**每次重算時現算現報**
（「疑似漏報」那節），沒有東西需要維護、也沒有東西會過期。
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
# 2026-08-11 這輪（`/note-wanted` 全跑）：上一版 20 本裡 3 本已經建好書站（Tuesdays with
# Morrie、Decode and Conquer、60 Seconds and You're Hired），「先扣掉」整體抓到 **38 本**
# wanted 其實早有 repo，回填 38 筆條目（跨 9 站）。全部逐筆對過作者才回填，沒有一筆撞名。
#
# 另外抓到 **一筆比對漏報**：`The $100 Startup 3000元開始的自主人生` 的英文名被 latin_of
# 抓成 `The $100 Startup 3000`（中譯書名以數字開頭，砍 CJK 砍不乾淨），於是 portal 早有的
# `100-startup` 對不上。修法在資料側補 `original`，形狀寫進本檔 docstring 第三個坑。
# 同形狀的 career `The Defining Decade 20 世代…` 一併補了（它目前沒 repo，還沒出事）。
#
# 回填之後近零名單是 **7 站差 1 本 ＋ 9 站差 2 本＝25 本候選**，又超過 20 格。依規矩
# 「差 1 本的站先全部排進去，再排差 2 本的」，前 20 **全部由歸零批填滿**，準則②這輪
# 一樣排不上（「優先收」是 0 本——多站共等的都回填成 owned 了）。
#
# 差 2 本的站有 7 站整對進榜，讓位的幾站與理由：
#   - `management-note`（Managing／Working Backwards）：兩位作者 portal 都掛零，但站內
#     引用薄到只剩孤證——Mintzberg 2 處、「逆向工作法」「PR/FAQ」各 1 處，準則④輸給
#     引用密度高的那幾站。
#   - `navarro-note`（Be Exceptional／Three Minutes to Doomsday）：「肢體語言」全星系
#     12 處／12 個檔案，navarro 站自己只有 3 處——同樣是準則④偏弱；Three Minutes 又厚。
#   - `fengtang-note`（成事／無所畏）：同一天四本馮唐裁決成 `unavailable` 之後才掉進
#     近零名單，本輪已無空格；下輪重挑時是新候選。
#
# 同日的後續裁決（2026-08-11）：`Living in Christ's Presence` 改成 `unavailable`，willard
# 站因此**直接收齊、不再需要採購**——空出來的那格沒有另找一站，而是補上 growth 的另一半
# `Awaken the Giant Within`，讓 growth 由半對變成整對、收齊即歸零。**歸零批的完整性
# 優先於再拉一站進來**：拆對只會讓兩站都停在差 1 本。
#
# 排序 = 消化順序：差 1 批在前（收一本歸零一站），批內與差 2 批內都依準則⑤ 薄→厚。
TOP20 = [
    ("running-lean", "startup 站 owned 61／wanted 1——**收了就歸零**，而這是全星系第二深的主題站（The $100 Startup 這輪查出 portal 早有 `100-startup`、回填成 owned 之後只剩這本）；portal 的 Ash Maurya 只有 Scaling Lean 一本，而那本是**續作**——Lean Canvas 的原典正是缺的這本；站內「精實」21 處／6 個檔案，「Lean Canvas」卻只有 1 處孤證；薄，有繁中《Running Lean 精實執行》"),
    ("a-little-history-of-the-world", "history 站 owned 33／wanted 1——**收了就歸零**（The Silk Roads、Collapse 這輪都查出早有書站）；portal 的 Gombrich **掛零**，但 Little History 這個系列的後輩已經收了 3 本（`little-history-of-literature`、`little-history-of-philosophy`、`little-history-of-economics`）——**系列開山的 1935 那本反而不在**；history 站內「世界史」4 處／3 個檔案；薄，有繁中《寫給年輕人的簡明世界史》"),
    ("the-50th-law", "greene 站 owned 6／wanted 1——**收了就歸零**；另一本《The Law of the Sublime》2026-08 查證仍未出版，已依裁決改成 `unavailable`，所以這是 greene 現在買得到的最後一本；portal 的 Greene 6 本全在（48 法則、33 戰爭策略、誘惑的藝術、人性 18 法則、喚醒你心中的大師、366 權力法則），獨缺這本與 50 Cent 的合著；greene 站內「恐懼」6 處／4 個檔案；有繁中《第 50 條法則》"),
    ("million-dollar-habits", "tracy 站 owned 35／wanted 1——**收了就歸零**，而這 35 本是**全星系最深的作者書櫃**（實查 portal 作者欄命中 35 筆）；財富線已有 The Way to Wealth、Get Rich Now、The Science of Money、21 Success Secrets 四本，缺的正是把財富歸因到習慣系統的這一本；tracy 站內「財富」40 處／10 個檔案、「習慣」24 處／11 個檔案"),
    ("the-7-habits-of-highly-effective-families", "covey 站 owned 9／wanted 1——**收了就歸零**；portal 的柯維 9 本全落在個人與組織層次（七個習慣、第 8 個習慣、與時間有約、原則中心領導…），家庭這一塊掛零，而 covey 站內「家庭」23 處／12 個檔案——最常被援引卻沒有專書可掛的應用場域；厚，有繁中《與幸福有約》"),
    ("bogle-on-mutual-funds", "bogle 站 owned 5／wanted 1——**收了就歸零**（portal 的柏格恰好 5 本，全對得上），獨缺 1993 年這本第一本書；「共同基金」全星系 31 處／20 個檔案／跨 5 站，其中 bogle 站內 15 處／7 個檔案——常識投資框架成形的那一刻沒有出處可掛；厚，排在差 1 批的最後"),
    ("discourses", "philosophy 站 owned 31／wanted 2——**這兩本收齊就歸零**（蘇菲的世界、尼各馬可倫理學、理想國、正義論這輪一次回填了 4 本）；portal 的 Epictetus **掛零**，站上已有奧理略與塞內卡，缺的正是斯多噶三巨頭的最後一角；「斯多噶」全星系 41 處／19 個檔案／跨 10 站，其中 philosophy 站內 27 處／8 個檔案——密度最高的站卻缺一根柱子。**下單前對作者**：portal 的 `discourses-on-livy` 是馬基維利的《論李維》，不是這本（見「作者這一關擋下的」）；薄"),
    ("the-myth-of-sisyphus", "philosophy 的另一半；portal 的 Camus **掛零**（作者欄 0 筆），而站上「人文主義與存在」那組已有佛洛姆 3 本、海德格《存在與時間》列 skipped——存在主義這條線目前沒有任何一本原典撐著（「存在主義」全星系只有 8 處／6 個檔案／跨 4 站，philosophy 站內 1 處）；最薄的一本，有繁中《薛西弗斯的神話》"),
    ("the-dark-side-of-valuation", "damodaran 站 owned 3／wanted 2——**這兩本收齊就歸零**（portal 的 Damodaran 恰好 3 本：Investment Valuation、The Little Book of Valuation、Narrative and Numbers）；「估值」全星系 236 處／40 個檔案／跨 10 站，其中 damodaran 站內 178 處／12 個檔案——**全星系概念密度最高的主題卻只有 3 本原典**，而年輕、高成長與困境公司這一塊在 Investment Valuation 之外沒有出處；厚"),
    ("investment-philosophies", "damodaran 的另一半；「投資哲學」6 處／6 個檔案／跨 2 站（bogle 4、damodaran 2）——兩站都在談流派光譜與各自的適配者，來源卻不在；厚"),
    ("the-innovator-s-prescription", "christensen 站 owned 7／wanted 2——**這兩本收齊就歸零**；portal 的克里斯汀生實查 7 本（創新的兩難、創新者的解答、看見未來、繁榮的悖論、與運氣競爭、你要如何衡量你的人生、創新者的 DNA），**理論本身收得很齊，缺的是兩條應用線**——站上索性把這兩本放進名為「缺口」的分組；這本是醫療端，站主自註「他自認最重要的一本」，而 christensen 站內「醫療」只有 2 處／1 個檔案；厚"),
    ("disrupting-class", "christensen 的另一半，教育端；「破壞式創新」全星系 27 處／22 個檔案／跨 9 站（business-strategy 8、christensen 6、management 5…）——理論被九個站引用，教育這條應用線卻只有 christensen 站內 2 處在轉述；有繁中《來上一堂破壞課》"),
    ("psychological-types", "jung 站 owned 5／wanted 2——**這兩本收齊就歸零**；portal 的榮格恰好 5 本（Answer to Job、原型與集體潛意識、人及其象徵、回憶‧夢‧省思、尋求靈魂的現代人）；「榮格」全星系 100 處／32 個檔案／跨 10 站，**引用他最多的是 thinking 站的 63 處，不是他自己站的 22 處**；這本是內傾／外傾與四種功能的原典、MBTI 整條產業鏈的源頭，而 jung 站內「個體化」19 處／7 個檔案卻沒有類型論的出處；厚"),
    ("the-red-book-liber-novus", "jung 的另一半；1913–1930 的私人筆記、2009 年才出版，他自承後半生的一切都從這裡長出來——站上的閱讀路徑缺的正是這個源頭；**大開本摹真本、二手價高**，排在 jung 這對的後面"),
    ("the-rules-of-parenting", "templar 站 owned 7／wanted 2——**這兩本收齊，整套 Templar Rules 就全了**（portal 的 7 本 Rules 與站上 owned 7 一一對上：love／thinking／life／management／wealth／work／people）；「教養」全星系 32 處／16 個檔案／跨 12 站（relationships 12、career 5…）**卻沒有任何一站有專書可掛**，而系列裡就缺這本場域書；薄"),
    ("the-rules-to-break", "templar 的另一半；系列裡唯一反手的角度——列出那些「大家都說該遵守、其實該打破」的通則，收了系列才完整；薄"),
    ("how-the-mighty-fall", "collins 站 owned 4／wanted 2——**這兩本收齊就歸零**；portal 的 Jim Collins 實查 4 本（Good to Great、Built to Last、Great by Choice、BE 2.0——搜「Collins」另外命中的 `simple-path-to-wealth` 是 J.L. Collins、`team-geek` 是 Collins-Sussman，**子字串假命中要濾掉**）；站主自註「與《從 A 到 A+》互為反面，這條線缺了它就只剩上升段」，而「第五級領導」41 處／20 個檔案、「刺蝟」51 處／22 個檔案，引用大戶是 leadership 與 business-strategy，collins 站自己只有 10 處與 3 處；薄"),
    ("good-to-great-and-the-social-sectors", "collins 的另一半；把同一套框架搬到沒有利潤計分板的非營利部門——「非營利」全星系 18 處／14 個檔案／跨 8 站（drucker 5、business-strategy 3…），杜拉克那條線接住了非營利管理，卓越框架這一側沒有；四十餘頁的專論，最薄"),
    ("the-obstacle-is-the-way", "growth 站 owned 42／wanted 2——**這兩本收齊就歸零**；portal 已有 Holiday 2 本（The Daily Stoic、Ego Is the Enemy），缺的是三本一組裡的第一本；「斯多噶」全星系 41 處／19 個檔案／跨 10 站，但 growth 站內只有 1 處——這條韌性線在 growth 目前是靠 Holiday 的另兩本撐著；薄，有繁中《障礙就是道路》"),
    ("awaken-the-giant-within", "growth 的另一半，遞補 Living in Christ's Presence 空出來的那格（willard 那本 2026-08 裁決成 `unavailable`，willard 站因此直接收齊、不再需要採購）；portal 的 Tony Robbins **掛零**（唯一命中 Robbins 的是 Mel Robbins 的 The Let Them Theory，不是他），站主自註是「自助正典名冊，補齊譜系用」；厚，排在最後"),
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

# `original` 裡放的是拉丁／希臘／法文原名，不是英文書名——命中就改拿 `title` 的拉丁
# 前綴當英文名（見檔頭「同一個坑的另一種形狀」）。漏列的代價是跨站併不起來、portal
# 也對不上，看到某書「應該多站都要卻只出現一次」時先查這裡。
NON_ENGLISH_ORIGINALS = {
    "Confessiones",
    "De Imitatione Christi",
    "Diatribai",
    "Ethika Nikomacheia",
    "Le Mythe de Sisyphe",
    "Politeia",
    "Tao Te Ching",
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
                "author": field("author"),
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


# 作者欄裡「— 之後」是給人看的註記（`Cal Newport — portal 同名 repo 內容實為…`、
# `Alister E. McGrath 麥葛福 — 不是 Millard Erickson 的同名書`）。**比對前一定要砍掉**：
# 那段註記裡常常就寫著撞名的另一位作者，不砍會反過來把假命中認成真的。
AUTHOR_NOTE = re.compile(r"\s*[—–]\s*.*$|\s+-\s+.*$")
# 姓名裡不帶識別力的字：縮寫、序數、常見連接詞與敬稱。
AUTHOR_STOP = {"jr", "sr", "ii", "iii", "and", "with", "et", "al", "the", "ed", "eds"}


def author_keys(s):
    """把作者欄拆成 (拉丁姓氏集合, CJK 字串)，兩種寫法各給一條比對路徑。

    寫法從來不統一——`John Stott` / `John R. W. Stott` / `Kent Beck & Martin Fowler` /
    `Alister E. McGrath 麥葛福` / `秦嗣林`。全等會過度嚴格（合著、有沒有中間名就對不上），
    所以拉丁側用**姓氏 token 交集**：砍掉單字母縮寫與 jr/ed 這類雜訊之後還剩下的詞。
    分得開 Stott 與 Johns、Greenleaf 與 Boone、Vos 與 Goldingay——這正是要擋的那一類。
    """
    s = AUTHOR_NOTE.sub("", s or "")
    latin = {
        t
        for t in re.findall(r"[A-Za-z][A-Za-z'’-]*", s.lower())
        if len(t) > 1 and t not in AUTHOR_STOP
    }
    cjk = "".join(re.findall(r"[㐀-鿿]", s))
    return latin, cjk


def author_ok(want, repo):
    """兩因子的第二關：書名對上之後，作者也要對得上。回 True/False/None（無從判斷）。

    **只有雙方都有作者訊號時才裁決**——缺資料不該變成拒絕（那會把一堆真命中誤殺），
    所以回 None 表示「這關棄權，交給書名那關」，並在輸出裡催補該站的 `author` 欄。

    這一關擋掉的是「原典很有名、後人拿同一個書名寫別的書」那一類。2026-08-10 之前
    matcher **只比書名**，作者純粹拿來顯示——於是 `understanding-the-bible`（Dorothy L.
    Johns 的函授查經課程）被判成 stott-note 想收的斯托得《認識聖經》，而那筆的
    當時的 `AUTHORS` 側表早就寫著 "John Stott"，資料就在檔案裡沒人用。
    接上之後側表整張搬進 bibliography 並刪除，NAME_COLLISIONS 也只剩
    「作者相同、repo 內容掛錯書」那一種需要人工兜底。
    """
    wl, wc = author_keys(want)
    rl, rc = author_keys(repo)
    if (wl or wc) and (rl or rc):
        return bool(wl & rl) or bool(wc and rc and (wc in rc or rc in wc))
    return None


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
            if (e["original"] or "").strip() in NON_ENGLISH_ORIGINALS:
                en = latin_of(e["title"]) or latin_of(e["original"])
            else:
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

    # 作者＝防買錯書的第二因子（見 author_ok）。正本是各站 bibliography 的 `author` 欄
    # （notes-core v0.27.0 起）。**產生器不再自己養對照表**——2026-08-10 那張 278 筆的
    # `AUTHORS` 側表已整批搬進資料並刪除（migrate-authors.py）。查不到就吵，不要靜靜留白。
    for r in rows:
        r["author"] = r.get("author") or ""
    unattributed = sorted({r["main"] for r in rows if not r["author"]})

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
    #   understanding-the-bible：repo 是 Dorothy L. Johns 的函授查經課程
    #   (Methods of Bible Study)，stott-note 想收的是斯托得 1972 年的《認識聖經》
    #   ——書名一字不差，作者與書種完全不同（2026-08-10 加）。
    NAME_COLLISIONS = {
        ("change-your-thinking-change-your-life", "tracy-note"),
        ("how-to-be-a-high-school-superstar", "newport-note"),
        ("biblical-theology-goldingay", "biblical-studies-note"),
        ("erickson-christian-theology", "theology-note"),
        ("servant-leadership", "leadership-note"),
        ("understanding-the-bible", "stott-note"),
    }

    def match_repo(r):
        """一筆 wanted 對得上哪個書 repo？對不上回 (None, 原因)——那才是真缺口。

        **兩因子**（2026-08-10 起）：書名對上還不夠，作者也要對得上。
          第一因子・書名，只認兩種命中，其餘一律當沒有：
            a. 正規化後**完全相同**（砍副標與冠詞之後，真的是同一個書名）。
            b. **作者前綴**：portal 書名 ＝ 作者姓氏 ＋ 想收的書名，且那個姓氏確實出現在
               description 的作者欄（`The Minto Pyramid Principle` ＝ `Pyramid Principle`）。
          第二因子・作者（見 author_ok）：雙方都登錄作者時才裁決，對不上就**否決這次命中**
            並記下原因，讓它留在 wanted。這一關把「同名不同書」從人工白名單變成自動判斷。
        曾經試過「token 連續包含」，結果 `Action` 吃掉 `Kubernetes in Action`、
        `Boundaries` 吃掉 `Boundaries with Kids`、`The Divine Conspiracy` 吃掉它的續集
        `Continued`——48 筆命中裡三十幾筆是假的。寧可漏報留在 wanted，也不要把還沒收的
        書從採購清單裡誤刪；漏掉的用 ALIASES 補。
        """
        alias = ALIASES.get(r["main"])
        if alias and alias in by_name:
            return by_name[alias], None

        hit = None
        for key in (r["en"], r["title"]):
            k = norm_title(key)
            if not k:
                continue
            if k in idx:
                hit = idx[k]
                break
            toks = k.split()
            for pk, it in title_idx.items():
                ptoks = pk.split()
                if len(ptoks) == len(toks) + 1 and ptoks[1:] == toks:
                    if ptoks[0] in norm_title(it["book_author"]).split():
                        hit = it
                        break
            if hit:
                break
        if not hit:
            return None, None

        verdict = author_ok(r["author"], hit["book_author"])
        if verdict is False:
            return None, (hit["name"], hit["book_author"])
        return hit, None

    existing = {}
    rejected = []  # 書名對上但作者不符——自動擋下的同名不同書
    for r in rows:
        hit, clash = match_repo(r)
        if clash:
            rejected.append((r, clash))
            continue
        if hit and (hit["name"], r["station"]) not in NAME_COLLISIONS:
            r["repo"] = hit["name"]
            existing.setdefault(hit["name"], []).append(r)

    # ── 疑似漏報：書名沒對上，但有 repo 長得很像 ──────────────────
    # 精確比對只認「正規化後完全相同」，所以英美版改書名（Between Two Worlds ＝
    # I Believe in Preaching）、華文書用英文轉寫（浪潮之巔 ＝ on-top-of-tides）都會漏，
    # 過去只能靠人踩到再補 ALIASES。這一節把「該對上卻沒對上」自動撈出來給人看。
    #
    # **為什麼是報候選、不是自動採用**：門檻放寬到能抓到改名，就一定會混進續集與同系列
    # （The Divine Conspiracy ↔ … Continued、Trend Following ↔ … Masters Vol.2）。
    # 這類錯誤的代價是把「還沒收的書」從採購清單裡誤刪——比漏報嚴重得多。所以這節只
    # 提名，確認過的請寫進 ALIASES，讓它下一輪走精確路徑。
    #
    # 這也是「預先填 slug」的替代方案：不把猜測**存進**資料（存了就會爛掉，而且爛得
    # 無聲——今天 4 個死鏈 anchor 就是頁面拿 wanted 書名猜 slug 猜出來的），
    # 改成每次重算時**現算現報**，沒有東西需要維護。
    # 相似度用**雙向 Jaccard**，不是單向覆蓋率。單向會被系列卷洗版：
    # `HBR's 10 Must Reads on Leadership` 的 4 個詞有 3 個出現在 `… on Communication`
    # 裡＝75%，但那是完全不同的一本。Jaccard 把 repo 那側多出來的詞也算進分母
    # （3/5＝60%）就篩掉了。同理擋掉 Trend Following ↔ Masters Vol.2、
    # 7 Habits Families ↔ People——這三類正是 2026-08-10 首次跑時全部 8 筆提名的內容。
    #
    # 詞相等的判準放寬到**共同前綴 ≥5 字元**，才抓得到真正該抓的那類：詞形差異
    # （`Forgiving and Reconciling` ↔ `Forgiveness and Reconciliation`——pastoral 站
    # 就有一筆這樣的，頁面還照著錯書名猜了 slug 去 anchor，結果 404）。
    STEM = 5

    def tok_match(a, b):
        return a == b or (min(len(a), len(b)) >= STEM and a[:STEM] == b[:STEM])

    def jaccard(a, b):
        inter = sum(1 for x in a if any(tok_match(x, y) for y in b))
        union = len(a) + len(b) - inter
        return inter / union if union else 0.0

    author_of_repo = {i["name"]: i.get("book_author", "") for i in portal_items}
    book_tokens = {
        it["name"]: {t for t in norm_title(it["book_title"]).split() if len(t) > 2}
        for it in portal_items
    }

    near_miss = []
    for r in rows:
        if r.get("repo") or not r["en"]:
            continue
        want = {t for t in norm_title(r["en"]).split() if len(t) > 2}
        if len(want) < 2:
            continue  # 一個詞的書名（Flow、Grit）跟太多東西像，放過
        best = None
        for name, toks in book_tokens.items():
            if len(toks) < 2:
                continue
            score = jaccard(want, toks)
            if score >= 0.7:
                if author_ok(r["author"], author_of_repo.get(name, "")) is False:
                    continue  # 作者已經否決，那就不是漏報
                if best is None or score > best[1]:
                    best = (name, score)
        # NAME_COLLISIONS 已經人工裁決過的不必再提名——那是「已結案」，不是「待確認」。
        if best and (best[0], r["station"]) not in NAME_COLLISIONS:
            near_miss.append((r, best[0], best[1]))

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
全部匯出成一張採購清單。書名以**英文原名**為主，中譯附在後面，並附**作者**——
同名不同書會讓人買錯（portal 上的 `servant-leadership` 是 Larry W. Boone 的教科書，
不是 Greenleaf 1977 原典），下單前請對作者。由
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
    w("| # | 英文書名 | 作者 | 中譯 | 年 | 站 | 為何排這裡 |\n| --- | --- | --- | --- | --- | --- | --- |\n")
    for i, (key, why) in enumerate(TOP20, 1):
        v = by_main.get(key)
        if not v:
            w(f"| {i} | ⚠ `{key}` 已不在 wanted（收到了或書名改了，請更新 `TOP20`） | | | | | {esc(why)} |\n")
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
            f"| {i} | **{esc(name)}** | {esc(best['author']) or '⚠ 作者未登錄'} "
            f"| {esc(zh(best)) if best['en'] else ''} | {year} "
            f"| {', '.join(stations)} | {flag}{esc(why)} |\n"
        )

    w(f"""
**這是「書本身還沒有」那個軸**，與 docs/ 其餘幾份不同：

| 文件 | 缺口是什麼 | 靠什麼補 |
| --- | --- | --- |
| [COVERAGE-GAPS.md](./COVERAGE-GAPS.md) | 還沒有**站** | 開新站 |
| [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md) | 站在、**內容**沒寫完 | `note-check --enrich` |
| [SOURCING-DEBT.md](./SOURCING-DEBT.md) | 內容寫了、查不到**出處** | 掛 anchor |
| [ORPHAN-BOOKS.md](./ORPHAN-BOOKS.md) | **書有了、沒有站在管** | 認領／開站 |
| **本檔** | **書本身還沒有** | **去收書** |

> 本檔是「**站**說它缺什麼」的正向視角，看不到「沒有任何站提過」的書——那一側看
> [ORPHAN-BOOKS.md](./ORPHAN-BOOKS.md)。兩份要成對看，`tools/refresh-galaxy-docs.sh` 一次重算。

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

    w(f"\n## 作者這一關擋下的：{len(rejected)} 筆同名不同書\n\n")
    w(
        "書名正規化後對得上某個書 repo，**但作者不符**——所以那本不是這一筆想收的書，"
        "維持 `wanted`。這關是 2026-08-10 加的第二因子；在那之前 matcher 只比書名，"
        "撞名只能靠 `NAME_COLLISIONS` 人工白名單一筆筆補（踩到才補）。\n\n"
        "**下面每一筆都要當成買錯書的預警**：想收的和 portal 上那本同名，"
        "下單前對作者，別對書名。\n\n"
    )
    if rejected:
        w("| 想收的書 | 想收的作者 | 撞到的 repo | repo 上的作者 | 登記在 |\n| --- | --- | --- | --- | --- |\n")
        for r, (repo_name, repo_author) in sorted(rejected, key=lambda x: (x[1][0], x[0]["station"])):
            w(
                f"| {esc(r['en'] or r['title'])} | {esc(r['author'])} | `{repo_name}` "
                f"| {esc(repo_author) or '（repo 無作者欄）'} | {r['station']} |\n"
            )
        w("\n")
    else:
        w("無——這輪沒有書名對上卻作者不符的。\n\n")

    w(f"## 疑似漏報：{len(near_miss)} 本可能其實已經有 repo\n\n")
    w(
        "書名**沒有**正規化後完全相同，但 portal 上有 repo 長得很像——改過書名"
        "（英美版不同、中譯轉寫）的書會落在這裡。**這節是提名，不是判決**：確認是同一本就"
        "寫進 `export-wanted.py` 的 `ALIASES`，下一輪它就走精確路徑並自動掉進「先扣掉」；"
        "確認是續集或同系列的不同書就不用管，下輪還會再問一次。\n\n"
        "門檻：兩邊書名的**雙向 Jaccard ≥70%**（詞相等的判準放寬到共同前綴 5 字元，"
        "才抓得到 `Forgiving` ↔ `Forgiveness` 這種詞形差異），且**作者沒有互相否決**。"
        "用雙向而不是單向覆蓋率，是因為單向會被系列卷洗版——`… on Leadership` 的詞"
        "有 75% 出現在 `… on Communication` 裡，但那是不同的一本。"
        "作者不符的已經在上一節擋掉；`NAME_COLLISIONS` 裁決過的不再提名。\n\n"
    )
    if near_miss:
        w("| 想收的書 | 作者 | 疑似 repo | 相似度 | repo 上的書名 | 登記在 |\n| --- | --- | --- | ---: | --- | --- |\n")
        for r, name, score in sorted(near_miss, key=lambda x: -x[2]):
            title = next((i["book_title"] for i in portal_items if i["name"] == name), name)
            w(
                f"| {esc(r['en'])} | {esc(r['author']) or '⚠ 作者未登錄'} | `{name}` "
                f"| {score:.0%} | {esc(title)} | {r['station']} |\n"
            )
        w("\n")
    else:
        w("無——沒有書名相近卻沒對上的。\n\n")

    w(f"## 快歸零的站：{len(near_zero)} 站只差 1–2 本\n\n")
    w(
        "**TOP20 的準則①就看這一節。** 這些站的書單已經接近收齊，剩下的一兩本收到，"
        "整站的採購缺口就歸零——缺書不再是它進 `note-check --enrich` 深化的瓶頸。"
        "分母只算 `owned + wanted`（`unavailable` / `skipped` 是永久不可收，不算欠）。\n\n"
    )
    if near_zero:
        w("| 站 | 已收 | 還差 | 差哪幾本 |\n| --- | ---: | ---: | --- |\n")
        for st in near_zero:
            need = "、".join(
                f"{esc(r['en'] or r['title'])}（{esc(r['author']) or '⚠ 作者未登錄'}）"
                for r in sorted(by_station[st], key=lambda r: r["title"])
            )
            w(f"| `{st}` | {station_owned[st]} | **{station_left[st]}** | {need} |\n")
    else:
        w("（目前沒有只差 1–2 本的站。）\n")

    if unattributed:
        w(
            f"\n> ⚠ **{len(unattributed)} 本還沒登錄作者**，表上標「⚠ 作者未登錄」："
            + "、".join(f"`{k}`" for k in unattributed)
            + "。**在該站 `bibliography.ts` 那筆補 `author:`** 再重跑（notes-core v0.27.0 起"
            "作者是 bibliography 的資料欄，產生器不再養對照表）——沒有作者就防不了同名不同書。\n"
        )

    w(f"\n## 優先收：{len(multi)} 本有兩個以上的站在等\n\n")
    w("同一本書被多站列為 `wanted`——收一本補多站的缺口，投資報酬率最高。\n\n")
    w("| 英文書名 | 作者 | 中譯 | 年 | 等它的站 |\n| --- | --- | --- | --- | --- |\n")
    for k in multi:
        v = by_main[k]
        best = max(v, key=lambda r: len(r["en"] or ""))
        stations = sorted({r["station"].replace("-note", "") for r in v})
        year = best["year"] or next((r["year"] for r in v if r["year"]), "")
        w(
            f"| **{esc(best['en'] or best['title'])}** | {esc(best['author']) or '⚠ 作者未登錄'} "
            f"| {esc(zh(best))} | {year} | {len(stations)}: {', '.join(stations)} |\n"
        )

    w(f"\n## 完整清單（依站，共 {len(rows)} 筆）\n\n")
    for st in sorted(by_station, key=lambda s: (-len(by_station[s]), s)):
        entries = by_station[st]
        w(f"### {st} — {len(entries)} 本\n\n")
        w("| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |\n| --- | --- | --- | --- | --- |\n")
        for r in entries:
            name = r["en"] or f"（{esc(r['title'])}）"
            mark = f" ⟵ 已有書站 `{r['repo']}`" if r.get("repo") else ""
            w(
                f"| {esc(name)}{mark} | {esc(r['author']) or '⚠ 作者未登錄'} "
                f"| {esc(zh(r))} | {r['year'] or ''} | {esc(r['note'])} |\n"
            )
        w("\n")

    w(f"## 沒有英文書名的 {len(cjk_only)} 本（華文／日文原著）\n\n")
    w("這些本來就沒有英文版，照原書名收。\n\n| 原書名 | 作者 | 站 | 為何想收 |\n| --- | --- | --- | --- |\n")
    for r in sorted(cjk_only, key=lambda r: (r["station"], r["title"] or "")):
        w(
            f"| {esc(r['title'])} | {esc(r['author']) or '⚠ 作者未登錄'} "
            f"| {r['station']} | {esc(r['note'])} |\n"
        )

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
