# @nplus-father/notes-core

技術筆記星系（`nplus.wiki`）Astro 筆記站的**共用核心套件**，是 books 端 `nplus-book-core` 的 Astro 對應物。抽出六個 note 站真正不變的核心，各站當 dependency 安裝，Renovate 升版。

以原始碼形式發布（`.ts` / `.astro` / `.scss`）——由各消費站台的 Astro/Vite 建置時編譯，套件本身無 build step。

## 內容（v0.1.0）

| export | 用途 |
|---|---|
| `withBase(path)` | 站內路徑接 base 前綴（`import.meta.env.BASE_URL` 以消費端 base 代換） |
| `createReviews(namespace)` | localStorage 複習紀錄 factory。**六站共用 nplus.wiki 網域故共用 localStorage，namespace 必須各站唯一**（`lk` / `cc` / `dp`…） |
| `todayStr()` | 本地時區 `YYYY-MM-DD` |
| `@nplus-father/notes-core/remark-details` | `:::` 摺疊區塊 remark 外掛 |
| `@nplus-father/notes-core/styles/tokens.scss` | 設計 token（`@use` 進各站 global.scss） |
| `@nplus-father/notes-core/Stars.astro` | ★ 重要性星等元件 |

**不收（各站差異為刻意）**：BaseLayout、global.scss 領域段落、content schema、分類資料、StatusBadge（狀態詞彙各站不同）、ConceptCard/題目卡等領域元件。

## 消費端用法

```jsonc
// .npmrc（各消費 repo 根目錄）
// @nplus-father:registry=https://npm.pkg.github.com
// //npm.pkg.github.com/:_authToken=${NODE_AUTH_TOKEN}
```

```ts
import { withBase, createReviews } from "@nplus-father/notes-core";
import remarkDetails from "@nplus-father/notes-core/remark-details";
import Stars from "@nplus-father/notes-core/Stars.astro";
const reviews = createReviews("lk"); // → localStorage key "lk-reviews"
```

```scss
// src/styles/global.scss
@use "@nplus-father/notes-core/styles/tokens.scss" as *;
```

## 發布

版本以 `package.json` 為準。推 `v*` tag 觸發 `.github/workflows/publish.yml`，用 repo `GITHUB_TOKEN` 發到 GitHub Packages：

```bash
npm version patch   # 或 minor / major
git push --follow-tags
```
