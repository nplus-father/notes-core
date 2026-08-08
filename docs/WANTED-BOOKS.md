# 待收書單（bibliography `wanted` 全星系匯出）

**這份是什麼**：各 note 站 `src/data/bibliography.ts` 裡標成 `status: "wanted"` 的書，
全部匯出成一張採購清單。書名以**英文原名**為主，中譯附在後面。由
`notes-core/tools/export-wanted.py` 生成，**不要手改**——改各站的 bibliography 再重跑。

**已收錄比對的資料源**：GitHub 現況（`gh repo list` nplus-father／Andrewnplus，1611 個 repo）。

## 先收這 20 本

整份 295 筆太長，這是從裡面挑出來的採購順序，也是建議的消化順序（薄的、起手容易的排前面）。**這節是全檔唯一的人工區塊**——要改請編 `export-wanted.py` 的 `TOP20`，不要改這裡。挑選準則依序：①多站共等，收一本補多站 ②站主自己在 `note` 裡標了「最大／頭號缺口」 ③portal 驗證的 anchor 深度——nplus.wiki 上已經建成幾本回指它的書站（同作者書櫃、同一條線的衍生書），書櫃愈深、原典愈缺就排愈前面（見 [SOURCING-DEBT.md](./SOURCING-DEBT.md)） ④同等重要時，薄的、有繁中在版的排前面。

「為何排這裡」的 portal 數字都是實查出來的（作者書櫃本數、同一條線的衍生書數、各站概念頁引用處數）；`/note-wanted` 每次重挑會一併重查。

| # | 英文書名 | 中譯 | 年 | 站 | 為何排這裡 |
| --- | --- | --- | --- | --- | --- |
| 1 | **The Rules of Love** |  | 2008 | templar | templar 站自標「親密關係那一塊的缺口，系列裡與 Life 最互補」；portal 已有 6 本 Templar（Life、Management、People、Thinking、Wealth、Work），系列就缺這本——薄，一晚讀完，起手式選它 |
| 2 | **Confessions** | 懺悔錄 | 397 | theology | **全星系最重的作者級空洞**：「奧古斯丁」被引用 34 處、25 個檔案、橫跨 9 站（theology、biblical-studies、keller、lewis、peck、peterson、spiritual-formation、stott、willard），而 portal 上奧古斯丁的書**一本都沒有**——這本是那 34 處的共同源頭；繁中多種在版 |
| 3 | **Rich Dad's Prophecy** | 富爸爸大預言 | 2002 | kiyosaki | portal 已有 25 本清崎——**書櫃只剩這一本**（kiyosaki 站 owned 23／wanted 1，收了就歸零）；退休金制度崩塌的預言；有繁中《富爸爸大預言》 |
| 4 | **Refactoring UI** |  | 2018 | design | design 站 owned 11／wanted 1——**收了就歸零**；portal 完全沒有這本，補的是 CRAP 原則到實際元件之間那一段；薄、工程師視角，一個週末讀完 |
| 5 | **The Everlasting Man** | 永恆的人 | 1925 | theology | portal 只有 2 本切斯特頓（Orthodoxy、What's Wrong with the World）；「切斯特頓」站內 11 處、跨 3 站（lewis、theology、design），而 portal 13 本路易斯那整個書櫃的歸信轉捩點正是這一本——收了才接得起來；薄、有繁中《永恆的人》 |
| 6 | **Servant Leadership** |  | 1977 | leadership | leadership 站 owned 94／wanted 2——**全星系最深的站書櫃、已收到 98%**，缺的正是這本 1977 原典；portal 的 Greenleaf **只有 1 本**（晚年文集 The Power of Servant-Leadership），源頭不在，而下游整片（Maxwell 13 本、Kouzes、Bennis、Kotter）全掛在它上面。注意 portal 的 `servant-leadership` repo 是 Larry W. Boone 的同名教科書，不是本書（見 NAME_COLLISIONS） |
| 7 | **Competitive Advantage** | 競爭優勢 | 1985 | business-strategy | portal 的 Porter **只有 2 本**（競爭策略、國家競爭優勢），三部曲中間這本價值鏈原典不在；「價值鏈」站內 8 處、7 個檔案、跨 4 站（business-strategy、problem-solving、management、agile） |
| 8 | **Emotional Intelligence** | EQ | 1995 | thinking | portal 已有 6 本情緒智力的**衍生書**（HBR 三本指南、Primal Leadership、Permission to Feel、Peak Performance），1995 年那本把 EQ 帶進大眾語彙的原典卻不在；「EQ／情緒智商／情緒智力」站內 28 處、跨 8 站（career、cloud、covey、hbr、kiyosaki、leadership、life-meaning、thinking） |
| 9 | **Trading in the Zone** |  | 2000 | investing | portal 已有 Mark Douglas 的前作 The Disciplined Trader，缺這本被當成交易心理標準讀物的成熟之作——「交易心理」站內 12 處，橫跨 investing 與 schwager 兩站，兩站的概念頁都指著它；investing 站 owned 54／wanted 8 |
| 10 | **Biblical Theology** |  | 1948 | biblical-studies | 「聖經神學」站內 49 處、13 個檔案、跨 3 站（biblical-studies、keller、theology）；portal 有 6 本掛聖經神學的書（According to Plan、A New Testament Biblical Theology…），缺的正是 Vos 1948 這本把它立成一門學科的奠基原典。注意 portal 同名 repo 是 Goldingay 的書（見 NAME_COLLISIONS） |
| 11 | **Leading Minds: An Anatomy of Leadership** | 領導心智 | 1995 | gardner | portal 已有 11 本加德納（gardner 站 owned 10／wanted 6）；「多元智能」站內 39 處，「說故事」跨 17 站——這本以說故事的人解剖領導，正是他從 MI 跨到領導研究的那一步，是 gardner 站與 leadership 站的接點 |
| 12 | **Advanced Selling Strategies** |  | 1995 | tracy | portal 已有 34 本 Brian Tracy——**全星系最深的作者書櫃**，而 tracy 站 owned 34／wanted 2；銷售線上已有 The Psychology of Selling、Sales Management、Negotiation 三本，缺的正是大客戶與關係銷售這一層進階正典（「銷售」全星系 298 處、113 個檔案、31 站） |
| 13 | **The Divine Conspiracy Continued** | 神聖的密謀・續篇 | 2014 | willard | portal 已有 7 本魏樂德，《神聖的密謀》本傳在、續篇不在（注意兩者是不同書，別讓比對誤併）；天國福音延伸到職場與公共領域 |
| 14 | **The Culture Map** | 文化地圖 | 2014 | leadership | leadership 站 owned 94／wanted 2 的另一本——收完這兩本該站就歸零；portal 的 Erin Meyer 只有與 Hastings 合著的 No Rules Rules，她自己那本跨文化八刻度的主著不在；有繁中《文化地圖》 |
| 15 | **The Body Keeps the Score** | 心靈的傷，身體會記住 | 2014 | wellness | 「創傷」是全星系橫跨最廣的概念之一——38 處、20 個檔案、**10 站**（growth、history、life-meaning、navarro、peterson、relationships、taleb、theology、thinking、wellness），而 portal 的 van der Kolk **掛零**，這片引用沒有任何原典可掛；有繁中《心靈的傷，身體會記住》，厚，排中後段 |
| 16 | **The Data Warehouse Toolkit** |  | 1996 | data-systems | data-systems 是**全星系最淺的站**（owned 9／wanted 10，僅 47%）；portal 的 Kimball **掛零**，「維度建模」站內只有 1 處——星型結構的正典不在，整個資料倉儲線沒有源頭可掛 |
| 17 | **Kanban: Successful Evolutionary Change for Your Technology Business** | Kanban | 2010 | agile | portal 有衍生的 Kanban in Action、卻沒有 Anderson 2010 的原典；「看板」在 agile 站 14 個檔案（另散見 career、hbr、tools、uncle-bob 等 7 站），限制在製品的理論來源全靠二手轉述 |
| 18 | **The Four Steps to the Epiphany** |  | 2005 | startup | startup 站 wanted 11 本、是缺口最深的主題站之一；portal 的 Steve Blank **掛零**，而下游（Running Lean／Scaling Lean、精實創業線）全從顧客開發長出來——源頭不在，「顧客開發」站內只剩 2 處孤證 |
| 19 | **The Chronicles of Narnia** | 納尼亞傳奇（七部曲） | 1950 | lewis | lewis 站 owned 13／wanted 1——**收了就歸零**；portal 已有 13 本路易斯而納尼亞掛零，「納尼亞」站內 4 處跨 3 站（lewis、keller、biblical-studies）卻無處可掛；七部曲，厚，排後段 |
| 20 | **We, Programmers: A Chronicle of Coders from Ada to AI** |  | 2024 | uncle-bob | uncle-bob 站自標「目前最大的缺口」；portal 已有 7 本 Robert C. Martin（Clean 系列全在），缺這本 2024 年從 Ada 到 AI 的晚年回望——厚，壓軸慢啃 |

