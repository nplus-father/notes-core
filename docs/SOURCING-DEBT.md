# Note 星系 溯源債（第三個軸）

> **現況（2026-08-05 重驗）：債已清空。** 全星系 1441 個概念頁，**0 頁**沒有 anchor；
> bibliography 指向不存在書 repo 的 slug **0 個**。本檔自此轉為**方法紀錄**——
> 掃描腳本、兩種欠債成因的判準、預防機制都還有效，債本身沒有了。下次大批新增內容後
> 重跑下面兩段掃描即可。

掃描日：2026-08-04（清償），2026-08-05（重驗）。**這是與另外三份文件不同的軸，別混用**：

- [COVERAGE-GAPS.md](./COVERAGE-GAPS.md)：**還沒有站**的人物／主題 —— 缺口靠「開新站」補。
- [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md)：**站已存在但還沒寫完** —— 缺口靠 `note-enrich` 長內容補。
- [WANTED-BOOKS.md](./WANTED-BOOKS.md)：**書本身還沒收** —— 缺口靠去收書補。
- **本檔**：**內容已經寫了，但查不到出處** —— 缺口靠掛 `anchor` 補（必要時回原文校正）。

## 指標與重算方式

指標＝一個內容頁的 `furtherReading` 有沒有任何 `anchor`。沒有 anchor 的頁**無法回查原文**，讀起來卻和書本位的頁一模一樣——這是它危險的地方。

```bash
# 在任一站根目錄下跑
for f in src/content/concepts/*/*.md; do
  case "$(basename "$f")" in _index.md) continue;; esac
  grep -q '^\s*anchor:' "$f" || echo "未溯源: $f"
done
```

```bash
# 全星系版本（在 notes/ 下跑）
for d in *-note/; do s=${d%/}; [ -d "$d/src/content/concepts" ] || continue
  un=0; for f in $(find "$d/src/content/concepts" -name "*.md" ! -name "_index.md"); do
    grep -q '^\s*anchor:' "$f" || un=$((un+1)); done
  [ "$un" -gt 0 ] && echo "$un $s"
done | sort -rn
```

## 2026-08-04 掃描結果

**開工時：全星系 1350 頁，其中 457 頁（33%）沒有任何 anchor。**

**收工時：1376 頁，僅剩 1 頁未溯源（0%）。**

### 兩種欠債成因（處置方式不同）

| 成因 | 症狀 | 處置 | 成本 |
| --- | --- | --- | --- |
| **A：內容是書本位的，只是沒填 anchor** | 逐段核對原文都對得上，具名事實（人名、數字、章節結構）也查得到 | 掛 anchor 即可 | 低 |
| **B：內容是憑既有理解寫的** | 對照原文會發現結構數字錯、主張方向反了 | **回原文逐段核對後改寫**，不是補 anchor 了事 | 高 |

**判斷方法**：抽驗兩頁的具名事實（幾個部分、幾條法則、誰說的、哪一年）。對得上就是 A，對不上就是 B。

> 2026-08-04 的實測：`templar-note`／`navarro-note`（開站種子概念）與 `agile`／`covey`／`design` 的開站種子屬於 **B**，13+13 頁改寫後共抓到 8 處實質錯誤；六個作者站（nt-wright/fromm/lewis/schwager/stott/maxwell）屬於 **A**，58 頁抽驗後直接掛 anchor。

## 已清（2026-08-04）

| 站 | 頁數 | 成因 | 備註 |
| --- | --- | --- | --- |
| templar-note | 7 | B | 抓到 3 處錯：Rules of Thinking 是 10 部不是 6 類、Rules of Management 的核心是「管理流程而非管理人」、work 分類頁改名 |
| navarro-note | 6 | B | 補入十大準則、三腦一體、識謊迷思 |
| agile-note | 4 | B | **WIP 起始值寫反了**（原寫「取一半」，Reinertsen 的方法是先加倍再遞減） |
| covey-note | 6 | B | 芝加哥／底特律的地圖比喻方向錯、「近 50 年」應為「一戰後」 |
| design-note | 3 | B | 一頁一骨幹被違反（Maeda 與 Ward 混用），改成純 simplicity-cycle |
| stott-note | 12 | A | |
| maxwell-note | 12 | A | |
| fromm-note | 10 | A | |
| lewis-note | 10 | A | |
| nt-wright-note | 7 | A | |
| schwager-note | 7 | A | |
| **其餘 51 站** | **456** | A | 用 `anchor.py` 批次掛上（見下節），逐站 build 驗證通過 |

