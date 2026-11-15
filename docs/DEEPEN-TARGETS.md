# 深挖對象：大部頭卻只有一鏟的正典

> **生成於 2026-11-15T14:58:26+08:00**｜由 `tools/export-deepen-targets.py` 產生，**不要手改**——改資料源再重跑。

**這份是什麼**：書的層級的排序表——**進站之後該挖哪本書**。與 [DEEPEN-READY.md](./DEEPEN-READY.md) 的分工：那份回答「該進哪一站」（站的層級），這份回答「進站之後挖哪一本」。兩份都是排序表，工作日誌在 [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md)。

**為什麼需要它**：判層債歸零後，「哪裡還薄」失去了現成訊號——`tier-audit` 只抓「spine 且**零**引用」，**被引 1 次的 spine 一律放行**，而那正是大部頭最常見的狀態。theology-note 49 本 spine 每本恰好 1 頁、management-note 42 本裡 37 本只有 1 頁：健康，但薄得看不出來。

**判準**：`tier: spine`、書 repo 章節數 ≥ **30**（書庫 1776 本的中位數是 18、90 百分位是 48）、且站上引到它的**不同頁數 ≤ 1**。排序鍵是 `章節數 ÷ 頁數`。

**這份只排序，不開單。** 每頁該切哪個概念、跟既有頁怎麼分工、anchor 落哪幾章，仍是進站跑 `/note-check --enrich` 時的判斷（依 MODEL-ROUTING 留給 Fable 開單）。

## 摘要

| 項目 | 數 |
| --- | ---: |
| 掃過的站 | 78 |
| **候選（大部頭 × ≤1 頁）** | **113** |
| 涉及的站 | 42 |
| 依體裁排除 | 16 |
| 已裁定不開 | 17 |

## 一、前 30 名（跨站總排序）

| # | 章節 | 頁 | 站 | 書 |
| ---: | ---: | ---: | --- | --- |
| 1 | 109 | 1 | `templar-note` | The Rules of Management |
| 2 | 91 | 1 | `keller-note` | 恐懼時代的盼望 |
| 3 | 78 | 1 | `personal-finance-note` | Early Retirement Extreme |
| 4 | 76 | 1 | `relationships-note` | The Book You Wish Your Parents Had Read |
| 5 | 75 | 1 | `theology-note` | 基督教神學（艾利克森） |
| 6 | 65 | 1 | `wan-weigang-note` | 你有你的計劃，世界另有計劃 |
| 7 | 65 | 1 | `hbr-note` | HBR Guide to Persuasive Presentations |
| 8 | 64 | 1 | `tools-note` | Flow 心流 |
| 9 | 63 | 1 | `wujun-note` | 大學之路 |
| 10 | 63 | 1 | `investing-note` | Security Analysis |
| 11 | 63 | 1 | `biblical-studies-note` | Exegetical Fallacies |
| 12 | 62 | 1 | `writing-note` | Writing Tools |
| 13 | 62 | 1 | `clean-code-note` | The Pragmatic Programmer |
| 14 | 61 | 1 | `stott-note` | 當代講道藝術 |
| 15 | 56 | 1 | `theology-note` | 系統神學（章力生等華人卷） |
| 16 | 56 | 1 | `data-systems-note` | Versioning in an Event Sourced System |
| 17 | 55 | 1 | `travel-note` | 破億下載 Podcast 製作人的經營指南 |
| 18 | 52 | 1 | `wujun-note` | 見識 |
| 19 | 52 | 1 | `habits-note` | 18 Minutes |
| 20 | 52 | 1 | `growth-note` | Mastery |
| 21 | 52 | 1 | `fengtang-note` | 勝者心法：資治通鑑成事之道 |
| 22 | 51 | 1 | `wellness-note` | The 4-Hour Body 身體調校聖經 |
| 23 | 51 | 1 | `travel-note` | The Almost Nearly Perfect People |
| 24 | 50 | 1 | `theology-note` | 神學的故事 |
| 25 | 50 | 1 | `maxwell-note` | 360 度全方位領導 |
| 26 | 49 | 1 | `kiyosaki-note` | 富爸爸投資指南 |
| 27 | 48 | 1 | `wujun-note` | 富足 |
| 28 | 47 | 1 | `system-design-note` | The Software Architect Elevator |
| 29 | 47 | 1 | `management-note` | 程天縱《專業力》 |
| 30 | 47 | 1 | `economics-note` | Misbehaving 不當行為 |

## 二、依站分組