**這是第四個軸**，與 docs/ 既有三份不同：

| 文件 | 缺口是什麼 | 靠什麼補 |
| --- | --- | --- |
| [COVERAGE-GAPS.md](./COVERAGE-GAPS.md) | 還沒有**站** | 開新站 |
| [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md) | 站在、**內容**沒寫完 | `note-enrich` |
| [SOURCING-DEBT.md](./SOURCING-DEBT.md) | 內容寫了、查不到**出處** | 掛 anchor |
| **本檔** | **書本身還沒有** | **去收書** |

## bibliography 的四個 status

`library.ts` 的 `BibliographyStatus`，語意是「**這本書在書庫裡的狀態**」，不是「讀過沒有」：

| status | 意思 | 判準 | 筆數 |
| --- | --- | --- | --- |
| `owned` | **已收錄**——書已經做成 `nplus.wiki/<slug>/` 的書站 | 必須有 `slug`；首頁書架的封面列就是取這批，概念頁的 `furtherReading.anchor` 也是連到這裡 | 1579 筆（去重 1134 本） |
| `wanted` | **待收錄**——想收、還沒有 | 買得到，只是還沒買／還沒做站 | **295 筆（去重 295 本）** |
| `unavailable` | **暫無來源**——想收但收不到 | 絕版、無中譯、或只有機構授權（如 Scrum Guide、Vanguard 內部傳記） | 40 筆 |
| `skipped` | **刻意略過**——不打算收 | 內容重複、練習冊、合輯、不合站主軸；`note` 欄寫明為何略過 | 79 筆 |

> `owned` 去重後的 1134 是**已建成書站的書**（1579 是含跨站重複的登錄筆數，
> 一本書被三站列進盤點就算三筆）。它代表「書站存在、封面抓得到、概念頁 anchor 回得去」，
> 不等於實體書在書架上。

## 先扣掉：0 本其實已經有書站了

這些 `wanted` 的書名對得上**已存在的書 repo**——不必再收，是各站 bibliography 的 status 沒跟上。**買書前先扣掉這批**，並把該筆改成 `status: "owned"` ＋ 補上 `slug`（＝下表的 repo slug）再重跑；`/note-wanted` 會代勞。

| 書 repo slug | 書名 | 登記在 | portal 上的描述（核對用） |
| --- | --- | --- | --- |

## 優先收：0 本有兩個以上的站在等

同一本書被多站列為 `wanted`——收一本補多站的缺口，投資報酬率最高。

| 英文書名 | 中譯 | 年 | 等它的站 |
| --- | --- | --- | --- |

## 完整清單（依站，共 295 筆）

### theology-note — 12 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Reformed Dogmatics | 改革宗教理學 | 1906 | 巴文克；改革宗系統神學的巔峰，中譯陸續出版 |
| Christian Theology: An Introduction | 基督教神學手冊 | 1994 | 麥葛福；最平衡的入門教科書 |
| Summa Theologiae | 神學大全 | 1274 | 阿奎那；中譯有全集但部頭極鉅 |
| Pensées | 思想錄 | 1670 | 巴斯卡；「賭注」與心之理由的源頭 |
| The Everlasting Man | 永恆的人 | 1925 | 切斯特頓；促成路易斯歸信的一本 |
| The Reformed Pastor | 改革宗的牧師 | 1656 | 巴克斯特；清教徒牧養的正典 |
| Lectures to My Students | 給我學生的信（講道講座） | 1875 | 司布真的牧職講義 |
| The Contemplative Pastor | 返璞歸真的牧養藝術 | 1989 | 畢德生；反職業化牧養的當代聲音 |
| Confessions | 懺悔錄 | 397 | 奧古斯丁；西方神學自傳體的源頭 |
| The City of God | 上帝之城 | 426 | 奧古斯丁；歷史神學與政治神學的奠基 |
| On the Incarnation | 論道成肉身 | 318 | 亞他那修；教父基督論最佳入門 |
| The Imitation of Christ | 效法基督 | 1418 | 金碧士；中世紀靈修最流通的一本 |

