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

### 2026-11-06 體檢輪（Fable）：契約層全綠之後，缺口在工具不量的地方 — **A 組已執行、C 組 0.44.0 已 tag 正在 bump、B 組 14 頁 Opus 已交付**

**先拉再盤**：開工時 80 個 repo 全部落後 origin 1–5 個 commit（都乾淨、都沒 ahead）。沒拉之前算出的四筆 GUIDE-DRIFT「要改」其實上游 10-27 已修；本機 notes-core 也沒有 `prose-metrics.py`／`prose-finalize.sh`。**任何全星系盤點前先 `git pull --ff-only` 全部 repo**（memory 已記）。

**現況（拉完重算）**：79 站＋core 全在 v0.43.4；galaxy-checkup 78 站 blocker 0／warn 0／nit 68；tier-audit 六類違規 0（writing 2 筆空頭支票本輪清掉）；溯源 100%；導覽 78/79（data-science 無）、overview 79/79、roadmap／mastery 100%；2233 概念頁＋474 題型頁；owned 2369、wanted 39（全在 data-science）。**工具量得到的都綻了**，剩下的在三個工具不量的維度：

| 維度 | 數字 | 判讀 |
| --- | ---: | --- |
| 頁級跨站連結（`seeAlso`） | 225/2233 頁（10%），41 站零跨站連結 | 79 站各自封閉，首頁 schools 卡是唯一通道；同一章同時撐著主題站與人物站各一頁的有 473 筆 |
| 對照型頁 `kind: debate` | 2/2233 | v0.38.0 的頁型幾乎沒用；導覽第四章卻已寫了 63 節具名爭點（兩造頁都在站上） |
| 大部頭第二鏟 | 143 本 spine 章節 ≥30 卻只被 1 頁引用（DEEPEN-TARGETS） | 47 站「可深化」；選題是 Fable 的活，起草交 Opus |
| `:::response` 使用者層 | 36/2233 頁有內容（31 在 data-systems） | 設計上只收真實 Q&A，不能批次填；但空佔位渲染在 2197 頁上（C2） |
| `status` | draft 2134／studied 48／reviewed 51 | 95% 一個值，徽章變噪音（C4） |
| `importance` | 4＝1249、5＝683、3＝300、2＝1 | 星等灌水，先記著不動 |

**A 組（已執行，63 站各一 commit、notes-core 一 commit；全部未 push）**
- [x] **跨站連結工具化＋補鏈**：新工具 `tools/export-seealso-gaps.py`（第九份生成文件 `docs/SEEALSO-GAPS.md`，已進 `refresh-galaxy-docs.sh`）＋ `tools/apply-seealso.py`。判準只收 **strong＝同書同章**（weak 同書不同章 421 筆只列數字）；目標頁同分類 ≥3 頁就連分類頁，否則依共用章節數最多連 2 頁，label 一律用目標頁 title。寫入 **529 筆、454 個檔、62 站**；有 seeAlso 的頁 **225 → 595（27%）**。驗證：md 全數 prettier 過（5 站全 config `format:check` 過）、leadership／image-style／writing `astro build` 綠、galaxy-checkup dead-seealso 0。
  **踩到**：strict 站（7 個技術站）的 `seeAlso.site` enum **只含那 7 個 key**，clean-code → uncle-bob 寫進去 build 直接紅（InvalidContentEntryDataError）。已回退 27 筆（19 檔），工具改成把這類列成「被 schema 擋住」（19 筆：clean-code→uncle-bob 14、→kent-beck 1、design-patterns→uncle-bob 1、behaviour-interview→management／communication／career 各 1）。放行要改 core 的 enum（C3）。
- [x] writing-note 2 筆空頭支票（Vogler《作家之路》、Egri《The Art of Creative Writing》，9977575 判 support 卻沒進導覽）：導覽第三章各織一句定位（Vogler＝坎伯的片廠譯本、八種原型是面具；Egri＝McKee 與 Truby 的上游、只借「角色的矛盾」一章），順帶把 McKee《人物的解剖》的查閱層位置寫進去；三個 anchor 進章 frontmatter、`writtenAt` 蓋 2026-11-06。tier-audit writing 0／0／0。
- [x] 單向 related 10 筆補雙向：marketing 3（brand-archetypes 的三個目標頁沒指回）、writing 7（character-archetypes／character-dimensions 的目標頁沒指回）。checkup oneway-related 歸零。
- [x] image-style-note 13 頁最後的舊骨架（`## 🧠 核心概念`／`## 🔑 總整理`）→ `::core`／`::takeaways`；build 綠、dist 渲染 Core Ideas／Takeaways。全星系舊骨架歸零。
- [x] notes-core 文件過期：DESIGN.md §5.2 從 v0.5.0 前的 h2 骨架改成 directive 骨架＋分站族詞彙表＋`kind` 頁型；README 開頭與「內容（v0.1.0）」節改成 v0.43 現況（exports 表）、tools／docs 表補第九份。
- [x] `refresh-galaxy-docs.sh` 重算：ORPHAN-BOOKS 冒出 **2 本孤兒書**（`tao-of-travel` Theroux、`cooks-tour` Bourdain，10-27 之後建的書站沒人認領）→ **已認領進 travel-note**：Theroux 判 `tool`（引文選集，查閱）、Bourdain 判 `support` 並在導覽第三章跨區段補一句；tier-audit travel 0／0／0，孤兒歸零。owned 去重 1827→1832。
- [x] theology bibliography 的 `systematic-theology` 書目歸屬錯：書 repo 是林鴻信 2017（圖賓根、莫特曼門下），盤點表寫「章力生等華人卷 1990」。title／year／note 已改，導覽第三章那句同步；B 組第 2 張單據此起草。
- [x] `export-deepen-targets.py` 體裁排除加書信體（`screwtape-letters`，31 封短信章節數高但全書薄）：候選 143→141。

**Opus 開工指令（Andrew 切模型後，照這段做；Fable 2026-11-06 交接）**
0. 前置：`for d in ~/workspace/andrew/notes/*/; do git -C $d pull -q --ff-only; done`；讀 `docs/MODEL-ROUTING.md` §四（驗證網）、`/note-check` §6（書本位紀律、`:::response` 留空、內文不夾行內引用、不自撰）、本節下面兩張單。
1. **investing-note 六頁 `kind: debate`**：每頁一個子代理、路徑 A，prompt 含 note-check §6.3 的六項；骨架照 `clean-code-note/src/content/concepts/comments-formatting/to-comment-or-not.md`；anchor 只從兩造既有頁的 `furtherReading` 取並逐一 `[ -d books-done/**/<book>/site/content/<anchor> ]`；不下裁決（裁決在導覽第四章）。每頁交回：grep `&gt;|&lt;|&amp;`、anchor 實存、`related` 雙向、**具名事實回源 grep ≥3 筆**；補進分類 `_index.md` roadmap；導覽第四章對應那節末尾加一行連到新頁（保語氣）。全部完成後 `npm run build`、`npm run format`、`format:check`，蓋 `curation.enrichedAt`，`tier-audit.py investing-note` 與 `galaxy-checkup.py --station investing-note` 必 0 warn。
2. **theology-note 八頁 claim**：起草順序 2、7、1 → 3、4 → 5、6 → 8（第 2 張先核對書目已改成林鴻信）。流程同上；每頁補 roadmap，該分類 mastery 若句子能從新頁收斂就補一條（可溯源才補）；導覽第三章講那本書的段落補一句連到新頁；蓋 `enrichedAt`；`tier-audit.py theology-note` 必 0。
3. **C3 收尾（只在全星系已 bump 到 ≥ v0.44.0 時做）**：`notes-core/tools/export-seealso-gaps.py --json --allow-strict > /tmp/sa.json && tools/apply-seealso.py /tmp/sa.json --apply`，三站 format、clean-code `npm run build` 綠，commit。
4. 收尾：`notes-core/tools/refresh-galaxy-docs.sh`，在本節補一段「Opus 執行」戰報（頁數、抽驗筆數、哪幾張單照書改了標題）。單行英文 commit，逐檔 add；**不 push**，Andrew 自己推。

**Opus 執行（2026-11-06 上午，Andrew「with Opus, go」）— B 組 14 頁全數交付＋C3 收尾，本機 commit**
- **investing-note 6 頁 `kind: debate`**：can-the-market-be-beaten、cut-losses-or-average-down、concentrate-or-diversify、does-market-timing-work、does-price-rewrite-fundamentals、rules-or-beliefs。標題四張照單改成中立問句（單上「由可驗證的優勢決定」「各自成立於自己的紀律框架」本身就是裁決）；骨架標題「共識區與真正的爭點」改「共識區與爭點」（AI 腔禁詞）。導覽第四章六節各補一行連到對照頁。全站 47→53 頁。
- **theology-note 8 頁 claim**：atonement-theories-map、person-and-relation、after-the-reformation、persecution-and-the-early-church、visible-yet-hidden、beyond-personality、order-of-salvation、historical-point-of-view。導覽第三章各書段落補連結；全站 41→49 頁。
- **抽驗**：每頁代理交 5 筆具名事實（含逐字原文），主會話回源 grep 抽 **40 筆，全中**。機檢 14 頁 entity／「——」／anchor 實存／related 雙向／`:::response` 空塊全過。
- **起草代理抓到的既有頁錯誤（校正表）**：
  - `mr-market-and-margin-of-safety` 掛的是《智慧型股票投資人》第 2 章（通膨），市場先生在第 8 章、安全邊際在第 20 章：換掛 08＋20。
  - `position-sizing-and-ruin` 寫海龜單位制，掛的 03／04 章都沒有「單位」：補掛第 10 章〈風險與資金管理〉。
  - `overconfidence-and-hindsight` 引「74% 經理人自認高於平均」，出處第 3 章沒掛：補上。
  - `efficient-market-and-random-walk` 的 CAUTION 框「巴菲特與林區像連丟十次正面、事前無法分辨技巧與運氣」**在《漫步華爾街》書 repo 全書找不到**（B 型債：憑印象寫的），導覽爭點一同句：兩處都刪。
  - 林鴻信原書 18 章把拉乖娜誤植為「拉納」一處、奧爾森原書三處可疑（柯恩赫特「年輕神學家」、查爾斯·衛斯理作〈萬古磐石〉、愛德華茲任「普林斯頓神學院」院長）：頁上照上下文歸屬或不寫，書 repo 未動。
- **判層**：新對照頁讓 Dhandho、Education of a Value Investor（各 3 頁）、Laws of Wealth（4 頁）成為既成事實衝突 → 升 spine，導覽第三章「支架」說法同步；tier-audit 兩站六類 0。overview 兩站重數（investing 脊梁 29→32、theology 41→49 頁）、`writtenAt`／`enrichedAt` 蓋 2026-11-06；GUIDE-DRIFT 要改 0。
- **踩到**：補反向 related 時，多行陣列帶尾逗號的格式被插成 `,,`，investing build 紅（concentrate-dont-diversify）。已修，全星系掃過 0 筆。日後插入 related 要先把陣列正規化成單行再插。
- **C3 收尾**：bump 跑過的三個技術站（clean-code 23、design-patterns 1、behaviour-interview 3）用 `--allow-strict` 補 27 筆 seeAlso，三站 build 綠。**還欠**：investing 新頁帶出的 5 筆 strong 缺口，等 bump 跑過 investing 再 apply（避免和 bump 的 commit 搶工作樹）。
- **build／format／lint**：兩站全綠（66／60 頁）；checkup 只剩 core-version warn，bump 完自然消失。

**B 組（已開單，等 Andrew 過目再動筆；起草交 Opus）**

### investing-note：六場爭點 → 六頁 `kind: debate`（Fable 2026-11-06 開單；起草交 Opus，每頁一個子代理、路徑 A）

判準（note-check §1.4 形狀測試）：一個問題、多本書吵、各方都已有溯源頁 → 對照型 concept。導覽第四章已把六場爭點各寫成一節並下了裁決；debate 頁是它的**查閱單位版本**：各造主張並排、各自掛 anchor、不下裁決（裁決留在導覽 Verdict），只寫得出處的「判別變數」（例如索羅斯自己畫的界線、Loeb 自己說的前提）。
每頁的 anchor **一律從兩造既有概念頁的 `furtherReading` 取**（都驗過），不另找章；起草前先讀兩造的頁與導覽第四章該節，避免重講。寫完補進該分類 `_index.md` 的 roadmap，`related` 雙向連到兩造的頁；`seeAlso` 依 SEEALSO-GAPS 重跑結果補。骨架照 clean-code `comments-formatting/to-comment-or-not.md`（`> 點題` → `::core` 列各造一句 → `## 各造立場` → `## ⚖️ 共識區與真正的爭點` → `::takeaways` → `:::response`）。

1. index-passive `can-the-market-be-beaten`「市場打不打得敗：證據線、實踐線與量化例外」— 證據線：a-random-walk-down-wall-street、winning-the-losers-game-ellis（取 efficient-market-and-random-walk、the-losers-game 的 anchor）；實踐線：most-important-thing 第 2 章（second-level-thinking）、investment-valuation（valuation-approaches-and-bias）、dhandho-investor／education-of-a-value-investor（low-risk-high-uncertainty）；量化例外：man-who-solved-the-market（efficient-market 頁已掛）。避開各頁對自己主張的完整論證，只並排「效率＝快不是對」「優勢昂貵稀有事前難辨」「大獎章紀錄」三件事；指數派的實務理由不依賴 EMH 這一點照書寫（柏格、艾利斯都說的是成本與分散）。
2. trading-speculation `cut-losses-or-average-down`「跌了該停損還是加碼：兩套規則來自兩個遊戲」— 停損派：market-wizards（risk-first-cut-your-losses）、reminiscences-of-a-stock-operator 第 8 章時機（timing-and-the-big-picture）；加碼派：intelligent-investor 市場先生章（mr-market-and-margin-of-safety）、dhandho-investor Stewart Enterprises 案例（low-risk-high-uncertainty）。判別變數只寫書裡有的：估值錨、保證金與每日結算（利弗摩 1906）、Guerin 案例（psychology-of-money，luck-risk-and-survival 頁已掛）。
3. value-investing `concentrate-or-diversify`「集中還是分散：由可驗證的優勢決定」— 集中：common-stocks-and-uncommon-profits（scuttlebutt-and-quality-growth）、essays-of-warren-buffett 凱因斯 1934 信（circle-of-competence）、battle-for-investment-survival（concentrate-dont-diversify）；分散：bogleheads-guide-to-investing Bernstein 15-stock myth（three-fund-portfolio）；裁決性證據：little-book-of-behavioral-investing 74% 自評高於平均（overconfidence-and-hindsight）、laws-of-wealth 25–30 檔「集中分散」（rules-over-discretion 頁已掛）。
4. index-passive `does-market-timing-work`「擇時與動能有沒有用：各自成立於自己的紀律框架」— 有用：how-to-make-money-in-stocks M 字訣與 95% 飆股（canslim-and-momentum）、reminiscences 時機課（timing-and-the-big-picture）；沒用：little-book-of-common-sense-investing（stay-the-course）、a-random-walk-down-wall-street 圖形分析章（efficient-market-and-random-walk）、laws-of-wealth 200 份電子報與 90 天統計（rules-over-discretion）。避開 behavior-gap 頁的 Dalbar 數字（那是共識二，不是這場爭點）。
5. market-history `does-price-rewrite-fundamentals`「價格是反映還是改寫基本面：反身性對上市場先生」— 單向論：intelligent-investor（mr-market-and-margin-of-safety）、a-random-walk-down-wall-street（efficient-market-and-random-walk）；反身性：alchemy-of-finance 第一部反身性章（narrative-and-feedback-loops）、irrational-exuberance 結構因素（anatomy-of-a-bubble）。索羅斯自己畫的界線（反身性補基本面不取代、日常事件只有參與函數）照書寫；馬克斯雅虎兩個價格的例子從 second-level-thinking 頁取 anchor。
6. trading-speculation `rules-or-beliefs`「寫下規則就夠了嗎：結構派對上信念派」— 結構派：laws-of-wealth RBI 四 C 與 84.1%／59.4% 實驗（rules-over-discretion）、way-of-the-turtle 單位制（position-sizing-and-ruin、edge-and-consistency）、little-book-of-common-sense-investing 待著別動（stay-the-course）；信念派：trading-in-the-zone 第 4、7 章（thinking-in-probabilities、mental-analysis）。避開 process-over-outcome 頁的決策矩陣（那是共識四前半）。

不開：共識一到五不開 debate 頁（沒有對造；它們已是各 claim 頁與導覽第四章的材料）。

### theology-note：九本大部頭的第二鏟（Fable 2026-11-06 開單，fork 讀目錄＋既有頁；起草交 Opus，每頁一個子代理、路徑 A；34 個章節目錄全部 `[ -d ]` 驗過）

判準：只為脊梁書開頁、主張標得到章節 anchor、與既有 41 頁重疊低於一半；體裁查閱型或第一鏟已涵蓋全書就不開。

#### 開單（8 張）

1. doctrine `atonement-theories-map`「贖罪的五種理論與一個核心：艾利克森的救贖論地圖」— erickson-christian-theology（08-work-of-christ/02-theories-of-the-atonement、08-work-of-christ/03-central-theme-of-the-atonement、08-work-of-christ/04-extent-of-the-atonement）。
   第一鏟（what-is-systematic-theology）只拿他當方法論對照，沒掛 anchor，這頁是本書第一個真正的章節頁。
   只寫五種救贖理論（蘇西努斯榜樣說、道德影響說、治理說、贖價說、滿足說）的主張與問題、五個前置教義因素、刑罰替代論的五項異議與回應、救贖範圍的兩個問題（為誰而死、為何而死）。
   避開 cross-of-christ 的斯托得四步代贖論證（赦免成難題、必須有滿足、被滿足的是神的本性、神的自我替代），這頁是理論地圖，不重講「神為何非死不可」；避開 incarnation 的亞他那修兩難。
   claim 頁；related 連 cross-of-christ、incarnation、costly-grace、resurrection-and-new-creation。

2. doctrine `person-and-relation`「點與線：三一神學的關係思維」— systematic-theology（03-knowing-god/16-trinity、03-knowing-god/17-modern-trinitarian-theology、03-knowing-god/18-relational-thinking、02-knowing-humanity/09-lines-and-dots）。
   第一鏟只掛 01-introduction 當入門定位；導覽第三章明說「華人視角還要再挖」。站上 41 頁沒有一頁講三一論，這是教義區最大的空洞。
   只寫位格概念史（波伊丟斯「位格是什麼」對聖威克多的理查德「位格是誰」，西方重獨特性、東方重關係性）、點與線的比喻、笛卡兒式神學對非笛卡兒式神學（邱立基）、赫舍爾「人是誰」、麥慕列與列維納斯的相互主體性、現代三一神學為何重拾關係思維。
   避開 incarnation（亞他那修）、calvin-double-knowledge（加爾文雙重知識）；與第 7 張分工：這頭講位格概念與關係存有論，路易斯的三一類比歸第 7 張。
   claim 頁；related 連 incarnation、calvin-double-knowledge、knowing-god。
   順帶一筆：這本書的章節內容（齊克果、赫舍爾、邱立基、田立克講章）讀起來是林鴻信《系統神學》，bibliography 的 title 卻寫「章力生等華人卷」，起草前請 Andrew 核對書目歸屬。

3. historical `after-the-reformation`「改革之後：亞米念、敬虔派、清教徒與循道派、自然神論怎麼分出今天的新教」— story-of-christian-theology（08-post-reformation/01-arminius、08-post-reformation/02-pietism、08-post-reformation/03-puritans-methodism、08-post-reformation/04-deism-enlightenment）。
   第一鏟（story-of-theology）掛的是序幕、君士坦丁、基督論之爭、宗教改革四段，停在十六世紀；twentieth-century-theology-map 從巴特起跳。中間兩百年沒有頁。
   只寫亞米念為何自認是改革宗內部的改革者而非敵人、敬虔主義「不是新神學而是新方向」、清教徒與循道派一改革宗一亞米念卻共同塑造福音派、自然神論與啟蒙運動對三十年戰爭宗派廝殺的反向回應（培根、笛卡兒、牛頓三位奠基者）。
   避開 story-of-theology 已寫的尼西亞到改革四段、避開 owen-on-mortification 的治死罪實踐、避開 three-faces-of-secular 的泰勒世俗化論（這頭只寫奧爾森的敘事，不做社會理論）。
   claim 頁；related 連 story-of-theology、twentieth-century-theology-map、owen-on-mortification、why-read-church-history。

