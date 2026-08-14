# 待收書單（bibliography `wanted` 全星系匯出）

**這份是什麼**：各 note 站 `src/data/bibliography.ts` 裡標成 `status: "wanted"` 的書，
全部匯出成一張採購清單。書名以**英文原名**為主，中譯附在後面，並附**作者**——
同名不同書會讓人買錯（portal 上的 `servant-leadership` 是 Larry W. Boone 的教科書，
不是 Greenleaf 1977 原典），下單前請對作者。由
`notes-core/tools/export-wanted.py` 生成，**不要手改**——改各站的 bibliography 再重跑。

**已收錄比對的資料源**：GitHub 現況（`gh repo list` nplus-father／Andrewnplus，1804 個 repo）。

## 先收這 20 本

整份 98 筆太長，這是從裡面挑出來的採購順序，也是建議的消化順序（薄的、起手容易的排前面）。**這節是全檔唯一的人工區塊**——要改請編 `export-wanted.py` 的 `TOP20`，不要改這裡。挑選準則依序：**①歸零槓桿——優先收「還差 1–2 本就收齊」的站所缺的書**（見下面「快歸零的站」那節，腳本自動算；站書單一歸零，缺書就不再是它進 `note-check --enrich` 深化的瓶頸） ②多站共等，收一本補多站 ③站主自己在 `note` 裡標了「最大／頭號缺口」 ④portal 驗證的 anchor 深度——nplus.wiki 上已經建成幾本回指它的書站（同作者書櫃、同一條線的衍生書），書櫃愈深、原典愈缺就排愈前面（見 [SOURCING-DEBT.md](./SOURCING-DEBT.md)） ⑤同等重要時，薄的、有繁中在版的排前面。

「站」欄的 `(n)` ＝**收了這本之後該站還剩幾本**；`(0)` 就是這一本收了該站即歸零。

「為何排這裡」的 portal 數字都是實查出來的（作者書櫃本數、同一條線的衍生書數、各站概念頁引用處數）；`/note-wanted` 每次重挑會一併重查。