### startup-note — 11 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| The Four Steps to the Epiphany |  | 2005 | Blank：顧客開發方法論的源頭 |
| The Startup Owner's Manual |  | 2012 | 顧客開發的百科式操作版 |
| Running Lean |  | 2012 | Maurya 前作：Lean Canvas 的原典（Scaling Lean 已收） |
| Traction |  | 2015 | Weinberg & Mares：19 個獲客渠道的 Bullseye 框架 |
| The Founder's Dilemmas |  | 2012 | Wasserman：共同創辦人與股權分配的地雷圖 |
| Blitzscaling | 閃電擴張 | 2018 | Hoffman：網路效應市場裡速度優先於效率 |
| High Growth Handbook |  | 2018 | Elad Gil：10 人到 1000 人的規模化手冊 |
| The Great Game of Business |  | 1992 | Stack：開卷管理——讓全員看懂財報玩同一場遊戲 |
| The $100 Startup 3000 | 元開始的自主人生 | 2012 | Guillebeau：微資本開業的案例集 |
| Venture Deals | 創業投資聖經 | 2011 | Feld & Mendelson：看懂 term sheet 再上談判桌 |
| Built to Sell |  | 2011 | Warrillow：打造一間可以賣掉的公司 |

### thinking-note — 11 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Superforecasting | 超級預測 | 2015 | Tetlock：預測是可訓練的技能 |
| The Scout Mindset | 零盲點思維 | 2021 | Galef：偵察兵心態 vs 士兵心態 |
| Moral Tribes | 道德部落 | 2013 | Joshua Greene：常識道德在部落之間失靈 |
| Behave: The Biology of Humans at Our Best and Worst | Behave 行為 | 2017 | Sapolsky：行為的全尺度生物學 |
| Civilization and Its Discontents | 文明及其不滿 | 1930 | Freud 晚期文化批判的正典 |
| How the Mind Works | 心智探奇 | 1997 | Pinker：演化＋計算視角的心智總覽 |
| Being You: A New Science of Consciousness | Being You 身為自己 | 2021 | Anil Seth：意識作為受控幻覺 |
| The Language Instinct | 語言本能 | 1994 | Pinker：語言是演化出的本能 |
| Metaphors We Live By | 我們賴以生存的譬喻 | 1980 | Lakoff & Johnson：概念隱喻——思考建立在譬喻上 |
| How Emotions Are Made | 情緒跟你以為的不一樣 | 2017 | Barrett：情緒建構論，對基本情緒論的正面挑戰 |
| Emotional Intelligence | EQ | 1995 | Goleman：把情緒智力帶進大眾語彙的原典 |

### biblical-studies-note — 10 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| The Art of Biblical Narrative |  | 1981 | Alter——文學讀法的分水嶺之作 |
| Theology of the Old Testament |  | 1997 | Brueggemann——「見證與爭訟」框架的舊約神學另一極 |
| Old Testament Theology | 三卷） | 2003 | Goldingay 的敘事進路大部頭（其單卷《聖經神學》已收） |
| Jesus and the Eyewitnesses |  | 2006 | Bauckham——福音書作為目擊者見證 |
| Echoes of Scripture in the Letters of Paul |  | 1989 | Hays——互文性讀保羅的開山之作 |
| Grasping God's Word |  | 2001 | Duvall & Hays——釋經步驟化的教科書標準 |
| Biblical Theology |  | 1948 | Vos——聖經神學作為學科的奠基原典 |
| Kingdom through Covenant |  | 2012 | Gentry & Wellum——以聖約串起正典的系統性嘗試 |
| The Temple and the Church's Mission |  | 2004 | Beale——聖殿主線的專論，本站主線概念的深化來源 |
| NICNT | ／NICOT 系列代表卷 |  | 學術註釋的系列級缺口——如 Moo《Romans》、Fee《1 Corinthians》、Wenham《Genesis》 |

### data-systems-note — 10 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Readings in Database Systems |  | 2015 | Red Book 第五版；Stonebraker 選編的論文導讀，線上免費 |
| SQL Antipatterns |  | 2010 | Karwin；schema 與查詢的反模式目錄 |
| NoSQL Distilled |  | 2012 | Fowler & Sadalage；聚合導向資料模型與 polyglot persistence 的語彙 |
| Seven Databases in Seven Weeks |  | 2012 | 以七種資料庫走一遍資料模型光譜 |
| Streaming Systems |  | 2018 | Akidau 等；watermark／trigger——串流語意的正典 |
| Kafka: The Definitive Guide |  | 2017 | log 為中心的資料骨幹，事實標準的官方指南 |
| Designing Event-Driven Systems |  | 2018 | Stopford；以 Kafka 為底的事件驅動服務，O'Reilly 免費電子書 |
| Fundamentals of Data Engineering |  | 2022 | Reis & Housley；資料工程生命週期的現代全景 |
| The Data Warehouse Toolkit |  | 1996 | Kimball；維度建模（star schema）的正典 |
| Versioning in an Event Sourced System |  | 2017 | Greg Young；事件溯源在演進期的實務難題 |

### career-note — 9 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Linchpin | 關鍵人物 | 2010 | Godin：讓自己成為不可取代的樞紐 |
| The Software Engineer's Guidebook |  | 2023 | Orosz 的工程師職涯全地圖（Tech Resume 已收） |
| Soft Skills: The Software Developer's Life Manual |  | 2014 | Sonmez：工程師的職涯經營生存手冊 |
| A Whole New Mind | 未來在等待的人才 | 2005 | Pink：右腦能力在自動化時代增值 |
| The Defining Decade 20 | 世代，你的人生是不是卡住了 | 2012 | Meg Jay：二十世代的不可替代性 |
| The Pathless Path |  | 2022 | Millerd：離開預設路徑的工作觀 |
| Working Identity | 轉行 | 2003 | Ibarra：轉職是先行動再認同，不是先想清楚 |
| The Alliance | 聯盟世代 | 2014 | Hoffman：僱傭關係是任期制聯盟 |
| Never Eat Alone | 別自己一個人吃飯 | 2005 | Ferrazzi 的人脈經營經典 |

### cloud-infra-note — 9 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| The Unicorn Project | 獨角獸專案 | 2019 | 鳳凰專案的開發者視角姊妹作 |
| Observability Engineering |  | 2022 | Majors 等；高基數事件與「未知的未知」——可觀測性學派的正典 |
| Practical Monitoring |  | 2017 | Julian；監控反模式與務實起步 |
| Systems Performance |  | 2020 | Brendan Gregg；USE 方法與效能分析的系統性正典 |
| TCP/IP Illustrated, Volume 1 |  | 1994 | Stevens；網路協定的經典解剖 |
| UNIX and Linux System Administration Handbook |  | 2017 | Nemeth 等；傳統系統管理的百科全書 |
| Terraform: Up & Running |  | 2017 | Brikman；IaC 落地的實戰標準 |
| Infrastructure as Code |  | 2016 | Kief Morris；把基礎設施當軟體管理的原則書 |
| The Practice of Cloud System Administration |  | 2014 | Limoncelli；分散式服務維運的教科書 |

