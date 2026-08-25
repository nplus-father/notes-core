# Note 星系 enrich backlog(鳥瞰)

> [!IMPORTANT]
> **排序表已搬走（2026-08-09）。** 「現在該進哪一站」看 [DEEPEN-READY.md](./DEEPEN-READY.md)——那份是**生成物**，
> 每次重算（書單完成度、頁/書、溯源率、mastery 覆蓋率），不會過期。
> **本檔從此只當工作日誌**：做過哪幾輪、抓到什麼、結案了什麼。
>
> 為什麼要搬：這裡原本那張手寫排序表的掃描日停在 **2026-07-31**，而中間 68 站的
> bibliography 已經翻過好幾輪（光 2026-08-09 一天就有 13 站被回填成 `owned`）——
> 手維護的排序表只要一停更新就會把人導去錯的站。

指標=內容頁數 vs bibliography owned 書數(粗指標:頁少書多=落差大;精確落差要進站跑 `/note-check`)。

**慣例:單站的詳細 TODO 放該站根目錄 `TODO-enrich.md`(工作暫存,不 commit,完成即刪);本檔記開工/完工與該輪的發現。**

> 本檔管的是「站已存在但還沒寫完」。「**還沒有站**的人物／主題」是另一個軸,見 [COVERAGE-GAPS.md](./COVERAGE-GAPS.md)。

## 進行中

（無）

## 兩站連打（2026-08-26 完成，Fable session 第十五〜十六站：startup＋personal-finance）

判層 54 本一次套用（startup 29：7 spine／11 support／4 tool／7 delegated；personal-finance 25：
8 spine／10 support／1 tool／6 delegated），兩站收工稽核全零。頁數：startup 44→51（創辦人兩難／
顧客開發／閃電擴張／Traction 靶心／Venture Deals／Rework／開卷管理）、personal-finance 29→36
（4HWW／F-You Money／Die with Zero／ERE／巴比倫／快車道／自動理財）＋Ramsey 原典補 anchor 進
baby-steps 頁（時程差異經核對相容）。

- 驗收：15 個代理共約 75 項具名事實／數字回源 grep 全數命中。兩筆術語修正：die-with-zero 的
  「記憶股息」改從書譯「記憶紅利」；fastlane 五誡書中作 **NECST** 非通行的 CENTS——代理照文本寫，
  又一次接住指揮層的預設。babylon 的「財富像一棵樹」為頁面逐字引文（抽驗樣式假警報）。
- 兩站單向邊共清 24 處；兩站首蓋 curation 戳記（僅 enrichedAt）。

## 四站連打（2026-08-26 完成，Fable session 第十一〜十四站：business-strategy／fromm／habits／marketing）

判層 51 本一次套用（BS 17：7 spine／1 support／9 delegated；fromm 6：5 spine／1 support；
habits 13：5 spine／5 support／2 tool；marketing 15：8 spine／4 support／1 tool／2 delegated），
四站收工稽核全零。裁決亮點：**blue-ocean 依 MODEL-ROUTING 明文推翻自動 delegated、判 spine 於
business-strategy 並開頁**（該文件點名的「判斷疊判斷」教案例正式兌現）；marketing 的 storybrand／
permission／100m-offers 三本原典判 spine 後以「補 anchor 進既有頁」兌現（頁在、原典沒被引的型態，
比開重複頁便宜且正確）。

頁數：business-strategy 31→38（Porter 五力／價值鏈／策略核／五問級聯／孫子／藍海／SPIN）、
fromm 10→15（開新分類「宗教與象徵」；思想自傳／釋夢／論不服從／精神分析與宗教／希望的革命）、
habits 28→33（Wood 情境摩擦／意志力科學／War of Art／Stolen Focus／刻意休息）、
marketing 27→32＋3 頁補強原典 anchor（Sharp／奧格威／STEPPS／成長駭客／峰值體驗 MOT）。

