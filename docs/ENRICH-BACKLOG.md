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

> 本檔管的是「站已存在但還沒寫完」。「**還沒有站**的人物／主題」是另一個軸,見 [COVERAGE-GAPS.md](./COVERAGE-GAPS.md)。

## 進行中

（無）

## Opus 輪：出版年跨站一致性（2026-08-26）——**新增第五份生成盤點**

第二輪 35 筆結案後回頭清 MISSING-YEARS，過程中發現一類**現有四份盤點全都抓不到**的錯誤：
同一本書被多站收錄時，各站的 `year` 可以彼此矛盾而永遠沒人發現。tier-audit 看 tier、
orphan-books 看 slug 存不存在、missing-years 看有沒有填——**填錯不會被抓，只有沒填會**。
而 `year` 是首頁年代分佈圖的軸，兩站對同一本書填不同年，圖上就落在兩個年代。

於是新增 `tools/export-year-conflicts.py` → `docs/YEAR-CONFLICTS.md`，並掛進
`refresh-galaxy-docs.sh`（四份變五份，`--check` 的 TRACKED 也一起加）。首跑：
**1925 個有 slug 的條目，23 本跨站矛盾、15 筆缺 year 但別站有現成答案。**

本輪處理（全部 11 站已 push）：

- **零判斷補漏 14 筆**：別站同 slug 已填 year，直接抄。剩下 1 筆（`wan-weigang-scientific-thinker`）
  因為來源自身就有兩個版本而留著。缺 year 從 130 → **116 筆**。
- **解衝突 11 筆**：只改「該站填的明顯是後出版次、schema 要初版年」而且初版年是公認事實的——
  `effective-executive` 1967→1966（三站）、`high-output-management` 1985→1983、
  `refactoring` 2018→1999、`nonviolent-communication` 2003→1999、
  `cracking-the-coding-interview` 2015→2008、`turn-the-ship-around` 2013→2012、
  `small-giants` 2006→2005、`judgment-in-managerial-decision-making` 1994→1986、
  `bigger-leaner-stronger` 2014→2012。矛盾 23 → **14 本**。

**刻意不動的 14 本**，兩種原因，都寫進工具的 docstring 當判準：

1. **不是債**——`message-of-romans`：biblical-studies-note 拿它當「聖經信息系列（全 52 冊）」
   的代表列填 1968（系列起始年），stott-note 填 1994（該卷初版年）。**兩邊都對**。
   工具因此連 `title` 一起印，就是為了讓這種情況一眼看得出來。
2. **不能無腦取小**——早年份可能指的是同名的錄音課程或講座，書本身晚很多年才出。
   `psychology-of-selling`（1985 錄音課程 vs 2004 書）與 `selfless-way-of-christ`
   （1981 講章發表 vs 2007 Orbis 成書）就是這型；`investment-valuation`（1994/1995，
   而我查不到哪個是初版）、Tracy 幾本小書、三本麥肯錫日譯本、萬維鋼兩本、
   `soft-skills-thirty-letters`（順帶發現兩站的 title 與書 repo 標題不一致）同理。
   **這些寧可留白／留矛盾，也不要寫進一個會餵年代圖的欄位。**

## Opus 輪：全星系體檢（2026-08-26）——**75 站首次一次掃完，checkedAt 全面歸位**

體檢戳記本來是 19 站過期、42 站從未蓋過。逐站手動不可行，所以先寫工具：
**`notes-core/tools/galaxy-checkup.py`**（已固化進 tools，不留 scratchpad），把 `/note-check`
§1 的五個指標與 §2 可機檢的項目一次跑完全部 75 站。

**首跑結果：blocker 0／warn 61／nit 332**，當場全部修掉：

| 發現 | 數量 | 處置 |
| --- | ---: | --- |
| `no-response`（缺 `:::response`） | 56 | **behaviour-interview-note 55 頁＝整站從沒導入雙層模型的回應層**（同為雙集合站的 system-design 是 67/67 全有）；business-strategy 1 頁。已補空塊 |
| `oneway-related`（單向邊） | 323 | 26 站，腳本一次補完（agile 71／leadership 36／design 35／learning 33 最多） |
| `orphan-page`（頁不在任何 roadmap） | 20 | growth 3／learning 6／life-meaning 3／relationships 3 排進既有 roadmap；pastoral 5 頁隨下一列一併處理 |
| `no-roadmap`（分類沒有 roadmap） | 4 | pastoral-psychology 四個分類只有 mastery 沒有 roadmap，已補齊（它的 5 頁孤兒同時解決） |
| `roadmap-planned`（roadmap 指未寫頁） | 9 | **不是 bug**——collins／grant／jung 等站的 planned 節點，本來就是 backlog |

- 兩筆誤報在修工具時清掉：`content.config.ts` 的「3 行 factory」不是數行數（要看有沒有
  `defineNoteCollections`、有沒有自寫 `z.object`）；`related` 的第四種寫法是**帶引號的單行陣列**，
  沒去引號會把整站報成死指（thinking 347 筆、writing 146 筆全是這個）。
- 收工：30 個改動站 format＋lint＋build 全綠 → 75 站蓋 `checkedAt: 2026-08-26` → 全部 build 再驗一次 → 逐站 commit＋push。
- **這輪體檢涵蓋什麼**：版本 currency、site.config 良構、首頁契約、content.config factory、
  divergence（站上自建 layouts/components/…）、分類三者一致、導覽時效、roadmap／mastery 覆蓋與死指、
  schema、書本位的 slug／anchor／label 分隔號、`:::response`、entity 殘留、related 雙向。
  **不涵蓋**：§2.5 的「抽驗防杜撰」（具名事實回源 grep）——那是判斷不是掃描，仍在每輪 enrich
  收工時逐頁做（今天 BST 五批就是這樣驗的）。看到 `checkedAt=2026-08-26` 要照這個範圍讀。

## 第二輪選題清單（2026-08-26 開出）——**同日 Opus 輪全數結案**

判層殘餘 109 本全數清零（15 站）後，spine 裁決直接生成這份單。共 **35 筆＝26 頁新頁＋9 筆補 anchor**，
**已於 2026-08-26 由 Opus 逐站清完並全部 push**（Andrew 當場指示「不用，直接做」，略過過目步驟）。
收工狀態：`tier-audit.py --all` 全星系 1922 本藏書，真欠債／空頭支票／漏接／文資不符／衝突／未判層**六類全數 0**。

逐站落點（每站都跑完站掃描→單向邊補齊→roadmap+mastery→format/lint/build→查證具名事實→單行英文 commit→push）：

