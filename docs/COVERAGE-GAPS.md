# Note 星系 coverage gap（還沒開站的人物與主題）

掃描日：2026-08-03（2026-08-04 重掃更新）。**星系的維護有三個軸，別混用**：

- 本檔：**還沒有站**的人物／主題 —— 缺口靠「開新站」補。
- [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md)：**站已存在但還沒寫完** —— 缺口靠 `note-enrich` 長內容補。
- [SOURCING-DEBT.md](./SOURCING-DEBT.md)：**內容寫了但查不到出處** —— 缺口靠掛 `anchor` 補（2026-08-04 新增的軸；當時全星系 33% 的頁沒有 anchor）。

## 指標與重算方式

指標＝一本藏書有沒有被**任何**站的 `src/data/bibliography.ts` 引用到。這比「站數 vs 書數」精確，因為它抓得到跨站分工（一本書被別站認領也算覆蓋）。

```bash
# 在 portal repo 下跑（需要 src/data/repos.json 是最新的：npm run fetch-repos）
python3 - <<'EOF'
import json, re, glob
from collections import Counter
items = json.load(open('src/data/repos.json'))['items']
books = [i for i in items if 'nplus-kind-book' in i.get('topics', [])]
leaf = lambda i: next((t[5:] for t in i.get('topics', []) if t.startswith('leaf-')), '')
cited = set()
for f in glob.glob('/home/andrew/workspace/andrew/notes/*/src/data/bibliography.ts'):
    cited |= set(re.findall(r'slug:\s*"([^"]+)"', open(f, encoding='utf-8').read()))
uncov = [b for b in books if b['name'] not in cited]
print(len(books), '本藏書，未被引用', len(uncov), '本')
for l, n in Counter(leaf(b) for b in uncov).most_common(20):
    tot = sum(1 for b in books if leaf(b) == l)
    print(f'  {n:4}/{tot:<4} {l}')
EOF
```

**讀法**：看**比例**不是看絕對數。未覆蓋比例高＝沒站在管（開新站）；絕對數高但比例低＝有站在管、只是還沒寫完（進 ENRICH-BACKLOG）。

## 2026-08-03 掃描結果

1391 本藏書，978 本已被 61 站引用，**413 本沒有任何站碰過**。

### 主題缺口（藏書 ≥8 本且未覆蓋 ≥60%）

只有兩個。其餘 leaf 只要藏書 ≥8 本，覆蓋率都在 70% 以上。

| leaf | 未覆蓋/總數 | 處置 |
| --- | --- | --- |
| `agile` | 7/8 | ✅ 已開 `agile-note`（2026-08-04） |
| `visual` | 11/12 | ✅ 已開 `design-note`（2026-08-04）——扣掉歸類錯誤的 `only-sales-guide`、`wtf-what-is-the-future`，與已歸 de-botton 站的 `architecture-of-happiness`，實收 9 本 |

> `sub` 層級幾乎全覆蓋（書庫 20 個 sub，筆記站已覆蓋 19 個），所以缺口只可能出現在更細的 `leaf` 層——別用 sub 層掃，會掃不出東西。

### 人物缺口

分兩類，價值不同：

**A 類——書多且大多沒讀過（開站＝真的補進新內容）**

| 作者 | 藏書 | 未引用 | 領域 | 處置 |
| --- | --- | --- | --- | --- |
| Stephen R. Covey | 6 | 4 | communication | ✅ 已開 `covey-note`（2026-08-04） |
| Richard Templar | 6 | 5 | communication | ✅ 已開 `templar-note`（2026-08-04）——The Rules 系列，決議獨立開站 |
| Joe Navarro | 4 | 3 | communication | ✅ 已開 `navarro-note`（2026-08-04）——決議獨立開站，不併進 `communication-note` |
| Michael Wilcock | 6 | 6 | theology | ❌ 不開站 |
| Alec Motyer | 4 | 4 | theology | ❌ 不開站 |
| Raymond Brown | 4 | 4 | theology | ❌ 不開站 |

> **神學那三位（＋已覆蓋的 John H. Walton）合計 18 本刻意不開人物站**：他們是釋經書系（BST 那類）的作者，讀者關心的是「這卷書怎麼解」而不是「這個人怎麼想」。這 18 本應併進 `biblical-studies-note` 的 enrich——它本來就排在 ENRICH-BACKLOG 第一位（19/47）。

**B 類——書已被主題站讀完，開站是「換個鏡頭重切」**

Yuval Noah Harari（4）、Malcolm Gladwell（5）、Ray Dalio（4）、Adam Grant（4）、C.G. Jung（4）、Timothy Ferriss（4）、Alex Hormozi（4）、Clayton Christensen（4）、Andrew S. Grove（4）。

這些人的未引用數都是 0–1。開站不會多讀到新書，但符合人物軸的定義（「順著一個人自己的脈絡讀完全集」）。**目前不開**——優先序低於任何會帶進新內容的工作。

### 掃描時排除的雜訊