- 驗收：wave 1＋wave 2 共 22 頁新開＋3 頁補強，約 110 項具名事實／引句回源 grep 全數命中
  （幾筆初判查無均為抽驗 grep 樣式問題——孫子譯注本用譯文非古文、瘋潮的「社交身價」正是章名）。
- 補強代理順帶抓到兩筆忠實紀錄：permission 頁的「33%／1000 倍」出自 this-is-marketing 的今昔對比
  （原典數字為 35–36%／1800%，引用歸屬正確不改）；StoryBrand 2.0 已把嚮導特徵 authority 改為
  competency（頁面沿用通行舊版措辭，原典章節有明文說明修訂）。
- habits 站 related 是 YAML 破折號格式——補邊腳本已升級為雙格式（close-scan2.py 型）。
- BS／fromm／habits／marketing 四站單向邊共清 49 處；BS 與 fromm 首蓋 curation 戳記。

## career-note 批次 2（2026-08-26 完成，Fable session 第十站——本輪存量最大的裁決批）

42→49 頁。判層 23 本（7 spine／9 support／6 tool／1 delegated）。裁決要點：刻意練習軸由既有兩頁
承重（talent-is-overrated 判 support）、work-optional 的 FIRE 軸偏 personal-finance 但該站未收
（support 一句定位）、工程師手冊群與 HBR guide 照合輯決議判 tool。7 頁新開：求職轉職 3
（Ibarra 轉行／聯盟世代／別自己一個人吃飯）、意義方向 2（決定性的十年／無路之路）、
職涯資本 1（Godin 關鍵人物）、通才跨域 1（Pink 感性時代六感）。收工稽核全零：未判層 23→0、真欠債 7→0。

- 驗收：40 項具名事實／研究／案例回源章節 grep 全數命中（零杜撰）、96 組 book/anchor 零死鏈、
  溯源掃描空、entity 零殘留。
- 用腳本一口氣清掉 24 處 related 單向邊（含既有頁遺留＋本批跨頁鏡射），全站 49 頁雙向歸零。

## gardner-note 批次 2（2026-08-25 完成，Fable session 第九站）

8→11 頁。判層 5 本（3 spine／2 support——MI 應用彙編由 theory＋myths 兩頁承重、真善美續章掛
disciplined-mind 頁作延伸）。3 頁新開：APP 世代（賦能 vs 依賴，認同／親密／想像三軸）、
學習的紀律（真善美三範例深挖）、領導心智（認同故事與反故事）。收工稽核全零：未判層 5→0、真欠債 3→0。

- 驗收：17 項具名事實／研究／術語回源章節 grep 全數命中（零杜撰）、34 組 book/anchor 零死鏈、
  溯源掃描空、entity 零殘留、related 全站雙向。本站首蓋 curation 戳記（僅 enrichedAt）。

## biblical-studies-note 批次 3（2026-08-25 完成，Fable session 第八站——單書開頁部分）

44→51 頁。判層 20 本（7 spine／8 support／4 tool／1 delegated）。裁決要點：basic-christianity 與
邪惡與上帝新世界的姊妹站（stott／nt-wright）皆判 support 不挖，本站同判 support 不互踢；
Beale 聖殿專論作既有聖殿主線頁的深化源、work-matters 由 gospel-and-work 頁承重、Waltke／Goldingay
的 OT 神學軸由 Brueggemann 新頁＋既有 toledot 頁承重；IVP 背景註釋等 4 本照既有「工具書不立頁」
決議判 tool。7 頁新開：釋經方法 3（卡森釋經謬誤／Alter 敘事的藝術／釋經之旅五步過河）、
聖經神學 2（Vos 奠基／漸進聖約論）、舊約 1（Brueggemann 見證與反見證）、新約 1（Hays 迴聲）。
收工稽核全零：未判層 20→0、真欠債 7→0。

- 驗收：41 項具名事實／術語／經文例回源章節 grep 全數命中。**本輪抓到一筆「結構數字錯」——
  在我開單的規格裡**：我把 Grasping God's Word 的釋經之旅寫成「四步走」，代理讀原文發現是五步、
  如實照書寫並在回報標出，標題已全面改為「五步過河」。這正是 §1.2 預言的病，只是這次錯在指揮層。
