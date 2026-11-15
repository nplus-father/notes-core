# 跨站連結缺口（同書同章、卻沒有互相 seeAlso）

> **生成於 2026-11-15T14:58:53+08:00**｜由 `tools/export-seealso-gaps.py` 產生，**不要手改**——改資料源再重跑。

**這份是什麼**：兩個站的概念頁掛了**同一本書的同一章**，來源頁卻沒有任何 `seeAlso` 指到對方那一站。
由 `notes-core/tools/export-seealso-gaps.py` 生成，**不要手改**——補各站的 seeAlso 再重跑。

**為什麼要補**：契約層全綠之後，星系最薄的是站與站之間。同一章同時撐著主題站的一頁與人物站的一頁，
讀者在任一邊都看不到另一邊——79 個站各自封閉，首頁 schools 卡的跨站門是唯一通道。
頁級的「Dive Deeper」就是為這件事存在的，它的使用率卻只有一成。

**判準只收 strong**：同書**同章**。同書不同章只列數字（weak），不開單——不同章可能講完全不同的事。

目前：2233 個概念頁，有 seeAlso 的 **229 頁（10%）**；一條跨站連結都沒有的站 **40**。
strong 缺口 **448 筆**（來源頁 384，分佈在 61 站）；全部補上後有 seeAlso 的頁變成 **595（27%）**。weak（同書不同章）另有 421 筆，只供參考。
另有 **19 筆被 schema 擋住**（strict 站指向非技術站，見下節）。

> [!NOTE]
> 目前零跨站連結的站：`behaviour-interview`、`business-strategy`、`career`、`christensen`、`communication`、`design`、`drucker`、`economics`、`gardner`、`greene`、`growth`、`habits`、`hbr`、`history`、`hr`、`image-style`、`jung`、`keller`、`kent-beck`、`kiyosaki`、`leadership`、`learning`、`life-meaning`、`management`、`marketing`、`pastoral-psychology`、`personal-finance`、`philosophy`、`problem-solving`、`relationships`、`science`、`security`、`spiritual-formation`、`startup`、`theology`、`thinking`、`tools`、`travel`、`wan-weigang`、`wujun`

## 各站缺口（當來源）

缺越多排越前；缺 0 的站略去。軸別來自 sites.ts。

| 站 | 軸 | 缺口 | 主要去向 |
| --- | --- | ---: | --- |
| `leadership` | topic | 28 | management 6、collins 6、hr 3、maxwell 2 |
| `career` | topic | 27 | growth 7、newport 4、hr 3、tools 2 |
| `management` | topic | 24 | drucker 6、business-strategy 5、leadership 4、grove 2 |
| `business-strategy` | topic | 19 | management 5、drucker 5、collins 3、leadership 3 |
| `growth` | topic | 19 | grant 6、learning 5、career 4、greene 1 |
| `covey` | person | 16 | tools 5、communication 5、habits 4、leadership 2 |
| `drucker` | person | 16 | management 8、business-strategy 5、career 1、startup 1 |
| `thinking` | topic | 16 | science 8、jung 5、economics 1、navarro 1 |
| `tools` | topic | 16 | habits 5、newport 3、career 2、covey 2 |
| `collins` | person | 14 | leadership 9、business-strategy 3、management 2 |
| `habits` | topic | 12 | tools 8、writing 1、spiritual-formation 1、covey 1 |
| `learning` | topic | 11 | growth 4、career 4、wan-weigang 2、problem-solving 1 |
| `science` | topic | 11 | thinking 6、liurun 1、history 1、growth 1 |
| `communication` | topic | 10 | writing 5、career 1、grant 1、data-science 1 |
| `de-botton` | person | 9 | philosophy 5、design 2、travel 1、relationships 1 |
| `theology` | topic | 9 | lewis 2、stott 2、keller 1、nt-wright 1 |
| `writing` | topic | 9 | communication 7、habits 1、marketing 1 |
| `grove` | person | 8 | leadership 4、management 3、business-strategy 1 |
| `hr` | topic | 8 | leadership 4、career 3、management 1 |
| `life-meaning` | topic | 8 | wellness 3、maxwell 2、grant 2、christensen 1 |
| `philosophy` | topic | 8 | de-botton 3、fromm 3、science 1、growth 1 |
| `spiritual-formation` | topic | 8 | nouwen 3、lewis 3、theology 1、habits 1 |
| `investing` | topic | 7 | economics 3、bogle 2、history 1、schwager 1 |
| `jung` | person | 7 | thinking 7 |
| `startup` | topic | 7 | management 2、career 1、hbr 1、business-strategy 1 |
| `system-design` | topic | 7 | data-systems 5、cloud-infra 2 |
| `economics` | topic | 6 | investing 3、history 2、thinking 1 |
| `hbr` | topic | 6 | leadership 1、career 1、wellness 1、tools 1 |
| `relationships` | topic | 6 | cloud 2、tracy 1、peck 1、nouwen 1 |
| `biblical-studies` | topic | 5 | nt-wright 3、keller 2 |
| `data-systems` | topic | 5 | system-design 5 |
| `grant` | person | 5 | life-meaning 3、career 1、growth 1 |
| `newport` | person | 5 | tools 3、career 1、growth 1 |
| `nouwen` | person | 5 | spiritual-formation 3、theology 1、relationships 1 |
| `problem-solving` | topic | 5 | business-strategy 2、leadership 1、learning 1、tools 1 |
| `travel` | topic | 5 | de-botton 1、tools 1、startup 1、leadership 1 |
| `cloud` | person | 4 | relationships 3、leadership 1 |
| `history` | topic | 4 | science 2、investing 1、economics 1 |
| `lewis` | person | 4 | theology 2、spiritual-formation 2 |
| `uncle-bob` | person | 4 | clean-code 3、agile 1 |
| `wellness` | topic | 4 | life-meaning 3、hbr 1 |
| `willard` | person | 4 | theology 4 |
| `agile` | topic | 3 | uncle-bob 2、kent-beck 1 |
| `christensen` | person | 3 | leadership 2、life-meaning 1 |
| `design` | topic | 3 | de-botton 3 |
| `keller` | person | 3 | biblical-studies 2、theology 1 |
| `kent-beck` | person | 3 | agile 2、clean-code 1 |
| `peck` | person | 3 | relationships 3 |
| `fromm` | person | 2 | philosophy 2 |
| `greene` | person | 2 | growth 2 |
| `marketing` | topic | 2 | writing 1、travel 1 |
| `maxwell` | person | 2 | life-meaning 2 |
| `navarro` | person | 2 | thinking 2 |
| `stott` | person | 2 | theology 2 |
| `bogle` | person | 1 | investing 1 |
| `cloud-infra` | topic | 1 | system-design 1 |
| `damodaran` | person | 1 | investing 1 |
| `liurun` | person | 1 | science 1 |
| `nt-wright` | person | 1 | theology 1 |
| `tracy` | person | 1 | relationships 1 |
| `wan-weigang` | person | 1 | learning 1 |

軸向：主題→人物 111、人物→主題 129、主題→主題 208、人物→人物 0。

## 逐筆清單

格式：來源頁 → 目標站：要掛的 path（label）。分類頁＝該分類 ≥3 頁同時命中，連分類不連單頁。

### agile（3 筆）

- `foundations/reasonable-expectations`「合理期望：主管有權要求的那十二件事」 → **uncle-bob**：`concepts/professionalism/agile-values/`（敏捷的初衷：回到四個價值觀）
- `xp-practices/test-driven-development`「TDD：軟體的複式簿記」 → **uncle-bob**：`concepts/professionalism/agile-values/`（敏捷的初衷：回到四個價值觀）
- `xp-practices/xp-values-principles-practices`「Beck 的推導：四個變數、變更成本與價值—原則—實踐」 → **kent-beck**：`concepts/xp/four-variables/`（四個變數：成本、時間、品質、範圍）；`concepts/xp/cost-of-change/`（變更成本曲線可以被壓平）

### biblical-studies（5 筆）

- `new-testament/gospels-in-cultural-context`「福音書的文化與歷史處境」 → **nt-wright**：`concepts/coqg/new-testament-in-its-world/`（新約導論：把工具交到讀者手上）
- `new-testament/jesus-and-the-victory-of-god`「歷史耶穌與神的得勝」 → **nt-wright**：`concepts/coqg/jesus-and-the-victory-of-god/`（耶穌與神的得勝：歷史中的彌賽亞）
- `new-testament/resurrection-as-history`「復活：歷史論證與盼望」 → **nt-wright**：`concepts/coqg/resurrection-of-the-son-of-god/`（神兒子的復活：復活作為歷史事件）
- `scripture-and-life/gospel-and-work`「工作的福音：從創造使命到職場呼召」 → **keller**：`concepts/life/every-good-endeavor/`（工作的意義：福音如何改變你的職場）
- `scripture-and-life/scripture-shaped-prayer`「以聖經塑造禱告：從交談到相遇」 → **keller**：`concepts/church/prayer/`（禱告：敬畏與親密的相遇）

### bogle（1 筆）

- `index-investing/dividends-and-creative-destruction`「股利與創造性破壞：報酬從哪裡來」 → **investing**：`concepts/index-passive/stay-the-course/`（堅持航向：別擇時、別被空頭嚇跑）；`concepts/index-passive/cost-matters-and-the-index/`（成本至關重要：為什麼買下整個市場最聰明）

### business-strategy（19 筆）

- `competitive-strategy/strategic-inflection-point`「策略轉折點：當 10X 力量改變遊戲規則」 → **grove**：`concepts/inflection/strategic-inflection-point/`（策略轉折點）
- `disruption/disruptive-innovation`「破壞式創新：好公司為何做對每件事仍失敗」 → **management**：`concepts/principles/disruptive-innovation/`（破壞式創新的兩難）
- `disruption/sources-of-innovation`「創新的七個來源：創新是一門可練的紀律」 → **drucker**：`concepts/innovation/seven-sources-of-innovation/`（創新的七個來源：有系統地搜尋機會）
- `disruption/sources-of-innovation`「創新的七個來源：創新是一門可練的紀律」 → **management**：`concepts/principles/marketing-and-innovation/`（行銷與創新：企業僅有的兩個功能）
- `disruption/sources-of-innovation`「創新的七個來源：創新是一門可練的紀律」 → **startup**：`concepts/opportunity/drucker-seven-sources/`（創新的七個機會來源（Drucker））
- `execution/hedgehog-concept`「刺蝟原則：三個圓的交集」 → **collins**：`concepts/greatness/hedgehog-concept/`（刺蝟原則：三個圓的交集）
- `execution/hedgehog-concept`「刺蝟原則：三個圓的交集」 → **leadership**：`concepts/vision/level-5-and-hedgehog/`（第五級領導與刺蝟原則：謙遜的意志）；`concepts/vision/bhag-and-core-purpose/`（膽大目標與核心使命：值得追隨的願景架構）
- `execution/level-5-leadership`「第五級領導：先找對人，再決定做什麼」 → **collins**：`concepts/greatness/level-5-leadership/`（第五級領導與窗戶鏡子）
- `execution/level-5-leadership`「第五級領導：先找對人，再決定做什麼」 → **leadership**：`concepts/vision/level-5-and-hedgehog/`（第五級領導與刺蝟原則：謙遜的意志）
- `execution/mece-problem-solving`「MECE 與假說導向：麥肯錫的問題解決法」 → **problem-solving**：`concepts/logic-structure/mece-and-logic-tree/`（MECE 與邏輯樹：把問題拆乾淨）；`concepts/logic-structure/three-problem-types/`（三型問題：恢復原狀、防杜潛在、追求理想）
- `execution/the-flywheel`「飛輪效應：偉大來自持續累積，而非單一奇蹟」 → **collins**：`concepts/greatness/level-5-leadership/`（第五級領導與窗戶鏡子）；`concepts/greatness/flywheel/`（飛輪與命運環路）
- `execution/the-flywheel`「飛輪效應：偉大來自持續累積，而非單一奇蹟」 → **leadership**：`concepts/vision/level-5-and-hedgehog/`（第五級領導與刺蝟原則：謙遜的意志）
- `management/knowledge-worker`「知識工作者：讓知識的生產力成為管理核心」 → **drucker**：`concepts/society/age-of-discontinuity/`（不連續的時代：看見尚未被察覺的斷裂）
- `management/knowledge-worker`「知識工作者：讓知識的生產力成為管理核心」 → **management**：`concepts/principles/knowledge-worker/`（知識工作者與知識社會）
- `management/management-by-objectives`「目標管理（MBO）：用目標與自我控制取代支配」 → **drucker**：`concepts/management/management-by-objectives/`（目標管理與自我控制：讓每個人的努力指向共同成果）
- `management/management-by-objectives`「目標管理（MBO）：用目標與自我控制取代支配」 → **management**：`concepts/principles/purpose-of-business/`（企業的目的是創造顧客）
- `management/results-are-outside`「成果在企業之外：內部只有成本」 → **drucker**：`concepts/management/managing-for-results/`（把資源集中在成果與機會）
- `management/the-effective-executive`「有效的經營者：效能是可以學的五個習慣」 → **drucker**：`concepts/executive/effectiveness-can-be-learned/`（效能是可以學的習慣：卓有成效的管理者不是天生的）
- `management/the-effective-executive`「有效的經營者：效能是可以學的五個習慣」 → **management**：`concepts/org-people/staff-on-strengths/`（用人之長）

### career（27 筆）

