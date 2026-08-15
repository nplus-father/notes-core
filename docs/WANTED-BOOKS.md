# 待收書單（bibliography `wanted` 全星系匯出）

**這份是什麼**：各 note 站 `src/data/bibliography.ts` 裡標成 `status: "wanted"` 的書，
全部匯出成一張採購清單。書名以**英文原名**為主，中譯附在後面，並附**作者**——
同名不同書會讓人買錯（portal 上的 `servant-leadership` 是 Larry W. Boone 的教科書，
不是 Greenleaf 1977 原典），下單前請對作者。由
`notes-core/tools/export-wanted.py` 生成，**不要手改**——改各站的 bibliography 再重跑。

**已收錄比對的資料源**：GitHub 現況（`gh repo list` nplus-father／Andrewnplus，1901 個 repo）。

## 先收這 7 本

全星系的 wanted 只剩 7 筆，**這節就是全部**，順序即建議的採購與消化順序（薄的、起手容易的排前面）。**這節是全檔唯一的人工區塊**——要改請編 `export-wanted.py` 的 `TOP20`，不要改這裡。挑選準則依序：**①歸零槓桿——優先收「還差 1–2 本就收齊」的站所缺的書**（見下面「快歸零的站」那節，腳本自動算；站書單一歸零，缺書就不再是它進 `note-check --enrich` 深化的瓶頸） ②多站共等，收一本補多站 ③站主自己在 `note` 裡標了「最大／頭號缺口」 ④portal 驗證的 anchor 深度——nplus.wiki 上已經建成幾本回指它的書站（同作者書櫃、同一條線的衍生書），書櫃愈深、原典愈缺就排愈前面（見 [SOURCING-DEBT.md](./SOURCING-DEBT.md)） ⑤同等重要時，薄的、有繁中在版的排前面。

「站」欄的 `(n)` ＝**收了這本之後該站還剩幾本**；`(0)` 就是這一本收了該站即歸零。

「為何排這裡」的 portal 數字都是實查出來的（作者書櫃本數、同一條線的衍生書數、各站概念頁引用處數）；`/note-wanted` 每次重挑會一併重查。

| # | 英文書名 | 作者 | 中譯 | 年 | 站 | 為何排這裡 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **The Wealthy Barber** | David Chilton |  | 1989 | personal-finance(0) | personal-finance 站 owned 39／wanted 1——**收了就歸零**，準則①，而且是全星系缺口最小的站（2.5%）；證據形狀是這輪最乾淨的一筆——portal 已經有 `wealthy-barber-returns`（David Barr Chilton 2011 的續集，README 標「富足理髮師回來了」），**續集在、1989 的原典不在**，Chilton 書櫃就這一本。「理財」全星系 51 處／32 檔／跨 17 站（personal-finance 16 居首、kiyosaki 10、investing 4）；北美國民理財入門的敘事體始祖，薄，無繁中 |
| 2 | **Versioning in an Event Sourced System** | Greg Young |  | 2017 | data-systems(0) | data-systems 站 owned 18／wanted 1——**收了就歸零**，準則①；「事件溯源」全星系 35 處／12 檔**只跨 2 站**（data-systems 22、system-design 13）、`schema` 112 處／27 檔（data-systems 66 居首、system-design 23）——兩個站都在談事件與 schema，而「事件 schema 改了、舊事件怎麼辦」這個演進期問題在星系裡**沒有任何出處**，那正是這本的全部內容；portal 的事件溯源線這輪剛補上 `designing-event-driven-systems`（Stopford）與 `cqrs-command-query-responsibility-segregation`（Ajay Kumar）兩本，**Greg Young 仍是 0 本**——提出這個詞的人不在架上；Leanpub 小冊，薄且便宜 |
| 3 | **Christian Theology: An Introduction** | Alister E. McGrath 麥葛福 | 基督教神學手冊 | 1994 | theology(1) | theology 站 owned 62／wanted 2——**這兩本收齊就歸零**，準則①，這批排頭是準則⑤（薄、有繁中）；準則④的證據這輪變強了：portal 有 McGrath 的 `christian-theology-reader`，那正是**這本教科書的配套讀本**（原始文獻選輯）——**配套在、本體不在**；McGrath 書櫃 2 本（另一本是他寫的巴刻傳記 `j-i-packer-his-life-and-thought`）。「系統神學」全星系 62 處／21 檔／跨 6 站（theology 49、biblical-studies 5），portal 系統神學線 4 本（Grudem、Erickson、Vos、林鴻信）——福音派、改革宗、華人都有，缺的是英美神學院最通行的那本導論。⚠ `erickson-christian-theology` 是 Millard Erickson 的**同名書**，下單前對作者；有繁中《基督教神學手冊》 |
| 4 | **Summa Theologiae** | Thomas Aquinas 阿奎那 | 神學大全 | 1274 | theology(1) | theology 的第二本，收了本站歸零；準則④同樣是「配套在、本體不在」——portal 的 `thomas-aquinas-summa-theologiae` 其實是 Bernard McGinn 寫的**這本書的傳記**（Princeton 名著傳記系列），**阿奎那本人 0 本**。概念側承認是薄的：「阿奎那」全星系 8 處／6 檔／跨 4 站（theology 4、peterson 2）、「中世紀」50 處／33 檔（theology 14 居首），但「經院」只有 **3 處**（lewis 2、theology 1）——所以它排在 McGrath 後面而不是前面；部頭極鉅，中譯有全集，起手挑選讀本即可 |
| 5 | **NICNT** | NICNT 系列（各卷作者不同：Moo《Romans》、Fee《1 Corinthians》…） | ／NICOT 系列代表卷 |  | biblical-studies(2) | **準則③**：站主在該筆 `note` 自註「學術註釋的系列級缺口」，是這 7 本裡唯一一筆站主自標。biblical-studies 站 owned 74／wanted 3（缺口 3.9%），背景註釋（IVP 舊約背景）、釋經學（`hermeneutical-spiral`）、Beale/Carson 的舊約引用註釋都齊了，逐節學術註釋也有 Waltke 的 `genesis-waltke`——**但那是舊約，新約那側一卷都沒有**：「羅馬書」全星系 54 處／19 檔／跨 4 站（stott 43、theology 8），portal 卻只有 Stott 的 `message-of-romans`（BST 講道式），**牧養式的在、逐節學術的不在**；起手就買 Moo 的《Romans》那一卷，別想一次收整套；厚，無繁中 |
| 6 | **Echoes of Scripture in the Letters of Paul** | Richard B. Hays |  | 1989 | biblical-studies(2) | biblical-studies 的第二本，準則④；portal 有 Hays 的 `moral-vision-of-the-new-testament`——**同作者書櫃 1 本、1989 的開山之作不在**；概念側是本站的主軸：「互文」全星系 9 處**只跨 2 站**（biblical-studies 6、lewis 3）、「聖約」23 處裡 **20 處在本站**，而 portal 搜 intertextual **0 本**——舊約在新約裡怎麼迴響，講了但沒有出處；薄，無繁中 |
| 7 | **Old Testament Theology** | John Goldingay |  | 2003 | biblical-studies(2) | biblical-studies 的第三本，排最後——**準則④的證據是這 7 本裡最弱的，誠實記下來**：portal 的舊約神學線已經有 Brueggemann 的 `theology-of-the-old-testament` 與 Waltke 的 `old-testament-theology-waltke` 兩本，Goldingay 自己的單卷 `biblical-theology-goldingay` 也已收（他還有 `ezra-nehemiah-esther-for-everyone`，書櫃 2 本）——**不是空格，是想多收一種進路**；站內「舊約神學」只有 3 處／2 檔且全在本站。三卷大部頭、無繁中，收了 biblical-studies 才歸零，但排序上讓它殿後 |

