# 深挖對象：大部頭卻只有一鏟的正典

> **生成於 2026-08-27T01:05:09+08:00**｜由 `tools/export-deepen-targets.py` 產生，**不要手改**——改資料源再重跑。

**這份是什麼**：書的層級的排序表——**進站之後該挖哪本書**。與 [DEEPEN-READY.md](./DEEPEN-READY.md) 的分工：那份回答「該進哪一站」（站的層級），這份回答「進站之後挖哪一本」。兩份都是排序表，工作日誌在 [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md)。

**為什麼需要它**：判層債歸零後，「哪裡還薄」失去了現成訊號——`tier-audit` 只抓「spine 且**零**引用」，**被引 1 次的 spine 一律放行**，而那正是大部頭最常見的狀態。theology-note 49 本 spine 每本恰好 1 頁、management-note 42 本裡 37 本只有 1 頁：健康，但薄得看不出來。

**判準**：`tier: spine`、書 repo 章節數 ≥ **30**（書庫 1776 本的中位數是 18、90 百分位是 48）、且站上引到它的**不同頁數 ≤ 1**。排序鍵是 `章節數 ÷ 頁數`。

**這份只排序，不開單。** 每頁該切哪個概念、跟既有頁怎麼分工、anchor 落哪幾章，仍是進站跑 `/note-check --enrich` 時的判斷（依 MODEL-ROUTING 留給 Fable 開單）。

## 摘要

| 項目 | 數 |
| --- | ---: |
| 掃過的站 | 75 |
| **候選（大部頭 × ≤1 頁）** | **123** |
| 涉及的站 | 44 |
| 依體裁排除 | 4 |

## 一、前 30 名（跨站總排序）

| # | 章節 | 頁 | 站 | 書 |
| ---: | ---: | ---: | --- | --- |
| 1 | 109 | 1 | `templar-note` | The Rules of Management |
| 2 | 104 | 1 | `templar-note` | The Rules of People |
| 3 | 101 | 1 | `thinking-note` | The Art of Thinking Clearly 思考的藝術 |
| 4 | 101 | 1 | `startup-note` | Rework 工作大解放 |
| 5 | 91 | 1 | `keller-note` | 恐懼時代的盼望 |
| 6 | 78 | 1 | `personal-finance-note` | Early Retirement Extreme |
| 7 | 76 | 1 | `relationships-note` | The Book You Wish Your Parents Had Read |
| 8 | 76 | 1 | `newport-note` | How to Win at College |
| 9 | 75 | 1 | `theology-note` | 基督教神學（艾利克森） |
| 10 | 69 | 1 | `fengtang-note` | 穩贏 |
| 11 | 65 | 1 | `wan-weigang-note` | 你有你的計劃，世界另有計劃 |
| 12 | 65 | 1 | `hbr-note` | HBR Guide to Persuasive Presentations |
| 13 | 64 | 1 | `tools-note` | Flow 心流 |
| 14 | 63 | 1 | `wujun-note` | 大學之路 |
| 15 | 63 | 1 | `investing-note` | Security Analysis |
| 16 | 63 | 1 | `biblical-studies-note` | Exegetical Fallacies |
| 17 | 62 | 1 | `clean-code-note` | The Pragmatic Programmer |
| 18 | 61 | 1 | `stott-note` | 當代講道藝術 |
| 19 | 60 | 1 | `wan-weigang-note` | 高手相對論 |
| 20 | 60 | 1 | `science-note` | 高手相對論 |
| 21 | 59 | 1 | `fengtang-note` | 能人謀勢 |
| 22 | 59 | 1 | `design-note` | Refactoring UI |
| 23 | 58 | 1 | `biblical-studies-note` | 聖經導覽手冊：逐卷讀經的藝術 |
| 24 | 56 | 1 | `theology-note` | 系統神學（章力生等華人卷） |
| 25 | 56 | 1 | `data-systems-note` | Versioning in an Event Sourced System |
| 26 | 55 | 1 | `personal-finance-note` | The Millionaire Fastlane 快速致富 |
| 27 | 55 | 1 | `habits-note` | 365 Days With Self-Discipline |
| 28 | 53 | 1 | `startup-note` | Anything You Want |
| 29 | 52 | 1 | `wujun-note` | 見識 |
| 30 | 52 | 1 | `management-note` | The Five Dysfunctions of a Team 團隊領導的五大障礙 |

## 二、依站分組

開單時整站一起看比較省力——同一站的候選常常共享脈絡。

### `theology-note`（9 本）

