# Note 星系 enrich backlog(鳥瞰)

> [!IMPORTANT]
> **排序表已搬走（2026-08-09）。** 「現在該進哪一站」看 [DEEPEN-READY.md](./DEEPEN-READY.md)——那份是**生成物**，
> 每次重算（書單完成度、頁/書、溯源率、mastery 覆蓋率），不會過期。
> **本檔從此只當工作日誌**：做過哪幾輪、抓到什麼、結案了什麼。
>
> 為什麼要搬：這裡原本那張手寫排序表的掃描日停在 **2026-07-31**，而中間 68 站的
> bibliography 已經翻過好幾輪（光 2026-08-09 一天就有 13 站被回填成 `owned`）——
> 手維護的排序表只要一停更新就會把人導去錯的站。

指標=內容頁數 vs bibliography owned 書數(粗指標:頁少書多=落差大;精確落差要進站跑 `/note-check`)。

**慣例:單站的詳細 TODO 放該站根目錄 `TODO-enrich.md`(工作暫存,不 commit,完成即刪);本檔記開工/完工與該輪的發現。**

> 本檔管的是「站已存在但還沒寫完」。「**書有了但沒有站在管**」是另一個軸,見 [ORPHAN-BOOKS.md](./ORPHAN-BOOKS.md)（1b 節列開新站候選）。

## 進行中

（無）

> **舊輪次已清（2026-09-03）**：2026-08-04～08-28 的 60 多節工作紀錄（首輪 enrich 16 站、第二～六輪深化、
> BST 批次 1～7、導覽補齊輪 32 站、體檢、判層收官、年份清債、anchor 覆蓋、死鏈輪、孤兒書認領輪）
> 已從本檔移除，要看用 `git log -p -- docs/ENRICH-BACKLOG.md`。跨輪教訓已收進
> [MODEL-ROUTING.md](./MODEL-ROUTING.md) §四與 memory；本檔只留最近三輪。

## 首頁總覽補齊輪＋CI 修復（2026-09-03 Opus）——**三站補 Overview、四站刷新、checkup 新規則、21 站 Deploy 轉綠**

**起因**：Andrew 問「主題站與人物站有沒有共同元素？theology 首頁只有 Schools」。查下來契約其實明寫在
DESIGN §4.2——每一站首頁 = Overview（overview.ts）＋地圖（主題站 schools.ts／人物站 profile.ts）＋Sources
（bibliography.ts）；「Methods」不是缺的區塊，是 schools.ts 的 `kind` 決定的地圖標題（七站用）。
**真正漏的是 Overview，全星系恰好三站**：theology、biblical-studies、startup——08-27 導覽輪的前三站，
總覽那一步輪到第四站（career）才接上，之後兩個多月沒人發現，因為 `galaxy-checkup` 從來沒查過它。

**做了**：
1. 三站以現有五章導覽為底寫 `overview.ts`（主題站 Landscape／Threads／Verdict）並接線；bst 與 startup
   的導覽數字順手對現況（bst 107→127 本、startup 62→64，各補「架上參考」節）。
2. `galaxy-checkup` 新增四條：`no-overview`、`overview-unwired`、`overview-heading`（非標準英文詞彙）、
   `overview-stale`（writtenAt < enrichedAt）＋ `overview-placeholder`（template 佔位稿）。
   **第四條立刻抓到 17 站**：13 站是前兩天改了 overview 內容卻沒更新戳記（`rep()` 的 writtenAt regex
   只認導覽 md 的無引號寫法，overview.ts 是引號寫法——工具抓到我自己），已用實際最後編輯日補戳；
   **4 站是真的落後**（covey、grant、keller、drucker：內容在 08-24〜08-26 補過，總覽停在 08-11〜08-21），
   以現行導覽為底刷新（grant 十三→十五頁、待寫清單兌現兩筆；keller 補《非凡之地》第五件工具；
   drucker 補 1939 處女作與 1999 七項過期假設、新增 Verdict；covey 補家庭與原則中心兩次搬家、新增 Verdict）。
3. drucker 的 overview 標題從中文改成標準英文（背景／貢獻／主要論點 → Background／Contributions／Claims）。
4. note-template 加 `overview.ts` 佔位稿並接線（含「（待寫）」字樣讓 checkup 報 placeholder）；
   `note-new-station` skill 的 config 行與收工清單補上 overview。
