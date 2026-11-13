# DESIGN-AWARDS — 把筆記星系推到獎項級的藝術指導與驗收

**這份是什麼**：2026-11-13 Andrew 定的目標——筆記星系的呈現以 Awwwards／Webby／FWA 得獎作品的水準為標準，自我檢查、反覆提升到過關為止。本檔是那一輪的**藝術指導（art direction）、驗收閘門、工作包與模型分派**。實作落地後，定案的規範要回寫 `DESIGN.md`（正本），本檔留作這一輪的決策紀錄。

**誠實的邊界**：真的得獎要送件、要評審投票，這裡做不到。能做到的是用同一套評分制度（Awwwards 的 Design 40％／Usability 30％／Creativity 20％／Content 10％）找不看規格的獨立評審打分，加上機器量得到的硬指標。過關＝這個代理指標過關。

---

## 0. 驗收閘門

三道全過才算完成，缺一道就回到「評審 → 裁決 → 修」的迴圈。

| 閘門 | 判準 | 誰判 |
| --- | --- | --- |
| **機器** | `tools/design/audit.mjs` 全綠：320／390／768／1440 四個寬度無橫向捲動、axe 無 serious／critical、無 console error、CLS < 0.05、chrome 裡沒有 emoji 字元、字體真的載入 | 腳本 |
| **評審** | 三位互不相見的評審各自看截圖打分（§10 協議）。加權總分**中位數 ≥ 8.0**，且四項沒有任何一項中位數 < 7.5；桌機淺色、桌機深色、手機三組都要過 | 獨立代理 |
| **裁決** | Fable 逐條看評審的扣分理由：真問題開修單、品味分歧寫明為什麼不採納。沒有未處理的扣分理由 | Fable |

基準（v0.44.0，Fable 自評，2026-11-13）：Design 5.5／Usability 6.5／Creativity 3.5／Content 8.0，加權 **5.65**。Awwwards 的 Honorable Mention 門檻約 6.5，Site of the Day 約 8.0 以上。

## 1. 診斷：現在為什麼不是獎項級

現況是乾淨、克制、一致的編輯風，方向沒錯（紙色、髮絲線、不用 SaaS 語彙），差在**強度**。

1. **沒有尺度對比**：h1 40px，全站塞在 900px 置中欄。獎項級的編輯版面靠懸殊的字級與不對稱的格線製造張力。
2. **字體沒有被控制**：全是系統字後備。Linux／Windows 上襯線中文會掉到黑體；拉丁標題用的是中文字型內附的拉丁字。
3. **chrome 用 emoji 當圖示**（topnav、區塊標題、狀態）：彩色字符隨平台而異，打破墨色盤。
4. **沒有動態**：沒有進場、沒有換頁轉場、沒有捲動敘事、沒有目前所在頁的標示。
5. **每一區都是同一種白卡片**：Overview／Schools／Sources 沒有節奏差異，掃過去分不出輕重。
6. **深色模式是反色，不是設計**：封面是一塊亮板。
7. **手機導覽列折成兩行**。
8. **79 站除了封面長得一模一樣**，而且沒有一個讓人記得住的記號。
9. **細節失修**：`FromClean Code` 少空白、頁首還掛著 `Draft`、日期戳是等寬字方框、沒有 meta description／OG 圖。

## 2. 概念：活字書系（Folio）

**每一站是一套編號書系裡的一卷，瀏覽器是那本書的版面。** 語彙全部取自書籍排印：卷號、書眉（running head）、頁碼（folio）、邊注（marginalia）、髮絲線、版權頁（colophon）、藏書印。

三個記號撐起識別，其餘一律退後：

- **朱印**：一個朱紅色的方形小印，是全站唯一的暖色訊號。用在卷號、目前所在位置、進度、連結的 hover。一頁裡朱色面積不超過 2％。
- **巨大的卷號**：首頁 hero 的 `N°04` 用描邊的超大數字當圖形，不是小標。
- **書眉＋頁碼**：每個區塊左欄有編號書眉（`01 — Overview`），讀者隨時知道自己在第幾區。

原則：**字就是圖**。不加插畫、不加漸層、不加玻璃、不加陰影卡片。張力來自字級、留白、格線與一個朱色。

## 3. 既有裁定：這些不能推翻

讀 `DESIGN.md` 全文再動手。以下是 Andrew 明確裁過的，設計要在裡面做，不是繞過：

