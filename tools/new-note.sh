#!/usr/bin/env bash
# 一鍵開新 note 站並自動入列星系。
#
# 用法：
#   tools/new-note.sh <slug> "<Brand 英文顯示名>" "<顯示名>" <topic|person> ["<tagline>"]
# 例：
#   tools/new-note.sh habits-note "Habits Notes" "習慣" topic "習慣養成筆記。"
#   tools/new-note.sh drucker-note "Drucker Notes" "Peter Drucker" person "杜拉克的管理思想。"
#
# 第三個參數是 registry 的 label——主題站用中文短名；人物站用**該人物通行的寫法**
# （西方作者英文全名 Peter Drucker，華文作者中文名 馮唐），不硬譯。v0.14.0 起
# subject: { nameZh, nameEn } 已收回，所以不再有第 6 個「原文名」參數。
#
# 做的事：
#   1. 從 GitHub template repo `nplus-father/note-template` 建新 repo 並 clone 到 notes/ 下
#   2. 跑 init.sh 套用 __SLUG__/__BRAND__/__TAGLINE__/__NS__ 佔位符（含站縮圖 cover.svg、footer）
#   3. 打上星系 topic `nplus-note`（→ 之後 `gh repo list nplus-father --topic nplus-note` 一次撈到）
#   4. 自動把新站 append 進 notes-core/src/lib/sites.ts（跨站連結與知識軸的 SSOT）
set -euo pipefail

OWNER=nplus-father
USAGE='用法: tools/new-note.sh <slug> "<Brand>" "<顯示名>" <topic|person> ["<tagline>"]'
SLUG="${1:?$USAGE}"
BRAND="${2:?需要 Brand 英文顯示名}"
LABEL="${3:?需要顯示名（主題站＝中文短名；人物站＝該人物通行的寫法）}"
AXIS="${4:?需要知識軸：topic（主題站）或 person（人物站）}"
TAGLINE="${5:-}"
# 星系根目錄＝放所有 -note 站的容器目錄。本腳本住在 notes-core/tools/，往上兩層就是。
# 佈局不同時用 NOTES_ROOT 覆寫（對應 tools/cover/render.sh 的 --install <notes-root>）。
ROOT="${NOTES_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"
NS="$(echo "$SLUG" | awk -F- '{printf "%s%s", substr($1,1,1), substr($2,1,1)}')"

case "$AXIS" in
  topic | person) ;;
  *) echo "✘ axis 只能是 topic 或 person（收到 \"$AXIS\"）" >&2; exit 2 ;;
esac

cd "$ROOT"

# 1) 建 repo（template repo 機制）並 clone
gh repo create "$OWNER/$SLUG" --template "$OWNER/note-template" --private --clone

# 2) 套用 tokens（init.sh 會自刪）
cd "$ROOT/$SLUG"
./init.sh "$SLUG" "$BRAND" "$TAGLINE" "$NS"

# 3) portal 可見性：homepage + topic
#
# portal 的 scripts/fetch-repos.ts 用「topic 含 nplus-portal **且** homepage 非空」兩個條件撈，
# 兩者缺一新站就不會出現在 nplus.wiki/notes/——而且不會報錯，只是靜靜地不見。
# （2026-08-04 開的三站就是這樣：只打了 nplus-note，那個 topic 沒有任何程式在讀。）
#
# top-*/sub-* 決定 portal 的領域分組，必須跟書庫同一套詞彙：拿該站主力書的
# leaf topic 去對照書 repo 的 top-/sub- 即可（例：leaf-agile → sub-engineering/top-craft）。
# 這兩個沒辦法從參數推導，所以留給人補——先設好前兩項，卡片至少出得來。
gh repo edit "$OWNER/$SLUG" \
  --homepage "https://nplus.wiki/$SLUG/" \
  --description "${TAGLINE:-$BRAND}" \
  --add-topic nplus-kind-notes \
  --add-topic nplus-portal
echo "⚠ 記得補 top-*/sub-* topic，否則 portal 會把本站歸到「未分類」："
echo "    gh repo edit $OWNER/$SLUG --add-topic top-<領域> --add-topic sub-<主題>"

# 4) 入列 notes-core sites.ts（若本地有 clone）
# 新站一律 seeAlsoMode "open"；要收進嚴格 enum（技術站群）請手動搬到 __NEW_SITE__ 那一區。
SITES="$ROOT/notes-core/src/lib/sites.ts"
KEY="${SLUG%-note}"
# v0.14.0 起 Site 型別只剩單一 label（人物站用該人物通行的寫法：西方作者英文全名、
# 華文作者中文名）。v0.13.x 那組 subject: { nameZh, nameEn } 已收回——這裡再寫出來
# 會變成型別不存在的欄位，registry 直接編不過。
if [ "$AXIS" = "person" ]; then
  MARKER="__NEW_PERSON_SITE__"
else
  MARKER="__NEW_TOPIC_SITE__"
fi
LINE="  { key: \"$KEY\", slug: \"$SLUG\", brand: \"$BRAND\", label: \"$LABEL\", axis: \"$AXIS\", seeAlsoMode: \"open\" },"
if [ -f "$SITES" ] && ! grep -q "slug: \"$SLUG\"" "$SITES"; then
  LINE="$LINE" MARKER="$MARKER" perl -0pi -e 's{(\n\s*// \Q$ENV{MARKER}\E)}{\n$ENV{LINE}$1}' "$SITES"
  echo "✔ 已加進 notes-core/src/lib/sites.ts（記得發 notes-core 新版讓各站吃到）"
else
  echo "⚠ 未自動入列 sites.ts（找不到本地 notes-core，或已存在）。請手動加：$LINE"
fi

cat <<MSG

✔ $SLUG 建好了：套版 + topic=nplus-note + sites.ts 入列。
下一步：
  cd $ROOT/$SLUG && nvm use && npm install && npm run dev
MSG
