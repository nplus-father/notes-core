# Note 星系 溯源債（第三個軸）

> **現況（2026-08-05 重驗）：債已清空。** 全星系 1441 個概念頁，**0 頁**沒有 anchor；
> bibliography 指向不存在書 repo 的 slug **0 個**。本檔自此轉為**方法紀錄**——
> 掃描腳本、兩種欠債成因的判準、預防機制都還有效，債本身沒有了。下次大批新增內容後
> 重跑下面兩段掃描即可。

掃描日：2026-08-04（清償），2026-08-05（重驗）。**這是與另外三份文件不同的軸，別混用**：

- [COVERAGE-GAPS.md](./COVERAGE-GAPS.md)：**還沒有站**的人物／主題 —— 缺口靠「開新站」補。
- [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md)：**站已存在但還沒寫完** —— 缺口靠 `note-check --enrich` 長內容補。
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

## 2026-08-06 追加校正（第 3 波 note-check 抓到）

「有 anchor ≠ 主張對」——problem-solving-note 的 4 頁種子頁 anchor 齊全，但 enrich 回原文逐段核對時抓到 **6 處實質錯誤**，全數已改（commit `ce9cfef`）：

| 頁 | 原本寫的 | 原文實際說的 |
| --- | --- | --- |
| issue-driven-start | 假說思考＝「先射箭再畫靶」 | 全書無此語；原文是「著手分析前先建立假說、鎖定方向」 |
| issue-driven-start | 「利潤下滑」的真論點可能是「定價權流失」 | 書中無定價權例；前言實例是「解決了錯誤的問題」系列 |
| issue-driven-start | 「兩週就被推翻的假說勝過模糊方向」 | 書中數字是「一個月後被全盤推翻仍比窮盡思考有效率」 |
| zero-second-a4-memo | 選項比較格式出自《零秒思考力實踐篇》 | 實為《麥肯錫零秒執行力》工具①（◎〇△×＋4–5 評價標準），已改掛正確書 |
| zero-second-a4-memo | 39 習慣例「會議前先想好產出」 | 查無此習慣；換成書中實有的「隨時回歸零發想」「天空雨傘三十秒」 |
| think-on-paper | 金線＝「不可增刪的順序」 | 原文定義是「假設驅動、事實為基、符合邏輯的真知灼見」「金字塔構成的項鍊」 |

kiyosaki-note 同輪自檢另抓 2 處措辭與原文不符（標準石油起薪、700 棟房現金流表述），未入站前即校正（commit `f4aa093`）。

同日稍晚的中落差六站批次再添三類發現（皆已處置）：

- **系統性錯掛（economics，commit `733ecb9`）**：12 頁 anchor 亂掛——8 頁不論主題一律指向 50-economics-ideas 前兩章、4 頁掛錯書，疑為 2026-08-04 `anchor.py` 批次的機械配對遺留。「有 anchor ≠ 掛對章」，逐頁回原文重掛；其中《推力》器捐段抓到**主張反向**的內容錯誤（書實際反對推定同意、主張提示選擇），已改寫。
- **死 anchor（relationships，commit `44f7c0c`）**：friendship-over-time 指向不存在的章節目錄，已修。同時發現書 repo `life-is-a-long-term-accumulation` 各章正文是**空 stub**（僅 frontmatter＋書根概覽）——書庫內容債，待補書。
- **書架誤植（history 當輪回報，已搬 2026-08-06）**：`war-of-words` 實為 Paul Tripp 的言語神學／溝通門訓書，卻放在 books-done 的 military 類。已搬 `faith/theology/pastoral/`、GitHub topics 改 `top-faith/sub-theology/leaf-pastoral`、盤點自 history-note 軍事組移入 theology-note 教會與牧養組。

### 新型債：書 repo 身分錯配（2026-08-06 首例，newport enrich 抓到）

book repo `how-to-be-a-high-school-superstar` 的**內容實為《How to Win at College》**（繁中《深度學習力》2019）——2026-04-04 建 repo 時「譯名→英文原名」推斷步驟把 Newport 兩本學生書搞混，錯名寫進 slug 與 GitHub 描述，矛盾甚至寫在書頁自己的作者背景段（「How to Be a High School Superstar，原書名為 How to Win at College」）。下游 newport-note bibliography 繼承錯名並把真 Superstar 的「鬆弛悖論」註記錯掛。