## 待清：無

2026-08-04 收工時 1376 頁中剩最後 1 頁，已於當日結清：

| 頁 | 問題 | 實際處置 |
| --- | --- | --- |
| `learning-note` / `self-directed-map` | `furtherReading.book` 指向 `self-made-talent`，但這本書**不存在**（本機沒有、`nplus.wiki/self-made-talent/` 回 404） | 頁與 bibliography 條目一併移除（`learning-note` e49948a）——沒有書就不留一頁假裝有出處 |

2026-08-05 重驗：1441 頁（比收工時多 65 頁）全部有 anchor。

## 自動化工具

第二批（456 頁）用腳本完成，**label 與章節名直接取自 `books-done` 原文的 frontmatter，不自行編造**：

- 找出頁的 `book` slug → 在 `books-done` 定位書 repo → 讀 `site/content/docs/` 的頂層章節（跳過 appendix/preface/foreword/introduction/conclusion/epilogue 等非內容章節）→ 取前兩章 → label 用「書名 — 章節標題」（兩者都讀自原文的 `title:`）。
- **anchor 保證存在**（目錄是實際掃出來的），**label 保證誠實**（就是那一章的標題）。
- 精度是**章**而非節。要更精確的錨點，之後在該站跑 `note-enrich` 時再細化。

腳本留在 scratchpad（`anchor.py`），要重跑或擴充時可以直接改。

## 順帶發現：指向不存在書 repo 的 bibliography slug —— 已清（2026-08-05 重驗 0 個）

掃描時比對 portal 的 `repos.json`，這類 slug 在書庫裡沒有對應的 repo——它們會讓首頁書架的封面 404。
2026-08-04 抓到 8 個，2026-08-05 重驗全部結清，分兩種收法：

| 站 | slug | 收法 |
| --- | --- | --- |
| thinking-note | `science-of-living` | **補建書 repo**，bibliography 照舊指向它 |
| history-note | `war-of-words` | 同上 |
| investing-note | `richer-wiser-happier` | 同上 |
| career-note | `how-world-class-professionals-practice-fundamentals`、`where-will-you-be-in-the-next-decade` | **撤掉這筆 `slug`**（書不存在就不掛死鏈） |
| thinking-note | `think-twice` | 同上 |
| learning-note | `self-made-talent` | 同上（連頁一起移除） |
| wan-weigang-note | `wan-weigang-your-plan-worlds-plan` | 同上，並改登記成 `wanted`——書是真的想收，只是還沒有 |

> 反方向的落差（bibliography 說 `wanted`、書 repo 其實**已經存在**）另有 14 筆，
> 見 [WANTED-BOOKS.md](./WANTED-BOOKS.md) 的「先扣掉」一節——那是 status 沒跟上，不是死鏈。

```bash
# 重跑（在 portal repo 下）
python3 - <<'EOF'
import json, re, glob
real = {i['name'] for i in json.load(open('src/data/repos.json'))['items']}
for f in glob.glob('/home/andrew/workspace/andrew/notes/*/src/data/bibliography.ts'):
    bad = [s for s in re.findall(r'slug:\s*"([^"]+)"', open(f, encoding='utf-8').read()) if s not in real]
    if bad: print(f.split('/')[-4], sorted(set(bad)))
EOF
```

## 預防

`note-new-station` 的種子概念與 `note-enrich` 的產出都已加上規範（2026-08-04）：

- **`note-new-station`**：種子概念二選一 —— 路徑 A（當場讀原文、掛驗證過的 anchor）或路徑 B（**一律不掛 anchor** 當作標記，並登記進 ENRICH-BACKLOG，且開站不算完成）。
- **`note-enrich`**：§0.5 新增溯源健檢（上面那段掃描），未溯源頁自動列為 §2 落差分析的**第一類、必改不是選改**；§5 自檢要求收尾重跑掃描且輸出為空。