- chrome 的固定標題與標籤一律**簡短英文**，區塊不寫說明副標；內文繁中。
- Overview 與 Guide 的內文**用滿方框、不提早換行**。這一輪的做法：方框本身改成格線上的一欄（見 §5），文字仍然填滿那一欄。
- 首頁沒有導覽入口卡、沒有分類格；順序固定 hero → Overview →（AuthorProfile｜SchoolsMap）→ Sources。
- topnav 的詞彙與順序固定（Guide／Concepts／Problems／Check／Search／Library，有資料才出現）；站名不進 topnav。
- 兩層模型：正文是書本位，`:::response` 空塊不渲染，`draft` 不畫點。
- 資料契約不動：`site.config.ts`、`src/data/*.ts`、content schema、frontmatter、`::name` directive 的寫法。**79 站的內容檔一個字都不用改**，升 core 版本就換裝。
- 無 JS 時所有內容仍讀得到（tab 攤開、動效不擋內容）。
- 不用毛玻璃、不用漸層底、卡片 hover 不浮起。

這一輪**推翻**的一條，理由要寫進 `DESIGN.md`：topnav「只出 emoji」改成**單線 SVG 圖示＋英文標籤**（窄螢幕只留圖示）。詞彙與順序不變，變的只是字符。

## 4. Tokens

### 4.1 字體

以 Google Fonts 一條 `<link>` 載入（`preconnect` 兩個網域、`display=swap`），放在 `BaseLayout` 的 `<head>`：

```
Inter:wght@400..700
JetBrains Mono:wght@400;600
Newsreader:ital,opsz,wght@0,6..72,300..700;1,6..72,300..700
Noto Serif TC:wght@500;700;900
```

| 角色 | 字族堆疊（拉丁在前，中文落到後面） |
| --- | --- |
| `$display` | Newsreader → Noto Serif TC → Noto Serif CJK TC → Songti TC → serif |
| `$sans`（內文） | Inter → 系統中文黑體（PingFang TC／Noto Sans TC／Microsoft JhengHei） |
| `$mono` | JetBrains Mono → ui-monospace |

內文中文**不載 webfont**（系統黑體已經夠好，省下最大的一包）；只有標題的襯線中文走 webfont，用到的字少、切片也少。數字一律 `font-variant-numeric: tabular-nums lining-nums`；卷號與頁碼用 `$mono`。

### 4.2 字級（流動）

| Token | 值 | 用途 |
| --- | --- | --- |
| `--fs-mega` | `clamp(4.5rem, 17vw, 15rem)` | hero 的描邊卷號 |
| `--fs-display` | `clamp(2.75rem, 7.2vw, 6.5rem)` | 首頁 h1 |
| `--fs-h1` | `clamp(2.1rem, 4.4vw, 3.6rem)` | 內頁 h1 |
| `--fs-h2` | `clamp(1.5rem, 2.4vw, 2rem)` | 區塊標題 |
| `--fs-h3` | `1.2rem` | |
| `--fs-lede` | `clamp(1.3rem, 2.1vw, 1.75rem)` | 總覽 lede、頁首點題句 |
| `--fs-body` | `1.0625rem` | 內文，行高 1.85 |
| `--fs-small` | `0.875rem` | |
| `--fs-label` | `0.72rem` | 書眉、標籤：大寫、字距 0.14em、600 |

中文標題字重 900、字距 0.02em；拉丁標題字重 500、字距 −0.02em、`font-optical-sizing: auto`。同一個 h1 裡中英混排時兩者各走各的字族，這是刻意的。

### 4.3 色

| Token | 淺（紙） | 深（夜版） |
| --- | --- | --- |
| `--bg` | `#f6f3ec` | `#111013` |
| `--surface` | `#fbf9f4` | `#18171b` |
| `--surface-2` | `#efebe2` | `#201f24` |
| `--border` | `#dcd6c8` | `#2e2c33` |
| `--border-strong` | `#1b1b1e` | `#e9e5da` |
| `--text` | `#1b1b1e` | `#ece8de` |
| `--text-2` | `#45444a` | `#bdb9af` |
| `--muted` | `#756f64` | `#8a867d` |
| `--accent`（主題站） | `#2f4858` | `#a9bfca` |
| `--accent`（人物站） | 沿用現行暖褐 | 沿用現行，深色提亮一階 |
| `--seal` | `#c23b22` | `#e8654c` |

`--border-strong` 改成墨色實線：重要的分隔用 1px 墨線，次要的用 `--border`。`--seal` 只給朱印語意用，不拿來當一般強調色。語意色（easy／medium／hard、alert）保留色相，降飽和到與紙色同一個調子。所有文字對比過 WCAG AA。

