# 跨站連結缺口（同書同章、卻沒有互相 seeAlso）

> **生成於 2026-11-06T13:16:25+08:00**｜由 `tools/export-seealso-gaps.py` 產生，**不要手改**——改資料源再重跑。

**這份是什麼**：兩個站的概念頁掛了**同一本書的同一章**，來源頁卻沒有任何 `seeAlso` 指到對方那一站。
由 `notes-core/tools/export-seealso-gaps.py` 生成，**不要手改**——補各站的 seeAlso 再重跑。

**為什麼要補**：契約層全綠之後，星系最薄的是站與站之間。同一章同時撐著主題站的一頁與人物站的一頁，
讀者在任一邊都看不到另一邊——79 個站各自封閉，首頁 schools 卡的跨站門是唯一通道。
頁級的「Dive Deeper」就是為這件事存在的，它的使用率卻只有一成。

**判準只收 strong**：同書**同章**。同書不同章只列數字（weak），不開單——不同章可能講完全不同的事。

目前：2291 個概念頁，有 seeAlso 的 **624 頁（27%）**；一條跨站連結都沒有的站 **7**。
strong 缺口 **15 筆**（來源頁 10，分佈在 7 站）；全部補上後有 seeAlso 的頁變成 **634（28%）**。weak（同書不同章）另有 438 筆，只供參考。
另有 **2 筆被 schema 擋住**（strict 站指向非技術站，見下節）。

> [!NOTE]
> 目前零跨站連結的站：`gardner`、`image-style`、`kiyosaki`、`pastoral-psychology`、`personal-finance`、`security`、`wujun`

## 各站缺口（當來源）

缺越多排越前；缺 0 的站略去。軸別來自 sites.ts。

| 站 | 軸 | 缺口 | 主要去向 |
| --- | --- | ---: | --- |
| `tools` | topic | 5 | habits 2、career 1、covey 1、newport 1 |
| `philosophy` | topic | 3 | de-botton 1、fromm 1、science 1 |
| `theology` | topic | 2 | lewis 1、stott 1 |
| `thinking` | topic | 2 | jung 1、science 1 |
| `cloud-infra` | topic | 1 | system-design 1 |
| `data-systems` | topic | 1 | system-design 1 |
| `hbr` | topic | 1 | leadership 1 |

軸向：主題→人物 7、人物→主題 0、主題→主題 8、人物→人物 0。

## 逐筆清單

格式：來源頁 → 目標站：要掛的 path（label）。分類頁＝該分類 ≥3 頁同時命中，連分類不連單頁。

### cloud-infra（1 筆）

- `slos-error-budgets/control-or-context`「控制還是脈絡：未達可用性目標該凍結部署，還是把差距交給團隊自己改？」 → **system-design**：`concepts/observability/slo-sli-sla/`（SLI / SLO / SLA）

### data-systems（1 筆）

- `cqrs-eventsourcing/where-does-truth-live`「真相住在哪：資料庫是事實、log 是副產物，還是 log 是事實、狀態只是快取」 → **system-design**：`concepts/messaging/stream-processing/`（串流處理 (Stream Processing)）；`concepts/messaging/message-queue/`（訊息佇列 (Message Queue)）

### hbr（1 筆）

- `leadership-teams/is-feedback-a-fallacy`「回饋能不能拆成技術：結構化回饋對上回饋的謬誤」 → **leadership**：`concepts/coaching/feedback-that-lands/`（有效回饋：對事不對人，即時不等年度）

### philosophy（3 筆）

- `applied/should-we-want-consolation`「痛苦該被減輕，還是該被保留？de Botton 的藥櫃對尼采與卡繆」 → **de-botton**：`concepts/philosophy/consolations-of-philosophy/`（哲學的慰藉：六位哲人面對人生困境）；`concepts/status/solutions-to-status/`（五種解方：哲學、藝術、政治、宗教、波希米亞）
- `eastern/who-is-doing-the-letting-go`「誰在收心：做判斷的我，還是沒有執行長的心」 → **fromm**：`concepts/love-being/to-have-or-to-be/`（擁有還是存在：兩種生存模式）
- `eastern/who-is-doing-the-letting-go`「誰在收心：做判斷的我，還是沒有執行長的心」 → **science**：`concepts/mind-cognition/modular-mind-and-no-self/`（模組心智與無我：大腦裡沒有執行長）

