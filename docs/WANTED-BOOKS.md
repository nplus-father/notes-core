# 待收書單（bibliography `wanted` 全星系匯出）

**這份是什麼**：各 note 站 `src/data/bibliography.ts` 裡標成 `status: "wanted"` 的書，
全部匯出成一張採購清單。書名以**英文原名**為主，中譯附在後面，並附**作者**——
同名不同書會讓人買錯（portal 上的 `servant-leadership` 是 Larry W. Boone 的教科書，
不是 Greenleaf 1977 原典），下單前請對作者。由
`notes-core/tools/export-wanted.py` 生成，**不要手改**——改各站的 bibliography 再重跑。

**已收錄比對的資料源**：GitHub 現況（`gh repo list` nplus-father／Andrewnplus，1882 個 repo）。

## 先收這 20 本

整份 25 筆太長，這是從裡面挑出來的採購順序，也是建議的消化順序（薄的、起手容易的排前面）。**這節是全檔唯一的人工區塊**——要改請編 `export-wanted.py` 的 `TOP20`，不要改這裡。挑選準則依序：**①歸零槓桿——優先收「還差 1–2 本就收齊」的站所缺的書**（見下面「快歸零的站」那節，腳本自動算；站書單一歸零，缺書就不再是它進 `note-check --enrich` 深化的瓶頸） ②多站共等，收一本補多站 ③站主自己在 `note` 裡標了「最大／頭號缺口」 ④portal 驗證的 anchor 深度——nplus.wiki 上已經建成幾本回指它的書站（同作者書櫃、同一條線的衍生書），書櫃愈深、原典愈缺就排愈前面（見 [SOURCING-DEBT.md](./SOURCING-DEBT.md)） ⑤同等重要時，薄的、有繁中在版的排前面。

「站」欄的 `(n)` ＝**收了這本之後該站還剩幾本**；`(0)` 就是這一本收了該站即歸零。

「為何排這裡」的 portal 數字都是實查出來的（作者書櫃本數、同一條線的衍生書數、各站概念頁引用處數）；`/note-wanted` 每次重挑會一併重查。

