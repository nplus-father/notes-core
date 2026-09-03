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
