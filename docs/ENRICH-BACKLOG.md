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

### 2026-11-12 下午 Fable 輪：三場對照頁裁決、Flow 第十章歸屬、26 本孤兒認領、信仰線與華文線選題 — **開 36 頁給 Opus**

**起點**：第三批 79／80 頁已 push；checkup blocker 0／warn 0／nit 18；ORPHAN-BOOKS 冒出 26 本（全是 11-06 之後新建的目的地書）；DEEPEN-TARGETS 剩 19 本。

**本輪做了四件事**
1. **三場「兩造都有頁」的官司**（下面「三個對照頁候選的裁決」）：clean-code 不開（導覽判互補，Thomas 與 Hunt 織進爭點三當第三層，clean-code `f918e54`）；wellness「看熱量還是看醣」開；travel「遊覽車該不該進公園」開，導覽「還開著的帳」第四條先改成三造並列（travel `a0b181a`）。
2. **Flow 第十章**：life-meaning 自挖一頁，落地後 tier 由 delegated:tools 改 spine。
3. **26 本孤兒認領進 travel-note**：兩個 fork 逐本讀書 repo 概述與章節、對照導覽第三章區域與既有頁，判 **spine 10／support 14／tool 2**，每本附 bibliography 條目、導覽句（spine 進區域小節、support 進支架清單、tool 進工具書）、spine 的頁工單。主會話抽 grep 三句導覽引文（史坦利的問候、Runte 的無用之地、杜拜三原則）全中。套用（bibliography 26 筆＋導覽第三章重算：脊梁 21→31、支架 12→26）交機械代理，travel-note 兩個 commit；tier-audit 在頁落地前會報 10 筆真欠債，是預期的。判層上留了三個條件：elephant-complex、travels-in-siberia 線成團再升 spine；last-spike、into-africa、city-of-gold 書站還是骨架，等書寫完再看；lost-heart-of-asia 判 spine 是依 Silk Roads 那筆 note「中亞是線」，若 lotto 不走烏茲別克就降 support。
4. **下一批選題**：信仰線 7 本開 12 收 **11**（keller 第 3 張與第一鏟同書同主題，改成 details）；華文線與 history 9 筆開 15 收 **12**（劉潤溝通、協作兩張與萬維鋼信息論人生觀留第三鏟）。體裁排除再加三本：《穩贏》（中年隨筆結集，六十九篇各自獨立）、《紅書》（幻象記錄，概念已由導論抽出）、《哲學經典的 32 堂公開課》（逐本導讀，按書查閱；**排除是排榜，不是禁止從它選題**，這輪就從它開了三頁）；已裁定再加《高手相對論》兩站（14 章 56 小節各數百字，章節數是小節撐高的，兩站兩頁已覆蓋）。

**本輪開給 Opus 的 36 頁**

| 來源 | 站 | 頁 |
| --- | --- | ---: |
| 孤兒認領 spine | travel-note | 10 |
| 對照頁 | wellness 1、travel 1 | 2 |
| Flow 第十章 | life-meaning | 1 |
| 信仰線 | keller 2、stott 2、spiritual-formation 2、lewis 2、philosophy 3 | 11 |
| 華文線與 history | fengtang 3、wan-weigang 2、liurun 5、history 2 | 12 |

**Opus 開工指令（Andrew 切模型後照這段做；Fable 2026-11-12 下午交接）**
0. 前置照上一輪（拉 repo、讀 MODEL-ROUTING §四、note-check §6、本節下面的單）。起草紀律照上一輪「Opus 開工指令」第 2、3 條：每頁一個子代理或一組一個代理自己寫、書本位、anchor 逐一 `[ -d ]`、**事實在哪章就掛哪章**、related 解析後重寫單行、`:::response` 留空、每頁交 3 筆具名事實附來源檔、主會話回源 grep、補 roadmap 與導覽第三章一句、蓋 enrichedAt、每站 build／format:check／tier-audit／checkup 全綠、單行英文 commit 不 push。**每個代理用自己的 scratchpad 子目錄**；`export-guide-drift.py` 不讀參數，別用 `--help` 試它。
1. **第一波（工具與既有頁）**：
   - `export-deepen-targets.py`：EXCLUDED_KINDS 加三本（理由見上）、SETTLED_BOOKS 加 `("wan-weigang-note","wan-weigang-what-is-relativity")` 與 `("science-note","wan-weigang-what-is-relativity")`；重跑。
   - `export-guide-drift.py` 句型放寬：overview.ts 與導覽 01／02 章裡「N 頁沿…」「N 頁」這類沒有「全站」前綴的頁數句，上一輪有約十處過期沒被抓到（hbr「三十一頁」、clean-code「七十七頁」、writing「四十六頁」、thinking「六十九頁」、travel「四十頁」、career「51 頁」、hr「二十一頁」）。把「overview 的 lede／導覽 01、02 章裡的 N 頁」也當整站宣稱試讀；仍沿用「所有合法讀法都不成立才報」。改完重跑，要改應為 0。
   - 既有頁補 anchor：science `relativity-of-simultaneity`（04、06、08、09、11/02）、history `table-manners-as-order`（04/06、03/05、05/02）、stott `between-two-worlds`（08/04）、fengtang `zizhi-tongjian-lessons` 的 label 改中文章題。
   - 既有頁加 details：travel `walking-japan-north-to-south` 加櫻前線一條掛 hokkaido-highway-blues 01 章（asia 單 hokkaido 那節）；keller 第一鏟頁加「復活的相遇」details 掛 06／07 那幾章（faith 單 keller 第 3 張的裁決）。
2. **第二波（36 頁）**，站的順序：travel 10（先 asia 單的紫禁城、澳洲、中亞、越南、芭蕉，再 west 單的荷蘭、義大利、西班牙、Runte、Nile；每頁落地時把該書的 tier 留 spine，tier-audit 真欠債隨頁數歸零）→ travel 對照頁 `the-coach-question`（Runte 頁先落地，依單上條件決定三造或四造）→ wellness `calories-or-carbs` → life-meaning `the-making-of-meaning`（落地後改 bibliography tier 與導覽第三章 28、33 行）→ 信仰線 11（philosophy 三張用 Warburton 當骨幹，alternative 照單）→ 華文線 12（liurun 先 8、7 再 12、13、11；fengtang 第 3 張若散就只寫 35、36）。
3. 收尾照上一輪第 4 條：`refresh-galaxy-docs.sh`、`export-seealso-gaps.py --allow-strict` → `apply-seealso.py`、在本節補「Opus 執行」戰報（頁數、抽驗筆數、照書改的標題、既有頁校正表、沒寫的張）。

**Opus 執行（2026-11-12 晚，Andrew「Go」）— 35 頁＋2 條 details 交付，19 站本機 commit（未 push）**
- **第一波**：notes-core `dd6b90c`（EXCLUDED_KINDS +3、SETTLED_BOOKS +2）、`4a5362a`（`export-guide-drift.py` 新增 BARE_TOTAL：總覽與導覽 01／02 章句首、沒有「站上／全站」前綴的「N 頁沿／用到／分在…」也試讀為整站宣稱）。新判定當場抓到三筆舊帳：design overview「四十九頁」→五十一、templar 導覽 02「十四頁」→十五、philosophy overview「三十五頁」（信仰線代理順手改成四十二）。既有頁補 anchor 四處、details 兩條（walking-japan 櫻前線、keller 復活的相遇）。
- **第二波**：五個代理（travel 11、wellness＋Flow 2、信仰線 10、華文線 12），主會話回源 grep 抽 **40 筆、全中**。
  - travel 10 頁讓 26 本認領書的真欠債 10 → 0、導覽死鏈 10 → 0；對照頁 `the-coach-question` 寫成**四造**（Runte 頁先落地，書裡確有「公園為觀光者而設」這條線）。
  - life-meaning `the-making-of-meaning` 落地，Flow 改 spine；tools 站少一筆 delegated，tier-audit 仍 0。
  - 照原文改的：fengtang 第 3 張只寫 ch35、36，標題改「伴君如伴虎：樂毅的四個關鍵與田單的攬功」；劉潤護城河照原文是「四類八條」（許可、品牌；規模、管理；用戶、生態；習慣、資產）；network-density 不寫「與網絡效應的差別」（書裡沒做這個區分）；澳洲頁補掛 03/06 鯊魚灣章（點題那句總結句出自那章）。
  - 收尾我補的事實對帳：wellness 導覽「Why We Sleep 是唯一的雙頁書」→ 七本多頁書照實列；liurun 導覽「幾乎一本一頁」補兩本體系書各三、四頁；fengtang `no-fire-on-arrival` 三條英文 label 改中文章題。
- **收尾**：seeAlso 補 2 筆（science、wan-weigang）；`refresh-galaxy-docs.sh` 後：checkup blocker 0／warn 0／nit 18（等書）、tier-audit 只剩 philosophy 2 筆已知衝突、GUIDE-DRIFT 要改 0、strong seeAlso 缺口 0、**ORPHAN-BOOKS 0**、DEEPEN-TARGETS **3**（data-science 2 等書、security 1 待 Andrew；life-meaning 的 Flow 記入 SETTLED_BOOKS）。
- **代理報的、主會話判誤報**：travel `visitor-management` 的杜布羅夫尼克 12,000 人，代理說查無出處；數字在 01/07 環境衝擊章，那頁本來就掛了，不動。
- **留給 Fable**：philosophy overview「四十二頁裡有二十六本書撐著」——概念頁實際引用 28 本，「撐著」可能另有算法，判讀句不由 Opus 改；philosophy 兩筆既成事實衝突（Great Thinkers、Daily Stoic 仍判 tool）若要重判；旅遊目的地第三鏟候選與兩個成團再升格的條件（Sri Lanka、Siberia）。


**留給 Andrew 的三個問題**：security-note 那張（Practical Malware Analysis 第五部）要不要寫、誰寫；lotto 走不走烏茲別克（決定 lost-heart-of-asia 的層）與西西里（若走，sicily 升 spine，west 單有工單草稿的章節：04-normans、05、06）。

#### 三個對照頁候選的裁決與 Flow 第十章（Fable 2026-11-12 下午）

上一批交付後，三場「兩造都有頁」的官司可以開 `kind: debate`，逐一過形狀測試：

- **clean-code「盡早崩潰 vs 把錯誤定義掉」：不開**。導覽第四章爭點三本來就判「分層互補」（先問 Ousterhout 的問題，消不掉再用 Clean Code 寫乾淨）；Thomas 與 Hunt 的 Tip 38 只是第三層（消不掉、寫乾淨之後仍違約就崩潰），沒有哪一造反對另外兩層。已把這一層織進爭點三（clean-code `04-consensus-and-disputes.md`），不另開頁。
- **wellness「減脂看熱量還是看醣」：開**（下面第 1 張）。三造各有頁、各說各的機制，導覽官司一已分層裁決。
- **travel「遊覽車進公園」：開**（第 2 張）。Abbey 要擋車、Holloway 要管車、Steves 要換旅館與景點的選法，三頁都在；導覽「還開著的帳」第四條已改寫成三造並列（travel `04-consensus-and-disputes.md`），帳仍掛著，對照頁是它的查閱單位版本。
- **Flow 第十章「意義的鍛造」：life-meaning 自挖**（第 3 張）。五站把這本書 delegated 給 tools，但 tools 的分類只有專注、習慣、筆記、時間，第十章沒有分類承接；life-meaning 導覽說「不深挖是因為別站已挖成多頁」，第十章沒有任何站挖過，理由不適用。頁落地後該站 bibliography 的 flow 由 `delegated:tools` 改 `spine`，導覽第三章 33 行那句改成「技術面在 tools 站，第十章意義的鍛造本站自挖」並連新頁。

骨架照既有 debate 頁（wellness 沒有 debate 頁，照 clean-code `comments-formatting/to-comment-or-not.md`）：`> 點題` → `::core` 列各造一句 → `## 各造立場` → `## ⚖️ 共識區與爭點` → `::takeaways` → `:::response`。不下裁決（裁決在導覽），判別變數只寫作者自己說的。anchor 從各造既有頁取並逐一 `[ -d ]`；事實在哪章就掛哪章。

1. wellness-note nutrition-sleep `calories-or-carbs`「減脂看熱量還是看醣：Matthews、江部與 Ferriss」— 熱量造：bigger-leaner-stronger（04-nutrition-advice/01-flexible-dieting、04-nutrition-advice/02-counting-calories-macros；取 flexible-dieting 頁的 anchor）；醣造：intermittent-fasting-low-carb-guide（02-no-weight-training-just-low-carb、03-two-meals-a-day；取 nutrition-foundations 頁的 anchor）；第三造 Ferriss：4-hour-body（01-principles/02-rules-that-change-rules 的「為什麼『卡路里進、卡路里出』說不通」一節與規則 1，03-fat-loss/01-slow-carb-diet-i 的「卡路里陷阱」）。
   各造只並排三件事：Matthews 說能量平衡是機制、沒有飲食法繞得過，控制卡路里排四步驟第一；江部說重點不是熱量而是有沒有醣，引 NEJM 與 JAMA 的比較研究，賣點是不必算卡路里；Ferriss 說消化不等於燃燒（Atwater 的卡路里是燒出來的）、研究者執著熱量是「停車場科學」（好測量好發表），他改走熱與荷爾蒙。判別變數只寫書裡有的：Matthews 的三套數字（赤字 20–25%、盈餘約 10%）、江部的飯後 2 小時血糖 160 mg/dl、Ferriss 的作弊日維持代謝。
   避開 daily-dozen（Greger 是「吃什麼」的軸，不是熱量對醣，只在點題句一句帶到）、nutritionism（Pollan 的意識形態批評歸導覽）、flexible-dieting／nutrition-foundations／slow-carb-diet 三頁各自的操作細節（三套數字的算法、三級減醣、五條規則不重講）；不寫「誰對」，導覽官司一已分三層裁。
   debate 頁；related 連 flexible-dieting、nutrition-foundations、slow-carb-diet、rules-that-change-the-rules、daily-dozen；導覽官司一第三層末尾加一行連到這頁。

2. travel-note tour-design `the-coach-question`「遊覽車該不該進公園：擋車、管車還是換選法」— 擋車：desert-solitaire（05-industrial-tourism-and-national-parks；取 desert-solitaire-and-industrial-tourism 頁的 anchor）；管車：business-of-tourism（03-intermediaries-in-tourism-services/01-management-of-visitors、01-defining-and-analysing-tourism/06-socio-cultural-impacts、01-defining-and-analysing-tourism/07-environmental-impacts；取 visitor-management 頁的 anchor）；換選法：europe-through-the-back-door（01-travel-skills/19-bus-tours-and-cruises；取 pacing-a-group-day 頁的 anchor）。
   各造只並排：Abbey 的提案（禁車、不修路、輪椅探險家既是消費者也是原料）、Holloway 的工具表（承載量與可接受改變限度、硬性與軟性、三個領域、導遊是遊客管理的一環）、Steves 的立場（辦團四十多年不反對團體旅遊，批評的是旅館蓋在城郊與景點因停車入選、50 人座與小巴之間選小巴）。判別變數只寫作者自己說的：Abbey 的湖泊比喻（距離與空間是速度與時間的函數）、Holloway 的「主要景點需求缺乏價格彈性，漲價未必減客」、Steves 的團體大小。
   避開 desert-solitaire 頁已寫的拱門成因與就地欣賞、visitor-management 頁的導遊四角色細節與杜布羅夫尼克數字（點題可引一次）、pacing-a-group-day 的節奏設計；不寫「我們就是那台車」的自省（那是導覽的判讀）。
   第四造（條件式）：Runte《National Parks: The American Experience》的頁 `worthless-lands-and-national-parks` 若先落地、且書裡確有「公園為觀光者而設」這條線，加為第四造並取那頁的 anchor；沒有就三造。
   debate 頁；related 連 desert-solitaire-and-industrial-tourism、visitor-management、pacing-a-group-day、staging-an-experience；導覽第四章「還開著的帳」第四條末尾加一行連到這頁。

3. life-meaning-note meaning `the-making-of-meaning`「意義的鍛造：目的、決心與和諧怎麼把人生連成一場心流」— flow-psychology-of-happiness（10-the-making-of-meaning、10-the-making-of-meaning/01-what-meaning-means、10-the-making-of-meaning/02-cultivating-purpose、10-the-making-of-meaning/03-forging-resolve、10-the-making-of-meaning/04-recovering-harmony、10-the-making-of-meaning/05-unification-of-meaning-in-life-themes；六個目錄 `[ -d ]` 驗過，合計約七萬字）。
   這本書在 life-meaning 判 `delegated:tools`，tools 站三頁掛第 2、3、4、7、8、9 章，第十章沒有任何站挖過。
   只寫 Csikszentmihalyi 的論證：在一項活動裡達成心流不保證其餘人生（畢卡索、費雪）、零散的享受仍受混沌擺布、掌控意識的最後一步是把全部人生變成統一的心流經驗；意義的三種用法（達成目的、追求目標的決心、重獲和諧）與三者合一；像磁場的目標、索羅金的三種文化（感官型、觀念型、理想型）；目的不讓生活變輕鬆（清教徒移民）、選擇太多決心變難（自由的悖論）；意識是雙面刃與人類特有的精神熵；人生主題的兩類（被接受的：艾希曼；被發現的）與鍛造被發現主題的三步（詮釋比創傷重要、把苦難詮釋為挑戰、把挑戰一般化到他人）。「認清生命本身是無意義的是一回事，認命接受是另一回事」照書引一次。
   避開 tools 站 flow-challenge-skill-balance 的八個成分與黃金比例、autotelic-self 的四條規則與耗散結構（第十章提到「自成目的的自我」時只接一句）、taming-solitude；避開本站 whats-worth-wanting 的四個水層與食譜測試、measure-your-life 的資源分配、redefine-retirement 的結構／目的／社群（related 連過去，不對照）；尼采「神已死」那段只寫 Csikszentmihalyi 怎麼回應，不做哲學史。
   claim 頁；related 連 whats-worth-wanting、measure-your-life、redefine-retirement、learn-to-die-learn-to-live；seeAlso 連 tools 站 focus-attention/flow-challenge-skill-balance 與 focus-attention/autotelic-self（路徑實存）。落地後：bibliography 的 flow 改 `tier: "spine"`、刪 delegatedTo、note 改「第十章意義的鍛造本站自挖，心流技術面在 tools」；導覽第三章 28 行「卻一本都不深挖」那句補一個例外、33 行改寫並連新頁；tier-audit 必 0。

#### travel-note 孤兒認領（亞洲／大洋洲／俄羅斯 14 本，Fable 2026-11-12）

判準照 2026-09-26 travel 判層的先例：目的地書多半 support／tool，只有團真的會走、而且書裡有一條領隊能在現場用的主張線才判 spine 開頁。這批 14 本都是 11-06 之後新建、沒有任何站認領的目的地書；lotto 走的線以導覽第三章的區域為準（日本、中國、東南亞、北歐俄羅斯紐澳，中亞依 Silk Roads 的 note 也算一條線），印度、斯里蘭卡不是線，先 support 等成團。year 填初版年（Penguin 的芭蕉英譯 1966、Ferguson 1998、Baker 的泰國史 2005、Evans 2002、Hayton 2010、Baker 的馬新史 1999、Pisani 2014、Gimlette 2015、Dalrymple 1993、Bryson 2000、Frazier 2010、Ziegler 2015、Thubron 1994、Barmé 2008），都早於或等於書 repo 的 published。spine 工單的章節目錄全部 `[ -d ]` 驗過（見檔尾驗證清單）。

**結果**：spine 5（芭蕉、紫禁城、Hayton 的越南、Bryson 的澳洲、Thubron 的中亞）、support 8、tool 1；開 5 頁，全部落 `destinations`。

##### narrow-road-to-deep-north（The Narrow Road to the Deep North and Other Travel Sketches）

**判層：spine**。spine。日本是第一名的線，東北團走的松島、平泉、山寺、象潟全在〈奧之細道〉一章裡（35KB），Booth 那頁只給東北一句開場；芭蕉的句子是領隊在現場能直接用的素材。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽句（「### 日本」那段，接在「……是關西寺社與庭園的講解底。」之後）：

> **The Narrow Road to the Deep North**（Matsuo Basho，Nobuyuki Yuasa 英譯，1966）是東北線的第三本：[奧之細道的幾站](../concepts/destinations/oku-no-hosomichi-stops/)取〈奧之細道〉從日光到象潟那幾站，領隊在松島與平泉開口時有芭蕉的句子可用。

頁工單：

1. destinations `oku-no-hosomichi-stops`「奧之細道的幾站：日光、松島、平泉、立石寺與象潟」— narrow-road-to-deep-north（docs/05-narrow-road-to-deep-north/、docs/00-preface/）。
   第一鏟：無（本輪認領）。東北線在站上只有 Booth 的〈北方之死〉一句開場（walking-japan-north-to-south）。
   只寫〈奧之細道〉裡團會站上的那幾站：序章「日月是百代的過客」與千住的離別、日光山、白河關與須賀川的第一首詩、仙台與壺碑、松島「日本最美之地」、平泉的夏草、立石寺的蟬聲、五月雨的最上川、羽黑山月山湯殿山、象潟「哀愁的美人」；每站只取芭蕉當場寫的句子與他記下的事，導論只借「不易」與「流行」兩個詞說明他為什麼邊走邊寫，一句帶過。
   避開 walking-japan-north-to-south 的 Booth 東北段（死亡與北方的語氣歸那頁）、japan-through-its-culture 的 Varley 文化史；湯淺導論裡的和歌到俳句的族譜、四行英譯的翻譯策略、五篇紀行的進步線都不寫（那是譯者的立場，不是現場）；前四篇紀行（野曝、鹿島、笈之小文、更科）不掛。學者指出芭蕉改動順序、虛構事件這一點照導論引一次，標明出處。
   claim 頁；related 連 walking-japan-north-to-south、japan-through-its-culture、learning-to-see-a-place、cultural-journey-sites（同為旁白語氣的範本）。

##### hokkaido-highway-blues（Hokkaido Highway Blues 北海道公路藍調）

**判層：support**。support。櫻前線與「外人さん」是好素材，但南北縱走的框架已由 Booth 的頁撐著，再開一頁地理重疊過半；它的位置是櫻花團的季節旁白。若要用，走「補進既有頁」：在 walking-japan-north-to-south 加一條櫻前線 details 並掛 docs/01-devils-washboard-kyushu/。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽句（「## 支架：一句話就位」的清單，依區域順序插在對應位置（日本的放最前面、東南亞的接在 Goscha 之後、南亞的接在 Zeppa 之後、俄羅斯的放 Coming into the Country 之後）；清單開頭「這十二本留在架上」的數字要跟著改）：

> **Hokkaido Highway Blues 北海道公路藍調**（Will Ferguson）：日本的第三本，追著櫻前線從佐多岬搭便車到宗谷岬；Booth 走路、Ferguson 搭便車，南北縱走那頁已由 Booth 撐著，它留給櫻花團當季節的旁白。

##### forbidden-city（The Forbidden City）

**判層：spine**。spine。片庫最多的中國線目前只有文化苦旅一本開頁、北京沒有書；Barmé 的〈階序的建築〉是進宮講解的底，〈三百年之後〉讓領隊能把 1949 之後的命運講進去。章節都二萬字以上。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽句（「### 中國」那段，接在「華東線的蘇州、上海與五城記另成……」之後；並把「片庫最多的中國線，目前只有這一本被挖成頁。」改成「片庫最多的中國線，到這裡才有兩本被挖成頁。」）：

> **The Forbidden City**（Geremie R. Barmé，2008）補上北京：[為展示而生的城](../concepts/destinations/forbidden-city-built-for-display/)取它的〈階序的建築〉與〈三百年之後〉，午門、三大殿的宇宙秩序，以及 1949 年之後這座城怎麼被拆、被改名、被毛澤東拒絕入住。

頁工單：

2. destinations `forbidden-city-built-for-display`「為展示而生的城：紫禁城的軸線、三大殿與它的二十世紀」— forbidden-city（docs/introduction/、docs/02-architecture-of-hierarchy/、docs/01-palace-of-blood-and-tears/、docs/07-three-hundred-years-on/）。
   第一鏟：無（本輪認領）。中國線只有文化苦旅一本開頁，北京沒有書。
   只寫：導論的「為展示而生的城」（逾 72 公頃、九百多個房間，層層城門的動線要讓天上宮廷投影到人間）；〈階序的建築〉的午門與乾隆凱旋、三大殿與宇宙秩序（金水河與景山、五行色彩數字、丹陛石）、外朝與內廷之間的三路格局；〈血淚宮〉的 1949 年後命運（四九方案、主席辦公樓的構想、工人說它「又空又醜」、大躍進與文革兩場浩劫反而救了它、單士元被掛牌示眾、周恩來下令重開）；〈三百年之後〉的李自成教訓、毛澤東拒入紫禁城而選中南海、「新的大內」。
   避開 cultural-journey-sites 與 suzhou-shanghai-five-cities（余秋雨的題）；慈禧（05）、帝王的一天（04）、宮牆內外（06）留第二鏟候選；作者在「帝制語彙只是被借用、還是在形塑權力」之間沒有選邊，頁上也不替他選；導論對西方「大內」想像的拆解只引一次。
   claim 頁；related 連 cultural-journey-sites、suzhou-shanghai-five-cities、reading-a-cathedral（同是用軸線與階序讀一座建築）、learning-to-see-a-place。

##### history-of-thailand（A History of Thailand）

**判層：support**。support。泰國團數多但取消率高，區域已降第二級；書是政治經濟取向的通史，領隊用它對年代，不是在車上講它。note 標「通史，講解底氣」。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽句（「## 支架：一句話就位」的清單，依區域順序插在對應位置（日本的放最前面、東南亞的接在 Goscha 之後、南亞的接在 Zeppa 之後、俄羅斯的放 Coming into the Country 之後）；清單開頭「這十二本留在架上」的數字要跟著改）：

> **A History of Thailand**（Chris Baker & Pasuk Phongpaichit）：東南亞的第三本，Osborne 給區域、Goscha 給越南，它給泰國；通史的用法是講解底氣，阿瑜陀耶與曼谷王朝的年代對它查。

##### short-history-of-laos（A Short History of Laos）

**判層：tool**。tool。六章簡史，寮國線沒有列在導覽區域裡；用法與 Keay 的中國通史相同，對年代與政權更替時查。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽句（「## 工具書」清單，接在 Keay 之後）：

> **A Short History of Laos**（Grant Evans，2002）：寮國簡史，六章；永珍、龍坡邦講解要對年代與政權更替時查它，和 Keay 的中國通史一樣不做成頁。

##### vietnam-rising-dragon（Vietnam: Rising Dragon）

**判層：spine**。spine。越南是東南亞區的主力，Goscha 已 support 給歷史，Hayton 給的是團員眼前的越南：街頭小吃的來歷、文明生活運動清街、下龍灣的門面與污染、特產餐廳的野生動物。〈趁它消失前去看〉直接就是觀光那一章。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽句（「### 東南亞」那段，接在 Osborne 那句之後）：

> 越南另有 **Vietnam: Rising Dragon**（Bill Hayton，2010）：Goscha 給近代史，它給團員眼前的越南。[斗笠之外的越南](../concepts/destinations/vietnam-beyond-the-conical-hat/)取〈街頭謀生〉與〈趁它消失前去看〉：街頭小吃怎麼來的、下龍灣的門面底下是什麼。

頁工單：

3. destinations `vietnam-beyond-the-conical-hat`「斗笠之外的越南：街頭、下龍灣與觀光客看不到的帳」— vietnam-rising-dragon（docs/introduction/、docs/03-living-on-the-streets/、docs/08-see-it-before-its-gone/）。
   第一鏟：無（本輪認領）。越南在站上只有 Osborne 的區域通史一頁與 Goscha 的一句支架。
   只寫：導論裡觀光客的「細節美學」（斗笠、稻田、水牛）正是越南人自己想拋在身後的國家、「只是在描述水面的漣漪」；〈街頭謀生〉的一條街在 24 小時內消失、被切割的房子、1989 年的街頭小吃革命、「文明生活」運動的清街與青蛙市場、臨街面從最低價變成最值錢、南北之別、機車上的青春；〈趁它消失前去看〉的下龍灣（觀光的門面、污染從四面八方湧入、管不動的管理機關）、吉婆島的「特產」餐廳與野生動物交易、熊膽禁令抓得到小農抓不到大戶、啤酒大亨的老虎、戰後砍掉的森林不比戰爭少。
   避開 southeast-asia-in-one-map 的 Osborne 三層（宮廷、農民、殖民）；政治章（04、05、06、07、09、10、11）與土地章（02）不掛，黨國體制只在點題句提一次；作者的處方（解開言論自由）是他的判斷，頁上不寫；數字密，起草代理每個數字回源。
   claim 頁；related 連 southeast-asia-in-one-map、visitor-management（下龍灣是遊客管理的實例）、working-with-local-partners、learning-to-see-a-place。

##### crossroads-malaysia-singapore（Crossroads: A Popular History of Malaysia and Singapore）

**判層：support**。support。新馬線沒有別的書，十九章通俗史；馬六甲、檳城、新加坡建國的講解底氣，但沒有一條領隊會在車上講的主張線。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽句（「## 支架：一句話就位」的清單，依區域順序插在對應位置（日本的放最前面、東南亞的接在 Goscha 之後、南亞的接在 Zeppa 之後、俄羅斯的放 Coming into the Country 之後）；清單開頭「這十二本留在架上」的數字要跟著改）：

> **Crossroads: A Popular History of Malaysia and Singapore**（Jim Baker）：新馬線唯一一本，馬六甲、檳城、萊佛士與新加坡建國的講解底氣；通史，查閱為主。

##### indonesia-etc（Indonesia, Etc. 印尼 Etc.）

**判層：support**。support。峇里島線用得到的只有開場那組數字，書的重心刻意放在爪哇與峇里之外；主張（恩庇是統一的代價）是政治判斷，不是講解。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽句（「## 支架：一句話就位」的清單，依區域順序插在對應位置（日本的放最前面、東南亞的接在 Goscha 之後、南亞的接在 Zeppa 之後、俄羅斯的放 Coming into the Country 之後）；清單開頭「這十二本留在架上」的數字要跟著改）：

> **Indonesia, Etc. 印尼 Etc.**（Elizabeth Pisani）：印尼唯一一本，寫的是爪哇與峇里之外的群島，峇里島線只借它第一章那組數字（13,466 座島、719 種語言）開場。

##### elephant-complex（Elephant Complex: Travels in Sri Lanka）

**判層：support**。support。斯里蘭卡不在導覽區域裡；書的章節正好是環島行程的站（可倫坡、獅子岩、康提、茶鄉、亭可馬里），線成團時可升 spine 開一頁。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽句（「## 支架：一句話就位」的清單，依區域順序插在對應位置（日本的放最前面、東南亞的接在 Goscha 之後、南亞的接在 Zeppa 之後、俄羅斯的放 Coming into the Country 之後）；清單開頭「這十二本留在架上」的數字要跟著改）：

> **Elephant Complex: Travels in Sri Lanka**（John Gimlette）：南亞的第二本，與 Zeppa 各守一國；環島一圈，可倫坡、獅子岩、康提、茶鄉各一章，斯里蘭卡線成團再升格。

##### city-of-djinns（City of Djinns）

**判層：support**。support。印度不在導覽區域裡；書是德里一城的七層史，語氣是旁白範本，線成團再升格。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽句（「## 支架：一句話就位」的清單，依區域順序插在對應位置（日本的放最前面、東南亞的接在 Goscha 之後、南亞的接在 Zeppa 之後、俄羅斯的放 Coming into the Country 之後）；清單開頭「這十二本留在架上」的數字要跟著改）：

> **City of Djinns**（William Dalrymple）：印度唯一一本，在德里住一年、一層一層往下挖的城市書；印度線成團前，它是德里講解的語氣範本。

##### in-a-sunburned-country（In a Sunburned Country）

**判層：spine**。spine。紐澳線只有 King 的紐西蘭，澳洲沒有書；Bryson 的第二、三部正好是雪梨、藍山、墨爾本、黃金海岸、大堡礁、烏魯魯，每章約二萬字，團天天站在這些點上。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽句（「### 北歐、俄羅斯、紐澳」那段，接在「Booth 的芬蘭篇另成……」那句之後，並把段尾「三個區域各一本，各自單兵。」改成「三個區域裡，紐澳現在兩本。」）：

> 澳洲原本沒有書，**In a Sunburned Country**（Bill Bryson，2000）補上：[空曠裡塞滿東西](../concepts/destinations/sunburned-country-east-coast/)取他的雪梨、藍山、墨爾本、黃金海岸、大堡礁與烏魯魯，King 管紐西蘭、Bryson 管澳洲。

頁工單：

4. destinations `sunburned-country-east-coast`「空曠裡塞滿東西：布萊森的雪梨、墨爾本、大堡礁與烏魯魯」— in-a-sunburned-country（docs/01-across-the-continent/01-forgotten-continent/、docs/02-the-civilized-south/01-sydney-and-first-fleet/、docs/02-the-civilized-south/02-blue-mountains/、docs/02-the-civilized-south/07-melbourne/、docs/02-the-civilized-south/10-aborigines-and-gold-coast/、docs/03-north-centre-and-west/01-cairns-and-great-barrier-reef/、docs/03-north-centre-and-west/03-alice-springs-and-uluru/、docs/03-north-centre-and-west/04-aboriginal-australia/）。
   第一鏟：無（本輪認領）。紐澳線只有 King 的紐西蘭，澳洲沒有頁。
   只寫團會站上的點：〈被遺忘的大陸〉的那組數字（1997 年《紐約時報》關於澳洲的文章 20 篇，祕魯 120、以色列 500 多）與「有那麼多東西可找，卻也有那麼大的地方要找」、1967 年弄丟總理；雪梨與第一艦隊（庫克把雨季誤認成旱季）；藍山；墨爾本；黃金海岸與原住民那章；凱恩斯與大堡礁的致命生物；愛麗絲泉與烏魯魯；原住民的澳洲那章只照書寫他記下的事與他自己承認的困境，不加評語。
   避開 aotearoa-two-settlements 與 treaty-comes-alive（紐西蘭）；內陸火車（01/02、01/03）、坎培拉、阿得雷德、達爾文、伯斯、鯊魚灣（團不走）不掛；布雷尼與克拉克的史學之爭只在點題句一句；幽默段落照書引，不自己加笑話。
   claim 頁；related 連 aotearoa-two-settlements、treaty-comes-alive、learning-to-see-a-place、pacing-a-group-day。

##### travels-in-siberia（Travels in Siberia）

**判層：support**。support。俄羅斯線是聖彼得堡與莫斯科，西伯利亞不是線；Figes 管歐俄，它管烏拉山以東，貝加爾湖線成團再升格。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽句（「## 支架：一句話就位」的清單，依區域順序插在對應位置（日本的放最前面、東南亞的接在 Goscha 之後、南亞的接在 Zeppa 之後、俄羅斯的放 Coming into the Country 之後）；清單開頭「這十二本留在架上」的數字要跟著改）：

> **Travels in Siberia**（Ian Frazier）：俄羅斯的第二本，Figes 管聖彼得堡與莫斯科，它管烏拉山以東；貝加爾湖與西伯利亞鐵路線成團再升格。

##### black-dragon-river（Black Dragon River 黑龍江）

**判層：support**。support。中俄邊界的河，主體在俄國一岸；哈爾濱、東北線只借它講邊界來歷，不夠撐一頁。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽句（「## 支架：一句話就位」的清單，依區域順序插在對應位置（日本的放最前面、東南亞的接在 Goscha 之後、南亞的接在 Zeppa 之後、俄羅斯的放 Coming into the Country 之後）；清單開頭「這十二本留在架上」的數字要跟著改）：

> **Black Dragon River 黑龍江**（Dominic Ziegler）：中俄邊界那條河，從蒙古源頭走到出海口；哈爾濱與東北線借它講邊界的來歷，主體在俄國那一岸。

##### lost-heart-of-asia（The Lost Heart of Asia）

**判層：spine**。spine。Silk Roads 的 note 明寫中亞是一條線（借歷史站當底），但本站沒有任何中亞現場的書；Thubron 的布哈拉、希瓦、撒馬爾罕三章就是烏茲別克團的三個站，各二萬五千字以上。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽句（「### 中東與埃及」那段末尾，接在「兩本各管一國，不互相補。」之後（中亞沒有自己的小節，暫放這裡））：

> 中亞線的書也放在這裡：**The Lost Heart of Asia**（Colin Thubron，1994）撐起[撒馬爾罕、布哈拉、希瓦](../concepts/destinations/samarkand-bukhara-khiva/)，蘇聯剛退場那一年的三座古城；絲路的歷史底借歷史站的 Frankopan，現場的樣子靠它。

頁工單：

5. destinations `samarkand-bukhara-khiva`「撒馬爾罕、布哈拉、希瓦：帝國剛退場的中亞」— lost-heart-of-asia（docs/03-bukhara/、docs/05-khorezmian-solitude/、docs/06-samarkand/、docs/08-tashkent/、docs/preface/）。
   第一鏟：無（本輪認領）。站上沒有中亞的頁，Silk Roads 判 delegated 給歷史站。
   只寫烏茲別克團的三個站加首都：布哈拉的卡蘭宣禮塔與修復中的聖城、兀魯伯經學院的守門人、異端的暗流（火與水）、消失的市集與飛走的鸛鳥；希瓦「被凍結的城市」與博物館化的古城、遲來的復興與稀薄的伊斯蘭、古烏爾根奇與瀕死的阿姆河；撒馬爾罕的雷吉斯坦「帝國的舞台布景」與走進後台、比比哈努姆清真寺的廢墟、帖木兒「最後的世界掠食者」與帖木兒之墓的看守人、「帖木兒讓我們成為一個國家」；塔什干一片空白的標語看板。序言只借「獨立後的第一個春天與夏天」定時間點，與「書中數位人物的身分已改寫隱匿」一句。
   避開歷史站的 Silk Roads（絲路通史歸那邊，seeAlso 不必，history 站沒有對口頁）；土庫曼（01、02）、費爾干納與帕米爾（09、10）、哈薩克與吉爾吉斯（11、12）不掛（團不走）；作者的四股力量框架（伊斯蘭、莫斯科、土耳其、西方）是他的分析，頁上不替五國下判。
   claim 頁；related 連 istanbul-huzun（同是伊斯蘭世界的城市書）、natashas-dance-two-russias（俄國留下的那一層）、learning-to-see-a-place。

##### 小結

- spine 5／support 8／tool 1；開 5 頁，全部 `destinations`，全部 claim。
- 支架清單從十二本變二十本，導覽那句「這十二本留在架上」要改數字；導覽第三章開頭「二十一本脊梁」變二十六本，也要改。
- 兩本判 support 但有升格條件：elephant-complex（斯里蘭卡線成團）、travels-in-siberia（貝加爾湖線成團）；hokkaido-highway-blues 的櫻前線可走「補進既有頁」，在 walking-japan-north-to-south 加一條 details 掛 docs/01-devils-washboard-kyushu/。
- 三本 note 標「通史，講解底氣」：history-of-thailand、crossroads-malaysia-singapore（support）、short-history-of-laos（tool）。
- 起草順序建議：2（紫禁城，章節最厚、邊界最乾淨）→ 4（澳洲，團點最多）→ 5（中亞）→ 3（越南，數字多要逐筆回源）→ 1（芭蕉，詩句要照書 repo 的譯文）。
- 旁註：in-a-sunburned-country 的書 repo 是兩層目錄（三部各有子章），anchor 要掛到子章；narrow-road-to-deep-north 的〈奧之細道〉是單一 35KB 章，anchor 掛章層即可。

#### travel-note 孤兒認領（歐洲／美洲／非洲／中東 12 本，Fable 2026-11-12）

判準：2026-09-26 的先例（目的地書多半 support／tool，只有團真的會走、書裡有一條領隊講解用得上的主張線才 spine 開頁）加三條本輪的補充：**書站只有骨架的不開頁**（last-spike 每章不到 2.5 KB、into-africa 與 city-of-gold 各章 1–2 KB，只有序與尾聲有內文）；**導覽沒列的線**（中歐、中南美、非洲、杜拜）一律 support 進支架，成團再升；**指南書判 tool**。
年份填初版年（書站 `published` 多半是美版或平裝版）。12 本都只有 travel-note 收；history-note 沒認領任何一本，通史類在 note 裡標「通史，講解底氣」。
spine 5 張的章節目錄全部 `[ -d ]` 驗過，related 的 slug 全部在 `concepts/destinations/` 與 `tour-design/` 實存。

##### 一、spine（5 本，開 5 頁）

**1. why-the-dutch-are-different（Ben Coates，2015）— spine，西歐**
判層理由：荷比線是第一級西歐線（書目 note 明列「德、法、瑞、荷、比」），架上原本沒有荷蘭的書；第一章「到處都是水」是風車、堤防、三角洲工程的講解底，每章四萬字，材料厚。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽第三章「### 西歐」段：開頭「四本脊梁，一國一本（瑞士兩本）」改成「五本脊梁，一國一本（瑞士兩本）」；在 Robb 那句之後加：
> **Why the Dutch Are Different**（Ben Coates，2015）撐起[從水裡造出來的國家](../concepts/destinations/dutch-water-and-polder-model/)：風車、圩田、1953 年的洪水與三角洲工程，荷比線從風車村到台夫特一路用得到。

頁工單：
1. destinations `dutch-water-and-polder-model`「從水裡造出來的國家：風車、圩田與 1953 年之後的荷蘭」— why-the-dutch-are-different（docs/introduction/、docs/01-water-water-everywhere/）。
   第一鏟：無，這是本書第一頁。
   只寫第一章與導論：面積只有蘇格蘭一半的國家為什麼是「隱形的超級強權」（導論）；風車一層一層把水抽上去造出低於海平面的圩田、「填海之國」、多德雷赫特與馬斯河上的曼哈頓（鹿特丹）；1953 年 1 月 31 日夜裡的洪水（近兩千人溺斃、七萬人離家、約二十萬公頃被淹）與之後三十年的三角洲工程、海岸線縮短近一半；maakbaarheid（可塑性）這個對自然的態度，以及它的另一面：荷蘭人均碳排幾乎是法國兩倍、「其實一點都不綠」；氣候變遷對一個低於海平面的國家意味什麼。數字逐字照書。
   避開 03-golden-age（VOC、鬱金香、林布蘭，留第二鏟給國家博物館那一天）、02 的柱化與 06 的移民爭論（那是政治題，導覽只帶一句）；avoid europe-in-three-strands 的三股力量、reading-a-cathedral 的教堂讀法。
   claim 頁；related 連 europe-in-three-strands、learning-to-see-a-place、pacing-a-group-day、germany-in-objects。
   第二鏟候選：03-golden-age（博物館之夜、香料、帝國的陰暗面、林布蘭）合國家博物館與林布蘭之家的講解；02-religious-divide 的柱化留給導覽。

**2. italians（John Hooper，2015）— spine，南歐**
判層理由：義大利線是第一級南歐線，架上只有 SPQR 管古代；Hooper 從地理與一千五百年外族統治解釋今天的義大利人，是領隊在車上回答「為什麼義大利這樣」的那本。每章兩萬字。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽第三章「### 南歐」段：在 Menocal 那句之後加：
> **The Italians**（John Hooper，2015）撐起[迴響與餘波](../concepts/destinations/italians-echoes-of-foreign-rule/)：SPQR 講羅馬人，它講今天的義大利人，南北、精明者與傻瓜、好面子都從一千五百年的外族統治講起。

頁工單：
2. destinations `italians-echoes-of-foreign-rule`「迴響與餘波：義大利人的習性從一千五百年的外族統治來」— italians（docs/01-beautiful-country/、docs/02-violent-past/、docs/03-echoes-and-reverberations/、docs/06-face-values/）。
   第一鏟：無，這是本書第一頁。
   只寫 Hooper 的主論證：每十個義大利人就有一個住在島上、本土被阿爾卑斯與亞平寧切碎，但真正的分界是南北不是東西（01）；良三世、倫巴底人、自治城邦、諾曼與西班牙統治、1527 年羅馬之劫，「在外國枷鎖之下」（02）；兩個義大利還是三個、帕特南把各區施政連到中世紀自治傳統、「精明者與傻瓜」（普雷佐里尼：傻瓜有原則，精明者只有目的）、脆弱的忠誠與兩次大戰換邊、轉型主義（03）；好面子與丟面子、用視覺說話、影像政治（06）。
   避開 rome-in-the-ruins 的羅馬遺跡與 SPQR 的帝國軸；避開 04 的法律迷宮、16–18 的黑手黨與回扣（留第二鏟或不開，領隊在車上不講黑手黨 GDP 比例）；飲食章（08）只在應用段一句。
   claim 頁；related 連 rome-in-the-ruins、europe-in-three-strands、seventeenth-century-painters、learning-to-see-a-place。
   第二鏟候選：08-gnocchi-on-thursdays（飲食與工作）、09-holy-orders（天主教與拉特朗條約，梵蒂岡那一天）、19-questions-of-identity（方言與地方主義）。

**3. ghosts-of-spain（Giles Tremlett，2006）— spine，南歐**
判層理由：西葡線是第一級南歐線，架上只有 Menocal 管中世紀安達魯斯；Tremlett 管二十世紀：烈士谷、內戰萬人塚、遺忘協定、巴斯克與加泰隆尼亞，領隊在馬德里與巴塞隆納被問到的全在這本。各章四到六萬字。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽第三章「### 南歐」段：接在 The Italians 那句之後：
> **Ghosts of Spain**（Giles Tremlett，2006）撐起[噪音底下的沉默](../concepts/destinations/spain-pact-of-forgetting/)：Menocal 的西班牙停在 1492 年，它從 1936 年接手，烈士谷、萬人塚與遺忘協定是馬德里那兩天會被問到的事。

頁工單：
3. destinations `spain-pact-of-forgetting`「噪音底下的沉默：內戰、佛朗哥與遺忘協定」— ghosts-of-spain（docs/introduction/、docs/01-secretos-a-voces/、docs/02-looking-for-the-generalisimo/、docs/03-pact-of-forgetting/、docs/14-fiesta-is-over/）。
   第一鏟：無，這是本書第一頁。
   只寫前三章與第十四章這條線：噪音之國對沉默（導論）；波亞萊斯德爾奧約 1936 年 12 月 29 日的三名女人與 2002 年諸聖節挖開的墳、戰爭的規模（約五十萬人死亡、雙方處決約二十萬人）與兩種殺戮的差別、佛朗哥一方的受害者留在路溝與井裡（01）；烈士谷、每年十一月的懷舊彌撒、被收進倉庫的佛朗哥、馬基游擊隊、恐懼留在血液裡（02）；1977 年大赦法第二條、「大赦就是一種遺忘」、沒有審判沒有真相委員會、23-F、遺忘的代價（03）；2007 年歷史記憶法、加爾松被停職、「兩個西班牙是否回來了」（14）。數字逐字照書。
   避開 al-andalus-three-faiths 的三教共處（時代不同，不接）；避開 04 觀光與貝尼多姆（那是 tour-design 的題，留第二鏟或補進 visitor-management）、09 三一一爆炸案、10–12 巴斯克、加泰隆尼亞、加利西亞（第二鏟候選：「三個不想當西班牙的地方」）。
   claim 頁；related 連 al-andalus-three-faiths、europe-in-three-strands、germany-divided-and-rebuilt、learning-to-see-a-place。
   第二鏟候選：10-serpent-and-axe、11-madness-of-verdaguer、12-coffins-celts-clothes 合成一頁（巴塞隆納與聖雅各之路都在裡面）；04-how-the-bikini-saved-spain 是觀光史，與 visitor-management 分工。

**4. national-parks-the-american-experience（Alfred Runte，1979）— spine，北美**
判層理由：導覽「未收與換書」自己寫了「國家公園線靠的是一本論戰散文而不是制度史」，這本就是那本制度史；Abbey 講看法，Runte 講公園為什麼存在，Holloway 的 visitor-management 講怎麼管，三頁正好三面。每章兩到三萬字。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽第三章「### 北美」段：在 Abbey 那句之後加：
> **National Parks: The American Experience**（Alfred Runte，1979）補上年表那一面，撐起[無用之地](../concepts/destinations/worthless-lands-and-national-parks/)：美國拿不出古堡與教堂，只能拿風景當民族自豪，而國會負擔得起公園，是因為那些地方本來就沒有別的經濟價值。

導覽「## 未收與換書」段末句「國家公園線靠的是一本論戰散文而不是制度史」已不成立，建議改成「國家公園線的制度史後來由 Runte 補上」（留 Fable 決定措辭）。

頁工單：
4. destinations `worthless-lands-and-national-parks`「無用之地：美國為什麼發明國家公園」— national-parks-the-american-experience（docs/prologue/、docs/01-american-west/、docs/02-yellowstone/、docs/03-worthless-lands/、docs/04-march-of-monumentalism/、docs/05-see-america-first/）。
   第一鏟：無，這是本書第一頁。
   只寫 Runte 的兩層論證：風景民族主義（傑佛遜的難題、新世界太新的文化自卑、卡特林的「國家的公園」、1864 年優勝美地公園法只保護 56 平方英里、尼加拉瀑布那個無可辯駁的損失）；無用之地（康尼斯在參議院保證優勝美地毫無價值、海登保證黃石每個月都有霜、道斯說若日後有用法案可廢、「無私很少能撐過限定條件」）；黃石營火邊的誕生神話是 1905 年修訂的日記、廣大邊界多半是偶然（02）；紀念碑主義：雷尼爾山法案由鐵路公司寫成、1905 年優勝美地被刪去三分之一、古物法、赫奇赫奇之戰（04）；「先看美國」與鐵路結盟、1916 年管理局法（05）只寫到法案成立，「啟發心靈永遠不足以成為擁有公園的理由」那一句收尾。
   避開 desert-solitaire-and-industrial-tourism 已寫的 1916 年授權兩派讀法與艾比的三項提案（這頁只交代法案怎麼來的，兩派之爭連過去）；避開 visitor-management 的承載量與遊客管理；06–13 的生態與擴張留第二鏟（紅杉國家公園那段與美西線關係最近）。
   claim 頁；related 連 desert-solitaire-and-industrial-tourism、visitor-management、chasing-the-aurora、learning-to-see-a-place。
   旁註：這頁落地後，導覽第四章爭點四（我們就是 Abbey 罵的那台車）有了第三個聲音（Runte：公園一開始就是給遊客看風景的，不是荒野保護），爭點四若要改寫一併看（Fable）。

**5. nile（Toby Wilkinson，2014）— spine，中東與埃及**
判層理由：埃及線的行程就是這本書的目錄，亞斯文、康翁波、艾德夫、路克索、西底比斯順流而下；同作者的通史已有兩頁管法老三千年，這本管河、水壩、採石場、泥磚村與今天的埃及人，三頁不重疊。每章三到五萬字。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽第三章「### 中東與埃及」段：原句「兩本各管一國，不互相補」改成「三本：Pamuk 管土耳其，Wilkinson 兩本管埃及」，並在 Wilkinson 那句之後加：
> 同一位作者的 **The Nile**（Toby Wilkinson，2014）沿河順流而下，撐起[順流而下的埃及](../concepts/destinations/nile-stone-and-mud/)：通史管法老，這本管亞斯文的水壩、採石場與泥磚村，遊輪每天停的那幾站。

頁工單：
5. destinations `nile-stone-and-mud`「順流而下的埃及：水壩、採石場與泥磚」— nile（docs/01-egypts-eternal-river/、docs/02-aswan/、docs/03-deep-south/、docs/05-western-thebes/）。
   第一鏟：無，這是本書第一頁；同作者的 rise-and-fall-of-ancient-egypt 已有 three-thousand-years-on-the-nile 與 ramesses-and-the-cost-of-empire 兩頁。
   只寫河這條線：沒有尼羅河就沒有埃及、95% 是沙漠、氾濫與王室編年史、船的家族、西方人眼中的尼羅河（庫克把達哈比亞行程壓成三週汽船、整趟 44 英鎊，愛德華茲與塞斯那批達哈比亞派）（01）；亞斯文是水的源頭也是控制水的地方：象島的水位計、1902 年舊壩讓棉產四倍、淹掉菲萊、1971 年高壩「把一年一度的氾濫送進了歷史」與代價（淤泥、鹽化、血吸蟲）（02）；石頭屬於國家、泥土屬於人民：傑貝爾西爾西拉的採石場、艾爾卡布的泥磚、艾德夫與伊斯納是外族統治下為安撫而蓋的晚期神廟（03）；西底比斯：底比斯是地方家族趁國家崩潰奪權的結果、戴爾麥地那的罷工與「先否認後冷漠、有限讓步配合安全鎮壓」、古爾納的盜墓者村莊被拆（05）。數字逐字照書。
   避開 three-thousand-years-on-the-nile 的王朝軸與路克索神廟＝王室之卡（04 不掛）、ramesses-and-the-cost-of-empire 的阿布辛貝與卡疊石；避開 07–10（阿拜多斯、中埃及、法尤姆、開羅）留第二鏟；2011 年與穆爾西只在作者立場一句帶過，不做時事。
   claim 頁；related 連 three-thousand-years-on-the-nile、ramesses-and-the-cost-of-empire、visitor-management、learning-to-see-a-place。
   第二鏟候選：10-cairo（開羅那一天）；06-qift-and-qena 的中央與地方張力（垃圾收集寓言、免稅令）是書的主旋律，若要開第二頁從這裡切。

##### 二、support（6 本，導覽各一句、不開頁）

**6. sicily（John Julius Norwich，2015）— support，南歐**
理由：西西里線（巴勒莫、蒙雷阿萊、切法盧、敘拉古）是義大利線的分支，導覽沒單獨列；書厚（每章二到四萬字）、諾曼那三章正是講解底，但照 Balkans 的先例「成團後再升格」。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽「## 支架：一句話就位」清單，接在 Glenny 那條之後：
> - **Sicily: An Island at the Crossroads of History**（John Julius Norwich）：南歐的第四本，SPQR 管羅馬、它管西西里這座每個強權都要佔的島；諾曼王國那幾章是巴勒莫與切法盧的講解底，西西里線成團再升格。

**7. habsburgs（Martyn Rady，2020）— support，中歐（第二級）**
理由：維也納、布拉格、布達佩斯那條線導覽沒列；三十一章的王朝通史，領隊要的是美泉宮、霍夫堡、皇家圖書館那幾段，查閱多於講述。通史，講解底氣。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽支架清單，接在 Sicily 之後：
> - **The Habsburgs: To Rule the World**（Martyn Rady）：維也納、布拉格、布達佩斯那條線的共同底，導覽沒有中歐這一節，先讓它在架上守著；美泉宮與霍夫堡要講瑪麗亞・特蕾莎或西西，翻它。

**8. last-spike（Pierre Berton，1971）— support，北美**
理由：加拿大洛磯線（班夫、露易絲湖、羅傑斯山口、螺旋隧道）全在這本書的路線上，本該 spine；但書站只有骨架（每章 1.7–2.5 KB，只有序與尾聲有內文），開不了頁。內文補上再升。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽支架清單，接在 McPhee 那條之後：
> - **The Last Spike**（Pierre Berton）：北美的第三本，專管加拿大洛磯線，羅傑斯山口、踢馬河的大坡與露易絲湖怎麼被找到都在裡面；書站還是骨架，先當支架。

**9. last-days-of-the-incas（Kim MacQuarrie，2007）— support，中南美（第二級）**
理由：祕魯線導覽沒列；書厚、敘事強（卡哈馬卡、馬丘比丘與比爾卡班巴之爭是馬丘比丘那一天的講解底），照 Zeppa「南亞唯一一本」的先例進支架，成團再升。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽支架清單，接在 Zeppa 那條之後：
> - **The Last Days of the Incas**（Kim MacQuarrie）：中南美唯一一本，卡哈馬卡的埋伏與「馬丘比丘是不是比爾卡班巴」是馬丘比丘那一天要講的；祕魯線成團再升格。

**10. into-africa（Martin Dugard，2003）— support，非洲（第二級）**
理由：東非線導覽沒列；書站只有序與尾聲有內文（各章 1–2 KB），開不了頁；坦干依喀湖、尚吉巴、「李文斯頓博士，我想？」是東非線的旁白素材。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽支架清單，接在 Incas 之後：
> - **Into Africa**（Martin Dugard）：非洲唯一一本，尚吉巴與坦干依喀湖的旁白素材，史坦利那句「李文斯頓博士，我想？」就是從這裡講起；書站還是骨架。

**11. city-of-gold（Jim Krane，2009）— support，中東與埃及（第二級）**
理由：杜拜是中轉點（Istanbul 那條書目 note 寫「杜拜多半只是中轉點，不另收書」，這本書進站後那句要改）；轉機停留一兩天的講解底：珍珠村落怎麼變黃金之城。書站只有序與尾聲有內文，不開頁。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽第三章「### 中東與埃及」段末加一句（不是支架清單，因為它接在既有區域段裡最順）：
> 杜拜本來只當中轉點，**City of Gold**（Jim Krane，2009）進站後，轉機停留那一兩天也有底：馬克圖姆家族的三條原則、拉希德在需求出現之前先蓋，以及勞工營那一章的代價。

另：bibliography 裡 `istanbul` 那條 note 的「杜拜多半只是中轉點，不另收書」改成「杜拜另收 Krane 的 City of Gold」。

##### 三、tool（1 本）

**12. national-parks-of-the-american-west（Don Laine & Barbara Laine，2012 版）— tool，北美**
理由：Frommer's 逐園指南（三十五園同一副骨架：避開人潮、只有一天怎麼玩、開車遊覽、露營住宿），排美西國家公園行程時查它，不講。年份填這一版的 2012（指南書的初版年沒有意義，每版重寫）。

（bibliography 條目已套用，見 travel-note `d7312de`）

導覽「## 工具書」清單，接在 Keay 之後：
> - **Frommer's National Parks of the American West**（Don Laine & Barbara Laine，2012）：三十五座西部國家公園逐園一章，避人潮的時段、只有一天怎麼玩、兩條招牌環線；排美西行程時查它，講解看 Abbey 與 Runte。

##### 小結

- spine 5（dutch、italians、ghosts-of-spain、runte、nile）開 5 頁；support 6（sicily、habsburgs、last-spike、incas、into-africa、city-of-gold）；tool 1（Frommer's）。
- 三本本該更高卻被書站材料擋下：last-spike（加拿大洛磯線的正典，骨架）、into-africa、city-of-gold；內文補上再回頭判。
- 導覽要動的地方：西歐段「四本脊梁」改五本並加 Coates；南歐段加 Hooper、Tremlett 兩句；北美段加 Runte；中東與埃及段改「兩本各管一國」並加 Wilkinson 第二本與 Krane；支架清單加 5 條（「這十二本留在架上」的數字要改十七本）；工具書加 Frommer's；「未收與換書」末句的「不是制度史」要改。導覽第三章開頭「目的地知識：二十一本脊梁」的數字加 5。
- 起草順序建議：4（Runte，補導覽自己承認的洞）→ 5（Nile，行程對口最直接）→ 3、2（西葡與義大利，第一級線）→ 1（荷蘭）。
- 旁註：Runte 落地後爭點四多了一造，導覽第四章改寫時一併看；Tremlett 第 4 章的貝尼多姆觀光史與 visitor-management 同題，第二鏟時分工。

#### 信仰線第二鏟選題單（keller／stott／spiritual-formation／lewis／jung／philosophy，DEEPEN-TARGETS 7 本，Fable 開單 2026-11-12）

判準取自 note-check §1.3 與 §1.4：只為脊梁書開頁、主張標得到章節 anchor、與既有頁重疊低於一半、能被單獨引用；先判體裁。七本裡兩本先過體裁關：《紅書》是幻象記錄、《哲學經典的 32 堂公開課》是逐本導讀，都不該用「大部頭只一鏟」的尺量，處置寫在不開那節。
姊妹站分工：theology-note 11-06 已從《追隨基督》取登山寶訓第二部（visible-yet-hidden、church-engage-or-contrast）、從《返璞歸真》取第四卷（beyond-personality）與前兩卷（argument-from-desire、head-or-heart-apologetics），本輪的單全部避開那些章；《當代講道藝術》biblical-studies 判 delegated 給 stott，沒有分工問題。
章節目錄名全部 `[ -d ]` 驗過（70 個）；單上引號裡的字句都 grep 過書 repo，查不到的改寫成「書裡講到」。

#### keller-note 第二鏟選題單（1 本，開 3 張）

《恐懼時代的盼望》91 章，第一鏟（jesus/hope-in-times-of-fear）掛 01-certain-hope 與 05-the-great-reversal 兩部，寫的是歷史性信仰、復活的證據、大逆轉與交換位置；第 2、3、4、6 到 12 部一字未用，書單 note 自己寫「大缺口」。站上五個分類裡 life 沒有一頁講成聖、apologetics 沒有一頁講盼望，這兩個洞正好是這本書第 8 與第 12 部。

1. life `resurrection-and-change`「復活與改變：脫去與穿上的兩個衝程」— hope-in-times-of-fear（docs/08-hope-for-you/01-risen-with-christ、docs/08-hope-for-you/02-resurrection-and-experience、docs/08-hope-for-you/03-resurrection-and-change、docs/08-hope-for-you/04-mistakes-about-growth-and-change）。
   第一鏟寫復活的證據與大逆轉的邏輯，停在「要被大逆轉拯救，就必須經過自己的逆轉」這一句；怎麼逆轉、改變的機制是什麼，書的第 8 部才講，站上 24 頁沒有一頁講成聖。
   只寫：成為基督徒「從一個領域被挪進另一個領域」而不是翻開新的一頁更努力（08/01，死的麥克風比喻）；教義純正必要卻不足夠，愛德華茲的印章與蠟印、保羅為「已經知道的事」禱告（08/02）；以弗所書與歌羅西書的兩個「衝程」，脫去與穿上、治死與求上面的事，書用二衝程引擎作比喻（08/03）；關於成長的誤解：向下衝程針對的不只是行為而是傾向犯罪的心的習慣，「把心安置」不等於努力好好過活（08/04）。
   避開 gospel 分類 counterfeit-gods 與 religion-vs-gospel 的偶像診斷（08/04 講到「只要得到這個」那段只引一句、related 連過去）、self-forgetfulness 的福音式謙卑；08/05 復活與實踐（海斯的兩條守則）與 08/06 大逆轉的倫理（艾略特「我們死，是為了活」）是倫理應用，不進這頁，留第三鏟。
   claim 頁；related 連 hope-in-times-of-fear、religion-vs-gospel、counterfeit-gods、self-forgetfulness。

2. apologetics `critique-of-secular-hope`「線性進步是誰的發明：世俗盼望的兩個設計缺陷」— hope-in-times-of-fear（docs/12-hope-for-the-future/01-the-rise-of-cultural-hope、docs/12-hope-for-the-future/02-the-loss-of-cultural-hope、docs/12-hope-for-the-future/03-a-revival-of-hope、docs/12-hope-for-the-future/04-the-critique-of-secular-hope、docs/12-hope-for-the-future/05-christian-resources-for-cultural-hope）。
   第一鏟沒碰第 12 部；making-sense-of-god 把盼望列為世俗主義與基督教並排的六項需要之一，只有一行。第 12 部五章四萬字是凱勒對文化盼望的完整論證。
   只寫：古代文化沒有「進步」的概念，循環或衰落，線性歷史觀是基督信仰帶來的（12/01）；1900 到 1950 年理性與科學沒能阻止的事，威爾斯從 1922 年《世界史綱》到二戰的信心崩解（12/02）；「歷史正確的一邊」怎麼在政治語言裡復興一種沒有神的進步信念（12/03，書引《大西洋》雜誌的統計）；世俗盼望的「兩個設計缺陷」，人性的問題與終極虛無的問題，用奧許維茲檢驗（12/04）；基督徒的盼望「合理的、豐滿的、實在的、有效的」四項（12/05，賴特的「更換典範」）。
   避開 making-sense-of-god 的六項並排與「世俗選項也需要信心」的總論證（這頁只做盼望一項，開頭一句接過去）、reason-for-god 與 doubt-your-doubts 的懷疑論證、第一鏟已寫的復活證據（12/05 第一項引用第 1 部時只說「見第一鏟」不重講）。
   claim 頁；related 連 making-sense-of-god、reason-for-god、doubt-your-doubts、hope-in-times-of-fear。

3. jesus `meeting-the-risen-jesus`「復活的相遇：馬利亞、多馬與彼得各自被拆掉的是什麼」— hope-in-times-of-fear（docs/06-personal-hope-1/01-mary-meets-jesus、docs/06-personal-hope-1/03-thomas-meets-jesus、docs/06-personal-hope-1/04-did-thomas-get-special-treatment、docs/07-personal-hope-2/02-jesus-confronts-peter、docs/07-personal-hope-2/03-jesus-restores-peter）。
   第一鏟只在 TIP 裡用了「目擊者起初認不出耶穌」一句；encounters-with-jesus 寫的是另一本書的約翰福音相遇（尼哥底母、拿但業等），多馬與彼得只各在一句裡帶過，抹大拉的馬利亞沒有。第 6、7 部十二章是復活後的相遇，兩站都沒挖。
   只寫：馬利亞認不出耶穌的更深原因，她心中的敘事「像濾網或屏幕一樣運作」，「她明明正看著他，卻看不見他」，耶穌先叫她的名字（06/01）；多馬「開出條件」，耶穌給他證據卻說沒有看見就信的有福了，多馬有沒有被特別對待（06/03、06/04）；彼得失敗的規模與三次否認，耶穌三問「你愛我嗎」對應三次否認，彼得沒有做的三件事與「沒有藉口。我知道我失敗了」（07/02、07/03）。
   避開第一鏟的復活證據（空墳墓、女性見證人、猶太世界觀），這頁不論證復活發生過，只寫相遇怎麼改變人；避開 forgive 的饒恕技術（彼得那段是復原不是饒恕論）；07/01 彼得遇見耶穌（加利利海邊，2.9K）與 07/04 保羅（4K）材料薄，只各一句；07/05 到 07/08 是護教收束，歸第一鏟題域不寫。
   claim 頁；related 連 hope-in-times-of-fear、encounters-with-jesus、jesus-the-king、forgive。
   **裁決（主會話）**：不開。與第一鏟同書同主題，三段相遇敘事重述的風險過半；改成第一鏟那頁加一條 details（馬利亞、多馬、彼得各一句，掛 06／07 那幾章），不另開頁。

##### 不開（留第三鏟）

- 11-hope-in-the-face-of-suffering/02-god-meant-it-for-good（約瑟，22K）：材料厚，但 forgive 頁已用《饒恕》的約瑟，suffering 頁已用《走過苦難》的六種姿態，第三本書的約瑟再開會是第三個版本的同一段敘事；留第三鏟，或在 suffering 頁加一條 details 掛這章（「藉著被勝過而得勝」書裡逐字有）。
- 10-hope-for-justice 整部與 life/generous-justice 題域重疊；09-hope-for-relationships 是種族、階級、性的應用章；02-future-hope 的已然未然國度（02/02）站上沒頁，但 6K 材料薄，等 jesus-the-king 第二鏟時一起看。

##### 小結

- 開 3 張，全部 claim 頁；起草順序 2（最獨立）→ 1 → 3。
- 旁註：第一鏟 TIP 引了波金霍恩「超物質的身體」那段，出處是 01/05-the-gospels-evidence-for-the-resurrection，現掛的 01 卷層涵蓋，不必動。

#### stott-note 第二鏟選題單（1 本，開 2 張）

《當代講道藝術》61 章，第一鏟（discipleship/between-two-worlds）掛 03、04、05、07 四部卷層，寫神學基礎五項信念、築橋、研究、真摯與熱誠；第 1 部歷史素描、第 2 部當代的反對、第 6 部預備講章、第 8 部勇氣與謙卑沒掛。第 6 部七萬八千字是全書最厚的一部，第一鏟只用一條子彈點列六個階段。

1. discipleship `preparing-a-sermon`「預備講章的六個階段：一篇講章只傳一個主要思想」— i-believe-in-preaching（docs/06-preparing-sermons/01-choose-your-text、docs/06-preparing-sermons/02-meditate-on-it、docs/06-preparing-sermons/03-isolate-the-dominant-thought、docs/06-preparing-sermons/04-arrange-your-material、docs/06-preparing-sermons/05-add-introduction-and-conclusion、docs/06-preparing-sermons/06-write-down-and-pray-over-it）。
   第一鏟在「築橋要求研究」那條底下列了六個階段的名稱，沒有展開任何一個。
   只寫：選經文的四項因素與「不是因為經文太少，而是因為經文太多」（06/01）；默想要像蜜蜂探花、最遲前一個星期一選好（06/02）；「每一段經文都有一個最重要的思想」，好撒瑪利亞人與羅馬書五章 8 節兩個例子，講道與講課的分別在只傳一個信息（06/03）；安排資料的消極面是無情捨棄、積極面靠結構、措辭與例證，書引「優美的講章是撒但最危險的陷阱之一」（06/04）；引言的兩個目的與結論，先寫本文再加頭添尾（06/05）；寫下講稿並為它禱告，沈美恩勸學生三百至四百篇講稿之前不要即席講道（06/06）。
   避開第一鏟的五項神學信念、築橋與化身、研究的呼召（05 部不掛）、真摯與熱誠；避開 living-church 與 understanding-the-bible 的解經三原則（「解釋的相反是強解」已在第一鏟，這頁不重講）。
   claim 頁；related 連 between-two-worlds、understanding-the-bible、living-church、radical-disciple。

2. discipleship `objections-to-preaching`「今天為什麼還要講道：反權威、電視與教會失去信心」— i-believe-in-preaching（docs/02-contemporary-objections-to-preaching/01-anti-authority-mood、docs/02-contemporary-objections-to-preaching/02-christian-response、docs/02-contemporary-objections-to-preaching/03-dialogical-preaching、docs/02-contemporary-objections-to-preaching/04-cybernetics-revolution、docs/02-contemporary-objections-to-preaching/05-influence-of-television、docs/02-contemporary-objections-to-preaching/06-the-learning-process、docs/02-contemporary-objections-to-preaching/07-church-loss-of-confidence-in-gospel、docs/02-contemporary-objections-to-preaching/08-recovery-of-christian-morale）。
   第一鏟只在點題句說「現代的情勢使它更困難，卻沒有減少其必要性」，第 2 部八章七萬字就是這句話的論證。
   只寫斯托得列的三種反對與回應：反權威的心態，有些反叛基督徒應該帶頭，兩種相反的錯誤（放棄講道、更獨斷），基督教對人性與權威的看法（02/01、02/02）；對話式講道，先澄清不是什麼，北美黑人教會的回講傳統，講道需要研究班與討論小組輔助（02/03、02/06）；神經機械學的革命與電視的五種害處，麥魯漢（02/04、02/05）；教會對福音失去信心，宣講與傳福音兩個字的前提都是「要說的話已經授與我們」，士氣的恢復要分辨確信、堅信、假定與盲信四個字（02/07、02/08）。
   避開第一鏟的全部；避開 issues-facing-christians-today 的 C 型觀點（02/01 講到基督徒該帶頭的反叛時只引一句連過去）；01 部歷史素描不掛（見不開）。
   claim 頁；related 連 between-two-worlds、issues-facing-christians-today、basic-christianity、preparing-a-sermon（第 1 張）。

##### 既有頁漏掛 anchor

- between-two-worlds 正文「勇氣的具體作法是按次序系統解經……牧會二十五年從未講過離婚」出自 08-courage-and-humility/04-value-of-systematic-exposition，anchor 只掛 03、04、05、07 四部，補掛 docs/08-courage-and-humility/04-value-of-systematic-exposition/（事實在哪章就掛哪章；目錄驗過）。

##### 不開（留第三鏟）

- 08-courage-and-humility/03-comfort-and-disturbance（18K，先知的兩面與假先知的虛謊安慰）與 08/08-the-power-of-the-spirit（13.7K）：材料夠一頁「講道的勇氣：安慰與使人不安」，但第一鏟已從 08 部取了系統解經與真摯熱誠的結論，排在上面兩張之後。
- 01-glory-of-preaching-historical-sketch 五章 56K 是講道史素描，導覽第四章已用它定位鍾馬田；體裁是歷史，不開概念頁。

##### 小結

- 開 2 張，全部 claim 頁；起草順序 1 → 2。
- biblical-studies 判 delegated 給 stott，兩張落地後漏接檢查仍過。

#### spiritual-formation-note 第二鏟選題單（2 本，開 2 張）

1. discipleship `conformed-to-christ`「聖徒與基督的形像：成聖不是效法，是被塑造」— cost-of-discipleship（docs/04-church-of-jesus-christ/05-the-saints、docs/04-church-of-jesus-christ/06-the-image-of-christ）。
   第一鏟（costly-grace）掛 01、02 兩部卷層，寫廉價恩典、信與順服不可分、捨己；theology 的 costly-grace 掛 01/01、03、04、05 與 02/15，visible-yet-hidden 掛 02/02、07、08、09、10，church-engage-or-contrast 掛 02/02、07、09。第 3、4 部兩站都沒碰，第 4 部五萬六千字是潘霍華的教會論與成聖論。
   只寫：「唯有神是聖潔的」，神在與罪惡世界分別中聖潔、也在罪惡世界中設立聖所中聖潔，真正的聖殿是基督的身體；中心難題是神如何由罪人造聖徒又不損祂的義，答案在十字架；稱義與成聖源頭相同、內容相同卻不相同，書裡有對照表（04/05）；人以自己的方式「如神」而失去神，神不放棄祂失喪的受造物，形變必須發生在神身上，神兒子取了奴僕的形像；「效法基督的形像」不是要追求的理想，是基督的形像要在我們裡面被塑造；道成肉身、被釘、復活三層形像；「對至小之人的攻擊，都是對基督本身的攻擊」（04/06）。
   避開本站 costly-grace 與 theology 兩頁的重價恩典、捨己、登山寶訓；避開 imitation-of-christ 與 inward-consolation 的多馬肯比斯（這頁要寫明潘霍華的「被塑造」與「效法」的差別，related 連過去對讀）；04/02 洗禮、04/03 身體（只在聖殿那段引一句）、04/04 可見的群體是教會論，歸 theology 題域或第三鏟；03 部使者不開（見不開）。
   claim 頁；related 連 costly-grace、imitation-of-christ、downward-way、life-together；seeAlso 連 theology 站 doctrine/costly-grace（已存在）。

2. prayer-pilgrimage `christ-the-intercessor`「基督是代求者，我們是祭司：代禱的根據」— with-christ-in-the-school-of-prayer（docs/26-christ-the-intercessor、docs/27-christ-the-high-priest、docs/28-christ-the-sacrifice、docs/30-the-ministry-of-intercession）。
   第一鏟（school-of-prayer）掛 01、05、21、24 四課，寫禱告要學、耶穌訓練代求者、應允是驗算、住在我裡面、奉我的名；它把「代求者」當成學校的終點，卻沒寫代求的根據在哪。第 26 到 30 課是全書的基督論收束，沒掛。
   只寫：「他活著，就是要代求」，麥基洗德比亞倫更榮耀，代求是絕對必要的工作，沒有它救贖就不能持續施行；不是兩道分開的禱告之流，「他所禱告的經過我們，我們所禱告的經過他」（26）；約翰福音十七章大祭司的禱告分三部分，教導奉耶穌的名可以求什麼（27）；客西馬尼那課，兩種祈求的無限差別，「正是在那句「父啊，不要從我的意思」裡，他取得了說「父啊，我願」的能力」，客西馬尼的四重奧祕（28）；祭司的工作有向神與向人兩面，「祭司是一個不為自己而活的人」，亞倫兒子的授職與血抹耳手腳的對照，每一位信徒都有作祭司的權利（30）。
   避開第一鏟的四課與它已寫的「訓練代求者」「國度的降臨繫於禱告」兩條（這頁從基督論補根據，不重講學校的課程表）；避開 prayer-as-conversation 的路易斯與 pursuit-of-god；31 禱告的生活（19K）是總結課，只在收尾引「整個生命完全降服於神」一句；16 恆切禱告與 29 放膽留第三鏟。
   claim 頁；related 連 school-of-prayer、prayer-as-conversation、practicing-the-presence、pursuit-of-god。

##### 不開（留第三鏟）

- cost-of-discipleship 03-the-messengers（馬太福音十章六章 28K）：「他們所做的不是自己的工作，而是神的工作」撐得起一頁，但本站 discipleship 已九頁，downward-way 與 long-obedience 的題域相鄰；等第 1 張落地再量重疊。
- with-christ-in-the-school-of-prayer 16-the-power-of-persevering-prayer（13.5K）：「為什麼神延遲應允」單課成頁，與第一鏟「拒絕也是一個回答」接得上；第三鏟候選。

##### 小結

- 開 2 張，全部 claim 頁；起草順序 1 → 2。
- 姊妹站分工：潘霍華的登山寶訓與恩典論歸 theology 已開的三頁，第 4 部成聖論落本站；教會論（04/02 到 04/04）兩站都沒挖，誰開由 Fable 下輪判。

#### lewis-note 第二鏟選題單（1 本，開 2 張）

《返璞歸真》第一鏟（apologetics/mere-christianity）掛第一卷與第四卷卷層，正文是四卷的漏斗總覽；theology 的三頁掛第一、二卷與第四卷 01、02、04、05、11。第三卷十二章約十萬字兩站都沒碰，第四卷 07 到 10 四章四萬字也沒有。人物站一書一頁是常態，這本是全集入口、兩卷整卷空著，開兩張。

1. devotional `the-great-sin`「大罪與兩種意志的動作：驕傲、饒恕與仁愛」— mere-christianity（docs/03-christian-behaviour/07-forgiveness、docs/03-christian-behaviour/08-the-great-sin、docs/03-christian-behaviour/09-charity）。
   第一鏟用一句話帶過「把驕傲診斷為一切惡的根源，寬恕、愛仇敵被解構為意志的選擇」；screwtape-letters 頁的驕傲是另一本書的魔鬼視角。
   只寫：「人人都說饒恕是可愛的觀念，直到自己有東西要饒恕」，愛人如己的「鄰人」包含仇敵，饒恕不是喜歡（07）；驕傲是「幾乎沒人（除了基督徒）會懷疑自己也犯了」的惡，「我們自己越多，就越在他人身上不能忍受」，書的小標「基督教道德的真正中心」，驕傲與其他罪的差別在它是競爭性的（08）；Charity 的本意是基督教意義的「愛」而不是施捨，基督教的「愛」不是感情，先做出愛的行動感情才跟上（09）。
   避開 four-loves 的四種愛（09 講 charity 時只在 related 連過去，不比較）；避開第四卷（theology 的 beyond-personality 與本站第 2 張）；03/01 到 03/04 道德的三個部分、四樞德、社會道德、精神分析與 03/10 盼望留第三鏟，03/05、03/06 性道德與婚姻歸 love 分類第三鏟；03/11、03/12 信心的兩種意義（16K）可併進這頁的收尾一段或留第三鏟，由起草者看篇幅定。
   claim 頁；related 連 mere-christianity、four-loves、screwtape-letters、great-divorce。

2. devotional `lets-pretend`「讓我們假裝：裝扮成基督怎麼變成真的」— mere-christianity（docs/04-beyond-personality/07-lets-pretend、docs/04-beyond-personality/08-is-christianity-hard-or-easy、docs/04-beyond-personality/09-counting-the-cost）。
   第一鏟把第四卷寫成「好的傳染」與「新人」兩句；theology 的 beyond-personality 取 01、02、04、05、11（生與造、三位格的神、良性感染、頑固的錫兵、新人）。07 到 09 兩站都沒掛，而這三章是路易斯講成聖機制的地方。
   只寫：美女與野獸與戴久了的面具兩個故事，「裝扮」演變成了真實，主禱文的「我們的父」就是在假裝（07）；基督教是難還是易，一般人對「做好人」的理解是讓步給要求，基督徒的路是把整個自然的自我交出去，所以更難也更易（08）；「你們要完全」不是「除非你完全否則我不會幫你」，「我唯一會給的幫助，是「使你成為完全」的幫助」（09）。
   避開 theology 那頁的五章（10-nice-people-or-new-men 緊鄰 11，只在收尾引「死本身是這療程的一部分」一句，不掛）；避開第一鏟的道德律與三選一；避開 weight-of-glory 的渴望論。
   claim 頁；related 連 mere-christianity、weight-of-glory、great-divorce、the-great-sin（第 1 張）；seeAlso 連 theology 站 doctrine/beyond-personality（路徑已存在）。

##### 小結

- 開 2 張，全部 claim 頁；起草順序 2（材料最集中）→ 1。
- 第三卷其餘九章與第四卷 03、06 兩章列第三鏟候選，不進工具。

#### jung-note（1 本，不開）

- jung-red-book-readers-edition《紅書》：不開。體裁是 1913 到 1930 年的幻象記錄加評註，四十章裡三十四章是 Liber Primus 與 Liber Secundus 的幻象序列（紅衣人、森林裡的城堡、隱士、地獄、三次夜、魔法師），不是論證。第一鏟（life/spirit-of-the-depths）已把能抽成概念的全部抽出：兩個精神、弄丟的靈魂、積極想像的方法與系譜、兩層結構、從《紅書》長出的理論、《省察》的去認同。剩下唯一成組的是斐勒蒙（02/19 魔法的恩賜、02/21 魔法師，合計 37K），但他教的「心靈的客觀性」已在 confrontation-with-the-unconscious 用《回憶・夢・省思》原句寫了，the-tower 也有門楣。tier 維持 spine。**建議進 EXCLUDED_KINDS**，體裁理由：「幻象記錄，章節是幻象序列與評註，概念已由導論與第一部抽出」。

#### philosophy-note 第二鏟選題單（1 本，開 3 張）

《哲學經典的 32 堂公開課》三十二章各講一部原典，每章六到九千字，章章獨立、全書只有編年沒有主軸，照「每則互不相承且全書無主軸」的判準該進 EXCLUDED_KINDS，體裁理由「逐本導讀，三十二章各講一部原典，按書查閱」；它不該再用「大部頭只一鏟」的尺排榜。
但導覽第三章自己寫這組是「取了工法，還沒取內容」：第一鏟（intro-history/reading-the-classics）拿它當方法論，示範了柏拉圖、亞里斯多德、笛卡兒三章，三十二部原典裡站上有頁的只有《理想國》《尼各馬可倫理學》《正義論》（都是原書）。下面三張不是第二鏟，是選題：各補一個分類裡缺席最明顯的經典，骨幹是 Warburton 的導讀章，Sandel 的章可當第二來源。重疊都 grep 過：康德在 three-paths-of-justice 只一行、彌爾的傷害原則在 utility-and-its-limits 沒有、沙特在站上只在卡繆頁被點名。

1. ethics-justice `categorical-imperative`「善意志與定言令式：康德為什麼說出於同情的善行沒有道德價值」— philosophy-the-classics（docs/15-kant-groundwork-of-the-metaphysic-of-morals）；alternative 掛 justice-whats-the-right-thing-to-do（docs/05-what-matters-is-the-motive）。
   站上 three-paths-of-justice 的路徑二只有「康德說人是目的、不是手段」一行；utility-and-its-limits 寫效益主義時拿康德當對照也只一句。
   只寫 Warburton 這章：唯一無條件善的是善意志，勇氣、權力、財富都要善意志保證；義務與傾向，精明商人的審慎不是道德，「僅僅出於同情傾向的行為完全沒有道德價值」與它的理由（傾向是運氣）、實踐的愛對病態的愛；準則，同樣的行為可能源自不同準則；假言令式對定言令式，普遍化公式與人是目的公式；章末 Warburton 列的批評（空洞形式、違反直覺）照書寫。Sandel 那章只取他對康德的轉述當第二來源，不寫 Sandel 自己的案例。
   避開 three-paths-of-justice 的三路徑架構與 utility-and-its-limits 的效益論本體（開頭一句接過去）；avoid justice-as-fairness 的羅爾斯（原初狀態不是康德的，related 連）。
   claim 頁；related 連 three-paths-of-justice、utility-and-its-limits、justice-as-fairness、eudaimonia-and-the-mean。

2. political `harm-principle`「傷害原則：對他人的傷害是阻止個人行為的唯一正當理由」— philosophy-the-classics（docs/18-mill-on-liberty）。
   political 八頁裡 Sandel 的共善、市場界線與才德佔了一半，自由主義那一造只有羅爾斯；utility-and-its-limits 寫彌爾的高低快樂，沒有《論自由》。
   只寫：彌爾自稱「一個單一真理的哲學教科書」，傷害原則與自由原則，界線畫在哪而不是無限制自由；基礎是效益主義不是自然權利，三個理由與「生活實驗」；冒犯不等於傷害；思想與言論自由的論證（被壓制的意見可能為真、部分為真、真理不經挑戰會變成死教條）；章末 Warburton 列的批評（傷害的界定、效益主義基礎的張力）照書寫。
   避開 utility-and-its-limits 的救生艇案與高低快樂（related 連過去）；避開 common-good-politics 與 markets-and-morals 的 Sandel 論證（這頁是對造，related 連、不下裁決）。
   claim 頁；related 連 utility-and-its-limits、common-good-politics、markets-and-morals、justice-as-fairness。

3. existential `existence-precedes-essence`「存在先於本質：沙特的自由、壞信仰與人道主義」— philosophy-the-classics（docs/27-sartre-being-and-nothingness、docs/28-sartre-existentialism-and-humanism）。
   existential 分類兩頁都是卡繆，沙特只在 absurd-and-philosophical-suicide 被點名；分類名叫存在主義卻沒有存在主義的定義頁。
   只寫：現象學方法，自為存在與自在存在，虛無與咖啡館裡缺席的 Pierre，自由意志與事實性，壞信仰的定義與約會中的女人、咖啡館侍者（27）；「存在先於本質」的三層意思與折疊刀的比喻，人道主義在沙特的用法，對「絕望的寂靜主義」等批評的回應（28）；兩章末 Warburton 的批評照書寫。
   避開 absurd-and-philosophical-suicide 與 revolt-freedom-passion 的卡繆（荒謬與反抗不重講，related 連過去讓兩造並列）；避開 eastern 分類 no-ceo-modular-mind 對自我的另一套講法。
   claim 頁；related 連 absurd-and-philosophical-suicide、revolt-freedom-passion、having-vs-being、productive-love。

##### 不開（留第三鏟）

- 07-hobbes、10-locke、13-rousseau 三章可合成一頁「社會契約的三個版本」（自然狀態、自然法、公意），justice-as-fairness 已把羅爾斯寫成契約論的當代版，這頁是它的上游；排在上面三張之後。
- 11、12 休謨兩章（歸納問題、設計論證）站上沒有知識論分類承接；20 齊克果、23 尼采《道德系譜學》在 existential 與 applied 都被多頁點名但沒有自己的頁；14 康德《純粹理性批判》、30 維根斯坦、24 羅素、25 艾耶爾是知識論與語言哲學，站上沒分類。這些是選題不是體裁，不進工具。
- 06 笛卡兒已是第一鏟的解剖示範；31 孔恩 science-note 有原書頁；05 蒙田本站有 how-to-live 頁；01、02、32 原書已挖。

##### 小結

- 開 3 張，全部 claim 頁；起草順序 1 → 3 → 2。
- 建議 EXCLUDED_KINDS 收這本（理由見上），同時在 ENRICH-BACKLOG 記下：排除是排榜，不是禁止選題。

#### 六站總結

- 開 12 張（keller 3、stott 2、spiritual-formation 2、lewis 2、philosophy 3），全部 claim 頁，沒有 debate：七本都是單一作者的書，站上沒有「一個問題多本書吵、兩造都有頁」的形狀。
- 不開 1 本（《紅書》）；兩本建議進 EXCLUDED_KINDS：jung-red-book-readers-edition「幻象記錄，章節是幻象序列與評註」、philosophy-the-classics「逐本導讀，三十二章各講一部原典，按書查閱」。
- 既有頁漏掛 anchor 一筆：stott between-two-worlds 補 08/04。
- 姊妹站分工：《追隨基督》第 4 部歸 spiritual-formation、登山寶訓歸 theology；《返璞歸真》第三卷與第四卷 07 到 09 歸 lewis、第四卷其餘歸 theology；《當代講道藝術》全歸 stott。
- 沒把握的：philosophy 三張是從導讀書開內容頁，與站的既有做法（挖原書）不同，但導覽自己說還沒取內容；若嫌多，先砍第 2 張（彌爾）保留康德與沙特。keller 第 3 張（復活的相遇）與第一鏟同書同主題，起草者若判敘事重述過半，退成第一鏟加一條 details。
- 起草順序建議：keller 2、stott 1、spiritual-formation 1（材料最獨立）→ lewis 2、philosophy 1 → keller 1、spiritual-formation 2、lewis 1 → stott 2、philosophy 3、2 → keller 3。

#### 華文作者線與 history 第二鏟選題單（fengtang／wan-weigang／science／liurun／history，DEEPEN-TARGETS 9 筆，Fable 開單 2026-11-12）

判準取自 note-check §1.3 與 §1.4：只為脊梁書開頁、主張標得到章節 anchor、與既有頁重疊低於一半、能被單獨引用；體裁先判。三位華文作者的書多是專欄或講稿結集，每本先問「有沒有一組相鄰章撐得起單一主張」：撐得起的照 wujun-note 上一批的做法開「一組相鄰章撐一頁」，撐不起的不開；逐篇獨立、全書無論證主軸的才進體裁排除。
章節目錄全部 `[ -d ]` 驗過；單上的原話都回書 repo grep 過，查不到的改寫成「書裡講到」。

##### fengtang-note（2 本：開 3 張、不開 1 本）

《勝者心法》是四十六個案例、五部各有主題的案例庫（秩序、業績至上、順勢與新事物、君臣與危機、戰略篤定與風投），第一鏟只用了序與兩章；《穩贏》是六十九篇中年隨筆，第一鏟已把三力框架與價值底盤寫完。

1. success-method `order-before-strategy`「制度先於戰略：禮分名、觀人五原則與才勝於德」— fengtang-winner-method（docs/part-1-zhou-chronicle-one/ch01-three-families-divide-jin-order-matters-most、docs/part-1-zhou-chronicle-one/ch04-lord-wen-selects-minister-five-principles、docs/part-1-zhou-chronicle-one/ch02-death-of-zhi-bo-avoid-wanting-everything、docs/part-1-zhou-chronicle-one/ch06-virtue-over-terrain-conquer-human-weakness）。
   第一鏟（zizhi-tongjian-lessons）掛序、ch14 徙木立信、ch42 紙上談兵，寫的是讀通鑑的四個理由、三步讀法、信任工程、企業文化、業績是用人金標準；第一部「秩序」十章一字未用。
   只寫第一部：司馬光為什麼把三家分晉放開篇（「臣聞天子之職莫大於禮，禮莫大於分，分莫大於名」，馮唐譯成管理制度、匯報線、職位待遇；「初創企業 CEO 的核心一件事：建立管理制度」，大忌是因人因事破壞制度）；魏文侯選相的「決定性瞬間」與李克觀人五原則（居視其所親、富視其所與、達視其所舉、窮視其所不為、貧視其所不取）；智伯「才勝於德」與馮唐拆「仁」為讓、厚、平三字、趙簡子看無恤的跟隨能力；吳起「在德不在險」與「舟中之人皆敵國」、領導自誇時三類庸俗回答、「在關鍵點上打深一層」。
   避開第一鏟的徙木立信、企業文化定義、業績金標準（ch08「業績至上」與第一鏟同主張，不掛）、紙上談兵；避開 chengshi-discipline 的曾國藩修煉與 no-fire-on-arrival 的漢初守成；business-strategy-note 與 leadership-note 的選人頁不對照，只在 seeAlso 連 management 站 `org-people/first-who-then-what`（起草前 `ls` 驗）。
   claim 頁；related 連 zizhi-tongjian-lessons、chengshi-discipline、no-fire-on-arrival、good-habits。

2. management `decide-without-consensus`「不與眾謀：變法、戰略與新事物為什麼不靠共識」— fengtang-winner-method（docs/part-2-zhou-chronicle-two/ch12-shang-yang-vs-ganlong-do-not-consult-crowds、docs/part-3-zhou-chronicle-three/ch27-yan-king-abdicates-only-one-final-decider、docs/part-5-zhou-chronicle-five/ch44-zishun-advises-wei-strategy-not-by-consensus、docs/part-3-zhou-chronicle-three/ch32-hufu-cavalry-responding-to-new-things）。
   第一鏟沒碰這四章；四章分在三部，共用同一條主張，書裡 ch32 自己點明「這呼應商鞅『不與眾謀』的原則」。
   只寫：奇才空降怎麼開局（位置不必顯赫但要重要、直接向一把手匯報、「經驗主義」是空降最大的陷阱）、重大變革前八個必須先想清楚的問題、商鞅對甘龍的辯論（ch12）；燕王噲禪讓子之為什麼變成鬧劇、子之奪權三步、「只能有一個最終決策者」（ch27）；子順諫魏的兩層無奈（「真理、正確的戰略只掌握在極少數人的手上」、弱者無戰略）與「燕雀處屋」、路徑依賴（ch44）；趙武靈王十四歲臨危受命、胡服騎射「愚者所笑，賢者察焉」、「這事我定了」、騎兵是戰爭史的一大步（ch32）。
   避開第一鏟的徙木立信（ch14 不掛，商鞅只取 ch12 的辯論與入職）、避開第 1 張的制度與選人；golden-line-principle 是麥肯錫的結構化解題，不是這頁的決策論，只在 related 連；management-note 與 leadership-note 的決策頁不對照。
   claim 頁；related 連 zizhi-tongjian-lessons、order-before-strategy（第 1 張）、golden-line-principle、nine-word-motto。
   馮唐在這四章下的是「重大決策不靠民主協商」的判斷，概念頁照書寫、不替他辯護也不替他緩頰；書站概覽指出的限制（史料只往現代翻譯、不反向檢驗）留給導覽第四章。

3. management `serving-the-tiger`「伴君如伴虎：樂毅的四個關鍵、田單的攬功與保持飢餓」— fengtang-winner-method（docs/part-4-zhou-chronicle-four/ch35-leyi-attacks-qi-four-keys-of-monarch-minister、docs/part-4-zhou-chronicle-four/ch36-qi-king-doubts-tiandan-interest-conflict、docs/part-4-zhou-chronicle-four/ch37-tiandan-attacks-di-stay-hungry-to-keep-achieving）。
   第一鏟沒碰第四部；三章連講同一對君臣（燕昭王與樂毅、齊襄王與田單），主張是功成之後上下級關係怎麼維持、怎麼崩。
   只寫：樂毅圍齊三年與讒言、燕昭王設酒會斬進讒者「由是齊人服其義，諸侯畏其信」、昭王死惠王立後反間計得逞與「人最容易聽進去他想聽進去的話」、君臣關係的四個關鍵（ch35，四字照書）；田單脫貂衣讓齊襄王起殺心、穿珠人「因以為己善」的點撥、「有時候需要推功攬過，也可以適當攬功」、九個寵臣與以退為進（ch36）；田單攻狄前魯仲連「將軍攻狄，不能下也」、拂袖而去與三月不克、「坐則織蕢，立則仗鍤」對「黃金橫帶而騁乎淄、澠之間」、位高權重時「默數十個數，多問一個問題」（ch37）。
   避開第一鏟與第 1、2 張；避開 real-capability 的財務自由論；leadership-note 的 managing-up 類頁不對照。
   claim 頁；related 連 zizhi-tongjian-lessons、decide-without-consensus（第 2 張）、chengshi-discipline、self-discipline-diary。
   第三鏟候選留著：ch11、ch13、ch19（商鞅方法論與趙良的警告）、ch46 奇貨可居加 ch38、ch39（戰略篤定與以小博大；書站概覽的限制說呂不韋四要素是從極端結果回推，起草時要連他的結局一起寫）。

###### 不開（1 本）

- fengtang-stable-win《穩贏》：不開。六十九篇各 1.5 到 2.4 千字的中年隨筆，腦力、體力、心力三章是編次不是論證；第一鏟（stable-win）已掛序、ch01 sec-1、sec-13，寫完三力框架、德才配位三條紅線、為智慧而活、最優答案與滯留倫敦的演示，既有頁自己寫「體力線的養生細節不展開」。剩下的材料是瀕死經驗、母親的最後時光、十五分鐘生活圈、侘寂這類私人篇章，本站三個分類（literature-life、management、success-method）沒有一個承接養生或美學，引用測試過不了。tier 維持 spine。**建議進 EXCLUDED_KINDS**，體裁理由：「中年隨筆結集，六十九篇各自獨立，三力只是編次」；若主會話判「三力算主軸」，改進 SETTLED_BOOKS。

###### 小結

- 開 3 張，全 claim；不開 1 本。三張都出自《勝者心法》，按書的五部各取一組相鄰章，與第一鏟（序、ch14、ch42）不重疊。
- 起草順序：1（材料最乾淨、與既有頁分工最清楚）→ 2 → 3。
- 旁註：zizhi-tongjian-lessons 的 label 用英文章題（「Moving the Pole: Establishing Trust」），書站章題是中文，起草第 1 張時順手改成中文章題。

##### wan-weigang-note（2 本：開 3 張、不開 1 本）

《你有你的計劃，世界另有計劃》八部五十餘節、每節約三千字，書站概覽自判是「一組彼此獨立的工具，不是一個體系」，但各部內有成組的論證；第一鏟掛序、第二部、第四部（部層級），正文用了 02/02、02/03、04/01 到 04/03。《高手相對論》兩站各一頁已把物理骨幹與不變量世界觀寫完，見不開。

4. system `expected-value-is-not-enough`「只有期望值是不夠的：標準差、對沖與遍歷性」— wan-weigang-world-has-another-plan（docs/02-necessity-within-chance/05-standard-deviation-and-life-philosophy、docs/02-necessity-within-chance/07-the-mathematics-of-hedging-risk、docs/02-necessity-within-chance/08-why-most-investors-lose-to-the-market）。
   第一鏟掛第二部整部，正文只用 02（把一生當系統）與 03（運氣是性格）；05 到 09 的量化章一字未用，而那是書站概覽說「量化含量最高」的一組。
   只寫：十萬元貨運到非洲的 180% 對 −100%（有很多錢就是系統，只有十萬元就輸不起）、「正態分布和標準差，是這個不確定的世界裡數學家送給世人最有用的禮物」、平均值定位置、標準差定寬度（05）；兩隻股票的故事、平均利潤不變而標準差變成 0、「投資組合的標準差，總是小於所有股票標準差的加權平均值」、胡亂分散也降風險（07）；142 萬元是市場的平均回報但不是你最可能拿到的回報、最幸運的人 1.8 的 52 次方、最不幸的人只是賠光不會出現負數、四個投資者的例子（08）。
   避開第一鏟的「把一生當系統」「期望值為正就下注」（這頁從它接下去，只在點題句引一次）；避開 option-thinking 的下檔上檔與 probabilistic-decision 的灰度認知；taleb-note 的遍歷性是原典，這頁只寫萬維鋼的算術，seeAlso 連 taleb 站 `asymmetry-practice/ergodicity-and-ruin`（路徑實存）。06 S 曲線與 09 回歸平均不掛，見第三鏟候選。
   claim 頁；related 連 wan-weigang-world-has-another-plan、option-thinking、probabilistic-decision、engineer-mindset。
   第三鏟候選：02/06 複利與真實世界的成長（「世界上沒有長期的指數級增長」、S 曲線、平台期）加 02/09 回歸平均（高爾頓的身高與「相關」的起源），合計約九千字，可成一頁「沒有長期的指數成長」。

5. system `inadequate-equilibria`「不充分均衡：街上為什麼撿不到百元鈔票，以及哪裡撿得到」— wan-weigang-world-has-another-plan（docs/04-systems-within-thinking/05-inadequate-equilibria）。
   第一鏟掛第四部整部，正文用了 01 到 03（線性對系統、上中下三策、好系統三特徵）；05 是全書最長的一章（約一萬三千字），轉述尤德考斯基《不充分均衡》，第一鏟沒碰。
   只寫：做大事是和市場較勁不是和自己較勁、安全氣囊與八歲小孩的質疑、「如果你認為你發現了一個別人沒發現的機會，你其實是在質疑市場的有效性」、經濟學家不撿街上的百元鈔票、「與其糾結於自己『有沒有資格』，不如分析這個市場的有效性」、有效市場的四個特點與股市、「你只不過是被市場選擇而已」、北京房市為什麼不是有效市場（有正確預測卻無法獲利）、低垂的果實（妻子的季節性情感障礙、六百美元一百三十個 LED）與這一章後半講的機會分布。
   避開第一鏟的系統三特徵與三策；避開 elite-vs-common-sense 的見識論；investing-note 的效率市場頁是另一造的主場，只 seeAlso 連 investing 站 `index-passive/efficient-market-and-random-walk` 與 `index-passive/can-the-market-be-beaten`（路徑實存），不重講。
   claim 頁；related 連 wan-weigang-world-has-another-plan、expected-value-is-not-enough（第 4 張）、option-thinking、elite-vs-common-sense。

6. thinking `life-as-information`「一個基於信息論的人生觀：人生就是要活一個選擇權」— wan-weigang-world-has-another-plan（docs/01-the-mindset-of-masters/04-a-view-of-life-based-on-information-theory）。
   第一鏟沒碰第一部；這一章六千三百字，是第一部最厚的一章，書站概覽稱它「一整節以香農的資訊論建立的人生觀」。
   只寫：兩條消息哪條信息量大（石黑一雄那句可壓縮、亂碼不可壓縮）、「一個東西信息量的大小，取決於它克服了多少不確定性」、信息熵與字符集（中文為什麼更高效）、韋弗「最重要的不是你說了什麼，而是你能說什麼」與空話套話的 CEO、「人生就是要活一個『選擇權』」、完全按劇本執行任務貢獻了什麼信息、人生的矛盾（既要不可預測才有創造性，又要可預測才能合作）、最值得做的兩種事（出乎別人意料的事、增加自己選項的事）。
   避開 option-thinking 的期權結構（「增加選項」在這頁是資訊論的推論，不是賠率結構，起草時寫清楚差別、related 連過去）；避開 intellectual-honesty 與 wan-weigang-scientific-thinker；science-note 若有資訊論頁再 seeAlso，起草前 `grep -rl 香農 ../science-note/src/content/concepts`。
   claim 頁，importance 3；related 連 wan-weigang-world-has-another-plan、option-thinking、engineer-mindset、reasoning-with-world。
   **裁決（主會話）**：不開。單章、與系統線關係最鬆，人物站一本書兩頁夠；留第三鏟候選。
   三張裡最可砍的一張：單章撐一頁，材料夠，但它與系統線的關係最鬆。

###### 不開（1 本）

- wan-weigang-what-is-relativity《高手相對論》（wan-weigang-note）：不開。十四章五十六節、每節四百到一千字，全書約四萬字，DEEPEN-TARGETS 算的 60 章是小節目錄，不是大部頭；本站 relativity-for-masters 掛 13、09、10，取的是「坐標系相對、不變量絕對」的世界觀，剩下的物理骨幹歸 science-note。tier 維持 spine；進 SETTLED_BOOKS，理由「小節目錄撐高的章節數，兩站兩頁已覆蓋世界觀與物理骨幹」。

###### 小結

- 開 3 張，全 claim：都出自《你有你的計劃，世界另有計劃》，分落第二部量化章、第四部最長的一章、第一部最厚的一章，與第一鏟用到的 02/02、02/03、04/01 到 04/03 不重疊。
- 起草順序：5（單章最厚、邊界最乾淨）→ 4 → 6。
- 書的 related 寫法：既有頁 related 是單行陣列，照站上格式。

##### science-note（1 本：不開，補 anchor）

- wan-weigang-what-is-relativity《高手相對論》：不開。relativity-of-simultaneity 一頁已寫光速不變、同時性、時間膨脹與長度收縮、光錐、廣義相對論、GPS，物理骨幹全在；剩下的雙生子計算（05/02 加 14 附錄，約三千字）、質能等價（07）、黑洞與紅移（11）、愛因斯坦的心願與楊振寧的三個原因（12）各不足以成頁，世界觀那一面歸 wan-weigang-note。tier 維持 spine；進 SETTLED_BOOKS。
- **既有頁漏掛 anchor（事實在哪章就掛哪章）**：relativity-of-simultaneity 只掛 01、02，正文用到 04-exciting-1905（時間膨脹）、06-now-is-an-illusion（同時性、光錐）、08-incredible-coincidence 與 09-beauty-of-large-scale（等效原理、重力是幾何）、11-poetry-on-black-hole-edge/02-gravitational-redshift（GPS 校正）。五個目錄都 `[ -d ]` 驗過，補掛章層。

##### liurun-note（2 本：開 7 張）

兩本都是體系書不是專欄結集：《關鍵躍升》是「心法加四種劍法角色」的乘法公式，第一鏟只開心法；《商業簡史》是用網路密度重寫商業史的單一透鏡，第一鏟只用第一部三章。導覽第三章自己寫「《商業簡史》七章只開交易成本一角，《關鍵躍升》五章只開心法，其餘還沒寫到」。

7. management `four-engines-of-motivation`「鼓手：員工不能自燃，人心的四台發動機與獎賞三原則」— liurun-key-leap（docs/02-motivation、docs/02-motivation/01-people-dont-try-because-their-engine-was-never-lit、docs/02-motivation/03-reward-hang-the-carrot-on-the-result-not-on-your-hand、docs/02-motivation/05-responsibility-this-is-my-own-business）。
   第一鏟（four-leaps-of-a-new-manager）掛導論、01 心態部、01/01 責任躍升；第二部動力六章一字未用。
   只寫：2001 年那位年輕經理的困擾與「連續三天買冰淇淋」、「員工往往不能自燃」、威廉・詹姆斯「被激發了動力的人，可以發揮出他能力的 80%～90%」、為什麼漲工資與換人都行不通（工資買到的是時間）、四台發動機（名稱與各自的點火法照 02/01）；5000 元獎金怎麼分、「成為『明君』是妄想」、尋賞與「把權力關在籠子裡」、三個獎賞原則（按大家認可的規則而不是經理的價值觀、規則在努力開始之前就定好、獎勵個人貢獻而不是共同結果）（02/03）；「這是我自己的事」的責任發動機（02/05）。
   避開 incentive-design 的五層需求、雙因素、期望理論、X-Y 理論（那頁是《5 分鐘商學院 管理篇》的激勵理論，這頁只寫劉潤在這本書裡自己的發動機與原則，related 連過去）；避開 results-through-others 的「激勵因素對保健因素」一條；02/02 憤怒與恐懼、02/04 跨代、02/06 意義只各一句帶到。
   claim 頁；related 連 four-leaps-of-a-new-manager、incentive-design、results-through-others、coach-train-reassign-replace（第 8 張）。

8. management `coach-train-reassign-replace`「教練：訓練、調崗與替換，用對人重於培養人」— liurun-key-leap（docs/03-capability、docs/03-capability/01-coaching-training-the-team-for-tomorrow、docs/03-capability/02-learning-by-doing-from-using-strengths-to-growing-people、docs/03-capability/05-reassignment-dont-grind-an-iron-rod-into-a-needle、docs/03-capability/06-replacement-teach-a-turkey-to-climb-or-hire-a-squirrel）。
   第三部能力六章第一鏟沒碰。
   只寫：教練的三件事（訓練、調崗、替換）與「今天用今天的他們，明天用明天的他們」、「辭職吧」的建議與「犯錯、解決、改進、成長」、允許犯錯是教練的修養（03/02）；「用對人重於培養人」、鐵杵不要磨成針（03/05）；「換掉他就沒人可用」的答案在問題之前、選擇權的定義、流失率的基本常識、替換是經理的「成人禮」（03/06）；03/03 教不是罵與 03/04 訓練各取一句。
   避開第一鏟的四個躍升；避開 knowledge-to-skill（那是個人把知識煉成技能）；management-note 與 hr-note 的用人頁不對照，seeAlso 可連 management 站 `org-people/first-who-then-what`（起草前 `ls` 驗）。
   claim 頁；related 連 four-leaps-of-a-new-manager、four-engines-of-motivation（第 7 張）、results-through-others、knowledge-to-skill。

9. management `ninety-percent-communication`「政委：九成時間在溝通，想明白、說清楚、能接受」— liurun-key-leap（docs/04-communication、docs/04-communication/01-communication-exists-to-reduce-information-asymmetry、docs/04-communication/02-think-it-through-why-what-and-how、docs/04-communication/04-the-seven-weapons-of-communication、docs/04-communication/05-process-policy-and-values-communication-across-time、docs/04-communication/06-acceptance-avoiding-outward-compliance）。
   第四部溝通六章第一鏟沒碰；第一鏟的「溝通躍升」只寫到「用別人的腦」一句。
   只寫：「只表揚不批評」引發的勞動仲裁、從「兵頭」變成「將尾」、「職場研究如何向上溝通，管理研究如何向下溝通」、「心委屈了」（04/01）；想明白的 why、what、how（04/02）；七種武器（一對一、即時溝通的「面談＞打電話＞企業微信」排序、走動管理、例會、看板、週報等，名稱照書）（04/04）；流程、制度與價值觀是與未來的員工溝通（04/05）；能接受與避免表面服從（04/06）。
   避開 org-tools（MECE、SWOT、SMART、OKR、PDCA 是另一套工具箱，不是溝通工具）；避開 communication-note 的溝通通論；pyramid-expression 在 fengtang 站不在本站。04/03 聽說寫畫只一句帶到。
   claim 頁；related 連 four-leaps-of-a-new-manager、org-tools、four-engines-of-motivation（第 7 張）、closed-loops-and-delegation（第 10 張）。
   **裁決（主會話）**：不開，留第三鏟。人物站一書多頁要省著開，《關鍵躍升》先開鼓手與教練兩張（與既有頁分工最清楚、材料最厚），溝通與協作等前兩張落地再看。

10. management `closed-loops-and-delegation`「指揮：凡事有交代、改進靠循環、格局靠授權」— liurun-key-leap（docs/05-collaboration、docs/05-collaboration/01-execution-rests-on-closed-loops、docs/05-collaboration/02-improvement-rests-on-cycles、docs/05-collaboration/03-growth-rests-on-planning、docs/05-collaboration/05-scope-rests-on-delegation）。
    第五部協作六章第一鏟沒碰。
    只寫：「不了了之」是最危險的小事、羅振宇「凡事有交代、件件有著落、事事有回音」、「一件事有了始，就一定要有終」、閉環像 4×100 接力必須交棒（05/01）；改進靠循環（05/02）；三年規劃與一年三件事（05/03）；「你放著，我來」為什麼走不遠、「格局，就是你能管多少人、做多大事」、授權分級（級數與名稱照 05/05，書站概覽說五級）、替下面的管理者承擔責任會導致「懶政」（05/05）。
    避開 results-through-others 的「授權要權責利對等並保留檢查點」（那是《5 分鐘商學院》的版本，這頁只寫劉潤在這本書裡的分級與格局論，related 連過去）；避開 org-tools 的 PDCA 與復盤（05/02 的循環若與 PDCA 同一套，只引一次、不重講）；05/04 文化（鼓勵白、壓縮灰、禁止黑）與 05/06 流程各一句。
    claim 頁；related 連 four-leaps-of-a-new-manager、results-through-others、org-tools、ninety-percent-communication（第 9 張）。
    **裁決（主會話）**：不開，留第三鏟（理由同第 9 張）。

11. business-logic `connection-is-the-engine`「連接是結構改變的引擎：鐵路、公路、貨櫃與電報」— liurun-evolution-of-business（docs/02-connection-is-the-engine-of-structural-change、docs/02-connection-is-the-engine-of-structural-change/01-railways-sears-and-the-mail-order-catalog、docs/02-connection-is-the-engine-of-structural-change/02-highways-walmart-in-a-small-town、docs/02-connection-is-the-engine-of-structural-change/03-shipping-the-container-changes-the-world、docs/02-connection-is-the-engine-of-structural-change/04-telegraph-the-first-information-superhighway）。
    第一鏟（transaction-cost）掛 01/01 到 01/03，寫交易的本質、兩個敵人、商業進化是降低交易成本；第二部「連接」六章沒碰。
    只寫：商業進步的推動力是連接（物理連接造成空間的折疊、虛擬連接造成時間的壓縮，措辭照 02 部首）；「鐵路，就是當時的網際網路」、美國六十年年均六千多公里、1916 年 408,745 公里占世界 39%、西爾斯從鐵路工人看到郵購手冊、「你這個吸血鬼，正在摧毀實體經濟！」（02/01）；公路與小鎮的沃爾瑪（02/02）；一個卡車司機的疑問、貨櫃讓運輸成本降一個數量級（02/03）；電報是第一條信息高速公路（02/04）；02/05、02/06 網際網路與萬物互聯各一句。
    避開第一鏟的交易成本定義與七項交易成本；避開 internet-five-laws 的五大定律（網際網路那段只接到「連接」這條線）；economics-note 的 globalization 頁若講貨櫃，seeAlso 連過去（起草前 `grep -rl 貨櫃 ../economics-note/src/content/concepts`）。
    claim 頁；related 連 transaction-cost、network-density（第 12 張）、internet-five-laws、trend-dividend。

12. business-logic `network-density`「網路密度：線段型、中心型、去中心型，商業為什麼先長出超級節點再消滅它」— liurun-evolution-of-business（docs/03-linear-commerce-the-first-evolution/01-network-density-and-business-evolution、docs/04-centralized-commerce-the-jurassic-era/01-what-is-centralized-commerce、docs/05-decentralized-commerce-what-is-long-united-must-divide/01-what-is-decentralized-commerce、docs/06-fully-connected-commerce-the-utopia/01-network-density-one-hundred-percent-transaction-cost-zero）。
    第三到六部第一鏟沒碰；這是書的主線（書站概覽：「密度增加會帶來超級節點，而密度進一步增加會消滅超級節點」）。
    只寫：「網路密度＝實際連接數 ÷ 可能連接數」、十七個節點最多 136 條連接、「商業原始社會：網路密度＝ 0，交易成本＝ ∞」、小農經濟 5.1%、線段型商業是商人首次出現（03/01）；從十字路口到米字路口、羅馬八萬公里道路與武漢九省通衢、超級節點的價值是交易中心不是交通樞紐、夫妻老婆店是社區級中心（04/01）；「副中心愈來愈多、超級節點愈來愈不重要的過程，就是『去中心化』」、區塊鏈的家族自述（父親去中心化、母親互聯網、三個哥哥）（05/01）；網路密度 100%、交易成本為零的理論極限（06/01）。
    避開第一鏟與第 11 張；避開 internet-five-laws 的網絡效應（那是用戶間的價值，這頁的密度是交易節點間的連接，起草時寫清楚差別）；business-strategy-note 的 `competitive-strategy/network-effects` seeAlso 連過去（路徑實存）。03/02、03/03、04/02、04/03、05/02、05/03 講各型怎麼解資訊不對稱與信用不傳遞，留第三鏟。
    claim 頁；related 連 transaction-cost、connection-is-the-engine（第 11 張）、internet-five-laws、bottom-logic-formula。

13. business-logic `moats-keep-dividends`「護城河把紅利守成利潤：無形資產、成本優勢、網路效應、遷移成本」— liurun-evolution-of-business（docs/07-how-do-we-ride-the-trend/01-what-is-real-profit、docs/07-how-do-we-ride-the-trend/02-how-to-turn-right-and-earn-profit）。
    第七部第一鏟沒碰；07/02 是全書第二厚的一章（約九千字）。
    只寫：「紅利，就是短暫的供需失衡」、沙灘賣可樂的狗蛋與小虎、「你以為是在創業，其實是在為這個社會打工」、紅利、利潤、工資三者的分別（07/01）；護城河是什麼、四類各兩種（無形資產的許可與品牌、成本優勢的規模與管理、網路效應的單邊與多邊、遷移成本的習慣與資產，名稱照書）、荷蘭東印度公司的許可、品牌是「了解、信任、偏好」（07/02）。
    避開 trend-dividend（那頁是《進化的力量》的紅利生命週期與流量三次打通，這頁只取 07/01「紅利是短暫供需失衡」一句當起點，不重講窪地、平地、高地）；避開 internet-five-laws 的網絡效應本體（這頁只寫它作為護城河的一種）；business-strategy-note 的 `competitive-strategy/seven-powers`（Helmer 七大力量）是同題的另一本書，seeAlso 連過去不並排。07/03 寫自己的商業未來史不掛。
    claim 頁；related 連 trend-dividend、transaction-cost、internet-five-laws、embrace-uncertainty。

###### 小結

- 開 7 張，全 claim：《關鍵躍升》4（四種劍法角色各一頁，對應書的乘法公式四項）、《商業簡史》3（連接、網路密度、護城河）。沒有 debate：兩本都是劉潤的體系書。
- 七張偏多；要壓量先砍第 9、10 張（溝通與協作可以等第三鏟，鼓手與教練和既有頁分工最清楚、材料最厚），再砍第 11 張（連接那部可併進第 12 張當背景）。
- 起草順序：8、7（個體面兩章，與 incentive-design 的邊界要先讀既有頁）→ 12、13 → 11 → 9、10。
- 既有頁分工：incentive-design、org-tools、results-through-others 三頁都出自《5 分鐘商學院》，這七張只寫《關鍵躍升》與《商業簡史》自己的說法，重疊處引一次、related 連過去。

##### history-note（2 本：開 2 張）

兩本都是文化史，站上各一頁。《文學的 40 堂公開課》四十堂各自獨立，但書站概覽點出它與布倫《西方正典》相反的地方：「花了同樣多的篇幅在機制上」，版權、禁書、暢銷榜與文學獎各有專章，這條機制線是第一鏟（史詩與國族）沒碰的。《餐桌儀式》第一鏟是「馴化暴力」的主張，第三部主客關係是另一條線。

14. culture-society `literature-as-an-industry`「文學的生產線：版權、禁書、暢銷榜與文學獎」— little-history-of-literature（docs/11-who-owns-literature、docs/25-dangerous-books、docs/38-guilty-pleasures、docs/39-whos-best、docs/40-literature-in-your-lifetime）。
    第一鏟（epic-and-nation）掛 03、10、26，寫史詩、國族與帝國；機制那條線一堂沒用。
    只寫：一本書的三種擁有者（作者擁有文字、出版社擁有版本、讀者擁有副本）、從卷軸到 codex、版權怎麼出現（11）；當權者為什麼怕書、柏拉圖把詩人趕出理想國、米爾頓「殺一個好人，幾乎等於殺一本好書」、1857 年兩場審判（25）；文學是一座爬不完的山（大英圖書館近兩百萬冊對一生約六百部）、斯特金「百分之九十的東西都是垃圾」、出版商「低」養「高」、暢銷榜是引擎（38）；文學獎的時代與「聖誕派對禮物」、評判標準從不太具體、獎項興盛的四個原因（39）；印刷書五百年可能到頭、「太多」的問題與兩種讀者策略（40）。
    避開 epic-and-nation 的全部；避開 consumption-history 的消費史本體（暢銷榜那段只在 related 連過去）；writing-note 的出版與投稿頁若有，seeAlso 連（起草前 `ls ../writing-note/src/content/concepts/`）。22 桂冠詩人、17 童書的興起各一句帶到，不掛。
    claim 頁；related 連 epic-and-nation、consumption-history、crowd-and-power、bobos-new-elite。

15. culture-society `hosts-and-guests`「主與客原是同一個字：款待的風險、回禮與門檻」— rituals-of-dinner（docs/03-pleasure-of-your-company、docs/03-pleasure-of-your-company/01-company、docs/03-pleasure-of-your-company/02-hosts-and-guests、docs/03-pleasure-of-your-company/03-invitations、docs/03-pleasure-of-your-company/04-coming-right-in）。
    第一鏟（table-manners-as-order）掛 01、02 兩部，寫共食的規矩、刀的去武器化、為謙卑而戰、閉嘴、好客維繫社群；第三部「有您作伴」五章只用了 05 座位那一章的材料（而且沒掛，見旁註）。
    只寫：晚宴居所有款待之首、回禮把客人變成下一個主人、pot luck 的演變、一起吃飯能化解戰鬥、共食讓人吃得更多與中華餐桌的設計（03/01）；一份高風險的款待、「主」與「客」原是同一個字、款待之律建基於兩面性「雙方都握有力量」、客人是有可能變成神的陌生人、對主人的最大罪是謀殺賓客、《奧德賽》裡阿伽門農「在餵飽我之後」被殺（03/02）；賓客名單的政治學、推掉邀請的兩難、invite 的詞源弔詭、賓客人數的迷信（03/03）；跨越門檻的儀式、去除武裝（脫鞋、卸帽、洗腳）、帶禮物可消耗不可逾矩、花的語言、客人不可坐得高於主人、為什麼要為晚宴穿衣（03/04）。
    避開第一鏟的食人禁忌、刀、謙卑之戰、閉嘴；03/05 座位歸第一鏟（補 anchor 後），這頁不寫入座；避開 sacred-and-profane-space 的伊利亞德。
    claim 頁；related 連 table-manners-as-order、sacred-and-profane-space、consumption-history、crowd-and-power。
    **既有頁漏掛 anchor（事實在哪章就掛哪章）**：table-manners-as-order 正文的黎胥留磨圓刀尖出自 04-dinner-is-served/06-knives-forks-spoons、Tafaddal 與「恭敬不如從命」出自 03-pleasure-of-your-company/05-taking-our-places、波斯特 1931 年「食物入口就得吞下」出自 05-no-offence/02-rules-of-the-mouth；現掛的 01、02 兩部都不含這三處，起草第 15 張時一併補掛三章（三個目錄都 `[ -d ]` 驗過）。
    第三鏟候選：02-learning-to-behave/02-inhibitions（維瑟對伊里亞思：「我們進步了」是一個討喜的神話、禮儀改變過但極為緩慢、伊拉斯謨是唯一的天才，約五千六百字）。站上沒有伊里亞思《文明的進程》（bibliography 只有卡內提），所以不是 debate 形狀，是維瑟單方的翻案頁；材料夠一頁，這輪先不開。

###### 小結

- 開 2 張，全 claim；不開 0 本，tier 不動。
- 《文學的 40 堂公開課》不進 EXCLUDED_KINDS：四十堂各自獨立，但時序與機制兩條主軸都在，條目可成組。開完第 14 張後它被兩頁引用，自然離榜。
- 起草順序：15 → 14。

##### 五站總結

- 開 15 張（fengtang 3、wan-weigang 3、liurun 7、history 2），全部 claim 頁；不開 3 筆（穩贏；高手相對論在 wan-weigang 與 science 各一筆），tier 都不動。
- 體裁排除建議 1 本：《穩贏》（中年隨筆結集）；SETTLED_BOOKS 2 筆：《高手相對論》在兩站（小節目錄撐高的章節數）。
- 既有頁漏掛 anchor 2 筆：science relativity-of-simultaneity 補 04、06、08、09、11/02；history table-manners-as-order 補 04/06、03/05、05/02。順手：fengtang zizhi-tongjian-lessons 的英文 label 改中文章題。
- 沒把握的：liurun 七張的量（砍法寫在小結）；wan-weigang 第 6 張（與系統線關係最鬆，可砍）；fengtang 第 3 張把三章三個教訓收成「功成之後的上下級關係」一個主張，起草代理若覺得散，改只寫 ch35、ch36。
- 第三鏟候選：勝者心法的商鞅方法論與呂不韋、世界另有計劃的 S 曲線與回歸平均、商業簡史各型怎麼解兩個敵人、餐桌儀式的維瑟對伊里亞思。

### 2026-11-12 第二鏟第三批（Fable 開單；起草交 Opus）— 七組 fork 讀 82 本候選 → **開 80 頁、不開 20 本、改判 2 本、B 型債 2 筆、工具三改**

**起點**：80 個 repo 全同步；galaxy-checkup blocker 0／warn 0／nit 18（data-science 17＋hr 1 等書）；tier-audit 違規 0；GUIDE-DRIFT、孤兒書、強 seeAlso 缺口、SOURCING-DEBT 全 0。DEEPEN-TARGETS 102 本候選（45 站），本輪取 82 本，留 20 本給下一輪（信仰線 keller／stott／spiritual-formation／lewis／jung／philosophy 7 本、華文作者線 fengtang／wan-weigang／liurun／history 9 本、data-science 2 本等書、五大障礙與活的教會上輪已裁定）。
**順手**：hbr 導覽第四章爭點一（上輪 Opus 改寫）Fable 抽查：五句引文全部回原書 grep 到，語氣與全章一致；只有「不要叫它回饋」是帶引號的轉述，改成書的措辭「不要稱之為『回饋』」（hbr-note `c476b28`）。

**開單方式**：承上一批，七個 Fable fork 平行讀原文（書 repo 目錄與章首、第一鏟頁整頁、導覽三／四／五章該段、姊妹站 bibliography 與頁），每張單寫明落點分類、slug、中立標題、骨幹書與章節目錄（全部 `[ -d ]` 驗過）、第一鏟掛了什麼、只寫什麼、避開什麼、related（`ls` 驗過）。主會話逐張審形狀（§1.4 四個測試）、重疊、材料厚度，並抽 grep 單上的原話與數字：**七組共抽 96 筆、命中 95 筆**，漏的一筆是 fork 自己數的「八頂帽子」（已在單上註明，起草時回章節數）。

| 組 | 站 | 候選 | 開 | 不開 |
| --- | --- | ---: | ---: | ---: |
| 技術 | system-design 5、clean-code 1、design-patterns 2、agile 2、data-systems 2、security 1 | 12 | 13 | 2 |
| 金錢 | economics 5、personal-finance 3、investing 1、kiyosaki 1 | 9 | 10 | 1 |
| 人與領導 | relationships 4、maxwell 3、business-strategy 2、leadership 1、communication 1、covey 2、growth 1 | 15 | 14 | 3 |
| 職場 | hbr 3、career 5、hr 2 | 10 | 10 | 4 |
| 身心習慣 | wellness 6、habits 2、tools 2 | 11 | 10 | 4 |
| 思考創業寫作 | writing 4、thinking 2、startup 1、templar 1 | 11 | 8 | 4 |
| travel | podcast 3、travel-video 3、tour-leading 1、tour-design 1、destinations 7 | 14 | 15 | 2 |
| **合計** | 33 站 | **82** | **80** | **20** |

全部 `kind: claim`，沒有 debate：82 本都是單一作者的體系書、敘事史或合輯，站上沒有「一個問題多本書吵、兩造都有頁」的形狀。三個 debate 候選等兩造落地再開單：clean-code「盡早崩潰」（第 6 張）對「把錯誤定義掉」、wellness「算熱量」（第 3 張）對「算醣」（nutrition-foundations 重寫後）再加 Ferriss 第三造、travel 爭點四 Abbey 對 Holloway（第 8 張落地後導覽第四章改寫，Fable）。

**主會話裁決（與 fork 原單不同處，單上都加了「裁決（主會話）」行）**
- War of Art 第三部撞題（habits 與 writing 兩個 fork 都要）：拆成兩面——habits 拿 06–11 身分論（`discipline/territory-versus-hierarchy`），writing 改開 `craft-mindset/invoking-the-muse` 拿 01–05 工作面；writing fork 原單作廢。
- 三張不開：startup `delegate-dont-abdicate`（四章不到四千字，改成 purpose-over-money 補一條 details 並掛那四章）、habits `procrastination-and-overload`（技巧清單體，兩招是 Eyal 轉述、原典頁已在）、travel `hotel-grading-and-group-business`（教科書章節，引用測試弱，留第三鏟）。
- 改判層 2 本：business-strategy `essential-drucker` spine → **tool**（drucker、leadership 判 tool，management 判 support，本站導覽自己說「當總目錄讀」）；communication `speed-of-trust` spine → **delegated:covey**（covey 八頁已挖完四部）。走 `apply-tiers.py`，跑 `tier-audit.py` 兩站必 0。
- 分類歸屬：travel `one-transcript-many-outputs` 落 podcast（書是 podcast 書、飛輪從 podcast 起）；growth `intuition-as-higher-reason` 留 growth 不改 delegated（導覽三角分工：growth 取心態與潛能）。
- 體裁排除 5 本進 `export-deepen-targets.py` EXCLUDED_KINDS（見工具三改）；其餘不開的 15 本是選題判斷，進新的「已裁定」清單，不進體裁排除。

**B 型債 2 筆（主會話回書 repo grep 確認過，起草前先清）**
- wellness `nutrition-sleep/nutrition-foundations`：掛江部《間歇性斷食減醣全書》02、03 章，頁上核心主張「能量平衡決定體重」「斷食減醣有效是因為減少總攝取」「蛋白質最該顧好」「依從性是隱藏變數」在江部書裡 grep 不到，江部講的相反（「和卡路里苦行說再見」「重點不是熱量，而是有沒有醣」）。這些是 Matthews（Bigger Leaner Stronger）的主張掛錯書。處理：第 3 張 `flexible-dieting` 寫成 Matthews 的頁；nutrition-foundations 回江部原文重寫成減醣的理由並改標題；導覽第四章官司一那兩句改成 Matthews 的話連到新頁；校正表進 SOURCING-DEBT。
- hbr `strategy-innovation/everyday-strategic-thinking`：core 第五點（事前驗屍、指定唱反調者、可逆／不可逆）、TIP「本週說了哪些 No」、「策略絞肉機」「兩分鐘內講清楚」、整節「四個斷點」在書 repo 全書 grep 不到。處理見第 3 張 `strategy-execution-gap` 附帶條件：四個斷點改成一行連新頁，決策那條以 04-align-decisions 三章回源改寫；校正表進 SOURCING-DEBT。

**既有頁漏掛 anchor（事實在哪章就掛哪章；起草該站時一併做，不另開頁）**
- business-strategy `create-a-customer`：主掛改 practice-of-management 01/02-what-is-a-business，副掛 essential-drucker 01/03。
- communication `rhetoric-toolbox`：補 02/01、02/05、02/07、02/10、02/12。
- leadership `leader-leader`：Goldsmith「別加太多價值」案例補 what-got-you-here-wont-get-you-there 的章；seeAlso 加 management `org-people/competence-and-clarity`。`circle-of-safety`：正文一半是 Horowitz 與 Netflix，補那兩本書的章（兩本在本站各有頁，related 連過去）。
- startup `purpose-over-money`：補 01/04、05/01，再加 Sivers 授權 details 掛 04/04、05/03、05/05、05/06；導覽第三章 47 行說 Sivers「兩頁引用」但 `enough-as-strategy` 沒掛 anything-you-want，看內文決定補 anchor 或改導覽那句。
- writing `nuts-and-bolts`：正文用到工具 2、3、4、6、7、8，補箱層 `docs/01-nuts-and-bolts/` 或那六章。newport `career-capital-over-passion`：「先變得值得認識」若用到第 66 條，補 docs/66-dont-network。
- system-design `distributed-transactions`：補 elevator 10-coffee-shop-two-phase-commit。
- economics `mental-accounting-endowment`：補 04/03-mugs。`gold-standard-and-fetters`：補 04/05-gold-fetters、05/01-gold-standard-on-the-booze；「符合每一條已知的規則」回源，找不到就改寫。kiyosaki `b-i-triangle`：四面體與福特若出自《投資指南》03/02，補掛。
- wellness `exercise-as-leverage`：補 4-hour-body 01/01-minimum-effective-dose。habits `design-your-day`：補 01/01、06/01。
- hbr `persuasive-presentations`：補 01、02、05/02、06/01、06/04，seeAlso 連 communication `presentation/slide-design-ideology`、`presentation/slides-that-resonate`；`run-meetings-that-matter`：補 02、03、04 卷層，05/08 領導高峰會以 details 收進；`toxic-workplace`：補 01、03、04、05 卷層。career `never-eat-alone`：卷層細化到 03/01、03/02。**hbr 站整站跑一次 `export-anchor-gaps.py hbr-note`**（Guide 系列第一鏟普遍一兩個卷層 anchor、正文掃全書）。
- travel `cultural-journey-sites`：敦煌段補道士塔 details 並掛 01-taoist-pagoda；`shooting-for-the-edit` 與第 4、5 張同掛 07-working-practices，label 要分開。

**工具三改（Opus，notes-core 一個 commit）**
1. `export-deepen-targets.py` EXCLUDED_KINDS 加 5 本：`art-of-thinking-clearly`「轉譯型偏誤短文合輯，近百則互不相承」、`rework`「格言體雜文集，近九十節各一兩頁、只給立場不給流程」、`tools-of-titans`「訪談語錄合輯，一人一條目，按人物查閱」、`365-days-with-self-discipline`「日課型，365 則每日短文按週合輯」、`soft-skills-thirty-letters`「多作者書信合輯，三十封各自獨立」。docstring 把判準寫明是「**每則互不相承且全書無主軸**」，不是「條目式」本身——Rules of Management、How to Win at College 同是條目書但可成組，不排除。
2. 新增 `SETTLED_BOOKS`（(站, slug) → 日期與理由），承 `SETTLED_DEPTH_PREFIXES` 的精神但逐本列、文件另開一節「四、已裁定不開」供覆核，並從候選數扣除：上輪 management `five-dysfunctions-of-a-team`、theology `living-church`；本輪 people 3（essential-drucker、speed-of-trust、turn-the-ship-around）、思考組 3（how-to-win-at-college、anything-you-want 另有 details、millionaire-fastlane）、技術 2（test-driven-development、impact-mapping）、身心 2（how-to-have-a-good-day、life-meaning 的 bigger-leaner-stronger）、職場 3（making-every-meeting-matter、toxic-workplace、mastering-behavioral-interviews）、travel 2（how-to-be-travel-writer、istanbul）。理由抄各單「不開」那行。
3. 引用計數改成 concepts＋problems（與 `tier-audit.py` 的 `citations()` 同口徑）：design-patterns `refactoring-for-software-design-smells` 六個題型頁掛著卻顯示 0 頁。改完它離榜，但第 8 張仍開（骨架層缺口，理由在單上）。

**留給 Fable 的判斷（本輪不動）**
- Flow 第十章「意義的形成」：五站 delegated 給 tools，但 tools 沒有分類承接；是 life-meaning 的題。下一輪 life-meaning 開單時裁：改 support＋導覽帶一句，或自挖一頁 10-the-making-of-meaning 並改 spine。
- 三個 debate 候選（見上）等兩造落地。
- 下一輪選題的 20 本（見起點）。

**Opus 開工指令（Andrew 切模型後照這段做；Fable 2026-11-12 交接）**
0. 前置：`for d in ~/workspace/andrew/notes/*/; do git -C $d pull -q --ff-only; done`；讀 `docs/MODEL-ROUTING.md` §四、`/note-check` §6、本節與下面七張單。**單上的「原話」已抽驗但不是全部：起草代理每句引文仍要回章節 grep**，查不到就改寫成「書裡講到」或刪。
1. **第一波（債與工具，先做）**：兩筆 B 型債回原文重寫＋SOURCING-DEBT 校正表；工具三改＋`refresh-galaxy-docs.sh`；兩筆改判層走 `apply-tiers.py`；「既有頁漏掛 anchor」那串按站做掉（各站一個 commit）。
2. **第二波（起草 80 頁）**：每頁一個子代理、路徑 A，prompt 含 note-check §6.3 六項；骨架照該站既有 claim 頁；anchor 從單上取並逐一 `[ -d books-done/**/<book>/site/content/<anchor> ]`，**事實在哪章就掛哪章**（單上沒列但用到的章可以補掛，label 用書站章題）；不下裁決、不寫站務口吻、不用「——」。每頁交回：grep `&gt;|&lt;|&amp;`、anchor 實存、`related` 雙向（**解析後重寫單行，不 regex 插尾**）、`:::response` 留空、**五筆具名事實附逐字原文，主會話回源 grep ≥3 筆**；補分類 `_index.md` roadmap；導覽第三章講那本書的段落補一句連到新頁（保語氣；travel 第 8 張落地後爭點四不改，留 Fable）；seeAlso 只掛單上點名且 `ls` 驗過的路徑。站的順序：技術 13 → 金錢 10 → 人與領導 14 → 職場 10 → 身心習慣 10 → 思考創業寫作 8 → travel 15；站內順序照各單「起草順序建議」。有附帶條件的張（wellness 3、hbr 3、thinking 6、career 6、startup 的 details）照單上寫的做。
3. 每站收尾：`npm run build`、`npm run format`、`format:check`，蓋 `curation.enrichedAt`，`tier-audit.py <站>` 與 `galaxy-checkup.py --station <站>` 必 0 warn；overview 重數頁數；單行英文 commit、逐檔 add、**不 push**。
4. 全部完成：`refresh-galaxy-docs.sh`，`export-seealso-gaps.py --json --allow-strict` → `apply-seealso.py --apply` 補新頁帶出的 strong 缺口，在本節補一段「Opus 執行」戰報（頁數、抽驗筆數、哪幾張照書改了標題、起草代理抓到的既有頁錯誤校正表、沒寫的張與原因）。

**Opus 執行（2026-11-12，Andrew「with opus, go」）— 79 頁交付（27 站）、1 張擋下，29 個 repo 本機 commit（未 push）**
- **第一波**：兩筆改判層（business-strategy essential-drucker → tool、communication speed-of-trust → delegated:covey）手改 bibliography（`apply-tiers.py` 只碰未判層的 entry），tier-audit 兩站 0；工具三改落在 notes-core `0eedafc`（EXCLUDED_KINDS +5、SETTLED_BOOKS 15 本、計數納入 problems）。DEEPEN-TARGETS 102 → **19** 本。兩筆 B 型債與約二十筆漏掛 anchor 隨各站起草一起做，校正表在 SOURCING-DEBT「2026-11-12 第三批」。
- **第二波**：七個起草代理（每組一個、組內自己寫不再分派），每頁交 3 筆具名事實與來源檔；主會話回源 grep 抽 **52 筆、全中**。各站 build:nosearch、format:check、tier-audit、checkup 全綠。
  - 技術 12（system-design 5、data-systems 2、clean-code 1、design-patterns 2、agile 2）；金錢 10；人與領導 14；職場 10；身心習慣 10；思考創業寫作 8 頁＋2 個 details（startup 授權、thinking 後記）；travel 15。
  - **沒寫 1 張**：security-note `malware-behavior-and-covert-launching`。起草代理讀《Practical Malware Analysis》第五部時被模型安全機制中止（`[cyber]`），依規不換說法重試；留 Andrew 裁（自己寫、換模型、或判不開）。
  - **照書改標題**：maxwell「高路」→「高道」、growth「第三次轉化」→「第三次轉變」、travel「布痕瓦爾德」→「布亨瓦德」，都照書 repo 譯名；wellness nutrition-foundations 重寫後改題。
  - **單上與原文不符、照原文處理**：maxwell「八頂帽子」書裡是列了八項角色；covey 第 2 張「舊策略模型」在 02/02 不在 02/03、「七個問題對應的習慣」原文沒有；money 第 10 張「越底層越重要」原文只說使命最重要；kiyosaki `b-i-triangle` 的四面體與福特不在既有頁，不補 anchor；newport 第 66 條沒用到，不補；startup `enough-as-strategy` 沒用 Sivers，改導覽那句。
- **頁數宣稱**：起草代理在 overview 與導覽裡改了約二十處寫死的頁數，其中半數是**新頁之前就過期、但 GUIDE-DRIFT 抓不到**的（句子沒有「全站」前綴：hbr「三十一頁」、clean-code「七十七頁」、writing「四十六頁」、thinking「六十九頁」、travel「四十頁」、career「51 頁」、hr「二十一頁」）。`export-guide-drift.py` 的句型判定值得放寬（Fable 或下次體檢）。
- **收尾**：`export-seealso-gaps.py --allow-strict` → `apply-seealso.py` 補 8 筆（5 站，各一 commit）；有 seeAlso 的頁 662（28%）。`refresh-galaxy-docs.sh` 重算：checkup blocker 0／warn 0／nit 18（不變，等書）；tier-audit 全星系只剩 philosophy 2 筆已知衝突；GUIDE-DRIFT 要改 0；strong seeAlso 缺口 0；ANCHOR-GAPS 證據充分 1（travel recovering-from-mistakes，前輪已判誤報）。
- **新冒出的（留 Fable）**：ORPHAN-BOOKS **26 本孤兒書**，全是 11-06 之後新建的目的地書（Bryson、Dalrymple、Thubron、Pisani、泰國史、寮國史、越南、杜拜、加拿大鐵路⋯⋯），該歸 travel-note 認領並判層。
- **代理協作的坑**：七個代理共用 scratchpad 的 `tools/` 會互相覆寫腳本，之後每個代理給獨立子目錄；`export-guide-drift.py` 不讀參數，`--help` 也會重寫 GUIDE-DRIFT.md。


#### 技術站第二鏟選題單（system-design／clean-code／design-patterns／agile／data-systems／security，DEEPEN-TARGETS 12 本，Fable 開單 2026-11-12）

判準取自 note-check §1.3 與 §1.4：只為脊梁書開頁、主張標得到章節 anchor、與既有頁重疊低於一半、能被單獨引用。
技術站的書 repo 章節厚（多在 10–50KB），所以第二鏟一律選「一章或一組相鄰章撐得起的單一主張」；目錄型的書（API 模式目錄、重構目錄、壞味目錄）切「一組相鄰條目共同支撐的主張」，不整本重講。
姊妹站分工：kent-beck-note 是人物站，TDD 與 XP 的理論層已在那邊；uncle-bob-note 沒收這批書。七個技術站的 seeAlso 自 v0.44.0 起可連全部 79 站。
每張單的章節目錄名全部 `[ -d ]` 驗過；related 的 slug 全部 `ls` 驗過。

##### system-design-note（4 本，開 5 張）

1. fundamentals `diagram-driven-design`「圖驅動設計：承載架構的是線，不是方塊」— software-architect-elevator（docs/03-communication/04-emphasis-over-completeness/、docs/03-communication/05-diagram-driven-design/、docs/03-communication/06-drawing-the-line/、docs/03-communication/07-sketching-bank-robbers/）。
   第一鏟（architect-elevator）掛第一部 01、05，第二部 02，第三部 01、02，第四部 02、05：電梯隱喻、三條腿、賣選擇權、斜坡與海盜船、控制是幻覺、組織當分散式系統。第三部八章只用了前兩章。
   只寫第三部後半：圖是模型、五秒測試、訊噪比與「圖例是拐杖」（04）；畫圖本身是設計技術，逼你清理抽象層次、精簡到本質、表達不確定性（05）；沒有線條的圖不算架構，同一組方塊可以是分層也可以是網狀，能力圖只是把文字包進方塊（06，書的原話：「沒有線條的架構圖很可能不算架構」「把文字包在方塊裡不構成架構」）；架構素描師的兩種方法，系統隱喻與觀點，從團隊的圖看出他們的思維層次（07）。
   避開 architect-elevator 已寫的斜坡／懸崖、海盜船、logos／ethos／pathos；避開 architecture-characteristics 的適應度函數；書第二部 10-coffee-shop-two-phase-commit 不進這頁（屬 distributed-transactions 的題域，見旁註）。
   claim 頁；related 連 architect-elevator、architecture-characteristics、coupling-and-cohesion、integration-styles。

2. reliability `fault-isolation-swim-lanes`「故障隔離泳道：不共享、不跨越、交易沿著泳道流」— art-of-scalability（docs/03-architecting-scalable-solutions/02-creating-fault-isolative-architectural-structures/）。
   第一鏟（akf-scale-cube）掛第三部 03、04、05，寫的是立方體三軸與應用層／資料層的切法；泳道（swim lane）在既有頁沒出現。
   只寫這一章：故障隔離架構的術語（泳道、艙壁、分片的用語差異）、五項好處（限制衝擊範圍、加快事故偵測、可擴展性、上市時間、成本）、三原則（書的原話：「故障隔離設計的第一原則是：絕對不共享任何東西」、不跨越泳道邊界、交易沿著泳道流動）、何時實作、怎麼測試泳道真的隔離。
   避開 stability-antipatterns 的 Nygard 版艙壁與連鎖反應（那頁只在連鎖反應一條裡帶過艙壁，這頁是 AKF 自己的泳道定義與設計原則）；避開 akf-scale-cube 的 y／z 軸切法，泳道怎麼對應軸只寫書說的那一句。
   claim 頁；related 連 stability-antipatterns、circuit-breaker、akf-scale-cube、microservices-vs-monolith。
   第三鏟候選留著：02-building-processes-for-scale/05-determining-headroom-for-applications（六步算餘裕與理想使用率，cloud-infra 的 capacity-planning-and-forecasting 走的是 SRE 的預測，兩者分工可寫）、02-building-processes-for-scale/06-exploring-architectural-principles（AKF 十二條原則）、02-building-processes-for-scale/12-barrier-conditions-and-rollback（為回滾與可停用而設計，cloud-infra 有 deployment 分類，先查分工）。

3. communication `long-running-operations`「長時間操作與可重跑作業：Operation 與 Job 兩種資源」— api-design-patterns（docs/03-fundamentals/05-long-running-operations/、docs/03-fundamentals/06-rerunnable-jobs/）。
   第一鏟（resource-oriented-api）掛的是第三、四、五部整部，正文用了標準方法、自訂方法三道關卡、關係四型、批次／分頁／過濾；LRO 與可重跑作業兩章一字未用。
   只寫：LRO 是回傳型別不是顯式建立的東西，與 promise 的三個差異（書有整節）；Operation 資源長什麼樣、取結果的兩條路（輪詢與等待）、錯誤碼必須給機器看、監控進度、取消、暫停與恢復、持久化；可重跑作業的三個動機（設定散落、兩種權限混為一談、排程只能靠外部）、Job 資源加自訂 run 方法加 Execution 資源。
   避開 resource-oriented-api 的標準方法與自訂方法規矩（這頁只寫 LRO 專屬的部分）；避開 realtime-updates 的長輪詢／WebSocket／SSE 傳輸層比較；避開 sync-vs-async 的訊息佇列論證。
   claim 頁；related 連 resource-oriented-api、sync-vs-async、realtime-updates、idempotency、message-queue。

4. communication `soft-deletion-and-revisions`「軟刪除與資源修訂：刪掉的和改掉的都還在」— api-design-patterns（docs/06-safety-and-security/02-soft-deletion/、docs/06-safety-and-security/05-resource-revisions/）。
   第一鏟沒碰第六部。
   只寫：刪除狀態的兩種表示（布林旗標與狀態欄位）、軟刪除怎麼改 get／list／delete 的行為、還原、徹底清除、到期、參照完整性；修訂識別碼、隱含修訂與明確修訂、取得與列出特定修訂、還原先前修訂、為什麼不重載標準 delete 來刪修訂。
   避開 api-design（Jin）的版本策略與 06/01 的三種版本化策略（版本化留在 api-design 頁，見旁註）；避開 idempotency 的去重鍵（06/03 請求去重不進這頁）；資料層的事件溯源歸 data-systems，seeAlso 連 data-systems 的 cqrs-eventsourcing/event-sourcing 即可。
   claim 頁；related 連 resource-oriented-api、api-design、idempotency、data-encoding。
   第三鏟候選：03-fundamentals/03-partial-updates-and-retrievals（欄位遮罩，25KB，單章可成頁）；06-safety-and-security/01-versioning-and-compatibility 若要開，先讀 api-design 頁判重疊（那頁已有累加式與 URI／Header／參數三方案）。

5. fundamentals `attribute-driven-design`「屬性驅動設計：ADD 的七個步驟與架構文件的視圖」— software-architecture-in-practice（docs/04-scalable-architecture-practices/20-designing-an-architecture/、docs/04-scalable-architecture-practices/22-documenting-an-architecture/）。
   第一鏟（quality-attribute-scenarios）掛 02/03 理解品質屬性、02/04 可用性、04/19 ASR、04/21 評估，寫的是六要素場景、tactics、問卷到 ATAM、架構債（千刀萬剮在 02/03，anchor 沒漏）。設計方法那章與文件化那章沒用。
   只寫：ADD 七步驟（審查輸入、選驅動因子、選要精煉的元素、選設計概念、實例化並分配責任、畫視圖草圖並記決策、分析並審查迭代目標）、何時建原型、架構待辦清單與設計看板；文件的三種視圖（模組、元件與連接器、配置）加品質視圖、文件化行為的兩種表示法、設計理據怎麼記、九類利害關係人各要什麼。
   避開 quality-attribute-scenarios 的場景格式與 ATAM；避開 architecture-characteristics（Richards 的特性識別）；第五部 24 架構師角色歸 architect-elevator 的題域，不寫。
   claim 頁；related 連 quality-attribute-scenarios、architecture-characteristics、nonfunctional-requirements、architect-elevator。
   第三鏟候選：02-quality-attributes/08-modifiability（提高內聚、降低耦合、延遲綁定三組 tactics；coupling-and-cohesion 掛的是 Newman 與 Ford，重疊要先量）、02-quality-attributes/09-performance（控制資源需求／管理資源兩組 tactics，站上有多頁實作但沒有這張分類樹）。

##### clean-code-note（2 本，開 1 張、不開 1 本）

6. functions `pragmatic-paranoia`「務實的偏執：合約、盡早崩潰、斷言與資源平衡」— pragmatic-programmer（docs/04-pragmatic-paranoia/23-design-by-contract/、docs/04-pragmatic-paranoia/24-dead-programs-tell-no-lies/、docs/04-pragmatic-paranoia/25-assertive-programming/、docs/04-pragmatic-paranoia/26-how-to-balance-resources/、docs/04-pragmatic-paranoia/27-dont-outrun-your-headlights/）。
   第一鏟（dry-orthogonality-and-broken-windows）掛 01/03、02/09、02/10、02/12：DRY、正交、熵、曳光彈。第四部「務實的偏執」五章沒碰，站上也沒有一頁講契約式設計或斷言。
   只寫 Tip 37 到 43：合約的三要素與「懶惰」的程式碼、Tip 38 Crash Early（書的原話：「崩潰往往是你能做的最好的事」）、斷言只防不可能的事且不關閉、Tip 40 善始善終與 Tip 41 在地行動（資源配對釋放、巢狀分配、例外下的平衡）、Tip 42 小步前進與 Tip 43 避免算命。
   避開 error-handling-exceptions-over-codes 的 Clean Code 第 7 章（例外勝過錯誤碼、別回傳 null）；避開 define-errors-out-of-existence 的 Ousterhout 立場，這頁只寫 Thomas 與 Hunt 的主張，兩造對立留 related 連過去（見旁註）；避開 dry 頁的曳光彈。
   claim 頁；related 連 error-handling-exceptions-over-codes、define-errors-out-of-existence、avoid-side-effects、dry-orthogonality-and-broken-windows。
   第三鏟候選：05-bend-or-break/28-decoupling、30-transforming-programming、31-inheritance-tax（解耦、轉換式程式設計、繼承稅，合計約 15KB；three-dimensions-of-coupling 掛的是 Balancing Coupling，design-patterns 有 composition-over-inheritance，分工要寫）；07-while-you-are-coding/38-programming-by-coincidence 單章 4KB 太薄，併進上面那張或不開。

- test-driven-development《Test-Driven Development》：不開。第一鏟 tdd-red-green-refactor 掛 Money 範例整部與 32 章，寫的是五步循環與步伐；kent-beck-note 已有五頁（money-example、xunit-bootstrap、tdd-patterns、fake-it-triangulate、mastering-tdd）把三部都挖了，紅綠條模式、測試模式、xUnit 模式都在那邊。clean-code 再開只會是人物站的複本；30-design-patterns 與 31-refactoring 兩章的內容分別落在 design-patterns-note 與本站 refactoring-moves（Fowler 版），不缺。tier 維持 spine，承諾已由既有頁兌現，既有 seeAlso 已連 kent-beck 的 mastering-tdd。

##### design-patterns-note（2 本，開 2 張）

7. principles `refactoring-conditionals-to-patterns`「條件邏輯太複雜：往 Strategy、State、Command 重構的三條路」— refactoring-to-patterns（docs/07-simplification/02-replace-conditional-logic-with-strategy/、docs/07-simplification/04-replace-state-altering-conditionals-with-state/、docs/07-simplification/06-replace-conditional-dispatcher-with-command/）。
   第一鏟（pattern-directed-refactoring）掛 01 到 04 章，寫的是雙病、三種走法、以壞味選模式；目錄 06 到 11 的 27 條重構一條沒用。
   只寫三條重構的動機、做法步驟與示例：為什麼不只是提煉方法、組合還是繼承、資料怎麼進 Strategy（02）；狀態改變的條件式與 UNIX 權限範例（04）；條件分派器為什麼換成 Command、優缺點（06）。三條共用的判準「條件邏輯太複雜」這個壞味從第一鏟頁的對應表接過來，不重講壞味理論。
   避開 strategy、state、command 三頁的 GoF 結構與意圖（那三頁講模式是什麼，這頁講從條件式走到模式的步驟）；避開 pattern-directed-refactoring 的三種走法；03-move-embellishment-to-decorator 篇幅最大（22KB）但 decorator 頁已厚，留第三鏟。seeAlso 連 clean-code 的 refactoring-moves/replace-conditional-with-polymorphism 與 decompose-conditional（Fowler 的小步版本）。
   claim 頁；related 連 pattern-directed-refactoring、strategy、state、command。
   第三鏟候選：06-creation 六條（建構子換 Creation Method、Factory、Builder、內聯 Singleton）；08-generalization 七條（Template Method、Composite、Observer、Adapter、Interpreter）。各可成一頁，與 creational／structural 既有頁的分工同上。

8. principles `design-smells-and-enabling-techniques`「設計壞味的四個家族：以壞味反推抽象、封裝、模組化、階層四原則」— refactoring-for-software-design-smells（docs/01-introduction/02-design-smells-overview/、docs/02-abstraction-smells/、docs/03-encapsulation-smells/、docs/04-modularization-smells/、docs/05-hierarchy-smells/、docs/06-wrapping-up/01-the-way-forward/）。
   這本書在概念頁零引用，但 problems/anti-pattern 六頁（god-object、hub-like-dependency、circular-dependency、rebellious-hierarchy、deep-hierarchy、over-engineering）都掛它，導覽三章也掛了。所以不是真欠債，是 DEEPEN-TARGETS 只數 concepts（見小結）。概念層缺的是書的骨架：壞味怎麼分類、每個原則底下的「使能技巧」是什麼、壞味的名字就是漏掉哪一項技巧。
   只寫：壞味從哪裡來（違反原則、不當套用樣式、語言限制、程序式思維、黏滯性）、四個原則各自的使能技巧（抽象五項、封裝兩項、模組化四項、階層五項）與壞味對應表、壞味不孤立出現（放大、共生、前導）、脈絡能不能讓人有意接受壞味。
   避開六個 problems 頁各自的單一壞味細節（cyclically-dependent、hub-like、rebellious、deep hierarchy 的症狀與重構留在那邊）；避開 single-responsibility 等 SOLID 頁的原則本體；01/01 技術債一章只取「設計債如何累積」一段，不重講技術債定義。
   claim 頁；related 連 pattern-directed-refactoring、single-responsibility、open-closed、liskov-substitution、law-of-demeter、composition-over-inheritance；problems 欄填 god-object、hub-like-dependency、circular-dependency、rebellious-hierarchy、deep-hierarchy。

##### agile-note（2 本，開 2 張、不開 1 本）

9. xp-practices `when-not-to-try-xp`「XP 什麼時候難、什麼時候別試：七個難處、五道障礙與合約形態」— extreme-programming-explained（docs/03-implementing-xp/06-what-makes-xp-hard/、docs/03-implementing-xp/07-when-you-shouldnt-try-xp/、docs/03-implementing-xp/08-xp-at-work/）。
   第一鏟（xp-values-principles-practices）掛第一部 04、05、07、08 與第二部 02：四變數、變更成本、價值到原則到實踐的推導。kent-beck-note 三頁也都在第一部。第三部「實施 XP」兩站都沒挖。
   只寫：簡單但不容易的七個難處（做簡單的事很難、承認不懂很難、協作很難、拆情緒的牆很難、聽起來違逆常識、小問題造成巨大影響、企業文化不接受掌舵）；五道障礙（企業文化含大規格書與加班文化、某些人、規模、技術含指數成本曲線與回饋週期過長、實體環境）；XP 在固定價格、委外、內包、計時計料、完工獎金、提前終止、框架開發、盒裝產品八種情境下怎麼變形。
   避開 why-agile-adoption-fails 的 Cohn 版失敗原因（那頁是導入敏捷的通論，這頁只寫 Beck 自己對 XP 畫的邊界）；避開 can-agile-scale 的規模化論證；避開第一鏟的四變數與價值推導。
   claim 頁；related 連 xp-values-principles-practices、why-agile-adoption-fails、starting-the-adoption、overcoming-resistance、can-agile-scale；seeAlso 連 kent-beck 的 xp/four-variables。

10. xp-practices `xp-roles-and-lifecycle`「XP 的七種角色與理想專案的生命週期」— extreme-programming-explained（docs/03-implementing-xp/03-lifecycle-of-an-ideal-xp-project/、docs/03-implementing-xp/04-roles-for-people/）。
    同上，第三部兩站都沒挖。
    只寫：角色只是慣例不是自然律（書用球隊位置開場）、程式設計師、客戶（你必須做決定、誰適合當客戶、要學的三件事）、測試人員、追蹤者、教練（間接工作最難、不必是技術大神）、顧問、大老闆；生命週期六期（探索、規劃、邁向首發的迭代、正式化、維護、死亡）各自該做什麼、多長、好的死法與不好的死法。
    避開 scrum 分類的 scrummaster-role、product-owner-role、development-team（Scrum 角色自成一套，這頁只寫 XP 的，related 連過去供對照）；避開 pair-programming 與 test-driven-development 兩頁的實踐本體；避開第 9 張的障礙與合約。
    claim 頁；related 連 xp-values-principles-practices、scrummaster-role、product-owner-role、development-team、managers-in-scrum。
    第三鏟候選：02-the-solution/06-planning-strategy（規劃遊戲三階段，與 sprint-planning、release-planning-constraints 分工先量）、02-the-solution/08-design-strategy（透過重構做設計、什麼叫最簡、圖在設計中的角色；refactoring-and-simple-design 掛的是 Clean Agile，Beck 原典版可補）。

- impact-mapping《Impact Mapping》：不開。46 章是章節數的假象，多數章 2–3KB，全書約 130KB；第一鏟 impact-mapping-four-levels 已用掉第二部（四層與兩個範例）與第四部（七步驟、三類典型錯誤）這兩個實質部，連 Gilb 五點、學習預算、八種角色都寫了。剩下第三部十章是定位章（影響地圖與適應式規劃、迭代交付、使用者故事、設計思考、從成本到投資怎麼接），合起來約 23KB，主張是「影響地圖與既有實踐的關係」，出處測試過但引用測試弱（沒有人會單獨連「影響地圖與交付實踐」），形狀偏導覽判讀。tier 維持 spine，承諾已由既有頁兌現；若日後導覽第四章要講「目標導向需求工程與迭代交付各缺一半」，直接掛 03/01 三個關鍵角色那章。

##### data-systems-note（1 本，開 2 張）

11. query-processing `access-vs-filter-predicates`「存取述詞與篩選述詞：索引用上了為什麼還是慢」— sql-performance-explained（docs/01-anatomy-of-an-index/03-slow-indexes/、docs/02-where-clause/04-searching-for-ranges/、docs/05-clustering-data/01-index-filter-predicates/）。
    第一鏟（pagination-and-top-n）掛 07 整部與 06/01，寫的是 Top-N、管線化 order by、偏移法與尋位法；存取述詞一詞只在 row values 那節出現一次。站上 execution-plans 與 query-optimization 掛的是 SQL Server 調校書與 Database Internals，沒有這組概念。
    只寫 Winand 的核心區分：拖慢索引查找的兩個成分（葉節點鏈與存取資料表）與三種索引操作（UNIQUE SCAN／RANGE SCAN／FULL SCAN）；範圍條件下欄位順序決定一切、順便推翻「最具選擇性的欄位放最左邊」（書的原話：「選擇性在這裡完全幫不上忙，但其中一種欄位順序仍然明顯較好」）；存取述詞對篩選述詞的定義與在執行計畫裡怎麼認；索引篩選述詞的正解是用索引來叢集，不是把 where 的所有欄位都索引。
    避開 covering-and-composite-indexes 的最左前綴與「等值在前、範圍在後」的經驗法則（那頁已寫，這頁只補 Winand 推翻選擇性迷思的那個例子，並在 related 指回去）；避開 pagination 頁的尋位法；LIKE 與索引合併只各寫一句。
    claim 頁；related 連 covering-and-composite-indexes、execution-plans、query-optimization、pagination-and-top-n、b-tree-internals。

12. indexing `obfuscated-conditions`「索引為什麼沒被用到：函式包欄位、日期、數值字串、組合欄位與聰明的邏輯」— sql-performance-explained（docs/02-where-clause/02-functions/、docs/02-where-clause/07-obfuscated-conditions/、docs/02-where-clause/03-parameterized-queries/）。
    同上，第二部六章第一鏟沒碰。
    只寫：函式索引與大小寫不敏感搜尋、使用者自訂函式與過度索引（02）；五種把條件弄混的寫法，TRUNC 陷阱、把日期當字串比較、數值字串、組合欄位用冗餘條件換回存取述詞、「聰明的邏輯」反模式與動態 SQL 正解、數學運算用移項換回索引（07）；繫結參數為什麼對最佳化工具不透明、專用計畫對通用計畫的兩難（03）。
    避開第 11 張的述詞定義（這頁只用「這個寫法讓條件變成篩選述詞」一句帶過）；避開 query-optimization 頁的統計與基數估計本體，繫結參數只寫 Winand 那個兩難。
    claim 頁；related 連 covering-and-composite-indexes、query-optimization、execution-plans、profiling-and-diagnosis。
    第三鏟候選：04-join-operation（巢狀迴圈的 N+1 與掌控 ORM 的 join 行為；query-optimization 已有演算法選擇，只有 ORM 那條線是空的）；08-modifying-data（索引對 insert／delete／update 的代價，合計 7KB 偏薄）。

##### security-note（1 本，開 1 張）

13. offensive-mindset `malware-behavior-and-covert-launching`「惡意程式的行為目錄：後門、竊憑證、持久化、提權與行程注入」— practical-malware-analysis（docs/05-malware-functionality/01-malware-behavior/、docs/05-malware-functionality/02-covert-malware-launching/）。
    第一鏟（malware-analysis）掛 01 入門、02/01 基礎靜態、02/03 基礎動態、06 反逆向整部、06/02 反除錯：四象限、簽章與指標、反分析軍備競賽。第五部「惡意程式功能」四章一字未用，而第一鏟說「先對它想幹嘛做出有根據的猜測」，猜的目錄就在這兩章。
    只寫：下載器與啟動器、後門（反向 shell、RAT 與殭屍網路）、竊憑證（GINA 攔截、傾印雜湊、鍵盤側錄）、持久化三型（登錄檔、木馬化系統二進位檔、DLL 載入順序劫持；書的原話：「持久化機制若夠獨特，本身就能成為指認某份惡意程式的絕佳指紋」）、提權（SeDebugPrivilege）、使用者模式 rootkit（IAT 掛勾、行內掛勾）；隱蔽啟動的行程注入家族（DLL 注入、直接注入、行程替換、掛勾注入、Detours、APC 注入）。
    避開 malware-analysis 的四象限與反除錯；避開 buffer-overflows 的漏洞利用本體；網路簽章（05/04）與資料編碼（05/03）不進這頁。
    claim 頁；related 連 malware-analysis、written-not-intended、know-your-opponent、buffer-overflows。
    第三鏟候選：06-anti-reverse-engineering/04-packers-and-unpacking（加殼器解剖、找 OEP、修匯入表，35KB，第一鏟只寫了加殼的兩個訊號）；05-malware-functionality/04-malware-focused-network-signatures（51KB，與 security-engineering 分類的偵測題域對口）。

##### 小結

- 開 13 張，全部 claim 頁；不開 2 本（test-driven-development、impact-mapping），tier 都維持 spine，承諾已由既有頁兌現。
- 分布：system-design 5（elevator 1、AKF 1、Geewax 2、Bass 1）、clean-code 1、design-patterns 2、agile 2、data-systems 2、security 1。
- `refactoring-for-software-design-smells` 顯示 0 頁的原因：`export-deepen-targets.py` 第 144 行只走 `content/concepts`，`tier-audit.py` 的 `citations()` 走 concepts＋problems。這本書被六個 problems 頁掛著，所以 tier-audit 真欠債 0、DEEPEN-TARGETS 卻報 0 頁。建議工具改成與 tier-audit 同口徑（concepts＋problems），不然雙集合站的題型頁承重永遠看不見。改了之後這本會從 0 頁變 6 頁、直接離榜；第 8 張仍值得開，理由在單上。
- 姊妹站分工：TDD 的第二鏟歸 kent-beck-note（已五頁）；XP 第三部兩站都空，這批落 agile 的 xp-practices；AKF 的餘裕流程與 cloud-infra 的容量規劃各走各的書，開第三鏟時再寫分工。
- 起草順序建議：2、13、7（單章材料最厚、邊界最乾淨）→ 3、4、11、12（目錄型書，每張都要先讀既有頁的 core 定邊界）→ 1、5、6 → 9、10 → 8（要同時讀六個 problems 頁，最後做）。
- 旁註一：clean-code 第 6 張寫完後，站上就有「盡早崩潰」（Thomas 與 Hunt）與「把錯誤定義掉」（Ousterhout）兩造，形狀測試過得了 `kind: debate`；但依「只有一造有頁不開」的規矩，等第 6 張落地再開單。
- 旁註二：elevator 第二部 10-coffee-shop-two-phase-commit（星巴克不用兩階段提交）是 distributed-transactions 頁的現成材料，那頁現在沒掛這本書；起草第 1 張時若順手，補一條 furtherReading 進 distributed-transactions，不另開頁。
- 旁註三：api-design 頁（Jin）的版本策略與 Geewax 06/01 的三種版本化策略（永久穩定、敏捷不穩定、語意化版本）有半頁重疊，第二鏟不開；若日後要補，走「補進既有頁」而不是新頁。
- 旁註四：elevator 第五部「轉型」八章（規模經濟到速度經濟、無痛則無變、錢買不到愛）是組織轉型題材，不屬 system-design；第一部 03 一階導數（多速架構）單章 7.7KB 偏薄，列第三鏟候選，可與 02/01 is-this-architecture 合開。

#### economics／personal-finance／investing／kiyosaki 第二鏟選題單（DEEPEN-TARGETS 9 本，Fable 開單 2026-11-12）

判準取自 note-check §1.3 與 §1.4：只為脊梁書開頁、主張標得到章節 anchor、與既有頁重疊低於一半、能被單獨引用。九本都是單一作者的體系書或敘事史，沒有「一個問題多本書吵」的形狀，全部 claim 頁、沒有 debate。
每張單的章節目錄全部 `[ -d ]` 驗過；單上引的原話與數字都 grep 過書 repo，起草時仍要逐筆回源。

##### economics-note（4 本，開 5 張）

站況：56 頁、六分類；四本候選都是 spine 各一頁。money-central-banks 這輪從 8 頁到 11 頁，`_index.md` roadmap 要補三條。

1. behavioral-narrative `price-is-not-right`「價格並不正確：從輸家組合到負股價，塞勒對效率市場的四個反例」— misbehaving（06-finance-1983-2003/02-does-the-stock-market-overreact、06-finance-1983-2003/04-the-price-is-not-right、06-finance-1983-2003/05-battle-of-closed-end-funds、06-finance-1983-2003/06-fruit-flies-icebergs-and-negative-stock-prices）。
   第一鏟（mental-accounting-endowment）掛第 1、2 部，寫 Econ 對 Human、心理帳戶、稟賦效應、沉沒成本；第 6 部「金融 1983–2003」六章一字未用。
   只寫：德邦特的輸家組合贏過贏家組合（人會根據薄弱證據做極端預測）、席勒 1981 年的波動上限（理性預測的波動不可能比被預測之物大；1871 年起的股利現值像新加坡氣溫一樣平坦，股價像醉漢預報員）、1987 年 10 月 19 日單日跌 20% 卻沒有任何重大新聞（珍珠港隔天只跌 4.4%）、封閉式基金的四個謎題與一價法則（發行附 7% 佣金、半年內常以 10% 以上折價交易；散戶情緒同時反映在折價與小型股報酬）、Palm／3Com 的負 stub value（1.5 × 95 = 142.5 美元對 3Com 收 82 美元，等於剩餘事業每股 −61 美元、合計 −230 億）。塞勒「我們發現了一隻獨角獸，卻為了牠的毛色該怎麼形容爭吵不休」照書引一次。
   避開：mental-accounting-endowment 的四個偏誤；market-myths-debunked（費雪的迷思手冊）；anatomy-of-bubbles（金德伯格的危機解剖）；market-cycles-psychology 那句「情緒是過度反應的引擎」只在 related 連過去。葛拉漢「為股東的惰性與愚蠢樹立的昂貴紀念碑」照書引一次。investing-note 的 efficient-market-and-random-walk 與 can-the-market-be-beaten 是另一造的主場，seeAlso 連過去，這頭不重講效率市場的正面論證。
   claim 頁；related 連 mental-accounting-endowment、narratives-move-economies、market-cycles-psychology、anatomy-of-bubbles。
   順手修既有頁：mental-accounting-endowment 的康乃爾馬克杯實驗（賣家中位 5.25 美元、買家 2.25 美元）出自 04-working-with-danny-1984-85/03-mugs，頁上只掛第 1、2 部，起草時補掛 04/03。

2. markets-incentives `fairness-constrains-prices`「雪鏟漲價為什麼不行：公平感怎麼約束價格與工資」— misbehaving（04-working-with-danny-1984-85/01-what-seems-fair、04-working-with-danny-1984-85/02-fairness-games）。
   第一鏟沒碰第 4 部；markets-incentives 十一頁沒有一頁講公平感對市場價格的約束，game-theory-basics 掛的是通識書的囚徒困境。
   只寫：雪鏟 15 → 20 美元 82% 認為不公平、MBA 學生 76% 可接受（理論誘發的盲點）、框架效應（取消 200 美元折扣 58% 可接受，加價 200 美元只有 29%）、成本上升的漲價被視為公平、既有狀態成為參考點、工資為何僵固（無通膨減薪 7% 62% 不公平；12% 通膨下只加薪 5% 卻 78% 可接受）、第一芝加哥銀行 3 美元櫃員費與可口可樂動態販賣機、Uber 激增定價與州檢察長的協議、滑雪旅館與 Next 餐廳的克制定價、最後通牒賽局（不超過派的 20% 的提案通常被拒；賭注放大到三個月收入行為幾乎不變）、獨裁者賽局 74% 平分、懲罰賽局 81% 寧可少拿 1 美元、公共財賽局平均投入一半。
   避開：mental-accounting-endowment 的稟賦效應（這頭只寫「既有狀態成為參考點」一句）；price-controls-consequences（政府的價格管制，這頭是市場自己的規範）；game-theory-basics 的囚徒困境（只在公共財賽局處一句帶到）；schools-of-economic-thought 的凱因斯工資僵固論，這頭只寫塞勒的民調證據，不寫總體理論。第 4 部 03-mugs 歸第一鏟（見第 1 張）。
   claim 頁；related 連 incentives-and-prices、supply-demand-prices、game-theory-basics、mental-accounting-endowment。
   Misbehaving 其餘不開：第 3 部自制力與第 8 部 Save More Tomorrow 已在 nudge-choice-architecture（SMarT 一節）；第 7 部芝加哥（美式足球選秀、益智節目）是逸事；第 5 部「與經濟學界交手」是學派鬥爭史，導覽第五章「邊講理論邊講學派鬥爭史」一句已帶到。

3. money-central-banks `taiwan-foreign-reserves`「外匯存底的帳：全臺灣最大、也最不透明的一筆錢」— central-bank-privilege（05-foreign-reserves/01-wealthy-central-bank、05-foreign-reserves/02-reserve-management、05-foreign-reserves/03-mysterious-reserves、05-foreign-reserves/04-benefits-of-large-reserves、05-foreign-reserves/05-costs-of-large-reserves）。
   第一鏟（central-bank-privilege）掛 03、04、06、08 四章，寫雙低、阻升不阻貶、盈餘繳庫與自我強化循環；外匯存底只在循環裡當一個環節，第 5 章五節沒用。
   只寫：2020 年 12 月底 5,299 億美元（約 15.1 兆新臺幣，超過國泰金控總資產）、兩次累積期都是阻升（1980 年代 1:40 到 1:25；2000 年起「彭淮南防線」30）、謝澤 2019 年指出的隱藏外幣資產與 2020 年 3 月首度揭露的 1,400 億美元（換匯交易 991 億、存放國內銀行 328 億、拆款 61 億）、報酬率 3.9%（1999–2018）對挪威 6.09%、GIC 5.5%、香港 4.7%、央行反對主權基金的兩個理由與書的反駁（短期外債 1,747 億、民間持有 8,100 億美元外匯）、透明度（美國 Fed 每季揭露幣別與標的、延遲兩年公布交易細項；臺灣只有 2018 年楊金龍一句「美元約占八成」）與無外部會計師查核（IMF：超過一半國家的央行交外部審計）、1997 年亞洲金融風暴的護身符（新臺幣貶 23% 對印尼盾 80%；臺灣不是 IMF 會員）、成本三項（匯損、資金氾濫逼出低利率、繳庫誘因）與「約是國際建議額四倍」。
   避開：central-bank-privilege 的雙低循環與盈餘繳庫機制（這頭只在成本三那段用一句接回去）；central-bank-mandate 的教科書職責；reserve-currency-cycle（達利歐的儲備貨幣週期，不同題）。
   claim 頁；related 連 central-bank-privilege、central-bank-mandate、lender-of-last-resort、reserve-currency-cycle。

4. money-central-banks `liquidity-preference`「利率是放棄流動性的報酬，不是儲蓄的報酬：凱因斯的利率理論」— general-theory-of-employment-interest-and-money（04-the-inducement-to-invest/03-the-general-theory-of-the-rate-of-interest、04-the-inducement-to-invest/04-the-classical-theory-of-the-rate-of-interest、04-the-inducement-to-invest/05-the-psychological-and-business-incentives-to-liquidity）。
   第一鏟（schools-of-economic-thought）掛 01/03、03/03、04/02、06/03，寫有效需求、乘數與剎車、動物精神、社會哲學；第四篇的利率理論（第 13 到 15 章）沒用，money-central-banks 八頁也沒有一頁講利率怎麼決定。
   只寫：時間偏好需要兩組決定（消費多少、以什麼形式持有）而古典理論只看第一組；「利率不可能是『儲蓄』或『等待』本身的報酬」（把儲蓄以現金囤起來的人一樣儲蓄卻賺不到利息）；利率是使「以現金形式持有財富的欲望」與「可得的現金數量」均衡的價格；M = L(r)；流動性偏好存在的必要條件是對未來利率的不確定；三個動機（交易、預防、投機）；古典利率理論的各家表述（馬歇爾、卡塞爾、瓦爾拉斯）與錯在哪（假定所得給定）；公開市場操作為什麼透過投機動機才起作用，消息若被所有人同樣解讀，利率會不經交易就改變；M = M1 + M2 = L1(Y) + L2(r)；貨幣數量大增、利率卻可能幾乎不動的情況。
   避開：schools 頁的全部；what-is-money（信任的度量）；credit-and-banking；central-bank-mandate 的現代央行操作（這頭只寫凱因斯 1936 年對公開市場操作的分析）。術語照書 repo 譯法（流動性偏好、資本邊際效率、工資單位）。
   claim 頁；related 連 schools-of-economic-thought、what-is-money、central-bank-mandate、credit-and-banking。
   第三鏟候選：05-money-wages-and-prices/01-changes-in-money-wages（削減貨幣工資為何不增加就業、七項反響），與第 2 張的工資僵固民調接得上。

5. money-central-banks `sterling-returns-to-gold-1925`「回到 4.86：1925 年英鎊重返戰前平價與 1927 年那杯威士忌」— lords-of-finance（03-sowing-a-new-wind/03-golden-chancellor、03-sowing-a-new-wind/04-la-bataille、03-sowing-a-new-wind/06-un-petit-coup-de-whisky；03-sowing-a-new-wind/05-first-squalls 講 1926–27 的 Coolidge 牛市，視需要掛）。
   第一鏟（gold-standard-and-fetters）掛第 1、2 部整部（四位央行家登場、賠款、野蠻遺跡），寫金本位的紀律與枷鎖、1931–36 連鎖脫金；1923–28 重建期的第 3 部沒用，而那正是枷鎖怎麼被親手扣上的。
   只寫：1924 年英國物價仍比美國高約 10%、英鎊卡在 4.35 美元、保留派對諾曼派（回到 4.86 是「對全世界托付者的道德承諾」）、「英國金融健康但經濟生病；法國經濟健康但金融生病」、邱吉爾 1924 年 11 月意外任財相與諾曼年底赴紐約徵詢斯壯、法國 1925 年「假帳」醜聞與法郎釘在 25 對 1 美元、1927 年 7 月長島密會（諾曼主張有儲備的國家放鬆信用、Rist 反駁英鎊釘太高是英國自找）、8 月降息 0.5% 到 3.5%（四家區域 Fed 拒跟、Crissinger 辭職）、斯壯對 Rist 說的「un petit coup de whisky」、道瓊年底漲 20% 破 200、經紀人貸款從 33 億到 44 億、斯壯 1928 年 2 月承認可能錯了、Miller 1931 年國會證詞「聯邦準備系統有史以來最大、最大膽的操作」。
   避開：gold-standard-and-fetters 的規則本身與 1931 之後；1929-and-depression 的高盛信託與保證金機制（崩盤現場歸那頁）；邱吉爾「人生最大的失敗」一句已在第一鏟，不重複。判讀只寫書裡有的（「部分歷史學家認為長島會議是關鍵轉折」、斯壯自己認知低美息沒解決英國問題），不自己下「大蕭條是誰造成的」。
   claim 頁；related 連 gold-standard-and-fetters、1929-and-depression、central-bank-mandate、gold-as-money。
   順手修既有頁：gold-standard-and-fetters 用了 1931 年秋聯準會 1.5% 升到 3.5%（04-reaping-another-whirlwind/05-gold-fetters）與羅斯福「喝醉的金本位」（05-aftermath/01-gold-standard-on-the-booze），anchor 只掛第 1、2 部，起草時補掛這兩章；頁上「符合每一條已知的規則」這句在書 repo grep 不到逐字原文（04/05 只有「過時規則」），回源確認措辭，找不到就改寫。

###### 小結

- 開 5 張，全 claim：塞勒 2（金融反例、公平感）、央行特權 1、凱因斯 1、金融之王 1。
- 不開 0 本；Misbehaving 其餘四部的理由寫在第 2 張下。
- 既有頁補 anchor 兩處（第 1、5 張的順手修）。
- 起草順序：4（教義最硬、全靠原文）→ 3（數字最多，逐筆回源）→ 1、5 → 2。

##### personal-finance-note（3 本，開 3 張、不開 1）

站況：36 頁、六分類；三本都是 spine 各一頁。Early Retirement Extreme 是站上最厚的書（78 章），第一鏟只用了四部的主軸，開兩張。

6. fire `four-economic-types`「薪水人、工作人、生意人、文藝復興人：耦合與線性兩軸切出的四種經濟人」— early-retirement-extreme（03-economic-degrees-of-freedom、03-economic-degrees-of-freedom/02-the-salary-man、03-economic-degrees-of-freedom/03-the-working-man、03-economic-degrees-of-freedom/04-the-businessman、03-economic-degrees-of-freedom/05-the-renaissance-man）。
   第一鏟（renaissance-ideal）掛 02、04、05、08 四部，寫鎖定的帳本、專業化尖峰、文藝復興理想、策略之網、r/(1-r)；核電廠／大學／工具三個類比出自第 5 部策略原則，已用。第 3 部的兩軸四型沒碰。
   只寫：自由度被藏起來（方向盤鎖死的車、刮鬍刀的選擇被限縮在多刀片一條線上）、耦合軸（緊耦合可預測、雇主用「只提供全職職缺」與「綁上優渥福利」讓勞動供給可預測；鬆耦合有餘裕，正常時效率較低、被打斷時代價小）、線性軸（輸出被輸入清楚定義；外科手術線性、創業與美式足球教練非線性；整體不同於各部分之和）、人怎麼把非線性硬掰成線性、四型：薪水人「有選項但不創造選項」與自由的錯覺、工作人、生意人「把自己插進事業現金流裡」與 OPM、文藝復興人（在廣泛領域具備能力、相當程度獨立於市場、需要的錢更少、不需槓桿）。
   避開：renaissance-ideal 的鎖定帳本、專業化尖峰、策略之網、三個系統類比；millionaire-fastlane 的三條路線圖（related 連過去，不比較）；kiyosaki-note 的現金流象限是另一套分類，seeAlso 連 cashflow-quadrant 即可，不對照。
   claim 頁；related 連 renaissance-ideal、savings-rate-buys-time、millionaire-fastlane、multiple-income-streams。

7. wealth-habits `renaissance-lifestyle-tactics`「花更少比賺更多容易：文藝復興式生活的物品、住、行、食」— early-retirement-extreme（06-a-renaissance-lifestyle、06-a-renaissance-lifestyle/01-things、06-a-renaissance-lifestyle/06-shelter、06-a-renaissance-lifestyle/09-eating、06-a-renaissance-lifestyle/11-transportation）。
   第一鏟掛的四部裡沒有第 6 部；frugality-as-system 掛的是 Hallam，real-hourly-wage 是《富足人生》，站上沒有一頁寫 Fisker 的戰術層。
   只寫：自由靠生產與消費之間的落差，兩種做法裡「花更少」在富裕社會對多數人容易得多（年收入 4,000 到 400,000 美元之間提高收入都很難；作者的支出一份兼職翻漢堡就賺得到）、駭進既有方法達不到重新設計（改良騎兵打不贏機關槍）、所有物的六個問題（花錢反而是最小的）與「工具隨時可能失去，技能卻會跟著你」、住所（房子變倉庫、郊區預設值讓人不會騎車、「愈無生產力愈是好的地位象徵」、中位房價 150,000 美元 5% 房貸一年 9,663 美元已超過整套生活方式的全年預算，再加 50%、「債務超過無生產力權益 400% 算保守」）、交通（先縮短 A 到 B 的距離、三英里走 45／跑 25／騎 15／開 10 分鐘、把車當休閒車輛）、飲食（為燃料而吃、以美味為副作用；慰藉食物與兩條成癮路徑；「需要靠廣告告訴你它對你好的產品，很可能不好」）。
   避開：renaissance-ideal 的鎖定與策略層；frugality-as-system 的 Hallam 做法；real-hourly-wage 的時薪換算；spending-with-intention；die-with-zero。第 6 部各章是摘要，表格外的數字不自補。
   claim 頁；related 連 renaissance-ideal、frugality-as-system、real-hourly-wage、savings-rate-buys-time。

8. save-invest `magic-beans`「魔豆：選股、分批進場與股市大師，三種看起來太好的東西」— simple-path-to-wealth（03-magic-beans、03-magic-beans/02-why-i-cant-pick-winning-stocks、03-magic-beans/03-why-no-dollar-cost-averaging、03-magic-beans/04-stock-market-gurus、03-magic-beans/05-you-too-can-be-conned）。
   第一鏟（f-you-money）掛第 1、2 部整部，寫 F-You Money、債務、市場永遠上漲、VTSAX 兩階段、1987 年；第 3 部魔豆與第 4 部提領沒用。
   只寫：1989 年降薪進投資研究公司看到的真相（分析師拿不到比市場早的消息、企業內部預測是一層層的猜再被高層「調好看一點」）、阿里類比、「一點點謙卑能救你的屁股，也救你的現金」；定期定額：1970–2013 市場 43 年漲 33 年（77%）、五個理由（賭下跌、就是擇時、破壞配置、時間範圍兩難、結束後風險沒消失）、累積期的薪資扣款是必要的 DCA、有巨款就依目標配置一次投入；股市大師：《Wall Street Week》總有人說對、七步驟 SOP 與 15% 經紀費；騙局：反向金字塔信（1,000 封減半六次剩 15 或 16 人收到六封全中）、不被騙的五條規則（Madoff 的受害者很多是金融專業人士）。
   避開：f-you-money 的全部；index-fund-investing（Hallam 的成本論）；just-keep-buying（Maggiulli 的神級擇時者與「紀律勝於擇時」，與柯林斯一致，只在 related 連、不並排成兩造）；investing-note 的 can-the-market-be-beaten 與 does-market-timing-work 是對照頁，seeAlso 連過去。第 4 部提領實作（04/01、04/02）不在這頁，留給 4-percent-rule 擴充或第三鏟。
   claim 頁；related 連 f-you-money、index-fund-investing、just-keep-buying、asset-allocation-basics。

###### 不開（1 本）

- millionaire-fastlane《快速致富》：不開。第一鏟掛了第 3、4、5、7 四部，路線圖、三條方程式、ULL／CUL、NECST 五誡、兩座金字塔全用了；剩下第 6 部是自我管理（方向盤、擋風玻璃、機油、紅線）、第 8 部是創業執行（執行是國王、SUCS 客服、USP、專一），在理財站只能寫成創業雞湯，題域是 startup-note 的（那站沒收這本，也不該為它開）。tier 維持 spine，承諾已由既有頁兌現。

###### 小結

- 開 3 張，全 claim：ERE 2、Simple Path 1；不開 1。
- 起草順序：8（材料最短、事實最密）→ 6 → 7（章節最長、數字最多）。

##### investing-note（1 本，開 1 張）

9. value-investing `below-liquidating-value`「賣得比清算價值還低的股票：淨流動資產買法與股東的三個錯誤假設」— security-analysis（06-balance-sheet-analysis/02-significance-of-current-asset-value、06-balance-sheet-analysis/03-liquidating-value-and-stockholder-management-relations）。
   第一鏟（voting-machine-and-weighing-machine）只掛 01/01，寫投票機、內在價值是區間、三大障礙、Wright Aeronautical；六十三章只用了一章。
   只寫：清算價值的計算規則（負債按面值扣、資產看可實現比例：現金約 100%、應收 75–90%、存貨 50–75%、固定與雜項 1–50%）、White Motor 1931 年底股價 8 美元對清算值約 31、1932 年 NYSE 四成以上工業股市價低於淨流動資產（「死掉比活著值錢」）與 1938 年初的 20.5%、「股票長期賣得低於清算價值，不是價格太低，就是公司應清算」的兩個推論、三條出路（盈利恢復、出售合併、清算）與案例（Pepperell、Hamilton Woolen、Standard Oil of Nebraska、Mohawk Mining、Northern Pipe Line）、便宜貨的三個條件、這類操作在中等市況表現最好；股東那一半：「典型美國股東是被囚禁動物中最溫順與最冷漠的」、Berle 與 Means 的所有權與控制權分離、三個錯誤假設、管理層與股東的五個利益衝突點、董事會不獨立（高管選董事的次數多於董事選高管）。
   避開：voting-machine 的內在價值概念；mr-market-and-margin-of-safety（《智慧型股票投資人》第 8、20 章，安全邊際原則歸那頁，這頭只寫資產面的操作）；stock-is-a-business（巴菲特的公司治理，這頭是葛拉漢 1934 年的版本，related 連過去不對照）；special-situations-and-spinoffs（Greenblatt 的分拆，這頁只寫葛拉漢的清算與部分清算案例）；low-risk-high-uncertainty。
   claim 頁；related 連 voting-machine-and-weighing-machine、mr-market-and-margin-of-safety、stock-is-a-business、special-situations-and-spinoffs。
   導覽：第三章「原典的原典」那段、第五章「《證券分析》壓軸」那行各補一句連到新頁。
   第三鏟候選：04-theory-of-common-stock-investment/01、02（戰前三要素對新時代理論：估值怎麼從股利與資產走向「潛力與預言」，與 market-history 的 does-price-rewrite-fundamentals 接得上）；05-analysis-of-income-account/03（Park and Tilford 的損益表灌水、用應計稅費核驗盈餘）。

###### 小結

- 開 1 張 claim；這本書六十三章幾乎每章近萬字，第三鏟還有兩個候選。

##### kiyosaki-note（1 本，開 1 張）

10. entrepreneur-investor `b-i-triangle-five-layers`「B-I 三角的五層內裡：現金流、溝通、系統、法務、產品」— rich-dads-guide-to-investing（03-how-to-build-a-strong-business/02-the-b-i-triangle、03-how-to-build-a-strong-business/03-cash-flow-management、03-how-to-build-a-strong-business/04-communications-management、03-how-to-build-a-strong-business/05-systems-management、03-how-to-build-a-strong-business/06-legal-management、03-how-to-build-a-strong-business/07-product-management）。
    第一鏟（sophisticated-investor）掛第 1、4、6 部整部，寫 90/10、SEC 合格對老練、十項控制權、創造資產、支出欄；既有 b-i-triangle 頁掛的是《富爸爸資本主義宣言》與軍隊領導課，寫外框三元素（使命、團隊、領導）與四面體。第 3 部的五層內裡兩頁都沒碰；導覽第三章自己寫「投資指南只開了內行投資人一頁，這幾處還能再挖」。
    只寫：五層由下而上的排序與「越底層越重要」（02 章只取結構表那一段）；現金流：利潤不等於現金流、實際現金流對幻影現金流、「任何採購若無法以銷售成長來正當化就不買」、各階段訣竅（延後支薪、盡快開發票、信用關係建立前先付款）；溝通：「流進你事業的現金，與流出的溝通量成正比」、六週週期、募資之前先學七項技能、「窮人是差勁的溝通者」、兩項基本功（克服銷售與公開演說的恐懼）；系統：每套系統有人負責、真正的系統不能是人（S 象限裡那個人本身就是系統）、麥當勞由青少年經營、從房地產入門練系統；法務：魔鬼氈皮夾沒花一萬美元申請專利被抄、點子曝光前先保護、歐納西斯憑一紙合約借錢買船；產品：評估企業時產品最不需要優先檢視、「我們大多數人都能煎出比麥當勞好吃的漢堡，卻鮮少有人能建立起更強的商業系統」、產品是使命的表達、「我們每個人的內在，都有一個 B-I 三角」。
    避開：b-i-triangle 的使命／團隊／領導／四面體；sophisticated-investor 的 90/10 與十項控制權；cashflow-quadrant；work-to-learn（「去找一份能訓練你銷售的工作」在這頭只引一次）。
    claim 頁；related 連 b-i-triangle、sophisticated-investor、cashflow-quadrant、three-leverages。
    順手查既有頁：b-i-triangle 頁的四面體與福特「讓汽車民主化」若出自 03/02（原典就在這章），補掛 03/02 進它的 furtherReading。
    導覽第三章第 33 行與第 81 行各補一句。
    不開：第 2 部「該成為哪一種投資人」（合格、具資格、老練、內部、終極五類）。合格對老練已在第一鏟，名稱又與 five-levels-of-investors（《現金流象限》的五個層次）相撞，再開會讓讀者把兩套分類混在一起；02/04 具資格投資人（基本面對技術面，一萬三千字）留第三鏟候選，標題要避開「五種」字眼。

###### 小結

- 開 1 張 claim。

##### 四站總結

- 開 10 張（economics 5、personal-finance 3、investing 1、kiyosaki 1），不開 1（Fastlane）。全部 claim，沒有 debate：九本都是單一作者體系書或敘事史，沒有兩造。
- 既有頁補 anchor 三處：mental-accounting-endowment 補 04/03-mugs；gold-standard-and-fetters 補 04/05-gold-fetters 與 05/01-gold-standard-on-the-booze，並回源「符合每一條已知的規則」；b-i-triangle 視內容補 03/02。
- 第三鏟候選四個：凱因斯第 19 章貨幣工資、證券分析第四部與第五部第 3 章、投資指南 02/04。
- 跨站 seeAlso：第 1、8 張連 investing-note 的 efficient-market-and-random-walk／can-the-market-be-beaten／does-market-timing-work；第 6 張連 kiyosaki-note 的 cashflow-quadrant。路徑起草前 `ls` 驗。
- 旁註：Fastlane 判不開之後仍會留在 DEEPEN-TARGETS 的 102 本裡，工具沒有「已裁決不開」的記號；management 的五大障礙與 theology 的活的教會上一輪也是這樣。
- 起草順序建議：4 → 3 → 9 → 10 → 8 → 1、5 → 6 → 2 → 7。

#### relationships／maxwell／business-strategy／leadership／communication／covey／growth 第二鏟選題單（DEEPEN-TARGETS 15 筆，Fable 開單 2026-11-12）

判準取自 note-check §1.3 與 §1.4：只為脊梁書開頁，主張要標得到章節 anchor，與既有頁重疊低於一半，能被單獨引用；同一本書被兩站收的，分工寫明。
15 筆裡有 4 筆是姊妹站已經挖深的書（speed-of-trust 在 covey 8 頁、mastery 在 greene 4 頁、turn-the-ship-around 第三四部在 management、essential-drucker 三站判 tool／support），這些以改判或不開收掉，不硬開第二頁。
章節目錄全部 `[ -d <book>/site/content/<anchor> ]` 驗過（64 條）。

##### relationships-note（開 4 張）

1. parenting `felt-with-not-dealt-with`「感受要被一起承受，不是被處理掉」— book-you-wish-your-parents-had-read（docs/03-feelings/01-learning-to-contain-feelings、docs/03-feelings/03-danger-of-disallowing-feelings、docs/03-feelings/05-felt-with-not-dealt-with、docs/03-feelings/08-demand-to-be-happy、docs/03-feelings/09-distracting-away-from-feelings）。
   第一鏟（rupture-and-repair）掛 01 教養傳承與 02 環境兩部，寫破裂與修復；第三部「感受」九章一字未用。
   只寫 Perry 的論證：情緒被禁止不會消失只會躲起來、成人憂鬱常見根源是當年沒學到自己可以被安撫（01）、Lucas 十歲跳窗的「看起來還好」（03）、Dave 與 Nova 的車位之爭與「駕車打滑要順勢轉」（05）、Adam Phillips「要求一定要快樂會破壞人生」與治療師 Jerry Hyde「情緒沒有混音台只有總音量」（08）、分心是詭計與什麼時候分心可以（09）。
   避開 talk-so-kids-will-listen 的法伯四技巧（全神貫注聽、一個字詞回應、說出感受、用幻想實現願望），這頁講「為什麼不能用哄、分心、要求快樂處理情緒」，不講怎麼聽；避開 rupture-and-repair 的破裂與修復；避開 whole-brain-parenting 的左右腦與上下層腦。
   claim 頁；related 連 rupture-and-repair、talk-so-kids-will-listen、whole-brain-parenting、thirty-million-words。

2. parenting `behaviour-is-communication`「行為是溝通：發脾氣、說謊與界線各在傳達什麼」— book-you-wish-your-parents-had-read（docs/06-behaviour-is-communication/05-what-does-behaviour-mean、docs/06-behaviour-is-communication/10-more-on-tantrums、docs/06-behaviour-is-communication/13-childrens-lies、docs/06-behaviour-is-communication/14-boundaries-define-yourself）。
   第一鏟同上；第六部十七章是全書最厚的一部（界線一章 11.6K、青少年一章 10K），沒有任何頁用到。
   只寫：從自己最差的時刻反推孩子失控的處境、觸發點要由父母觀察而不是問孩子（05）、沒有人享受發脾氣、三步驟（問這行為傳達什麼感受、肯認它、冷靜後給可接受的表達方式）、不留孩子一個人尖叫到完（10）、校長 Margaret Connell「你的孩子會對你撒謊」與「不要把它當天大的事」（13）、愛加界線、界線要在極限之前設下、「我不能讓你玩我的鑰匙」、奇蹟之子的父母設不下界線（14）。
   避開第 1 張的情緒論證（這頁只在開頭一句接「行為背後是感受」）；避開 whole-brain-parenting 的腦科學解釋；避開 boundaries 分類的成人界線頁（saying-no-without-guilt、own-your-life），這頁的界線是父母對孩子的。
   claim 頁；related 連 felt-with-not-dealt-with（第 1 張）、rupture-and-repair、whole-brain-parenting、break-toxic-patterns。
   第三鏟候選：06/16-teenagers-and-young-adults（10K）與 05/14-sleep、05/17-play，材料夠厚，等這兩張落地再看。

3. connection `confront-with-care`「在乎到願意面質：衝突要早、別為小事砸鎚子」— winning-with-people（docs/02-connection-question/06-confrontation-principle、docs/01-readiness-question/04-the-hammer-principle）。
   第一鏟（connection/winning-with-people）掛 01 預備問題一部，寫五問總覽與四個案例；maxwell-note 同名頁掛 02、03 兩部，也是總覽。兩站都沒有把任何一條原則寫成一頁。
   只寫：面質原則（衝突像癌症早期發現、「我是否夠在乎對方足以用對的方式面質」、接任 Skyline 教會後打給喬的那通電話）與鎚子原則（「別人會不會說我在關係中對小事過度反應」、Maxwell 1969 年婚後每次都「贏」卻在情緒上擊垮 Margaret、把「贏得爭辯」放在「贏得關係」之前）；判別變數只寫書裡有的：面質的前提是在乎、鎚子的檢查點是比例。
   避開兩站首頁的五問架構（只在點題句提一次「這是連結問題與預備問題各一條」）；避開 boundaries/navigate-conflict 的 HBR 衝突類型學與 apology-and-repair 的 Lerner 道歉技術，這頁是 Maxwell 的兩條原則，不做衝突通論。
   claim 頁；related 連 winning-with-people、navigate-conflict、apology-and-repair、empathy-as-skill。與 maxwell-note 第 3 張分工：這站拿衝突（02/06＋01/04），人物站拿投資問題一整部（04）。

4. friendship `dark-side-of-social-capital`「社會資本的黑暗面：博愛會不會吃掉自由與平等」— bowling-alone（docs/04-so-what/07-the-dark-side-of-social-capital）。
   第一鏟（bowling-alone-social-capital）掛導論、第二部全部、03/06 總結、第四部全部，寫社會資本的定義、兇手比重、保齡球數字；凝聚型與橋接型只有一條 core。
   只寫這一章（25K）：巴比特與梭羅的「怪人會」成員是文學定型角色、法國三色旗的第三個字「博愛」就是社會資本、兩百年政治辯論談自由對平等卻少談博愛對兩者的取捨、Putnam 自己列的幾個爭點（社會資本與自由寬容為敵？與平等為敵？），以及他怎麼用凝聚型／橋接型回答。
   避開第一鏟已寫的定義、四大兇手與比重、保齡球數字；避開 third-places 與 true-community。
   claim 頁；related 連 bowling-alone-social-capital、true-community、third-places、friendship-over-time。
   不開第五部（05/01 鍍金時代與進步時代 53K、05/02 社會資本家的議程 30K）：材料厚，但那是公民史與政策議程，離這站的人際主題遠；留作第三鏟候選或 history-note 題材。

##### maxwell-note（開 3 張）

1. leadership `seven-challenges-of-the-middle`「夾在中間的七個挑戰」— 360-degree-leader（docs/02-challenges-360-leaders-face/01-tension-challenge、docs/02-challenges-360-leaders-face/02-frustration-challenge、docs/02-challenges-360-leaders-face/03-multi-hat-challenge、docs/02-challenges-360-leaders-face/04-ego-challenge、docs/02-challenges-360-leaders-face/05-fulfillment-challenge、docs/02-challenges-360-leaders-face/06-vision-challenge、docs/02-challenges-360-leaders-face/07-influence-challenge）。
   第一鏟（360-degree-leader）掛 01 迷思與 03 向上領導，七個挑戰只有一條 core 帶過（壓力大、自由有限、多頭指揮、看不見全局）。
   只寫七個挑戰各自的「關鍵一句」與一個書裡的案例：張力挑戰的「彷彿擁有所有權力又沒有權力」（Dan Reiland）與影響張力的五個因素（01）、挫折挑戰的李將軍跟隨戴維斯（02）、多重角色挑戰的 Stan Toler 一人身兼多職（03；「八頂」是 fork 數的，不是書的原話，起草時回章節數）、自我挑戰的「你想不想做我為了能做這件事所做過的所有事」（04）、成就感挑戰的雪橇隊領頭狗（05）、願景挑戰的六種反應（06）、影響力挑戰「沒人躲得掉」（07）。
   避開第一鏟的七個迷思與向上／橫向／向下三組原則；避開 five-levels-of-leadership。
   claim 頁；related 連 360-degree-leader、five-levels-of-leadership、developing-leader-within-you、leadership-gold。

2. leadership `people-development-level`「第四層立人：為什麼多數領導者停在第三層」— 5-levels-of-leadership（docs/04-people-development-helping-individual-leaders-grow-extends-your-influence/01-the-upside-of-people-development、docs/04-people-development-helping-individual-leaders-grow-extends-your-influence/02-the-downside-of-people-development、docs/04-people-development-helping-individual-leaders-grow-extends-your-influence/03-best-behaviors-on-level-4、docs/04-people-development-helping-individual-leaders-grow-extends-your-influence/06-guide-to-growing-through-level-4）。
   第一鏟（five-levels-of-leadership）掛第一、二、三、五層四部，第四層是唯一沒掛的一部，正文只有一條 core 與「準備好上 Level 4 沒有」的八個問題（那是第三層末尾的信念章）。
   只寫第四層本身：上行（讓公司成長的辦法是讓人成長、Synovus 的 Jim Blanchard）、下行（「不訓練他們然後他們留下來」更糟、自我中心與不安全感讓領導者不栽培人）、七個最佳行為（招募、定位、示範、裝備、栽培、賦能、衡量；「需要一位領導者才能認出、示範給、養成一位領導者」）。
   避開第一鏟的五層總覽、疊加不取代、八個自檢問題；避開 developing-leader-within-you（那是領導自己）。
   claim 頁；related 連 five-levels-of-leadership、developing-leader-within-you、21-laws-of-leadership、17-laws-of-teamwork。

3. relationships `investment-question`「投資的問題：園丁、101%、耐心、慶祝與高路」— winning-with-people（docs/04-investment-question/01-gardening-principle、docs/04-investment-question/02-101-percent-principle、docs/04-investment-question/03-patience-principle、docs/04-investment-question/04-celebration-principle、docs/04-investment-question/05-high-road-principle）。
   第一鏟（relationships/winning-with-people）掛 02 連結與 03 信任兩部，寫五問診斷架構；第四部投資問題沒掛，五條原則只在表裡各一行。
   只寫五條原則各自的問句與案例：園丁（「我是偶爾灌溉還是持續灌溉」、Albom 與艾迪叔叔）、101%（「找到那一件事並給它 100%」、海餅乾三人組）、耐心（「即使不方便我會帶上他人同行嗎」、Larry Walters 的氦氣球椅）、慶祝（「我會為朋友的成功加油嗎」、Maxwell 早年最年輕紀錄卻最寂寞）、高路（Beecher 的墓地、卜威廉與救世軍）。
   避開兩站首頁的五問總覽；避開 relationships-note 第 3 張的面質與鎚子；relationships-note 首頁已用 Albom／Porter 當投資與綜效的案例，這頁的 Albom 只取園丁章原文、不重講 Porter。
   claim 頁；related 連 winning-with-people、25-ways-to-win-with-people、17-laws-of-teamwork、everyone-communicates-few-connect。

##### business-strategy-note（開 2 張，改判 1 本）

1. management `objectives-in-eight-key-areas`「單一目標的謬誤：事業目標的八個關鍵領域」— practice-of-management（docs/01-managing-a-business/04-objectives-of-a-business、docs/01-managing-a-business/05-todays-decisions-tomorrows-results）。
   第一鏟（management-by-objectives）掛 02-managing-managers 整部，寫自我控制；「目標要平衡涵蓋所有關鍵領域」只有一條 core。這本書在 drucker-note（MBO、what-is-a-business）與 management-note（purpose-of-business、marketing-and-innovation）共四頁，全掛 01/02 與 02 部，01/04 這章 22K 沒有任何站用。
   只寫 01/04：追尋單一目標為何「既不會有結果又必然有害」（只強調利潤會為今天犧牲未來）、關鍵領域的五個條件、八個領域（市場地位、創新、生產力、實體與財務資源、獲利能力、管理者績效與培養、工作者績效與態度、公共責任）、前五項無爭議後三項「無形」卻最快致死、衡量工具「比 IQ 還搖晃」只算進度報告、市場地位過高的風險、服務目標；05 只取「今天的決策、明天的成果」的時間跨度一段。
   避開 create-a-customer 與 management-note purpose-of-business 的「創造顧客」「我們的事業是什麼」三問（01/02、01/03 不掛）；避開 management-by-objectives 的自我控制與三個石匠。management-note purpose-of-business 第 57 行用一句話列了八個領域，seeAlso 連過去即可。
   claim 頁；related 連 management-by-objectives、create-a-customer、results-are-outside、the-effective-executive。

2. management `theory-of-the-business`「事業理論：三組假設、四項規格與五大致命罪」— managing-in-a-time-of-great-change（docs/01-management/01-theory-of-the-business、docs/01-management/03-five-deadly-business-sins）。
   第一鏟（knowledge-worker）掛 02-information-based-organization 整部，寫知識工作者；第一部「管理」六篇沒掛。drucker-note 導覽第三章說「事業理論已被 1954、1966、1985 三本覆蓋」，但全星系沒有一頁叫事業理論，grep 只命中那一句導覽。
   只寫 01/01：多數新管理工具是「怎麼做」而困境在「做什麼」、事業理論的三組假設（環境、使命、核心能力）、三個案例（洪堡的柏林大學、西門子的德意志銀行、三菱）、IBM 與 GM 兩個失效典型、有效理論的四項規格、四個預警信號（含「意外的成功」）、兩項預防措施（系統性放棄、研究非顧客）；01/03 五大致命罪只取第一罪（崇拜高利潤率，Xerox 與 GM 小車）與「高利潤率不等於最大利潤」的公式，其餘四罪一句帶過。
   避開 knowledge-worker 的資訊型組織；避開 strategic-inflection-point（Grove 的轉折點是同一現象的另一本書，related 連過去不重講）；drucker-note 沒有對口頁，seeAlso 連 drucker 的 management/what-is-a-business。
   claim 頁；related 連 knowledge-worker、create-a-customer、strategic-inflection-point、strategy-kernel。
   這本在 drucker-note 與 management-note 都在 2026-08-26 判 support（「訪談文章集體裁」）；本站開了這頁後兩頁引用，spine 站得住，不改判。

##### business-strategy-note 不開（1 本，改判）

- essential-drucker《杜拉克精選》：不開，**改判 tool**。drucker-note 判 tool、leadership-note 判 tool、management-note 判 support（「文選體裁切不出第二頁的論證」），本站導覽第三章自己也寫「當本組的總目錄讀」，那是查閱書的定位。順手修既有頁：create-a-customer 現掛的是 01-management 與 02-individual 兩整部，太粗；「創造顧客」原文在 practice-of-management 的 01-managing-a-business/02-what-is-a-business（grep 5 筆），精選本的對應章是 01-management/03-purpose-and-objectives-of-business（grep 3 筆）。改成主掛 practice 01/02、副掛精選 01/03。改完 practice-of-management 在本站被兩頁引用，自然從 DEEPEN-TARGETS 消失。

##### leadership-note（開 1 張）

1. culture `abstraction-kills`「抽象化殺人：Milgram、股東價值與鄧巴數」— leaders-eat-last（docs/05-the-abstract-challenge/13-abstraction-kills、docs/05-the-abstract-challenge/14-modern-abstraction、docs/05-the-abstract-challenge/15-managing-the-abstraction、docs/05-the-abstract-challenge/16-imbalance、docs/06-destructive-abundance/21-lead-the-people-not-the-numbers）。
   第一鏟（circle-of-safety）掛 01、02 兩部，Sinek 的內容只有安全圈與最後吃飯兩條 core，其餘是 Horowitz 與 Netflix。第五部「抽象的挑戰」四章沒掛。
   只寫：Milgram 1961 年實驗 65% 加到 450 伏特與距離對服從率的影響（13）、Friedman 1970 年股東至上把人變成成本項目、Apple 稅務策略（14）、管理抽象化的五條規則（保持真實聚在一起、遵守鄧巴數、認識你幫助的人、給時間不只給錢、七天七年的耐心）（15）、破壞性豐裕是多巴胺壓過催產素的失衡（16）；21 只取 Jensen 與 Meckling 1976 代理人理論與 Welch 的 rank and yank 當 14 的續集。
   避開 circle-of-safety 的安全圈與最後吃飯；避開 culture-is-behavior、freedom-and-responsibility（Horowitz 與 Netflix 各有自己的頁）；避開 belonging-cues 的 Coyle。
   claim 頁；related 連 circle-of-safety、culture-is-behavior、belonging-cues、intelligent-failure。

##### leadership-note 不開（1 本）

- turn-the-ship-around：不開，tier 維持 spine。leader-leader 掛第一、二部（請准我做改成我打算做），management-note 的 intent-based-leadership 掛第二部、competence-and-clarity 掛第三、四部（2026-11-06 第二鏟）。全書四部都有頁，leadership 這頭沒有剩下的章。順手補：leader-leader 的 core「控制要配上能力與清晰」只有一句，seeAlso 加 management 的 org-people/competence-and-clarity（路徑已存在）。

##### communication-note（開 1 張，改判 1 本）

1. persuasion `spot-fallacies-and-fouls`「修辭的防守：三個問題抓謬誤、一條規則判犯規」— thank-you-for-arguing（docs/03-defense/01-spot-fallacies、docs/03-defense/02-call-a-foul、docs/03-defense/03-know-whom-to-trust、docs/03-defense/04-find-the-sweet-spot）。
   第一鏟（rhetoric-toolbox）掛 02/02 時態與 02/03 三支柱，整頁是進攻篇；第三部防守四章（29K）沒掛。
   只寫：所有謬誤歸結為三個問題（證據站得住嗎、選擇數量對嗎、證據導向結論嗎）與邏輯謬誤在修辭裡「沒被抓到就過關、被抓到 ethos 就完了」（01）、唯一規則「永遠不要爭論無法爭論的事」、犯規的三條界線（把球帶走、踢人不踢球、拒絕碰球）、修辭允許的「好謬誤」如權力謬誤（02）、測騙器：無利害關係測試與「誰獲益最多」、媽媽買撞球桌（03）、實踐智慧的三個信號與「視情況而定」（04）。
   避開 rhetoric-toolbox 的三支柱、時態、讓步系技法；避開 influence-six-principles（那是心理學不是修辭）。thinking-note 沒有謬誤專頁（grep「謬誤」只命中偏誤頁的旁句），不加 seeAlso。
   claim 頁；related 連 rhetoric-toolbox、influence-six-principles、separate-story-from-facts、crucial-conversations-safety。
   第三鏟候選：04/03 修辭格（11K）與 04/04 時宜 kairos（6K），首頁的讓步技法表已用到兩個辭格，等這張落地再判重疊。
   順手修既有頁：rhetoric-toolbox 正文用了 02/01（西塞羅三個聽眾目標、Gottman）、02/05（ethos 三要素）、02/07（猶疑法）、02/10（共識）、02/12（省略推理），anchor 只掛 02/02 與 02/03。起草時一併補這五章進 furtherReading（事實在哪章就掛哪章，五個目錄都 `[ -d ]` 驗過）。

##### communication-note 不開（1 本，改判）

- speed-of-trust《高效信任力》：不開，**改判 delegated → covey**。covey-note 八頁（trust-economics、four-cores-of-credibility、thirteen-behaviors 三頁、smart-trust、restoring-trust，加 emotional-bank-account 引用）已把全書四部挖完；本站 social/speed-of-trust 是整本書的總覽頁，seeAlso 也已指向 covey 的 trust-and-execution 分類。再開第二頁只會重寫 covey 的某一頁。既有頁與導覽三處引用都不動，tier-audit 的 delegated 要姊妹站接住，covey 判 spine 八頁，接得住。

##### covey-note（開 2 張）

1. principles `three-kinds-of-power`「三種權力：強制、功利與原則中心」— principle-centered-leadership（docs/01-personal-and-interpersonal-effectiveness/09-principle-centered-power、docs/01-personal-and-interpersonal-effectiveness/11-thirty-methods-of-influence）。
   第一鏟（principle-centered-four-levels）掛序言、01/08 羅盤、01 與 02 兩整部、02/05 賦權六條件、02/16 憲章，寫羅盤對地圖、農場法則、四個層次、雙贏協議、憲章；權力三型沒碰。
   只寫 01/09：不問領導者問追隨者「為什麼追隨」、強制性權力出於恐懼（委身是表面的、威脅消失能量轉為破壞）、功利性權力出於交換（撐住多數組織卻導向個人主義、「買方自負其責」）、原則中心的權力出於信任與敬重（稀有、持續的主動影響）、「本質上的領導抉擇就是決定用哪一個權力基礎」、十項權力工具；01/11 只取影響的三個類別（以身作則讓人看見、關懷關係讓人感受、教導讓人聽見）當原則中心權力的操作面，三十種方法不逐條列。
   避開第一鏟的四個層次與羅盤；避開 four-cores-of-credibility（信用是權力的來源，related 連過去）；legacy/four-roles-of-leadership 是《第 8 個習慣》的道德權威，不同書，seeAlso 不必。
   claim 頁；related 連 principle-centered-four-levels、four-cores-of-credibility、emotional-bank-account、think-win-win。

2. principles `seven-chronic-problems`「七個慢性問題：急性痛底下的病」— principle-centered-leadership（docs/02-managerial-and-organizational-development/02-seven-chronic-problems、docs/02-managerial-and-organizational-development/03-shifting-your-management-paradigm）。
   第一鏟同上，02 部整部掛了但正文只用賦權與憲章兩章；02/02（19K）是本書組織診斷的核心章。
   只寫：急性病對慢性病、速成藥只治急性症狀、「有時需要動手術」、七個慢性問題（沒有共享的願景與價值、沒有策略路徑、糟糕的校準、錯誤的風格、技能不足、低信任、沒有誠信）各自的症狀與對應的習慣、「這些問題是可治癒的」；02/03 只取舊策略模型（目的、途徑、手段）對羅盤模型那一段，那是問題二的解法。
   避開第一鏟的四層次與農場法則（農場法則在這章也出現，只在點題句接一句）；避開 four-disciplines-of-execution；management-note 有 deming-fourteen-points，02/14 七習慣對戴明十四點不在這張，留作第三鏟候選。
   claim 頁；related 連 principle-centered-four-levels、three-kinds-of-power（第 1 張）、four-cores-of-credibility、transformational-interdependence。
   第三鏟候選：02/10 completed-staff-work（摩西與葉忒羅、為什麼不授權，13K）、02/14 七習慣與戴明（20K）。

##### growth-note（開 1 張）

1. deliberate-practice `intuition-as-higher-reason`「第三次轉化：直覺是理性的更高形式」— mastery（docs/07-fuse-intuitive-rational/01-the-third-transformation、docs/07-fuse-intuitive-rational/02-keys-to-mastery、docs/07-fuse-intuitive-rational/03-return-to-reality-and-environment、docs/07-fuse-intuitive-rational/05-fingertip-feel-and-life-force、docs/07-fuse-intuitive-rational/06-global-perspective-and-inside-out）。
   第一鏟（path-to-mastery）掛 02 天命與 03 學徒期，和 greene-note 的 mastery 頁掛同兩部；greene 另有 apprenticeship（03）、mentor-dynamic（04）、dimensional-mind（06）。第七部「直覺與理性融合」兩站都沒掛，第一鏟只有最後一條 core 一句「兩萬多小時深度浸泡後的質變」。
   只寫：Proust 從社交蝴蝶到軟木房的漫長潛伏（01）、直覺不是理性的對立而是更高形式（Fischer 的棋盤力場、Gould 的建築結構、Einstein 的視覺圖像）、古人叫它道、邏各斯（02）、加羅林群島導航者的多維感知（03）、Cesar Rodriguez 的技能層疊與沙漠風暴（05）、Freddie Roach 把手靶從輔助變核心、整體策略要內化（06）。
   避開 path-to-mastery 的天命、學徒期三階段、導師；避開 greene 的 dimensional-mind（第二次轉化、創造期）；避開 mental-representations 的 Ericsson（同一現象的實驗室版，related 連過去不重講）；07/04 Einstein 與 Grandin、07/07 歌德通才不寫，前者與 02 重疊、後者是通才論。
   claim 頁；related 連 path-to-mastery、mental-representations、inner-game-quiet-mind、purposeful-practice；seeAlso 連 greene 的 concepts/mastery/dimensional-mind。
   分工：growth 取心態與潛能（導覽第三章的三角分工），第七部講的是練到最後心智變成什麼，歸這站；第五部社會智慧（05，21K）兩站都沒挖，歸 greene-note，本單不開。

##### 小結

- 開 14 張，全部 claim 頁：relationships 4、maxwell 3、business-strategy 2、leadership 1、communication 1、covey 2、growth 1。沒有 debate：15 本都是單一作者體系書，站上沒有「一個問題多本書吵」且兩造都有頁的形狀。
- 不開 4 本：essential-drucker（改判 tool）、speed-of-trust（改判 delegated → covey）、turn-the-ship-around（四部都有頁）、bowling-alone 第五部（題材離站）。
- 兩站同書的分工：winning-with-people 主題站拿衝突兩條、人物站拿投資一整部；mastery 第七部歸 growth、第五部歸 greene；turn-the-ship-around 第三四部歸 management。
- 順手修既有頁（三筆 anchor 缺口，起草時一併做）：business-strategy create-a-customer 改掛 practice 01/02 主位；communication rhetoric-toolbox 補 02/01、02/05、02/07、02/10、02/12；leadership leader-leader 加 seeAlso 到 management competence-and-clarity。
- 既有頁越界（不在本單處理，留給 Opus 判）：leadership circle-of-safety 正文一半是 Horowitz 的震撼性規則與 Netflix 的高手密度，furtherReading 只掛 Sinek，而兩本書在本站各有自己的頁（culture-is-behavior、freedom-and-responsibility）；leader-leader 的 Goldsmith「別加太多價值」案例整段沒 anchor，書在 bibliography（what-got-you-here-wont-get-you-there）但沒掛。
- 起草順序建議：business-strategy 2（全星系沒有事業理論頁）、covey 1、leadership 1（材料最獨立）→ relationships 1、2（Perry 兩張一起讀第三、六部）→ maxwell 1、2 → relationships 3 與 maxwell 3 同一本書一起做 → business-strategy 1、communication 1、covey 2、growth 1。

#### hbr／career／hr／behaviour-interview 第二鏟選題單（DEEPEN-TARGETS 10 本，Fable 開單 2026-11-12）

判準取自 note-check §1.3 與 §1.4：只為脊梁書開頁，主張要標得到章節 anchor，與既有頁重疊低於一半，能被單獨引用；同一本書在姊妹站已有頁的，先查分工再開。
HBR Guide 是短文合輯，章多但每章一兩千字，第二頁要能站成一個主張，不是「再抄幾篇」；所以這批 HBR 的單一律合併相鄰章，單章撐不起的不開。
章節目錄全部 `[ -d <book>/site/content/<anchor> ]` 驗過（10 本共 88 個目錄，0 缺）；單上引號裡的字句全部 grep 過書 repo。

##### hbr-note（4 本：開 3 張、不開 2 本）

1. communication-collab `delivering-the-presentation`「登台之後：語調、肢體、問答與遠距簡報」— hbr-guide-to-persuasive-presentations（docs/06-delivery/05-tone、docs/06-delivery/06-be-yourself、docs/06-delivery/07-body-language、docs/06-delivery/08-voice、docs/06-delivery/09-stories-alive、docs/06-delivery/11-q-and-a、docs/06-delivery/12-remote-trust、docs/06-delivery/13-remote-listeners、docs/06-delivery/14-remote-checklist、docs/07-impact/01-social-relationships、docs/07-impact/03-gauge-connection、docs/07-impact/04-follow-up）。
   第一鏟（persuasive-presentations）只掛 03-story 一個卷層 anchor，正文卻寫了觀眾分析、大想法、現狀與理想、glance test、排練與怯場；第六部十四章只用了排練（01）與怯場（04），第七部一章未用。
   只寫：開口前的四個定調細節（事前溝通、氛圍、外表「配合觀眾或打成平手」、神態）、真實不是某一種風格（Ballmer 與 Susan Cain 兩極）、肢體五技巧與「肌肉記憶」、「七種聲音語調」與揪出語助詞、用感官細節重新體驗故事、Q&A 六法（規畫時機、預期問題、聽言下之意、不知道就承認、控場、留下最終印象）、遠距三章（鏡頭與站姿、六個拉回注意力的方法、八項清單與主持人）、「後通道」雙面刃與「鋼鐵般的胃」、七種跟進。
   避開第一鏟的觀眾功課、大想法、三段結構、glance test、排練與怯場；避開 10-interpreter（口譯合作，體裁太窄）與 07-impact/02-spread-ideas（社群散播，與站無關）；避開 communication-note 的 talk-like-ted（Gallo 的情緒、新奇、18 分鐘）與 slides-that-resonate（Resonate 的聽眾英雄與 sparkline），seeAlso 連 communication 站 presentation/talk-like-ted 即可。
   claim 頁；related 連 persuasive-presentations、run-meetings-that-matter、managing-up、authenticity-paradox。
   不開投影片設計頁（05-slides 十章）：那一部是 slide:ology 的濃縮版，communication-note 的 presentation/slide-design-ideology 已用原書寫完 slideument 光譜、三秒法則、圖解類型學、六件排列工具、資料五原則，再開就是跨站重覆；第一鏟補一條 seeAlso 連過去就好。

2. strategy-innovation `priorities-without-ranking`「優先順序不靠排名：關鍵、重要、期望，與該砍掉的殭屍專案」— hbr-guide-to-thinking-strategically（docs/05-priorities-tradeoffs/01-set-priorities、docs/05-priorities-tradeoffs/02-hands-off-manager、docs/05-priorities-tradeoffs/03-kill-outdated、docs/05-priorities-tradeoffs/04-conflicting-goals、docs/05-priorities-tradeoffs/05-manage-tradeoffs）。
   第一鏟（everyday-strategic-thinking）掛 01-get-started 與 02-understand-org-strategy 兩個卷層，core 寫的是取捨、向上一層、預留思考時段、問題框架；第五部五章一字未用。
   只寫：Lidow 反對排名的三個理由與目標／資源／時間三角（「資源至高無上」）、critical／important／desirable 三類與宣告 critical 等於開「空白支票」、四步驟資源矩陣；Su 的 contribution × passion 四象限（Prioritize／Tolerate／Elevate／Delegate）；Avery 的 Box 2 與「殭屍專案」（Telex 撐到 2008）、翻轉「舉證責任」讓專案證明自己還值得做、大中小三種尺度各自的砍法；Ashkenas 與 Manville 的執行策略四問（順序、頻寬、人才、再平衡）；取捨的六個提問與「有時取捨就是明確說不」。
   避開第一鏟的 Porter 取捨定義、向上一層、思考時段、「本週說了哪些 No」；避開 leadership-note vision/okr 的聚焦四超能力與 management-note managers-work/managerial-leverage 的槓桿率，seeAlso 連 leadership 站 vision/okr。
   claim 頁；related 連 everyday-strategic-thinking、what-is-strategy、better-decisions、manage-your-energy。

3. strategy-innovation `strategy-execution-gap`「策略到執行的斷層：Big Arrow、預算連動與 if-then 計畫」— hbr-guide-to-thinking-strategically（docs/07-execute-strategy/01-people-not-strategy、docs/07-execute-strategy/02-strategy-and-execution、docs/07-execute-strategy/03-bridge-the-gap、docs/07-execute-strategy/04-do-what-it-says）。
   第一鏟有一節「策略構想為何死在落地：計畫與行動的斷層」寫了四個斷點，沒有 anchor，導覽第四章 124 行已點名「那一段也沒有錨」；書裡講執行的是第七部四章，第一鏟沒用。
   只寫：Bregman 的「策略行動（strategic acting）」與 Big Arrow 六步驟（一個 pivotal strength、一個 game changer）、六問驗證；Leinwand 與 Rotering 的「只有 8%」領導者同時擅長策略與執行、Starbucks「第三個地方」綁在能力上、預算流程連回策略、用人話表達策略與三階段檢核題；Wiita 與 Leonard 的五件事（承諾認同、翻譯到日常、文化驅力、排序、塑造未來）與用會議議程自我檢核；Heidi Grant 的 If-Then 計畫（200 多項研究）、對群體迷思與沉沒成本的用法。
   避開第一鏟的日常習慣與數據素養那節；避開 leadership-note change/why-transformations-fail（Kotter 八步）；第八部三章（策略錯了、訊息矛盾、策略不清時中層怎麼辦）留第三鏟。
   claim 頁；related 連 everyday-strategic-thinking、leading-through-change、project-management-essentials、managing-up。
   附帶條件：新頁交付後，第一鏟那節「四個斷點」改成一行連到新頁；它的 core 第五點（事前驗屍、指定唱反調者、可逆／不可逆）與 TIP（「本週說了哪些 No」）、「策略絞肉機」「兩分鐘內講清楚」在書 repo 全書 grep 不到，列 B 型債：唱反調只出現在 01-get-started/01-essential-skills 與 05/04，決策那條以 04-align-decisions 三章（反思三問、七步 checklist、Data DIET）回源改寫，校正表進 SOURCING-DEBT。

不開（2 本）：
- hbr-guide-to-making-every-meeting-matter：第一鏟 run-meetings-that-matter 已走完會議全生命週期（該不該開、目標議程、主持規則、與會者技術、收尾追蹤、遠距），剩下第五部是會議型態變體（跨文化、站立、走路、站會）。唯一厚的是 08-leadership-summits（5.3k 字，Frisch 與 Greene 的大會設計十三步），單章撐一頁勉強、引用測試也弱，改以 `:::details` 補進既有頁並掛 anchor。tier 維持 spine，承諾已由既有頁兌現。
- hbr-guide-to-navigating-the-toxic-workplace：第一鏟 toxic-workplace 用了全書三十三章裡約二十章（五屬性、三種上司、走或留、復原、霸凌、男子氣概競賽、怪罪文化、毒性巨星），剩下 01/02 有毒同事、01/04 與 05/03 女性處境、04/04 打斷偏見、05/02 混合辦公、06/03 八卦、06/04 權力腐化，各一千字、湊不成一個主張。tier 維持 spine。

##### career-note（4 本：開 5 張、不開 1 本）

4. career-capital `operating-at-staff`「以 Staff 身分運作：做重要的事、對齊借來的權責、學會跟隨」— staff-engineer（docs/02-operating-at-staff/01-work-on-what-matters、docs/02-operating-at-staff/04-stay-aligned-with-authority、docs/02-operating-at-staff/05-to-lead-you-have-to-follow、docs/02-operating-at-staff/06-learn-to-never-be-wrong、docs/02-operating-at-staff/07-create-space-for-others、docs/02-operating-at-staff/08-build-a-network-of-peers、docs/02-operating-at-staff/09-present-to-executives）。
   第一鏟（staff-path-beyond-senior）掛 01-overview 卷層當「另一條路徑」，寫了四種原型與升遷工具箱一段；behaviour-interview 姊妹站的 big-tech/staff-plus 掛 01/01 原型與 04/02 面試 Staff 職位，story-mining/example-library 掛 05 兩篇訪談。第二部九章兩站都沒挖。
   只寫：三種絆腳石「吃零食」「擺姿態」「追鬼」與讓職涯步調配合人生；組織權責是「更高的組織權責借給你的」、「越過安全網」與「為總統效力」、永遠別讓主管意外；領導是看得見落差加在乎到願意行動，但「在學會跟隨之前，你無法成為長期有效的領導者」；「永遠不出錯」靠傾聽、定義目的、觀察全場，分享觀點前先問三個好問題；為他人「創造空間」（好討論是事後發現你不需要出席的討論；把它寫下來、未定案前先流傳）；同儕網絡的兩條路；向高階主管簡報為什麼難（「預處理過的現實」）與三種目的。
   避開第一鏟的三大支柱、四種原型、五種資源、回饋循環變長與升遷資料包；避開 behaviour-interview 站的 staff-plus 與 example-library（seeAlso 連 behaviour-interview 站 big-tech/staff-plus）；避開本站 find-a-sponsor-not-mentor 的贊助者論（第七張 create-space 提到 sponsorship 時只引一句）。
   claim 頁；related 連 staff-path-beyond-senior、career-capital-theory、find-a-sponsor-not-mentor、be-seen-smart-not-loud、impact-player-mindset。
   第三鏟候選：02/02-writing-engineering-strategy（「寫五份設計文件，把其中的共通點抽出來」）與 02/03-managing-technical-quality（9.7k 字），題域偏工程領導，若日後有技術站收這本書歸那邊，否則留本站。

5. manage-yourself `role-power-responsibility-unity`「職、權、責合一：績效考核為什麼要先看增值流程」— terry-cheng-workplace-power（docs/03-performance-review-and-management/18-kpi-or-okr、docs/03-performance-review-and-management/21-unity-of-role-power-responsibility-1、docs/03-performance-review-and-management/22-unity-of-role-power-responsibility-2、docs/03-performance-review-and-management/23-quantifying-role-power-responsibility、docs/03-performance-review-and-management/24-setting-department-performance-items）。
   第一鏟（tech-hiring-pipeline）掛 01 求職兩章；第三部績效考核十二章一字未用。管理站剛開的兩張程天縱單用的是另兩本書（專業力的策略規劃、經營學的真話假話），不撞。
   只寫：索尼「績效主義毀滅索尼」與他對「KPI 與 OKR 分別運用」說法的懷疑、「人的績效系統」；赫德在惠普五年的職權責合一改革；職務／權力／責任的定義、為何分離（分工太細、矩陣式管理）、「只要槍斃一個人，那個人會是誰」的當責測試、核決權限不是授權；用主要增值流程（產品產生、訂單產生、產品生產、訂單交付）量化合一程度與實線虛線；「笨蛋！問題在流程」、市場部考「抓取率」業務部考「打擊率」的拆解。
   避開 leadership-note vision/okr（Doerr 的四超能力與 CFR）與 grove-note 的 MBO，這頁只寫程天縱怎麼看 KPI／OKR 的共同缺口；避開 management-note principles/terry-cheng-rethinking 那條「職權責分離的白色空間」（只引一次並連過去）；避開 hr-note two-tails 與 nine-lies-about-ratings 的評等爭論。
   claim 頁，importance 3；related 連 first-year-manager、q12-and-four-keys、managing-oneself、tech-hiring-pipeline；seeAlso 連 leadership 站 vision/okr、management 站 principles/terry-cheng-rethinking。
   第三鏟候選：03/25–29 績效管理五個誤區（年度目標數字怎麼來、短中長期平衡）。

6. manage-yourself `all-round-professional-manager`「全能的專業經理人：權力缺口、成熟度與每晚一問」— terry-cheng-workplace-power（docs/02-capabilities/07-what-professional-managers-need、docs/02-capabilities/08-becoming-a-mature-professional-manager、docs/02-capabilities/09-stay-or-move-on、docs/02-capabilities/17-did-i-earn-my-salary-today）。
   第二部「能力」十一章第一鏟沒碰；10–16 章（誰扼殺了轉型、競爭力、方向）是組織診斷，歸管理題域，本站不開。
   只寫：NBA 三分球與灌籃大賽改變他對職業球員的定義（職業與業餘的差別在「全能」、能互相補位）、十個年輕人有九個答不出自家組織架構、組織政治就是填補「權力缺口」（需要一○○、企業只給六○）；對事的成熟度（time to maturity、依熟練度換管理模式、薪資區間）與對人的成熟度（後悔越來越少、身邊的人是老師）；離職面試只問「要去哪裡」不問「為什麼離開」、撿貝殼的職涯回顧、惠利特「即使員工離開了惠普，仍然認為惠普是最優秀的公司」；賺與賠的三個層次（交換、撿便宜、投資）與「我今天賺到我的薪水了沒」。
   避開 professionalism-customer-first（大前研一的專業四力）、managing-oneself（杜拉克）、seven-habits-inside-out；避開本站 find-a-sponsor-not-mentor；「成功不必在我」只在開頭引一次。
   claim 頁，importance 3；related 連 professionalism-customer-first、managing-oneself、first-year-manager、role-power-responsibility-unity（第 5 張）。

7. job-search-change `conference-commando`「研討會突擊隊：把會議、超級連結者與餐桌變成主場」— never-eat-alone（docs/02-the-skill-set/08-be-a-conference-commando、docs/02-the-skill-set/09-connecting-with-connectors、docs/03-turning-connections-into-compatriots/04-find-anchor-tenants-and-feed-them、docs/03-turning-connections-into-compatriots/03-pinging-all-the-time）。
   第一鏟（never-eat-alone）掛 01、02、03 三個卷層，寫的是慷慨、在需要之前先建好、做功課與跟進、健康財富與孩子、成為總機；第二部最厚的兩章（研討會 11.6k、閒聊 10k）與第三部的餐桌、保持聯絡都沒用。
   只寫：「大部分的仗，在第一槍之前就打完了」、研討會的投資報酬式評估、以為研討會是取得洞見的地方是誤解、「保齡球，還是球瓶」；「超級連結者」是任何網絡的基石與 Granovetter 的 56%／17%／55%／28%；「最強的連結是在餐桌上鍛造的」與「錨定房客」怎麼把圈外的人拉進晚宴；保持聯絡八成是重複、「唯一能穿透白噪音的東西」、把網絡分成 1、2、3 級。
   避開第一鏟全部 core；避開 hbr-note 的 smarter-networking（弱連結與三種人脈框架出自另一本書，seeAlso 連過去）；02/11 閒聊的藝術不寫，communication-note social/small-talk-to-connection 已用 Lowndes 寫過，seeAlso 連過去。
   claim 頁；related 連 never-eat-alone、job-search-system、alliance、givers-takers-matchers。

8. job-search-change `content-builds-trust`「內容建立信任：GVAC、機場問題與品牌廣播」— never-eat-alone（docs/04-connecting-in-the-digital-age/02-become-the-king-of-content、docs/04-connecting-in-the-digital-age/03-engineering-serendipity、docs/05-trading-up-and-giving-back/01-be-interesting、docs/05-trading-up-and-giving-back/02-build-your-brand、docs/05-trading-up-and-giving-back/03-broadcast-your-brand）。
   第四部數位時代與第五部品牌，第一鏟整部沒碰；這是 2014 增訂版新加的材料，與第一鏟的 2005 核心分得開。
   只寫：太空人 Hadfield 的推特與「信任的代數式」（慷慨＋脆弱＋當責＋坦率＝信任，GVAC）；「設計機緣」與「機運偏愛有網絡的心智」；顧問業的「機場問題」與沒有「理念平台」就會輸掉選舉；湯姆．彼得斯的「我股份有限公司」、白領革命「要嘛獨特，要嘛絕跡」；「你把工作做得多好，還不夠」與「戳破泡泡」。
   避開本站 be-seen-smart-not-loud（Jessica Chen 的策略性能見度與 4A）、linchpin（Godin 的禮物與出貨）、career-as-product（Chad Fowler 的行銷自己）；三頁各一句 related 連過去即可，這頁只寫費拉齊的內容與品牌打法。
   claim 頁；related 連 never-eat-alone、conference-commando（第 7 張）、be-seen-smart-not-loud、linchpin、career-as-product。
   第三鏟候選：03/02 社交套利（第一鏟已帶一句）、05/04 接近權力、04/01 開發邊緣地帶。

不開（1 本）：
- mastering-behavioral-interviews：behaviour-interview 姊妹站是整本書的體系深挖（41 頁引到它），本站 behavioral-interview-storytelling 是三本行為面試書合撐的總覽頁，導覽第三章 94 行已寫明「體系深挖在 behaviour-interview 姊妹站」。再開第二頁必是跨站重覆。tier 維持 spine（總覽頁引用它，承諾已兌現）。

##### hr-note（1 本：開 2 張）

9. retention-motivation `development-is-retention`「發展就是留才：職涯對話的黃金時機、任務交換與導師制度」— hbr-guide-to-retaining-your-best-people（docs/04-development/01-professional-development、docs/04-development/02-talk-about-career-development、docs/04-development/03-task-trading、docs/04-development/05-young-remote-employees、docs/06-reinvent-retention/03-mentoring-program）。
   第一鏟（why-people-stay）掛十一章：序言、為什麼離職、重新想像、問快不快樂、被重視、明星待遇、不升遷也能激勵、說出感謝、敬業度、留任獎金、乾升遷；第四部發展五章與第六部的導師制度沒用。
   只寫：專業發展是員工心中改善文化的第一名（LinkedIn 2022）與「教練文化」是和留任最相關的實踐（Deloitte，支出 1.5–3 倍）；職涯對話的黃金時機是到職 12–18 個月、問對問題與設計小型實驗；「任務交換」把團隊從工具箱變成「一群瑞士刀」的四步驟與會失敗的原因；年輕遠距員工的五個挑戰與「反向指導」「跟班學習」；指導計畫普及卻失效的原因與轉成留才工具的四策略。
   避開第一鏟的進展四型、留任對話六步、乾升遷與留任獎金；避開 04/04 生成式 AI 學習（工具條目）；避開 tours-of-duty（Hoffman 的任期制）與 four-keys-of-great-managers（蓋洛普四把鑰匙），related 連過去。
   claim 頁；related 連 why-people-stay、tours-of-duty、four-keys-of-great-managers、autonomy-mastery-purpose。

10. retention-motivation `b-players-and-high-performers`「B 級球員與高績效者：各自需要什麼才留得住」— hbr-guide-to-retaining-your-best-people（docs/03-motivate-and-engage/03-retain-b-players、docs/03-motivate-and-engage/02-high-performers-feedback、docs/05-adjust-work/01-protect-from-burnout）。
   第一鏟用了第三部的 01 明星待遇、04 不升遷、05 感謝，跳過 02 高績效者回饋與 03 B 級球員；第五部防倦怠也沒用。
   只寫：「只雇用 A 級」的迷思與 Google「亞里斯多德計畫」看見的 B 級價值、B 級最常停滯是不相信自己被允許挺身而出、五個策略；高績效者更在乎你說的話、主管的盲點與五個行動（不省略建設性回饋、不用「總是」「從不」、不針對個性、留意刻板印象、畫出成長路徑）；三個讓高績效者倦怠的做法（永遠分到最難的專案、補低績效者的洞、零碎小事）與三個保護策略（偶爾自選專案、「高績效者配對」、追蹤額外時間需求）。
   避開第一鏟的明星待遇與感謝四要素；避開 two-tails（Google 兩端是評等制度，這頁是主管的留才動作）、radical-candor-quadrants（回饋象限）、psychological-safety；hbr-note self-management/beating-burnout 是個人視角，seeAlso 連過去。
   claim 頁；related 連 why-people-stay、two-tails、radical-candor-quadrants、receiving-feedback。

第三鏟候選（不開，記著）：05/02 工作再造＋05/04 工作外的熱情＋06/06 更快樂的職場（彈性與歸屬）；01/03 入職定成敗（四個 C，單章 1.9k 字太薄，可補進 recruiting 分類既有頁）；02/03 內在目的五問＋06/05 目的是磁鐵（可與 culture-people-ops/mission-transparency-voice 分工後再開）。

##### behaviour-interview-note（1 本：不開，建議體裁排除）

- soft-skills-thirty-letters《軟技能》：不開。這是得到三十位作者各寫一封信的合輯（羅振宇序；萬維鋼、吳軍、香帥、施展、薛兆豐、劉潤、李希貴、湯君健、熊太行、梁寧⋯⋯），每封兩到四千字、各自獨立、沒有單一論旨，與 EXCLUDED_KINDS 裡「5分鐘商學院 工具篇：工具條目合輯，每條各自獨立」同一種體裁，建議加進 `export-deepen-targets.py` 體裁排除（理由：多作者書信合輯，三十封各自獨立）。本站 big-tech/cultural-boundary 已用湯君健與熊太行兩封信寫成對照頁，導覽三章都掛了；career 與 wujun 兩站 delegated 到本站，漏接檢查過得了。tier 維持 spine。

##### 順手發現的既有頁問題（交 Opus 一起修）

- hbr `strategy-innovation/everyday-strategic-thinking`：core 第五點（事前驗屍、指定唱反調者、可逆／不可逆）、TIP「本週說了哪些 No」、「策略絞肉機」、「兩分鐘內講清楚」與整節「四個斷點」，在書 repo 全書 grep 不到，是 B 型債；處理法寫在第 3 張附帶條件，校正表進 SOURCING-DEBT。
- hbr `communication-collab/persuasive-presentations`：正文用了 01-audience（七問）、02-message（大想法）、05-slides/02-three-second-test、06-delivery/01-rehearse、06-delivery/04-stage-fright，anchor 只掛 03-story；照「事實在哪章就掛哪章」補五條。並補 seeAlso 連 communication 站 presentation/slide-design-ideology 與 presentation/slides-that-resonate。
- hbr `communication-collab/run-meetings-that-matter`：anchor 只掛 docs/01-prepare，正文寫了 02-conduct（沉默等於同意、jellyfish）、03-participate（婉拒與插話句術）、04-close-follow-up（三件事、Roses & Thorns），補三個卷層 anchor；順便把 05-specific-types/08-leadership-summits 以 details 收進來。
- hbr `communication-collab/toxic-workplace`：anchor 四條，正文用到 01-harmful-environment（有毒或只是一份工作、找 HR）、03-quit-or-stay（過渡期、復原四步）、04-managing-toxic-team（心理安全感、招募把關）、05-culture-toxicity（霸凌、男子氣概競賽、怪罪、好好文化），補四個卷層 anchor。
- career `job-search-change/never-eat-alone`：三個卷層 anchor 合規；但 core 第四點「忠誠孕育在健康、財富與孩子」實際在 03/01，第五點「成為總機」在 03/02，起草第 7、8 張時順手把卷層 anchor 細化到章。

##### 小結

- 開 10 張，全部 claim 頁：hbr 3、career 5、hr 2；沒有 debate，這批都是單一作者或單一合輯的材料，沒有「一個問題多本書吵」的形狀。
- 不開 4 本（making-every-meeting-matter、toxic-workplace、mastering-behavioral-interviews、soft-skills-thirty-letters），tier 都不動；《軟技能》建議進體裁排除。
- 姊妹站分工：投影片設計歸 communication 的 slide:ology 頁；Staff Engineer 的原型與面試歸 behaviour-interview，第二部運作歸 career；KPI／OKR 的 Doerr 版歸 leadership，程天縱的增值流程版歸 career；閒聊歸 communication 的 Lowndes 頁。
- 起草順序建議：2、3（連帶清 everyday-strategic-thinking 的 B 型債）→ 4 → 9、10 → 1 → 7、8 → 5、6。
- 沒把握的兩張：第 6 張（程天縱第二部四章各自成篇，合成一頁的黏著度要靠「專業經理人」這條線，起草代理若判材料散就只寫 07＋17 兩章）；第 10 張（三章合計 5.6k 字，是這批最薄的一張，排在第 9 張之後）。
- 旁註：hbr 站的 Guide 系列第一鏟普遍只掛一兩個卷層 anchor、正文卻掃全書，四頁裡三頁有 anchor 缺口；這是站級型態，起草這批時順手補，之後值得對 hbr 站整站跑一次 export-anchor-gaps.py。

#### wellness／habits／tools／life-meaning 第二鏟選題單（DEEPEN-TARGETS 11 筆，Fable 開單 2026-11-12）

判準取自 note-check §1.3 與 §1.4：只為脊梁書開頁，主張要標得到章節 anchor，與既有頁重疊低於一半，能被單獨引用；體裁查閱型（日課、訪談合輯）一頁夠就不開。
四站 11 筆裡兩筆是同一本書在兩站（Bigger Leaner Stronger 在 wellness 與 life-meaning），War of Art 另在 writing 站有候選，分工都寫明。
每張單寫明第一鏟掛了什麼、第二鏟只寫什麼、避開哪幾頁；章節目錄名全部 `[ -d ]` 驗過（46 個 anchor 全部存在）；單上引的原話逐一 grep 過書 repo。

#### wellness-note 第二鏟選題單（5 本）

##### 開單（6 張）

1. fitness-body `rules-that-change-the-rules`「改變規則的十條法則：Ferriss 的自我實驗方法」— 4-hour-body（docs/01-principles/01-minimum-effective-dose、docs/01-principles/02-rules-that-change-rules、docs/02-ground-zero/02-elusive-body-fat）。
   第一鏟（form-and-injury-prevention）只掛 07-fixing-injuries/03-prehabilitation，而且頁的主體是 Manocchia 的暖身與伸展，Ferriss 只佔「預防重於修復」一條；exercise-as-leverage 的 details 已寫了 MED 與 100°C 燒開水的例子，furtherReading 卻沒掛這本書（要補 anchor，見旁註）。
   只寫：MED 的定義與身體改造的兩個關鍵 MED（Arthur Jones 的遺產）；十條法則各一句（運動消耗的熱量少得可憐、藥物就是藥物、目標設在 10 公斤改造、飲食／藥物／訓練計算尺的 60／10／30、黏貼測試「能堅持的次佳方法，勝過必須放棄的完美方法」、休閒不等於訓練、相關不等於因果的三個問題、衝浪式進食、肯亞選手的快縮肌纖維、行銷話術用「能不能測量」刪掉）；體重計會騙人、該測量什麼（02/02）。
   避開 exercise-as-leverage 的漸進超負荷與複合動作，「最小有效劑量勝過過度訓練」那條只引不展開；避開 form-and-injury-prevention 的 prehab；Occam 協議（04-building-muscle）留第三鏟，這頁只講方法論不講課表。導覽第三章說他「不是科學家」，概念頁不下這個評語，只照書寫第七條規則。
   claim 頁；related 連 exercise-as-leverage、form-and-injury-prevention、titans-health-toolbox、healthspan。

2. nutrition-sleep `slow-carb-diet`「慢碳飲食：五條規則與每週一天的作弊日」— 4-hour-body（docs/03-fat-loss/01-slow-carb-diet-i、docs/03-fat-loss/02-slow-carb-diet-ii、docs/03-fat-loss/03-damage-control）。
   第一鏟與第 1 張都不碰減脂部；書自己說減脂是「最容易成功、最容易看見變化」的實作章，七章裡前三章就是方法本體。
   只寫：五條規則（避開白色碳水、反覆吃同樣的東西、不喝液體熱量、不吃水果、每週一天放假全力作弊）；卡路里陷阱（一碗飯 300 卡對一碗菠菜 15 卡，靠豆類補熱量）；FAQ 裡的判別點（牛奶的胰島素反應指數比 GI 高 3 到 6 倍、作弊日後 48 小時內的水分、量圍度不量體重、鉀鎂鈣三種電解質）；暴食損害控制那一章的作法。數字逐字照書；「上千人平均減去 9.5 公斤」這類數字要標明是作者的追蹤，不是對照試驗。
   避開 nutrition-foundations 的能量平衡與依從性（那是第 3 張的題）、避開 daily-dozen 的植物性論證與 nutritionism；減醣那一側在同站（江部），不必 seeAlso。
   claim 頁；related 連 nutrition-foundations、daily-dozen、nutritionism、rules-that-change-the-rules（第 1 張）。

3. nutrition-sleep `flexible-dieting`「靈活飲食：熱量、蛋白質、80／20 與三套數字」— bigger-leaner-stronger（docs/04-nutrition-advice/01-flexible-dieting、docs/04-nutrition-advice/02-counting-calories-macros、docs/04-nutrition-advice/05-cheat-meals、docs/02-debunking-fitness-myths/04-fat-loss-myths）。
   第一鏟（exercise-as-leverage）掛 01、02 兩部，寫的是訓練端；書的公式「飲食決定體脂，訓練決定肌肉」的飲食端整部沒碰。
   只寫：四根支柱不是拼圖碎片；靈活飲食四步驟（控制熱量、足夠蛋白質、未加工食物為主、找到碳水與脂肪的平衡）；80／20；減脂／精實增肌／維持三套數字（赤字 20 到 25%、盈餘約 10%、每磅體重的大卡與蛋白質克數）；分層建構飲食計畫（先蛋白質）；減脂十大迷思表裡的三條（熱量進出不是過時理論、代謝損傷不存在、少量多餐無助減重）；作弊餐的作法。
   **附帶條件（B 型債，起草前先處理）**：nutrition-foundations 現掛江部《快速瘦肚！間歇性斷食減醣全書》02、03 兩章，但頁上的核心主張「能量平衡決定體重的大方向」「各種斷食減醣有效，多半是因為幫人減少了總攝取，不是違反了能量守恆」「蛋白質是最該顧好的營養素」「依從性是隱藏變數」在江部那兩章裡都找不到，江部講的正好相反（「吃得多也能瘦：和卡路里苦行說再見」「重點不是熱量，而是有沒有醣」）。這些句子是 Matthews 的主張掛錯了書。處理：這張單把能量平衡那一側寫成 Matthews 的頁；nutrition-foundations 回江部原文重寫成減醣的理由（不算熱量、脂肪不是敵人、從葡萄糖體質切換為脂肪燃燒體質、血糖飆升、一日兩餐、三大減醣等級），標題改掉「基本盤」；導覽第四章官司一第三層那兩句（「長期的能量平衡與一套你能持續執行的模式勝過任何單一神奇飲食法」「各種斷食減醣有效，多半是因為幫人減少了總攝取」）改成 Matthews 的話並連到新頁。校正表進 SOURCING-DEBT。
   避開 exercise-as-leverage 的訓練三角、避開第 2 張的慢碳規則；重寫後的 nutrition-foundations 與這頁是官司一的兩造（熱量對醣），不互相重講。
   claim 頁；related 連 exercise-as-leverage、nutrition-foundations、slow-carb-diet（第 2 張）、daily-dozen。

4. stress-mental-health `not-a-zero-sum-life`「人生不是零和：四面向的小實驗、成人的下課時間與分散自我」— hbr-guide-to-managing-stress（docs/03-richer-life/01-better-leader-richer-life、docs/03-richer-life/02-work-taking-over、docs/03-richer-life/04-grown-ups-recess、docs/03-richer-life/07-diversify-yourself）。
   第一鏟（managing-stress-and-burnout）掛 01、02 兩部，寫的是壓力生理、耗竭三面向與「能量而非時間」；第三部「更豐富的人生」七章一字未用。
   只寫：弗里德曼的取捨思維對整合（工作、家庭、社群、自我四面向，Reflect／Brainstorm／Choose 三步，小實驗的篩選標準，四面向滿意度提升 20% 到 39%、績效進步 9%）；科金代爾的「能者過勞」與三步（每週工時上限 50 到 55 小時、「不要做」清單、對老闆與自己說不）；成人的下課時間清單；布雷格曼的「分散自我」（法國電信 24 名員工自殺、Rosenfield 那句「只透過工作建立身份，會限縮你的自我感」、多重身份要有行動才算數）。
   避開 managing-stress-and-burnout 的恢復節律與耗竭三面向、避開 mental-health-at-work；03/05 睡眠那章不寫（站上已有兩頁睡眠）；hbr-note 的 manage-your-energy 是這本書的第二部，seeAlso 連過去即可。
   claim 頁；related 連 managing-stress-and-burnout、mental-health-at-work、meaning-as-medicine、what-makes-a-good-life。
   第三鏟候選：06-rest-and-recovery 五章（週末症候群三成因、每週一天在家工作、午睡的競爭優勢、企業菜園、公司能做什麼），是公司層級的設計題，若開頁也落 stress-mental-health。

5. stress-mental-health `food-and-mood`「飲食與憂鬱：花生四烯酸、MAO 與番紅花」— how-not-to-die（docs/01-preventing-and-reversing-disease/12-suicidal-depression）。
   第一鏟（daily-dozen）的 anchor 掛在兩部的部層級，正文用的是心臟、糖尿病、高血壓三章；十五個死因章只動了三個。
   只寫：卡內基美隆的感冒病毒實驗（負面情緒組三人中一人感冒、快樂組五人中一人）；花生四烯酸與神經發炎（身體自製、不必再從飲食攝取；阿斯匹靈與布洛芬的作用點就在這裡）；植物性飲食者的 POMS／DASS 分數；單胺理論與 MAO（阻斷 MAO 的藥有「起司效應」，蘋果、莓果、洋蔥、綠茶與丁香肉桂等香料天然抑制 MAO）；種子與血清素；番紅花對百憂解的直接比較（百憂解組約 20% 性功能障礙、番紅花組無）；杜克大學的運動對舍曲林試驗（含在家自己運動的第三組）；咖啡與阿斯巴甜；抗氧化物與葉酸；FOIA 文件揭露 FDA 知道 Paxil、Prozac 效果沒比安慰劑好多少。瑪格麗特的信可當開場，標明是讀者來信。
   避開 daily-dozen 的紅綠燈與十二清單、避開 cognitive-distortions（認知層）與 stress-physiology；這頁是營養書落在心理區，分類放 stress-mental-health 是刻意的。
   claim 頁；related 連 daily-dozen、cognitive-distortions、managing-stress-and-burnout、exercise-and-the-brain。

6. nutrition-sleep `heart-healthy-is-brain-healthy`「對心臟好的也對大腦好：中風、阿茲海默與飲食」— how-not-to-die（docs/01-preventing-and-reversing-disease/03-brain-diseases）。
   只寫：九成中風是缺血性、無聲中風的累積；纖維每天多 7 克中風風險降 7%、97% 的美國人纖維不足、童年就開始累積（二十四年追蹤）；鉀與柑橘類；抗氧化物排行榜；阿茲海默「無法治癒，但可以預防」、阿茲海默醫師 1901 年就記下奧古斯特的動脈硬化、血管疾病假說與六十五歲腦血流少 20%；全球十倍差距（賓州鄉間 19 對印度鄉村 3）、移民研究（日裔美國人、奈及利亞對印第安納波利斯低四倍）、日本動物性脂肪 1961 到 2008 年增近 600%、素食三十年以上失智風險低三倍；ApoE4（七分之一的人帶一份、三倍、九倍）與「奈及利亞悖論」；莓果與綠葉菜；AGEs。
   避開 daily-dozen 已寫的心臟與糖尿病逆轉、避開 why-we-sleep 的腦部清除；數字密，起草代理每個數字回源。
   claim 頁；related 連 daily-dozen、nutrition-foundations、healthspan、exercise-and-the-brain。
   第三鏟候選：15-iatrogenic-disease（醫源病是第三大死因、醫師洗手遵從率不到四分之一、輻射、「阿斯匹靈：吃植物不是吃藥丸」、大腸鏡的三種篩檢）是書裡最尖銳的一章，但站上沒有分類承接「醫療本身的代價」；若要開，落 fitness-body 與 healthspan 並列。

##### 不開（1 本）

- tools-of-titans：不開。第一鏟 titans-health-toolbox 已把 01-healthy 十一位受訪者整部攤成選單；02-wealthy 是創業與投資題（不在本站題域），03-wise 十一位（Jocko、Naval、Sam Harris、BJ Miller、Brené Brown）再開只會是第二份選單。體裁是訪談語錄合輯、一人一條目、按人物查閱，導覽第三章已寫明「當菜單抄，不當教條讀」。tier 維持 spine。建議加進 `export-deepen-targets.py` 的 EXCLUDED_KINDS：「訪談語錄合輯，一人一條目」（同體裁的 Tribe of Mentors 章節數不到門檻，暫不列）。

##### 小結

- 開 6 張（4HB 2、BLS 1、HBR 壓力指南 1、How Not to Die 2），全部 claim 頁；不開 1 本，tier 不動，建議進體裁排除。
- 第 3 張附帶一筆 B 型債：nutrition-foundations 的能量平衡論掛錯書（江部書裡講的相反），起草前回原文重寫並進 SOURCING-DEBT；重寫後與第 3 張正好是導覽官司一的兩造，日後若要開 debate 頁「減脂算熱量還是算醣」，兩造頁都在站上了（Ferriss 第 2 張是第三造：規則 1 明說「卡路里進、卡路里出說不通」）。
- 旁註（既有頁漏掛 anchor，不必等第二鏟）：exercise-as-leverage 的 details 用了 4HB 的最小有效劑量與 100°C 燒開水，furtherReading 沒掛 4-hour-body → 補 docs/01-principles/01-minimum-effective-dose/。
- 起草順序：3（含重寫 nutrition-foundations 與導覽第四章改句）→ 2、1 → 5、6 → 4。

#### habits-note 第二鏟選題單（4 本）

##### 開單（3 張）

1. productivity `four-elements-of-focus`「一年該聚焦在哪：優勢、弱點、差異與熱情的交集」— 18-minutes（docs/02-what-is-this-year-about/01-when-you-dont-know-what-to-do、docs/02-what-is-this-year-about/02-reinvent-the-game、docs/02-what-is-this-year-about/03-take-the-shrimp、docs/02-what-is-this-year-about/04-heated-seats、docs/02-what-is-this-year-about/05-pilot-who-saved-155、docs/02-what-is-this-year-about/07-recipe-for-right-work、docs/02-what-is-this-year-about/08-what-matters-to-you）。
   第一鏟（weekly-planning-18-min）掛 03/08 的 18 分鐘儀式與 02/13 的年度焦點，年度焦點只在 core 一條裡當「漏斗」帶過；第二部前十二章沒用。
   只寫：沒有計畫時先靠四個元素出發、年度焦點落在四個元素的交集上（02/01）；發揮優勢（02/02 重新發明比賽）、擁抱弱點（02/03 我就拿蝦子）、突顯差異（02/04 加熱座椅）、熱情的四個面向（慾望 02/05 拯救 155 人的機長、自在 02/07「放棄一部分」的求職配方、意義 02/08 美國時間使用調查的 8.68／7.78／3.45 小時與臨終者最常後悔的兩件事）。
   避開 weekly-planning-18-min 的三段儀式與好儀式四條件；避開 big-rocks-first、wildly-important-goals（別本書）；第一部 Pause 的「FIND ME 按鈕」只作一句引入。
   claim 頁；related 連 weekly-planning-18-min、big-rocks-first、wildly-important-goals、own-your-168-hours。
   第三鏟候選：04-what-is-this-moment-about 十八篇（精通分心、精通主動、精通界線），與 focus 區三頁的重疊要再量。

2. discipline `territory-versus-hierarchy`「領地還是階序：藝術家用什麼定義自己」— war-of-art（docs/03-beyond-resistance-the-higher-realm/09-territory-versus-hierarchy、docs/03-beyond-resistance-the-higher-realm/07-the-ego-and-the-self、docs/03-beyond-resistance-the-higher-realm/10-the-supreme-virtue、docs/03-beyond-resistance-the-higher-realm/11-the-artists-life）。
   第一鏟（resistance-and-turning-pro）掛第一、二部；writing 站同名頁掛同兩部；第三部「更高的領域」兩站都沒碰。
   只寫：個體用兩種方式定義自己，階序為何是預設值；階序在規模上崩潰（二十人到大約八百人的部落、紐約太大）；對藝術家而言用階序定義自己是致命的，「寫手」是用階序的方式寫作（McKee 的定義）、《重返榮耀》的反例；領地的五個性質（提供養分、沒有外部輸入也維繫我們、只能獨自佔有、只能靠工作取得、精確返還你投入的東西）；自我與本我各自相信什麼（07）；至高美德是對失敗的蔑視、克里希那的「擁有勞動的權利，但不擁有勞動果實的權利」（10）；這個問題只能用行動回答（11）。
   避開第一、二部的抗拒與職業者準則；繆思、天使、開始與持續的魔法（03/01、02、04、05）歸 writing 站（見下）；seeAlso 連 writing 的 craft-mindset/resistance-and-turning-pro。
   claim 頁；related 連 resistance-and-turning-pro、identity-based-habits、callus-the-mind、never-finished。
   給 writing 站的分工建議：writing 拿繆思那一面，開 `craft-mindset/invoking-the-muse`「召喚繆思：上工前的禱詞、開始的魔法與誰在替你修稿」（docs/03-beyond-resistance-the-higher-realm/01-angels-in-the-abstract、02-invoking-the-muse、04-the-magic-of-making-a-start、05-the-magic-of-keeping-going，視需要加 03-testament-of-a-visionary、06-life-and-death；四個目錄都驗過存在）。寫作實務的那一面都在那幾章：加州小屋二十六個月與「今天就開始下一本」、健行帶口袋錄音機「誰在替我們修稿」、莫瑞的「投身其中的那一刻天意也隨之移動」。領地對階序歸 habits，writing 頁用 seeAlso 連過來；related 可連 daily-practice、writers-block、perfectionism-and-fear（都在 writing 站 craft-mindset 底下）。

3. productivity `procrastination-and-overload`「拖延與超載：現時偏誤的六招、來不及的七個戰術」— how-to-have-a-good-day（docs/02-productivity/04-beating-procrastination、docs/02-productivity/03-overcoming-overload）。
   第一鏟（design-your-day）掛 introduction 與 07-energy，正文其實用到 01/01 的三個 A 與 06/01 的貼標籤、拉開距離、腹式呼吸（anchor 要補，見旁註）；第二部生產力四章沒用。
   只寫：連諾貝爾獎得主都會拖延與現時偏誤；六招（把好處畫進腦海、規劃短期獎勵、把第一步綁在喜歡的事上、放大「不做」的代價、預先承諾、問五個為什麼）；超載的七個戰術（正念暫停、把記憶外包、問「最重要的一件事」、「最小的第一步」、比較利益、「正向地說不」的四步驟、劃出界線）。
   避開 make-distraction-hard 的預先承諾（Eyal 版）與 hooked-model 的五個為什麼（也是 Eyal）：這兩招只在 Webb 的版本上寫一句、related 連過去；避開 02/01 單工與 02/02 刻意休息（timeboxing、deliberate-rest 已各有頁）。
   claim 頁，importance 3；related 連 design-your-day、make-distraction-hard、make-it-tiny、willpower-science。
   三張裡最薄的一張，技巧清單體；排最後，可砍。
   **裁決（主會話）**：不開。技巧清單體，兩招是 Eyal 的轉述而原典頁已在；design-your-day 的 anchor 缺口照旁註補。進已裁定清單。

##### 不開（1 本）

- 365-days-with-self-discipline：不開。體裁是日課（52 週、每週七則、每則數百字的每日短文），第一鏟 discipline-is-freedom 掛序言與第一週，已把全書的命題（走難的路、選擇的漣漪效應、意志力肌肉、設計系統勝過仰賴自制）寫完，其餘五十一週是同一命題的每日變奏，再開只會是語錄選。tier 維持 spine。建議加進 EXCLUDED_KINDS：「日課型，365 則每日短文按週合輯」（philosophy 的 Daily Stoic 是同一體裁，那本因章節數不到門檻沒進榜）。

##### 小結

- 開 3 張，全部 claim 頁；不開 1 本，tier 不動，建議進體裁排除。
- 與 writing 站分工：War of Art 第三部拆成兩面，habits 拿領地對階序，writing 拿繆思；兩頁互連。
- 旁註（既有頁漏掛 anchor，不必等第二鏟）：design-your-day 正文的三個 A 來自 docs/01-priorities/01-choosing-your-filters/，貼標籤／拉開距離／腹式呼吸來自 docs/06-resilience/01-keeping-a-cool-head/，三件好事與峰終來自 docs/07-energy/01-topping-up-the-tank/（現掛 07-energy 部層級，祖章可接受；前兩章要補）。
- 起草順序：2 → 1 → 3。

#### tools-note 第二鏟選題單（1 本）

##### 開單（2 張）

1. focus-attention `autotelic-self`「自成目的的自我：把威脅轉譯成挑戰的四條規則」— flow-psychology-of-happiness（docs/09-cheating-chaos/01-tragedies-transformed、docs/09-cheating-chaos/02-coping-with-stress、docs/09-cheating-chaos/03-power-of-dissipative-structures、docs/09-cheating-chaos/04-autotelic-self-a-summary）。
   第一鏟（flow-challenge-skill-balance）掛 02、03、04、07 四章，連第七章工作的弔詭都用了；第九章「欺騙混沌」整章沒碰。
   只寫：「最優經驗是健康與財富之上的糖霜」的反駁；米蘭研究三群（下半身癱瘓者、視障者、街頭流浪者）；災難的兩條岔路（摧毀自我，或提供一個新的更迫切的目標）、三種抗壓資源（外部支持、心理資源、應對策略）、四十歲被解雇的 Jim；耗散結構（普里高津、火）、轉化技能在青春期晚期形成（健康的青少年平均只沮喪半小時）；自成目的的自我的四條規則（設定目標、沉浸於活動之中、留意正在發生的事、學會享受當下的經驗）與「還缺最後一步」。
   避開既有頁的精神熵、八個成分、黃金比例、自成目的的人格（04/03 的 Hamilton 與 Rathunde 已在既有頁）；「心智統御身體」那段的整體醫學引述（卡辛斯、席格）只點名不展開。
   claim 頁；related 連 flow-challenge-skill-balance、deep-work-value、lead-through-noise、finitude-four-thousand-weeks。

2. focus-attention `taming-solitude`「獨處為什麼難：沒有外在結構時的週日早晨」— flow-psychology-of-happiness（docs/08-enjoying-solitude-and-other-people/01-conflict-between-being-alone-and-with-others、docs/08-enjoying-solitude-and-other-people/02-pain-of-loneliness、docs/08-enjoying-solitude-and-other-people/03-taming-solitude）。
   只寫：被排除在人際之流外的恐懼（拉丁文「活著」是 inter hominem esse、放逐僅次於處死）；「他人即地獄」的矛盾怎麼解；最糟的心情發生在「獨自一人、且沒有任何事需要做」、獨居且不上教堂的人週日早晨最低落；三種逃避策略（電視、藥物、性與自我傷害）與代價；終極測試「獨處時你做什麼」、青少年時期與資訊時代；馴服獨處（Dorothy 的島、Susan Butcher、「結構時間比結構空間更重要」）。
   避開既有頁第七章的「閒暇的 52% 落在冷漠區」（這頁從獨處切入，不重講工作對閒暇）；08/04 家庭與 08/05 朋友不寫（關係題，歸 relationships 站）；digital-minimalism、internal-triggers 的獨處論是 Newport 與 Eyal，related 連過去不重講。
   claim 頁；related 連 flow-challenge-skill-balance、digital-minimalism、internal-triggers-indistractable、hyperfocus-and-scatterfocus。

##### 小結

- 開 2 張，全部 claim 頁。
- 結構旁註：Flow 在 career、growth、learning、wellness、life-meaning 五站都判 delegated，tools 接住，但 tools 的分類只有專注、習慣、筆記、時間，第十章「意義的形成」（目的的培養、人生主題）沒有分類承接，是 life-meaning 的題卻 delegated 出去了。建議 life-meaning 把 flow 改回 support 並在導覽帶一句，或自挖一頁 10-the-making-of-meaning，否則那章永遠沒人寫。第六章「思想的心流」（閱讀、文字遊戲、業餘科學、終身學習）是 tools 的第三鏟候選。
- 起草順序：1 → 2。

#### life-meaning-note 第二鏟選題單（1 本）

##### 不開（1 本）

- bigger-leaner-stronger：不開。life-meaning 的 progressive-overload 掛 05-exercise-advice 整部，與 wellness 的 exercise-as-leverage 是同一命題的兩個版本；這本書的第二鏟（飲食端）歸 wellness（見 wellness 第 3 張），life-meaning 的 body-wellness 區不收飲食頁。03-fitness-mindset 五章是 McGonigal 意志力三面向與 Duhigg 習慣迴路的轉述，habits 站已有原典的頁。tier 維持 spine，承諾由既有頁兌現。DEEPEN-TARGETS 會一直列它，這是工具不記「不開」判斷的限制。

#### 四站總結

- 開 11 張（wellness 6、habits 3、tools 2），全部 claim 頁，沒有 debate：這批都是單一作者的方法書，「一個問題多本書吵」的形狀只在 wellness 的減脂題出現，但要等第 3 張與 nutrition-foundations 重寫完才有兩造頁。
- 不開 3 本（Tools of Titans、365 Days、life-meaning 的 BLS），tier 都不動。
- 建議加進 `export-deepen-targets.py` EXCLUDED_KINDS 兩本：tools-of-titans「訪談語錄合輯，一人一條目」、365-days-with-self-discipline「日課型，365 則每日短文按週合輯」。
- 一筆 B 型債（wellness nutrition-foundations，能量平衡論掛在講相反話的江部書上）與兩筆既有頁漏掛 anchor（wellness exercise-as-leverage 補 4HB 的 MED 章；habits design-your-day 補 01/01 與 06/01）。
- 起草順序建議：wellness 3（先清債）→ habits 2、tools 1 → wellness 2、1、5、6 → tools 2、habits 1 → wellness 4 → habits 3。

#### thinking／startup／writing／templar／newport 第二鏟選題單（DEEPEN-TARGETS 11 本，Fable 開單 2026-11-12）

判準取自 note-check §1.3 與 §1.4：只為脊梁書開頁、主張標得到章節 anchor、與既有頁重疊低於一半、能被單獨引用；體裁先判。這批 11 本裡有四本是「一條一則」的條目合輯（思考的藝術 99 則、Rework 近 90 節、Rules of Management 107 條、How to Win at College 75 條），每本先問「有沒有一組相鄰條目撐得起單一主張」，撐不起的不開；撐得起但站上已有同一主張的也不開。章節目錄全部 `[ -d ]` 驗過；單上引的原話全部回書 repo grep 過，查不到的改寫成「書裡講到」。

##### 開單（9 張）

**writing-note（4 張）**

1. nonfiction-copy `reports-vs-stories`「報導與故事：關鍵問題、內部懸崖與路上的金幣」— writing-tools（docs/03-blueprints/02-learn-the-difference-between-reports-and-stories、docs/03-blueprints/07-generate-suspense-use-internal-cliffhangers、docs/03-blueprints/08-build-your-work-around-a-key-question、docs/03-blueprints/09-place-gold-coins-along-the-path、docs/03-blueprints/12-report-and-write-for-scenes、docs/03-blueprints/13-mix-narrative-modes、docs/03-blueprints/16-write-toward-an-ending）。
   第一鏟（nuts-and-bolts）只開第一箱「螺絲與螺帽」，第三箱「藍圖」十六件工具一件沒用；導覽第五章說「第一箱已開頁」。
   只寫 Clark 給新聞寫作者的敘事工具：報導給資訊、故事給經驗（工具 02 的 IMPORTANT 框原話「一個用來呈現資訊，另一個用來呈現經驗」）、把 5W1H 解凍成故事、故事需要一具引擎（一個由行動為讀者解答的問題）、內部懸崖「要推動讀者前進，就讓他們等待」、金幣「用高潮點獎賞讀者，尤其是在中段」與記者把好料全搬到最上面的劣勢、場景是敘事文學的基本單位、「斷線」形式混合敘事模式、朝結尾寫「幫助讀者閉合意義的圓」。
   避開 nonfiction-structure（McPhee 的「結構從素材長出來」）、story-as-persuasion 與 unexpected-and-curiosity（Heath 的好奇心缺口是同一機制的另一本書，只在 related 連）、story-shape 與 scene-turns（McKee 的判準）；工具 03「對話是行動的一種形式」與站上 dialogue-as-action（McKee）同題，不重講；工具 06 伏筆只點一句。
   claim 頁；related 連 nuts-and-bolts、nonfiction-structure、unexpected-and-curiosity、scene-turns、story-shape。

2. style-clarity `ladder-of-abstraction`「抽象之梯：何時上、何時下、狗的名字」— writing-tools（docs/02-special-effects/12-climb-up-and-down-the-ladder-of-abstraction、docs/02-special-effects/04-get-the-name-of-the-dog、docs/02-special-effects/06-seek-original-images、docs/02-special-effects/10-choose-the-number-of-elements-with-a-purpose-in-mind、docs/02-special-effects/13-tune-your-voice）。
   第一鏟只開第一箱；第二箱「特殊效果」十三件工具一件沒用。
   只寫梯子的三個位置與「學會何時該展示、何時該講述、以及何時兩者並用」、「去問那隻狗的名字」的重點是好奇心不是想像力與細節的說服功能、陳腔濫調是思考的替代品與「拒絕第一層創意」、元素的數量（一是力量、二切分世界、三是完整、四以上是清點）、聲音的測試是「把故事大聲讀出來」。
   避開 concrete-over-abstract（Heath 的「具體勝於抽象」是單向的，這頁的主張是梯子兩端都要、死區在中段，起草時明寫這個差別）、sentence-rhythm 與 nuts-and-bolts 已講的句長與標點（工具 08、09 不掛）、characters-and-actions。
   claim 頁；related 連 nuts-and-bolts、concrete-over-abstract、sentence-rhythm、exposition。

3. story-structure `structure-as-perception`「結構為什麼存在：排序是一種感知行為」— into-the-woods（docs/03-the-forest/01-showing-and-telling、docs/05-home-again-changed/04-home-again、docs/05-home-again-changed/05-why）。
   第一鏟（five-act-map）掛第一、二部，寫的是五幕、中點、改變的路線圖、碎形與 Snyder 的節拍表；導覽第三章寫了「Yorke 給的不是第三條路」的判詞，但「為什麼是這個形狀」在站上沒有頁。
   只寫三件事：庫勒雪夫效應與「二加二的統一理論」（觀眾自己算出四，電視草創期為何背棄這種語言）、第四部「給對立面平等的權利」（主題就是那場論證、一個故事只值它的反論那麼好、主題會自己浮現）、第五章「為什麼」（七種說故事的常見解釋被「如果九成的囚犯喝茶，我們不能下結論說茶要為九成的犯罪負責」懸置；「排序是一種感知行為，而正是這個行為給了我們敘事、修辭與戲劇」；「坎伯沒有發現神話結構，他發現的是故事結構」、「單一神話的核心單位，其實不過就是一場戲」，三句都在 05-why 逐字找得到）。
   避開 five-act-map 的五幕與中點、monomyth（坎伯自己的語法，這頁只寫 Yorke 對坎伯的翻案，related 連過去讓兩造並列）、exposition（McKee 的「讓交代隱形」只在講到展示與講述時點一句）、storytelling-brain（Storr 的預測腦是另一本書的機制論，不混）。
   claim 頁；related 連 five-act-map、monomyth、storytelling-brain、premise-and-theme、exposition。第三鏟候選：第五部一到三章的電視結構（迷你影集一集就是一幕、影集為什麼撐不過三年），約一萬六千字，等站上有影視線再開。

4. craft-mindset `invoking-the-muse`「召喚繆思：上工前的禱詞、開始的魔法與誰在替你修稿」— war-of-art（docs/03-beyond-resistance-the-higher-realm/01-angels-in-the-abstract、docs/03-beyond-resistance-the-higher-realm/02-invoking-the-muse、docs/03-beyond-resistance-the-higher-realm/03-testament-of-a-visionary、docs/03-beyond-resistance-the-higher-realm/04-the-magic-of-making-a-start、docs/03-beyond-resistance-the-higher-realm/05-the-magic-of-keeping-going；五個目錄 `[ -d ]` 驗過）。
   第一鏟（resistance-and-turning-pro）掛第一、二部整部；habits-note 同名頁掛的也是第一、二部，兩頁已互 seeAlso。第三部「超越抗拒」兩站都沒碰，本輪拆成兩面：habits 拿 06–11 的身分論（領地對階序，見 habits 單第 2 張），writing 拿 01–05 的工作面。
   只寫：天使與繆思是 Pressfield 自己對「靈感從哪來」的說法（抽象中的天使、每天上工前念的荷馬禱詞）、加州小屋二十六個月與寫完第一本就「今天開始下一本」、健行帶口袋錄音機與「誰在替我們修稿」、莫瑞那句投身其中的那一刻天意也隨之移動（三件在章裡都 grep 到）、開始的魔法與持續的魔法。
   避開第一鏟的抗拒性格與職業者準則；避開 habits 第 2 張的領地對階序、自我對本我、對失敗的蔑視（06–11 不掛）；finding-your-voice（Lamott）與 daily-practice 的實務只在 related 連。
   claim 頁；related 連 resistance-and-turning-pro、daily-practice、writers-block、perfectionism-and-fear（craft-mindset 底下實存）；seeAlso 連 habits 站 discipline/territory-versus-hierarchy（habits 第 2 張落地後再掛）。
   **裁決（主會話）**：fork 原單開的是 `territory-versus-hierarchy`（03/06–10），與 habits fork 撞題；依「身分論歸 habits 的 discipline、工作面歸 writing 的 craft-mindset」拆分，原單作廢。

**thinking-note（2 張）**

5. affect `temperament-is-not-destiny`「氣質不等於命運：創傷的再學習與害羞孩子的杏仁核」— emotional-intelligence（docs/04-windows-of-opportunity/02-trauma-and-emotional-relearning、docs/04-windows-of-opportunity/03-temperament-is-not-destiny）。
   第一鏟（emotional-hijacking）掛第一部第二章與第二部一到五章，寫的是視丘直達杏仁核的捷徑、五個領域、糖果測驗、宣洩的謬誤；第四部「機會之窗」三章一章沒用，而書站概覽指出的全書內部張力（糖果測驗被當成「可習得」的證據，第四部卻說氣質有生理基礎）正落在這兩章。
   只寫：斯托克頓校園槍擊後孩子自發玩起的「玩普迪」與恐懼怎麼被刻進記憶、創傷後壓力症作為邊緣系統的障礙與再學習的三階段、凱根的四種氣質類型與害羞對大膽那條軸、「膽怯的孩子遺傳上具有較高濃度的正腎上腺素或其他活化杏仁核的腦內傳導物質」、湯姆與拉爾夫、八到九個月大出現陌生人恐懼、以及為什麼童年可塑所以氣質不等於命運。
   避開 emotional-hijacking 的捷徑解剖與五領域、somatic-markers、constructed-emotion；第四部第一章「家庭的熔爐」（父母的三種情緒錯誤與情感教練）屬親職題域不掛；第三部婚姻章（高特曼四道警訊）歸 relationships-note（那站收了 Gottman 原典）。
   claim 頁；related 連 emotional-hijacking、primal-emotion-systems、constructed-emotion、somatic-markers。life-meaning-note 已把這本 delegated 給 thinking，不必另判。

6. judgment-bias `why-smart-people-do-dumb-things`「為何聰明人也會做蠢事：誤判寫在解剖與演化裡」— seeking-wisdom（docs/01-introduction、docs/02-what-influences-our-thinking/01-our-anatomy-sets-the-limits-for-our-behaviour、docs/02-what-influences-our-thinking/02-evolution-selected-the-connections-that-produce、docs/02-what-influences-our-thinking/03-adaptive-behaviour-for-survival-and-reproduction）。
   第一鏟（numbers-and-evidence）掛第三篇物理與數學整篇；導覽第三章說「取其數學面」。第一篇「什麼影響我們的思考」是書站概覽點名的本書對 Parrish 的差異（能回答偏誤為什麼存在），站上沒有頁從演化講誤判的來源。
   只寫 Bevelin 的因果鏈：改變解剖結構就改變行為（Gage、Whitman 的腫瘤壓迫杏仁核）、突變與天擇、痛苦與愉悅是導航系統、自利是最底層特徵而合作只在符合自利時穩定（囚犯困境）、恐懼與快速分類在狩獵採集環境是有效策略在現代才變錯誤，收在 02/03 的「為何聰明人也會做蠢事」一節。
   避開 numbers-and-evidence 的全部、two-systems（康納曼的架構，這頁不用系統一二的詞）、primal-emotion-systems（Panksepp 的七個系統）、common-thinking-errors 的清單；第二篇二十八種傾向不掛（與 Dobelli 頁、predictable-irrationality、prospect-theory 重疊過半）；第四篇十二條指南也不開，反向思考與檢查清單已在 mental-models-toolkit（Super Thinking）。
   claim 頁；related 連 numbers-and-evidence、common-thinking-errors、two-systems、primal-emotion-systems。

**startup-note（2 張）**

7. growth-scale `when-to-stop-blitzscaling`「何時開始、何時停止：閃電擴張的四個領先指標與創辦人的換檔」— blitzscaling（docs/03-strategy-innovation/01-when-should-i-start-to-blitzscale、docs/03-strategy-innovation/02-when-should-i-stop-blitzscaling、docs/03-strategy-innovation/03-can-i-choose-not-to-blitzscale、docs/03-strategy-innovation/06-how-the-role-of-the-founder-changes-in-each-stage）。
   第一鏟（blitzscaling）掛第一、二、四、六部，寫了定義、四象限、五階段、成長因子與限制、九條規則與責任；第三部「策略創新」整部沒掛，而書站概覽說「何時該停的四個領先指標」是全書最負責任的設計。
   只寫：開始前要丟掉哪些正常商業規則（01 的對照表）、「你在市場很大、或成長很快時閃電擴張；如果你的市場停止成長、或觸及上限，你就該停止」、四個領先指標（成長率下滑相對市場與對手、以及 02 列的其餘三項）、耗盡頂部空間的症狀是內部衝突與業務副總被拿來背鍋、Twitter 2014 年底「該鬆開油門、聚焦效率的訊號」、亞馬遜對 The French Laundry（逾 541,900 人對不到 50 人）說明可以選擇不閃電、創辦人在五個階段各做什麼（親手拉槓桿、管理拉槓桿的人、……）。
   避開第一鏟的定義與象限、九條規則、火場分流；grow-fast-or-slow 的 Masters of Scale 逃逸速度只在 related 連；第五部「防守閃電擴張」是在位者視角，不掛，留給 business-strategy-note 或第三鏟。
   claim 頁；related 連 blitzscaling、grow-fast-or-slow、wartime-vs-peacetime-ceo、persevere-or-pivot。

8. team-culture `delegate-dont-abdicate`「授權不是退位：三百三十萬美元的教訓」— anything-you-want（docs/04-communication-and-management/04-delegate-or-die、docs/05-legacy-and-exit/03-my-mistake、docs/05-legacy-and-exit/05-trust-but-verify、docs/05-legacy-and-exit/06-delegate-dont-abdicate）。
   第一鏟（purpose-over-money）掛 01/02 指南針，寫的是意義、烏托邦、being 不是 having；第四、五部的授權與治理這條線沒碰，而書站概覽的第一條限制正是「唯一一次系統真的壞掉，書的回應是退出而不是修正哲學」。站上沒有頁講創辦人的授權。
   只寫：2001 年八名員工時所有事情都經過 Derek、每五分鐘一個問題的授權陷阱、不讀文件就簽名的習慣怎麼在四年後變成 CD Baby 成了別人的公司與 330 萬美元、數位發行那個「每張專輯、每家公司、每一週、無論如何都要送到」的唯一要求怎麼被簽了字的人放掉、過度授權（辦公室怎麼布置、健保方案投票決定）之後發生什麼、授權與退位的分界。
   避開 purpose-over-money 的指南針與四條規則、enough-as-strategy 與 finish-big-patterns 的退場；05/07「我知道我做完了」與 05/08 捐給慈善不掛（那是退場題，不是授權題）。
   claim 頁，importance 3；related 連 purpose-over-money、take-care-of-your-people、work-on-not-in-the-business、first-who-then-what。這是九張裡最薄的一張：四章合計不到四千字；起草者若寫不出八百字以上的正文，改成在 purpose-over-money 加一個 details，不勉強開頁。
   順帶一筆要修既有頁：purpose-over-money 正文的 CD Baby 四條規則在 01/04-make-a-dream-come-true、「報名跑馬拉松不會想搭計程車到終點線」與 being 對 having 在 05/01-being-not-having，anchor 卻只掛 01/02，起草時一併補這兩章。
   **裁決（主會話）**：不開新頁。四章不到四千字，頁會是來源的六成；改成在 purpose-over-money 加一條 details「授權不是退位」並掛上面四章 anchor，連同 01/04、05/01 一次補。

**templar-note（1 張）**

9. work `on-the-companys-side`「站在公司這邊：對上司、同儕與部門戰爭的不成文規矩」— rules-of-management（docs/02-managing-yourself/79-let-company-see-you-are-on-its-side、docs/02-managing-yourself/80-dont-bad-mouth-your-boss、docs/02-managing-yourself/81-dont-bad-mouth-your-team、docs/02-managing-yourself/82-accept-bosses-will-be-wrong、docs/02-managing-yourself/83-accept-bosses-are-scared-too、docs/02-managing-yourself/89-dont-back-down、docs/02-managing-yourself/90-dont-play-politics、docs/02-managing-yourself/91-dont-criticize-other-managers、docs/02-managing-yourself/93-dont-intimidate、docs/02-managing-yourself/94-be-above-interdepartmental-warfare、docs/02-managing-yourself/95-fight-to-the-death-for-your-team、docs/02-managing-yourself/96-aim-for-respect）。
   第一鏟（manage-the-process-not-the-people）掛兩部卷層，寫的是第一部宣言，第二部只在一個 details 裡點了 80、81、90、94、95 各一句；導覽第五章明寫「《管理的法則》管自己的 70 條還沒開頁」，書單 note 說這本要補的是「教科書略過的不成文規範」，79 到 96 這一組就是。
   只寫這十二條：讓公司看見你是自己人的具體動作（買股票、編內部通訊）、不說上司與團隊的壞話、接受上司也會錯（拒絕執行或辭職之外的選項）、「老闆也是人」會恐懼會偏執、堅定但不具攻擊性（「不需要咄咄逼人，只需要堅定」）、不玩政治、不批評其他主管、「絕不用職位來壓人」、超越部門戰爭但為團隊拼死戰鬥、追求的是尊重。
   避開第一鏟的宣言與第一部、85「表現得像上一級的人」（與 Rules of Work 的 act-one-step-ahead 同一主張，不掛）、67 紀念牌匾（第一鏟已用）、keep-it-under-your-hat 的印象管理。
   claim 頁；related 連 manage-the-process-not-the-people、act-one-step-ahead、difficult-people、understand-before-influence。leadership-note 已把這本 delegated 給 templar，不必另判。

##### 不開（3 本）

- art-of-thinking-clearly《思考的藝術》（thinking-note）：不開。99 則各自獨立的短文，每則一千餘字，是他人實驗的轉譯（泰特洛克、康納曼、Asch），而站上已有那些原典的頁（two-systems、prospect-theory、forecasting-as-skill、how-false-beliefs-form）；書自己說它拒絕組織、要的是隨手翻查。唯一不是轉譯的材料是後記（熱理論對冷理論、演化解釋、米開朗基羅的負面知識，約兩千字），重疊測試落在「補進既有頁」：建議在 common-thinking-errors 加一個 details，不開新頁。tier 維持 spine。**建議進 EXCLUDED_KINDS**，體裁理由：近百則互不相承的偏誤短文，每則是他人研究的轉譯。
- rework《工作大解放》（startup-note）：不開。格言體雜文集，近九十節多數一兩頁（書站概覽原話），導覽第三章已判「101 章雜文集，一頁抓主軸即兌現」。逐部看過：第九部雇人（12 節，約七千字：痛了才雇、履歷是笑話、面試價值有限、試工）是唯一撐得起單一主張的一組，但站上 hire-for-attitude 與 first-who-then-what 已占這個位置；第八部行銷的「建造受眾、用教學勝出」是書站概覽指出的不可複製資產（Rails），是導覽層的判讀不是概念頁。tier 維持 spine。**建議進 EXCLUDED_KINDS**，體裁理由：格言體雜文集，近九十節各一兩頁、書自己拒絕給流程只給立場。
- how-to-win-at-college《大學生勝出的 75 個祕訣》（newport-note）：不開。75 條各自獨立，兩條原則（睡眠是不可協商的邊界、把義務換成排定的時間區塊）在站上都已有更成熟的版本：時間分塊、五十分鐘區塊、工作進度日誌（12、22、52）在隔年《如何成為全 A 學生》重寫過一遍，pseudo-work 一頁已承接；「別經營人脈、深耕一件事、大計畫」（11、16、66）已是 career-capital-over-passion 的「學生版」一節；測驗與回想法（70）屬 learning-note 題域，那站有提取練習的頁。要做的只有一筆 anchor 補掛：career-capital-over-passion 的「先變得值得認識」若正文用到 66，補 docs/66-dont-network。tier 維持 spine。不建議進 EXCLUDED_KINDS：條目可以成組，是選題判斷不是體裁。

##### 小結

- 開 9 張，全部 claim 頁，沒有 debate：十一本都是單一作者的書，沒有「一個問題多本書吵」的形狀。
- 不開 3 本，tier 都不動；兩本建議進 `export-deepen-targets.py` 的 EXCLUDED_KINDS（思考的藝術：轉譯型偏誤短文合輯；Rework：格言體雜文集），How to Win at College 與 Rules of Management 同是條目合輯但可以成組，不排除。EXCLUDED_KINDS 若收了前兩本，要在 docstring 寫清楚判準是「每則互不相承且全書無主軸」，不是「條目式」本身，否則 templar-note 整站都會被排除。
- 起草順序建議：writing 1、2（Clark 每件工具三到四千字，材料最厚）→ writing 3（Yorke 三章三萬字）→ thinking 5（EQ 兩章兩萬五千字）→ startup 7 → thinking 6 → writing 4 → templar 9 → startup 8（最薄，有退路）。
- 順手要修的既有頁 anchor（事實在哪章就掛哪章）：startup purpose-over-money 補 01/04 與 05/01（見第 8 張）；writing nuts-and-bolts 正文用到工具 2、3、4、6、7、8（2-3-1 強調、主動被動三條拇指法則、-ing、128 字長句、模式加轉折），anchor 只掛 01、05、09、10，補掛 `docs/01-nuts-and-bolts/` 箱層或那六章。
- 姊妹站分工：War of Art 第三部歸 writing、第一二部兩站各留一頁不動；EQ 婚姻章歸 relationships（有 Gottman 原典）；Blitzscaling 第五部的防守視角留給 business-strategy 或第三鏟；Rules of Management 第 85 條不重講 Rules of Work 的 act-one-step-ahead。

#### travel-note 第二鏟選題單（DEEPEN-TARGETS 14 本，Fable 開單 2026-11-12）

判準取自 note-check §1.3 與 §1.4：只為脊梁書開頁，主張要標得到章節 anchor，與既有 40 頁重疊低於一半，能被單獨引用。
這站的 14 本候選全在 2026-09-26 Batch 3 各開過一頁，目的地書那一頁多半就是「領隊講解底氣」的全部；第二鏟只為兩種情況開：工藝書還有整部沒碰（podcast 兩本、Grammar of the Shot、Murch、Steves、Holloway），或目的地書裡有一條團會走到、第一鏟沒寫的主張線（芬蘭極光線、華東線、柏林、紐西蘭的今天、阿布辛貝、荷比西葡與奧塞的美術館）。
14 本都只有 travel-note 收（podcast-producer-guide 在 marketing-note 判 tool、零頁），沒有姊妹站分工問題；seeAlso 只在下面點名的既有路徑上掛。
章節目錄名全部 `[ -d ]` 驗過；單上沒有引任何原話，只用書 repo 的章節標題與頁上已有的事實。

##### 開單（16 張）

1. podcast `interview-episodes`「訪談集：北極星、訪綱與預期管理」— podcast-producer-guide（ch02-blueprint-for-building-each-episode/s26-how-to-plan-an-interview-episode、ch02-blueprint-for-building-each-episode/s27-tips-for-interview-episodes）；alternative 掛 so-you-want-to-start-a-podcast（04-cast-it/01-get-the-guests-you-want、04-cast-it/02-prepare-guests-and-yourself、04-cast-it/03-first-rate-interview）。
   第一鏟（episode-blueprint）掛 ch02 的 s21、s23、s24、s25、s210，寫的是單集結構元素、開場白、單口的四種大綱骨架；訪談集與來賓一字未提。
   只寫粘瀚文的訪談集流程：用北極星引導訪談方向（含《敏迪選讀》《大人的 Small Talk》兩個案例）、訪綱怎麼準備、讓來賓自己介紹自己、付費訪談要講「人」不只講品牌、訪綱裡容易忽略的小事（三個名稱、播出日期、排版）、錄前的預期管理（長度、主持人習慣、哪些錯可以犯、認識環境）、按錄音鍵前別聊太多、把來賓的稿子放到旁邊、翻譯成聽眾懂的語言、講錯怎麼接、為來賓做總結；Meinzer 的三章只當對照：來賓三類（一般人、專家、名人）與邀約信、預訪做不做、九個讓訪問更順的做法。
   避開 episode-blueprint 的結構元素與單口骨架、show-positioning 的十字描述與聽眾化身、writing-for-the-ear 的為耳朵寫；主持人該是誰、多人節目的角色分配歸第 2 張。
   claim 頁；related 連 episode-blueprint、show-positioning、hosting-and-co-hosting（第 2 張）、writing-for-the-ear、travel-narrative-craft。

2. podcast `hosting-and-co-hosting`「主持像你自己：口音、脆弱、共同主持與角色分配」— so-you-want-to-start-a-podcast（03-host-it/02-host-like-a-pro、03-host-it/03-consider-co-host、03-host-it/04-art-of-co-hosting、03-host-it/05-co-host-conflict）；alternative 掛 podcast-producer-guide（ch02-blueprint-for-building-each-episode/s22-who-should-be-the-host、ch02-blueprint-for-building-each-episode/s28-planning-multi-host-episodes）。
   第一鏟（writing-for-the-ear）只掛 Meinzer 的 02-write-it/04-prepare-to-script；第三部「主持」整部沒用。
   只寫 Meinzer 的主持課：口音與氣泡音別理批評、最重要的一條是聽起來像你自己（主持人要不要中立、適度展現脆弱）、十個主持技巧、共同主持的四個好處與怎麼找人、「是的，而且」規則與五個技巧、不合從極端到隱微、盡力了還是不行就結束；粘瀚文那兩章當對照：單口的好處、多人別超過四個、個人品牌自己主持而企業品牌由主管級主持、團隊夥伴主持的優缺點、多人節目的角色分配（知識、專業、立場、個性）、節奏與內梗。
   避開 writing-for-the-ear 的「主持人也是素材」與艾拉降音高（那是念稿，這頁是主持人格與搭檔）、避開 episode-blueprint 的「主持人喜歡最重要」一句；來賓與訪綱歸第 1 張。
   claim 頁；related 連 interview-episodes（第 1 張）、writing-for-the-ear、episode-blueprint、show-positioning。
   對旅行社的落點明確：企業品牌由主管主持、領隊當共同主持或來賓，書裡有依據，起草時放在「套用」段，不當主張。

3. podcast `one-transcript-many-outputs`「一稿多用：從逐字稿出發的內容行銷飛輪」— podcast-producer-guide（ch06-brand-promotion-strategy/s62-build-your-content-marketing-funnel-to-attract-and-convert-audiences、ch06-brand-promotion-strategy/s63-create-your-content-marketing-flywheel-combo）。
   第一鏟與第六章無關；行銷站判 tool 也沒開頁，全星系沒有任何頁講內容行銷漏斗或飛輪（grep 過）。
   只寫：內容行銷漏斗是什麼、各平台特性與「自然流量／長尾流量」兩個觀察指標、以文字／影片／圖文哪種媒材為主、知識濃度越高越能收費、基本與進階漏斗兩個範例、Podcast 適合「黏著」潛在客戶；再寫飛輪：三大部分、為什麼文章與 Podcast 最適合當起點、一稿多用三步驟（逐字稿 → 各平台文案 → 各平台媒材）、組合技依喜歡／擅長／「鈔」能力選、建議的發展順序。s57 裡「Youtube 要發嗎／Podcast 搭配 Youtube」若用到，anchor 補掛 ch05-publishing-and-first-impressions/s57-choosing-publish-times-define-your-release-strategy。
   避開 seven-cs-channel-strategy 的七 C 與「頻道是電視台」、youtube-algorithm-and-retention 的演算法機制、show-positioning 的定位；這頁只講一趟素材怎麼拆成多個平台的產出。
   claim 頁，importance 4；related 連 episode-blueprint、seven-cs-channel-strategy、youtube-algorithm-and-retention、documentary-story-design、travel-narrative-craft。
   旅行社正好是「一趟團 → 電視節目、YouTube、Podcast、部落格」的形狀，套用段可以直接對應，但數字與順序只用書的。

4. travel-video `shot-sizes-and-framing`「景別與構圖：團員入鏡怎麼框」— grammar-of-the-shot（01-shots-what-how-and-why/03-introduction-to-shot-types、01-shots-what-how-and-why/04-extended-family-of-basic-shots、02-basics-of-composition/01-framing-human-subjects、02-basics-of-composition/02-camera-angle、02-basics-of-composition/03-two-shot、03-composition-beyond-basics/02-use-of-lines、03-composition-beyond-basics/03-depth-of-film-space）。
   第一鏟（shooting-for-the-edit）掛 05 整部、01/05、07 整章，寫的是涵蓋鏡頭、銀幕方向、180 度與 30 度法則、對應鏡頭與視線匹配、早開機晚停機、拍攝比、連戲陷阱；第一、二、三章的景別與構圖一個字都沒用。
   只寫：三大基本鏡頭與九種景別、同一鏡頭的資訊與主題兩層意義、頭頂空間、主觀與客觀拍攝、視線空間與質量平衡、三分法、水平角度（正面到背面五種）與垂直角度（高低中性）、雙人鏡頭四種取景（側面、正對、過肩、髒單人）與權力關係、地平線與垂直線、荷蘭角、對角線與消失點、前中後三層深度與刻意遮蔽。07 的 11（頭頂空間）、16（重要的東西放上半部）、17（干擾物）若用到，anchor 補掛 07-working-practices（兩頁同掛一章可以，事實在哪章就掛哪章）。
   避開 shooting-for-the-edit 的 180／30 度、跨剪接點的視線匹配（這頁的「視線空間」是一個畫格之內的留白，不是兩個鏡頭之間的呼應，起草時寫清楚）、連戲與拍攝比；鏡頭焦距與運鏡歸第 5 張。
   claim 頁；related 連 shooting-for-the-edit、lens-and-camera-movement（第 5 張）、cutting-for-emotion、learning-to-see-a-place；seeAlso 掛 design 站 visual-basics/concord-conflict-contrast（路徑實存，同是構圖的對比原則）。

5. travel-video `lens-and-camera-movement`「鏡頭與運鏡：透視、對焦、搖攝與推軌」— grammar-of-the-shot（03-composition-beyond-basics/05-camera-lens、06-dynamic-shots/03-blocking-talent、06-dynamic-shots/04-camera-in-motion、06-dynamic-shots/05-equipment-to-move-camera）。
   第一鏟沒碰第六章；07 的 22（鬆開雲台跟拍）、29–32（長鏡頭、鏡頭中變焦、推軌動機、短焦減少手持晃動）在既有頁的 anchor 裡但正文沒寫。
   只寫：鏡頭做的三件事、定焦與變焦、廣角擴張與望遠壓縮、人眼不會變焦、對焦引導注意力與景深、走位的兩種基本方向、手持的限制與適用情境、搖攝與俯仰要有動機、起幅／運動／落幅、腳架雲台、推軌的橫移與推拉（Dolly／Track／Truck）、慢速推近、變焦與推軌的差別。
   避開第 4 張的景別與構圖、避開 shooting-for-the-edit 的涵蓋鏡頭與軸線；器材採購清單與品牌不寫。
   claim 頁；related 連 shot-sizes-and-framing（第 4 張）、shooting-for-the-edit、cutting-for-emotion。

6. travel-video `finding-the-cut`「剪接點怎麼找：位移、決定性瞬間、拉網與試映」— in-the-blink-of-an-eye（02-why-do-cuts-work、03-cut-out-the-bad-bits、10-decisive-moment、14-dragnet、12-test-screenings）。
   第一鏟（cutting-for-emotion）掛 05、04、01、06、07、13，寫的是六法則與權重、以最少做最多、影子剪接與《現代啟示錄》的數字、看見畫框之外，並在 ⚖️ 段用 13 講了「剪接就是一次眨眼」。
   只寫：剪接為什麼行得通（每秒被剪二十四次、半調子的位移最難接受、不連續為王、為什麼不一鏡到底）、什麼才算爛的部分（人與黑猩猩的同一批毛片、順序決定一切、不要中途改變心意）、每個機位一張代表畫格與照片的四種用途、決定性的瞬間與「看毛片就像選角」、拉網式剪輯與剪接點像樹枝、剪接頻率應與眨眼頻率相稱、試映的兩種哲學、過幾天再問、轉移痛、「心臟還是臍帶」。
   避開 cutting-for-emotion 的六法則、最少做最多、影子剪接；14 的「眨眼是思緒的簽名」與既有頁的 13 同一個論點，這頁只取拉網與頻率兩節，不重講眨眼；08（配對做夢）與 09（多位剪輯師）材料薄，不進。afterword 的數位剪接史不開（見不開清單）。
   claim 頁；related 連 cutting-for-emotion、shooting-for-the-edit、documentary-story-design。

7. tour-leading `theft-and-scams-briefing`「扒手與騙術：出發說明會的歐洲街頭課」— europe-through-the-back-door（01-travel-skills/15-theft-and-scams）。
   第一鏟（pacing-a-group-day）掛 01、12、18、19，寫的是節奏與住幾晚；第 15 章的扒竊、詐騙、失竊後的補救整章沒用，tour-leading 四頁也沒有一頁講安全。
   只寫 Steves 這一章：扒竊怎麼發生與怎麼防（腰包、租車防竊）、詐騙與坑錢的幾種形狀（好康上門、金錢往來、與「當地人」相遇、人不可貌相）、一無所有之後怎麼重新站起來（報警與關鍵資訊、補辦護照、停卡調錢、重排行程與補裝備）。
   避開 departure-checklists 的清單方法論（那頁講清單怎麼設計，這頁是清單裡該有的內容）；錢與匯率的細節在 07-money，沒用到就不掛。
   claim 頁；related 連 departure-checklists、recovering-from-mistakes、working-with-local-partners、pacing-a-group-day。
   這頁寫給自助旅人，套用段要翻成「領隊在說明會與車上講什麼、團員自由活動前提醒什麼」，但招數只用書的。

8. tour-design `visitor-management`「承載量、惱怒指數與遊客管理：景點怎麼應付團體」— business-of-tourism（03-intermediaries-in-tourism-services/01-management-of-visitors、01-defining-and-analysing-tourism/06-socio-cultural-impacts、01-defining-and-analysing-tourism/07-environmental-impacts）。
   第一鏟（tour-supply-chain）掛 03/03、04/05、02/08，寫的是通路鏈、成本結構、飯店簽法、巴士的帳；衝擊與遊客管理整部沒碰。導覽第四章爭點四說「我們就是 Abbey 罵的那台車」，站上只有 Abbey 一造，這頁補上教科書怎麼量、怎麼管。
   只寫：承載量與可接受改變限度、遊客管理的成本由誰負擔、三種操作方法（控制需求與流量、改變遊客行為、調整供給）、輔助的科技；社會文化面只取 Doxey 的惱怒指數、示範效應、舞台化的真實、拍照的爭議；環境面只取壅塞與侵蝕、旅客對人造遺址的侵蝕、觀光的正面影響。
   避開 desert-solitaire-and-industrial-tourism 的 Abbey 論證（related 連過去，不重講）、避開 tour-supply-chain 的成本與通路、避開 staging-an-experience；永續立法與布倫特蘭報告只點一句，不展開。
   claim 頁；related 連 desert-solitaire-and-industrial-tourism、tour-supply-chain、pacing-a-group-day、staging-an-experience。
   不開 debate：Holloway 是教科書，不是 Abbey 的對造；兩頁並排後若導覽第四章要改寫爭點四，那是 Fable 的活。

9. tour-design `hotel-grading-and-group-business`「飯店的星星：分級為什麼各國不同、團體房怎麼走」— business-of-tourism（02-travel-and-tourism-product/05-hospitality-sector）。
   第一鏟只用了 03/03 裡飯店的三種簽法；住宿業本身（結構、分級、需求、通路）一章 85KB 沒碰。
   只寫：住宿業的結構（連鎖、多品牌、聯盟、忠誠計畫、經濟型與特色物業）、分類／分級／評等三個常被混用的術語、英國評等制度沿革與歐洲統一評等的難題、地點與價格的取捨、高固定成本與城市旅館、多元房價、住宿的類別、通路裡的團體業務與訂房系統、旅行社角色有限、線上評論的雙面刃。
   避開 tour-supply-chain 的三種簽法與成本占比、避開 pacing-a-group-day 的「旅館在哪」（那頁講位置對節奏的影響，這頁講位置對價格的影響，起草時分清楚）；餐飲一節只點一句。
   claim 頁，importance 3；related 連 tour-supply-chain、pacing-a-group-day、departure-checklists。
   **裁決（主會話）**：不開。教科書章節，「分級」與「團體房」是兩個題，引用測試弱（沒有人會單獨連「飯店的星星」）；留第三鏟候選。

10. destinations `finland-four-neighbours`「芬蘭：聖誕老人、酒、瑞典、俄羅斯與學校」— almost-nearly-perfect-people（04-finland/01-santa、04-finland/03-alcohol、04-finland/04-sweden、04-finland/05-russia、04-finland/06-school、04-finland/07-wives）。
   第一鏟（almost-nearly-perfect-five）五國各取一兩章，芬蘭只掛 02-silence，寫了沉默與高語境、「這是螺絲」與觀光局長那兩句（都在 02）。極光線在羅瓦涅米落地，芬蘭是五國裡團真正住下來的那一國，書的芬蘭篇七章只用了一章。
   只寫：七月去見聖誕老人（羅瓦涅米與聖誕老人村在這章）、赫爾辛基像北歐又不太像、酒的名聲與數字對不上、Sisu 與男子氣概、站在文明斷層線上（瑞典統治的遺緒、今日的瑞典裔芬蘭人、羨慕與較勁）、獨立與內戰、冬季戰爭與繼續戰爭、冷戰的「芬蘭化」、受害者還是成功故事、學校看不出祕密的成功與教師「人民的蠟燭」、世界最性別平等的社會與揹老婆錦標賽、芬蘭算不算北歐。
   避開既有頁的 02-silence 整章（沉默、高語境、螺絲、觀光局長）、避開既有頁對丹麥／冰島／挪威／瑞典的全部段落；芬蘭與瑞典的較勁只寫芬蘭這一側，瑞典篇不進。
   claim 頁；related 連 almost-nearly-perfect-five、chasing-the-aurora、working-with-local-partners、learning-to-see-a-place。

11. destinations `suzhou-shanghai-five-cities`「從蘇州到上海：余秋雨筆下的城市性格」— bittersweet-journey-through-culture（13-white-haired-suzhou、19-shanghainese、20-five-cities）。
   第一鏟（cultural-journey-sites）掛 02、03、04、07、08、14、17，寫的是敦煌、陽關、都江堰、三峽、江南小鎮、西湖；華東線天天走的蘇州與上海沒有一句。
   只寫：蘇州二千五百歲的生日與「文化的後院」、吳越之爭與西施（最苦的是蘇州百姓）、明代的唐伯虎與非官方文化、小巷深處的精魂；上海人為什麼最尷尬、徐光啟作為第一個上海人、租界與拆城牆的百年身世、上海文明的三種心理品性（寬容並存、精明估算、開放追求）；五城記裡開封、南京、成都、蘭州、廣州各一段（爬塔、把歷史溶解於自然、從深厚走向寬廣、濃厚與清甜、花市早茶與北伐）。
   避開既有頁的江南小鎮（14）與西湖（17）、避開「被消費的名勝」那一段的導遊批評；五城記的重慶對照只在成都段帶一句。
   claim 頁；related 連 cultural-journey-sites、learning-to-see-a-place、writing-for-the-ear。
   旁註見小結：01-taoist-pagoda（道士塔）不另開頁，建議補進既有頁。

12. destinations `germany-divided-and-rebuilt`「分裂與重建：圍牆、紙鈔、布痕瓦爾德與瓦礫婦女」— germany-memories-of-a-nation（01-where-is-germany/02-divided-heaven、05-descent/03-money-in-crisis、05-descent/05-at-the-buchenwald-gate、06-living-with-history/01-germans-expelled、06-living-with-history/02-beginning-again）。
   第一鏟（germany-in-objects）掛 01/01、02/02、02/05、04/01、04/03、06/05，寫的是勃蘭登堡門、格林童話、古騰堡、麥森瓷器、香腸與啤酒、國會大廈；二十世紀只在國會大廈那條與「空白也是記憶」details 裡各一段。柏林、威瑪、德勒斯登的團天天站在這段歷史前面。
   只寫：《分裂的天空》、共和國逃亡與圍牆、淚宮與腓特烈大街車站、史塔西與監控的記憶；Ersatz 的年代與緊急貨幣（Notgeld）、惡性通膨與地產馬克、被回收的廢鈔怎麼為納粹開門；布痕瓦爾德大門「Jedem das Seine」與包浩斯字體的密碼式抗議、解放之後同一座營的另一種囚禁、兩個德國的兩種記憶；1945 年的逃亡與驅逐、加害者也是受害者；瓦礫婦女、沉默的重建、兩種馬克與兩個國家。
   避開既有頁的國會大廈段（塗鴉、玻璃圓頂、克拉克「罪責內化」）、避開「空白也是記憶」details 的城市宮與共和國宮、避開格林童話被納粹挪用那一句；05/04（淨化墮落藝術）與 05/02（珂勒惠支）留第三鏟。
   claim 頁；related 連 germany-in-objects、europe-in-three-strands、reading-a-cathedral；seeAlso 掛 economics 站 econ-foundations/inflation-and-deflation（路徑實存；只掛不重講）。

13. destinations `treaty-comes-alive`「條約活過來：都市化、懷唐伊法庭與雙文化」— penguin-history-of-new-zealand（04-unsettlement/04-return-of-mana-maori、04-unsettlement/05-revolution-confirmed、05-posthistory/01-configurations-old-and-new）。
   第一鏟（aotearoa-two-settlements）掛 01/01、02/03、02/05、02/10、02/11、03/08，寫的是兩次移民、1840 年條約兩種版本、1901 年人口回升與納塔；1975 年之後條約怎麼從文件變成制度沒有寫，而旅客問的多半是「毛利人現在怎麼樣」。
   只寫：戰前的兩套神話（農村田園、世界最佳種族關係）、第三次遷徙（都市化）與都市裡的毛利性、貧窮陷阱與語言危機、從部族到全國的 Whina Cooper、Hunn 報告與「整合」、都市抗議與毛利文藝復興、懷唐伊法庭作為革命的伏筆；1984 之後的毛利政策、懷唐伊法庭與和解、條約進入法理（MMP 與 Rogernomics 只各一句當背景）；雙文化的現實、Pakeha 是不是第二個原住民文化、「雙文化是既定事實」。
   避開既有頁的 1840 年條約文本落差、Moriori 與 Waitaha 神話、納塔與蒂普埃亞（這頁從 1945 年後起筆）；紐西蘭戰爭（03/02）與火槍戰爭（02/09）留第三鏟。
   claim 頁；related 連 aotearoa-two-settlements、working-with-local-partners、almost-nearly-perfect-five。

14. destinations `ramesses-and-the-cost-of-empire`「拉美西斯的埃及：卡疊石、阿布辛貝與徭役」— rise-and-fall-of-ancient-egypt（04-military-might/01-martial-law、04-military-might/02-war-and-peace、04-military-might/03-triumph-and-tragedy、04-military-might/04-double-edged-sword）。
   第一鏟（three-thousand-years-on-the-nile）掛 01、03、05 三個 Part，寫的是金字塔時代、第十八王朝、最後一千年；第四部整部跳過，而阿布辛貝、卡納克多柱廳、拉美西斯神廟、梅迪內特哈布都是這一部的建築。
   只寫：士兵的生活與常備軍、戰車、霍朗赫布的政變與敕令；卡疊石（兩則情報、「陛下孤身一人」、把敗局變成宣傳）、「萬王之王」的名字永存、阿布辛貝作為個人崇拜的極致、拉美西斯神廟是上埃及的儲備銀行；分裂的王國與海上民族、史上最早的罷工；徭役是最沉重的稅、哈馬馬特乾谷的統計、王權的出血、拉美西斯九世時代的盜墓世紀大案與委員會的掩蓋。
   避開既有頁的路克索神廟＝王室之卡（04/02 的路克索段只寫拉美西斯加建的塔門與方尖碑）、避開既有頁「帝王谷前講官方盜墓」那條（那是第五部前 1066 年起的國庫清空；這頁的世紀大案是拉美西斯九世的審判，時間與性質不同，起草時明說兩者分開）。
   claim 頁；related 連 three-thousand-years-on-the-nile、rome-in-the-ruins、istanbul-huzun。

15. destinations `seventeenth-century-painters`「十七世紀的畫：卡拉瓦喬、魯本斯、維拉斯奎茲、林布蘭與維梅爾」— story-of-art（19-vision-and-visions、20-mirror-of-nature；18-crisis-of-art 只為葛雷柯與老布勒哲爾各掛一段）。
   第一鏟（story-of-art-for-tour-leaders）掛 09、10、12、15、16、21、25，從羅馬式講到印象派，十七世紀只用 21 的義大利巴洛克建築與雕刻（波洛米尼、貝尼尼、高利）；荷比線的國家美術館、西葡線的普拉多、維也納的藝術史博物館掛的畫全在 18–20 章。
   只寫：走出矯飾主義的死胡同（卡拉契的古典之美對卡拉瓦喬的自然主義）、學院派理想（雷尼、普桑、克勞德怎麼塑造人們看風景的眼光）、魯本斯讓一切活起來與工作室的祕訣、范戴克、維拉斯奎茲；新教荷蘭的品味、哈爾斯的「快照」、為市場作畫的專門化、風景畫發現天空、林布蘭直視人心（自畫像、聖經插圖、蝕刻）、揚・斯汀、雷斯達爾、「自然的鏡子」題材不再是重點、維梅爾的「有人物的靜物」；18 章只取葛雷柯的西班牙異象與老布勒哲爾〈農村婚禮〉。
   避開既有頁的 21 章巴洛克建築段（19 章開頭的耶穌會教堂與立面也不寫，與既有頁重疊）、避開既有頁「巴洛克教堂太像劇場」details；矯飾主義的切利尼、帕米加尼諾、丁托列多不進（留第三鏟或不開）。
   claim 頁；related 連 story-of-art-for-tour-leaders、reading-a-cathedral、al-andalus-three-faiths、discovering-france-beyond-paris。
   書 repo 拼法是「維拉斯奎茲」，標題與內文照它。

16. destinations `after-impressionism`「印象派之後：塞尚、梵谷與高更各要解決什麼」— story-of-art（26-in-search-of-new-standards）。
   第一鏟停在 25 章的印象派；奧塞與梵谷美術館是法國線與荷蘭線的固定點，26 章 20KB 整章沒碰。
   只寫 26 章的繪畫部分：印象派勝利之後的空虛、「印象派其實仍是傳統的延續」、塞尚在自然中重建秩序（「依照自然畫出普桑」、四面八方的矛盾、看似笨拙的靜物）、梵谷以筆觸傳達情感（為所有人而畫、筆觸如同字跡）、高更。建築段（美術工藝運動、新藝術、萊特）只點一句或不寫。
   避開既有頁的 25 章印象派（馬奈、莫內、退後幾步看）；27 章的實驗藝術不進。
   claim 頁，importance 4；related 連 story-of-art-for-tour-leaders、learning-to-see-a-place、discovering-france-beyond-paris。
   單章撐一頁，材料 20KB 夠；若起草時發現高更段太薄，標題改「塞尚與梵谷」即可，不硬湊。

##### 不開（2 本）

- how-to-be-travel-writer（How to Be a Travel Writer）：不開。第一鏟 travel-narrative-craft 已取走第二部速成課的核心五章（研究、形塑、活起來、風格、改寫），剩下的是投稿與出版（第三部）、部落格與 SEO（第四部）、謀生與報稅（第五部）、資源清單（第七部），屬作者職涯與工具層，不是帶團與節目的內容；第六部的攝影訣竅 11KB 是通用建議，不夠一頁。tier 維持 spine，承諾已由既有頁兌現。
- istanbul（Istanbul: Memories and the City）：不開。第一鏟 istanbul-huzun 取了 05、06、10 的呼愁骨幹，並在 ⚖️ 段用掉 23–25 章（奈瓦爾、戈蒂耶、西方之眼）的主張；其餘三十章是家族回憶（01–04、08–09、12–17、29–37）或畫家與專欄作家（07、18、28），團不會用到。19-conquest-or-decline 是這本書裡唯一與市區導覽直接對口的章，但只有 6KB，與 20-religion、22-ships-fires 合起來也撐不出一條主張線。tier 維持 spine。

##### 第三鏟候選（本輪不開，留著）

- podcast-producer-guide ch05/s55 單集標題五策略、ch05/s57 發布策略、Meinzer 05-make-it/05 二十到四十分鐘甜蜜點與 06-share-it/01：合起來是一頁「標題、長度與發布節奏」，屬作業層，平台規格會過期，等前三張落地後再看要不要開。
- grammar-of-the-shot 第四章光線：04/03 色溫與白平衡、04/06 硬光柔光與「善用太陽」、04/10 動機光源，可成一頁「外景的光」；團拍不打燈，先緩。
- europe-through-the-back-door 09-eating（餐廳禮儀、小費、咖啡館）與 17-health-and-hygiene 的健康段（時差、急救、在歐洲就醫）：都是說明會素材，各自可成一頁，排在第 7 張之後。
- business-of-tourism 01/04 需求（推力拉力、市場區隔、觀光地生命週期）：產品規劃層，與 staging-an-experience 不重疊，材料 68KB。
- in-the-blink-of-an-eye afterword 十二節數位剪接史：體裁是回憶錄式的技術史，不建議開。
- germany-memories-of-a-nation 第二條線「德國在哪裡」：01/03 失落的首都（柯尼斯堡、布拉格）、01/05 權力的碎片、02/04 瓦爾哈拉（語言就是國界）、03/01 查理曼與亞琛；或南線「羅曼蒂克大道與紐倫堡」：03/02 里門施奈德、04/02 杜勒。
- penguin-history-of-new-zealand 02/09 火槍戰爭與傳教、03/02 紐西蘭戰爭；04/02 土地的壓力（Manapouri、保育運動、資源管理法）是「紐西蘭為什麼乾淨」的來源。
- story-of-art 03–05 希臘與羅馬（衛城、勞孔、萬神殿），等希臘線或義大利線的書單定了再開。
- almost-nearly-perfect-people 瑞典篇十一章，等北歐線確定會住瑞典再開。

##### 小結

- 開 16 張，全部 claim 頁，沒有 debate：十四本都是單一作者的書，站上沒有「一個問題多本書吵」的形狀；第 8 張與 Abbey 那頁並排後，導覽第四章爭點四要不要改寫，留 Fable。
- 不開 2 本，tier 不動；第三鏟候選 9 條留在單上，不進工具。
- 分布：podcast 3、travel-video 3、tour-leading 1、tour-design 2、destinations 7。工藝書六本開 9 張，目的地書八本開 7 張（芬蘭、華東、柏林、紐西蘭的今天、拉美西斯、十七世紀畫、印象派之後），伊斯坦堡與 travel-writer 不開。
- 起草順序建議：6、4、5（影片線，材料最厚、與既有頁分工最清楚）→ 1、2、3（podcast）→ 14、12、10（目的地裡材料最厚的三張）→ 8、7 → 15、16、13、11 → 9。
- 沒把握的三張：第 9 張（飯店分級，教科書章節，與 tour-supply-chain 的邊界要靠起草時守住）、第 3 張（一稿多用落在 podcast 分類但內容跨影片與文字，若 Andrew 覺得該落 travel-video 就換）、第 15 張（19 章開頭的耶穌會教堂段與既有頁的 21 章巴洛克建築重疊，單上已要求跳過）。
- 旁註（既有頁補強，不必等第二鏟）：
  - cultural-journey-sites 的敦煌段沒有道士塔：01-taoist-pagoda（王道士的粉刷、藏經洞的打開與官場的冷漠、外國探險家的車隊、敦煌學也在中國）是中國線最常講的一段，8.8KB 不夠單獨開頁，建議在既有頁加一條 details 並補掛 01 的 anchor。
  - almost-nearly-perfect-five 的芬蘭段事實全在 02-silence，anchor 也只掛 02，沒有漏掛；第 10 張起草時以此為界。
  - shooting-for-the-edit 的 anchor 掛整章 07-working-practices，正文只用了其中「為剪輯而拍」一組；第 4、5 張會再掛同一章的構圖與運鏡條目，兩頁同掛一章可以，但 label 要不同（例如「實務守則：構圖」「實務守則：運鏡」），讀者才分得出。
  - DEEPEN-TARGETS 把八本目的地書列成「大部頭只一鏟」，其中 istanbul 與 travel-writer 本輪判不開；它們會一直留在候選表上，這是選題不是體裁，不進 EXCLUDED_KINDS。

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
  - **兩筆 B 型債**：hbr `coaching-and-feedback` 的 SBI、design-patterns `oop-vs-functional` 的一級函數論，同日回原文改寫清償，校正表在 SOURCING-DEBT。
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
