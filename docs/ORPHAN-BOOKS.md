# 孤兒書與死鏈（反向盤點）

**這份是什麼**：從**書庫那一側**反過來問的四個問題——書庫的書有沒有站在管、站上的 slug 指得到書嗎。由 `notes-core/tools/export-orphan-books.py` 生成，**不要手改**——改各站的 bibliography／內容再重跑。

**為什麼需要反向**：另外幾份都是「站說它缺什麼」的正向視角，看不到「**沒有任何站提過**」的書——新建的書站如果沒人認領，正向工具永遠不會提醒你，因為沒有站提過它。

**資料源**：GitHub 現況（`gh repo list` nplus-father／Andrewnplus，1666 個 repo），其中 `nplus-kind-book` 的書 repo 1548 本。

| 文件 | 缺口是什麼 | 靠什麼補 |
| --- | --- | --- |
| [COVERAGE-GAPS.md](./COVERAGE-GAPS.md) | 還沒有**站** | 開新站 |
| [ENRICH-BACKLOG.md](./ENRICH-BACKLOG.md) | 站在、**內容**沒寫完 | `note-check --enrich` |
| [SOURCING-DEBT.md](./SOURCING-DEBT.md) | 內容寫了、查不到**出處** | 掛 anchor |
| [WANTED-BOOKS.md](./WANTED-BOOKS.md) | **書本身**還沒有 | 去收書 |
| **本檔** | **書有了、沒有站在管**（或指到的書不存在） | 認領／開站／修 slug |

## 摘要

| 檢查 | 數 | 後果 |
| --- | ---: | --- |
| 孤兒書（沒有任何站的 bibliography 指到） | **364** | 書站建了但沒有筆記在用，等於白建 |
| ↳ 其中內容頁已經 anchor 到、盤點沒登記 | **0** | 補一筆 bibliography 就好，不必開站 |
| 死鏈 slug（bibliography 指到不存在的 repo） | **0** | 首頁書架封面 404 |
| `owned` 沒有 slug | **0** | 不會出現在首頁書架，登記了卻看不到 |
| 死鏈 anchor（內容頁 `book:` 指到不存在的 repo） | **4** | 延伸閱讀連結 404 |

## 一、孤兒書：364 本沒有任何站認領

判準＝這本書的 repo name 沒有出現在**任何**站 `bibliography.ts` 的 `slug` 欄。用 slug 而不是站數對書數，是因為它抓得到跨站分工——一本書被別站認領也算覆蓋。

### 1a. 內容已經引了、盤點沒登記：0 本

無——內容引用到的書都已經登記在盤點裡。

### 1b. 開新站候選：1 個 leaf

判準沿用 COVERAGE-GAPS 那輪：**藏書 ≥8 本且未覆蓋 ≥60%**。低於這個比例的 leaf 表示已經有站在管、只是還沒寫完——那是 [ENRICH-BACKLOG](./ENRICH-BACKLOG.md) 的事，不是這裡的。

| leaf | 未覆蓋/總數 | 未覆蓋率 | 沒人認領的是哪幾本 |
| --- | ---: | ---: | --- |
| `security` | 6/8 | **75%** | Security Engineering、Attacking Network Protocols、Hacking: The Art of Exploitation、Serious Cryptography、Real-World Bug Hunting、The Browser Hacker's Handbook |

### 1c. 各 leaf 覆蓋率與目前誰在管

**看比例不是看絕對數。** 未覆蓋比例高＝沒站在管（開新站）；絕對數高但比例低＝有站在管、只是還沒寫完。「目前誰在管」是該 leaf **已覆蓋**的書被哪些站引用——孤兒通常就該歸這幾站認領，不必另外開站。

| leaf | sub | 未覆蓋/總數 | 未覆蓋率 | 目前誰在管 |
| --- | --- | ---: | ---: | --- |
| `investing` | finance | 52/123 | 42% | investing(46)、schwager(9)、personal-finance(7) |
| `biblical-studies` | theology | 43/117 | 37% | biblical-studies(63)、stott(8)、nt-wright(7) |
| `growth` | mindset | 37/115 | 32% | growth(22)、thinking(17)、science(11) |
| `systematic` | theology | 31/78 | 40% | theology(27)、keller(13)、spiritual-formation(9) |
| `persuasion` | communication | 30/64 | 47% | communication(18)、greene(3)、business-strategy(3) |
| `coding-practice` | engineering | 29/70 | 41% | clean-code(18)、design-patterns(12)、uncle-bob(5) |
| `ethics` | philosophy | 25/69 | 36% | philosophy(15)、fromm(9)、de-botton(7) |
| `productivity` | habit | 11/53 | 21% | tools(25)、habits(20)、tracy(5) |
| `self-learning` | education | 9/29 | 31% | learning(17)、growth(4)、career(2) |
| `strategy` | business | 9/35 | 26% | business-strategy(18)、startup(5)、hbr(3) |
| `community` | relationships | 8/26 | 31% | relationships(14)、maxwell(2)、communication(2) |
| `security` | engineering | 6/8 | 75% | cloud-infra(1)、system-design(1) |
| `public-speaking` | communication | 5/13 | 38% | communication(5)、hbr(3)、tracy(1) |
| `civilization` | history | 5/24 | 21% | history(13)、fengtang(2)、wujun(2) |
| `systems-design` | engineering | 5/26 | 19% | system-design(14)、design-patterns(6)、fowler(3) |
| `storytelling` | communication | 4/11 | 36% | communication(5)、writing(2)、greene(1) |
| `personal-finance` | finance | 4/29 | 14% | personal-finance(17)、kiyosaki(14)、schwager(1) |
| `economics` | finance | 4/36 | 11% | economics(32)、investing(3)、kiyosaki(2) |
| `negotiation` | communication | 3/16 | 19% | communication(10)、hbr(2)、relationships(1) |
| `political-philosophy` | philosophy | 3/6 | 50% | philosophy(2)、economics(1) |
| `emotion` | mindset | 3/12 | 25% | life-meaning(9)、thinking(2)、maxwell(1) |
| `apologetics` | theology | 2/9 | 22% | theology(7)、lewis(4)、spiritual-formation(1) |
| `cognitive` | science | 2/32 | 6% | thinking(23)、science(12)、gardner(7) |
| `databases` | engineering | 2/10 | 20% | data-systems(8)、fowler(1) |
| `vision` | leadership | 2/45 | 4% | leadership(39)、management(7)、business-strategy(5) |
| `discipline` | habit | 2/5 | 40% | habits(2)、writing(1)、cloud(1) |
| `non-fiction` | writing | 2/19 | 11% | writing(15)、learning(1)、philosophy(1) |
| `visual` | design | 2/14 | 14% | design(11)、problem-solving(1)、de-botton(1) |
| `coffee` | tools | 2/2 | 100% | **沒有站在管** |
| `fiction` | writing | 2/7 | 29% | writing(4)、lewis(1) |

