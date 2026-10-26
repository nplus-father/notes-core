# 導覽數字與現況不符

> **生成於 2026-10-27T00:39:42+08:00**｜由 `tools/export-guide-drift.py` 產生，**不要手改**——改資料源再重跑。

由 `tools/export-guide-drift.py` 產生。判準：導覽（`guide/*.md`）與首頁總覽（`overview.ts`）裡**指向站台自身規模的數字**——總頁數、某分類幾頁、收了幾本——回去數實際檔案對不對得上。

**為什麼另立一支**：`tier-audit.py` 的「導覽落後」欄只比日期（`enrichedAt` vs `writtenAt`），抓的是「內容補過、策展層還沒回頭看」；但站台長大時**日期可以完全不動而內容照樣說謊**。2026-08-27 收《飛輪效應》那輪就是這樣被手動抓到的。

**判法（2026-09-03 起）**：每個數字逐一試過所有合法讀法——整站總數、句內／段內列舉的連結數、句內／段內點名的書被引頁數（含聯集）、段內連結所在分類的頁數（含加總）——**沒有任何讀法成立的才報**。這取代了先前靠句型分「強／弱訊號」的做法（句型分不完，2026-09-03 那輪從弱訊號裡人工撈出 22 筆真債）。

- **要改：0 筆**——沒有任何讀法能解釋這個數字。
- 低信心通過：0 筆——只靠「等於某本未點名的書的被引頁數」放行，抽查用。
- 通過：28 筆——具體讀法成立，理由列在表裡。

計數口徑同時接受「只算概念頁」與「概念頁＋題型頁」兩種。

## 要改：0 筆

無——導覽的規模數字都對得上現況。

## 低信心通過：0 筆

無。

## 通過：28 筆

<details><summary>展開</summary>

