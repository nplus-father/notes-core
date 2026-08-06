# Note 星系 enrich backlog(鳥瞰)

掃描日:2026-07-31(2026-08-04 補入三個新站)。指標=內容頁數 vs bibliography owned 書數(粗指標:頁少書多=落差大;精確落差要進站跑 note-enrich 的 grep 分析)。

**慣例:單站的詳細 TODO 放該站根目錄 `TODO-enrich.md`(工作暫存,不 commit,完成即刪);本檔只維護跨站排序,開工/完工時更新狀態欄。**

> 本檔管的是「站已存在但還沒寫完」。「**還沒有站**的人物／主題」是另一個軸,見 [COVERAGE-GAPS.md](./COVERAGE-GAPS.md)。

## 進行中

(無)

## v0.19.0 版面契約債(2026-08-05 登記,2026-08-06 全數結案)

core v0.19.0 把首頁綜覽升格必備、新增 `/check/` 檢核頁。三筆存量債已於 2026-08-06 一次清完(校準批 5 站先驗風格,再 8 批平行 agent 放量,逐站 build 驗證+slug 機械核對):

1. ~~mastery 全站皆缺~~:**66 站全數補齊**(除 leetcode-note),每個分類 `_index.md` 都有 2–4 條書本位 mastery、slug 只連真實存在的頁;分類只有單頁已寫成時 2 條同掛該頁。範本=covey-note。
2. ~~kind 指派~~:9 站完成——methods:agile、design、problem-solving、biblical-studies、learning、tools;themes:history、science、hbr。其餘 schools 站維持預設學派地圖。
3. ~~缺 schools 的主題站~~:behaviour-interview-note 已補 methods 方法地圖(6 張卡,跨站連 newport)。
   > `leetcode-note` 仍除外:唯一沒遷移到 core 版面的站,v0.19.0 的導覽列、卡片、檢核頁一概吃不到。要它跟上得先做 Phase-2 遷移,是另一個獨立工項。

> 順手修掉的雜項(2026-08-06):economics 2 頁、keller 13 頁檔尾殘留的工具呼叫雜訊行(`</content>`/`</invoke>`)已清;agile/investing 3 條「尚未收」過時註記隨 wanted→owned 翻轉一併改寫。

## 新站(2026-08-04 開站,同日全部完成 enrich)

開站緣由與缺口分析見 COVERAGE-GAPS.md。五站的內容皆為書本位、每頁掛章節 anchor。

| 站 | pages/owned | 備註 |
|---|---|---|
| templar-note | 7 / 6 | 開站種子概念全數改寫為書本位並掛章節 anchor;順手修正三處事實(Rules of Thinking 是 10 部不是 6 類、Rules of Management 的核心是「管理流程而非管理人」、work 分類頁改名 manage-the-process-not-the-people) |
| navarro-note | 6 / 4 | 同上;補入十大準則、三腦一體、識謊迷思(慣性說謊者反而增加眼神接觸)、討喜 vs 善良對照表 |
| design-note | 8 / 9 | 批次 1 完成;新增 5 頁(SHE 削減、SLIP 組織、三個重疊空間、創造是減法、清晰與神秘) |
| agile-note | 13 / 8 | 批次 1 完成;新增 9 頁(DEEP/相對估算/技術債、視覺化/管理流動、角色建模/故事異味、ADAPT/自組織領導) |
| covey-note | 12 / 8 | 批次 1 完成;新增 6 頁(以終為始、磨鋸、雙贏、統合綜效、信用四核心、4DX) |

> **溯源債已清（2026-08-04）**:上表三站開站當天的種子概念(agile 4 頁、covey 6 頁、design 3 頁)原本沒有 anchor,同日已全部回原文逐段核對後改寫。五站現在跑 `note-enrich` §0.5 掃描皆為空。

> 三站的來源書都在 `books-done` 下且章節完整,溯源 anchor 已掛。covey 站刻意不另開「影響圈」頁——既有的 `space-between-stimulus-and-response` 已完整涵蓋。

## 高落差(owned 遠大於 pages,優先)

| 站 | pages/owned |
|---|---|
| biblical-studies-note | 19 / 47(**暫緩**——2026-08-04 決議這一輪先不做) |
| problem-solving-note | 17 / 20(批次 1 完成 2026-08-06;13 頁新增+4 頁種子頁回原文校正(抓到 6 處實質錯誤,見 SOURCING-DEBT.md);16 本已引用,zero-second 系列/mckinsey-work-method 與既有頁重疊刻意不寫——實際落差歸零) |
| kiyosaki-note | 11 / 13(批次 1 完成 2026-08-06;8 頁新增;10 本已引用,for-teens/rich-brother 等 3 本重疊或無容器刻意不寫——實際落差歸零) |
| career-note | 36 / 58 |
| leadership-note | 44 / 77 |

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
| investing-note | 38 / 53(2026-07-31 收回 4 頁中斷遺留稿) |
| business-strategy-note | 31 / 39(批次 1 完成 2026-07-31;39 本中 29 本已消化——9 本跨站分工(management/startup/leadership/habits/marketing/hbr/communication/tracy)、concept-of-the-corporation 依決議歸 management-note 佇列——實際落差歸零;附註:art-of-strategy 書 repo 有「乃許」類 CJK 損壞譯名待修) |
| habits-note | 28 / 34(批次 1 完成 2026-08-01;34 本中 25 本已消化——8 本 tools/wellness 站領土、workbook 練習冊不消化——實際落差歸零) |
| economics/history/relationships/thinking/tracy/startup-note 等 | 差距 8~16 |
| 作者站小落差:nouwen(3/9)、gardner(3/9)、fengtang(3/8)、willard(3/5)、newport(4/6)、liurun(4/7)、taleb(3/5)、schwager(7/9) | 頁數絕對值低,一批就能補完 |

## 低落差 / 已充實(暫不動)

behaviour-interview、clean-code、cloud-infra、data-systems、design-patterns、system-design、learning、writing、marketing、peterson、greene、uncle-bob、wan-weigang、image-style、peck、bogle、damodaran、de-botton、cloud、fromm、lewis、nt-wright、maxwell、stott、keller、drucker、wujun、personal-finance、philosophy、life-meaning、growth、economics…(pages≥owned 或差距小)

## 用法

1. 挑一站 → `cd notes/<站>` → 跑 note-enrich skill(或照 hbr-note 這輪的配方)。
2. 開工時在該站建 `TODO-enrich.md`,並把本檔該站移到「進行中」。
3. 完工(commit+push、刪站內 TODO)後,回本檔更新 pages 數、移回對應區塊。
