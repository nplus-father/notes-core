# 導覽數字與現況不符

> **生成於 2026-10-27T11:36:05+08:00**｜由 `tools/export-guide-drift.py` 產生，**不要手改**——改資料源再重跑。

由 `tools/export-guide-drift.py` 產生。判準：導覽（`guide/*.md`）與首頁總覽（`overview.ts`）裡**指向站台自身規模的數字**——總頁數、某分類幾頁、收了幾本——回去數實際檔案對不對得上。

**為什麼另立一支**：`tier-audit.py` 的「導覽落後」欄只比日期（`enrichedAt` vs `writtenAt`），抓的是「內容補過、策展層還沒回頭看」；但站台長大時**日期可以完全不動而內容照樣說謊**。2026-08-27 收《飛輪效應》那輪就是這樣被手動抓到的。

**判法（2026-09-03 起）**：每個數字逐一試過所有合法讀法——整站總數、句內／段內列舉的連結數、句內／段內點名的書被引頁數（含聯集）、段內連結所在分類的頁數（含加總）——**沒有任何讀法成立的才報**。這取代了先前靠句型分「強／弱訊號」的做法（句型分不完，2026-09-03 那輪從弱訊號裡人工撈出 22 筆真債）。

- **要改：0 筆**——沒有任何讀法能解釋這個數字。
- 低信心通過：0 筆——只靠「等於某本未點名的書的被引頁數」放行，抽查用。
- 通過：91 筆——具體讀法成立，理由列在表裡。

計數口徑同時接受「只算概念頁」與「概念頁＋題型頁」兩種。

## 要改：0 筆

無——導覽的規模數字都對得上現況。

## 低信心通過：0 筆

無。

## 通過：91 筆

<details><summary>展開</summary>

