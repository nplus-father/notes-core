# 人文／人生 note 星系 → 站別「納入 repo」範圍界定（草稿）

> 2026-07-02 以 `books-management/books-done/` 實際資料夾盤點產生。
> 界定單位＝ **leaf-topic 資料夾**（`domain/category/leaf-topic/`）。
> 一個 note 站納入 = 該資料夾底下全部單書 repo。細節（哪本書進哪個 concept）留待各站 repo 內個別規劃。
> 對應正本規劃：[[humanities-books-by-domain]]（`notes/humanities-books-by-domain.md`）。

## 結構事實

`books-done/<domain>/<category>/<leaf-topic>/<單書-repo>` —— 四層。
90 個 leaf-topic 資料夾，底下共約 1385 個單書 repo。leaf-topic 才是規劃「納入」的自然顆粒。

---

## 已建站

### `writing-note` ✅ 已上線
- `craft/writing/fiction` (6)、`craft/writing/non-fiction` (19)、`craft/writing/screenwriting` (1) — 共 26 本

---

## 待建 13 站 → 納入 leaf-topic（含實際藏書量）

### 財經（3 站，最大宗）
- **`investing-note`** — `professional/finance/investing` (120)
- **`personal-finance-note`** — `professional/finance/personal-finance` (11)、`professional/finance/real-estate` (5) — 共 16
  - ⚠️ 大量理財書（richest-man-in-babylon、simple-path-to-wealth、i-will-teach-you…）目前物理位置在 `investing/` 底下，跨站引用時再處理
- **`economics-note`** — `professional/finance/economics` (26)、`wisdom/finance/economics` (2) — 共 28

### 哲學（1 站）
- **`philosophy-note`** — `wisdom/philosophy/ethics` (68)、`wisdom/philosophy/political-philosophy` (5)、`wisdom/philosophy/stoicism` (4)、`wisdom/philosophy/eastern` (2)、`personal/mindset/stoicism` (2) — 共 81

### 創業／商業（2 站）
- **`startup-note`** — `professional/business/startup` (34)
- **`business-strategy-note`** — `professional/business/strategy` (32)、`professional/business/marketing` (19)、`professional/business/management` (15)、`professional/business/sales` (5)、`professional/business/operations` (1) — 共 72
  - ⚠️ marketing 19 本，量足可獨立成 `marketing-note`

### 工作（3 站）
- **`career-note`** — `professional/career/skill-building` (43)、`professional/career/job-search` (5)、`professional/career/career-change` (1)、`personal/career/skill-building` (2) — 共 51
- **`leadership-note`** — `professional/leadership/vision` (35)、`professional/leadership/team-building` (13)、`professional/leadership/culture` (8)、`professional/leadership/coaching` (5)、`professional/leadership/decision-making` (8) — 共 69
  - ⚠️ decision-making (8) 可改歸 `thinking-note`
- **`communication-note`** — `professional/communication/persuasion` (70)、`professional/communication/negotiation` (16)、`professional/communication/public-speaking` (13)、`professional/communication/storytelling` (10) — 共 109

### 人生智慧（4 站）
- **`thinking-note`** — `wisdom/science/cognitive` (23)、`personal/science/cognitive` (2)（+ 可選 `professional/leadership/decision-making` 8）— 25～33
- **`habits-note`** — `personal/habit/productivity` (34)、`personal/habit/routine` (4)、`personal/habit/discipline` (3)、`personal/habit/focus` (1) — 共 42
- **`growth-note`** — `personal/mindset/growth` (101)、`wisdom/mindset/growth` (5)、`personal/mindset/self-awareness` (5)、`professional/mindset/growth` (3) — 共 114
  - ⚠️ growth 101 本為單一 leaf 最大宗，可能需再拆子主題
- **`life-meaning-note`** — `personal/mindset/emotion` (10)、`personal/mindset/resilience` (6)、`wisdom/mindset/emotion` (1)、`personal/relationships/community` (31)、`personal/relationships/dating` (11)、`personal/relationships/marriage` (5)、`personal/relationships/parenting` (5)、`personal/relationships/friendship` (2)、`professional/relationships/community` (6)、`personal/wellness/mental-health` (12) — 共 89
  - ⚠️ relationships 合計 60 本，量足可獨立成 `relationships-note`

