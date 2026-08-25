# 待收書單（bibliography `wanted` 全星系匯出）

> **生成於 2026-08-25T21:52:12+08:00**｜由 `tools/export-wanted.py` 產生，**不要手改**——改資料源再重跑。

**這份是什麼**：各 note 站 `src/data/bibliography.ts` 裡標成 `status: "wanted"` 的書，
全部匯出成一張採購清單。書名以**英文原名**為主，中譯附在後面，並附**作者**——
同名不同書會讓人買錯（portal 上的 `servant-leadership` 是 Larry W. Boone 的教科書，
不是 Greenleaf 1977 原典），下單前請對作者。由
`notes-core/tools/export-wanted.py` 生成，**不要手改**——改各站的 bibliography 再重跑。

**已收錄比對的資料源**：GitHub 現況（`gh repo list` nplus-father／Andrewnplus，1902 個 repo）。

## 先收這 1 本

整份 5 筆太長，這是從裡面挑出來的採購順序，也是建議的消化順序（薄的、起手容易的排前面）。**這節是全檔唯一的人工區塊**——要改請編 `export-wanted.py` 的 `TOP20`，不要改這裡。挑選準則依序：**①歸零槓桿——優先收「還差 1–2 本就收齊」的站所缺的書**（見下面「快歸零的站」那節，腳本自動算；站書單一歸零，缺書就不再是它進 `note-check --enrich` 深化的瓶頸） ②多站共等，收一本補多站 ③站主自己在 `note` 裡標了「最大／頭號缺口」 ④portal 驗證的 anchor 深度——nplus.wiki 上已經建成幾本回指它的書站（同作者書櫃、同一條線的衍生書），書櫃愈深、原典愈缺就排愈前面（見 [SOURCING-DEBT.md](./SOURCING-DEBT.md)） ⑤同等重要時，薄的、有繁中在版的排前面。

「站」欄的 `(n)` ＝**收了這本之後該站還剩幾本**；`(0)` 就是這一本收了該站即歸零。

「為何排這裡」的 portal 數字都是實查出來的（作者書櫃本數、同一條線的衍生書數、各站概念頁引用處數）；`/note-wanted` 每次重挑會一併重查。

> ⚠ **這 1 本裡有 1 本已經建好書站了**（下表標 ✅），代表這張採購清單該重挑——跑 `/note-wanted` 把 bibliography 回填成 `owned` 之後重排。

| # | 英文書名 | 作者 | 中譯 | 年 | 站 | 為何排這裡 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **Old Testament Theology** | John Goldingay |  | 2003 | biblical-studies(0) | ✅ 已建站 `old-testament-theology-israels-life`——**全星系最後一本還沒收的書**。biblical-studies 站 owned 75／wanted 1——收了就歸零，準則①（同輪 Hays 回填成 owned、NICNT 系列改 skipped 之後，這是本站最後一筆）。**要買的是第一卷 `Israel's Gospel`（IVP 2003）**，不是整套：2026-08-20 清點手上的檔案，三部曲的第二卷 Israel's Faith 早已建站 `old-testament-theology-israels-faith`、第三卷 Israel's Life 的 epub 也在手，**只缺第一卷**；Andrew 同日裁決三卷齊了才結案，不以單卷收錄（見 NAME_COLLISIONS 那筆）。準則④的證據仍是全星系最弱的一批，誠實記著：舊約神學線已有 Brueggemann 的 `theology-of-the-old-testament` 與 Waltke 的 `old-testament-theology-waltke`，Goldingay 自己的單卷 `biblical-theology-goldingay` 也已收（他書櫃 3 本）——**不是空格，是想多收一種進路**；「舊約神學」全星系只有 **3 處／2 檔且全在本站**（2026-08-20 現查）。大部頭、無繁中 |

**這是「書本身還沒有」那個軸**，與 docs/ 其餘幾份不同：