| 站 | 產出 | commit |
| --- | --- | --- |
| problem-solving-note | 2 新頁＋4 補 anchor | bulletproof 七步、look-see-imagine-show |
| maxwell-note | 2 新頁＋1 補 anchor | 21 法則、團隊 17 法則 |
| communication-note | 1 新頁＋1 補 anchor | 三種對話 |
| relationships-note | 5 新頁＋1 補 anchor | Gottman 七原則、Hold Me Tight、怎麼說孩子才會聽、全腦教養、獨自打保齡 |
| cloud-note | 3 新頁＋1 補 anchor | 為婚姻立界線、Integrity、Trust |
| growth-note | 2 新頁 | The Formula 五法則、Insight |
| learning-note | 2 新頁 | Dehaene 四支柱、學習的王道 |
| life-meaning-note | 3 新頁 | 凝視死亡、最後 14 堂星期二的課、值得活的人生 |
| de-botton-note | 3 新頁 | 擁抱似水年華、旅行的藝術、工作！工作！ |
| liurun-note | 1 新頁＋1 補 anchor | 關鍵躍升 |
| history-note | 2 新頁 | 大崩壞、絲綢之路 |

十一站全部蓋上 `enrichedAt: 2026-08-26`。原始清單保留在下方供追溯。

**補 anchor 型（不開新頁，把原典掛進既有頁；起草者要先核對頁面主張與原典對得上）**：

| 站 | 原典 | 掛進哪頁 |
| --- | --- | --- |
| problem-solving | 金字塔原理（Minto） | pyramid-principle-in-writing（現引 BCG＋麥肯錫寫作術） |
| problem-solving | 真正的問題你想通了嗎（Gause & Weinberg） | reframe-the-problem／spot-the-real-issue |
| problem-solving | Say It with Charts（Zelazny） | good-charts-that-persuade（現只引 Berinato） |
| problem-solving | The McKinsey Way（Rasiel） | mece-and-logic-tree／build-and-verify-hypotheses |
| maxwell | 領導力的 5 個層次 | five-levels-of-leadership（現引 2.0 合訂本） |
| relationships | Attached 依附（Levine） | attachment-and-attraction（**現引搭訕書**，科學正典缺席） |
| communication | The Storytelling Animal（Gottschall） | brain-on-story（現引 Storr） |
| cloud | 成長神學（How People Grow） | grace-truth-time（現引改變帶來醫治） |
| liurun | 商業簡史 | transaction-cost（現引 5 分鐘商學院） |

**新頁型（26 頁）**：problem-solving 2（Bulletproof 七步解題、餐巾紙的背後視覺化解題）；
communication 1（Supercommunicators 三種對話與配對）；maxwell 2（21 法則總綱、團隊 17 法則）；
relationships 5（Gottman 七原則、Hold Me Tight EFT、怎麼說孩子才會聽、全腦教養、獨自打保齡）；
cloud 3（為婚姻立界線、Integrity、Trust）；growth 2（The Formula 成功的科學、Insight 自我覺察實證）；
learning 2（Dehaene 學習四支柱、學習的王道劃小圈）；life-meaning 3（凝視死亡、最後 14 堂星期二的課、
值得活的人生）；de-botton 3（擁抱似水年華、旅行的藝術、工作！工作！）；liurun 1（關鍵躍升）；
history 2（大崩壞、絲綢之路）。

## Fable 輪：留單結案＋判層收官（2026-08-26）

**兩筆留單當日結案**：

- **peck《與心靈對話》**：地面真相翻案——repo 不是不存在，是躺在 `books-management/archive/`
  （內容完整、被刻意下架；Opus 只搜了 books-done）。裁決降 support：中段由首部曲深挖＋
  《心靈成熟的旅程》兩頁承重，書站若回歸 books-done 再議升層。**留單前提不完整的教訓：
  查書要連 archive 一起搜**。
- **philosophy 導覽問題三**：整節重寫非只改一句——節標題改「從 Sandel 的一人講堂，到三造對質」、
  開頭改「十頁裡五頁骨架來自 Sandel，依賴稀釋成一半但座標仍是他畫的」、判讀改「多數仍在德性／
  共善側發言，但已不是獨白」，並把柏拉圖兩頁補進「對手到庭」清單；「Lukes 是唯一非 Sandel 聲音」
  一併修掉。

**判層殘餘 109 本（15 站）全數清零**：growth 20、learning 13、problem-solving 9、communication 10、
maxwell 7、relationships 10、cloud 7、de-botton 5、life-meaning 9、liurun 5、history 6、fengtang 3、
image-style 2、newport 2、pastoral-psychology 1。每站裁決 JSON 走 apply-tiers → tier-audit →
build → 單站 commit＋push；`--verify` 兩份稽核實作對帳一致。

- 裁決要點：**原典補 anchor 型 9 筆**（最傳神＝relationships 的 attachment 頁引搭訕書、科學正典
  《依附》缺席；problem-solving 四本麥肯錫／Minto／Weinberg 原典的概念頁全引衍生書）；
  **重複書系嚴判**（fengtang 三本全 support、newport 學生二書 support、liurun 網路時代舊作 support、
  life-meaning 臨終回憶錄三本取一［Morrie spine，當呼吸化為空氣與最後的演講 support］）；
  **人物站正典從寬**（maxwell 21 法則／5 層次／團隊 17 法則、de-botton 普魯斯特／旅行／工作、
  cloud 婚姻界線／Integrity／Trust／成長神學）。
- **又抓到一筆書庫重複建站**：《刻意進化》＝ `mental-fitness` 與 `learned-excellence` 同書兩 repo；
  learning-note 的 slug 已改指正本（life-meaning 已挖的那個），`mental-fitness` 將出現在
  ORPHAN-BOOKS 孤兒清單——**books-management 端的合併／刪除留給 Andrew**。
- 抽查 Opus 批次 3～7 產出：四頁跨四批、十筆事實獨立回源 grep 全中，通過。

## Opus 輪：導覽事實對帳（43 站）＋BST 批次 3（2026-08-26）

**導覽對帳**：第一次對 43 個有導覽的站做機器對帳（腳本檢四件事：站內 `../concepts/` 連結是否有檔、
`furtherReading` 的書 slug 是否在該站 bibliography、anchor 目錄是否實存、label 有沒有 em-dash）。
**結構層 43 站全乾淨、零死鏈**——導覽從 2026-08-15／21／24 三波寫下來沒有爛掉。
數字層抓到的多是分區小計（誤報），逐筆核完只有四站的**站級**宣稱過期，共改 11 處：

