# 待收書單（bibliography `wanted` 全星系匯出）

**這份是什麼**：各 note 站 `src/data/bibliography.ts` 裡標成 `status: "wanted"` 的書，
全部匯出成一張採購清單。書名以**英文原名**為主，中譯附在後面，並附**作者**——
同名不同書會讓人買錯（portal 上的 `servant-leadership` 是 Larry W. Boone 的教科書，
不是 Greenleaf 1977 原典），下單前請對作者。由
`notes-core/tools/export-wanted.py` 生成，**不要手改**——改各站的 bibliography 再重跑。

**已收錄比對的資料源**：GitHub 現況（`gh repo list` nplus-father／Andrewnplus，1795 個 repo）。

## 先收這 20 本

整份 138 筆太長，這是從裡面挑出來的採購順序，也是建議的消化順序（薄的、起手容易的排前面）。**這節是全檔唯一的人工區塊**——要改請編 `export-wanted.py` 的 `TOP20`，不要改這裡。挑選準則依序：**①歸零槓桿——優先收「還差 1–2 本就收齊」的站所缺的書**（見下面「快歸零的站」那節，腳本自動算；站書單一歸零，缺書就不再是它進 `note-check --enrich` 深化的瓶頸） ②多站共等，收一本補多站 ③站主自己在 `note` 裡標了「最大／頭號缺口」 ④portal 驗證的 anchor 深度——nplus.wiki 上已經建成幾本回指它的書站（同作者書櫃、同一條線的衍生書），書櫃愈深、原典愈缺就排愈前面（見 [SOURCING-DEBT.md](./SOURCING-DEBT.md)） ⑤同等重要時，薄的、有繁中在版的排前面。

「站」欄的 `(n)` ＝**收了這本之後該站還剩幾本**；`(0)` 就是這一本收了該站即歸零。

「為何排這裡」的 portal 數字都是實查出來的（作者書櫃本數、同一條線的衍生書數、各站概念頁引用處數）；`/note-wanted` 每次重挑會一併重查。

