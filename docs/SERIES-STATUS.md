# SERIES-STATUS — check → enrich → guide 系列帳本

**這份是什麼**：全星系「書收齊＋相關書都做完（content fill＋deep overview）」的站，推進
**check → enrich → guide** 產線的執行帳本。

**站側數字是重算的，不是手打的**（2026-08-28 起）：`tools/galaxy-checkup.py --json` 一次掃完
75 站（頁數／溯源／mastery／roadmap／findings），導覽日期取 `src/content/guide/*.md` 的最大
`writtenAt`，owned 數來自各站 `bibliography.ts`。要刷新就重跑那支再更新本檔——
08-20 那輪用的一次性 scratchpad 腳本已被它取代。**書端也已工具化**（2026-08-28 起）：
空葉章用 `hugo-book-manager/scripts/audit-empty-leaves.py --all`、深度概覽用同目錄的
`audit-overview.py`；本檔留著手動維護的只剩「這筆債要不要現在還」的判斷。

**與其他 docs 的分工**：[GUIDE-QUEUE.md](./GUIDE-QUEUE.md)＝`/note-guide` 佇列正本；
[DEEPEN-READY.md](./DEEPEN-READY.md)＝每次重算的自動排序表；本檔＝**系列定義＋站側快照＋書端卡點＋進度**。

> **注意 leetcode-note 不在這 75 站裡**：它 2026-07 起自維護前端（`src/content/` 是
> `guides`／`overviews`／`problems`，沒有 `concepts`），`galaxy-checkup` 不掃它，本系列也不涵蓋。

## 系列判準（2026-08-20 對帳定案）

- **收書歸零**：bibliography `wanted = 0`（`unavailable`／`skipped` 不算欠）。
- **書端完工**：owned 全數 ① deep overview 品檢 PASS（`audit-overview.py`）② content fill 完成。
  content fill **以本機實測為準**——portal `health.json`（08-18 產）過期，21 本 08-19～20 剛填完的書被誤標 thin/near-empty。
  **真欠債**葉章 ≥2 的書算未完；恰 1 個（多為附錄）不擋站、只註記；watch 級（8–15k 字）不擋。
  「真欠債」由 `audit-empty-leaves.py` 判定——交叉參照條目與原書就沒有的章不算（見書端卡點節）。

**結果（2026-08-28 收官）：達標 75 站全數 `wanted = 0`、站側 findings 0，導覽 75/75 全數完工**
——B 組六站當日補齊（pf／lm／cloud／gardner／fengtang／pastoral），guide 產線收官。
書端仍有 7 本帶真空葉章的書（見下表，2026-08-28 全庫重掃後的數字），書端補洞是獨立的
Opus 線，不再擋任何站。

## A 組——導覽已完工（69 站，2026-08-28 重算）

依導覽 `writtenAt` 排序。全數 `wanted = 0`、溯源 100%、`galaxy-checkup` findings 0。