### nouwen-note — 9 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Intimacy | 親密 | 1969 | 處女作；牧養心理學時期的起點 |
| Out of Solitude | 始於寧謐處 | 1974 | 獨處與服事的小經典；三篇講章 |
| The Genesee Diary | 萬花筒般的隱修日記 | 1976 | 特拉普修院七個月的日記；學者第一次真正安靜下來 |
| Clowning in Rome | 羅馬城的小丑戲 | 1979 | 小丑（邊緣人）作為屬靈生活的隱喻 |
| Compassion | 慈心憐憫 | 1982 | 與 McNeill、Morrison 合著；憐憫＝一同受苦的神學 |
| The Road to Daybreak | 黎明路上 | 1988 | 從哈佛到黎明之家的轉折日記 |
| Heart Speaks to Heart | 心應心 | 1989 | 對基督之心的三篇禱文；崩潰後的深水之作 |
| Can You Drink the Cup? | 你能飲這杯嗎？ | 1996 | 杯的三個動作：拿起、舉起、喝下 |
| The Inner Voice of Love | 心靈愛語 | 1996 | 崩潰低谷的「秘密日記」；最赤裸的一本 |

### economics-note — 8 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| The Worldly Philosophers | 俗世哲學家 | 1953 | Heilbroner；經濟思想史最會說故事的一冊 |
| Freakonomics | 蘋果橘子經濟學 | 2005 | Levitt & Dubner；誘因分析的大眾化里程碑 |
| The Undercover Economist | 臥底經濟學家 | 2005 | Harford；用日常現象教會你像經濟學家思考 |
| Naked Economics |  | 2002 | Wheelan；無方程式的經濟學通識入門 |
| Animal Spirits | 動物本能 | 2009 | Akerlof & Shiller；把心理拉回總體經濟學 |
| This Time Is Different | 這次不一樣 | 2009 | Reinhart & Rogoff；八百年金融危機的量化通史 |
| Globalization and Its Discontents | 全球化的許諾與失落 | 2002 | Stiglitz；體制內人對 IMF／世銀的批判 |
| 23 Things They Don't Tell You About Capitalism | 資本主義沒告訴你的 23 件事 | 2010 | Ha-Joon Chang；主流敘事的反方教材 |

### investing-note — 8 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Pioneering Portfolio Management |  | 2000 | Swensen 機構版正典——耶魯模式本尊 |
| 100 Baggers |  | 2015 | Mayer 對百倍股的系統研究(承 Phelps 1972) |
| Trading in the Zone |  | 2000 | Douglas 更成熟的一冊,交易心理標準讀物 |
| Trend Following |  | 2004 | Covel 本傳(目前只收錄 Masters Vol.2 訪談集) |
| The Alchemy of Finance | 金融煉金術 | 1987 | 索羅斯的反身性理論 |
| Technical Analysis of the Financial Markets |  | 1999 | Murphy;技術分析的教科書標準(Schwager 入門冊已收) |
| Valuation (McKinsey) |  | 1990 | Koller 等;企業估值的業界標準 |
| Financial Shenanigans | 財報詭計 | 1993 | Schilit;財報偵錯的防守面 |

### philosophy-note — 8 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Sophie's World | 蘇菲的世界 | 1991 | 小說形式的哲學史，國民級入門 |
| Ethika Nikomacheia | Nicomachean Ethics 尼各馬可倫理學 |  | 亞里斯多德德性倫理的原典 |
| Politeia | The Republic 理想國 |  | 柏拉圖——政治哲學的起點 |
| A Theory of Justice | 正義論 | 1971 | Rawls——當代政治哲學的座標原點 |
| Diatribai | Discourses 愛比克泰德語錄 |  | 補齊斯多噶三巨頭的最後一角 |
| Le Mythe de Sisyphe | The Myth of Sisyphus 薛西弗斯的神話 | 1942 | 卡繆——荒謬與反抗的存在主義原典 |
| The Analects | 論語 |  | 儒家原典——關係與德性的東方座標 |
| Tao Te Ching | 道德經 |  | 道家原典——無為與反者道之動 |

### marketing-note — 7 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Obviously Awesome | 顯而易見的傑出 | 2019 | Dunford；B2B／產品定位的現代操作手冊 |
| How Brands Grow | 品牌如何成長 | 2010 | Byron Sharp；實證行銷科學，對忠誠度神話的反擊 |
| Purple Cow | 紫牛 | 2003 | Godin；卓越到值得談論才是行銷 |
| Contagious | 瘋潮行銷 | 2013 | Berger；STEPPS——內容為何被瘋傳 |
| Permission Marketing | 許可行銷 | 1999 | Godin；從打擾式到許可式——email／訂閱通路的思想起點 |
| Scientific Advertising | 科學的廣告 | 1923 | Hopkins；直效廣告與測試思維的百年原點 |
| Marketing Management | 行銷管理 | 1967 | Kotler；學院派教科書標準，補理論骨架用 |

### nt-wright-note — 7 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Justification: God's Plan and Paul's Vision |  | 2009 | 回應 Piper 的稱義論戰之作：稱義是盟約成員身分的宣告 |
| Paul: A Biography |  | 2018 | 保羅生平的敘事重建，學術成果的普及出口 |
| Simply Jesus |  | 2011 | 《耶穌與神的得勝》的普及版：耶穌如何作王 |
| How God Became King |  | 2012 | 四福音「被遺忘的中段」：上帝作王的故事，補信經跳過的一塊 |
| The Day the Revolution Began |  | 2016 | 十架論的普及重述：赦罪帶來的是新出埃及與革命 |
| After You Believe (Virtue Reborn) | 信主了，然後呢？ | 2010 | 新創造框架下的品格與德行倫理——盼望三部曲的收尾 |
| Scripture and the Authority of God |  | 2011 | 「聖經權柄」＝上帝藉聖經行使的權柄；五幕劇詮釋框架的出處 |

### personal-finance-note — 7 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Early Retirement Extreme |  | 2010 | Fisker；FIRE 數學與哲學的硬核根基 |
| Quit Like a Millionaire |  | 2019 | Kristy Shen；可複製的中產 FIRE 實證 |
| Die with Zero | 別把你的錢留到死 | 2020 | Perkins；反過度累積——花錢也要最佳化 |
| The Millionaire Mind |  | 2000 | Stanley 續作——富人的決策與性格研究 |
| The Total Money Makeover |  | 2003 | Ramsey 主著；Baby Steps 無債務體系的原典 |
| The Automatic Millionaire | 讓錢為你工作的自動理財法 | 2004 | Bach；把儲蓄自動化的經典操作手冊 |
| The Wealthy Barber |  | 1989 | Chilton；北美國民理財入門的敘事體始祖 |

