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
| drucker-note | 人物 | 19 | 14 | 0.7 | — | writtenAt 2026-08-21；19 本帳（脊梁 7 缺 Landmarks of Tomorrow unavailable）；GM 冷遇史當爭議軸；enrich 未做，火力序在導覽 ch3 |
| nt-wright-note | 人物 | 11 | 10 | 0.9 | 2026-08-21 | 一條龍：7→10 頁（PFG 卷補齊 COQG 四卷、Simply Jesus、After You Believe）；11/11 已挖、該挖未挖＝0；Justification unavailable 是最痛缺口 |
| fowler-note | 人物 | 6 | 9 | 1.5 | 2026-08-21 | 一條龍：2→9 頁、新開 Modeling 分類；bibliography Refactoring 1999→2018 二版（實書）；code-smells 節點判 clean-code 分工移除 |
| nouwen-note | 人物 | 16 | 12 | 0.75 | 2026-08-21 | 一條龍：8→12 頁、16/16 全引用；校正 3 筆（刪子代理腦補句、兩句引文貼回原文）；In the Name of Jesus unavailable 最大缺口 |
| grove-note | 人物 | 5 | 12 | 2.4 | 2026-08-21 | 一條龍：3→12 頁；內容債 0；measure-what-matters 改判「他的遺產」組；backlog：OPS 六力與 10 倍速可再開一頁 |
| collins-note | 人物 | 7 | 12 | 1.7 | 2026-08-21 | 一條龍：3→12 頁、新開 decline 分類；校正 1（AMD 十年內→1980 年代結束前）；wanted 新增 turning-the-flywheel；backlog：return-on-luck、stage-4 兩節點 planned |
| christensen-note | 人物 | 9 | 14 | 1.6 | 2026-08-21 | 一條龍：4→14 頁、新開 applications 分類；內容債 0；「缺口」組兩本 owned 併入應用領域組 |
| grant-note | 人物 | 5 | 13 | 2.6 | 2026-08-21 | 一條龍：3→13 頁、新開 potential／resilience 兩分類；內容債 0；backlog：各書人際／組織層（導覽 ch3 點名） |
| bogle-note | 人物 | 6 | 14 | 2.3 | 2026-08-21 | 一條龍：8→14 頁、新開 vanguard 分類；**B 型債 10 筆**（杜撰引語刪除、凱因斯引語張冠李戴、方向反寫等，見 SOURCING-DEBT） |
| damodaran-note | 人物 | 5 | 13 | 2.6 | 2026-08-21 | 一條龍：7→13 頁、新開 dark-side／philosophy 兩分類；內容債 0；backlog：金融股／困境公司 |
| templar-note | 人物 | 9 | 13 | 1.4 | 2026-08-21 | 一條龍：7→13 頁、新開 home 家庭分類；校正 6 筆（母體時序、控制狂補償等）；backlog：People 第二頁、Management 管自己 70 條 |
| willard-note | 人物 | 8 | 12 | 1.5 | 2026-08-21 | 一條龍：7→12 頁、renovation 線補齊、待寫債 2 筆還清；校正 7 筆（兩個自創比喻換回書中原語、吸血鬼基督徒出處歸位） |
| security-note | 主題 | 14 | 12 | 0.86 | 2026-08-21 | 一條龍：4→12 頁；BSRS 自 cloud-infra 判歸本站已挖；零引用剩 threat-modeling、practical-malware-analysis（malware 線要不要開分類待裁決） |
| theology-note | 主題 | 64 | 38 | 0.6 | — | writtenAt 2026-08-27；導覽補齊輪首站——五章全新；四本 support 兌現、十本 delegated 跨站分工清單 |
| biblical-studies-note | 主題 | 107 | 83 | 0.8 | — | writtenAt 2026-08-27；全星系最大站；BST 52 卷兌現史入導覽；9 support 逐本帶到；書名連寫防空頭支票假報 |
| startup-note | 主題 | 62 | 51 | 0.8 | — | writtenAt 2026-08-27；驗證學派正典鏈＋小而美戰線；11 support 逐本帶到；每階配驗收動作 |
| career-note | 主題 | 68 | 51 | 0.75 | 2026-08-27 | writtenAt 2026-08-27；三問一暗線（共同敵人=追隨熱情）；四場官司含一萬小時公案（被告本人出庭）；9 support 兌現、8 delegated 指路；讀序=底盤＋處境分流 |
| relationships-note | 主題 | 46 | 40 | 0.87 | 2026-08-26 | writtenAt 2026-08-27；三問一暗線（共同敵人=關係是自然的）；七卡六分類的橫切面判讀；寬恕官司（Lerner vs Forward）判分場景；spine 85% 給誠實解讀；讀序=分診不是課綱 |
| communication-note | 主題 | 49 | 39 | 0.8 | 2026-08-26 | writtenAt 2026-08-27；暗線「主角是對面那個人／口才缺席」；權力卡整卡通往 greene 的門判讀；談判內戰（Voss 踢館回源驗證）；delegated 18% 判「十字路口不是孤島」；5 support 兌現、9 delegated 指路 |
| business-strategy-note | 主題 | 49 | 38 | 0.78 | 2026-08-26 | writtenAt 2026-08-27；暗線「策略≠雄心」；權力卡判寄居型（孫子＝最老那面牆）；護城河與死因官司（Helmer 反向定位＝框架派自我收編）；delegated 31% 全星系之最判「十字路口中樞」；交會點「策略是一連串的不」 |
| history-note | 主題 | 34 | 32 | 0.94 | — | writtenAt 2026-08-27；暗線「歷史≠大人物編年史／事件是浪結構是潮汐」；戴蒙兩本各站一邊當官司證人；地理 vs 制度判尺分工；大歷史判「透鏡不是判決」；Lessons of History 判隱形主帥；萬曆十五年 unavailable 如實掛帳 |
| learning-note | 主題 | 33 | 36 | 1.09 | — | writtenAt 2026-08-27；暗線「假用功」；知識管理卡整卡外包判立場（收藏≠學習）；交會點「提取是共同引擎」＋一秒判書法；輸出神話判「引擎不是燃料」；delegated 39% 刷新全星系之最判「底層技能站的形狀」 |
| growth-note | 主題 | 44 | 35 | 0.8 | — | writtenAt 2026-08-27；暗線「反天賦決定論但不掉進努力萬能論」；成功學卡判熔解型（說得出機制的留下）；與 learning/career 三角分工判「同一座礦的三個開採面」；The Formula 補「表現有界成功無界」半張帳；交會點「成長是動詞」 |
| habits-note | 主題 | 44 | 33 | 0.75 | — | writtenAt 2026-08-27；暗線「意志力是最後的手段」；Hooked 判敵方教材與 Indistractable 成鏡像對；專注官司兩造同門師兄弟（教勾人的人教你脫鉤）；habits↔tools 單向分工線（8 本）；交會點「讓對的行為不需要意志力」 |
| marketing-note | 主題 | 31 | 32 | 1.03 | — | writtenAt 2026-08-27；暗線「說得更對不是更大聲」；廣告基本功組判地下室、Godin 判水電管線；Sharp 立為對兩派開槍的踢館者；大海 vs 泳池官司證據最硬（兩頁 related 互指）；選書規則「收原理略戰術」 |
| management-note | 主題 | 47 | 30 | 0.64 | 2026-08-01 | writtenAt 2026-08-27；暗線「管理≠控制」；創新與杜拉克卡判同居型（型態譜系第四種）；杜拉克三站分工；OKR 判「MBO 的文藝復興」（兩造是站內兩頁互指）；「用人之長的唯一結構性例外是管理職本身」；40 spine 對 30 頁寫成挖礦圖 |
| problem-solving-note | 主題 | 26 | 19 | 0.73 | 2026-08-06 | writtenAt 2026-08-27；暗線「判斷的速度是紀律不是資訊量的函數」；四卡判兩座本山＋兩條道場；零 delegated 判「不是孤島是獨門」；交會點「把思考外化到一張紙上」；額度中斷後三章靠落盤保險存活 |
| science-note | 主題 | 48 | 29 | 0.6 | 2026-07-31 | writtenAt 2026-08-27；暗線「科學≠確定的知識清單」；兩張無房卡判寄居＋分居（型態譜系再添）；方法內戰擴成四造（補 Kuhn）；藥理教科書組判「tool 是體裁不是降級」；官司三誠實寫「還沒開的庭」（科學×神學＝全星系最值得未來開庭的一場） |
| image-style-note | 主題 | 7 | 13 | 1.9 | — | writtenAt 2026-08-27；暗線「風格是文法流行只是流行語」；三張風格卡判「同一套文法的三種口音」；unavailable 8>owned 7 全星系獨有（市場的判決不是待辦）；官司一「被告的卡片自帶判決」；fork 抓到 bibliography note 複製殘留（Style and the Man 誤標 Boyer 已修） |
| spiritual-formation-note | 主題 | 35 | 21 | 0.6 | 2026-07-31 | writtenAt 2026-08-27；全星系時間縱深之最（1622 年）；福音派卡判散居型（名冊不是房間）；delegated 37% 判「人物站群的主題聚合層——沒有一本是丟出去的」；苦難官司「路易斯一人兩本各站一邊」判分時不分勝負；交會點「方向勝過速度」 |
| wellness-note | 主題 | 33 | 19 | 0.6 | 2026-07-31 | writtenAt 2026-08-27；暗線「健康是系統的設計不是意志力的考驗」；身心官司證人都是叛逃者（Sapolsky 與 Ratey 中間會合）；Grain Brain 的 skip 判立場宣言（證據撐得住什麼才收什麼）；HBR 四本立「不是書是頁」判準；公理「睡眠不可協商」 |
| de-botton-note | 人物 | 11 | 15 | 1.4 | — | writtenAt 2026-08-27；主線「先沒收只有你，再打開藥房」；愛情雙書判「同一題隔二十三年的兩次作答——他自己就是對照組」；安慰劑批評判「把狄波頓寫得比他本人更天真」；讀法判「掛號不是課綱」；fork 抓到 profile 死 slug（status-anxiety-book 已修） |
| maxwell-note | 人物 | 18 | 14 | 0.78 | — | writtenAt 2026-08-27；主線「一個定義四個推論」；牧職判讀「沒有組織權力可用的人發展的領導學天生不信組織權力」；法則判「違約代價表不是物理定律」（柯林斯簽了機率條款他沒簽）；skip 分三型態；濃縮版反向裁決 |
| schwager-note | 人物 | 9 | 12 | 1.3 | — | writtenAt 2026-08-27；主線「同一個否定的六次應用」；9 本全 spine 判「一人書架沒有裝飾品」；skip 帳全是版本學；倖存者批評判「三道防線最硬是後記那句被動指數」；自述批評判「分布很難集體說謊」；fork 抓到 profile 死 slug 變體（已修） |