**這是「書本身還沒有」那個軸**，與 docs/ 其餘幾份不同：

| 文件 | 缺口是什麼 | 靠什麼補 |
| --- | --- | --- |
| [COVERAGE-GAPS.md](./COVERAGE-GAPS.md) | 還沒有**站** | 開新站 |
| [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md) | 站在、**內容**沒寫完 | `note-check --enrich` |
| [SOURCING-DEBT.md](./SOURCING-DEBT.md) | 內容寫了、查不到**出處** | 掛 anchor |
| [ORPHAN-BOOKS.md](./ORPHAN-BOOKS.md) | **書有了、沒有站在管** | 認領／開站 |
| **本檔** | **書本身還沒有** | **去收書** |

> 本檔是「**站**說它缺什麼」的正向視角，看不到「沒有任何站提過」的書——那一側看
> [ORPHAN-BOOKS.md](./ORPHAN-BOOKS.md)。兩份要成對看，`tools/refresh-galaxy-docs.sh` 一次重算。

## bibliography 的四個 status

`library.ts` 的 `BibliographyStatus`，語意是「**這本書在書庫裡的狀態**」，不是「讀過沒有」：

| status | 意思 | 判準 | 筆數 |
| --- | --- | --- | --- |
| `owned` | **已收錄**——書已經做成 `nplus.wiki/<slug>/` 的書站 | 必須有 `slug`；首頁書架的封面列就是取這批，概念頁的 `furtherReading.anchor` 也是連到這裡 | 1891 筆（去重 1410 本） |
| `wanted` | **待收錄**——想收、還沒有 | 買得到，只是還沒買／還沒做站 | **7 筆（去重 7 本）** |
| `unavailable` | **暫無來源**——想收但收不到 | 絕版、無中譯、或只有機構授權（如 Scrum Guide、Vanguard 內部傳記） | 86 筆 |
| `skipped` | **刻意略過**——不打算收 | 內容重複、練習冊、合輯、不合站主軸；`note` 欄寫明為何略過 | 82 筆 |

> `owned` 去重後的 1410 是**已建成書站的書**（1891 是含跨站重複的登錄筆數，
> 一本書被三站列進盤點就算三筆）。它代表「書站存在、封面抓得到、概念頁 anchor 回得去」，
> 不等於實體書在書架上。

## 先扣掉：0 本其實已經有書站了