| 站 | 型 | owned | 頁 | 頁/書 | 溯源 | mastery | roadmap | 導覽完成 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `greene-note` | 人物 | 7 | 18 | 2.57 | 100% | 100% | 100% | 2026-08-15 |
| `kent-beck-note` | 人物 | 6 | 14 | 2.33 | 100% | 100% | 100% | 2026-08-15 |
| `lewis-note` | 人物 | 14 | 12 | 0.86 | 100% | 100% | 100% | 2026-08-15 |
| `peterson-note` | 人物 | 4 | 24 | 6.00 | 100% | 100% | 100% | 2026-08-15 |
| `stott-note` | 人物 | 14 | 14 | 1.00 | 100% | 100% | 100% | 2026-08-15 |
| `fowler-note` | 人物 | 6 | 9 | 1.50 | 100% | 100% | 100% | 2026-08-21 |
| `grove-note` | 人物 | 5 | 12 | 2.40 | 100% | 100% | 100% | 2026-08-21 |
| `nouwen-note` | 人物 | 16 | 12 | 0.75 | 100% | 100% | 100% | 2026-08-21 |
| `tracy-note` | 人物 | 36 | 27 | 0.75 | 100% | 100% | 100% | 2026-08-21 |
| `willard-note` | 人物 | 8 | 12 | 1.50 | 100% | 100% | 100% | 2026-08-21 |
| `bogle-note` | 人物 | 6 | 14 | 2.33 | 100% | 100% | 100% | 2026-08-24 |
| `christensen-note` | 人物 | 9 | 14 | 1.56 | 100% | 100% | 100% | 2026-08-24 |
| `clean-code-note` | 主題 | 25 | 75 | 3.00 | 100% | 100% | 100% | 2026-08-24 |
| `cloud-infra-note` | 主題 | 26 | 44 | 1.69 | 100% | 100% | 100% | 2026-08-24 |
| `covey-note` | 人物 | 10 | 40 | 4.00 | 100% | 100% | 100% | 2026-08-24 |
| `damodaran-note` | 人物 | 5 | 13 | 2.60 | 100% | 100% | 100% | 2026-08-24 |
| `data-systems-note` | 主題 | 19 | 53 | 2.79 | 100% | 100% | 100% | 2026-08-24 |
| `design-note` | 主題 | 12 | 49 | 4.08 | 100% | 100% | 100% | 2026-08-24 |
| `design-patterns-note` | 主題 | 20 | 46 | 2.30 | 100% | 100% | 100% | 2026-08-24 |
| `drucker-note` | 人物 | 19 | 17 | 0.89 | 100% | 100% | 100% | 2026-08-24 |
| `economics-note` | 主題 | 50 | 51 | 1.02 | 100% | 100% | 100% | 2026-08-24 |
| `hbr-note` | 主題 | 46 | 30 | 0.65 | 100% | 100% | 100% | 2026-08-24 |
| `investing-note` | 主題 | 62 | 45 | 0.73 | 100% | 100% | 100% | 2026-08-24 |
| `keller-note` | 人物 | 23 | 24 | 1.04 | 100% | 100% | 100% | 2026-08-24 |
| `navarro-note` | 人物 | 6 | 25 | 4.17 | 100% | 100% | 100% | 2026-08-24 |
| `nt-wright-note` | 人物 | 11 | 10 | 0.91 | 100% | 100% | 100% | 2026-08-24 |
| `peck-note` | 人物 | 9 | 17 | 1.89 | 100% | 100% | 100% | 2026-08-24 |
| `philosophy-note` | 主題 | 32 | 34 | 1.06 | 100% | 100% | 100% | 2026-08-24 |
| `security-note` | 主題 | 14 | 14 | 1.00 | 100% | 100% | 100% | 2026-08-24 |
| `templar-note` | 人物 | 9 | 13 | 1.44 | 100% | 100% | 100% | 2026-08-24 |
| `tools-note` | 主題 | 46 | 30 | 0.65 | 100% | 100% | 100% | 2026-08-24 |
| `uncle-bob-note` | 人物 | 7 | 16 | 2.29 | 100% | 100% | 100% | 2026-08-24 |
| `wan-weigang-note` | 人物 | 11 | 16 | 1.45 | 100% | 100% | 100% | 2026-08-24 |
| `writing-note` | 主題 | 32 | 41 | 1.28 | 100% | 100% | 100% | 2026-08-24 |
| `grant-note` | 人物 | 5 | 15 | 3.00 | 100% | 100% | 100% | 2026-08-26 |
| `jung-note` | 人物 | 7 | 17 | 2.43 | 100% | 100% | 100% | 2026-08-26 |
| `agile-note` | 主題 | 15 | 66 | 4.40 | 100% | 100% | 100% | 2026-08-27 |
| `behaviour-interview-note` | 主題 | 20 | 36 | 1.80 | 100% | 100% | 100% | 2026-08-27 |
| `biblical-studies-note` | 主題 | 107 | 83 | 0.78 | 100% | 100% | 100% | 2026-08-27 |
| `business-strategy-note` | 主題 | 50 | 38 | 0.76 | 100% | 100% | 100% | 2026-08-27 |
| `career-note` | 主題 | 68 | 51 | 0.75 | 100% | 100% | 100% | 2026-08-27 |
| `collins-note` | 人物 | 7 | 15 | 2.14 | 100% | 100% | 100% | 2026-08-27 |
| `communication-note` | 主題 | 49 | 39 | 0.80 | 100% | 100% | 100% | 2026-08-27 |
| `de-botton-note` | 人物 | 11 | 15 | 1.36 | 100% | 100% | 100% | 2026-08-27 |
| `fromm-note` | 人物 | 16 | 15 | 0.94 | 100% | 100% | 100% | 2026-08-27 |
| `growth-note` | 主題 | 44 | 35 | 0.80 | 100% | 100% | 100% | 2026-08-27 |
| `habits-note` | 主題 | 44 | 33 | 0.75 | 100% | 100% | 100% | 2026-08-27 |
| `history-note` | 主題 | 34 | 32 | 0.94 | 100% | 100% | 100% | 2026-08-27 |
| `image-style-note` | 主題 | 7 | 13 | 1.86 | 100% | 100% | 100% | 2026-08-27 |
| `kiyosaki-note` | 人物 | 23 | 14 | 0.61 | 100% | 100% | 100% | 2026-08-27 |
| `leadership-note` | 主題 | 94 | 70 | 0.74 | 100% | 100% | 100% | 2026-08-27 |
| `learning-note` | 主題 | 33 | 36 | 1.09 | 100% | 100% | 100% | 2026-08-27 |
| `liurun-note` | 人物 | 12 | 13 | 1.08 | 100% | 100% | 100% | 2026-08-27 |
| `management-note` | 主題 | 47 | 30 | 0.64 | 100% | 100% | 100% | 2026-08-27 |
| `marketing-note` | 主題 | 31 | 32 | 1.03 | 100% | 100% | 100% | 2026-08-27 |
| `maxwell-note` | 人物 | 18 | 14 | 0.78 | 100% | 100% | 100% | 2026-08-27 |
| `newport-note` | 人物 | 8 | 10 | 1.25 | 100% | 100% | 100% | 2026-08-27 |
| `problem-solving-note` | 主題 | 26 | 19 | 0.73 | 100% | 100% | 100% | 2026-08-27 |
| `relationships-note` | 主題 | 46 | 40 | 0.87 | 100% | 100% | 100% | 2026-08-27 |
| `schwager-note` | 人物 | 9 | 12 | 1.33 | 100% | 100% | 100% | 2026-08-27 |
| `science-note` | 主題 | 48 | 29 | 0.60 | 100% | 100% | 100% | 2026-08-27 |
| `spiritual-formation-note` | 主題 | 35 | 21 | 0.60 | 100% | 100% | 100% | 2026-08-27 |
| `startup-note` | 主題 | 62 | 51 | 0.82 | 100% | 100% | 100% | 2026-08-27 |
| `system-design-note` | 主題 | 25 | 48 | 1.92 | 100% | 100% | 100% | 2026-08-27 |
| `taleb-note` | 人物 | 6 | 15 | 2.50 | 100% | 100% | 100% | 2026-08-27 |
| `theology-note` | 主題 | 64 | 38 | 0.59 | 100% | 100% | 100% | 2026-08-27 |
| `thinking-note` | 主題 | 56 | 68 | 1.21 | 100% | 100% | 100% | 2026-08-27 |
| `wellness-note` | 主題 | 33 | 19 | 0.58 | 100% | 100% | 100% | 2026-08-27 |
| `wujun-note` | 人物 | 18 | 17 | 0.94 | 100% | 100% | 100% | 2026-08-27 |