- 112 組 book/anchor 零死鏈；順手用腳本清掉既有頁 21 條 related 單向邊（本站存量最多的一站）。
- **BST 38 卷系列債本輪未動**（比照批次 1 卷冊框架逐批寫，獨立工項，仍掛在「批次 3+ 剩餘」）。

## wujun-note 批次 2（2026-08-25 完成，Fable session 第七站）

10→17 頁。判層 7 本**全 spine**——與 kiyosaki 相反的形狀：吳軍的待判書全是重量級獨立正典
（既有 10 頁引的反而是得到隨筆集），豁免率僅 6%。開新分類「科技與文明」（對應 bibliography
既有分群），7 頁新開：浪潮之巔／智能時代／全球科技通史／文明之光／信息傳（新分類 5 頁）＋
大學之路（學習與卓越）＋數學通識（科技之美）。收工稽核全零：未判層 7→0、真欠債 7→0。

- 驗收：44 項具名事實／史實／數字回源章節 grep 全數命中（一筆「23:59」初判查無係 grep 半形樣式
  對不上原文全形「23 點 59 分」，逐格核對後頁面數字與原書表格完全吻合——零杜撰）；
  39 組 book/anchor 零死鏈、溯源掃描空、entity 零殘留。
- 順手清掉既有頁 9 條 related 單向邊；本站首次蓋 curation 戳記（僅 enrichedAt——本輪沒跑全站體檢，
  不謊報 checkedAt）。

## kiyosaki-note 批次 2（2026-08-25 完成，Fable session 第六站）

11→14 頁。判層 14 本（3 spine／9 support／2 tool）——清崎書系重複度高，嚴判是本輪重點：
豁免率 48%，但每筆都有可對帳的理由（before-you-quit 的 B-I 三角已有頁、who-took-my-money 等
四本與 five-iqs／fake 頁重疊、for-teens／rich-brother／rich-kid 沿用批次 1 決議、兩本合集判 tool）。
3 頁新開：90/10 與內行投資人（投資指南）、不公平的優勢（五重紅利）、三種槓桿（提早享受財富）。
收工稽核全零：未判層 14→0、真欠債 3→0。

- 驗收：18 項具名事實／數字回源章節 grep 全數命中（零杜撰）、35 組 book/anchor 零死鏈、
  溯源掃描空、entity 零殘留、related 全站雙向。

## management-note 批次 3（2026-08-25 完成，Fable session 第五站）

20→26 頁。判層 8 本（6 spine／2 delegated——批次 2 之後新進的 8 本書全數消化，5-min-mba-tools→
liurun、first-break-all-the-rules→career 皆為既有文件化決議）。6 頁新開：動機 3.0（Pink）、
執行力（Bossidy/Charan）、限制理論（The Goal，小說體 40 章實讀 11 章、anchor 落章）、戴明十四要點、
管理者實際在做什麼（明茲伯格）、逆向工作法（亞馬遜）。收工稽核全零：未判層 8→0、真欠債 6→0。

- 驗收：約 40 項具名事實／實驗／數字回源章節 grep 全數命中（零杜撰）、28 組 book/anchor 零死鏈、
  溯源掃描空、entity 零殘留。
- 順手清掉既有頁 16 條 related 單向邊（本站首次跑雙向檢查，managerial-leverage 作為樞紐頁補回 7 條反向）。

## theology-note 批次 3（2026-08-25 完成，Fable session 第四站——本輪最大站）

24→34 頁。判層 19 本（10 spine／5 delegated／4 support）。裁決亮點：奧古斯丁懺悔錄、效法基督、
天路歷程、痛苦的奧秘四本 delegated:spiritual-formation——姊妹站頁正是本 session 剛開的，委託
即時兌現；incomparable-christ→stott（該站有同名專頁在挖）。10 頁新開：doctrine 3（認識神／
道成肉身／巴文克恩典恢復自然）、apologetics 3（巴斯卡思想錄／阿奎那五路／切斯特頓永恆的人）、
historical 2（上帝之城兩座城／奧爾森神學的故事）、牧養 2（巴克斯特改革宗的牧師／畢德生返璞歸真）。
收工稽核全零：未判層 19→0、真欠債 10→0。

