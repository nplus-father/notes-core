# DESIGN — 筆記星系呈現規範（正本）

`nplus.wiki/<slug>/` 筆記星系各站的**呈現正本**。自 **notes-core v0.4.0** 起，版面／路由／schema 由 notes-core 整合器提供，各站是「純 config + 內容」的薄殼；本檔講「怎麼呈現」，程式碼在 `@nplus-father/notes-core`。

> 這份是**星系唯一正本**（v0.4.0 起不再複製到各站 repo）。星系成員權威清單見 `@nplus-father/notes-core/sites`（`sites.ts`）；遠端撈取用 GitHub topic `nplus-note`（見 §8）。

---

## 1. 版面骨架（notes-core `BaseLayout`）

- **Topnav（v0.45.0，2026-11-13 Andrew 裁定，取代 v0.19.0 的 emoji 分頁）**：左**只放人像**連首頁（與 favicon 同一張人像，core asset；nav 用 96px WebP 縮圖，favicon 仍是原 PNG）——站名退出 topnav，身分由人像＋首頁 hero 承擔，各站的導覽列長得一模一樣。右為 `buildNav()` 自動生成的**文字分頁**：（Guide，僅有導覽）／ Concepts ／（Problems，僅 `hasProblems`）／（Check，僅站台有 mastery 資料）／ …`extraNav` ／ Search ／（Library，僅有 bibliography），**不含首頁**，順序與出現條件同 v0.33.0。詞彙全星系統一、只出簡短英文、不出 emoji；`conceptLabelEn` / `problemLabelEn` 只用於麵包屑與頁標題，不影響 nav。
  - **樣式＝portal 的分區列**：0.8125rem、600、`--muted`，不填底色；分頁高＝nav 高（56px）；hover 轉 `--text` 並出 2px `--border-strong` 底線，當前頁轉 `--text` 並出 2px `--text` 底線＋`aria-current="page"`（pathname 以該 href 開頭即當前；首頁沒有當前分頁）。底線是 inset `box-shadow`，貼齊 nav 的底框。
  - **手機（< 600px）一列不換行**：分頁列自己是橫向捲動窗（隱藏捲軸、`scroll-snap-type: x proximity`），左側返回箭頭＋人像固定、右側深淺色切換固定（左側 1px 分隔線）。當前分頁以設定捲動窗的 `scrollLeft` 置中（不用 `scrollIntoView`，它會捲動整頁）；溢出的一側以 `data-more-start` / `data-more-end` 驅動的 mask 淡出，與 portal 的 TopNav 同一套。
  - **姊妹手冊 `extraNav`**：label 原樣輸出；但 label 只有 emoji（如各站慣用的 `📘`）而有 `title` 時，改以 `title` 當可見文字——不然「nav 不出 emoji」在 42 個用 📘 的站上就破功。`nav` 完全覆寫仍是逃生口，內容原樣採用。
  - `title`／`aria-label` 只在可見文字不是全名時才加，不重複唸同一個詞。
  - **v0.46.0 只在 v0.45.0 上加一條書布色帶**：每頁 topnav 頂端 3px 的 `--cloth`（§1.6），是站台在 chrome 裡唯一的顏色。nav 高仍是 `$nav-h` 56px；其餘照上面四條，一個字不改。hover 底線在 v0.46.0 的 token 下寫成 `--border-mid`——v0.46.0 的 `--border-strong` 是墨色，與「當前頁」的底線分不出來，`--border-mid` 才是 v0.45.0 那個淡灰的角色。
- **往上一層（v0.20.0）**：topnav 最左是「‹ 筆記星系」，連 `site.parentSite`（預設 `DEFAULT_PARENT_SITE` = `https://nplus.wiki/notes/`，**不是 wiki 根**——從一個筆記站往上就是那張主題／人物索引）；窄螢幕只留箭頭。同一連結仍在頁尾出現一次；`parentSite: null` 兩處一起隱藏。
- **麵包屑 `<Crumbs>`（v0.20.0）**：所有子頁（分類／概念／題目／檢核／搜尋）統一用這個元件，六個路由不再各寫一份 `<nav class="crumbs">`。**第一項固定是回本站首頁**，文字用 `site.brand` 而非泛稱的 "Home"（62 站同網域，"Home" 是哪個家不自明）；其後才是祖先鏈。於是「star 站 → 本站 → 本層」三級都是一步。**v0.46.0 起**排成一行書眉（`--fs-label`、大寫字距、`/` 分隔），不再是框線鍵；手機（≤ 720px）只留一個「← 上一層」返回連結。閱讀頁與索引頁改用書眉 `<VolumeHead>`（§1.7），那裡不再出麵包屑。
- **Footer＝版權頁（v0.46.0，§9）**：書布色小印記＋卷號＋站名、保養紀錄、上一卷／下一卷，底下一行 `© 2026 Andrew`（可用 `site.footer` 覆寫）與排印說明。不要再加「· 筆記星系的一站 · 延伸閱讀…」那串。
- **favicon**：星系**共用人像**，由 notes-core 以 asset 注入（single source of truth）——各站**不再放** `public/favicon.svg`。
- 深淺色、回想模式（recall）由 notes-core inline script 處理，勿改。
- 版面全在 notes-core：升 `package.json` 的 notes-core 版本即全站同步，**各站不寫 `.astro` 外殼**。
- **v0.11.0 起 astro.config 也收進 core**：各站 `astro.config.mjs` 只剩 `defineNotesAstroConfig({ base, site, bibliography, profile?|schools?, overview? })` 一句（markdown pipeline／shiki／sitemap 由 `@nplus-father/notes-core/astro-config` 工廠提供，Astro 升版遷移只改 core 一處）。`ns` 欄位同時轉 optional，各站已清除。

## 1.1 排版基礎（v0.45.0）

與 portal 同一層基礎，只動排版行為、**不動字級、行高與行長**：

- `html`：`text-autospace: normal`（中英之間自動留白）、`line-break: strict`（不讓標點落到行首）。不支援的瀏覽器直接忽略。
- `h1`–`h3`：`text-wrap: balance`＋`text-spacing-trim: trim-start`；hero 與列表頁的 `.lede` 也 balance；`.prose` 段落 `text-wrap: pretty`（少一字孤行）。
- 數字欄位一律 `tabular-nums`：計數、日期戳記、`N°` 編號、星等、表格。**v0.46.0 起 `body` 整頁 `tabular-nums lining-nums`**，不再逐一列 class。
- **與既有的中文標點處理不重疊（v0.46.0）**：中英之間的空白只由 `text-autospace` 給——`remark-reading` 在 build 時反而**刪掉**中文與行內連結／強調／`code` 之間手打的半形空白，否則兩者疊成一個半字寬的洞。標點擠壓只有一套：頁面標題、導覽章名與點題句（standfirst）用 `text-spacing-trim: space-all` 關掉瀏覽器的擠壓，改由 `punct-kern`（`<Kern>`／`kernTree`）逐對插 `.pk` 負邊距；其餘文字交給瀏覽器（h1–h3 的 `trim-start`、內文的 `normal`）。新增展示字時二選一，不要兩套一起上。

## 1.2 字型（v0.45.0；v0.46.0 補兩個拉丁字族）

v0.44 以前字型堆疊寫著 `Inter`，但沒有字型檔隨站出貨——拉丁字落到裝置有什麼用什麼。

