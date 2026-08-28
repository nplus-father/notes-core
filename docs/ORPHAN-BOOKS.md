# 孤兒書與死鏈（反向盤點）

> **生成於 2026-08-28T14:01:43+08:00**｜由 `tools/export-orphan-books.py` 產生，**不要手改**——改資料源再重跑。

**這份是什麼**：從**書庫那一側**反過來問的四個問題——書庫的書有沒有站在管、站上的 slug 指得到書嗎。由 `notes-core/tools/export-orphan-books.py` 生成，**不要手改**——改各站的 bibliography／內容再重跑。

**為什麼需要反向**：另外幾份都是「站說它缺什麼」的正向視角，看不到「**沒有任何站提過**」的書——新建的書站如果沒人認領，正向工具永遠不會提醒你，因為沒有站提過它。

**資料源**：GitHub 現況（`gh repo list` nplus-father／Andrewnplus，1904 個 repo），其中 `nplus-kind-book` 的書 repo 1773 本（9 本經 [EXCLUDED-BOOKS.md](./EXCLUDED-BOOKS.md) 裁決排除，不入盤點）。

| 文件 | 缺口是什麼 | 靠什麼補 |
| --- | --- | --- |
| [COVERAGE-GAPS.md](./COVERAGE-GAPS.md) | 還沒有**站** | 開新站 |
| [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md) | 站在、**內容**沒寫完 | `note-check --enrich` |
| [SOURCING-DEBT.md](./SOURCING-DEBT.md) | 內容寫了、查不到**出處** | 掛 anchor |
| [WANTED-BOOKS.md](./WANTED-BOOKS.md) | **書本身**還沒有 | 去收書 |
| **本檔** | **書有了、沒有站在管**（或指到的書不存在） | 認領／開站／修 slug |

## 摘要

| 檢查 | 數 | 後果 |
| --- | ---: | --- |
| 孤兒書（沒有任何站的 bibliography 指到） | **1** | 書站建了但沒有筆記在用，等於白建 |
| ↳ 其中內容頁已經 anchor 到、盤點沒登記 | **0** | 補一筆 bibliography 就好，不必開站 |
| 刻意排除（[EXCLUDED-BOOKS.md](./EXCLUDED-BOOKS.md) 裁決不進任何站） | **9** | 不列孤兒、不再提醒 |
| 死鏈 slug（bibliography 指到不存在的 repo） | **0** | 首頁書架封面 404 |
| `owned` 沒有 slug | **0** | 不會出現在首頁書架，登記了卻看不到 |
| 死鏈 anchor（內容頁 `book:` 指到不存在的 repo） | **0** | 延伸閱讀連結 404 |

## 一、孤兒書：1 本沒有任何站認領

判準＝這本書的 repo name 沒有出現在**任何**站 `bibliography.ts` 的 `slug` 欄。用 slug 而不是站數對書數，是因為它抓得到跨站分工——一本書被別站認領也算覆蓋。

### 1a. 內容已經引了、盤點沒登記：0 本

無——內容引用到的書都已經登記在盤點裡。

### 1b. 開新站候選：0 個 leaf

判準沿用 COVERAGE-GAPS 那輪：**藏書 ≥8 本且未覆蓋 ≥60%**。低於這個比例的 leaf 表示已經有站在管、只是還沒寫完——那是 [ENRICH-BACKLOG](./ENRICH-BACKLOG.md) 的事，不是這裡的。

無——沒有任何 leaf 同時滿足「書夠多」與「大多沒人碰」。

### 1c. 各 leaf 覆蓋率與目前誰在管

**看比例不是看絕對數。** 未覆蓋比例高＝沒站在管（開新站）；絕對數高但比例低＝有站在管、只是還沒寫完。「目前誰在管」是該 leaf **已覆蓋**的書被哪些站引用——孤兒通常就該歸這幾站認領，不必另外開站。

| leaf | sub | 未覆蓋/總數 | 未覆蓋率 | 目前誰在管 |
| --- | --- | ---: | ---: | --- |
| `systematic` | theology | 1/43 | 2% | theology(30)、biblical-studies(8)、spiritual-formation(4) |

### 1d. 同一作者 ≥3 本沒人認領：0 位

作者站的線索。**有同名站就是該站漏收**（回去補 bibliography），沒有站才是開站候選——COVERAGE-GAPS 的人物缺口就是這樣抓出 covey／templar／navarro 三站的。

無。

### 1e. 全部 1 本（依 leaf 分組）

#### `systematic` — 1/43 沒人認領（目前：theology(30)、biblical-studies(8)、spiritual-formation(4)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `martin-luthers-catechisms-forming-the-faith` | 馬丁路德的門徒培育班 | Timothy J. Wengert |

## 二、死鏈 slug：0 個

bibliography 的 `slug` 在書庫裡找不到對應 repo——**首頁書架的封面會 404**。兩種收法（2026-08-04 那批 8 個就是這樣分的）：書其實該有就**補建書 repo**，書根本不存在就**撤掉這筆 `slug`**，不要掛死鏈。

無——所有 `slug` 都指得到真的 repo。

## 三、`owned` 沒有 slug：0 筆

`owned` 的語意是「已經做成 `nplus.wiki/<slug>/` 書站」，slug 是必要條件。沒填 slug 的 `owned` **不會出現在首頁書架的封面列**，概念頁的 `furtherReading.anchor` 也無處可指——書登記了卻看不到。書真的有就補 slug；其實還沒收就改回 `wanted`。

無——每一筆 `owned` 都有 slug。

## 四、死鏈 anchor：0 個 slug

內容頁 `furtherReading` 的 `book:` 指到不存在的書 repo——延伸閱讀連結 404。[SOURCING-DEBT](./SOURCING-DEBT.md) 只驗過「頁有沒有 anchor」，沒驗過「anchor 到的書在不在」。

無——所有 anchor 都指得到真的 repo。

## 重跑

```bash
notes-core/tools/export-orphan-books.py
```

認領一本孤兒＝在該站 `bibliography.ts` 加一筆 `status: "owned"` ＋ `slug: "<repo name>"`，
重跑就會從這裡消失。整個 leaf 都沒站在管就走 `/note-new-station`。
裁定**永遠不進任何站**＝在 [EXCLUDED-BOOKS.md](./EXCLUDED-BOOKS.md) 加一行，重跑後不再提醒。
