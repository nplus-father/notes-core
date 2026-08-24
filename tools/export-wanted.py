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
     作者只在**雙方都有可比通道**時裁決（都有拉丁字或都有漢字），缺一邊、或一邊漢字
     一邊拉丁的音譯（`孫子` vs `Sun Tzu`）就棄權——沒有訊號不該變成否定的訊號
     （2026-08-13 修，那之前 `art-of-war` 就是這樣被擋在「先扣掉」外面的）。
  4. **NAME_COLLISIONS 剩下的職責**：作者相同、但 repo 內容掛錯書的那種——
     `how-to-be-a-high-school-superstar` 的 repo 內容實為《How to Win at College》
     （見 SOURCING-DEBT.md），作者同樣是 Cal Newport，所以第二因子救不了，只能人工列。
     其餘幾筆是歷史紀錄（那些書已不在 wanted），留著當決策存檔。
  5. **改名／轉寫沒有演算法可解，列 ALIASES**：英美版書名不同（Between Two Worlds
     ＝ I Believe in Preaching）、華文書 repo 用英文轉寫（浪潮之巔 ＝ on-top-of-tides）。
     「該對上卻沒對上」現在會自己浮出來——報告的「疑似漏報」那節用雙向 Jaccard
     提名候選（**只提名不採用**：門檻放寬到能抓改名，就一定混進續集與同系列，
     而誤刪一本還沒收的書比漏報嚴重得多）。確認過的寫進 ALIASES 走精確路徑。
  6. **比書名這條路本身有系統性盲區——每輪都要拿作者欄反查一次**（2026-08-11 第二輪）。
     那一輪「先扣掉」歸零之後，改用 `gh repo list` 的 description 作者欄去查候選書的
     作者書櫃，**又挖出 16 本 wanted 其實早有 repo**。三種形狀，前兩種是 `norm_title`
     切不乾淨，第三種根本不可能靠書名解：
       a. 副標用**逗號**或 `, or` 分隔——`norm_title` 只砍冒號後的副標，於是
          `Psychological Types, or The Psychology of Individuation` 與《心理類型》對不上。
       b. 書名帶**括號附註**——`The Red Book (Liber Novus)`、`After You Believe
          (Virtue Reborn)`，括號沒被砍掉，與 repo 的 `The Red Book: A Reader's Edition`、
          `After You Believe` 差一截。
       c. **華文原著的 repo 用英譯書名**——`成事` 是 `Getting Things Done: Feng Tang
          Reads Zeng Guofan`、`商業簡史` 是 `The Evolution of Business`、`文明之光` 是
          `The Glory of Civilization`。這不是零星幾本而是**整站**：wujun 6 本裡 5 本、
          liurun 5 本全部、fengtang 2 本全部。ALIASES 只在「踩到才補」時有用，而這種
          站是一次全滅——**唯一撈得到的辦法是拿作者反查 portal 書櫃，逐本用 README 的
          「這是 **中文書名** 的專案倉庫」那行核對**，比書名永遠對不上。
     反查也會撈到假的，擋下來的都記在 TOP20 上方的註解裡（`wujun-information-theory-40`
     ≠《信息傳》、`simply-managing` ≠《Managing》，2026-08-13 再加三筆）——**同作者、
     書名接近、但確實是兩本書**，只有讀 README 分得出來。所以這關是人工的，不要想自動化
     成判決。2026-08-13 那輪反查 17 筆候選**全數落空**（那 45 本靠書名就對上了），
     這關仍然要每輪跑——落空是結果，不是可以省略的理由。

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
import datetime as _dt