4. historical `persecution-and-the-early-church`「從尼祿到戴克里先：迫害怎麼塑造初代教會」— story-of-christianity-vol-1（01-early-church/04-first-conflicts-with-state、01-early-church/05-persecution-second-century、01-early-church/09-persecution-third-century、01-early-church/11-great-persecution-and-final-victory、01-early-church/10-christian-life）。
   第一鏟（why-read-church-history）是方法論頁，anchor 掛了 01 與 02 兩卷卻幾乎沒用到書的內容；這頁是岡薩雷斯第一個真正的敘事頁。
   只寫迫害政策的四個轉折（尼祿嫁禍、圖拉真「不搜捕但被告發須表態」、塞維魯斯禁改宗與德修的祭祀證書「製造背教者而非殉道者」、戴克里先 303 年敕令與四帝共治）、殉道行傳（伊格那丟、珀佩圖亞與菲利西塔絲）、草根信徒的敬拜與社會出身（塞爾蘇斯的「廚房、店鋪、製革坊」）。
   避開 story-of-theology 的異端與信經（教義軸）、避開 two-cities（奧古斯丁）、避開 why-read-church-history 的方法論；多納徒派與背教者爭議在 02-imperial-church/04，留給第三鏟，這頁只點到「背教者問題由此埋下」一句。
   claim 頁；related 連 why-read-church-history、story-of-theology、two-cities、victory-of-reason。

5. doctrine `visible-yet-hidden`「超凡與隱藏：潘霍華讀登山寶訓的可見與不可見」— cost-of-discipleship（02-the-sermon-on-the-mount/02-the-visible-community、02-the-sermon-on-the-mount/07-revenge、02-the-sermon-on-the-mount/08-the-enemy-the-extraordinary、02-the-sermon-on-the-mount/09-the-hidden-righteousness、02-the-sermon-on-the-mount/10-the-hiddenness-of-prayer）。
   第一鏟（costly-grace）掛了第一部五章與登山寶訓結語，登山寶訓本體十四章只用了結語一章。
   只寫鹽與光是「你們是」不是「你們要成為」、不抵抗根植於十字架而非政治理想（舊以色列以力對力、教會放棄政治身分）、愛仇敵是「超凡」的最具體形式、第五章可見性與第六章隱藏性的悖論（狂熱式誤讀與批評者反應）、禱告透過中保而非直通父。
   避開 costly-grace 的廉價恩典對重價恩典、單純順服、捨己與個體、「聽道唯一的方式是去行」；避開 kingdom-of-god-here-and-now（魏樂德「神的國已經來到」）；willard-note 的登山寶訓頁是「天國課程表」角度，這頭只取潘霍華的可見與隱藏張力，seeAlso 連過去即可。
   claim 頁；related 連 costly-grace、kingdom-of-god-here-and-now、will-to-embrace、narrative-ethics。

6. doctrine `beyond-personality`「超越位格：路易斯的三一類比與新造的人」— mere-christianity（04-beyond-personality/01-making-and-begetting、04-beyond-personality/02-the-three-personal-god、04-beyond-personality/04-good-infection、04-beyond-personality/05-the-obstinate-toy-soldiers、04-beyond-personality/11-the-new-men）。
   第一鏟（argument-from-desire）掛第一卷道德律與第二卷基督信念；第三卷倫理、第四卷三一都沒頁。第四卷是路易斯自己標的「走向三位一體教義的第一步」，與站的教義區對口。
   只寫生與造的分別（Bios 與 Zoe）、「超位格」為何只有基督教給了實際內容（維度類比，「被吸收進神」其實是比位格更少）、兩本書疊放的「結果不必在原因之後」、良性感染、頑固的錫兵（兩種生命如今對立）、新人是轉化而非改善。
   避開 argument-from-desire 的道德律與渴望論證、避開 incarnation 的亞他那修兩難（錫兵章那句「神的兒子成為人，是要使人能成為神的兒子」只引一次、標明路易斯轉述）；第三卷倫理（驕傲、寬恕、性道德）屬 spiritual-formation 題域，不開。與第 2 張分工見上。
   claim 頁；related 連 argument-from-desire、incarnation、person-and-relation（第 2 張）；seeAlso 連 lewis 站的返璞歸真頁。

7. doctrine `order-of-salvation`「救恩的次序：巴文克論稱義、成聖與堅忍」— reformed-dogmatics（05-the-holy-spirit-and-salvation/01-the-order-of-salvation、05-the-holy-spirit-and-salvation/02-calling-and-regeneration、05-the-holy-spirit-and-salvation/03-faith-and-conversion、05-the-holy-spirit-and-salvation/04-justification-sanctification-and-perseverance）。
   第一鏟（grace-restores-nature）掛緒論、三一與創造、聖靈更新萬有，取的是全書主軸；救恩論整卷未挖，而站上沒有一頁講稱義與成聖的關係。
   只寫「所有宗教都在找得救之路，只有一條是被賜下的」（佛陀、伊斯蘭、繆勒四十年梵文研究的對照）、救恩次序是聖靈施行基督工作的有機次序而非時間表、赦罪為何不容易（公義與愛在十架綑在一起；因果報應不懂赦免）、稱義與成聖的分際、堅忍。
   避開 grace-restores-nature 的恩典對自然、兩條戰線、新天新地；避開 owen-on-mortification 的治死罪操練（成聖的實踐面歸那頁，這頭只寫教義結構）；避開 costly-grace。
   claim 頁；related 連 grace-restores-nature、owen-on-mortification、costly-grace、christian-hedonism。第三鏟候選：03-humanity-and-sin/01-the-image-of-god（站上也沒有上帝形像頁）。

8. apologetics `historical-point-of-view`「歷史觀點與對老套的恐懼：魔鬼怎麼對付讀書人」— screwtape-letters（23-letter-23、25-letter-25、27-letter-27、30-letter-30）。
   第一鏟（imaginative-apologetics）取了第一、八、十二封信（攪糊、波動律、平緩下坡），都是對平信徒的誘惑；後半部寫給知識人的那幾封沒用到。
   只寫「歷史的耶穌」每二十年換一版且把敬拜對象降格為大師、「相信它不是因為真而是因為有用」、對老套的厭惡被升格為哲學（用「合不合潮流」取代「合不合公義」）、「歷史觀點」讀古書只問誰影響了作者而不問是否為真、「真實」一詞被壟斷給醜陋的物質事實。
   避開 imaginative-apologetics 已寫的三封信與切斯特頓、人之廢；lewis-note 的地獄來鴻頁是全書角度，這頭只取知識人這條線，seeAlso 連過去。
   claim 頁；related 連 imaginative-apologetics、faith-in-a-secular-age、science-and-faith。
   這是九張裡最薄的一張：書 repo 每封信只有一千多字的摘要，四封合計約兩千五百字，寫得出一頁、寫不出第二頁；排最後。

## 不開（1 本）

- living-church《活的教會》（The Living Church）：不開。第一鏟 what-makes-a-living-church 已把八章用了七章（本質四記號、敬拜、佈道四條件、事奉、團契三層、奉獻十原則、鹽與光，外加後現代一章），剩下的講道章（五組對偶）落在 stott-note《當代講道藝術》頁與本站 preaching-to-a-skeptical-age 的題域。tier 維持 spine，承諾已由既有頁兌現，不必改判。

## 小結

- 開 8 張，全部 claim 頁，沒有 debate：九本都是單一作者的體系書，沒有「一個問題多本書吵」的形狀。
- 不開 1 本（living-church），tier 不動。
- 兩個教義區的結構空洞順便補上：三一論（第 2、6 張）與救恩次序（第 7 張）。
- DEEPEN-TARGETS 用章節數排序，把三十一封短信的《地獄來鴻》排進大部頭，是體裁誤判；第 8 張照單寫，但建議把書信體加進該工具的「依體裁排除」判準。
- 起草順序建議：2、7、1（教義空洞）→ 3、4（歷史軸）→ 5、6 → 8。

**C 組（Andrew 2026-11-06「幫我作到」→ 已在 notes-core 0.44.0 落地；本機 commit，待 tag＋push＋bump）**
- [x] **C1 prose-trim 與 body-thin 地板打架**：43 頁被精簡輪縮到 893–998 字、落到 `THIN_BODY=1000` 以下。**改地板不改頁**：`galaxy-checkup.py` 門檻降到 800（docstring 記了理由）。checkup nit 68→18（剩 data-science 17＋hr 1 的 roadmap-planned）。
- [x] **C2 空 `:::response` 不渲染**：`remark-response.mjs` 空塊直接從樹上移除、`two-block.scss` 刪 `.response-empty`；DESIGN §5.3 同步（來源檔仍保留空區塊當標記）。keller 本機 build 驗過：空塊 0 個框、填了內容的照常出「✍️ My Notes」。
- [x] **C3 seeAlso enum 開放**：`sites.ts` 的 `siteKeys` 改成 registry 全部 79 個 key（仍是封閉集合）。clean-code 掛 uncle-bob 的 seeAlso 本機 build 綠。**bump 到 0.44.0 之後**跑 `export-seealso-gaps.py --json --allow-strict` → `apply-seealso.py --apply`，那 19 筆才能真的寫進去（現在寫會讓 CI 紅）。
- [x] **C4 draft 不畫點**：ConceptCard／ProblemCard 只在 `status !== "draft"` 時畫點；DESIGN §6 補一條。keller 本機 build：draft 0 點、studied 1 點。
- **部署（Andrew 自己推）**：① 先推 65 站的本機 commit（`for d in ~/workspace/andrew/notes/*-note; do git -C $d push -q; done`）；② `cd notes-core && git push && git tag v0.44.0 && git push origin v0.44.0`；③ `tools/bump-notes-core.sh v0.43.4 v0.44.0 --push`；④ 再做上面 C3 的 `--allow-strict` 那步（Opus 可做）。
- [ ] **C5 data-science-note**：唯一「先收書」的站（26 本／7 頁／39 本 wanted／無導覽／17 roadmap-planned）。瓶頸在收書，不在寫。
- [ ] 旁註：leetcode-note 自維護前端（39 個本地 .astro／.ts），`galaxy-checkup` 不掃，它自己的 TODO 說 407 題還沒人背書；portal repo（`sites/`）不在本機，portal 層本輪沒體檢；fork 回報 `systematic-theology` 書 repo 內容讀起來是林鴻信而 bibliography title 寫「章力生等華人卷」，起草第 2 張前請核對；DEEPEN-TARGETS 用章節數排序把 31 封短信的《地獄來鴻》當大部頭，建議「依體裁排除」加書信體。


### B 組第二批（Fable 2026-11-06 中午開單；起草交 Opus）— 第二鏟 21 頁 claim ＋ 對照頁 23 頁 debate，共 44 頁

**開單方式**：六個 Fable fork 平行讀原文（書 repo 目錄＋章首、兩造既有頁整頁、導覽第三／四章該段），每張單寫明落點分類、slug、中立標題、骨幹書與章節目錄（全部 `[ -d ]` 驗過）、避開哪些既有頁的什麼、判別變數只寫作者自己說的。主會話逐張審過：形狀不過（導覽自己判互補／接力、只有一造有頁、兩造出自同一本書同一頁）的一律不開，理由留在單上。
**順手修掉的既有頁漏掛 anchor（已 commit）**：management `jelled-teams` 補 Peopleware 三章（西班牙理論、Coding War Games、E-Factor）；philosophy `philosophy-as-consolation` 補《哲學的慰藉》第 6 章（尼采）。`export-deepen-targets.py` 體裁排除再加逐卷導覽與逐條釋疑兩本（候選 132→130）。
**Opus 開工指令**：沿用上面那段（前置拉 repo、§6 紀律、每頁一個子代理、anchor 從單上取並 `[ -d ]`、交回五筆具名事實逐字原文、主會話回源 grep、補 roadmap／related 雙向／導覽連結、蓋 `enrichedAt`、tier-audit 與 checkup 0、單行英文 commit 不 push）。起草順序：先 debate 的 cloud-infra 7、8 與 clean-code 2、1（兩造最乾淨），再 theology 1、2 與 philosophy 2、3，再第二鏟 management 1、3、biblical-studies 2、6、7、wujun 7、2、4，其餘照各單的建議順序。theology debate 第 3 張與 philosophy debate 第 1 張各有附帶條件（重疊過半改補強；先補 anchor 再寫，anchor 已補）。**補 related 用解析後重寫單行，不要 regex 插尾**（上午踩過 `,,`）。

**Opus 執行（2026-11-06 下午）— B 組第二批 44 頁全數交付，本機 commit（未 push）**
- **第二鏟 21 頁**：management 5、wujun 9、biblical-studies 7；導覽第三章在第一鏟那行之後各補一句連到新頁。
- **對照頁 23 頁 `kind: debate`**：clean-code 2、agile 2、data-systems 1、design-patterns 1、cloud-infra 2、theology 3、philosophy 4、tools 2、writing 1、thinking 1、hbr 2、behaviour-interview 1、design 1；導覽第四章對應那節末尾各補一行。theology 第 3 張的退路沒觸發（起草代理判重疊未過半，整頁交付）。
- **驗收**：44 頁機檢全過（entity、「——」、AI 腔、anchor 實存、related 存在、`:::response` 空塊）；每頁至少一筆具名事實回源 grep，**約 60 筆全中**。15 站 format／build 綠，checkup 0 blocker／0 warn／0 nit，tier-audit 六類違規 0；GUIDE-DRIFT 17 筆頁數過期已逐筆改成現況，重算後 0。
- **出處規則的修正（重要）**：單上「anchor 只從既有頁取」在第二批撞牆 12 次：頁上用到的事實其實在某一章，但既有頁從沒掛那章。處理改成「**事實在哪章就掛哪章**」（`[ -d ]` 驗過、label 用書站章題），不再為了守規則而刪內容或留無出處的句子。出處不是書的正文（書站首頁概述）的句子一律刪。
- **起草代理抓到的既有頁錯誤**：
  - 補掛 anchor（內容用了、章沒掛）：philosophy `way-of-water`（老子章）、`no-self-and-emptiness`（無我章），hbr `hiring-for-fit`、`better-decisions`，writing `composting`。
  - 改內容：philosophy `premeditatio-malorum` 刪掉頁面自加的「那不是預想，是焦慮」；design-patterns `oop-vs-functional` 點題句改成書的原話。
  - **兩筆 B 型債記進 SOURCING-DEBT**：hbr `coaching-and-feedback` 整頁的 SBI 書裡沒有；`oop-vs-functional` 其餘「一級函數」幾句也沒有出處。要回原文改寫，留給下一輪。
  - 單上幾句「作者自己說的判別變數」其實是導覽或既有頁的轉述（Bob 的「先分意圖與腳手架」、亞歷山大的「語彙可以永恆」、侯世達的「沒有小人卻有自我」、Stopford 的「坡道」、賴特的「世界被修復」等），起草代理一律改用原文。**教訓：Fable 開單時引的「原話」也要回源，單本身會帶進轉述。**
- **判層**：philosophy 的 Great Thinkers、Daily Stoic 因新頁各散到三頁；兩本都是查閱體裁（資源庫、366 則日課），照規則保留 tool 並在 note 寫明理由。
- **工具教訓**：補反向 related 時遇到三種寫法（單行陣列、prettier 多行陣列、YAML 條列），落盤腳本改成先解析再寫回單行；全星系 `,,` 掃描 0。

#### management-note 第二鏟選題單（DEEPEN-TARGETS 六本大部頭，Fable 開單 2026-11-06）

判準取自 note-check §1.3 與 §1.4：只為脊梁書開頁，主張要標得到章節 anchor，與既有 30 頁重疊低於一半，能被單獨引用。
這站 42 本 spine 有 37 本只一頁、頁/spine 0.75，第二鏟價值高；但 leadership-note 是姊妹站，已在那邊挖過的章不重挖，分工寫明。
每張單寫明第一鏟掛了什麼、第二鏟只寫什麼、避開哪幾頁；章節目錄名全部 `[ -d ]` 驗過。

##### 開單（5 張）

1. principles `drum-buffer-rope`「鼓、緩衝、繩：讓非瓶頸遷就瓶頸的排程」— goal-ongoing-improvement（21-chapter-21、25-chapter-25、26-chapter-26、28-chapter-28、39-chapter-39）。
   第一鏟（theory-of-constraints）掛 05、08、13、19、36 五章，寫的是目標、三指標、相依事件與波動、瓶頸小時成本、五步驟與慣性；鼓與繩只在 core 一條裡帶過一句。
   只寫排程機制：紅綠標籤讓全廠知道什麼重要（21）、啟動資源不等於利用資源與銑床區的「假瓶頸」（25）、健行隊伍第二版與由瓶頸決定投料的鼓與繩（26）、批量減半、非瓶頸省下的一小時是海市蜃樓（28）、畢區放棄成本指標後緩衝與閒置產能的取捨（39）。
   避開 theory-of-constraints 的目標與三指標、五步驟、檢查假設；避開 managerial-leverage 的個人層槓桿。
   claim 頁；related 連 theory-of-constraints、deming-fourteen-points、managerial-leverage、execution。
   第三鏟候選留著：34-chapter-34、35-chapter-35、40-chapter-40 的管理思考法（蒐集事實走不通、門得列夫的內在秩序、改變什麼／改成什麼／如何造成改變），與既有頁「檢查假設」一節有部分重疊，排在這張之後。

2. org-people `hiring-and-turnover`「找對的人與留住人：面試看作品、流動率的帳、人力資本是投資」— peopleware（03-the-right-people/01-the-hornblower-factor、03-the-right-people/03-hiring-a-juggler、03-the-right-people/05-childhoods-end、03-the-right-people/06-happy-to-be-here、03-the-right-people/07-human-capital）。
   第一鏟（jelled-teams）只掛 04-growing-productive-teams，寫的是心流、加班、凝結團隊與 teamicide。
   只寫第三部：管理者改變不了人所以要找對人（Hornblower）、面試要看作品集與試演（雜耍演員）、世代差異是科技對環境（童年末日）、流動率的顯性成本與隱性成本、人力投資在損益表上被記成費用（人力資本）。
   避開 jelled-teams 的心流與 teamicide，避開 first-who-then-what 的柯林斯「先找人再找事」與 staff-on-strengths 的杜拉克用人之長，兩頁只在 related 連過去。
   claim 頁；related 連 jelled-teams、first-who-then-what、staff-on-strengths、performance-review。
   順帶一筆要修既有頁：jelled-teams 正文用了西班牙理論（01-managing-the-human-resource/03-vienna-waits-for-you）、E-Factor 與腦力時間（02-the-office-environment/05-brain-time-vs-body-time）、Coding War Games（02-the-office-environment/02-you-never-get-anything-done），anchor 卻只掛第四部，起草時一併補這三章進 jelled-teams 的 furtherReading。
   第三鏟候選：05-fertile-soil（自癒系統、會議與獨白、浪費人時間是管理終極罪、讓改變成為可能、組織學習）。

3. org-people `competence-and-clarity`「能力與清晰：下放控制的兩根支柱怎麼蓋」— turn-the-ship-around（03-competence/01-mistakes-just-happen、03-competence/02-we-learn、04-clarity/03-leadership-at-every-level、04-clarity/08-a-new-method-of-resupplying、04-clarity/09-ripples）。
   第一鏟（intent-based-leadership）掛 02-control，寫的是「我打算」、改基因碼、拆監控、兩支柱只在一個 details 裡各一句。leadership-note 的 coaching/leader-leader 掛 01、02 兩部，第三、四部兩站都沒挖。
   只寫第三、四部：紅牌事件的八小時檢討怎麼推出慎重行動（03/01）、魚雷室事故與「沒有能力的控制就是混亂」（03/02）、指導原則怎麼真的拿來做決策而不是掛牆上（04/03）、荷莫茲海峽那次「賦權還不夠」（04/08）、交出指揮權十二年後的漣漪（04/09）。
   避開 intent-based-leadership 的「我打算」語言、基因碼、拆監控，避開 shared-consciousness 的 McChrystal；seeAlso 連 leadership 站的 coaching/leader-leader（已存在）。
   claim 頁；related 連 intent-based-leadership、shared-consciousness、drive、one-on-one。

