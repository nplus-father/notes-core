# 出版年跨站矛盾（同一本書、兩個年份）

> **生成於 2026-08-26T19:20:21+08:00**｜由 `tools/export-year-conflicts.py` 產生，**不要手改**——改資料源再重跑。

**這份是什麼**：全星系 bibliography 的**跨站**一致性檢查。既有四份盤點都是一站之內的視角，答不出「這一格填的跟隔壁站不一樣」——而一本書被多站收錄是常態，所以填錯永遠不會被抓，只有沒填會。`year` 是首頁年代分佈圖的軸，兩站對同一本書填不同年，圖上就會落在不同年代。

**工具不替人判**：矛盾至少有兩種，處理方式相反——(1) **初版 vs 改版**，schema 要初版年，但不能無腦取小（有些早年份指的是同名錄音課程，書晚很多年才出）；(2) **系列列 vs 單卷列**，一個 slug 被當成一整套書的代表列，兩邊都對、不是債。下面把 title 一起列出來，就是為了讓第二種一眼看得出來。

## 摘要

| 檢查 | 數 | 後果 |
| --- | ---: | --- |
| 有 slug 的條目 | 1925 | — |
| **跨站 year 矛盾** | **13** | 同一本書在年代圖上出現在兩個年代 |
| 缺 year、但別站已填 | **1** | 零判斷可補（直接抄，不必查書） |
| **slug 撞號嫌疑** | **0** | 兩站可能指到不同的書，封面與連結全指錯 |
| `original` 語言不一致 | **0** | 原文書名欄填了譯名 |

## 一、跨站矛盾：13 本

每組列出各年份及主張它的站；`title` 不同時多半是「系列列 vs 單卷列」，不是債。

### `hbr-guide-to-better-recruiting-and-hiring`

- **2024** — hbr-note（HBR Guide to Better Recruiting and Hiring）
- **2025** — leadership-note（哈佛商業評論：精準招募與聘用指南）

### `investment-valuation`

- **1994** — damodaran-note（投資估價）
- **1995** — investing-note（Investment Valuation）

### `just-shut-up-and-do-it`

- **2015** — tracy-note（Just Shut Up and Do It）
- **2016** — tools-note（Just Shut Up and Do It）

### `liurun-power-of-evolution`

- **2021** — liurun-note（進化的力量）
- **2022** — science-note（進化的力量）

### `mckinsey-elite-reading-method`

- **2015** — learning-note（麥肯錫精英高效閱讀法）
- **2018** — problem-solving-note（麥肯錫精英高效閱讀法）

### `mckinsey-note-taking-method`

- **2015** — problem-solving-note（麥肯錫的筆記術）
- **2016** — tools-note（麥肯錫的筆記術）

### `mckinsey-problem-solving`

- **2012** — problem-solving-note（麥肯錫問題分析與解決技巧）
- **2014** — business-strategy-note（麥肯錫問題分析與解決技巧）

### `psychology-of-selling`

- **1985** — business-strategy-note（The Psychology of Selling 銷售心理學）
- **2004** — tracy-note（銷售心理學）

### `selfless-way-of-christ`

- **1981** — nouwen-note（向下的移動）
- **2007** — spiritual-formation-note（The Selfless Way of Christ）

### `soft-skills-thirty-letters`

- **2014** — behaviour-interview-note（軟技能：soft skills，讓你不過時、不貶值、不消失）、career-note（軟技能：soft skills，讓你不過時、不貶值、不消失）
- **2021** — wujun-note（軟技能（多人合著））

### `time-management`

- **2013** — tools-note（Time Management 時間管理）
- **2014** — tracy-note（時間管理21項關鍵）

### `wan-weigang-scientific-thinker`

- **2020** — science-note（科學思考者）
- **2021** — wan-weigang-note（科學思考者）

### `wan-weigang-what-is-relativity`

- **2020** — wan-weigang-note（高手相對論）
- **2021** — science-note（高手相對論）

## 二、缺 year、別站有現成答案：1 筆

這批不必查書：同一個 slug 別站已經填了。**來源本身也在第一節出現的先別抄**——那表示答案自己就有兩個版本。

| 缺的站 | slug | 書名 | 別站填的 |
| --- | --- | --- | --- |
| `thinking-note` | `wan-weigang-scientific-thinker` | 萬維鋼《科學思考者》 | 2020（science-note）；2021（wan-weigang-note） ⚠︎ 來源自身矛盾 |

## 三、slug 撞號嫌疑：0 本

無——被多站收錄的書，作者姓氏鍵都一致。

## 四、`original` 語言不一致：0 本

無。

## 已知例外（不報進上面各節）：1 本

同一個 slug 被一站當「整套書的代表列」、另一站當「單卷」用，於是 `year` 與 `original` 天生不一致，而**兩邊都對**。清單寫在 `export-year-conflicts.py` 的 `KNOWN_SERIES_ROWS`；要加新的，先確認它是這一類——「初版 vs 改版」不屬於此。

- `message-of-romans`

## 重跑

```bash
notes-core/tools/export-year-conflicts.py
```

補完之後重跑，該筆就會從這裡消失。與 [MISSING-YEARS.md](./MISSING-YEARS.md) 的分工：那份問「空不空」，這份問「一不一致」。