| # | 英文書名 | 作者 | 中譯 | 年 | 站 | 為何排這裡 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **Technical Analysis of the Financial Markets** | John J. Murphy |  | 1999 | investing(0) | investing 站 owned 61／wanted 1——**收了就歸零**，準則①，而且是全星系缺口最小的站（1.6%）；證據形狀很乾淨：「技術分析」全星系 37 處裡 **35 處在 schwager 站、investing 站只有 2 處**，而 portal 這條線的 7 本全是 Schwager（含入門冊 `getting-started-in-technical-analysis` 與 Market Wizards 五卷）——**入門冊與訪談錄都在，教科書不在**，Murphy 0 本；厚，無繁中 |
| 2 | **Purple Cow** | Seth Godin | 紫牛 | 2003 | marketing(0) | marketing 站 owned 30／wanted 1——**收了就歸零**，準則①；portal 的 Godin 書櫃 3 本（`linchpin`、`permission-marketing`、`this-is-marketing`）獨缺這本成名作，而定位／差異化那條線在 portal 只有 Ries & Trout 的 `positioning` 一本撐著——「值得談論才叫差異化」這半沒有源頭；薄，有繁中《紫牛》，排第一批消化 |
| 3 | **Observability Engineering** | Charity Majors、Liz Fong-Jones & George Miranda |  | 2022 | cloud-infra(1) | cloud-infra 站 owned 24／wanted 2——**這兩本收齊就歸零**，準則①，這批第一本：「可觀測性」全星系 35 處／12 檔，其中 **34 處在本站**、「高基數」9 處（cloud-infra 7、system-design 2）——本站已經在用這套詞彙講事情，而 portal 只有一本華文《可觀測性入門指南》（`observability-beginners-guide`），**Charity Majors／Liz Fong-Jones 0 本**，學派原典不在；無繁中 |
| 4 | **Practical Monitoring** | Mike Julian |  | 2017 | cloud-infra(1) | cloud-infra 的第二本，收了本站歸零；「監控」全星系 132 處／76 檔／跨 25 站（cloud-infra 29 居首、system-design 19、data-systems 9），而站內「監控反模式」只有 **1 處孤證**——講了 132 次監控，反模式那一側只有一句話；portal 搜 monitoring 除了那本華文入門指南之外 0 本；薄，排這批前面，無繁中 |
| 5 | **The Automatic Millionaire** | David Bach | 讓錢為你工作的自動理財法 | 2004 | personal-finance(1) | personal-finance 站 owned 38／wanted 2——**這兩本收齊就歸零**，準則①；「複利」全星系 235 處／107 檔／跨 30 站（tracy 53、personal-finance 39、habits 21、bogle 17），而 portal 的 David Bach 只有 `latte-factor`（拿鐵因子是他的比喻書），**把儲蓄自動化的那本操作手冊不在**；薄，有繁中《讓錢為你工作的自動理財法》 |
| 6 | **The Wealthy Barber** | David Chilton |  | 1989 | personal-finance(1) | personal-finance 的第二本，收了本站歸零；這是準則④裡**證據形狀最乾淨的一筆**——portal 已經有 `wealthy-barber-returns`（Chilton 2011 的續集，README 標「富足理髮師回來了」），**續集在、1989 的原典不在**；北美國民理財入門的敘事體始祖，薄，無繁中 |
| 7 | **The Shellcoder's Handbook** | Chris Anley, John Heasman, Felix Lindner & Gerardo Richarte |  | 2004 | security(1) | security 站 owned 12／wanted 2——**這兩本收齊就歸零**，準則①；缺口 14.3% 是這批三個站裡最高的。站內「緩衝區溢位」2 處全在本站；portal 記憶體漏洞這條線只有 `hacking-art-of-exploitation`（Erickson 講原理），**Anley 0 本**，各平台實務那半沒有；厚，無繁中，所以排在歸零批的後段 |
| 8 | **Practical Malware Analysis** | Michael Sikorski & Andrew Honig |  | 2012 | security(1) | security 的第二本，收了本站歸零；「惡意程式」全星系只有 2 處／2 檔**且都在本站**，security 站內「逆向工程」**0 處**（全星系那 6 處在 de-botton／marketing／writing／management，是比喻用法，不算數）；portal 搜 malware **0 本**——防守方讀攻擊產物這條線在星系裡完全空白。缺口最大但概念證據最薄，所以排準則①批的最後；厚，無繁中 |
| 9 | **NICNT** | NICNT 系列（各卷作者不同：Moo《Romans》、Fee《1 Corinthians》…） | ／NICOT 系列代表卷 |  | biblical-studies(3) | **準則③**：站主在該筆 `note` 自註「學術註釋的系列級缺口」。biblical-studies 站 owned 73 本，背景註釋（IVP 新約／舊約背景）、釋經學（`hermeneutical-spiral`）、Beale/Carson 的舊約引用註釋都齊了，單卷學術註釋也有 Waltke 的 `genesis-waltke`——**但新約那側一卷都沒有**：「羅馬書」全星系 34 處／14 檔／跨 4 站（stott 23、theology 8），portal 卻只有 Stott 的 `message-of-romans`（BST 講道式），**牧養式的在、逐節學術的不在**；起手就買 Moo 的《Romans》那一卷，別想一次收整套；厚，無繁中 |
| 10 | **Designing Event-Driven Systems** | Ben Stopford |  | 2018 | data-systems(2) | data-systems 站 owned 16／wanted 3，缺口 15.8% 是四個候選站裡最高的，**整批排進來就是第四個歸零的站**（準則①的本意延伸）；這本排頭是準則⑤——O'Reilly 免費電子書，**零成本起手**。「事件驅動」全星系 42 處／21 檔／跨 6 站（system-design 24、data-systems 5、design-patterns 5），而 portal 這條線只有 `kafka-definitive-guide`，**Stopford 0 本**；薄 |
| 11 | **Streaming Systems** | Tyler Akidau、Slava Chernyak & Reuven Lax |  | 2018 | data-systems(2) | data-systems 的第二本，**這批最該收的一本**：「串流」全星系 56 處／28 檔／跨 11 站（system-design 24、data-systems 20）、「事件溯源」35 處只跨 2 站（data-systems 22、system-design 13）、watermark 9 處全在本站——**兩個站在互相引用同一組概念，卻共用不到一本原典**；portal 這條線目前是 Kleppmann 的 `designing-data-intensive-applications` ＋ `kafka-definitive-guide` 兩本在撐，**Akidau 0 本**，watermark／trigger 的語意出處不在；厚，無繁中 |
| 12 | **Versioning in an Event Sourced System** | Greg Young |  | 2017 | data-systems(2) | data-systems 的第三本，收了本站歸零；「事件溯源」那 35 處講的是模型，**版本演進**（事件 schema 改了舊事件怎麼辦）在站內沒有出處，而那正是這本的全部內容；portal 的 Greg Young **0 本**——事件溯源這個詞的提出者本人不在架上；Leanpub 小冊，薄且便宜，排這批最後當補完 |
| 13 | **The Reformed Pastor** | Richard Baxter 巴克斯特 | 改革宗的牧師 | 1656 | theology(3) | theology 站 owned 60／wanted 4，準則④這批第一本，選它排頭是因為**薄、有繁中、而且 portal 完全空白**：搜 puritan／Baxter **0 本**，牧養線只有 Peterson 的 `contemplative-pastor`（當代默觀進路）。概念側對得上——「牧養」全星系 129 處／45 檔／跨 7 站（theology 58、pastoral-psychology 25、nouwen 20、stott 16）、「清教徒」26 處（theology 22）——清教徒牧養講了 22 次，正典不在；有繁中《改革宗的牧師》 |
| 14 | **Christian Theology: An Introduction** | Alister E. McGrath 麥葛福 | 基督教神學手冊 | 1994 | theology(3) | theology 的第二本；「系統神學」全星系 60 處／19 檔／跨 5 站（theology 49、biblical-studies 5），portal 的系統神學線有 Grudem、加爾文《基督教要義》、林鴻信《系統神學》——**福音派、改革宗、華人各一本，缺的是英美神學院最通行的那本教科書式導論**。⚠ portal 的 `erickson-christian-theology` 是 Millard Erickson 的同名書，**要收的是麥葛福（McGrath）那本**，下單前對作者；有繁中《基督教神學手冊》 |
| 15 | **Willpower: Rediscovering the Greatest Human Strength** | Roy F. Baumeister & John Tierney | Willpower 增強你的意志力 | 2011 | habits(5) | habits 站 owned 38／wanted 6，準則④這批第一本，也是 habits 六本裡證據最強的：「意志力」全星系 **167 處／94 檔／跨 32 站**（habits 30、tools 16、tracy 12、cloud 12、newport 11、growth 10）——散得極開，而站內「自我耗損」只有 **1 處孤證**；portal 的 Baumeister **0 本**，意志力線只有 Meadows 的 `365-days-with-self-discipline` 這種通俗冊。講了 167 次的東西沒有機制層的出處；有繁中《增強你的意志力》 |
| 16 | **Good Habits, Bad Habits** | Wendy Wood |  | 2019 | habits(5) | habits 的第二本；「習慣」線在 portal 是通俗三本當家（`atomic-habits`、`power-of-habit`、`tiny-habits`），**Wendy Wood 0 本**；站內「習慣迴路」22 處裡 **19 處在本站**且全是 Duhigg 那套模型，而「習慣科學」只有 **1 處孤證**——情境與摩擦力的學院派證據沒有出處；無繁中 |
| 17 | **Discipline Is Destiny** | Ryan Holiday |  | 2022 | habits(5) | habits 的第三本；「自律」全星系 196 處／81 檔／跨 23 站（peck 53、habits 35、tracy 33、thinking 12、leadership 12），portal 的 Ryan Holiday 書櫃 3 本（`daily-stoic`、`ego-is-the-enemy`、`obstacle-is-the-way`）——**四樞德系列獨缺自律卷**（那 3 本加 Seneca `letters-from-a-stoic`、Salzgeber `little-book-of-stoicism` 就是 portal 斯多噶線的全部 5 本）；薄，無繁中 |
| 18 | **Stolen Focus** | Johann Hari | 誰偷走了你的專注力？ | 2022 | habits(5) | habits 的第四本；「專注力」全星系 40 處／19 檔／跨 8 站（tools 24、habits 5、newport 4），portal 這條線已經有 `indistractable`（Eyal）、`hyperfocus`（Bailey）等個人對策書——**缺的是「為什麼整代人的專注力被拿走」那個系統性成因**，Hari 0 本；有繁中《誰偷走了你的專注力？》 |
| 19 | **Echoes of Scripture in the Letters of Paul** | Richard B. Hays |  | 1989 | biblical-studies(3) | biblical-studies 的第二本（NICNT 之後）；portal 已經有 Hays 的 `moral-vision-of-the-new-testament`——**同作者書櫃有 1 本、1989 的開山之作不在**；站內「互文」7 處裡 6 處在本站、「聖約」23 處裡 20 處在本站，舊約在新約裡怎麼迴響是本站的主軸之一，卻沒有這本；薄，無繁中 |
| 20 | **Jesus and the Eyewitnesses** | Richard Bauckham |  | 2006 | biblical-studies(3) | biblical-studies 的第三本；「目擊者」全星系 17 處／8 檔（biblical-studies 6、keller 6），portal 搜 eyewitness／historical Jesus／Bauckham **0 本**——新約書櫃已有 9 本掛 new testament（Carson 導論、賴特三本、`state-of-new-testament-studies` 等），**福音書史料可信度這一格是空的**；厚（500+ 頁），無繁中，排最後 |

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
| `owned` | **已收錄**——書已經做成 `nplus.wiki/<slug>/` 的書站 | 必須有 `slug`；首頁書架的封面列就是取這批，概念頁的 `furtherReading.anchor` 也是連到這裡 | 1875 筆（去重 1393 本） |
| `wanted` | **待收錄**——想收、還沒有 | 買得到，只是還沒買／還沒做站 | **25 筆（去重 25 本）** |
| `unavailable` | **暫無來源**——想收但收不到 | 絕版、無中譯、或只有機構授權（如 Scrum Guide、Vanguard 內部傳記） | 85 筆 |
| `skipped` | **刻意略過**——不打算收 | 內容重複、練習冊、合輯、不合站主軸；`note` 欄寫明為何略過 | 82 筆 |