### 4.4 空間與格線

- 版心 `--canvas: min(100% - 2 * var(--gutter), 1320px)`，`--gutter: clamp(1.25rem, 4.5vw, 4rem)`。
- 12 欄、欄距 `clamp(1rem, 2vw, 2rem)`。區塊的標準切法：**左 3 欄書眉＋右 9 欄內容**；≤ 900px 收成單欄，書眉疊在內容上方。
- 內頁閱讀欄：左 3 欄邊注（來源、星等、本頁目錄，sticky）＋中 7 欄正文＋右 2 欄留白。
- 區塊間距 `--space-section: clamp(4rem, 10vw, 9rem)`。垂直節奏用 0.25rem 的倍數。
- 圓角維持 0–3px。

### 4.5 動態

- `--ease: cubic-bezier(0.2, 0.7, 0.1, 1)`；時長 160ms（hover）／420ms（進場）／700ms（hero）。
- **換頁**：`@view-transition { navigation: auto; }`，整頁淡接；首頁 h1 與封面、概念卡標題與內頁 h1 用 `view-transition-name` 做形變。零 JS。
- **進場**：hero 一次編排好的進場（卷號描線、標題逐行升起、短橫線畫出、封面淡入），其餘區塊用 `animation-timeline: view()` 做 12px 的升起，包在 `@supports` 裡，不支援就靜止。
- **閱讀進度**：內頁頂端一條 2px 朱線，`animation-timeline: scroll()`。
- **微互動**：連結底線從左畫出、箭頭 hover 位移 3px、tab 指示線滑動、details 展開有高度過渡。
- `prefers-reduced-motion: reduce` 時全部關掉。動效一律不擋內容、不造成 CLS。

## 5. chrome

- **topnav**：高 64px、紙色實底、底下一條墨色髮絲線。左：`‹ 筆記星系`＋人像。右：單線圖示（24px 格、1.5px 線、`currentColor`）＋英文小標，目前頁有朱色小方點（`aria-current="page"`）。≤ 720px 只留圖示，一行排完，觸控目標 ≥ 40px。圖示集放 `src/components/Icon.astro`，一個元件、以 `name` 取用。
- **麵包屑**：改成書眉一行——`CLEAN CODE NOTES / CONCEPTS / FUNCTIONS`，`--fs-label`，第一項仍是回本站首頁，不要方框鍵。
- **頁尾＝版權頁**：左邊大字站名與卷號；中間保養紀錄（體檢／補齊日期，用線性圖示不用 emoji）；右邊「上一卷／下一卷」（依 `sites.ts` 同軸順序連到相鄰的站）與回筆記星系。底下一行 `© 2026 Andrew`。
- **跳到內容**的 skip link、`:focus-visible` 的 2px 墨色外框（偏移 3px）。
- `<head>` 補 `meta description`（`heroLede` 去標籤／頁面點題句）、Open Graph（`og:image` 用 `cover.png`）、`theme-color` 隨主題。

## 6. 各版面

每一項都是「現在 → 要變成」。class 名稱可以改，資料與路由不動。

### 6.1 首頁

- **Hero**：佔滿首屏（`min-height: min(86vh, 860px)`）。背景是描邊的巨大卷號 `N°04`（`--fs-mega`、1px 描邊、不填色，靠右下出血）。左 7 欄：眉標（`主題 · N°04`，朱印方點）→ `--fs-display` 的 h1 → 朱色短橫線 → 寬字距的 brand → `--fs-lede` 的 heroLede。右 4 欄：直式封面放大到 `clamp(220px, 26vw, 380px)`，墨色髮絲框，底下一行 `--fs-label` 的圖說。深色模式封面外加紙色襯邊，不壓暗。首屏底部一行統計書眉：`77 PAGES · 10 CATEGORIES · 42 BOOKS · UPDATED 2026-11-12`（數字從 build 時算，沒有的項目不出）。
- **Overview**：左欄書眉 `01 — Overview` 與 writtenAt（純文字，不要方框）。右欄 lede 用 `--fs-lede` 襯線；tab 改成文字 tab（底線指示、目前項朱色方點），內文填滿右欄。
- **SchoolsMap**：拿掉白卡片。改成編號條目的索引版面——每條一列：左大數字（`01`，襯線、`--fs-h1`）、中間名稱＋主張、右邊代表人物（文字連結，逗號分隔，不用 pill）與「站內筆記 →」。條目之間墨色髮絲線。≥ 1100px 可以兩欄。
- **AuthorProfile**：Thesis 做成頁面裡最大的引文（`--fs-h1` 襯線、懸掛引號）。Contributions 是無框的編號格。Reading Path 保留直式 stepper，節點改朱印方點＋等寬編號。Influences 是一行文字連結。
- **Sources**：橫向書架——封面立在一條墨線上（底對齊）、`scroll-snap`、可用鍵盤與滑鼠拖曳捲動，右端淡出，標題列有書數與 `Library →`。hover 時那一本上移 6px 並顯示書名。不再用固定高度的垂直捲動窗（頁捲套框捲是壞體驗），橫向一列同樣不佔版面。

