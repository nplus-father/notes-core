#!/usr/bin/env bash
# 一鍵開新 note 站並自動入列星系。
#
# 用法：
#   tools/new-note.sh <slug> "<Brand 英文顯示名>" "<中文短名>" <topic|person> ["<tagline>"] ["<原文名>"]
# 例：
#   tools/new-note.sh habits-note "Habits Notes" "習慣" topic "習慣養成筆記。"
#   tools/new-note.sh drucker-note "Drucker Notes" "杜拉克" person "杜拉克的管理思想。" "Peter Drucker"
#
# 做的事：
#   1. 從 GitHub template repo `nplus-father/note-template` 建新 repo 並 clone 到 notes/ 下
#   2. 跑 init.sh 套用 __SLUG__/__BRAND__/__TAGLINE__/__NS__ 佔位符（含站縮圖 cover.svg、footer）
#   3. 打上星系 topic `nplus-note`（→ 之後 `gh repo list nplus-father --topic nplus-note` 一次撈到）
#   4. 自動把新站 append 進 notes-core/src/lib/sites.ts（跨站連結與知識軸的 SSOT）
set -euo pipefail

OWNER=nplus-father
USAGE='用法: tools/new-note.sh <slug> "<Brand>" "<中文短名>" <topic|person> ["<tagline>"] ["<原文名>"]'
SLUG="${1:?$USAGE}"
BRAND="${2:?需要 Brand 英文顯示名}"
LABEL="${3:?需要中文短名（人物站 = 傳主中文名）}"
AXIS="${4:?需要知識軸：topic（主題站）或 person（人物站）}"
TAGLINE="${5:-}"
NAME_EN="${6:-}"
# 星系根目錄＝放所有 -note 站的容器目錄。本腳本住在 notes-core/tools/，往上兩層就是。
# 佈局不同時用 NOTES_ROOT 覆寫（對應 tools/cover/render.sh 的 --install <notes-root>）。
ROOT="${NOTES_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"
NS="$(echo "$SLUG" | awk -F- '{printf "%s%s", substr($1,1,1), substr($2,1,1)}')"

case "$AXIS" in
  topic) ;;
  person) : "${NAME_EN:?人物站需要第 6 個參數（傳主原文名）}" ;;
  *) echo "✘ axis 只能是 topic 或 person（收到 \"$AXIS\"）" >&2; exit 2 ;;
esac

cd "$ROOT"

# 1) 建 repo（template repo 機制）並 clone
gh repo create "$OWNER/$SLUG" --template "$OWNER/note-template" --private --clone

# 2) 套用 tokens（init.sh 會自刪）
cd "$ROOT/$SLUG"
./init.sh "$SLUG" "$BRAND" "$TAGLINE" "$NS"

# 3) 星系 topic（遠端撈取用）
gh repo edit "$OWNER/$SLUG" --add-topic nplus-note

# 4) 入列 notes-core sites.ts（若本地有 clone）
# 新站一律 seeAlsoMode "open"；要收進嚴格 enum（技術站群）請手動搬到 __NEW_SITE__ 那一區。
SITES="$ROOT/notes-core/src/lib/sites.ts"
KEY="${SLUG%-note}"
if [ "$AXIS" = "person" ]; then
  MARKER="__NEW_PERSON_SITE__"
  SUBJECT=", subject: { nameZh: \"$LABEL\", nameEn: \"$NAME_EN\" }"
else
  MARKER="__NEW_TOPIC_SITE__"
  SUBJECT=""
fi
LINE="  { key: \"$KEY\", slug: \"$SLUG\", brand: \"$BRAND\", label: \"$LABEL\", axis: \"$AXIS\", seeAlsoMode: \"open\"$SUBJECT },"
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
