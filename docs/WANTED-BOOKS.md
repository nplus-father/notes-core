# 待收書單（bibliography `wanted` 全星系匯出）

> **生成於 2026-11-15T10:50:07+08:00**｜由 `tools/export-wanted.py` 產生，**不要手改**——改資料源再重跑。

**這份是什麼**：各 note 站 `src/data/bibliography.ts` 裡標成 `status: "wanted"` 的書，
全部匯出成一張採購清單。書名以**英文原名**為主，中譯附在後面，並附**作者**——
同名不同書會讓人買錯（portal 上的 `servant-leadership` 是 Larry W. Boone 的教科書，
不是 Greenleaf 1977 原典），下單前請對作者。由
`notes-core/tools/export-wanted.py` 生成，**不要手改**——改各站的 bibliography 再重跑。

**已收錄比對的資料源**：GitHub 現況（`gh repo list` nplus-father／Andrewnplus，2010 個 repo）。

## 先收這 9 本

全星系的 wanted 只剩 9 筆，**這節就是全部**，順序即建議的採購與消化順序（薄的、起手容易的排前面）。**這節是全檔唯一的人工區塊**——要改請編 `export-wanted.py` 的 `TOP20`，不要改這裡。挑選準則依序：**①歸零槓桿——優先收「還差 1–2 本就收齊」的站所缺的書**（見下面「快歸零的站」那節，腳本自動算；站書單一歸零，缺書就不再是它進 `note-check --enrich` 深化的瓶頸） ②多站共等，收一本補多站 ③站主自己在 `note` 裡標了「最大／頭號缺口」 ④portal 驗證的 anchor 深度——nplus.wiki 上已經建成幾本回指它的書站（同作者書櫃、同一條線的衍生書），書櫃愈深、原典愈缺就排愈前面（見 [SOURCING-DEBT.md](./SOURCING-DEBT.md)） ⑤同等重要時，薄的、有繁中在版的排前面。

「站」欄的 `(n)` ＝**收了這本之後該站還剩幾本**；`(0)` 就是這一本收了該站即歸零。

「為何排這裡」的 portal 數字都是實查出來的（作者書櫃本數、同一條線的衍生書數、各站概念頁引用處數）；`/note-wanted` 每次重挑會一併重查。

| # | 英文書名 | 作者 | 中譯 | 年 | 站 | 為何排這裡 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **The Elements of Statistical Learning** | Trevor Hastie, Robert Tibshirani & Jerome Friedman |  | 2001 | data-science(8) | ISLP 2026-11-14 剛建站，ESL 是同一組作者（Hastie、Tibshirani）的數學完整版；線上免費，可先做站 |
| 2 | **The Hundred-Page Machine Learning Book** | Andriy Burkov |  | 2019 | data-science(8) | ML 基礎分類只剩它與 ESL；一百頁，最薄、最快消化 |
| 3 | **Statistical Rethinking** | Richard McElreath |  | 2020 | data-science(8) | 機率與貝氏分類剛建了 Blitzstein、Kurt 兩本入門，缺一本貝氏建模的進階課 |
| 4 | **Mastering 'Metrics** | Joshua D. Angrist & Jörn-Steffen Pischke |  | 2014 | data-science(8) | Causal Inference: The Mixtape 剛建站，這本是同一套五招（隨機、迴歸、IV、RDD、DiD）的平易版 |
| 5 | **Bernoulli's Fallacy** | Aubrey Clayton |  | 2021 | data-science(8) | Signal and the Noise 第 8 章那場頻率派 vs 貝氏論戰的整本版；Taleb 書櫃已 7 本，同一條機率哲學線 |
| 6 | **Competing on Analytics** | Thomas H. Davenport & Jeanne G. Harris |  | 2007 | data-science(8) | 本站概念頁 consumer-of-analytics 已點名 Davenport（1 處，另見 schools.ts），portal 上 Davenport 0 本 |
| 7 | **The Model Thinker** | Scott E. Page |  | 2018 | data-science(8) | 分析與決策分類的多模型思維；portal 上 Scott E. Page 0 本 |
| 8 | **Ace the Data Science Interview** | Nick Singh & Kevin Huo |  | 2021 | data-science(8) | portal 已有 14 個名稱含 interview 的書 repo（system design、behavioral、coding、PM、ML system design），獨缺資料科學版 |
| 9 | **（統計學，最強的商業武器）** | 西內啓 |  | 2013 | data-science(8) | 日系商業統計入門，繁中在版；統計思維分類收尾 |

**這是「書本身還沒有」那個軸**，與 docs/ 其餘幾份不同：

| 文件 | 缺口是什麼 | 靠什麼補 |
| --- | --- | --- |
| [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md) | 站在、**內容**沒寫完 | `note-check --enrich` |
| [SOURCING-DEBT.md](./SOURCING-DEBT.md) | 內容寫了、查不到**出處** | 掛 anchor |
| [ORPHAN-BOOKS.md](./ORPHAN-BOOKS.md) | **書有了、沒有站在管** | 認領／開站 |
| **本檔** | **書本身還沒有** | **去收書** |

> 本檔是「**站**說它缺什麼」的正向視角，看不到「沒有任何站提過」的書——那一側看
> [ORPHAN-BOOKS.md](./ORPHAN-BOOKS.md)。兩份要成對看，`tools/refresh-galaxy-docs.sh` 一次重算。

## bibliography 的四個 status

`library.ts` 的 `BibliographyStatus`，語意是「**這本書在書庫裡的狀態**」，不是「讀過沒有」：