- `career-capital/career-as-startup`「把自己當新創經營：ABZ 計畫」 → **startup**：`concepts/founder/permanent-beta/`（永遠處於 Beta：像新創一樣經營自己）
- `career-capital/career-capital-theory`「職涯資本理論：技能先於熱情」 → **growth**：`concepts/talent-grit/passion-follows-mastery/`（職涯資本：別追隨熱情，先變得夠好）
- `career-capital/career-capital-theory`「職涯資本理論：技能先於熱情」 → **newport**：`concepts/career-capital/career-capital-over-passion/`（職涯資本勝過熱情：技能先於使命）
- `career-capital/craftsman-mindset`「工匠心態：別問世界能給你什麼」 → **growth**：`concepts/talent-grit/passion-follows-mastery/`（職涯資本：別追隨熱情，先變得夠好）
- `career-capital/craftsman-mindset`「工匠心態：別問世界能給你什麼」 → **newport**：`concepts/career-capital/career-capital-over-passion/`（職涯資本勝過熱情：技能先於使命）
- `career-capital/deliberate-practice-at-work`「把刻意練習搬進工作」 → **growth**：`concepts/talent-grit/passion-follows-mastery/`（職涯資本：別追隨熱情，先變得夠好）
- `career-capital/deliberate-practice-at-work`「把刻意練習搬進工作」 → **newport**：`concepts/career-capital/career-capital-over-passion/`（職涯資本勝過熱情：技能先於使命）
- `career-capital/mission-through-little-bets`「使命：先累積資本，再用小賭注長出來」 → **newport**：`concepts/career-capital/control-and-mission/`（自主與使命：資本的兩種兌換）
- `grit-mastery/atomic-habits-identity`「原子習慣：身分認同驅動的系統」 → **habits**：`concepts/systems-over-goals/one-percent-compounding/`（系統勝於目標：1% 的複利）
- `grit-mastery/atomic-habits-identity`「原子習慣：身分認同驅動的系統」 → **tools**：`concepts/habits/systems-over-goals-atomic-habits/`（原子習慣：系統勝過目標，身分帶動行為）
- `grit-mastery/deliberate-practice-mastery`「刻意練習與精進」 → **growth**：`concepts/deliberate-practice/role-of-the-teacher/`（好教練的角色：加速學習的目標、回饋與方法）；`concepts/talent-grit/grit-passion-perseverance/`（恆毅力：熱情 × 毅力的長期主義）
- `grit-mastery/effort-counts-twice`「努力算兩次」 → **growth**：`concepts/talent-grit/grit-passion-perseverance/`（恆毅力：熱情 × 毅力的長期主義）
- `grit-mastery/grit-passion-perseverance`「恆毅力：熱情 × 毅力的長期複利」 → **growth**：`concepts/talent-grit/grit-passion-perseverance/`（恆毅力：熱情 × 毅力的長期主義）
- `grit-mastery/outliers-opportunity`「異數：機運結構與累積優勢」 → **growth**：`concepts/talent-grit/ten-thousand-hours/`（異數：一萬小時、機運與時代造就的成功）
- `grit-mastery/ultralearning-projects`「超速學習：自主設計高強度學習專案」 → **learning**：`concepts/self-learning/`（Self-Learning & Feynman）；`concepts/practice/drill-weakest-point/`（鑽研法則：找出限速的那一步，單獨猛攻）
- `job-search-change/alliance`「聯盟世代：僱傭是任期制的互利同盟」 → **hr**：`concepts/culture-people-ops/tours-of-duty/`（任期制：終身雇用之後，雇主與員工怎麼互相承諾）
- `job-search-change/behavioral-interview-storytelling`「行為面試：用故事證明你做過」 → **behaviour-interview**：`concepts/frameworks/piecing-together/`（組裝完整故事 (Piecing It Together)）
- `job-search-change/job-search-system`「求職是系統工程，不是碰運氣」 → **hbr**：`concepts/self-management/career-transitions/`（職涯轉換的設計）
- `manage-yourself/first-year-manager`「初任主管：第一年在學什麼」 → **hr**：`concepts/performance-feedback/four-keys-of-great-managers/`（四把鑰匙：挑天賦、定結果、專注優勢、放對位置）
- `manage-yourself/givers-takers-matchers`「給予者、索取者與互利者」 → **communication**：`concepts/persuasion/givers-take-all/`（給予者的長期優勢）
- `manage-yourself/givers-takers-matchers`「給予者、索取者與互利者」 → **grant**：`concepts/giving/three-reciprocity-styles/`（三種互惠風格）
- `manage-yourself/know-your-strengths`「用回饋分析找出長處」 → **drucker**：`concepts/executive/managing-oneself/`（自我管理：長處、價值與歸屬）
- `manage-yourself/know-your-strengths`「用回饋分析找出長處」 → **management**：`concepts/managers-work/know-thy-time/`（認識你的時間）
- `manage-yourself/managing-oneself`「認識自己：長處、學習方式與貢獻」 → **drucker**：`concepts/executive/managing-oneself/`（自我管理：長處、價值與歸屬）
- `manage-yourself/managing-oneself`「認識自己：長處、學習方式與貢獻」 → **management**：`concepts/managers-work/know-thy-time/`（認識你的時間）
- `manage-yourself/q12-and-four-keys`「Q12 與四把鑰匙：衡量職場強度的量尺」 → **hr**：`concepts/performance-feedback/four-keys-of-great-managers/`（四把鑰匙：挑天賦、定結果、專注優勢、放對位置）；`concepts/performance-feedback/twelve-questions/`（十二道問題：衡量職場強度的量尺，先站穩山腳）
- `manage-yourself/seven-habits-inside-out`「與成功有約：由內而外的效能」 → **tools**：`concepts/habits/seven-habits-effectiveness/`（七個習慣：從依賴到互賴的效能連續體）

### christensen（3 筆）

- `disruption/value-networks`「價值網絡：為什麼資源流不到破壞上」 → **leadership**：`concepts/vision/disruption-dilemma/`（創新的兩難：好管理為什麼會害死好公司）
- `disruption/why-good-management-fails`「好管理為何導致失敗」 → **leadership**：`concepts/vision/disruption-dilemma/`（創新的兩難：好管理為什麼會害死好公司）
- `life-strategy/just-this-once`「「就這一次」的邊際成本陷阱」 → **life-meaning**：`concepts/meaning/marginal-thinking/`（邊際思維的陷阱：just this once）

### cloud（4 筆）

- `boundaries/boundaries`「過猶不及：界線是什麼、為何需要」 → **relationships**：`concepts/boundaries/own-your-life/`（界線：為自己的生命負責）
- `boundaries/boundaries-for-leaders`「領導者的界線：畫出團隊的道德範圍」 → **leadership**：`concepts/team/boundaries-for-leaders/`（領導者的界線：你創造與容忍的一切，就是你得到的團隊）
- `boundaries/boundaries-in-dating`「為約會立界線：戀愛中的自由與責任」 → **relationships**：`concepts/dating/boundaries-in-dating/`（約會前先照顧好自己：約會治不好寂寞）
- `boundaries/ten-laws-of-boundaries`「界線十律：按現實生活的法則」 → **relationships**：`concepts/boundaries/own-your-life/`（界線：為自己的生命負責）

### cloud-infra（1 筆）

- `observability/observability-vs-monitoring`「可觀測性 vs 監控（Observability vs Monitoring）」 → **system-design**：`concepts/observability/golden-signals/`（四個黃金指標 (Golden Signals)）

### collins（14 筆）

- `discipline/fire-bullets-then-cannonballs`「先射子彈，再射砲彈」 → **leadership**：`concepts/vision/twenty-mile-march/`（十倍勝：不確定中的二十哩行軍）
- `discipline/return-on-luck`「運氣報酬率」 → **leadership**：`concepts/vision/twenty-mile-march/`（十倍勝：不確定中的二十哩行軍）
- `discipline/twenty-mile-march`「二十哩行軍」 → **leadership**：`concepts/vision/twenty-mile-march/`（十倍勝：不確定中的二十哩行軍）
- `enduring/clock-building-not-time-telling`「造鐘，不是報時」 → **leadership**：`concepts/vision/clock-building/`（造鐘，而非報時：讓公司自己會走的組織設計）
- `enduring/clock-building-not-time-telling`「造鐘，不是報時」 → **management**：`concepts/org-people/first-who-then-what/`（先找對人，再決定做什麼）
- `enduring/preserve-core-stimulate-progress`「保存核心，刺激進步」 → **leadership**：`concepts/vision/clock-building/`（造鐘，而非報時：讓公司自己會走的組織設計）
- `greatness/confront-the-brutal-facts`「面對殘酷的現實（史托克戴爾弔詭）」 → **leadership**：`concepts/vision/confront-brutal-facts/`（直面殘酷事實，卻永不失去信念：史托克戴爾悖論）
- `greatness/first-who-then-what`「先找對人，再決定要做什麼」 → **leadership**：`concepts/vision/first-who-then-what/`（先人後事：先把對的人請上車，再決定車開去哪）
- `greatness/first-who-then-what`「先找對人，再決定要做什麼」 → **management**：`concepts/org-people/first-who-then-what/`（先找對人，再決定做什麼）
- `greatness/flywheel`「飛輪與命運環路」 → **business-strategy**：`concepts/execution/the-flywheel/`（飛輪效應：偉大來自持續累積，而非單一奇蹟）
- `greatness/flywheel`「飛輪與命運環路」 → **leadership**：`concepts/vision/level-5-and-hedgehog/`（第五級領導與刺蝟原則：謙遜的意志）
- `greatness/hedgehog-concept`「刺蝟原則：三個圓的交集」 → **business-strategy**：`concepts/execution/hedgehog-concept/`（刺蝟原則：三個圓的交集）
- `greatness/hedgehog-concept`「刺蝟原則：三個圓的交集」 → **leadership**：`concepts/vision/level-5-and-hedgehog/`（第五級領導與刺蝟原則：謙遜的意志）；`concepts/vision/bhag-and-core-purpose/`（膽大目標與核心使命：值得追隨的願景架構）
- `greatness/level-5-leadership`「第五級領導與窗戶鏡子」 → **business-strategy**：`concepts/execution/level-5-leadership/`（第五級領導：先找對人，再決定做什麼）；`concepts/execution/the-flywheel/`（飛輪效應：偉大來自持續累積，而非單一奇蹟）

### communication（10 筆）

- `persuasion/givers-take-all`「給予者的長期優勢」 → **career**：`concepts/manage-yourself/givers-takers-matchers/`（給予者、索取者與互利者）
- `persuasion/givers-take-all`「給予者的長期優勢」 → **grant**：`concepts/giving/three-reciprocity-styles/`（三種互惠風格）
- `presentation/data-storytelling`「用資料說故事：從圖表到敘事」 → **data-science**：`concepts/visualization-storytelling/context-before-charts/`（先有脈絡再畫圖：解釋型分析的 Who／What／How）
- `presentation/smart-brevity`「精簡寫作：二十六秒裡的四個動作」 → **writing**：`concepts/nonfiction-copy/find-the-core/`（找到核心訊息 (Find the Core)）
- `social/speed-of-trust`「信任的速度：最被低估的經濟變數」 → **covey**：`concepts/trust-and-execution/`（Trust & Execution）；`concepts/public-victory/emotional-bank-account/`（情感帳戶：六種存款）
- `storytelling/brain-on-story`「大腦如何被故事點燃：敘事的心理機制」 → **writing**：`concepts/story-structure/desire-and-conflict/`（欲望與衝突 (Desire & Conflict)）；`concepts/story-structure/storytelling-brain/`（說故事的大腦：預測、缺陷與戲劇問題 (The Storytelling Brain)）
- `storytelling/curiosity-gap`「好奇心缺口：先製造未知」 → **writing**：`concepts/nonfiction-copy/`（非虛構與文案）
- `storytelling/four-business-stories`「黏住人的四種商業故事」 → **behaviour-interview**：`concepts/delivery/story-typology/`（故事類型學：四種必備故事）
- `storytelling/heros-journey`「千面英雄：單一神話的敘事骨架」 → **writing**：`concepts/story-structure/monomyth/`（單一神話：離別・啟蒙・回歸 (The Monomyth)）
- `storytelling/made-to-stick-success`「黏性六原則：為什麼有些觀念記得住」 → **writing**：`concepts/nonfiction-copy/`（非虛構與文案）

### covey（16 筆）

- `personal-victory/integrity-in-the-moment`「抉擇時刻的正直：大石頭、焦點圈、問聽行」 → **habits**：`concepts/productivity/big-rocks-first/`（要事第一：先放大石頭）
- `personal-victory/integrity-in-the-moment`「抉擇時刻的正直：大石頭、焦點圈、問聽行」 → **tools**：`concepts/time-management/clock-and-compass-quadrant-two/`（鐘與羅盤：第二象限的要事規劃）
- `personal-victory/quadrant-two`「第二象限：重要但不緊急」 → **habits**：`concepts/productivity/big-rocks-first/`（要事第一：先放大石頭）
- `personal-victory/quadrant-two`「第二象限：重要但不緊急」 → **tools**：`concepts/time-management/clock-and-compass-quadrant-two/`（鐘與羅盤：第二象限的要事規劃）
- `personal-victory/urgency-addiction`「時鐘與羅盤：緊急成癮」 → **habits**：`concepts/productivity/big-rocks-first/`（要事第一：先放大石頭）
- `personal-victory/urgency-addiction`「時鐘與羅盤：緊急成癮」 → **tools**：`concepts/time-management/clock-and-compass-quadrant-two/`（鐘與羅盤：第二象限的要事規劃）
- `principles/character-over-personality`「品格倫理與個性倫理」 → **leadership**：`concepts/mindset/inside-out-leadership/`（由內而外：品格先於技巧的領導修練）
- `principles/habit-anatomy-and-maturity-continuum`「習慣的解剖與成熟連續體」 → **leadership**：`concepts/mindset/inside-out-leadership/`（由內而外：品格先於技巧的領導修練）
- `principles/live-love-learn-leave-a-legacy`「生活、愛、學習、留下傳承：四項基本需要」 → **habits**：`concepts/productivity/big-rocks-first/`（要事第一：先放大石頭）
- `principles/live-love-learn-leave-a-legacy`「生活、愛、學習、留下傳承：四項基本需要」 → **tools**：`concepts/time-management/clock-and-compass-quadrant-two/`（鐘與羅盤：第二象限的要事規劃）
- `public-victory/emotional-bank-account`「情感帳戶：六種存款」 → **communication**：`concepts/social/speed-of-trust/`（信任的速度：最被低估的經濟變數）
- `public-victory/emotional-bank-account`「情感帳戶：六種存款」 → **tools**：`concepts/habits/seven-habits-effectiveness/`（七個習慣：從依賴到互賴的效能連續體）
- `trust-and-execution/thirteen-behaviors-both`「十三個行為（下）：品格與才能各半的三個」 → **communication**：`concepts/social/speed-of-trust/`（信任的速度：最被低估的經濟變數）
- `trust-and-execution/thirteen-behaviors-character`「十三個行為（上）：品格型的五個」 → **communication**：`concepts/social/speed-of-trust/`（信任的速度：最被低估的經濟變數）
- `trust-and-execution/thirteen-behaviors-competence`「十三個行為（中）：才能型的五個」 → **communication**：`concepts/social/speed-of-trust/`（信任的速度：最被低估的經濟變數）
- `trust-and-execution/trust-economics`「信任的經濟學：稅、紅利與五道漣漪」 → **communication**：`concepts/social/speed-of-trust/`（信任的速度：最被低估的經濟變數）