- `agile-note`：站上六十一頁／六十四頁 → 六十六頁；「還沒被挖進站的那七本」→ 三本（ch3 帳已是 12 挖／3 未挖）；ch5「已收未挖的四本」→ 三本。
- `philosophy-note`：站上二十四頁 → 三十四頁；「二十八頁裡有十七頁」→「三十四頁裡有十八頁」（東方思想四頁 → 六頁，算式自洽）；另兩處「十五頁」與 ch4「十七頁／政治六頁」一併對齊成十八頁／七頁。
- `writing-note`：ch1／ch2 的「站上三十八頁」→ 四十一頁。
- `tracy-note`：ch1「站上二十五頁」→ 二十七頁。

原因一律相同：導覽寫完的**同一天**又跑了 enrich，頁數當場過期而沒回頭改。查「導覽日之後才新增的頁」
嚴格比對是 **0 站**，所以這批只是數字債，沒有內容債（唯一的例外＝上面留單那條）。
`behaviour-interview`／`system-design`／`design-patterns` 的「五十頁／六十七頁／六十頁」是
概念頁＋題型頁的合計，正確，未動。

**BST 批次 3**（biblical-studies-note，清 2026-08-06 起掛著的「其餘 38 卷」系列債）：
依 COVERAGE-GAPS 同一條規則（作者沒有人物站的卷冊逐本列進本站；Stott 自己那 6 卷歸 stott-note，
該站 `bst/` 分類已有頁）補列 6 卷並各寫一頁——約書亞（Firth，誰的地／誰是以色列人）、
撒母耳（Evans，權力與大衛之約）、約伯（Atkinson，旋風裡的回答）、傳道書（Kidner，拆毀以重建）、
以賽亞（Webb，一個異象與「你到底依靠誰」）、約翰福音（Milne，被釘的王）。
站況 75→81 本、51→57 頁，稽核四違約全零，`enrichedAt` 蓋 2026-08-26。

- 驗收：六頁的具名事實逐筆回源 grep 全中（聖彼得廣場的十點五十分／十一點正、新約引以賽亞 66 次、
  約翰序言十八節 44 個動詞、尼西亞 325／迦克墩 451、亞基人戶篩、十章 36 ～ 37 的希伯崙反證等）。
- **踩到一個新坑**：補 `related` 單向邊的腳本吃不下「多行括號」寫法（`related:\n  [\n ... \n  ]`），
  誤把新 slug 以破折號行接在括號後面 → YAML 壞掉。7 個檔已修回單行括號並過 `format:check`。
  以後改 related 的腳本要三種寫法都吃：單行括號、**多行括號**、YAML 破折號清單。
- 本輪新列 6 卷沒填 `year`（書庫 frontmatter 只有再版日期，不是原版年份），會出現在 MISSING-YEARS。

## Opus 輪：BST 批次 4（2026-08-26，同日續批）

再照同一條規則補列 6 卷、各寫一頁，補齊「四福音」與「智慧三卷」，並開出三卷大先知／啟示：
以西結（C. J. H. Wright，榮耀離開與歸回、守望者、識別公式）、但以理（Wallace，獸的國與人子的國、
以全書合一性回應馬喀比時代說）、耶利米（Kidner，「反抗潮流」）、箴言（Atkinson，把敬虔放進工作服）、
馬太（Green，五大教導＋第十三章樞紐）、馬可（English，從行神蹟者到受苦僕人）。
站況 81→87 本、57→63 頁，稽核四違約仍全零。

- 驗收：逐頁具名事實回源 grep（異教卡車、識別公式七十次、二十九 17 的例外日期、亙古常在者、
  奧古斯都式的「福音」、毛勒論背十架、五段收尾公式與十三 57、柯德納「工作服」、莫諾／波金霍恩、
  杏樹枝 _šāqēd_／_šōqēd_、布賴特「神的話已成就」）。
- **抓到自己的漏**：耶利米頁的開場（「反抗潮流」出自《天路歷程》私心先生）與結尾（第五十二章、
  約雅斤獲釋）分別出自作者序與跋，兩者都不在原本掛的兩個 anchor 裡；箴言頁的「肖像／草圖」也
  出自 `01-the-portrait-of-wisdom` 本節而非其子節。**已補 anchor**——教訓：寫完要回頭核對
  「正文用到的每一段，是否都落在掛出去的 anchor 裡」，不能只驗 anchor 目錄存在。
- 掃描腳本已修好上一輪那個坑（多行括號的 related 一律正規化成單行），本輪 18 條單向邊一次補完。

## Opus 輪：BST 批次 5（2026-08-26，同日第三批）

再補列 6 卷、各寫一頁：利未記（Tidball，聖潔地圖與贖罪日）、列王紀（Olley，用敗局講道的歷史）、
何西阿（Kidner，用婚姻作比喻）、哥林多前書（Prior，十字架的道與教會體制）、
哥林多後書（Barnett，軟弱中的能力）、彼得前書（Clowney，寄居者的活潑盼望）。
站況 87→93 本、63→69 頁，稽核四違約仍全零。

- 驗收：逐頁具名事實回源 grep 全中（凱洛格 1891 的「氣餒的態度」、索雅論命令句密度、詹森的聖潔
  等級表、阿撒瀉勒不是給魔鬼的祭、「藉歷史來傳道」與 561 年、以未米羅達與王上八 50、何西阿的
  痛苦階梯與「因我是神，並非世人」、巴瑞特論羅馬書／哥林多前書、_apatheia_ 與艾略特、
  _Power in Weakness_ 與十三 14 的三一祝福、史畢克論教牧書信典範、「巴比倫」＝羅馬與主後 63 年）。
- 本輪起改掉一個壞習慣：**寫完先回頭核對「正文用到的每一段是否都在掛出去的 anchor 裡」**，
  批次 4 那兩筆漏掛就是這樣抓出來的；批次 5 的六頁在寫作當下就按這個規矩掛齊。

## Opus 輪：BST 批次 6（2026-08-26，同日第四批）

再補列 6 卷、各寫一頁：路得（Atkinson，「神的安排」與 _go'el_）、約拿（Nixon，比喻形式的先知式
神諭）、耶利米哀歌（C. J. H. Wright，哀痛的語言與三明治中央的盼望）、雅歌（Gledhill，文學性的
自然解讀）、歌羅西與腓利門（Lucas，危險來自教會內部）、約翰書信（Jackman，回到基本真理上）。
站況 93→99 本、69→75 頁，稽核四違約仍全零。

- 驗收：逐頁回源 grep（柏格曼兩部電影、亞斯她錄、脫鞋吐唾沫、便西拉智訓、王下十四 25、
  齊休姆〈祢信實何廣大〉、子拿韻與離合體、奧康納的「霧裡看花」、「一把失去鑰匙的鎖」與史溫本、
  萊富特 1875 與胡克的反向讀法、耶柔米記的老約翰、克林妥與 _dokein_、庇哩亞型會眾）。
  **一筆自查**：路得頁引的彼德森「沒有兒子就等於生命完結」不在導論而在小叔／救贖者那章——
  該章本來就是第二個 anchor，所以掛得住；但這再次印證批次 4 立下的規矩要每頁都跑。