### wellness-note — 7 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Spark: The Revolutionary New Science of Exercise and the Brain | Spark 運動改造大腦 | 2008 | Ratey：運動對大腦與情緒的實證經典 |
| In Defense of Food | 食物無罪 | 2008 | Pollan：「吃食物，別太多，以植物為主」 |
| How Not to Die | 食療聖經 | 2015 | Greger：疾病別的飲食實證彙整 |
| Why Zebras Don't Get Ulcers | 為什麼斑馬不會得胃潰瘍 | 1994 | Sapolsky：壓力生理學的經典 |
| The Body Keeps the Score | 心靈的傷，身體會記住 | 2014 | van der Kolk：創傷研究的當代標準 |
| Feeling Good: The New Mood Therapy |  | 1980 | Burns：認知行為治療（CBT）自助經典 |
| Flourish | 邁向圓滿 | 2011 | Seligman：PERMA 幸福模型 |

### fengtang-note — 6 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| （成事：馮唐品讀曾國藩嘉言鈔） | 成事：馮唐品讀曾國藩嘉言鈔 | 2019 | 成事學的起點：逐條品讀曾國藩嘉言——《成事心法》的前作 |
| （活著活著就老了） | 活著活著就老了 | 2005 | 雜文成名作；馮唐聲口的原型——文學觀與人生觀的底稿 |
| （三十六大） | 三十六大 | 2012 | 三十六封公開信：「大」系列雜文的代表作 |
| （無所畏） | 無所畏 | 2018 | 中年心境的雜文集：無所畏與無所謂之間 |
| （萬物生長三部曲（十八歲給我一個姑娘／萬物生長／北京，北京）） | 萬物生長三部曲（十八歲給我一個姑娘／萬物生長／北京，北京） | 2001 | 青春三部曲：文學馮唐的主線長篇，一筆合併收錄 |
| （馮唐詩百首） | 馮唐詩百首 | 2011 | 「春風十里，不如你」的出處；詩人馮唐的代表集 |

### gardner-note — 6 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Art, Mind, and Brain: A Cognitive Approach to Creativity | 藝術、心智與大腦 | 1982 | MI 前夜的藝術認知研究；Project Zero 時期的成果 |
| The Mind's New Science: A History of the Cognitive Revolution | 心智的新科學 | 1985 | 認知革命的權威史；理解加德納學術座標的背景書 |
| Leading Minds: An Anatomy of Leadership | 領導心智 | 1995 | 以「說故事的人」解剖領導——創造力解剖學的姊妹作 |
| Extraordinary Minds | 非凡心智 | 1997 | 大師（Mozart）、創造者（Freud）、內省者（Woolf）、影響者（Gandhi）四種非凡 |
| Truth, Beauty, and Goodness Reframed | 重新定義真善美 | 2011 | 數位時代如何守住三大古典價值；《學習的紀律》的續章 |
| The App Generation | 破解 APP 世代 | 2013 | 與 Katie Davis 合著；app 心態如何形塑青少年的認同、親密與想像 |

### habits-note — 6 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Good Habits, Bad Habits |  | 2019 | Wendy Wood：習慣科學的學院派正典——情境與摩擦力 |
| Stolen Focus | 誰偷走了你的專注力？ | 2022 | Hari：專注力崩壞的系統性成因 |
| Daily Rituals: How Artists Work |  | 2013 | Currey：161 位創作者的作息田野調查 |
| Rest |  | 2016 | Pang：刻意休息是深度工作的另一半 |
| Discipline Is Destiny |  | 2022 | Holiday：斯多噶四樞德的自律卷 |
| Willpower: Rediscovering the Greatest Human Strength | Willpower 增強你的意志力 | 2011 | Baumeister：意志力科學的正典（自我耗損後續有爭議，仍值得收） |

### liurun-note — 6 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| （商業簡史） | 商業簡史 | 2020 | 把商業進化史讀成「交易成本不斷降低」的歷史——底層邏輯的史學版 |
| （進化的力量2） | 進化的力量2 | 2022 | 年度演講系列續作；趨勢判讀框架的年度更新 |
| （趨勢紅利） | 趨勢紅利 | 2016 | 早期代表作：紅利＝短暫供需失衡的出處 |
| （新零售：低價高效的數據賦能之路） | 新零售：低價高效的數據賦能之路 | 2018 | 「人貨場」重構的新零售方法論 |
| （互聯網+：傳統企業，互聯網在踢門） | 互聯網+：傳統企業，互聯網在踢門 | 2015 | 成名作：傳統企業轉型的早期宣言 |
| （關鍵躍升：新任管理者的底層邏輯） | 關鍵躍升：新任管理者的底層邏輯 | 2023 | 寫給新手管理者的「驚險一躍」專書——管理分類的直接補強 |

### science-note — 6 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Cosmos | 宇宙 | 1980 | Sagan：科學普及史上最有影響力的一本 |
| Surely You're Joking, Mr. Feynman! | 別鬧了，費曼先生 | 1985 | 科學家性格與「絕不自欺」的第一手示範 |
| Brain Rules | 大腦當家 | 2008 | Medina：認知神經科學的實用十二則 |
| The Blind Watchmaker | 盲眼鐘錶匠 | 1986 | Dawkins：累積選擇如何無心智地造出設計 |
| The Demon-Haunted World | 魔鬼盤據的世界 | 1995 | Sagan：懷疑論工具箱（baloney detection kit） |
| Conjectures and Refutations | 猜想與反駁 | 1963 | Popper：可否證性原則的原典 |

### wujun-note — 6 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| （文明之光） | 文明之光 | 2014 | 四冊文明史；把科技放進人類文明長河的大歷史書寫 |
| （智能時代） | 智能時代 | 2016 | 大數據與智能革命的方法論——AI 浪潮前夜的預言書 |
| （全球科技通史） | 全球科技通史 | 2019 | 從石器到量子的科技全史；「能量與資訊」雙主線的史觀 |
| （信息傳） | 信息傳 | 2020 | 資訊史詩；香農資訊論如何成為理解未來的方法論（無繁中版） |
| （吳軍數學通識講義） | 吳軍數學通識講義 | 2021 | 得到課程結集；把數學史講成通識教育的系統嘗試 |
| （大學之路） | 大學之路 | 2015 | 兩冊英美名校巡禮；博雅教育理念最完整的陳述 |

### business-strategy-note — 5 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Competitive Advantage | 競爭優勢 | 1985 | Porter；價值鏈分析的原典 |
| Good Strategy Bad Strategy | 好策略壞策略 | 2011 | Rumelt；策略核（診斷—指導方針—一致行動） |
| Playing to Win |  | 2013 | Lafley & Martin；P&G 的五問策略級聯 |
| The Art of War | 孫子兵法 |  | 不戰而屈人之兵——一切戰略書的源頭 |
| SPIN Selling | 銷售巨人 | 1988 | Rackham；大型銷售的實證研究——B2B 提問法原典 |