### damodaran（1 筆）

- `valuation/choosing-an-approach`「為什麼有三種取徑，以及何時該換」 → **investing**：`concepts/value-investing/valuation-approaches-and-bias/`（評價的百慕達三角與三種取徑）

### data-systems（5 筆）

- `indexing/clustered-vs-secondary`「聚簇索引 vs 次級索引 (Clustered vs Secondary)」 → **system-design**：`concepts/caching/caching-strategies/`（快取策略 (Caching Strategies)）
- `indexing/covering-and-composite-indexes`「覆蓋索引與多欄索引 (Covering & Composite Indexes)」 → **system-design**：`concepts/caching/caching-strategies/`（快取策略 (Caching Strategies)）
- `storage-engines/b-tree-internals`「B-Tree 內部機制 (B-Tree Internals)」 → **system-design**：`concepts/caching/caching-strategies/`（快取策略 (Caching Strategies)）
- `storage-engines/column-oriented-storage`「欄式儲存與 OLAP (Column-Oriented Storage)」 → **system-design**：`concepts/caching/caching-strategies/`（快取策略 (Caching Strategies)）
- `storage-engines/compaction-strategies`「LSM 壓縮策略 (Compaction Strategies)」 → **system-design**：`concepts/caching/caching-strategies/`（快取策略 (Caching Strategies)）

### de-botton（9 筆）

- `beauty/architecture-of-happiness`「幸福建築：建築如何形塑我們」 → **design**：`concepts/built-environment/architecture-shapes-us/`（建築作為身分的守護者）；`concepts/built-environment/in-what-style/`（該用什麼風格蓋？從古典共識到居住的機器）
- `beauty/art-of-travel`「旅行的藝術：我不小心把自己一起帶去了」 → **travel**：`concepts/destinations/learning-to-see-a-place/`（學會看一個地方：期待、藝術與素描的眼光）
- `beauty/what-is-beauty`「美的判準：秩序、平衡與自我認識」 → **design**：`concepts/built-environment/virtues-of-buildings/`（建築的五種美德：秩序、平衡、優雅、連貫、自我認識）
- `love/love-as-institution`「愛的進化論：從激情到經營」 → **relationships**：`concepts/marriage/love-as-craft/`（浪漫主義的陷阱：婚姻從幻滅之後才開始）
- `philosophy/consolations-of-philosophy`「哲學的慰藉：六位哲人面對人生困境」 → **philosophy**：`concepts/applied/philosophy-as-consolation/`（哲學作為慰藉：六帖給日常煩惱的解藥）
- `philosophy/epicurus-on-money`「伊壁鳩魯論缺錢：友誼、自由與思想」 → **philosophy**：`concepts/applied/philosophy-as-consolation/`（哲學作為慰藉：六帖給日常煩惱的解藥）
- `philosophy/religion-for-atheists`「無神論者的宗教：世俗如何借用信仰的智慧」 → **philosophy**：`concepts/applied/religion-for-atheists/`（取其功能、去其信仰：無神論者的宗教用途）
- `status/solutions-to-status`「五種解方：哲學、藝術、政治、宗教、波希米亞」 → **philosophy**：`concepts/applied/status-anxiety/`（地位焦慮：為什麼我們怕被人看輕）
- `status/status-anxiety`「身分的焦慮：我們為何在意地位」 → **philosophy**：`concepts/applied/status-anxiety/`（地位焦慮：為什麼我們怕被人看輕）

### design（3 筆）

- `built-environment/architecture-shapes-us`「建築作為身分的守護者」 → **de-botton**：`concepts/beauty/architecture-of-happiness/`（幸福建築：建築如何形塑我們）
- `built-environment/in-what-style`「該用什麼風格蓋？從古典共識到居住的機器」 → **de-botton**：`concepts/beauty/architecture-of-happiness/`（幸福建築：建築如何形塑我們）
- `built-environment/virtues-of-buildings`「建築的五種美德：秩序、平衡、優雅、連貫、自我認識」 → **de-botton**：`concepts/beauty/what-is-beauty/`（美的判準：秩序、平衡與自我認識）

### drucker（16 筆）

- `executive/effectiveness-can-be-learned`「效能是可以學的習慣：卓有成效的管理者不是天生的」 → **business-strategy**：`concepts/management/the-effective-executive/`（有效的經營者：效能是可以學的五個習慣）
- `executive/effectiveness-can-be-learned`「效能是可以學的習慣：卓有成效的管理者不是天生的」 → **management**：`concepts/org-people/staff-on-strengths/`（用人之長）；`concepts/managers-work/know-thy-time/`（認識你的時間）
- `executive/managing-oneself`「自我管理：長處、價值與歸屬」 → **career**：`concepts/manage-yourself/managing-oneself/`（認識自己：長處、學習方式與貢獻）；`concepts/manage-yourself/know-your-strengths/`（用回饋分析找出長處）
- `executive/managing-oneself`「自我管理：長處、價值與歸屬」 → **management**：`concepts/managers-work/know-thy-time/`（認識你的時間）
- `executive/managing-your-time`「先管理你的時間：認識時間，才能認識工作」 → **management**：`concepts/org-people/staff-on-strengths/`（用人之長）；`concepts/managers-work/know-thy-time/`（認識你的時間）
- `innovation/seven-sources-of-innovation`「創新的七個來源：有系統地搜尋機會」 → **business-strategy**：`concepts/disruption/sources-of-innovation/`（創新的七個來源：創新是一門可練的紀律）
- `innovation/seven-sources-of-innovation`「創新的七個來源：有系統地搜尋機會」 → **management**：`concepts/principles/marketing-and-innovation/`（行銷與創新：企業僅有的兩個功能）
- `innovation/seven-sources-of-innovation`「創新的七個來源：有系統地搜尋機會」 → **startup**：`concepts/opportunity/drucker-seven-sources/`（創新的七個機會來源（Drucker））
- `management/five-questions`「杜拉克的五個關鍵問題」 → **leadership**：`concepts/vision/drucker-five-questions/`（杜拉克的五個最重要問題：逼出使命與方向的自我評量）
- `management/management-by-objectives`「目標管理與自我控制：讓每個人的努力指向共同成果」 → **business-strategy**：`concepts/management/management-by-objectives/`（目標管理（MBO）：用目標與自我控制取代支配）
- `management/management-by-objectives`「目標管理與自我控制：讓每個人的努力指向共同成果」 → **management**：`concepts/principles/purpose-of-business/`（企業的目的是創造顧客）
- `management/managing-for-results`「把資源集中在成果與機會」 → **business-strategy**：`concepts/management/results-are-outside/`（成果在企業之外：內部只有成本）
- `management/what-is-a-business`「企業是什麼：創造顧客」 → **management**：`concepts/principles/marketing-and-innovation/`（行銷與創新：企業僅有的兩個功能）
- `society/age-of-discontinuity`「不連續的時代：看見尚未被察覺的斷裂」 → **business-strategy**：`concepts/management/knowledge-worker/`（知識工作者：讓知識的生產力成為管理核心）
- `society/age-of-discontinuity`「不連續的時代：看見尚未被察覺的斷裂」 → **management**：`concepts/principles/knowledge-worker/`（知識工作者與知識社會）
- `society/corporation-as-social-institution`「企業作為社會制度：通用汽車的十八個月」 → **management**：`concepts/org-people/centralization-and-decentralization/`（集權與分權：公司的概念）

### economics（6 筆）

- `behavioral-narrative/anchoring-relativity`「定錨與相對性：偏好是被製造出來的」 → **thinking**：`concepts/judgment-bias/predictable-irrationality/`（可預測的非理性：行為經濟學的實驗場）
- `financial-history/anatomy-of-bubbles`「泡沫的解剖：狂熱、恐慌與崩盤的循環」 → **investing**：`concepts/market-history/anatomy-of-a-bubble/`（泡沫的解剖：反饋循環與非理性繁榮）；`concepts/market-history/this-time-is-different/`（「這次不一樣」的陷阱：史上最貴的四個字）
- `financial-history/minsky-credit-cycle`「明斯基時刻：信用如何自我毀滅」 → **investing**：`concepts/market-history/anatomy-of-a-bubble/`（泡沫的解剖：反饋循環與非理性繁榮）；`concepts/market-history/this-time-is-different/`（「這次不一樣」的陷阱：史上最貴的四個字）
- `financial-history/speculation-through-ages`「投機四百年：一再重演的歷史」 → **investing**：`concepts/market-history/madness-of-crowds/`（群眾的瘋狂：鬱金香、南海與密西西比）
- `globalization-order/debt-cycle-world-order`「債務大週期與世界秩序更替」 → **history**：`concepts/rise-and-fall/empire-cycle/`（帝國大週期：儲備貨幣的興衰）
- `globalization-order/reserve-currency-cycle`「儲備貨幣的興衰：過度特權與它的代價」 → **history**：`concepts/rise-and-fall/empire-cycle/`（帝國大週期：儲備貨幣的興衰）

### fromm（2 筆）

- `love-being/art-of-loving`「愛的藝術：愛是需要學習與修練的能力」 → **philosophy**：`concepts/ethics-justice/productive-love/`（愛是一種能力，不是運氣：Fromm 的愛之藝術）
- `love-being/to-have-or-to-be`「擁有還是存在：兩種生存模式」 → **philosophy**：`concepts/ethics-justice/having-vs-being/`（占有還是存在：兩種活法，兩種自我）

### grant（5 筆）

- `giving/three-reciprocity-styles`「三種互惠風格」 → **career**：`concepts/manage-yourself/givers-takers-matchers/`（給予者、索取者與互利者）
- `potential/deliberate-play`「刻意玩樂：把磨練變好玩」 → **growth**：`concepts/originals-potential/character-skills-over-talent/`（品格技能勝過天賦：決定你走多遠的那組能力）；`concepts/originals-potential/hidden-potential/`（隱性潛能：起點不決定終點）
- `resilience/platinum-rule`「友誼的白金法則」 → **life-meaning**：`concepts/resilience/three-ps-of-resilience/`（復原的三個 P：擋住讓你陷更深的三個念頭）
- `resilience/post-traumatic-growth`「創傷後成長：向前彈起」 → **life-meaning**：`concepts/resilience/post-traumatic-growth/`（創傷後成長：不是復原，是向前反彈）
- `resilience/three-ps`「三個 P：擋住復原的思維陷阱」 → **life-meaning**：`concepts/resilience/three-ps-of-resilience/`（復原的三個 P：擋住讓你陷更深的三個念頭）

### greene（2 筆）

- `mastery/apprenticeship`「學徒期：觀察、習得、實驗」 → **growth**：`concepts/deliberate-practice/path-to-mastery/`（精通之路：天命、學徒期與導師）
- `mastery/mastery`「喚醒你心中的大師：邁向精通之路」 → **growth**：`concepts/deliberate-practice/path-to-mastery/`（精通之路：天命、學徒期與導師）

### grove（8 筆）

- `inflection/strategic-inflection-point`「策略轉折點」 → **business-strategy**：`concepts/competitive-strategy/strategic-inflection-point/`（策略轉折點：當 10X 力量改變遊戲規則）
- `output/managerial-leverage`「管理槓桿與產出方程式」 → **leadership**：`concepts/team/managerial-leverage/`（管理槓桿率：管理者的產出＝組織的產出）
- `output/mbo-and-okr`「目標管理：從 MBO 到 OKR」 → **leadership**：`concepts/vision/okr/`（OKR：聚焦、對齊、追蹤與挑戰極限）
- `output/meetings-as-medium`「會議是管理工作的媒介」 → **leadership**：`concepts/team/managerial-leverage/`（管理槓桿率：管理者的產出＝組織的產出）
- `output/meetings-as-medium`「會議是管理工作的媒介」 → **management**：`concepts/managers-work/one-on-one/`（一對一會議）
- `people/performance-appraisal`「績效考核：最難的那場對話」 → **management**：`concepts/goals-performance/performance-review/`（績效評估與回饋）
- `people/right-to-be-managed`「你有被好好管理的權利」 → **management**：`concepts/managers-work/one-on-one/`（一對一會議）
- `people/task-relevant-maturity`「任務相關成熟度（TRM）」 → **leadership**：`concepts/team/managerial-leverage/`（管理槓桿率：管理者的產出＝組織的產出）

### growth（19 筆）