| 站 | 檔 | 宣稱的是 | 導覽說 | 實際 | 判定理由 | 上下文 |
| --- | --- | --- | ---: | ---: | --- | --- |
| `agile-note` | 02-threads-and-methods.md | 站台總頁 | **67** | 67 | 整站總數 | …是另一張的組織放大版。 > 以下把八張卡連成四組對話。 > 這個分組不在任何一本書裡，是全站六十七頁互相連結之後浮出來的結構。  ## 第一組對話：敏捷宣言 ✕… |
| `agile-note` | 03-canon-guide.md | scrum 分類 | **12** | 12 | 分類頁數 | …Scrum（Kenneth S. Rubin，2012）**。十八處引用，被引最多的書：scrum 分類十二頁裡十頁的骨架、product 分類八頁裡五頁的主要來… |
| `agile-note` | 03-canon-guide.md | product 分類 | **8** | 8 | 分類頁數 | …ubin，2012）**。十八處引用，被引最多的書：scrum 分類十二頁裡十頁的骨架、product 分類八頁裡五頁的主要來源，retrospectives 也有… |
| `agile-note` | 03-canon-guide.md | flow 分類 | **11** | 11 | 分類頁數 | …Hammarberg & Joakim Sundén，2014）**。十處引用，撐起 flow 分類十一頁裡的九頁。 從[便利貼的撕法](../concept… |
| `agile-note` | 03-canon-guide.md | user-stories 分類 | **8** | 8 | 分類頁數 | …ser Stories Applied（Mike Cohn，2004）**。十三處引用，user-stories 分類八頁全部由它撐起，外加 scrum 的量測速度頁。 這是… |
| `agile-note` | 03-canon-guide.md | adoption 分類 | **10** | 10 | 分類頁數 | …cceeding with Agile（Mike Cohn，2009）**。十六處引用，adoption 分類十頁裡八頁由它撐起，另支援 scrum 與 xp-pra… |
| `agile-note` | overview.ts | 站台總頁 | **67** | 67 | 整站總數 | …的 Team Topologies 再把問題推到組織形狀本身。" +         "全站六十七頁概念頁全部從這批書逐章溯源。",     },     {… |
| `behaviour-interview-note` | 02-threads-and-schools.md | 站台總頁 | **50** | 36（＋題型 14） | 整站總數 | …），後兩條在房間**外**（職涯經營、自我盤點）。 > 這個接力順序不在任何一本書裡，是全站五十頁互相連結之後浮出來的結構。  ## 房間裡的四條線：一條生產… |
| `behaviour-interview-note` | 03-canon-guide.md | frameworks 分類 | **7** | 7 | 分類頁數 | …二根脊梁：The STAR Interview（Misha Yurchenko）。** frameworks 分類七頁有六頁由它撐起：[腦力傾倒](../concepts… |
| `behaviour-interview-note` | overview.ts | 站台總頁 | **36** | 36（＋題型 14） | 整站總數 | …am Geek》給協作用詞，《軟技能》給矽谷之外的第二套座標。" +         "全站三十六頁概念是<strong>方法語彙</strong>，十… |
| `bogle-note` | 02-threads.md | 站台總頁 | **14** | 14 | 整站總數 | …夠"     anchor: "docs/04-whats-enough/" ---  全站十四頁分在三個分類：指數投資七頁、投資哲學與德性四頁、Vang… |
| `bogle-note` | overview.ts | 站台總頁 | **14** | 14 | 整站總數 | …heading: "Claims",       body:         "全站十四頁可以疊成四條線。" +         "<stro… |
| `business-strategy-note` | 02-schools-in-dialogue.md | 站台總頁 | **38** | 38 | 整站總數 | …進那個產業」，破壞理論的忠告是「別追那群最好的顧客」。 這個交會點不在任何一本書裡，是 全站38 頁互相連結之後浮出來的。… |
| `clean-code-note` | 02-five-schools-in-dialogue.md | 站台總頁 | **77** | 77 | 整站總數 | …係：一場判準之爭、一個安全網同盟、一層無所不在的底色。 > 這個分組不在任何一本書裡，是全站七十七頁互相連結之後浮出來的結構。  ## 第一組 Clean 學派… |
| `cloud-infra-note` | 03-canon-guide.md | infrastructure 分類 | **4** | 6 | 歷史敘述 | …四本）：四本全數開口，借來的支架換成了自己的柱子  這一群翻得最徹底：四本原本都零引用，infrastructure 分類四頁全靠 Continuous Delivery、Wor… |
| `collins-note` | 02-threads.md | 站台總頁 | **15** | 15 | 整站總數 | …el/02-durability-of-a-great-flywheel/" ---  全站十五頁概念頁分在四個分類裡：卓越、長青、紀律、衰敗，分類的邊界幾… |
| `collins-note` | overview.ts | 站台總頁 | **15** | 15 | 整站總數 | …下》的衰敗五階段：傲慢、過度伸展、否認風險、病急亂投醫、投降。" +         "全站十五頁概念頁把這條鏈逐環攤開，每一環都溯源到七本書的章節。",… |
| `communication-note` | 02-schools-in-dialogue.md | 站台總頁 | **42** | 42 | 整站總數 | …4 年的科普新書與 1936 年的百年原典在同一點收斂；這個交會點不在任何一本書裡，是 全站42 頁互相連結之後浮出來的。… |
| `damodaran-note` | 02-threads.md | 站台總頁 | **14** | 14 | 整站總數 | …to-choosing-an-investment-philosophy/" ---  全站十四頁概念頁收在四個分類裡：估值方法、故事與數字、估值難題、投資… |
| `damodaran-note` | 04-critiques-and-limits.md | 站台總頁 | **14** | 14 | 整站總數 | …半針對他書外的公開估值與部落格，那些文章沒有收，只能轉述、不能背書；**判讀**，只站在全站十四頁已寫的內容上說話。 下文每一段都標明是哪一種聲音。… |
| `damodaran-note` | overview.ts | 站台總頁 | **14** | 14 | 整站總數 | …heading: "Claims",       body:         "全站十四頁可以疊成一條線。" +         "骨架是三個… |
| `de-botton-note` | 02-threads.md | 站台總頁 | **16** | 16 | 整站總數 | …論者的宗教學、建築與美的心理學。 五個題目看似互不相干：哲學、社會、愛情、宗教、建築。 全站十六頁一口氣讀完，浮出來的是**同一個動作做了五次**：把… |
| `design-patterns-note` | 03-canon-guide.md | di-ioc 分類 | **6** | 6 | 分類頁數 | …n & Mark Seemann，2019）。** 九條引用，**單書深挖密度第一**：di-ioc 分類六頁全部由它撐起，[DI 本體](../concepts… |
| `drucker-note` | 02-threads.md | 站台總頁 | **18** | 18 | 整站總數 | …)的回饋分析；往社會方向展開，回到 1939 年的老問題：一個給得出地位與功能的社會。 全站十八頁是同一個關懷在四個尺度上的展開：社會、組織、工作、人… |
| `economics-note` | 02-schools-in-dialogue.md | 站台總頁 | **53** | 53 | 整站總數 | …poverty/" ---  > 首頁的學派地圖擺了六張卡，單看像六個並列的陣營。 > 全站五十三頁讀完再回頭看，六張卡在進行**三場對話**：政府該不… |
| `fowler-note` | overview.ts | 站台總頁 | **11** | 11 | 整站總數 | …Layer、草圖不是藍圖、「模型無所謂對錯，只有有用與否」。" +         "全站十一頁分重構、企業架構、建模三區，對應這三個尺度。",… |
| `grant-note` | 02-threads.md | 站台總頁 | **16** | 16 | 整站總數 | …anchor: "docs/06-bouncing-forward/" ---  全站十六頁分在五個分類裡，跟著五本書走，乍看是人際、創新、認知、學… |
| `grant-note` | 04-critiques-and-limits.md | 站台總頁 | **16** | 16 | 整站總數 | …心理學經典正在經歷什麼、三分法有多粗、《擁抱 B 選項》的前提。 每一筆先講批評，再看 全站16 頁的證據，最後給判讀。 這些帳多半不是要刮掉書的價值，… |
| `grant-note` | overview.ts | 站台總頁 | **16** | 16 | 整站總數 | …heading: "Claims",       body:         "全站十六頁可以疊成一條由外而內、再往下扎根的線。" +… |
| `greene-note` | 03-canon-tour.md | 站台總頁 | **18** | 18 | 整站總數 | …條權力法則》《33 條戰爭策略》《喚醒你心中的大師》《人性 18 法則》，各有三到四頁，全站十八頁裡有十四頁半長在它們身上。  **支架兩本**：《誘… |
| `greene-note` | 03-canon-tour.md | power 分類 | **5** | 5 | 分類頁數 | …基維利《君主論》收束：關鍵不在永遠使壞，而在「保有選擇的能力」。  **對應概念頁**：power 分類五頁中的三頁。 [48 條權力法則](../concep… |
| `greene-note` | 03-canon-tour.md | mastery 分類 | **4** | 4 | 分類頁數 | …性 18 法則》的預演；學徒期的隱忍是「自我導向的戰爭」換了戰場。 **對應概念頁**：mastery 分類四頁全部出自此書：[喚醒你心中的大師](../conce… |
| `greene-note` | 03-canon-tour.md | human-nature 分類 | **5** | 5 | 分類頁數 | …己）；兩者互為表裡，「人性的理解愈深，權力的運用才愈不至於失控」。 **對應概念頁**：human-nature 分類五頁中的四頁：[人性法則](../concepts/hu… |
| `greene-note` | overview.ts | 站台總頁 | **18** | 18 | 整站總數 | …證精通是可理解、可複製的過程，把前面的清醒能量從防人導向成事。" +         "全站十八頁分權力、人性、策略、精通四類，對應這條從權術到精通的… |
| `grove-note` | 02-threads.md | 站台總頁 | **12** | 12 | 整站總數 | …新世界"     anchor: "docs/11-new-world/" ---  全站十二頁概念頁分在三個分類：產出（Output）、人（People… |
| `grove-note` | 03-canon-tour.md | 站台總頁 | **12** | 12 | 整站總數 | …ther-of-okrs/" ---  收五本書：葛洛夫親筆的四本，加一本別人寫他的。 全站十二頁概念頁的母體分佈極不平均：兩根脊梁餵飽十一頁，習題本只開一… |
| `grove-note` | overview.ts | 站台總頁 | **12** | 12 | 整站總數 | …heading: "Claims",       body:         "全站十二頁可以疊成一條線。" +         "先是量測（… |
| `growth-note` | 02-schools-in-dialogue.md | 站台總頁 | **37** | 37 | 整站總數 | …是動作的累積：名詞會被證明或證偽，動詞只會繼續或停止。 這個交會點不在任何一本書裡，是 全站37 頁概念頁互相連結後浮出來的。… |
| `habits-note` | 02-schools-in-dialogue.md | 站台總頁 | **34** | 34 | 整站總數 | …是**省著用**：預先決策、養成習慣，都為了少動用它。 這個交會點不在任何一本書裡，是 全站34 頁互連後浮出的結構：意志力是公認的稀缺資源，六個學派是… |
| `hbr-note` | 01-what-this-field-asks.md | 站台總頁 | **31** | 31 | 整站總數 | …Emotional Intelligence》）。 正典就是那些會被一再重印的東西。  全站三十一頁裡，掛到 Must Reads 原文的有十一頁。 [… |
| `hbr-note` | 02-threads.md | 站台總頁 | **31** | 31 | 整站總數 | …ensen、Kim、Ury、Amy Gallo、Maxwell）是按「架上有誰」畫的，與全站三十一頁實際挖出來的名字已經大部分重疊。 Porter（[什… |
| `hbr-note` | 03-canon-guide.md | 站台總頁 | **31** | 31 | 整站總數 | …立一條**合集專用的分層規則**，再照四個書群逐群攤帳。 > 四十六本裡有四十三本被挖進全站三十一頁，只剩三本沒被任何一頁引用：《Managing St… |
| `history-note` | 02-schools-in-dialogue.md | 站台總頁 | **32** | 32 | 整站總數 | …歷史、文明興衰、文化與社會史、戰爭與軍事、近現代與極權、歷史思維，與六個分類一一對應。 全站32 頁讀完，浮出來的是**三場對話**：歷史是被推著走的還… |
| `image-style-note` | 03-canon-guide.md | 站台總頁 | **13** | 13 | 整站總數 | …人打的**。 《Dressing the Man》（2002）是比例與合身的百科級正典，全站十三頁概念頁有九頁掛著它。 [比例與合身](../concept… |
| `investing-note` | 05-reading-path.md | 站台總頁 | **47** | 47 | 整站總數 | …細節在姊妹站 damodaran-note。  ## 站內動線：書讀到哪，頁就跟到哪  全站四十七頁概念是全程索引：六個分類各有 roadmap，從 b… |
| `jung-note` | overview.ts | 站台總頁 | **17** | 17 | 整站總數 | …性主導、以危機登門的歷程；自性是整體的中心，自我只是一小部分。" +         "全站十七頁分六區：機制、結構、道路、座標、生平、宗教。",… |
| `kent-beck-note` | overview.ts | 站台總頁 | **16** | 16 | 整站總數 | …可逆，先整理與否是時間價值與選擇權的拔河，而軟體的成本≈耦合。" +         "全站十六頁分六區，對應 1996→2023 的弧線。",     }… |
| `kiyosaki-note` | 02-threads.md | 站台總頁 | **14** | 14 | 整站總數 | …the-five-financial-iqs/" ---  首頁側寫列了清崎的六項貢獻，全站十四頁讀完，浮出來的是**同一個動作做了六次：先換定義，再… |
| `kiyosaki-note` | 03-canon-tour.md | 站台總頁 | **14** | 14 | 整站總數 | …trepreneur-investor/work-to-learn/)都在這裡首次出現，全站14 頁概念頁有 4 頁直接引它。 **富爸爸，有錢有理：神奇的現… |
| `lewis-note` | overview.ts | 站台總頁 | **13** | 13 | 整站總數 | …給分析版，《裸顏》給敘事版，讓佔有在一位敘事者身上現形五十年。" +         "全站十三頁分四區，對應這幾條線。",     },     {… |
| `management-note` | 03-canon-guide.md | 站台總頁 | **30** | 30 | 整站總數 | …書的地位**：誰承重、誰補一句、誰歸姊妹站。 48 本裡 **40 本是脊梁**，目前 全站30 頁，多數脊梁只挖了一鏟，所以這也是一張標出哪裡還沒挖的… |
| `marketing-note` | 02-schools-in-dialogue.md | 站台總頁 | **34** | 34 | 整站總數 | …明的文案讓人記住文案，清晰的文案讓人記住你要他做的事。 這個交會點不在任何一本書裡，是 全站34 頁互相連結之後浮出來的結構。… |
| `navarro-note` | 04-critiques-and-limits.md | 站台總頁 | **27** | 27 | 整站總數 | …判斷」成立，前三路的觀察紀律都有一個沒寫進去的前提：**觀察者當下的狀態必須夠格**。 全站二十七頁裡只有這一頁談到這件事，而它排在最後一區。 這是策展… |
| `navarro-note` | overview.ts | 站台總頁 | **27** | 27 | 整站總數 | …，<strong>誰提供心理舒適，誰就贏了</strong>。" +         "全站二十七頁分六區：四層各對應一區，另加一份《Three Minute… |
| `newport-note` | 02-threads.md | 站台總頁 | **11** | 11 | 整站總數 | …wport）八本書、五條招牌主張，攤開像五個題目：職涯、專注、手機、Email、節奏。 全站十一頁讀完，浮出來的不是五條平行線，而是**一個資本、四條… |
| `nouwen-note` | 04-critiques-and-limits.md | 站台總頁 | **12** | 12 | 整站總數 | …去向。 《心靈愛語》壓了八年才出版，是他把這條標準用在自己身上。 第二支打中一部分事實：全站十二頁裡，「罪」幾乎不曾是主語，「自我拒斥」才是。 這個替… |
| `peck-note` | 03-canon-tour.md | growth 分類 | **7** | 7 | 分類頁數 | …面展開，社群線是「愛」的群體尺度，安樂死辯論是「恩典」與靈魂觀的臨終應用。 開採也最深，growth 分類七頁中有五頁出自它：總樞紐[心靈地圖](../conce… |
| `peck-note` | 03-canon-tour.md | evil 分類 | **5** | 5 | 分類頁數 | …梁。** 它把邪惡從神學帶進臨床精神醫學：邪惡不在罪行大小，而在對自身罪性的絕對否認。 evil 分類五頁中三頁半出自它：總樞紐[邪惡人性](../conce… |
| `peck-note` | 03-canon-tour.md | community 分類 | **5** | 5 | 分類頁數 | …真社群四階段（偽社群、混亂、空、社群）與「真社群可以被刻意營造」的核心命題都在這裡。 community 分類五頁中四頁溯源到它：總樞紐[不同的鼓聲](../conc… |
| `peck-note` | 05-how-to-read.md | community 分類 | **5** | 5 | 分類頁數 | …*從組織與社群工作進來的讀者**：《不同的鼓聲》→《等待重生的世界》連讀是成立的短路徑，community 分類五頁全程隨行。 欠下的《心靈地圖》語彙（放棄、小小的死亡… |
| `peck-note` | overview.ts | 站台總頁 | **17** | 17 | 整站總數 | …群、混亂、空、社群四階段，一路下沉到婚姻與職場的「文明有禮」。" +         "全站十七頁分三區，對應這三層。",     },     {… |
| `peterson-note` | 03-canon-tour.md | meaning 分類 | **6** | 6 | 分類頁數 | …義是「對手」原型放大到國家尺度（終章〈The Hostile Brothers〉）。  meaning 分類六頁都出自此書：[意義的地圖：神話如何組織經驗](../… |
| `philosophy-note` | 02-schools-in-dialogue.md | 站台總頁 | **35** | 35 | 整站總數 | …> 以下把七張卡連成三組對話，再記一筆卡片本身的結構問題。 > 分組不在任何一本書裡，是全站三十五頁互相連結之後浮出來的。  ## 斯多噶 ✕ 應用哲學 ✕ 東… |
| `relationships-note` | 02-schools-in-dialogue.md | 站台總頁 | **42** | 42 | 整站總數 | …/)：兩個不完美的人相處，困難是必然，也是成長的邀請。  這個共識不在任何一本書裡，是 全站42 頁互相連結之後浮出來的。 科學派給修復工具，靈性派給修復理由，… |
| `science-note` | 02-schools-in-dialogue.md | 站台總頁 | **29** | 29 | 整站總數 | …語彙，同一個結構：先讓錯誤浮出水面，再讓它死在你之前。 這個交會點不在任何一本書裡，是 全站29 頁互相連結後浮出的結構，也是這裡叫科學**思維**而不是科學知… |
| `security-note` | 05-reading-path.md | 站台總頁 | **16** | 16 | 整站總數 | …nalysis/03-basic-dynamic-analysis/" ---  > 這全站十六頁沒有唯一正確的讀序：四個切面同心，從任何一面切進去，… |
| `spiritual-formation-note` | 02-schools-in-dialogue.md | 站台總頁 | **22** | 22 | 整站總數 | …；速食文化裡最反文化的一句話，是「這條路要走一輩子」。 這個交會點不在任何一本書裡，是 全站22 頁互相連結之後浮出來的結構。… |
| `stott-note` | overview.ts | 站台總頁 | **14** | 14 | 整站總數 | …可挑選項目，從不從眾、像基督，一路排到受造界關懷、簡樸與死亡。" +         "全站十四頁分三區，對應信仰根基、門徒與教會、聖經信息。",… |
| `taleb-note` | 03-canon-tour.md | randomness 分類 | **5** | 5 | 分類頁數 | …：灰天鵝、四象限地圖、截斷曝險與冗餘，**判斷從預測移到脆弱性**。  **對應頁**：randomness 分類五頁裡的四頁：[黑天鵝與極端世界](../concept… |
| `taleb-note` | 03-canon-tour.md | antifragility 分類 | **3** | 3 | 分類頁數 | …ame〉已指出凸性可以靠把凹性轉嫁給別人來偽造，這是下一本書的主題。  **對應頁**：antifragility 分類三頁全部出自此書：[反脆弱三元組與槓鈴策略](../co… |
| `taleb-note` | 03-canon-tour.md | asymmetry-practice 分類 | **4** | 4 | 分類頁數 | …的統計直覺推到最深：集合機率不等於時間機率，理性就是避免系統性毀滅。  **對應頁**：asymmetry-practice 分類四頁全部出自此書：[切膚之痛](../concepts/… |
| `taleb-note` | 03-canon-tour.md | fat-tails 分類 | **3** | 3 | 分類頁數 | …,000 檔證券沒有一檔細尾）。 它也是塔雷伯對批評者的技術答辯狀。  **對應頁**：fat-tails 分類三頁：出自《動態避險》的[選擇權風險的實務課](../c… |
| `taleb-note` | 05-how-to-read.md | randomness 分類 | **5** | 5 | 分類頁數 | …《黑天鵝效應》要讀第二版：〈後記論文〉是兩本書之間的橋，四象限地圖與冗餘哲學都在那裡。 randomness 分類五頁裡的四頁（從[黑天鵝與極端世界](../concep… |
| `taleb-note` | 05-how-to-read.md | antifragility 分類 | **3** | 3 | 分類頁數 | …mness/fourth-quadrant-and-robustness/)）接住前者，antifragility 分類三頁（從[反脆弱三元組與槓鈴策略](../concept… |
| `taleb-note` | 05-how-to-read.md | asymmetry-practice 分類 | **4** | 4 | 分類頁數 | …為預設你已有前兩階的裝備。 遍歷性一章是系列統計直覺的最深處，先讀反而會覺得只是格言。 asymmetry-practice 分類四頁逐章展開，讀前地圖是[切膚之痛](../concep… |
| `taleb-note` | 05-how-to-read.md | fat-tails 分類 | **3** | 3 | 分類頁數 | …體感進，流動性坑洞與陰影 gamma 是模型課不教的東西。 **散文線讀者**不必硬啃：fat-tails 分類三頁（[肥尾的統計後果](../concepts/fat… |
| `taleb-note` | overview.ts | 站台總頁 | **15** | 15 | 整站總數 | …之痛說風險必須回到決策者身上，凸性不能靠把凹性丟給別人來達成。" +         "全站十五頁分四區，對應騙局、診斷、處方、倫理四層。",     },… |
| `templar-note` | 02-threads.md | 站台總頁 | **14** | 14 | 整站總數 | …— 導論"     anchor: "docs/introduction/" ---  全站十四頁概念頁分在五個分類：守則、工作、人際、家庭、自我。 九本書… |
| `templar-note` | overview.ts | 站台總頁 | **14** | 14 | 整站總數 | …heading: "Claims",       body:         "全站十四頁在講五件事：規則體而非理論體（方法）；不必宣揚（姿態… |
| `thinking-note` | 02-threads-and-schools.md | 站台總頁 | **69** | 69 | 整站總數 | …話：判斷層的兩張處方、機制層的翻案同盟、向內層的接力。 > 這個分組不在任何一本書裡，是全站六十九頁互相連結之後浮出來的結構。  ## 第一組對話：判斷與偏誤… |
| `tools-note` | 02-threads-and-schools.md | 站台總頁 | **31** | 31 | 整站總數 | …種，習慣卡底下有一場關於「什麼讓習慣黏住」的三方混戰。 > 這個結構不在任何一本書裡，是全站三十一頁互相連結之後浮出來的。  ## 時間管理卡之內：一張桌上的三… |
| `tracy-note` | 02-threads.md | 站台總頁 | **27** | 27 | 整站總數 | …anchor: "docs/01-the-laws-of-life/" ---  全站二十七頁概念頁分在四個分類裡：目標與成就、時間與執行、銷售與影響力… |
| `uncle-bob-note` | overview.ts | 站台總頁 | **17** | 17 | 整站總數 | …smanship》熔成以 TDD 為基石的五大紀律與職業倫理。" +         "全站十七頁概念頁分三區，對應整潔程式碼、軟體架構、專業素養三個尺度。… |
| `willard-note` | 02-threads.md | 站台總頁 | **12** | 12 | 整站總數 | …w-testament-charter-on-apologetics/" ---  > 全站十二頁概念讀完，最先沉澱下來的往往是幾句一再回來的口訣：「… |
| `willard-note` | 04-critiques-and-limits.md | 站台總頁 | **12** | 12 | 整站總數 | …開場白。 這條他正面處理過，處理在體系的每個關節上。 「恩典不反對努力，反對的是賺取」在全站十二頁裡反覆出現（見[第二章](#02-threads)）… |
| `writing-note` | 02-schools-in-conversation.md | 站台總頁 | **46** | 46 | 整站總數 | …哪張是其餘四張的供水系統。 > 這一章把五張卡連成四組對話；這個結構不在任何一本書裡，是全站四十六頁互相連結之後浮出來的。  ## 對話一：風格與清晰 ✕ 非虛… |
| `wujun-note` | 02-threads.md | 站台總頁 | **17** | 17 | 整站總數 | …"docs/04-systematic-self-improvement/" ---  全站十七頁讀完，浮出來的是**一個命題與五種實現它的方式**。… |
| `wujun-note` | 02-threads.md | tech-civilization 分類 | **5** | 5 | 分類頁數 | …長鏡頭，大勢不是玄學，是有定律的  要看清位置與方向，得先看見大勢。 第一支透鏡是歷史，tech-civilization 分類五頁。 [浪潮之巔](../concepts/tech-… |
| `wujun-note` | 02-threads.md | science 分類 | **3** | 3 | 分類頁數 | …的人談格局，只能靠運氣站位。  ## 透鏡二：數學的顯微鏡，工程師給見識裝的另一隻眼  science 分類三頁是吳軍的本行。 [數學之美](../concepts… |
| `wujun-note` | 02-threads.md | wisdom 分類 | **3** | 3 | 分類頁數 | …嗅出來的。  ## 方法論：元智慧，可遷移的那一層  具體領域的知識會過期，什麼不會？ wisdom 分類三頁的答案是「智慧的智慧」。 [元智慧](../conc… |
| `wujun-note` | 02-threads.md | learning 分類 | **3** | 3 | 分類頁數 | …看的能力，元智慧把看到的東西變成可遷移的判斷力。  ## 養成：卓越是複利，不是事件  learning 分類三頁管時間。 [卓越](../concepts/lear… |

</details>

## 修法

**保語氣、只改被現況打臉的數字**（MODEL-ROUTING §二最後一列：導覽過期多數不必重寫，只要對帳）。改完把該章的 `writtenAt` 推到當天；如果是 `overview.ts`，順手看一眼`lede`／`Verdict` 有沒有一起過期。

數字對不上時**不預設是導覽錯**：頁被合併或除役時，導覽反而可能是對的——先看那句話在講什麼。

## 驗證

```bash
notes-core/tools/export-guide-drift.py --validate "2026-09-03 15:00"
```
拿各站在那個時間點的導覽文字配**現在**的頁數重跑：那之後被人改掉的數字＝真債、沒改的＝正確；算分類器在這套標籤上的漏報與誤報。

## 重跑

```bash
notes-core/tools/export-guide-drift.py
```
