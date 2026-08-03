# Phase C — 共用核心 notes-core（已完成）

**狀態：已上線。** 六站 + note-template 都吃共用核心，六站 Deploy 全綠、`https://nplus.wiki/<slug>-note/` HTTP 200。

## 最終做法：git 依賴（非 GitHub Packages）

org 政策**禁止 public npm package**，private package 跨 repo 讀取又麻煩。改用 **git 依賴**：

```jsonc
// 各站 package.json
"dependencies": {
  "@nplus-father/notes-core": "github:nplus-father/notes-core#v0.1.0"
}
```

notes-core 的 **repo 是 public** → npm 直接 clone。**零 token、零 .npmrc、零 registry**，CI 與本機都免設定。Renovate 升 git tag。

- 共用套件：`@nplus-father/notes-core`（repo：github.com/nplus-father/notes-core）—— `withBase` / `createReviews(ns)` / `remark-details` / 設計 token / `Stars.astro`。
- 消費端接法：`url.ts`/`reviews.ts` 用 2 行 shim、`_tokens.scss` 用 1 行 `@forward`、Stars 改吃套件。呼叫端零改動。
- 複習 namespace：cc / ci / ds / dp / lk / sd（新站避開；`init.sh` 會設 `__NS__`）。
- 發新版：在 notes-core `npm version patch && git push --follow-tags`，再讓 Renovate（或手動）把各站 `#vX.Y.Z` 升上去。
- 再接新站/重接：用 `./rewire-notes-core.sh <dir> <ns> [tag]`。

## 可選的清理（非必要，我做不到／被 auto 模式擋）

1. `nplus-father/workflows` @v1 還留著 Phase C 中途加的 GitHub Packages 認證設定（registry-url/scope + `NODE_AUTH_TOKEN`）。**對 git 依賴無害**（已驗證），但屬 dead config。要清就在 auto 模式外把那兩支 astro workflow 還原、`v1` tag 移回。
2. `@nplus-father/notes-core` 的 **GitHub Package**（v0.1.0，private）現已無人使用（改吃 git）。可刪。
3. `note-template` 自己的 Actions 會跑 deploy 但沒設 Pages → 可能紅。要清可在該 repo Settings 停用 Actions（不影響由它建立的新站）。

> 歷史：本檔原本描述 GitHub Packages 方案，已被 git 依賴取代。`phase-c-workflows-auth.patch` 亦已作廢。
