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
| `tools/export-orphan-books.py`  | 反向盤點：書庫的書沒站在管、slug 死鏈 `docs/ORPHAN-BOOKS.md`              |
| `tools/export-year-conflicts.py` | 跨站同一本書的 `year`／`original` 不一致 `docs/YEAR-CONFLICTS.md`        |
| `tools/export-deepen-targets.py` | 大部頭卻只被挖一鏟的書 `docs/DEEPEN-TARGETS.md`（只排序，開單留 Fable）  |
| `tools/export-anchor-gaps.py`   | 頁面用了書裡的事實、卻掛到不含它的章 `docs/ANCHOR-GAPS.md`                |
| `tools/export-guide-drift.py`   | 導覽的數字宣稱跟不上站台現況 `docs/GUIDE-DRIFT.md`                        |
| `tools/refresh-galaxy-docs.sh`  | **一次重算上面八份生成文件**並印落差；`--check` 有落差就 exit 1          |

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
| `docs/ENRICH-BACKLOG.md`            | **站已存在但還沒寫完**（缺口靠 `note-check --enrich` 補）；跨站排序          |
| `docs/SOURCING-DEBT.md`             | **內容寫了但查不到出處**（缺口靠掛 `anchor` 補）；2026-08-05 已清空  |
| `docs/WANTED-BOOKS.md`              | **書還沒收**（缺口靠去收書補）；由 `tools/export-wanted.py` 生成     |
| `docs/MISSING-YEARS.md`             | **書收了但沒填出版年**（缺口靠查初版年補）；由 `tools/export-missing-years.py` 生成 |
| `docs/DEEPEN-READY.md`              | **哪些站書收齊了、可以進場深化**（排序表）；由 `tools/export-deepen-ready.py` 生成 |
| `docs/ORPHAN-BOOKS.md`              | **書有了但沒有站在管**，外加死鏈 slug／anchor（缺口靠認領或開站補）；由 `tools/export-orphan-books.py` 生成 |
| `docs/YEAR-CONFLICTS.md`            | **同一本書在不同站填了不同年**（缺口靠挑一個對的補）；由 `tools/export-year-conflicts.py` 生成 |
| `docs/DEEPEN-TARGETS.md`            | **大部頭卻只被挖一鏟**的書（排序表，開單仍留 Fable）；由 `tools/export-deepen-targets.py` 生成 |
| `docs/ANCHOR-GAPS.md`               | **頁面掛的章不含它引用的事實**（缺口靠改 `furtherReading` 補）；由 `tools/export-anchor-gaps.py` 生成 |
| `docs/GUIDE-DRIFT.md`               | **導覽的數字跟不上現況**（站上幾頁、某分類幾頁、收了幾本）；由 `tools/export-guide-drift.py` 生成 |
| `docs/MODEL-ROUTING.md`             | **哪些工作值得花高階模型額度**（分工原則與各輪判準，手維護）        |
| `docs/SERIES-STATUS.md`             | **系列產線帳本**（各波導覽與 enrich 的進度，手維護）                |
| `docs/EXCLUDED-BOOKS.md`            | **裁定不進任何站**的書（品質把關的裁決紀錄，手維護）；orphan 掃描讀它，命中者不列孤兒不再提醒 |

**前十一份是活的、要持續更新；其餘是歷史紀錄，不再維護。** 各自是不同的軸，別混用——
「書有了沒站在管」進 ORPHAN-BOOKS，「有站沒寫完」進 ENRICH-BACKLOG，「查不到出處」進 SOURCING-DEBT，
「書還沒收」進 WANTED-BOOKS，「書收了但沒填出版年」進 MISSING-YEARS，
「哪些站現在可以進場深化」看 DEEPEN-READY，「書有了卻沒有站在管」看 ORPHAN-BOOKS，
「同一本書各站年份打架」看 YEAR-CONFLICTS，「大部頭只挖了一鏟」看 DEEPEN-TARGETS，
「延伸閱讀掛錯章」看 ANCHOR-GAPS，「導覽數字過期」看 GUIDE-DRIFT
（後八份是生成物，改各站 bibliography／內容再重跑，不要手改）。

