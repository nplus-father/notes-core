# Note 星系 溯源債（第三個軸）

> **現況（2026-08-05 重驗）：債已清空。** 全星系 1441 個概念頁，**0 頁**沒有 anchor；
> bibliography 指向不存在書 repo 的 slug **0 個**。本檔自此轉為**方法紀錄**——
> 掃描腳本、兩種欠債成因的判準、預防機制都還有效，債本身沒有了。下次大批新增內容後
> 重跑下面兩段掃描即可。

掃描日：2026-08-04（清償），2026-08-05（重驗）。**這是與另外三份文件不同的軸，別混用**：

- [ORPHAN-BOOKS.md](./ORPHAN-BOOKS.md)：**書有了但沒有站在管**（含開新站候選）—— 缺口靠認領或開站補。
- [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md)：**站已存在但還沒寫完** —— 缺口靠 `note-check --enrich` 長內容補。
- [WANTED-BOOKS.md](./WANTED-BOOKS.md)：**書本身還沒收** —— 缺口靠去收書補。
- **本檔**：**內容已經寫了，但查不到出處** —— 缺口靠掛 `anchor` 補（必要時回原文校正）。

## 指標與重算方式

**分工**：「有沒有 anchor」＝本檔這兩段掃描；「anchor 掛得對不對」＝[ANCHOR-GAPS.md](./ANCHOR-GAPS.md)（`export-anchor-gaps.py`，2026-08-27 起第七類債）；「anchor 指到的書 repo／章存不存在」＝`galaxy-checkup.py` 的雙向溯源。

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


## 兩種欠債成因（處置方式不同）

| 成因 | 症狀 | 處置 | 成本 |
| --- | --- | --- | --- |
| **A：內容是書本位的，只是沒填 anchor** | 逐段核對原文都對得上，具名事實（人名、數字、章節結構）也查得到 | 掛 anchor 即可 | 低 |
| **B：內容是憑既有理解寫的** | 對照原文會發現結構數字錯、主張方向反了 | **回原文逐段核對後改寫**，不是補 anchor 了事 | 高 |

**判斷方法**：抽驗兩頁的具名事實（幾個部分、幾條法則、誰說的、哪一年）。對得上就是 A，對不上就是 B。

> 2026-08-04 的實測：`templar-note`／`navarro-note`（開站種子概念）與 `agile`／`covey`／`design` 的開站種子屬於 **B**，13+13 頁改寫後共抓到 8 處實質錯誤；六個作者站（nt-wright/fromm/lewis/schwager/stott/maxwell）屬於 **A**，58 頁抽驗後直接掛 anchor。


## 待清：無

2026-11-12 第三批：Fable 開單時就撞見兩筆（fork 讀第一鏟頁時回源查不到），Opus 起草鄰頁時回原文改寫清償；起草代理另抓到四頁轉述。都是 **B 型**。

**wellness `nutrition-sleep/nutrition-foundations`（校正表）**——掛江部《間歇性斷食減醣全書》，寫的卻是 Matthews 的熱量論

| 原本寫的 | 原文實際說的 |
| --- | --- |
| 能量平衡決定體重；斷食減醣有效多半是減少了總攝取 | 江部：「重點不是熱量，而是有沒有醣」。能量平衡那句出自 Matthews《Bigger Leaner Stronger》04/01，移到新頁 flexible-dieting |
| 蛋白質是最該顧好的營養素 | 江部書沒有；「蛋白質先排」出自 BLS 04/02 |
| 以真食物為主、進食時機是工具不是魔法 | 江部沒講；他說「重點不是吃幾餐，而是每餐有沒有醣」 |
| 糖與酒精推高尿酸，連到痛風、脂肪肝 | 江部書沒有尿酸、痛風、脂肪肝；他講血糖飆升、胰島素、β 細胞疲乏 |
| 依從性是隱藏變數 | 全書沒有；江部講「沒有壓力，所以容易持續」 |

頁改寫成江部的減醣理由，標題改「減醣的理由：不算熱量、脂肪燃燒與一日兩餐」；導覽官司一第三層改由 Matthews 立論、結語改掛 Ferriss 黏貼測試；導覽另三處誤連改連 daily-dozen／nutritionism；overview 一句同步。**同一個錯掛把一場三造官司（熱量、醣、植物）壓成了一句共識。**

**hbr `strategy-innovation/everyday-strategic-thinking`（校正表）**

| 原本寫的 | 原文實際說的 |
| --- | --- |
| 事前驗屍、指定唱反調者、可逆／不可逆決策 | 書裡沒有；改用 04 三章：Davey 反思三問、Larson 七步 checklist、Menon 與 Thompson 的 Data DIET；唱反調改引 01/01 Schoemaker |
| 「向上一層」「向後拉」時段、問題框架三問 | 改用 Roger Martin 給每層主管的四問（02/02）、Bowman 每週 30 分鐘的案例（01/03）、listening tour（02/01） |
| 策略要能在兩分鐘內講清楚 | 書裡沒有；改 Martin「策略是你做什麼，不是你說什麼」 |
| TIP「本週我們說了哪些 No」、IMPORTANT「忙碌只是在被管理」 | 書裡沒有；改 Bowman 週會議程與 Davey「策略性最終在選擇這個點上被檢驗」 |
| 整節「四個斷點」與「策略絞肉機」 | 書裡沒有；改連新頁 strategy-execution-gap（書的第七部）與 priorities-without-ranking |
| 數據與 AI 一節 | 本頁無錨，刪主張改連 manager-data-literacy、ai-for-managers |