| # | 英文書名 | 作者 | 中譯 | 年 | 站 | 為何排這裡 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **The News: A User's Manual** | Alain de Botton | 新聞的騷動 | 2014 | de-botton(0) | de-botton 站 owned 12／wanted 1——**收了就歸零**；portal 的 de Botton 12 本已經把「慰藉方法」套在建築、工作、藝術、宗教、地位上（這輪剛回填 art-as-therapy、pleasures-and-sorrows-of-work、school-of-life 三本），**獨缺套在新聞上的這本**；站內「新聞」只有 2 處——書櫃裡沒有一本處理媒體；薄，有繁中《新聞的騷動》 |
| 2 | **How to Be a High School Superstar** | Cal Newport |  | 2010 | newport(0) | newport 站 owned 8／wanted 1——**收了就歸零**；這輪 portal 補建了正名的 `how-to-win-at-college`，Newport 學生三部曲只剩這本真的沒有（同名的 `how-to-be-a-high-school-superstar` repo 內容仍是 How to Win at College，見 SOURCING-DEBT.md——**下單前別被 portal 上那個 slug 騙了**）；portal 的 Newport 8 本；「鬆弛悖論」站內 1 處孤證；薄，有繁中《深度學習力》 |
| 3 | **Playing to Win** | A. G. Lafley & Roger L. Martin |  | 2013 | business-strategy(0) | business-strategy 站 owned 49／wanted 1——**收了就歸零**，而這是全星系第三深的主題站；portal 的 Lafley 與 Roger Martin **各 0 本**（description 裡 22 個「Martin」全是別人：Martin Fowler、Martin Kleppmann…）；站內「策略級聯」1 處孤證、「五問」全星系 13 處但 business-strategy 只佔 1 處——P&G 那套五問框架整套沒有出處；有繁中《策略就是要贏》 |
| 4 | **Managing** | Henry Mintzberg |  | 2009 | management(0) | management 站 owned 46／wanted 1——**收了就歸零**（上輪排第 2，這輪其餘全回填完，它是最後一本）；portal 的 Mintzberg 只有 `simply-managing`，那是他 2013 年**自己把這本濃縮改寫**的版本，2009 年的原典不在——比對時特地讀了 README 確認是兩本書；站內「經理人角色」1 處孤證，而「知識工作者」全星系 94 處／34 檔／跨 7 站（drucker 34、management 23、business-strategy 18）——管理者實際在做什麼這條線目前全靠 Drucker 轉述 |
| 5 | **Hold Me Tight** | Sue Johnson | 抱緊我 | 2008 | relationships(0) | relationships 站 owned 45／wanted 1——**收了就歸零**；portal 的 Sue Johnson **0 本**；「依附」全星系 62 處／38 檔／**跨 22 站**（thinking 10、de-botton 8、relationships 8）——散得極開卻沒有情緒取向治療（EFT）的原典，站內「情緒取向」只有 1 處孤證；有繁中《抱緊我》 |
| 6 | **Into the Woods** | John Yorke |  | 2013 | writing(0) | writing 站 owned 31／wanted 1——**收了就歸零**；portal 的 John Yorke **0 本**；writing 站這輪剛回填 4 本（save-the-cat、artists-way、draft-no-4、writing-tools），結構理論卻只剩 Snyder 的十五節拍一家之言——「故事結構」全星系 22 處／13 檔／跨 5 站，writing 站內 11 處，而把三幕／五幕各家收攏成一套的這本不在；無繁中 |
| 7 | **（信息傳）** | 吳軍 |  | 2020 | wujun(0) | wujun 站 owned 17／wanted 1——**收了就歸零**；portal 的吳軍 17 本是**全星系最深的華文作者書櫃**，獨缺這本；站內「資訊論」3 處、「香農」1 處——資訊論當方法論這條線目前只有轉述；**別買錯**：portal 的 `wujun-information-theory-40` 是《信息論 40 講》，不是這本（已對過 README）；無繁中版，要買簡中 |
| 8 | **The Dark Side of Valuation** | Aswath Damodaran | 估值的黑暗面 | 2001 | damodaran(0) | damodaran 站 owned 4／wanted 1——**收了就歸零**（Investment Philosophies 這輪查出早有書站、已回填）；portal 的 Damodaran 4 本；「估值」全星系 236 處／40 檔／跨 10 站，其中 damodaran 站內 178 處——**全星系概念密度最高的主題**，而這本處理的年輕、高成長與困境公司，站內「困境」「高成長」各只有 3 處；厚，無繁中 |
| 9 | **Zen Buddhism and Psychoanalysis** | Erich Fromm & 鈴木大拙 | 禪與心理分析 | 1960 | fromm(0) | fromm 站 owned 15／wanted 1——收了就歸零，**但這筆待 Andrew 裁決**：portal 2026-08-12 建了 `psychoanalysis-and-zen-buddhism`（《精神分析與禪佛教》，六章全是 Fromm 那半的內容），站上想收的是 1960 年 Fromm＋鈴木大拙＋De Martino 的**合集**《禪與心理分析》——若判定 Fromm 那半就算收了，這格空出來；portal 的 Fromm 16 本；站內「存在樣式」3 處；薄 |
| 10 | **Globalization and Its Discontents** | Joseph E. Stiglitz | 全球化的許諾與失落 | 2002 | economics(0) | economics 站 owned 49／wanted 1——收了就歸零，**同樣待裁決**（上輪就掛著）：portal 的 `globalization-and-its-discontents-revisited` 是 2017 增訂版，報告的「疑似漏報」列它 80% 相似；「全球化」全星系 39 處／12 檔／跨 10 站（economics 29），體制內人批判 IMF／世銀這條線只有增訂版的視角；厚，有繁中《全球化的許諾與失落》 |
| 11 | **Scripture and the Authority of God** | N. T. Wright |  | 2011 | nt-wright(3) | nt-wright 站 owned 11／wanted 4——**這四本收齊就歸零**，是差 1 本那批之外最接近終點的站；portal 的 N. T. Wright 11 本（含這輪回填的 simply-jesus）；這本排第一是因為它是**方法論的出處**：五幕劇詮釋框架全星系都在用（biblical-studies 站「五幕」23 處），而「聖經權柄」只有 1 處孤證；薄 |
| 12 | **Justification: God's Plan and Paul's Vision** | N. T. Wright |  | 2009 | nt-wright(3) | nt-wright 的第二本；「稱義」全星系 69 處／21 檔／跨 7 站，其中 **stott 41 處、theology 10、keller 8，賴特自己的站只有 4 處**——引用最多的站都不是他的，而他與 Piper 那場論戰的正面陳述不在 |
| 13 | **How God Became King** | N. T. Wright |  | 2012 | nt-wright(3) | nt-wright 的第三本；福音書「被遺忘的中段」——「神的國」全星系 31 處／14 檔／跨 5 站（theology 16、nt-wright 6）、「天國」117 處（willard 71），兩個詞都在用，而把四福音讀成「上帝作王的故事」的這本不在 |
| 14 | **The Day the Revolution Began** | N. T. Wright |  | 2016 | nt-wright(3) | nt-wright 的第四本；「十架」全星系 162 處／42 檔／跨 7 站（stott 57、biblical-studies 36、keller 29、nt-wright 15）——**十架論在星系裡幾乎都是斯托得的版本**，賴特的新出埃及重述沒有出處；厚，排這批最後 |
| 15 | **Boundaries with Kids** | Henry Cloud & John Townsend | 為孩子立界線 | 1998 | cloud(4) | cloud 站 owned 8／wanted 5——**這五本收齊就歸零**；選這站整批收的理由：「界線」是**全星系散布最廣的概念**，461 處／146 檔／**跨 48 站**（cloud 180、relationships 89、leadership 25、wellness 15），而 portal 的 Cloud 書櫃 8 本全是應用篇（婚姻、約會、領導、結束）。這本補教養那一側——relationships 站「教養」12 處、「界線」89 處，兩條線在那裡交會卻沒有這本；有繁中《為孩子立界線》 |
| 16 | **Safe People** | Henry Cloud & John Townsend | 安全的人 | 1995 | cloud(4) | cloud 的第二本；關係篩選那一側——「如何辨認並成為值得靠近的人」，站內「安全的人」只有 2 處；有繁中《安全的人》 |
| 17 | **How People Grow** | Henry Cloud & John Townsend | 成長神學 | 2001 | cloud(4) | cloud 的第三本，**這批最該收的一本**：整套界線思想的神學基座（恩典—真理—時間）。站內「恩典」65 處、「真理」66 處都在用這組概念，而「成長神學」只有 **1 處孤證**——講了 131 次的東西沒有源頭；有繁中《成長神學》 |
| 18 | **Integrity: The Courage to Meet the Demands of Reality** | Henry Cloud | Integrity | 2006 | cloud(4) | cloud 的第四本；品格六面向——「品格」全星系 286 處／107 檔／跨 34 站（covey 72、growth 28、leadership 24），cloud 站內只有 6 處，能力之外的人格結構這條線在本站幾乎空白；無繁中 |
| 19 | **Trust: Knowing When to Give It, When to Withhold It...** | Henry Cloud | Trust | 2023 | cloud(4) | cloud 的第五本，2023 年的最新主著；站內「信任」只有 6 處，而全星系 1176 處裡 covey 一站就佔 356——**信任這條線目前是柯維的版本**，界線思想的當代續篇不在；厚，無繁中，排這批最後 |
| 20 | **The Web Application Hacker's Handbook** | Dafydd Stuttard & Marcus Pinto |  | 2007 | security(5) | 唯一按**準則③**進榜的一格：security 站主在該筆 `note` 自註「本站 Web 這條線最大的原典缺口」。站內證據對得上——XSS 5 處、SQL 10 處、OWASP 只有 1 處，Web 攻防講到了卻沒有出處；security 站 owned 8／wanted 6，收了降到差 5，離歸零還遠，所以只給 1 格；厚 |

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
| `owned` | **已收錄**——書已經做成 `nplus.wiki/<slug>/` 的書站 | 必須有 `slug`；首頁書架的封面列就是取這批，概念頁的 `furtherReading.anchor` 也是連到這裡 | 1788 筆（去重 1306 本） |
| `wanted` | **待收錄**——想收、還沒有 | 買得到，只是還沒買／還沒做站 | **138 筆（去重 138 本）** |
| `unavailable` | **暫無來源**——想收但收不到 | 絕版、無中譯、或只有機構授權（如 Scrum Guide、Vanguard 內部傳記） | 59 筆 |
| `skipped` | **刻意略過**——不打算收 | 內容重複、練習冊、合輯、不合站主軸；`note` 欄寫明為何略過 | 82 筆 |