### 6.2 概念總覽 `/concepts/`

做成一本書的**目錄頁**。每個分類是一章：左欄章號（大數字）與分類名、`done/total`；右欄條目用**點線引導**排成目錄行（標題 ······ `BASIC`／`ADV`），兩欄。待寫的條目是淡色斜體、不可點。分類 emoji 縮成章名旁的小圖，不放進方框。

### 6.3 分類頁、概念頁、題目頁

- **頁首**：書眉麵包屑 → `--fs-h1` 標題（中英混排，括號裡的英文降一階、換拉丁襯線斜體）→ 點題句（正文第一個 blockquote）升格為 `--fs-lede` 的 standfirst，不要灰底框。
- **左欄邊注**（sticky）：來源書（`From` 與書名之間要有空白）、星等（改成 5 格小方塊，實心數＝重要度，不用彩色星星）、本頁目錄（h2 清單，目前區塊朱點）。`Draft` 不顯示。≤ 900px 邊注收成標題下的一行。
- **區塊標題**：`::core` 這類 directive 產生的 h2，emoji 包進 `<span class="sec-emoji" aria-hidden="true">` 後以 CSS 隱藏，換成自動編號的書眉（`01`）＋襯線標題。手寫的 `## ⚖️ …` 屬於內容，原樣保留。
- **Alert**：不要整塊色底。上下各一條髮絲線、左上角 `--fs-label` 的類型標籤配一個語意色小方塊，內文正常字級。
- **details**：一列一條、右端 `+`／`−`、展開有高度過渡；不要白卡片。
- **程式碼**：頂端一行語言標籤＋複製鍵，字級 0.9rem、行高 1.65，深淺色各一套 shiki 主題，橫向溢出時右緣淡出。
- **表格**：髮絲線表、表頭 `--fs-label`、窄螢幕橫向捲動。
- **Further Reading／Dive Deeper／Related**：統一成同一種清單——書封縮圖＋章節標題＋書名，一列一條，hover 整列底線畫出。
- **上一頁／下一頁**：兩個大字連結並排（`--fs-h3` 襯線），不要方框。

### 6.4 Guide

章節 tab 改成帶編號的文字 tab（`01 The Field`），sticky 在 topnav 下、底線指示。章標題 `--fs-h1`。每章第一段是 standfirst。內文填滿 8 欄。

### 6.5 Check

頁首是巨大的進度數字（`0 / 46`，`--fs-display` 等寬）加一條朱色進度線。checkbox 自繪（方框、勾選時朱印填滿），勾掉的句子畫刪除線並淡出。各分類是編號章節。

### 6.6 Library

統計數字做成一排大數字（已挖／待挖／引用數）。條列圖與年代長條圖沿用，條改墨色、目前 hover 的條朱色、軸標用 `$mono`。盤點表是髮絲線表；狀態欄的 emoji（✅⬜🚫➖）換成四個自繪記號（實心方／空心方／斜線方／短橫），hover 與 `aria-label` 仍帶全名。

### 6.7 Search、404

Search：一條只有底線的大輸入列（`--fs-h2`），Pagefind 結果排成目錄行。404：巨大的描邊 `404`，一句話與回首頁連結。

## 7. 可及性與效能

- 鍵盤：tab 元件用 roving tabindex 與方向鍵；書架可用方向鍵捲；所有互動元素有可見 focus。
- 語意：一頁一個 h1、標題層級不跳、圖示有 `aria-label` 或 `aria-hidden`、地標齊全。
- 效能：CSS 一包、JS 維持 inline 小段（不引框架）、圖片有尺寸屬性與 `loading="lazy"`（首屏封面 `fetchpriority="high"`）、字體 `preconnect`。Lighthouse 的 Performance／Accessibility／Best Practices 目標 ≥ 95。
- 320px 寬不破版；列印樣式（`@media print`）把 chrome 拿掉、正文黑白。

## 8. 樣式檔的切分