## B 組——已收官（2026-08-28 六站導覽全數補齊）

六站站側指標本就乾淨（溯源／mastery／roadmap 皆 100%、findings 0、wanted 0），
2026-08-28 由 Fable 依 5-fork 產線一日補齊導覽——下次 `galaxy-checkup.py --json` 重算時
這六站會自然併入 A 組表，本節屆時可刪。

| 站 | 型 | owned | 頁 | 頁/書 | 溯源 | mastery | roadmap | 導覽完成 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `personal-finance-note` | 主題 | 40 | 36 | 0.90 | 100% | 100% | 100% | 2026-08-28 |
| `life-meaning-note` | 主題 | 39 | 34 | 0.87 | 100% | 100% | 100% | 2026-08-28 |
| `cloud-note` | 人物 | 13 | 15 | 1.15 | 100% | 100% | 100% | 2026-08-28 |
| `gardner-note` | 人物 | 13 | 13 | 1.00 | 100% | 100% | 100% | 2026-08-28 |
| `fengtang-note` | 人物 | 10 | 12 | 1.20 | 100% | 100% | 100% | 2026-08-28 |
| `pastoral-psychology-note` | 主題 | 5 | 8 | 1.60 | 100% | 100% | 100% | 2026-08-28 |

詳帳見 ENRICH-BACKLOG「導覽補齊輪・第二十七、二十八站」與「第二十九～三十二站」兩則
（含 fork 驗證網抓到的站內既有錯誤：gardner「25 年」、fengtang 金線用字、pastoral REACH 溯源還債）。