> **八份生成物用 `tools/refresh-galaxy-docs.sh` 一次重算，不要單獨跑其中一支。**
> 生成物停更會開始騙人，而它看起來跟剛跑完一模一樣——2026-08-10 實測，committed 的
> WANTED-BOOKS 說「先扣掉 0 本」，當場重跑是 23 本，採購前 20 名裡 2 本早就建好書站了。

> **正向與反向要成對看**：WANTED-BOOKS／DEEPEN-READY 都是「**站**說它缺什麼」，
> 看不到「沒有任何站提過」的書；ORPHAN-BOOKS 是唯一從**書庫**那一側問的，
> 新建的書站沒人認領只有它抓得到。

> **ENRICH-BACKLOG 與 DEEPEN-READY 的分工**：前者是**做過什麼**的工作日誌（抽查輪次、
> 契約債結案），手維護；後者是**現在該做什麼**的排序表，每次重算。原本 ENRICH-BACKLOG
> 裡那張手寫的「頁少書多」排序表已由 DEEPEN-READY 取代——手寫的掃描日一停就過期
> （2026-08-09 那份還停在 07-31，中間 68 站的 bibliography 已經翻過好幾輪）。

## 資料的三種身分（防漂移的規則）

星系裡每一份資料檔只能是兩種身分之一，**第三種禁止存在**：

| 身分 | 是什麼 | 規則 |
| --- | --- | --- |
| **正本** | 手寫、唯一權威。`bibliography.ts`（本站收了哪些書、判什麼層）、concept frontmatter 的 `furtherReading`（誰引了誰）、books-done 的 repo 與 topics（書庫有哪些書）、`goals.yaml`／`health-waivers.yaml`／`EXCLUDED-BOOKS.md`（決定與裁決） | 只有它能被手改 |
| **衍生** | 從正本算出來。`docs/` 那四份、portal 的 `health.json`／`overview.json`／`stations.json`／`site-meta.json`、各站的 `/index.json` | **不准手改**，必須有一鍵重生的指令，而且要**自報生成時間** |
| ~~手抄交集~~ | 兩個正本的交集被抄成第三份 | **不要建**。它對兩邊同時漂移 |

第三種是真的發生過：各站的 `BOOKS.md` 是 `bibliography.ts` 與 books-done 的手抄交集，
2026-08-24 實測 75 站裡有 65 站對不上——往後**落後 640 筆**、往前**超前 112 筆**、
外加 7 條死鏈。**兩個方向同時漂**，正是「抄交集」的特徵。該檔已全數退役。
想再抄一份清單出來之前，先問它會對誰過期。

三條配套原則：

1. **衍生物一停更就開始騙人，而且看起來跟剛跑完一模一樣。** 所以 `docs/` 的四份在 H1
   底下有一行生成戳記（`tools/_stamp.py`），portal 的每份 JSON 有 `generatedAt`。
   `refresh-galaxy-docs.sh` 的落差檢查用 `git diff -I` 忽略戳記行，否則它會永遠報「有變動」。
2. **沿用前值（carry-over）要能被看見。** 抓不到就沿用是對的，但沿用值與新鮮值在資料上
   長得一模一樣——書站 404 之後那一筆會永遠留著，而且在頁面上看起來完全健康。
   所以筆數要寫進資料本身（`health.json` 的 `carriedOver`）並顯示在 `/health/`，
   不能只印在沒人會翻的 CI log。
3. **正本之間的一致性靠稽核，不靠同步。** 同步會製造第三份副本；稽核不會。
   `tier-audit.py` 是這個形狀：不產生資料、不修改資料，只報「A 說的和 B 說的不一致」。

判層稽核的邏輯刻意有兩份實作——`src/lib/audit.ts`（build 時算完，隨 `/index.json`
發佈給 portal 與 CLI 消費）與 `tools/tier-audit.py`（讀工作區，給「剛改完想馬上看」）。
兩份是必要的（發佈的結論不能要求消費端 clone 76 個 repo；工作區的回饋不能等部署），
但**兩份實作就是兩份會各自演化的東西**，所以用 `tier-audit.py --verify` 逐站對帳六個數字。
它上線第一次就抓到一個真 bug：TS 的 `[\s,.:-—]` 被讀成字元範圍（U+003A–U+2014，
涵蓋整個英文字母表），把 `"The Unicorn Project"` 這類候選詞整段剝成空字串，
於是 4 站 5 本書被誤判成空頭支票。**被監控的重複，比沒人看的重複安全得多。**

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