## Opus 輪：BST 批次 7（2026-08-26）——**系列債結案**

最後 8 卷一次補完、各寫一頁：創世記 BST 版（Atkinson／Baldwin）、以斯帖（Firth）、
以斯拉與哈該（Fyall）、約珥／彌迦／哈巴谷（Prior）、俄巴底亞／那鴻／西番雅（Bridger）、
瑪拉基（Adam）、撒迦利亞（Webb）、彼得後書與猶大書（Lucas／Green）。
站況 99→107 本、75→83 頁，稽核四違約仍全零。

**至此 2026-08-06 掛出的「BST 其餘 38 卷」系列債全部清空**：52 冊裡 46 卷逐本列在本站、
Stott 自己那 6 卷在 stott-note，全系列每一冊都有頁承載。

- **創世記那一卷的重疊判斷（本輪唯一的選題判斷）**：本站已有 Walton 的功能性創造與 Waltke 的
  toledot 兩頁，所以新頁**不重寫創造與世系**，改切 Atkinson／Baldwin 的獨有角度——
  十二 1 ～ 3 作為全書樞紐、論戰式神學、族長的考古與年代背景、「亞伯拉罕不是游牧民族」，
  並在正文明文連回那兩頁分工。
- 驗收：逐頁回源 grep（裘比斯與 _bōʼ_ 的雙關、瑪拉基「我的使者」與 460 ～ 400 年、撒迦利亞的
  五十五公里與「破漏的囊」、拿哈瑪尼與七十四個利未人、卡魯臺地的蝗蟲與馬西尼沙、伍茲與阿奇米爾
  論那鴻書、孟頓與塔西圖斯、《埃努瑪·埃利什》與吾珥的月神南納）。
- 一天之內五批（3 ～ 7）共 32 卷、32 頁：biblical-studies-note 從 75 本／51 頁長到 107 本／83 頁，
  每一批收工都跑同一套驗證網（回源 grep → 站內掃描 → 補雙向邊 → format/lint/build → tier-audit）。

## 兩站連打（2026-08-26 完成，Fable session 第十五〜十六站：startup＋personal-finance）

判層 54 本一次套用（startup 29：7 spine／11 support／4 tool／7 delegated；personal-finance 25：
8 spine／10 support／1 tool／6 delegated），兩站收工稽核全零。頁數：startup 44→51（創辦人兩難／
顧客開發／閃電擴張／Traction 靶心／Venture Deals／Rework／開卷管理）、personal-finance 29→36
（4HWW／F-You Money／Die with Zero／ERE／巴比倫／快車道／自動理財）＋Ramsey 原典補 anchor 進
baby-steps 頁（時程差異經核對相容）。

- 驗收：15 個代理共約 75 項具名事實／數字回源 grep 全數命中。兩筆術語修正：die-with-zero 的
  「記憶股息」改從書譯「記憶紅利」；fastlane 五誡書中作 **NECST** 非通行的 CENTS——代理照文本寫，
  又一次接住指揮層的預設。babylon 的「財富像一棵樹」為頁面逐字引文（抽驗樣式假警報）。
- 兩站單向邊共清 24 處；兩站首蓋 curation 戳記（僅 enrichedAt）。

## 四站連打（2026-08-26 完成，Fable session 第十一〜十四站：business-strategy／fromm／habits／marketing）

判層 51 本一次套用（BS 17：7 spine／1 support／9 delegated；fromm 6：5 spine／1 support；
habits 13：5 spine／5 support／2 tool；marketing 15：8 spine／4 support／1 tool／2 delegated），
四站收工稽核全零。裁決亮點：**blue-ocean 依 MODEL-ROUTING 明文推翻自動 delegated、判 spine 於
business-strategy 並開頁**（該文件點名的「判斷疊判斷」教案例正式兌現）；marketing 的 storybrand／
permission／100m-offers 三本原典判 spine 後以「補 anchor 進既有頁」兌現（頁在、原典沒被引的型態，
比開重複頁便宜且正確）。

頁數：business-strategy 31→38（Porter 五力／價值鏈／策略核／五問級聯／孫子／藍海／SPIN）、
fromm 10→15（開新分類「宗教與象徵」；思想自傳／釋夢／論不服從／精神分析與宗教／希望的革命）、
habits 28→33（Wood 情境摩擦／意志力科學／War of Art／Stolen Focus／刻意休息）、
marketing 27→32＋3 頁補強原典 anchor（Sharp／奧格威／STEPPS／成長駭客／峰值體驗 MOT）。

- 驗收：wave 1＋wave 2 共 22 頁新開＋3 頁補強，約 110 項具名事實／引句回源 grep 全數命中
  （幾筆初判查無均為抽驗 grep 樣式問題——孫子譯注本用譯文非古文、瘋潮的「社交身價」正是章名）。
- 補強代理順帶抓到兩筆忠實紀錄：permission 頁的「33%／1000 倍」出自 this-is-marketing 的今昔對比
  （原典數字為 35–36%／1800%，引用歸屬正確不改）；StoryBrand 2.0 已把嚮導特徵 authority 改為
  competency（頁面沿用通行舊版措辭，原典章節有明文說明修訂）。
- habits 站 related 是 YAML 破折號格式——補邊腳本已升級為雙格式（close-scan2.py 型）。
- BS／fromm／habits／marketing 四站單向邊共清 49 處；BS 與 fromm 首蓋 curation 戳記。

## career-note 批次 2（2026-08-26 完成，Fable session 第十站——本輪存量最大的裁決批）

42→49 頁。判層 23 本（7 spine／9 support／6 tool／1 delegated）。裁決要點：刻意練習軸由既有兩頁
承重（talent-is-overrated 判 support）、work-optional 的 FIRE 軸偏 personal-finance 但該站未收
（support 一句定位）、工程師手冊群與 HBR guide 照合輯決議判 tool。7 頁新開：求職轉職 3
（Ibarra 轉行／聯盟世代／別自己一個人吃飯）、意義方向 2（決定性的十年／無路之路）、
職涯資本 1（Godin 關鍵人物）、通才跨域 1（Pink 感性時代六感）。收工稽核全零：未判層 23→0、真欠債 7→0。

- 驗收：40 項具名事實／研究／案例回源章節 grep 全數命中（零杜撰）、96 組 book/anchor 零死鏈、
  溯源掃描空、entity 零殘留。
- 用腳本一口氣清掉 24 處 related 單向邊（含既有頁遺留＋本批跨頁鏡射），全站 49 頁雙向歸零。