5. **順手抓到前一輪自己留下的錯**：15 站分層帳裡有 9 處「N 本 tool、M 本 tool」重複——我在原本的 tool 數
   前面插了新數字、沒刪舊的（career 的 overview 甚至寫成「15 本 tool、8 本 tool、8 本 delegated」）。全數清掉。

**CI 修復（Andrew 同時提的）**：`gh run list` 掃 77 個 repo，**24 個最新 Deploy 是紅的**，21 個同一根因——
08-30「feat: link the nav back to the sister handbook」那批 commit 的 `extraNav` 單行寫法沒過 prettier，
Deploy 的 **Format check** 步驟就停在那裡（後面的 Build／Pages 全沒跑，站台停在 08-30 前的版本）。
另 3 個（keller、spiritual-formation、thinking）是 08-26 的舊失敗、之後已綠，不用動。
修法：21 站 pull → `npm run format` → commit → push，19 站當場轉綠、2 站在跑。
**為什麼我前兩天推的站沒紅**：我的流程是 format → commit → `pull --rebase` → push，rebase 把 Andrew 那個
未格式化的 commit 拉進來時已經在 format **之後**，所以第一次 push 的 Deploy 其實紅了（growth 15:47 那次），
是下一輪再 format 才順手蓋掉——**流水線要改：rebase 之後再跑一次 `format:check` 才 push**。

收工：checkup 75 站 0／0／0（含新規則）、tier-audit 六類 0、CI 除 uncle-bob 與剛推的四站在跑外全綠。

## 認領後對帳輪（2026-09-03 Opus）——**導覽數字 15 站歸零、年份 65→7、孤兒書 0、工具盲區一支**

織入輪之後剩的三件全部結案，加上一支工具修正。

**① 導覽數字對帳（15 站）**：GUIDE-DRIFT 強訊號 14→**0**（另補弱訊號裡的整站宣稱 schwager
「站上十三頁」→十二，實查 12 頁、無刪頁紀錄，是寫導覽時就數錯）。改法照上一輪定的規矩：
「收完 N 本」改現數並括號註明「其中 M 本是認領上架的參考書，尚未開頁」；每站在 03 補一節
**架上參考**逐本列出認領書（最長 personal-finance 19 本、career 9 本、learning 8 本），
並寫明「上面各組的本數不含這些」；03 標題本數、分層帳 tier 數、01/02/04/05/overview 的
規模數字全對現況；writtenAt 推 2026-09-03。

**工具抓不到、靠手查抓出來的三筆**（比數字本身值錢）：
1. **security 的「十四本全部已挖、零引用歸零」變成假的**——認領輪上架的 Rootkits 沒有頁引它，
   原句在 03 與 overview 各一處，都改成「十五本裡十四本已挖，未挖的那本是認領新上架的」。
2. **personal-finance 的豁免率 48%** 若把認領的 19 本算進去會跳到 64%，但那是「上架還沒讀」
   不是「判過、決定不挖」——**兩種豁免不該混算**，導覽改成分開陳述。
3. **history 的 delegated 3→4** 是富蘭克林自傳改判給 habits 的結果（頁開在那裡），
   在 03 補記這筆跨站異動。

**② 缺 year 65→7**，而且先修了工具的盲區：`export-missing-years.py` 找的線索是
`book-cover` shortcode 的 `date="…"`，**現行 1781 本書 repo 一本都沒有**，而 frontmatter 的
`published:` 有 1779 本——工具因此長期回報「0 筆有線索」，填年份的人看到 0 就不會去查。
補上 `published_dates()` 後線索從 0 筆變 **59 筆**。58 筆已填（腳本插在 `slug:` 之前，
沿 apply-claims 的欄位順序），照 Andrew 的豁免用線索年，但**能確認初版年的用初版年**——
覆蓋線索的 13 筆：Ryken《Written in Stone》2003（線索 2010 是重印）、Bishop《The Long Win》2020
（線索 2024 是二版，而且它是 spine）、Halvorson 2015、Corey《Theory and Practice》1977（線索 2012 是第九版）、
McCormack 1987、Schäfer 1998、Buscaglia 1982、Adams 2004、QBQ 2001、李起周《말의 품격》2017、
齋藤孝 2019、Silén 2022、McKay《Self-Esteem》1987、Maggio《How to Say It》1990。
**剩 7 筆全是已裁決的留白**：NICNT 系列列、tracy 兩筆彙總列、greene 彙總列、learning 的
unavailable、`bible-atlas`（本機無 repo）、以及新裁決的一筆——愛默生《Beautiful Thoughts》
是**公版作家的後人彙編**，彙編年放上時間軸會把十九世紀作者標到二十一世紀，比留白更誤導。
後兩類已寫進工具的「補不上來」清單。