開單時整站一起看比較省力——同一站的候選常常共享脈絡。

### `travel-note`（12 本）

- **破億下載 Podcast 製作人的經營指南** — 55 章 / 1 頁（`podcast-producer-guide`）
- **The Almost Nearly Perfect People** — 51 章 / 1 頁（`almost-nearly-perfect-people`）
- **So You Want to Start a Podcast** — 46 章 / 1 頁（`so-you-want-to-start-a-podcast`）
- **Grammar of the Shot** — 46 章 / 1 頁（`grammar-of-the-shot`）
- **Europe Through the Back Door** — 42 章 / 1 頁（`europe-through-the-back-door`）
- **文化苦旅** — 39 章 / 1 頁（`bittersweet-journey-through-culture`）
- **Germany: Memories of a Nation** — 38 章 / 1 頁（`germany-memories-of-a-nation`）
- **The Penguin History of New Zealand** — 36 章 / 1 頁（`penguin-history-of-new-zealand`）
- **The Business of Tourism** — 33 章 / 1 頁（`business-of-tourism`）
- **The Rise and Fall of Ancient Egypt** — 31 章 / 1 頁（`rise-and-fall-of-ancient-egypt`）
- **The Story of Art** — 30 章 / 1 頁（`story-of-art`）
- **In the Blink of an Eye** — 30 章 / 1 頁（`in-the-blink-of-an-eye`）

### `wujun-note`（9 本）

- **大學之路** — 63 章 / 1 頁（`wujun-road-to-university`）
- **見識** — 52 章 / 1 頁（`wujun-insight`）
- **富足** — 48 章 / 1 頁（`wujun-abundance`）
- **態度** — 46 章 / 1 頁（`wujun-attitude`）
- **信息傳** — 45 章 / 1 頁（`wujun-information-theory-40`）
- **數學之美** — 40 章 / 1 頁（`wujun-beauty-of-math`）
- **脈絡** — 38 章 / 1 頁（`wujun-context`）
- **境界** — 36 章 / 1 頁（`wujun-realm`）
- **卓越** — 36 章 / 1 頁（`wujun-excellence`）

### `theology-note`（7 本）

- **基督教神學（艾利克森）** — 75 章 / 1 頁（`erickson-christian-theology`）
- **系統神學（章力生等華人卷）** — 56 章 / 1 頁（`systematic-theology`）
- **神學的故事** — 50 章 / 1 頁（`story-of-christian-theology`）
- **The Story of Christianity, Vol. 1** — 45 章 / 1 頁（`story-of-christianity-vol-1`）
- **追隨基督（做門徒的代價）** — 38 章 / 1 頁（`cost-of-discipleship`）
- **返璞歸真：純粹的基督教** — 38 章 / 1 頁（`mere-christianity`）
- **改革宗教理學** — 33 章 / 1 頁（`reformed-dogmatics`）

### `biblical-studies-note`（7 本）

- **Exegetical Fallacies** — 63 章 / 1 頁（`exegetical-fallacies`）
- **上帝子民的新約導論** — 46 章 / 1 頁（`new-testament-in-its-world`）
- **走入中東看耶穌** — 39 章 / 1 頁（`jesus-through-middle-eastern-eyes`）
- **新約的聖經神學** — 38 章 / 1 頁（`a-new-testament-biblical-theology`）
- **按照計畫** — 35 章 / 1 頁（`according-to-plan`）
- **Theology of the Old Testament** — 35 章 / 1 頁（`theology-of-the-old-testament`）
- **先知神學** — 32 章 / 1 頁（`prophets-heschel`）

### `management-note`（5 本）

- **程天縱《專業力》** — 47 章 / 1 頁（`terry-cheng-professional-power`）
- **Peopleware 腦力密集產業的人才管理之道** — 46 章 / 1 頁（`peopleware`）
- **The Goal 目標** — 43 章 / 1 頁（`goal-ongoing-improvement`）
- **程天縱《經營學》** — 35 章 / 1 頁（`terry-cheng-business-management`）
- **Turn the Ship Around! 當責領導** — 35 章 / 1 頁（`turn-the-ship-around`）

### `hbr-note`（4 本）

- **HBR Guide to Persuasive Presentations** — 65 章 / 1 頁（`hbr-guide-to-persuasive-presentations`）
- **HBR Guide to Thinking Strategically** — 39 章 / 1 頁（`hbr-guide-to-thinking-strategically`）
- **HBR Guide to Better Recruiting and Hiring** — 35 章 / 1 頁（`hbr-guide-to-better-recruiting-and-hiring`）
- **HBR Guide to Making Better Decisions** — 31 章 / 1 頁（`hbr-guide-to-making-better-decisions`）

