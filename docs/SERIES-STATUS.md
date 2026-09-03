# SERIES-STATUS — check → enrich → guide 系列帳本

**這份是什麼**：全星系「書收齊＋相關書都做完（content fill＋deep overview）」的站，推進
**check → enrich → guide** 產線的執行帳本。

**站側數字是重算的，不是手打的**（2026-08-28 起）：`tools/galaxy-checkup.py --json` 一次掃完
75 站（頁數／溯源／mastery／roadmap／findings），導覽日期取 `src/content/guide/*.md` 的最大
`writtenAt`，owned 數來自各站 `bibliography.ts`。要刷新就重跑那支再更新本檔——
08-20 那輪用的一次性 scratchpad 腳本已被它取代。**書端也已工具化**（2026-08-28 起）：
空葉章用 `hugo-book-manager/scripts/audit-empty-leaves.py --all`、深度概覽用同目錄的
`audit-overview.py`；本檔留著手動維護的只剩「這筆債要不要現在還」的判斷。

**與其他 docs 的分工**：[DEEPEN-READY.md](./DEEPEN-READY.md)＝每次重算的自動排序表；
本檔＝**系列定義＋收官狀態＋書端現況**。站側逐站數字不再抄在這裡——要看就跑 `galaxy-checkup.py --json`。

> **注意 leetcode-note 不在這 75 站裡**：它 2026-07 起自維護前端（`src/content/` 是
> `guides`／`overviews`／`problems`，沒有 `concepts`），`galaxy-checkup` 不掃它，本系列也不涵蓋。

## 系列判準（2026-08-20 對帳定案）

- **收書歸零**：bibliography `wanted = 0`（`unavailable`／`skipped` 不算欠）。
- **書端完工**：owned 全數 ① deep overview 品檢 PASS（`audit-overview.py`）② content fill 完成。
  content fill **以本機實測為準**——portal `health.json`（08-18 產）過期，21 本 08-19～20 剛填完的書被誤標 thin/near-empty。
  **真欠債**葉章 ≥2 的書算未完；恰 1 個（多為附錄）不擋站、只註記；watch 級（8–15k 字）不擋。
  「真欠債」由 `audit-empty-leaves.py` 判定——交叉參照條目與原書就沒有的章不算（見書端卡點節）。

**結果（2026-08-28 收官）：達標 75 站全數 `wanted = 0`、站側 findings 0，導覽 75/75 全數完工**
——B 組六站當日補齊（pf／lm／cloud／gardner／fengtang／pastoral），guide 產線收官。
書端真欠債 2026-08-28 三輪清畢歸零，thin 待判 2026-09-03 收工不再追（見下節）。
站側進入維護節奏：新書進站才再動；歷次各波戰報已於 2026-09-03 從本檔移除，看 git 歷史。


## 書端：判準與現況

判準同上：空葉章 ≥2 算未完；恰 1 個空葉不擋站、只註記。空葉＝該章 `_index.md` 去掉
frontmatter 後不足 200 字元。深度概覽用 `hugo-book-manager/scripts/audit-overview.py` 驗。

> **空葉不能只用字數判——2026-08-28 為此重掃過一次全庫。** 字數門檻只是「值得看一眼」
> 的觸發器，體裁決定一章該多長。正本工具是 `hugo-book-manager/scripts/audit-empty-leaves.py`
> （`--all` 掃全庫），它把短葉章分四類，只有前兩類算債：`placeholder`（寫著待補）、
> `blank`（完全沒內文）算債；`xref`（辭典的「參見 X」交叉參照）、`source-absent`
> （原書此版本就沒這章）不算債；其餘 `thin` 列出來給人判。
> 首掃 1829 本：**真欠債 56 章，另有 237 章是被門檻撈出來、體裁本來就短的**。
>
> 兩個活標本說明為什麼非分類不可：`dictionary-of-paul` 的 231 條「空葉」**全部**是
> 「阿們 → 參見 Prayer」這種交叉參照，那就是該條的完整內容，真欠債 **0**；
> `on-top-of-tides` 的 5 章則是原書該版本只列章名、正文標「待續」，書上就沒有，補不了。
> 兩本都已從下表移除。
>
> **portal 的 `health.json` 也代替不了這張表**（但原因不同）：它的分級只吃兩個**聚合**
> 數字——總字數與平均密度（`fetch-health.ts` 的 `tierOf(chars, density)`）。聚合值看不見
> 分佈，所以條目型的書半數條目再短也照樣判 `ok`。反過來它判 thin 的書多半真薄，可以信。

> **通則（2026-08-28 Andrew 定案）：以 book repo 為主，它沒有的就當成本來就沒有。**
> 書庫裡沒有原始檔（PDF／EPUB／OCR）的章節**不列為內容債**——要寫只剩「憑模型記憶編造」
> 一條路，那是整套流水線的紅線。`audit-empty-leaves.py` 已加 `no-source` 分類承接這條規則；
> 日後把原始檔放進 repo 目錄，換掉說明重跑即可。