- 驗收：約 65 項具名事實／引文回源章節 grep 全數命中（兩筆初判「查無」實為我抽驗樣式比原文措辭嚴，
  對原文後確認頁面皆逐字引用——零杜撰）、60 組 book/anchor 零死鏈、溯源掃描空、entity 零殘留。
- 代理紀律兩例可貴：亞他那修名句「祂成為人使我們成為神」因落在未指定章節而拒用、改以實讀章節
  措辭承載同一邏輯；巴刻 balconeer/traveler 因文本未用該譯名而改用文本實際用語「旁觀者／旅人」。
- 順手清掉既有頁 11 條 related 單向邊（遺留債）＋1 條本批漏鏡射。
- 刻意不寫：christian-theology-introduction（support，survey 教科書）、journey-of-modern-theology
  （support，20 世紀地圖頁已涵蓋軸線）、lectures-to-my-students（support，牧養軸由兩本正典承重）、
  war-of-words（support）。

## spiritual-formation-note 批次 2（2026-08-25 完成，Fable session 第三站）

13→20 頁。判層 10 本（7 spine／1 delegated／1 support／1 tool）。裁決亮點：problem-of-pain 由
**本站 spine 接手深挖、lewis-note 維持 support**——主題站深挖、作者站一句帶到的互補分工；
friendly-snowflake 與 peck-note 同判 support 口徑一致。7 頁新開：prayer-pilgrimage 3（懺悔錄／
勞倫斯與神同在／慕安德烈禱告學校）、discipleship 2（效法基督／消滅匆忙）、suffering-grief 2
（痛苦的奧秘／為兒子哀哭——與既有的卿卿如晤頁組成理性面＋兩座哀歌的完整苦難軸）。
收工稽核全零：未判層 10→0、真欠債 7→0。

- 驗收：47 項具名事實／引文逐一回源章節 grep 全數命中（零杜撰）、40 組 book/anchor 零死鏈、
  溯源掃描空、entity 零殘留、related 全站雙向（含 grief-and-faith 原本空著的 related 一併接上）。
- 刻意不寫：50-spiritual-classics（tool，跨信仰合輯，批次 1 已有決議）、friendly-snowflake（support）、
  desiring-god（delegated:theology，該站已開採）。

## wellness-note 批次 2（2026-08-25 完成，Fable session 第二站，配方同 science-note）

11→19 頁。判層 16 本（8 spine／6 delegated／1 support／1 tool——delegated 全是批次 1 已文件化的
跨站決議，複核後照套），再對 8 本 0 引用 spine 各開一頁：stress-mental-health 3（斑馬壓力生理學／
CBT 認知扭曲／創傷與身體）、nutrition-sleep 2（營養主義批判／每日十二清單）、fitness-body 2
（醫學 3.0／運動改造大腦）、happiness-wellbeing 1（PERMA）。收工稽核全零：未判層 16→0、真欠債 8→0。

- 驗收：約 80 項具名事實逐一回源章節 grep，唯一偏差是譯名（頁面寫「零時體育課」、書用「第零節體育課」，已改從書）；
  41 組 book/anchor 零死鏈、溯源掃描空、entity 零殘留、related 全站雙向。
- 工作流改良：子代理改為**直接寫檔＋回覆驗收摘要**，science 輪 task 通知轉手的 `&gt;` entity 污染這輪零發生。
- 刻意不寫：lets-eat-right-to-keep-fit（support，1954 先驅、科學過時，一句定位即可）、
  living-without-gout（tool，單病查閱型）、fengtang×2→fengtang、happier 等 4 本→life-meaning（delegated）。