- **Inter 隨站出貨**：`@fontsource-variable/inter` 是 notes-core 的 `dependencies`，`BaseLayout` 匯入 `wght.css` 一次，`$sans` 第一順位是 `"Inter Variable"`。字型檔依 unicode-range 切片，中文頁只抓 latin 那片（約 47 KB）。
- **中文襯線刻意交給系統字**：`$serif`（hero h1、h2／h3、卡片標題）是系統字優先的堆疊——`Noto Serif CJK TC` → `Source Han Serif TC` → `Songti TC` → `Noto Serif TC` → …，站台不出貨 CJK 襯線 webfont。CJK webfont 是逐字切片：一個三字的 hero 標籤就要抓三片（約 139 KB），外加約 137 KB 的 `@font-face` 宣告 CSS——為了首頁一個詞不值得（v0.45.0 開發時實測首頁傳輸 561 → 823 KB，因此撤掉）。
- **portal 才出貨展示用襯線**：nplus.wiki 門廳的 masthead 載 Noto Serif TC 700／900；筆記站不跟。
- 不連任何第三方字型主機。
- **v0.46.0：三個拉丁字族都隨站出貨（2026-11-13 Andrew 裁定）**。設計輪原本用 Google Fonts 一條 `<link>` 載 Newsreader、JetBrains Mono 與 Noto Serif TC，與上面兩條衝突；裁定是照 v0.45.0：拿掉 Google Fonts 與 preconnect，拉丁字改由 fontsource 套件出貨，中文襯線維持系統字。
  | 角色 | 字族（`font-family` 第一順位） | 套件與匯入（`BaseLayout` 各一次） |
  | --- | --- | --- |
  | `$sans` 內文、chrome | `"Inter Variable"` | `@fontsource-variable/inter/wght.css` |
  | `$display` 標題、卷號、引文 | `"Newsreader Variable"`（含 `opsz` 光學尺寸軸） | `@fontsource-variable/newsreader/opsz.css`＋`opsz-italic.css` |
  | `$mono` 程式碼、書眉編號、日期 | `"JetBrains Mono Variable"` | `@fontsource-variable/jetbrains-mono/wght.css`（只載正體；一個可變檔 40 KB，比靜態 400＋600 兩檔 43 KB 小） |
- 中文永遠落到系統字：`$display` 在 Newsreader 之後接 `$cjk-serif`（＝上面 v0.45.0 的系統襯線堆疊，順序一字不改），`$sans` 接 PingFang TC／Noto Sans TC／Microsoft JhengHei。字型檔依 unicode-range 切片，中文頁只抓用得到的 latin 片：Inter 約 47 KB、Newsreader 正體 129 KB（斜體 143 KB，頁面有斜體才抓）、JetBrains Mono 40 KB。`opsz` 軸讓同一個字族在 15rem 的卷號與 13px 的圖說都對；代價是檔案比只有 `wght` 軸的版本大一倍多（57 KB → 129 KB）。v0.46.0 實測 clean-code 首頁（不含封面與人像圖）傳輸：v0.45.0 約 66 KB（壓縮後）→ v0.46.0 桌機約 405 KB、手機約 261 KB，其中字型 360／216 KB（桌機多抓一支 Newsreader 斜體，給 hero 的斜體圖說）。要省這段就改匯入 `wght.css`／`wght-italic.css`，大字會失去展示切面。
- **換字不位移**：fontsource 預設 `font-display: swap`。三個字族後面各接一個本機度量對齊的後備字（`Newsreader Fallback`、首屏大字用的 `Newsreader Display Fallback`（`$display-xl`）、`Inter Fallback`、`JetBrains Mono Fallback`；`src: local()` 指向 Times New Roman／Liberation Serif、Arial／Liberation Sans、Courier New／Liberation Mono，以 `size-adjust` 與 ascent／descent override 對齊），webfont 晚到時行高與行寬不變。驗收：把字型請求延遲 1.5 秒，首頁與概念頁在 1440／390 的 CLS < 0.02（v0.46.0 實測：clean-code 首頁、概念頁與 drucker 首頁在 1440／390 都 ≤ 0.0004）。新的首屏大字若用 Newsreader 拉丁字，用 `$display-xl`。
- **系統中文襯線的差異是刻意接受的**：Linux 有 Noto Serif CJK TC（700／900 齊）、macOS 是 Songti TC，Windows 沒有繁中襯線，會落到 Georgia／系統 serif 的中文後備（新細明體一類）。標題的字重、字寬因此因平台而異；版面不依賴任何一款中文字的度量（hero 標題的縮放、星圖標籤寬度、目錄點線都用字數或保守的固定寬估算）。

## 1.3 動態（v0.45.0，與 portal 同值）

- **跨頁 view transition**：`@view-transition { navigation: auto }`，root 新舊畫面 160ms 交叉淡化、`cubic-bezier(0.2, 0.7, 0.2, 1)`。topnav 的 `view-transition-name` 是 `topnav`，與 portal 的 nav 同名——portal ↔ 站台互跳時兩條導覽列原地變形，而不是閃一下。**這是唯一的具名轉場**：設計輪的 `station-title`／`station-cover`／`page-title` 形變在 v0.46.0 拿掉。
- **減少動態**：`prefers-reduced-motion: reduce` 下所有動畫／轉場 0.01ms、`scroll-behavior: auto`、`@view-transition { navigation: none }`。
- 錨點落點：`html { scroll-padding-top: 56px + 1rem }`（topnav 高＋留白），站內錨點不再落到 nav 底下；原本各自補 nav 高度的 `scroll-margin-top` 已拿掉或扣掉這段（導覽章節只補 tab 列）。
- 站台**沒有進場動畫**；**任何 hover 都不位移**（既有規則）。
- **v0.46.0：整站只有兩支動畫**（2026-11-13 Andrew 裁定）：
  1. **星圖描線**（`/concepts/`）：星點淡入、連線依序畫出。一個 session 只播一次——星圖前一段 inline script 在繪製前讀寫 `sessionStorage["sc-seen"]`，看過就在 `<html>` 掛 `.sc-seen`，CSS 只對 `html:not(.sc-seen)` 下動畫；無 JS 時照播；減少動態時不播。
  2. **閱讀進度線**：內頁 topnav 底緣一條 2px 印色線，`animation-timeline: scroll()`；不支援就不出現，減少動態時隱藏。
- 其餘一律靜止：首頁 hero 直接是最終狀態（書布、符號、卷號都不進場）；區塊不做捲動進場（`.reveal` 已撤）；404 的大字不淡入。hover／focus 只換顏色與底線（底線可由左畫出，那是底線的變化不是位移），不 `transform`：箭頭不推、書架封面不抬、閱讀路徑的書封不浮。狀態轉場（tab 指示線、details 展開、勾選進度條、目錄印點）保留短轉場，不算動畫。程式碼框右緣的淡出是隨橫向捲動位置變的遮罩，也不算。

## 1.4 觸控、焦點、跳到內容（v0.45.0）

- `@media (pointer: coarse)`：chrome 裡每個控制項的點擊區至少 44px 高——nav 分頁、深淺色切換、返回鍵、Overview／盤點表／導覽的切換鍵、上一頁／下一頁、學派卡的「站內筆記」鍵、檢核頁的勾選與複習鍵。能撐高的直接 `min-height`；外觀要維持小框的（返回鍵、複習鍵、站內筆記、書架入口）用透明的 `::after` 撐出點擊區。v0.46.0 這組規則集中在 `styles/base/_touch.scss`（`.text-tab`、`.school-cat`、`.check-hit` 撐高；`.crumbs a`、`.check-review`、`.shelf-more` 用 `::after`），多數元件本身已是 44–48px。
- **跳到內容**：`BaseLayout` 第一個可聚焦元素是「跳到內容」連結，平時隱藏、聚焦才出現，目標是 `<main id="main" tabindex="-1">`。
- **焦點環統一**：`:focus-visible` 一律 2px `--accent` outline、offset 2px；輸入框（篩選列）維持 `focus-ring` mixin，搜尋框與 404 搜尋列是底線輸入框，焦點時底線轉墨色。設計輪的墨色焦點框（2px `--ink`、offset 3px）在 v0.46.0 併回這一條，元件不再各寫一份。

## 1.5 畫布與 token（v0.46.0，設計輪「活字書系」）

每一站是一套編號書系裡的一卷，瀏覽器是那本書的版面：卷號、書眉、頁碼、邊注、髮絲線、版權頁。張力來自字級、留白、格線與一個印色（§1.6），不加插畫、漸層、玻璃或陰影卡片。這一輪的決策紀錄在 `docs/DESIGN-AWARDS.md`，本節是定案。