`src/styles/global.scss` 現在是 3501 行一個檔。第一步先**原樣切開**成 partial（輸出的 CSS 逐位元相同才算過），之後各工作包各改各的檔，才能平行：

```
styles/global.scss          只剩 @use 清單，順序＝原本的層疊順序
styles/base/                _theme（色）_typography _layout _motion
styles/chrome/              _topnav _crumbs _footer
styles/home/                _hero _overview _schools _profile _bookshelf
styles/reading/             _prose _alerts _details _code _page-head _further _prevnext _guide
styles/index/               _concepts-path _category _problems _check _library _bibliography _search _404
styles/legacy/              目前沒有任何 core 元件用到的區段（儀表板／熱圖／演化鏈…）原樣搬過來，不刪
```

## 9. 工程紀律

- 在 worktree `notes/.wt/notes-core-design`（分支 `design-awards`）做，不動 `notes-core` 主 clone。
- 預覽與截圖：`tools/design/preview.sh build <站>…`（把 worktree 的 core 灌進站台副本再 `astro build`，一站約 4 秒）→ `preview.sh serve` → `node tools/design/shot.mjs <jobs.json>`。平行作業時各自設 `PREVIEW_DIR` 與 `PORT`。
- 測試站：`clean-code-note`（主題、技術、程式碼多）、`drucker-note`（人物）、`system-design-note`（有題庫）、`theology-note`（純中文長文）。
- 每改一輪都要自己看截圖：桌機 1440 淺／深、手機 390。沒看過圖不算做完。
- 不寫程式碼註解（新增的部分）；為什麼這樣做寫進 commit 與 `DESIGN.md`。
- commit 單行英文，沿用本 repo 的 `feat:`／`fix:`／`docs:`／`refactor:` 前綴。不 push。
- `npm run` 沒有的檢查不用發明；`astro build` 綠、`astro check` 不新增錯誤即可。

## 10. 評審協議

每一輪評審找三位**全新的**代理，彼此不通氣，也不給這份規格的設計理由（避免拿規格當答案對）。給每位的只有：

1. 一組截圖路徑（首頁、概念總覽、概念頁、Guide、Check、Library、Search；主題站與人物站各一套；桌機淺色、桌機深色、手機）。
2. 評分表：Design／Usability／Creativity／Content 各 1–10 分，附 Awwwards 的級距（6.5 Honorable Mention、8.0 Site of the Day、8.5 以上 Developer／Site of the Month 等級）。
3. 要求：先列出**最弱的十個具體問題**（哪張圖、哪個位置、為什麼扣分），再打分；每一項分數要引用至少兩個問題或優點當證據；拿它跟近年得獎的編輯型／閱讀型網站比，不是跟一般文件站比。
4. 輸出固定 JSON：`{scores:{design,usability,creativity,content}, weighted, issues:[{shot,where,why,severity}], strengths:[…]}`。

Fable 收三份、取中位數、逐條裁決，開下一輪修單。同一個問題兩位以上提到就是必修。

## 11. 工作包與模型分派

判準沿用 `MODEL-ROUTING.md`：**貴的額度花在「難、沒有驗證網、而且不會被下一輪推翻」的判斷上；有驗證網的執行交給 Opus。** 這一輪的驗證網是 build、機器稽核與截圖評審。

| # | 工作包 | 模型 | 為什麼 |
| --- | --- | --- | --- |
| A | 診斷、概念、本檔（藝術指導與 tokens） | **Fable** | 品味與取捨，沒有機器能驗；定了之後整輪都靠它 |
| B | `global.scss` 原樣切分（輸出逐位元相同） | Opus | 純機械，有位元比對當網 |
| C | 基礎層：tokens、字體、格線、動態、chrome（topnav／麵包屑／頁尾／圖示集／head meta） | Opus | 規格寫死了數值，有截圖可對 |
| D | 首頁五區 | Opus | 同上，與 E、F 檔案不重疊，可平行 |
| E | 閱讀頁（概念／題目／Guide 與 markdown 元件） | Opus | 同上 |
| F | 索引與工具頁（概念總覽／分類／Check／Library／Search／404） | Opus | 同上 |
| G | `tools/design/audit.mjs` 機器稽核 | Sonnet | 規格明確的小工具 |
| H | 評審（每輪三位） | Opus，全新 context | 獨立性比模型等級重要；評審不能是寫規格的那個 context |
| I | 裁決評審意見、開修單、判斷何時過關 | **Fable** | 哪些扣分是真問題、哪些是品味分歧，是這一輪唯一沒有網的判斷 |
| J | 修單執行（每輪） | Opus | 修單逐條具體 |
| K | `DESIGN.md` 改寫成新正本 | Opus 起草、Fable 定稿 | 事實對帳便宜，定調要一致 |
| L | `leetcode-note` 換裝（它有自己的版面與樣式，不吃 core 的 layout） | Opus | 照 core 的 tokens 移植 |
| M | 發版與鋪開 79 站（tag、`bump-notes-core.sh`、逐站 build） | 腳本＋Andrew 放行 | 要 push，等 Andrew 說 go |

