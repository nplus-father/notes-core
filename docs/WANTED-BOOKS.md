# 待收書單（bibliography `wanted` 全星系匯出）

> **生成於 2026-09-26T14:08:05+08:00**｜由 `tools/export-wanted.py` 產生，**不要手改**——改資料源再重跑。

**這份是什麼**：各 note 站 `src/data/bibliography.ts` 裡標成 `status: "wanted"` 的書，
全部匯出成一張採購清單。書名以**英文原名**為主，中譯附在後面，並附**作者**——
同名不同書會讓人買錯（portal 上的 `servant-leadership` 是 Larry W. Boone 的教科書，
不是 Greenleaf 1977 原典），下單前請對作者。由
`notes-core/tools/export-wanted.py` 生成，**不要手改**——改各站的 bibliography 再重跑。

**已收錄比對的資料源**：GitHub 現況（`gh repo list` nplus-father／Andrewnplus，1962 個 repo）。

## 先收這 18 本

整份 46 筆太長，這是從裡面挑出來的採購順序，也是建議的消化順序（薄的、起手容易的排前面）。**這節是全檔唯一的人工區塊**——要改請編 `export-wanted.py` 的 `TOP20`，不要改這裡。挑選準則依序：**①歸零槓桿——優先收「還差 1–2 本就收齊」的站所缺的書**（見下面「快歸零的站」那節，腳本自動算；站書單一歸零，缺書就不再是它進 `note-check --enrich` 深化的瓶頸） ②多站共等，收一本補多站 ③站主自己在 `note` 裡標了「最大／頭號缺口」 ④portal 驗證的 anchor 深度——nplus.wiki 上已經建成幾本回指它的書站（同作者書櫃、同一條線的衍生書），書櫃愈深、原典愈缺就排愈前面（見 [SOURCING-DEBT.md](./SOURCING-DEBT.md)） ⑤同等重要時，薄的、有繁中在版的排前面。

「站」欄的 `(n)` ＝**收了這本之後該站還剩幾本**；`(0)` 就是這一本收了該站即歸零。

「為何排這裡」的 portal 數字都是實查出來的（作者書櫃本數、同一條線的衍生書數、各站概念頁引用處數）；`/note-wanted` 每次重挑會一併重查。

| # | 英文書名 | 作者 | 中譯 | 年 | 站 | 為何排這裡 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **The Art of Statistics** | David Spiegelhalter | 統計的藝術 | 2019 | data-science(38) | 統計思維分類的正典入門；整個站的第一本 |
| 2 | **The Data Detective** | Tim Harford |  | 2020 | data-science(38) | 看數字的十條規則；薄、起手容易 |
| 3 | **The Fearless Organization** | Amy C. Edmondson |  | 2018 | hr(6) | 心理安全感的原典：全星系 7 站 18 頁在談心理安全，架上只有 Edmondson 的 Right Kind of Wrong；hr 站留才分類的 psychological-safety 節點在等它 |
| 4 | **Nine Lies About Work** | Marcus Buckingham & Ashley Goodall |  | 2019 | hr(6) | hr 脊梁 First, Break All the Rules（hr 已 2 頁）二十年後的續篇；績效分類的 nine-lies-about-ratings 節點在等它 |
| 5 | **Introduction to Probability** | Joseph K. Blitzstein & Jessica Hwang |  | 2019 | data-science(38) | 機率基礎的教科書，線上免費，可先做站 |
| 6 | **The Book of Why** | Judea Pearl & Dana Mackenzie | 因果革命 | 2018 | data-science(38) | 因果分類的脊梁：因果階梯與反事實 |
| 7 | **Trustworthy Online Controlled Experiments** | Ron Kohavi, Diane Tang & Ya Xu |  | 2020 | data-science(38) | A/B 測試正典；工程師做實驗的第一本 |
| 8 | **An Introduction to Statistical Learning with Applications in Python** | Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani & Jonathan Taylor |  | 2023 | data-science(38) | ML 基礎的正典入門（ISLP），線上免費 |
| 9 | **Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow** | Aurélien Géron | 精通機器學習 | 2017 | data-science(38) | 動手做的 ML 主幹；收第三版 |
| 10 | **Designing Machine Learning Systems** | Chip Huyen |  | 2022 | data-science(38) | 把已收的兩本 ML system design interview 接成正典 |
| 11 | **Python for Data Analysis** | Wes McKinney |  | 2012 | data-science(38) | pandas 作者親寫，線上免費；實作分類的第一本 |
| 12 | **Practical Statistics for Data Scientists** | Peter Bruce, Andrew Bruce & Peter Gedeck |  | 2017 | data-science(38) | 資料科學家該懂的五十個統計概念 |
| 13 | **Fundamentals of Data Visualization** | Claus O. Wilke |  | 2019 | data-science(38) | 視覺化的系統課，線上免費 |
| 14 | **Thanks for the Feedback** | Douglas Stone & Sheila Heen |  | 2014 | hr(6) | 同作者群的 Difficult Conversations 已有書站、被 4 頁引用；這本補回饋的接收方，hr 績效分類只有給回饋的一半 |
| 15 | **Data Science for Business** | Foster Provost & Tom Fawcett |  | 2013 | data-science(38) | 把商業問題翻成資料問題的框架；分析與決策分類的脊梁 |
| 16 | **How to Measure Anything** | Douglas W. Hubbard | 如何衡量萬事萬物 | 2007 | data-science(38) | 校準估計與資訊價值；「無形資產」也能量 |
| 17 | **Weapons of Math Destruction** | Cathy O'Neil | 大數據的傲慢與偏見 | 2016 | data-science(38) | 演算法與社會分類的入門；有中譯 |
| 18 | **Compensation** | George T. Milkovich, Jerry M. Newman & Barry Gerhart |  | 1984 | hr(6) | 薪酬結構教科書；hr 薪酬分類只有 Work Rules! 一本，pay-structure-basics 節點在等它 |