- **樣式檔切分**：`src/styles/global.scss` 只是有序的 `@use` 清單；partial 依層分在 `base/`（色、字、格線、動態、觸控、列印）、`chrome/`（topnav、麵包屑、頁尾）、`home/`、`reading/`、`index/`、`legacy/`（目前沒有 core 元件用到、原樣保留的舊區段）。新 partial 照層疊位置插進清單。
- **色（`base/_theme`）**：紙與墨。淺色 `--bg #f6f3ec`／`--surface #fbf9f4`／`--surface-2 #efebe2`、`--border #dcd6c8`、`--border-mid #bdb5a5`（淡灰：空星、虛線、未收長條、hover 底線）、`--border-strong`＝`--ink #1b1b1e`（重要分隔用 1px 墨線）；深色是夜版（`#111013` 底、`#e9e5da` 墨），不是反色。`--muted` 在兩種主題的三種底色上都過 AA。語意色（easy／medium／hard、alert）保留色相、降飽和到紙色的調子；`--on-accent`（淺 `#fff`、深 `#111013`）給 accent 或 easy 實心底上的字。
- **字級（流動）**：`--fs-mega`（卷號、404）、`--fs-display`（首頁 h1）、`--fs-h1`（內頁 h1）、`--fs-h2`、`--fs-h3`、`--fs-lede`（點題句）、`--fs-intro`（區塊導言）、`--fs-body` 1.0625rem、`--fs-small`、`--fs-label` 0.8125rem（書眉：大寫、字距、600）。中文標題 900、拉丁標題 500 與 −0.02em 字距、`font-optical-sizing: auto`；同一個 h1 裡中英各走各的字族。
- **格線（`base/_layout`）**：版心 `--canvas = min(100% − 2·--gutter, 1320px)`，`--gutter: clamp(1.25rem, 4.5vw, 4rem)`；12 欄、欄距 `--col-gap`。區塊標準切法：左 3 欄書眉＋右 9 欄內容（`.section`），≤ 900px 收成單欄。只放一個標籤的區塊用 `.section.is-wide`（書眉在上、內容跨滿）。區塊間距只由 `:where(.section, .hero) ~ :where(.section)` 給一次（`--space-section`）。圓角 0–3px。
- **nav 高**：`--nav-h`＝`$nav-h`＝56px，所有寬度同值。sticky 元素（篩選列、導覽 tab 列、邊注、目錄側欄、藏書頁區塊導覽）一律 `top: var(--nav-h)`＋自己的留白；錨點落點由 `html` 的 `scroll-padding-top` 負責，元件的 `scroll-margin-top` 只補自己的 sticky 列（導覽頁的 tab 列），不再加 nav 高。

## 1.6 站色：書布、印、第二墨（v0.46.0；印 v0.47.0）

- **書布（cloth）**：每站一塊布面精裝的書布色。`BaseLayout` 在 `<html>` 寫 `--cloth-l`／`--cloth-d`，build 時由 `cover-plate.ts` 的 `clothFor()` 從站色相（`site-covers.ts` 的 `accent2` 換成 OKLCH 色相）算成 sRGB：淺 L≈0.42、深再暗 0.1，暖色相提亮加彩、藍綠紫降彩；人物站一律暖褐布，`siteCovers` 沒登記的主題站用軸色石板布，registry 查不到的站沒有布。`site-covers.ts` 的 `cloth: { hue?, tone? }` 可把色相太近的兩站拉開。`--cloth-ink` 是布上的紙色字（對每一塊布 ≥ 4.5:1）。
- **書布出現的地方是固定的**：每頁 topnav 頂端 3px 色帶、首頁 hero 的布面、頁尾版權頁的小印記，以及閱讀／索引頁的 `--vol`——`volume.ts` 把書布色寫成 `--vol-l`／`--vol-d`，只有對紙色／夜色 ≥ 3:1 時才用，否則退成墨；它畫書眉的色塊、頁首標題下與目錄章節上緣的 3px 色線、藏書頁的開採度長條與年代圖。首頁的 `theme-color` 取書布色。其他地方不用書布。
- **第二墨（站色相）**：主題站 `<html>` 帶 `data-station-hue`，`--accent`／`--accent-2`／`--accent-weak`／`--ring` 由該色相以固定低彩度推出（淺 L 0.40 C 0.055、深 L 0.80 C 0.045）；人物站、不支援 OKLCH 的瀏覽器、設了 `accentOverride` 的站維持軸色。用途：連結、選取底色、書眉編號。
- **印由書布決定（2026-11-14 Andrew 裁定，v0.47.0）**：`--seal` 是唯一的「你在這裡／已完成」訊號，色相跟著這一卷的書布走，不再是固定朱色。`cover-plate.ts` 的 `sealFor()` 吃 `clothFor()` 用的同一個最終色相（含 `cloth.hue` 覆寫；人物站共用暖褐布的色相，所以人物站的印也是同一個），算成 sRGB：淺色從 OKLCH L 0.52 C 0.15 起、超出色域先降彩度，再以 0.005 一步壓低 L，直到對三張紙（`#f6f3ec`／`#fbf9f4`／`#efebe2`）都 ≥ 4.5:1；深色從 L 0.76 C 0.13 起，必要時提高 L，直到對三種夜色（`#111013`／`#18171b`／`#201f24`）都 ≥ 4.5:1。`BaseLayout` 在寫書布變數的同一處寫 `--seal-l`／`--seal-d`；`_theme` 是 `--seal: var(--seal-l, #c23b22)`（深 `var(--seal-d, #e8654c)`），registry 查不到、沒有書布的站維持舊朱色。`--seal-weak` 是 `--seal` 與透明的 `color-mix`（淺 10％、深 14％）。用途不變：眉標方點、目錄與邊注的目前項、檢核頁的勾選、閱讀進度線、首頁 hero 的短橫線、文字 tab 的目前項方點。一頁印色面積不超過 2％；不拿來當一般強調色。印與第二墨同色相，靠彩度與明度分開（印 C≈0.09–0.15，第二墨 C 0.045–0.055）；某個色相若分不開，在色域內加彩度，不換色相。印不畫在書布上——同色相會消失；布上的記號一律用 `--cloth-ink`／`--cloth-line`。`tools/cover` 生成的主題站封面，右下角的印也取 `sealFor()` 的淺色（重新產生封面才會換）。

## 1.7 書眉 `<VolumeHead>`（v0.46.0）

閱讀頁與索引頁頂端一行書眉取代麵包屑：書布色小方塊 → 卷號 `N°04` → 站名（連首頁）→ 分隔 → 區塊名（連上一層，可帶章號）。卷號由 `sites.ts` 同軸順序算，名稱取 registry `label`。區塊與標籤書眉的寫法一律：等寬編號、破折號、字距大寫標籤（`01 — Overview`），數字與日期走 `$mono`。閱讀頁頁尾再出一次同樣的一行（`<VolumeColophon>`），讀完知道自己在哪一卷哪一章。

## 2. 首頁（notes-core `routes/index.astro`）

> **Chrome 語彙原則（v0.34.0，Andrew 裁定）**：固定標題與標籤一律**簡短英文**（Overview／Schools／Methods／Themes／Thesis／Contributions／Reading Path／Influences／Sources／Inventory／Coverage…），中文長標拗口；區塊副標說明句一律**省略**（標題自己講完了）；**內文維持繁中**。guide 章內小標屬內容、不在此列（2026-08-15 裁決：只動 chrome）。

由上而下：

