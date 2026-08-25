# 缺出版年清單（bibliography `year` 全星系匯出）

> **生成於 2026-08-26T01:08:52+08:00**｜由 `tools/export-missing-years.py` 產生，**不要手改**——改資料源再重跑。

**這份是什麼**：各 note 站 `src/data/bibliography.ts` 裡**沒填 `year`** 的條目。由
`notes-core/tools/export-missing-years.py` 生成，**不要手改**——補各站的 bibliography 再重跑。

**為什麼要補**：notes-core v0.20.0 起 `year` 是盤點表的**排序鍵**與首頁**年代分佈圖的軸**。
缺 year 的條目會沉到該分組最底、也不進圖表——書還在表上，只是從時間軸上消失了。

**填哪一個年份**：schema 要的是**初版年**（原文首次出版），不是手上這一版、更不是中譯版。
下面的 📕 是該書 repo `book-cover` 記的版次日，只能當**線索**——照抄會把時間軸整條往後推。

目前：75 站 / 2066 筆，缺 year **98 筆**（4.7%），分佈在 24 站；其中 0 筆查得到版次日線索。

每一站「有 year」的條目都 ≥ 4 筆，所以年代分佈圖全都畫得出來，只是少了這些點。

## 各站缺口

缺越多排越前；缺 0 的站略去。

| 站 | 總筆數 | 有 year | 缺 year |
| --- | ---: | ---: | ---: |
| tracy-note | 39 | 27 | 12 |
| leadership-note | 98 | 87 | 11 |
| biblical-studies-note | 78 | 70 | 8 |
| career-note | 72 | 64 | 8 |
| cloud-infra-note | 26 | 20 | 6 |
| startup-note | 64 | 58 | 6 |
| management-note | 47 | 42 | 5 |
| theology-note | 66 | 61 | 5 |
| wellness-note | 34 | 29 | 5 |
| science-note | 49 | 45 | 4 |
| behaviour-interview-note | 20 | 17 | 3 |
| fengtang-note | 15 | 12 | 3 |
| marketing-note | 33 | 30 | 3 |
| system-design-note | 25 | 22 | 3 |
| design-patterns-note | 21 | 19 | 2 |
| greene-note | 9 | 7 | 2 |
| history-note | 36 | 34 | 2 |
| keller-note | 27 | 25 | 2 |
| learning-note | 34 | 32 | 2 |
| relationships-note | 47 | 45 | 2 |
| habits-note | 45 | 44 | 1 |
| hbr-note | 46 | 45 | 1 |
| life-meaning-note | 40 | 39 | 1 |
| thinking-note | 58 | 57 | 1 |

## 逐筆清單

格式：`[status]` 書名 / 原文 · 分組 — 📕 書 repo 記的版次日（若有）

### behaviour-interview-note（3 筆）

- [owned] Mastering Behavioral Interviews · 行為面試核心
- [owned] Behavioral Interviews for Software Engineers · 行為面試核心
- [owned] The STAR Interview · 行為面試核心

### biblical-studies-note（8 筆）

- [owned] 21世紀聖經講道學 · 釋經方法與讀經
- [owned] 出埃及記的信息 / The Message of Exodus · 逐卷解經（BST 系列）
- [owned] 詩篇的信息（上）1–72 / The Message of Psalms 1–72 · 逐卷解經（BST 系列）
- [owned] 詩篇的信息（下）73–150 / The Message of Psalms 73–150 · 逐卷解經（BST 系列）
- [owned] 路加福音的信息 / The Message of Luke · 逐卷解經（BST 系列）
- [owned] 希伯來書的信息 / The Message of Hebrews · 逐卷解經（BST 系列）
- [owned] 雅各書的信息 / The Message of James · 逐卷解經（BST 系列）
- [skipped] NICNT／NICOT 系列代表卷 · 逐卷解經（BST 系列）

### career-note（8 筆）

- [owned] 將世界菁英的工作方式整理成冊 · 恆毅力與精通
- [owned] 馮唐成事心法 · 自我管理
- [owned] 創客創業導師程天縱的職場力：解析職場的人與事，提升工作與管理績效的34條建言 · 自我管理
- [owned] HBR Guide to Your Professional Growth · 自我管理
- [wanted] Where Will You Be in the Next Decade? · 意義與方向
- [owned] 軟體工程師的行為面試 / Behavioral Interviews for Software Engineers · 求職與轉職
- [owned] 精通行為面試：科技業說故事指南 / Mastering Behavioral Interviews: The Guide to Storytelling in Tech · 求職與轉職
- [owned] STAR 面試法 / The STAR Interview · 求職與轉職

### cloud-infra-note（6 筆）