流程：A →（B → C）‖ G → D ‖ E ‖ F → H → I → J → H → …（直到 §0 三道閘門全過）→ K、L → M。

## 12. Foundation API（工作包 B／C 交付，D／E／F 從這裡取用）

Partial 一律 `@use "../tokens.scss" as *;`（`$display`／`$sans`／`$mono`／`$serif`＝`$display`、`$bp-grid` 900px、`$bp-nav` 720px、`$canvas-max`、`$ease`），要用 mixin 再加 `@use "../base/mixins" as *;`。`global.scss` 只是有序的 `@use` 清單，新 partial 照層疊位置插進去。

**Tokens（`base/_theme`）**：`--fs-mega／display／h1／h2／h3／lede／intro／body／small／label`、`--lh-body`、`--font-display／sans／mono`、`--bg／surface／surface-2／border／border-mid／border-strong（＝墨）／ink／text／text-2／muted／accent／seal／seal-weak`、`--gutter／canvas／col-gap／space-section／nav-h`（64px，≤ 720px 52px）`／tabbar-h`（≤ 720px 底部分頁列的高度含 safe-area，其餘 0）、`--ease／dur-hover／dur-enter／dur-hero`。`--border-mid` 是舊 `--border-strong` 的淡灰角色（空星、虛線框、未收長條），`--border-strong` 現在是墨線。

第二輪補充（2026-11-13）：

- `--fs-intro: 1.25rem` 是 body 與 lede 之間的那一階，給區塊開頭的導言段落（如 Schools 的 lede）；`--fs-label` 提到 `0.75rem`，`--muted` 在 `--bg`／`--surface`／`--surface-2` 兩種主題都過 AA（最低 4.78）。
- `--space-section` 改成 `clamp(3.5rem, 7vw, 6.5rem)`。間距只由 `:where(.section, .hero) ~ :where(.section)` 給一次（零特異度、跨過 Astro 插在元件之間的 `<script>`），區塊自己不要再加 `padding-bottom`；要特別的間距就用更具體的選擇器覆寫 `margin-top`。`main.container` 的底部留白是 `clamp(3rem, 6vw, 5rem)`（頁尾自己有墨線與上緣留白），各頁不必再覆寫。`.reveal` 與 `.reading-progress` 的捲動動畫寫成 longhand（`animation-timeline` 放最後），否則壓縮器會把它併進 `animation` 簡寫而失效；新的 `scroll()`／`view()` 規則照這個寫法。
- **站色（第二墨）**：主題站的 `<html>` 帶 `data-station-hue` 與 `--station-hue`（`site-covers.ts` 的 `accent2` 換成 OKLCH 色相，build 時算好）。`--accent`／`--accent-2`／`--accent-weak`／`--ring` 由這個色相以固定的低彩度推出（淺 L 0.40 C 0.055、深 L 0.80 C 0.045），不支援 OKLCH 的瀏覽器與人物站、設了 `accentOverride` 的站維持原本的軸色。用途：連結、選取底色、書眉編號（`.running-head-num`）、首頁的條目編號與頁尾的符號印記。朱印不被取代，一頁仍只有它是暖色訊號。
- ≤ 720px 的導覽是**底部分頁列**：同一組 `.topnav-link` 改成固定在底部的列（圖示＋短英文標籤、目前項朱色方點、墨色髮絲線、`env(safe-area-inset-bottom)`），塞不下時橫向捲動加吸附與邊緣淡出；頂列只剩返回、人像、深淺色。`body` 底部留 `--tabbar-h`。版面工作包的 sticky 元素一律用 `var(--nav-h)` 對齊頂列，不要寫死 64px；固定在底部的元素要讓出 `--tabbar-h`。

第三輪補充（2026-11-13）：