1. **Hero＝布面精裝的這一卷（v0.46.0，取代 v0.36.0 的封面圖＋扉頁）**：佔滿首屏（扣掉 nav 高）。左 7 欄是扉頁活字：眉標（印色方點＋`Topic`／`Person`＋同軸 `N°` 編號）→ registry `label` 的 `--fs-display` 襯線 h1（標題短就放大：中文 2 字 ×1.9、3 字 ×1.5、4 字 ×1.25；拉丁 ≤ 8 字 ×1.35 起遞減——依字數算，不依字型度量）→ 印色短橫線 → `site.brand` 寬字距副題 → `site.heroLede`（`--fs-lede`）。右側出血是**書布**（§1.6，經緯織紋）：頂端燙印行（站名、符號名的斜體圖說、`Pl. I`）、中央是站的**符號**（主題站＝`site-covers.ts` 的單線符號，以壓印的雙層線畫出；人物站＝`public/cover.png` 肖像，加襯框）、左下描邊的巨大卷號 `N°04`（`--fs-mega`，`$display-xl`）。底部一行統計書眉：`80 PAGES · 10 CATEGORIES · 42 BOOKS`，布上是 `UPDATED` 日期（數字 build 時算，沒有的項目不出）。手機上書布在上（較矮的一條）、活字在下。**靜態**：沒有進場動畫（§1.3）。hero 圖片是裝飾（`alt=""`，h1 已說出站名）；`<title>` 仍用 brand。
> v0.46.0 起首頁每個區塊都是 `.section.is-wide`：一行書眉在上（`01 — Overview`、右側數量或日期），內容跨 12 欄；區塊邊界只有書眉上緣那一條墨線，區塊自己不畫收尾線。單欄文字（Overview 的 lede／tab／內文、Thesis）共用從第 3 欄起的 8 欄寬。

2. **總覽 `<Overview>`（v0.29.0，見 §4.2）**：首頁唯一的長散文區，排在 hero 之後、其餘區塊之前——**先讀懂「這是什麼」，再往下看結構化的卡片與表格**。標題固定 **"Overview"**（v0.34.0，無副標）；**lede 常駐、段落收進切換鍵**（機制同盤點表分組鍵：無 JS 攤開、Ctrl+F 命中隱藏段自動切段），段落 heading＝tab 標籤，**標準英文詞彙**：人物站 `Background / Contributions / Claims`（＋選配 `Verdict`）、主題站 `Landscape / Threads / Verdict`；行長不設上限（tab 化後一次只有一段，文字用滿方框）。首頁**沒有**導覽入口卡（v0.30.0 曾有、v0.31.0 移除）——導覽動線交給 topnav 的 Guide。
   v0.46.0 外觀：lede 是 `--fs-lede` 襯線（中文標點以 `tightenPunct` 擠壓），段落切換鍵是文字 tab（`.text-tabs`：底線指示、目前項印點，單行可橫捲、被切的一側淡出），內文是 sans。
3. **思想側寫 `<AuthorProfile>`**（人物站必備，見 §4.1）：中心思想、特定貢獻（連站內概念頁）、建議閱讀路徑（**直式 stepper**：N° 節點＋書封＋一行 why——階段名短、不做名詞解釋條列）、思想脈絡。v0.46.0：Thesis 是全頁最大的引文（懸掛引號、襯線）；Contributions 是無框的編號格，最後一列不滿就撐滿整寬；Reading Path 每階段是編號＋文字＋整寬的書封列；Influences 是一行文字連結。
4. **領域地圖 `<SchoolsMap>`**（主題站**必備**，見 §4.1）：領域鳥瞰——主張、代表人物（有作者站就跨站連結）、站內分類；標題依 `kind` 三選一（學派／方法／主題地圖），可加一句 `lede` 提綱挈領。v0.46.0 拿掉白卡片，改成編號條目的索引版面：每條一列，左邊編號、中間名稱＋主張、右邊代表人物（文字連結）與「站內筆記 →」，條目之間髮絲線；「站內筆記」仍是每條唯一的去處，hover 轉印色、不位移。
3. **書架 `<Bookshelf>`**：本站彙整自哪些 owned books（見 §4）。**v0.46.0 起是橫向書架**（取代 v0.29.0 的固定高度垂直捲動窗——頁捲套框捲是壞體驗）：封面立在一條墨線上底對齊、書名在下、`scroll-snap`，可用鍵盤、拖曳與左右兩個 44px 箭頭鍵捲動，左上角是位置讀數（`1–9 / 42`），右端淡出。書眉列右端補書數與 `Library →`（有 bibliography 的站）。hover 只讓書名變深，封面不動。

> **藏書盤點 `<Bibliography>` 自 v0.30.0 遷往 `/library/`（見 §6.3）**——收藏狀態（owned/wanted/…）是工作文件（採購 roadmap），不是門面。表格本身的規範不變：欄序 = **收錄 → 書名 → 註記 → 年份**；狀態只出記號（v0.46.0 起是四個自繪記號取代 ✅⬜🚫➖，hover 與 `aria-label` 有全名，見 §6.3）；**v0.20.0 起**組內依出版年排序＋表格上方的**年代分佈長條圖**（桶寬自適應 10–1000 年、壓進 14 格、「已收錄」堆在「未收」下、少於 4 本不畫）；**v0.29.0 起**分組是切換鍵（預設「全部」、無 JS 退回攤開）。

> 首頁文案（brand / tagline / heroLede / searchLede / searchPlaceholder）全在 `src/site.config.ts`，各站自訂。

## 3. 站封面（v0.36.0 起 hero 與 portal 同一張）

- **每站一張直式 3:4 封面 `public/cover.png`（900×1200）**：人物站＝傳主肖像照（人工挑選）、主題站＝**印刷風設計圖**（`tools/cover/` 生成——紙色底＋髮絲框＋襯線大字＋`N°` 編號＋accent2 符號；配色與符號在 `src/lib/site-covers.ts`，一符號一站，生成器啟動時對帳）。portal 卡片（HEAD 探測 `nplus.wiki/<slug>/cover.png`）與首頁 hero 消費**同一張圖**——讀者在 portal 憑封面挑站，點進來看到的就是那張，身分交接不斷。**不可刪**。
- **`/site-cover.svg` 已退役（v0.36.0）**：橫式扉頁卡是「用圖片印出來的文字」，內容與 hero 的 h1／heroLede 逐字重複，且 portal 明確不用它；其排版元素（眉標／襯線大字／短橫線／寬字距副題）攤成活字進了首頁 hero（見 §2）。主題站封面的深色編輯風（Style A：#0e1220 底、glow、點陣格）同批退役——那套語彙與站內的印刷風打架，v2 生成器改走同一套紙色墨階。
- **v0.46.0**：首頁 hero 不再直接放這張點陣圖——主題站的符號由 `site-covers.ts` 在 hero 的書布上以向量重畫（同一個符號、同一個卷號，深淺色各自對），人物站的書布上仍放 `public/cover.png` 肖像。portal 卡片照舊用 `cover.png`，兩邊的身分記號一致；`og:image` 也仍是它。
- 各站**不放** `public/cover.svg`（舊制已廢；2026-08-15 已把 62 站的殘留檔掃掉，全星系歸零）。favicon 由 core 提供。

## 4. 書架 Bookshelf（書縮圖 = SSOT）

- 用 `@nplus-father/notes-core/Bookshelf.astro`，`books` 由各站 `src/data/books.ts`（`{slug, title}[]`）提供。
- 縮圖直接吃書 repo 的封面 `https://nplus.wiki/<book-slug>/cover.png`——**single source of truth**，圖歸書 repo 管，筆記站不另存。
- 書的歸屬集中在首頁書架；內文頁不必逐段重述書名，改在 frontmatter `furtherReading` 逐條溯源。
- **v0.10.0 起**：站台若提供 `bibliography`（§4.1），書架自動取其中 `owned` 項——`books.ts` 退役，盤點表成為單一資料源。

## 4.1 藏書盤點／學派地圖／思想側寫（v0.10.0）

首頁三個選配區塊，型別與 helpers 在 `@nplus-father/notes-core/library`，資料放各站 `src/data/*.ts`，經 `astro.config.mjs` 傳入整合器：`notesCore({ site, bibliography?, schools?, profile? })`。