- **機構不算人物**：Harvard Business Review（36 本，已有 `hbr-note`）、CFA Institute（6 本）。
- **共同作者字串會重複計數**：`Robert T. Kiyosaki & Sharon L. Lechter` 與 `Robert Kiyosaki` 會被算成兩個作者。重算時取 `&`／`,`／`and` 之前的第一作者。

## 2026-08-04 重掃（開完五站之後）

**1401 本藏書，1006 本已被引用，395 本沒有任何站碰過**（08-03 是 1391 / 978 / 413）。

藏書 ≥6 本且未覆蓋 ≥50% 的 leaf 只剩兩個：

| leaf | 未覆蓋/總數 | 處置 |
| --- | --- | --- |
| `biblical-studies` | 59/109（54%） | 依決議暫緩；歸 `biblical-studies-note` 的 enrich，見 ENRICH-BACKLOG |
| `security` | 6/7（85%） | **新發現的主題缺口**，之前沒被列進候選。藏書量小，先評估併進 `cloud-infra-note` 還是獨立開站 |

> 08-03 的兩個主題缺口（`agile` 7/8、`visual` 11/12）已由開站解決；A 類人物缺口也已清空。

## 已執行（2026-08-04）

### 第一批：主題缺口 + Covey

開站時為骨架階段，同日已跑過 `note-enrich`：

| 站 | 軸 | 分類 | 頁數（開站 → enrich 後） | owned |
| --- | --- | --- | --- | --- |
| `agile-note` | topic | scrum / flow / user-stories / adoption | 4 → 13 | 8 |
| `covey-note` | person | principles / personal-victory / public-victory / legacy | 6 → 12 | 8 |
| `design-note` | topic | simplicity / design-thinking / visual-basics | 3 → 8 | 9 |

### 第二批：A 類人物（Templar / Navarro）

決議兩位都獨立開站，不併進 `communication-note`。理由：Templar 的體例（一條規則一頁對頁、拒絕理論）與 Navarro 的方法論（基準線紀律、反測謊立場）各自成體系，併站會把兩套語彙壓成通用溝通建議。開站後同日已改寫為書本位：

| 站 | 軸 | 分類 | 頁數 | owned |
| --- | --- | --- | --- | --- |
| `templar-note` | person | the-code / work / people / self | 7 | 6 |
| `navarro-note` | person | observation / limbic / dictionary / danger | 6 | 4 |

> 兩站的 registry 入列與封面走 `notes-core` v0.18.0；portal 分組 topic 都取主力書的 `top-professional` / `sub-communication`。

### 開站種子概念的溯源債（已清）

`note-new-station` 對種子概念沒有書本位要求（那是 `note-enrich` 的紀律），所以開站當下寫出來的頁是憑既有理解寫的、`furtherReading` 只掛書不掛 anchor。**同日已全部回頭對照 `books-done` 原文改寫**，並掛上章節 anchor。這一輪校正抓到三處實質錯誤：

- 《The Rules of Thinking》是**十個部分**，不是六類。
- 《The Rules of Management》的核心是**「管理流程而非管理人」**（第一部卷首），而不是「管自己先於管團隊」——書的順序也是團隊先、自己後。
- Navarro 的識謊立場比原本寫的更強：**慣性說謊者反而會增加眼神接觸**，而「說謊者不敢對視」是明確的迷思。

> **教訓**：新站開完就該接一輪 `note-enrich`，別讓種子概念以未溯源的狀態留在站上——它讀起來跟書本位的頁一模一樣，但沒有 anchor 可以查。

## 下一輪的候選

1. **溯源債** —— 見 [SOURCING-DEBT.md](./SOURCING-DEBT.md)。這是目前投報率最高的一項：全星系 33% 的頁查不到出處，而清債的過程會抓出實質錯誤（2026-08-04 的 26 頁抓到 8 處）。
2. `security` leaf 缺口 —— 7 本藏書、6 本未覆蓋，先決定併站還是開站。
3. `biblical-studies-note` enrich（吃掉神學那 18 本 + leaf 層的 59 本）—— **暫緩，2026-08-04 決議先不做**；見 ENRICH-BACKLOG
4. B 類人物站 —— 想清楚「重切」的價值再動

## 這份文件掃不到的東西

三個軸都不涵蓋的維護面向，2026-08-04 實測數字：

| 面向 | 現況 | 為什麼 enrich 補不了 |
| --- | --- | --- |
| **跨站連結** | 1203 頁空 `seeAlso`，只有 114 頁有 | `note-enrich` 的紀律是「確認姊妹站路徑存在才加，否則留空」——實務上永遠留空。星系目前是 69 個各自獨立的站 |
| **複習狀態** | 1219 draft / 51 reviewed / 47 studied；`lastReviewed` 只有 14 頁設過 | enrich 只管產出不管複習 |
| **心得層** | `:::response` 只有 36 頁有內容（2.7%） | enrich 明文不填這層，那是 `note-master` 與 `*-study` 的職責 |

> 舊的規劃稿（`humanities-books-by-domain.md`、`humanities-note-scope-draft.md`、`books-by-domain.md`）是 2026-07-01～02 的建站期文件，其提案多已落地，保留作歷史紀錄；**新的缺口盤點以本檔為準**。