### `wellness-note`（4 本）

- **The 4-Hour Body 身體調校聖經** — 51 章 / 1 頁（`4-hour-body`）
- **Bigger Leaner Stronger** — 44 章 / 1 頁（`bigger-leaner-stronger`）
- **HBR Guide to Managing Stress** — 34 章 / 1 頁（`hbr-guide-to-managing-stress`）
- **How Not to Die 食療聖經** — 33 章 / 1 頁（`how-not-to-die`）

### `system-design-note`（4 本）

- **The Software Architect Elevator** — 47 章 / 1 頁（`software-architect-elevator`）
- **The Art of Scalability** — 39 章 / 1 頁（`art-of-scalability`）
- **API Design Patterns** — 37 章 / 1 頁（`api-design-patterns`）
- **軟體架構實踐** — 32 章 / 1 頁（`software-architecture-in-practice`）

### `economics-note`（4 本）

- **Misbehaving 不當行為** — 47 章 / 1 頁（`misbehaving`）
- **Central Bank Privilege** — 39 章 / 1 頁（`central-bank-privilege`）
- **The General Theory of Employment, Interest and Money 就業、利息與貨幣的一般理論** — 31 章 / 1 頁（`general-theory-of-employment-interest-and-money`）
- **Lords of Finance** — 30 章 / 1 頁（`lords-of-finance`）

### `relationships-note`（3 本）

- **The Book You Wish Your Parents Had Read** — 76 章 / 1 頁（`book-you-wish-your-parents-had-read`）
- **Winning with People** — 32 章 / 1 頁（`winning-with-people`）
- **Bowling Alone** — 30 章 / 1 頁（`bowling-alone`）

### `investing-note`（3 本）

- **Security Analysis** — 63 章 / 1 頁（`security-analysis`）
- **Winning the Loser's Game** — 36 章 / 1 頁（`winning-the-losers-game-ellis`）
- **Investment Valuation** — 35 章 / 1 頁（`investment-valuation`）

### `writing-note`（3 本）

- **Writing Tools** — 62 章 / 1 頁（`writing-tools`）
- **The War of Art** — 32 章 / 1 頁（`war-of-art`）
- **Into the Woods** — 30 章 / 1 頁（`into-the-woods`）

### `maxwell-note`（3 本）

- **360 度全方位領導** — 50 章 / 1 頁（`360-degree-leader`）
- **領導力的 5 個層次** — 42 章 / 1 頁（`5-levels-of-leadership`）
- **與人同贏** — 32 章 / 1 頁（`winning-with-people`）

### `career-note`（3 本）

- **Staff Engineer: Leadership beyond the management track** — 45 章 / 1 頁（`staff-engineer`）
- **創客創業導師程天縱的職場力：解析職場的人與事，提升工作與管理績效的34條建言** — 40 章 / 1 頁（`terry-cheng-workplace-power`）
- **Never Eat Alone 別自己一個人吃飯** — 39 章 / 1 頁（`never-eat-alone`）

### `business-strategy-note`（3 本）

- **The Practice of Management 彼得‧杜拉克的管理聖經** — 37 章 / 1 頁（`practice-of-management`）
- **Managing in a Time of Great Change 巨變時代的管理** — 32 章 / 1 頁（`managing-in-a-time-of-great-change`）
- **The Essential Drucker 杜拉克精選** — 31 章 / 1 頁（`essential-drucker`）

### `personal-finance-note`（2 本）

- **Early Retirement Extreme** — 78 章 / 1 頁（`early-retirement-extreme`）
- **The Simple Path to Wealth** — 41 章 / 1 頁（`simple-path-to-wealth`）

### `tools-note`（2 本）

- **Flow 心流** — 64 章 / 1 頁（`flow-psychology-of-happiness`）
- **Indistractable 專注力協定** — 44 章 / 1 頁（`indistractable`）

### `clean-code-note`（2 本）

- **The Pragmatic Programmer** — 62 章 / 1 頁（`pragmatic-programmer`）
- **Growing Object-Oriented Software, Guided by Tests** — 34 章 / 1 頁（`growing-object-oriented-software`）

### `data-systems-note`（2 本）

- **Versioning in an Event Sourced System** — 56 章 / 1 頁（`versioning-in-an-event-sourced-system`）
- **SQL Performance Explained** — 42 章 / 1 頁（`sql-performance-explained`）