### cloud-note — 5 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Boundaries with Kids | 為孩子立界線 | 1998 | 把界線變成教養框架——讓孩子為自己的行為承擔後果 |
| How People Grow | 成長神學 | 2001 | 與 Townsend 合寫的成長框架神學基座——恩典、真理、時間的系統陳述 |
| Safe People | 安全的人 | 1995 | 如何辨認（並成為）值得靠近的人——關係線的實用篇 |
| Integrity: The Courage to Meet the Demands of Reality | Integrity | 2006 | 品格六面向——能力之外，讓成果留下來的是人格結構 |
| Trust: Knowing When to Give It, When to Withhold It... | Trust | 2023 | 最新主著：信任的五要素與重建之路，界線思想的續篇 |

### design-patterns-note — 5 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Head First Design Patterns | 深入淺出設計模式 | 2004 | 公認最好的模式入門教材 |
| Smalltalk Best Practice Patterns |  | 1996 | Beck；Implementation Patterns 的前身，模式思維的源頭之一 |
| Analysis Patterns |  | 1996 | Fowler；領域模型層級的可重用模式 |
| Pattern-Oriented Software Architecture Vol.1 (POSA) |  | 1996 | 架構層級模式的學院正典（Layers、Broker、Pipes and Filters） |
| Game Programming Patterns |  | 2014 | Nystrom；GoF 在遊戲場景的再詮釋，免費線上版可先讀 |

### drucker-note — 5 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| The Future of Industrial Man | 工業人的未來 | 1942 | 提出「合法性」與「地位與功能」問題，通往《企業的概念》 |
| Managing in Turbulent Times | 動盪時代的管理 | 1980 | 不確定時代的經營綱領，與當下高度共鳴 |
| Managing the Non-Profit Organization | 使命與領導：非營利組織的管理 | 1990 | 杜拉克晚年最重視的部門——社會部門 |
| Drucker on Asia | 杜拉克看亞洲 | 1997 | 與中內功的對談錄；杜拉克與日本經營的互動 |
| Managing in the Next Society | 下一個社會 | 2002 | 最後的社會預言：少子高齡化、資訊革命的下一步 |

### hbr-note — 5 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| HBR's 10 Must Reads: The Essentials |  | 2010 | 主系列的總綱卷——Porter/Drucker/Kotter/Christensen 名文合輯 |
| HBR's 10 Must Reads on Leadership |  | 2011 | 主系列領導卷——Goleman〈What Makes a Leader?〉、Kotter 名文 |
| HBR's 10 Must Reads on Managing People |  | 2011 | 主系列帶人卷——One Minute Manager 級的經典選文 |
| HBR's 10 Must Reads on Strategy |  | 2011 | 主系列策略卷——Porter〈What Is Strategy?〉所在 |
| HBR's 10 Must Reads on Innovation |  | 2013 | 主系列創新卷——Christensen 破壞式創新名文 |

### image-style-note — 5 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| True Style: The History and Principles of Classic Menswear | True Style | 2015 | Boyer 晚期集大成——逐單品講歷史與原則 |
| ABC of Men's Fashion |  | 1964 | Hardy Amies；英倫剪裁祖師的辭典式小書 |
| The Suit: A Machiavellian Approach to Men's Style | The Suit | 2006 | Antongiavanni 仿《君主論》體例談西裝——文體奇書 |
| Take Ivy |  | 1965 | 石津謙介企劃；美式 Ivy 風格的攝影聖經 |
| Icons of Men's Style |  | 2011 | Sims；逐單品的設計史——每件經典從哪來 |

### relationships-note — 5 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Games People Play | 人間遊戲 | 1964 | Berne：溝通分析（TA）的原典 |
| Hold Me Tight | 抱緊我 | 2008 | Sue Johnson：情緒取向治療（EFT） |
| How to Talk So Kids Will Listen & Listen So Kids Will Talk |  | 1980 | Faber & Mazlish：親子溝通的標準讀物 |
| The Whole-Brain Child | 教孩子跟情緒做朋友 | 2011 | Siegel：全腦教養 |
| Bowling Alone |  | 2000 | Putnam：社會資本流失的實證經典 |

### spiritual-formation-note — 5 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| De Imitatione Christi | The Imitation of Christ 效法基督 | 1418 | 金碧士：中世紀以降最廣傳的靈修經典 |
| Confessiones | Confessions 懺悔錄 | 397 | 奧古斯丁：自傳式靈修書寫的原點 |
| The Practice of the Presence of God | 與神同在 | 1692 | 勞倫斯弟兄：廚房裡的操練 |
| With Christ in the School of Prayer | 基督的禱告學校 | 1885 | 慕安德烈：代禱操練的經典 |
| Lament for a Son | 為兒子哀哭 | 1987 | 沃特斯托夫：哀傷書寫的另一座標 |

### writing-note — 5 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Writing Tools |  | 2006 | Roy Peter Clark 的 55 個寫作工具——新聞寫作圈的標準讀物 |
| The Artist's Way | 創作，是心靈療癒的旅程 | 1992 | Cameron；晨間隨筆的出處 |
| Save the Cat! | 先讓英雄救貓咪 | 2005 | Snyder 的 15 拍節奏表——好萊塢最流行的結構模板 |
| Into the Woods |  | 2013 | Yorke 的五幕論，把各家結構理論收攏成一套 |
| Draft No. 4 |  | 2017 | McPhee 談非虛構的結構——《紐約客》級的工藝示範 |

### agile-note — 4 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Kanban: Successful Evolutionary Change for Your Technology Business | Kanban | 2010 | David Anderson 的原典——看板方法的理論來源，尚未收 |
| The Principles of Product Development Flow |  | 2009 | Reinertsen 的排隊理論基礎，解釋「為什麼限制在製品有效」 |
| Impact Mapping |  | 2012 | 把商業目標接到交付項的地圖法，補使用者故事「為誰、為什麼」那一段 |
| Project Retrospectives |  | 2001 | Norm Kerth 的原典，聚焦專案結束時的長型回顧，尚未收 |

### clean-code-note — 4 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| The Art of Readable Code |  | 2011 | 可讀性專書的標準入門 |
| Tidy First? |  | 2023 | Kent Beck；小步整理的經濟學 |
| Growing Object-Oriented Software, Guided by Tests |  | 2009 | GOOS；倫敦學派 mock 驅動設計的正典 |
| The Software Craftsman |  | 2014 | Mancuso；軟體工藝運動的宣言 |

### communication-note — 4 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Bargaining for Advantage | 華頓談判學 | 1999 | Shell；談判學術與實務的教科書標準 |
| Fierce Conversations | 開啟你的正向溝通 | 2002 | Susan Scott；一次一場真對話 |
| Supercommunicators | 超級溝通者 | 2024 | Duhigg；對話配對（matching）的新科普標準 |
| The Storytelling Animal | 大腦會說故事的動物 | 2012 | Gottschall；人為何是敘事動物 |