## 書端卡點（2026-08-28 全庫重掃，判準已修正）

判準同上：空葉章 ≥2 算未完；恰 1 個空葉不擋站、只註記。空葉＝該章 `_index.md` 去掉
frontmatter 後不足 200 字元。深度概覽用 `hugo-book-manager/scripts/audit-overview.py` 驗。

> **空葉不能只用字數判——2026-08-28 為此重掃過一次全庫。** 字數門檻只是「值得看一眼」
> 的觸發器，體裁決定一章該多長。正本工具是 `hugo-book-manager/scripts/audit-empty-leaves.py`
> （`--all` 掃全庫），它把短葉章分四類，只有前兩類算債：`placeholder`（寫著待補）、
> `blank`（完全沒內文）算債；`xref`（辭典的「參見 X」交叉參照）、`source-absent`
> （原書此版本就沒這章）不算債；其餘 `thin` 列出來給人判。
> 首掃 1829 本：**真欠債 56 章，另有 237 章是被門檻撈出來、體裁本來就短的**。
>
> 兩個活標本說明為什麼非分類不可：`dictionary-of-paul` 的 231 條「空葉」**全部**是
> 「阿們 → 參見 Prayer」這種交叉參照，那就是該條的完整內容，真欠債 **0**；
> `on-top-of-tides` 的 5 章則是原書該版本只列章名、正文標「待續」，書上就沒有，補不了。
> 兩本都已從下表移除。
>
> **portal 的 `health.json` 也代替不了這張表**（但原因不同）：它的分級只吃兩個**聚合**
> 數字——總字數與平均密度（`fetch-health.ts` 的 `tierOf(chars, density)`）。聚合值看不見
> 分佈，所以條目型的書半數條目再短也照樣判 `ok`。反過來它判 thin 的書多半真薄，可以信。

| 書 | 葉章 | 真欠債 | 卡哪一站 | 現況 |
| --- | ---: | ---: | --- | --- |
| `cost-of-discipleship` | 34 | 10 | theology、spiritual-formation | 9 章全空＋附錄佔位；兩站導覽皆已完工 |
| `new-market-wizards` | 29 | 7 | schwager | 7 篇訪談章全空；導覽已完工 |
| `microservices-patterns` | 29 | 7 | design-patterns、system-design | 兩站導覽皆已完工 |
| `weight-of-glory` | 14 | 3 | lewis、spiritual-formation | 兩站導覽皆已完工 |
| `building-microservices` | 17 | 2 | system-design | 原判 3，其一為「原書定稿無附錄」不算債 |
| `message-of-hosea` | 19 | 2 | biblical-studies | **2026-08-28 全庫掃描才發現**——舊掃描漏了 |
| `world-waiting-to-be-born` | 23 | 2 | peck | 導覽已完工 |