**書端真欠債：0**——2026-08-28 三輪清畢（56 → 32 → 23 → 0）。第一輪修判準（幽靈章／
交叉參照不算債）、第二輪定通則（repo 無原始檔＝no-source 不算債）、第三輪把剩餘 21 本
23 章逐本結清：**能寫的寫**（surprised-by-joy 6,055 字、trend-following 兩章 7.2k 字）、
**原書沒有的寫查證說明**（7 章——含 what-life 的「PREFACE」其實是出版社叢書序非阿德勒）、
**沒原始檔的記 no-source**（14 章）。全庫剩 25 本 thin 待判（工具不猜、逐本人看，多為單章）。

**thin 待判已於 2026-09-03 收工（Andrew 裁決）**：08-30 那筆 strip 註解的 commit 把 `audit-empty-leaves.py`
讀 docstring 的那一行弄壞（跑就 crash），修好後重掃 25 本 54 章。真正像「沒寫」的只有
`witness-to-jesus-as-christ` 五章（只有標題；repo 沒有 PDF／EPUB，git 歷史也從未有過），依 08-28 通則
逐章寫入 no-source 說明。另外 10 章是序、跋、書名頁、索引、讀者須知、有聲書 embed 這類**結構頁**，
工具新增 `structural` 分類（目錄名或 `<embed>` 判定，不計債也不列 thin），同時把「原版 PDF 未包含」
加進 source-absent 的線索。重掃後 thin 剩 **15 本 39 章**，全是體裁本來就短的章（make-time 單招、
dignity-of-speaking 單節、daily-rituals 人物條目之類）與 5 本正文單節，**裁定不再追蹤**；
書端帳到此只剩「新原始檔進 repo 時重跑」一件事。

三筆補洞輪的額外發現，記檔備查：
- `flying-together` 的 PDF **不是原書**——是 Bookey 第三方摘要（jsPDF 產生）；該 repo 的
  「原始檔」其實是衍生品，日後補真原著才能擴寫。
- `resident-aliens` 第二部譯自 1996 年續作 *Where Resident Aliens Live*，repo 只有 1989 原著
  PDF——那一部 5 章偏薄的原因；補 1996 原檔可一次補平。
- `pdftotext -layout` 對 Adobe-Identity-H 字型會整檔萃不出來，**去掉 `-layout` 重跑**即可。
- ~~`central-bank-privilege` 的附錄待定奪~~：2026-08-28 Andrew 確認**原書無附錄**，目錄已刪（`9811d76`）；`message-of-hosea` 的〈致讀者〉同輪確認原書沒有，目錄已刪（`4bcae7e`）。

**08-28 補洞三輪留下的判斷（詳帳在 git 歷史）**：
- **空葉章的成因常是「目錄開錯」不是「還沒寫」**——建 repo 時照猜測或英文選集慣例開的幽靈章，原書根本沒有
  （weight-of-glory 第 10–12 篇、building-microservices 04／05、world-waiting-to-be-born 的 preface）。
  要分兩種缺席：原書沒有 → 刪目錄；原書有、手上這版沒出 → 留目錄標 source-absent。
- **刪目錄前必查有沒有 note 站 anchor 指過去**（實測 0 處才刪）。
- **判斷順序**：先看 repo 有沒有原始檔 → 沒有就是 no-source；有原始檔才問「原書到底有沒有這章」。
- 孤兒書那側的欠債不卡任何站，認領前不必補；舊掃描從站的 owned 出發看不見它們，`--all` 從書庫側掃才看得到。

## 掃描涵蓋範圍與重跑方式

**站側（機器判得準的那半）已固化成 `notes-core/tools/galaxy-checkup.py`**，08-20 那份
一次性 scratchpad 腳本退役。它涵蓋：§1.1 五指標、§1.2 雙向溯源（頁無 anchor＋anchor 對
books-done 實檔驗證＋book slug 存在）、§2 結構（首頁契約、divergence、core pin、分類
`_index.md`、roadmap↔內容、mastery slug、label 分隔號、related 存在＋雙向、seeAlso 實檔、
importance/status 值域、跳脫實體、`:::response`），2026-08-28 起再加**內文相對連結**
（`dead-inline-link`——seeAlso 之外的第二種靜默 404，首掃 101 條）。

**仍要進場逐站做的**：學語氣、§1.3 該挖而未挖分層、§3 backlog 撰寫、§2.5 抽驗防杜撰、
§2.8 build/format/lint。所以跑 checkup **不蓋 `checkedAt`**——蓋章留給進站跑完整
`/note-check` 的那次。

**重跑本檔**：`galaxy-checkup.py --json` 出站側數字，書端那張表要手工重掃空葉章＋
`audit-overview.py`。兩邊都更新完再改本檔的日期標記。