## gardner-note 批次 2（2026-08-25 完成，Fable session 第九站）

8→11 頁。判層 5 本（3 spine／2 support——MI 應用彙編由 theory＋myths 兩頁承重、真善美續章掛
disciplined-mind 頁作延伸）。3 頁新開：APP 世代（賦能 vs 依賴，認同／親密／想像三軸）、
學習的紀律（真善美三範例深挖）、領導心智（認同故事與反故事）。收工稽核全零：未判層 5→0、真欠債 3→0。

- 驗收：17 項具名事實／研究／術語回源章節 grep 全數命中（零杜撰）、34 組 book/anchor 零死鏈、
  溯源掃描空、entity 零殘留、related 全站雙向。本站首蓋 curation 戳記（僅 enrichedAt）。

## biblical-studies-note 批次 3（2026-08-25 完成，Fable session 第八站——單書開頁部分）

44→51 頁。判層 20 本（7 spine／8 support／4 tool／1 delegated）。裁決要點：basic-christianity 與
邪惡與上帝新世界的姊妹站（stott／nt-wright）皆判 support 不挖，本站同判 support 不互踢；
Beale 聖殿專論作既有聖殿主線頁的深化源、work-matters 由 gospel-and-work 頁承重、Waltke／Goldingay
的 OT 神學軸由 Brueggemann 新頁＋既有 toledot 頁承重；IVP 背景註釋等 4 本照既有「工具書不立頁」
決議判 tool。7 頁新開：釋經方法 3（卡森釋經謬誤／Alter 敘事的藝術／釋經之旅五步過河）、
聖經神學 2（Vos 奠基／漸進聖約論）、舊約 1（Brueggemann 見證與反見證）、新約 1（Hays 迴聲）。
收工稽核全零：未判層 20→0、真欠債 7→0。

- 驗收：41 項具名事實／術語／經文例回源章節 grep 全數命中。**本輪抓到一筆「結構數字錯」——
  在我開單的規格裡**：我把 Grasping God's Word 的釋經之旅寫成「四步走」，代理讀原文發現是五步、
  如實照書寫並在回報標出，標題已全面改為「五步過河」。這正是 §1.2 預言的病，只是這次錯在指揮層。
- 112 組 book/anchor 零死鏈；順手用腳本清掉既有頁 21 條 related 單向邊（本站存量最多的一站）。
- **BST 38 卷系列債本輪未動**（比照批次 1 卷冊框架逐批寫，獨立工項，仍掛在「批次 3+ 剩餘」）。

## wujun-note 批次 2（2026-08-25 完成，Fable session 第七站）

10→17 頁。判層 7 本**全 spine**——與 kiyosaki 相反的形狀：吳軍的待判書全是重量級獨立正典
（既有 10 頁引的反而是得到隨筆集），豁免率僅 6%。開新分類「科技與文明」（對應 bibliography
既有分群），7 頁新開：浪潮之巔／智能時代／全球科技通史／文明之光／信息傳（新分類 5 頁）＋
大學之路（學習與卓越）＋數學通識（科技之美）。收工稽核全零：未判層 7→0、真欠債 7→0。

- 驗收：44 項具名事實／史實／數字回源章節 grep 全數命中（一筆「23:59」初判查無係 grep 半形樣式
  對不上原文全形「23 點 59 分」，逐格核對後頁面數字與原書表格完全吻合——零杜撰）；
  39 組 book/anchor 零死鏈、溯源掃描空、entity 零殘留。
- 順手清掉既有頁 9 條 related 單向邊；本站首次蓋 curation 戳記（僅 enrichedAt——本輪沒跑全站體檢，
  不謊報 checkedAt）。

## kiyosaki-note 批次 2（2026-08-25 完成，Fable session 第六站）

11→14 頁。判層 14 本（3 spine／9 support／2 tool）——清崎書系重複度高，嚴判是本輪重點：
豁免率 48%，但每筆都有可對帳的理由（before-you-quit 的 B-I 三角已有頁、who-took-my-money 等
四本與 five-iqs／fake 頁重疊、for-teens／rich-brother／rich-kid 沿用批次 1 決議、兩本合集判 tool）。
3 頁新開：90/10 與內行投資人（投資指南）、不公平的優勢（五重紅利）、三種槓桿（提早享受財富）。
收工稽核全零：未判層 14→0、真欠債 3→0。

- 驗收：18 項具名事實／數字回源章節 grep 全數命中（零杜撰）、35 組 book/anchor 零死鏈、
  溯源掃描空、entity 零殘留、related 全站雙向。

## management-note 批次 3（2026-08-25 完成，Fable session 第五站）

20→26 頁。判層 8 本（6 spine／2 delegated——批次 2 之後新進的 8 本書全數消化，5-min-mba-tools→
liurun、first-break-all-the-rules→career 皆為既有文件化決議）。6 頁新開：動機 3.0（Pink）、
執行力（Bossidy/Charan）、限制理論（The Goal，小說體 40 章實讀 11 章、anchor 落章）、戴明十四要點、
管理者實際在做什麼（明茲伯格）、逆向工作法（亞馬遜）。收工稽核全零：未判層 8→0、真欠債 6→0。

- 驗收：約 40 項具名事實／實驗／數字回源章節 grep 全數命中（零杜撰）、28 組 book/anchor 零死鏈、
  溯源掃描空、entity 零殘留。
- 順手清掉既有頁 16 條 related 單向邊（本站首次跑雙向檢查，managerial-leverage 作為樞紐頁補回 7 條反向）。

## theology-note 批次 3（2026-08-25 完成，Fable session 第四站——本輪最大站）

24→34 頁。判層 19 本（10 spine／5 delegated／4 support）。裁決亮點：奧古斯丁懺悔錄、效法基督、
天路歷程、痛苦的奧秘四本 delegated:spiritual-formation——姊妹站頁正是本 session 剛開的，委託
即時兌現；incomparable-christ→stott（該站有同名專頁在挖）。10 頁新開：doctrine 3（認識神／
道成肉身／巴文克恩典恢復自然）、apologetics 3（巴斯卡思想錄／阿奎那五路／切斯特頓永恆的人）、
historical 2（上帝之城兩座城／奧爾森神學的故事）、牧養 2（巴克斯特改革宗的牧師／畢德生返璞歸真）。
收工稽核全零：未判層 19→0、真欠債 10→0。

- 驗收：約 65 項具名事實／引文回源章節 grep 全數命中（兩筆初判「查無」實為我抽驗樣式比原文措辭嚴，
  對原文後確認頁面皆逐字引用——零杜撰）、60 組 book/anchor 零死鏈、溯源掃描空、entity 零殘留。
