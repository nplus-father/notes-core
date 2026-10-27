#!/usr/bin/env zsh
set -e
CORE=${0:A:h:h}
G=${CORE:h}
S=$1
MSG=${2:?usage: prose-finalize.sh <station> "<commit message>"}
cd $G/$S
python3 - <<'PY'
import glob,re
for f in glob.glob('src/content/**/*.md',recursive=True):
    s=open(f,encoding='utf-8').read()
    t=re.sub(r'^(#{2,6} .*)$',lambda m:m.group(1).replace('——','：'),s,flags=re.M)
    t=re.sub(r'^(#{2,6} [^：\n]{1,4})：([^\n]*：)',r'\1 \2',t,flags=re.M)
    if t!=s: open(f,'w',encoding='utf-8').write(t)
PY
find src/content -name '*.md' | python3 ~/.claude/skills/fix-book-bold/scripts/fix-md-bold-flanking.py --write >/dev/null
po=$(git grep -o -E '(站外|書外)(脈絡|補充|資料)' HEAD -- src | wc -l)
pn=$(grep -r -o -E '(站外|書外)(脈絡|補充|資料)' src | wc -l)
if [ $pn -lt $po ]; then echo "STOP $S: provenance markers $po -> $pn"; exit 1; fi
out=$(python3 $CORE/tools/prose-metrics.py --gate . || true)
if echo "$out" | grep "^FAIL" | grep -v -E "link added|frontmatter changed" | grep -q .; then echo "$out" | grep '^FAIL'; echo "STOP $S: gate failed"; exit 1; fi
npm run format >/dev/null
npm run format:check >/dev/null
npm run build >/dev/null 2>&1 || { echo "STOP $S: build failed"; exit 1; }
python3 - <<'PY' || { echo "STOP $S: literal ** in built HTML"; exit 1; }
import glob,re,sys
bad=[]
for f in glob.glob('dist/**/*.html',recursive=True):
    s=open(f,encoding='utf-8').read()
    for t in ('pre','code','script'): s=re.sub(rf'<{t}.*?</{t}>','',s,flags=re.S)
    if '**' in s: bad.append(f)
print('\n'.join(bad[:5])); sys.exit(1 if bad else 0)
PY
git add -A src
git commit -q -m "$MSG"
git push -q
echo "$S $(git log -1 --format=%h) $(echo "$out" | grep 'files,')"