- **書布（cloth）**：每一站是布面精裝書系裡的一卷。`BaseLayout` 在 `<html>` 寫 `--cloth-l`／`--cloth-d`（build 時由 `cover-plate.ts` 的 `clothFor()` 從站色相算成 sRGB hex：淺 L≈0.42、深 L≈0.34，暖色相提亮加彩、藍綠紫降彩），`--cloth` 依主題取其一；`--cloth-ink`（紙色墨，對所有書布 ≥ 4.5:1）、`--cloth-line`（布上的髮絲線）。`@include cloth` 給底色＋極淡的經緯織紋。人物站一律暖褐布、`siteCovers` 沒登記的主題站用軸色石板布、registry 查不到的站沒有布。`site-covers.ts` 的 `cloth: { hue?, tone? }` 覆寫色相與明度（tone 是 L 的增減），用來把色相太近的站拉開；`--station-hue` 也跟著 `cloth.hue` 走，連結色與書布同色相。書布只出現在三處：首頁 hero 的布面（`view-transition-name: station-cover`）、頁尾版權頁的布面小方塊、首頁的 `theme-color`。朱印仍是唯一的暖色 UI 訊號。
- **`.section.is-wide`**：左欄只會放一個標籤的區塊，改用這個修飾：書眉疊在上方，`.section-body` 跨滿 12 欄。不要留一條只有標籤的空左欄。首頁 Thesis 已採用；索引與閱讀頁同樣情況請直接加 class。
- **`.text-tabs` 一律單行**：不換行、可橫向捲動、`scroll-snap`、被切掉的那一側淡出（`edge-fade`），底線畫在列底、指示線在 tab 內（`bottom: 0`，不再 `-1px` 被捲動容器切掉）。**要讓目前的 tab 自動捲進視野**：tab 列加 `data-edge-fade`，目前項用 `aria-selected="true"`／`aria-current`／`.is-active` 標示；`BaseLayout` 的 script 在載入時與這三個屬性變動時（MutationObserver）把它捲進來，只動 `scrollLeft`、不捲整頁。Guide 的章節 tab 用 `@include text-tab` 自己排的話，在捲動容器上加 `data-edge-fade` 與 `@include edge-fade` 即可拿到同一套行為。
- **手機頂列站名**：≤ 720px 頂列在人像右邊顯示 registry `label`（襯線、超出以刪節號截斷），這是「站名不進 topnav」唯一核准的例外，只在手機。底部分頁列往下捲時藏起、往上捲或回到頁頂時出現（只用 `transform`；reduced motion 時不藏；焦點在列內時不藏；無 JS 時永遠在）。

第四輪補充（2026-11-13）：

- **字體換入不位移**：`$display`／`$sans`／`$mono` 在 webfont 後面接本機度量對齊的後備（`Newsreader Fallback`、`Newsreader Display Fallback`（`$display-xl`，給 hero 標題與卷號）、`Inter Fallback`、`JetBrains Mono Fallback`，以 Times New Roman／Liberation Serif、Arial／Liberation Sans、Courier New／Liberation Mono 加 `size-adjust` 與 ascent/descent override 對齊）。Inter 與 JetBrains Mono 用 `display=optional`（內文永不在讀到一半時重排），Newsreader 與 Noto Serif TC 仍 `swap`。新的大字標題若在首屏、又用 Newsreader 拉丁字，改用 `$display-xl`。
- **站名回到桌機 topnav**：人像後面一個書布色小方塊＋站名（襯線），連回本站首頁；`site.config` 的 `showStationInNav: false` 關掉桌機版（手機頂列站名不受影響）。每頁 topnav 頂端一條 3px 書布色帶。`--cloth`／`--cloth-ink` 在每一頁的 `<html>` 都有。
- **手機底部分頁列最多五格**：超過五個目的地時第五格是 `More`（`<details>` 彈出清單，無 JS 可用、有 JS 時點外面或 Esc 關）。保留順序 Guide → Concepts → Problems → Check → Search，其餘（Library、Handbook、extraNav）進 More。
- **首頁區塊一律 `.section.is-wide`**：書眉（編號、標籤、數量或日期）一行在上，內容 12 欄。第二輪的 `.home-rail-index` 撤銷。每個區塊邊界只有一條線（書眉上緣的墨線），區塊自己不要再畫收尾線。
- `--fs-label` 改為 0.8125rem，`running-head` 的字色改為 `--text-2`。