**孤兒書那側另有 3 本帶欠債，但不卡任何站**（沒有站認領，見 [ORPHAN-BOOKS.md](./ORPHAN-BOOKS.md)）：
`trend-following-masters-volume-2`（空 2）、`what-life-should-mean-to-you`（空 2）、
`flying-together-a-christian-marriage-guide`（佔位 1＋待判 2）。**認領它們之前不必補**。

> **舊掃描為什麼會漏**：它是從「站的 owned 書」出發的，孤兒書天生不在掃描範圍內。
> `--all` 從書庫那側掃才看得見——與 ORPHAN-BOOKS 是同一種反向視角。

**這一輪清掉的卡點（08-20 還掛著、現已通過）**：`christian-theology-introduction`、
`contemplative-pastor`、`reformed-dogmatics`（theology）與 `automatic-millionaire`
（personal-finance）四本的深度概覽**全數 `audit-overview.py` PASS**、葉章 0 空。
**personal-finance-note 因此完全解鎖**——它是 B 組裡唯一曾被書端擋住的站。
`further-along-the-road-less-traveled`（peck）仍躺在 `archive/`、books-done 查無，除役或補寫待裁決。

## 必改帳（2026-08-20 清帳輪結果）

1. ✅ **schwager-note**（`46b107a`，build 綠）：查明是**版本併帳**不是打錯字——repo `complete-guide-to-futures-markets`
   實為 2017 二版（出版日／Amazon 連結／七章結構皆符），初版與二版卻各立一筆 owned。已併成一筆 owned（二版，真 slug）、
   另一筆改 skipped 留譯名對照；三頁中兩頁的重複引用刪除、technical-analysis 一筆改錨 `02-technical-analysis`。
2. ✅ **de-botton-note**（`e5a74da`，build 綠）：同書雙譯本各立 owned、repo 只有一個——《我愛身分地位》改 skipped 留帳對照，
   站以《身份的焦慮》（`status-anxiety`）收錄。
3. ✅ **newport-note**（`2974408`，build 綠）：書端已把錯配 repo 換回真 Superstar 正文、另立 `how-to-win-at-college`
   （repo log `69dbca4`），站帳沒跟上——「深度學習力」重複筆改 skipped、Superstar 由 unavailable 轉 owned＋slug；
   死 anchor 換成 win-at-college 實錨兩筆（ch11 精通一項技能／ch16 grand project，皆 grep 核實）。
4. ✅ **career-note**（`8b5d448`，build 綠）：查明**母書整本不在書庫**（內容出自大人學談「拿掉名片」的那本，
   《大人學選擇》筆記無這些主張、掛上去＝假溯源）。Andrew 裁決照 self-made-talent 前例**移除頁面、收書後重寫**——
   頁已刪、roadmap／related／內文連結全同步（站內 0 殘留），《沒了名片，你還剩下什麼？》列 wanted 追帳。
   副作用：career-note wanted 0→1，暫退出達標系列（見上表）。
   **2026-08-27 後記**：那本收不到，Andrew 判 `unavailable`——wanted 回到 0、career-note 重新達標；
   概念頁維持不寫（未溯源紀律不因狀態改變而放寬），書真的到手再回原文核對重寫。

（pastoral-psychology 的 5 頁全未溯源＋3 本引用書不存在＝enrich 級工程，不算小帳，見 ③檔。）

## 逐站 findings（2026-08-28 重掃）

**全星系 75 站：blocker 0／warn 0／nit 0。** 08-20 快照裡的那批（economics 7 個孤兒頁、
learning 6 個、各站 related 單向數十筆⋯⋯）已在 08-26 體檢輪與其後各輪清畢，明細不再留檔——
要看現況直接跑 `notes-core/tools/galaxy-checkup.py`，它就是這一節的正本。

## 推進流程設計（2026-08-20 定案）