- 教訓：**anchor 驗證只驗目錄存在，驗不到 repo 身分**——「有 anchor ≠ 掛對書」。
- 處置（依 Andrew 決議，以不動 repo 名為原則）：newport-note bibliography 條目改回 Win at College（slug 沿用、note 註明錯配史，commit `e8f4ae3`）、真 Superstar 另立 wanted；防再犯規則已寫進 `book-import-to-queue` skill A2（版權頁查原名＋三方核對，claude-code-commands `a5eb4d4`）。

## 2026-08-09 追加校正（taleb-note enrich 抓到）

教訓仍是 08-06 那句「有 anchor ≠ 主張對」——本輪三處皆為**頁級溯源齊全、段級／數字級破口**（站內容與本表一併待 Andrew review 後 commit）：

| 頁 | 原本寫的 | 原文實際說的 |
| --- | --- | --- |
| antifragile-and-barbell | 槓鈴比例「90/10 的虧損有底、獲益無頂」 | book-3 ch11（Never Marry the Rock Star）的表格是**絕對安全 85–90% ＋ 高風險投機 10–15%**；且該頁原只錨 book-1/book-2，主打的槓鈴本章反而沒錨——數字與 anchor 一併補正 |
| skin-in-the-game | 兩句加引號的「語錄」：「用工作摧毀閒暇的人不懂閒暇為何物」「被雇用就是被馴化」 | 書 repo 查無此二句——主題有支撐（ch7 視閒暇為高尚、ch5 薪資奴役），但**轉述被包裝成直引**。改為轉述＋書中實句「讓奴隸相信自己是自由的，是現代社會控制最高明的手段」，並補 ch5/ch7 anchor |
| black-swan-and-extremistan | 🖼️ 段整段講《隨機騙局》（牙醫、俄羅斯債券交易員），furtherReading 卻無該書 | 內容回查可驗（非杜撰）；補 fooled-by-randomness 卷一 Solon's Warning anchor——**段落引書也要錨**，頁級 ≥1 本不夠 |

## 2026-08-20 追加校正（investing-note enrich 抓到）

教訓同 08-06「有 anchor ≠ 掛對章」——`this-time-is-different` 頁錨齊全、卻是**錯掛＋漏掛**（站 commit `6907574`）：

| 問題 | 原狀 | 處置 |
| --- | --- | --- |
| Montier 兩 anchor 錯掛 | 掛 `01-in-the-heat-of-the-moment`／`02-afraid-of-big-bad-market`（同理鴻溝、損失恐懼章，與本頁主張無關） | 改掛 `11-this-time-is-different`（Templeton 四字、五階段、五大障礙全在此章，逐項核實） |
| 席勒主張整批無錨 | 詞頻 1997/7、占卜板、Fisher 高原、36 國 94%/65% 等主張無 anchor 覆蓋 | 逐項對 `irrational-exuberance` ch05/06 核實後補掛（內容無錯，免改寫） |
| Bernstein 引句無錨 | 「泡沫高點最大的謊言」 | 補掛 four-pillars `01-tops-history-of-manias` |

同輪兩筆 bibliography 帳（非溯源債、記脈絡）：economics `capitalist-manifesto` note/year 誤植 Norberg 2023（實為 Kiyosaki 2022，`9ad4f77` 修）；investing `trend-following` note 誤記只收訪談集（實收 2017 五版本傳，`6907574` 修）。

## 2026-08-20 追加校正（data-systems-note enrich 抓到）

同輪第二批（站 commit `fa363e3`）——一筆主張改寫＋三筆 label 錯章（「有 anchor ≠ 掛對章」再驗證）：