> **pastoral-psychology-note 溯源債已清（2026-08-24 晚，帳本 08-25 才補記）**：五本可收的書已到架
> （其餘五本同日判 `unavailable`），兩個 commit（a11e359、254b40e）把 5 頁全數掛上實 anchor，
> 溯源率 0%→100%（本輪 DEEPEN-READY 重算已確認）。**殘債記在各頁 frontmatter 註解**：five-views
> 的中間三觀點、forgiveness 的 REACH 五步、trauma 的哀歌＋Herman 三階段——都得等 unavailable
> 的來源書（Johnson／Worthington／Langberg）才能溯源。站尚未蓋 curation 戳記，留給收尾那輪。

## science-note 批次 2（2026-08-25 完成，首個 Fable session，判層＋enrich 同站串打）

16→27 頁。先判層（21 本裁決：11 spine／6 tool／2 support／2 delegated，套用走 `apply-tiers.py`），
再對 11 本 0 引用 spine 各開一頁：scientific-method 4（可否證性／典範轉移／鬼扯偵測／草包族科學）、
physics-cosmos 3（原子假說／膨脹的宇宙／星塵）、evolution-life 3（天擇原典／基因視角／累積選擇）、
mind-cognition 1（GEB 怪圈）。收工稽核全零：未判層 48→0、真欠債 11→0、空頭支票／漏接／衝突 0。

- 驗收：53 項具名事實逐一回源章節 grep 全數命中（零杜撰）、37 組 book/anchor 零死鏈、溯源掃描空、entity 零殘留。
- 順手清掉既有頁 8 條 related 單向邊（遺留債，非本批製造）；四分類 roadmap＋mastery 已跟上。
- 刻意不寫：brain-rules 與 pleased-to-meet-me（support——thinking-note 同判 support，兩站口徑一致，不互踢）、
  6 冊藥學 handbook（tool，依既定決議不進站）、frames-of-mind→gardner、槍炮病菌→history（delegated）。
- 工作流備忘：子代理交回的稿經 task 通知轉手會帶 `&gt;` entity 污染，主代理寫檔時逐一還原——§共通紀律的 grep 果然每輪都有用。

## 下次開工第一件事

(無——v0.19.3 全站 bump 已於 2026-08-06 當日完成,68 站 0 失敗。)

## note-check 抽查(2026-08-06,大改後驗證輪)

抽 5 站(problem-solving/kiyosaki/behaviour-interview/drucker/system-design)跑全站唯讀體檢:**零紅燈,5 站 PASS with warnings**。黃燈已修:10 站 schools 接線 prettier 格式(kind 指派的 sed 遺留)、6 站翻 owned 後過時的「最大缺口」註記、kiyosaki 2 翻+3 補列、drucker/kiyosaki 7 條 related 單向邊、notes-fmt 執行位(→v0.19.3)。behaviour-interview 與 system-design 的系統性 related/雙集合反向不對稱另發 --fix 清理。遺留人工判斷項:behaviour-interview 的 `::discussion` 變體是否認可、system-design caching-strategies 的 `:::response` 疑似範例殘留、problems 全站未填 difficulty。

## v0.19.0 版面契約債(2026-08-05 登記,2026-08-06 全數結案)

core v0.19.0 把首頁綜覽升格必備、新增 `/check/` 檢核頁。三筆存量債已於 2026-08-06 一次清完(校準批 5 站先驗風格,再 8 批平行 agent 放量,逐站 build 驗證+slug 機械核對):

1. ~~mastery 全站皆缺~~:**66 站全數補齊**(除 leetcode-note),每個分類 `_index.md` 都有 2–4 條書本位 mastery、slug 只連真實存在的頁;分類只有單頁已寫成時 2 條同掛該頁。範本=covey-note。
2. ~~kind 指派~~:9 站完成——methods:agile、design、problem-solving、biblical-studies、learning、tools;themes:history、science、hbr。其餘 schools 站維持預設學派地圖。
3. ~~缺 schools 的主題站~~:behaviour-interview-note 已補 methods 方法地圖(6 張卡,跨站連 newport)。
   > `leetcode-note` 仍除外:唯一沒遷移到 core 版面的站,v0.19.0 的導覽列、卡片、檢核頁一概吃不到。要它跟上得先做 Phase-2 遷移,是另一個獨立工項。