from _stamp import stamp
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
# 2026-08-14（Andrew 裁決輪，資料源：GitHub 現況 1794 個 repo）：這輪沒有新的「先扣掉」，
# 動的是**狀態裁決**，wanted 從 138 → 116 筆：
#   a. **三筆懸案裁掉**（上兩輪都掛在 TOP20 上等 Andrew）：
#      - fromm 的《禪與心理分析》→ 以 `psychoanalysis-and-zen-buddhism`（Fromm 那半，
#        README 標「精神分析與禪佛教」）算收錄，鈴木大拙與 De Martino 兩篇不另收。
#      - economics 的《Globalization and Its Discontents》→ 以 2017 增訂版
#        `globalization-and-its-discontents-revisited` 收錄，不另收 2002 初版。
#      - management 的《Managing》→ **以 `simply-managing` 代替**（Mintzberg 2013 自己的濃縮
#        改寫本）。下面「兩本書」那段的 simply-managing 那條因此作廢——比對規則沒錯，是
#        Andrew 決定這本就夠了；三筆都已在各站改成 owned ＋ 補 slug，所以從清單消失。
#      - wujun 的《信息傳》→ **與《信息論 40 講》當同一本結案**（`wujun-information-theory-40`）。
#        比對時查得很清楚：吳軍書櫃 17 本逐個看過，那個 repo 的 README 標「吳軍．信息論40講」，
#        書目上是兩本；Andrew 2026-08-14 裁決不分了，以那個書站收錄，wujun 站因此歸零。
#   b. **19 筆判定 unavailable**（Andrew 指名，各站 note 補「2026-08 判定暫無來源」）：
#      de-botton 1（The News）、nt-wright 4（整站）、pastoral-psychology 5（整站）、
#      nouwen 5（整站）、image-style 4（只留 Take Ivy）。**四個站的 wanted 直接歸零**，
#      上一輪 TOP20 裡的 5 格（The News、賴特 4 本）跟著作廢。
#
# 於是近零名單重排成 **6 站各差 1 本**（image-style 因為那 4 本出局而新進榜，剩 Take Ivy），
# 準則②照樣是 0（多站共等的都回填成 owned 了）；其餘 14 格分給 security 整站 6 本（準則③領頭）、
# cloud 5 本（準則④）、NICNT、Good Habits, Bad Habits、Why Zebras Don't Get Ulcers。
#
# 2026-08-14 第二輪（同日晚間，資料源：GitHub 現況 1804 個 repo）：Andrew 在裁決輪之後
# **一口氣建了 10 個書站**，其中 8 本正是上一版 TOP20 裡的——所以這輪是真正的「買到了」對帳。
#   a. **10 本回填 owned**：dark-side-of-valuation、hold-me-tight、into-the-woods、
#      playing-to-win、take-ivy（以上 5 本是上版 TOP20 的第 2–6 格）＋ HBR Must Reads 5 卷
#      （the-essentials／on-strategy／on-innovation／on-leadership／on-managing-people）。
#      wanted 115 → 105，**business-strategy／relationships／writing／image-style／damodaran
#      五站同時歸零**，近零名單只剩 newport 一站。
#   b. **比對規則補了 EDITION_TAIL**（見 norm_title 上方）：HBR 的 on-leadership 與
#      on-managing-people 明明已經有 repo 卻沒進「先扣掉」——portal 描述書名帶
#      `, Updated and Expanded`，精確比對打不中，連「疑似漏報」都撈不到（尾綴三個詞灌進
#      Jaccard 分母，真命中只剩 57%，輸給同系列另一卷的假命中 75%）。砍掉版次尾綴後兩本都歸位。
#      **hbr 站因此也不再是「讓位」而是收乾淨了**——上一輪那句「hbr 5 卷是合輯所以讓位」作廢。
#   c. 準則①這輪只剩 newport 一格（第 1 格），準則②仍是 0，準則③兩筆（Web Hacker's
#      Handbook、NICNT）都已在榜——所以空出來的 5 格全由準則④填，選的是「portal 書櫃夠深
#      ／衍生書已在、原典卻缺」那種（第 2–6 格，數字都現查過）。
#   - drucker（5）這輪仍讓位：portal 書櫃 18 本是全星系最深的單一作者，但那 5 本是早期／
#     晚期邊緣作，概念側證據撐不起來——「合法性」全星系 13 處裡 8 處在 leetcode 站是
#     **字面假命中**（輸入合法性），drucker 站真命中只有 3 處。下輪若要排，先補概念頁再說。
#
# 2026-08-14 第三輪（Andrew 再裁決 7 筆 unavailable，wanted 105 → 98）：
#   newport 1（How to Be a High School Superstar）、gardner 3（Art, Mind, and Brain／
#   The Mind's New Science／Extraordinary Minds）、drucker 3（The Future of Industrial Man／
#   Managing in Turbulent Times／Managing the Non-Profit Organization）。
#   **newport 站直接歸零**（那是它最後一本 wanted），TOP20 第 1、2 格同時作廢。
#   於是近零名單重排成 drucker 與 gardner **各差 2 本**，沒有差 1 本的站；兩格空缺塞不下
#   兩站四本，所以照準則①的本意「讓一個站真的歸零」，整批給 drucker。
#   **選 drucker 不選 gardner 的實查依據**：「知識工作者」94 處跨 4 站（drucker 34、
#   management 23、business-strategy 18、newport 8）對上 gardner 那兩本的「真善美」3 處、
#   「卓越與倫理」5 處（且都只在本站）。上面第二輪那句「drucker 讓位」因此作廢——讓位的
#   理由是那 5 本裡的早期邊緣作，而它們 3 本已經被裁成 unavailable，剩下的 2 本是有槓桿的。
#   gardner 的 2 本（The App Generation／Truth, Beauty, and Goodness Reframed）下輪再排。
#
# 2026-08-15（資料源：GitHub 現況 1882 個 repo，前一輪是 1804）：**這輪整張表重挑**——
# Andrew 一口氣建了 70 個書站，wanted 98 → 28，上一版 TOP20 有 **16 格**（第 1–6、7–12
# 的 security 4 本、13–17 的 cloud 5 本、19、20）當場作廢。加上作者反查再撈到 2 本，
# 剩 **26 本**，而表只有 20 格——所以這輪的工作不是「挑哪 20 本」而是「哪 6 本落選」。
#   a. **作者反查撈到的 2 本**（docstring 第 6 點那關，這輪沒有落空）：
#      - `sql-antipatterns-volume-1` ＝ Karwin 2010《SQL Antipatterns》的 2022 卷一改版
#        （README 標「SQL 反模式 卷一」）。書名尾綴 `, Volume 1` 不在 EDITION_TAIL 裡，
#        精確比對打不中。**不要把 `, Volume N` 加進 EDITION_TAIL**——`TCP/IP Illustrated,
#        Volume 1` 與 `Volume 2` 是真的兩本書，砍掉會誤併。這筆走資料側回填即可。
#      - `valuation-measuring-and-managing-value-of-companies` ＝ McKinsey《Valuation》第八版，
#        正是 investing 想收的那本。漏掉的原因是 wanted 那側書名寫成 `Valuation (McKinsey)`，
#        **括號附註灌進 norm_title**（docstring 第 6b 點的老形狀）。同樣走資料側回填。
#      兩筆都不寫 ALIASES：回填成 owned 之後就離開 wanted，alias 只會變成死條目
#      （現存的 `between-two-worlds` / `cjk::浪潮之巔` 兩筆其實早就是這種狀態了）。
#   b. **準則① 8 格**：差 1 本的 investing、marketing 各 1（第 1–2 格），差 2 本的
#      cloud-infra、personal-finance、security 各 2（第 3–8 格）。準則②照樣是 0。
#   c. **第 9 格給準則③**（NICNT，站主自標「系列級缺口」），第 10–20 格是準則④。
#      data-systems 只剩 3 本、缺口 15.8% 是四個候選站裡最高的，整批排進去（第 10–12 格）
#      ——它不在「差 1–2 本」名單裡，但收齊就是第四個歸零的站，這是準則①的本意延伸。
#   d. **落選的 6 本與理由**（都是準則④的證據撐不起來，不是不重要）：
#      《神學大全》（「經院」全星系只有 3 處、theology 站 1 處，且部頭極鉅）、
#      《改革宗教理學》巴文克（4 卷，中譯還沒出齊）、
#      Goldingay《Old Testament Theology》三卷（同作者單卷《聖經神學》已收）、
#      Currey《Daily Rituals》（「作息」habits 站只有 5 處，且是田野調查不是機制）、
#      Pang《Rest》（「刻意休息」1 處孤證，portal 休息線已有 why-we-sleep／
#      stanford-method-of-sleep／hbr-guide-to-beating-burnout 三本）。
#      落選第 6 本原是 Gentry & Wellum《Kingdom through Covenant》，當天就被裁掉了，見 e。
#   e. **Andrew 同日裁決**：Gentry & Wellum 的《Kingdom through Covenant》（2012）
#      **以 `gods-kingdom-through-gods-covenants` 算收錄**，不另收原典。那個 repo 的 README
#      標「神的國度藉著神的聖約」、副標 `A Concise Biblical Theology`，是同兩位作者把 2012
#      那本濃縮改寫的版本——書目上是兩本，比照 `simply-managing` 代替《Managing》的前例
#      當同一本結案。wanted 26 → 25，biblical-studies 從 5 本降到 4 本。
#      **這是「已裁決」不是「沒查過」**，下輪的「疑似漏報」不要再提名它。
#
# 2026-08-16（資料源：GitHub 現況 1901 個 repo，前一輪是 1882）：**又一次整表重挑，而且
# 這輪表比書多**——Andrew 再建了 17 個書站，上一版 TOP20 有 **14 格**（第 1–5、7–8、
# 10–11、13、15–18）當場作廢，全星系 wanted 25 → 8。8 本裝不滿 20 格，所以工作變成
# 「把剩下的全部排出順序」而不是「挑 20 本」。
#   a. **只剩 4 個站還有 wanted**：biblical-studies 4、theology 2、personal-finance 1、
#      data-systems 1。其餘四十幾站的採購缺口全部歸零。
#   b. **產生器跟著改**：`## 先收這 N 本` 的 N 改成 `len(TOP20)`，且當 TOP20 已涵蓋全部
#      wanted 時，開場白從「整份 N 筆太長，這是從裡面挑出來的」換成「只剩 N 筆，這節就是
#      全部」——原本的寫法會讓人以為還有沒排進來的書。這是星系收乾淨之後的新常態。
#   c. **準則①吃掉前 4 格**：差 1 本的 personal-finance、data-systems（第 1–2 格），
#      差 2 本的 theology（第 3–4 格）。第 5 格給準則③（NICNT，唯一站主自標的一筆），
#      第 6–8 格是準則④的 biblical-studies 三本。準則②照樣是 0（沒有多站共等的書）。
#   d. **作者反查（docstring 第 6 點）這輪 0 收穫，但撈到兩個「配套在、本體不在」的證據**，
#      都寫進了排序理由：`christian-theology-reader` 是 McGrath 那本教科書的**配套讀本**、
#      `thomas-aquinas-summa-theologiae` 其實是 **Bernard McGinn 寫的《神學大全》傳記**
#      （Princeton 名著傳記系列），阿奎那本人 0 本。**後者是個 matcher 陷阱**：repo 名長得
#      像原典，但精確比對打不中（portal 標題是 `Thomas Aquinas's Summa theologiae: A
#      Biography`，去副標後仍多兩個詞），作者因子也會否決——**不要為了「讓它對上」去放寬
#      norm_title**，那會把一堆傳記／導讀併進原典。
#   e. **Goldingay《Old Testament Theology》排最後，理由誠實寫在表裡**：portal 的舊約神學線
#      已有 Brueggemann、Waltke 兩本，他自己的單卷《聖經神學》也已收——那格不是空的，是想
#      多收一種進路。順手把該筆 title 的 `（三卷）` 移進 note：括號會被 latin_of 切在
#      中譯欄印成「三卷）」（第 6b 點那個老形狀的表親）。
#   e2. **Andrew 同日裁決**：Bauckham《Jesus and the Eyewitnesses》**找不到，改
#      `unavailable`**（原第 7 格，表縮成 7 本）。缺口本身沒有消失——「目擊者」17 處、
#      keller 與 biblical-studies 各 6 處那個證據仍然成立，只是不再佔採購清單版面。
#      依 2026-08-10 的決議**不要撈出來提醒複查**；他自己找到了會主動說。
#   f. **theology 的《改革宗教理學》以 `reformed-dogmatics` 回填**——那個 repo 是 John Bolt
#      編的**單卷精簡本**（描述標 `Abridged in One Volume`），不是巴文克四卷全譯。比照
#      `simply-managing`／`gods-kingdom-through-gods-covenants` 兩個前例：**同作者（或授權
#      編者）的濃縮本算同一本結案**，已寫進該筆的 note。這條現在是慣例，不是個案。
#
# **同作者、書名接近、但確實是兩本書**——擋下來沒回填的，記在這裡免得每輪重查（都比對過
# README 的中文書名或章節才判的）：`software-developers-career-guide` 是 Sonmez 2017 的另一本，
# 不是 2014 的 Soft Skills；`emotionally-healthy-leader` 不是《建立高EQ的教會》；
# `when-good-men-are-tempted` 的 Bill Perkins 是牧師，不是寫 Die with Zero 的那位。
#
# 2026-08-15 加一筆：`wealthy-barber-returns`（David Barr Chilton）是 2011 的**續集**，
# 不是 personal-finance 想收的 1989 原典《The Wealthy Barber》——反查提名時撈到，讀 README
# （標「富足理髮師回來了」）確認。續集在、原典不在，反而成了那本排進 TOP20 的證據。
#
# 這張表上原本還有兩筆，2026-08-14 都被 Andrew 裁掉了——**書目判斷成立，但他決定不分**：
# `simply-managing`（不是 2009 的《Managing》，裁決以它代替原典）、`wujun-information-theory-40`
# （是《信息論 40 講》，不是《信息傳》，裁決當同一本結案）。留這段是為了讓下輪知道
# **這兩筆是「已裁決」而不是「沒查過」**，不要再提名成漏報。
#
# `how-to-be-a-high-school-superstar` 這筆的狀態 2026-08-13 變了一半：portal 補建了正名的
# `how-to-win-at-college`，所以 newport 的《How to Win at College》已回填成 owned；但同名
# repo 的**內容仍是** How to Win at College（README 標「深度學習力」、`_index.md` 的 Amazon
# 連結指向 How to Win at College），於是現在是**兩個 repo 裝同一本書**，而真正的 Superstar
# 仍然沒有站。NAME_COLLISIONS 那筆要留著，重複的 repo 是 SOURCING-DEBT 的事。
# 2026-08-20（Andrew 裁決一筆，表 7 → 6）：**NICNT／NICOT 系列代表卷改 `skipped`**——
# 「整套收不齊全，這系列省略」。這是唯一一筆準則③（站主自標「系列級缺口」），拿掉之後
# **準則③歸零，剩下的全是準則①與④**。與 Bauckham 那筆（2026-08-16 e2）的差別要記清楚：
# 那本是**找不到**（`unavailable`），這筆是**刻意不收**（`skipped`）——一筆代表一套書而非
# 一本，跟「勵志小品群」那種彙總列同一類。缺口本身沒有消失（新約側逐節學術註釋仍是 0 卷，
# 「羅馬書」全星系 54 處只對到 Stott 的 `message-of-romans`），只是不再佔採購清單版面；
# 日後要補是單卷單收（Moo《Romans》起手），**不要再把整套提名回 TOP20**。
# biblical-studies 因此從 3 本降到 2 本，第 5–6 格順位往前挪。
#
# 2026-08-20 第二段（同日 `/note-wanted` 對帳，資料源：GitHub 現況 1895 個 repo，前一輪
# 是 1901——repo 數往下走是因為中間刪過站，不是查漏了）：**上一版 TOP20 六格作廢四格**，
# wanted 6 → 2，這張表縮成 2 本。
#   a. **回填 4 本**（逐筆核對過 portal description 的作者欄）：`wealthy-barber`
#      （David Chilton，1989 原典；續集 `wealthy-barber-returns` 是另一個 repo，沒認錯）、
#      `versioning-in-an-event-sourced-system`（Gregory Young）、
#      `echoes-of-scripture-in-the-letters-of-paul`（Richard B. Hays）、
#      `summa-theologica`（Thomas Aquinas）。**personal-finance 與 data-systems 兩站歸零。**
#   b. **`summa-theologica` 是「疑似漏報」那節撈到的**（雙向 Jaccard 100%）：portal 用的是
#      舊英譯書名 Summa Theologica，wanted 寫 Summa Theologiae，精確比對差一個字母。
#      **不寫進 ALIASES**——照 2026-08-15 a 的前例，回填成 owned 之後它就離開 wanted，
#      alias 只會變成死條目。順帶把 `thomas-aquinas-summa-theologiae`（McGinn 寫的傳記）
#      與它的分別寫進該筆 note，免得下次又混。
#   c. **Goldingay 那筆維持 wanted，是裁決不是遺漏**：portal 的
#      `old-testament-theology-israels-faith` 是三部曲的第二卷，Andrew 2026-08-20 決定
#      繼續等整套（見 NAME_COLLISIONS 那筆）。因為進了 NAME_COLLISIONS，「先扣掉」與
#      「疑似漏報」兩節都不會再提名它，`先扣掉 = 0` 這條驗收才回得去。
#   d. **McGrath 那本在同一輪之內就建好站了**（`christian-theology-introduction`，
#      2026-08-19 建）——Andrew 答「已買到／建站中」，重跑一次腳本它就自己掉進「先扣掉」，
#      當場回填成 owned，**theology 站歸零**。這也是「權威資料源要現況不要快照」的又一個
#      實例：同一輪跑兩次 `gh repo list`，第二次才有這個 repo（1895 → 1886 是同時間
#      Andrew 也在刪站，數字上下跳動很正常，不要拿它當「查漏了」的訊號）。
#   d2. **Goldingay 三部曲的實際持有狀況**（2026-08-20 清點 ~/Downloads/BookMaterials）：
#      第二卷 Israel's Faith 已建站、**第三卷 Israel's Life 的 epub 已在手**、缺的是
#      **第一卷 Israel's Gospel（IVP 2003）**。所以這筆的採購動作是明確的：補第一卷。
#      同一個資料夾裡那份 `theology-of-the-old-testament-vol-1` 的 PDF **不是** Goldingay，
#      是 Walther Eichrodt 的 OTL 同名經典（1961 J. A. Baker 英譯），別混。
#   e. **作者反查（docstring 第 6 點）這輪 0 收穫**：McGrath 書櫃 2 本（配套讀本
#      `christian-theology-reader`、巴刻傳記 `j-i-packer-his-life-and-thought`），
#      Goldingay 書櫃 3 本（`biblical-theology-goldingay`、`ezra-nehemiah-esther-for-everyone`、
#      三部曲第二卷）——兩本想收的都真的不在。落空是結果，不是可以省略這關的理由。
#   f. 於是表只剩 **1 本**（Goldingay 第一卷），準則①（收了 biblical-studies 歸零），
#      準則②③④都沒有可排的。**全星系 78 站裡只剩這一站還有採購缺口**——TOP20 這個
#      人工區塊接下來的意義比較接近「最後一本的追蹤欄」，等新站開起來才會再長回來。
TOP20 = [
    ("old-testament-theology", "**全星系最後一本還沒收的書**。biblical-studies 站 owned 75／wanted 1——收了就歸零，準則①（同輪 Hays 回填成 owned、NICNT 系列改 skipped 之後，這是本站最後一筆）。**要買的是第一卷 `Israel's Gospel`（IVP 2003）**，不是整套：2026-08-20 清點手上的檔案，三部曲的第二卷 Israel's Faith 早已建站 `old-testament-theology-israels-faith`、第三卷 Israel's Life 的 epub 也在手，**只缺第一卷**；Andrew 同日裁決三卷齊了才結案，不以單卷收錄（見 NAME_COLLISIONS 那筆）。準則④的證據仍是全星系最弱的一批，誠實記著：舊約神學線已有 Brueggemann 的 `theology-of-the-old-testament` 與 Waltke 的 `old-testament-theology-waltke`，Goldingay 自己的單卷 `biblical-theology-goldingay` 也已收（他書櫃 3 本）——**不是空格，是想多收一種進路**；「舊約神學」全星系只有 **3 處／2 檔且全在本站**（2026-08-20 現查）。大部頭、無繁中"),
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

    **只有雙方都有「可比的」作者訊號時才裁決**——缺資料不該變成拒絕（那會把一堆真命中
    誤殺），所以回 None 表示「這關棄權，交給書名那關」，並在輸出裡催補該站的 `author` 欄。

    「可比」＝**同一條通道兩邊都有東西**（都有拉丁字，或都有漢字）。2026-08-13 之前只檢查
    「兩邊都非空」，於是**一邊漢字、一邊拉丁**的音譯對照被判成不符：business-strategy 的
    《孫子兵法》作者寫 `孫子`、repo 寫 `Sun Tzu`，兩邊都有作者卻沒有共同通道，
    結果 `art-of-war` 這個 2026-08-12 就建好的書站被擋在「先扣掉」外面，還被列進
    「作者這一關擋下的」當成買錯書預警——正好反了。沒有共同通道就是**沒有訊號**，
    不是**否定的訊號**；音譯沒有演算法可解（孫子／Sun Tzu、老子／Laozi），要判就得列表，
    而那條路在 ALIASES 已經走過一次，不值得為作者欄再養一張。

    這一關擋掉的是「原典很有名、後人拿同一個書名寫別的書」那一類。2026-08-10 之前
    matcher **只比書名**，作者純粹拿來顯示——於是 `understanding-the-bible`（Dorothy L.
    Johns 的函授查經課程）被判成 stott-note 想收的斯托得《認識聖經》，而那筆的
    當時的 `AUTHORS` 側表早就寫著 "John Stott"，資料就在檔案裡沒人用。
    接上之後側表整張搬進 bibliography 並刪除，NAME_COLLISIONS 也只剩
    「作者相同、repo 內容掛錯書」那一種需要人工兜底。
    """
    wl, wc = author_keys(want)
    rl, rc = author_keys(repo)
    if not ((wl and rl) or (wc and rc)):
        return None  # 沒有共同通道（漢字 vs 拉丁的音譯）＝棄權，不是否決
    return bool(wl & rl) or bool(wc and rc and (wc in rc or rc in wc))


# 版次尾綴：portal 的 description 書名常帶 `, Updated and Expanded`（HBR Must Reads
# 那批都是），wanted 那側只寫本名，精確比對就打不中。2026-08-14 的 `on Leadership`
# 與 `on Managing People` 就是這樣漏掉的——更糟的是連「疑似漏報」也撈不出來：尾綴
# 那三個詞全灌進 Jaccard 的分母，真命中只剩 57%，反而輸給同系列另一卷的假命中 75%。
# 改版與原版當同一本收（Andrew 一本書只建一個 repo），所以砍掉尾綴再比。
EDITION_TAIL = re.compile(r",\s*(updated|revised|expanded|new)\b.*$", re.I)


def norm_title(s):
    """書名正規化：砍版次尾綴與副標、砍冠詞、去標點——兩邊都過這關才能比。"""
    s = re.sub(r"[:：].*", "", EDITION_TAIL.sub("", s or "")).lower()
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
    #   old-testament-theology-israels-faith：repo 是 Goldingay 三部曲的**第二卷**
    #   （Israel's Faith，2006），biblical-studies-note 想收的是 2003 年第一卷起的
    #   **整套三卷**；第一卷 Israel's Gospel 與第三卷 Israel's Life 都還沒有站。
    #   Andrew 2026-08-20 裁決**繼續等整套**，不比照 simply-managing 那條「同作者
    #   濃縮本算同一本」——部分卷不是濃縮本，收到的內容就是缺兩卷（2026-08-20 加）。
    NAME_COLLISIONS = {
        ("change-your-thinking-change-your-life", "tracy-note"),
        ("how-to-be-a-high-school-superstar", "newport-note"),
        ("biblical-theology-goldingay", "biblical-studies-note"),
        ("erickson-christian-theology", "theology-note"),
        ("servant-leadership", "leadership-note"),
        ("understanding-the-bible", "stott-note"),
        ("old-testament-theology-israels-faith", "biblical-studies-note"),
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

    w(f"## 先收這 {len(TOP20)} 本\n\n")
    # 星系收得夠乾淨時，wanted 會少於表格容量——那時這節就不是「挑出來的」而是全部，
    # 講成「從裡面挑」會讓人以為還有沒排進來的書（2026-08-16 只剩 8 本時第一次發生）。
    covers_all = len({r["main"] for r in rows}) <= len(TOP20)
    w(
        (
            f"全星系的 wanted 只剩 {len(rows)} 筆，**這節就是全部**，順序即建議的採購與消化順序"
            "（薄的、起手容易的排前面）。"
            if covers_all
            else f"整份 {len(rows)} 筆太長，這是從裡面挑出來的採購順序，也是建議的消化順序（薄的、"
            "起手容易的排前面）。"
        )
        + "**這節是全檔唯一的人工區塊**——要改請編 `export-wanted.py` 的 "
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
            f"> ⚠ **這 {len(TOP20)} 本裡有 {built} 本已經建好書站了**（下表標 ✅），代表這張採購清單該重挑——"
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

    # 新鮮度戳記：生成物看起來永遠跟剛跑完一樣，不寫上去就沒人分得出今天算的還是三週前算的。
    text = stamp(o.getvalue(), "tools/export-wanted.py", _dt.datetime.now().astimezone().isoformat(timespec="seconds"))
    if len(sys.argv) > 1 and sys.argv[1] == "-":
        sys.stdout.write(text)
    else:
        OUT.write_text(text, encoding="utf-8")
        print(f"{OUT}: {len(rows)} wanted 筆 / {len(by_main)} 本、{len(existing)} 本已有書站、{len(multi)} 本多站共同")


if __name__ == "__main__":
    main()
