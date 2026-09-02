# 缺出版年清單（bibliography `year` 全星系匯出）

> **生成於 2026-09-02T23:21:50+08:00**｜由 `tools/export-missing-years.py` 產生，**不要手改**——改資料源再重跑。

**這份是什麼**：各 note 站 `src/data/bibliography.ts` 裡**沒填 `year`** 的條目。由
`notes-core/tools/export-missing-years.py` 生成，**不要手改**——補各站的 bibliography 再重跑。

**為什麼要補**：notes-core v0.20.0 起 `year` 是盤點表的**排序鍵**與首頁**年代分佈圖的軸**。
缺 year 的條目會沉到該分組最底、也不進圖表——書還在表上，只是從時間軸上消失了。

**填哪一個年份**：schema 要的是**初版年**（原文首次出版），不是手上這一版、更不是中譯版。
下面的 📕 是該書 repo `book-cover` 記的版次日，只能當**線索**——照抄會把時間軸整條往後推。

目前：75 站 / 2425 筆，缺 year **65 筆**（2.7%），分佈在 26 站；其中 0 筆查得到版次日線索。

每一站「有 year」的條目都 ≥ 4 筆，所以年代分佈圖全都畫得出來，只是少了這些點。

## 各站缺口

缺越多排越前；缺 0 的站略去。

| 站 | 總筆數 | 有 year | 缺 year |
| --- | ---: | ---: | ---: |
| biblical-studies-note | 130 | 121 | 9 |
| growth-note | 68 | 61 | 7 |
| life-meaning-note | 52 | 47 | 5 |
| communication-note | 87 | 83 | 4 |
| learning-note | 42 | 38 | 4 |
| relationships-note | 58 | 54 | 4 |
| theology-note | 87 | 83 | 4 |
| philosophy-note | 50 | 47 | 3 |
| career-note | 80 | 78 | 2 |
| investing-note | 106 | 104 | 2 |
| marketing-note | 35 | 33 | 2 |
| system-design-note | 33 | 31 | 2 |
| tracy-note | 39 | 37 | 2 |
| wellness-note | 39 | 37 | 2 |
| writing-note | 37 | 35 | 2 |
| clean-code-note | 43 | 42 | 1 |
| data-systems-note | 23 | 22 | 1 |
| design-patterns-note | 22 | 21 | 1 |
| greene-note | 9 | 8 | 1 |
| habits-note | 48 | 47 | 1 |
| hbr-note | 46 | 45 | 1 |
| pastoral-psychology-note | 11 | 10 | 1 |
| personal-finance-note | 60 | 59 | 1 |
| science-note | 51 | 50 | 1 |
| spiritual-formation-note | 45 | 44 | 1 |
| thinking-note | 70 | 69 | 1 |

## 逐筆清單

格式：`[status]` 書名 / 原文 · 分組 — 📕 書 repo 記的版次日（若有）

### biblical-studies-note（9 筆）

- [skipped] NICNT／NICOT 系列代表卷 · 逐卷解經（BST 系列）
- [owned] 五經行--妥拉中的生命智慧 · 舊約
- [owned] 21世紀新約導覽 · 新約
- [owned] 新約聖經研究導論 · 新約
- [owned] 誰說字句叫人死 · 釋經方法與讀經
- [owned] 見證耶穌是基督：基督宗教釋經學初探 · 釋經方法與讀經
- [owned] Written in Stone · 聖經與生活實踐
- [owned] Bible Atlas · 聖經神學與背景
- [owned] 在診療室遇見摩西：精神科醫師帶你探索隱藏在聖經裡的心靈祕密 · 聖經與生活實踐

### career-note（2 筆）

- [owned] 沒人敢告訴你的MBA大揭密 · 職涯資本
- [owned] 大人學選擇 · 自我管理

### clean-code-note（1 筆）

- [owned] 整潔程式碼原則與模式：軟體從業者手冊 / Clean Code Principles and Patterns: A Software Practitioner's Handbook · 工藝基石

### communication-note（4 筆）

- [owned] 說話的品格 · 對話與衝突
- [owned] Ohne Worte · 社交與人性洞察
- [owned] The Terrible Truth About Lawyers · 談判
- [owned] 寫給每個人的社會學讀本 · 社交與人性洞察

### data-systems-note（1 筆）

- [owned] PostgreSQL 14 Internals · 儲存與查詢優化

### design-patterns-note（1 筆）

- [owned] 物件導向設計面試 / Object-Oriented Design Interview · GoF 正典與入門

### greene-note（1 筆）

- [skipped] 精華節錄版 / The Concise 48 Laws of Power ... · 權力與策略

### growth-note（7 筆）