- **`bibliography.ts`（`defineBibliography`）**：人物站 = 作者**全集**、主題站 = 領域**公認經典**的完整盤點。每筆 `{title, original?, year?, slug?, status, note?, group?}`；`status`: `owned`（連書站）/ `wanted`（待收）/ `unavailable`（絕版、無中譯）/ `skipped`（刻意略過＋原因）。**缺口如實列出**——盤點表兼作收書 roadmap（這是**寫資料時的規矩**；v0.20.0 起表頭那行只報進度與圖例，不再把這句印在頁面上）。`year` 從「可有可無的補充」升格為**排序與年代分佈圖的軸**，新資料盡量補上。
- **`schools.ts`（`defineSchools(entries, {kind?, lede?})`）**：主題站的**領域地圖**。每張卡 `{name, icon?, claim, figures?, categorySlug?}`；`figures[].site` 填 sites.ts 的 key 即跨站連結作者站——主題站因此成為串起作者站的樞紐。第二參數選配：`kind` 三選一決定標題與副標（**詞彙表收在 core 的 SchoolsMap，站台只挑 enum**）——`"schools"` 學派地圖＝流派互相對立（預設）｜`"methods"` 方法地圖＝方法體系並存（敏捷、設計思考…）｜`"themes"` 主題地圖＝核心命題分區（歷史、科學…）；`lede` 一句話提綱挈領。舊的純 array 形式視同 schools 口味（向後相容）。
- **`profile.ts`（`defineProfile`）**：人物站的思想側寫。`thesis`（一句話中心思想）＋ `contributions`（研究主軸，`conceptPath` 連站內概念頁）＋ `readingPath`（slug 由 bibliography 反查書名）＋ `influences`（思想脈絡，有姊妹站就跨站連結）。

慣例：人物站給 `profile + bibliography`，主題站給 `schools + bibliography`——**v0.19.0 起兩者升格為該站型的必備區塊**（缺的列入 note-check 紅燈；存量站隨 enrich 補）。試點範本見 `drucker-note`（人物）與 `investing-note`（主題）。

## 4.2 首頁總覽（v0.29.0）

`src/data/overview.ts`（`defineOverview`），與其他三份資料同一個歸位，經 `astro.config.mjs` 的 `overview` 傳入整合器。

```ts
export const overview = defineOverview({
  kind: "person", // domain 主題站｜person 人物站
  writtenAt: "2026-08-11",
  lede: "一句話把形狀講完（允許行內 HTML）",
  sections: [{ heading: "背景", body: "……" }],
});
```

- **為什麼要有它**：首頁其餘三區都是結構化的卡片與表格——掃得很快，但掃完只知道「有哪些東西」，不知道「這個領域長什麼樣」。那句判讀只有連貫散文寫得出來，卡片的一句話 `claim` 裝不下。書站的「深度概覽」是同一個東西的書本版。
- **段落骨架**（`/note-overview` 產出的預設，站台可增減）：主題站 = 這個領域現在的樣貌／幾條主線／收錄之後讀出來的判讀；人物站 = 背景／貢獻／主要論點。
- **`body` 是 HTML 不是 Markdown**（走 `set:html`，與 `heroLede`、`schools.claim` 同一個慣例）。要粗體寫 `<strong>`，寫 `**…**` 只會原樣印出星號。
- **一段連貫敘事，不要寫成條列**——條列版首頁已經有三個了。
- **`writtenAt` 記日期而非布林**：書單再進新書、概念頁再翻修，判讀就會過期，日期自帶時效判讀（與 `site.curation` 同一個理由）。渲染在標題列右端。
- 產出與更新走 **`/note-guide`**（2026-08-14 起，原 `/note-overview` 併入；正本在 `tools/claude-code-commands/`）——導覽寫完順手以其為底刷新總覽。

## 5. 內容頁結構（概念 / 題目）

### 5.1 Frontmatter（schema = `@nplus-father/notes-core/content` factory）

`title / category(或 domain) / importance / status / related / furtherReading / seeAlso`。**每個內容單元都要能溯源**到某本 owned book：`furtherReading: [{book, label, anchor?}]`，`anchor` = 線上書路徑（如 `docs/2-distributed-data/7-sharding/`）；不確定就省略，避免深連 404。

`label` 慣例 **「書名 — 章節」**（破折號分隔）如今是 load-bearing：頁尾「Further Reading」渲染成**卡片**——破折號後段（章節）當子標題主角、書名退為小字、右側配書圖（吃書架同一個 cover 代理）；頁首 SourceByline 取破折號前段（書名）。沒有分隔號的 label 整句當子標題、不出書名小字。

> **分隔號寫全形破折號 `—`**（或 en dash `–`，或**前後有空白**的 ` - `）。拆法（`splitBookLabel`）刻意不認貼著字的 ASCII 連字號——書名常含連字號（The Non-Designer's…／High-Performance…／Test-Driven…），無條件拆會把書名攔腰斬成「The Non」，而錯的那半正好是卡片最大的字。

### 5.2 正文骨架（固定順序）

```markdown
> 一句話點題（blockquote）

::core

> [!TIP]
> 直覺／心智模型（一句話抓住本質）

- 要點…

## ⚖️ 關鍵權衡

:::details{title="…"}

- 取捨…

:::

::takeaways

- 收斂重點…

:::response
:::
```

- 區塊標題由 **`::<name>` leaf directive** 產生（notes-core `remark-sections`，v0.5.0 起）：站上寫 `::core`，渲染成「🧠 Core Ideas」的 h2。英文標籤與 emoji 的詞彙表在 `src/plugins/remark-sections.mjs`，改字一處生效。手寫 `## 🧠 核心概念`／`## 🔑 總整理` 是 v0.5.0 前的舊骨架（`note-check` §2.6 列 nit；2026-11-06 最後 13 頁清完，全星系歸零）。
- 第一個區塊一律 `::core`（技術站族可用 `::intuition`），收尾一律 `::takeaways` → `:::response`。
- **分站族詞彙**（同一份外掛，各族挑自己的）：通用 `core`／`case`／`takeaways`；技術站 `intuition`／`tradeoffs`／`whentouse`／`structure`／`antipatterns`；clean-code `whyproblem`／`whymatters`／`refactor`；behaviour-interview `discussion`／`signals`／`pitfalls`／`questions`／`star`／`scenario`；system-design `requirements`／`reference`；leetcode `approaches`。
- 題目頁的架構圖放在 `::core` 的 TIP 之後，一頁一張（見 §5.4「架構圖」）。
- 中段的 `## ⚖️ …` 仍是手寫 h2（標題是內容，各頁不同），摺疊用 `:::details{title="…"}`（notes-core `remark-details`）。
- Alert 用 `> [!TIP] / [!NOTE] / [!WARNING]`。
- **頁型 `kind`（v0.38.0）**：`claim`（預設，一頁一主張）｜`debate`（一個問題、多本書吵——各方主張並排、各自溯源，不下裁決；裁決與閱讀順序歸 guide 的 Verdict）。選型的決策樹在 `note-check` §1.4。

### 5.3 兩層模型（**書本位** vs **心得層**）

- **正文層 = 書本位**：內容精確由 owned books 組成、可溯源；引不到書的主張不寫進正文。譯者角色限縮在繁中轉譯、結構、串接、illustrative 程式碼。
- **心得 / Q&A 層 = `:::response`**：與正文**分開、明標**（notes-core `remark-response` 渲染成「✍️ 我的回應」）。**只收**真實 Q&A 或使用者心得；沒有就留空。**不自行杜撰這層。** **v0.44.0 起空塊不渲染**：來源檔仍保留 `:::response` 空區塊當兩層模型的標記，頁面上什麼都不出現——與 topnav 的 Check／Guide「有資料才出現」同一原則。v0.43 以前畫一個「No notes yet」空框，2026-11-06 盤點時 2233 頁有 2197 頁是那個空框，佔位變成了噪音。

### 5.4 閱讀頁版面（概念／題目，v0.46.0）

資料與骨架照 §5.1–5.3，一個字不改；以下是它怎麼排。