> 另有 19 個 leaf 各有 1–2 本孤兒，逐本列在下面「全部孤兒書」那節。

### 1d. 同一作者 ≥3 本沒人認領：4 位

作者站的線索。**有同名站就是該站漏收**（回去補 bibliography），沒有站才是開站候選——COVERAGE-GAPS 的人物缺口就是這樣抓出 covey／templar／navarro 三站的。

| 作者 | 孤兒本數 | 已有作者站？ | 書 |
| --- | ---: | --- | --- |
| CFA Institute | 5 | — | Corporate Finance Workbook、Portfolio Management in Practice, Volume 1: Investment Management、Portfolio Management in Practice, Volume 2: Asset Allocation、Portfolio Management in Practice, Volume 3: Equity Portfolio Management、Quantitative Investment Analysis |
| 秦嗣林 | 4 | — | 29張當票：典當不到的人生啟發、29張當票2：當舖裡特有的人生風景、29張當票3：門簾外的人生鑑定、學上當 |
| David J. Atkinson | 3 | — | The Message of Job、The Message of Proverbs、The Message of Ruth |
| John Ortberg | 3 | — | God Is Closer Than You Think、行在水面上、Who Is This Man? |

### 1e. 全部 364 本（依 leaf 分組）

#### `investing` — 52/123 沒人認領（目前：investing(46)、schwager(9)、personal-finance(7)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `50-questions-retail-investors` | 散戶的50道難題：一次解開所有台股散戶們的共同疑問 | 安納金、葉芳、金律 |
| `7-mistakes-every-investor-makes` | 7 Mistakes Every Investor Makes | Joachim Klement |
| `attitude-of-the-rich` | 富者的態度 | J won |
| `battle-for-investment-survival` | The Battle for Investment Survival | Gerald M. Loeb |
| `beat-the-crowd` | Beat the Crowd | Ken Fisher & Elisabeth Dellinger |
| `bogleheads-guide-to-three-fund-portfolio` | The Bogleheads' Guide to the Three-Fund Portfolio | Taylor Larimore |
| `cfa-corporate-finance-workbook` | Corporate Finance Workbook | CFA Institute |
| `debunkery` | Debunkery | Ken Fisher |
| `devils-financial-dictionary` | The Devil's Financial Dictionary | Jason Zweig |
| `elements-of-investing` | The Elements of Investing | Burton G. Malkiel & Charles D. Ellis |
| `first-book-for-retail-investors` | 散戶投資上手的第一本書 | 王力群 |
| `five-key-numbers` | 不懂財報，也能輕鬆選出賺錢績優股 | 林明樟（MJ） |
| `fool-and-his-money` | A Fool and His Money | John Rothchild |
| `forrest-investing` | 阿甘投資法 | 闕又上 |
| `how-finance-works` | How Finance Works | Mihir Desai |
| `how-i-invest-my-money` | How I Invest My Money | Joshua Brown & Brian Portnoy |
| `im-worth-more` | I'm Worth More | Rob Moore |
| `in-pursuit-of-perfect-portfolio` | In Pursuit of the Perfect Portfolio | Andrew W. Lo & Stephen R. Foerster |
| `invested` | Invested | Charles Schwab |
| `investing-hagstrom` | Investing: The Last Liberal Art | Robert G. Hagstrom |
| `joys-of-compounding` | The Joys of Compounding | Gautam Baid |
| `kostolany-confessions` | Die Kunst, über Geld nachzudenken | André Kostolany |
| `kostolany-practical` | 一個投機者的告白實戰書 | 安納金 |
| `little-book-of-currency-trading` | The Little Book of Currency Trading | Kathy Lien |
| `little-book-of-investing-like-the-pros` | The Little Book of Investing Like the Pros | Joshua Pearl & Joshua Rosenbaum |
| `little-book-of-safe-money` | The Little Book of Safe Money | Jason Zweig |
| `long-term-investing` | 長期買進 | 周冠男 |
| `money-game` | The Money Game | George J. W. Goodman (writing as "Adam Smith") |
| `money-rob-moore` | Money: Know More, Make More, Give More | Rob Moore |
| `new-tao-of-warren-buffett` | The New Tao of Warren Buffett | Mary Buffett & David Clark |
| `nothing-but-net` | Nothing But Net | Mark Mahaney |
| `only-three-questions-that-still-count` | The Only Three Questions That Still Count | Ken Fisher (with Lara Hoffmans) |
| `payback-time` | Payback Time | Phil Town |
| `portfolio-management-in-practice-vol-1` | Portfolio Management in Practice, Volume 1: Investment Management | CFA Institute |
| `portfolio-management-in-practice-vol-2` | Portfolio Management in Practice, Volume 2: Asset Allocation | CFA Institute |
| `portfolio-management-in-practice-vol-3` | Portfolio Management in Practice, Volume 3: Equity Portfolio Management | CFA Institute |
| `power-law` | The Power Law | Sebastian Mallaby |
| `quantitative-investment-analysis` | Quantitative Investment Analysis | CFA Institute |
| `quants` | The Quants | Scott Patterson |
| `random-walk-guide-to-investing` | The Random Walk Guide to Investing | Burton G. Malkiel |
| `rule` | The Rule | Larry Hite |
| `soul-of-wealth` | 財富的靈魂 | Daniel Crosby |
| `speculator-confession-practice` | 一個投機者的告白實戰書 | 安納金 |
| `taking-stock` | 盤點人生：一位安寧醫師教你什麼才是真正的財富 | Jordan Grumet |
| `tap-dancing-to-work` | Tap Dancing to Work | Carol J. Loomis |
| `thou-shall-prosper` | Thou Shall Prosper | Daniel Lapin |
| `trading-game` | The Trading Game | Gary Stevenson |
| `trend-following-masters-volume-2` | Trend Following Masters Volume 2 | Michael Covel |
| `us-stock-investing-with-jc` | 美股投資學：跟著JC錢進美股 | 財女Jenny |
| `warren-buffetts-ground-rules` | Warren Buffett's Ground Rules | Jeremy C. Miller |
| `yale-finance-course` | 受用一生的耶魯金融投資課 | 陳志武 |
| `yale-financial-literacy` | 耶魯最受歡迎的金融通識課 | 陳志武 |

