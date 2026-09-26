# 出版年跨站矛盾（同一本書、兩個年份）

> **生成於 2026-09-26T14:37:18+08:00**｜由 `tools/export-year-conflicts.py` 產生，**不要手改**——改資料源再重跑。

**這份是什麼**：全星系 bibliography 的**跨站**一致性檢查。既有四份盤點都是一站之內的視角，答不出「這一格填的跟隔壁站不一樣」——而一本書被多站收錄是常態，所以填錯永遠不會被抓，只有沒填會。`year` 是首頁年代分佈圖的軸，兩站對同一本書填不同年，圖上就會落在不同年代。

**工具不替人判**：矛盾至少有兩種，處理方式相反——(1) **初版 vs 改版**，schema 要初版年，但不能無腦取小（有些早年份指的是同名錄音課程，書晚很多年才出）；(2) **系列列 vs 單卷列**，一個 slug 被當成一整套書的代表列，兩邊都對、不是債。下面把 title 一起列出來，就是為了讓第二種一眼看得出來。

## 摘要

| 檢查 | 數 | 後果 |
| --- | ---: | --- |
| 有 slug 的條目 | 2358 | — |
| **跨站 year 矛盾** | **1** | 同一本書在年代圖上出現在兩個年代 |
| 缺 year、但別站已填 | **0** | 零判斷可補（直接抄，不必查書） |
| **slug 撞號嫌疑** | **1** | 兩站可能指到不同的書，封面與連結全指錯 |
| `original` 語言不一致 | **0** | 原文書名欄填了譯名 |
| **year 晚於書 repo 的 published** | **2** | 填的是某個改版年，不是初版年 |

## 一、跨站矛盾：1 本

每組列出各年份及主張它的站；`title` 不同時多半是「系列列 vs 單卷列」，不是債。

### `hbr-guide-to-better-recruiting-and-hiring`

- **2023** — hr-note（HBR Guide to Better Recruiting and Hiring 精準招募與聘用指南）
- **2024** — hbr-note（HBR Guide to Better Recruiting and Hiring）、leadership-note（哈佛商業評論：精準招募與聘用指南）

## 二、缺 year、別站有現成答案：0 筆

無。

## 三、slug 撞號嫌疑：1 本

同一個 `slug` 在不同站被填成不同作者（**姓氏鍵**不同）。這是最嚴重的一類——多半代表兩站其實指到**不同的書**，而封面與延伸連結會全部指錯。

- `alliance`：「Reid Hoffman、Ben Casnocha & Chris Yeh」（career-note）；「Reid Hoffman, Ben Casnocha & Chris Yeh」（hr-note）

## 四、`original` 語言不一致：0 本

無。

## 五、`year` 晚於書 repo 的 `published`：2 本

書 repo 的 `_index.md` frontmatter 有 `published` 欄位（1777 本 **100% 都有**），是做摘要時手上那一版的出版日。**我們的 `year` 晚於它就必錯**——初版年不可能晚於一個已經存在的印次，代表這格填的是某次改版的年份。

**但 `published` 也不是初版年**（High Performance MySQL 標的是第 3 版 2012、Release It! 標的是第 2 版 2017），所以**不能直接抄過來**——要查真初版。反向也有假陽性：`published` 偶爾是預告上架年而早於實際出版（HBR 那批），查證後把 slug 加進 `SETTLED_AGAINST_PUBLISHED` 就不會再報。

| slug | 書名 | 我們填的 | repo published |
| --- | --- | ---: | ---: |
| `fengtang-succeeding-method` | 馮唐成事心法 | 2021 | 2020 |
| `tourism-marketing` | Tourism Marketing: A Collaborative Approach | 2005 | 2004 |

## 已知例外（不報進上面各節）：1 本

同一個 slug 被一站當「整套書的代表列」、另一站當「單卷」用，於是 `year` 與 `original` 天生不一致，而**兩邊都對**。清單寫在 `export-year-conflicts.py` 的 `KNOWN_SERIES_ROWS`；要加新的，先確認它是這一類——「初版 vs 改版」不屬於此。

- `message-of-romans`

## 重跑

```bash
notes-core/tools/export-year-conflicts.py
```

補完之後重跑，該筆就會從這裡消失。與 [MISSING-YEARS.md](./MISSING-YEARS.md) 的分工：那份問「空不空」，這份問「一不一致」。