4. principles `strategy-planning-five-steps`「策略規劃：市場區隔、核心競爭力與制訂優勢策略的五大步驟」— terry-cheng-professional-power（03-strategic-planning/19-define-market-segments、03-strategic-planning/22-core-competence-of-startup-teams、03-strategic-planning/23-capability-and-monetization、03-strategic-planning/24-strategy-vs-execution、03-strategic-planning/25-five-steps-of-competitive-strategy、03-strategic-planning/31-nokia-rise-and-fall）。
   第一鏟（terry-cheng-rethinking）只掛 04-corporate-mission/36 德州儀器變革一章；第三部策略規劃十三章一字未用。
   只寫程天縱自己的框架：市場區隔是第一步、核心能力與核心競爭力之辨、能力與變現、策略與執行孰重、五大步驟、Nokia 戰勝對手卻輸給時代。
   避開 terry-cheng-rethinking 的大歷史觀與管理理論更替、terry-cheng-on-culture 的洋蔥圈；business-strategy-note 已有 porter-five-forces 與 value-proposition-fit，波特與價值主張不在這頁重講，seeAlso 連過去（起草前 `ls ../business-strategy-note/src/content/concepts/*/` 確認 path）。
   claim 頁，importance 3；related 連 terry-cheng-rethinking、purpose-of-business、marketing-and-innovation、disruptive-innovation。

5. managers-work `truth-lies-and-right-wrong`「說真話，但要能聽懂三種假話：真假、是非與權力的灰色空間」— terry-cheng-business-management（02-rethinking-leadership/16-changing-hearts-highest-leadership、02-rethinking-leadership/17-telling-truth-hearing-three-lies、02-rethinking-leadership/18-right-wrong-beyond-true-false、02-rethinking-leadership/19-the-gray-space-of-power、02-rethinking-leadership/20-three-small-management-stories）。
   第一鏟（terry-cheng-rethinking）掛 01/01 以人為本，正文用了 13 管理與領導時機、15 改革專業關懷、12 透明溝通、中國惠普六年；第二部 16 到 20 沒用。
   只寫：當上主管後假話變多、三種假話的分級（17）、真假基於事實而是非基於利他（18）、權力空間裡的灰色地帶與判斷力（19）、改變人心是領導的最高境界（16）、三個四兩撥千斤的小故事裡惠利特答離職率那一則（20）。
   避開 terry-cheng-rethinking 的管理對領導、以人為本、成本鴉片、中國惠普改革；避開 idea-meritocracy 的達利歐極度透明制度（那是系統設計，這頁是主管的聽力）。
   claim 頁，importance 3；related 連 terry-cheng-rethinking、idea-meritocracy、one-on-one、performance-review。

##### 不開（1 本）

- five-dysfunctions-of-a-team《團隊領導的五大障礙》：不開。本站 trust-and-team-dysfunctions 已用 06-the-model 寫完模型與逐層工具；leadership-note 另有三頁（team/five-dysfunctions 掛 01-the-fable、02-under-achievement、06-the-model，team/vulnerability-based-trust、team/healthy-conflict 掛 06 與 03/17），寓言章歸那邊。剩下 03-lighting-the-fire、04-heavy-lifting、05-traction 是寓言敘事，再開只會是故事重述。tier 維持 spine，承諾已由既有頁兌現。

##### 小結

- 開 5 張，全部 claim 頁；這站的大部頭都是單一作者體系書，沒有「一個問題多本書吵」的形狀。
- 不開 1 本，tier 不動。
- 兩本程天縱各開一張，分別落 principles 與 managers-work，和既有的 rethinking、on-culture 兩頁合成四頁，實務派在原理層與主管層都有聲音。
- 姊妹站分工：五大障礙的寓言歸 leadership；Turn the Ship Around 的第一、二部歸 leadership 的 leader-leader，第三、四部這站挖；波特與價值主張歸 business-strategy。
- 起草順序建議：1、3（最厚的材料）→ 2（含修既有頁 anchor）→ 5、4。
- 旁註：jelled-teams 既有頁有三章 anchor 缺口（見第 2 張），不必等第二鏟也可以先補。

#### wujun-note 第二鏟選題單（DEEPEN-TARGETS 九本，Fable 開單 2026-11-06）

判準取自 note-check §1.3 與 §1.4：只為脊梁書開頁，頁要能單獨被引用、主張要標得到章節 anchor、與既有 17 頁重疊低於一半。
這站是人物站、一書一頁，第一鏟全是「整本書的導覽頁」，每本書的各章在既有頁上多半只有一句。
所以第二鏟一律選「一章或一組相鄰章撐得起的單一主張」，不再寫整本書；吳軍的成長系列互相重講，選題前逐一比對過別本書撐的頁。
書 repo 是摘要，章節短；材料不到一萬字的章不單獨開頁，合併相鄰章或不開。

##### 開單（9 張）

1. learning `elite-admissions-unfair-by-design`「名校錄取為什麼不透明：一場不公平競爭的解剖」— wujun-road-to-university（06-applying-to-and-being-admitted-by-elite-private-universities/01-anatomy-of-an-unfair-competition、06-.../02-how-the-unfairness-arose、06-.../03-basic-admission-requirements、06-.../05-what-asian-students-and-parents-can-do）。
   第一鏟（wujun-university）掛的是第 1、2、13 章：大學的理念、紐曼對洪堡、文理學院。第 6 章八萬字沒碰。
   只寫錄取競爭為什麼不公平、不透明為何是刻意設計、基本要求是哪幾項、亞裔學生與家長能做什麼。
   避開 wujun-university 的大學理念與通才專才；避開 wujun-math-course 那句哈佛提前申請 13.4% 的機率算術。
   claim 頁；related 連 wujun-university、wujun-excellence、wujun-insight。

2. insight `business-means-spending-more`「商業的本質是讓人多花錢，不是幫人省錢」— wujun-insight（7-essence-of-business/1-business-is-spend-more、7-essence-of-business/2-management-secret-no-choice、7-essence-of-business/3-third-eye-beauty-product-stages）。
   第一鏟（wujun-insight）掛第 1、2 章，商業那章只在收尾段落留了一句蔦屋書店。
   只寫省下來的錢與時間最終去了哪裡、兩個相反的趨勢、蔦屋的生活平台、「不給選擇」的經營祕訣（蘋果三星華為砍產品線、對內管理同理）、第三眼美女與產品階段。
   避開 wujun-insight 的幸福與成功、減法、偽工作者；避開 wujun-tides 的產業興衰定律。
   claim 頁；related 連 wujun-insight、wujun-tides、wujun-pattern。

3. learning `hand-before-mind`「先動手還是先動腦：行動是答案」— wujun-abundance（ch04-methods-of-action/01-hand-before-mind、ch04-methods-of-action/02-mind-before-hand、ch04-methods-of-action/03-action-is-the-answer、ch04-methods-of-action/04-beyond-just-brain、ch04-methods-of-action/05-step-back-to-see-problem）。
   第一鏟（wujun-abundance）掛第 1 章，正文寫到第 1 到 3 章與「從術到道」；第 4 章做事方法在既有頁只是四種能力清單裡的四個字。
   只寫先動手與先動腦各適用什麼情境、為什麼行動本身是答案、不只用腦還用什麼、退一步看問題。
   避開 wujun-abundance 的量級思維、機會成本、經歷與經驗之分；避開 wujun-pattern 的可疊加式進步。
   claim 頁；related 連 wujun-abundance、wujun-pattern、wujun-meta-wisdom。

4. insight `professional-vs-amateur`「專業與業餘的差別：細節、情緒與四大原則」— wujun-attitude（6-conduct-and-work/36-difference-professional-amateur、6-conduct-and-work/37-always-seek-better-way、6-conduct-and-work/38-obedience-is-first-step-to-lead、6-conduct-and-work/39-do-most-important-things-first）。
   第一鏟（wujun-attitude）掛第 1 部，六大主題各一句，第 6 部「做人做事」只在收尾段落列了四個標題。
   只寫一流人的細節、專業的情緒控制、實踐專業精神的四大原則、內田光子的例子、永遠找更好的方法、服從是學會領導的第一步（西點軍校）、先做最重要的事。
   避開 wujun-insight 的偽工作者與職業盲點；避開 wujun-soul-of-computing 的五級工程師標尺。
   claim 頁；related 連 wujun-attitude、wujun-insight、wujun-soul-of-computing。

5. tech-civilization `cybernetics-and-systems-theory`「控制論與系統論：資訊論旁邊的兩把工具」— wujun-information-theory-40（04-extensions/01-cybernetics、04-extensions/02-systems-theory）。
   第一鏟（wujun-information）掛前三個模組，資訊論本體已寫滿；第四模組「延伸」一字未提，站上只有 wujun-tech-history 一句「機械論讓位給系統論、控制論與資訊論」。
   只寫維納控制論的三個要點（突破絕對時間觀、輸出反過來影響系統、用回饋自我調節）、阿波羅登月的兩種方法論對比、「輕預測重反應」；系統論的三個基本觀點與三個體會（整體大於部分之和、關上一扇門打開一扇窗、用系統論改進做事方法）。
   避開 wujun-information 的熵、第二定律、信噪比、交叉驗證與最大熵原理；避開 wujun-intelligence 的機械思維對大數據思維。
   claim 頁；related 連 wujun-information、wujun-tech-history、wujun-intelligence。

6. science `learning-models-from-data`「數據怎麼變成模型：最大熵、貝氏網路與 EM 演算法」— wujun-beauty-of-math（ch20-maximum-entropy-model、ch24-bayesian-network、ch25-conditional-random-field、ch27-expectation-maximization）。
   第一鏟（wujun-beauty-of-math）掛序與第 1 章，正文寫統計語言模型、HMM、搜尋四件套、PageRank、計算邊界；機器學習模型那組章節沒碰。
   只寫最大熵模型的原理與訓練、貝氏網路與心血管疾病例子、詞分類的應用、條件隨機場、EM 演算法的期望與最大化兩步。
   避開 wujun-beauty-of-math 的 HMM 與搜尋；避開 wujun-information 把最大熵當判斷原則的那條（雞蛋與籃子）；避開 wujun-intelligence 的托勒密與開普勒。
   claim 頁；related 連 wujun-beauty-of-math、wujun-soul-of-computing、wujun-information。
   這是九張裡材料最薄的一張：四章各兩千到四千字，合計約一萬二，正文目標 1400 到 1800 字，寫不滿就不要撐。
   不選第 13、19 章（辛格的簡單哲學、數學模型的重要性）：兩章合計不到五千字，而且托勒密到開普勒那段 wujun-intelligence 已經講過。

7. wisdom `civilization-is-thirty-meters`「文明只有三十米：貪婪、虛偽與好心辦壞事」— wujun-context（part-3-society/ch20-human-greed、part-3-society/ch21-is-hypocrisy-from-survival、part-3-society/ch23-civilization-is-only-30-meters、part-3-society/ch24-humans-are-not-gods）。
   第一鏟（wujun-context）掛第一部歷史，社會那部在既有頁只有一條要點，貪婪、虛偽、偽雙贏、好心辦壞事各佔兩個字。
   只寫高爾夫球場的觀察與「文明的範圍只有三十米」、擴大自我邊界為什麼是提升文明的關鍵、開市客塑膠袋與登機口輪椅的貪婪、貪婪的結果是損失、虛偽是不是生存所需、通向天堂的路也可能通向地獄（法國大革命、阿根廷）、好心辦壞事。
   避開 wujun-context 的農業與工業兩次革命、財富三要素定義、漸進改良對推倒重來（阿克頓、托克維爾、柯立芝）；避開 wujun-realm 的尼采。
   claim 頁；related 連 wujun-context、wujun-realm、wujun-attitude。
   第 16 章「思想並不總是進步的」（兩個啟蒙運動、伯克）不選：它與既有頁的漸進改良要點同一條線，留第三鏟。

8. wisdom `rationalism-as-a-tool`「理性主義的工具箱：從笛卡兒的方法到充足理由律」— wujun-realm（ch02-gaining-knowledge-through-rational-thinking/sec-2-what-is-rationalist-thinking、ch02-.../sec-3-what-is-logical-predictability、ch02-.../sec-4-is-there-a-systematic-way-to-find-truth、ch02-.../sec-5-sufficient-reasoning-every-effect-has-a-cause、ch02-.../sec-8-why-rationalism-is-not-omnipotent）。
   第一鏟（wujun-realm）掛第 1 章，第 2 章在既有頁只有一句「理性主義與科學黃金時代的因果」。
   只寫什麼是理性主義思考、邏輯可預測性、有沒有系統地找到真理的方法、充足理由律（凡事皆有因）、理性主義為什麼不萬能。
   避開 wujun-realm 的境界公式與注意力、第 3 章經驗主義、第 4 章尼采；避開 wujun-math-course 的數學思維與笛卡兒；避開 wujun-meta-wisdom 的主人道德。第 6 節理性主義者能不能信上帝、第 7 節牛頓怎麼打開現代西方社會，只在段落裡一句帶到。
   claim 頁；related 連 wujun-realm、wujun-math-course、wujun-meta-wisdom。

9. learning `choosing-a-path`「選什麼路：職業教育、文科與理工科的取捨」— wujun-excellence（ch05-path-of-education/sec-2-trends-vocational-vs-higher-education、ch05-path-of-education/sec-3-future-humanities-vs-stem-majors、ch05-path-of-education/sec-5-environment-unrecognized-talent）。
   第一鏟（wujun-excellence）掛後記與第 1 章，六章各一句；第 5 章「道路」在既有頁只有分類名。
   只寫職業教育對高等教育的趨勢、文科理工怎麼選（中等收入陷阱與文科生數量無關、工業革命的真相、各國文理比例、蘇聯的教訓）、環境與未被看見的才能。
   避開 wujun-excellence 的教育目的、廣度先於深度、節奏；避開 wujun-university 的通才專才（第 5 章第 4 節不選）；第 1 節教育資源不平等不寫，wujun-context 的當下部有同題材料，留給那邊。
   claim 頁；related 連 wujun-excellence、wujun-university、wujun-insight。
   材料約一萬三千字，正文目標 1400 到 2000 字。

##### 不開（0 本）

九本都是脊梁、每本都有一章以上沒被第一鏟碰到的材料，全部開單。

##### 小結

- 開 9 張，全部 claim 頁；人物站單一作者，沒有「一個問題多本書吵」的形狀。
- 第一鏟是整本書導覽，所以第二鏟的紀律是「一章撐一頁」，起草時不要回頭重講全書。
- 最薄的兩張是第 6（數學之美）與第 9（卓越），正文目標下修，寫不滿就停。
- 起草順序建議：7、2、4（人生線，材料最厚）→ 1、3、9（教育與做事）→ 5、8（方法論）→ 6。
- 每頁寫完補進該分類 `_index.md` 的 roadmap（tier: advanced），related 雙向；導覽第三章講那本書的那行補一句連到新頁。

#### biblical-studies-note 第二鏟選題單（DEEPEN-TARGETS 九本大部頭，Fable 開單 2026-11-06）

判準取自 note-check §1.3 與 §1.4：只為脊梁書開頁，頁要能單獨被引用、主張要標得到具體章節 anchor、與既有 83 頁重疊低於一半。
每張單寫明第一鏟掛了什麼、第二鏟只寫什麼、避開哪幾頁；章節目錄名全部是書 repo 裡實際存在的目錄。
逐卷、逐條查閱體裁的書不開第二頁，改列進 `export-deepen-targets.py` 的體裁排除。

##### 開單（7 張）

1. hermeneutics `grammatical-fallacies`「文法謬誤：不定過去式、關身語態與冠詞規則」— exegetical-fallacies（02-grammatical-fallacies/01-the-flexibility-of-new-testament-greek、02-grammatical-fallacies/02-the-aorist-tense、02-grammatical-fallacies/04-the-middle-voice、02-grammatical-fallacies/06-conditionals、02-grammatical-fallacies/08-the-article-the-granville-sharp-rule、02-grammatical-fallacies/09-the-article-the-colwell-rule）。
   第一鏟（exegetical-fallacies）掛了 01、03、04 三部，只寫字義、邏輯、預設三類謬誤，第 2 部一字未提。
   只寫卡森為何文法例子反而少、新約希臘文的彈性、不定過去式不表「一次完成」、關身語態不等於反身、條件句的真值、Granville Sharp 與 Colwell 兩條冠詞規則各能證明什麼與不能證明什麼。
   避開 exegetical-fallacies 的字根謬誤、語意時代錯置、錯誤二分；避開 nt-textual-criticism 的抄本異文。
   claim 頁；related 連 exegetical-fallacies、hermeneutical-spiral、nt-textual-criticism、nt-use-of-ot。

2. new-testament `canon-formation`「二十七卷怎麼成為新約：正典化的歷程與判準」— new-testament-in-its-world（08-textual-criticism-and-canon/02-canonization；08-textual-criticism-and-canon/01-textual-criticism 只在對照 Ehrman 時用一段）。
   第一鏟（gospels-in-cultural-context）掛的是 01 方法論與 02 第一世紀世界；站上 83 頁沒有一頁講正典成形。
   只寫正典化的歷程、各卷被認可的時間與判準、哪些書在邊緣、Wright 與 Bird 怎麼回答「誰決定的」。
   避開 nt-textual-criticism 的抄本與異文論證（那頁以 Ehrman 為骨幹；Wright 的文本鑑別立場最多列 alternative 一段）、避開 gospels-in-cultural-context 的對觀問題與作者考證。
   與 nt-wright-note 分工：那站的 new-testament-in-its-world 頁寫全書三軸與教學法（tier tool），這裡只取正典這一章；Paul 的部分（05-paul/02-primer）不開，nt-wright-note 已有 paul-and-the-faithfulness-of-god 頁。
   claim 頁；related 連 nt-textual-criticism、gospels-in-cultural-context、reading-nt-as-history、hebrews-son-and-better-covenant。

3. new-testament `jesus-and-women-middle-eastern-eyes`「耶穌與婦女：中東之眼下的幾次相遇」— jesus-through-middle-eastern-eyes（05-jesus-and-women/01-jesus-and-women-introduction、05-jesus-and-women/02-the-woman-at-the-well、05-jesus-and-women/03-the-syro-phoenician-woman、05-jesus-and-women/04-the-lady-is-not-for-stoning、05-jesus-and-women/06-the-widow-and-the-judge）。
   第一鏟（birth-through-middle-eastern-eyes）只用了導論與降生一章；Bailey 的六大主題群裡婦女這一群完整未挖。
   只寫舊約高峰與兩約之間的墜落、婦女門徒的證據、井旁婦人的白天與黑夜編排、敘利亞腓尼基婦人、行淫婦人、寡婦與法官；每個相遇只取 Bailey 的文化讀法。
   避開 birth 頁的平行體工具箱與默示觀、避開 prodigal 頁的比喻方法論（比喻那一群留第三鏟）。
   claim 頁；related 連 birth-through-middle-eastern-eyes、prodigal-through-middle-eastern-eyes、john-the-crucified-king、luke-written-for-certainty。

4. biblical-theology `idolatry-and-image-restoration`「拜什麼就像什麼：偶像崇拜與神的形像的恢復」— a-new-testament-biblical-theology（05-part-4/01-idolatry-and-image、05-part-4/02-image-restoration-ot-synoptic、05-part-4/03-image-restoration-paul-hebrews-revelation）。
   第一鏟（new-creation-storyline）掛導論、舊約主線、已然未然，取的是全書框架；第 4 部整部未挖。
   只寫 Beale 的核心命題：罪的根源是拜偶像、人變得像所崇拜的、耶穌作為末世亞當在對觀福音書恢復形像、保羅與希伯來書與啟示錄的形像恢復。
   避開 new-creation-storyline 的五步循環與末世透鏡；避開 adam-and-eve-archetypes 的 Walton 原型讀法（只在 related 連過去，不重講）。
   claim 頁；related 連 new-creation-storyline、adam-and-eve-archetypes、genesis-one-functional-creation、eden-to-new-jerusalem。

5. hermeneutics `knowing-god-through-his-word`「我們怎麼能知道：三種認識論立場與神人之言」— according-to-plan（02-biblical-theology-how/01-god-makes-himself-known、02-biblical-theology-how/02-but-how-can-we-know、02-biblical-theology-how/05-bible-is-divine-human-word）。
   第一鏟（kingdom-according-to-plan）掛 01、02、03 三部整部，但方法那條只寫了「從基督開始也以基督為終」，認識論三立場與神人之言兩章沒有進頁。
   只寫完全獨立於神、部分獨立於神、完全依賴啟示三種立場及其後果、神藉既神聖又人性的話說話、不能貶低一邊來尊崇另一邊。
   避開 kingdom-according-to-plan 的國度框架與各站圖示、避開 02-biblical-theology-how/06（從基督開始，第一鏟已寫）、避開 authorial-intent-and-meaning 的 Vanhoozer 詮釋學論證。
   claim 頁；related 連 kingdom-according-to-plan、authorial-intent-and-meaning、hermeneutical-spiral、vos-biblical-theology。