#### `biblical-studies` — 43/117 沒人認領（目前：biblical-studies(63)、stott(8)、nt-wright(7)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `an-introduction-to-the-new-testament` | An Introduction to the New Testament: Contexts, Methods & Ministry Formation | David A. deSilva |
| `bible-atlas` | bible-atlas | ⚠ 描述沒有作者欄 |
| `books-of-the-pentateuch` | The Books of the Pentateuch | William Evans |
| `dictionary-of-the-later-new-testament` | Dictionary of the Later New Testament & Its Developments | Ralph P. Martin & Peter H. Davids (eds.) |
| `ezra-nehemiah-esther-for-everyone` | Ezra, Nehemiah, and Esther for Everyone | John Goldingay |
| `message-of-1-corinthians` | The Message of 1 Corinthians | David Prior |
| `message-of-1-peter` | The Message of 1 Peter | Edmund Clowney |
| `message-of-2-corinthians` | The Message of 2 Corinthians | Paul Barnett |
| `message-of-2-peter-jude` | The Message of 2 Peter & Jude | Dick Lucas & Christopher Green |
| `message-of-colossians-philemon` | The Message of Colossians & Philemon | Dick Lucas |
| `message-of-daniel` | The Message of Daniel | Ronald S. Wallace |
| `message-of-ecclesiastes` | The Message of Ecclesiastes | Derek Kidner |
| `message-of-esther` | The Message of Esther | David G. Firth |
| `message-of-ezekiel` | The Message of Ezekiel | Christopher J. H. Wright |
| `message-of-ezra-and-haggai` | The Message of Ezra & Haggai | Robert Fyall |
| `message-of-genesis-bst` | The Message of Genesis | David Atkinson & Joyce G. Baldwin |
| `message-of-hosea` | The Message of Hosea | Derek Kidner |
| `message-of-isaiah` | The Message of Isaiah | Barry G. Webb |
| `message-of-jeremiah` | The Message of Jeremiah | Derek Kidner & Hywel R. Jones |
| `message-of-job` | The Message of Job | David J. Atkinson |
| `message-of-joel-micah-habakkuk` | The Message of Joel, Micah & Habakkuk | David Prior |
| `message-of-john` | The Message of John | Bruce Milne |
| `message-of-johns-letters` | The Message of John's Letters | David Jackman |
| `message-of-jonah` | The Message of Jonah | Rosemary Nixon |
| `message-of-joshua` | The Message of Joshua | David G. Firth |
| `message-of-kings` | The Message of Kings | John W. Olley |
| `message-of-lamentations` | The Message of Lamentations | Christopher J. H. Wright |
| `message-of-leviticus` | The Message of Leviticus | Derek Tidball |
| `message-of-malachi` | The Message of Malachi | Peter Adam |
| `message-of-mark` | The Message of Mark | Donald English |
| `message-of-matthew` | The Message of Matthew | Michael Green |
| `message-of-obadiah-nahum-zephaniah` | The Message of Obadiah, Nahum and Zephaniah | Gordon Bridger |
| `message-of-proverbs` | The Message of Proverbs | David J. Atkinson |
| `message-of-ruth` | The Message of Ruth | David J. Atkinson |
| `message-of-samuel` | The Message of Samuel | Mary J. Evans |
| `message-of-song-of-songs` | The Message of the Song of Songs | Tom Gledhill |
| `message-of-zechariah` | The Message of Zechariah | Barry Webb |
| `on-the-holy-spirit` | On the Holy Spirit | Basil the Great |
| `sherlock-who-2-biblical-world` | 胡爾摩斯Ⅱ重返聖經現場 | 胡維華 |
| `sherlock-who-3-new-light` | 胡爾摩斯Ⅲ新世紀拉比探案 | 胡維華 |
| `state-of-new-testament-studies` | The State of New Testament Studies | Scot McKnight & Nijay K. Gupta (eds.) |
| `understanding-the-bible` | Understanding the Bible: Methods of Bible Study | Dorothy L. Johns |
| `when-good-men-are-tempted` | When Good Men Are Tempted | Bill Perkins |