| 站 | 檔 | 宣稱的是 | 導覽說 | 實際 | 判定理由 | 上下文 |
| --- | --- | --- | ---: | ---: | --- | --- |
| `agile-note` | 03-canon-guide.md | scrum 分類 | **12** | 12 | 分類頁數 | …Scrum（Kenneth S. Rubin，2012）**。十八處引用，被引最多的書：scrum 分類十二頁裡十頁的骨架、product 分類八頁裡五頁的主要來… |
| `agile-note` | 03-canon-guide.md | product 分類 | **8** | 8 | 分類頁數 | …ubin，2012）**。十八處引用，被引最多的書：scrum 分類十二頁裡十頁的骨架、product 分類八頁裡五頁的主要來源，retrospectives 也有… |
| `agile-note` | 03-canon-guide.md | flow 分類 | **11** | 11 | 分類頁數 | …Hammarberg & Joakim Sundén，2014）**。十處引用，撐起 flow 分類十一頁裡的九頁。 從[便利貼的撕法](../concept… |
| `agile-note` | 03-canon-guide.md | user-stories 分類 | **8** | 8 | 分類頁數 | …ser Stories Applied（Mike Cohn，2004）**。十三處引用，user-stories 分類八頁全部由它撐起，外加 scrum 的量測速度頁。 這是… |
| `agile-note` | 03-canon-guide.md | adoption 分類 | **10** | 10 | 分類頁數 | …cceeding with Agile（Mike Cohn，2009）**。十六處引用，adoption 分類十頁裡八頁由它撐起，另支援 scrum 與 xp-pra… |
| `behaviour-interview-note` | 03-canon-guide.md | frameworks 分類 | **7** | 7 | 分類頁數 | …二根脊梁：The STAR Interview（Misha Yurchenko）。** frameworks 分類七頁有六頁由它撐起：[腦力傾倒](../concepts… |
| `cloud-infra-note` | 03-canon-guide.md | infrastructure 分類 | **4** | 6 | 歷史敘述 | …四本）：四本全數開口，借來的支架換成了自己的柱子  這一群翻得最徹底：四本原本都零引用，infrastructure 分類四頁全靠 Continuous Delivery、Wor… |
| `design-patterns-note` | 03-canon-guide.md | di-ioc 分類 | **6** | 6 | 分類頁數 | …n & Mark Seemann，2019）。** 九條引用，**單書深挖密度第一**：di-ioc 分類六頁全部由它撐起，[DI 本體](../concepts… |
| `greene-note` | 03-canon-tour.md | power 分類 | **5** | 5 | 分類頁數 | …基維利《君主論》收束：關鍵不在永遠使壞，而在「保有選擇的能力」。  **對應概念頁**：power 分類五頁中的三頁。 [48 條權力法則](../concep… |
| `greene-note` | 03-canon-tour.md | mastery 分類 | **4** | 4 | 分類頁數 | …性 18 法則》的預演；學徒期的隱忍是「自我導向的戰爭」換了戰場。 **對應概念頁**：mastery 分類四頁全部出自此書：[喚醒你心中的大師](../conce… |
| `greene-note` | 03-canon-tour.md | human-nature 分類 | **5** | 5 | 分類頁數 | …己）；兩者互為表裡，「人性的理解愈深，權力的運用才愈不至於失控」。 **對應概念頁**：human-nature 分類五頁中的四頁：[人性法則](../concepts/hu… |
| `peck-note` | 03-canon-tour.md | growth 分類 | **7** | 7 | 分類頁數 | …面展開，社群線是「愛」的群體尺度，安樂死辯論是「恩典」與靈魂觀的臨終應用。 開採也最深，growth 分類七頁中有五頁出自它：總樞紐[心靈地圖](../conce… |
| `peck-note` | 03-canon-tour.md | evil 分類 | **5** | 5 | 分類頁數 | …梁。** 它把邪惡從神學帶進臨床精神醫學：邪惡不在罪行大小，而在對自身罪性的絕對否認。 evil 分類五頁中三頁半出自它：總樞紐[邪惡人性](../conce… |
| `peck-note` | 03-canon-tour.md | community 分類 | **5** | 5 | 分類頁數 | …真社群四階段（偽社群、混亂、空、社群）與「真社群可以被刻意營造」的核心命題都在這裡。 community 分類五頁中四頁溯源到它：總樞紐[不同的鼓聲](../conc… |
| `peck-note` | 05-how-to-read.md | community 分類 | **5** | 5 | 分類頁數 | …*從組織與社群工作進來的讀者**：《不同的鼓聲》→《等待重生的世界》連讀是成立的短路徑，community 分類五頁全程隨行。 欠下的《心靈地圖》語彙（放棄、小小的死亡… |
| `peterson-note` | 03-canon-tour.md | meaning 分類 | **6** | 6 | 分類頁數 | …義是「對手」原型放大到國家尺度（終章〈The Hostile Brothers〉）。  meaning 分類六頁都出自此書：[意義的地圖：神話如何組織經驗](../… |
| `taleb-note` | 03-canon-tour.md | randomness 分類 | **5** | 5 | 分類頁數 | …：灰天鵝、四象限地圖、截斷曝險與冗餘，**判斷從預測移到脆弱性**。  **對應頁**：randomness 分類五頁裡的四頁：[黑天鵝與極端世界](../concept… |
| `taleb-note` | 03-canon-tour.md | antifragility 分類 | **3** | 3 | 分類頁數 | …ame〉已指出凸性可以靠把凹性轉嫁給別人來偽造，這是下一本書的主題。  **對應頁**：antifragility 分類三頁全部出自此書：[反脆弱三元組與槓鈴策略](../co… |
| `taleb-note` | 03-canon-tour.md | asymmetry-practice 分類 | **4** | 4 | 分類頁數 | …的統計直覺推到最深：集合機率不等於時間機率，理性就是避免系統性毀滅。  **對應頁**：asymmetry-practice 分類四頁全部出自此書：[切膚之痛](../concepts/… |
| `taleb-note` | 03-canon-tour.md | fat-tails 分類 | **3** | 3 | 分類頁數 | …,000 檔證券沒有一檔細尾）。 它也是塔雷伯對批評者的技術答辯狀。  **對應頁**：fat-tails 分類三頁：出自《動態避險》的[選擇權風險的實務課](../c… |
| `taleb-note` | 05-how-to-read.md | randomness 分類 | **5** | 5 | 分類頁數 | …《黑天鵝效應》要讀第二版：〈後記論文〉是兩本書之間的橋，四象限地圖與冗餘哲學都在那裡。 randomness 分類五頁裡的四頁（從[黑天鵝與極端世界](../concep… |
| `taleb-note` | 05-how-to-read.md | antifragility 分類 | **3** | 3 | 分類頁數 | …mness/fourth-quadrant-and-robustness/)）接住前者，antifragility 分類三頁（從[反脆弱三元組與槓鈴策略](../concept… |
| `taleb-note` | 05-how-to-read.md | asymmetry-practice 分類 | **4** | 4 | 分類頁數 | …為預設你已有前兩階的裝備。 遍歷性一章是系列統計直覺的最深處，先讀反而會覺得只是格言。 asymmetry-practice 分類四頁逐章展開，讀前地圖是[切膚之痛](../concep… |
| `taleb-note` | 05-how-to-read.md | fat-tails 分類 | **3** | 3 | 分類頁數 | …體感進，流動性坑洞與陰影 gamma 是模型課不教的東西。 **散文線讀者**不必硬啃：fat-tails 分類三頁（[肥尾的統計後果](../concepts/fat… |
| `wujun-note` | 02-threads.md | tech-civilization 分類 | **5** | 5 | 分類頁數 | …長鏡頭，大勢不是玄學，是有定律的  要看清位置與方向，得先看見大勢。 第一支透鏡是歷史，tech-civilization 分類五頁。 [浪潮之巔](../concepts/tech-… |
| `wujun-note` | 02-threads.md | science 分類 | **3** | 3 | 分類頁數 | …的人談格局，只能靠運氣站位。  ## 透鏡二：數學的顯微鏡，工程師給見識裝的另一隻眼  science 分類三頁是吳軍的本行。 [數學之美](../concepts… |
| `wujun-note` | 02-threads.md | wisdom 分類 | **3** | 3 | 分類頁數 | …嗅出來的。  ## 方法論：元智慧，可遷移的那一層  具體領域的知識會過期，什麼不會？ wisdom 分類三頁的答案是「智慧的智慧」。 [元智慧](../conc… |
| `wujun-note` | 02-threads.md | learning 分類 | **3** | 3 | 分類頁數 | …看的能力，元智慧把看到的東西變成可遷移的判斷力。  ## 養成：卓越是複利，不是事件  learning 分類三頁管時間。 [卓越](../concepts/lear… |

</details>

## 修法

**保語氣、只改被現況打臉的數字**（MODEL-ROUTING §二最後一列：導覽過期多數不必重寫，只要對帳）。改完把該章的 `writtenAt` 推到當天；如果是 `overview.ts`，順手看一眼`lede`／`Verdict` 有沒有一起過期。

數字對不上時**不預設是導覽錯**：頁被合併或除役時，導覽反而可能是對的——先看那句話在講什麼。

## 驗證

```bash
notes-core/tools/export-guide-drift.py --validate "2026-09-03 15:00"
```
拿各站在那個時間點的導覽文字配**現在**的頁數重跑：那之後被人改掉的數字＝真債、沒改的＝正確；算分類器在這套標籤上的漏報與誤報。

## 重跑

```bash
notes-core/tools/export-guide-drift.py
```