6. old-testament `yahwehs-four-partners`「雅威的四個夥伴：以色列、人、列國、受造界」— theology-of-the-old-testament（05-israels-unsolicited-testimony/01-israels-unsolicited-testimony、05-israels-unsolicited-testimony/02-israel-as-yahwehs-partner、05-israels-unsolicited-testimony/03-the-human-person-as-yahwehs-partner、05-israels-unsolicited-testimony/04-the-nations-as-yahwehs-partner、05-israels-unsolicited-testimony/05-creation-as-yahwehs-partner）。
   第一鏟（testimony-and-countertestimony）掛 03、04、06 三部，寫法庭隱喻、核心見證與反見證、中介；第 5 部「未被要求的見證」整部未挖，而它是全書最厚的一部。
   只寫證人為何說出未被要求的話、以色列作為神學現象的古怪、舊約對自主普世人性觀念毫無興趣的人觀、列國在雅威面前的位置、受造界作為夥伴。每個夥伴取 Brueggemann 自己的「關係中的雅威」這條線。
   避開 testimony-and-countertestimony 的證詞文法與哀求詩篇、避開 ethics-for-gods-people 的 Wright 舊約倫理框架。
   claim 頁；related 連 testimony-and-countertestimony、ethics-for-gods-people、genesis-one-functional-creation、ane-comparative-reading。

7. old-testament `prophets-are-not-ecstatics`「先知不是狂喜者：赫舍爾對狂喜論、詩人論與病理論的反駁」— prophets-heschel（02-prophetic-consciousness/08-prophecy-and-ecstasy、02-prophetic-consciousness/10-examination-of-ecstasy-theory、02-prophetic-consciousness/11-prophecy-and-poetic-inspiration、02-prophetic-consciousness/12-prophecy-and-psychosis、02-prophetic-consciousness/14-event-and-experience）。
   第一鏟（prophetic-pathos）用整部當 anchor，寫的是悲愴、同感、忿怒與四位先知的音色；第二部後半那一整段對學界化約論的反駁未進頁。
   只寫狂喜概念的源流、「先知即狂喜者」從斐羅到現代學術怎麼嫁接進來、Heschel 逐項拆解的理由、先知靈感與詩人靈感是主體對主體與客體對客體之別、病理化指控的拆解、靈感是神轉向人的事件而經驗只是回響。
   避開 prophetic-pathos 的悲愴與忿怒論、避開 ethics-for-gods-people（公義那章 01-the-prophets/11 留第三鏟）。
   claim 頁；related 連 prophetic-pathos、jeremiah-against-wind-and-tide、isaiah-vision-and-trust、amos-lion-and-plumb-line。

##### 不開（2 本）

- how-to-read-the-bible-book-by-book《聖經導覽手冊：逐卷讀經的藝術》（Fee & Stuart）：不開。逐卷導覽體裁，每章是一卷書的定位卡；站上 61 個逐卷頁已各自承重，再開只會是第二份目錄。第一鏟 book-by-book-reading 已把全書的方法（大故事四段、兩個隨身問題）寫完。tier 維持 spine（承諾已由既有頁兌現），建議加進 `export-deepen-targets.py` 的 EXCLUDED_KINDS，理由「逐卷導覽，按卷查閱」。可做的是補 anchor：既有逐卷頁若缺第二來源，掛它對應卷的目錄。
- hard-sayings-of-the-bible《聖經經典500問》（Kaiser、Davids、Bruce、Brauch）：不開。逐條釋疑合輯，章節數是書卷數不是論證數；第一鏟 handling-hard-sayings 已寫兩類難、五個來源、十二篇導論文章與創世記示範。tier 維持 spine，同樣建議加進 EXCLUDED_KINDS，理由「逐條釋疑，按經文查閱」。第三鏟若要開，唯一的候選是 02-historical-books/01-joshua 的聖戰與滅絕令，但要先確認與 joshua-whose-land-whose-israel 的重疊。

##### 小結

- 開 7 張，全部 claim 頁；九本都是單一體系書或單一作者，沒有「一個問題多本書吵」的形狀。
- 不開 2 本，都是查閱體裁，tier 不動，建議進體裁排除名單。
- 補上的結構空洞：新約正典成形（第 2 張，站上零頁）、舊約人觀與夥伴論（第 6 張）、先知意識的學術論戰（第 7 張）。
- 第三鏟候選順手記下：Bailey 的比喻群（06-the-parables-of-jesus，好撒馬利亞人、葡萄園主）、Heschel 的歷史與公義（01-the-prophets/09、11）、Beale 的教會即以色列與土地應許（08-part-7）、Brueggemann 的詮釋前景（07）。
- 起草順序建議：2、6、7（結構空洞）→ 4、5 → 1、3。

#### 技術站六站：導覽第四章具名爭點 → `kind: debate` 對照頁（Fable 2026-11-06 開單；起草交 Opus，每頁一個子代理、路徑 A）

判準同 investing 那批（note-check §1.4 形狀測試）：一個問題、多本書吵、各造都已有溯源頁 → 對照型 concept；導覽第四章已下的裁決留在導覽，debate 頁只並排各造主張、各自掛 anchor，判別變數只寫書裡作者自己說的。
anchor 一律從兩造既有概念頁的 `furtherReading` 取，不另找章；起草前先讀兩造的頁與導覽該節，避開各頁已講完的論證。
這六站都是 strict 站，`seeAlso.site` 只能填技術站 key；寫完補進該分類 `_index.md` roadmap，`related` 雙向連到兩造的頁。骨架照 clean-code `comments-formatting/to-comment-or-not.md`，標題用中立問句，「共識區與爭點」那節不寫「真正的」。
形狀不過的四題（導覽自己判為互補、接力，或只有一造在說話）不開，理由列在最後。

#### clean-code-note（2 張）

1. complexity `small-functions-or-deep-modules`「小函式還是深模組：拆分讓讀者腦中要裝的東西變少，還是只是搬了家？」— Clean 學派：refactoring 第 6 章 Extract Function、clean-code 第 3 章（extract-function；long-function 頁另掛 refactoring 第 3 章與 code-complete 第 7 章）；深模組派：philosophy-of-software-design 第 9 章（better-together-or-better-apart）；量尺：code-that-fits-in-your-head 的 03-complexity 與 02-sustainability/03-decomposition（code-that-fits-in-your-head 頁）；上游：mythical-man-month 第 4 章貴族制與民主制（conceptual-integrity 頁，只取功能／複雜度比率那一章）。避開 extract-function 頁的抽取判準與步驟、better-together 頁的四項拆分成本清單、code-that-fits 頁的分形架構與檢查表全貌、conceptual-integrity 頁的第二系統效應；只並排三件事：拆的判準（Fowler「一行也值得抽」對 Ousterhout「介面本身就是負荷」）、兩造都接受的紅旗（連體方法、抽出後要在父子函式間來回翻）、Seemann 的七格預算與他自己劃的界線「指標只說該分解了，不說分解什麼」。Brooks 的「設計由誰做主」只當上游一句，不展開。
2. testing `mocks-or-state`「mock 驗互動還是驗狀態：領域模型住在物件的狀態裡，還是住在物件之間的溝通裡？」— 古典派：art-of-unit-testing 第 2 部 03、04（test-doubles-stubs-vs-mocks）與第 3 部 08 三支柱（pillars-of-good-unit-tests）；倫敦學派：growing-object-oriented-software 的 01/02、02/01、02/04、04/01 四章（london-school-outside-in-tdd）。避開 test-doubles 頁的 stub／mock 定義教學、pillars 頁的可信賴與可維護全套手段、london-school 頁的行走骨架與由外而內流程；只並排「互動測試是最後手段、一測一 mock」對「mock 同儕不 mock 內部、期望即契約」、Osherove 的三種結果分類對 GOOS 的「行為是組合的湧現性質」。判別變數只寫書裡的：兩造各自寫下的過度指定紅線（Osherove 一測一 mock；GOOS 期望要少、不 mock 值、不 mock 具體類別）。不判誰對，兩頁互列 related。

#### agile-note（2 張；爭點二與三合併成一張）

3. flow `timebox-or-flow`「時間盒還是流動：節奏該由迭代邊界規定，還是由交易成本議定？」— 時間盒派：essential-scrum 第 1 部 04 Sprints 與 scrum-the-art-of-doing-twice 的「掌握時間的節奏」（timebox-is-the-constraint）；流動派：kanban 的 01/01、01/02、03/03 建立交付節奏、03/10（kanban-method-evolutionary-change）、kanban-in-action 第 12 章陷阱（kanban-pitfalls，Schwaber 的死亡行軍批評與回應都在這章）與第 9 章規劃與估算（kanban-planning-and-estimating）；地基：principles-of-product-development-flow 的 03 佇列與 05 批量（cost-of-delay-and-queues，只取「兩邊都在壓批量與佇列」這一點）。避開 timebox 頁的六個好處清單與變更／釐清之分、kanban-method 頁的五核心屬性與無權者變革策略、planning 頁的訂購點機制；只並排 Schwaber 的指控、Anderson 正面拒絕時間箱並解耦三種節奏與「故事跨三迭代」的失能證據、Rubin 的「延長 Sprint 是症狀不是理由」、Hammarberg 的「時間盒要主動放回去」。判別變數只寫書裡的：Anderson 自己說的「頻率由交易成本與協調成本議定」、kanban-in-action 的「工作來源只有一個 Backlog 還是隨時冒出」。
4. adoption `can-agile-scale`「敏捷放大之後，跨團隊依賴怎麼辦：不存在、把依賴管起來，還是把依賴設計掉？」— 不存在派：clean-agile 第 6 章（becoming-agile；同章 Damon Poole 的就地反對也在，照書寫成第四個聲音）；管理派：succeeding-with-agile 第 17 章規模化與第 18 章分散團隊（scaling-and-distributed-teams）、essential-scrum 第 11、12 章 Release Train 與組件團隊乘法（development-team）；設計派：team-topologies 的 01/02 康威定律、01/03 團隊優先、02/02 四種拓撲、03/01 互動模式（conways-law-and-cognitive-load、four-team-types-and-interaction-modes）。合併理由：爭點二與三共用 scaling 頁與 development-team 頁，分開寫會各寫一半，且三造回答的是同一個問題「規模化之後依賴怎麼辦」。避開 becoming-agile 頁的四個價值觀與教練批評、scaling 頁的分散團隊六條凝聚力工法、conways 頁的認知負荷上限論證、four-team-types 的四拓撲三模式全表與 6:1 比例；只並排三造處方與各自承認的前提：Bob 自承沒研究 SAFe／LeSS、Cohn 的「可以擴展但需要相當程度的額外開銷」、Skelton 與 Pais 承認既有架構會反推新團隊結構而需要過渡模式。判別變數只寫書裡的：Cohn 提出、Team Topologies 沿用的兩個溝通路徑問題（最小化路徑數、是否鼓勵本不該溝通的團隊溝通）；「並非所有溝通都是好的」是 Team Topologies 原話。SAFe 與 LeSS 原生書未收，不能寫成一造，core 只能點名缺席。

#### data-systems-note（1 張）

5. cqrs-eventsourcing `where-does-truth-live`「真相住在哪：資料庫是事實、log 是副產物，還是 log 是事實、狀態只是快取？」— 資料庫在前：designing-data-intensive-applications 第 12 章串流處理（change-data-capture）、designing-event-driven-systems 第 3 部 02 事件流作為共享事實來源（cdc 頁）；log 在前：cqrs-command-query-responsibility-segregation 的 01 概覽與 03 範例專案（event-sourcing）、versioning-in-an-event-sourced-system 第 2 章「為什麼不能更新事件」與第 8 章 copy-and-replace（event-versioning）；兩邊都站的證人：designing-event-driven-systems 第 2 部 03（cdc 與 event-sourcing 兩頁都掛）。避開 cdc 頁的雙寫問題與 binlog 機制、event-sourcing 頁的 replay／snapshot／讀模型機制、event-versioning 頁的 upcast 與 weak schema 全套；只並排「唯一 source of truth 在資料庫，log 是本來就有的副產物」對「事件是事實、狀態是 cache」，以及 Stopford 自己說的「資料庫是一道連貫的接縫、CDC 是坡道」「資料庫在前保住讀你所寫」與 Young 的「不可變沒有中間地帶」及其三個失效（快取、稽核、WORM）。判別變數只寫兩位作者原話：改造成本、事後改不掉只能補償。導覽的「按改造成本選方向」是裁決，不進頁。

#### design-patterns-note（1 張）

6. paradigms `patterns-vocabulary-or-patch`「模式是永恆語彙，還是語言缺陷的補丁？」— 語彙派：timeless-way-of-building 的 01 永恆之道、03-the-gate/02 我們的模式語言、03-the-gate/07 模式的真實性（timeless-way-and-pattern-language）；補丁派（作者自己說「部分對」）：functional-design-principles-patterns-practices 第 5 章 Design Patterns Review（gof-in-functional）；對照：thinking-in-programming-paradigms-and-oop 的 2、3 章（oop-vs-functional）。GoF 本書沒有任何頁掛 `docs/01-introduction/`，照「anchor 只從既有頁取」的規則不掛 GoF；語彙派的原典用亞歷山大，GoF 只能在內文點名。避開 timeless-way 頁的無名品質七個詞與語言崩解史、gof-in-functional 頁逐一模式的三種函式形式、oop-vs-functional 的整張對照表；只並排「模式是從活的結構裡辨認出來的、判準是衝突的力能否自行化解」對「Visitor 的雙重分派與 Abstract Factory 的每產品一方法是 closed class 的腳手架、在有一級函數的語言裡蒸發」與「意圖層的模式換範式照收」。判別變數只寫作者自己的：Bob 的「先分意圖與腳手架、再問語言內建了哪部分」、亞歷山大的「語彙可以永恆，用法不一定」（解除專業壟斷卻成了另一種壟斷）。

#### cloud-infra-note（2 張）

7. observability `observability-or-monitoring`「可觀測性對上監控：指標是類別錯誤，還是監控失敗從頭到尾是實踐問題？」— 結構派：observability-engineering 第 1 章、第 2 章除錯實踐差異、第 9 章兩者如何並存（observability-vs-monitoring；three-pillars 頁另掛第 1 章）；實踐派：practical-monitoring 第 1 部 01 反模式、02 設計模式（monitoring-antipatterns）；中間聲音：observability-beginners-guide 的 01 概覽（three-pillars、observability-vs-monitoring 兩頁）、site-reliability-engineering 第 2 部 04 監控分散式系統（兩頁都掛）。避開 obs-vs-mon 頁的控制理論溯源與「不部署新程式碼」檢驗標準、antipatterns 頁五反模式四設計模式的全表、three-pillars 頁三種資料型別的教學；只並排 Majors 的「指標這種資料型別是類別錯誤、三支柱是廠商產品線的投影、指標能承載的複雜度有上界」、Julian 的「監控專案失敗頭號原因是工具偏執、問題在實踐不在工具」與他對分散式追蹤的判斷、Majors 第 9 章的和解條款「監控管系統層、可觀測性管應用層」。判別變數只寫書裡的：Majors 第 9 章的配比「由維運責任決定」。導覽提的兩位作者利益位置與 OpenTelemetry 打臉是站外判讀，不進頁。seeAlso 可連 system-design 的 observability 分類（golden-signals、slo-sli-sla），起草時 `ls` 驗過路徑才掛。
8. slos-error-budgets `control-or-context`「控制還是脈絡：未達可用性目標該凍結部署，還是把差距交給團隊自己改？」— 控制派：site-reliability-engineering 第 2 部 02 SLO 與 site-reliability-workbook 的 02 implementing-slos（error-budget）、site-reliability-engineering 第 3 部 02 on-call 與 workbook 08（on-call，只取「把 pager 還給開發團隊」這道平衡閥）；脈絡派：seeking-sre 第 1 部 SRE implementation 與第 4 部 human side（sre-beyond-google：Netflix 計分卡、Spotify Ops-in-Squads、Facebook「你寫的就是你的」、SoundCloud 八人算術）。避開 error-budget 頁的 SLI／SLO 定義教學與 KPI 章、on-call 頁的 50%／25% 約束推導、sre-beyond-google 頁逐家公司的細節（每家只取一句）；只並排「燒光就凍結」對「沒達標是資訊不是懲罰、先問這個人有沒有足夠脈絡」，以及兩造各自承認的邊界：Seeking SRE 自己標出組織極大與人命關天時倒向控制、SRE book 的 pager 回流是控制路線內建的平衡閥。判別變數只寫書裡的：Blank-Edelman 自承「沒有給判準說明什麼組織適合哪一條」、SoundCloud 的「撐得起一輪值班的團隊最小八人」。編輯刻意不仲裁照書寫，不替他裁。

#### 不開（4 題）

- clean-code 爭點三「錯誤該處理得漂亮還是定義到不存在」：導覽判為分層互補而非對立，兩頁互相引用；Clean Code 治表達、Ousterhout 治源頭，是兩個問題不是一題兩答，形狀測試不過。
- data-systems 爭點一「悲觀還是樂觀」：既有頁 `transactions/optimistic-vs-pessimistic-locking` 本身就是對照頁，重疊超過一半；而且兩造不是不同的書在吵，DDIA 一本提供兩側、「高競爭下 2PL 更穩」那句出自討論區的使用者層，Red Book 的結論是條件論、沒有對造。
- design-patterns 爭點四「尺度上移之後 GoF 的名字還算數嗎」：只有 PoEAA 一造在說話，「名字會失效」是導覽設的預期不是哪本書的主張；重疊 base-patterns 與 web-presentation-patterns 兩頁。
- system-design 爭點四「-ility 怎麼變成可驗收的」：導覽自己判為接力不是替代品，唯一對立「分類值不值得花力氣」撐不起一頁；重疊 architecture-characteristics 與 quality-attribute-scenarios 兩頁超過一半。

（clean-code 爭點二已有 debate 頁、design-patterns 爭點二站已選邊，依指示不列。）

#### 小結

- 13 個候選：開 8 張（覆蓋 9 個候選，agile 爭點二與三合併），不開 4 題。
- 8 張單的兩造頁與 anchor 都已存在，起草不必另找章；唯一的例外是 design-patterns 第 6 張，GoF 本書沒有 intro 頁可掛，語彙派改用亞歷山大當原典。
- 建議起草順序：7、8（cloud-infra 兩造最乾淨）→ 2、1（clean-code）→ 5 → 3、4 → 6。

#### theology-note／philosophy-note：導覽第四章的具名爭點 → `kind: debate` 對照頁（Fable 2026-11-06 開單；起草交 Opus，每頁一個子代理、路徑 A）

判準同 investing 那批（note-check §1.4 形狀測試）：一個問題、多本書吵、兩造各自已有溯源頁，才開對照頁。
debate 頁是導覽第四章那一節的查閱單位版本：各造主張並排、各自掛 anchor、不下裁決；導覽裡「判讀：」「這裡不裁決」之後的話一句都不進頁面，連「不是二選一」這種軟裁決也不寫。
只寫得出處的判別變數，而且要是作者自己說的（阿奎那自己畫的自然理性邊界、巴斯卡自己排的說服次序、索羅斯式的「作者自己畫的界線」）。
anchor 一律從兩造既有頁的 `furtherReading` 取，每條 `[ -d ]`；唯一例外標在單上（philosophy 第 1 張要先補掛一章）。
骨架照 investing 那批（`> 點題` → `::core` 各造一句 → `## 各造立場` → `## ⚖️ 共識區與爭點` → `::takeaways` → `:::response` 空塊）；標題用中立問句。
寫完補分類 `_index.md` roadmap、`related` 雙向、導覽第四章該節末尾加一行連到新頁、重跑 `export-seealso-gaps.py`。

#### theology-note（3 張）