#### `growth` — 37/115 沒人認領（目前：growth(22)、thinking(17)、science(11)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `11-rules-for-life` | 11 Rules For Life | Chetan Bhagat |
| `29-pawn-tickets-2` | 29張當票2：當舖裡特有的人生風景 | 秦嗣林 |
| `29-pawn-tickets-3` | 29張當票3：門簾外的人生鑑定 | 秦嗣林 |
| `5-types-of-wealth` | The 5 Types of Wealth | Sahil Bloom |
| `50-erfolgsmodelle` | The Decision Book | Mikael Krogerus & Roman Tschappeler |
| `achievement-habit` | The Achievement Habit | Bernard Roth |
| `anlegerpsychologie` | Anlegerpsychologie | Heinz-Kurt Wahren |
| `art-of-action` | The Art of Thinking Clearly: Acting Wisely | Rolf Dobelli |
| `art-of-adult-decision-making` | 大人學選擇 | 姚詩豪、張國洋 |
| `art-of-selfishness` | The Art of Selfishness | David Seabury |
| `asking-the-right-questions` | Asking the Right Questions | M. Neil Browne & Stuart M. Keeley |
| `be-obsessed-or-be-average` | Be Obsessed or Be Average | Grant Cardone |
| `biased` | Biased | Jennifer L. Eberhardt |
| `biggest-bluff` | The Biggest Bluff | Maria Konnikova |
| `bright-sided` | Bright-Sided | Barbara Ehrenreich |
| `chancing-it` | Chancing It | Robert Matthews |
| `change-your-questions-change-your-life` | Change Your Questions, Change Your Life | Marilee G. Adams |
| `change-your-thinking-change-your-life` | Change Your Thinking, Change Your Life | Joseph Murphy |
| `confidence-game` | The Confidence Game | Maria Konnikova |
| `critical-thinking-concepts-and-tools` | Critical Thinking: Concepts and Tools | Richard Paul & Linda Elder |
| `die-empty` | Die Empty | Todd Henry |
| `difference-that-makes-the-difference` | The Difference That Makes the Difference | Joseph O'Connor & Andrea Lages |
| `everyone-can-succeed` | 每個人都可以成功：程天縱的31個見解 | 程天縱 |
| `fei-style-thinking` | 菲式思考：從 22K 到頂尖，一個交易員逆轉人生的關鍵思維 | 菲比斯 |
| `giant-trader-thinking` | 巨人思維 | 巨人傑 |
| `grey-thinking` | 灰階思考 | 謝孟恭 |
| `long-win` | The Long Win | Cath Bishop |
| `mindset-secrets-for-winning` | Mindset Secrets for Winning | Mark Minervini |
| `no-one-understands-you-and-what-to-do-about-it` | No One Understands You and What to Do About It | Heidi Grant Halvorson |
| `payoff` | 動機背後的隱藏邏輯 | Dan Ariely |
| `reinventing-your-life` | Reinventing Your Life | Jeffrey E. Young & Janet S. Klosko |
| `road-back-to-you` | The Road Back to You | Ian Morgan Cron & Suzanne Stabile |
| `self-esteem-a-proven-program-of-cognitive-techniques-for` | Self-Esteem | Matthew McKay |
| `think-twice-harnessing-the-power-of-counterintuition` | 再想一下-好決策的關鍵思考術 | Michael J. Mauboussin |
| `thinking-101` | 思考 101：耶魯大學改變人生的一堂思辨課 | Woo-kyoung Ahn (安宇敬) |
| `welcome-to-your-brain` | 大腦開竅手冊 | Sandra Aamodt & Sam Wang |
| `winning-grover` | 贏者之道 | Tim S. Grover |

#### `systematic` — 31/78 沒人認領（目前：theology(27)、keller(13)、spiritual-formation(9)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `21st-century-theology-casebook` | 21世紀神學事件簿--如何在多元處境下做神學 | 謝木水 |
| `along-with-moses` | 五經行--妥拉中的生命智慧 | 李思敬 |
| `anti-intellectualism-chinese-church` | 中國教會的反智主義 | 葛牧之 |
| `call` | The Call | Os Guinness |
| `casket-empty-new-testament-study-guide-god-s-plan-of` | 21世紀新約導覽 | David L. Palmer |
| `culture-making` | Culture Making | Andy Crouch |
| `exclusion-and-embrace` | Exclusion and Embrace | Miroslav Volf |
| `finding-sanctuary-monastic-steps-for-everyday-life` | Finding Sanctuary | Abbot Christopher Jamison |
| `flying-together-a-christian-marriage-guide` | Flying Together: A Christian Marriage Guide | Mike Mason |
| `god-is-closer-than-you-think` | God Is Closer Than You Think | John Ortberg |
| `ichabod-toward-home` | Ichabod Toward Home | Walter Brueggemann |
| `if-you-want-to-walk-on-water-you-have-got-to-get-out-of-the` | 行在水面上 | John Ortberg |
| `introduction-to-nt-research` | 新約聖經研究導論 | 中華福音神學院師資群編 |
| `is-hell-for-real` | Is Hell for Real | Morgan Peterson eds |
| `jesus-i-never-knew` | The Jesus I Never Knew | Philip Yancey |
| `living-gently-in-a-violent-world` | Living Gently in a Violent World | Stanley Hauerwas & Jean Vanier |
| `martin-luthers-catechisms-forming-the-faith` | 馬丁路德的門徒培育班 | Timothy J. Wengert |
| `moses-in-the-clinic` | 在診療室遇見摩西：精神科醫師帶你探索隱藏在聖經裡的心靈祕密 | 林信男 |
| `nine-adventures-in-knowing-god-and-people` | 認識上帝與認識人的9個探險 | 林鴻信 |
| `peaceable-kingdom` | The Peaceable Kingdom | Stanley Hauerwas |
| `pursuit-of-holiness` | The Pursuit of Holiness | Jerry Bridges |
| `telling-the-truth` | Telling the Truth: The Gospel as Tragedy, Comedy, and Fairy Tale | Frederick Buechner |
| `tongue-a-creative-force` | 言語的威力 | Paul David Tripp |
| `toward-a-christian-moral-imagination` | 是與非以外：基督教的倫理想像 | 龔立人 |
| `when-god-interrupts` | When God Interrupts | M. Craig Barnes |
| `who-is-this-man` | Who Is This Man? | John Ortberg |
| `who-says-the-letter-kills` | 誰說字句叫人死 | 蔡麗貞 |
| `witness-to-jesus-as-christ` | 見證耶穌是基督：基督宗教釋經學初探 | 彭國瑋 (Peng Kuo-Wei) |
| `wound-of-knowledge` | Wound of Knowledge | Rowan Williams |
| `written-in-stone` | Written in Stone | Philip Graham Ryken |
| `you-are-what-you-love` | You Are What You Love | James K. A. Smith |