- **頁首**：書眉 `<VolumeHead>`（§1.7，右端是站符號的小徽記）→ `--fs-h1` 標題（`標題（English）` 拆成中文主標＋下一行拉丁斜體副標）→ 3px `--vol` 色線，橫跨 12 欄。
- **邊注欄（marginalia）**：左 3 欄、sticky 在 nav 下：`From`（來源書，斜體）、`Importance`（5 格小方塊，實心數＝重要度，不用星星）、題目頁多一行 `Difficulty`（三格墨色步階＋字）、`Contents`（h2 清單，目前區塊印點，捲過視窗 35％ 才換）。`Draft` 不顯示。≤ 900px 邊注收成標題下的兩行，Contents 收進一個 `+` 開關。
- **正文欄**：從第 4 欄起、7 欄寬的置中行長（`--measure`），18px sans、行高 1.88；中文段落的手動換行在 build 時接回（`remark-reading`）。表格與程式碼可以**破格到 9 欄**，表格依內容寬度選「行長內」或「整個格線」；手機橫捲。
- **點題句（standfirst）**：正文第一個 blockquote 升格為 `--fs-lede` 襯線段落，不要灰底框，下方一段墨色短橫線收尾；太長的改用 `--fs-intro`，超過一段的退回內文樣式（`is-body`）。**整站只有這裡與導覽章首用襯線排段落**，其餘內文一律 sans。
- **編號區塊**：`::core` 這類 directive 與手寫 `##` 的 h2 一律自動編號——上緣墨線、等寬 `01`、襯線標題；directive 的 emoji 包進 `.sec-emoji` 後隱藏，手寫 `## ⚖️ …` 的 emoji 屬內容、原樣保留。
- **Alert（callout）**：不要整塊色底。上下各一條髮絲線，左上角 `--fs-label` 類型標籤配一個語意色小記號——TIP 圓點、NOTE 方點、IMPORTANT 菱形、WARNING 三角、CAUTION 斜線圈——靠形狀而不只靠顏色區分。
- **details**：一列一條、右端 `+`／`−`，展開有高度過渡，不要白卡片。
- **對照圖（compare figures）**：clean-code 一類的 Before／After 對照是編號的圖（`□ 01`），摘要（`BEFORE`／`AFTER` 各一行）留在行長內；打開的分欄才破格到 9 欄、自己一條墨線，兩欄的說明是小字圖說。手機上 Before／After 疊成兩行。
- **架構圖（`::figure`）**：內文寫一行 `::figure[圖說]{src="./<slug>.svg"}`，SVG 與 `.md` 同資料夾（content loader 只收 `.md`，SVG 不進集合）。`remark-figure` 在 build 時把 SVG **內嵌**進頁面——不是 `<img>`，因為只有內嵌的 SVG 吃得到頁面的 CSS 變數，深淺色才會跟著切；兩張 PNG 輪流換要維護兩份、也縮放不了。圖是編號的圖：與對照圖共用 `Fig. 01` 計數，上緣一條墨線、破格到 9 欄，圖說是小字 `figcaption`。SVG 只准用 `reading/_figure.scss` 的詞彙上色——`d-box`（`is-store` 資料儲存、`is-key` 題目的關鍵決策，墨色實心反白字，一圖最多兩個）、`d-edge`（`is-async` 虛線、`is-key` 粗墨線）、`d-head` 箭頭、`d-zone` 分區虛線、`d-sub`／`d-label`／`d-tag`／`d-mono` 文字；外掛遇到寫死的 `fill`／`stroke` 顏色、`style`、`<style>`、`<script>`、`<image>`、字型屬性，或缺 `viewBox`／`<title>`／`<desc>`／圖說，build 直接失敗。`<title>`＋`<desc>` 經 `aria-labelledby`／`aria-describedby` 給輔助科技，`desc` 要用一段話把圖講完；id 自動加前綴，一頁多張不撞。SVG 文字不進 Pagefind 索引（圖說會進）。寬度：桌機撐滿 9 欄；容器窄於 `viewBox` 寬的 0.86 倍時（手機、窄平板）改為橫捲，捲動窗與程式碼同一套邊緣淡出與 `Scroll →` 提示——字不會縮到讀不了。不用 Mermaid：它在瀏覽器執行期排版、要另載一支大 JS，且版面無法逐張調到能讀。
- **程式碼**：頂端一行語言標籤＋`Copy` 鍵；0.9rem、行高 1.65，深淺各一套 shiki 主題（淺色的 token 色在紙色程式底上過 AA）；**手機也不軟換行**，橫向溢出時隨捲動位置在被切的一側淡出，並出一次捲動提示。
- **頁尾（end matter）**：Further Reading／Dive Deeper／Related 統一成一列一條的清單（書封縮圖＋章節標題＋書名，hover 整列底線畫出）；上一頁／下一頁是兩個並排的大字襯線連結，不要方框；最後是一行 `<VolumeColophon>` 版權行（卷號、站名、章）。

## 6. 概念總覽 = 分層學習路徑

`/concepts` 總覽由整合器產生，畫**分層學習路徑**：每個分類把概念由 `基礎 → 進階` 排成一條 rail，已寫＝實心可點、待寫＝空心「待寫」，附 `done/total` 進度。

- 資料源＝各分類 `src/content/concepts/<cat>/_index.md` 的 **`roadmap`** 欄位：`[{slug, title, tier:'basic'|'advanced'}]`。
- 已寫 vs 待寫由實際 `.md` 檔決定（SSOT）；`roadmap` 的 planned 節點＝**書已涵蓋、頁未寫**的 backlog，每個都應可溯源到某本 owned book 的章節。
- **v0.46.0 外觀＝一本書的目錄頁加一張星圖**：頁首左邊是書眉、`Concepts` 大標、`80 WRITTEN · 10 CHAPTERS`，下面是星圖的圖說（`Pl. II`、`Chart of … Notes`、最亮三顆星的 α β γ 圖例、星等圖例）與章節索引（兩欄、編號＋章名＋頁數）；右邊是星圖。再往下每個分類是一章：左欄 sticky 的章號、章名、`done/total` 進度線；右欄條目以**點線引導**排成目錄行（標題 ······ 標籤），基礎在前、進階在後；待寫的條目淡色、不可點。分類 emoji 不渲染。標題太長折行時不畫點線。
- **星圖（`<StarChart>`，`lib/star-chart.ts`，build 時算好的靜態 SVG）**：每個分類是一個星座、佔圓環上的一個扇區（寬度依頁數分配）；每一頁是一顆星，星等＝`importance`（1–5），已寫實心、待寫空心；連線取同分類內 `related` 的互連，不夠就依 roadmap 順序補。版面由站名當種子的偽隨機數決定，同一站每次 build 都一樣。星座名用展示襯線（中文字級略大），標籤避開格線圓、時角線與扇區邊界，畫在所有星座之上，必要時拉一條不超過標籤高 1.6 倍的引線；外環是分類名與章號，最亮的三顆星標 α β γ 並在圖說列出。整張圖可點：星連到該頁、扇區連到該章。**手機（≤ 600px 或粗指標 ≤ 900px）**：外環只出章號或只出名稱（二擇一，不混排），下方一行「Tap a constellation to jump to its chapter」。描線動畫一個 session 只播一次（§1.3）。
- **分類頁／題庫領域頁（v0.46.0）**：書眉（`CHAPTER 02`）→ 大標 → `6 PAGES · 3 BOOKS` → 分類導言；下面是 `01 — Pages` 的編號清單：每列編號、標題（拉丁副標斜體）、一行摘要、重要度方塊、右端箭頭；待寫的另成 `Planned` 一區。題庫頁同一套，多一欄難度步階。有姊妹站的分類在頁尾給一條「深入 →」文字連結。
- **概念卡／題目卡的狀態點（v0.44.0）**：只有 `studied`／`reviewed` 畫點，`draft` 不畫。`draft` 是 schema 預設值，記的是 Andrew 自己讀過沒；2026-11-06 時 2233 頁有 2134 頁是它，每張卡都一顆灰點等於沒有資訊。資料欄位不變，只是預設狀態不佔視覺。

## 6.1 檢核頁 `/check/`（v0.19.0）

