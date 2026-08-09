#!/usr/bin/env bash
# 把所有 note 站的 @nplus-father/notes-core 依賴版本 bump 到新 tag，逐站重裝＋建置驗證。
# 前置：notes-core 已 push 新 tag（見下方「發版」步驟）。
#
# 用法：tools/bump-notes-core.sh <old-tag> <new-tag> [--push]
#   tools/bump-notes-core.sh v0.14.0 v0.15.0            # 只 bump + install + build + commit（不 push）
#   tools/bump-notes-core.sh v0.14.0 v0.15.0 --push     # 同上並 git push（觸發各站 GitHub Pages 部署）
#
# SKIP="a-note b-note" 可排除指定站。用途：**別的 session 正在那幾站改稿**——
# 本腳本收工時 `git add src/content`，會把人家還沒寫完的內容一起提交進 bump commit。
# 星系常有多個 session 併行，跑之前先 `git status` 掃一遍，內容還髒的站放進 SKIP。
set -euo pipefail

# 星系根目錄＝放所有 -note 站的容器目錄。本腳本住在 notes-core/tools/，往上兩層就是。
# 佈局不同時用 NOTES_ROOT 覆寫（對應 tools/cover/render.sh 的 --install <notes-root>）。
NOTES_ROOT="${NOTES_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"
cd "$NOTES_ROOT"
ls -d *-note >/dev/null 2>&1 || { echo "✘ $NOTES_ROOT 底下找不到任何 *-note——用 NOTES_ROOT= 指定星系根目錄" >&2; exit 2; }

OLD="${1:?用法: ./bump-notes-core.sh <old-tag> <new-tag> [--push]}"
NEW="${2:?需要 new-tag，如 v0.5.0}"
PUSH="${3:-}"

# 新 tag 對應的 commit sha——用來驗證各站 lockfile 真的重新解析了。
# 為何需要：npm 對「只有 committish 變」的 git dep 會沿用 lockfile 舊 resolved，
# 裝的還是舊 core，build 照樣綠——2026-07-20 一次 44 站 bump 就是這樣整批做白工。
# **build 綠不是升級成功的證據，lockfile 的 sha 才是。**
NEW_SHA=$(git ls-remote https://github.com/nplus-father/notes-core.git "refs/tags/$NEW^{}" | cut -f1)
[ -n "$NEW_SHA" ] || NEW_SHA=$(git ls-remote https://github.com/nplus-father/notes-core.git "refs/tags/$NEW" | cut -f1)
if [ -z "$NEW_SHA" ]; then
  echo "✘ 抓不到 $NEW 的 commit sha——tag 推上去了嗎？（git push origin $NEW）" >&2
  exit 2
fi
echo "目標 $NEW = $NEW_SHA"
echo

# 單站失敗不中斷整批——62 站的視覺大改要的是「跑完看全表」，不是停在第一個紅燈。
FAILED=()
DONE=()

SKIPPED=()

for d in *-note note-template; do
  [ -f "$d/package.json" ] || continue
  if [[ " ${SKIP:-} " == *" $d "* ]]; then
    echo "[$d] 在 SKIP 名單 — 略過"; SKIPPED+=("$d"); continue
  fi
  if ! grep -q "notes-core#$OLD" "$d/package.json"; then
    echo "[$d] 不在 $OLD（可能已 bump 或特殊）— 略過"; continue
  fi
  echo "=== $d : $OLD → $NEW ==="
  if (
    set -e
    cd "$d"
    sed -i "s|notes-core#$OLD|notes-core#$NEW|g" package.json
    # 強制重抓 git 依賴：npm 對「只有 committish 變」的 git dep 常略過重裝，會留下舊 core。
    rm -rf node_modules/@nplus-father/notes-core
    npm install "@nplus-father/notes-core@github:nplus-father/notes-core#$NEW" --silent
    # 先驗 lockfile 再 build——build 過不了不代表沒升級，升級沒生效卻一定 build 得過。
    if ! grep -q "notes-core.git#$NEW_SHA" package-lock.json; then
      echo "  ✘ lockfile 沒指向 $NEW（$NEW_SHA）——npm 沿用了舊 resolved"
      grep -o 'notes-core\.git#[0-9a-f]*' package-lock.json | head -1
      exit 1
    fi
    npm run build:nosearch >/dev/null
    echo "  lockfile OK / build OK"
    git add package.json package-lock.json
    # 舊結構站（如 leetcode-note 自帶 pages/）沒有這兩個路徑，硬 add 會 fatal 中斷整批
    [ -f src/site.config.ts ] && git add src/site.config.ts
    [ -d src/content ] && git add src/content
    git commit -q -m "chore: bump notes-core to $NEW"
    if [ "$PUSH" = "--push" ]; then
      git push -q && echo "  pushed"
    fi
  ); then
    DONE+=("$d")
  else
    echo "  ✘ 失敗——已跳過，繼續下一站"
    FAILED+=("$d")
  fi
done

echo
echo "完成 ${#DONE[@]} 站；失敗 ${#FAILED[@]} 站；略過 ${#SKIPPED[@]} 站。"
if [ ${#SKIPPED[@]} -gt 0 ]; then
  printf '  - %s（SKIP，仍停在 '"$OLD"'）\n' "${SKIPPED[@]}"
fi
if [ ${#FAILED[@]} -gt 0 ]; then
  printf '  ✘ %s\n' "${FAILED[@]}"
  echo "（失敗站的 package.json 可能已被 sed 改過但未 commit——修好後重跑或手動處理）"
fi
[ "$PUSH" != "--push" ] && echo "（未 push；確認各站 diff 後再加 --push 或各自 git push）"
[ ${#FAILED[@]} -eq 0 ]