| # | 英文書名 | 作者 | 中譯 | 年 | 站 | 為何排這裡 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **Managing in the Next Society** | Peter F. Drucker | 下一個社會 | 2002 | drucker(1) | drucker 站 owned 18／wanted 2——**這兩本收齊就歸零**，準則①；這批選 drucker 而不是同樣差 2 本的 gardner，是因為概念側證據差很多：「知識工作者」全星系 **94 處跨 4 站**（drucker 34、management 23、business-strategy 18、newport 8），而這本正是講知識工作者成為下一個社會重心的那本——站內「下一個社會」只有 1 處、「高齡化」1 處，講了 94 次的主軸沒有終點站；portal 的 Drucker 書櫃 **18 本**是全星系最深的單一作者；有繁中《下一個社會》 |
| 2 | **Drucker on Asia** | Peter F. Drucker & 中內功 | 杜拉克看亞洲 | 1997 | drucker(1) | drucker 的第二本，收了本站歸零。**這本本身的概念證據很薄**（「亞洲」全星系 19 處、drucker 站 0 處，「日本式經營」0 處）——排進來純粹是準則①：它是這站最後一本，不收就得為了一本書把整站留在採購清單上。與中內功的對談錄，薄；有繁中《杜拉克看亞洲》 |
| 3 | **The Total Money Makeover** | Dave Ramsey |  | 2003 | personal-finance(6) | personal-finance 站 owned 33／wanted 7，準則④裡**證據最乾淨的一筆**：portal 已經有它的續集 `baby-steps-millionaire`，那個 repo 自己的描述就寫著「The Total Money Makeover follow-up」——**衍生書在、原典不在**；「無債務」全星系只有 2 處且都在本站，Baby Steps 這套體系在星系裡沒有源頭（「債務」185 處看起來多，但 economics 97 處是主權債務、agile 28 處是技術債，不能算數）；薄，繁中在版與否未查證，下單前自己確認一下 |
| 4 | **Observability Engineering** | Charity Majors、Liz Fong-Jones & George Miranda |  | 2022 | cloud-infra(8) | cloud-infra 站 owned 17／wanted 9（缺口 34.6%，僅次於已整批進榜的 security），這批第一本：「可觀測性」全星系 35 處／12 檔，其中 **34 處在本站**、「高基數」9 處（cloud-infra ＋ system-design）——本站已經在用這套詞彙講事情，而 portal 的 Charity Majors／Liz Fong-Jones **0 本**，整個可觀測性學派沒有原典；無繁中 |
| 5 | **Systems Performance** | Brendan Gregg |  | 2020 | cloud-infra(8) | cloud-infra 的第二本；「效能」是全星系散得最開的工程概念之一——276 處／133 檔／**跨 29 站**（system-design 43、drucker 34、data-systems 29、business-strategy 22），而 portal 的 Brendan Gregg **0 本**；站內「USE 方法」只有 1 處孤證，講了 276 次效能卻沒有一本系統性的量測方法論；厚，無繁中 |
| 6 | **Streaming Systems** | Tyler Akidau、Slava Chernyak & Reuven Lax |  | 2018 | data-systems(7) | data-systems 站 owned 11／wanted 8（缺口 42.1%，全星系第二高），這輪只排一本當起手：「串流」全星系 54 處／26 檔／跨 11 站（system-design 22、data-systems 20）、「事件溯源」32 處（data-systems 22、system-design 10）、watermark 9 處全在本站——**兩個站在互相引用同一組概念卻共用不到一本原典**；portal 這條線只有 Kleppmann 的 `designing-data-intensive-applications` 一本撐著，Akidau、Stonebraker／Hellerstein、Karwin、Stopford、Reis/Housley、Greg Young **全部 0 本**；厚，無繁中 |
| 7 | **The Web Application Hacker's Handbook** | Dafydd Stuttard & Marcus Pinto |  | 2007 | security(5) | security 站 owned 8／wanted 6——**這六本收齊就歸零**，缺口 42.9% 是全星系最高，也是唯一整站排進來的；這本領頭是準則③：站主在該筆 `note` 自註「本站 Web 這條線最大的原典缺口」。站內證據對得上——XSS 5 處、SQL 10 處、OWASP 只有 1 處、「滲透測試」1 處，Web 攻防講到了卻沒有出處；portal 的 Stuttard **0 本**，搜 penetration 也是 0；厚 |
| 8 | **Threat Modeling: Designing for Security** | Adam Shostack |  | 2014 | security(5) | security 的第二本；「威脅建模」全星系 4 處／3 檔**全在本站**、STRIDE 只有 1 處孤證；portal 的 Shostack **0 本**——站上 Anderson《Security Engineering》講的是「對手是誰」，「怎麼系統性地問哪裡會被打」這條線沒有出處；薄，排這批前面 |
| 9 | **The Tangled Web** | Michal Zalewski |  | 2011 | security(5) | security 的第三本；「同源政策」3 處、「瀏覽器安全」1 處，都只在本站；portal 的 Zalewski **0 本**，而瀏覽器那一側已經有 `browser-hackers-handbook`（攻擊面）——**同源政策為何長成這樣**的歷史考據不在 |
| 10 | **Cryptography Engineering** | Niels Ferguson, Bruce Schneier & Tadayoshi Kohno |  | 2010 | security(5) | security 的第四本；「密碼學」全星系 19 處／7 檔／跨 3 站（security 17、data-systems 1、wujun 1），portal 搜 cryptograph 只有 2 本（serious-cryptography、security-engineering），**Schneier 0 本**——把密碼學當工程紀律而非數學的那半不在 |
| 11 | **The Shellcoder's Handbook** | Chris Anley, John Heasman, Felix Lindner & Gerardo Richarte |  | 2004 | security(5) | security 的第五本；「緩衝區溢位」站內 2 處；portal 的 Anley **0 本**，記憶體漏洞這條線目前只有 `hacking-art-of-exploitation`（Erickson 講原理），各平台實務那半沒有；厚 |
| 12 | **Practical Malware Analysis** | Michael Sikorski & Andrew Honig |  | 2012 | security(5) | security 的第六本；「惡意程式」全星系只有 2 處／2 檔**且都在本站**、security 站內「逆向工程」0 處；portal 搜 malware **0 本**——防守方讀攻擊產物這條線在星系裡完全空白；厚，排這批最後 |
| 13 | **Boundaries with Kids** | Henry Cloud & John Townsend | 為孩子立界線 | 1998 | cloud(4) | cloud 站 owned 8／wanted 5——**這五本收齊就歸零**；選這站整批收的理由：「界線」是**全星系散布最廣的概念之一**，461 處／146 檔／**跨 48 站**（cloud 180、relationships 89、leadership 25、wellness 15），而 portal 的 Cloud 書櫃 8 本全是應用篇（婚姻、約會、領導、結束）。這本補教養那一側——relationships 站「教養」12 處、「界線」89 處，兩條線在那裡交會卻沒有這本；有繁中《為孩子立界線》 |
| 14 | **Safe People** | Henry Cloud & John Townsend | 安全的人 | 1995 | cloud(4) | cloud 的第二本；關係篩選那一側——「如何辨認並成為值得靠近的人」，站內「安全的人」只有 2 處；有繁中《安全的人》 |
| 15 | **How People Grow** | Henry Cloud & John Townsend | 成長神學 | 2001 | cloud(4) | cloud 的第三本，**這批最該收的一本**：整套界線思想的神學基座（恩典—真理—時間）。站內「恩典」65 處、「真理」66 處都在用這組概念，而「成長神學」只有 **1 處孤證**——講了 131 次的東西沒有源頭；有繁中《成長神學》 |
| 16 | **Integrity: The Courage to Meet the Demands of Reality** | Henry Cloud | Integrity | 2006 | cloud(4) | cloud 的第四本；品格六面向——「品格」全星系 286 處／107 檔／跨 34 站（covey 72、growth 28、leadership 24），cloud 站內只有 6 處，能力之外的人格結構這條線在本站幾乎空白；無繁中 |
| 17 | **Trust: Knowing When to Give It, When to Withhold It...** | Henry Cloud | Trust | 2023 | cloud(4) | cloud 的第五本，2023 年的最新主著；站內「信任」只有 6 處，而全星系 1176 處裡 covey 一站就佔 356——**信任這條線目前是柯維的版本**，界線思想的當代續篇不在；厚，無繁中，排這批最後 |
| 18 | **NICNT** | NICNT 系列（各卷作者不同：Moo《Romans》、Fee《1 Corinthians》…） | ／NICOT 系列代表卷 |  | biblical-studies(8) | 準則③：站主在該筆 `note` 自註「學術註釋的系列級缺口」。biblical-studies 站 owned 69 本，背景註釋（IVP 新約背景、校園舊約背景）、釋經學手冊、聖經神學都齊了，**逐節的學術註釋一本都沒有**；站內「註釋」22 處、「註釋書」5 處在講它，而「羅馬書」全星系 34 處／14 檔／跨 4 站（stott 23、theology 8）——起手就買 Moo 的《Romans》那一卷，別想一次收整套；厚，無繁中 |
| 19 | **Good Habits, Bad Habits** | Wendy Wood |  | 2019 | habits(5) | habits 站 owned 38／wanted 6，按準則④進榜：「習慣」全星系 827 處／346 檔／**跨 56 站**（habits 189、covey 116、career 43、leadership 43），而 portal 的習慣書櫃是通俗三本（atomic-habits、power-of-habit、tiny-habits），**Wendy Wood 0 本**；站內「習慣迴路」19 處全是 Duhigg 那套模型，「習慣科學」只有 1 處孤證——情境與摩擦力的學院派證據沒有出處；無繁中 |
| 20 | **Why Zebras Don't Get Ulcers** | Robert M. Sapolsky | 為什麼斑馬不會得胃潰瘍 | 1994 | wellness(5) | wellness 站 owned 27／wanted 6，同樣按準則④：「壓力」全星系 587 處／248 檔／**跨 56 站**（navarro 79、life-meaning 74、wellness 57、thinking 28）——散得極開，而 portal 的 Sapolsky 只有 `behave`（行為的起源），壓力生理學那本不在；「皮質醇」全星系只有 4 處／4 站，講了 587 次的東西幾乎沒有機制層的出處；厚，有繁中《為什麼斑馬不會得胃潰瘍》 |

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
| `owned` | **已收錄**——書已經做成 `nplus.wiki/<slug>/` 的書站 | 必須有 `slug`；首頁書架的封面列就是取這批，概念頁的 `furtherReading.anchor` 也是連到這裡 | 1802 筆（去重 1320 本） |
| `wanted` | **待收錄**——想收、還沒有 | 買得到，只是還沒買／還沒做站 | **98 筆（去重 98 本）** |
| `unavailable` | **暫無來源**——想收但收不到 | 絕版、無中譯、或只有機構授權（如 Scrum Guide、Vanguard 內部傳記） | 85 筆 |
| `skipped` | **刻意略過**——不打算收 | 內容重複、練習冊、合輯、不合站主軸；`note` 欄寫明為何略過 | 82 筆 |