> 順手修掉的雜項(2026-08-06):economics 2 頁、keller 13 頁檔尾殘留的工具呼叫雜訊行(`</content>`/`</invoke>`)已清;agile/investing 3 條「尚未收」過時註記隨 wanted→owned 翻轉一併改寫。

## 新站(2026-08-10):security-note

開站緣由:`ORPHAN-BOOKS.md` 1b 的唯一開新站候選——`leaf-security` 8 本藏書裡 6 本沒有任何站認領(75%),
是全星系唯一同時滿足「藏書 ≥8」與「未覆蓋 ≥60%」的 leaf。這也是**反向盤點腳本化之後抓到的第一個站**。

| 站 | pages/owned | 備註 |
|---|---|---|
| security-note | 4 / 8 | 四個分類各一則種子概念,**全部走路徑 A**(逐章讀 `books-done` 原文後寫,每頁掛章節 anchor,anchor 目錄已逐一驗證存在)——**不欠溯源債**。分類:安全工程/攻擊者視角/應用密碼學/Web 與應用安全 |

> **待深化**:pages/owned = 4/8,每個分類的 roadmap 各留了 2 個 planned 節點(共 8 頁)。
> 8 本 owned 書全部在本機 `books-done/craft/engineering/security/` 且章節完整,下一輪 `note-check --enrich` 直接可用。

> **本站是第一個原生使用 `author` 欄的站**(notes-core v0.27.0);`wanted` 那 6 本已於開站當日實掃 portal 與
> 本機 books-done,確認都不存在,不是假缺口。

## 新站(2026-08-04 開站,同日全部完成 enrich)

開站緣由與缺口分析見 COVERAGE-GAPS.md。五站的內容皆為書本位、每頁掛章節 anchor。

| 站 | pages/owned | 備註 |
|---|---|---|
| templar-note | 7 / 6 | 開站種子概念全數改寫為書本位並掛章節 anchor;順手修正三處事實(Rules of Thinking 是 10 部不是 6 類、Rules of Management 的核心是「管理流程而非管理人」、work 分類頁改名 manage-the-process-not-the-people) |
| navarro-note | 6 / 4 | 同上;補入十大準則、三腦一體、識謊迷思(慣性說謊者反而增加眼神接觸)、討喜 vs 善良對照表 |
| design-note | 8 / 9 | 批次 1 完成;新增 5 頁(SHE 削減、SLIP 組織、三個重疊空間、創造是減法、清晰與神秘) |
| agile-note | 13 / 8 | 批次 1 完成;新增 9 頁(DEEP/相對估算/技術債、視覺化/管理流動、角色建模/故事異味、ADAPT/自組織領導) |
| covey-note | 12 / 8 | 批次 1 完成;新增 6 頁(以終為始、磨鋸、雙贏、統合綜效、信用四核心、4DX) |

> **溯源債已清（2026-08-04）**:上表三站開站當天的種子概念(agile 4 頁、covey 6 頁、design 3 頁)原本沒有 anchor,同日已全部回原文逐段核對後改寫。五站現在跑 `note-check` §0.5 掃描皆為空。

> 三站的來源書都在 `books-done` 下且章節完整,溯源 anchor 已掛。covey 站刻意不另開「影響圈」頁——既有的 `space-between-stimulus-and-response` 已完整涵蓋。

## 高落差(owned 遠大於 pages,優先)

