# Note 星系 溯源債（第三個軸）

掃描日：2026-08-04。**這是與另外兩份文件不同的第三個軸，別混用**：

- [COVERAGE-GAPS.md](./COVERAGE-GAPS.md)：**還沒有站**的人物／主題 —— 缺口靠「開新站」補。
- [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md)：**站已存在但還沒寫完** —— 缺口靠 `note-enrich` 長內容補。
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

**全星系 1350 頁，其中 457 頁（33%）沒有任何 anchor。**

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

## 待清（457 頁）

| 批次 | 站 | 頁數 |
| --- | --- | --- |
| **大站（要分批）** | writing 38、economics 37、investing 30、learning 27、design-patterns 25、philosophy 24、history 23 | 204 |
| **中站** | tracy 18、growth 18、keller 17、biblical-studies 14、tools 12 | 79 |
| **零星（多為 5–9 頁）** | spiritual-formation 9、cloud 9、thinking 6、startup 6、relationships 6、life-meaning 6、leadership 6、habits 6、communication 6、career 6、business-strategy 6、wellness 5、personal-finance 5、其餘各站 | 174 |

> 零星那一批多半是「站已 enrich 過，但早期的頁沒補 anchor」——優先做完整站別的批次比零散處理有效率。

## 預防

`note-new-station` 的種子概念與 `note-enrich` 的產出都已加上規範（2026-08-04）：

- **`note-new-station`**：種子概念二選一 —— 路徑 A（當場讀原文、掛驗證過的 anchor）或路徑 B（**一律不掛 anchor** 當作標記，並登記進 ENRICH-BACKLOG，且開站不算完成）。
- **`note-enrich`**：§0.5 新增溯源健檢（上面那段掃描），未溯源頁自動列為 §2 落差分析的**第一類、必改不是選改**；§5 自檢要求收尾重跑掃描且輸出為空。