- **基督教神學（艾利克森）** — 75 章 / 1 頁（`erickson-christian-theology`）
- **系統神學（章力生等華人卷）** — 56 章 / 1 頁（`systematic-theology`）
- **神學的故事** — 50 章 / 1 頁（`story-of-christian-theology`）
- **活的教會** — 46 章 / 1 頁（`living-church`）
- **The Story of Christianity（兩卷）** — 45 章 / 1 頁（`story-of-christianity-vol-1`）
- **追隨基督（做門徒的代價）** — 38 章 / 1 頁（`cost-of-discipleship`）
- **返璞歸真：純粹的基督教** — 38 章 / 1 頁（`mere-christianity`）
- **改革宗教理學** — 33 章 / 1 頁（`reformed-dogmatics`）
- **地獄來鴻** — 31 章 / 1 頁（`screwtape-letters`）

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

### `biblical-studies-note`（9 本）

- **Exegetical Fallacies** — 63 章 / 1 頁（`exegetical-fallacies`）
- **聖經導覽手冊：逐卷讀經的藝術** — 58 章 / 1 頁（`how-to-read-the-bible-book-by-book`）
- **聖經經典500問** — 51 章 / 1 頁（`hard-sayings-of-the-bible`）
- **上帝子民的新約導論** — 46 章 / 1 頁（`new-testament-in-its-world`）
- **走入中東看耶穌** — 39 章 / 1 頁（`jesus-through-middle-eastern-eyes`）
- **新約的聖經神學** — 38 章 / 1 頁（`a-new-testament-biblical-theology`）
- **按照計畫** — 35 章 / 1 頁（`according-to-plan`）
- **Theology of the Old Testament** — 35 章 / 1 頁（`theology-of-the-old-testament`）
- **先知神學** — 32 章 / 1 頁（`prophets-heschel`）

### `hbr-note`（6 本）

- **HBR Guide to Persuasive Presentations** — 65 章 / 1 頁（`hbr-guide-to-persuasive-presentations`）
- **HBR Guide to Thinking Strategically** — 39 章 / 1 頁（`hbr-guide-to-thinking-strategically`）
- **HBR Guide to Making Every Meeting Matter** — 37 章 / 1 頁（`hbr-guide-to-making-every-meeting-matter`）
- **HBR Guide to Better Recruiting and Hiring** — 35 章 / 1 頁（`hbr-guide-to-better-recruiting-and-hiring`）
- **HBR Guide to Navigating the Toxic Workplace** — 33 章 / 1 頁（`hbr-guide-to-navigating-the-toxic-workplace`）
- **HBR Guide to Making Better Decisions** — 31 章 / 1 頁（`hbr-guide-to-making-better-decisions`）

### `management-note`（6 本）

- **The Five Dysfunctions of a Team 團隊領導的五大障礙** — 52 章 / 1 頁（`five-dysfunctions-of-a-team`）
- **程天縱《專業力》** — 47 章 / 1 頁（`terry-cheng-professional-power`）
- **Peopleware 腦力密集產業的人才管理之道** — 46 章 / 1 頁（`peopleware`）
- **The Goal 目標** — 43 章 / 1 頁（`goal-ongoing-improvement`）
- **程天縱《經營學》** — 35 章 / 1 頁（`terry-cheng-business-management`）
- **Turn the Ship Around! 當責領導** — 35 章 / 1 頁（`turn-the-ship-around`）

### `wellness-note`（5 本）

- **The 4-Hour Body 身體調校聖經** — 51 章 / 1 頁（`4-hour-body`）
- **Bigger Leaner Stronger** — 44 章 / 1 頁（`bigger-leaner-stronger`）
- **Tools of Titans 巨人的工具** — 36 章 / 1 頁（`tools-of-titans`）
- **HBR Guide to Managing Stress** — 34 章 / 1 頁（`hbr-guide-to-managing-stress`）
- **How Not to Die 食療聖經** — 33 章 / 1 頁（`how-not-to-die`）

### `fengtang-note`（4 本）

- **穩贏** — 69 章 / 1 頁（`fengtang-stable-win`）
- **能人謀勢** — 59 章 / 1 頁（`fengtang-capable-strategy`）
- **勝者心法：資治通鑑成事之道** — 52 章 / 1 頁（`fengtang-winner-method`）
- **有本事** — 50 章 / 1 頁（`fengtang-have-capability`）

### `habits-note`（4 本）

- **365 Days With Self-Discipline** — 55 章 / 1 頁（`365-days-with-self-discipline`）
- **18 Minutes** — 52 章 / 1 頁（`18-minutes`）
- **The War of Art** — 32 章 / 1 頁（`war-of-art`）
- **How to Have a Good Day** — 30 章 / 1 頁（`how-to-have-a-good-day`）

### `economics-note`（4 本）