- `deliberate-practice/get-out-of-comfort-zone`「走出舒適區：身體與大腦如何被「逼」出改變」 → **learning**：`concepts/practice/deliberate-practice-basics/`（刻意練習入門：不是苦練，是有方法的練）
- `deliberate-practice/path-to-mastery`「精通之路：天命、學徒期與導師」 → **greene**：`concepts/mastery/mastery/`（喚醒你心中的大師：邁向精通之路）；`concepts/mastery/apprenticeship/`（學徒期：觀察、習得、實驗）
- `deliberate-practice/purposeful-practice`「刻意練習：不是練久，而是練對」 → **learning**：`concepts/practice/deliberate-practice-basics/`（刻意練習入門：不是苦練，是有方法的練）
- `deliberate-practice/role-of-the-teacher`「好教練的角色：加速學習的目標、回饋與方法」 → **career**：`concepts/grit-mastery/deliberate-practice-mastery/`（刻意練習與精進）
- `learning-resilience/make-it-stick`「有效學習：提取練習勝過反覆重讀」 → **learning**：`concepts/memory/stop-highlighting/`（別再邊讀邊畫線：重讀與畫線為何最沒用）；`concepts/metacognition/illusion-of-competence/`（能力的錯覺：為什麼我們高估自己懂多少）
- `learning-resilience/retrieval-practice`「提取練習：測試效應與對抗「我懂了」的錯覺」 → **learning**：`concepts/memory/stop-highlighting/`（別再邊讀邊畫線：重讀與畫線為何最沒用）；`concepts/metacognition/illusion-of-competence/`（能力的錯覺：為什麼我們高估自己懂多少）
- `learning-resilience/spaced-interleaved-practice`「間隔與交錯練習：為什麼「更難的練法」記得更牢」 → **learning**：`concepts/practice/not-just-repetition/`（練習 ≠ 重複）
- `originals-potential/character-skills-over-talent`「品格技能勝過天賦：決定你走多遠的那組能力」 → **grant**：`concepts/potential/deliberate-play/`（刻意玩樂：把磨練變好玩）
- `originals-potential/creature-of-discomfort`「當一個不適感的生物：主動尋求不舒服來學習」 → **grant**：`concepts/potential/creatures-of-discomfort/`（成為不適感的生物）
- `originals-potential/hidden-potential`「隱性潛能：起點不決定終點」 → **grant**：`concepts/potential/deliberate-play/`（刻意玩樂：把磨練變好玩）
- `originals-potential/originals`「原創者：如何產生並推動與眾不同的想法」 → **grant**：`concepts/originality/vuja-de-and-defaults/`（vuja de 與預設值）；`concepts/originality/strategic-procrastination/`（策略性拖延）
- `originals-potential/procrastination-as-incubation`「時機與拖延：把拖延當孵化」 → **grant**：`concepts/originality/strategic-procrastination/`（策略性拖延）
- `originals-potential/vuja-de-question-defaults`「質疑預設：用 vuja de 重新看世界」 → **grant**：`concepts/originality/vuja-de-and-defaults/`（vuja de 與預設值）
- `self-awareness/ego-is-the-enemy`「自我是敵人：謙遜是持續精進的前提」 → **philosophy**：`concepts/stoicism/ego-as-obstacle/`（自我是絆腳石：在追求、成功、失敗三階段馴服 ego）
- `self-awareness/observe-your-biases`「潛意識：看不見的心智如何驅動你」 → **science**：`concepts/mind-cognition/metacognition-and-confidence/`（後設認知：知道自己知不知道）
- `talent-grit/grit-passion-perseverance`「恆毅力：熱情 × 毅力的長期主義」 → **career**：`concepts/grit-mastery/`（Grit & Mastery）
- `talent-grit/passion-follows-mastery`「職涯資本：別追隨熱情，先變得夠好」 → **career**：`concepts/career-capital/`（Career Capital）
- `talent-grit/passion-follows-mastery`「職涯資本：別追隨熱情，先變得夠好」 → **newport**：`concepts/career-capital/career-capital-over-passion/`（職涯資本勝過熱情：技能先於使命）
- `talent-grit/ten-thousand-hours`「異數：一萬小時、機運與時代造就的成功」 → **career**：`concepts/grit-mastery/outliers-opportunity/`（異數：機運結構與累積優勢）

### habits（12 筆）

- `discipline/resistance-and-turning-pro`「抵抗力與轉職業：創作紀律的戰爭」 → **writing**：`concepts/craft-mindset/resistance-and-turning-pro/`（抗拒與轉職業 (Resistance & Turning Pro)）
- `discipline/spiritual-disciplines`「靈性操練：通往自由的門」 → **spiritual-formation**：`concepts/discipleship/twelve-spiritual-disciplines/`（十二個屬靈操練：內在、外在與團契）
- `energy-routine/finitude-4000-weeks`「承認有限：四千個禮拜」 → **tools**：`concepts/time-management/finitude-four-thousand-weeks/`（四千個禮拜：接受做不完，才談得上選擇）
- `focus/make-distraction-hard`「讓分心變困難：成為 Indistractable」 → **tools**：`concepts/focus-attention/internal-triggers-indistractable/`（分心的根源在內不在外：專注力協定）
- `habit-loop/behavior-model`「行為 = 動機 × 能力 × 提示（B=MAP）」 → **tools**：`concepts/habits/tiny-habits-behavior-design/`（行為設計：B=MAP 與小到不可能失敗的習慣）
- `habit-loop/cue-craving-response-reward`「習慣迴路：提示 → 渴望 → 回應 → 獎賞」 → **tools**：`concepts/habits/systems-over-goals-atomic-habits/`（原子習慣：系統勝過目標，身分帶動行為）
- `habit-loop/identity-based-habits`「身分認同式習慣：先決定你想成為誰」 → **tools**：`concepts/habits/systems-over-goals-atomic-habits/`（原子習慣：系統勝過目標，身分帶動行為）
- `habit-loop/make-it-tiny`「把習慣縮到極小：微習慣」 → **tools**：`concepts/habits/tiny-habits-behavior-design/`（行為設計：B=MAP 與小到不可能失敗的習慣）
- `productivity/big-rocks-first`「要事第一：先放大石頭」 → **covey**：`concepts/personal-victory/`（Personal Victory）；`concepts/principles/live-love-learn-leave-a-legacy/`（生活、愛、學習、留下傳承：四項基本需要）
- `productivity/big-rocks-first`「要事第一：先放大石頭」 → **tools**：`concepts/time-management/clock-and-compass-quadrant-two/`（鐘與羅盤：第二象限的要事規劃）
- `systems-over-goals/one-percent-compounding`「系統勝於目標：1% 的複利」 → **career**：`concepts/grit-mastery/atomic-habits-identity/`（原子習慣：身分認同驅動的系統）
- `systems-over-goals/one-percent-compounding`「系統勝於目標：1% 的複利」 → **tools**：`concepts/habits/systems-over-goals-atomic-habits/`（原子習慣：系統勝過目標，身分帶動行為）

### hbr（6 筆）

- `leadership-teams/set-up-to-fail`「注定失敗症候群：低績效者是怎麼被做出來的」 → **leadership**：`concepts/coaching/feedback-that-lands/`（有效回饋：對事不對人，即時不等年度）
- `self-management/career-transitions`「職涯轉換的設計」 → **career**：`concepts/job-search-change/job-search-system/`（求職是系統工程，不是碰運氣）
- `self-management/manage-your-energy`「管理精力，而非時間」 → **wellness**：`concepts/stress-mental-health/managing-stress-and-burnout/`（壓力與耗竭：從硬撐到恢復的管理）
- `self-management/managing-oneself`「認識自己的長處與工作方式」 → **tools**：`concepts/time-management/results-over-hours/`（看成果，不看工時）
- `strategy-innovation/buy-a-small-business`「買下一家小公司：另一條創業路」 → **startup**：`concepts/money-exit/buy-dont-build/`（用買的，別從零打造：透過收購創業（ETA））
- `strategy-innovation/manager-data-literacy`「經理人的數據與財務素養」 → **data-science**：`concepts/analytics-decisions/consumer-of-analytics/`（分析的消費者：經理人該問的六個問題）

### history（4 筆）

- `ancient-origins/agricultural-trap`「農業革命：史上最大的騙局？」 → **science**：`concepts/evolution-life/shared-fictions/`（共享的虛構：讓陌生人合作的技術）
- `ancient-origins/cognitive-revolution`「認知革命：虛構故事讓大規模合作成真」 → **science**：`concepts/evolution-life/shared-fictions/`（共享的虛構：讓陌生人合作的技術）
- `historical-thinking/history-of-risk`「風險觀念史：從命運到機率」 → **investing**：`concepts/market-history/invention-of-risk/`（風險的觀念史：從骰子到效率前緣）
- `rise-and-fall/empire-cycle`「帝國大週期：儲備貨幣的興衰」 → **economics**：`concepts/globalization-order/debt-cycle-world-order/`（債務大週期與世界秩序更替）；`concepts/globalization-order/reserve-currency-cycle/`（儲備貨幣的興衰：過度特權與它的代價）

### hr（8 筆）

- `culture-people-ops/talent-density-and-candor`「人才密度與坦誠：Netflix 鬆綁管控的三步循環」 → **leadership**：`concepts/culture/freedom-and-responsibility/`（自由與責任：先密度、再坦誠、最後才拿掉規則）
- `culture-people-ops/talent-density-and-candor`「人才密度與坦誠：Netflix 鬆綁管控的三步循環」 → **management**：`concepts/org-people/first-who-then-what/`（先找對人，再決定做什麼）
- `culture-people-ops/tours-of-duty`「任期制：終身雇用之後，雇主與員工怎麼互相承諾」 → **career**：`concepts/job-search-change/alliance/`（聯盟世代：僱傭是任期制的互利同盟）
- `performance-feedback/four-keys-of-great-managers`「四把鑰匙：挑天賦、定結果、專注優勢、放對位置」 → **career**：`concepts/manage-yourself/q12-and-four-keys/`（Q12 與四把鑰匙：衡量職場強度的量尺）；`concepts/manage-yourself/first-year-manager/`（初任主管：第一年在學什麼）
- `performance-feedback/radical-candor-quadrants`「徹底坦率：個人關懷與直接挑戰的二乘二」 → **leadership**：`concepts/coaching/radical-candor/`（徹底坦率：個人在乎 × 直接挑戰）
- `performance-feedback/twelve-questions`「十二道問題：衡量職場強度的量尺，先站穩山腳」 → **career**：`concepts/manage-yourself/q12-and-four-keys/`（Q12 與四把鑰匙：衡量職場強度的量尺）
- `recruiting/interview-questions-that-work`「問得出東西的面試題：行為題與追問」 → **leadership**：`concepts/team/hiring-and-keeping/`（招對人、留住人：把選才當科學，把留才當日常）
- `retention-motivation/why-people-stay`「留才不從辭呈開始：進展、重要感與留任對話」 → **leadership**：`concepts/team/hiring-and-keeping/`（招對人、留住人：把選才當科學，把留才當日常）

### investing（7 筆）

- `index-passive/cost-matters-and-the-index`「成本至關重要：為什麼買下整個市場最聰明」 → **bogle**：`concepts/index-investing/little-book-of-common-sense-investing/`（指數投資常識：擁有整個市場、成本至上）；`concepts/index-investing/dividends-and-creative-destruction/`（股利與創造性破壞：報酬從哪裡來）
- `index-passive/stay-the-course`「堅持航向：別擇時、別被空頭嚇跑」 → **bogle**：`concepts/index-investing/little-book-of-common-sense-investing/`（指數投資常識：擁有整個市場、成本至上）；`concepts/index-investing/dividends-and-creative-destruction/`（股利與創造性破壞：報酬從哪裡來）
- `market-history/anatomy-of-a-bubble`「泡沫的解剖：反饋循環與非理性繁榮」 → **economics**：`concepts/financial-history/minsky-credit-cycle/`（明斯基時刻：信用如何自我毀滅）；`concepts/financial-history/anatomy-of-bubbles/`（泡沫的解剖：狂熱、恐慌與崩盤的循環）
- `market-history/invention-of-risk`「風險的觀念史：從骰子到效率前緣」 → **history**：`concepts/historical-thinking/history-of-risk/`（風險觀念史：從命運到機率）
- `market-history/madness-of-crowds`「群眾的瘋狂：鬱金香、南海與密西西比」 → **economics**：`concepts/financial-history/speculation-through-ages/`（投機四百年：一再重演的歷史）
- `market-history/this-time-is-different`「「這次不一樣」的陷阱：史上最貴的四個字」 → **economics**：`concepts/financial-history/minsky-credit-cycle/`（明斯基時刻：信用如何自我毀滅）；`concepts/financial-history/anatomy-of-bubbles/`（泡沫的解剖：狂熱、恐慌與崩盤的循環）
- `trading-speculation/risk-first-cut-your-losses`「風險優先：交易高手的第一課是先學會虧損」 → **schwager**：`concepts/wizards/market-wizards/`（金融怪傑：頂尖交易員的共通特質）

### jung（7 筆）

- `dreams/compensation-and-dreams`「補償法則與夢」 → **thinking**：`concepts/depth-psychology/dreams-as-messages/`（夢作為潛意識的訊息）
- `dreams/dream-series`「夢的系列：為什麼單一夢不可靠」 → **thinking**：`concepts/depth-psychology/dreams-as-messages/`（夢作為潛意識的訊息）
- `individuation/process-of-individuation`「個體化的歷程」 → **thinking**：`concepts/depth-psychology/anima-animus/`（阿尼瑪與阿尼姆斯）
- `life/confrontation-with-the-unconscious`「與無意識的對峙」 → **thinking**：`concepts/depth-psychology/individuation-and-the-self/`（個體化：邁向完整的自己）
- `religion/spiritual-problem-of-modern-man`「現代人的精神問題」 → **thinking**：`concepts/self-knowledge/meaning-in-modern-life/`（現代人的意義追尋）
- `unconscious/anima-animus`「阿尼瑪與阿尼姆斯」 → **thinking**：`concepts/depth-psychology/anima-animus/`（阿尼瑪與阿尼姆斯）
- `unconscious/collective-unconscious-and-archetypes`「集體無意識與原型」 → **thinking**：`concepts/depth-psychology/collective-unconscious/`（集體潛意識與原型）