### de-botton-note — 4 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Art as Therapy | 藝術的慰藉 | 2013 | 與 John Armstrong 合著：藝術作為心理工具——慰藉系列的收官 |
| The Pleasures and Sorrows of Work | 工作！工作！ | 2009 | 十種行業的田野書寫：工作如何承載（或承載不了）意義 |
| The News: A User's Manual | 新聞的騷動 | 2014 | 資訊焦慮時代的媒體使用手冊——慰藉方法用在新聞上 |
| The School of Life: An Emotional Education | 人生學校：了解自己 | 2019 | 人生學校十年集大成的情感教育教科書 |

### fromm-note — 4 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| On Disobedience | 論不服從 | 1981 | 不服從作為道德能力：人類始於不服從，也可能終於服從 |
| The Forgotten Language | 被遺忘的語言 | 1951 | 夢、童話與神話的象徵語言——佛洛姆的釋夢學 |
| Zen Buddhism and Psychoanalysis | 禪與心理分析 | 1960 | 與鈴木大拙合著：東方的資源如何滋養「存在樣式」 |
| Beyond the Chains of Illusion | 超越幻想的鎖鏈 | 1962 | 自述思想自傳：我與馬克思和佛洛伊德的相遇——理解佛洛姆體系的鑰匙 |

### history-note — 4 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| The Silk Roads | 絲綢之路 | 2015 | Frankopan——以貿易為軸、去歐洲中心的世界史 |
| Collapse | 大崩壞 | 2005 | Diamond 的另一半：文明如何選擇失敗 |
| 1587, a Year of No Significance | 萬曆十五年 | 1981 | 黃仁宇——大歷史觀的微觀切片，中文史學經典 |
| A Little History of the World | 世界小史 | 1935 | Gombrich——一人一筆寫完的世界史，最好的入門 |

### maxwell-note — 4 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Leadershift | 領導力轉移 | 2019 | 十一個領導轉移，晚期領導觀的更新 |
| The 17 Indisputable Laws of Teamwork | 團隊合作 17 法則 | 2001 | 從個人領導走向團隊的法則化整理 |
| Becoming a Person of Influence | 成為有影響力的人 | 1997 | 與 Jim Dornan 合著；影響力四階段的早期系統化 |
| Today Matters | 今天很重要 | 2004 | 把成長落到「每日例程」的實踐手冊，補齊行動層 |

### problem-solving-note — 4 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Bulletproof Problem Solving |  | 2019 | Conn & McLean：麥肯錫七步解題法的現代正典 |
| （邏輯思考的技術） | 邏輯思考的技術 | 2001 | 照屋華子・岡田惠子：MECE 與 So What?/Why So? 的教科書 |
| The Back of the Napkin | 餐巾紙的背後 | 2008 | Dan Roam：視覺化解題的普及經典 |
| The McKinsey Way | 專業主義：麥肯錫的成功之道 | 1999 | Ethan Rasiel：局內人視角的麥肯錫方法論第一手記錄 |

### system-design-note — 4 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Release It! |  | 2018 | Nygard；circuit breaker／bulkhead 等穩定性模式的出處 |
| The Art of Scalability |  | 2009 | Abbott & Fisher；Scale Cube（X/Y/Z 軸擴展）框架 |
| API Design Patterns |  | 2021 | Geewax；API 設計決策的模式目錄 |
| Acing the System Design Interview |  | 2024 | Zhiyong Tan；比 Alex Xu 更深入權衡討論的面試書 |

### growth-note — 3 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| The Obstacle Is the Way | 障礙就是道路 | 2014 | Holiday：斯多噶韌性的現代入門 |
| Insight |  | 2017 | Eurich：自我覺察的實證研究——內省常常做錯 |
| Awaken the Giant Within |  | 1991 | Robbins：自助正典名冊的一員，補齊譜系用 |

### learning-note — 3 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| How We Learn: Why Brains Learn Better Than Any Machine |  | 2020 | Dehaene；學習四支柱的神經科學正典 |
| Why Don't Students Like School? | 學生為什麼不喜歡上學 | 2009 | Willingham；「記憶是思考的殘留物」出處 |
| Moonwalking with Einstein | 記憶人人 hold 得住 | 2011 | Foer；記憶宮殿與記憶競技的第一手報導 |

### life-meaning-note — 3 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Emotional Intelligence EQ |  | 1995 | Goleman 的 EQ 原典（HBR 選集已收，本傳未收） |
| Being Mortal | 凝視死亡 | 2014 | Gawande——醫療極限與善終的必讀經典 |
| Tuesdays with Morrie | 最後 14 堂星期二的課 | 1997 | 臨終導師的人生課，本題最溫柔的入口 |

### management-note — 3 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Managing |  | 2009 | Mintzberg 對「管理者實際在做什麼」的實地研究——經理人角色學派正典 |
| Out of the Crisis | 轉危為安 | 1982 | Deming 十四要點；品質管理與系統觀的源頭 |
| Working Backwards | 亞馬遜逆向工作法 | 2021 | PR/FAQ 與輸入指標的亞馬遜機制 |

### newport-note — 3 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| How to Win at College |  | 2005 | 大四時寫的處女作：75 條非常規的大學致勝法則 |
| How to Become a Straight-A Student | 如何成為全A學生 | 2006 | 「偽工作」概念的起點：用更少時間拿更好成績的學習系統 |
| How to Be a High School Superstar |  | 2010 | 「鬆弛悖論」：不靠更多課外活動，靠深耕一件事到引人好奇的深度——原誤標在深度學習力的 repo 上，2026-08-06 校正 |

### stott-note — 3 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Why I Am a Christian |  | 2003 | 晚年的個人見證版《真理的尋索》——「基督的獵犬」追上他的故事 |
| Understanding the Bible | 認識聖經 | 1972 | 聖經總論入門：地理、故事、信息到讀法的一冊鳥瞰 |
| Christian Mission in the Modern World |  | 1975 | 洛桑運動時期的宣教神學：整全使命（佈道＋社會責任）的定調之作 |

### templar-note — 3 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| The Rules of Love |  | 2008 | 親密關係那一塊的缺口；系列裡與 Life 最互補的一本 |
| The Rules of Parenting |  | 2008 | 教養場域；Life 只用幾條規則帶過的部分在這裡展開 |
| The Rules to Break |  | 2012 | 反手的一本——列出那些「大家都說該遵守、其實該打破」的通則 |

