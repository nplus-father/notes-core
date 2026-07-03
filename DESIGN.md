# DESIGN — 筆記星系呈現規範（正本）

`nplus.wiki/<slug>/` 筆記星系各站的**呈現正本**。自 **notes-core v0.4.0** 起，版面／路由／schema 由 notes-core 整合器提供，各站是「純 config + 內容」的薄殼；本檔講「怎麼呈現」，程式碼在 `@nplus-father/notes-core`。

> 這份是**星系唯一正本**（v0.4.0 起不再複製到各站 repo）。星系成員權威清單見 `@nplus-father/notes-core/sites`（`sites.ts`）；遠端撈取用 GitHub topic `nplus-note`（見 §8）。

---

## 1. 版面骨架（notes-core `BaseLayout`）

- **Topnav**：左 `site.brand` 連首頁；右為 `site.nav` 分頁（首頁／主題（或概念）／題庫／🔍 搜尋，依站啟用）＋ 深淺色切換。
- **Footer**：預設 `© 2026 Andrew`（可用 `site.footer` 覆寫）。不要再加「· 筆記星系的一站 · 延伸閱讀…」那串。
- **favicon**：星系**共用人像**，由 notes-core 以 asset 注入（single source of truth）——各站**不再放** `public/favicon.svg`。
- 深淺色、回想模式（recall）由 notes-core inline script 處理，勿改。
- 版面全在 notes-core：升 `package.json` 的 notes-core 版本即全站同步，**各站不寫 `.astro` 外殼**。

## 2. 首頁（notes-core `routes/index.astro`）

由上而下：

1. **Hero**：左 `site-cover`（站縮圖 `public/cover.svg`）＋ 右 `site.brand` 標題與 `site.heroLede`。
2. **書架 `<Bookshelf>`**：本站彙整自哪些 owned books（見 §4）。
3. **分類格**：`site.homeShowCategories: true` 時顯示分類卡片（icon／name／intro／已寫頁數）。純內容站點常開；不想重複 topnav 就設 `false`。

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

## 5. 內容頁結構（概念 / 題目）

### 5.1 Frontmatter（schema = `@nplus-father/notes-core/content` factory）

`title / category(或 domain) / importance / status / related / furtherReading / seeAlso`。**每個內容單元都要能溯源**到某本 owned book：`furtherReading: [{book, label, anchor?}]`，`anchor` = 線上書路徑（如 `docs/2-distributed-data/7-sharding/`）；不確定就省略，避免深連 404。

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

## 7. 技術注記

- **分類 = 資料夾 + `_index.md`**：`src/content/concepts/<cat>/_index.md` frontmatter 當 config（`name/icon/order/intro/roadmap`）。題庫站同理 `src/content/problems/<domain>/_index.md`（`site.config` 設 `hasProblems: true`）。
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

**開新站用 `/note-new-station` skill**（clone template → `init.sh` → 填 `site.config` + `_index.md` 分類 + 內容 → build）。內容充實用 `/note-enrich`。