> `owned` 去重後的 1393 是**已建成書站的書**（1875 是含跨站重複的登錄筆數，
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

## 快歸零的站：5 站只差 1–2 本

**TOP20 的準則①就看這一節。** 這些站的書單已經接近收齊，剩下的一兩本收到，整站的採購缺口就歸零——缺書不再是它進 `note-check --enrich` 深化的瓶頸。分母只算 `owned + wanted`（`unavailable` / `skipped` 是永久不可收，不算欠）。

| 站 | 已收 | 還差 | 差哪幾本 |
| --- | ---: | ---: | --- |
| `investing-note` | 61 | **1** | Technical Analysis of the Financial Markets（John J. Murphy） |
| `marketing-note` | 30 | **1** | Purple Cow（Seth Godin） |
| `personal-finance-note` | 38 | **2** | The Automatic Millionaire（David Bach）、The Wealthy Barber（David Chilton） |
| `cloud-infra-note` | 24 | **2** | Observability Engineering（Charity Majors、Liz Fong-Jones & George Miranda）、Practical Monitoring（Mike Julian） |
| `security-note` | 12 | **2** | Practical Malware Analysis（Michael Sikorski & Andrew Honig）、The Shellcoder's Handbook（Chris Anley, John Heasman, Felix Lindner & Gerardo Richarte） |