#### `persuasion` — 30/64 沒人認領（目前：communication(18)、greene(3)、business-strategy(3)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `ask-more-the-power-of-questions` | Ask More | Frank Sesno |
| `communication-methods` | 溝通的方法 | 脫不花 |
| `dignity-of-speaking` | 說話的品格 | 李起周 |
| `four-seconds` | Four Seconds | Peter Bregman |
| `friend-and-foe` | Friend and Foe | Adam Galinsky & Maurice Schweitzer |
| `get-anyone-to-do-anything` | Get Anyone to Do Anything | David J. Lieberman |
| `how-to-become-famous` | How to Become Famous | Cass R. Sunstein |
| `how-to-use-power-phrases` | How to Use Power Phrases | Meryl Runion |
| `impromptu` | Impromptu | Judith Humphrey |
| `influence-the-psychology-of-persuasion` | Influence: The Psychology of Persuasion | Robert B. Cialdini |
| `lets-talk` | Let's Talk | Therese Huston |
| `make-it-clear` | Make It Clear | Patrick Henry Winston |
| `mba-confidential` | 沒人敢告訴你的MBA大揭密 | （作者待補） |
| `next-conversation` | The Next Conversation | Jefferson Fisher |
| `no-thanks-im-just-looking` | No Thanks, I'm Just Looking | Harry J. Friedman |
| `ohne-worte` | Ohne Worte | Thorsten Havener |
| `power-questions` | Power Questions | Andrew Sobel & Jerold Panas |
| `reinforcements-how-to-get-people-to-help-you` | Reinforcements: How to Get People to Help You | Heidi Grant |
| `remember-who-you-are` | Remember Who You Are | Daisy Wademan |
| `repeatable-communication` | 可複製的溝通力 | 樊登 |
| `secrets-of-consulting` | The Secrets of Consulting | Gerald M. Weinberg |
| `secrets-of-power-problem-solving` | Secrets of Power Problem Solving | Roger Dawson |
| `simply-put` | Simply Put | Ben Guttmann |
| `simply-said` | Simply Said | Jay Sullivan |
| `speak-well` | 好好說話：新鮮有趣的話術精進技巧 | 馬薇薇、黃執中、周玄毅 |
| `terrible-truth-about-lawyers` | The Terrible Truth About Lawyers | Mark H. McCormack |
| `what-to-ask-the-person-in-the-mirror` | What to Ask the Person in the Mirror | Robert Steven Kaplan |
| `winning` | Winning | Jack Welch & Suzy Welch |
| `you-can-read-anyone` | You Can Read Anyone | David J. Lieberman |
| `youve-got-8-seconds` | You've Got 8 Seconds | Paul Hellman |

#### `coding-practice` — 29/70 沒人認領（目前：clean-code(18)、design-patterns(12)、uncle-bob(5)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `97-things-every-programmer-should-know` | 97 Things Every Programmer Should Know | Kevlin Henney (ed.) |
| `97-things-every-software-architect-should-know` | 97 Things Every Software Architect Should Know | Richard Monson-Haefel |
| `algorithms-to-live-by` | Algorithms to Live By | Brian Christian & Tom Griffiths |
| `art-of-clean-code` | 精通無瑕程式碼 | Christian Mayer |
| `art-of-doing-science-and-engineering` | The Art of Doing Science and Engineering | Richard Hamming |
| `balancing-coupling-in-software-design` | Balancing Coupling in Software Design | Vlad Khononov |
| `bdd-in-action` | BDD in Action | John Ferguson Smart |
| `big-refactoring` | 大話重構：軟體重構實戰指南 | 王洋 |
| `clean-code-principles-and-patterns` | 整潔程式碼原則與模式：軟體從業者手冊 | Petri Silen |
| `coders-at-work` | Coders at Work | Peter Seibel |
| `coding-interview-patterns` | Coding Interview Patterns | Alex Xu |
| `effective-debugging` | Effective Debugging | Diomidis Spinellis |
| `exploring-requirements` | Exploring Requirements | Donald C. Gause & Gerald M. Weinberg |
| `joel-on-software` | Joel on Software | Joel Spolsky |
| `living-documentation` | Living Documentation | Cyrille Martraire |
| `more-joel-on-software` | More Joel on Software | Joel Spolsky |
| `mythical-man-month` | The Mythical Man-Month | Frederick P. Brooks Jr. |
| `nine-algorithms-that-changed-the-future` | Nine Algorithms That Changed the Future | John MacCormick |
| `perfect-software` | Perfect Software | Gerald M. Weinberg |
| `prefactoring` | Prefactoring | Ken Pugh |
| `programmer-self-cultivation` | 程式設計師的自我修養：連結、裝載與程式庫 | 俞甲子、石凡、潘愛民 |
| `programming-pearls` | Programming Pearls | Jon Bentley |
| `running-on-empty` | Running on Empty | Jonice Webb |
| `seriously-good-software` | Seriously Good Software | Marco Faella |
| `software-architect-12-disciplines` | 12 Essential Skills for Software Architects | Dave Hendricksen |
| `software-architect-elevator` | The Software Architect Elevator | Gregor Hohpe |
| `software-developers-career-guide` | The Complete Software Developer's Career Guide | John Sonmez |
| `specification-by-example` | Specification by Example | Gojko Adzic |
| `zen-programmer` | The Zen Programmer | Christian Grobmeier |

