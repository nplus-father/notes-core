#!/usr/bin/env bash
# ⚠️ 已退役——請勿執行。保留純為紀錄 v0.1.0 那次接線的決策與手法。
#
# 這是 2026 年把六個獨立站接上 notes-core 的一次性遷移腳本，寫於 v0.1.0 時期。
# 它預期各站有 src/lib/url.ts、src/lib/reviews.ts、src/styles/_tokens.scss、
# src/plugins/remark-details.mjs、src/components/Stars.astro——v0.4.0 版面收進 core、
# v0.11.0 astro.config 也收進 core 之後，這些檔案在現行站台一個都不存在，
# 跑下去只會把站弄壞。
#
# 現在要新站：用 `/note-new-station` skill 從 note-template 開，模板已經是接好的狀態。
#
# 為何用 git 依賴而非 GitHub Packages：org 政策禁止 public npm package，
# 而 private package 跨 repo 讀取很痛。notes-core 的 *repo* 是 public，
# 故直接 `github:nplus-father/notes-core#<tag>` 由 npm clone —— 零 token / 零 .npmrc / 零 registry。
# （這條決策仍然有效，見 README「tools/」一節。）
#
# 原用法：./rewire-notes-core.sh <note-dir> <複習ns> [<tag>]
#   例：./rewire-notes-core.sh system-design-note sd v0.1.0
set -euo pipefail
echo "✘ rewire-notes-core.sh 已退役：現行站台沒有它要改的那些檔案，跑下去會弄壞站。" >&2
echo "  新站請用 /note-new-station 從 note-template 建立。" >&2
exit 2

# ---- 以下為 v0.1.0 當時的實作，保留供考古 ----
cd "$(dirname "$0")"

D="${1:?用法: ./rewire-notes-core.sh <note-dir> <ns> [tag]}"
NS="${2:?需要複習 namespace（cc/ci/ds/dp/lk/sd 已用，新站避開）}"
TAG="${3:-v0.1.0}"

cd "$D"
# package.json：改成 git 依賴（若原本是 unist-util-visit 末項，順手替換）
if grep -q '"unist-util-visit"' package.json; then
  perl -0pi -e 's/    "unist-util-visit": "[^"]+"/    "\@nplus-father\/notes-core": "github:nplus-father\/notes-core#'"$TAG"'"/' package.json
elif ! grep -q '@nplus-father/notes-core' package.json; then
  echo "請手動在 dependencies 加：\"@nplus-father/notes-core\": \"github:nplus-father/notes-core#$TAG\"" >&2; exit 1
fi
rm -f .npmrc  # git 依賴不需要 registry 設定

# url.ts / reviews.ts → shim（呼叫端零改動；reviews 沿用 namespace）
printf 'export { withBase } from "@nplus-father/notes-core";\n' > src/lib/url.ts
cat > src/lib/reviews.ts <<EOF
import { createReviews } from "@nplus-father/notes-core";
export type { ReviewRecord, ReviewLog } from "@nplus-father/notes-core";
export const { loadLog, saveLog, lastReviewed, reviewCount, isReviewedToday, markReviewedToday, undoToday, todayStr } =
  createReviews("$NS");
EOF
# _tokens.scss → 1 行 @forward（所有 @use "tokens" 不動，含 leet 的多個 partials）
cat > src/styles/_tokens.scss <<'SCSS'
// 轉發共用設計 token（實體在 @nplus-father/notes-core）
@forward "@nplus-father/notes-core/styles/tokens.scss";
SCSS
# astro.config：remark-details → 套件
perl -0pi -e 's{import remarkDetails from "\./src/plugins/remark-details\.mjs";}{import remarkDetails from "\@nplus-father/notes-core/remark-details";}' astro.config.mjs
# Stars 匯入 → 套件
grep -rlE 'from "[^"]*Stars\.astro"' src 2>/dev/null | while read -r f; do
  perl -pi -e 's{from "[^"]*Stars\.astro"}{from "\@nplus-father/notes-core/Stars.astro"}g' "$f"
done
rm -f src/plugins/remark-details.mjs src/components/Stars.astro
rmdir src/plugins 2>/dev/null || true

# 乾淨重建 lock（一定要清 node_modules，否則 npm ci 會抱怨 optional-deps 不同步）
rm -rf node_modules package-lock.json
npm install
rm -rf node_modules && npm ci   # 本地模擬 CI 驗證
npm run build:nosearch
echo "✓ $D 接上 notes-core（ns=$NS, $TAG）。git diff 後 commit/push。"