### `habits-note`（2 本）

- **18 Minutes** — 52 章 / 1 頁（`18-minutes`）
- **The War of Art** — 32 章 / 1 頁（`war-of-art`）

### `design-patterns-note`（2 本）

- **Refactoring to Patterns** — 41 章 / 1 頁（`refactoring-to-patterns`）
- **The Timeless Way of Building** — 31 章 / 1 頁（`timeless-way-of-building`）

### `history-note`（2 本）

- **文學的40堂公開課** — 40 章 / 1 頁（`little-history-of-literature`）
- **餐桌儀式** — 34 章 / 1 頁（`rituals-of-dinner`）

### `data-science-note`（2 本）

- **數學之美** — 40 章 / 1 頁（`wujun-beauty-of-math`）
- **Noise 雜訊** — 37 章 / 1 頁（`noise`）

### `spiritual-formation-note`（2 本）

- **The Cost of Discipleship 追隨基督** — 38 章 / 1 頁（`cost-of-discipleship`）
- **With Christ in the School of Prayer 基督的禱告學校** — 32 章 / 1 頁（`with-christ-in-the-school-of-prayer`）

### `liurun-note`（2 本）

- **關鍵躍升：新任管理者的底層邏輯** — 36 章 / 1 頁（`liurun-key-leap`）
- **商業簡史** — 32 章 / 1 頁（`liurun-evolution-of-business`）

### `thinking-note`（2 本）

- **Emotional Intelligence EQ** — 35 章 / 1 頁（`emotional-intelligence`）
- **Seeking Wisdom** — 31 章 / 1 頁（`seeking-wisdom`）

### `communication-note`（2 本）

- **Thank You for Arguing 說理** — 35 章 / 1 頁（`thank-you-for-arguing`）
- **The Speed of Trust 高效信任力** — 30 章 / 1 頁（`speed-of-trust`）

### `templar-note`（1 本）

- **The Rules of Management** — 109 章 / 1 頁（`rules-of-management`）

### `keller-note`（1 本）

- **恐懼時代的盼望** — 91 章 / 1 頁（`hope-in-times-of-fear`）

### `wan-weigang-note`（1 本）

- **你有你的計劃，世界另有計劃** — 65 章 / 1 頁（`wan-weigang-world-has-another-plan`）

### `stott-note`（1 本）

- **當代講道藝術** — 61 章 / 1 頁（`i-believe-in-preaching`）

### `growth-note`（1 本）

- **Mastery** — 52 章 / 1 頁（`mastery`）

### `fengtang-note`（1 本）

- **勝者心法：資治通鑑成事之道** — 52 章 / 1 頁（`fengtang-winner-method`）

### `kiyosaki-note`（1 本）

- **富爸爸投資指南** — 49 章 / 1 頁（`rich-dads-guide-to-investing`）

### `startup-note`（1 本）

- **Blitzscaling 閃電擴張** — 38 章 / 1 頁（`blitzscaling`）

### `lewis-note`（1 本）

- **返璞歸真** — 38 章 / 1 頁（`mere-christianity`）

### `cloud-infra-note`（1 本）

- **Seeking SRE** — 38 章 / 1 頁（`seeking-sre`）

### `leadership-note`（1 本）

- **Leaders Eat Last** — 36 章 / 1 頁（`leaders-eat-last`）

### `covey-note`（1 本）

- **Principle-Centered Leadership** — 35 章 / 1 頁（`principle-centered-leadership`）

### `hr-note`（1 本）

- **HBR Guide to Retaining Your Best People** — 34 章 / 1 頁（`hbr-guide-to-retaining-your-best-people`）

### `agile-note`（1 本）

- **Extreme Programming Explained** — 33 章 / 1 頁（`extreme-programming-explained`）

### `security-note`（1 本）

- **Practical Malware Analysis** — 30 章 / 1 頁（`practical-malware-analysis`）

## 三、依體裁排除：16 本

這些書章節數必然很高，但體裁上就不該挖成多頁——不排除會永遠霸佔排行前段。清單在 `export-deepen-targets.py` 的 `EXCLUDED_KINDS`；加新的要寫**體裁**理由，「暫時不想挖」屬於選題，不該寫進工具。