| 文件 | 缺口是什麼 | 靠什麼補 |
| --- | --- | --- |
| [COVERAGE-GAPS.md](./COVERAGE-GAPS.md) | 還沒有**站** | 開新站 |
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
| `owned` | **已收錄**——書已經做成 `nplus.wiki/<slug>/` 的書站 | 必須有 `slug`；首頁書架的封面列就是取這批，概念頁的 `furtherReading.anchor` 也是連到這裡 | 1890 筆（去重 1409 本） |
| `wanted` | **待收錄**——想收、還沒有 | 買得到，只是還沒買／還沒做站 | **5 筆（去重 5 本）** |
| `unavailable` | **暫無來源**——想收但收不到 | 絕版、無中譯、或只有機構授權（如 Scrum Guide、Vanguard 內部傳記） | 85 筆 |
| `skipped` | **刻意略過**——不打算收 | 內容重複、練習冊、合輯、不合站主軸；`note` 欄寫明為何略過 | 86 筆 |

> `owned` 去重後的 1409 是**已建成書站的書**（1890 是含跨站重複的登錄筆數，
> 一本書被三站列進盤點就算三筆）。它代表「書站存在、封面抓得到、概念頁 anchor 回得去」，
> 不等於實體書在書架上。

## 先扣掉：1 本其實已經有書站了

這些 `wanted` 的書名對得上**已存在的書 repo**——不必再收，是各站 bibliography 的 status 沒跟上。**買書前先扣掉這批**，並把該筆改成 `status: "owned"` ＋ 補上 `slug`（＝下表的 repo slug）再重跑；`/note-wanted` 會代勞。

| 書 repo slug | 書名 | 登記在 | portal 上的描述（核對用） |
| --- | --- | --- | --- |
| `old-testament-theology-israels-life` | Old Testament Theology | biblical-studies-note | Old Testament Theology: Israel's Life (Vol. 3) \| John Goldin |

## 作者這一關擋下的：0 筆同名不同書

書名正規化後對得上某個書 repo，**但作者不符**——所以那本不是這一筆想收的書，維持 `wanted`。這關是 2026-08-10 加的第二因子；在那之前 matcher 只比書名，撞名只能靠 `NAME_COLLISIONS` 人工白名單一筆筆補（踩到才補）。

**下面每一筆都要當成買錯書的預警**：想收的和 portal 上那本同名，下單前對作者，別對書名。

無——這輪沒有書名對上卻作者不符的。

## 疑似漏報：0 本可能其實已經有 repo

書名**沒有**正規化後完全相同，但 portal 上有 repo 長得很像——改過書名（英美版不同、中譯轉寫）的書會落在這裡。**這節是提名，不是判決**：確認是同一本就寫進 `export-wanted.py` 的 `ALIASES`，下一輪它就走精確路徑並自動掉進「先扣掉」；確認是續集或同系列的不同書就不用管，下輪還會再問一次。

門檻：兩邊書名的**雙向 Jaccard ≥70%**（詞相等的判準放寬到共同前綴 5 字元，才抓得到 `Forgiving` ↔ `Forgiveness` 這種詞形差異），且**作者沒有互相否決**。用雙向而不是單向覆蓋率，是因為單向會被系列卷洗版——`… on Leadership` 的詞有 75% 出現在 `… on Communication` 裡，但那是不同的一本。作者不符的已經在上一節擋掉；`NAME_COLLISIONS` 裁決過的不再提名。

無——沒有書名相近卻沒對上的。

## 快歸零的站：4 站只差 1–2 本

**TOP20 的準則①就看這一節。** 這些站的書單已經接近收齊，剩下的一兩本收到，整站的採購缺口就歸零——缺書不再是它進 `note-check --enrich` 深化的瓶頸。分母只算 `owned + wanted`（`unavailable` / `skipped` 是永久不可收，不算欠）。