#### `ethics` — 25/69 沒人認領（目前：philosophy(15)、fromm(9)、de-botton(7)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `29-pawn-tickets` | 29張當票：典當不到的人生啟發 | 秦嗣林 |
| `almanack-of-naval-ravikant` | The Almanack of Naval Ravikant | Eric Jorgenson |
| `art-of-asking-life-questions` | The Art of Asking Life Questions | Rolf Dobelli |
| `autobiography-john-stuart-mill` | Autobiography | John Stuart Mill |
| `beautiful-thoughts-from-emerson` | Beautiful Thoughts from Ralph Waldo Emerson | Ralph Waldo Emerson |
| `death` | Death | Shelly Kagan |
| `essays-of-francis-bacon` | The Essays | Francis Bacon |
| `fallen-leaves` | Fallen Leaves | Will Durant |
| `gazing-at-life-theological-aesthetics-of-the-decalogue` | 凝視生命：奇士勞斯基《十誡》的神學美學 | 曾慶豹 |
| `golden-rules` | The Golden Rules | Bob Bowman |
| `illness-narratives` | The Illness Narratives | Arthur Kleinman |
| `intuition-pumps` | Intuition Pumps | Daniel C. Dennett |
| `let-your-life-speak` | Let Your Life Speak | Parker J. Palmer |
| `life-in-three-dimensions` | 心理富足的人生：好奇、探索與體驗如何成就更完整的生活 | Shigehiro Oishi |
| `live-your-best-life` | 活出生命最好的可能 | 彭明輝 |
| `marx-capital-and-the-madness-of-economic` | Marx, Capital and the Madness of Economic Reason | David Harvey |
| `philosophy-and-life` | 哲學與人生 | 傅佩榮 |
| `poor-richard-s-almanack` | Poor Richard's Almanack | Benjamin Franklin |
| `reading-as-a-wilderness` | 讀書這個荒野 | 見城徹 |
| `talmud-the-jewish-bible-of-wealth` | 塔木德——猶太人的致富聖經 | 佛蘭克．赫爾 |
| `theory-and-practice-of-counseling-and-psychotherapy` | Theory and Practice of Counseling and Psychotherapy | Gerald Corey |
| `wait-what-book` | Wait, What? | James E. Ryan |
| `walden` | Walden | Henry David Thoreau |
| `way-of-munger` | 蒙格之道：關於投資、閱讀、工作與幸福的普通常識 | Charles T. Munger |
| `what-life-should-mean-to-you` | What Life Should Mean to You | Alfred Adler |

#### `productivity` — 11/53 沒人認領（目前：tools(25)、habits(20)、tracy(5)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `art-of-work-and-life` | 工作與生活的技術 | 王永福 |
| `dont-sweat-the-small-stuff-at-work` | Don't Sweat the Small Stuff at Work | Richard Carlson |
| `laws-of-winners` | 贏家的法則：30 個通往成功的鐵律 | Bodo Schäfer |
| `learning-to-be-deceived` | 學上當 | 秦嗣林 |
| `mindset-for-wealth` | 心態致富 | Franklyn Hobbs |
| `qbq-question-behind-question` | QBQ! The Question Behind the Question | John G. Miller |
| `rich-habits-corley` | Rich Habits | Thomas C. Corley |
| `rich-habits-practice` | Effort-Less Wealth | Tom Corley |
| `rich-kids` | Rich Kids: How to Raise Our Children to Be Happy and Successful in Life | Tom Corley |
| `world-only-readers-can-reach` | 只有讀書能抵達的境界 | 齋藤孝 |
| `worries-are-all-in-your-head` | 煩惱都是自己想出來的 | 古川武士 |

#### `self-learning` — 9/29 沒人認領（目前：learning(17)、growth(4)、career(2)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `english-is-not-easy` | English Is Not Easy | Luci Gutiérrez |
| `grid-notebook` | 讀書筆記模版 | 高橋政史 |
| `living-loving-and-learning` | Living, Loving and Learning | Leo F. Buscaglia |
| `online-teaching-technique` | 線上教學的技術 | 福哥（王永福） |
| `sociology-for-everyone` | 寫給每個人的社會學讀本 | 岩本茂樹 |
| `teaching-technique` | 教學的技術 | 福哥（王永福） |
| `understanding-human-nature` | 阿德勒心理學講義 | Alfred Adler |
| `where-do-top-performers-draw-the-line-when-reading` | 一流的人讀書，都在哪裡畫線？ | 土井英司 |
| `why-study-the-past` | Why Study the Past | Rowan Williams |

#### `strategy` — 9/35 沒人認領（目前：business-strategy(18)、startup(5)、hbr(3)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `50-success-classics` | 50 Business Classics | Tom Butler-Bowdon |
| `bad-blood` | Bad Blood | John Carreyrou |
| `billion-dollar-secret` | The Billion Dollar Secret | Rafael Badziag |
| `competitive-advantage-of-nations` | The Competitive Advantage of Nations | Michael E. Porter |
| `hustle-and-gig` | Hustle and Gig | Alexandrea J. Ravenelle |
| `mis-server-82` | MIS 一定要懂的 82 個伺服器建置與管理知識 | きはし まさひろ |
| `podcast-producer-guide` | 破億下載 Podcast 製作人的經營指南 | 粘瀚文 Billy Nien |
| `post-corona` | Post Corona | Scott Galloway |
| `secrets-of-the-javascript-ninja` | Secrets of the JavaScript Ninja, 2nd ed. | John Resig, Bear Bibeault & Josip Maras |

#### `community` — 8/26 沒人認領（目前：relationships(14)、maxwell(2)、communication(2)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `art-of-the-table` | The Art of the Table | Suzanne von Drachenfels |
| `asshole-survival-guide` | The Asshole Survival Guide | Robert I. Sutton |
| `emily-posts-etiquette-19th-edition` | Emily Post's Etiquette, 19th Edition | Peggy Post et al. |
| `how-to-say-it` | How to Say It | Rosalie Maggio |
| `sizing-people-up` | Sizing People Up | Robin Dreeke |
| `sociopath-next-door` | The Sociopath Next Door | Martha Stout |
| `whos-pulling-your-strings` | Who's Pulling Your Strings? | Harriet B. Braiker |
| `your-anxiety-comes-from-being-too-used-to-getting-hurt` | 你的不安，是因為太習慣受傷害 | 中島輝 |

#### `security` — 6/8 沒人認領（目前：cloud-infra(1)、system-design(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `attacking-network-protocols` | Attacking Network Protocols | James Forshaw |
| `browser-hackers-handbook` | The Browser Hacker's Handbook | Wade Alcorn, Christian Frichot & Michele Orrù |
| `hacking-art-of-exploitation` | Hacking: The Art of Exploitation | Jon Erickson |
| `real-world-bug-hunting` | Real-World Bug Hunting | Peter Yaworski |
| `security-engineering` | Security Engineering | Ross Anderson |
| `serious-cryptography` | Serious Cryptography | Jean-Philippe Aumasson |