---

## ⚠️ 缺口：books-done 有實際藏書，但 14 站規劃未涵蓋

盤點暴露原 md 沒安置的實際 done 藏書：

| 未安置類別 | leaf-topic（藏書量） | 建議 |
|---|---|---|
| **歷史** 42 本 | history/civilization(23)、modern(8)、cultural(6)、military(3)、ancient(2) | 缺 `history-note`；或部分史料歸 economics/philosophy |
| **學習方法** 28 本 | education/self-learning：wisdom(24)、personal(2)、professional(2) | 缺 `learning-note`；或併入 growth/career |
| **健康養生** ~13 本 | wellness：mental-health(12→已歸 life)、nutrition(6)、fitness(3)、sleep(3)、aging(1) | 缺 `wellness-note`；或併入 life-meaning |
| **科普** ~12 本 | science：pharmacology(7)、cosmology(2)、physics(2)、evolution(1)（cognitive→thinking） | 缺 `science-note`；量偏少，可暫緩 |

## 非本星系（不納入人文 14 站）

- **faith/** 218 本（biblical-studies 107、systematic 76、pastoral 10…）— 信仰星系，另由靈修／podcast 流程處理
- **craft/engineering・craft/tools・craft/design** — 技術星系（clean-code / system-design 等，見 `notes/books-by-domain.md`）

---

## 定案（2026-07-02）

### 最終站別：18 站（已建 1 + 待建 17）

已建：`writing-note` ✅

| 群 | 站 | 納入主軸 leaf（藏書） |
|---|---|---|
| 財經 | `investing-note` | investing (120) |
| 財經 | `personal-finance-note` | personal-finance (11)、real-estate (5) |
| 財經 | `economics-note` | economics (26+2) |
| 哲學 | `philosophy-note` | ethics (68)、political-philosophy (5)、stoicism (4+2)、eastern (2) |
| 創業商業 | `startup-note` | startup (34) |
| 創業商業 | `business-strategy-note` | strategy (32)、management (15)、sales (5)、operations (1) |
| 創業商業 | `marketing-note` 🆕拆 | marketing (19) |
| 工作 | `career-note` | career/skill-building (43+2)、job-search (5)、career-change (1) |
| 工作 | `leadership-note` | vision (35)、team-building (13)、culture (8)、coaching (5)、decision-making (8) |
| 工作 | `communication-note` | persuasion (70)、negotiation (16)、public-speaking (13)、storytelling (10) |
| 人生智慧 | `thinking-note` | cognitive (23+2) |
| 人生智慧 | `habits-note` | productivity (34)、routine (4)、discipline (3)、focus (1) |
| 人生智慧 | `growth-note` | mindset/growth (101+5+3)、self-awareness (5) |
| 人生智慧 | `life-meaning-note` | mindset/emotion (10+1)、resilience (6)、wellness/*(13) |
| 人生智慧 | `relationships-note` 🆕拆 | relationships/*(60) |
| 新增 | `history-note` 🆕補 | history/*(42) |
| 新增 | `learning-note` 🆕補 | education/self-learning (28) |

**併入 / 暫緩**：wellness → `life-meaning-note`；science 科普(~12) 量少暫緩（cognitive 已歸 thinking）。
**站內再拆**：growth(114)、investing(120)、communication(109) 為超大站，子主題切分留待各站 repo 內規劃。

### 建站順序

**首批 5 站**（Claude 決定，一次開齊後統一 `note-enrich` 充實）：

1. `startup-note` — business/startup (34)
2. `habits-note` — habit/productivity+routine+discipline+focus (42)
3. `thinking-note` — science/cognitive (25)
4. `personal-finance-note` — finance/personal-finance+real-estate (16)
5. `marketing-note` — business/marketing (19)

選站原則：規模適中(16–42)、主題超內聚、經典書密度高、分散 5 群以驗證流程；避開超大站(investing 120 / communication 109 / growth 114)。
流程：`note-new-station` 逐站建 → 建好後逐站 `note-enrich`（以 owned books 為源充實）。`startup-note` 先跑通格式，其餘照辦。
