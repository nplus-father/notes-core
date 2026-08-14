# DESIGN — 筆記星系呈現規範（正本）

`nplus.wiki/<slug>/` 筆記星系各站的**呈現正本**。自 **notes-core v0.4.0** 起，版面／路由／schema 由 notes-core 整合器提供，各站是「純 config + 內容」的薄殼；本檔講「怎麼呈現」，程式碼在 `@nplus-father/notes-core`。

> 這份是**星系唯一正本**（v0.4.0 起不再複製到各站 repo）。星系成員權威清單見 `@nplus-father/notes-core/sites`（`sites.ts`）；遠端撈取用 GitHub topic `nplus-note`（見 §8）。

---

## 1. 版面骨架（notes-core `BaseLayout`）

- **Topnav（v0.19.0）**：左**只放人像**連首頁（與 favicon 同一張圖，core asset）——站名退出 topnav，身分由人像＋首頁 hero 承擔，62 站的導覽列長得一模一樣。右為 `buildNav()` 自動生成的**固定 emoji 分頁**：🧠 Concepts ／（📝 Problems，僅 `hasProblems`）／（✅ Check，僅站台有 mastery 資料）／ 🔍 Search（hover／aria-label 帶英文全名，**不含首頁**）＋ 深淺色切換。詞彙全星系統一、只出 emoji；`conceptLabelEn` / `problemLabelEn` 只用於麵包屑與頁標題，不再影響 nav。姊妹手冊用 `extraNav`（插在 Search 前，想配 emoji 自己寫進 label），特例可用 `nav` 完全覆寫。
- **往上一層（v0.20.0）**：topnav 最左是「‹ 筆記星系」，連 `site.parentSite`（預設 `DEFAULT_PARENT_SITE` = `https://nplus.wiki/notes/`，**不是 wiki 根**——從一個筆記站往上就是那張主題／人物索引）；窄螢幕只留箭頭。同一連結仍在頁尾出現一次；`parentSite: null` 兩處一起隱藏。
- **麵包屑 `<Crumbs>`（v0.20.0）**：所有子頁（分類／概念／題目／檢核／搜尋）統一用這個元件，六個路由不再各寫一份 `<nav class="crumbs">`。**第一項固定是回本站首頁**，做成有框線的返回鍵、文字用 `site.brand` 而非泛稱的 "Home"（62 站同網域，"Home" 是哪個家不自明）；其後才是祖先鏈。於是「star 站 → 本站 → 本層」三級都是一步。
- **Footer**：預設 `© 2026 Andrew`（可用 `site.footer` 覆寫）。不要再加「· 筆記星系的一站 · 延伸閱讀…」那串。
- **favicon**：星系**共用人像**，由 notes-core 以 asset 注入（single source of truth）——各站**不再放** `public/favicon.svg`。
- 深淺色、回想模式（recall）由 notes-core inline script 處理，勿改。
- 版面全在 notes-core：升 `package.json` 的 notes-core 版本即全站同步，**各站不寫 `.astro` 外殼**。
- **v0.11.0 起 astro.config 也收進 core**：各站 `astro.config.mjs` 只剩 `defineNotesAstroConfig({ base, site, bibliography, profile?|schools?, overview? })` 一句（markdown pipeline／shiki／sitemap 由 `@nplus-father/notes-core/astro-config` 工廠提供，Astro 升版遷移只改 core 一處）。`ns` 欄位同時轉 optional，各站已清除。

## 2. 首頁（notes-core `routes/index.astro`）

由上而下：

1. **Hero**：左 `site-cover`（站縮圖 `public/cover.svg`）＋ 右 `site.brand` 標題與 `site.heroLede`。
2. **總覽 `<Overview>`（v0.29.0，見 §4.2）**：首頁唯一的長散文區，排在 hero 之後、其餘區塊之前——**先讀懂「這是什麼」，再往下看結構化的卡片與表格**。反過來排的話，讀者得自己從卡片拼出全貌，而那正是總覽要代勞的事。標題由 `kind` 二選一（領域總覽／人物總覽），**v0.31.0 起無副標**（標題自己講完了）；**lede 常駐、三段收進切換鍵**（機制同盤點表分組鍵：無 JS 攤開、Ctrl+F 命中隱藏段自動切段）。首頁**沒有**導覽入口卡（v0.30.0 曾有、v0.31.0 移除）——導覽動線交給 topnav 的 📖。
3. **思想側寫 `<AuthorProfile>`**（人物站必備，見 §4.1）：中心思想、特定貢獻（連站內概念頁）、建議閱讀路徑（**直式 stepper**：N° 節點＋書封＋一行 why——階段名短、不做名詞解釋條列）、思想脈絡。
4. **領域地圖 `<SchoolsMap>`**（主題站**必備**，見 §4.1）：領域鳥瞰——主張、代表人物（有作者站就跨站連結）、站內分類；標題依 `kind` 三選一（學派／方法／主題地圖），可加一句 `lede` 提綱挈領。卡片上的「站內筆記 →」**v0.20.0 起是鍵不是小灰字**（框線＋箭頭，整張卡 hover 先亮框、滑到鍵上轉主色）——那是每張卡唯一的去處，得看得出可以點。
3. **書架 `<Bookshelf>`**：本站彙整自哪些 owned books（見 §4）。**v0.29.0 起固定高度**（約兩排半封面）＋垂直捲動，標題列右端補書數——書多的站（startup 61 本）攤開就是五六排 190px 的封面。有 bibliography 的站，標題列再補「盤點與開採度 →」連 `/library/`。