「讀完這站」的定義——**出師條件**。資料源＝各分類 `_index.md` 的 **`mastery`** 欄位：`[{text, slug?}]`，一句一條「認定讀完此分類時該具備的知識」；**roadmap 說讀什麼、mastery 說讀完該會什麼**，兩者同處維護。

- 頁面依分類分組（章號＋分類名；**分類 emoji 不再渲染**，站台資料的 `icon` 欄位保留——灰階半透明的系統 emoji 在評審眼中像破圖，是整頁唯一跳出字體系統的元素），`slug` 填同分類的概念頁 → 渲染「複習 →」回連（只連真的存在的頁）。複習連結靠右對齊成一欄（v0.20.0 的原則不變：句子長短不一時仍排成整齊一行）；v0.46.0 起是無框的 `Review →` 小字連結，桌機在 hover 那一列時才出箭頭。
- **v0.46.0 外觀**：頁首是巨大的進度數字（`16 / 46 MASTERED`）加一條印色進度線；各分類是編號章節，左欄章號、章名與該章進度線。checkbox 自繪（方框，勾選時印色填滿）；整句是 44px 的切換區。**勾掉的句子不畫刪除線、不淡出**——維持全對比，句尾補一個印色 `Mastered` 標記（重讀才是這頁的用途）。
- 勾選記進 localStorage（key = `check:<base>`，62 站同網域不互撞）；頁首與各分類顯示進度。
- topnav 的 Check 只在站台有任何 mastery 時出現；路由恆注入，沒資料時是空狀態頁不是 404。
- mastery 句子維持**書本位**——每句都要能溯源到某本 owned book；存量站隨 `note-check --enrich` 補（記進 ENRICH-BACKLOG），note-check 檢查。

## 6.2 導覽頁 `/guide/`（v0.30.0）

**策展層長文**——「我們收完、讀完這批書之後，怎麼帶你走」。站上的第三種聲音：概念頁正文＝書本位、`:::response`＝使用者層、導覽＝策展層（curator's voice）。由 **`/note-guide`** 產出。

- 資料源＝**guide collection**：`src/content/guide/NN-<slug>.md`，一章一檔、檔名 `NN` 定序；frontmatter `{title, tab?, writtenAt, furtherReading}`（schema 在 content factory；loader base 釘 `src/content` 以免 72 個無導覽站每次 build 印 "base directory does not exist"）。`tab`（v0.32.0）＝tab 列的**固定英文短標**（The Man／Themes／Books／Critiques／Reading；主題站 The Field／Schools…）——中文長題塞 tab 太拗口；缺省退回標題冒號前的主標。
- **v0.46.0 外觀**：書眉＋`Guide` 大標＋`UPDATED` 日期；章節 tab 是帶編號的文字 tab（`01 The Field`），sticky 在 nav 下、底線指示、目前項印點、單行可橫捲。每章左欄是 sticky 的章書眉（`01 — The Field`、`WRITTEN` 日期、本章目錄），右欄 8 欄；章首段落是襯線的 standfirst。
- **章節收進 tab（v0.31.0）**：tab 列 sticky 貼在 topnav 下、一次只顯示一章、**章身自然高度**——固定形式給固定空間，但不固定高度（單章 1,500–7,500 字，固定高度必然框內捲動，頁捲＋框捲巢狀是長文閱讀大忌）。非當前章 `hidden="until-found"`（Ctrl+F 搜得到、命中自動切章）；`#<章id>` 錨點驅動切章，章際互連與站外深連不斷；無 JS 退回五章攤開。頁首無 lede（h1＋章節自己會說話），writtenAt 戳記保留；**無「第N章」眉標**（v0.32.0——tab 列本身已標示位置；v0.46.0 起 tab 前面帶等寬章號 `01`，是書眉語彙，不是章名的一部分）。accent 沿 `data-axis` 分岔（人物暖褐／主題冷藍），導覽天生帶站型識別。`[hidden]` 章的分隔線要歸零——`content-visibility` 藏內容不藏元素自身的 border，否則當前章下面留一疊空線（2026-08-15 抓到的 bug）。
- 章尾 `furtherReading` 用概念頁同款卡片（`<FurtherReading>`）；行長紀律同總覽（42em）。
- 骨架（`/note-guide` 產出的預設五章）：人物站＝這個人是誰／思想主線／經典著作導讀／爭議與侷限／怎麼讀；主題站＝領域在回答什麼問題／流派敘事／經典書導讀／共識與爭點／閱讀路徑。
- topnav 的 Guide 只在站台有 guide 內容時出現（同 Check 機制），**排在最左**（v0.32.0——導覽是「先讀我」的入口，在概念庫之前）；路由恆注入，沒資料時是空狀態頁。
- `writtenAt` 流進 `/index.json` 的 `guide`（章數＋最新日期）——`note-check` 拿它比對 `enrichedAt`，站再深化過而導覽沒跟上就列 warning。

## 6.3 藏書頁 `/library/`（v0.30.0）

盤點表（§2 的遷移注記）＋**開採度圖**。入口兩個：首頁書架標題列的「盤點與開採度 →」＋ topnav 的 **Library（v0.33.0，排在 Search 右邊、整列最右）**——工作文件收在閱讀動線的尾端；有 bibliography 的站才出。

- **開採度（頁面標題 "Coverage"，v0.34.0）**＝每本 owned 書被幾頁筆記（concepts＋problems 的 `furtherReading`）引用，**build 時全自動計算、零人工欄位**。水平條列、單一色相（站台 accent）、行多收捲動窗；**未挖（0 頁）的書不畫零長條**——v0.34.0 起列成**書封牆**（一排小封面，hover 書名，附一句白話說明「已收進書庫、尚無筆記頁引用——下一輪深化的現成材料」），它們的身分本來就是 `note-check --enrich` 的下一批材料。
- **v0.46.0 版面**：頁首是三個大數字加一句話——`On Shelf`（已收錄）、`Cited`（至少一頁引用）、`Citations`（引用總數），各帶一行繁中小註，下面一句白話把數字講完（含只作參考／交姊妹站的本數）。內容分 `Coverage`／`Timeline`／`Inventory` 三區，左欄是 sticky 的區塊導覽（目前區塊印點）。開採度長條、年代圖用站的書布色（`--vol`，§1.6），軸標用 `$mono`；長條多時前段直接列出、其餘收進 `N more`。盤點表是髮絲線表，狀態欄是四個自繪記號（實心方＝已收、空心方＝待收、斜線方＝不可得、短橫＝略過），hover 與 `aria-label` 帶全名；書名連結常駐一條淡灰底線，hover 轉實。
- **讀者用語（設計輪 2）**：統計列是 `Canon`（書目全部）／`On Shelf`（已收錄）／`Cited`（至少一頁引用）／`Uncited`（已收錄未引用，0 時不出）／`Citations`／`Referred`（只作參考或交姊妹站，0 時不出），每格帶一句繁中說明（`title`＋螢幕閱讀器）。`LISTED／MINED／EXEMPT` 是管線術語，不給讀者看。盤點表空的註記／年份畫淡色破折號，不留白格。
- 少於 4 本 owned 不畫（一兩本畫不成分佈）；無 bibliography 時整頁空狀態＋noindex。

## 6.4 搜尋頁 `/search/`（v0.46.0）