> `owned` 去重後的 1306 是**已建成書站的書**（1788 是含跨站重複的登錄筆數，
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

## 疑似漏報：3 本可能其實已經有 repo

書名**沒有**正規化後完全相同，但 portal 上有 repo 長得很像——改過書名（英美版不同、中譯轉寫）的書會落在這裡。**這節是提名，不是判決**：確認是同一本就寫進 `export-wanted.py` 的 `ALIASES`，下一輪它就走精確路徑並自動掉進「先扣掉」；確認是續集或同系列的不同書就不用管，下輪還會再問一次。

門檻：兩邊書名的**雙向 Jaccard ≥70%**（詞相等的判準放寬到共同前綴 5 字元，才抓得到 `Forgiving` ↔ `Forgiveness` 這種詞形差異），且**作者沒有互相否決**。用雙向而不是單向覆蓋率，是因為單向會被系列卷洗版——`… on Leadership` 的詞有 75% 出現在 `… on Communication` 裡，但那是不同的一本。作者不符的已經在上一節擋掉；`NAME_COLLISIONS` 裁決過的不再提名。

| 想收的書 | 作者 | 疑似 repo | 相似度 | repo 上的書名 | 登記在 |
| --- | --- | --- | ---: | --- | --- |
| Zen Buddhism and Psychoanalysis | Erich Fromm & 鈴木大拙 | `psychoanalysis-and-zen-buddhism` | 100% | Psychoanalysis and Zen Buddhism | fromm-note |
| Globalization and Its Discontents | Joseph E. Stiglitz | `globalization-and-its-discontents-revisited` | 80% | Globalization and Its Discontents Revisited | economics-note |
| HBR's 10 Must Reads: The Essentials | Harvard Business Review | `hbr-s-10-must-reads-on-communication` | 75% | HBR's 10 Must Reads on Communication | hbr-note |