**這是「書本身還沒有」那個軸**，與 docs/ 其餘幾份不同：

| 文件 | 缺口是什麼 | 靠什麼補 |
| --- | --- | --- |
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
| `owned` | **已收錄**——書已經做成 `nplus.wiki/<slug>/` 的書站 | 必須有 `slug`；首頁書架的封面列就是取這批，概念頁的 `furtherReading.anchor` 也是連到這裡 | 2355 筆（去重 1819 本） |
| `wanted` | **待收錄**——想收、還沒有 | 買得到，只是還沒買／還沒做站 | **46 筆（去重 46 本）** |
| `unavailable` | **暫無來源**——想收但收不到 | 絕版、無中譯、或只有機構授權（如 Scrum Guide、Vanguard 內部傳記） | 87 筆 |
| `skipped` | **刻意略過**——不打算收 | 內容重複、練習冊、合輯、不合站主軸；`note` 欄寫明為何略過 | 87 筆 |

> `owned` 去重後的 1819 是**已建成書站的書**（2355 是含跨站重複的登錄筆數，
> 一本書被三站列進盤點就算三筆）。它代表「書站存在、封面抓得到、概念頁 anchor 回得去」，
> 不等於實體書在書架上。

## 先扣掉：0 本其實已經有書站了

這些 `wanted` 的書名對得上**已存在的書 repo**——不必再收，是各站 bibliography 的 status 沒跟上。**買書前先扣掉這批**，並把該筆改成 `status: "owned"` ＋ 補上 `slug`（＝下表的 repo slug）再重跑；`/note-wanted` 會代勞。

| 書 repo slug | 書名 | 登記在 | portal 上的描述（核對用） |
| --- | --- | --- | --- |

## 作者這一關擋下的：0 筆同名不同書

書名正規化後對得上某個書 repo，**但作者不符**——所以那本不是這一筆想收的書，維持 `wanted`。這關是 2026-08-10 加的第二因子；在那之前 matcher 只比書名，撞名只能靠 `NAME_COLLISIONS` 人工白名單一筆筆補（踩到才補）。

**下面每一筆都要當成買錯書的預警**：想收的和 portal 上那本同名，下單前對作者，別對書名。

無——這輪沒有書名對上卻作者不符的。

## 疑似漏報：0 本可能其實已經有 repo

書名**沒有**正規化後完全相同，但 portal 上有 repo 長得很像——改過書名（英美版不同、中譯轉寫）的書會落在這裡。**這節是提名，不是判決**：確認是同一本就寫進 `export-wanted.py` 的 `ALIASES`，下一輪它就走精確路徑並自動掉進「先扣掉」；確認是續集或同系列的不同書就不用管，下輪還會再問一次。

門檻：兩邊書名的**雙向 Jaccard ≥70%**（詞相等的判準放寬到共同前綴 5 字元，才抓得到 `Forgiving` ↔ `Forgiveness` 這種詞形差異），且**作者沒有互相否決**。用雙向而不是單向覆蓋率，是因為單向會被系列卷洗版——`… on Leadership` 的詞有 75% 出現在 `… on Communication` 裡，但那是不同的一本。作者不符的已經在上一節擋掉；`NAME_COLLISIONS` 裁決過的不再提名。

無——沒有書名相近卻沒對上的。

## 快歸零的站：0 站只差 1–2 本

