# GUIDE-QUEUE — 導覽產出佇列（已收完書的站）

> 由 `/note-guide` 消化的工作佇列。**收錄條件：`wanted = 0`**（`unavailable`／`skipped` 不算欠收）。
> 產出前必讀 skill 正本的「防重複」節：已有 `src/content/guide/` 的站預設增量、絕不重做；
> 每站動工時順手把 notes-core pin＋lockfile bump 到 ≥ v0.35.0。
> 分批依據（note-guide 深度門檻）：主題站 ≥30 頁／人物站 ≥15 頁＝內容撐得起判讀；
> 10 頁以上可做但導讀章「待挖」比例高（誠實呈現即可）；<10 頁或有未溯源頁＝先 `note-check --enrich`。
> 本檔手動維護：完成一站就把它移進「已完成」。盤點重跑：`for d in notes/*/src/content/guide; do echo ${d%%/*}; done`

## 已完成

| 站 | 型 | owned | 頁 | 頁/書 | enriched | 備註 |
| --- | --- | ---: | ---: | ---: | --- | --- |
| leadership-note | 主題 | 94 | 54 | 0.6 | 2026-08-06 | writtenAt 2026-08-14；enrich 進行中（七本正典） |
| thinking-note | 主題 | 56 | 46 | 0.8 | — | writtenAt 2026-08-14 |
| covey-note | 人物 | 10 | 37 | 3.7 | 2026-08-04 | writtenAt 2026-08-14 |
| keller-note | 人物 | 23 | 23 | 1.0 | — | writtenAt 2026-08-14 |

## 第一批——站深料足，直接可做

| 站 | 型 | owned | 頁 | 頁/書 | enriched | 備註 |
| --- | --- | ---: | ---: | ---: | --- | --- |
| clean-code-note | 主題 | 25 | 69 | 2.8 | — |  |
| agile-note | 主題 | 15 | 61 | 4.1 | 2026-08-04 |  |
| design-note | 主題 | 12 | 46 | 3.8 | 2026-08-04 |  |
| economics-note | 主題 | 50 | 45 | 0.9 | — |  |
| startup-note | 主題 | 62 | 44 | 0.7 | — |  |
| design-patterns-note | 主題 | 20 | 43 | 2.1 | — |  |
| system-design-note | 主題 | 25 | 41 | 1.6 | — |  |
| writing-note | 主題 | 32 | 38 | 1.2 | — |  |
| communication-note | 主題 | 49 | 37 | 0.8 | 2026-07-31 |  |
| learning-note | 主題 | 33 | 34 | 1.0 | — |  |
| relationships-note | 主題 | 46 | 34 | 0.7 | — |  |
| growth-note | 主題 | 44 | 33 | 0.8 | — |  |
| business-strategy-note | 主題 | 50 | 31 | 0.6 | — |  |
| life-meaning-note | 主題 | 39 | 31 | 0.8 | — |  |
| behaviour-interview-note | 主題 | 20 | 30 | 1.5 | — |  |
| history-note | 主題 | 34 | 30 | 0.9 | — |  |
| tracy-note | 人物 | 36 | 25 | 0.7 | — |  |
| peterson-note | 人物 | 4 | 24 | 6.0 | — |  |
| navarro-note | 人物 | 6 | 23 | 3.8 | — |  |
| peck-note | 人物 | 9 | 17 | 1.9 | — |  |
| greene-note | 人物 | 7 | 16 | 2.3 | — |  |
| wan-weigang-note | 人物 | 11 | 15 | 1.4 | — |  |

## 第二批——可做；導讀章的「待挖」比例會偏高

| 站 | 型 | owned | 頁 | 頁/書 | enriched | 備註 |
| --- | --- | ---: | ---: | ---: | --- | --- |
| philosophy-note | 主題 | 33 | 24 | 0.7 | — |  |
| hbr-note | 主題 | 47 | 22 | 0.5 | 2026-07-31 |  |
| management-note | 主題 | 47 | 20 | 0.4 | 2026-08-01 |  |
| tools-note | 主題 | 46 | 20 | 0.4 | 2026-07-31 |  |
| problem-solving-note | 主題 | 26 | 17 | 0.7 | 2026-08-06 |  |
| image-style-note | 主題 | 7 | 13 | 1.9 | — |  |
| spiritual-formation-note | 主題 | 35 | 13 | 0.4 | 2026-07-31 |  |
| de-botton-note | 人物 | 12 | 12 | 1.0 | — |  |
| maxwell-note | 人物 | 18 | 12 | 0.7 | — |  |
| schwager-note | 人物 | 10 | 12 | 1.2 | — |  |
| stott-note | 人物 | 14 | 12 | 0.9 | — |  |
| uncle-bob-note | 人物 | 7 | 12 | 1.7 | — |  |
| kiyosaki-note | 人物 | 23 | 11 | 0.5 | 2026-08-06 |  |
| liurun-note | 人物 | 12 | 11 | 0.9 | — |  |
| fromm-note | 人物 | 16 | 10 | 0.6 | — |  |
| lewis-note | 人物 | 14 | 10 | 0.7 | — |  |
| newport-note | 人物 | 8 | 10 | 1.2 | — |  |
| wujun-note | 人物 | 18 | 10 | 0.6 | — |  |

## 先 enrich 再 guide（頁數不足或有溯源債）

| 站 | 型 | owned | 頁 | 頁/書 | enriched | 備註 |
| --- | --- | ---: | ---: | ---: | --- | --- |
| bogle-note | 人物 | 6 | 8 | 1.3 | — | 站太薄 |
| fengtang-note | 人物 | 10 | 8 | 0.8 | — | 站太薄 |
| nouwen-note | 人物 | 16 | 8 | 0.5 | — | 站太薄 |
| taleb-note | 人物 | 6 | 8 | 1.3 | — | 站太薄 |
| damodaran-note | 人物 | 5 | 7 | 1.4 | — | 站太薄 |
| nt-wright-note | 人物 | 11 | 7 | 0.6 | — | 站太薄 |
| templar-note | 人物 | 9 | 7 | 0.8 | — | 站太薄 |
| willard-note | 人物 | 8 | 7 | 0.9 | — | 站太薄 |
| pastoral-psychology-note | 主題 | 5 | 5 | 1.0 | — | 未溯源 5 頁，先還債 |
| christensen-note | 人物 | 9 | 4 | 0.4 | — | 站太薄 |
| collins-note | 人物 | 6 | 3 | 0.5 | — | 站太薄 |
| grant-note | 人物 | 5 | 3 | 0.6 | — | 站太薄 |
| grove-note | 人物 | 5 | 3 | 0.6 | — | 站太薄 |
| jung-note | 人物 | 7 | 3 | 0.4 | — | 站太薄 |
| kent-beck-note | 人物 | 6 | 3 | 0.5 | — | 站太薄 |
| fowler-note | 人物 | 6 | 2 | 0.3 | — | 站太薄 |

