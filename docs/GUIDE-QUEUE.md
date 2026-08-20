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
| leadership-note | 主題 | 94 | 62 | 0.7 | 2026-08-15 | writtenAt 2026-08-15；七本正典已挖，開變革線（Coverage 未挖 33） |
| thinking-note | 主題 | 56 | 60 | 1.1 | 2026-08-15 | writtenAt 2026-08-15；十三本正典一次還清（Kahneman 線×3、判斷偏誤×5、Barrett、Greene、Seth、語言辯論×2），Coverage 未挖 27→14，餘為支架／姊妹站分工 |
| covey-note | 人物 | 10 | 38 | 3.8 | 2026-08-15 | writtenAt 2026-08-15；PCL 已開採，未挖僅剩 Families（應用衍生，合理不挖） |
| keller-note | 人物 | 23 | 23 | 1.0 | — | writtenAt 2026-08-14；未挖 5 本全為靈修日課／選集＝工具書層，該挖=0，判定免 enrich |
| peterson-note | 人物 | 4 | 24 | 6.0 | — | writtenAt 2026-08-15；四本全脊梁全挖、wanted=0，全星系挖最深的人物站之一 |
| clean-code-note | 主題 | 25 | 71 | 2.8 | 2026-08-15 | writtenAt 2026-08-15；挖 10（＋Pragmatic、GOOS——mock 官司兩造到齊）、待挖 15＝支架層 |
| design-patterns-note | 主題 | 20 | 44 | 2.2 | 2026-08-15 | writtenAt 2026-08-15；挖 10（＋RtP）；企業層判姊妹站分工緩挖，POSA unavailable |
| system-design-note | 主題 | 25 | 44+20題 | 1.8 | 2026-08-15 | writtenAt 2026-08-15；三筆最急債已還（Evans/Release It/EIP）、挖 16 待挖 9；估算頁錯字已修 |
| writing-note | 主題 | 32 | 39 | 1.2 | 2026-08-15 | writtenAt 2026-08-15；Storr 開頁＋借聲債還清（校正表在 SOURCING-DEBT.md）；餘借聲 3 筆待下輪 |
| navarro-note | 人物 | 6 | 23 | 3.8 | — | writtenAt 2026-08-15；一脊梁（WEBIS）三支架；待挖 Three Minutes、Be Exceptional |
| peck-note | 人物 | 9 | 17 | 1.9 | — | writtenAt 2026-08-15；脊梁三本一線一根；友善的雪花書站已寫、站內未開頁 |
| agile-note | 主題 | 15 | 64 | 4.3 | 2026-08-15 | writtenAt 2026-08-15；三原典已挖（Beck/Anderson/Reinertsen，爭點一兩造原生到齊）；餘 4 本待挖屬邊界外推 |
| design-note | 主題 | 12 | 49 | 4.1 | 2026-08-15 | writtenAt 2026-08-15；Norman×2＋RUI 已挖（「錯是誰的錯」開庭判給設計）；BOOKS.md 已補齊 |
| behaviour-interview-note | 主題 | 20 | 32+14題 | 2.3 | 2026-08-15 | writtenAt 2026-08-15；Stories That Stick＋Parachute 已挖；Made to Stick 歸 writing、So Good 歸 newport（分工）；餘 14 本支架 |
| greene-note | 人物 | 7 | 18 | 2.6 | 2026-08-15 | writtenAt 2026-08-15；50th Law＋誘惑的藝術已挖，七本正典全開採 |
| philosophy-note | 主題 | 32 | 28 | 0.9 | 2026-08-15 | writtenAt 2026-08-15；Rawls／Aristotle／Epictetus／Seneca 已挖（正義官司三造到齊）、5 筆借聲債還清；原典 7 挖 5，剩柏拉圖、卡繆 |
| hbr-note | 主題 | 47 | 25 | 0.5 | 2026-08-15 | writtenAt 2026-08-15；Essentials／Innovation／Managing People 已挖（Feedback 官司兩造到齊）；Kotter「70%」查無原文已記帳 |
| lewis-note | 人物 | 14 | 12 | 0.86 | 2026-08-15 | writtenAt 2026-08-15；神蹟＋納尼亞已挖（護教三部曲齊、安斯康姆改寫入站）；剩裸顏、詩篇擷思 |
| stott-note | 人物 | 14 | 14 | 1.0 | 2026-08-15 | writtenAt 2026-08-15；講道藝術＋認識聖經已挖，14 本全數開採、未挖歸零 |
| uncle-bob-note | 人物 | 7 | 14 | 2.0 | 2026-08-15 | writtenAt 2026-08-15；工匠篇標準／倫理＋Coder 預估壓力已挖；剩函數式篇、PPP 獨有章 |
| tools-note | 主題 | 46 | 20 | 0.4 | 2026-07-31 | writtenAt 2026-08-15；23 挖／23 待挖，火力序：習慣三部曲→Four Thousand Weeks→Flow+Indistractable；「半天工」補錨五本；enrich 未做 |
| jung-note | 人物 | 7 | 14 | 2.0 | 2026-08-15 | writtenAt 2026-08-15；3→14 頁、七本原典全開採；bibliography「缺口」group 名失真待 note-inventory |
| kent-beck-note | 人物 | 6 | 14 | 2.3 | 2026-08-15 | writtenAt 2026-08-15；3→14 頁 Beck 全弧線；XP 二版未收待 note-inventory 補帳 |
| taleb-note | 人物 | 6 | 15 | 2.5 | 2026-08-15 | writtenAt 2026-08-15；8→15 頁、開肥尾技術線；profile readingPath 掛 skipped 書待 --fix |
| data-systems-note | 主題 | 19 | 50 | 2.6 | 2026-08-20 | writtenAt 2026-08-20；串流三本已挖（爭點二升格原生書源）＋15 條補錨；餘待挖 6 支架（indexing 兩本→Greg Young→Red Book/NoSQL/Kimball） |
| economics-note | 主題 | 50 | 45 | 0.9 | 2026-08-20 | writtenAt 2026-08-20；通論＋動物本能已挖（31/19）、roadmap 孤兒 7 頁歸零、capitalist-manifesto 錯帳修；火力序 2＝國富論 |
| investing-note | 主題 | 62 | 43 | 0.7 | 2026-08-20 | writtenAt 2026-08-20；煉金術＋Kindleberger 已挖（38/24，脊梁級歸零）、導覽開爭點五；this-time-is-different 錨錯掛已修（SOURCING-DEBT） |
| cloud-infra-note | 主題 | 26 | 39 | 1.5 | 2026-08-21 | writtenAt 2026-08-21；OE/SP/IaC 三本已挖（77 條/10 本開口）、爭點一造反者進場；TT→agile、BSRS→security 判姊妹站分工（Andrew 裁決）；次輪火力 K8s/Terraform |
| tracy-note | 人物 | 36 | 27 | 0.75 | 2026-08-21 | writtenAt 2026-08-21；總綱＋習慣兩新頁、銷售起源加厚（25→27 頁）；strategic-thinking 判假警報（書 repo slug/章題不一致）；餘 CYT-CYL 當佐證不開頁 |
| wan-weigang-note | 人物 | 11 | 16 | 1.5 | 2026-08-21 | writtenAt 2026-08-21；**B 型債 16 筆校正**（拐點兩頁重寫、t-shaped-talent 廢棄改 more-yourself-in-ai-era）＋計劃書開頁（15→16 頁）；校正表在 SOURCING-DEBT |