## 快歸零的站：10 站只差 1–2 本

**TOP20 的準則①就看這一節。** 這些站的書單已經接近收齊，剩下的一兩本收到，整站的採購缺口就歸零——缺書不再是它進 `note-check --enrich` 深化的瓶頸。分母只算 `owned + wanted`（`unavailable` / `skipped` 是永久不可收，不算欠）。

| 站 | 已收 | 還差 | 差哪幾本 |
| --- | ---: | ---: | --- |
| `business-strategy-note` | 49 | **1** | Playing to Win（A. G. Lafley & Roger L. Martin） |
| `economics-note` | 49 | **1** | Globalization and Its Discontents（Joseph E. Stiglitz） |
| `management-note` | 46 | **1** | Managing（Henry Mintzberg） |
| `relationships-note` | 45 | **1** | Hold Me Tight（Sue Johnson） |
| `writing-note` | 31 | **1** | Into the Woods（John Yorke） |
| `wujun-note` | 17 | **1** | 信息傳（吳軍） |
| `fromm-note` | 15 | **1** | Zen Buddhism and Psychoanalysis（Erich Fromm & 鈴木大拙） |
| `de-botton-note` | 12 | **1** | The News: A User's Manual（Alain de Botton） |
| `newport-note` | 8 | **1** | How to Be a High School Superstar（Cal Newport） |
| `damodaran-note` | 4 | **1** | The Dark Side of Valuation（Aswath Damodaran） |

## 優先收：0 本有兩個以上的站在等

同一本書被多站列為 `wanted`——收一本補多站的缺口，投資報酬率最高。

| 英文書名 | 作者 | 中譯 | 年 | 等它的站 |
| --- | --- | --- | --- | --- |

## 完整清單（依站，共 138 筆）

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

