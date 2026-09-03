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
| `portfolio-management-in-practice-vol-1` | Portfolio Management in Practice, Vol.1 | CFA 課綱教科書卷——機構教材，非思想原典（2026-08-03 首輪盤點已裁「機構不算人物」，見下節） | 2026-08-13 |
| `portfolio-management-in-practice-vol-2` | Portfolio Management in Practice, Vol.2 | 同上 | 2026-08-13 |
| `portfolio-management-in-practice-vol-3` | Portfolio Management in Practice, Vol.3 | 同上 | 2026-08-13 |
| `quantitative-investment-analysis` | Quantitative Investment Analysis | CFA 課綱教科書卷——同上 | 2026-08-13 |
| `29-pawn-tickets` | 29張當票：典當不到的人生啟發 | 當舖人生故事集——勵志小品，無主題站可歸，人物軸也不為其開站 | 2026-08-13 |
| `29-pawn-tickets-2` | 29張當票2：當舖裡特有的人生風景 | 同上 | 2026-08-13 |
| `learning-to-be-deceived` | 學上當 | 同上（秦嗣林系列第四本） | 2026-08-13 |
| `mental-fitness` | 刻意進化：突破極限的心智鍛鍊 | **書庫重複建站**——與 `learned-excellence` 同一本書（Potterat & Eagle），2026-08-26 已裁決 slug 指向正本；本檔補記，讓它不再回到孤兒清單 | 2026-08-28 |

## 不開站的裁決（原 COVERAGE-GAPS.md，2026-08-03～08-10 定案，2026-09-03 併入本檔）

「還沒有站」的現況改由 [ORPHAN-BOOKS.md](./ORPHAN-BOOKS.md) 的 1b（開新站候選 leaf）與 1d（同一作者多本沒人認領）
每次重算；判準沿用首輪：leaf 藏書 ≥8 本且未覆蓋 ≥60%。這裡只留**人裁過、工具不該再提醒**的決定：

- **釋經書系作者不開人物站**：Michael Wilcock、Alec Motyer、Raymond Brown、John H. Walton（合計 18 本）。
  讀者關心的是「這卷書怎麼解」不是「這個人怎麼想」，書併入 biblical-studies-note 的盤點。
- **主題站已讀完、開站只是換鏡頭的人物，目前不開**：Yuval Noah Harari、Malcolm Gladwell、Ray Dalio、
  Timothy Ferriss、Alex Hormozi（未引用數都是 0–1，開站不會多讀到新書）。同一批裡 grant／jung／christensen／grove
  後來因人物軸需求開了站，不是這條裁決翻案。
- **機構不算人物**：Harvard Business Review（已有 hbr-note）、CFA Institute。
- **共同作者字串會重複計數**：「Robert T. Kiyosaki & Sharon L. Lechter」與「Robert Kiyosaki」會被算成兩位——
  重算時取 `&`／`,`／`and` 之前的第一作者。
- **要用 leaf 層掃**：書庫 20 個 sub 早已覆蓋 19 個，用 sub 層掃永遠掃不出缺口。

## 重跑

```bash
notes-core/tools/export-orphan-books.py
```

排除的書會在 ORPHAN-BOOKS.md 摘要裡以獨立一行計數，不再列進孤兒清單；
若某站的 bibliography 又用 `slug` 指到了被排除的書，重跑會在輸出裡標 ⚠ 提醒裁決衝突。