## 第一批——站深料足，直接可做

| 站 | 型 | owned | 頁 | 頁/書 | enriched | 備註 |
| --- | --- | ---: | ---: | ---: | --- | --- |
| life-meaning-note | 主題 | 39 | 31 | 0.8 | — |  |

## 第二批——可做；導讀章的「待挖」比例會偏高

| 站 | 型 | owned | 頁 | 頁/書 | enriched | 備註 |
| --- | --- | ---: | ---: | ---: | --- | --- |
| kiyosaki-note | 人物 | 23 | 11 | 0.5 | 2026-08-06 |  |
| liurun-note | 人物 | 12 | 11 | 0.9 | — |  |
| fromm-note | 人物 | 16 | 10 | 0.6 | — |  |
| newport-note | 人物 | 8 | 10 | 1.2 | — |  |
| wujun-note | 人物 | 18 | 10 | 0.6 | — |  |

## 先 enrich 再 guide（頁數不足或有溯源債）

| 站 | 型 | owned | 頁 | 頁/書 | enriched | 備註 |
| --- | --- | ---: | ---: | ---: | --- | --- |
| cloud-note | 人物 | 13 | 9 | 0.7 | — | 站太薄 |
| gardner-note | 人物 | 13 | 8 | 0.6 | — | 站太薄 |
| fengtang-note | 人物 | 10 | 8 | 0.8 | — | 站太薄 |
| pastoral-psychology-note | 主題 | 5 | 5 | 1.0 | — | 未溯源 5 頁，先還債 |