- `behaviour-interview-note` — 軟技能：soft skills，讓你不過時、不貶值、不消失：多作者書信合輯，三十封各自獨立
- `biblical-studies-note` — 聖經導覽手冊：逐卷讀經的藝術：逐卷導覽，按卷查閱
- `biblical-studies-note` — 聖經經典500問：逐條釋疑合輯，按經文查閱
- `fengtang-note` — 穩贏：中年隨筆結集，六十九篇各自獨立
- `habits-note` — 365 Days With Self-Discipline：日課型，365 則每日短文按週合輯
- `history-note` — 古拉格群島：文學性紀實巨著
- `jung-note` — 紅書：幻象記錄，章節是幻象序列與評註，概念已由導論抽出
- `lewis-note` — The Screwtape Letters：書信體，31 封短信各千餘字
- `lewis-note` — 納尼亞傳奇（七部曲）：小說七部曲
- `liurun-note` — 5分鐘商學院 工具篇：工具條目合輯，每條各自獨立
- `philosophy-note` — Philosophy: The Classics 哲學經典的 32 堂公開課：逐本導讀，三十二章各講一部原典，按書查閱；排除是排榜，不禁止從它選題
- `startup-note` — Rework 工作大解放：格言體雜文集，近九十節各一兩頁、只給立場不給流程
- `theology-note` — 地獄來鴻：書信體，31 封短信各千餘字
- `theology-note` — 當代神學辭典：神學辭典，按條目查閱
- `thinking-note` — The Art of Thinking Clearly 思考的藝術：轉譯型偏誤短文合輯，近百則互不相承
- `wellness-note` — Tools of Titans 巨人的工具：訪談語錄合輯，一人一條目，按人物查閱

## 四、已裁定不開：17 本

開單時逐本看過、判第一鏟已兌現、歸姊妹站或材料太薄的書。這是選題判斷，不是體裁；清單在 `export-deepen-targets.py` 的 `SETTLED_BOOKS`，理由失效就從表上刪掉。

- `agile-note` — Impact Mapping（2026-11-12）：章多而薄，兩個實質部已用；剩下是與既有實踐的定位章
- `career-note` — 精通行為面試：科技業說故事指南（2026-11-12）：behaviour-interview-note 四十一頁是體系深挖，本站是總覽頁
- `clean-code-note` — Test-Driven Development（2026-11-12）：kent-beck-note 五頁已挖完三部
- `habits-note` — How to Have a Good Day（2026-11-12）：生產力四章是技巧清單，兩招是 Eyal 轉述而原典頁已在
- `hbr-note` — HBR Guide to Making Every Meeting Matter（2026-11-12）：第一鏟已走完會議全生命週期，領導高峰會章收成 details
- `hbr-note` — HBR Guide to Navigating the Toxic Workplace（2026-11-12）：三十三章已用約二十章，其餘各一千字湊不成主張
- `leadership-note` — Turn the Ship Around!（2026-11-12）：四部都有頁：本站 leader-leader 掛一二部、management-note 掛三四部
- `life-meaning-note` — Bigger Leaner Stronger（2026-11-12）：飲食端第二鏟歸 wellness，本站不收飲食頁
- `management-note` — The Five Dysfunctions of a Team 團隊領導的五大障礙（2026-11-06）：模型與工具已在本站一頁、寓言歸 leadership 三頁，剩下是故事重述
- `newport-note` — How to Win at College（2026-11-12）：兩條原則已在 pseudo-work 與 career-capital-over-passion 的成熟版
- `personal-finance-note` — The Millionaire Fastlane 快速致富（2026-11-12）：第一鏟四部用盡，剩自我管理與創業執行不屬理財站
- `science-note` — 高手相對論（2026-11-12）：同上，與 wan-weigang-note 共用一次裁定
- `startup-note` — Anything You Want（2026-11-12）：授權四章不到四千字，收進 purpose-over-money 的 details
- `theology-note` — 活的教會（2026-11-06）：第一鏟已用八章裡的七章，講道章歸 stott-note
- `travel-note` — How to Be a Travel Writer（2026-11-12）：速成課已用，其餘是投稿、SEO、謀生與資源清單
- `travel-note` — Istanbul: Memories and the City（2026-11-12）：呼愁骨幹已用，其餘三十章是家族回憶與畫家專欄
- `wan-weigang-note` — 高手相對論（2026-11-12）：14 章 56 小節各數百字，章節數是小節撐高的；兩站兩頁已覆蓋物理骨幹與不變量世界觀

## 重跑

```bash
notes-core/tools/export-deepen-targets.py
```

補完某本書的第二頁之後重跑，該筆就會從這裡消失。