| status | 意思 | 判準 | 筆數 |
| --- | --- | --- | --- |
| `owned` | **已收錄**——書已經做成 `nplus.wiki/<slug>/` 的書站 | 必須有 `slug`；首頁書架的封面列就是取這批，概念頁的 `furtherReading.anchor` 也是連到這裡 | 2399 筆（去重 1860 本） |
| `wanted` | **待收錄**——想收、還沒有 | 買得到，只是還沒買／還沒做站 | **9 筆（去重 9 本）** |
| `unavailable` | **暫無來源**——想收但收不到 | 絕版、無中譯、或只有機構授權（如 Scrum Guide、Vanguard 內部傳記） | 87 筆 |
| `skipped` | **刻意略過**——不打算收 | 內容重複、練習冊、合輯、不合站主軸；`note` 欄寫明為何略過 | 87 筆 |

> `owned` 去重後的 1860 是**已建成書站的書**（2399 是含跨站重複的登錄筆數，
> 一本書被三站列進盤點就算三筆）。它代表「書站存在、封面抓得到、概念頁 anchor 回得去」，
> 不等於實體書在書架上。

## 先扣掉：0 本其實已經有書站了

這些 `wanted` 的書名對得上**已存在的書 repo**——不必再收，是各站 bibliography 的 status 沒跟上。**買書前先扣掉這批**，並把該筆改成 `status: "owned"` ＋ 補上 `slug`（＝下表的 repo slug）再重跑；`/note-wanted` 會代勞。

| 書 repo slug | 書名 | 登記在 | portal 上的描述（核對用） |
| --- | --- | --- | --- |

## 作者這一關擋下的：0 筆同名不同書

書名正規化後對得上某個書 repo，**但作者不符**——所以那本不是這一筆想收的書，維持 `wanted`。這關是 2026-08-10 加的第二因子；在那之前 matcher 只比書名，撞名只能靠 `NAME_COLLISIONS` 人工白名單一筆筆補（踩到才補）。

**下面每一筆都要當成買錯書的預警**：想收的和 portal 上那本同名，下單前對作者，別對書名。

無——這輪沒有書名對上卻作者不符的。

## 疑似漏報：0 本可能其實已經有 repo

書名**沒有**正規化後完全相同，但 portal 上有 repo 長得很像——改過書名（英美版不同、中譯轉寫）的書會落在這裡。**這節是提名，不是判決**：確認是同一本就寫進 `export-wanted.py` 的 `ALIASES`，下一輪它就走精確路徑並自動掉進「先扣掉」；確認是續集或同系列的不同書就不用管，下輪還會再問一次。

門檻：兩邊書名的**雙向 Jaccard ≥70%**（詞相等的判準放寬到共同前綴 5 字元，才抓得到 `Forgiving` ↔ `Forgiveness` 這種詞形差異），且**作者沒有互相否決**。用雙向而不是單向覆蓋率，是因為單向會被系列卷洗版——`… on Leadership` 的詞有 75% 出現在 `… on Communication` 裡，但那是不同的一本。作者不符的已經在上一節擋掉；`NAME_COLLISIONS` 裁決過的不再提名。

無——沒有書名相近卻沒對上的。

## 快歸零的站：0 站只差 1–2 本

**TOP20 的準則①就看這一節。** 這些站的書單已經接近收齊，剩下的一兩本收到，整站的採購缺口就歸零——缺書不再是它進 `note-check --enrich` 深化的瓶頸。分母只算 `owned + wanted`（`unavailable` / `skipped` 是永久不可收，不算欠）。

（目前沒有只差 1–2 本的站。）

## 優先收：0 本有兩個以上的站在等

同一本書被多站列為 `wanted`——收一本補多站的缺口，投資報酬率最高。

| 英文書名 | 作者 | 中譯 | 年 | 等它的站 |
| --- | --- | --- | --- | --- |

## 完整清單（依站，共 9 筆）

### data-science-note — 9 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| （統計學，最強的商業武器） | 西內啓 | 統計學，最強的商業武器 | 2013 | 日系商業統計入門；把「為什麼要學統計」講給經理人聽 |
| Statistical Rethinking | Richard McElreath |  | 2020 | 貝氏建模與因果思維的進階課；第二版 |
| Bernoulli's Fallacy | Aubrey Clayton |  | 2021 | 頻率派統計的邏輯缺陷與再現性危機——Silver 第 8 章那場論戰的整本版 |
| Mastering 'Metrics | Joshua D. Angrist & Jörn-Steffen Pischke |  | 2014 | 計量經濟五招（隨機、迴歸、工具變數、RDD、DiD）的平易版；接 economics 站 |
| The Hundred-Page Machine Learning Book | Andriy Burkov |  | 2019 | 一百頁講完 ML 的骨架；複習用 |
| The Elements of Statistical Learning | Trevor Hastie, Robert Tibshirani & Jerome Friedman |  | 2001 | ISL 的數學完整版；查閱用，線上免費 |
| Competing on Analytics | Thomas H. Davenport & Jeanne G. Harris |  | 2007 | 分析型競爭者的組織條件；Davenport 那篇 HBR 文章的整本版 |
| The Model Thinker | Scott E. Page |  | 2018 | 多模型思維：同一現象用幾個簡單模型交叉看 |
| Ace the Data Science Interview | Nick Singh & Kevin Huo |  | 2021 | 接 leetcode／system-design／behaviour-interview 三個面試站的資料科學版 |

## 沒有英文書名的 1 本（華文／日文原著）

這些本來就沒有英文版，照原書名收。

| 原書名 | 作者 | 站 | 為何想收 |
| --- | --- | --- | --- |
| 統計學，最強的商業武器 | 西內啓 | data-science-note | 日系商業統計入門；把「為什麼要學統計」講給經理人聽 |

## 重跑

```bash
notes-core/tools/export-wanted.py
```

收到書、建好書站之後，把該站 bibliography 那筆改成 `status: "owned"` 並補 `slug`，
重跑就會從這裡消失。