### willard-note — 3 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| The Divine Conspiracy Continued | 神聖的密謀・續篇 | 2014 | 與 Gary Black 合著；天國福音延伸到職場與公共領域的領袖 |
| Living in Christ's Presence | 活在基督的同在中 | 2014 | 與 John Ortberg 的最後對談錄；臨終前的思想總回顧 |
| Life Without Lack | 一無所缺的生命 | 2018 | 身後出版的詩篇 23 篇講章：活在耶和華的豐足裡 |

### behaviour-interview-note — 2 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Decode and Conquer |  | 2013 | Lewis Lin；大廠行為題與情境題的答題框架 |
| 60 Seconds and You're Hired! |  | 1994 | 把答案收斂在一分鐘內的經典 |

### covey-note — 2 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Principle-Centered Leadership |  | 1991 | 把原則中心從個人推到組織層次的關鍵一本，尚未收 |
| The 7 Habits of Highly Effective Families |  | 1997 | 同一套原則用在家庭；柯維本人最看重的應用場域之一 |

### damodaran-note — 2 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| The Dark Side of Valuation | 估值的黑暗面 | 2001 | 年輕、高成長與困境公司的估值難題——正典外最值得補的一塊 |
| Investment Philosophies | 投資哲學 | 2003 | 把估值放進完整光譜：從價值、成長到交易，各流派的證據與適配者 |

### greene-note — 2 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| The 50th Law | 第 50 條法則 | 2009 | 與 50 Cent 合著；「無所畏懼」——48 法則之外的第 50 條 |
| The Law of the Sublime |  |  | 醞釀多年的「崇高」主題新作，出版與中譯後再收 |

### leadership-note — 2 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| The Culture Map | 文化地圖 | 2014 | Erin Meyer：跨文化團隊的八個刻度 |
| Servant Leadership |  | 1977 | Greenleaf——僕人領導思想的源頭 |

### navarro-note — 2 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Be Exceptional |  | 2021 | 晚期的正向轉向：從「讀懂別人」推到「成為值得被信任的人」 |
| Three Minutes to Doomsday |  | 2017 | 回憶錄式的間諜案偵訊實錄——方法論在真實高壓現場的完整展開 |

### tracy-note — 2 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Advanced Selling Strategies |  | 1995 | 銷售進階正典，大客戶與關係銷售的完整方法 |
| Million Dollar Habits |  | 2004 | 把財富歸因到習慣系統，補齊「習慣」這一塊拼圖 |

### bogle-note — 1 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Bogle on Mutual Funds: New Perspectives for the Intelligent Investor | 柏格談共同基金 | 1993 | 第一本書，普通投資人挑選基金的原始教本；常識投資框架在此成形 |

### design-note — 1 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Refactoring UI |  | 2018 | 工程師視角的介面設計實務，補 CRAP 到實際元件之間那一段 |

### kiyosaki-note — 1 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Rich Dad's Prophecy | 富爸爸大預言 | 2002 | 預言退休金制度（401k 世代）引發的市場危機 |

### lewis-note — 1 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| The Chronicles of Narnia | 納尼亞傳奇（七部曲） | 1950 | 1950–1956 七部合併一筆；想像護教最廣為人知的成品，值得整套收錄 |

### schwager-note — 1 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| Market Sense and Nonsense | 市場真相 | 2012 | 拆解投資圈流行謬誤：效率市場、波動度、對沖基金迷思的實證清算 |

### uncle-bob-note — 1 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| We, Programmers: A Chronicle of Coders from Ada to AI |  | 2024 | 晚年回望：從 Ada 到 AI 的程式設計師群像史——目前最大的缺口 |

### wan-weigang-note — 1 本

| 英文書名 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- |
| （你有你的計劃，世界另有計劃） | 你有你的計劃，世界另有計劃 | 2019 | 精英日課結集之一；原列在建議閱讀路徑卻沒有對應書站，2026-08-05 校正為待收 |

## 沒有英文書名的 20 本（華文／日文原著）

這些本來就沒有英文版，照原書名收。

| 原書名 | 站 | 為何想收 |
| --- | --- | --- |
| 三十六大 | fengtang-note | 三十六封公開信：「大」系列雜文的代表作 |
| 成事：馮唐品讀曾國藩嘉言鈔 | fengtang-note | 成事學的起點：逐條品讀曾國藩嘉言——《成事心法》的前作 |
| 活著活著就老了 | fengtang-note | 雜文成名作；馮唐聲口的原型——文學觀與人生觀的底稿 |
| 無所畏 | fengtang-note | 中年心境的雜文集：無所畏與無所謂之間 |
| 萬物生長三部曲（十八歲給我一個姑娘／萬物生長／北京，北京） | fengtang-note | 青春三部曲：文學馮唐的主線長篇，一筆合併收錄 |
| 馮唐詩百首 | fengtang-note | 「春風十里，不如你」的出處；詩人馮唐的代表集 |
| 互聯網+：傳統企業，互聯網在踢門 | liurun-note | 成名作：傳統企業轉型的早期宣言 |
| 商業簡史 | liurun-note | 把商業進化史讀成「交易成本不斷降低」的歷史——底層邏輯的史學版 |
| 新零售：低價高效的數據賦能之路 | liurun-note | 「人貨場」重構的新零售方法論 |
| 趨勢紅利 | liurun-note | 早期代表作：紅利＝短暫供需失衡的出處 |
| 進化的力量2 | liurun-note | 年度演講系列續作；趨勢判讀框架的年度更新 |
| 關鍵躍升：新任管理者的底層邏輯 | liurun-note | 寫給新手管理者的「驚險一躍」專書——管理分類的直接補強 |
| 邏輯思考的技術 | problem-solving-note | 照屋華子・岡田惠子：MECE 與 So What?/Why So? 的教科書 |
| 你有你的計劃，世界另有計劃 | wan-weigang-note | 精英日課結集之一；原列在建議閱讀路徑卻沒有對應書站，2026-08-05 校正為待收 |
| 信息傳 | wujun-note | 資訊史詩；香農資訊論如何成為理解未來的方法論（無繁中版） |
| 全球科技通史 | wujun-note | 從石器到量子的科技全史；「能量與資訊」雙主線的史觀 |
| 吳軍數學通識講義 | wujun-note | 得到課程結集；把數學史講成通識教育的系統嘗試 |
| 大學之路 | wujun-note | 兩冊英美名校巡禮；博雅教育理念最完整的陳述 |
| 文明之光 | wujun-note | 四冊文明史；把科技放進人類文明長河的大歷史書寫 |
| 智能時代 | wujun-note | 大數據與智能革命的方法論——AI 浪潮前夜的預言書 |

## 重跑

```bash
notes-core/tools/export-wanted.py
```

收到書、建好書站之後，把該站 bibliography 那筆改成 `status: "owned"` 並補 `slug`，
重跑就會從這裡消失。