- 代理紀律兩例可貴：亞他那修名句「祂成為人使我們成為神」因落在未指定章節而拒用、改以實讀章節
  措辭承載同一邏輯；巴刻 balconeer/traveler 因文本未用該譯名而改用文本實際用語「旁觀者／旅人」。
- 順手清掉既有頁 11 條 related 單向邊（遺留債）＋1 條本批漏鏡射。
- 刻意不寫：christian-theology-introduction（support，survey 教科書）、journey-of-modern-theology
  （support，20 世紀地圖頁已涵蓋軸線）、lectures-to-my-students（support，牧養軸由兩本正典承重）、
  war-of-words（support）。

## spiritual-formation-note 批次 2（2026-08-25 完成，Fable session 第三站）

13→20 頁。判層 10 本（7 spine／1 delegated／1 support／1 tool）。裁決亮點：problem-of-pain 由
**本站 spine 接手深挖、lewis-note 維持 support**——主題站深挖、作者站一句帶到的互補分工；
friendly-snowflake 與 peck-note 同判 support 口徑一致。7 頁新開：prayer-pilgrimage 3（懺悔錄／
勞倫斯與神同在／慕安德烈禱告學校）、discipleship 2（效法基督／消滅匆忙）、suffering-grief 2
（痛苦的奧秘／為兒子哀哭——與既有的卿卿如晤頁組成理性面＋兩座哀歌的完整苦難軸）。
收工稽核全零：未判層 10→0、真欠債 7→0。

- 驗收：47 項具名事實／引文逐一回源章節 grep 全數命中（零杜撰）、40 組 book/anchor 零死鏈、
  溯源掃描空、entity 零殘留、related 全站雙向（含 grief-and-faith 原本空著的 related 一併接上）。
- 刻意不寫：50-spiritual-classics（tool，跨信仰合輯，批次 1 已有決議）、friendly-snowflake（support）、
  desiring-god（delegated:theology，該站已開採）。

## wellness-note 批次 2（2026-08-25 完成，Fable session 第二站，配方同 science-note）

11→19 頁。判層 16 本（8 spine／6 delegated／1 support／1 tool——delegated 全是批次 1 已文件化的
跨站決議，複核後照套），再對 8 本 0 引用 spine 各開一頁：stress-mental-health 3（斑馬壓力生理學／
CBT 認知扭曲／創傷與身體）、nutrition-sleep 2（營養主義批判／每日十二清單）、fitness-body 2
（醫學 3.0／運動改造大腦）、happiness-wellbeing 1（PERMA）。收工稽核全零：未判層 16→0、真欠債 8→0。

- 驗收：約 80 項具名事實逐一回源章節 grep，唯一偏差是譯名（頁面寫「零時體育課」、書用「第零節體育課」，已改從書）；
  41 組 book/anchor 零死鏈、溯源掃描空、entity 零殘留、related 全站雙向。
- 工作流改良：子代理改為**直接寫檔＋回覆驗收摘要**，science 輪 task 通知轉手的 `&gt;` entity 污染這輪零發生。
- 刻意不寫：lets-eat-right-to-keep-fit（support，1954 先驅、科學過時，一句定位即可）、
  living-without-gout（tool，單病查閱型）、fengtang×2→fengtang、happier 等 4 本→life-meaning（delegated）。

> **pastoral-psychology-note 溯源債已清（2026-08-24 晚，帳本 08-25 才補記）**：五本可收的書已到架
> （其餘五本同日判 `unavailable`），兩個 commit（a11e359、254b40e）把 5 頁全數掛上實 anchor，
> 溯源率 0%→100%（本輪 DEEPEN-READY 重算已確認）。**殘債記在各頁 frontmatter 註解**：five-views
> 的中間三觀點、forgiveness 的 REACH 五步、trauma 的哀歌＋Herman 三階段——都得等 unavailable
> 的來源書（Johnson／Worthington／Langberg）才能溯源。站尚未蓋 curation 戳記，留給收尾那輪。

## science-note 批次 2（2026-08-25 完成，首個 Fable session，判層＋enrich 同站串打）

16→27 頁。先判層（21 本裁決：11 spine／6 tool／2 support／2 delegated，套用走 `apply-tiers.py`），
再對 11 本 0 引用 spine 各開一頁：scientific-method 4（可否證性／典範轉移／鬼扯偵測／草包族科學）、
physics-cosmos 3（原子假說／膨脹的宇宙／星塵）、evolution-life 3（天擇原典／基因視角／累積選擇）、
mind-cognition 1（GEB 怪圈）。收工稽核全零：未判層 48→0、真欠債 11→0、空頭支票／漏接／衝突 0。

- 驗收：53 項具名事實逐一回源章節 grep 全數命中（零杜撰）、37 組 book/anchor 零死鏈、溯源掃描空、entity 零殘留。
- 順手清掉既有頁 8 條 related 單向邊（遺留債，非本批製造）；四分類 roadmap＋mastery 已跟上。
- 刻意不寫：brain-rules 與 pleased-to-meet-me（support——thinking-note 同判 support，兩站口徑一致，不互踢）、
  6 冊藥學 handbook（tool，依既定決議不進站）、frames-of-mind→gardner、槍炮病菌→history（delegated）。
- 工作流備忘：子代理交回的稿經 task 通知轉手會帶 `&gt;` entity 污染，主代理寫檔時逐一還原——§共通紀律的 grep 果然每輪都有用。

## 下次開工第一件事

(無——v0.19.3 全站 bump 已於 2026-08-06 當日完成,68 站 0 失敗。)

## note-check 抽查(2026-08-06,大改後驗證輪)

抽 5 站(problem-solving/kiyosaki/behaviour-interview/drucker/system-design)跑全站唯讀體檢:**零紅燈,5 站 PASS with warnings**。黃燈已修:10 站 schools 接線 prettier 格式(kind 指派的 sed 遺留)、6 站翻 owned 後過時的「最大缺口」註記、kiyosaki 2 翻+3 補列、drucker/kiyosaki 7 條 related 單向邊、notes-fmt 執行位(→v0.19.3)。behaviour-interview 與 system-design 的系統性 related/雙集合反向不對稱另發 --fix 清理。遺留人工判斷項:behaviour-interview 的 `::discussion` 變體是否認可、system-design caching-strategies 的 `:::response` 疑似範例殘留、problems 全站未填 difficulty。

## v0.19.0 版面契約債(2026-08-05 登記,2026-08-06 全數結案)

core v0.19.0 把首頁綜覽升格必備、新增 `/check/` 檢核頁。三筆存量債已於 2026-08-06 一次清完(校準批 5 站先驗風格,再 8 批平行 agent 放量,逐站 build 驗證+slug 機械核對):