| 站 | pages/owned |
|---|---|
| biblical-studies-note | 44 / 74(批次 1+2 完成 2026-08-06:批次 1 補列 14 本 BST 並寫 14 頁卷冊解經框架;批次 2 再寫 11 頁清高價值缺口——Beale 新創造、賴特卷一史學方法、Bailey 中東之眼、Waltke toledot、Hays 三焦點、Ehrman 文本鑑別、逐卷讀經法/難解經文/孫寶玲講道學、Watkin 對角化、Peterson lectio divina。**批次 3+ 剩餘**:BST 其餘 38 卷(Stott Romans/Acts/Ephesians、Webb Isaiah、Kidner Jeremiah/Ecclesiastes 等,系列級,比照批次 1 卷冊框架逐批寫);工具書群(TDNT/IVP 背景註釋等)作 alternative 不立頁) |
| problem-solving-note | 17 / 20(批次 1 完成 2026-08-06;13 頁新增+4 頁種子頁回原文校正(抓到 6 處實質錯誤,見 SOURCING-DEBT.md);16 本已引用,zero-second 系列/mckinsey-work-method 與既有頁重疊刻意不寫——實際落差歸零) |
| kiyosaki-note | 11 / 13(批次 1 完成 2026-08-06;8 頁新增;10 本已引用,for-teens/rich-brother 等 3 本重疊或無容器刻意不寫——實際落差歸零) |
| career-note | 44 / 58(批次 1 完成 2026-08-06;8 頁新增,底子乾淨無未溯源頁;30 本名目落差中 8 本跨站分工、3 本姊妹站認領、3 本本地無書源、其餘書摘太薄或軸不合刻意不寫——實際落差歸零) |
| leadership-note | 54 / 77(批次 1 完成 2026-08-06;10 頁新增(multipliers/radical-candor/great-by-choice 等今日剛翻 owned 的新書為主);28 本刻意不寫:12 本跨站分工、9 本姊妹站認領、7 本重疊或離題——實際落差歸零。遺留小債:6 個既存頁不在 roadmap 內(ceo-excellence/confront-brutal-facts/drucker-five-questions/boundaries-for-leaders/team-of-teams/five-levels-of-leadership),roadmap 視圖不顯示,下輪順手補) |

> biblical-studies-note 這一筆現在額外吃得下 18 本:Wilcock/Motyer/Raymond Brown/Walton 四位釋經作者的書,依 COVERAGE-GAPS.md 的決議不另開人物站,全歸這裡。

## 中落差