### keller（3 筆）

- `apologetics/making-sense-of-god`「在信仰之前：世俗選項也需要信心」 → **theology**：`concepts/apologetics/faith-in-a-secular-age/`（世俗時代還能信嗎：給懷疑者的邀請）
- `church/prayer`「禱告：敬畏與親密的相遇」 → **biblical-studies**：`concepts/scripture-and-life/scripture-shaped-prayer/`（以聖經塑造禱告：從交談到相遇）
- `life/every-good-endeavor`「工作的意義：福音如何改變你的職場」 → **biblical-studies**：`concepts/scripture-and-life/gospel-and-work/`（工作的福音：從創造使命到職場呼召）

### kent-beck（3 筆）

- `tdd/mastering-tdd`「Mastering TDD：步伐、測試品質與吸引子」 → **clean-code**：`concepts/testing/tdd-red-green-refactor/`（TDD 節奏：紅－綠－重構 (Red-Green-Refactor)）
- `xp/cost-of-change`「變更成本曲線可以被壓平」 → **agile**：`concepts/xp-practices/xp-values-principles-practices/`（Beck 的推導：四個變數、變更成本與價值—原則—實踐）
- `xp/four-variables`「四個變數：成本、時間、品質、範圍」 → **agile**：`concepts/xp-practices/xp-values-principles-practices/`（Beck 的推導：四個變數、變更成本與價值—原則—實踐）

### leadership（28 筆）

- `coaching/feedback-that-lands`「有效回饋：對事不對人，即時不等年度」 → **hbr**：`concepts/leadership-teams/set-up-to-fail/`（注定失敗症候群：低績效者是怎麼被做出來的）
- `coaching/leader-leader`「領導者領導者：把命令變成意圖」 → **management**：`concepts/org-people/intent-based-leadership/`（意圖式領導：把權力交給資訊）
- `coaching/radical-candor`「徹底坦率：個人在乎 × 直接挑戰」 → **hr**：`concepts/performance-feedback/radical-candor-quadrants/`（徹底坦率：個人關懷與直接挑戰的二乘二）
- `culture/culture-map`「文化地圖：八條量表，而位置永遠是相對的」 → **travel**：`concepts/tour-leading/working-with-local-partners/`（跟地接、司機、餐廳溝通的文化地圖）
- `culture/freedom-and-responsibility`「自由與責任：先密度、再坦誠、最後才拿掉規則」 → **hr**：`concepts/culture-people-ops/talent-density-and-candor/`（人才密度與坦誠：Netflix 鬆綁管控的三步循環）
- `culture/freedom-and-responsibility`「自由與責任：先密度、再坦誠、最後才拿掉規則」 → **management**：`concepts/org-people/first-who-then-what/`（先找對人，再決定做什麼）
- `decisions/beware-cognitive-bias`「系統性偏誤：判斷的錯是可預測的，也能被設計掉」 → **management**：`concepts/managers-work/effective-decisions/`（有效的決策）
- `decisions/decisions-at-the-edge`「把決策授權到邊緣：眼睛盯著、手放開」 → **management**：`concepts/org-people/shared-consciousness/`（共享意識：從複雜到賦能執行）；`concepts/org-people/intent-based-leadership/`（意圖式領導：把權力交給資訊）
- `decisions/solve-the-right-problem`「先解對的問題：重新框架，比解得快更重要」 → **problem-solving**：`concepts/hypothesis-thinking/reframe-the-problem/`（重組問題框架：電梯太慢，還是等待太難熬？）
- `mindset/five-levels-of-leadership`「領導力是影響力，不是職位：五個層級的成長階梯」 → **maxwell**：`concepts/leadership/developing-leader-within-you/`（從內做起：先領導自己，影響力才長得出來）
- `mindset/inside-out-leadership`「由內而外：品格先於技巧的領導修練」 → **covey**：`concepts/principles/character-over-personality/`（品格倫理與個性倫理）；`concepts/principles/habit-anatomy-and-maturity-continuum/`（習慣的解剖與成熟連續體）
- `mindset/lead-yourself-first`「先領導自己：最難帶的人是你自己」 → **maxwell**：`concepts/leadership/five-levels-of-leadership/`（領導力的五個層級：影響力是一級一級爬上來的）；`concepts/leadership/leadership-gold/`（領導黃金法則：領導力就是影響力）
- `team/boundaries-for-leaders`「領導者的界線：你創造與容忍的一切，就是你得到的團隊」 → **cloud**：`concepts/boundaries/boundaries-for-leaders/`（領導者的界線：畫出團隊的道德範圍）
- `team/hiring-and-keeping`「招對人、留住人：把選才當科學，把留才當日常」 → **hr**：`concepts/recruiting/interview-questions-that-work/`（問得出東西的面試題：行為題與追問）；`concepts/retention-motivation/why-people-stay/`（留才不從辭呈開始：進展、重要感與留任對話）
- `team/managerial-leverage`「管理槓桿率：管理者的產出＝組織的產出」 → **grove**：`concepts/people/task-relevant-maturity/`（任務相關成熟度（TRM））；`concepts/output/meetings-as-medium/`（會議是管理工作的媒介）
- `vision/bhag-and-core-purpose`「膽大目標與核心使命：值得追隨的願景架構」 → **business-strategy**：`concepts/execution/hedgehog-concept/`（刺蝟原則：三個圓的交集）
- `vision/bhag-and-core-purpose`「膽大目標與核心使命：值得追隨的願景架構」 → **collins**：`concepts/greatness/hedgehog-concept/`（刺蝟原則：三個圓的交集）
- `vision/clock-building`「造鐘，而非報時：讓公司自己會走的組織設計」 → **collins**：`concepts/enduring/preserve-core-stimulate-progress/`（保存核心，刺激進步）；`concepts/enduring/clock-building-not-time-telling/`（造鐘，不是報時）
- `vision/clock-building`「造鐘，而非報時：讓公司自己會走的組織設計」 → **management**：`concepts/org-people/first-who-then-what/`（先找對人，再決定做什麼）
- `vision/confront-brutal-facts`「直面殘酷事實，卻永不失去信念：史托克戴爾悖論」 → **collins**：`concepts/greatness/confront-the-brutal-facts/`（面對殘酷的現實（史托克戴爾弔詭））
- `vision/disruption-dilemma`「創新的兩難：好管理為什麼會害死好公司」 → **christensen**：`concepts/disruption/value-networks/`（價值網絡：為什麼資源流不到破壞上）；`concepts/disruption/why-good-management-fails/`（好管理為何導致失敗）
- `vision/drucker-five-questions`「杜拉克的五個最重要問題：逼出使命與方向的自我評量」 → **drucker**：`concepts/management/five-questions/`（杜拉克的五個關鍵問題）
- `vision/first-who-then-what`「先人後事：先把對的人請上車，再決定車開去哪」 → **collins**：`concepts/greatness/first-who-then-what/`（先找對人，再決定要做什麼）
- `vision/first-who-then-what`「先人後事：先把對的人請上車，再決定車開去哪」 → **management**：`concepts/org-people/first-who-then-what/`（先找對人，再決定做什麼）
- `vision/level-5-and-hedgehog`「第五級領導與刺蝟原則：謙遜的意志」 → **business-strategy**：`concepts/execution/`（Execution & Operations）
- `vision/level-5-and-hedgehog`「第五級領導與刺蝟原則：謙遜的意志」 → **collins**：`concepts/greatness/`（Good to Great）
- `vision/okr`「OKR：聚焦、對齊、追蹤與挑戰極限」 → **grove**：`concepts/output/mbo-and-okr/`（目標管理：從 MBO 到 OKR）
- `vision/twenty-mile-march`「十倍勝：不確定中的二十哩行軍」 → **collins**：`concepts/discipline/`（Great by Choice）

### learning（11 筆）

- `memory/stop-highlighting`「別再邊讀邊畫線：重讀與畫線為何最沒用」 → **growth**：`concepts/learning-resilience/make-it-stick/`（有效學習：提取練習勝過反覆重讀）；`concepts/learning-resilience/retrieval-practice/`（提取練習：測試效應與對抗「我懂了」的錯覺）
- `metacognition/growth-mindset`「成長心態：能力不是天賦，是長出來的」 → **wan-weigang**：`concepts/thinking/how-learning-works/`（學習究竟是什麼：刻意練習）
- `metacognition/illusion-of-competence`「能力的錯覺：為什麼我們高估自己懂多少」 → **growth**：`concepts/learning-resilience/make-it-stick/`（有效學習：提取練習勝過反覆重讀）；`concepts/learning-resilience/retrieval-practice/`（提取練習：測試效應與對抗「我懂了」的錯覺）
- `practice/deliberate-practice-basics`「刻意練習入門：不是苦練，是有方法的練」 → **growth**：`concepts/deliberate-practice/purposeful-practice/`（刻意練習：不是練久，而是練對）；`concepts/deliberate-practice/get-out-of-comfort-zone/`（走出舒適區：身體與大腦如何被「逼」出改變）
- `practice/desirable-difficulty`「甜蜜點：把難度停在剛好超出能力的邊界」 → **wan-weigang**：`concepts/thinking/how-learning-works/`（學習究竟是什麼：刻意練習）
- `practice/drill-weakest-point`「鑽研法則：找出限速的那一步，單獨猛攻」 → **career**：`concepts/grit-mastery/ultralearning-projects/`（超速學習：自主設計高強度學習專案）
- `practice/not-just-repetition`「練習 ≠ 重複」 → **growth**：`concepts/learning-resilience/spaced-interleaved-practice/`（間隔與交錯練習：為什麼「更難的練法」記得更牢）
- `reading/purposeful-reading`「帶著目的讀：先問為什麼，再翻開書」 → **problem-solving**：`concepts/instant-execution/read-for-action/`（為行動而讀：麥肯錫式主動閱讀）
- `self-learning/directness`「直接原則：在你真正要用它的地方學」 → **career**：`concepts/grit-mastery/ultralearning-projects/`（超速學習：自主設計高強度學習專案）
- `self-learning/feynman-technique`「費曼技巧：戳破「我以為我懂」」 → **career**：`concepts/grit-mastery/ultralearning-projects/`（超速學習：自主設計高強度學習專案）
- `self-learning/metalearning-first`「後設學習：動手前，先畫一張地圖」 → **career**：`concepts/grit-mastery/ultralearning-projects/`（超速學習：自主設計高強度學習專案）

### lewis（4 筆）

- `apologetics/abolition-of-man`「人之廢：客觀價值與教育的危機」 → **theology**：`concepts/apologetics/imaginative-apologetics/`（想像力的護教：悖論、魔鬼書信與人之廢）
- `apologetics/mere-christianity`「返璞歸真：從道德律到基督信仰」 → **theology**：`concepts/apologetics/argument-from-desire/`（從道德律與渴望出發：路易斯式護教的起點）
- `apologetics/problem-of-pain`「痛苦的奧秘：全善全能與苦難」 → **spiritual-formation**：`concepts/suffering-grief/problem-of-pain/`（痛苦的奧秘：全能與美善如何並存）
- `love/grief-observed`「卿卿如晤：哀傷作為信仰的試煉」 → **spiritual-formation**：`concepts/suffering-grief/grief-and-faith/`（在悲傷中觀看：信心如何面對失落）

### life-meaning（8 筆）

- `aging-finitude/take-the-long-view`「用一生的長度回望現在」 → **wellness**：`concepts/happiness-wellbeing/what-makes-a-good-life/`（什麼造就美好人生：哈佛 84 年的答案）
- `body-wellness/first-90-minutes`「顧好開頭的黃金 90 分鐘」 → **wellness**：`concepts/nutrition-sleep/sleeping-better/`（如何睡得更好：把睡眠品質做出來）
- `body-wellness/sleep-is-the-foundation`「睡眠是一切的地基」 → **wellness**：`concepts/nutrition-sleep/why-we-sleep/`（為什麼要睡覺：睡眠是不可協商的根基）
- `meaning/attitude-is-a-choice`「態度：你唯一能百分之百掌握的資產」 → **maxwell**：`concepts/growth/difference-maker/`（態度是差異製造者：不是一切，卻是那一件足以拉開差距的事）
- `meaning/marginal-thinking`「邊際思維的陷阱：just this once」 → **christensen**：`concepts/life-strategy/just-this-once/`（「就這一次」的邊際成本陷阱）
- `resilience/fail-forward`「重新定義失敗：它是事件，不是身份」 → **maxwell**：`concepts/growth/failing-forward/`（從失敗中前進：把每一次跌倒變成墊腳石）
- `resilience/post-traumatic-growth`「創傷後成長：不是復原，是向前反彈」 → **grant**：`concepts/resilience/post-traumatic-growth/`（創傷後成長：向前彈起）
- `resilience/three-ps-of-resilience`「復原的三個 P：擋住讓你陷更深的三個念頭」 → **grant**：`concepts/resilience/three-ps/`（三個 P：擋住復原的思維陷阱）；`concepts/resilience/platinum-rule/`（友誼的白金法則）

### liurun（1 筆）

- `trend-evolution/embrace-uncertainty`「進化的力量：把不確定性變成機會」 → **science**：`concepts/evolution-life/evolution-as-algorithm/`（演化是一套演算法）

### management（24 筆）

