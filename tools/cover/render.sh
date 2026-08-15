#!/usr/bin/env bash
#
# render.sh — 產生主題站封面 (Style B・印刷風・3:4 直式・900x1200)
#
# 站名與英文副題取自 src/lib/sites.ts，配色與符號取自 src/lib/site-covers.ts，
# 由 cover-gen.mjs 組成 HTML，這裡負責把 HTML 變成 PNG 並（可選）安裝到各 note repo。
#
# 為什麼繞 headless Chrome：中文大字得靠瀏覽器排版，截成點陣圖才能把字型烘進去；
# 若改成 SVG 交給讀者端渲染，沒裝 Noto Sans CJK 的機器上版面就會跑掉。
# 為什麼截 2x 再縮：1x 直接截，文字與細線邊緣會有鋸齒。
#
# 這支工具刻意不在 package.json 的 files 白名單裡——62 站建置時會 import notes-core，
# 不該把 Chrome 與 ImageMagick 拖進那條依賴鏈。它只跟著 repo 走。
#
# 需求：node (>=22，直接吃 .ts)、google-chrome、ImageMagick(convert)、Noto Sans CJK TC 字型
#
# 用法：
#   ./render.sh <slug> [outfile.png]              # 產生單一封面（預設輸出到 ./<slug>.png）
#   ./render.sh --install <notes-root> [slug...]  # 安裝到 <root>/<slug>/public/cover.png
#                                                 # 不給 slug 就是全部主題站重畫
#
# 範例：
#   ./render.sh philosophy-note
#   ./render.sh --install ~/workspace/andrew/notes theology-note hbr-note
#
# 只想補幾站時務必列出 slug：不列＝所有主題站重繪，每個 note repo 都會多出一筆
# cover.png 改動，得逐一 review 才知道哪些是真的改了。
#
# 人物站不歸這裡管——封面是傳主的肖像照，給錯 slug 時 cover-gen.mjs 會擋下來。
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT

# 主題站清單直接問 registry，不要在這裡再抄一份
topic_slugs() {
  node --input-type=module -e "
    import { sites } from '$DIR/../../src/lib/sites.ts';
    console.log(sites.filter(s => s.axis === 'topic').map(s => s.slug).join('\n'));
  "
}

render() {  # <slug> <outPng>
  local slug="$1" out="$2"
  node "$DIR/cover-gen.mjs" "$slug" "$TMP/$slug.html"
  google-chrome --headless=new --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=2 --window-size=900,1200 \
    --screenshot="$TMP/$slug@2x.png" "file://$TMP/$slug.html" >/dev/null 2>&1
  convert "$TMP/$slug@2x.png" -resize 900x1200 -strip -quality 95 "$out"
  echo "rendered $slug -> $out"
}

if [[ "${1:-}" == "--install" ]]; then
  root="${2:?usage: ./render.sh --install <notes-root> [slug...]}"
  shift 2
  targets=("$@")
  [[ ${#targets[@]} -gt 0 ]] || mapfile -t targets < <(topic_slugs)
  for k in "${targets[@]}"; do
    dest="$root/$k/public/cover.png"
    [[ -d "$root/$k/public" ]] || { echo "skip $k (no $root/$k/public)"; continue; }
    render "$k" "$dest"
  done
else
  slug="${1:?usage: ./render.sh <slug> [outfile.png]}"
  out="${2:-$DIR/$slug.png}"
  render "$slug" "$out"
fi