**TOP20 的準則①就看這一節。** 這些站的書單已經接近收齊，剩下的一兩本收到，整站的採購缺口就歸零——缺書不再是它進 `note-check --enrich` 深化的瓶頸。分母只算 `owned + wanted`（`unavailable` / `skipped` 是永久不可收，不算欠）。

（目前沒有只差 1–2 本的站。）

## 優先收：0 本有兩個以上的站在等

同一本書被多站列為 `wanted`——收一本補多站的缺口，投資報酬率最高。

| 英文書名 | 作者 | 中譯 | 年 | 等它的站 |
| --- | --- | --- | --- | --- |

## 完整清單（依站，共 46 筆）

### data-science-note — 39 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| The Art of Statistics | David Spiegelhalter | 統計的藝術 | 2019 | 統計思維的現代入門正典：PPDAC 循環、從資料到結論的每一步都可能出錯在哪 |
| The Data Detective | Tim Harford |  | 2020 | 英版書名 How to Make the World Add Up；看數字的十條規則，比 Silver 更輕、比 Huff 更當代 |
| Naked Statistics | Charles Wheelan | 聰明學統計的 13 又 ½ 堂課 | 2013 | 與已收的 Naked Economics 同作者同路數；迴歸、推論、中央極限定理的無痛版 |
| How to Lie with Statistics | Darrell Huff |  | 1954 | 七十年不過時的短書：平均的選擇、被截的軸、樣本偏差 |
| Statistics Done Wrong | Alex Reinhart |  | 2015 | p 值、檢定力、多重比較的錯誤圖鑑；線上有免費版 |
| Calling Bullshit | Carl T. Bergstrom & Jevin D. West | 數據的假象 | 2020 | 資料時代的鬼扯偵測：選擇偏差、誤導圖表、大數據的傲慢 |
| （統計學，最強的商業武器） | 西內啓 | 統計學，最強的商業武器 | 2013 | 日系商業統計入門；把「為什麼要學統計」講給經理人聽 |
| Introduction to Probability | Joseph K. Blitzstein & Jessica Hwang |  | 2019 | 哈佛 Stat 110 教科書，機率基礎的正典；第二版線上免費 |
| Bayesian Statistics the Fun Way | Will Kurt |  | 2019 | 貝氏統計的無痛入門：從星際大戰到 A/B 測試 |
| Statistical Rethinking | Richard McElreath |  | 2020 | 貝氏建模與因果思維的進階課；第二版 |
| Bernoulli's Fallacy | Aubrey Clayton |  | 2021 | 頻率派統計的邏輯缺陷與再現性危機——Silver 第 8 章那場論戰的整本版 |
| The Book of Why | Judea Pearl & Dana Mackenzie | 因果革命 | 2018 | 因果階梯、do 算子、反事實——「相關不是因果」之後的那一步 |
| Trustworthy Online Controlled Experiments | Ron Kohavi, Diane Tang & Ya Xu |  | 2020 | A/B 測試正典：實驗平台、陷阱、指標設計；工程師做實驗的第一本 |
| Causal Inference: The Mixtape | Scott Cunningham |  | 2021 | DAG、工具變數、DiD、RDD 的實作課；線上免費 |
| Mastering 'Metrics | Joshua D. Angrist & Jörn-Steffen Pischke |  | 2014 | 計量經濟五招（隨機、迴歸、工具變數、RDD、DiD）的平易版；接 economics 站 |
| An Introduction to Statistical Learning with Applications in Python | Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani & Jonathan Taylor |  | 2023 | ISLP；ML 基礎的正典入門：偏差—變異、交叉驗證、樹與 boosting，線上免費 |
| Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow | Aurélien Géron | 精通機器學習 | 2017 | 動手做的 ML 主幹；收第三版（2022） |
| The Hundred-Page Machine Learning Book | Andriy Burkov |  | 2019 | 一百頁講完 ML 的骨架；複習用 |
| Designing Machine Learning Systems | Chip Huyen |  | 2022 | 把已收的兩本 ML system design interview 接成正典：資料、特徵、部署、監控 |
| AI Engineering | Chip Huyen |  | 2025 | 基礎模型時代的應用工程：評估、RAG、微調、推論最佳化 |
| The Elements of Statistical Learning | Trevor Hastie, Robert Tibshirani & Jerome Friedman |  | 2001 | ISL 的數學完整版；查閱用，線上免費 |
| Python for Data Analysis | Wes McKinney |  | 2012 | 中譯《Python 資料分析》；pandas 作者親寫，收第三版（2022），線上免費 |
| Practical Statistics for Data Scientists | Peter Bruce, Andrew Bruce & Peter Gedeck |  | 2017 | 統計學家會用、資料科學家該懂的五十個概念；收第二版（2020） |
| Data Science from Scratch | Joel Grus |  | 2015 | 不靠套件從零手刻演算法，理解比效率重要時讀它；收第二版（2019） |
| Think Stats | Allen B. Downey |  | 2011 | 用 Python 做探索式統計；收第三版（2025），線上免費 |
| Fundamentals of Data Visualization | Claus O. Wilke |  | 2019 | 圖表選型與視覺編碼的系統課；線上免費 |
| The Visual Display of Quantitative Information | Edward R. Tufte |  | 1983 | 資料墨水比、圖表垃圾、Minard 的拿破崙圖——視覺化的原典 |
| Effective Data Storytelling | Brent Dykes |  | 2019 | 資料、敘事、視覺三者交集的框架；Knaflic 之後的下一本 |
| Data Science for Business | Foster Provost & Tom Fawcett |  | 2013 | 把商業問題翻成資料問題的思考框架：期望值、提升、過擬合、資料即資產 |
| How to Measure Anything | Douglas W. Hubbard | 如何衡量萬事萬物 | 2007 | 「無形資產」也能量：校準估計、資訊價值、五人法則 |
| Lean Analytics | Alistair Croll & Benjamin Yoskovitz |  | 2013 | One Metric That Matters、各商業模式的關鍵指標；接 startup 站 |
| Prediction Machines | Ajay Agrawal, Joshua Gans & Avi Goldfarb |  | 2018 | 中譯《AI 經濟的策略思維》；AI＝預測變便宜，預測與判斷分工的經濟學 |
| Competing on Analytics | Thomas H. Davenport & Jeanne G. Harris |  | 2007 | 分析型競爭者的組織條件；Davenport 那篇 HBR 文章的整本版 |
| The Model Thinker | Scott E. Page |  | 2018 | 多模型思維：同一現象用幾個簡單模型交叉看 |
| Ace the Data Science Interview | Nick Singh & Kevin Huo |  | 2021 | 接 leetcode／system-design／behaviour-interview 三個面試站的資料科學版 |
| Weapons of Math Destruction | Cathy O'Neil | 大數據的傲慢與偏見 | 2016 | 不透明、規模化、自我強化的模型如何傷害弱勢——演算法倫理的入門 |
| Everybody Lies | Seth Stephens-Davidowitz | 數據、謊言與真相 | 2017 | Google 搜尋資料揭露人們不會對問卷說的事；大數據的四種力量與極限 |
| Invisible Women | Caroline Criado Perez | 被隱形的女性 | 2019 | 資料缺口本身就是偏見：從撞擊測試假人到藥物劑量 |
| The Alignment Problem | Brian Christian |  | 2020 | ML 系統怎麼學到我們沒打算教的東西；與 Algorithms to Live By 同作者 |