> `owned` 去重後的 1320 是**已建成書站的書**（1802 是含跨站重複的登錄筆數，
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

## 快歸零的站：2 站只差 1–2 本

**TOP20 的準則①就看這一節。** 這些站的書單已經接近收齊，剩下的一兩本收到，整站的採購缺口就歸零——缺書不再是它進 `note-check --enrich` 深化的瓶頸。分母只算 `owned + wanted`（`unavailable` / `skipped` 是永久不可收，不算欠）。

| 站 | 已收 | 還差 | 差哪幾本 |
| --- | ---: | ---: | --- |
| `drucker-note` | 18 | **2** | Managing in the Next Society（Peter F. Drucker）、Drucker on Asia（Peter F. Drucker & 中內功） |
| `gardner-note` | 11 | **2** | The App Generation（Howard Gardner & Katie Davis）、Truth, Beauty, and Goodness Reframed（Howard Gardner） |

## 優先收：0 本有兩個以上的站在等

同一本書被多站列為 `wanted`——收一本補多站的缺口，投資報酬率最高。

| 英文書名 | 作者 | 中譯 | 年 | 等它的站 |
| --- | --- | --- | --- | --- |

## 完整清單（依站，共 98 筆）

### biblical-studies-note — 9 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| The Art of Biblical Narrative | Robert Alter |  | 1981 | Alter——文學讀法的分水嶺之作 |
| Theology of the Old Testament | Walter Brueggemann |  | 1997 | Brueggemann——「見證與爭訟」框架的舊約神學另一極 |
| Old Testament Theology | John Goldingay | 三卷） | 2003 | Goldingay 的敘事進路大部頭（其單卷《聖經神學》已收） |
| Jesus and the Eyewitnesses | Richard Bauckham |  | 2006 | Bauckham——福音書作為目擊者見證 |
| Echoes of Scripture in the Letters of Paul | Richard B. Hays |  | 1989 | Hays——互文性讀保羅的開山之作 |
| Grasping God's Word | J. Scott Duvall & J. Daniel Hays |  | 2001 | Duvall & Hays——釋經步驟化的教科書標準 |
| Kingdom through Covenant | Peter J. Gentry & Stephen J. Wellum |  | 2012 | Gentry & Wellum——以聖約串起正典的系統性嘗試 |
| The Temple and the Church's Mission | G. K. Beale |  | 2004 | Beale——聖殿主線的專論，本站主線概念的深化來源 |
| NICNT | NICNT 系列（各卷作者不同：Moo《Romans》、Fee《1 Corinthians》…） | ／NICOT 系列代表卷 |  | 學術註釋的系列級缺口——如 Moo《Romans》、Fee《1 Corinthians》、Wenham《Genesis》 |