| 名稱 | 種類 | 一行說明 |
| --- | --- | --- |
| `@include outlined-numeral($stroke, $width: 1px)` | mixin | 描邊不填色的數字（`-webkit-text-stroke`，不支援時退成實心）；首頁 hero 卷號用它，404 與目錄頁的大數字之後也改用它，不要各寫一份 |
| `.edge-fade`／`@include edge-fade($size)`＋`data-edge-fade` | class／mixin＋屬性 | 橫向捲動列：吸附、隱藏捲軸，只在被切掉的那一側淡出。元素加 `data-edge-fade`，`BaseLayout` 的 inline script 依捲動位置寫 `data-cut="start end"`；無 JS 時不淡出、照樣可捲 |
| `@include cjk-emphasis` | mixin | `em`／`i` 在中文裡不做假斜體，改用著重號（字下圓點） |
| `.section.is-wide` | class | 書眉疊在上方、內容跨滿 12 欄；給左欄只會有標籤的區塊 |
| `@include cloth` | mixin | 書布底色＋織紋＋`--cloth-ink` 字色 |
| `data-edge-fade` | 屬性 | 橫向捲動列：邊緣淡出，且目前項（`aria-selected`／`aria-current`／`.is-active`）自動捲進視野 |

**版面（`base/_layout`）**：`.container` 寬＝`--canvas`；≥ 901px 時 `main.container > *` 預設從第 4 欄開始（左 3 欄留給書眉／邊注），`.crumbs`／`.home-hero`／`.grid-12`／`.section`／`.bleed` 例外、滿版。`--span-3`／`--span-7`／`--span-9`／`--col` 是以 vw 算的欄寬長度，給還沒改成格線的舊版面對齊用。

| 名稱 | 種類 | 一行說明 |
| --- | --- | --- |
| `.grid-12`／`@include grid-12` | class／mixin | 12 欄、欄距 `--col-gap` |
| `.section`／`@include section-split($head, $body)` | class／mixin | 左 3 欄 `.running-head`＋右 9 欄 `.section-body`，≤ 900px 疊成單欄；相鄰 `.section` 間距 `--space-section` |
| `.running-head`＋`.running-head-num`／`@include running-head`、`running-head-num` | class／mixin | 書眉：`--fs-label` 大寫、字距 0.14em、600；編號走 `$mono`，後面自動接「—」 |
| `.label`／`@include label` | class／mixin | 只要書眉字樣、不要 flex 排列時用 |
| `.seal`／`@include seal($size)` | class／mixin | 朱印實心方點（預設 0.5rem），全站唯一暖色 |
| `.text-tabs`＋`.text-tab`／`@include text-tab`、`text-tab-active` | class／mixin | 文字 tab：底線指示從左畫出；`[aria-selected="true"]`／`[aria-current]`／`.is-active` 時墨字＋朱點＋底線 |
| `.hairline-list`（`.is-ink`）／`@include hairline-row($color)` | class／mixin | 一列一條的髮絲線清單；`.is-ink` 換墨線 |
| `.link-draw`／`@include link-draw($thickness)` | class／mixin | hover／focus 時底線由左畫出（可跨行） |
| `.arrow-nudge`／`@include arrow-nudge($distance)` | class／mixin | hover 時裡面的 `.icon`／`.arrow` 右移 3px |
| `@include above-grid`／`below-grid` | mixin | ≥ 901px／≤ 900px 的 media 包裝 |
| `.visually-hidden`／`@include visually-hidden` | class／mixin | 只給螢幕閱讀器 |
| `.display-latin`、`h1–h3:lang(en)` | class | 拉丁標題字重 500、字距 −0.02em（標題預設 900：中文 Noto Serif TC 900，Newsreader 封頂 700） |
| `.reveal` | class | `animation-timeline: view()` 的 12px 升起，包在 `@supports` 與 no-preference 裡 |
| `<BaseLayout progress>` → `.reading-progress` | prop | 內頁頂端 2px 朱線，`animation-timeline: scroll()` |
| `<BaseLayout description="…">` | prop | 頁面點題句；省略時用 `heroLede` 去標籤 |
| `@keyframes folio-rise／folio-fade／folio-draw` | keyframes | 進場升起／淡入／橫線 `scaleX` 畫出，hero 編排用 |
| `<Icon name size label? class?>` | 元件 | `src/lib/icons.ts` 的單線圖示（24 格、1.5px、`currentColor`）：guide concepts problems check search library handbook archive bookmark arrow-left/right/up-right chevron-left/right sun moon checkup enrich plus minus copy close |

Chrome 的 class（`.topnav*`、`.crumbs`、`.colophon*`、`.skip-link`）屬於基礎層，版面工作包不要改。換頁轉場已全站開啟（`@view-transition`），要做形變就在兩端元素上加同一個 `view-transition-name`。`prefers-reduced-motion: reduce` 會關掉所有動畫與轉場，列印樣式拿掉 chrome。