- [owned] 網站可靠性工程師實務指南 / Site Reliability Engineering Handbook · SRE
- [owned] Observability (Beginner's Guide) · 可觀測性
- [owned] 鳥哥的 Linux 私房菜：基礎學習篇 · Linux 與網路
- [owned] 鳥哥的 Linux 私房菜：伺服器架設篇 · Linux 與網路
- [owned] MIS 一定要懂的 82個網路技術知識 · Linux 與網路
- [owned] 30 Days of GitLab · 工具鏈

### design-patterns-note（2 筆）

- [owned] 物件導向設計面試 / Object-Oriented Design Interview · GoF 正典與入門
- [owned] 程式設計範式與物件導向思維 · 範式視角

### fengtang-note（3 筆）

- [owned] 勝者心法：資治通鑑成事之道 · 成事心法系列
- [owned] 能人謀勢 · 成事心法系列
- [owned] 穩贏 · 管理與職場

### greene-note（2 筆）

- [skipped] 精華節錄版 / The Concise 48 Laws of Power ... · 權力與策略
- [unavailable] The Law of the Sublime · 精通與日課

### habits-note（1 筆）

- [owned] The Atomic Habits Workbook · 習慣迴路

### hbr-note（1 筆）

- [owned] HBR Guide Collection（合輯） · 溝通協作

### history-note（2 筆）

- [owned] 舊約背景與年代表 · 古代與起源
- [owned] 脈絡：小我與大勢 · 文明興衰

### keller-note（2 筆）

- [owned] 順服的主 · 福音核心
- [owned] 智慧之道 / The Way of Wisdom · 靈修與智慧

### leadership-note（11 筆）

- [owned] 彼得·杜拉克與管理學：歐洲、社會、思想 · 管理正典
- [skipped] 5分鐘商學院 管理篇 · 管理正典
- [owned] 我用軍隊學到的8堂領導課 / 8 Lessons in Military Leadership for Entrepreneurs · 帶人與團隊
- [owned] Sales Management: The Brian Tracy Success Library · 帶人與團隊
- [owned] 哈佛教你高EQ管理術 / HBR's 10 Must Reads on Emotional Intelligence · 帶人與團隊
- [owned] 哈佛商業評論：領導變革指南 / HBR Guide to Leading Through Change · 帶人與團隊
- [owned] HBR Guide to Retaining Your Best People · 帶人與團隊
- [owned] Meetings That Get Results · 帶人與團隊
- [owned] 可複製的領導力 · 教練與回饋
- [owned] 選民進化論 / Won't Get Fooled Again · 決策與判斷
- [owned] 黑道商學院 / I Will Make You an Offer You Can't Refuse · 領導者修練與權力

### learning-note（2 筆）

- [owned] 刻意進化 · 刻意練習與精熟
- [wanted] 人才，自造者 · 自學與超速學習

### life-meaning-note（1 筆）

- [owned] The Harvard Guide to a Healthy Life · 老化與有限性

### management-note（5 筆）

- [owned] 程天縱《經營學》 · 管理者的工作
- [owned] 程天縱《管理力》 · 管理者的工作
- [owned] 程天縱《專業力》 · 管理者的工作
- [owned] 5 分鐘商學院・管理工具篇 · 管理者的工作
- [owned] Peter Drucker Café 杜拉克咖啡館 · 管理者的工作

### marketing-note（3 筆）

- [owned] Social Media Marketing & Online Business · 社群與通路
- [owned] 峰值體驗 · 廣告與基本功
- [owned] 峰值體驗 2 · 廣告與基本功

### relationships-note（2 筆）

- [owned] 與家人的財務界線 · 界線
- [owned] 生命是長期而持續的累積 · 友誼與群體

### science-note（4 筆）

- [owned] 應用治療學：臨床用藥 / Applied Therapeutics · 專業教科書
- [owned] 藥物治療學：原理與實務 / Pharmacotherapy: Principles and Practice · 專業教科書
- [owned] 藥物治療學案例集 / Pharmacotherapy Casebook · 專業教科書
- [skipped] 牛津臨床藥學手冊 / Oxford Handbook of Clinical Pharmacy · 專業教科書

### startup-note（6 筆）

- [owned] Entrepreneurship · 機會與創新
- [owned] HBR on Entrepreneurship · 機會與創新
- [owned] The Fail-Safe Startup · 驗證與精實
- [owned] The 10X Entrepreneur · 創辦人實戰
- [owned] 6 Essentials to Start & Succeed in Your Own Business · 創辦人實戰
- [owned] Make Phenomenal Profits · 財務與退場

### system-design-note（3 筆）

- [owned] Grokking the System Design Interview · 面試實戰
- [owned] Grokking the Advanced System Design Interview · 面試實戰
- [owned] Mobile System Design Interview · 面試實戰

### theology-note（5 筆）

- [owned] 系統神學（章力生等華人卷） / Systematic Theology · 教義與系統神學
- [owned] 莫特曼神學 · 教義與系統神學
- [owned] 牧養是場冒險：靈性關顧12講 / Spiritual Care · 教會與牧養
- [owned] 20世紀神學評論 / 20th-Century Theology · 歷史神學
- [owned] Overcoming Sin and Temptation · 歷史神學

### thinking-note（1 筆）

- [owned] 萬維鋼《科學思考者》 / 科學思考者 · 思維模型

### tracy-note（12 筆）

- [owned] Think Big · 目標與成就
- [owned] Take Charge of Your Life · 目標與成就
- [owned] 運氣的法則 / The Laws of Luck · 目標與成就
- [skipped] 勵志小品群 / Kiss That Frog! / Crunch Point / Reinvention / Full Engagement! ... · 目標與成就
- [owned] Creativity and Problem Solving · 時間與執行
- [owned] Sales Management · 經營與領導
- [owned] Entrepreneurship · 經營與領導
- [owned] 6 Essentials to Start and Succeed in Your Own Business · 經營與領導
- [owned] Master Course for Business Success / Brian Tracy's Master Course for Business Success · 經營與領導
- [owned] Make Phenomenal Profits · 經營與領導
- [skipped] How the Best Leaders Lead / TurboStrategy · 經營與領導
- [owned] 立即致富 / Get Rich Now · 財富

### wellness-note（5 筆）

- [owned] 間歇性斷食減醣全書 · 飲食與睡眠
- [owned] 不再痛風的生活 · 飲食與睡眠
- [owned] 哈佛教你打造健康人生 · 飲食與睡眠
- [owned] 有本事 · 幸福與安適
- [owned] 了不起 · 幸福與安適

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