- **Misbehaving 不當行為** — 47 章 / 1 頁（`misbehaving`）
- **Central Bank Privilege** — 40 章 / 1 頁（`central-bank-privilege`）
- **The General Theory of Employment, Interest and Money 就業、利息與貨幣的一般理論** — 31 章 / 1 頁（`general-theory-of-employment-interest-and-money`）
- **Lords of Finance** — 30 章 / 1 頁（`lords-of-finance`）

### `career-note`（4 本）

- **Staff Engineer: Leadership beyond the management track** — 45 章 / 1 頁（`staff-engineer`）
- **創客創業導師程天縱的職場力：解析職場的人與事，提升工作與管理績效的34條建言** — 40 章 / 1 頁（`terry-cheng-workplace-power`）
- **Never Eat Alone 別自己一個人吃飯** — 39 章 / 1 頁（`never-eat-alone`）
- **精通行為面試：科技業說故事指南** — 38 章 / 1 頁（`mastering-behavioral-interviews`）

### `thinking-note`（3 本）

- **The Art of Thinking Clearly 思考的藝術** — 101 章 / 1 頁（`art-of-thinking-clearly`）
- **Emotional Intelligence EQ** — 35 章 / 1 頁（`emotional-intelligence`）
- **Seeking Wisdom** — 31 章 / 1 頁（`seeking-wisdom`）

### `startup-note`（3 本）

- **Rework 工作大解放** — 101 章 / 1 頁（`rework`）
- **Anything You Want** — 53 章 / 1 頁（`anything-you-want`）
- **Blitzscaling 閃電擴張** — 38 章 / 1 頁（`blitzscaling`）

### `personal-finance-note`（3 本）

- **Early Retirement Extreme** — 78 章 / 1 頁（`early-retirement-extreme`）
- **The Millionaire Fastlane 快速致富** — 55 章 / 1 頁（`millionaire-fastlane`）
- **The Simple Path to Wealth** — 41 章 / 1 頁（`simple-path-to-wealth`）

### `relationships-note`（3 本）

- **The Book You Wish Your Parents Had Read** — 76 章 / 1 頁（`book-you-wish-your-parents-had-read`）
- **Winning with People** — 32 章 / 1 頁（`winning-with-people`）
- **Bowling Alone** — 30 章 / 1 頁（`bowling-alone`）

### `wan-weigang-note`（3 本）

- **你有你的計劃，世界另有計劃** — 65 章 / 1 頁（`wan-weigang-world-has-another-plan`）
- **高手相對論** — 60 章 / 1 頁（`wan-weigang-what-is-relativity`）
- **萬萬沒想到** — 46 章 / 1 頁（`wan-weigang-wanwan-meixiangdao`）

### `investing-note`（3 本）

- **Security Analysis** — 63 章 / 1 頁（`security-analysis`）
- **Winning the Loser's Game** — 36 章 / 1 頁（`winning-the-losers-game-ellis`）
- **Investment Valuation** — 35 章 / 1 頁（`investment-valuation`）

### `clean-code-note`（3 本）

- **The Pragmatic Programmer** — 62 章 / 1 頁（`pragmatic-programmer`）
- **Test-Driven Development** — 35 章 / 1 頁（`test-driven-development`）
- **Growing Object-Oriented Software, Guided by Tests** — 34 章 / 1 頁（`growing-object-oriented-software`）

### `maxwell-note`（3 本）

- **360 度全方位領導** — 50 章 / 1 頁（`360-degree-leader`）
- **領導力的 5 個層次** — 42 章 / 1 頁（`5-levels-of-leadership`）
- **與人同贏** — 32 章 / 1 頁（`winning-with-people`）

### `business-strategy-note`（3 本）

- **The Practice of Management 彼得‧杜拉克的管理聖經** — 37 章 / 1 頁（`practice-of-management`）
- **Managing in a Time of Great Change 巨變時代的管理** — 32 章 / 1 頁（`managing-in-a-time-of-great-change`）
- **The Essential Drucker 杜拉克精選** — 31 章 / 1 頁（`essential-drucker`）

### `templar-note`（2 本）

- **The Rules of Management** — 109 章 / 1 頁（`rules-of-management`）
- **The Rules of People** — 104 章 / 1 頁（`rules-of-people`）

### `tools-note`（2 本）

- **Flow 心流** — 64 章 / 1 頁（`flow-psychology-of-happiness`）
- **Indistractable 專注力協定** — 44 章 / 1 頁（`indistractable`）

### `data-systems-note`（2 本）

- **Versioning in an Event Sourced System** — 56 章 / 1 頁（`versioning-in-an-event-sourced-system`）
- **SQL Performance Explained** — 42 章 / 1 頁（`sql-performance-explained`）