1. apologetics `head-or-heart-apologetics`「護教該從論證還是從心出發？阿奎那、普蘭丁格對巴斯卡、路易斯、卻斯特頓」— 論證造：summa-theologica 第一部（five-ways）、where-the-conflict-really-lies 的 EAAN 與方法論自然主義章（science-and-faith）；心與想像造：pensees 的「論信的途徑」「論打賭的必要」（pensees）、mere-christianity 第 1、2 卷（argument-from-desire）、orthodoxy 第 8 章悖論（imaginative-apologetics）；第三個聲音是條件結構：secular-age 內在框架章（three-faces-of-secular），只寫泰勒「信與不信都涉及超越可用理由的跳躍」這一條，不寫成裁決。
   避開 argument-from-desire 頁已有的「⚖️ 理性派與想像派」三條分工原則（那是路易斯視角的小結，不重講）、避開 faith-in-a-secular-age 頁的五個地基體檢與凱勒「合流手冊」的定位（導覽的判讀）、避開 three-faces-of-secular 的三道堡壘史。
   判別變數只寫書裡有的：阿奎那「神存在對神自明、對我們不自明，只能從結果後驗證明」與「拿不具說服力的理由證明信德之事會損害信德」；巴斯卡「先顯示宗教不違反理性、再使它可愛、最後才證明它是真的」與「不是藉增加證明而是削減激情」；普蘭丁格「表面衝突不構成反證者」；卻斯特頓「與瘋子辯論你多半會輸，要給他空氣不是論證」。
   related：five-ways、science-and-faith、pensees、argument-from-desire、imaginative-apologetics、faith-in-a-secular-age。

2. doctrine `atonement-legal-or-participatory`「十架救贖的重音該落在法理、參與，還是神的受苦？斯托得、賴特、莫特曼」— 法理造：cross-of-christ 第 2 章「全書核心」（cross-of-christ）；參與造：surprised-by-hope 的「重新思考救恩」「整個世界在等什麼」（resurrection-and-new-creation）；第三聲音：theology-of-jurgen-moltmann 第 6 章十字架神學（moltmann-hope-and-cross）；地圖層：erickson-christian-theology 第 8 部 02、03 章（atonement-theories-map），只借艾利克森「每種理論抓住一個元素、沒有一種單獨涵蓋全貌」與「贖罪論取決於前置教義」兩句當框架，不重列五種理論。
   避開 cross-of-christ 頁的四步代贖論證全文（赦免成難題→必須有滿足→被滿足的是神的本性→自我替代，只取「神的自我替代」一句當法理造的立場）、避開 resurrection 頁的「上天堂」誤解史與復活身體論、避開 atonement-theories-map 的五理論逐一評點、避開 order-of-salvation。
   判別變數只寫書裡有的：斯托得「一切不足夠的贖罪論，都源自不足夠的神論與人論」；賴特「救恩不是離開世界而是世界被修復」與「盼望使現在的工作有永恆重量」；莫特曼「兩根柱子不可分離，只有盼望沒有十字架就變成樂觀的社會計畫」與「稱義的原則不是相似性而是對異他性的稱義」。導覽那句「只有法理福音縮成個人脫罪、只有參與十架淡成象徵」是站主判讀，不寫。
   related：cross-of-christ、resurrection-and-new-creation、moltmann-hope-and-cross、atonement-theories-map、incarnation。

3. doctrine `church-engage-or-contrast`「教會對世界的貢獻是進去發言，還是做教會？沃弗、侯活士、潘霍華」— 參與造：a-public-faith 第 3 章失能（public-faith）、exclusion-and-embrace 的「擁抱」與「排斥」章（will-to-embrace）、generous-justice 第 5 章（justice-and-generosity）；對比造：resident-aliens-life-in-the-christian-colony 第 1 部 02 基督徒的政治（已掛在 public-faith 頁）、peaceable-kingdom 第 6 章僕人社群（narrative-ethics）；第三聲音：cost-of-discipleship 登山寶訓「可見的社群」「報復」「隱藏的義」（visible-yet-hidden），只取「鹽與光是你們是不是你們要成為」「舊以色列以力對力、教會放棄政治身分」「逃進不可見就是否認呼召」三條。
   **重疊風險最高的一張**：public-faith 頁已經並排沃弗與侯活士（僑居地、兩人互引）。起草前先整頁讀 public-faith；這頁只寫「公共貢獻的形式」這一個問題，不重講失能框架（怠惰／強制）、不重講僑居地比喻、不重講四幕擁抱。並排之後若與 public-faith 重疊仍超過一半，就改成在 public-faith 補一段潘霍華、不開新頁，並回報。
   判別變數只寫書裡有的：侯活士「教會不是有一套社會倫理，教會本身就是一套社會倫理」；沃弗「邊界本身不是排斥，排斥是阻止與他者創造性相遇的屏障」「暴力是擁抱的反面」；潘霍華「可見的，必須同時被隱藏」。導覽把畢德生歸到侯活士那一側是氣質判讀，不寫；「兩人在最底層反而接近」也不寫成結論，兩造的暴力論各自列在共識區即可。
   related：public-faith、will-to-embrace、narrative-ethics、visible-yet-hidden、justice-and-generosity。

不開（theology）：
- 爭議四 屬靈爭戰紀實的認識論地位：只有一造有頁（spiritual-warfare-realities），批評方沒有書在架上。
- 公分母與「這個書架缺了誰」：沒有對造，是導覽的材料。

#### philosophy-note（4 張）

1. applied `should-we-want-consolation`「痛苦該被減輕，還是該被保留？de Botton 的藥櫃對尼采與卡繆」— 慰藉造：consolations-of-philosophy 第 1、2 章（philosophy-as-consolation）、status-anxiety 第 2 部解方（status-anxiety）；反慰藉造：consolations-of-philosophy 第 6 章「困難的慰藉」（尼采）、myth-of-sisyphus 的「荒謬的推理」「荒謬的人」（absurd-and-philosophical-suicide、revolt-freedom-passion）；旁證：daily-stoic 的 amor fati（premeditatio-malorum）、ego-is-the-enemy 的止痛膏句（ego-as-obstacle）。
   **anchor 例外**：尼采那一章 `docs/06-consolation-for-difficulties/` 目錄存在，但 philosophy-as-consolation 頁沒掛，而該頁正文已在講尼采的反對票。起草前先把這一章補進 philosophy-as-consolation 的 furtherReading（label「哲學的慰藉 — Consolation for Difficulties」），再供本頁取用；這是補既有頁的漏掛，不是另找章。
   避開 absurd 頁的四種荒謬面貌與自殺問題本身、避開 revolt 頁的三個結果全文，只取卡繆「迴避的典型形式就是希望」「荒謬只有在不被同意的限度內才有意義」；避開 philosophy-as-consolation 的六格藥櫃逐一介紹。
   判別變數只寫書裡有的：de Botton「慰藉不是騙自己沒事，而是校正你對事情的預期與詮釋」與「把矛盾留在書裡不縫合」；尼采「痛苦是偉大的必要成本」；卡繆對帕斯卡「消遣」的那句比較（既少一些又多一些）。導覽「衝突點在手段是不是夾帶承諾」「力量對比反過來了」是站主判讀，不寫。
   related：philosophy-as-consolation、status-anxiety、absurd-and-philosophical-suicide、revolt-freedom-passion、premeditatio-malorum。

2. eastern `who-is-doing-the-letting-go`「收心的時候，有沒有一個做判斷的我？斯多噶、Fromm 對佛教、道家、Wright」— 有我造：epictetus-discourses-fragments-handbook 的手冊與第 1 卷（dichotomy-of-control、what-is-up-to-us）、to-have-or-to-be 第 1、2 章（having-vs-being）；無我造：how-the-world-thinks 的「世界如何認知」「世界是什麼樣」（no-self-and-emptiness）、why-buddhism-is-true 第 5、6、7 章（no-ceo-modular-mind）與第 1、3 章（feelings-as-illusions）；回歸真我造：great-thinkers 哲學章老子（way-of-water）。
   避開 dichotomy 頁的可控／不可控清單與面試例子、避開 no-ceo 頁的裂腦實驗全文（只取「意識心至多是眾議院議長」與「判準只有控制與恆常兩條」）、避開 feelings 頁的多巴胺與路怒例子（只取「天擇設計大腦的初衷不是讓我們看清世界」）、避開 way-of-water 的治理論與水的比喻全文（只取「讓被 ego 遮住的真我浮現」與頁上 NOTE 區分道家與佛教的空）。
   判別變數只寫書裡有的：愛比克泰德「眾神只把正確運用印象的能力放進我們手裡」；佛陀「色身若是我，不會讓它自己有不適」（資格論證）；Wright「接納製造距離」；老子「當我放下我所是，我就成為我所能是」；Baggini「明白沒有永恆不變的自我核心，照常生活並沒有什麼不對」。導覽那段「若態度可以是系統的重新配置就未必互斥」的和解假設，連「假設」兩字都不帶進頁面。
   related：dichotomy-of-control、what-is-up-to-us、having-vs-being、no-self-and-emptiness、no-ceo-modular-mind、feelings-as-illusions、way-of-water。

3. political `desert-entitlement-or-worth`「分配該按應得、按資格，還是按價值？羅爾斯、亞里斯多德、桑德爾，與柏拉圖更早的問題」— 資格造：theory-of-justice 第 1 部三章（justice-as-fairness）；價值造：nicomachean-ethics 第 5 卷正義（eudaimonia-and-the-mean）；共善造：tyranny-of-merit 的「贏家與輸家」、public-philosophy 的「道德與政治論證」（tyranny-of-merit、common-good-politics）；前置問題：republic 卷二格勞孔、卷四、卷九（justice-and-the-soul）。效益造只用 justice-whats-the-right-thing-to-do 第 2 章一條「邊沁拒絕自然權利」當對照，不展開。
   避開 three-paths-of-justice 頁的三把尺總覽（那是桑德爾單書的框架頁，本頁不重講「三條路徑」）、避開 utility-and-its-limits 的救生艇與彌爾、避開 justice-as-fairness 頁的無知之幕細節（只取「沒有人應得自己更大的自然能力」與「資格預設合作方案已存在」兩條）、避開 eudaimonia 頁的中庸與習慣論（只取第 5 卷「分配正義是按價值的幾何比例、什麼算價值各家不同」）、避開 justice-and-the-soul 的定義階梯與色拉敘馬霍斯（只取格勞孔三類善與「單獨出現在靈魂裡時還剩什麼」）。
   判別變數只寫書裡有的：羅爾斯「視自己為平等的人不會同意僅為他人更大利益總和接受較差前景」；亞里斯多德「民主派、寡頭派、貴族派對什麼算價值給不同答案」；桑德爾「成功全憑本事的信念腐蝕對彼此的虧欠感」；《理想國》導論「與其說是政治著作不如說是反政治的」照頁上已有的引用寫明是導論的判斷。導覽「同一個困難的兩種閃避法」「柏拉圖沒有回答格勞孔」是站主判讀，不寫。
   related：justice-as-fairness、eudaimonia-and-the-mean、tyranny-of-merit、common-good-politics、justice-and-the-soul、three-paths-of-justice。

4. stoicism `rehearse-death-or-forget-it`「死亡該天天預演，還是別去想？斯多噶對蒙田」— 預演造：daily-stoic 的「知覺的紀律」「行動的紀律」、letters-from-a-stoic 書簡 26（premeditatio-malorum）、epictetus-discourses-fragments-handbook 手冊「日復一日把死亡擺在眼前」（what-is-up-to-us）；別想造：how-to-live 的「別擔心死亡」（montaigne-how-to-live）。
   這是四張裡材料最薄的一張，正文 1200–1800 字即可，不灌水。避開 premeditatio 頁的逆境條款操練與 TIP、避開 montaigne 頁其他十九個答案。只並排「每天演一遍」與「越演越不平靜、墜馬後學到死亡到之前你已先離場、農民不去想反而死得從容」。
   判別變數只寫書裡有的：奧理略「不要把心填滿所有可能還會發生的壞事，那不是預想是焦慮」（斯多噶自己對預演的邊界）；Bakewell 轉述蒙田「照斯多噶處方做結果剛好相反」。導覽「路徑相反、終點重合」「同一個目的地有人得繞路」是站主判讀，不寫；amor fati 兩頁都有，可以各自列在共識區，不說「重合」。
   related：premeditatio-malorum、what-is-up-to-us、montaigne-how-to-live、philosophy-as-consolation。

不開（philosophy）：
- 爭點五 和諧靠德行還是靠制度：儒家與法家兩造都出自同一本書（Baggini）同一頁（harmony-over-truth），跟桑德爾的對照是導覽自己說的「筆記的觀察，不是任何一本書的主張」。過不了出處測試與形狀測試，留在導覽。
- 懸置 收心術與第三面權力：Lukes 沒有針對斯多噶發言，「同一個姿態」是策展層的並置；沒有一本書在吵這一題，過不了出處測試。要處理只能在導覽，或等收到一本把兩者對質的書。
- 共識一到三：沒有對造。

#### 小結
- 開 7 張：theology 3、philosophy 4。全部兩造都有既有溯源頁，anchor 可從既有頁取；唯一例外是 philosophy 第 1 張要先替 philosophy-as-consolation 補掛《哲學的慰藉》第 6 章（目錄已確認存在）。
- 重疊風險：theology 第 3 張（public-faith 已並排沃弗與侯活士）附了「重疊過半就改補強、不開頁」的退路；philosophy 第 3 張與 three-paths-of-justice 的重疊靠「只寫應得／資格／價值一題、不重講三把尺」控制。
- 不開 5 筆：theology 爭議四；philosophy 爭點五、懸置、共識。
- 起草順序建議：theology 1、2 → philosophy 2、3 → philosophy 1、4 → theology 3（最後做，因為它可能收成補強）。
- 既有頁順手要修的：philosophy-as-consolation 補第 6 章 anchor（上面已列）。

#### 六站導覽第四章的具名爭點 → 八頁 `kind: debate`（Fable fork 2026-11-06 開單；起草交 Opus，每頁一個子代理、路徑 A）

判準同 investing 那批：一個問題、多本書吵、各造都已有溯源頁，才開對照型 concept。
導覽第四章已各寫一節並多半下了裁決；debate 頁是它的查閱單位版本：各造並排、各自掛 anchor、不下裁決，判別變數只寫書裡作者自己說的。
anchor 一律從兩造既有頁的 `furtherReading` 取（八張單點名的每一頁都驗過有 anchor），不另找章。
寫完補進該分類 `_index.md` 的 roadmap，`related` 雙向連到各造頁，導覽第四章該節末尾補一行連到新頁；骨架照 clean-code `comments-formatting/to-comment-or-not.md`，小節標題用「共識區與爭點」（不含「真正的」）。
六站目前都沒有 `kind: debate` 頁，只有 behaviour-interview 有一頁 `big-tech/cultural-boundary`（文化座標，與本批第 7 張不重疊）。

#### tools-note（2 頁）

1. time-management `what-is-efficiency-for`「效率省下的時間該換什麼：外包、慢下來，還是接受做不完？」— 變現派：life-leverage IGV 與外包瑣事（life-leverage-outsource）；慢速派：slow-productivity 做更少、自然節奏、品質執念（slow-productivity）；拒絕前提派：four-thousand-weeks 效率陷阱、電子郵件輸入端無限、洗衣機與乾淨標準同步上漲（finitude-four-thousand-weeks）。
   第四造是被 Burkeman 點名的排序法：first-things-first 大石頭寓言（clock-and-compass-quadrant-two）、essentialism／one-thing 關鍵少數（essential-few-over-trivial-many），只並排「寓言說了什麼」與「Burkeman 說老師作弊了」兩句，不替排序法辯護。
   避開導覽的「Burkeman 勝在唯一不預設終點」與「被降級的是終極目標不是工具」兩句裁決；避開 four-thousand-weeks 頁對有限性的完整論證。
   判別變數只寫書裡有的：Burkeman 自己說的「任何技巧的衡量標準是它能否幫你忽略對的東西」、Moore 的 IGV 門檻、Newport 的三原則。

2. habits `what-makes-a-habit-stick`「什麼讓一個習慣黏住：渴求、重複，還是情緒？」— 渴求派：power-of-habit 渴求與黃金法則、習慣不會被刪除只會被壓到背景（habit-loop-and-golden-rule）；重複與身分派：atomic-habits 每一次行動都是為身分投票、每天 1%（systems-over-goals-atomic-habits）；情緒派：tiny-habits 情緒創造習慣、21 天與 66 天都不準確、有時做一次就形成（tiny-habits-behavior-design）。
   共識區可收「身分」這條會師，三本書都在站上：atomic-habits 的身分層、indistractable 的身分協議與「我不」對「我不能」兩倍實驗（internal-triggers-indistractable）、7-habits 的品格倫理對個性倫理（seven-habits-effectiveness）。
   避開導覽的「三本疊起來是一條完整路徑」與「Fogg 的說法比較具體」兩句裁決；避開各頁對自家四步驟或 B=MAP 的完整講解。
   判別變數只寫書裡有的：Fogg 自己對通用天數公式的否定、Duhigg 自己說的「保留提示與獎酬、只置換慣性行為」、Clear 的 identity 字源。

#### writing-note（1 頁）

3. story-structure `design-first-or-discover-by-writing`「結構先設計，還是邊寫邊發現：五本書的三種答案」— 設計派：anatomy-of-story 先從自我揭露的終點寫起再回推（character-arc）、story-mckee 握有高潮之後反向重寫（story-shape）；發現派：bird-by-bird 的 Doctorow 車燈比喻（bird-by-bird）、writing-down-the-bones 堆肥、你不掌控寫作（composting）；第三造：draft-no-4 結構從素材內部長出來、但動筆前必須先蓋藍圖、三十六張卡片與夾板（nonfiction-structure）。
   避開導覽共識一的「初稿用車燈、重寫用反向設計」和解（那是導覽的判讀）；避開各頁對 Truby 七步驟、McKee 五部分的完整講解。
   判別變數只寫書裡有的：麥克菲自己說的高中老師麥基的規矩與「設計的依據從素材來」、Lamott 轉述的車燈距離、Truby 的操作順序。

#### thinking-note（1 頁）

4. consciousness `where-is-the-self`「自我在哪裡：沒有劇場、湧現的迴圈、腦幹的 SELF，還是自性？」— 拆掉派：consciousness-explained 多重草稿、沒有匯聚點、任何意識時刻都是武斷劃線（no-cartesian-theater）；湧現派：godel-escher-bach 自我符號參與決策、怪圈（strange-loops-and-self）；腦幹派：affective-neuroscience 的 SELF 原始神經表徵（social-emotions，該頁只有一段講 SELF，起草者要讀 docs/03-social-emotions/ 原文把它寫夠）；統整派：jungs-map-of-the-soul 自我只是意識的中心、自性更廣（individuation-and-the-self）。
   第五個聲音已在站上可選用：being-you 自我本身也是一種知覺、一束被編織的最佳猜測（controlled-hallucination）。
   避開導覽的「Jung 是類別錯誤」裁決：Jung 回答的是哪個問題，用 Stein 導讀自己的話寫，不寫「混讀是錯的」；避開各頁對多重草稿模型、哥德爾不完備的完整講解。
   判別變數只寫書裡有的：丹尼特的「沒有人在看」、侯世達的「沒有小人卻有自我」、潘克塞普把 SELF 放在腦幹的理由。

#### hbr-note（2 頁）

5. leadership-teams `is-feedback-a-fallacy`「回饋能不能拆成技術：SBI 對上回饋的謬誤」— 技術派：hbr-guide-to-coaching-employees SBI、對事不對人、正面回饋是主食（coaching-and-feedback）；謬誤派：hbr-10-must-reads-on-managing-people 特異評分者效應、學習在最強處發生、卓越不是失敗的反面、教學有用但回饋是另一回事（feedback-fallacy）；各給一半的第三來源：hbr-guide-to-delivering-effective-feedback 主管的意見不等於事實、不要叫它回饋（set-up-to-fail，另有 coaching 頁掛的 03-feedback-that-sticks）。
   避開導覽的「兩造對糾錯場合與成長場合的邊界畫在不同地方」那段判讀，但可以並排兩造各自怎麼畫邊界（Buckingham 自己讓步的教學場合、SBI 的「影響」要寫成觀察）；避開 set-up-to-fail 頁對症候群本身的講解。
   判別變數只寫書裡有的：Buckingham 與 Goodall 自己的教學例外、Manzoni 與 Barsoux 的「不要叫它回饋」、SBI 的三段定義。