### hr-note — 7 本

| 英文書名 | 作者 | 中譯 | 年 | 為何想收 |
| --- | --- | --- | --- | --- |
| Nine Lies About Work | Marcus Buckingham & Ashley Goodall |  | 2019 | 績效評等、回饋、目標串接——九個人資慣例為什麼站不住；First, Break All the Rules 二十年後的續篇 |
| Thanks for the Feedback | Douglas Stone & Sheila Heen |  | 2014 | 回饋的另一半：接收方怎麼聽；三種回饋、三種觸發 |
| The Fearless Organization | Amy C. Edmondson |  | 2018 | 中譯《心理安全感的力量》；人敢不敢說話決定團隊學不學得到東西 |
| Compensation | George T. Milkovich, Jerry M. Newman & Barry Gerhart |  | 1984 | 薪酬設計的標準教科書：職等、市場定位、績效連動；收最新版 |
| HR from the Outside In | Dave Ulrich, Jon Younger, Wayne Brockbank & Mike Ulrich |  | 2012 | 人資的六種能力：從業務與顧客往回看 HR 該做什麼 |
| Victory Through Organization | Dave Ulrich, David Kryscynski, Mike Ulrich & Wayne Brockbank |  | 2017 | 組織能力比個別人才更能解釋績效——HR 該經營的是組織，不只是人 |
| Human Resource Management | Gary Dessler |  | 1976 | 人資管理的通用教科書：招募、訓練、績效、薪酬、勞資關係全覽；收最新版 |

## 沒有英文書名的 1 本（華文／日文原著）

這些本來就沒有英文版，照原書名收。

| 原書名 | 作者 | 站 | 為何想收 |
| --- | --- | --- | --- |
| 統計學，最強的商業武器 | 西內啓 | data-science-note | 日系商業統計入門；把「為什麼要學統計」講給經理人聽 |

## 重跑

```bash
notes-core/tools/export-wanted.py
```

收到書、建好書站之後，把該站 bibliography 那筆改成 `status: "owned"` 並補 `slug`，
重跑就會從這裡消失。