### theology（2 筆）

- `apologetics/head-or-heart-apologetics`「護教該從論證還是從心出發？阿奎那、普蘭丁格對帕斯卡、路易斯、切斯特頓」 → **lewis**：`concepts/apologetics/mere-christianity/`（返璞歸真：從道德律到基督信仰）
- `doctrine/atonement-legal-or-participatory`「十架救贖的重音：法理、參與，還是神的受苦」 → **stott**：`concepts/foundations/cross-of-christ/`（基督的十架：福音的中心）

### thinking（2 筆）

- `consciousness/where-is-the-self`「自我在哪裡：沒有劇場、湧現的迴圈、腦幹的 SELF，還是自性？」 → **jung**：`concepts/life/confrontation-with-the-unconscious/`（與無意識的對峙）
- `consciousness/where-is-the-self`「自我在哪裡：沒有劇場、湧現的迴圈、腦幹的 SELF，還是自性？」 → **science**：`concepts/mind-cognition/strange-loops/`（怪圈：自我指涉如何湧現出意義）

### tools（5 筆）

- `habits/what-makes-a-habit-stick`「什麼讓一個習慣黏住：渴求、重複，還是情緒？」 → **career**：`concepts/grit-mastery/atomic-habits-identity/`（原子習慣：身分認同驅動的系統）；`concepts/manage-yourself/seven-habits-inside-out/`（與成功有約：由內而外的效能）
- `habits/what-makes-a-habit-stick`「什麼讓一個習慣黏住：渴求、重複，還是情緒？」 → **habits**：`concepts/systems-over-goals/one-percent-compounding/`（系統勝於目標：1% 的複利）
- `time-management/what-is-efficiency-for`「效率省下的時間該換什麼：外包、慢下來，還是接受做不完？」 → **covey**：`concepts/personal-victory/integrity-in-the-moment/`（抉擇時刻的正直：大石頭、焦點圈、問聽行）；`concepts/principles/live-love-learn-leave-a-legacy/`（生活、愛、學習、留下傳承：四項基本需要）
- `time-management/what-is-efficiency-for`「效率省下的時間該換什麼：外包、慢下來，還是接受做不完？」 → **habits**：`concepts/energy-routine/finitude-4000-weeks/`（承認有限：四千個禮拜）；`concepts/productivity/big-rocks-first/`（要事第一：先放大石頭）
- `time-management/what-is-efficiency-for`「效率省下的時間該換什麼：外包、慢下來，還是接受做不完？」 → **newport**：`concepts/slow-productivity/three-principles-of-slow-productivity/`（慢速生產力三原則：少做、自然節奏、品質執念）

## 被 schema 擋住的缺口（strict 站 → 非技術站）

技術站群的 `seeAlso.site` 走 `siteKeys` enum，目前只含技術站自己的 key。這些缺口**真實存在**
（同書同章），但寫進 frontmatter build 會紅。要放行得改 notes-core：讓 enum 涵蓋全部 79 個 key
（仍是封閉集合，拼錯照樣抓得到），升版後重跑本工具它們就會進決策 JSON。

| 來源站 | 目標站 | 筆數 |
| --- | --- | ---: |
| `clean-code` | `uncle-bob` | 1 |
| `design-patterns` | `uncle-bob` | 1 |

<details><summary>逐筆</summary>

- `clean-code` `complexity/small-functions-or-deep-modules`「小函式還是深模組：拆分讓讀者腦中要裝的東西變少，還是只是搬了家？」 → **uncle-bob**（共用 1 章）
- `design-patterns` `paradigms/patterns-vocabulary-or-patch`「模式是永恆語彙，還是語言缺陷的補丁：亞歷山大對上 Bob 大叔」 → **uncle-bob**（共用 1 章）

</details>

## 套用

```bash
notes-core/tools/export-seealso-gaps.py --json > /tmp/seealso.json
notes-core/tools/apply-seealso.py /tmp/seealso.json            # 乾跑
notes-core/tools/apply-seealso.py /tmp/seealso.json --apply    # 寫入各站 frontmatter
```

寫入後各站 `npm run format`，抽幾站 build（strict 站的 `seeAlso.site` 走 siteKeys enum，拼錯 build 會紅），
`galaxy-checkup.py` 的 dead-seealso 必須維持 0。補完重跑本工具，該站就會從這裡消失。
