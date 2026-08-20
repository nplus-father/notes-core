# SERIES-STATUS — check → enrich → guide 系列帳本

**這份是什麼**：全星系「書收齊＋相關書都做完（content fill＋deep overview）」的站，推進
**check → enrich → guide** 產線的執行帳本。Andrew 固定在 notes-core 下執行本系列。
本檔手動維護：完成一站就在該行「導覽完成」欄填日期；體檢快照為 2026-08-20 唯讀掃描（範圍與方法見文末）。

**與其他 docs 的分工**：[GUIDE-QUEUE.md](./GUIDE-QUEUE.md)＝`/note-guide` 佇列正本（完成後搬「已完成」也記在那）；
[DEEPEN-READY.md](./DEEPEN-READY.md)＝每次重算的自動排序表；本檔＝**系列定義＋逐站體檢快照＋優先順序＋進度**。

## 系列判準（2026-08-20 對帳定案）

- **收書歸零**：bibliography `wanted = 0`（`unavailable`／`skipped` 不算欠）。
- **書端完工**：owned 全數 ① deep overview 品檢 PASS（`audit-overview.py`）② content fill 完成。
  content fill **以本機實測為準**——portal `health.json`（08-18 產）過期，21 本 08-19～20 剛填完的書被誤標 thin/near-empty。
  空葉章節 ≥2 的書算未完；恰 1 個空葉（多為附錄）不擋站、只註記；watch 級（8–15k 字）不擋。

**結果：65 站達標＝A 20（連導覽都完工）＋ B 45（本系列的工作範圍）**；10 站書端未過（其中 4 站導覽已寫、只欠書端補洞）。

## A 組——全流程完工（20 站，僅存查）

agile、behaviour-interview、clean-code、covey、design、greene、hbr、jung、keller、kent-beck、
leadership、navarro、peterson、philosophy、stott、taleb、thinking、tools、uncle-bob、writing

## B 組——體檢快照（45 站，2026-08-20 唯讀掃描，未蓋 `checkedAt`）

分檔依 note-guide 深度門檻（主題 ≥30 頁／人物 ≥15 頁）。「待寫」＝roadmap 已排、檔案未寫的節點（enrich 素材）。
「體檢」欄是本輪機械掃描的 findings 計數，細節在下面「逐站 findings」。

### ①站深料足——check 後可直接 guide，enrich 還導覽點名的債（15 站）

| 站 | 型 | owned | 頁 | 頁/書 | 溯源 | mastery | roadmap | 待寫 | 上次 check/enrich | 體檢 | 導覽完成 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| `data-systems-note` | 主題 | 19 | 50 | 2.63 | 100% | 13/13 | 100% | 0 | — | CLEAN |  |
| `economics-note` | 主題 | 50 | 45 | 0.90 | 100% | 6/6 | 84% | 0 | — | warning1·nit1 |  |
| `startup-note` | 主題 | 62 | 44 | 0.71 | 100% | 6/6 | 100% | 0 | — | CLEAN |  |
| `career-note` | 主題 | 68 | 43 | 0.63 | 98% | 6/6 | 100% | 0 | 08-06/08-06 | 必改1·nit1 |  |
| `investing-note` | 主題 | 62 | 43 | 0.69 | 100% | 6/6 | 100% | 0 | — | nit1 |  |
| `cloud-infra-note` | 主題 | 26 | 39 | 1.50 | 100% | 9/9 | 100% | 0 | — | CLEAN |  |
| `communication-note` | 主題 | 49 | 37 | 0.76 | 100% | 6/6 | 100% | 0 | 07-31/07-31 | nit1 |  |
| `learning-note` | 主題 | 33 | 34 | 1.03 | 100% | 6/6 | 82% | 0 | — | warning1·nit1 |  |
| `relationships-note` | 主題 | 46 | 34 | 0.74 | 100% | 6/6 | 91% | 0 | — | warning1 |  |
| `growth-note` | 主題 | 44 | 33 | 0.75 | 100% | 6/6 | 91% | 0 | — | warning1 |  |
| `business-strategy-note` | 主題 | 50 | 31 | 0.62 | 100% | 6/6 | 100% | 0 | — | nit2 |  |
| `life-meaning-note` | 主題 | 39 | 31 | 0.79 | 100% | 6/6 | 90% | 0 | — | warning1·nit1 |  |
| `history-note` | 主題 | 34 | 30 | 0.88 | 100% | 6/6 | 100% | 0 | — | nit1 |  |
| `tracy-note` | 人物 | 36 | 25 | 0.69 | 100% | 4/4 | 100% | 0 | — | nit1 |  |
| `wan-weigang-note` | 人物 | 11 | 15 | 1.36 | 100% | 4/4 | 100% | 0 | — | CLEAN |  |

