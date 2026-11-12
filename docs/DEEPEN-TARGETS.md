# 深挖對象：大部頭卻只有一鏟的正典

> **生成於 2026-11-13T01:23:56+08:00**｜由 `tools/export-deepen-targets.py` 產生，**不要手改**——改資料源再重跑。

**這份是什麼**：書的層級的排序表——**進站之後該挖哪本書**。與 [DEEPEN-READY.md](./DEEPEN-READY.md) 的分工：那份回答「該進哪一站」（站的層級），這份回答「進站之後挖哪一本」。兩份都是排序表，工作日誌在 [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md)。

**為什麼需要它**：判層債歸零後，「哪裡還薄」失去了現成訊號——`tier-audit` 只抓「spine 且**零**引用」，**被引 1 次的 spine 一律放行**，而那正是大部頭最常見的狀態。theology-note 49 本 spine 每本恰好 1 頁、management-note 42 本裡 37 本只有 1 頁：健康，但薄得看不出來。

**判準**：`tier: spine`、書 repo 章節數 ≥ **30**（書庫 1776 本的中位數是 18、90 百分位是 48）、且站上引到它的**不同頁數 ≤ 1**。排序鍵是 `章節數 ÷ 頁數`。

**這份只排序，不開單。** 每頁該切哪個概念、跟既有頁怎麼分工、anchor 落哪幾章，仍是進站跑 `/note-check --enrich` 時的判斷（依 MODEL-ROUTING 留給 Fable 開單）。

## 摘要

| 項目 | 數 |
| --- | ---: |
| 掃過的站 | 78 |
| **候選（大部頭 × ≤1 頁）** | **3** |
| 涉及的站 | 2 |
| 依體裁排除 | 14 |
| 已裁定不開 | 18 |

## 一、前 30 名（跨站總排序）

| # | 章節 | 頁 | 站 | 書 |
| ---: | ---: | ---: | --- | --- |
| 1 | 40 | 1 | `data-science-note` | 數學之美 |
| 2 | 37 | 1 | `data-science-note` | Noise 雜訊 |
| 3 | 30 | 1 | `security-note` | Practical Malware Analysis |

## 二、依站分組

開單時整站一起看比較省力——同一站的候選常常共享脈絡。

### `data-science-note`（2 本）

- **數學之美** — 40 章 / 1 頁（`wujun-beauty-of-math`）
- **Noise 雜訊** — 37 章 / 1 頁（`noise`）

### `security-note`（1 本）

- **Practical Malware Analysis** — 30 章 / 1 頁（`practical-malware-analysis`）

## 三、依體裁排除：14 本

這些書章節數必然很高，但體裁上就不該挖成多頁——不排除會永遠霸佔排行前段。清單在 `export-deepen-targets.py` 的 `EXCLUDED_KINDS`；加新的要寫**體裁**理由，「暫時不想挖」屬於選題，不該寫進工具。

- `behaviour-interview-note` — 軟技能：soft skills，讓你不過時、不貶值、不消失：多作者書信合輯，三十封各自獨立
- `biblical-studies-note` — 聖經導覽手冊：逐卷讀經的藝術：逐卷導覽，按卷查閱
- `biblical-studies-note` — 聖經經典500問：逐條釋疑合輯，按經文查閱
- `fengtang-note` — 穩贏：中年隨筆結集，六十九篇各自獨立
- `habits-note` — 365 Days With Self-Discipline：日課型，365 則每日短文按週合輯
- `history-note` — 古拉格群島：文學性紀實巨著
- `jung-note` — 紅書：幻象記錄，章節是幻象序列與評註，概念已由導論抽出
- `lewis-note` — The Screwtape Letters：書信體，31 封短信各千餘字
- `lewis-note` — 納尼亞傳奇（七部曲）：小說七部曲
- `liurun-note` — 5分鐘商學院 工具篇：工具條目合輯，每條各自獨立
- `startup-note` — Rework 工作大解放：格言體雜文集，近九十節各一兩頁、只給立場不給流程
- `theology-note` — 當代神學辭典：神學辭典，按條目查閱
- `thinking-note` — The Art of Thinking Clearly 思考的藝術：轉譯型偏誤短文合輯，近百則互不相承
- `wellness-note` — Tools of Titans 巨人的工具：訪談語錄合輯，一人一條目，按人物查閱

## 四、已裁定不開：18 本

開單時逐本看過、判第一鏟已兌現、歸姊妹站或材料太薄的書。這是選題判斷，不是體裁；清單在 `export-deepen-targets.py` 的 `SETTLED_BOOKS`，理由失效就從表上刪掉。

- `agile-note` — Impact Mapping（2026-11-12）：章多而薄，兩個實質部已用；剩下是與既有實踐的定位章
- `career-note` — 精通行為面試：科技業說故事指南（2026-11-12）：behaviour-interview-note 四十一頁是體系深挖，本站是總覽頁
- `clean-code-note` — Test-Driven Development（2026-11-12）：kent-beck-note 五頁已挖完三部
- `habits-note` — How to Have a Good Day（2026-11-12）：生產力四章是技巧清單，兩招是 Eyal 轉述而原典頁已在
- `hbr-note` — HBR Guide to Making Every Meeting Matter（2026-11-12）：第一鏟已走完會議全生命週期，領導高峰會章收成 details
- `hbr-note` — HBR Guide to Navigating the Toxic Workplace（2026-11-12）：三十三章已用約二十章，其餘各一千字湊不成主張
- `leadership-note` — Turn the Ship Around!（2026-11-12）：四部都有頁：本站 leader-leader 掛一二部、management-note 掛三四部
- `life-meaning-note` — Bigger Leaner Stronger（2026-11-12）：飲食端第二鏟歸 wellness，本站不收飲食頁
- `life-meaning-note` — Flow 心流（2026-11-12）：本站只取第十章意義的鍛造一頁，心流技術面的其餘各章在 tools-note 三頁
- `management-note` — The Five Dysfunctions of a Team 團隊領導的五大障礙（2026-11-06）：模型與工具已在本站一頁、寓言歸 leadership 三頁，剩下是故事重述
- `newport-note` — How to Win at College（2026-11-12）：兩條原則已在 pseudo-work 與 career-capital-over-passion 的成熟版
- `personal-finance-note` — The Millionaire Fastlane 快速致富（2026-11-12）：第一鏟四部用盡，剩自我管理與創業執行不屬理財站
- `science-note` — 高手相對論（2026-11-12）：同上，與 wan-weigang-note 共用一次裁定
- `startup-note` — Anything You Want（2026-11-12）：授權四章不到四千字，收進 purpose-over-money 的 details
- `theology-note` — 活的教會（2026-11-06）：第一鏟已用八章裡的七章，講道章歸 stott-note
- `travel-note` — How to Be a Travel Writer（2026-11-12）：速成課已用，其餘是投稿、SEO、謀生與資源清單
- `travel-note` — Istanbul: Memories and the City（2026-11-12）：呼愁骨幹已用，其餘三十章是家族回憶與畫家專欄
- `wan-weigang-note` — 高手相對論（2026-11-12）：14 章 56 小節各數百字，章節數是小節撐高的；兩站兩頁已覆蓋物理骨幹與不變量世界觀

## 重跑

```bash
notes-core/tools/export-deepen-targets.py
```

補完某本書的第二頁之後重跑，該筆就會從這裡消失。