| 站 | 已收 | 還差 | 差哪幾本 |
| --- | ---: | ---: | --- |
| `biblical-studies-note` | 75 | **1** | Old Testament Theology（John Goldingay） |
| `learning-note` | 33 | **1** | 人才，自造者（⚠ 作者未登錄） |
| `collins-note` | 6 | **1** | Turning the Flywheel（Jim Collins） |
| `career-note` | 68 | **2** | Where Will You Be in the Next Decade?（⚠ 作者未登錄）、沒了名片，你還剩下什麼？（姚詩豪、張國洋） |

> ⚠ **2 本還沒登錄作者**，表上標「⚠ 作者未登錄」：`cjk::人才，自造者`、`where-will-you-be-in-the-next-decade`。**在該站 `bibliography.ts` 那筆補 `author:`** 再重跑（notes-core v0.27.0 起作者是 bibliography 的資料欄，產生器不再養對照表）——沒有作者就防不了同名不同書。

## 優先收：0 本有兩個以上的站在等

同一本書被多站列為 `wanted`——收一本補多站的缺口，投資報酬率最高。

| 英文書名 | 作者 | 中譯 | 年 | 等它的站 |
| --- | --- | --- | --- | --- |

## 完整清單（依站，共 5 筆）

### career-note — 2 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| （沒了名片，你還剩下什麼？） | 姚詩豪、張國洋 | 沒了名片，你還剩下什麼？ | 2017 | 大人學「拿掉名片」主題的原書（下單前對作者）。原概念頁 2026-08-20 依未溯源紀律移除，收書後回原文核對重寫 |
| Where Will You Be in the Next Decade? | ⚠ 作者未登錄 |  |  | 2026-08-24 從退役的 BOOKS.md 接手：那份清單列過它，但書庫沒有 repo、盤點表也沒登記，等於只活在手抄檔裡。作者待查——export-wanted.py 拿作者當第二比對因子，缺了它比不出「這本其實已經有書站」 |

### biblical-studies-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Old Testament Theology ⟵ 已有書站 `old-testament-theology-israels-life` | John Goldingay |  | 2003 | Goldingay 的敘事進路大部頭，共三卷（其單卷《聖經神學》已收）。2026-08-20 清點：第二卷 Israel's Faith 已建站 `old-testament-theology-israels-faith`、第三卷 Israel's Life 檔案已在手，**缺的是第一卷 Israel's Gospel（IVP 2003）**；裁決是等整套齊了再結案，不以單卷收錄 |

### collins-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Turning the Flywheel | Jim Collins | 飛輪效應 | 2019 | 飛輪單行本：把《從 A 到 A+》第八章擴成畫飛輪的方法與案例集——站上飛輪頁目前由三本書拼出 |

### learning-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| （人才，自造者） | ⚠ 作者未登錄 | 人才，自造者 |  | 2026-08-24 從退役的 BOOKS.md 接手：那份清單列過它，但書庫沒有 repo、盤點表也沒登記，等於只活在手抄檔裡。作者待查——export-wanted.py 拿作者當第二比對因子，缺了它比不出「這本其實已經有書站」 |

## 沒有英文書名的 2 本（華文／日文原著）

這些本來就沒有英文版，照原書名收。

| 原書名 | 作者 | 站 | 為何想收 |
| --- | --- | --- | --- |
| 沒了名片，你還剩下什麼？ | 姚詩豪、張國洋 | career-note | 大人學「拿掉名片」主題的原書（下單前對作者）。原概念頁 2026-08-20 依未溯源紀律移除，收書後回原文核對重寫 |
| 人才，自造者 | ⚠ 作者未登錄 | learning-note | 2026-08-24 從退役的 BOOKS.md 接手：那份清單列過它，但書庫沒有 repo、盤點表也沒登記，等於只活在手抄檔裡。作者待查——export-wanted.py 拿作者當第二比對因子，缺了它比不出「這本其實已經有書站」 |

## 重跑

```bash
notes-core/tools/export-wanted.py
```

收到書、建好書站之後，把該站 bibliography 那筆改成 `status: "owned"` 並補 `slug`，
重跑就會從這裡消失。
