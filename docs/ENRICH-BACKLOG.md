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