- `goals-performance/performance-review`「績效評估與回饋」 → **behaviour-interview**：`concepts/big-tech/management-track/`（管理軌：從指導到管理經理）
- `goals-performance/performance-review`「績效評估與回饋」 → **grove**：`concepts/people/performance-appraisal/`（績效考核：最難的那場對話）
- `managers-work/effective-decisions`「有效的決策」 → **leadership**：`concepts/decisions/beware-cognitive-bias/`（系統性偏誤：判斷的錯是可預測的，也能被設計掉）
- `managers-work/know-thy-time`「認識你的時間」 → **career**：`concepts/manage-yourself/know-your-strengths/`（用回饋分析找出長處）；`concepts/manage-yourself/managing-oneself/`（認識自己：長處、學習方式與貢獻）
- `managers-work/know-thy-time`「認識你的時間」 → **drucker**：`concepts/executive/`（自我管理與效能）
- `managers-work/know-thy-time`「認識你的時間」 → **tools**：`concepts/time-management/gtd-trusted-system/`（GTD：把待辦清空大腦，交給可信賴的系統）
- `managers-work/one-on-one`「一對一會議」 → **grove**：`concepts/people/right-to-be-managed/`（你有被好好管理的權利）；`concepts/output/meetings-as-medium/`（會議是管理工作的媒介）
- `org-people/centralization-and-decentralization`「集權與分權：公司的概念」 → **drucker**：`concepts/society/corporation-as-social-institution/`（企業作為社會制度：通用汽車的十八個月）
- `org-people/first-who-then-what`「先找對人，再決定做什麼」 → **collins**：`concepts/greatness/first-who-then-what/`（先找對人，再決定要做什麼）；`concepts/enduring/clock-building-not-time-telling/`（造鐘，不是報時）
- `org-people/first-who-then-what`「先找對人，再決定做什麼」 → **hr**：`concepts/culture-people-ops/talent-density-and-candor/`（人才密度與坦誠：Netflix 鬆綁管控的三步循環）
- `org-people/first-who-then-what`「先找對人，再決定做什麼」 → **leadership**：`concepts/vision/first-who-then-what/`（先人後事：先把對的人請上車，再決定車開去哪）；`concepts/culture/freedom-and-responsibility/`（自由與責任：先密度、再坦誠、最後才拿掉規則）
- `org-people/intent-based-leadership`「意圖式領導：把權力交給資訊」 → **leadership**：`concepts/decisions/decisions-at-the-edge/`（把決策授權到邊緣：眼睛盯著、手放開）；`concepts/coaching/leader-leader/`（領導者領導者：把命令變成意圖）
- `org-people/shared-consciousness`「共享意識：從複雜到賦能執行」 → **leadership**：`concepts/decisions/decisions-at-the-edge/`（把決策授權到邊緣：眼睛盯著、手放開）
- `org-people/staff-on-strengths`「用人之長」 → **business-strategy**：`concepts/management/the-effective-executive/`（有效的經營者：效能是可以學的五個習慣）
- `org-people/staff-on-strengths`「用人之長」 → **drucker**：`concepts/executive/effectiveness-can-be-learned/`（效能是可以學的習慣：卓有成效的管理者不是天生的）；`concepts/executive/managing-your-time/`（先管理你的時間：認識時間，才能認識工作）
- `principles/disruptive-innovation`「破壞式創新的兩難」 → **business-strategy**：`concepts/disruption/disruptive-innovation/`（破壞式創新：好公司為何做對每件事仍失敗）
- `principles/disruptive-innovation`「破壞式創新的兩難」 → **startup**：`concepts/validation/mvp-and-learning/`（MVP 與驗證式學習）
- `principles/knowledge-worker`「知識工作者與知識社會」 → **business-strategy**：`concepts/management/knowledge-worker/`（知識工作者：讓知識的生產力成為管理核心）
- `principles/knowledge-worker`「知識工作者與知識社會」 → **drucker**：`concepts/society/age-of-discontinuity/`（不連續的時代：看見尚未被察覺的斷裂）
- `principles/marketing-and-innovation`「行銷與創新：企業僅有的兩個功能」 → **business-strategy**：`concepts/disruption/sources-of-innovation/`（創新的七個來源：創新是一門可練的紀律）
- `principles/marketing-and-innovation`「行銷與創新：企業僅有的兩個功能」 → **drucker**：`concepts/management/what-is-a-business/`（企業是什麼：創造顧客）；`concepts/innovation/seven-sources-of-innovation/`（創新的七個來源：有系統地搜尋機會）
- `principles/marketing-and-innovation`「行銷與創新：企業僅有的兩個功能」 → **startup**：`concepts/opportunity/drucker-seven-sources/`（創新的七個機會來源（Drucker））
- `principles/purpose-of-business`「企業的目的是創造顧客」 → **business-strategy**：`concepts/management/management-by-objectives/`（目標管理（MBO）：用目標與自我控制取代支配）
- `principles/purpose-of-business`「企業的目的是創造顧客」 → **drucker**：`concepts/management/management-by-objectives/`（目標管理與自我控制：讓每個人的努力指向共同成果）

### marketing（2 筆）