#### `public-speaking` — 5/13 沒人認領（目前：communication(5)、hbr(3)、tracy(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `power-of-eye-contact` | The Power of Eye Contact | Michael Ellsberg |
| `say-it-well` | Say It Well | Terry Szuplat |
| `show-and-tell` | Show and Tell | Dan Roam |
| `speaking-up` | Speaking Up | Frederick Gilbert |
| `stage-presentation-skills` | 上台的技術 | 王永福 |

#### `civilization` — 5/24 沒人認領（目前：history(13)、fengtang(2)、wujun(2)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `autobiography-of-benjamin-franklin` | The Autobiography of Benjamin Franklin | Benjamin Franklin |
| `conversations-with-myself` | Conversations with Myself | Nelson Mandela |
| `elephant-and-the-flea` | The Elephant and the Flea | Charles Handy |
| `sovereign-individual` | The Sovereign Individual | James Dale Davidson & Lord William Rees-Mogg |
| `wealth-of-humans` | The Wealth of Humans | Ryan Avent |

#### `systems-design` — 5/26 沒人認領（目前：system-design(14)、design-patterns(6)、fowler(3)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `beautiful-architecture` | Beautiful Architecture | Diomidis Spinellis & Georgios Gousios |
| `get-your-hands-dirty-clean-architecture` | Get Your Hands Dirty on Clean Architecture | Tom Hombergs |
| `software-architecture-for-developers-vol1` | Software Architecture for Developers, Vol. 1 | Simon Brown |
| `software-architecture-for-developers-vol2` | Software Architecture for Developers, Vol. 2 | Simon Brown |
| `system-architecture-design` | 系統架構設計：從程式設計師向架構師轉型之路 | 鄭天民 |

#### `storytelling` — 4/11 沒人認領（目前：communication(5)、writing(2)、greene(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `diary-of-a-ceo` | The Diary of a CEO | Steven Bartlett |
| `five-stars` | Five Stars | Carmine Gallo |
| `leading-matters` | Leading Matters | John L. Hennessy |
| `reputation-game` | The Reputation Game | David Waller |

#### `personal-finance` — 4/29 沒人認領（目前：personal-finance(17)、kiyosaki(14)、schwager(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `tax-secrets-of-the-rich` | Tax Secrets of the Rich | Allan Mason |
| `ten-roads-to-riches` | The Ten Roads to Riches | Ken Fisher et al. |
| `who-stole-my-pension` | Who Stole My Pension? | Robert Kiyosaki & Edward Siedle |
| `why-a-students-work-for-c-students` | Why "A" Students Work for "C" Students | Robert T. Kiyosaki |

#### `economics` — 4/36 沒人認領（目前：economics(32)、investing(3)、kiyosaki(2)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `algebra-of-wealth` | The Algebra of Wealth | Scott Galloway |
| `from-here-to-financial-happiness` | From Here to Financial Happiness | Jonathan Clements |
| `how-economy-grows` | How an Economy Grows and Why It Crashes | Peter D. Schiff & Andrew J. Schiff |
| `little-book-that-builds-wealth` | The Little Book That Builds Wealth | Pat Dorsey |

#### `negotiation` — 3/16 沒人認領（目前：communication(10)、hbr(2)、relationships(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `code-of-trust` | The Code of Trust | Robin Dreeke |
| `getting-to-yes-with-yourself` | Getting to Yes with Yourself | William Ury |
| `secrets-of-power-negotiating-for-salespeople` | Secrets of Power Negotiating for Salespeople | Roger Dawson |

#### `political-philosophy` — 3/6 沒人認領（目前：philosophy(2)、economics(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `50-politics-classics` | 50 Politics Classics | Tom Butler-Bowdon |
| `equality` | Equality | Thomas Piketty & Michael J. Sandel |
| `secular-age` | A Secular Age | Charles Taylor |

#### `emotion` — 3/12 沒人認領（目前：life-meaning(9)、thinking(2)、maxwell(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `inner-excellence` | Inner Excellence | Jim Murphy |
| `social-animal` | The Social Animal | David Brooks |
| `your-mind-an-owners-manual-for-a-better-life` | Your Mind: An Owner's Manual for a Better Life | Christopher Cortman & Harold Shinitzky |

#### `apologetics` — 2/9 沒人認領（目前：theology(7)、lewis(4)、spiritual-formation(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `god-in-the-dock` | God in the Dock: Essays on Theology and Ethics | C. S. Lewis |
| `shadowlands` | Shadowlands | Brian Sibley |

#### `cognitive` — 2/32 沒人認領（目前：thinking(23)、science(12)、gardner(7)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `beast-gentleman` | 野獸紳士 | 巫家民 |
| `less-is-more` | Less Is More | Jason Hickel |

#### `databases` — 2/10 沒人認領（目前：data-systems(8)、fowler(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `art-of-postgresql` | The Art of PostgreSQL | Dimitri Fontaine |
| `postgresql-14-internals` | PostgreSQL 14 Internals | Egor Rogov |

#### `vision` — 2/45 沒人認領（目前：leadership(39)、management(7)、business-strategy(5)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `power-of-servant-leadership` | The Power of Servant-Leadership | Robert K. Greenleaf |
| `servant-leadership` | Servant Leadership: Attitudes, Skills and Behaviours | Larry W. Boone |

#### `discipline` — 2/5 沒人認領（目前：habits(2)、writing(1)、cloud(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `positive-discipline` | Positive Discipline | Jane Nelsen |
| `power-of-action` | 行動的力量 | 謝文憲 |

#### `non-fiction` — 2/19 沒人認領（目前：writing(15)、learning(1)、philosophy(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `wild-at-heart` | 我心狂野 | 艾傑奇 (John Eldredge) |
| `working-poor` | The Working Poor | David K. Shipler |

#### `visual` — 2/14 沒人認領（目前：design(11)、problem-solving(1)、de-botton(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `only-sales-guide` | The Only Sales Guide You'll Ever Need | Anthony Iannarino |
| `wtf-what-is-the-future` | WTF? What's the Future and Why It's Up to Us | Tim O'Reilly |

#### `coffee` — 2/2 沒人認領（目前：**沒有站在管**）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `uncommon-grounds` | Uncommon Grounds | Mark Pendergrast |
| `world-atlas-of-coffee` | The World Atlas of Coffee | James Hoffmann |