6. strategy-innovation `assigned-or-genuine-dissent`「異議要指派還是去找真的：魔鬼代言人的兩種用法」— 指派派：hbr-guide-to-making-better-decisions 資產管理公司專設一人（better-decisions）、hbr-guide-to-better-recruiting-and-hiring 至少授權一人質疑、大組設兩位（hiring-for-fit）；找真的派：hbr-guide-to-unlocking-creativity 引 Grant 與 Nemeth，指派的代言人克服不了確認偏誤（unlocking-creativity）。
   三頁各只有一段講這題，起草者要讀三章原文（01-hidden-traps、03-effective-interviews、04-make-org-creative/03-culture-of-originality）把兩造寫夠；材料仍薄，正文目標 1200–1800 字，不灌水。
   避開導覽的「指派是下限、找真的是上限」讀法；避開三頁各自主題（決策偏誤、選才、創造力）的其餘內容。
   判別變數只寫書裡有的：Nemeth 研究的結論、兩位以免孤立的理由。

#### behaviour-interview-note（1 頁；strict 站，seeAlso 只能連技術站，沒有合適目標就留空）

7. pitfalls `reframing-or-padding`「改寫到哪裡算灌水：同一句「主管指派我」的三種溫度」— 最寬：mastering-behavioral-interviews 把被指派重寫成主動當責的 Builder 語言（big-tech-behaviorals）；最嚴：star-interview 代名詞紀律、我做了 X 等於獨力完成、馬斯克式追問（star-action）；居中：mastering-behavioral-interviews 不說謊但側步繞過、從 sprint 帶著任務出來（sensitive-situations）。
   三頁各一，分類落點取 pitfalls，因為這題問的是「哪裡越界」。
   避開導覽的「改寫只許動詮釋層不許動事實層」與「底線取 frameworks 嚴格版」兩句裁決；避開 cultural-boundary 頁的文化座標題；`problems` 欄留空。
   判別變數只寫書裡有的：Yurchenko 自己的代名詞規則與追問機制、Mastering 一書自己寫的「不說謊」限定。

#### design-note（1 頁）

8. design-thinking `who-decides-what-is-good`「好由誰說了算：顧客、處境，還是被塑造的品味？」— 顧客派：simplicity-cycle 專業意見都重要但顧客有最終決定權（why-complexity-seduces）；處境派：change-by-design 直接問只會得到更快的馬、人極善於適應不便（insight-observation-empathy）；塑造派：architecture-of-happiness 品味不是天生落定、需要外部引導才知道該注意什麼、日本美感的反例（promise-of-a-field）。
   導覽說三造「尚未對質」，這頁就是對質的場所；三頁各一，落點取 design-thinking，因為 Brown 與 de Botton 同側且題目是需求從哪來。
   避開導覽的「Ward 只是共識三的反面教材」；避開三頁各自主題（複雜度週期、同理心方法、醜建築）的其餘內容。
   判別變數只寫書裡有的：Ward 自己的「專業意見都重要」前提、Brown 的適應論、de Botton 的 Keene 反例。

#### 不開

無。八個候選兩造（或三造）都各有既有頁且頁上有 anchor，形狀都是一個問題多本書吵。

#### 小結

- 開 8 張：tools 2、writing 1、thinking 1、hbr 2、behaviour-interview 1、design 1；全部 `kind: debate`。
- 最厚的是 1、3、4（各造都有整頁可取材），最薄的是 6（三頁各一段，要回原章）。
- 第 4 張多了一個站上已有的第五聲音（Seth），寫不寫由起草者看篇幅決定。
- 起草順序建議：3、1、5 → 4、8 → 2、7 → 6。

**抽查 Opus 上午產出（Fable）**：整頁讀 investing `rules-or-beliefs`（debate）與 theology `person-and-relation`（claim）。對照頁沒有偷渡裁決，「分歧落在哪裡」三條都是書裡的判別變數；claim 頁具名、有出處、TIP 與 IMPORTANT 都是作者主張。通過，不改。另：hr-note 與 travel-note 從開站起一直缺 `checkedAt`，兩站 checkup 0 blocker／0 warn、bump build 綠，蓋 2026-11-06。

### 兩新站（travel／hr）開站後的分批隊列（2026-09-26 開單，Andrew 要求依模型分批）

**現況**：travel-note 64 本／5 頁（頁/待深挖 0.1，全星系最低）、hr-note 12 本／5 頁（待收 7）；tier-audit 未判層 47（travel 46＋hr 1）、
空頭支票 travel 1（George 的觀光行銷教科書判 support 但沒導覽）、漏接 hr 2（Great People Decisions 兩站皆 support；Radical Candor 溝通站 delegated 零引用）；
galaxy-checkup 77 站 core-version（釘 v0.43.2／v0.43.3，最新 v0.43.4）、guide-unlinked 2（cloud-infra circuit-breaker、security human-factors）、
roadmap-planned 40（travel 12、hr 11、data-science 17）。data-science 的 7 筆空頭支票＋1 漏接自 09-14 開站就在，該站待收 39 本，導覽時機未到。

**Batch 1 — Opus（機械與照單起草，可立刻開）**
- [x] 全星系 bump 到 v0.43.4（2026-09-26 完成：78 站成功 0 失敗，travel 手動補；79 站全在 v0.43.4）：`tools/bump-notes-core.sh v0.43.2 v0.43.4 --push`（travel 是 v0.43.3 另跑一次）；撞 rejected 照 memory：rebase → format:check → push。清 77 筆 warn。
- [x] `/note-wanted` 重挑（2026-09-26：0 本待回填；TOP20 改為 18 本＝data-science 14＋hr 4；Ulrich 兩本與 Dessler 暫不排，hr 沒有 HR 角色分類）「先收這 20 本」（hr 7＋data-science 39）。
- [x] hr-note `alliance`：沒照自動建議判 delegated:career——本輪 hr 已用它寫 tours-of-duty，判 spine。
- [x] guide-unlinked ×2（兩站導覽各織一句，writtenAt 蓋 2026-09-26）：把 cloud-infra `reliability-patterns/circuit-breaker` 與 security `security-engineering/human-factors` 織進既有導覽段落（保語氣、一句真話），改完蓋導覽 writtenAt。
- [x] **roadmap-planned 起草 19 頁**（2026-09-26 全數交付：travel 12＋hr 7；9 筆具名事實抽驗全中、anchor／死鏈／雙向 0；travel 17 頁、hr 12 頁；checkup 全星系 warn 0）（選題已定、標題已定，照 `_index.md` 的 roadmap 直接寫，走路徑 A、每頁子代理、逐頁抽驗 anchor）：
  - travel 12：peak-end-itinerary（Power of Moments）、pacing-a-group-day（Steves）、tour-supply-chain（Business of Tourism）、recovering-from-mistakes（Setting the Table 第 10 章）、working-with-local-partners（Culture Map）、shooting-for-the-edit（Grammar of the Shot）、cutting-for-emotion（Murch）、writing-for-the-ear（Meinzer／Abel）、show-positioning（Make Noise）、europe-in-three-strands（Hirst）、reading-a-cathedral（Taylor）、chasing-the-aurora（Arctic Dreams）。
  - hr 7：four-keys-of-great-managers（First Break）、radical-candor-quadrants、what-to-look-for（Great People Decisions）、interview-questions-that-work（HBR 招募）、talent-density-and-candor（No Rules Rules）、tours-of-duty（Alliance）、autonomy-mastery-purpose（Drive）。
  - 不開（書還沒收）：hr nine-lies-about-ratings、psychological-safety、pay-structure-basics、taiwan-labor-standards；data-science 17 筆等 39 本 wanted。
  - 起草前先 `ls` 落分類既有頁、確認書在本機 books-done；書不在本機就跳過留單。每頁交回後 grep entity、驗 anchor、related 雙向、重數導覽／overview 的頁數。

**Batch 2 — Fable（判斷型，與 Batch 1 可並行）**
- [x] travel-note 判層 46 本（2026-09-26 Fable 裁決，apply-tiers 套用：spine 34（11 本已被頁引用＋23 本各承諾一頁）、support 11、tool 1（Keay 的中國通史當查閱）。真欠債 23＝下面的開單；空頭支票 11 等導覽帶到）：`tools/tier-evidence.py travel-note --detail` → 只輸出 JSON 決策 → 套用走 `apply-tiers.py` → `tier-audit.py` 必跑。目的地 30 本多半 support／tool（講解底氣，不一定開頁），影音與行程設計的主幹判 spine。順手裁 George 那本空頭支票（改 tool 或等導覽帶到）。
- [x] hr-note 漏接 2 筆裁決（兩本在 hr 都已有頁，改判 spine 自挖；漏接歸零）：Great People Decisions（兩站皆 support → 本站改 support 或升 spine）、Radical Candor（溝通站 delegated 零引用 → 誰接？領導力站有 15 頁教練與回饋，改 delegatedTo leadership 或本站自挖）。
- [x] 抽查 Batch 1 的 19 頁（Fable 再抽 8 筆：12%、十種偏誤、寬帶薪酬、留任測試、GIT、朝東敬拜、索耶效應、兩到四年——8 筆全中；tours-of-duty 的「二到五年」我一度誤判為錯，回查第 2 章「首段轉變型任期通常持續兩到五年」是對的——教訓：回源 grep 的窗口別用同一行前 50 字，短句會漏）（Opus 已抽 9 筆全中；hr 兩筆漏接現在兩本在 hr 都有頁：Great People Decisions → what-to-look-for、Radical Candor → radical-candor-quadrants）：逐頁具名事實回源 grep＋entity／anchor／雙向掃描（協議在 MODEL-ROUTING §四）。
- [x] **第二輪選題開單**（2026-09-26，單在下方「Batch 3 開單」；等 Andrew 過目）：travel 還有約 35 本零引用（目的地區域書為主）、hr 借來的 8 本——每頁的邊界、避開哪些既有頁、anchor 落哪幾章；**選題清單先交 Andrew 過目再動筆**。travel 的行程規劃／領隊兩塊不收書、要從 lotto 供應商地圖與領隊返國報告寫頁，這種頁的選題也在這一步。

**Batch 3 開單（Fable 2026-09-26；27 頁，每頁一個子代理、路徑 A；起草前照例 `ls` 落分類既有頁、先讀既有頁 core、anchor 逐一 `[ -d ]`；每頁寫完補進 `_index.md` roadmap）**