導覽第四章共識三的收束「看可逆性」改成「看下一份資料會不會改變決定」（Menon 與 Thompson），overview 同步。

**起草代理抓到的轉述（已改）**

| 檔案 | 原寫 | 原文實際 |
| --- | --- | --- |
| leadership `coaching/leader-leader` | Goldsmith：8 分補成 9 分、投入從 100% 掉到 50%；「好主意，就照你的做」 | 品質可能提升 5%、承諾掉 50%；後一句書裡沒有 |
| leadership `culture/circle-of-safety` | Horowitz「開會遲到罰跪」、看「升遷誰、開除誰、容忍誰」、「文化會複利」 | 例子是 Coughlin 準時到場罰款；前言原話「你是誰，是你做了什麼」；複利一條三本書都沒有，刪 |
| communication `persuasion/rhetoric-toolbox` | 一整句當引文 | 引文只有前半句，後半是轉述 |
| economics `gold-standard-and-fetters` | （開單時疑為杜撰）「符合每一條已知的規則」 | 不是杜撰：出自《黃金的魔力》第 18 章 Eugene Meyer；補掛那章 |

2026-11-06 第二批起草時，起草代理回源抓到兩頁有 anchor、核心主張卻不在掛的書裡（§1.2 掃不到這一類），同日回原文改寫清償。都是 **B 型**。

**hbr `leadership-teams/coaching-and-feedback`（校正表）**

| 原本寫的 | 原文實際說的 |
| --- | --- |
| SBI（情境—行為—影響）是標準結構 | 兩本指南全書沒有；換成 Bradford「待在球網的自己這一邊」，只講行為與自身感受 |
| 行為發生 48 小時內給回饋 | 書裡沒有時限；Dowling 說開完會走回辦公室的兩分鐘最好 |
| 每週／每季／即時三層迴圈 | 書裡沒有；實際是持續性回饋加年度或半年度正式回饋 |
| 教練時刻與指令時刻 | 書裡的判準是部屬經驗不足、需要立即改善時偏向教學 |
| 信任三支柱、回饋是禮物或攻擊 | 掛的兩本沒有；換成 Dougherty 與 Manzoni 的接受條件 |
| 三明治法的細節、HBR 調查、OKR 的 CFR | 書裡沒有；Valcour 與 Knight 的說法保留，其餘刪 |

SBI 同時滲進導覽五章、mastery、overview 與 feedback-fallacy 頁，導覽爭點一改以球網原則立論。**一個沒出處的框架進了概念頁，就會被導覽放大成整場爭點**，這正是 note-guide 擋薄站的理由。

**design-patterns `paradigms/oop-vs-functional`（校正表）**

| 原本寫的 | 原文實際說的 |
| --- | --- |
| 多數 GoF 模式在補 OO 缺一級函數的洞 | Bob：部分正確，整體不正確；模式通用，形式可能受語言限制 |
| Strategy＝傳函數、Decorator＝`g(f)`、Factory＝thunk、Observer＝stream | 書裡沒有這組對應；Bob 用 `defmulti` 與 `journaled-shape` |
| 有狀態偏 OOP、型別開放偏介面 | 書裡沒有，且 Bob 反對：沒有任何複雜度高到必須放棄不可變性 |
| 混用要劃清範式邊界 | 書裡沒有；Bob 主張兩者完全相容 |

標題改為「OOP vs FP：兩種範式的對照」，導覽三句、mastery 一條、gof-in-functional 兩句同步。

**這類債的抓法**：grep 掃不到，只有起草鄰頁時整章回源才會撞見。對照頁的起草代理是這輪最有效的稽核員。

2026-08-04 一輪清償（1350 頁、457 頁未溯源 → 0），2026-08-05 重驗 1441 頁全部有 anchor。
之後各輪 enrich 抓到的 **B 型債校正表**（08-06 第 3 波、08-09 taleb、08-20 investing／data-systems、
08-21 wan-weigang／tracy／cloud-infra／nouwen／fowler、第四、五波一條龍的 bogle／templar／willard）
已於 2026-09-03 從本檔移除，看 `git log -p -- docs/SOURCING-DEBT.md`。三條留下來的判斷：
**早期薄站的既有頁比書 repo 產線直改的頁髒得多，人物薄站的既有頁務必逐條 grep 回書**；
**判「label 錯章」先開書 repo 的 `_index.md` 對章題**（tracy 那筆是 slug 與章題系統性不一致的假警報）；
**種子頁的流行語彙框架最容易腦補進轉譯者的書**（wan-weigang 的 T 型人才、元認知）。

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