### career-note — 9 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Linchpin | Seth Godin | 關鍵人物 | 2010 | Godin：讓自己成為不可取代的樞紐 |
| The Software Engineer's Guidebook | Gergely Orosz |  | 2023 | Orosz 的工程師職涯全地圖（Tech Resume 已收） |
| Soft Skills: The Software Developer's Life Manual | John Sonmez |  | 2014 | Sonmez：工程師的職涯經營生存手冊 |
| A Whole New Mind | Daniel H. Pink | 未來在等待的人才 | 2005 | Pink：右腦能力在自動化時代增值 |
| The Defining Decade | Meg Jay | 20 世代，你的人生是不是卡住了 | 2012 | Meg Jay：二十世代的不可替代性 |
| The Pathless Path | Paul Millerd |  | 2022 | Millerd：離開預設路徑的工作觀 |
| Working Identity | Herminia Ibarra | 轉行 | 2003 | Ibarra：轉職是先行動再認同，不是先想清楚 |
| The Alliance | Reid Hoffman、Ben Casnocha & Chris Yeh | 聯盟世代 | 2014 | Hoffman：僱傭關係是任期制聯盟 |
| Never Eat Alone | Keith Ferrazzi | 別自己一個人吃飯 | 2005 | Ferrazzi 的人脈經營經典 |

