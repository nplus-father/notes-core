# 缺出版年清單（bibliography `year` 全星系匯出）

> **生成於 2026-09-03T00:41:36+08:00**｜由 `tools/export-missing-years.py` 產生，**不要手改**——改資料源再重跑。

**這份是什麼**：各 note 站 `src/data/bibliography.ts` 裡**沒填 `year`** 的條目。由
`notes-core/tools/export-missing-years.py` 生成，**不要手改**——補各站的 bibliography 再重跑。

**為什麼要補**：notes-core v0.20.0 起 `year` 是盤點表的**排序鍵**與首頁**年代分佈圖的軸**。
缺 year 的條目會沉到該分組最底、也不進圖表——書還在表上，只是從時間軸上消失了。

**填哪一個年份**：schema 要的是**初版年**（原文首次出版），不是手上這一版、更不是中譯版。
下面的 📕 是該書 repo 記的出版日（frontmatter 的 `book.published`，或舊格式 book-cover 的
版次日），只能當**線索**——那是做摘要時手上那一版，照抄會把時間軸整條往後推。

目前：75 站 / 2426 筆，缺 year **7 筆**（0.3%），分佈在 5 站；其中 1 筆查得到出版日線索。

每一站「有 year」的條目都 ≥ 4 筆，所以年代分佈圖全都畫得出來，只是少了這些點。

## 各站缺口

缺越多排越前；缺 0 的站略去。

| 站 | 總筆數 | 有 year | 缺 year |
| --- | ---: | ---: | ---: |
| biblical-studies-note | 130 | 128 | 2 |
| tracy-note | 39 | 37 | 2 |
| greene-note | 9 | 8 | 1 |
| learning-note | 42 | 41 | 1 |
| philosophy-note | 50 | 49 | 1 |

## 逐筆清單

格式：`[status]` 書名 / 原文 · 分組 — 📕 書 repo 記的出版日（若有；是手上那一版，不是初版）

### biblical-studies-note（2 筆）

- [skipped] NICNT／NICOT 系列代表卷 · 逐卷解經（BST 系列）
- [owned] Bible Atlas · 聖經神學與背景

### greene-note（1 筆）

- [skipped] 精華節錄版 / The Concise 48 Laws of Power ... · 權力與策略

### learning-note（1 筆）

- [unavailable] 人才，自造者 · 自學與超速學習

### philosophy-note（1 筆）

- [owned] Beautiful Thoughts from Ralph Waldo Emerson · 人文主義與存在 — 📕 August 24, 2018

### tracy-note（2 筆）

- [skipped] 勵志小品群 / Kiss That Frog! / Crunch Point / Reinvention / Full Engagement! ... · 目標與成就
- [skipped] How the Best Leaders Lead / TurboStrategy · 經營與領導

## 補不上來的那幾筆

有些條目**本來就不該有單一年份**，補不上是對的，不是欠債：

- **上古典籍**（論語、道德經、孫子兵法、理想國、尼各馬可倫理學…）：成書年本身是區間。
  真要上時間軸就填約略的負數年（`year: -500`），圖表標籤會顯示成 `500 BC`。
- **`skipped` 的彙總列**（「勵志小品群 / Kiss That Frog! / Crunch Point …」）：
  一列代表一整批書，沒有單一出版年。留白即可。
- **系列代表卷**（NICNT／NICOT 系列）：指的是一套書而非一本。
- **公版作家的後人彙編**（《Beautiful Thoughts from Ralph Waldo Emerson》）：彙編年份放上
  時間軸會把十九世紀的作者標到二十一世紀，比留白更誤導；愛默生的原作年也不是這本的年份。
  2026-09-03 裁決留白。
- **本機沒有 repo 的書**（`bible-atlas`）：沒有 frontmatter 可讀，metadata 待補。

## 重跑

```bash
notes-core/tools/export-missing-years.py
```

補完某站的 `year` 之後重跑，該站就會從這裡消失。