#### `fiction` — 2/7 沒人認領（目前：writing(4)、lewis(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `brothers-karamazov` | The Brothers Karamazov | Fyodor Dostoyevsky |
| `crime-and-punishment` | Crime and Punishment | Fyodor Dostoevsky |

#### `engineering-management` — 2/5 沒人認領（目前：agile(1)、cloud-infra(1)、career(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `become-an-effective-software-engineering-manager` | Become an Effective Software Engineering Manager | James Stanier |
| `effective-engineer` | The Effective Engineer | Edmond Lau |

#### `mental-health` — 1/14 沒人認領（目前：wellness(13)、life-meaning(5)、fengtang(2)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `forgiveness-and-reconciliation` | Forgiveness and Reconciliation: Initiating Individuation and Enabling Liberation | Monika Renz |

#### `discipleship` — 1/12 沒人認領（目前：spiritual-formation(7)、willard(4)、pastoral-psychology(2)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `after-you-believe` | After You Believe: Why Christian Character Matters | N. T. Wright |

#### `eastern` — 1/2 沒人認領（目前：philosophy(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `seven-stages-of-money-maturity` | The Seven Stages of Money Maturity | George Kinder |

#### `marriage` — 1/8 沒人認領（目前：relationships(5)、templar(1)、cloud(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `be-a-better-dad-today` | Be a Better Dad Today | Gregory W. Slayton |

#### `resilience` — 1/9 沒人認領（目前：life-meaning(5)、growth(3)、habits(2)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `resilience-hbr` | Resilience (HBR Emotional Intelligence Series) | Harvard Business Review |

#### `devops` — 1/12 沒人認領（目前：cloud-infra(11)、system-design(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `kubernetes-patterns` | Kubernetes Patterns | Bilgin Ibryam & Roland Huß |

#### `modern` — 1/9 沒人認領（目前：history(7)、drucker(2)、fromm(2)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `whats-wrong-with-the-world` | What's Wrong with the World | G. K. Chesterton |

#### `self-awareness` — 1/6 沒人認領（目前：growth(5)、career(1)、greene(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `your-turn` | Your Turn | Julie Lythcott-Haims |

#### `parenting` — 1/6 沒人認領（目前：relationships(4)、templar(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `raising-children-with-survival-skills` | 教出孩子的生存力 | 大前研一 |

#### `nutrition` — 1/5 沒人認領（目前：wellness(4)、life-meaning(2)、hbr(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `ignore-everybody` | Ignore Everybody | Hugh MacLeod |

#### `screenwriting` — 1/2 沒人認領（目前：communication(1)、writing(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `action-mckee` | Action | Robert McKee & Bassim El-Wakil |

#### `devotional` — 1/12 沒人認領（目前：spiritual-formation(8)、lewis(6)、nouwen(3)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `adam` | adam | ⚠ 描述沒有作者欄 |

#### `historical` — 1/6 沒人認領（目前：theology(5)、stott(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `story-of-christianity-vol-2` | The Story of Christianity, Vol. 2 | Justo L. González |

#### `dating` — 1/9 沒人認領（目前：relationships(7)、life-meaning(1)、peck(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `secrets-of-sexual-body-language` | Secrets of Sexual Body Language | Martin Lloyd-Elliott |

#### `job-search` — 1/10 沒人認領（目前：career(9)、behaviour-interview(7)、management(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `cracking-the-pm-interview` | Cracking the PM Interview | Gayle Laakmann McDowell & Jackie Bavaro |

#### `ai-ml` — 1/3 沒人認領（目前：system-design(2)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `mastering-ai-survival-guide` | Mastering AI: A Survival Guide to Our Superpowered Future | Jeremy Kahn |

#### `architecture` — 1/1 沒人認領（目前：**沒有站在管**）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `timeless-way-of-building` | The Timeless Way of Building | Christopher Alexander |

#### `marketing` — 1/22 沒人認領（目前：marketing(20)、tracy(2)、writing(1)）

| 書 repo | 書名 | 作者 |
| --- | --- | --- |
| `30-day-mba` | The 30 Day MBA | Colin Barrow |

## 二、死鏈 slug：0 個

bibliography 的 `slug` 在書庫裡找不到對應 repo——**首頁書架的封面會 404**。兩種收法（2026-08-04 那批 8 個就是這樣分的）：書其實該有就**補建書 repo**，書根本不存在就**撤掉這筆 `slug`**，不要掛死鏈。

無——所有 `slug` 都指得到真的 repo。

## 三、`owned` 沒有 slug：0 筆

`owned` 的語意是「已經做成 `nplus.wiki/<slug>/` 書站」，slug 是必要條件。沒填 slug 的 `owned` **不會出現在首頁書架的封面列**，概念頁的 `furtherReading.anchor` 也無處可指——書登記了卻看不到。書真的有就補 slug；其實還沒收就改回 `wanted`。

無——每一筆 `owned` 都有 slug。

## 四、死鏈 anchor：4 個 slug

內容頁 `furtherReading` 的 `book:` 指到不存在的書 repo——延伸閱讀連結 404。[SOURCING-DEBT](./SOURCING-DEBT.md) 只驗過「頁有沒有 anchor」，沒驗過「anchor 到的書在不在」。

| book slug | 出現在哪些頁 |
| --- | --- |
| `forgiveness-and-reconciling` | `pastoral-psychology-note/concepts/ministry-practice/forgiveness-two-kinds.md` |
| `psychology-and-christianity-five-views` | `pastoral-psychology-note/concepts/integration/five-views.md` |
| `psychology-theology-and-spirituality` | `pastoral-psychology-note/concepts/integration/ministerial-not-magisterial.md` |
| `suffering-and-the-heart-of-god` | `pastoral-psychology-note/concepts/trauma-grief/trauma-informed-reading.md` |

## 重跑

```bash
notes-core/tools/export-orphan-books.py
```

認領一本孤兒＝在該站 `bibliography.ts` 加一筆 `status: "owned"` ＋ `slug: "<repo name>"`，
重跑就會從這裡消失。整個 leaf 都沒站在管就走 `/note-new-station`。