### cloud-infra-note — 9 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| The Unicorn Project | Gene Kim | 獨角獸專案 | 2019 | 鳳凰專案的開發者視角姊妹作 |
| Observability Engineering | Charity Majors、Liz Fong-Jones & George Miranda |  | 2022 | Majors 等；高基數事件與「未知的未知」——可觀測性學派的正典 |
| Practical Monitoring | Mike Julian |  | 2017 | Julian；監控反模式與務實起步 |
| Systems Performance | Brendan Gregg |  | 2020 | Brendan Gregg；USE 方法與效能分析的系統性正典 |
| TCP/IP Illustrated, Volume 1 | W. Richard Stevens |  | 1994 | Stevens；網路協定的經典解剖 |
| UNIX and Linux System Administration Handbook | Evi Nemeth 等 |  | 2017 | Nemeth 等；傳統系統管理的百科全書 |
| Terraform: Up & Running | Yevgeniy Brikman |  | 2017 | Brikman；IaC 落地的實戰標準 |
| Infrastructure as Code | Kief Morris |  | 2016 | Kief Morris；把基礎設施當軟體管理的原則書 |
| The Practice of Cloud System Administration | Thomas A. Limoncelli、Strata R. Chalup & Christina J. Hogan |  | 2014 | Limoncelli；分散式服務維運的教科書 |

### theology-note — 9 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Reformed Dogmatics | Herman Bavinck 巴文克 | 改革宗教理學 | 1906 | 巴文克；改革宗系統神學的巔峰，中譯陸續出版 |
| Christian Theology: An Introduction | Alister E. McGrath 麥葛福 | 基督教神學手冊 | 1994 | 麥葛福；最平衡的入門教科書。portal 的 erickson-christian-theology 是 Millard Erickson 的同名書，不是這一本——下單前對作者 |
| Summa Theologiae | Thomas Aquinas 阿奎那 | 神學大全 | 1274 | 阿奎那；中譯有全集但部頭極鉅 |
| Pensées | Blaise Pascal 巴斯卡 | 思想錄 | 1670 | 巴斯卡；「賭注」與心之理由的源頭 |
| The Reformed Pastor | Richard Baxter 巴克斯特 | 改革宗的牧師 | 1656 | 巴克斯特；清教徒牧養的正典 |
| Lectures to My Students | Charles H. Spurgeon 司布真 | 給我學生的信（講道講座） | 1875 | 司布真的牧職講義 |
| The Contemplative Pastor | Eugene H. Peterson 畢德生 | 返璞歸真的牧養藝術 | 1989 | 畢德生；反職業化牧養的當代聲音 |
| The City of God | Augustine 奧古斯丁 | 上帝之城 | 426 | 奧古斯丁；歷史神學與政治神學的奠基 |
| On the Incarnation | Athanasius 亞他那修 | 論道成肉身 | 318 | 亞他那修；教父基督論最佳入門 |

### data-systems-note — 8 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Readings in Database Systems | Peter Bailis、Joseph M. Hellerstein & Michael Stonebraker 編 |  | 2015 | Red Book 第五版；Stonebraker 選編的論文導讀，線上免費 |
| SQL Antipatterns | Bill Karwin |  | 2010 | Karwin；schema 與查詢的反模式目錄 |
| Seven Databases in Seven Weeks | Eric Redmond & Jim R. Wilson |  | 2012 | 以七種資料庫走一遍資料模型光譜 |
| Streaming Systems | Tyler Akidau、Slava Chernyak & Reuven Lax |  | 2018 | Akidau 等；watermark／trigger——串流語意的正典 |
| Kafka: The Definitive Guide | Gwen Shapira 等（O'Reilly） |  | 2017 | log 為中心的資料骨幹，事實標準的官方指南 |
| Designing Event-Driven Systems | Ben Stopford |  | 2018 | Stopford；以 Kafka 為底的事件驅動服務，O'Reilly 免費電子書 |
| Fundamentals of Data Engineering | Joe Reis & Matt Housley |  | 2022 | Reis & Housley；資料工程生命週期的現代全景 |
| Versioning in an Event Sourced System | Greg Young |  | 2017 | Greg Young；事件溯源在演進期的實務難題 |

