#!/usr/bin/env bash
# 一次重算所有生成型星系盤點文件（docs/ 下的八份），並印出這一輪的落差。
#
# 用法：
#   tools/refresh-galaxy-docs.sh            # 重算八份，印摘要與 diffstat
#   tools/refresh-galaxy-docs.sh --check    # 同上，但有落差就 exit 1（給 cron／CI 用）
#
# **為什麼要有這支**：四個生成器各跑各的，於是「只重算其中一份就下判斷」變成常態。
# 2026-08-10 實測：committed 的 WANTED-BOOKS.md 說「先扣掉 0 本」，當場重跑是 **23 本**
# ——採購清單前 20 名裡有 2 本其實早就建好書站了。生成物一旦停更就會開始騙人，而它
# 看起來跟剛跑完一模一樣。**重算要是一個動作，不是四個。**
#
# 做的事（順序無關，八份彼此獨立）：
#   1. export-wanted.py        → WANTED-BOOKS.md  （書還沒收）        ※ 需要 gh
#   2. export-orphan-books.py  → ORPHAN-BOOKS.md  （書有了沒站在管）  ※ 需要 gh
#   3. export-deepen-ready.py  → DEEPEN-READY.md  （哪站可以進場深化）
#   4. export-missing-years.py → MISSING-YEARS.md  （缺初版年）
#   5. export-year-conflicts.py→ YEAR-CONFLICTS.md（跨站欄位不一致）
#   6. export-deepen-targets.py→ DEEPEN-TARGETS.md（大部頭卻只有一鏟的書）
#   7. export-anchor-gaps.py   → ANCHOR-GAPS.md   （頁面用了書裡的事實，卻掛到不含它的章）
#   8. export-guide-drift.py   → GUIDE-DRIFT.md   （導覽的數字宣稱跟不上站台現況）
#
# 前兩份的權威資料源是 GitHub 現況（`gh repo list`），問不到會退回站台的 repos.json
# 快照——快照落後好幾天很正常，拿它下判斷出過事（2026-08-07，20 本裡漏報 16 本）。
# 所以這裡**先擋 gh auth**：沒登入就直接停，不要讓人拿快照的結論當事實。
#
# 重算完不會自動 commit。回填 wanted → owned 要逐本核對作者（同名不同書會買錯），
# 那是 `/note-wanted` 的事，不是這支的事。
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
DOCS="$(cd "$HERE/.." && pwd)/docs"
CHECK=0
[[ "${1:-}" == "--check" ]] && CHECK=1

if ! gh auth status >/dev/null 2>&1; then
  echo "✘ gh 未登入——WANTED-BOOKS 與 ORPHAN-BOOKS 會退回站台快照，結論不可信。" >&2
  echo "  先跑 gh auth login，或明確接受快照時單獨跑那兩支。" >&2
  exit 2
fi

echo "── 重算八份生成文件 ──────────────────────────────"
"$HERE/export-wanted.py"
"$HERE/export-orphan-books.py"
"$HERE/export-deepen-ready.py"
"$HERE/export-missing-years.py"
"$HERE/export-year-conflicts.py"
"$HERE/export-deepen-targets.py"
"$HERE/export-anchor-gaps.py"
"$HERE/export-guide-drift.py"

echo
echo "── 與 committed 版的落差 ─────────────────────────"
# 只看 docs/ 底下這八份；其他 docs 是手維護的，不該被這支影響。
TRACKED=(WANTED-BOOKS.md ORPHAN-BOOKS.md DEEPEN-READY.md MISSING-YEARS.md YEAR-CONFLICTS.md DEEPEN-TARGETS.md ANCHOR-GAPS.md GUIDE-DRIFT.md)
# -I 忽略戳記行：每份生成物的 H1 底下有一行「生成於 <ISO>」，那一行**每次重算必變**，
# 不忽略的話這個落差檢查會永遠報「有變動」，等於沒有檢查。改戳記格式時要一起改這裡
# （格式的正本在 tools/_stamp.py 的 STAMP_RE）。
DIFF="$(git -C "$DOCS" diff --stat -I'^> \*\*生成於' -- "${TRACKED[@]}" 2>/dev/null || true)"
UNTRACKED="$(git -C "$DOCS" ls-files --others --exclude-standard -- "${TRACKED[@]}" 2>/dev/null || true)"

if [[ -z "$DIFF" && -z "$UNTRACKED" ]]; then
  echo "無落差——八份都還是最新的。"
  exit 0
fi
[[ -n "$DIFF" ]] && echo "$DIFF"
[[ -n "$UNTRACKED" ]] && echo "新檔（尚未 commit）：$UNTRACKED"

cat <<'EOF'

── 接下來 ────────────────────────────────────────
  WANTED-BOOKS  「先扣掉 N 本」> 0 → 跑 `/note-wanted` 回填並重挑前 20（要逐本核對作者）
  ORPHAN-BOOKS  1a 那節 > 0 → 補一筆 bibliography 就好；1b 有 leaf → 考慮開新站
  DEEPEN-READY  「可深化」那批 → 挑一站進 `/note-check --enrich`
  MISSING-YEARS 逐筆補初版年（不是手上這版、也不是中譯版的年份）
  YEAR-CONFLICTS 第一節每組挑一個年份（先分清是「初版 vs 改版」還是「系列列 vs 單卷列」）；
                第二節可直接抄別站的答案；第三節（slug 撞號）出現任何一筆都要立刻查
  DEEPEN-TARGETS 「依站分組」挑一站 → 進 `/note-check --enrich` 開單（開單本身留 Fable）
  ANCHOR-GAPS   「證據充分」那節逐頁修 furtherReading：建議章是母章就擴大，否則另加一條
                （建議只是提示，掛上去前要確認那一章真的在講頁面說的事）
  GUIDE-DRIFT   「強訊號」那節逐筆對現況改導覽數字（保語氣、只改數字），改完推 writtenAt；
                弱訊號多半是「有幾頁引用這本書」的子集宣稱，不是債
EOF

[[ $CHECK -eq 1 ]] && exit 1
exit 0