## 優先收：0 本有兩個以上的站在等

同一本書被多站列為 `wanted`——收一本補多站的缺口，投資報酬率最高。

| 英文書名 | 作者 | 中譯 | 年 | 等它的站 |
| --- | --- | --- | --- | --- |

## 完整清單（依站，共 25 筆）

### habits-note — 6 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Good Habits, Bad Habits | Wendy Wood |  | 2019 | Wendy Wood：習慣科學的學院派正典——情境與摩擦力 |
| Stolen Focus | Johann Hari | 誰偷走了你的專注力？ | 2022 | Hari：專注力崩壞的系統性成因 |
| Daily Rituals: How Artists Work | Mason Currey |  | 2013 | Currey：161 位創作者的作息田野調查 |
| Rest | Alex Soojung-Kim Pang |  | 2016 | Pang：刻意休息是深度工作的另一半 |
| Discipline Is Destiny | Ryan Holiday |  | 2022 | Holiday：斯多噶四樞德的自律卷 |
| Willpower: Rediscovering the Greatest Human Strength | Roy F. Baumeister & John Tierney | Willpower 增強你的意志力 | 2011 | Baumeister：意志力科學的正典（自我耗損後續有爭議，仍值得收） |

### biblical-studies-note — 4 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Old Testament Theology | John Goldingay | 三卷） | 2003 | Goldingay 的敘事進路大部頭（其單卷《聖經神學》已收） |
| Jesus and the Eyewitnesses | Richard Bauckham |  | 2006 | Bauckham——福音書作為目擊者見證 |
| Echoes of Scripture in the Letters of Paul | Richard B. Hays |  | 1989 | Hays——互文性讀保羅的開山之作 |
| NICNT | NICNT 系列（各卷作者不同：Moo《Romans》、Fee《1 Corinthians》…） | ／NICOT 系列代表卷 |  | 學術註釋的系列級缺口——如 Moo《Romans》、Fee《1 Corinthians》、Wenham《Genesis》 |