### investing-note — 7 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Pioneering Portfolio Management | David F. Swensen |  | 2000 | Swensen 機構版正典——耶魯模式本尊 |
| 100 Baggers | Christopher W. Mayer |  | 2015 | Mayer 對百倍股的系統研究(承 Phelps 1972) |
| Trend Following | Michael W. Covel |  | 2004 | Covel 本傳(目前只收錄 Masters Vol.2 訪談集) |
| The Alchemy of Finance | George Soros 索羅斯 | 金融煉金術 | 1987 | 索羅斯的反身性理論 |
| Technical Analysis of the Financial Markets | John J. Murphy |  | 1999 | Murphy;技術分析的教科書標準(Schwager 入門冊已收) |
| Valuation (McKinsey) | Tim Koller、Marc Goedhart & David Wessels（McKinsey） |  | 1990 | Koller 等;企業估值的業界標準 |
| Financial Shenanigans | Howard M. Schilit | 財報詭計 | 1993 | Schilit;財報偵錯的防守面 |

### marketing-note — 7 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Obviously Awesome | April Dunford | 顯而易見的傑出 | 2019 | Dunford；B2B／產品定位的現代操作手冊 |
| How Brands Grow | Byron Sharp | 品牌如何成長 | 2010 | Byron Sharp；實證行銷科學，對忠誠度神話的反擊 |
| Purple Cow | Seth Godin | 紫牛 | 2003 | Godin；卓越到值得談論才是行銷 |
| Contagious | Jonah Berger | 瘋潮行銷 | 2013 | Berger；STEPPS——內容為何被瘋傳 |
| Permission Marketing | Seth Godin | 許可行銷 | 1999 | Godin；從打擾式到許可式——email／訂閱通路的思想起點 |
| Scientific Advertising | Claude C. Hopkins | 科學的廣告 | 1923 | Hopkins；直效廣告與測試思維的百年原點 |
| Marketing Management | Philip Kotler & Kevin Lane Keller | 行銷管理 | 1967 | Kotler；學院派教科書標準，補理論骨架用 |

### personal-finance-note — 7 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Early Retirement Extreme | Jacob Lund Fisker |  | 2010 | Fisker；FIRE 數學與哲學的硬核根基 |
| Quit Like a Millionaire | Kristy Shen & Bryce Leung |  | 2019 | Kristy Shen；可複製的中產 FIRE 實證 |
| Die with Zero | Bill Perkins | 別把你的錢留到死 | 2020 | Perkins；反過度累積——花錢也要最佳化 |
| The Millionaire Mind | Thomas J. Stanley |  | 2000 | Stanley 續作——富人的決策與性格研究 |
| The Total Money Makeover | Dave Ramsey |  | 2003 | Ramsey 主著；Baby Steps 無債務體系的原典 |
| The Automatic Millionaire | David Bach | 讓錢為你工作的自動理財法 | 2004 | Bach；把儲蓄自動化的經典操作手冊 |
| The Wealthy Barber | David Chilton |  | 1989 | Chilton；北美國民理財入門的敘事體始祖 |

### habits-note — 6 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Good Habits, Bad Habits | Wendy Wood |  | 2019 | Wendy Wood：習慣科學的學院派正典——情境與摩擦力 |
| Stolen Focus | Johann Hari | 誰偷走了你的專注力？ | 2022 | Hari：專注力崩壞的系統性成因 |
| Daily Rituals: How Artists Work | Mason Currey |  | 2013 | Currey：161 位創作者的作息田野調查 |
| Rest | Alex Soojung-Kim Pang |  | 2016 | Pang：刻意休息是深度工作的另一半 |
| Discipline Is Destiny | Ryan Holiday |  | 2022 | Holiday：斯多噶四樞德的自律卷 |
| Willpower: Rediscovering the Greatest Human Strength | Roy F. Baumeister & John Tierney | Willpower 增強你的意志力 | 2011 | Baumeister：意志力科學的正典（自我耗損後續有爭議，仍值得收） |