| 頁 | 原本寫的 | 原文實際說的 |
| --- | --- | --- |
| stream-processing | 「沒有完美解：『資料到齊』本質上不可知，只能啟發式逼近」 | Streaming Systems ch3：**完美浮水印在特定來源可建**（入口時間戳、靜態分區＋分區內單調的 Kafka topic），多數真實來源才退回啟發式——已改寫並補專段 |
| clustered-vs-secondary | HPJP label「索引與執行計畫」（書中無此章） | 實出處 Mapping Types and Identifiers（UUID vs 序列鍵、叢集索引碎裂） |
| isolation-levels／mvcc | HPJP label「並發控制與隔離級別」「MVCC 與快照」 | 隔離級別表與各家 MVCC 實作（SCN／xmin-xmax／rollback segment）在 Part 1 Transactions 章 |
| rebalancing | DBI label「Part II：叢集與分片」（無此章） | 分片與一致性雜湊在 Distributed Transactions 章末 |

## 2026-08-21 追加校正（wan-weigang-note enrich 抓到——迄今最大一張 B 型債）

拐點兩頁＋human-uniqueness 的核心框架**書稿全文零命中**（主代理獨立複核屬實），共 16 筆校正（站 commit `83ea32e`）。三筆是**方向相反**級：

| 頁 | 原本寫的 | 原文實際說的 |
| --- | --- | --- |
| 拐點頁 | 「脆弱的智能」／分布內外、元認知、索馬提克標記、「三種角色」框架 | 全書查無；實際框架＝底牌（預測下一詞長出類人思維）／命門（「用來思考不是用來計算」，可用工具彌補）、門檻領導力四途徑＋自由技藝六項 |
| 拐點頁 | 「原始突破仍屬人類」 | **方向相反**：書主張 AI「不但有創造力，而且可以有更好的創造力」（GPT-4 勝 MBA、AlphaGo 創造新棋知識） |
| 拐點頁 | 「AI 放大勞動市場贏家通吃」 | **方向偏移**：勝者通吃指 AI 公司；就業反而「自動化最高的行業就業增加最多」 |
| 拐點頁 | 「人腦 CPU vs AI GPU 不分高下」 | **方向相反**：「啟發模式重要性在下降，窮舉模式在上升」 |
| t-shaped-talent | 「T 型人才」整頁（連 slug） | 全書零命中——整頁廢棄，改立 `more-yourself-in-ai-era`（ch03 置身智能＋人比AI兇微決策） |
| human-uniqueness | 四項清單錨 ch04＋「三大根本缺陷」 | 四項清單真實但在**序言**；「局域上下文」是變形；末那識論證在 ch01 sec-2（缺身體邊界感＋連貫敘事兩前提） |
| relativity-for-masters | 惠勒（Wheeler）歸屬＋「四大驗證」 | 引句逐字在書但**無惠勒歸屬**；書為**三大**驗證，「引力時間延遲」查無 |
| elite-vs-common-sense | 狐狸刺蝟錨 `02-worldview-demystified` | 實際在 `01-preface` 與 `04-eighteen-arts/10-reliable-knowledge` |

另 bibliography《人比AI兇》year 2024→2025（序言署名 2025-07）。教訓：**種子頁的「聽起來像那本書會講的框架」最危險**——T 型人才、元認知這類流行語彙極易被腦補進轉譯者的書；防線仍是導覽書帳（逐本回原文）＋enrich 逐段核對。

### 同輪 tracy-note：一筆假警報（記檢核脈絡）

導覽點名 strategic-thinking 兩條 label「與 anchor 錯章」，enrich 回書查證判**非錯配**：`business-strategy`
書 repo 的**目錄 slug 與 `_index.md` 章題系統性不一致**（`05-where-are-you-now/` 章題實為 "Values, Vision,
and Purpose"、`07-how-do-you-get-there/` 實為 "Back from the Future"，主代理複核屬實）。label 取章題是對的。
教訓：**判 label 錯章前先開 `_index.md` 對章題，別只看目錄名**。書 repo 的 slug／章題不一致本身是書庫小債，暫不動。

### 同輪 cloud-infra-note：label 書名錯掛＋事實升級（站 commit `5101ebf`）