- `content-attention/ogilvy-on-advertising`「奧格威談廣告：會賣的廣告才是好廣告」 → **writing**：`concepts/nonfiction-copy/lead-with-benefit/`（以讀者利益開場 (Lead with the Reader's Benefit)）
- `social-channels/youtube-watchability`「YouTube 可看性：七個 C 與演算法」 → **travel**：`concepts/travel-video/seven-cs-channel-strategy/`（七 C 法則：把 YouTube 頻道當成一個電視台來經營）

### maxwell（2 筆）

- `growth/difference-maker`「態度是差異製造者：不是一切，卻是那一件足以拉開差距的事」 → **life-meaning**：`concepts/meaning/attitude-is-a-choice/`（態度：你唯一能百分之百掌握的資產）
- `growth/failing-forward`「從失敗中前進：把每一次跌倒變成墊腳石」 → **life-meaning**：`concepts/resilience/fail-forward/`（重新定義失敗：它是事件，不是身份）

### navarro（2 筆）

- `limbic/freeze-flight-fight`「凍結、逃跑、戰鬥——順序不是隨機的」 → **thinking**：`concepts/judgment-bias/reading-the-body/`（讀身體：非語言的真信號）
- `limbic/pacifying-behaviors`「安撫行為是壓力的收據」 → **thinking**：`concepts/judgment-bias/reading-the-body/`（讀身體：非語言的真信號）

### newport（5 筆）

- `career-capital/career-capital-over-passion`「職涯資本勝過熱情：技能先於使命」 → **career**：`concepts/career-capital/`（Career Capital）
- `career-capital/career-capital-over-passion`「職涯資本勝過熱情：技能先於使命」 → **growth**：`concepts/talent-grit/passion-follows-mastery/`（職涯資本：別追隨熱情，先變得夠好）
- `deep-work/deep-work-hypothesis`「深度工作假說：專注是新經濟的資本」 → **tools**：`concepts/focus-attention/deep-work-value/`（深度工作：稀缺而高價值的專注能力）
- `digital-minimalism/digital-declutter`「30 天數位斷捨離：以價值觀重建科技生活」 → **tools**：`concepts/focus-attention/digital-minimalism/`（數位極簡：把注意力從螢幕手中奪回來）
- `slow-productivity/three-principles-of-slow-productivity`「慢速生產力三原則：少做、自然節奏、品質執念」 → **tools**：`concepts/focus-attention/slow-productivity/`（慢生產力：以品質與節奏取代忙碌的表演）

### nouwen（5 筆）

- `compassion-ministry/wounded-healer`「負傷的治療者：以傷口服事的牧養」 → **spiritual-formation**：`concepts/community-solitude/wounded-healer/`（受傷的醫治者：從自己的傷口服事人）
- `compassion-ministry/wounded-healer`「負傷的治療者：以傷口服事的牧養」 → **theology**：`concepts/church-and-ministry/wounded-healer/`（負傷的治療者：牧養的核心身分）
- `spiritual-life/solitude-silence-prayer`「獨處、靜默、禱告：沙漠靈修的三重操練」 → **spiritual-formation**：`concepts/community-solitude/solitude-silence-prayer/`（獨處、靜默與禱告：心靈的三重操練）
- `transformation/befriending-death`「與死亡為友：最大的禮物」 → **relationships**：`concepts/friendship/presence-in-loss/`（陪伴脆弱者：關係裡最後的禮物）
- `transformation/homecoming`「回家：從小兒子、大兒子到成為父親」 → **spiritual-formation**：`concepts/discipleship/downward-way/`（向下的道路：捨己與跟隨的方向）

### nt-wright（1 筆）

- `apologetics/simply-christian`「Simply Christian：從四種渴望指向上帝」 → **theology**：`concepts/apologetics/faith-in-a-secular-age/`（世俗時代還能信嗎：給懷疑者的邀請）

### peck（3 筆）

- `growth/four-disciplines`「自律的四項原則」 → **relationships**：`concepts/dating/love-is-a-choice/`（愛是選擇，不是墜落）
- `growth/real-love`「重新定義愛：投入與抉擇」 → **relationships**：`concepts/dating/love-is-a-choice/`（愛是選擇，不是墜落）
- `growth/road-less-traveled`「心靈地圖：紀律、愛與成長」 → **relationships**：`concepts/dating/love-is-a-choice/`（愛是選擇，不是墜落）

### philosophy（8 筆）

- `applied/philosophy-as-consolation`「哲學作為慰藉：六帖給日常煩惱的解藥」 → **de-botton**：`concepts/philosophy/consolations-of-philosophy/`（哲學的慰藉：六位哲人面對人生困境）；`concepts/philosophy/epicurus-on-money/`（伊壁鳩魯論缺錢：友誼、自由與思想）
- `applied/religion-for-atheists`「取其功能、去其信仰：無神論者的宗教用途」 → **de-botton**：`concepts/philosophy/religion-for-atheists/`（無神論者的宗教：世俗如何借用信仰的智慧）
- `applied/status-anxiety`「地位焦慮：為什麼我們怕被人看輕」 → **de-botton**：`concepts/status/status-anxiety/`（身分的焦慮：我們為何在意地位）；`concepts/status/solutions-to-status/`（五種解方：哲學、藝術、政治、宗教、波希米亞）
- `eastern/no-ceo-modular-mind`「心智沒有 CEO：無我的現代論證」 → **science**：`concepts/mind-cognition/modular-mind-and-no-self/`（模組心智與無我：大腦裡沒有執行長）
- `ethics-justice/having-vs-being`「占有還是存在：兩種活法，兩種自我」 → **fromm**：`concepts/love-being/to-have-or-to-be/`（擁有還是存在：兩種生存模式）
- `ethics-justice/productive-love`「愛是一種能力，不是運氣：Fromm 的愛之藝術」 → **fromm**：`concepts/love-being/art-of-loving/`（愛的藝術：愛是需要學習與修練的能力）
- `ethics-justice/three-paths-of-justice`「正義的三條路徑：效益、自由、德性」 → **fromm**：`concepts/freedom/man-for-himself/`（自我的追尋：人本主義倫理學）
- `stoicism/ego-as-obstacle`「自我是絆腳石：在追求、成功、失敗三階段馴服 ego」 → **growth**：`concepts/self-awareness/ego-is-the-enemy/`（自我是敵人：謙遜是持續精進的前提）

### problem-solving（5 筆）

- `hypothesis-thinking/reframe-the-problem`「重組問題框架：電梯太慢，還是等待太難熬？」 → **leadership**：`concepts/decisions/solve-the-right-problem/`（先解對的問題：重新框架，比解得快更重要）
- `instant-execution/read-for-action`「為行動而讀：麥肯錫式主動閱讀」 → **learning**：`concepts/reading/purposeful-reading/`（帶著目的讀：先問為什麼，再翻開書）
- `instant-execution/zero-second-a4-memo`「零秒思考：A4 一分鐘筆記」 → **tools**：`concepts/note-systems/structured-thinking-to-conclusion/`（把思考倒到紙上：逼出結論的結構化書寫）
- `logic-structure/mece-and-logic-tree`「MECE 與邏輯樹：把問題拆乾淨」 → **business-strategy**：`concepts/execution/mece-problem-solving/`（MECE 與假說導向：麥肯錫的問題解決法）
- `logic-structure/three-problem-types`「三型問題：恢復原狀、防杜潛在、追求理想」 → **business-strategy**：`concepts/execution/mece-problem-solving/`（MECE 與假說導向：麥肯錫的問題解決法）

### relationships（6 筆）

- `boundaries/own-your-life`「界線：為自己的生命負責」 → **cloud**：`concepts/boundaries/ten-laws-of-boundaries/`（界線十律：按現實生活的法則）；`concepts/boundaries/boundaries/`（過猶不及：界線是什麼、為何需要）
- `connection/charm-is-attention`「魅力的本質：讓對方覺得自己重要」 → **tracy**：`concepts/sales/power-of-charm/`（魅力的力量：讓人喜歡與信任你）
- `dating/boundaries-in-dating`「約會前先照顧好自己：約會治不好寂寞」 → **cloud**：`concepts/boundaries/boundaries-in-dating/`（為約會立界線：戀愛中的自由與責任）
- `dating/love-is-a-choice`「愛是選擇，不是墜落」 → **peck**：`concepts/growth/`（心靈成長）
- `friendship/presence-in-loss`「陪伴脆弱者：關係裡最後的禮物」 → **nouwen**：`concepts/transformation/befriending-death/`（與死亡為友：最大的禮物）
- `marriage/love-as-craft`「浪漫主義的陷阱：婚姻從幻滅之後才開始」 → **de-botton**：`concepts/love/love-as-institution/`（愛的進化論：從激情到經營）

### science（11 筆）

- `evolution-life/evolution-as-algorithm`「演化是一套演算法」 → **liurun**：`concepts/trend-evolution/embrace-uncertainty/`（進化的力量：把不確定性變成機會）
- `evolution-life/shared-fictions`「共享的虛構：讓陌生人合作的技術」 → **history**：`concepts/ancient-origins/cognitive-revolution/`（認知革命：虛構故事讓大規模合作成真）；`concepts/ancient-origins/agricultural-trap/`（農業革命：史上最大的騙局？）
- `mind-cognition/elephant-and-rider`「象與騎象人：直覺先行，理性隨後」 → **thinking**：`concepts/moral-mind/elephant-and-rider/`（大象與騎象人：直覺先行，理性後補）
- `mind-cognition/metacognition-and-confidence`「後設認知：知道自己知不知道」 → **growth**：`concepts/self-awareness/observe-your-biases/`（潛意識：看不見的心智如何驅動你）
- `mind-cognition/modular-mind-and-no-self`「模組心智與無我：大腦裡沒有執行長」 → **philosophy**：`concepts/eastern/no-ceo-modular-mind/`（心智沒有 CEO：無我的現代論證）
- `mind-cognition/strange-loops`「怪圈：自我指涉如何湧現出意義」 → **thinking**：`concepts/consciousness/strange-loops-and-self/`（怪圈與自我指涉）
- `mind-cognition/system-one-and-system-two`「系統一與系統二：捷思如何生成偏誤」 → **thinking**：`concepts/judgment-bias/two-systems/`（系統一與系統二：驟下結論的機器與懶惰的監督者）
- `scientific-method/how-false-beliefs-form`「錯誤信念如何形成：我們怎麼「知道」其實不然的事」 → **thinking**：`concepts/judgment-bias/luck-and-superstition/`（運氣、迷信與可被設計的機率）；`concepts/judgment-bias/how-false-beliefs-form/`（錯誤信念如何形成：有缺陷的理性，而非非理性）
- `scientific-method/noise-in-judgment`「雜訊：偏誤之外的另一半誤差」 → **thinking**：`concepts/judgment-bias/decision-hygiene/`（決策保健：雜訊的「怎麼辦」那一半）；`concepts/judgment-bias/noise-in-judgment/`（雜訊：誤差的另一半）
- `scientific-method/prediction-and-bayes`「預測的極限與貝氏思維」 → **data-science**：`concepts/probability-bayes/bayesian-updating/`（貝氏更新：先驗、證據，與愈來愈少的錯誤）；`concepts/statistical-thinking/overfitting-signal-and-noise/`（過度配適：把雜訊當成訊號）
- `scientific-method/prediction-and-bayes`「預測的極限與貝氏思維」 → **thinking**：`concepts/mental-models/bayesian-thinking/`（貝氏思維：在雜訊裡錯得越來越少）

### spiritual-formation（8 筆）

- `community-solitude/solitude-silence-prayer`「獨處、靜默與禱告：心靈的三重操練」 → **nouwen**：`concepts/spiritual-life/solitude-silence-prayer/`（獨處、靜默、禱告：沙漠靈修的三重操練）
- `community-solitude/wounded-healer`「受傷的醫治者：從自己的傷口服事人」 → **nouwen**：`concepts/compassion-ministry/wounded-healer/`（負傷的治療者：以傷口服事的牧養）
- `community-solitude/wounded-healer`「受傷的醫治者：從自己的傷口服事人」 → **theology**：`concepts/church-and-ministry/wounded-healer/`（負傷的治療者：牧養的核心身分）
- `discipleship/downward-way`「向下的道路：捨己與跟隨的方向」 → **nouwen**：`concepts/transformation/downward-mobility/`（向下的移動：基督的捨己之路）；`concepts/transformation/homecoming/`（回家：從小兒子、大兒子到成為父親）
- `discipleship/twelve-spiritual-disciplines`「十二個屬靈操練：內在、外在與團契」 → **habits**：`concepts/discipline/spiritual-disciplines/`（靈性操練：通往自由的門）
- `prayer-pilgrimage/prayer-as-conversation`「禱告：與神持續的對話」 → **lewis**：`concepts/devotional/letters-to-malcolm/`（禱告的奧祕：與神對談）
- `suffering-grief/grief-and-faith`「在悲傷中觀看：信心如何面對失落」 → **lewis**：`concepts/love/grief-observed/`（卿卿如晤：哀傷作為信仰的試煉）
- `suffering-grief/problem-of-pain`「痛苦的奧秘：全能與美善如何並存」 → **lewis**：`concepts/apologetics/problem-of-pain/`（痛苦的奧秘：全善全能與苦難）

### startup（7 筆）

- `founder/permanent-beta`「永遠處於 Beta：像新創一樣經營自己」 → **career**：`concepts/career-capital/career-as-startup/`（把自己當新創經營：ABZ 計畫）
- `money-exit/buy-dont-build`「用買的，別從零打造：透過收購創業（ETA）」 → **hbr**：`concepts/strategy-innovation/buy-a-small-business/`（買下一家小公司：另一條創業路）
- `opportunity/drucker-seven-sources`「創新的七個機會來源（Drucker）」 → **business-strategy**：`concepts/disruption/sources-of-innovation/`（創新的七個來源：創新是一門可練的紀律）
- `opportunity/drucker-seven-sources`「創新的七個機會來源（Drucker）」 → **drucker**：`concepts/innovation/seven-sources-of-innovation/`（創新的七個來源：有系統地搜尋機會）
- `opportunity/drucker-seven-sources`「創新的七個機會來源（Drucker）」 → **management**：`concepts/principles/marketing-and-innovation/`（行銷與創新：企業僅有的兩個功能）
- `team-culture/hire-for-attitude`「為態度招募：51% 情商解方」 → **travel**：`concepts/tour-leading/enlightened-hospitality/`（開明款待：服務是獨白，款待是對話）
- `validation/mvp-and-learning`「MVP 與驗證式學習」 → **management**：`concepts/principles/disruptive-innovation/`（破壞式創新的兩難）

### stott（2 筆）

- `discipleship/living-church`「活的教會：新約教會的記號」 → **theology**：`concepts/church-and-ministry/what-makes-a-living-church/`（活的教會：斯托得的教會觀）
- `discipleship/radical-disciple`「世界在等待的門徒：非隨波逐流的基督徒」 → **theology**：`concepts/church-and-ministry/what-makes-a-living-church/`（活的教會：斯托得的教會觀）

### system-design（7 筆）

- `caching/caching-strategies`「快取策略 (Caching Strategies)」 → **data-systems**：`concepts/storage-engines/`（Storage Engines）；`concepts/indexing/clustered-vs-secondary/`（聚簇索引 vs 次級索引 (Clustered vs Secondary)）；`concepts/indexing/covering-and-composite-indexes/`（覆蓋索引與多欄索引 (Covering & Composite Indexes)）
- `communication/data-encoding`「資料編碼與演進 (Encoding & Evolution)」 → **data-systems**：`concepts/encoding/`（Encoding & Evolution）
- `consistency-consensus/quorum-replication`「Quorum 讀寫 (Quorum Reads & Writes)」 → **data-systems**：`concepts/replication/`（Replication）
- `messaging/message-queue`「訊息佇列 (Message Queue)」 → **data-systems**：`concepts/batch-stream/`（Batch & Stream）
- `observability/golden-signals`「四個黃金指標 (Golden Signals)」 → **cloud-infra**：`concepts/observability/`（Observability）
- `observability/slo-sli-sla`「SLI / SLO / SLA」 → **cloud-infra**：`concepts/slos-error-budgets/`（SLOs & Error Budgets）
- `reliability/idempotency`「冪等設計 (Idempotency)」 → **data-systems**：`concepts/encoding/`（Encoding & Evolution）

### theology（9 筆）

- `apologetics/argument-from-desire`「從道德律與渴望出發：路易斯式護教的起點」 → **lewis**：`concepts/apologetics/mere-christianity/`（返璞歸真：從道德律到基督信仰）
- `apologetics/faith-in-a-secular-age`「世俗時代還能信嗎：給懷疑者的邀請」 → **keller**：`concepts/apologetics/making-sense-of-god/`（在信仰之前：世俗選項也需要信心）
- `apologetics/faith-in-a-secular-age`「世俗時代還能信嗎：給懷疑者的邀請」 → **nt-wright**：`concepts/apologetics/simply-christian/`（Simply Christian：從四種渴望指向上帝）
- `apologetics/imaginative-apologetics`「想像力的護教：悖論、魔鬼書信與人之廢」 → **lewis**：`concepts/apologetics/abolition-of-man/`（人之廢：客觀價值與教育的危機）
- `church-and-ministry/what-makes-a-living-church`「活的教會：斯托得的教會觀」 → **stott**：`concepts/discipleship/radical-disciple/`（世界在等待的門徒：非隨波逐流的基督徒）；`concepts/discipleship/living-church/`（活的教會：新約教會的記號）
- `church-and-ministry/wounded-healer`「負傷的治療者：牧養的核心身分」 → **nouwen**：`concepts/compassion-ministry/wounded-healer/`（負傷的治療者：以傷口服事的牧養）
- `church-and-ministry/wounded-healer`「負傷的治療者：牧養的核心身分」 → **spiritual-formation**：`concepts/community-solitude/wounded-healer/`（受傷的醫治者：從自己的傷口服事人）
- `doctrine/cross-of-christ`「十字架的中心：神為何非死不可」 → **stott**：`concepts/foundations/cross-of-christ/`（基督的十架：福音的中心）
- `doctrine/kingdom-of-god-here-and-now`「天國就在此時此地：與神互動的生活」 → **willard**：`concepts/kingdom-gospel/`（天國的福音）；`concepts/spiritual-disciplines/curriculum-for-christlikeness/`（像基督課程：作門徒的課綱）

### thinking（16 筆）

- `consciousness/strange-loops-and-self`「怪圈與自我指涉」 → **science**：`concepts/mind-cognition/strange-loops/`（怪圈：自我指涉如何湧現出意義）
- `depth-psychology/anima-animus`「阿尼瑪與阿尼姆斯」 → **jung**：`concepts/individuation/process-of-individuation/`（個體化的歷程）；`concepts/unconscious/anima-animus/`（阿尼瑪與阿尼姆斯）
- `depth-psychology/collective-unconscious`「集體潛意識與原型」 → **jung**：`concepts/unconscious/collective-unconscious-and-archetypes/`（集體無意識與原型）
- `depth-psychology/dreams-as-messages`「夢作為潛意識的訊息」 → **jung**：`concepts/dreams/dream-series/`（夢的系列：為什麼單一夢不可靠）；`concepts/dreams/compensation-and-dreams/`（補償法則與夢）
- `depth-psychology/individuation-and-the-self`「個體化：邁向完整的自己」 → **jung**：`concepts/life/confrontation-with-the-unconscious/`（與無意識的對峙）
- `judgment-bias/decision-hygiene`「決策保健：雜訊的「怎麼辦」那一半」 → **science**：`concepts/scientific-method/noise-in-judgment/`（雜訊：偏誤之外的另一半誤差）
- `judgment-bias/how-false-beliefs-form`「錯誤信念如何形成：有缺陷的理性，而非非理性」 → **science**：`concepts/scientific-method/how-false-beliefs-form/`（錯誤信念如何形成：我們怎麼「知道」其實不然的事）
- `judgment-bias/luck-and-superstition`「運氣、迷信與可被設計的機率」 → **science**：`concepts/scientific-method/how-false-beliefs-form/`（錯誤信念如何形成：我們怎麼「知道」其實不然的事）
- `judgment-bias/noise-in-judgment`「雜訊：誤差的另一半」 → **science**：`concepts/scientific-method/noise-in-judgment/`（雜訊：偏誤之外的另一半誤差）
- `judgment-bias/predictable-irrationality`「可預測的非理性：行為經濟學的實驗場」 → **economics**：`concepts/behavioral-narrative/anchoring-relativity/`（定錨與相對性：偏好是被製造出來的）
- `judgment-bias/reading-the-body`「讀身體：非語言的真信號」 → **navarro**：`concepts/limbic/freeze-flight-fight/`（凍結、逃跑、戰鬥——順序不是隨機的）；`concepts/limbic/pacifying-behaviors/`（安撫行為是壓力的收據）
- `judgment-bias/two-systems`「系統一與系統二：驟下結論的機器與懶惰的監督者」 → **science**：`concepts/mind-cognition/system-one-and-system-two/`（系統一與系統二：捷思如何生成偏誤）
- `mental-models/bayesian-thinking`「貝氏思維：在雜訊裡錯得越來越少」 → **data-science**：`concepts/statistical-thinking/overfitting-signal-and-noise/`（過度配適：把雜訊當成訊號）；`concepts/probability-bayes/bayesian-updating/`（貝氏更新：先驗、證據，與愈來愈少的錯誤）
- `mental-models/bayesian-thinking`「貝氏思維：在雜訊裡錯得越來越少」 → **science**：`concepts/scientific-method/prediction-and-bayes/`（預測的極限與貝氏思維）
- `moral-mind/elephant-and-rider`「大象與騎象人：直覺先行，理性後補」 → **science**：`concepts/mind-cognition/elephant-and-rider/`（象與騎象人：直覺先行，理性隨後）
- `self-knowledge/meaning-in-modern-life`「現代人的意義追尋」 → **jung**：`concepts/religion/spiritual-problem-of-modern-man/`（現代人的精神問題）

### tools（16 筆）

- `focus-attention/deep-work-value`「深度工作：稀缺而高價值的專注能力」 → **newport**：`concepts/deep-work/deep-work-hypothesis/`（深度工作假說：專注是新經濟的資本）
- `focus-attention/digital-minimalism`「數位極簡：把注意力從螢幕手中奪回來」 → **newport**：`concepts/digital-minimalism/digital-declutter/`（30 天數位斷捨離：以價值觀重建科技生活）
- `focus-attention/internal-triggers-indistractable`「分心的根源在內不在外：專注力協定」 → **habits**：`concepts/focus/make-distraction-hard/`（讓分心變困難：成為 Indistractable）
- `focus-attention/slow-productivity`「慢生產力：以品質與節奏取代忙碌的表演」 → **newport**：`concepts/slow-productivity/three-principles-of-slow-productivity/`（慢速生產力三原則：少做、自然節奏、品質執念）
- `habits/checklist-against-complexity`「清單革命：在極端複雜下防止已知的失誤」 → **travel**：`concepts/tour-design/departure-checklists/`（出團清單：暫停點、DO-CONFIRM 與殺手項目）
- `habits/seven-habits-effectiveness`「七個習慣：從依賴到互賴的效能連續體」 → **career**：`concepts/manage-yourself/seven-habits-inside-out/`（與成功有約：由內而外的效能）
- `habits/seven-habits-effectiveness`「七個習慣：從依賴到互賴的效能連續體」 → **covey**：`concepts/public-victory/emotional-bank-account/`（情感帳戶：六種存款）
- `habits/systems-over-goals-atomic-habits`「原子習慣：系統勝過目標，身分帶動行為」 → **career**：`concepts/grit-mastery/atomic-habits-identity/`（原子習慣：身分認同驅動的系統）
- `habits/systems-over-goals-atomic-habits`「原子習慣：系統勝過目標，身分帶動行為」 → **habits**：`concepts/systems-over-goals/one-percent-compounding/`（系統勝於目標：1% 的複利）；`concepts/habit-loop/identity-based-habits/`（身分認同式習慣：先決定你想成為誰）
- `habits/tiny-habits-behavior-design`「行為設計：B=MAP 與小到不可能失敗的習慣」 → **habits**：`concepts/habit-loop/behavior-model/`（行為 = 動機 × 能力 × 提示（B=MAP））；`concepts/habit-loop/make-it-tiny/`（把習慣縮到極小：微習慣）
- `note-systems/structured-thinking-to-conclusion`「把思考倒到紙上：逼出結論的結構化書寫」 → **problem-solving**：`concepts/instant-execution/zero-second-a4-memo/`（零秒思考：A4 一分鐘筆記）
- `time-management/clock-and-compass-quadrant-two`「鐘與羅盤：第二象限的要事規劃」 → **covey**：`concepts/personal-victory/`（Personal Victory）；`concepts/principles/live-love-learn-leave-a-legacy/`（生活、愛、學習、留下傳承：四項基本需要）
- `time-management/clock-and-compass-quadrant-two`「鐘與羅盤：第二象限的要事規劃」 → **habits**：`concepts/productivity/big-rocks-first/`（要事第一：先放大石頭）
- `time-management/finitude-four-thousand-weeks`「四千個禮拜：接受做不完，才談得上選擇」 → **habits**：`concepts/energy-routine/finitude-4000-weeks/`（承認有限：四千個禮拜）
- `time-management/gtd-trusted-system`「GTD：把待辦清空大腦，交給可信賴的系統」 → **management**：`concepts/managers-work/know-thy-time/`（認識你的時間）
- `time-management/results-over-hours`「看成果，不看工時」 → **hbr**：`concepts/self-management/managing-oneself/`（認識自己的長處與工作方式）

### tracy（1 筆）

- `sales/power-of-charm`「魅力的力量：讓人喜歡與信任你」 → **relationships**：`concepts/connection/charm-is-attention/`（魅力的本質：讓對方覺得自己重要）

### travel（5 筆）

- `destinations/learning-to-see-a-place`「學會看一個地方：期待、藝術與素描的眼光」 → **de-botton**：`concepts/beauty/art-of-travel/`（旅行的藝術：我不小心把自己一起帶去了）
- `tour-design/departure-checklists`「出團清單：暫停點、DO-CONFIRM 與殺手項目」 → **tools**：`concepts/habits/checklist-against-complexity/`（清單革命：在極端複雜下防止已知的失誤）
- `tour-leading/enlightened-hospitality`「開明款待：服務是獨白，款待是對話」 → **startup**：`concepts/team-culture/hire-for-attitude/`（為態度招募：51% 情商解方）
- `tour-leading/working-with-local-partners`「跟地接、司機、餐廳溝通的文化地圖」 → **leadership**：`concepts/culture/culture-map/`（文化地圖：八條量表，而位置永遠是相對的）
- `travel-video/seven-cs-channel-strategy`「七 C 法則：把 YouTube 頻道當成一個電視台來經營」 → **marketing**：`concepts/social-channels/youtube-watchability/`（YouTube 可看性：七個 C 與演算法）

### uncle-bob（4 筆）

- `clean-code/clean-code`「Clean Code：什麼是整潔的程式碼」 → **clean-code**：`concepts/naming/`（Naming）
- `clean-code/meaningful-names`「有意義的命名：讓意圖自明」 → **clean-code**：`concepts/naming/`（Naming）
- `clean-code/small-functions`「函式：短小、只做一件事」 → **clean-code**：`concepts/functions/`（Functions）；`concepts/refactoring-moves/extract-function/`（提取函式 (Extract Function)）；`concepts/code-smells/long-function/`（長函式 (Long Function)）
- `professionalism/agile-values`「敏捷的初衷：回到四個價值觀」 → **agile**：`concepts/xp-practices/test-driven-development/`（TDD：軟體的複式簿記）；`concepts/foundations/reasonable-expectations/`（合理期望：主管有權要求的那十二件事）

### wan-weigang（1 筆）

- `thinking/how-learning-works`「學習究竟是什麼：刻意練習」 → **learning**：`concepts/metacognition/growth-mindset/`（成長心態：能力不是天賦，是長出來的）；`concepts/practice/desirable-difficulty/`（甜蜜點：把難度停在剛好超出能力的邊界）

### wellness（4 筆）

- `happiness-wellbeing/what-makes-a-good-life`「什麼造就美好人生：哈佛 84 年的答案」 → **life-meaning**：`concepts/aging-finitude/take-the-long-view/`（用一生的長度回望現在）
- `nutrition-sleep/sleeping-better`「如何睡得更好：把睡眠品質做出來」 → **life-meaning**：`concepts/body-wellness/first-90-minutes/`（顧好開頭的黃金 90 分鐘）
- `nutrition-sleep/why-we-sleep`「為什麼要睡覺：睡眠是不可協商的根基」 → **life-meaning**：`concepts/body-wellness/sleep-is-the-foundation/`（睡眠是一切的地基）
- `stress-mental-health/managing-stress-and-burnout`「壓力與耗竭：從硬撐到恢復的管理」 → **hbr**：`concepts/self-management/manage-your-energy/`（管理精力，而非時間）

### willard（4 筆）

- `kingdom-gospel/eternal-living-now`「永生從現在開始：天國作為此刻的實存」 → **theology**：`concepts/doctrine/kingdom-of-god-here-and-now/`（天國就在此時此地：與神互動的生活）
- `kingdom-gospel/gospel-of-the-kingdom`「天國的福音，不是罪管理的福音」 → **theology**：`concepts/doctrine/kingdom-of-god-here-and-now/`（天國就在此時此地：與神互動的生活）
- `kingdom-gospel/sermon-on-the-mount`「登山寶訓：天國生活的課程表」 → **theology**：`concepts/doctrine/kingdom-of-god-here-and-now/`（天國就在此時此地：與神互動的生活）
- `spiritual-disciplines/curriculum-for-christlikeness`「像基督課程：作門徒的課綱」 → **theology**：`concepts/doctrine/kingdom-of-god-here-and-now/`（天國就在此時此地：與神互動的生活）

### writing（9 筆）

- `craft-mindset/resistance-and-turning-pro`「抗拒與轉職業 (Resistance & Turning Pro)」 → **habits**：`concepts/discipline/resistance-and-turning-pro/`（抵抗力與轉職業：創作紀律的戰爭）
- `nonfiction-copy/find-the-core`「找到核心訊息 (Find the Core)」 → **communication**：`concepts/presentation/smart-brevity/`（精簡寫作：二十六秒裡的四個動作）；`concepts/storytelling/made-to-stick-success/`（黏性六原則：為什麼有些觀念記得住）
- `nonfiction-copy/lead-with-benefit`「以讀者利益開場 (Lead with the Reader's Benefit)」 → **marketing**：`concepts/content-attention/ogilvy-on-advertising/`（奧格威談廣告：會賣的廣告才是好廣告）
- `nonfiction-copy/make-them-care`「讓讀者在乎、相信 (Make Them Care & Believe)」 → **communication**：`concepts/storytelling/made-to-stick-success/`（黏性六原則：為什麼有些觀念記得住）；`concepts/storytelling/curiosity-gap/`（好奇心缺口：先製造未知）
- `nonfiction-copy/story-as-persuasion`「用故事說服 (Story as Persuasion)」 → **communication**：`concepts/storytelling/made-to-stick-success/`（黏性六原則：為什麼有些觀念記得住）；`concepts/storytelling/curiosity-gap/`（好奇心缺口：先製造未知）
- `nonfiction-copy/unexpected-and-curiosity`「製造意外，打開好奇 (Unexpected & Curiosity Gap)」 → **communication**：`concepts/storytelling/made-to-stick-success/`（黏性六原則：為什麼有些觀念記得住）；`concepts/storytelling/curiosity-gap/`（好奇心缺口：先製造未知）
- `story-structure/desire-and-conflict`「欲望與衝突 (Desire & Conflict)」 → **communication**：`concepts/storytelling/brain-on-story/`（大腦如何被故事點燃：敘事的心理機制）
- `story-structure/monomyth`「單一神話：離別・啟蒙・回歸 (The Monomyth)」 → **communication**：`concepts/storytelling/heros-journey/`（千面英雄：單一神話的敘事骨架）
- `story-structure/storytelling-brain`「說故事的大腦：預測、缺陷與戲劇問題 (The Storytelling Brain)」 → **communication**：`concepts/storytelling/brain-on-story/`（大腦如何被故事點燃：敘事的心理機制）

## 被 schema 擋住的缺口（strict 站 → 非技術站）

技術站群的 `seeAlso.site` 走 `siteKeys` enum，目前只含技術站自己的 key。這些缺口**真實存在**
（同書同章），但寫進 frontmatter build 會紅。要放行得改 notes-core：讓 enum 涵蓋全部 79 個 key
（仍是封閉集合，拼錯照樣抓得到），升版後重跑本工具它們就會進決策 JSON。

| 來源站 | 目標站 | 筆數 |
| --- | --- | ---: |
| `clean-code` | `uncle-bob` | 14 |
| `behaviour-interview` | `management` | 1 |
| `behaviour-interview` | `communication` | 1 |
| `behaviour-interview` | `career` | 1 |
| `clean-code` | `kent-beck` | 1 |
| `design-patterns` | `uncle-bob` | 1 |

<details><summary>逐筆</summary>

- `behaviour-interview` `big-tech/management-track`「管理軌：從指導到管理經理」 → **management**（共用 1 章）
- `behaviour-interview` `delivery/story-typology`「故事類型學：四種必備故事」 → **communication**（共用 1 章）
- `behaviour-interview` `frameworks/piecing-together`「組裝完整故事 (Piecing It Together)」 → **career**（共用 1 章）
- `clean-code` `code-smells/long-function`「長函式 (Long Function)」 → **uncle-bob**（共用 1 章）
- `clean-code` `functions/avoid-side-effects`「避免副作用 (Avoid Side Effects)」 → **uncle-bob**（共用 1 章）
- `clean-code` `functions/command-query-separation`「分離命令與查詢 (Command-Query Separation)」 → **uncle-bob**（共用 1 章）
- `clean-code` `functions/function-arguments`「函式參數 (Function Arguments)」 → **uncle-bob**（共用 1 章）
- `clean-code` `functions/small-functions-do-one-thing`「小函式，只做一件事 (Do One Thing)」 → **uncle-bob**（共用 1 章）
- `clean-code` `naming/avoid-disinformation`「避免誤導 (Avoid Disinformation)」 → **uncle-bob**（共用 2 章）
- `clean-code` `naming/avoid-encodings`「別把型別編進名字 (Avoid Encodings)」 → **uncle-bob**（共用 2 章）
- `clean-code` `naming/intention-revealing-names`「意圖揭露命名 (Intention-Revealing Names)」 → **uncle-bob**（共用 2 章）
- `clean-code` `naming/name-length-and-scope`「名稱長度與作用域 (Length & Scope)」 → **uncle-bob**（共用 2 章）
- `clean-code` `naming/one-word-per-concept`「一詞一概念與一致性 (Consistency)」 → **uncle-bob**（共用 2 章）
- `clean-code` `naming/parts-of-speech-and-context`「詞性與上下文 (Parts of Speech & Context)」 → **uncle-bob**（共用 2 章）
- `clean-code` `naming/problem-vs-solution-domain-names`「問題領域 vs 解決方案領域命名 (Problem vs Solution Domain Names)」 → **uncle-bob**（共用 2 章）
- `clean-code` `naming/pronounceable-and-searchable-names`「可朗誦與可搜尋的名字 (Pronounceable & Searchable Names)」 → **uncle-bob**（共用 2 章）
- `clean-code` `refactoring-moves/extract-function`「提取函式 (Extract Function)」 → **uncle-bob**（共用 1 章）
- `clean-code` `testing/tdd-red-green-refactor`「TDD 節奏：紅－綠－重構 (Red-Green-Refactor)」 → **kent-beck**（共用 1 章）
- `design-patterns` `paradigms/gof-in-functional`「GoF 模式的函數式形態」 → **uncle-bob**（共用 1 章）

</details>

## 套用

```bash
notes-core/tools/export-seealso-gaps.py --json > /tmp/seealso.json
notes-core/tools/apply-seealso.py /tmp/seealso.json            # 乾跑
notes-core/tools/apply-seealso.py /tmp/seealso.json --apply    # 寫入各站 frontmatter
```

寫入後各站 `npm run format`，抽幾站 build（strict 站的 `seeAlso.site` 走 siteKeys enum，拼錯 build 會紅），
`galaxy-checkup.py` 的 dead-seealso 必須維持 0。補完重跑本工具，該站就會從這裡消失。