**③ Berne《人生腳本》認領**：走 `apply-claims.py` 進 relationships「溝通與衝突」組、tool、
初版 1972（repo `published` 2018 是再版）——**孤兒書 1→0，書庫第一次全部有站在管**。
導覽的本數與分層帳同步改（57→58、tool 10→11），架上參考那節補一段講它與《人間遊戲》的分工。

收工：checkup 75 站 0／0／0、tier-audit 六類 0（2252 本）、GUIDE-DRIFT 強訊號 0、孤兒 0、
死鏈 slug/anchor 0、全部 commit＋push、無髒 repo。

## 導覽織入輪（2026-09-02 Fable）——**21 本新脊梁織進 15 站導覽，數字對帳 34 筆，enrichedAt 補蓋**

**起因**：08-28 兩批升層開了 19 頁、升了 21 本 tool→spine，導覽完全不知道它們存在——12 站連作者名
都沒出現。工具抓不到：tier-audit 只要求 support 書被導覽帶到（脊梁的債用概念頁還）；guide-stale
也沒亮，因為**兩批升層都沒蓋 `curation.enrichedAt`**（起草代理照契約不動 bibliography，主會話
收尾升了 tier 卻漏了流水線第 5 步）。是 `export-guide-drift.py` 靠數字撞出來的。

**做法（15 站，每站同一套）**：03 書架帳該組加一段（材料就是新頁的引言與 core，先有頁再升層的
規矩寫進去）；04 爭議在對的官司補一段（bright-sided 進成功學官司並新開「贏到的是什麼」、Loeb 進
集中 vs 分散、Volf／Hauerwas 進教會與世界、Taylor 進護教頭心之爭、Alexander 進語彙 vs 補丁、
Brooks 進小函式 vs 深模組、Ury 進談判內戰、Weinberg 進說服 vs 操縱、Stout 進界線 vs 無條件的愛、
Franklin 進意志力官司、Smith 進律法主義官司、Kleinman 進口音）；新增「架上參考」一節把認領輪
上架、仍是 tool 的書逐本列出（communication 35、investing 42 最長），並寫明「上面各組本數不含」；
01／02／05／overview 的規模數字全對現況；writtenAt 推到當天、enrichedAt 蓋 2026-08-28（頁進站日）。
站：growth（3 本）、wellness（2）、communication（2）、theology（3）、relationships、habits、
life-meaning、spiritual-formation、thinking、philosophy、design-patterns、clean-code、system-design、
investing、leadership。收工：15 站 build 綠、tier-audit 六類 0、checkup 75 站 0、導覽新增連結
腳本驗證全實存、GUIDE-DRIFT 強訊號 48→14。

**教訓三條**：①「收完這 N 本」不能只把數字換大——認領的書是上架未讀，句子要說明白，定成
「N 本（其中 M 本是認領上架的參考書，尚未開頁）」；②drift 工具只看「收完／寫完／互相連結」
那幾句，**03 的標題本數、分層帳 tier 數、02 的「整組唯一的 spine」這種句子都不抓**，要手查——
growth 的 02 就有一句「Halvorson 是整組唯一的 spine」被三本新脊梁打臉；③批次輪的收尾清單要加
一行「蓋 enrichedAt」。另記一筆帳目不符：第一批記「Dorsey《The Little Book That Builds Wealth》
補 anchor 完成」，實查 investing 沒有任何頁引它、tier 仍 tool——導覽照實寫成架上參考，補 anchor
那筆算未做。工具面：philosophy 的 `A Secular Age` 認領後改 delegated→theology，導覽兩邊都記了。
Opus 剩的 14 站數字對帳見「進行中」。