> **藏書盤點 `<Bibliography>` 自 v0.30.0 遷往 `/library/`（見 §6.3）**——收藏狀態（owned/wanted/…）是工作文件（採購 roadmap），不是門面。表格本身的規範不變：欄序 = **收錄 → 書名 → 註記 → 年份**；狀態只出 emoji（✅⬜🚫➖，hover 有全名）；**v0.20.0 起**組內依出版年排序＋表格上方的**年代分佈長條圖**（桶寬自適應 10–1000 年、壓進 14 格、「已收錄」堆在「未收」下、少於 4 本不畫）；**v0.29.0 起**分組是切換鍵（預設「全部」、無 JS 退回攤開）。

> 首頁文案（brand / tagline / heroLede / searchLede / searchPlaceholder）全在 `src/site.config.ts`，各站自訂。

## 3. 站縮圖 cover.svg

- 位置：`public/cover.svg`，只用**英文站名** `site.brand` 構圖。
- 尺寸 `1200×630`（og:image 比例），品牌漸層 `#4f46e5 → #7c3aed`。
- 用途：首頁 Hero；亦可掛 `<meta property="og:image">`。
- 原則：**每站一張、由 brand 生成**，不要手抄別站文字。

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

### 5.2 正文標題慣例（固定順序）

```markdown
> 一句話點題（blockquote）

## 🧠 核心概念

> [!TIP]
> 直覺／心智模型（一句話抓住本質）

- 要點…

## ⚖️ 關鍵權衡 (Tradeoffs)

:::details{title="…"}

- 取捨…
  :::

## 🔑 總整理 (Takeaways)

- 收斂重點…

:::response
:::
```

- 第一個 h2 一律 **`## 🧠 核心概念`**。
- 摺疊用 `:::details{title="…"}`（notes-core `remark-details`）。
- Alert 用 `> [!TIP] / [!NOTE] / [!WARNING]`。

### 5.3 兩層模型（**書本位** vs **心得層**）

- **正文層 = 書本位**：內容精確由 owned books 組成、可溯源；引不到書的主張不寫進正文。譯者角色限縮在繁中轉譯、結構、串接、illustrative 程式碼。
- **心得 / Q&A 層 = `:::response`**：與正文**分開、明標**（notes-core `remark-response` 渲染成「✍️ 我的回應」）。**只收**真實 Q&A 或使用者心得；沒有就留空（低調 placeholder）。**不自行杜撰這層。**

## 6. 概念總覽 = 分層學習路徑

`/concepts` 總覽由整合器產生，畫**分層學習路徑**：每個分類把概念由 `基礎 → 進階` 排成一條 rail，已寫＝實心可點、待寫＝空心「待寫」，附 `done/total` 進度。

- 資料源＝各分類 `src/content/concepts/<cat>/_index.md` 的 **`roadmap`** 欄位：`[{slug, title, tier:'basic'|'advanced'}]`。
- 已寫 vs 待寫由實際 `.md` 檔決定（SSOT）；`roadmap` 的 planned 節點＝**書已涵蓋、頁未寫**的 backlog，每個都應可溯源到某本 owned book 的章節。

## 6.1 檢核頁 `/check/`（v0.19.0）

「讀完這站」的定義——**出師條件**。資料源＝各分類 `_index.md` 的 **`mastery`** 欄位：`[{text, slug?}]`，一句一條「認定讀完此分類時該具備的知識」；**roadmap 說讀什麼、mastery 說讀完該會什麼**，兩者同處維護。

- 頁面依分類分組（沿用分類 emoji 與名稱），`slug` 填同分類的概念頁 → 渲染「複習 →」回連（只連真的存在的頁）。**v0.20.0 起**它是**靠右對齊的幽靈鍵**（框線＋箭頭）而非句尾的一行小字——句子長短不一時仍排成整齊一行，一眼看得出每條都能回去重讀；已勾選的那條會連鍵一起淡出。
- 勾選記進 localStorage（key = `check:<base>`，62 站同網域不互撞）；頁首與各分類顯示進度。
- topnav 的 ✅ 只在站台有任何 mastery 時出現；路由恆注入，沒資料時是空狀態頁不是 404。
- mastery 句子維持**書本位**——每句都要能溯源到某本 owned book；存量站隨 `note-check --enrich` 補（記進 ENRICH-BACKLOG），note-check 檢查。