- [owned] 贏家的法則：30 個通往成功的鐵律 / Die Gesetze der Gewinner · 成功學傳統
- [owned] QBQ! The Question Behind the Question · 成功學傳統
- [owned] Change Your Questions, Change Your Life · 成長心態
- [owned] Change Your Thinking, Change Your Life · 成功學傳統
- [owned] The Difference That Makes the Difference · 成長心態
- [owned] The Long Win · 成功學傳統
- [owned] No One Understands You and What to Do About It · 自我覺察

### habits-note（1 筆）

- [owned] 行動的力量 · 紀律與品格

### hbr-note（1 筆）

- [owned] HBR Guide Collection（合輯） · 溝通協作

### investing-note（2 筆）

- [owned] Investing: The Last Liberal Art · 行為與心理
- [owned] The New Tao of Warren Buffett · 價值投資

### learning-note（4 筆）

- [unavailable] 人才，自造者 · 自學與超速學習
- [owned] 只有讀書能抵達的境界 / 読書する人だけがたどり着ける場所 · 閱讀與吸收
- [owned] English Is Not Easy · 自學與超速學習
- [owned] 一流的人讀書，都在哪裡畫線？ · 閱讀與吸收

### life-meaning-note（5 筆）

- [owned] Living, Loving and Learning · 意義與召命
- [owned] 活出生命最好的可能 · 意義與召命
- [owned] Your Mind: An Owner's Manual for a Better Life · 心理健康
- [owned] 你的不安，是因為太習慣受傷害 · 情緒與內在
- [owned] Forgiveness and Reconciliation: Initiating Individuation and Enabling Liberation · 老化與有限性

### marketing-note（2 筆）

- [owned] No Thanks, I'm Just Looking · 需求與提案
- [owned] 破億下載 Podcast 製作人的經營指南 · 內容與注意力

### pastoral-psychology-note（1 筆）

- [owned] Theory and Practice of Counseling and Psychotherapy · 整合光譜

### personal-finance-note（1 筆）

- [owned] 心態致富 · 節儉與財富習慣

### philosophy-note（3 筆）

- [owned] The Art of Asking Life Questions · 應用哲學
- [owned] Beautiful Thoughts from Ralph Waldo Emerson · 人文主義與存在
- [owned] 哲學與人生 · 思想史與入門

### relationships-note（4 筆）

- [owned] Be a Better Dad Today · 教養
- [owned] Flying Together: A Christian Marriage Guide · 婚姻
- [owned] 教出孩子的生存力 · 教養
- [owned] Secrets of Sexual Body Language · 愛情與親密

### science-note（1 筆）

- [skipped] 牛津臨床藥學手冊 / Oxford Handbook of Clinical Pharmacy · 專業教科書

### spiritual-formation-note（1 筆）

- [owned] When Good Men Are Tempted · 門徒與跟隨

### system-design-note（2 筆）

- [owned] Software Architecture for Developers, Vol. 1 · 軟體架構
- [owned] Software Architecture for Developers, Vol. 2 · 軟體架構

### theology-note（4 筆）

- [owned] 21世紀神學事件簿--如何在多元處境下做神學 · 教義與系統神學
- [owned] 中國教會的反智主義 · 教會與牧養
- [owned] 認識上帝與認識人的9個探險 · 教義與系統神學
- [owned] 是與非以外：基督教的倫理想像 · 教義與系統神學

### thinking-note（1 筆）

- [owned] Critical Thinking: Concepts and Tools · 思維模型

### tracy-note（2 筆）

- [skipped] 勵志小品群 / Kiss That Frog! / Crunch Point / Reinvention / Full Engagement! ... · 目標與成就
- [skipped] How the Best Leaders Lead / TurboStrategy · 經營與領導

### wellness-note（2 筆）

- [owned] 煩惱都是自己想出來的 · 壓力與心理健康
- [owned] Self-Esteem · 壓力與心理健康

### writing-note（2 筆）

- [owned] 2nd Iteration · 閱讀即輸入
- [owned] How to Say It · 非虛構與文案

## 補不上來的那幾筆

有些條目**本來就不該有單一年份**，補不上是對的，不是欠債：

- **上古典籍**（論語、道德經、孫子兵法、理想國、尼各馬可倫理學…）：成書年本身是區間。
  真要上時間軸就填約略的負數年（`year: -500`），圖表標籤會顯示成 `500 BC`。
- **`skipped` 的彙總列**（「勵志小品群 / Kiss That Frog! / Crunch Point …」）：
  一列代表一整批書，沒有單一出版年。留白即可。
- **系列代表卷**（NICNT／NICOT 系列）：指的是一套書而非一本。

## 重跑

```bash
notes-core/tools/export-missing-years.py
```

補完某站的 `year` 之後重跑，該站就會從這裡消失。