**check 的機械半已集中做完（就是本檔快照），不再逐站單跑一次完整 `/note-check`**；認站、學語氣、
§1.3 該挖分層這些 LLM 級前置，由 guide／enrich 代理進場時自然吸收——它們本來就要讀全站與 owned books，
單獨先跑一輪 check 等於同一筆閱讀花兩次錢。分四種批型：

0. **清帳輪（先做，幾乎零 token）**：上面必改 4 筆，各站單獨 commit。nit 級（related 單向等）**不**集中清——
   進站的代理順手 `--fix` 蓋 `checkedAt` 即可，省得一輪碰 27 個 repo。
1. **厚站波（①檔 → ②檔，表內由上而下）**：照 08-15 驗證的量產模式——
   **一站一代理跑完整 `/note-guide` → enrich 波還導覽點名的債 → 主代理獨立驗收**
   （anchor `[-d]` 逐一驗、dist 連結、具名事實 grep 防杜撰、`git status` 全清、pin＋lockfile 同 bump）後 commit＋push。
   一波 3–5 站、以額度為界，斷點用 SendMessage 續跑。
   蓋章紀律：guide 蓋 `writtenAt`、enrich 蓋 `enrichedAt`、`--fix` 蓋 `checkedAt`。
2. **薄站一條龍（③檔）**：單站 `note-check --enrich` 拓站鋪思想弧線 → 接力 `/note-guide` 直接沿用
   （jung 3→14 頁／kent-beck／taleb 驗證過）。**pastoral-psychology 先還溯源債**（5 頁回原文改寫＋3 本書單修正）再談導覽。
3. **書端另一條線（不佔 note 產能，可平行）**：`books-done/tmp/` 下跑 `/book-generate-deep-overview`（3 本，做完自動歸檔）
   ＋ `/book-promote-to-tmp` 收 `christian-theology-introduction`；空章書逐本補寫。
   清一站的帳就依上表「清帳後入檔」欄把該站放進對應檔次。

完成一站：本檔該行「導覽完成」欄填日期，GUIDE-QUEUE 同步搬「已完成」。

## 跨站遺留帳

- **導覽補齊輪完工（2026-08-27，Fable）**：一天 26 站，全星系導覽覆蓋 43 → **69/75**。
  同日 Opus 補完末四站深化（cloud／gardner／fengtang／pastoral 共 11 頁），四站進 B 組待導覽。
  **B 組另外兩站是排程漏接**：life-meaning 躺在 GUIDE-QUEUE 第一批沒被領走、
  personal-finance 卡的書端已解除（見「書端卡點」節）——兩站現在都可直接寫導覽。

- **內文死鏈輪（2026-08-28，Opus）**：101 條 `](../x/y/)` 靜默 404 散在 23 站，一輪清零；
  檢查固化成 `galaxy-checkup` 的 `dead-inline-link`。詳帳見 ENRICH-BACKLOG。

- **第五波完工（2026-08-21）**：grant／bogle／damodaran／templar／willard 五站一條龍全 push（ad68bd5／cd2d8fe／c1359bf／33005e2／bd8c26d）。
  戰績：3→13（potential＋resilience）、8→14（vanguard）、7→13（dark-side＋philosophy）、7→13（home）、7→12（renovation 線補齊），合計 32→65 頁。
  **本波 B 型債豐收 23 筆**（bogle 10＋templar 6＋willard 7，見 SOURCING-DEBT）——bogle 抓到一句三書查無的杜撰引語，willard 抓到兩個外加比喻冒充書語。
  途中三度撞額度（Fable 5／weekly／session），SendMessage 續跑＋子代理直接寫檔紀律全程生效，零重工。
  backlog（導覽 ch3 點名）：grant 各書人際層、damodaran 金融股／困境公司、templar People 第二頁、bogle 無。