- **版面**：書眉（`FULL TEXT`）＋`Search` 大標；一條只有底線的大輸入列（可見的 `Query` 標籤以 `<label for>` 綁在 Pagefind 產生的 input 上，不另設 `aria-label`）；結果排成目錄行（編號、標題＋拉丁副標斜體、分類／難度一行、摘錄），篩選在右欄、手機收成 `Category +` 開關。摘錄去掉與標題、分類重複的開頭；首段沒有命中時改用含命中的子段或內文片段。
- **中文詞組搜尋包裝**：兩字以上的純中文查詢，以「完整詞組」排序在前、拆字結果退後；完整詞組零筆時才顯示拆字結果，並在結果上方一行說明。拉丁字三碼以上的查詢，若最佳結果的命中都不是以查詢字開頭，就視為雜訊回零筆。
- **實作與風險**：包裝是一個 `data:text/javascript` 模組——`import * as pf from "<站>/pagefind/pagefind.js"`＋`export * from` 同一支，再覆寫 `search(term, opts)`；`PagefindUI` 的 `bundlePath` 指向這個 `data:` URL（結尾 `//` 讓 UI 自己補的 `pagefind.js` 落進註解）。它依賴三件事：Pagefind 1.x 的 `pagefind.js` 匯出名稱與 `search()` 的回傳形狀（`results[].id／score／data()`）、`PagefindUI` 接受任意 `bundlePath` 並以它 `import()`、瀏覽器允許從頁面 `import()` 一個 `data:` 模組（站台若加 CSP 要放行 `data:` 的 `script-src`）。`import()` 失敗時自動退回原生 `bundlePath`，搜尋照常可用、只是沒有詞組排序。**升 Pagefind（現行 1.5.x）時要測**：兩字中文詞（如「重構」）的完整詞組排在前、零筆時出現拆字說明行；三碼英文詞；分類篩選勾選與計數；子段結果；console 無錯；以及把 `import()` 故意弄壞時退回原生搜尋。
- 輸入列下方常駐一份 `Browse Concepts` 分類目錄（編號＋頁數）。無 JS 或 Pagefind 載入失敗時，一行說明搜尋暫時無法使用，目錄照樣帶得到每一頁；404 頁的搜尋表單以 `?q=` 帶到這一頁並直接執行。

## 6.5 404（v0.46.0）

左邊一句襯線的「這一頁不在書裡……」＋`NOT FOUND` 眉標、一條底線的站內搜尋表單（`?q=` 送到 `/search/`）、幾個去處（Guide／Concepts／Library、回本站首頁）；右下是描邊的巨大 `404`（`outlined-numeral`，與卷號同一個 mixin），靜態、不淡入。手機上大字在上。

## 6.6 頁尾版權頁（v0.46.0）

`BaseLayout` 的 `<footer class="colophon">`，取代單行 footer：

- 左：書布色小印記（主題站是符號、人物站是卷號）＋書眉（`N°04 — Topic`）＋大字站名（registry `label`）＋寬字距的 `site.brand`。
- 中：`Upkeep`——`Checked`／`Enriched` 兩行日期（`site.curation`，單線圖示，不用 emoji），沒有就不出。
- 右：`Volumes`——依 `sites.ts` 同軸順序的上一卷／下一卷，以及回 `parentSite`（`null` 時不出）。
- 最下一行：印色小方點＋`© 2026 Andrew`（`site.footer` 可覆寫），右側排印說明「Set in Newsreader, Inter & JetBrains Mono; Chinese in the system serif & sans」——說的是真的出貨的字（§1.2），換字時一起改。

## 6.7 試過而撤回（v0.46.0 定案，不要再提）

- **nav 用圖示＋英文標籤**：設計輪推翻「只出 emoji」改成單線圖示，2026-11-13 裁定照 v0.45.0 只出文字分頁——詞彙本身就夠，圖示是第二套要維護的語言。
- **手機底部分頁列與 More 面板**：拇指好按，但與 portal 的導覽不同一套、要藏在捲動後面、還要讓出 safe-area；裁定照 v0.45.0 的頂列單行橫捲。
- **站名進 topnav（桌機站名晶片／手機頂列站名）**：違反 v0.19.0「站名不進 topnav」，身分由人像、首頁 hero 與書眉承擔。
- **Google Fonts 與 Noto Serif TC webfont**：第三方主機，且 CJK webfont 為首頁一個詞多抓數百 KB（§1.2）；拉丁字改由 fontsource 出貨，中文用系統襯線。
- **首頁 hero 進場動畫（書布展開、符號描線、卷號升起）**：即使一個 session 只播一次，仍是「站台沒有進場動畫」的例外；hero 直接是最終狀態。區塊的捲動進場（`.reveal`）同理撤掉。
- **首頁 Overview 排兩欄**：一段連貫的判讀被切成兩欄要上下跳讀，tab 內文長短不一時兩欄也排不齊；回到從第 3 欄起的單欄 8 欄寬。
- **手機程式碼軟換行（懸掛縮排）**：縮排就是程式的結構，折行後讀不出層次；改回不換行＋邊緣淡出＋捲動提示。
- **襯線排導言段落**：長段襯線在螢幕上不好讀；襯線段落只留給點題句與導覽章首，其餘內文一律 sans。
- **分類 emoji 顯示在索引頁與檢核頁**：灰階半透明的系統 emoji 像破圖，是整頁唯一跳出字體系統的元素；資料欄位保留、不渲染。
- **固定朱印（淺 `#c23b22`、深 `#e8654c`，v0.46.0 以前）**：全星系同一個朱紅，跟每一站的書布色打架——藍、綠、紫布旁邊多出一個無關的紅；2026-11-14 改成由書布色相推出的印（§1.6），朱色只留給沒有書布的站當退路。

## 7. 技術注記

- **分類 = 資料夾 + `_index.md`**：`src/content/concepts/<cat>/_index.md` frontmatter 當 config（`name/icon/order/intro/roadmap/mastery`）。題庫站同理 `src/content/problems/<domain>/_index.md`（`site.config` 設 `hasProblems: true`）。
- **站內連結**由 notes-core `withBase()` 處理（base = `/<slug>`）；各站不寫 shim。
- **跨站連結**用 frontmatter `seeAlso`（`site` + `path` + `label`）；schema factory `openSeeAlso: true` 時不寫死 enum。strict 站（技術站群）的 enum＝`sites.ts` 的 `siteKeys`，**v0.44.0 起涵蓋 registry 全部 79 個 key**（v0.43 以前只含技術站自己，技術站因此連不到 uncle-bob／kent-beck／fowler 等作者站——封閉集合是為了抓拼字錯，不是限制去向）。頁級缺口由 `tools/export-seealso-gaps.py` 盤點（判準＝同書同章）。
- **Node** ≥ 20（Astro 需求；`.nvmrc` 釘 22）。若曾在 Node 18 裝過依賴、build 報缺 `@rolldown/binding-linux-x64-gnu`，`rm -rf node_modules package-lock.json` 後在 Node ≥ 20 重裝。
- **站台資料在 dev 會熱更新（v0.37.0）**：`src/site.config.ts` 與 `src/data/*.ts` 只被 `astro.config.mjs` import，不在 Vite 的 module graph 裡，改了不會有任何反應——v0.36.0 以前必須重跑 `npm run dev` 才看得到。現在整合器在 dev 時把 `virtual:notes-core/site` 從「啟動時的 JSON 快照」換成**轉發到真檔案**（`import { overview } from "/src/data/overview.ts"`），Vite 因此會監看它們，存檔約 1 秒生效。前提是站台 config 原封不動轉交同名 export（68 站現行寫法）；名稱對不上就自動退回快照，維持舊行為。**build 路徑不變**（仍是快照，產出經位元比對相同）。
  - 別改用 `addWatchFile` 讓 dev server 重啟解這題：實測 Astro 7.0.7 在 config restart 之後，content layer 的檔案監看不會重新掛上，markdown 從此靜悄悄不再熱更新，直到完整重跑 `npm run dev`。同理，`touch astro.config.mjs` 這個手動招式也有這個副作用。

## 8. 星系成員與撈取

- **GitHub topic `nplus-note`（遠端權威）**：每個 note repo 都打此 topic。撈取：
  ```bash
  gh repo list nplus-father --topic nplus-note --limit 100 --json name,sshUrl
  ```
- **`-note` 命名（本地 fallback）**：`ls -d ~/workspace/andrew/notes/*-note`。
- **notes-core `sites.ts`（星系內部 SSOT）**：`@nplus-father/notes-core/sites` 匯出 `sites`（key/slug/brand/ns）、`siteKeys`。用於姊妹站選單、sitemap、`seeAlso` 白名單。

**開新站用 `/note-new-station` skill**（clone template → `init.sh` → 填 `site.config` + `_index.md` 分類 + 內容 → build）。內容充實用 `/note-check`。