## 6.2 導覽頁 `/guide/`（v0.30.0）

**策展層長文**——「我們收完、讀完這批書之後，怎麼帶你走」。站上的第三種聲音：概念頁正文＝書本位、`:::response`＝使用者層、導覽＝策展層（curator's voice）。由 **`/note-guide`** 產出。

- 資料源＝**guide collection**：`src/content/guide/NN-<slug>.md`，一章一檔、檔名 `NN` 定序；frontmatter `{title, writtenAt, furtherReading}`（schema 在 content factory；loader base 釘 `src/content` 以免 72 個無導覽站每次 build 印 "base directory does not exist"）。
- **章節收進 tab（v0.31.0）**：tab 列 sticky 貼在 topnav 下、一次只顯示一章、**章身自然高度**——固定形式給固定空間，但不固定高度（單章 1,500–7,500 字，固定高度必然框內捲動，頁捲＋框捲巢狀是長文閱讀大忌）。非當前章 `hidden="until-found"`（Ctrl+F 搜得到、命中自動切章）；`#<章id>` 錨點驅動切章，章際互連與站外深連不斷；無 JS 退回五章攤開。頁首無 lede（h1＋章節自己會說話），writtenAt 戳記保留。章序用**襯線中文數字**（第一章…），accent 沿 `data-axis` 分岔（人物暖褐／主題冷藍），導覽天生帶站型識別。
- 章尾 `furtherReading` 用概念頁同款卡片（`<FurtherReading>`）；行長紀律同總覽（42em）。
- 骨架（`/note-guide` 產出的預設五章）：人物站＝這個人是誰／思想主線／經典著作導讀／爭議與侷限／怎麼讀；主題站＝領域在回答什麼問題／流派敘事／經典書導讀／共識與爭點／閱讀路徑。
- topnav 的 📖 只在站台有 guide 內容時出現（同 ✅ 機制）；路由恆注入，沒資料時是空狀態頁。
- `writtenAt` 流進 `/index.json` 的 `guide`（章數＋最新日期）——`note-check` 拿它比對 `enrichedAt`，站再深化過而導覽沒跟上就列 warning。

## 6.3 藏書頁 `/library/`（v0.30.0）

盤點表（§2 的遷移注記）＋**開採度圖**。首頁入口＝書架標題列的「盤點與開採度 →」；不進 topnav——nav 留給閱讀動線，工作文件走首頁動線。

- **開採度**＝每本 owned 書被幾頁筆記（concepts＋problems 的 `furtherReading`）引用，**build 時全自動計算、零人工欄位**。水平條列、單一色相（站台 accent）、行多收捲動窗；**未挖（0 頁）的書不畫零長條**——列成 chip 工作清單，它們的身分本來就是 `note-check --enrich` 的下一批材料。
- 少於 4 本 owned 不畫（一兩本畫不成分佈）；無 bibliography 時整頁空狀態＋noindex。

## 7. 技術注記

- **分類 = 資料夾 + `_index.md`**：`src/content/concepts/<cat>/_index.md` frontmatter 當 config（`name/icon/order/intro/roadmap/mastery`）。題庫站同理 `src/content/problems/<domain>/_index.md`（`site.config` 設 `hasProblems: true`）。
- **站內連結**由 notes-core `withBase()` 處理（base = `/<slug>`）；各站不寫 shim。
- **跨站連結**用 frontmatter `seeAlso`（`site` + `path` + `label`）；schema factory `openSeeAlso: true` 時不寫死 enum。
- **Node** ≥ 20（Astro 需求；`.nvmrc` 釘 22）。若曾在 Node 18 裝過依賴、build 報缺 `@rolldown/binding-linux-x64-gnu`，`rm -rf node_modules package-lock.json` 後在 Node ≥ 20 重裝。

## 8. 星系成員與撈取

- **GitHub topic `nplus-note`（遠端權威）**：每個 note repo 都打此 topic。撈取：
  ```bash
  gh repo list nplus-father --topic nplus-note --limit 100 --json name,sshUrl
  ```
- **`-note` 命名（本地 fallback）**：`ls -d ~/workspace/andrew/notes/*-note`。
- **notes-core `sites.ts`（星系內部 SSOT）**：`@nplus-father/notes-core/sites` 匯出 `sites`（key/slug/brand/ns）、`siteKeys`。用於姊妹站選單、sitemap、`seeAlso` 白名單。

**開新站用 `/note-new-station` skill**（clone template → `init.sh` → 填 `site.config` + `_index.md` 分類 + 內容 → build）。內容充實用 `/note-check`。