### `design-patterns-note`（2 本）

- **Refactoring to Patterns** — 41 章 / 1 頁（`refactoring-to-patterns`）
- **Refactoring for Software Design Smells** — 38 章 / 0 頁（`refactoring-for-software-design-smells`）

### `history-note`（2 本）

- **文學的40堂公開課** — 40 章 / 1 頁（`little-history-of-literature`）
- **餐桌儀式** — 34 章 / 1 頁（`rituals-of-dinner`）

### `system-design-note`（2 本）

- **The Art of Scalability** — 39 章 / 1 頁（`art-of-scalability`）
- **軟體架構實踐** — 32 章 / 1 頁（`software-architecture-in-practice`）

### `spiritual-formation-note`（2 本）

- **The Cost of Discipleship 追隨基督** — 38 章 / 1 頁（`cost-of-discipleship`）
- **With Christ in the School of Prayer 基督的禱告學校** — 32 章 / 1 頁（`with-christ-in-the-school-of-prayer`）

### `lewis-note`（2 本）

- **返璞歸真** — 38 章 / 1 頁（`mere-christianity`）
- **The Screwtape Letters** — 31 章 / 1 頁（`screwtape-letters`）

### `liurun-note`（2 本）

- **關鍵躍升：新任管理者的底層邏輯** — 36 章 / 1 頁（`liurun-key-leap`）
- **商業簡史** — 32 章 / 1 頁（`liurun-evolution-of-business`）

### `leadership-note`（2 本）

- **Leaders Eat Last** — 36 章 / 1 頁（`leaders-eat-last`）
- **Turn the Ship Around!** — 35 章 / 1 頁（`turn-the-ship-around`）

### `communication-note`（2 本）

- **Thank You for Arguing 說理** — 35 章 / 1 頁（`thank-you-for-arguing`）
- **The Speed of Trust 高效信任力** — 30 章 / 1 頁（`speed-of-trust`）

### `keller-note`（1 本）

- **恐懼時代的盼望** — 91 章 / 1 頁（`hope-in-times-of-fear`）

### `newport-note`（1 本）

- **How to Win at College** — 76 章 / 1 頁（`how-to-win-at-college`）

### `stott-note`（1 本）

- **當代講道藝術** — 61 章 / 1 頁（`i-believe-in-preaching`）

### `science-note`（1 本）

- **高手相對論** — 60 章 / 1 頁（`wan-weigang-what-is-relativity`）

### `design-note`（1 本）

- **Refactoring UI** — 59 章 / 1 頁（`refactoring-ui`）

### `growth-note`（1 本）

- **Mastery** — 52 章 / 1 頁（`mastery`）

### `kiyosaki-note`（1 本）

- **富爸爸投資指南** — 49 章 / 1 頁（`rich-dads-guide-to-investing`）

### `life-meaning-note`（1 本）

- **Bigger Leaner Stronger** — 44 章 / 1 頁（`bigger-leaner-stronger`）

### `jung-note`（1 本）

- **紅書** — 40 章 / 1 頁（`jung-red-book-readers-edition`）

### `covey-note`（1 本）

- **Principle-Centered Leadership** — 35 章 / 1 頁（`principle-centered-leadership`）

### `behaviour-interview-note`（1 本）

- **軟技能：soft skills，讓你不過時、不貶值、不消失** — 35 章 / 1 頁（`soft-skills-thirty-letters`）

### `agile-note`（1 本）

- **Extreme Programming Explained** — 33 章 / 1 頁（`extreme-programming-explained`）

### `philosophy-note`（1 本）

- **Philosophy: The Classics 哲學經典的 32 堂公開課** — 32 章 / 1 頁（`philosophy-the-classics`）

### `security-note`（1 本）

- **Practical Malware Analysis** — 30 章 / 1 頁（`practical-malware-analysis`）

## 三、依體裁排除：4 本

這些書章節數必然很高，但體裁上就不該挖成多頁——不排除會永遠霸佔排行前段。清單在 `export-deepen-targets.py` 的 `EXCLUDED_KINDS`；加新的要寫**體裁**理由，「暫時不想挖」屬於選題，不該寫進工具。

- `history-note` — 古拉格群島：文學性紀實巨著
- `lewis-note` — 納尼亞傳奇（七部曲）：小說七部曲
- `liurun-note` — 5分鐘商學院 工具篇：工具條目合輯，每條各自獨立
- `theology-note` — 當代神學辭典：神學辭典，按條目查閱

## 重跑

```bash
notes-core/tools/export-deepen-targets.py
```

補完某本書的第二頁之後重跑，該筆就會從這裡消失。