travel-note（24 頁；先做第一級區域與四條工作線，第二級區域殿後）
1. tour-design `staging-an-experience`「行程是一場被設計的體驗：體驗經濟的四個領域」— experience-economy（01-preview、02-intermission）。避開 peak-end-itinerary 的峰終／轉折，只寫 4E 領域、主題化、紀念物、把服務「演」出來。
2. tour-leading `unreasonable-hospitality-playbook`「超乎常理的款待：意圖、儀式與『織夢』怎麼設計」— unreasonable-hospitality（02 making-magic、03 power-of-intention、07 setting-expectations、13 leveraging-affirmation）。避開 enlightened-hospitality 的定義與五個 A，只寫 Guidara 的做法。
3. travel-video `documentary-story-design`「一趟團剪成一集節目：紀錄片的故事設計與 treatment」— documentary-storytelling（01-story-design、02-ideas-to-treatments）。避開 shooting／cutting 兩頁的技術層。
4. travel-video `youtube-algorithm-and-shorts`「演算法看什麼：點閱率、觀看時長與 Shorts」— youtube-formula（01-the-platform、03-the-youtube-formula）。避開 seven-cs 的策略層，只寫機制。
5. travel-video `scripting-for-the-screen`「影像腳本怎麼寫：從溝通問題到分鏡稿」— writing-for-visual-media（01、02，03 視需要）。避開 writing-for-the-ear（聲音）。
6. podcast `travel-narrative-craft`「旅遊敘事的工藝：從行程筆記到能讀出聲的故事」— how-to-be-travel-writer（**repo 不在本機，起草前先 clone 進 books-done/personal/lifestyle/travel/**）。
7. destinations `story-of-art-for-tour-leaders`「藝術的故事：走進歐洲教堂與美術館前的幾個轉折」— story-of-art，挑 09 church-militant、10 church-triumphant、12 conquest-of-reality、15 harmony-attained、16 light-and-colour 等 6–8 章（哥德、文藝復興、巴洛克、印象派——對準團會進的館）。避開 reading-a-cathedral 的建築讀法。
8. destinations `japan-through-its-culture`「日本文化史的幾個轉折：寺社、庭園、茶道從哪來」— japanese-culture（02 buddhism、03 court、05 medieval-taste、07 bourgeois-culture）。
9. destinations `walking-japan-north-to-south`「從宗谷岬走到佐多岬：Booth 眼中的日本鄉間」— roads-to-sata（01–04 北海道／東北、09 九州）。旁白語氣的範本，不重講文化史。
10. destinations `alps-passes-and-peaks`「阿爾卑斯：從日內瓦湖到聖哥達、從海蒂之鄉到格林德瓦」— alps-human-history（01、02；03 只在講到因斯布魯克時用）。
11. destinations `why-switzerland-works`「瑞士為什麼是瑞士：四種語言、州與直接民主」— why-switzerland（01、03 politics、04 language、06 religion；02 history 視需要）。與 #10 分工：#10 是山，#11 是國。
12. destinations `germany-in-objects`「用物件講德國：MacGregor 的記憶之國」— germany-memories-of-a-nation（01 where-is-germany、02 imagining、04 made-in-germany、06 living-with-history）。
13. destinations `discovering-france-beyond-paris`「巴黎之外的法國：Robb 的鄉間地理」— discovery-of-france（結構是 01-part-one／02-part-two，起草者先讀目錄自己切；itinerary 那節可用）。
14. destinations `cultural-journey-sites`「文化苦旅的路線：敦煌、都江堰、江南小鎮」— bittersweet-journey-through-culture（02 mogao、03 yangguan、04 crescent-spring、07 dujiangyan、08 three-gorges、14 jiangnan、17 west-lake）。對準中國線實際會去的點。
15. destinations `rome-in-the-ruins`「從羅馬到達爾馬提亞：SPQR 的帝國怎麼走到你腳下的遺跡」— spqr（07 from-empire-to-emperors、09 augustus、10 fourteen-emperors、12 rome-outside-rome）。義大利、克羅埃西亞、西班牙三線共用。
16. destinations `al-andalus-three-faiths`「安達魯斯：三教共處的西班牙與摩洛哥」— ornament-of-world（01、02、03）。西葡摩線。
17. destinations `desert-solitaire-and-industrial-tourism`「拱門與『工業化觀光』：Abbey 對國家公園的兩種看法」— desert-solitaire（01、05 industrial-tourism、06 rocks、12 down-the-river）。美西線。
18. destinations `southeast-asia-in-one-map`「東南亞是什麼：宮廷、農民與殖民的三層」— southeast-asia-introductory-history（01、03、05）。
19. destinations `istanbul-huzun`「呼愁：Pamuk 的伊斯坦堡怎麼看博斯普魯斯」— istanbul（05 black-and-white、06 bosphorus、10 huzun）。土耳其線。
20. destinations `three-thousand-years-on-the-nile`「尼羅河上的三千年：神權、榮光與衰落」— rise-and-fall-of-ancient-egypt（01、03、05）。
21. destinations `almost-nearly-perfect-five`「北歐五國各自的『不完美』」— almost-nearly-perfect-people（挑 01 丹麥、03 挪威、05 瑞典，冰島 02 一段）。峽灣／極光線。
22. destinations `natashas-dance-two-russias`「兩個俄羅斯：聖彼得堡的歐洲與莫斯科的土地」— natashas-dance（01、03、05）。
23. destinations `aotearoa-two-settlements`「兩次移民的紐西蘭：毛利與英國」— penguin-history-of-new-zealand（01、02、03）。
24. 行程規劃作業層（**不是書，要 Andrew 點頭**）：`supplier-memory-from-leader-reports`「供應商地圖：領隊返國報告怎麼變成下一團的選擇」— 資料源 lotto ADR-0015／0021／0033 與 dataset.json 的 suppliers／atlas；涉及內部供應商評分，站在密碼閘門後但仍要 Andrew 決定可不可以寫、寫到什麼粒度。

hr-note（3 頁）
25. culture-people-ops `radical-honesty-and-good-goodbyes`「徹底誠實與好聚好散：McCord 的 Netflix 人資」— powerful-mccord（03 humans-hate-being-lied-to、04 debate-vigorously、06 someone-really-smart、08 good-goodbyes）。避開 07 pay（已用）與 talent-density 頁的 Hastings 版。
26. recruiting `dont-trust-your-gut`「別相信直覺：Google 怎麼把面試變成結構化評分」— work-rules（03 lake-wobegon、04 searching、05 dont-trust-your-gut）。與 the-a-method、interview-questions 分工：這頁是 Google 的資料與制度（面試上限、委員會、結構化評分），不重講 Who 的四道面試。
27. performance-feedback `two-tails`「兩端：績效管理為什麼人人討厭，最好與最差的人為什麼要分開看」— work-rules（07、08 two-tails、09 learning-institution）。

不開：hook-point、grammar-of-the-edit、be-our-guest、balkans、vietnam、beyond-sky、notes-from-small-island、coming-into-country（3 章）、tv-studio／directing-documentary（判 support，導覽帶到即可）；china-history 判 tool。

**Batch 3 執行（Opus 2026-09-26）**：27 張單交付 25 頁——travel 22 頁（39 頁／39 本被引）、hr 3 頁（15 頁）。
- **沒寫 2 張**：#6 `travel-narrative-craft`——how-to-be-travel-writer 書站只有章節骨架（每章 _index.md 只有 frontmatter，PDF 在 books-management/new-books/how-to-be-travel-writer/），等書寫完再起草；#24 供應商地圖——**不開，結案**（Andrew 2026-09-26 裁定：供應商評分是旅行社內部 DB 的東西，與 nplus.wiki 及 note 站無關；不需要「資料頁」規範）。
- **照書改的**：#4 slug 改 `youtube-algorithm-and-retention`（全書沒提 Shorts，書單 note 同步修正）；#15 標題改「羅馬以外的羅馬」（書沒寫達爾馬提亞／斯普利特）；#16 改「三教共處的西班牙」（摩洛哥只是背景）；#2 標題「織夢」改書的「築夢」。
- **驗證**：兩站 entity／anchor／死鏈／區塊閉合 0，回向邊補 89 條；抽 10 頁 30 個具名詞全部在原書；俄羅斯頁起稿者未重讀的兩句（紅色錫鈴、舍伍德的博物館）已逐句回源。checkup 全星系 blocker 0／warn 0。
- 下一步：兩站 `/note-guide`（Fable；現在夠厚了）。

**Batch 3 — Opus**：照 Batch 2 的單起草；兩站導覽對帳前置（重算頁數本數）。（Batch 3 起草順序：#1–#6 工作線 → #7–#17 第一級區域 → #25–#27 hr → #18–#23 第二級；#24 等裁決）
**收書輪（2026-09-26 傍晚，Fable 主會話＋Opus 起草）**：Andrew 一口氣建了 8 個書站（hr 7 本全到——Compensation 收的是 Yap 等人的加拿大第六版；加勞動部的勞基法與工作規則手冊，判脊梁），How to Be a Travel Writer 也有內文了。做掉：hr 書單 20 本全收；新開第六分類「HR 的角色與策略」＋主題卡；7 頁起草（hr 6：評分者效應、回饋怎麼收、心理安全感、薪酬結構、勞基法底線、從外而內的人資；travel 1：旅遊敘事的工藝）；兩站導覽增量改寫（未收／骨架句子全清）、overview 同步；travel 40 頁、hr 21 頁；tier-audit 兩站全 0（travel 真欠債歸零）；checkup 全星系 warn 0。剩：hr 的 organization-over-individual 節點等 Victory 開第二頁（support，不急）。
**模型分工的交接說明**：例行輪（建好書→回填→起草→上線）預設 Opus；只有判層、選題開單、寫或改導覽才切 Fable。

**Batch 4 — Fable（2026-09-26 收工）**：兩站導覽各五章（The Field／Themes／Books／Debates／Reading）落盤上線——travel 約 9,900 字、hr 約 8,600 字；每章 anchor 逐一驗過、概念頁連結全通（39＋15 頁每頁都被導覽連到）、章際錨點通；tier-audit 兩站空頭支票 0／漏接 0／未判層 0（travel 真欠債 1＝Don George 那本書站還是骨架）；checkup 全星系 blocker 0／warn 0。順手修：hr 的 HBR 招募指南 delegatedTo 從 leadership（那站判 tool）改 hbr（那站判 spine）。導覽裡的判讀只採站上已表態的頁；沒表態的爭點（Meyer 慷慨 vs Guidara 95/5、Murch 拍剪分離 vs Bowen 為剪而拍、Abbey vs 遊覽車團、Google 委員會 vs Netflix 留任測試誰對）標「還開著」。；data-science 等書進站再判。
**Andrew**：hr 7 本待收（Nine Lies、Thanks for the Feedback、Fearless Organization、Compensation、Ulrich ×2、Dessler）＋挑一本台灣勞基法；data-science 39 本。


### 深度與連結度地板：Fable 收尾，**56→0，三條地板全星系歸零**（2026-09-03 深夜）

**covey 37 筆**：讀完五章才發現問題比數字小——導覽本來就逐頁點名了全部 41 頁，只是用「」寫標題、沒掛連結。
所以做的是把 64 處引號標題換成連結（04 章只換兩處，「雙贏」「第二象限」在那章是口號用法，不連），外加一句過期敘述
（05 章說家庭使命宣言還沒寫，今天 A 類輪已開頁）。**教訓：`guide-unlinked` 抓的是「沒連結」，不等於「沒講到」**——
先看導覽是不是用引號在點名，那種站一個腳本就收完。

**19 筆／8 站**：全部織進去了，沒有一筆是硬塞。分兩種：
- **清單漏一筆（9 筆）**——design 的 Change by Design 十一頁清單補上最後一章、Maeda 判準句補 Law 3；clean-code 的
  命名骨架補兩頁、APoSD「從…一路到」補兩頁、Clean Code 那句補 testing 一頁；agile 的 Succeeding with Agile
  組織面百科補兩頁。這些句子本來就在列該書的頁，補的是完整度。
- **書在架上但導覽沒位置（10 筆）**——每筆都給一個真句子，不是連結：leadership 的 Cloud《Boundaries for Leaders》
  接在 Extreme Ownership 後面（「當責不只是失敗算誰的，還包括你默許了什麼」）；startup 的 Kawasaki 進「矽谷敘事」組，
  兩頁分工（Make Meaning 給起點、Pitch 給第一個動作）；data-systems 的 partitioning 進 NoSQL 造反段（規模靠切開來扛，
  再平衡與請求路由是切開後永遠跟著的兩件事），**「五派疆域」地圖從 11 個分類補成 13 個**（partitioning 歸 NoSQL 殖民地，
  encoding 歸物理定律那排）；system-design 的 DDIA 段補「編碼只落一頁，因為主場在 data-systems」、SDI 段補
  storage-abstractions 的兩個原型；biblical-studies 三本各給位置——Hard Sayings 進方法論（小節改名「三本入門、一本防守、
  一本查閱」）、Hays《Moral Vision》進大部頭（四座→五座）、Watkin 接在主線二尾巴當**反向箭頭**（主線二把聖經放回處境，
  他用聖經讀我們的處境）；agile 的 Clean Agile 段補中環那頁，並明講「這是 Bob 的圈，不是第二章八張卡那個圈」。

**結果**：`galaxy-checkup` 75 站 blocker 0／warn 0／nit 0——含新加的 `guide-unlinked`／`related-thin`／`body-thin`
三條。這輪起「每一頁都從導覽走得到、每一頁至少兩條 related、沒有一頁正文不到一千字」是有工具背書的事實。

### 深度與連結度地板：Opus 那三批已交付，**剩 56 筆留 Fable**（2026-09-03）

**Opus 交付**（14 個代理、34 站、43 個 commit，全部已 push）：`related-thin` 77→**0**、`body-thin` 45→**0**、
`guide-unlinked` 191→**56**。全星系 blocker 0／warn 0／nit 56。

`body-thin` 那 45 頁全部加深到 1400–3800 字，材料一律取自該頁**已掛的 anchor**（不夠用的補同書別章），
具名事實逐筆回源 grep。`related-thin` 那 77 頁全部補到 2–5 條且雙向。

**順帶清掉、不在原單上的**（都是代理回報、主會話逐筆重驗後才改）：
- **導覽數字錯 9 筆**：system-design（concepts 四十七→五十、六十七頁→七十頁）、clean-code（testing 七→八頁、
  註解編排四→五頁）、leadership（九十九→一百本、帶人與團隊二十六→二十七本、未引用二十七→三十一本）、
  data-systems（01 章十九本／五十三頁→二十一本／五十五頁）、liurun（13→14 頁）、
  biblical-studies（BST 六十一頁→四十五頁）、thinking（語言與知覺六→七頁、Haidt「三頁由它撐起」改成
  「三頁講它的主張，其中兩頁直接溯源」）。
  **教訓：代理報回來的數字也要自己重數**——leadership 那筆代理說 103 本，實際 100（它數的是 `status:` 行數）。
- **一句查無出處的引言**：image-style `gentleman-presence` 把「風格是人格的可見呈現」掛給 Flusser，
  實際出自 O'Brien《How to Be a Man》，Flusser 那句「品味的外顯」全書庫 grep 不到。已改歸屬。
- **三處 anchor 掛錯章**：business-strategy 飛輪頁沒掛《從 A 到 A+》第 8 章（飛輪原典章）、
  cloud-infra `load-balancing` 的 label 寫「Frontend / Datacenter」但只掛 Frontend、
  writing `pay-attention` 掛的兩章其實是 `daily-practice` 的材料（頁上的 Yad Vashem、雪松木湯匙出自 15/16/28 章）。
  **這三筆都是 `export-anchor-gaps.py` 的漏網**——它查「數字在不在掛出去的章底下」，查不到「掛的章對不對」。

#### 留給 Fable 的 56 筆（兩堆，性質不同）

**堆一：covey 導覽重寫（37 筆，整站）。** 41 頁只連到 4 頁，五章合計 8 個連結，全星系最少。
分類是 legacy 15、trust-and-execution 8、personal-victory 6、public-victory 5、principles 4、family 3。
這不是補連結——導覽根本沒把頁當材料寫，要重新決定哪一章帶哪幾頁。

**堆二：書單與導覽脫節（19 筆，8 站）。** 每一筆都 grep 驗證過導覽零命中，硬織就要新增段落（規格禁止）。
要決定的是「導覽該不該講這本書／這個主題」，不是連結問題：

| 站 | 頁 | 導覽那邊的狀況 |
| --- | --- | --- |
| leadership | `team/boundaries-for-leaders` | 該書判 **spine**、歸「帶人與團隊」組，但五章導覽 `Henry`／`Cloud`／`Boundaries`／`界線` **全部零命中** |
| startup | `opportunity/pitching` | 03 書單章**根本沒有《The Art of the Start》的條目**；五條主線也沒有「對外溝通／pitch」這條 |
| data-systems | `partitioning/rebalancing`、`request-routing` | 02 章「五派疆域」地圖列 11 個分類，**漏掉的正好是 encoding 與 partitioning**——這兩個分類在導覽層本來就是孤兒 |
| system-design | `communication/data-encoding`、`storage-abstractions/object-storage` | 03 章明寫 DDIA「統治複製、分片、一致性、串流四個分類」，編碼不在這個定位裡；物件儲存／S3 導覽零命中 |
| clean-code | `naming/avoid-encodings`、`parts-of-speech-and-context`、`complexity/design-it-twice`、`different-layer-different-abstraction`、`testing/clean-tests-first-and-aaa` | 前四筆的導覽句**自承是取樣**（「命名八頁的骨架（三項）」「從 A、B、C 一路到 D、E」）；第五筆要改寫「站的前三個分類」那個作用域宣稱 |
| biblical-studies | `biblical-theology/diagonalization`、`hermeneutics/handling-hard-sayings`、`new-testament/nt-ethics-three-focal-images` | 三本書在五章導覽一個字都沒出現；織進去分別要開第六條主線／改「三本入門一本防守」那句／多開一個 bucket |
| agile | `adoption/leading-self-organizing-teams`、`measuring-the-transition`、`xp-practices/team-practices-around-the-code` | 前兩筆「自組織」「敏捷度」零命中；第三筆是 XP 的 Circle of Life 中環，**而 02 章的「中環」是站上自己的重新分層（Scrum／看板／回顧），名字撞上但不同義，不能借用** |
| design | `design-thinking/design-thinking-practices`、`simplicity/time-feels-like-simplicity` | 前者是 Change by Design 最後一章，03 章列了該書十一頁主題**剛好只漏這一項**；後者是 Maeda Law 3，導覽提了 Law 1/5/6/7/9/10 就是沒有 3 |

**判準建議**：這 19 筆分兩種——「導覽的清單漏了一筆」（design 那兩筆、clean-code 的取樣句）補回去即可；
「書在架上但導覽沒有它的位置」（leadership、startup、data-systems、system-design、biblical-studies）
要先決定分層敘事要不要收它，再決定寫不寫。

### 深度與連結度地板（2026-09-03 開單）——**313 筆 nit、三種，模型分兩堆**

**起因**：Andrew 問「各站的深度和連結度都夠了嗎」。契約層（脊梁有頁、anchor 實存、related 雙向、
roadmap／mastery 100%、導覽數字對得上）全綠，但「夠」在三個維度從來沒定義過。量出來不均，
於是把三條地板寫進 `galaxy-checkup.py` §2.8（都是 nit）：`guide-unlinked`／`related-thin`／`body-thin`。
逐頁清單不抄在這裡——`galaxy-checkup.py --json` 隨時重算。

| 規則 | 筆數 | 站 | 集中在哪 |
| --- | ---: | ---: | --- |
| `guide-unlinked` 頁沒被任何導覽章連到 | 191 | 19 | covey 37/41、biblical-studies 37（舊約 23、新約 12）、clean-code 34（refactoring-moves 10、code-smells 6）、agile 20、design-patterns 10、thinking 9、system-design 9、economics 8、design 8，其餘 10 站 ≤4 |
| `related-thin` related < 2 條 | 77 | 21 | growth 33（六個分類平均分布、20 頁是空的）、leadership 10，其餘 ≤4 |
| `body-thin` 正文去空白 < 1000 字 | 45 | 9 | system-design 15、writing 11、clean-code 6、leadership 4、image-style 3、cloud-infra 3；**45 頁全部都有 anchor**，材料在書裡 |

**模型分流**：

- **Opus（三批，可平行）**
  1. `related-thin` 77 頁：讀該頁引言＋同分類姊妹頁，補到 2–4 條並雙向指回；growth 33 頁一站一次做完。機械活，checkup 驗雙向。
  2. `body-thin` 45 頁：**加深不重寫**——保留既有區塊，讀 anchor 指到的章把具名事實補進去，目標 ≥1500 字；
     技術站照該站 directive 族（intuition／tradeoffs、whentouse／structure／antipatterns）。每個具名事實回源 grep。
  3. `guide-unlinked` 的**織入既有段落**那一半（18 站、154 頁，covey 除外）：規則是「導覽 03／05 已在講這本書或這個主題的那一段，把頁面連結補進既有句子」——
     biblical-studies 逐卷頁對 03 章逐卷段落是 1:1；clean-code 的 refactoring-moves／code-smells 是型錄頁，在 Fowler《重構》那段列一句型錄清單即可。
     **導覽完全沒講到的頁不要硬塞**，留單給 Fable。改到的章推 `writtenAt`。
- **Fable（兩件）**
  1. **covey 導覽重寫連結層**：五章合計只有 8 個連結、41 頁連到 4 頁，全星系最少——這不是補連結，是導覽沒把頁當材料寫。要重寫哪一章帶哪幾頁（legacy 15 頁尤其）。
  2. Opus 織入輪留下的殘單：導覽沒講到的頁，決定是織進去還是導覽本來就不該講它。

**不做的**：正文零內鏈（約三分之一的頁）不立規則——related 與 takeaways 延伸行已在承擔，體裁差異大；
頁／脊梁 < 1 的四站（management 0.75、theology 0.79、problem-solving 0.83、wellness 0.84）是寬而淺，
但每本脊梁都有頁，屬 C 類厚書第二頁的範圍，維持第六輪「紅利已盡」的判定。

### B 類開單（2026-09-03，Fable）——**193 本零引用 support 逐本裁決：開 20 頁、補 16 條 anchor、其餘 157 本維持 support**（**單已全部執行完畢，見下一節**）

**判準**（沿 MODEL-ROUTING：面向覆蓋非頁厚）：導覽第三章對每本 support 都已寫了理由（一句帶到／主張已含於某頁／退居譜系／人證／查閱型／續作／年度更新／合著對談／入門改寫／導讀非原典）。
**只有「這本書帶著站上還沒有的面向」才翻案**；同一研究傳統的側翼、正典的通俗版、讀者見證、機構彙編一律不開。
每筆都對過既有頁的分類與 core，撞題的不開。**開頁後把該書 tier 由 support 升 spine**（lewis《裸顏》前例）。

**起草規格（給 Opus，每頁一個代理直接寫檔）**：先讀「避開」欄那幾頁的 core 全文再動筆；anchor 只掛「落點」欄列的章，實檔驗證；
具名事實逐筆回源 grep；雙向 related；更新 `_index.md` roadmap＋mastery；導覽 03 該書那段改成已開頁並連結；overview 頁數／頁書比同步；
蓋 `enrichedAt`、五章 `writtenAt`、overview `writtenAt`；format → lint → build:nosearch → `galaxy-checkup.py` 0／0／0 → commit → `pull --rebase` → `format:check` → push。

#### 開頁（20 筆）

| # | 站 | 書 | 頁題（暫定） | 切什麼 | 避開既有頁 | anchor 落點（章目錄） | 落分類 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | writing | war-of-art | 抗拒與轉職業 | Pressfield 把創作阻力命名為「抗拒」的那套敵人學，加上第二部「轉職業」——業餘與職業的差別不在才華在態度 | writers-block（只引 Lamott 的完美主義）、daily-practice、revision | 01-resistance-defining-the-enemy、02-combating-resistance-turning-pro | craft-mindset |
| 2 | writing | into-the-woods（＋save-the-cat 當第二 anchor） | 五幕論：McKee 與 Truby 之外的第三條路 | Yorke 把各家結構理論收攏成五幕（home→woodland→forest→road back→home changed）的地圖，Snyder 十五拍當它批評的對象 | story-shape（McKee 三幕）、monomyth（Campbell）、scene-turns | into-the-woods 01–05；save-the-cat 主章 | story-structure |
| 3 | writing | writing-tools | 句子層的工具箱：Clark 的五十五個工具 | 新聞寫作圈的標準讀物，取「Nuts and Bolts」那一部：主詞動詞靠近、強字放句尾、副詞刪法——句子層而非段落層 | style-clarity 既有頁（Williams 的工程、Strunk 的規則、Pinker 的知識詛咒）——這頁只做句子內部的機械 | 第一部工具 1–10 擇要 | style-clarity |
| 4 | relationships | games-people-play | 心理遊戲：人間遊戲的結構與六種常見劇本 | Berne 的 TA 原典：遊戲＝一連串帶隱藏動機的互補交流，以「報償」收場；三個結構層（分析、詞典擇例、超越遊戲） | people-without-conscience、illuminator-vs-diminisher、listen-to-understand | 01-analysis-of-games、02-a-thesaurus-of-games（擇 Why Don't You—Yes But、Now I've Got You、If It Weren't for You）、03-beyond-games | boundaries |
| 5 | tools | hyperfocus（＋productivity-project 第二本） | Bailey：極度專注與發散專注 | 導覽自承「唯一不放心的一筆」：Bailey 是學派卡上唯一沒頁的人。切 hyperfocus／scatterfocus 兩種模式的切換，productivity-project 只取時間×注意力×精力三角一段 | deep-work-value、internal-triggers-indistractable、slow-productivity（那頁已借「注意力空間」）、lead-through-noise | hyperfocus 01-hyperfocus、02-scatterfocus；productivity-project 三角那章 | focus-attention |
| 6 | data-systems | data-warehouse-toolkit | 維度建模：事實表、維度表與星型結構 | Kimball 的維度建模入門：事實／維度、粒度宣告、緩慢變化維度——站上分析型建模完全缺席 | column-oriented-storage（提過 star schema 一句）、relational-vs-document、query-languages | 01-dimensional-modeling-primer、02-retail-sales | data-models |
| 7 | data-systems | readings-in-database-systems | 弱隔離：Red Book 的一手證詞 | 導覽第四章明說「弱隔離那章是爭點還缺的證詞」：Bailis 等人對真實資料庫預設隔離級別的整理，一手論文的聲音 | transactions 分類既有頁（先讀清單，別重講 ACID 定義） | 06-weak-isolation-and-distribution、03-techniques-everyone-should-know | transactions |
| 8 | cloud-infra | seeking-sre | 控制還是信任：Google 之外的 SRE | 導覽第二章點名「五張卡之外沒有卡的張力」：多數 SRE 實踐圍繞控制（預算燒光就凍結），本書開場對照信任取向；取實作群像＋人的那一面 | error-budget、sli-slo-sla、handling-overload | 01-sre-implementation、04-the-human-side-of-sre | slos-error-budgets |
| 9 | communication | smart-brevity | 精簡寫作：書面短溝通的四個動作 | 導覽自承「書面短溝通在這個書架上的唯一代表」：Axios 式的 muscular tease、一句話要點、why it matters、go deeper——口語簡報之外的另一半 | presentation 分類全是口語（18-minute-focus、talk-like-ted）；writing 站的 find-the-core 已借過它，本頁掛回原典並以書面訊息為主 | 01-what-is-smart-brevity、02-how-to-do-it | presentation |
| 10 | drucker | concept-of-the-corporation | 企業作為社會制度：通用汽車十八個月 | 「管理」成為研究對象的第一現場：分權、企業作為人的努力與社會制度、大型企業的正當性——這是站上 Claims「每個發明的第一現場」缺的那一個 | end-of-economic-man（1939 提問）、managements-new-paradigms（分權一句）、what-is-a-business | 02-corporation-as-human-effort、03-corporation-as-social-institution | society |
| 11 | marketing | obviously-awesome | 定位的十步驟：從競爭替代品開始 | Dunford 的操作法：先列競爭替代品→獨特屬性→價值→最在乎的客群→市場類別——Ries & Trout 給世界觀，這頁給工作表 | own-a-word、reposition-the-competition、smallest-viable-market、law-of-leadership | 01-what-is-positioning、02-the-10-step-positioning-process | positioning |
| 12 | clean-code | balancing-coupling | 耦合的三個維度：整合強度、距離與波動 | Khononov 的模型：耦合＝整合強度×距離×波動，三者的平衡決定模組邊界——導覽稱這群「全站最大的縱深」 | complexity 分類的 deep-modules、better-together-or-better-apart、nature-of-complexity；**別越界到服務層**（system-design 的 coupling-and-cohesion 引的是 Newman 與 Hard Parts） | 01-coupling-fundamentals、02-integration-strength、03-distance-and-volatility | complexity |
| 13 | design-patterns | game-programming-patterns | GoF 在遊戲裡：重訪六個模式 | Nystrom 用遊戲場景重訪 Command、Flyweight、Observer、Prototype、Singleton、State，加 Game Loop——與 gof-in-functional 同構的第二次典範檢驗 | gof-in-functional（結構平行可以，內容不能重講）、oop-vs-functional | 02-design-patterns-revisited、03-sequencing-patterns（game loop） | paradigms |
| 14 | navarro | three-minutes-to-doomsday | 拉姆齊案：方法論在高壓現場 | 導覽自列「已收待挖」：Rod Ramsay 間諜案偵訊實錄，舒適／不適判準與基準線在真實高壓下怎麼用、哪裡失靈 | psychological-comfort、self-mastery、baseline-first、comfort-not-deception（這些是方法，本頁是實錄） | 01-subject-ramsay-was-naked、03-tired-and-wired、04-clarifications-and-evasions、12-this-changes-everything | exceptional |
| 15 | agile | impact-mapping | 影響地圖：為什麼、誰、怎麼、什麼 | Adzic 的四層地圖把商業目標接到交付項——導覽第五章已排進路徑、書單說它補使用者故事「為誰、為什麼」那段 | product-vision-and-mmp、product-owner-and-customers、kanban-planning-and-estimating（借過一句） | 02-what-is-an-impact-map、04-creating-an-impact-map | product |
| 16 | investing | against-the-gods | 風險的觀念史：從骰子到效率前緣 | Bernstein 的風險觀念史：Pascal–Fermat、Bernoulli 效用、Galton 回歸、Markowitz——站上 market-history 講泡沫，沒講「風險」這個概念怎麼被發明 | luck-risk-and-survival、process-over-outcome、loss-aversion-and-prospect（**本書末段講展望理論，到此為止不要重講**） | 01-beginnings、03-measurement-unlimited、05-degrees-of-belief | market-history |
| 17 | economics | blind-robbery | 坎蒂隆效應：新錢先到誰手上 | 導覽自列「本群最該先挖」：奧地利學派的機制段——新錢的分配順序決定誰得利誰受害 | hidden-cost-inflation（那頁講課稅面與德國 1923，本頁只講分配順序）、central-bank-privilege、what-is-money | 02-who-can-create-money、03-current-money-creates-injustice、05-state-exploits-with-inflation | money-central-banks |
| 18 | system-design | api-design-patterns | 資源導向 API：標準方法與集合操作 | Geewax 的模式目錄：資源導向設計、五種標準方法、集合操作（批次、分頁、過濾）——導覽稱它 Designing Web APIs 的工程化續篇 | api-design（版本與 Designing Web APIs）、rest-grpc-graphql | 03-fundamentals、04-resource-relationships、05-collective-operations | communication |
| 19 | economics | worldly-philosophers | 俗世哲學家：經濟思想史怎麼說故事 | Heilbroner 的思想史體——站上 econ-foundations 講概念不講人；取 Smith、Marx、Keynes、Schumpeter 四章的敘事法 | creative-destruction（熊彼得已在，本頁只帶一句）、econ-foundations 既有頁 | Smith、Keynes、Schumpeter 三章 | econ-foundations |
| 20 | newport | how-to-become-a-straight-a-student | 偽工作：深度工作的少年期（**可選，優先序最低**） | 「偽工作」概念的起點，三部曲裡唯一有方法的一本；站只有 10 頁，這頁補人物弧線的起點 | deep-work 分類既有頁、three-principles-of-slow-productivity（提過 pseudo） | 偽工作那一部 | deep-work |

#### 補 anchor（16 筆，不開頁，Opus 直接做）——導覽已寫明落點

- **investing**（9）：intelligent-asset-allocator→asset-allocation-and-rebalancing；pioneering-portfolio-management→asset-allocation-and-rebalancing（機構視角段）；wealth-of-common-sense→stay-the-course；beating-the-street→lynch-stock-categories；100-baggers→scuttlebutt-and-quality-growth；devil-take-the-hindmost→madness-of-crowds；liars-poker、too-big-to-fail→subprime-and-moral-hazard；man-who-solved-the-market→efficient-market-and-random-walk。每筆掛 anchor 時要在該頁補一段（不是只掛連結），並在 03 章把「已收待挖」改成已引。
- **economics**（3）：freakonomics→incentives-and-prices（實證段）；undercover-economist→opportunity-cost-scarcity；exile-on-wall-street→financial-history 的 2008 頁事後段。
- **writing**（3，借聲未掛錨）：if-you-want-to-write→daily-practice／seeking-feedback；storynomics→story-as-persuasion；ogilvy-on-advertising→lead-with-benefit。
- **drucker**（1）：drucker-on-asia→導覽第四章對帳段（已是那章材料，掛回即可）。

#### 維持 support、不開（157 本）——理由已在各站導覽 03 章，這裡只記類型

同一研究傳統的側翼（Talent Code、Colvin、Coyle）、正典的通俗版或入門改寫（富爸爸系列衍生七本、Learning How to Learn、Head First）、
讀者見證與人證（Quit Like a Millionaire、Last Lecture、When Breath）、查閱型（Carson 導論、Nemeth 百科、麥肯錫筆記術）、
續作與年度更新（峰值體驗 2、進化的力量 2、Unicorn Project）、合著對談與格言集（與川普合著、Entrepreneur Mind、Excellent Advice）、
導讀非原典（哲學的 40 堂、蘇菲的世界——**真正的缺是 Kant／Hume 原典，屬收書不屬開頁**）、機構彙編（HBR 兩本 Guide、人生學校）、
時代切片（互聯網+、就業的終結）、體裁史（Wealthy Barber、Scientific Advertising）、姊妹站主場（Team Topologies→agile、Obstacle→philosophy）。
**特別記三筆不開的理由**：Factfulness（thinking 導覽明文「刻意不開頁但不從導覽消失」）；Waltke 舊約神學 39 章（創世記讀法已入頁，其餘是逐卷註釋層，屬 biblical-studies 的 BST 同型工作，要開就是系列不是單頁）；Understanding Distributed Systems（兩站都判「緩坡入門」，開頁只會重講 DDIA）。

### B 類執行輪（2026-09-03，Opus）——**20 頁全數交付，15 站，全星系維持 0／0／0**

上面那張單一次做完。分工是每站一個代理端到端（讀避開頁與原書 → 寫頁 → 雙向 related → 分類 `_index.md` → 升 spine → 導覽 → overview → format/lint/build/checkup → commit → rebase → format:check → push）。

| 站 | 產出 |
| --- | --- |
| writing | 抗拒與轉職業；五幕論：去程與返程；句子層的工具箱（四本升脊梁，含 save-the-cat） |
| relationships | 心理遊戲：人間遊戲的結構與三個經典劇本 |
| tools | 注意力空間：極度專注與散發專注 |
| data-systems | 維度建模：事實表、維度表與星型結構；弱隔離：Red Book 的一手證詞 |
| cloud-infra | 控制還是信任：Google 之外的 SRE |
| communication | 精簡寫作：二十六秒裡的四個動作 |
| drucker | 企業作為社會制度：通用汽車的十八個月 |
| marketing | 定位的十步驟：從競爭替代品開始 |
| clean-code | 耦合的三個維度：整合強度、距離與波動 |
| design-patterns | GoF 在遊戲裡：重訪六個模式 |
| navarro | 拉姆齊案：方法論在高壓現場 |
| agile | 影響地圖：為什麼、誰、怎麼、什麼 |
| investing | 風險的觀念史：從骰子到效率前緣 |
| economics | 坎蒂隆效應：新錢先到誰手上；俗世哲學家：經濟思想史怎麼說故事 |
| system-design | 資源導向 API：標準方法與集合操作 |
| newport | 偽工作：深度工作的少年期 |

16 條 anchor 同輪補完（investing 9、economics 3、writing 3、drucker 1），每筆都在該頁補一段而非只掛連結。

**四條跨站教訓**：

1. **區塊 directive 是分站族的，起草規格不能寫死。** `notes-core/src/plugins/remark-sections.mjs` 把 directive 分成三族：一般站 `core／case／takeaways`、技術站 `intuition／tradeoffs` 或 `whentouse／structure／antipatterns`、clean-code 的 `whymatters／whyproblem／refactor`。這輪發出的規格把 `::core / ## ⚖️ / ## 🖼️` 寫成「照抄這個順序」，結果 cloud-infra 與 design-patterns 各長出一頁全站唯一的 `::core`（design-patterns 連它的結構雙胞胎 gof-in-functional 都用 `whentouse`）。兩頁事後改回站台慣例，design-patterns 那頁補寫 `::antipatterns`。**下次規格要寫「照該站既有頁的 directive 族」，不要給字面骨架。**
2. **導覽與 overview 裡寫死的頁數／本數會靜靜過期，而且是跨輪累積的。** 這輪至少四站在動手時就已經是錯帳：navarro 導覽寫 25 頁（實際 26）、data-systems 寫十九本（`1758777` 之後已 21）、investing 章首寫 40 本已挖（實際 50）、cloud-infra 寫「其餘十本一條都沒有」（實際 13）。代理多半只被要求改第三章，但同一頁其他章寫著同一組數字，改一半就自相矛盾——**開頁時要把五章與 overview 的規模數字一起重算，用程式數不要沿用**。investing 留下的兩個小節標題（指數與被動、成長與選股）已另行核算後修正為 11/12 與 7/7。
3. **開單的事實前提本身可能錯。** #2 的單寫「Snyder 的十五拍當 Yorke 批評的對象」，grep 全書後發現 Yorke 唯一提到 Snyder 的地方是附錄七的對照表，而且結論是正面的（「所有大師都在試圖表述同一件事」）；真正挨刀的是佛格勒與考夫曼。頁與導覽都改成「同一張圖的地圖版 vs 施工圖版」。**開單時的角度是假說，起草者要有推翻它的權限。**
4. **落點會偏離預測，而偏離要記帳。** #7 原本規劃「補進既有 isolation 頁」，實際 Bailis 那章是**預設值的普查**不是定義，塞進機制頁會兩邊都稀釋，於是獨立成頁；#17、#19 同樣從「補進既有頁」改成獨立開頁。data-systems 的導覽把這記成「第五次連續落點偏離預測」——這個模式本身值得在下一次開單時當成預設。

### A 類排程執行輪（2026-09-03 起，Opus）——**22 筆已交付並 push，全星系 checkup 維持 0／0／0**

**起因**：Andrew 問「導覽裡寫的排程做完了嗎」。盤點後的關鍵事實：**契約上沒有欠債**——tier-audit 真欠債 0、空頭支票 0；
資料算出的 198 本「未挖」**全部是 support 層**，而 support 的定義就是「導覽一句帶到即可，不欠概念頁」。
所以排程不是欠債是機會，依「選題已由導覽做完」的程度分三類：**A（書與章節都點名，約 25 筆）／B（書點名、章節要選，約 60）／C（厚書第二頁，約 110）**。
Andrew 裁決先做 A，B 與 C 要一次開單（開單留 Fable，起草給 Opus）。

**已交付（每筆都逐章讀原書、避開既有頁角度、掛 anchor、雙向 related、更新導覽與 overview、蓋 enrichedAt 與 writtenAt、build＋checkup 後才 push）**：

| 站 | 產出 |
| --- | --- |
| lewis | 裸顏：佔有如何冒充愛（並升 spine） |
| kent-beck | xUnit 自舉；狀態與集合 |
| covey | 家庭使命宣言 |
| grant | 把異見寫進制度 |
| fromm | 釋夢的藝術：白馬上的拿破崙 |
| fowler | 整合應用：一張決策順序表；數量與觀測 |
| navarro | 頭部細部 |
| schwager | 機械系統 |
| templar | 難搞的人 |
| uncle-bob | 設計模式不是 OO 的補丁 |
| damodaran | 為什麼有三種取徑 |
| de-botton | 愛作為服務 |
| drucker | **不是新頁**：補《談自我管理》第 2–4 章 anchor |
| wan-weigang | 成功學的解藥 |
| liurun | 思考的底層邏輯 |
| wellness | 發展性創傷 |
| security | 把威脅建模帶進組織；人因與儀式 |
| hbr | 藍海策略（學派卡的 Kim 終於有頁） |
| design | 文字、影像與收尾 |

**三個把單縮小而非照做的判斷**（都改寫進導覽）：
1. **drucker 那筆是溯源債不是內容債**——導覽說第 2–4 章沒開，打開既有頁卻發現艾森豪、鏡子測試都寫在裡面，只是沒掛 anchor。多寫一頁只會製造重複。
2. **fromm 的希特勒個案挖不了**——《人類破壞性的剖析》repo 只有三章加跋，沒有那一章。書端缺料，導覽已改成只留成立的兩筆。
3. **navarro 的髖臀章、schwager 的基本面章刻意不開**——前者書裡自己標低頻，後者早被既有頁掛過 anchor，真正沒動的是交易系統那一部。

**A 類剩下的**：philosophy 的《哲學的 40 堂公開課》（一章一頁不可行，要重新開單）、writing 三本借聲未掛錨（anchor 級）、
clean-code 的設計與演化四本、theology 的十八本架上參考、system-design 的 Understanding Distributed Systems——**這幾筆的性質其實已落到 B 類**，
需要開單才動。


## 文案精簡輪（2026-09-03，Andrew 指示）——**三批做完，75 站全數 commit＋push**

**原則**（Andrew 給的，以 learning-note 為樣本）：首頁簡述與五章導覽都要精簡，把**內部記帳語彙**
從讀者看得到的地方拿掉——「認領上架」「尚未開頁」「零寫作義務」「帳在文末」「tool 層」這類詞是
產線的話，不是讀者的話。

**Opus 那半（已提交）**：
- 首頁 `heroLede`：刪與 tagline 重複的開頭（13 站）、刪「每頁含「討論區」與「總整理」。」（48 站）。
- 導覽 01：刪「收完這 N 本（…）、寫完站上 N 頁之後，我們的判讀是：」整句（17 站）；句中型只刪時間句、
  保留判讀語（31 站）；刪「（其中 N 本是認領上架的參考書，尚未開頁）」括號（18 站）。
- 導覽 02：刪「讀完 N 頁，浮出來的是三場對話」模板（10 站）＋ learning 專屬兩句。
- 導覽 03：標題「架上參考（N本）：認領輪上架，尚未開頁」→「架上參考（N本）」（21 站）；段首
  「2026-08-28 的孤兒書認領輪…一律以 tool 層上架——列進盤點即可，零寫作義務：」→「這幾本在架上、還沒開頁：」
  （23 站，保留「聖經研究是書庫裡最厚的一疊」這類讀者向插話）；「另 N 本是認領上架的參考書（帳在文末）」
  →「另 N 本在架上還沒開頁」（14 站）；刪「認領輪先以 tool 上架、開頁後才升 spine。」（10 站＋1 站改寫）；
  刪所有「（帳在文末）」「（tool 層，…文末）」。
- 章末**純導覽句**（每個分句都只是「見第 N 章」）逐句刪：01×36、02×41、03×8、04×41、05×30 站。
- `overview.ts`：刪「（N 本是認領上架的參考書）」括號（19 站）、learning 的「三聲道…是缺口」段、
  biblical-studies／career／relationships 的「書架的口音誠實標明…」句、security 與 philosophy 的認領句。

**Fable 那半（已提交）**，三條原則：
1. **分層帳留、換讀者語言**：書架頁本來就把 tier 秀給讀者（`TIER_META`：脊梁／支架／工具書／姊妹站），所以
   總覽 Verdict 與 03 的分層帳不是刪，是把 `owned／spine／support／tool／delegated／skipped／unavailable` 全換成
   中文標籤，「帳攤開：N 本 owned 判下來…」改成「N 本書分層：…」，百分比改成「近四成／三分之一」這種話。
2. **「架上參考」節留**：段首句已是讀者向，刪掉的是對帳句（「上面各組的本數不含這 N 本」）與流程句
   （「tool 層不會被任何盤點工具推上檯面，哪本值得升層要有人回頭看」「升層輪已裁決維持 tool、理由記檔免重審」）
   ——改成「哪本值得先開頁：…」「X 決定不開頁：理由…」。
3. **章末融合句留內容、去指路**：67 句逐句改（bogle「成本、結構、足夠」那類保留，改成「接下來要攤開的」；
   純指路的「N 組的帳攤完了，先讀哪本見閱讀路徑」整句刪）。**正文中段的交叉引用一律不動**——
   「攻防歸第四章」「這筆帳歸第四章」是內容組織，不是導覽噪音。
4. 順手清掉 03 正文裡的 changelog 時間戳（「2026-08-24 開挖兩章」→「後來開挖兩章」、「已於 2026-08-21 開口」→「已開口」，
   約 190 處），與「這一輪／上一輪」保留（那是敘事）。
**一個踩過又修回的坑**：我一度把「每個分句都帶章節連結、前綴 ≤20 字」的刪句規則跑到正文全篇，吃掉 112 句——
其中至少十幾句是內容（bogle「後三本書的作者是一個每天吃抗排斥藥的人」、lewis「它是主線一的第三根柱子」、
personal-finance「兩派其實在處理同一個敵人的兩端」）。已從 HEAD 逐句還原 111 句（唯一沒還的是 personal-finance 03
一段純指路）。**教訓：這條規則只能跑章末段落，正文裡的連結是內容的一部分。**
另一個坑：「標題後直接接標題就是空節」的清理規則把 `##` 後面接 `###` 的正常結構也當成空節刪了（damodaran、wan-weigang
共 6 個標題），已還原——判空節要看「到下一個同級或更高級標題之間有沒有內文」。

**驗證**：prettier 全綠；learning／theology／career／biblical-studies／system-design／uncle-bob／data-systems／
personal-finance／fowler／wujun／bogle／lewis／pastoral／damodaran／wan-weigang 十五站 build 綠。
**第三批：稽核黑話與產線排程（2026-09-03 Opus，53＋7 站已 push）**——Andrew 問「導覽裡還有沒有待辦事項語氣」，
掃出三層，前兩層去掉、第三層留下：
- **去（稽核黑話 32 句）**：`欠債／溯源債／空頭支票／排隊名單／排隊順序／判過層／真欠債零／豁免`
  → 改成讀者的話（「沒有一本是收了卻沒寫的」「還沒寫到的地方」「決定不挖」「架上沒有還在等的書」）。
  **`豁免` 要逐句分**：tier 意義的 27 處改掉，內容意義的 8 處留（christensen 的「自我豁免」、leadership 的「被才華豁免」、
  templar 的「連他自己的規則也不豁免」）。
- **去（產線排程 84＋25 句）**：`優先序（產線排序那種）／之後深挖的事，不是導覽的事／最現成的材料／該挖而未挖／
  挖掘順序／挖礦圖／火力（指未來工作分配那種）／導覽的債` → 「還有第二頁的空間」「還沒寫到的地方」「礦脈圖」「最該補的地方」。
  **`優先序` 與 `火力` 都是雙義詞**：security 的「按對手排優先序」、tools 的 ABCDE、life-meaning 的「用死亡逼出優先序」、
  image-style 的預算順序全是內容，留；philosophy／taleb／learning 的「火力」是修辭，留。
- **留（缺口陳述 536 處、72 站）**：「十二本已挖、六本還在架上」「兩本收不到，誠實列缺」「書架缺口」——
  **這是導覽的設計本身**（03 章就是逐本說已寫沒寫、04 章固定有「書架缺口」節），拿掉等於改版不是精簡。
  同理保留：`承重／記帳／帳單／分層帳／兌現／結案`——那是導覽的語氣，不是待辦。

**收尾（Andrew 裁決「都做」）**：`searchLede` 的「（描述、核心觀念、討論區、總整理）」括號刪掉（56 站）；
「本輪／這一輪／上一輪／下一輪／那一輪」改成「這次／先前／接下來／後來」，「深化輪」→「之後深挖」、「enrich」→「深挖」、
「火力序」→「優先序」、「火力分配」→「分層表」、「盤點表」→「書單」、「批次一到七」→「逐卷」（約 300 處）；
「一輪／兩輪育兒／第二輪讀物」這種內容用法保留。全部 lint＋build 綠後逐站 commit → `pull --rebase` → `format:check` → push，
**75 站全數推上**（commit 訊息 `docs: trim the ledger and process wording from the homepage and guides`）。

~~**留給 Fable 的（帳與判斷黏在同一句，刪數字就要重寫）**~~（已做完，原清單留作對照）：
1. **overview 的 Verdict 帳句**（34 站）：都以「帳攤開：N 本 owned 判下來 a spine、b support…」開頭，
   後半才是判斷。另 7 站是別種寫法（clean-code、damodaran、investing、system-design、thinking、tracy、writing）。
2. **導覽 03 的分層帳／總帳句**（43 站）：「先把帳攤開：N 本 owned 裡，M 本已被挖進概念頁…」。
3. **導覽 03「架上參考」整節的去留**（21 站）：段首句已改成讀者向，剩下的是這批書的形狀判讀——留不留是策展決定。
4. **章末融合型導覽句**（58 站）：句首有實質內容、句尾才轉成「見第 N 章」，例如 bogle 01 的
   「這份生平裡反覆出現的三樣東西——成本、結構、足夠——就是下一章要攤開的三條主線；…留給第三章。」
   逐句判：內容要留、指路要刪，得重寫接縫。**偵測法**：章末段落裡，所有「；」分句都含 `](#0` 的句子，
   其中第一個連結前的文字 >20 字者即是（≤20 字的已由 Opus 刪掉）。
5. 零星幾句：theology 03「認領輪之後，從新上架的書裡挑了三本開頁升脊梁」、security 03「未挖的那一本是
   認領輪新上架的」、behaviour-interview 03「書架現在只剩三種書…」、personal-finance 03「兩種豁免不該混算」
   那段（**這段是刻意的誠實記帳，刪之前要想清楚**）、philosophy 03「剩下的七本待挖…出處依然是轉述者」。

**驗證**：改完逐站 `npm run format` → `npm run build:nosearch`（本輪 learning／theology／career 三站已驗綠）。
**尚未決定**：搜尋框的 `searchLede` 仍寫「（描述、核心觀念、討論區、總整理）」，要不要一起精簡沒問過 Andrew。

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
