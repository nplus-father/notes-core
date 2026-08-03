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

## tools/ — 星系操作腳本（不發佈）

`bin/` 是**站內**工具，跟著套件裝進每一站；`tools/` 是**站外**工具，站在星系的視角一次操作很多個 repo。

判準只有一條：**需要 host 環境依賴（`gh`、`git push`、headless Chrome、ImageMagick）或會跨 repo 寫入的，一律放 `tools/`，且不列進 `package.json` 的 `files`。** 62 站建置時會 import notes-core，不該把這些拖進那條依賴鏈。

| 腳本                            | 用途                                                                     |
| ------------------------------- | ------------------------------------------------------------------------ |
| `tools/new-note.sh`             | 開新站：建 repo、套模板、打 `nplus-note` topic、自動入列 `sites.ts`       |
| `tools/bump-notes-core.sh`      | 把所有站的 notes-core 釘版 bump 到新 tag，逐站重裝＋驗 lockfile＋build    |
| `tools/cover/render.sh`         | 重繪主題站封面 PNG（需 Chrome + ImageMagick）                            |
| `tools/rewire-notes-core.sh`    | ⚠️ 已退役，保留考古；新站請走 `new-note.sh`                              |

星系根目錄（放所有 `-note` 站的容器目錄）預設由腳本自己推導成 `notes-core/../..`；佈局不同時用
`NOTES_ROOT=` 覆寫。

**為何各站用 git 依賴而非 GitHub Packages**：org 政策禁止 public npm package，而 private package
跨 repo 讀取很痛。notes-core 的 *repo* 是 public，故直接 `github:nplus-father/notes-core#<tag>`
由 npm clone——零 token / 零 `.npmrc` / 零 registry。

代價是 **npm 對「只有 committish 變」的 git 依賴會沿用 lockfile 舊 `resolved`**：改了 tag、`npm install`
跑完、build 還是綠，裝的卻仍是舊版（2026-07-20 一次 44 站 bump 就這樣整批做白工）。所以
`bump-notes-core.sh` 在 build 之前先比對 `package-lock.json` 裡的 commit sha——**build 綠不是升級成功的證據，lockfile 的 sha 才是。**

## 發布

版本以 `package.json` 為準。推 `v*` tag 觸發 `.github/workflows/publish.yml`，用 repo `GITHUB_TOKEN` 發到 GitHub Packages：

```bash
npm version patch   # 或 minor / major
git push --follow-tags
```