### drucker-note — 5 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| The Future of Industrial Man | Peter F. Drucker | 工業人的未來 | 1942 | 提出「合法性」與「地位與功能」問題，通往《企業的概念》 |
| Managing in Turbulent Times | Peter F. Drucker | 動盪時代的管理 | 1980 | 不確定時代的經營綱領，與當下高度共鳴 |
| Managing the Non-Profit Organization | Peter F. Drucker | 使命與領導：非營利組織的管理 | 1990 | 杜拉克晚年最重視的部門——社會部門 |
| Drucker on Asia | Peter F. Drucker & 中內功 | 杜拉克看亞洲 | 1997 | 與中內功的對談錄；杜拉克與日本經營的互動 |
| Managing in the Next Society | Peter F. Drucker | 下一個社會 | 2002 | 最後的社會預言：少子高齡化、資訊革命的下一步 |

### gardner-note — 5 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Art, Mind, and Brain: A Cognitive Approach to Creativity | Howard Gardner | 藝術、心智與大腦 | 1982 | MI 前夜的藝術認知研究；Project Zero 時期的成果 |
| The Mind's New Science: A History of the Cognitive Revolution | Howard Gardner | 心智的新科學 | 1985 | 認知革命的權威史；理解加德納學術座標的背景書 |
| Extraordinary Minds | Howard Gardner | 非凡心智 | 1997 | 大師（Mozart）、創造者（Freud）、內省者（Woolf）、影響者（Gandhi）四種非凡 |
| Truth, Beauty, and Goodness Reframed | Howard Gardner | 重新定義真善美 | 2011 | 數位時代如何守住三大古典價值；《學習的紀律》的續章 |
| The App Generation | Howard Gardner & Katie Davis | 破解 APP 世代 | 2013 | 與 Katie Davis 合著；app 心態如何形塑青少年的認同、親密與想像 |

### hbr-note — 5 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| HBR's 10 Must Reads: The Essentials | Harvard Business Review |  | 2010 | 主系列的總綱卷——Porter/Drucker/Kotter/Christensen 名文合輯 |
| HBR's 10 Must Reads on Leadership | Harvard Business Review |  | 2011 | 主系列領導卷——Goleman〈What Makes a Leader?〉、Kotter 名文 |
| HBR's 10 Must Reads on Managing People | Harvard Business Review |  | 2011 | 主系列帶人卷——One Minute Manager 級的經典選文 |
| HBR's 10 Must Reads on Strategy | Harvard Business Review |  | 2011 | 主系列策略卷——Porter〈What Is Strategy?〉所在 |
| HBR's 10 Must Reads on Innovation | Harvard Business Review |  | 2013 | 主系列創新卷——Christensen 破壞式創新名文 |

### image-style-note — 5 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| True Style: The History and Principles of Classic Menswear | G. Bruce Boyer | True Style | 2015 | Boyer 晚期集大成——逐單品講歷史與原則 |
| ABC of Men's Fashion | Hardy Amies |  | 1964 | Hardy Amies；英倫剪裁祖師的辭典式小書 |
| The Suit: A Machiavellian Approach to Men's Style | Nicholas Antongiavanni | The Suit | 2006 | Antongiavanni 仿《君主論》體例談西裝——文體奇書 |
| Take Ivy | 石津謙介 企劃／林田昭慶 等 |  | 1965 | 石津謙介企劃；美式 Ivy 風格的攝影聖經 |
| Icons of Men's Style | Josh Sims |  | 2011 | Sims；逐單品的設計史——每件經典從哪來 |

### nouwen-note — 5 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Intimacy | Henri J. M. Nouwen | 親密 | 1969 | 處女作；牧養心理學時期的起點 |
| Out of Solitude | Henri J. M. Nouwen | 始於寧謐處 | 1974 | 獨處與服事的小經典；三篇講章 |
| Clowning in Rome | Henri J. M. Nouwen | 羅馬城的小丑戲 | 1979 | 小丑（邊緣人）作為屬靈生活的隱喻 |
| Compassion | Henri J. M. Nouwen、Donald P. McNeill & Douglas A. Morrison | 慈心憐憫 | 1982 | 與 McNeill、Morrison 合著；憐憫＝一同受苦的神學 |
| Heart Speaks to Heart | Henri J. M. Nouwen | 心應心 | 1989 | 對基督之心的三篇禱文；崩潰後的深水之作 |

