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
| `tools/export-wanted.py`        | 匯出全星系 bibliography 的 `wanted` 成採購清單 `docs/WANTED-BOOKS.md`     |
| `tools/export-missing-years.py` | 匯出全星系 bibliography 缺 `year` 的條目成 `docs/MISSING-YEARS.md`        |
| `tools/export-deepen-ready.py`  | 盤點各站書單完成度與頁/書，排出可深化順序 `docs/DEEPEN-READY.md`          |

星系根目錄（放所有 `-note` 站的容器目錄）預設由腳本自己推導成 `notes-core/../..`；佈局不同時用
`NOTES_ROOT=` 覆寫。

**為何各站用 git 依賴而非 GitHub Packages**：org 政策禁止 public npm package，而 private package
跨 repo 讀取很痛。notes-core 的 *repo* 是 public，故直接 `github:nplus-father/notes-core#<tag>`
由 npm clone——零 token / 零 `.npmrc` / 零 registry。

代價是 **npm 對「只有 committish 變」的 git 依賴會沿用 lockfile 舊 `resolved`**：改了 tag、`npm install`
跑完、build 還是綠，裝的卻仍是舊版（2026-07-20 一次 44 站 bump 就這樣整批做白工）。所以
`bump-notes-core.sh` 在 build 之前先比對 `package-lock.json` 裡的 commit sha——**build 綠不是升級成功的證據，lockfile 的 sha 才是。**

## docs/ — 星系規劃文件（不發佈）

跨站的盤點與規劃文件。這些原本散在星系根目錄（`notes/*.md`）**完全沒有版控**——改了沒有歷史、
壞了無法回溯，2026-08-04 收進這裡。同樣不列進 `files`，消費站不需要它們。

| 文件                                | 用途                                                                |
| ----------------------------------- | ------------------------------------------------------------------- |
| `docs/COVERAGE-GAPS.md`             | **還沒有站**的人物／主題（缺口靠開新站補）；附可重跑的掃描腳本      |
| `docs/ENRICH-BACKLOG.md`            | **站已存在但還沒寫完**（缺口靠 `note-check --enrich` 補）；跨站排序          |
| `docs/SOURCING-DEBT.md`             | **內容寫了但查不到出處**（缺口靠掛 `anchor` 補）；2026-08-05 已清空  |
| `docs/WANTED-BOOKS.md`              | **書還沒收**（缺口靠去收書補）；由 `tools/export-wanted.py` 生成     |
| `docs/MISSING-YEARS.md`             | **書收了但沒填出版年**（缺口靠查初版年補）；由 `tools/export-missing-years.py` 生成 |
| `docs/DEEPEN-READY.md`              | **哪些站書收齊了、可以進場深化**（排序表）；由 `tools/export-deepen-ready.py` 生成 |
| `docs/humanities-books-by-domain.md` | 2026-07 人文星系建站期的領域規劃（歷史紀錄）                        |
| `docs/humanities-note-scope-draft.md` | 同上，站別「納入 repo」的範圍界定草稿（歷史紀錄）                 |
| `docs/books-by-domain.md`           | 2026-07 技術六站的參考書來源盤點（歷史紀錄）                        |
| `docs/books-index.md`               | 早期書架照片辨識清單（歷史紀錄）                                    |
| `docs/RUNBOOK-phase-c.md`           | 共用核心上線的 runbook（已完成，歷史紀錄）                          |

**前六份是活的、要持續更新；其餘是歷史紀錄，不再維護。** 六者是不同的軸，別混用——
「沒有站」進 COVERAGE-GAPS，「有站沒寫完」進 ENRICH-BACKLOG，「查不到出處」進 SOURCING-DEBT，
「書還沒收」進 WANTED-BOOKS，「書收了但沒填出版年」進 MISSING-YEARS，
「哪些站現在可以進場深化」看 DEEPEN-READY（後三份是生成物，改各站 bibliography／內容再重跑，不要手改）。

> **ENRICH-BACKLOG 與 DEEPEN-READY 的分工**：前者是**做過什麼**的工作日誌（抽查輪次、
> 契約債結案），手維護；後者是**現在該做什麼**的排序表，每次重算。原本 ENRICH-BACKLOG
> 裡那張手寫的「頁少書多」排序表已由 DEEPEN-READY 取代——手寫的掃描日一停就過期
> （2026-08-09 那份還停在 07-31，中間 68 站的 bibliography 已經翻過好幾輪）。

## 發布

版本以 `package.json` 為準。**沒有 publish workflow**——各站是 `github:nplus-father/notes-core#<tag>`
由 npm 直接 clone（理由見上面「為何各站用 git 依賴」），所以**打上 tag 就等於發布**：

```bash
npm version patch   # 或 minor / major
git push --follow-tags
```

發完別忘了讓各站跟上，否則 core 升了、線上還是舊版：

```bash
tools/bump-notes-core.sh <舊 tag> <新 tag> --push
```
