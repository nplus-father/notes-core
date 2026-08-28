# 刻意排除的書（不再考慮進任何站）

**這份是什麼**：品質把關的裁決紀錄。這些書 repo 存在於書庫，但**裁定不進任何 note 站的
bibliography**——note 星系留下來考量的每一本都該撐得起 ground truth，這批撐不起
（練習冊、機構教材、故事集⋯⋯），也不值得為它開站。**手維護**；
`export-orphan-books.py` 會讀下面的表，把命中的 repo 從孤兒清單移除，**以後重算不再提醒**。

**與站內 `skipped` 的分工**：`skipped` 是**單一站**說「這本不合我的主軸」（別站仍可收）；
本檔是**全星系**說「這本哪一站都不該收」。已經 `owned` 而要移出的書**不進本檔**——
在該站把那筆改成 `status: "skipped"`、**保留 slug**、`note` 寫明理由即可（寫了 slug
就算認領，不會掉回孤兒清單；書架封面列只取 `owned`，所以會自動下架）。

**格式**：一行一本，slug 用反引號包住（腳本靠 `` `slug` `` 這個樣式抓，別拆行）。
反悔就刪那一行重跑。書 repo 本身**不刪**——排除的是「進 note 盤點」這件事，不是書庫。

| repo slug | 書名 | 理由 | 裁決日 |
| --- | --- | --- | --- |
| `cfa-corporate-finance-workbook` | Corporate Finance Workbook | CFA 練習冊——練習冊不進盤點（沿用站內 skipped 既有判準） | 2026-08-13 |
| `portfolio-management-in-practice-vol-1` | Portfolio Management in Practice, Vol.1 | CFA 課綱教科書卷——機構教材，非思想原典（COVERAGE-GAPS 已裁「機構不算人物」） | 2026-08-13 |
| `portfolio-management-in-practice-vol-2` | Portfolio Management in Practice, Vol.2 | 同上 | 2026-08-13 |
| `portfolio-management-in-practice-vol-3` | Portfolio Management in Practice, Vol.3 | 同上 | 2026-08-13 |
| `quantitative-investment-analysis` | Quantitative Investment Analysis | CFA 課綱教科書卷——同上 | 2026-08-13 |
| `29-pawn-tickets` | 29張當票：典當不到的人生啟發 | 當舖人生故事集——勵志小品，無主題站可歸，人物軸也不為其開站 | 2026-08-13 |
| `29-pawn-tickets-2` | 29張當票2：當舖裡特有的人生風景 | 同上 | 2026-08-13 |
| `learning-to-be-deceived` | 學上當 | 同上（秦嗣林系列第四本） | 2026-08-13 |
| `mental-fitness` | 刻意進化：突破極限的心智鍛鍊 | **書庫重複建站**——與 `learned-excellence` 同一本書（Potterat & Eagle），2026-08-26 已裁決 slug 指向正本；本檔補記，讓它不再回到孤兒清單 | 2026-08-28 |

## 重跑

```bash
notes-core/tools/export-orphan-books.py
```

排除的書會在 ORPHAN-BOOKS.md 摘要裡以獨立一行計數，不再列進孤兒清單；
若某站的 bibliography 又用 `slug` 指到了被排除的書，重跑會在輸出裡標 ⚠ 提醒裁決衝突。