### ②可 guide，導讀章「待挖」比例會偏高（14 站）

| 站 | 型 | owned | 頁 | 頁/書 | 溯源 | mastery | roadmap | 待寫 | 上次 check/enrich | 體檢 | 導覽完成 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| `habits-note` | 主題 | 44 | 28 | 0.64 | 100% | 6/6 | 100% | 0 | — | nit1 |  |
| `marketing-note` | 主題 | 31 | 27 | 0.87 | 100% | 6/6 | 100% | 0 | — | nit1 |  |
| `management-note` | 主題 | 47 | 20 | 0.43 | 100% | 4/4 | 100% | 0 | 08-01/08-01 | nit1 |  |
| `problem-solving-note` | 主題 | 26 | 17 | 0.65 | 100% | 4/4 | 100% | 0 | 08-06/08-06 | CLEAN |  |
| `science-note` | 主題 | 48 | 16 | 0.33 | 100% | 4/4 | 100% | 0 | 07-31/07-31 | nit1 |  |
| `drucker-note` | 人物 | 19 | 14 | 0.74 | 100% | 4/4 | 100% | 0 | — | CLEAN |  |
| `image-style-note` | 主題 | 7 | 13 | 1.86 | 100% | 4/4 | 100% | 0 | — | nit1 |  |
| `de-botton-note` | 人物 | 12 | 12 | 1.00 | 100% | 4/4 | 100% | 0 | — | blocker1·nit1 |  |
| `maxwell-note` | 人物 | 18 | 12 | 0.67 | 100% | 3/3 | 100% | 0 | — | nit1 |  |
| `kiyosaki-note` | 人物 | 23 | 11 | 0.48 | 100% | 3/3 | 100% | 0 | 08-06/08-06 | CLEAN |  |
| `liurun-note` | 人物 | 12 | 11 | 0.92 | 100% | 4/4 | 100% | 1 | — | nit1 |  |
| `wellness-note` | 主題 | 33 | 11 | 0.33 | 100% | 4/4 | 100% | 0 | 07-31/07-31 | CLEAN |  |
| `fromm-note` | 人物 | 16 | 10 | 0.62 | 100% | 3/3 | 100% | 0 | — | nit1 |  |
| `newport-note` | 人物 | 8 | 10 | 1.25 | 100% | 4/4 | 100% | 0 | — | 必改1·nit1 |  |

### ③太薄——check → enrich 拓站 → guide（16 站，jung／kent-beck／taleb 模式）

| 站 | 型 | owned | 頁 | 頁/書 | 溯源 | mastery | roadmap | 待寫 | 上次 check/enrich | 體檢 | 導覽完成 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| `cloud-note` | 人物 | 13 | 9 | 0.69 | 100% | 3/3 | 100% | 0 | — | nit1 |  |
| `bogle-note` | 人物 | 6 | 8 | 1.33 | 100% | 2/2 | 100% | 0 | — | nit1 |  |
| `fengtang-note` | 人物 | 10 | 8 | 0.80 | 100% | 3/3 | 100% | 1 | — | CLEAN |  |
| `gardner-note` | 人物 | 13 | 8 | 0.62 | 100% | 3/3 | 100% | 0 | — | CLEAN |  |
| `nouwen-note` | 人物 | 16 | 8 | 0.50 | 100% | 3/3 | 100% | 4 | — | nit1 |  |
| `damodaran-note` | 人物 | 5 | 7 | 1.40 | 100% | 2/2 | 100% | 0 | — | CLEAN |  |
| `nt-wright-note` | 人物 | 11 | 7 | 0.64 | 100% | 3/3 | 100% | 0 | — | nit1 |  |
| `templar-note` | 人物 | 9 | 7 | 0.78 | 100% | 4/4 | 100% | 0 | — | nit1 |  |
| `willard-note` | 人物 | 8 | 7 | 0.88 | 100% | 3/3 | 100% | 2 | — | CLEAN |  |
| `pastoral-psychology-note` | 主題 | 5 | 5 | 1.00 | 0% | 4/4 | 0% | 0 | — | 必改2·warning1·nit1 |  |
| `christensen-note` | 人物 | 9 | 4 | 0.44 | 100% | 4/4 | 100% | 6 | — | nit1 |  |
| `security-note` | 主題 | 14 | 4 | 0.29 | 100% | 4/4 | 100% | 8 | — | nit1 |  |
| `collins-note` | 人物 | 6 | 3 | 0.50 | 100% | 3/3 | 100% | 7 | — | CLEAN |  |
| `grant-note` | 人物 | 5 | 3 | 0.60 | 100% | 3/3 | 100% | 6 | — | CLEAN |  |
| `grove-note` | 人物 | 5 | 3 | 0.60 | 100% | 3/3 | 100% | 6 | — | CLEAN |  |
| `fowler-note` | 人物 | 6 | 2 | 0.33 | 100% | 2/2 | 100% | 4 | — | CLEAN |  |