| 原本寫的 | 原文實際 | 處置 |
| --- | --- | --- |
| 四頁 label 書名「Observability Engineering — …」，`book:` 實指 `observability-beginners-guide`（《可觀測性入門指南》，另一本書） | 兩本不同書——頁首 byline 與頁尾卡印錯書名 | 四頁 label 改「Observability 入門指南 — …」（observability-vs-monitoring、three-pillars、four-golden-signals、distributed-tracing）。「有 anchor ≠ 掛對書」的 label 變體 |
| 「1960 年代匈牙利數學家 Rudolf Kálmán」（轉引自入門指南） | 原典 OE ch1：「工程師 Rudolf E. Kálmán 在 **1960 年**提出」＋與可控制性互為對偶 | 骨幹改掛原典；兩書衝突以原典優先 |

## 2026-08-21 第三波校正（nouwen／fowler 一條龍抓到）

| 站 | 原本寫的 | 原文實際 | 處置 |
| --- | --- | --- | --- |
| nouwen `downward-mobility` | 子代理稿「召命就隱藏在目前的光景、目前的居處」 | road-to-daybreak 全書查無 | 刪除，改以 selfless epilogue 有據的「處方比診斷薄」收尾 |
| nouwen guide 01／03 | 兩句引文被改寫（班伯格地圖句、living-reminder「把心丟了」） | 原句各多一個限定語 | 貼回原句（主代理逐字複核） |
| fowler bibliography | Refactoring year 1999 | repo 實為 2018 二版（published 2018-11-20、Extract Function 術語） | 改 2018，導覽如實交代 |
| fowler bibliography | 4 本 owned 掛「缺口」group | 收書後未更新 | 重新分組 |

子代理稿的 `&amp;gt;` 跳脫實體污染在 nt-wright／fowler／nouwen 三站都出現，母代理落盤時全清；主代理驗收加了 entities 掃描。

## 自動化工具

第二批（456 頁）用腳本完成，**label 與章節名直接取自 `books-done` 原文的 frontmatter，不自行編造**：

- 找出頁的 `book` slug → 在 `books-done` 定位書 repo → 讀 `site/content/docs/` 的頂層章節（跳過 appendix/preface/foreword/introduction/conclusion/epilogue 等非內容章節）→ 取前兩章 → label 用「書名 — 章節標題」（兩者都讀自原文的 `title:`）。
- **anchor 保證存在**（目錄是實際掃出來的），**label 保證誠實**（就是那一章的標題）。
- 精度是**章**而非節。要更精確的錨點，之後在該站跑 `note-check` 時再細化。

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

`note-new-station` 的種子概念與 `note-check` 的產出都已加上規範（2026-08-04）：

- **`note-new-station`**：種子概念二選一 —— 路徑 A（當場讀原文、掛驗證過的 anchor）或路徑 B（**一律不掛 anchor** 當作標記，並登記進 ENRICH-BACKLOG，且開站不算完成）。
- **`note-check`**：§0.5 新增溯源健檢（上面那段掃描），未溯源頁自動列為 §2 落差分析的**第一類、必改不是選改**；§5 自檢要求收尾重跑掃描且輸出為空。

## 損壞譯名類（2026-08-09 立案並大掃除）

**病灶**：books-done 書 repo 的音譯專名（人名/片名/書名/樂團名）內有字被錯置成罕用字或簡體字，
形成「看起來像譯名、其實查無此人」的損壞——與缺 anchor 同屬「查不到出處」軸，故記於本檔。
已確認的損壞字類：**乃**（乃許＝納許、乃潔兒＝瑞秋）、**乙**（乙希＝柔伊、乙溫絲蕾＝溫絲蕾）、
**乔/乏/乌/泽/乍/乘/乾**（乔佛乔德·希區乔克＝希區考克、乏乙德＝博伊德）、
以及**簡體字卡在譯名內**（馬丁·路德·乔治＝金恩——注意不能盲轉「喬治」）。

**本輪成果**：8 個工作包（主代理＋7 子代理）掃全庫 239 本嫌疑書，
確認並修復 **~95 本書、550+ 處**（含簡體字卡名內的第四類 ~140 處）；凱勒書架（forgive/counterfeit-gods/prodigal-god 含講義）全清。
keller-note 站內引用已同步修正。修正明細見各書 repo 的未 commit diff。

**掃描方式**（下次大批產書後重跑）：