- **第四波完工（2026-08-21）**：grove／collins／christensen 三站一條龍全 push（16026a3／7f3ab18／7205252）。
  戰績：3→12、3→12（新開 decline）、4→14（新開 applications），合計 10→38 頁。內容債僅 1 筆（collins AMD，見 SOURCING-DEBT）。
  現成 backlog（roadmap planned 節點，下輪增量 enrich 素材）：grove OPS「六力與 10 倍速」、collins return-on-luck＋HTMF stage-4（grasping-for-salvation）。
  collins 新增 wanted：turning-the-flywheel（飛輪單行本）。

- **第三波完工（2026-08-21 02:06）**：Andrew 親選五站全 push——drucker guide、nt-wright／fowler／nouwen／security 一條龍。
  途中全部代理撞兩次 session 額度，靠 SendMessage 續跑＋主代理代落盤子代理成稿救回零重工。**新紀律**：子代理起草必須直接寫檔、
  不能只回傳文字（security 兩份遲到稿因錨點對不上被棄用）。待裁決：security 的 malware／防守方線（practical-malware-analysis 零引用）要不要開分類。

- **cloud-infra 兩本無分類承接的書——Andrew 2026-08-21 裁決判姊妹站分工，不開新分類**：
  Building Secure and Reliable Systems → security-note（已收 owned、有 security-engineering 分類；它是 ③檔拓站的好材料）、
  Team Topologies → agile-note（已收 owned、導覽已完工，下次增量 enrich 處理）。cloud-infra 導覽第三章的判層
  從「落點薄，如實記帳」改「姊妹站分工」＝帳平（照 keller／navarro「未挖 ≠ 欠債」前例）。

- ~~GUIDE-QUEUE 12 站已達標未登錄~~：2026-08-21 已補齊——5 站已進「已完成」，餘 7 站（career、habits、marketing、science、
  wellness、cloud、gardner）補進對應批次表。
- portal `health.json`（08-18）過期：21 本剛填完的書仍標 thin/near-empty，書站部署後重跑 fetch-health。
  （本檔的書端數字一律本機實測，不吃 health.json——這條只影響 portal 顯示。）
- `archive/further-along-the-road-less-traveled`：躺在 archive/ 但 GitHub repo 未 archive、topics 照舊——除役還是補寫，待裁決。
- ~~`dictionary-of-paul-and-his-letters` 是否 waive 待裁決~~：2026-08-28 Andrew 裁決**不 waive、親自重寫中**
  （448 條目空 231）。這筆從 08-20 就掛在待裁決欄整整八天沒被端上檯面——**待裁決欄會沉底**，
  每輪收工時該主動把它念出來，不要只留在文件裡等人翻。
- 恰 1 空葉的書（不擋站、記帳）：four-loves（附錄）、lessons-of-history（ch3）、time-management、hearing-god、
  boundaries-in-dating、encounters-with-jesus 等 20 本，多為附錄或單章，逐站進場時順手判定補或放。

## 掃描涵蓋範圍與重跑方式

**站側（機器判得準的那半）已固化成 `notes-core/tools/galaxy-checkup.py`**，08-20 那份
一次性 scratchpad 腳本退役。它涵蓋：§1.1 五指標、§1.2 雙向溯源（頁無 anchor＋anchor 對
books-done 實檔驗證＋book slug 存在）、§2 結構（首頁契約、divergence、core pin、分類
`_index.md`、roadmap↔內容、mastery slug、label 分隔號、related 存在＋雙向、seeAlso 實檔、
importance/status 值域、跳脫實體、`:::response`），2026-08-28 起再加**內文相對連結**
（`dead-inline-link`——seeAlso 之外的第二種靜默 404，首掃 101 條）。

**仍要進場逐站做的**：學語氣、§1.3 該挖而未挖分層、§3 backlog 撰寫、§2.5 抽驗防杜撰、
§2.8 build/format/lint。所以跑 checkup **不蓋 `checkedAt`**——蓋章留給進站跑完整
`/note-check` 的那次。

**重跑本檔**：`galaxy-checkup.py --json` 出站側數字，書端那張表要手工重掃空葉章＋
`audit-overview.py`。兩邊都更新完再改本檔的日期標記。