## 書端未過、也還沒導覽的 6 站（站側體檢一併做完，等書端清帳後入列）

| 站 | 型 | 頁 | 站側體檢 | 卡在哪（書端） | 清帳後入檔 |
| --- | --- | ---: | --- | --- | --- |
| `biblical-studies-note` | 主題 | 44 | nit1 | wanted 1（Goldingay《OT Theology》卷一，三卷齊才結案）；`dictionary-of-paul-and-his-letters` 448 條目空 227（辭典型，是否 waive 待裁決） | ① |
| `theology-note` | 主題 | 24 | nit1 | `christian-theology-introduction`（new-books，內容已滿 21/21）＋`contemplative-pastor`、`reformed-dogmatics`（tmp）3 本待深度概覽；`cost-of-discipleship` 空 9/34 章 | ② |
| `personal-finance-note` | 主題 | 29 | CLEAN | `automatic-millionaire`（tmp，內容已滿）待深度概覽 | ② |
| `spiritual-formation-note` | 主題 | 13 | CLEAN | `cost-of-discipleship` 空 9/34 章；`weight-of-glory` 空 3/14 章 | ② |
| `schwager-note` | 人物 | 12 | 必改1·blocker1 | `new-market-wizards` 7 篇訪談章全空 | ② |
| `wujun-note` | 人物 | 10 | nit1 | `on-top-of-tides` 空 5/24 章 | ② |

> 另 4 站書端未過但**導覽已寫**：design-patterns（`microservices-patterns` 空 7 章）、lewis（`weight-of-glory` 空 3 章）、
> peck（`further-along-the-road-less-traveled` 僅 954 字、無概覽、躺在 `archive/`；`world-waiting-to-be-born` 空 2 章）、
> system-design（`building-microservices` 空 3 章＋`microservices-patterns`）。只欠書端補洞，不佔本系列產能。

## 必改帳（進場前就能清，幾乎零 token）

1. **schwager-note**：bibliography slug `complete-guide-to-futures-market` → 實際 repo 是 `complete-guide-to-futures-markets`（少個 s）；
   同一錯 slug 也出現在 4 筆 `furtherReading`（options-and-spreads ×2、risk-management、technical-analysis）——站上這些引用現在是 404。
2. **de-botton-note**：bibliography slug `status-anxiety-book` → 實際 repo 是 `status-anxiety`（頁面的 furtherReading 是對的，只有書單錯）。
3. **newport-note**：`career-capital/career-capital-over-passion` 的 anchor `how-to-be-a-high-school-superstar/docs/04-personal-growth` 不存在
   （該 repo 即 2026-08-06 的身分錯配書，實為《How to Win at College》）——回書 repo 對實際章節重掛。
4. **career-note**：`meaning-direction/beyond-the-business-card` 未溯源——回原文核對後補 anchor（必改不是選改）。

（pastoral-psychology 的 5 頁全未溯源＋3 本引用書不存在＝enrich 級工程，不算小帳，見 ③檔。）

## 逐站 findings（唯讀掃描；nit 級只記數量，進場時由 `--fix` 機械清）

- **economics-note**
  - warning: roadmap 孤兒頁 ×7: econ-foundations/inflation-and-deflation, econ-foundations/schools-of-economic-thought, econ-foundations/gdp-and-economic-indicators, globalization-order/globalization-and-trade, markets-incentives/game-theory-basics, markets-incentives/creative-destruction, money-central-banks/gold-standard-and-fetters
  - nit:related 單向 ×12（`--fix` 可機械清）
- **career-note**
  - 必改: 未溯源頁 ×1: meaning-direction/beyond-the-business-card
  - nit:related 單向 ×18（`--fix` 可機械清）
- **investing-note**
  - nit:related 單向 ×9（`--fix` 可機械清）