### pastoral-psychology-note — 5 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Psychology & Christianity: Five Views | Eric L. Johnson 編 |  | 2010 | Eric Johnson 編；五種觀點同場對話，全站的定位地圖 |
| Suffering and the Heart of God | Diane Langberg |  | 2015 | Diane Langberg；創傷心理學家寫給教會，哀歌類經文的最大回饋 |
| Generation to Generation | Edwin H. Friedman |  | 1985 | Edwin Friedman；家庭系統理論進會眾——創世記家族敘事的透鏡 |
| Forgiveness and Reconciling | Everett L. Worthington Jr. |  | 2003 | Everett Worthington；饒恕實證研究——REACH 模型與兩種饒恕 |
| The Emotionally Healthy Church | Peter Scazzero | 建立高EQ的教會 | 2003 | Pete Scazzero；情緒健康×門徒訓練，華人教會接受度高 |

### nt-wright-note — 4 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Justification: God's Plan and Paul's Vision | N. T. Wright |  | 2009 | 回應 Piper 的稱義論戰之作：稱義是盟約成員身分的宣告 |
| How God Became King | N. T. Wright |  | 2012 | 四福音「被遺忘的中段」：上帝作王的故事，補信經跳過的一塊 |
| The Day the Revolution Began | N. T. Wright |  | 2016 | 十架論的普及重述：赦罪帶來的是新出埃及與革命 |
| Scripture and the Authority of God | N. T. Wright |  | 2011 | 「聖經權柄」＝上帝藉聖經行使的權柄；五幕劇詮釋框架的出處 |

### business-strategy-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Playing to Win | A. G. Lafley & Roger L. Martin |  | 2013 | Lafley & Martin；P&G 的五問策略級聯 |

### damodaran-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| The Dark Side of Valuation | Aswath Damodaran | 估值的黑暗面 | 2001 | 年輕、高成長與困境公司的估值難題——正典外最值得補的一塊 |

### de-botton-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| The News: A User's Manual | Alain de Botton | 新聞的騷動 | 2014 | 資訊焦慮時代的媒體使用手冊——慰藉方法用在新聞上 |

### economics-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Globalization and Its Discontents | Joseph E. Stiglitz | 全球化的許諾與失落 | 2002 | Stiglitz；體制內人對 IMF／世銀的批判 |

### fromm-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Zen Buddhism and Psychoanalysis | Erich Fromm & 鈴木大拙 | 禪與心理分析 | 1960 | 與鈴木大拙合著：東方的資源如何滋養「存在樣式」 |

### management-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Managing | Henry Mintzberg |  | 2009 | Mintzberg 對「管理者實際在做什麼」的實地研究——經理人角色學派正典 |

### newport-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| How to Be a High School Superstar | Cal Newport |  | 2010 | 「鬆弛悖論」：不靠更多課外活動，靠深耕一件事到引人好奇的深度——原誤標在深度學習力的 repo 上，2026-08-06 校正；portal 上同名的 how-to-be-a-high-school-superstar 內容實為《How to Win at College》，作者同樣是 Newport，所以作者比對擋不掉，靠 NAME_COLLISIONS 人工排除 |

### relationships-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Hold Me Tight | Sue Johnson | 抱緊我 | 2008 | Sue Johnson：情緒取向治療（EFT） |

### writing-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Into the Woods | John Yorke |  | 2013 | Yorke 的五幕論，把各家結構理論收攏成一套 |

### wujun-note — 1 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| （信息傳） | 吳軍 | 信息傳 | 2020 | 資訊史詩；香農資訊論如何成為理解未來的方法論（無繁中版） |

## 沒有英文書名的 1 本（華文／日文原著）

這些本來就沒有英文版，照原書名收。

| 原書名 | 作者 | 站 | 為何想收 |
| --- | --- | --- | --- |
| 信息傳 | 吳軍 | wujun-note | 資訊史詩；香農資訊論如何成為理解未來的方法論（無繁中版） |

## 重跑

```bash
notes-core/tools/export-wanted.py
```

收到書、建好書站之後，把該站 bibliography 那筆改成 `status: "owned"` 並補 `slug`，
重跑就會從這裡消失。