### theology-note — 4 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Reformed Dogmatics | Herman Bavinck 巴文克 | 改革宗教理學 | 1906 | 巴文克；改革宗系統神學的巔峰，中譯陸續出版 |
| Christian Theology: An Introduction | Alister E. McGrath 麥葛福 | 基督教神學手冊 | 1994 | 麥葛福；最平衡的入門教科書。portal 的 erickson-christian-theology 是 Millard Erickson 的同名書，不是這一本——下單前對作者 |
| Summa Theologiae | Thomas Aquinas 阿奎那 | 神學大全 | 1274 | 阿奎那；中譯有全集但部頭極鉅 |
| The Reformed Pastor | Richard Baxter 巴克斯特 | 改革宗的牧師 | 1656 | 巴克斯特；清教徒牧養的正典 |

### data-systems-note — 3 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Streaming Systems | Tyler Akidau、Slava Chernyak & Reuven Lax |  | 2018 | Akidau 等；watermark／trigger——串流語意的正典 |
| Designing Event-Driven Systems | Ben Stopford |  | 2018 | Stopford；以 Kafka 為底的事件驅動服務，O'Reilly 免費電子書 |
| Versioning in an Event Sourced System | Greg Young |  | 2017 | Greg Young；事件溯源在演進期的實務難題 |

### cloud-infra-note — 2 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Observability Engineering | Charity Majors、Liz Fong-Jones & George Miranda |  | 2022 | Majors 等；高基數事件與「未知的未知」——可觀測性學派的正典 |
| Practical Monitoring | Mike Julian |  | 2017 | Julian；監控反模式與務實起步 |

### personal-finance-note — 2 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| The Automatic Millionaire | David Bach | 讓錢為你工作的自動理財法 | 2004 | Bach；把儲蓄自動化的經典操作手冊 |
| The Wealthy Barber | David Chilton |  | 1989 | Chilton；北美國民理財入門的敘事體始祖 |

### security-note — 2 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| The Shellcoder's Handbook | Chris Anley, John Heasman, Felix Lindner & Gerardo Richarte |  | 2004 | 記憶體漏洞利用的另一本正典，與 Erickson 互補（他講原理，這本講各平台實務） |
| Practical Malware Analysis | Michael Sikorski & Andrew Honig |  | 2012 | 防守方讀攻擊產物的標準教材——本站目前完全沒有惡意程式分析這條線 |

### investing-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Technical Analysis of the Financial Markets | John J. Murphy |  | 1999 | Murphy;技術分析的教科書標準(Schwager 入門冊已收) |

### marketing-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Purple Cow | Seth Godin | 紫牛 | 2003 | Godin；卓越到值得談論才是行銷 |

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