- **communication-note**
  - nit:related 單向 ×17（`--fix` 可機械清）
- **learning-note**
  - warning: roadmap 孤兒頁 ×6: memory/memory-techniques, metacognition/growth-mindset, practice/desirable-difficulty, practice/value-and-target, reading/deconstruct-a-book, reading/purposeful-reading
  - nit:related 單向 ×33（`--fix` 可機械清）
- **relationships-note**
  - warning: roadmap 孤兒頁 ×3: connection/reading-people-accurately, connection/empathy-as-skill, connection/rapport-vs-report
- **growth-note**
  - warning: roadmap 孤兒頁 ×3: deliberate-practice/path-to-mastery, growth-mindset/goal-pursuit-science, originals-potential/originals
- **business-strategy-note**
  - nit:related 單向 ×14（`--fix` 可機械清）
  - nit:頁尾缺 :::response ×1（`--fix` 可機械清）
- **life-meaning-note**
  - warning: roadmap 孤兒頁 ×3: emotion/hopeful-skepticism, emotion/objectivity-illusion, mental-health/self-compassion
  - nit:related 單向 ×7（`--fix` 可機械清）
- **history-note**
  - nit:related 單向 ×3（`--fix` 可機械清）
- **tracy-note**
  - nit:related 單向 ×5（`--fix` 可機械清）
- **habits-note**
  - nit:related 單向 ×1（`--fix` 可機械清）
- **marketing-note**
  - nit:related 單向 ×8（`--fix` 可機械清）
- **management-note**
  - nit:related 單向 ×16（`--fix` 可機械清）
- **science-note**
  - nit:related 單向 ×11（`--fix` 可機械清）
- **image-style-note**
  - nit:related 單向 ×14（`--fix` 可機械清）
- **de-botton-note**
  - blocker: bibliography owned slug 對不到書 repo: ['status-anxiety-book']
  - nit:related 單向 ×4（`--fix` 可機械清）
- **maxwell-note**
  - nit:related 單向 ×11（`--fix` 可機械清）
- **liurun-note**
  - nit:related 單向 ×1（`--fix` 可機械清）
- **fromm-note**
  - nit:related 單向 ×5（`--fix` 可機械清）
- **newport-note**
  - 必改: anchor 死連 ×1: career-capital/career-capital-over-passion→how-to-be-a-high-school-superstar/docs/04-personal-growth
  - nit:related 單向 ×3（`--fix` 可機械清）
- **cloud-note**
  - nit:related 單向 ×6（`--fix` 可機械清）
- **bogle-note**
  - nit:related 單向 ×3（`--fix` 可機械清）
- **nouwen-note**
  - nit:related 單向 ×5（`--fix` 可機械清）
- **nt-wright-note**
  - nit:related 單向 ×4（`--fix` 可機械清）
- **templar-note**
  - nit:related 單向 ×4（`--fix` 可機械清）
- **pastoral-psychology-note**
  - 必改: 未溯源頁 ×5: inner-life/shame-vs-guilt, integration/five-views, integration/ministerial-not-magisterial, ministry-practice/forgiveness-two-kinds, trauma-grief/trauma-informed-reading
  - 必改: furtherReading book 不存在 ×3: integration/five-views→psychology-and-christianity-five-views, ministry-practice/forgiveness-two-kinds→forgiveness-and-reconciling, trauma-grief/trauma-informed-reading→suffering-and-the-heart-of-god
  - warning: 無 roadmap 的分類 ×4: inner-life, integration, ministry-practice, trauma-grief
  - nit:related 單向 ×1（`--fix` 可機械清）
- **christensen-note**
  - nit:related 單向 ×2（`--fix` 可機械清）
- **security-note**
  - nit:related 單向 ×1（`--fix` 可機械清）
- **biblical-studies-note**
  - nit:related 單向 ×21（`--fix` 可機械清）
- **theology-note**
  - nit:related 單向 ×11（`--fix` 可機械清）
- **schwager-note**
  - blocker: bibliography owned slug 對不到書 repo: ['complete-guide-to-futures-market']
  - 必改: furtherReading book 不存在 ×4: analysis/options-and-spreads→complete-guide-to-futures-market, analysis/options-and-spreads→complete-guide-to-futures-market, analysis/risk-management→complete-guide-to-futures-market, analysis/technical-analysis→complete-guide-to-futures-market
- **wujun-note**
  - nit:related 單向 ×9（`--fix` 可機械清）