```bash
# 在 books-done 下：損壞字 + 人名情境（分隔號/書名號/鄰近拉丁字母）
grep -rn '[乃乙乔乏乌泽]' . --include='*.md' \
  | grep -v '乃是\|乃至\|西乃\|乃縵\|康乃\|木乃伊\|美乃滋\|甲\|乙方' \
  | grep -P '[·．・《（(]'
```

**未結**：
1. **簡體殘留（另一類，未修）**：簡體原著書（馮唐×4、萬維鋼×3、劉潤、溝通的方法、secret-of-loving…）
   的正文/引文大量簡體字（刘邦、持之以恒、整句簡體），核心字集掃描 55 本 ~350 命中、寬字集千行級。
   建議獨立專案：逐書 `opencc s2twp` ＋人工過譯名（譯名不可盲轉，見上）。
2. 不可考 3 筆：laws-of-human-nature 的「乃乃乃·乃奧乃爾」（git 初版即損壞，無英文可考）；
   wan-weigang-scientific-thinker「麥乃志」（華裔可能本名含乃）；why-wont-you-apologize「乃拉」（疑 Nora）。
3. thank-you-for-arguing 一處片名疑似生成期誤植（《一生中最美好的歲月》情節實為《風雲人物》），僅去損字未改題。

**成因推測與預防**：損壞集中在 AI 批次產書期的輸出（非 OCR）；書 repo 產線（hugo-book-manager / 相關 skill）
的收尾檢查應加上面的掃描一鍵。

## 校正紀錄：借聲債（anchor 掛錯書）— 2026-08-15，writing-note

**新型態的債**：頁面有 anchor、掃描器抓不到，但部分主張實出自另一本書——「借聲」。發現途徑是 `/note-guide` 第三章逐本對帳（Coverage 引用數 vs 行文取材），掃描腳本抓不到這種債，**導覽的書帳是目前唯一的偵測器**。

| 頁 | 原寫 | 書中實際 | 修法 |
| --- | --- | --- | --- |
| story-structure/desire-and-conflict | 「設定期望→違反期望，意外是機制本身」 | Storr：注意力雙鑰＝偵測改變＋資訊缺口；打破預期只是誘發好奇四式之一 | 照書改寫＋補 science-of-storytelling anchor |
| story-structure/character-arc | 「缺陷內建進信念與控制理論、故不可見」 | Storr：缺陷內建進**受控幻覺（知覺）**才不可見；控制理論是另一概念（信念的加總） | 拆開照書寫＋補 anchor |
| nonfiction-copy/find-the-core | 「找核心＝核心＋緊湊」；掃不是讀／電梯測試／Why it matters 掛 made-to-stick | 「簡單＝核心＋緊湊」；該三組素材實出自 Smart Brevity（一件大事／為什麼重要） | 改掛 smart-brevity 正確 anchor；made-to-stick 僅留真屬它的 |

同輪已還：science-of-storytelling 開機制頁（storytelling-brain）。其餘借聲債（writing 站剩 Ueland／Storynomics／Ogilvy 三筆）記在該站導覽 ch3，待下輪。

### 追加：philosophy-note 借聲債五筆（2026-08-15，同輪還清）

| 頁 | 主張 | 原掛 | 實補 |
| --- | --- | --- | --- |
| what-is-philosophy | Nagel「不能外包給科學」 | Durant | what-does-it-all-mean docs/01-introduction/ |
| three-paths-of-justice | Fromm「德性＝實現自身潛能」 | Sandel | man-for-himself docs/02-humanistic-ethics/ |
| dichotomy-of-control | 愛比克泰德開篇引言 | 奧理略 | Epictetus handbook |
| premeditatio-malorum | 塞內卡預想語 | Daily Stoic 選本 | 書簡 26 |
| philosophy-as-consolation | 塞內加藥方 | 僅 de Botton | 書簡 91 |

另 hbr-note 一筆**查無原文**的引用：Kotter「70% 變革失敗」不在 Kotter 原文（Essentials 的 Leading Change），是 Guide to Leading Through Change 的轉述——已在該站導覽記帳，防未來誤掛。