### science-note — 6 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Cosmos | Carl Sagan | 宇宙 | 1980 | Sagan：科學普及史上最有影響力的一本 |
| Surely You're Joking, Mr. Feynman! | Richard P. Feynman | 別鬧了，費曼先生 | 1985 | 科學家性格與「絕不自欺」的第一手示範 |
| Brain Rules | John Medina | 大腦當家 | 2008 | Medina：認知神經科學的實用十二則 |
| The Blind Watchmaker | Richard Dawkins | 盲眼鐘錶匠 | 1986 | Dawkins：累積選擇如何無心智地造出設計 |
| The Demon-Haunted World | Carl Sagan | 魔鬼盤據的世界 | 1995 | Sagan：懷疑論工具箱（baloney detection kit） |
| Conjectures and Refutations | Karl Popper | 猜想與反駁 | 1963 | Popper：可否證性原則的原典 |

### security-note — 6 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Threat Modeling: Designing for Security | Adam Shostack |  | 2014 | 威脅建模的方法書（STRIDE／攻擊樹）——Anderson 講「對手是誰」，這本講「怎麼系統性地問」 |
| The Shellcoder's Handbook | Chris Anley, John Heasman, Felix Lindner & Gerardo Richarte |  | 2004 | 記憶體漏洞利用的另一本正典，與 Erickson 互補（他講原理，這本講各平台實務） |
| Practical Malware Analysis | Michael Sikorski & Andrew Honig |  | 2012 | 防守方讀攻擊產物的標準教材——本站目前完全沒有惡意程式分析這條線 |
| Cryptography Engineering | Niels Ferguson, Bruce Schneier & Tadayoshi Kohno |  | 2010 | 把密碼學當工程紀律而非數學——與 Serious Cryptography 是同一格的兩種寫法 |
| The Web Application Hacker's Handbook | Dafydd Stuttard & Marcus Pinto |  | 2007 | Web 滲透測試的百科全書——本站 Web 這條線最大的原典缺口 |
| The Tangled Web | Michal Zalewski |  | 2011 | Zalewski——瀏覽器安全模型為何長成這副樣子的歷史考據，同源政策的來龍去脈 |

### wellness-note — 6 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Spark: The Revolutionary New Science of Exercise and the Brain | John J. Ratey | Spark 運動改造大腦 | 2008 | Ratey：運動對大腦與情緒的實證經典 |
| In Defense of Food | Michael Pollan | 食物無罪 | 2008 | Pollan：「吃食物，別太多，以植物為主」 |
| How Not to Die | Michael Greger | 食療聖經 | 2015 | Greger：疾病別的飲食實證彙整 |
| Why Zebras Don't Get Ulcers | Robert M. Sapolsky | 為什麼斑馬不會得胃潰瘍 | 1994 | Sapolsky：壓力生理學的經典 |
| Feeling Good: The New Mood Therapy | David D. Burns |  | 1980 | Burns：認知行為治療（CBT）自助經典 |
| Flourish | Martin E. P. Seligman | 邁向圓滿 | 2011 | Seligman：PERMA 幸福模型 |

### cloud-note — 5 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Boundaries with Kids | Henry Cloud & John Townsend | 為孩子立界線 | 1998 | 把界線變成教養框架——讓孩子為自己的行為承擔後果 |
| How People Grow | Henry Cloud & John Townsend | 成長神學 | 2001 | 與 Townsend 合寫的成長框架神學基座——恩典、真理、時間的系統陳述 |
| Safe People | Henry Cloud & John Townsend | 安全的人 | 1995 | 如何辨認（並成為）值得靠近的人——關係線的實用篇 |
| Integrity: The Courage to Meet the Demands of Reality | Henry Cloud | Integrity | 2006 | 品格六面向——能力之外，讓成果留下來的是人格結構 |
| Trust: Knowing When to Give It, When to Withhold It... | Henry Cloud | Trust | 2023 | 最新主著：信任的五要素與重建之路，界線思想的續篇 |

### drucker-note — 2 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Drucker on Asia | Peter F. Drucker & 中內功 | 杜拉克看亞洲 | 1997 | 與中內功的對談錄；杜拉克與日本經營的互動 |
| Managing in the Next Society | Peter F. Drucker | 下一個社會 | 2002 | 最後的社會預言：少子高齡化、資訊革命的下一步 |

### gardner-note — 2 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Truth, Beauty, and Goodness Reframed | Howard Gardner | 重新定義真善美 | 2011 | 數位時代如何守住三大古典價值；《學習的紀律》的續章 |
| The App Generation | Howard Gardner & Katie Davis | 破解 APP 世代 | 2013 | 與 Katie Davis 合著；app 心態如何形塑青少年的認同、親密與想像 |

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
