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
      for pkg in $(node -e 'const d=require(process.argv[1]).dependencies||{};for(const k of Object.keys(d))if(k.startsWith("@fontsource"))console.log(k)' "$CORE/package.json"); do
        if [ ! -d "$P/node_modules/$pkg" ]; then
          [ -d "$CORE/node_modules/$pkg" ] || { echo "missing $CORE/node_modules/$pkg (run npm install in core)" >&2; exit 1; }
          mkdir -p "$(dirname "$P/node_modules/$pkg")"
          cp -r "$CORE/node_modules/$pkg" "$P/node_modules/$pkg"
        fi
      done
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