## 第一批——站深料足，直接可做

| 站 | 型 | owned | 頁 | 頁/書 | enriched | 備註 |
| --- | --- | ---: | ---: | ---: | --- | --- |
| startup-note | 主題 | 62 | 44 | 0.7 | — |  |
| communication-note | 主題 | 49 | 37 | 0.8 | 2026-07-31 |  |
| learning-note | 主題 | 33 | 34 | 1.0 | — |  |
| relationships-note | 主題 | 46 | 34 | 0.7 | — |  |
| growth-note | 主題 | 44 | 33 | 0.8 | — |  |
| business-strategy-note | 主題 | 50 | 31 | 0.6 | — |  |
| life-meaning-note | 主題 | 39 | 31 | 0.8 | — |  |
| history-note | 主題 | 34 | 30 | 0.9 | — |  |

## 第二批——可做；導讀章的「待挖」比例會偏高

| 站 | 型 | owned | 頁 | 頁/書 | enriched | 備註 |
| --- | --- | ---: | ---: | ---: | --- | --- |
| management-note | 主題 | 47 | 20 | 0.4 | 2026-08-01 |  |
| problem-solving-note | 主題 | 26 | 17 | 0.7 | 2026-08-06 |  |
| image-style-note | 主題 | 7 | 13 | 1.9 | — |  |
| spiritual-formation-note | 主題 | 35 | 13 | 0.4 | 2026-07-31 |  |
| de-botton-note | 人物 | 12 | 12 | 1.0 | — |  |
| maxwell-note | 人物 | 18 | 12 | 0.7 | — |  |
| schwager-note | 人物 | 10 | 12 | 1.2 | — |  |
| kiyosaki-note | 人物 | 23 | 11 | 0.5 | 2026-08-06 |  |
| liurun-note | 人物 | 12 | 11 | 0.9 | — |  |
| fromm-note | 人物 | 16 | 10 | 0.6 | — |  |
| newport-note | 人物 | 8 | 10 | 1.2 | — |  |
| wujun-note | 人物 | 18 | 10 | 0.6 | — |  |

## 先 enrich 再 guide（頁數不足或有溯源債）

| 站 | 型 | owned | 頁 | 頁/書 | enriched | 備註 |
| --- | --- | ---: | ---: | ---: | --- | --- |
| bogle-note | 人物 | 6 | 8 | 1.3 | — | 站太薄 |
| fengtang-note | 人物 | 10 | 8 | 0.8 | — | 站太薄 |
| nouwen-note | 人物 | 16 | 8 | 0.5 | — | 站太薄 |
| damodaran-note | 人物 | 5 | 7 | 1.4 | — | 站太薄 |
| nt-wright-note | 人物 | 11 | 7 | 0.6 | — | 站太薄 |
| templar-note | 人物 | 9 | 7 | 0.8 | — | 站太薄 |
| willard-note | 人物 | 8 | 7 | 0.9 | — | 站太薄 |
| pastoral-psychology-note | 主題 | 5 | 5 | 1.0 | — | 未溯源 5 頁，先還債 |
| christensen-note | 人物 | 9 | 4 | 0.4 | — | 站太薄 |
| collins-note | 人物 | 6 | 3 | 0.5 | — | 站太薄 |
| grant-note | 人物 | 5 | 3 | 0.6 | — | 站太薄 |
| grove-note | 人物 | 5 | 3 | 0.6 | — | 站太薄 |
| fowler-note | 人物 | 6 | 2 | 0.3 | — | 站太薄 |