CLEAN（18 站）：data-systems、startup、cloud-infra、problem-solving、wan-weigang、drucker、kiyosaki、wellness、
fengtang、gardner、damodaran、willard、christensen、collins、grant、grove、fowler、personal-finance、spiritual-formation。

## 推進流程設計（2026-08-20 定案）

**check 的機械半已集中做完（就是本檔快照），不再逐站單跑一次完整 `/note-check`**；認站、學語氣、
§1.3 該挖分層這些 LLM 級前置，由 guide／enrich 代理進場時自然吸收——它們本來就要讀全站與 owned books，
單獨先跑一輪 check 等於同一筆閱讀花兩次錢。分四種批型：

0. **清帳輪（先做，幾乎零 token）**：上面必改 4 筆，各站單獨 commit。nit 級（related 單向等）**不**集中清——
   進站的代理順手 `--fix` 蓋 `checkedAt` 即可，省得一輪碰 27 個 repo。
1. **厚站波（①檔 → ②檔，表內由上而下）**：照 08-15 驗證的量產模式——
   **一站一代理跑完整 `/note-guide` → enrich 波還導覽點名的債 → 主代理獨立驗收**
   （anchor `[-d]` 逐一驗、dist 連結、具名事實 grep 防杜撰、`git status` 全清、pin＋lockfile 同 bump）後 commit＋push。
   一波 3–5 站、以額度為界，斷點用 SendMessage 續跑。
   蓋章紀律：guide 蓋 `writtenAt`、enrich 蓋 `enrichedAt`、`--fix` 蓋 `checkedAt`。
2. **薄站一條龍（③檔）**：單站 `note-check --enrich` 拓站鋪思想弧線 → 接力 `/note-guide` 直接沿用
   （jung 3→14 頁／kent-beck／taleb 驗證過）。**pastoral-psychology 先還溯源債**（5 頁回原文改寫＋3 本書單修正）再談導覽。
3. **書端另一條線（不佔 note 產能，可平行）**：`books-done/tmp/` 下跑 `/book-generate-deep-overview`（3 本，做完自動歸檔）
   ＋ `/book-promote-to-tmp` 收 `christian-theology-introduction`；空章書逐本補寫。
   清一站的帳就依上表「清帳後入檔」欄把該站放進對應檔次。

完成一站：本檔該行「導覽完成」欄填日期，GUIDE-QUEUE 同步搬「已完成」。

## 跨站遺留帳

- [GUIDE-QUEUE.md](./GUIDE-QUEUE.md) 有 12 站已達標未登錄：data-systems、career、investing、cloud-infra、habits、marketing、
  science、drucker、wellness、cloud、gardner、security——下次動它時一併補。
- portal `health.json`（08-18）過期：21 本剛填完的書仍標 thin/near-empty，書站部署後重跑 fetch-health。
- `archive/further-along-the-road-less-traveled`：躺在 archive/ 但 GitHub repo 未 archive、topics 照舊——除役還是補寫，待裁決。
- `dictionary-of-paul-and-his-letters`：448 條目空 227（辭典型參考書）——是否 waive 待裁決。
- 恰 1 空葉的書（不擋站、記帳）：four-loves（附錄）、lessons-of-history（ch3）、time-management、hearing-god、
  boundaries-in-dating、encounters-with-jesus 等 20 本，多為附錄或單章，逐站進場時順手判定補或放。

## 本輪掃描做了什麼／沒做什麼（2026-08-20）

**做了（note-check 可腳本化的部分，51 站）**：§1.1 五指標；§1.2 雙向溯源（頁無 anchor＋anchor 對 books-done 實檔驗證＋
furtherReading book slug 存在）；§2 結構——首頁契約檔、divergence 掃描、notes-core pin（51 站全 v0.36.0）、分類 `_index.md`
與 name/icon/order、roadmap↔內容（孤兒頁／待寫節點）、mastery slug 有效性、label 分隔號、related 存在＋雙向、seeAlso 實檔、
importance/status 值域、跳脫實體、`:::response` 存在。

**沒做（進場逐站補）**：學語氣、§1.3 該挖而未挖分層、§3 backlog 撰寫、§2.5 抽驗防杜撰、§2.8 build/format/lint。
所以本輪**不蓋 `checkedAt`**——蓋章留給進站跑完整 `/note-check` 的那次。

**重跑方式**：掃描是一次性腳本（session scratchpad），不入 repo；要刷新就再請 Claude 依本節「做了」的清單重掃、更新本檔。