1. ~~mastery 全站皆缺~~:**66 站全數補齊**(除 leetcode-note),每個分類 `_index.md` 都有 2–4 條書本位 mastery、slug 只連真實存在的頁;分類只有單頁已寫成時 2 條同掛該頁。範本=covey-note。
2. ~~kind 指派~~:9 站完成——methods:agile、design、problem-solving、biblical-studies、learning、tools;themes:history、science、hbr。其餘 schools 站維持預設學派地圖。
3. ~~缺 schools 的主題站~~:behaviour-interview-note 已補 methods 方法地圖(6 張卡,跨站連 newport)。
   > `leetcode-note` 仍除外:唯一沒遷移到 core 版面的站,v0.19.0 的導覽列、卡片、檢核頁一概吃不到。要它跟上得先做 Phase-2 遷移,是另一個獨立工項。

> 順手修掉的雜項(2026-08-06):economics 2 頁、keller 13 頁檔尾殘留的工具呼叫雜訊行(`</content>`/`</invoke>`)已清;agile/investing 3 條「尚未收」過時註記隨 wanted→owned 翻轉一併改寫。

## 新站(2026-08-10):security-note

開站緣由:`ORPHAN-BOOKS.md` 1b 的唯一開新站候選——`leaf-security` 8 本藏書裡 6 本沒有任何站認領(75%),
是全星系唯一同時滿足「藏書 ≥8」與「未覆蓋 ≥60%」的 leaf。這也是**反向盤點腳本化之後抓到的第一個站**。

| 站 | pages/owned | 備註 |
|---|---|---|
| security-note | 4 / 8 | 四個分類各一則種子概念,**全部走路徑 A**(逐章讀 `books-done` 原文後寫,每頁掛章節 anchor,anchor 目錄已逐一驗證存在)——**不欠溯源債**。分類:安全工程/攻擊者視角/應用密碼學/Web 與應用安全 |

> **待深化**:pages/owned = 4/8,每個分類的 roadmap 各留了 2 個 planned 節點(共 8 頁)。
> 8 本 owned 書全部在本機 `books-done/craft/engineering/security/` 且章節完整,下一輪 `note-check --enrich` 直接可用。

> **本站是第一個原生使用 `author` 欄的站**(notes-core v0.27.0);`wanted` 那 6 本已於開站當日實掃 portal 與
> 本機 books-done,確認都不存在,不是假缺口。

## 新站(2026-08-04 開站,同日全部完成 enrich)

開站緣由與缺口分析見 COVERAGE-GAPS.md。五站的內容皆為書本位、每頁掛章節 anchor。

| 站 | pages/owned | 備註 |
|---|---|---|
| templar-note | 7 / 6 | 開站種子概念全數改寫為書本位並掛章節 anchor;順手修正三處事實(Rules of Thinking 是 10 部不是 6 類、Rules of Management 的核心是「管理流程而非管理人」、work 分類頁改名 manage-the-process-not-the-people) |
| navarro-note | 6 / 4 | 同上;補入十大準則、三腦一體、識謊迷思(慣性說謊者反而增加眼神接觸)、討喜 vs 善良對照表 |
| design-note | 8 / 9 | 批次 1 完成;新增 5 頁(SHE 削減、SLIP 組織、三個重疊空間、創造是減法、清晰與神秘) |
| agile-note | 13 / 8 | 批次 1 完成;新增 9 頁(DEEP/相對估算/技術債、視覺化/管理流動、角色建模/故事異味、ADAPT/自組織領導) |
| covey-note | 12 / 8 | 批次 1 完成;新增 6 頁(以終為始、磨鋸、雙贏、統合綜效、信用四核心、4DX) |

> **溯源債已清（2026-08-04）**:上表三站開站當天的種子概念(agile 4 頁、covey 6 頁、design 3 頁)原本沒有 anchor,同日已全部回原文逐段核對後改寫。五站現在跑 `note-check` §0.5 掃描皆為空。

> 三站的來源書都在 `books-done` 下且章節完整,溯源 anchor 已掛。covey 站刻意不另開「影響圈」頁——既有的 `space-between-stimulus-and-response` 已完整涵蓋。

## 高落差(owned 遠大於 pages,優先)

| 站 | pages/owned |
|---|---|
| biblical-studies-note | 44 / 74(批次 1+2 完成 2026-08-06:批次 1 補列 14 本 BST 並寫 14 頁卷冊解經框架;批次 2 再寫 11 頁清高價值缺口——Beale 新創造、賴特卷一史學方法、Bailey 中東之眼、Waltke toledot、Hays 三焦點、Ehrman 文本鑑別、逐卷讀經法/難解經文/孫寶玲講道學、Watkin 對角化、Peterson lectio divina。**批次 3～7 完成 2026-08-26**:三批各補列 6 卷、各寫一頁(批次 3:約書亞/撒母耳/約伯/傳道書/以賽亞/約翰福音;批次 4:以西結/但以理/耶利米/箴言/馬太/馬可;批次 5:利未記/列王紀/何西阿/哥林多前書/哥林多後書/彼得前書;批次 6:路得/約拿/耶利米哀歌/雅歌/歌羅西腓利門/約翰書信;批次 7:創世記/以斯帖/以斯拉哈該/約珥彌迦哈巴谷/俄巴底亞那鴻西番雅/瑪拉基/撒迦利亞/彼得後書猶大書),站況 83 頁 107 本;Stott 那 6 卷確認歸 stott-note 不重寫。**批次 7 完成 2026-08-26:系列債結案**——最後 8 卷(創世記 BST 版[已判與 Walton／Waltke 不重疊,改切十二 1～3 樞紐]、以斯帖、以斯拉與哈該、約珥彌迦哈巴谷、俄巴底亞那鴻西番雅、瑪拉基、撒迦利亞、彼得後書與猶大書)全數補完;全 52 冊每一冊都有頁承載;工具書群(TDNT/IVP 背景註釋等)作 alternative 不立頁) |
| problem-solving-note | 17 / 20(批次 1 完成 2026-08-06;13 頁新增+4 頁種子頁回原文校正(抓到 6 處實質錯誤,見 SOURCING-DEBT.md);16 本已引用,zero-second 系列/mckinsey-work-method 與既有頁重疊刻意不寫——實際落差歸零) |
| kiyosaki-note | 11 / 13(批次 1 完成 2026-08-06;8 頁新增;10 本已引用,for-teens/rich-brother 等 3 本重疊或無容器刻意不寫——實際落差歸零) |
| career-note | 44 / 58(批次 1 完成 2026-08-06;8 頁新增,底子乾淨無未溯源頁;30 本名目落差中 8 本跨站分工、3 本姊妹站認領、3 本本地無書源、其餘書摘太薄或軸不合刻意不寫——實際落差歸零) |
| leadership-note | 54 / 77(批次 1 完成 2026-08-06;10 頁新增(multipliers/radical-candor/great-by-choice 等今日剛翻 owned 的新書為主);28 本刻意不寫:12 本跨站分工、9 本姊妹站認領、7 本重疊或離題——實際落差歸零。遺留小債:6 個既存頁不在 roadmap 內(ceo-excellence/confront-brutal-facts/drucker-five-questions/boundaries-for-leaders/team-of-teams/five-levels-of-leadership),roadmap 視圖不顯示,下輪順手補) |

