#!/usr/bin/env bash
set -euo pipefail
CORE="$(cd "$(dirname "$0")/../.." && pwd)"
NOTES_ROOT="${NOTES_ROOT:-/home/andrew/workspace/andrew/notes}"
PREVIEW_DIR="${PREVIEW_DIR:-$HOME/.cache/notes-design-preview/$(basename "$CORE")}"
PORT="${PORT:-8820}"
cmd="${1:?usage: preview.sh build <station>... | serve | stop | url}"
shift || true
case "$cmd" in
  build)
    mkdir -p "$PREVIEW_DIR/srv"
    for st in "$@"; do
      P="$PREVIEW_DIR/$st"
      mkdir -p "$P"
      rsync -a --delete --exclude node_modules --exclude dist --exclude .git --exclude .astro "$NOTES_ROOT/$st/" "$P/"
      [ -d "$P/node_modules" ] || cp -al "$NOTES_ROOT/$st/node_modules" "$P/node_modules"
      T="$P/node_modules/@nplus-father/notes-core"
      rm -rf "$T" && mkdir -p "$T"
      rsync -a "$CORE/bin" "$CORE/src" "$CORE/package.json" "$CORE/eslint.config.js" "$CORE/prettier.config.json" "$CORE/prettierignore" "$CORE/tsconfig.base.json" "$CORE/versions.json" "$T/"
      rm -rf "$P/node_modules/.astro"
      echo "── build $st"
      (cd "$P" && systemd-run --user --scope -q -p MemoryMax=4G -p MemorySwapMax=0 npx astro build 2>&1 | tail -n "${TAIL:-6}")
      if [ "${PAGEFIND:-0}" = "1" ]; then (cd "$P" && npx pagefind --site dist 2>&1 | tail -n 2); fi
      ln -sfn "$P/dist" "$PREVIEW_DIR/srv/$st"
    done
    ;;
  serve)
    mkdir -p "$PREVIEW_DIR/srv"
    if [ -f "$PREVIEW_DIR/srv.pid" ] && kill -0 "$(cat "$PREVIEW_DIR/srv.pid")" 2>/dev/null; then
      echo "already serving http://localhost:$PORT/"
    else
      nohup python3 -m http.server "$PORT" --directory "$PREVIEW_DIR/srv" >/dev/null 2>&1 &
      echo $! > "$PREVIEW_DIR/srv.pid"
      echo "serving http://localhost:$PORT/"
    fi
    ;;
  stop)
    [ -f "$PREVIEW_DIR/srv.pid" ] && kill "$(cat "$PREVIEW_DIR/srv.pid")" 2>/dev/null || true
    rm -f "$PREVIEW_DIR/srv.pid"
    ;;
  url) echo "http://localhost:$PORT/" ;;
  *) echo "unknown command $cmd" >&2; exit 2 ;;
esac