這些 `wanted` 的書名對得上**已存在的書 repo**——不必再收，是各站 bibliography 的 status 沒跟上。**買書前先扣掉這批**，並把該筆改成 `status: "owned"` ＋ 補上 `slug`（＝下表的 repo slug）再重跑；`/note-wanted` 會代勞。

| 書 repo slug | 書名 | 登記在 | portal 上的描述（核對用） |
| --- | --- | --- | --- |

## 作者這一關擋下的：1 筆同名不同書

書名正規化後對得上某個書 repo，**但作者不符**——所以那本不是這一筆想收的書，維持 `wanted`。這關是 2026-08-10 加的第二因子；在那之前 matcher 只比書名，撞名只能靠 `NAME_COLLISIONS` 人工白名單一筆筆補（踩到才補）。

**下面每一筆都要當成買錯書的預警**：想收的和 portal 上那本同名，下單前對作者，別對書名。

| 想收的書 | 想收的作者 | 撞到的 repo | repo 上的作者 | 登記在 |
| --- | --- | --- | --- | --- |
| Christian Theology: An Introduction | Alister E. McGrath 麥葛福 | `erickson-christian-theology` | Millard J. Erickson | theology-note |

## 疑似漏報：0 本可能其實已經有 repo

書名**沒有**正規化後完全相同，但 portal 上有 repo 長得很像——改過書名（英美版不同、中譯轉寫）的書會落在這裡。**這節是提名，不是判決**：確認是同一本就寫進 `export-wanted.py` 的 `ALIASES`，下一輪它就走精確路徑並自動掉進「先扣掉」；確認是續集或同系列的不同書就不用管，下輪還會再問一次。

門檻：兩邊書名的**雙向 Jaccard ≥70%**（詞相等的判準放寬到共同前綴 5 字元，才抓得到 `Forgiving` ↔ `Forgiveness` 這種詞形差異），且**作者沒有互相否決**。用雙向而不是單向覆蓋率，是因為單向會被系列卷洗版——`… on Leadership` 的詞有 75% 出現在 `… on Communication` 裡，但那是不同的一本。作者不符的已經在上一節擋掉；`NAME_COLLISIONS` 裁決過的不再提名。

無——沒有書名相近卻沒對上的。

## 快歸零的站：3 站只差 1–2 本

**TOP20 的準則①就看這一節。** 這些站的書單已經接近收齊，剩下的一兩本收到，整站的採購缺口就歸零——缺書不再是它進 `note-check --enrich` 深化的瓶頸。分母只算 `owned + wanted`（`unavailable` / `skipped` 是永久不可收，不算欠）。

| 站 | 已收 | 還差 | 差哪幾本 |
| --- | ---: | ---: | --- |
| `personal-finance-note` | 39 | **1** | The Wealthy Barber（David Chilton） |
| `data-systems-note` | 18 | **1** | Versioning in an Event Sourced System（Greg Young） |
| `theology-note` | 62 | **2** | Christian Theology: An Introduction（Alister E. McGrath 麥葛福）、Summa Theologiae（Thomas Aquinas 阿奎那） |

## 優先收：0 本有兩個以上的站在等

同一本書被多站列為 `wanted`——收一本補多站的缺口，投資報酬率最高。

| 英文書名 | 作者 | 中譯 | 年 | 等它的站 |
| --- | --- | --- | --- | --- |

## 完整清單（依站，共 7 筆）

### biblical-studies-note — 3 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Old Testament Theology | John Goldingay |  | 2003 | Goldingay 的敘事進路大部頭，共三卷（其單卷《聖經神學》已收） |
| Echoes of Scripture in the Letters of Paul | Richard B. Hays |  | 1989 | Hays——互文性讀保羅的開山之作 |
| NICNT | NICNT 系列（各卷作者不同：Moo《Romans》、Fee《1 Corinthians》…） | ／NICOT 系列代表卷 |  | 學術註釋的系列級缺口——如 Moo《Romans》、Fee《1 Corinthians》、Wenham《Genesis》 |

### theology-note — 2 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Christian Theology: An Introduction | Alister E. McGrath 麥葛福 | 基督教神學手冊 | 1994 | 麥葛福；最平衡的入門教科書。portal 的 erickson-christian-theology 是 Millard Erickson 的同名書，不是這一本——下單前對作者 |
| Summa Theologiae | Thomas Aquinas 阿奎那 | 神學大全 | 1274 | 阿奎那；中譯有全集但部頭極鉅 |

### data-systems-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Versioning in an Event Sourced System | Greg Young |  | 2017 | Greg Young；事件溯源在演進期的實務難題 |

### personal-finance-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| The Wealthy Barber | David Chilton |  | 1989 | Chilton；北美國民理財入門的敘事體始祖 |

## 沒有英文書名的 0 本（華文／日文原著）

這些本來就沒有英文版，照原書名收。

| 原書名 | 作者 | 站 | 為何想收 |
| --- | --- | --- | --- |

## 重跑

```bash
notes-core/tools/export-wanted.py
```

收到書、建好書站之後，把該站 bibliography 那筆改成 `status: "owned"` 並補 `slug`，
重跑就會從這裡消失。