> biblical-studies-note 這一筆現在額外吃得下 18 本:Wilcock/Motyer/Raymond Brown/Walton 四位釋經作者的書,依 COVERAGE-GAPS.md 的決議不另開人物站,全歸這裡。

## 中落差

| 站 | pages/owned |
|---|---|
| management-note | 20 / 39(批次 2 完成 2026-08-01;39 本中 38 本已消化——concept-of-the-corporation/程天縱三部曲/管理備忘錄/managers-handbook 全開頁,drucker-cafe 補強掛 know-thy-time,5-min-mba-tools 歸 liurun 站——落差歸零) |
| wellness-note | 11 / 24(批次 1 完成 2026-07-31;24 本中 20 本已消化——4 本跨站:harvard-guide/two-awesome-hours→life-meaning、fengtang×2→fengtang 作者站——實際落差歸零) |
| hbr-note | 32 / 42(批次 2 完成 2026-07-31;42 本中 41 本已消化,managing-stress 以補強掛進 manage-your-energy;僅 hbr-guide-collection 合輯不消化——落差歸零) |
| tools-note | 20 / 42(批次 1 完成 2026-07-31;34 本已消化——8 本跨站重疊刻意不寫:atomic/tiny-habits、indistractable、4000-weeks、first-things-first、eat-that-frog 歸 habits-note,7-habits 歸 career/leadership,zstp 與既有頁重疊;實際剩餘落差已小) |
| science-note | 16 / 37(批次 1 完成 2026-07-31,含撿回上次中斷的 6 頁遺留稿;剩 4 本 niche 認知書:affective-neuroscience/through-the-language-glass/pleased-to-meet-me/frames-of-mind,7 冊臨床藥學 handbook 依 BOOKS.md 不進站——實際剩餘落差已小) |
| communication-note | 37 / 44(批次 1 完成 2026-07-31;44 本中 34 本已消化——10 本跨站刻意不寫:48-laws/human-nature→greene、start-with-why→leadership、everyone-communicates→maxwell、story-mckee/smart-brevity→writing、2 本→relationships、speak-to-win→tracy、body-language→thinking——實際落差歸零) |
| spiritual-formation-note | 13 / 28(批次 1 完成 2026-07-31;28 本中 12 本跨站已覆蓋(willard×3/lewis×4/nouwen/keller/theology×2/habits)、50-spiritual-classics 跨信仰選集不合站主軸刻意不寫——實際落差歸零) |
| theology-note | 24 / 49(批次 2 完成 2026-07-31;49 本中 43 本已消化——4 本跨站刻意不寫:prodigal-son→nouwen、incomparable-christ→stott、pilgrims-progress→spiritual-formation、wrestle-with-god→peterson;systematic-theology/new-dictionary 以補強掛進 what-is-systematic-theology——實際落差歸零) |
| investing-note | 43 / 53(批次完成 2026-08-06;9 頁新增+利弗摩三頁溯源修復;引用書 17→27 本,其餘跨站分工/重疊/密度不足刻意不寫——實際落差歸零) |
| business-strategy-note | 31 / 39(批次 1 完成 2026-07-31;39 本中 29 本已消化——9 本跨站分工(management/startup/leadership/habits/marketing/hbr/communication/tracy)、concept-of-the-corporation 依決議歸 management-note 佇列——實際落差歸零;附註:art-of-strategy 書 repo 有「乃許」類 CJK 損壞譯名待修) |
| habits-note | 28 / 34(批次 1 完成 2026-08-01;34 本中 25 本已消化——8 本 tools/wellness 站領土、workbook 練習冊不消化——實際落差歸零) |
| economics/history/relationships/thinking/tracy/startup | **六站批次全數完成 2026-08-06**:economics 37→45(另抓 12 頁系統性錯掛 anchor+推力器捐主張反向,見 SOURCING-DEBT)、history 23→30、relationships 29→34、thinking 36→46(新開 mental-models 分類)、tracy 18→25、startup 37→44(藍海/獲利世代由本站認領)——各站實際落差歸零,刻意不寫清單見各站 commit 當輪回報 |
| peterson-note | 12→24 / 4(批次 1 完成 2026-08-09;12 頁新增——與神摔跤 5 章(亞當夏娃/挪亞/亞伯拉罕/摩西 I+II 合一頁/約拿,theology-note 的 wrestle-with-god 分工至此兌現)、十二法則 3 條(法則四/六/八)、秩序之上 2 條(VI 意識型態/XI 怨恨)、意義的地圖 2 章(異常的出現/學徒期);WWWG 結論章歸概覽頁、兩本法則書其餘條目刻意不寫防逐章書摘化、MM 序言歸概覽——實際落差歸零。溯源 100%(29 anchors 全驗)、抽驗零杜撰、seeAlso 首開 3 條跨站連結(biblical-studies×2/keller×1)) |
| 作者站小落差 8 站 | **批次 1 全數完成 2026-08-06**:nouwen(3→8)、gardner(3→8)、fengtang(3→8)、willard(3→7)、newport(4→10)、liurun(4→11)、taleb(3→8)、schwager(7→10)。全書本位+anchor 逐一驗證;newport 這輪順帶揪出書 repo 身分錯配首例(見 SOURCING-DEBT.md);各站刻意不寫的重疊/跨站分工清單在各自 commit 訊息對應的回報——實際落差歸零 |

## 低落差 / 已充實(暫不動)

behaviour-interview、clean-code、cloud-infra、data-systems、design-patterns、system-design、learning、writing、marketing、greene、uncle-bob、wan-weigang、image-style、peck、bogle、damodaran、de-botton、cloud、fromm、lewis、nt-wright、maxwell、stott、keller、drucker、wujun、personal-finance、philosophy、life-meaning、growth、economics…(pages≥owned 或差距小)

## 用法

1. 挑一站 → `cd notes/<站>` → 跑 note-check skill(或照 hbr-note 這輪的配方)。
2. 開工時在該站建 `TODO-enrich.md`,並把本檔該站移到「進行中」。
3. 完工(commit+push、刪站內 TODO)後,回本檔更新 pages 數、移回對應區塊。