| 站 | pages/owned |
|---|---|
| management-note | 20 / 39(批次 2 完成 2026-08-01;39 本中 38 本已消化——concept-of-the-corporation/程天縱三部曲/管理備忘錄/managers-handbook 全開頁,drucker-cafe 補強掛 know-thy-time,5-min-mba-tools 歸 liurun 站——落差歸零) |
| wellness-note | 11 / 24(批次 1 完成 2026-07-31;24 本中 20 本已消化——4 本跨站:harvard-guide/two-awesome-hours→life-meaning、fengtang×2→fengtang 作者站——實際落差歸零) |
| hbr-note | 32 / 42(批次 2 完成 2026-07-31;42 本中 41 本已消化,managing-stress 以補強掛進 manage-your-energy;僅 hbr-guide-collection 合輯不消化——落差歸零) |
| tools-note | 20 / 42(批次 1 完成 2026-07-31;34 本已消化——8 本跨站重疊刻意不寫:atomic/tiny-habits、indistractable、4000-weeks、first-things-first、eat-that-frog 歸 habits-note,7-habits 歸 career/leadership,zstp 與既有頁重疊;實際剩餘落差已小) |
| science-note | 16 / 37(批次 1 完成 2026-07-31,含撿回上次中斷的 6 頁遺留稿;剩 4 本 niche 認知書:affective-neuroscience/through-the-language-glass/pleased-to-meet-me/frames-of-mind,7 冊臨床藥學 handbook 依 BOOKS.md 不進站——實際剩餘落差已小) |
| communication-note | 37 / 44(批次 1 完成 2026-07-31;44 本中 34 本已消化——10 本跨站刻意不寫:48-laws/human-nature→greene、start-with-why→leadership、everyone-communicates→maxwell、story-mckee/smart-brevity→writing、2 本→relationships、speak-to-win→tracy、body-language→thinking——實際落差歸零) |
| spiritual-formation-note | 13 / 28(批次 1 完成 2026-07-31;28 本中 12 本跨站已覆蓋(willard×3/lewis×4/nouwen/keller/theology×2/habits)、50-spiritual-classics 跨信仰選集不合站主軸刻意不寫——實際落差歸零) |
| theology-note | 24 / 49(批次 2 完成 2026-07-31;49 本中 43 本已消化——4 本跨站刻意不寫:prodigal-son→nouwen、incomparable-christ→stott、pilgrims-progress→spiritual-formation、wrestle-with-god→peterson;systematic-theology/new-dictionary 以補強掛進 what-is-systematic-theology——實際落差歸零) |
| investing-note | 43 / 53(批次完成 2026-08-06;9 頁新增+利弗摩三頁溯源修復;引用書 17→27 本,其餘跨站分工/重疊/密度不足刻意不寫——實際落差歸零) |
| business-strategy-note | 31 / 39(批次 1 完成 2026-07-31;39 本中 29 本已消化——9 本跨站分工(management/startup/leadership/habits/marketing/hbr/communication/tracy)、concept-of-the-corporation 依決議歸 management-note 佇列——實際落差歸零;附註:art-of-strategy 書 repo 有「乃許」類 CJK 損壞譯名待修) |
| habits-note | 28 / 34(批次 1 完成 2026-08-01;34 本中 25 本已消化——8 本 tools/wellness 站領土、workbook 練習冊不消化——實際落差歸零) |
| economics/history/relationships/thinking/tracy/startup | **六站批次全數完成 2026-08-06**:economics 37→45(另抓 12 頁系統性錯掛 anchor+推力器捐主張反向,見 SOURCING-DEBT)、history 23→30、relationships 29→34、thinking 36→46(新開 mental-models 分類)、tracy 18→25、startup 37→44(藍海/獲利世代由本站認領)——各站實際落差歸零,刻意不寫清單見各站 commit 當輪回報 |
| peterson-note | 12→24 / 4(批次 1 完成 2026-08-09;12 頁新增——與神摔跤 5 章(亞當夏娃/挪亞/亞伯拉罕/摩西 I+II 合一頁/約拿,theology-note 的 wrestle-with-god 分工至此兌現)、十二法則 3 條(法則四/六/八)、秩序之上 2 條(VI 意識型態/XI 怨恨)、意義的地圖 2 章(異常的出現/學徒期);WWWG 結論章歸概覽頁、兩本法則書其餘條目刻意不寫防逐章書摘化、MM 序言歸概覽——實際落差歸零。溯源 100%(29 anchors 全驗)、抽驗零杜撰、seeAlso 首開 3 條跨站連結(biblical-studies×2/keller×1)) |
| 作者站小落差 8 站 | **批次 1 全數完成 2026-08-06**:nouwen(3→8)、gardner(3→8)、fengtang(3→8)、willard(3→7)、newport(4→10)、liurun(4→11)、taleb(3→8)、schwager(7→10)。全書本位+anchor 逐一驗證;newport 這輪順帶揪出書 repo 身分錯配首例(見 SOURCING-DEBT.md);各站刻意不寫的重疊/跨站分工清單在各自 commit 訊息對應的回報——實際落差歸零 |

## 低落差 / 已充實(暫不動)

behaviour-interview、clean-code、cloud-infra、data-systems、design-patterns、system-design、learning、writing、marketing、greene、uncle-bob、wan-weigang、image-style、peck、bogle、damodaran、de-botton、cloud、fromm、lewis、nt-wright、maxwell、stott、keller、drucker、wujun、personal-finance、philosophy、life-meaning、growth、economics…(pages≥owned 或差距小)

## 用法

1. 挑一站 → `cd notes/<站>` → 跑 note-check skill(或照 hbr-note 這輪的配方)。
2. 開工時在該站建 `TODO-enrich.md`,並把本檔該站移到「進行中」。
3. 完工(commit+push、刪站內 TODO)後,回本檔更新 pages 數、移回對應區塊。
