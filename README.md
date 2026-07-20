# @nplus-father/notes-core

技術筆記星系（`nplus.wiki`）Astro 筆記站的**共用核心套件**，是 books 端 `nplus-book-core` 的 Astro 對應物。抽出六個 note 站真正不變的核心，各站當 dependency 安裝，Renovate 升版。

以原始碼形式發布（`.ts` / `.astro` / `.scss`）——由各消費站台的 Astro/Vite 建置時編譯，套件本身無 build step。

## 內容（v0.1.0）

| export                                        | 用途                                                                                                                          |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `withBase(path)`                              | 站內路徑接 base 前綴（`import.meta.env.BASE_URL` 以消費端 base 代換）                                                         |
| `createReviews(namespace)`                    | localStorage 複習紀錄 factory。**六站共用 nplus.wiki 網域故共用 localStorage，namespace 必須各站唯一**（`lk` / `cc` / `dp`…） |
| `todayStr()`                                  | 本地時區 `YYYY-MM-DD`                                                                                                         |
| `@nplus-father/notes-core/remark-details`     | `:::` 摺疊區塊 remark 外掛                                                                                                    |
| `@nplus-father/notes-core/styles/tokens.scss` | 設計 token（`@use` 進各站 global.scss）                                                                                       |
| `@nplus-father/notes-core/Stars.astro`        | ★ 重要性星等元件                                                                                                              |

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

## CLI

套件帶兩支 bin，消費站在 `scripts` 裡叫用：

| bin                         | 用途                                                                                              |
| --------------------------- | ------------------------------------------------------------------------------------------------- |
| `notes-fmt <write\|check>`  | prettier 的 config／ignore／目標集中在這裡，各站不必再放 `.prettierignore`                        |
| `notes-doctor <check\|fix>` | 依賴版本健檢：對照本套件的 `versions.json`，`check` 報漂移（漂了回非 0，可接 CI）、`fix` 就地改齊 |

`versions.json` 是**星系依賴版本的正本**，只列統一管的套件；站別特有的依賴（例如 `leetcode-note` 的
`unist-util-visit`）不在其中，`notes-doctor` 不會碰。它同時檢查各站釘的 `@nplus-father/notes-core`
是不是最新 tag（需要 `gh`；拿不到就跳過，離線不會變紅燈）。

升星系依賴版本的流程：改 `versions.json` → 發新 tag → 各站 `notes-doctor fix` + `npm install` + build 驗證。

## 發布

版本以 `package.json` 為準。推 `v*` tag 觸發 `.github/workflows/publish.yml`，用 repo `GITHUB_TOKEN` 發到 GitHub Packages：

```bash
npm version patch   # 或 minor / major
git push --follow-tags
```
