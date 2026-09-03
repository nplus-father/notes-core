# ANCHOR 覆蓋不足

> **生成於 2026-09-03T19:41:45+08:00**｜由 `tools/export-anchor-gaps.py` 產生，**不要手改**——改資料源再重跑。

由 `tools/export-anchor-gaps.py` 產生。判準：頁面正文用到的**具名數字**（金額、百分比、年份、人次⋯⋯）在它 `furtherReading` 掛的那本書裡找得到，卻不在掛出去的 anchor 章節底下——讀者點「延伸閱讀」會落在找不到內容的章。

- 證據充分（同一章被 ≥2 個非年份數字命中）：**0** 頁
- 證據單薄（只有一個數字，或全靠裸年份）：136 頁——裸年份如「1990年」在任何一章都可能碰巧出現，不足以當證據，列在後面備查。
- 另有 166 筆數字在整本書摘裡查無。books-done 是摘要不是全文，全書才有的細節本來就不會進摘要，**這類不算違規**，只供抽查。

修法兩種：建議章是現掛 anchor 的**祖章**→ 直接擴大；是別的子樹 → 另加一條`furtherReading`。「建議 anchor」附的標題取自該章 `_index.md`，可直接當 label。

---

# 證據單薄（備查，先不動）

## agile-note / scrum/timebox-is-the-constraint.md

- 現掛：`essential-scrum` → `docs/01-core-concepts/04-sprints/`、`scrum-the-art-of-doing-twice-the-work-in-half-the-time` → `docs/04-time/`
- 建議 anchor：`essential-scrum` → `docs/02-roles/`「角色」（1 個數字）、`essential-scrum` → `docs/01-core-concepts/`「核心概念」（1 個數字、擴大）、`essential-scrum` → `docs/04-sprinting/`「衝刺進行」（1 個數字）
- 落空數字：15分鐘

## behaviour-interview-note / pitfalls/common-pitfalls.md

- 現掛：`mastering-behavioral-interviews` → `docs/00-introduction/06-common-pitfalls/`
- 建議 anchor：`mastering-behavioral-interviews` → `docs/03-refining-responses/`「精修回應」（1 個數字）、`mastering-behavioral-interviews` → `docs/05-appendix/`「附錄」（1 個數字）、`mastering-behavioral-interviews` → `docs/02-preparation-roadmap/`「準備藍圖」（1 個數字）
- 落空數字：60分鐘

## biblical-studies-note / new-testament/gospels-in-cultural-context.md

- 現掛：`new-testament-in-its-world` → `docs/01-beginning-to-study/`、`new-testament-in-its-world` → `docs/02-the-world-of-jesus/`
- 建議 anchor：`new-testament-in-its-world` → `docs/06-gospels/`「福音書」（1 個數字）
- 落空數字：75年

## business-strategy-note / business-models/company-of-one.md

- 現掛：`company-of-one` → `docs/part-1-starting-a-company-of-one/ch01-what-is-a-company-of-one`、`company-of-one` → `docs/part-1-starting-a-company-of-one/ch02-staying-small-as-the-end-goal`、`company-of-one` → `docs/part-2-defining-a-company-of-one/`
- 落空數字：1980年

## business-strategy-note / business-models/small-giants-choice.md

- 現掛：`small-giants` → `docs/introduction`、`small-giants` → `docs/07-how-small-giants-fail`
- 建議 anchor：`small-giants` → `docs/05-a-culture-of-intimacy/`「親密的文化」（1 個數字）
- 落空數字：1978年、65%

## business-strategy-note / competitive-strategy/network-effects.md

- 現掛：`seven-powers-foundations-business-strategy` → `docs/01-strategy-statics/02-network-economies/`
- 建議 anchor：`seven-powers-foundations-business-strategy` → `docs/02-strategy-dynamics/`「策略動態」（1 個數字）
- 落空數字：5000萬

## business-strategy-note / competitive-strategy/strategic-inflection-point.md

- 現掛：`only-the-paranoid-survive` → `docs/03-strategic-inflection-point/`
- 建議 anchor：`only-the-paranoid-survive` → `docs/02-10x-change/`「10 倍速變化」（1 個數字）
- 落空數字：40%

## business-strategy-note / execution/capital-allocation.md

- 現掛：`outsiders` → `docs/09-radical-rationality/`、`outsiders` → `docs/02-unconventional-conglomerateur-henry-singleton/`
- 建議 anchor：`outsiders` → `docs/01-perpetual-motion-machine-tom-murphy/`「永動的回報機器：Tom Murphy 與 Capital Cities」（1 個數字）
- 落空數字：204美元

## business-strategy-note / management/business-adventures-lessons.md

- 現掛：`business-adventures` → `docs/02-fate-of-the-edsel`、`business-adventures` → `docs/07-impacted-philosophers`、`business-adventures` → `docs/06-making-customers-whole/`、`business-adventures` → `docs/01-fluctuation-little-crash/`
- 落空數字：1938年、1950年、1966年

## career-note / grit-mastery/ultralearning-projects.md

- 現掛：`ultralearning` → `docs/02-why-ultralearning-matters/`、`ultralearning` → `docs/06-directness-go-straight/`、`ultralearning` → `docs/13-first-ultralearning-project/`
- 建議 anchor：`ultralearning` → `docs/09-feedback-dont-dodge/`「原則 6 回饋：別躲避拳擊」（1 個數字）
- 落空數字：38%

## career-note / manage-yourself/find-a-sponsor-not-mentor.md

- 現掛：`forget-a-mentor-find-a-sponsor` → `docs/01-the-sponsor-effect/`、`smart-not-loud` → `docs/03-make-yourself-known/`
- 建議 anchor：`forget-a-mentor-find-a-sponsor` → `docs/07-distinguish-yourself/`「讓自己脫穎而出」（1 個數字）
- 落空數字：32%

## career-note / range-exploration/sampling-period.md

- 現掛：`range-why-generalists-triumph` → `docs/ch03-music-prodigies/`、`range-why-generalists-triumph` → `docs/ch04-slow-learning-wins/`
- 落空數字：2014年

## cloud-note / boundaries/boundaries-for-leaders.md

- 現掛：`boundaries-for-leaders` → `docs/01-people-are-the-plan/`、`boundaries-for-leaders` → `docs/02-ridiculously-in-charge/`
- 建議 anchor：`boundaries-for-leaders` → `docs/03-leading-so-brains-can-work/`「領導，讓大腦能工作」（1 個數字）、`boundaries-for-leaders` → `docs/05-power-through-connection/`「透過連結展現力量」（1 個數字）
- 落空數字：20分鐘

## communication-note / persuasion/pre-suasion-framing.md

- 現掛：`pre-suasion` → `docs/01-frontloading-of-attention/`
- 建議 anchor：`pre-suasion` → `docs/03-best-practices-optimization/`「最佳實踐：鋪梗力的最佳化」（1 個數字）
- 落空數字：585家

## communication-note / presentation/talk-like-ted.md

- 現掛：`talk-like-ted` → `docs/02-emotional/`、`talk-like-ted` → `docs/03-novel/`
- 建議 anchor：`talk-like-ted` → `docs/01-preface/`「前言：構想是二十一世紀的貨幣」（1 個數字）、`talk-like-ted` → `docs/04-memorable/`「令人印象深刻」（1 個數字）
- 落空數字：18分鐘

## communication-note / social/talking-to-strangers-traps.md

- 現掛：`talking-to-strangers` → `docs/02-default-to-truth`、`talking-to-strangers` → `docs/05-coupling`
- 建議 anchor：`talking-to-strangers` → `docs/03-transparency/`「透明性」（1 個數字）
- 落空數字：100萬

## communication-note / storytelling/four-business-stories.md

- 現掛：`stories-that-stick` → `docs/02-four-essential-stories`、`stories-that-stick` → `docs/01-irresistible-power-of-storytelling/03-what-makes-a-story-great`
- 建議 anchor：`stories-that-stick` → `docs/01-irresistible-power-of-storytelling/`「故事的不可抗拒力量」（1 個數字、擴大）、`stories-that-stick` → `docs/03-create-your-story/`「創造你的故事」（1 個數字）
- 落空數字：2015年、95%

## design-patterns-note / principles/timeless-way-and-pattern-language.md

- 現掛：`timeless-way-of-building` → `docs/01-the-timeless-way/`、`timeless-way-of-building` → `docs/02-the-quality/01-the-quality-without-a-name/`、`timeless-way-of-building` → `docs/02-the-quality/05-patterns-which-are-alive/`、`timeless-way-of-building` → `docs/03-the-gate/02-our-pattern-languages/`、`timeless-way-of-building` → `docs/03-the-gate/05-the-breakdown-of-language/`、`timeless-way-of-building` → `docs/03-the-gate/07-the-reality-of-patterns/`、`timeless-way-of-building` → `docs/05-the-kernel-of-the-way/`
- 建議 anchor：`timeless-way-of-building` → `docs/03-the-gate/`「大門」（1 個數字、擴大）
- 落空數字：253個

## drucker-note / innovation/entrepreneurial-management.md

- 現掛：`innovation-and-entrepreneurship` → `docs/02-practice-of-entrepreneurship/12-entrepreneurial-management/`
- 落空數字：2000年

## drucker-note / innovation/purposeful-innovation.md

- 現掛：`innovation-and-entrepreneurship` → `docs/01-practice-of-innovation/11-principles-of-innovation/`
- 落空數字：1880年、1914年

## drucker-note / management/five-questions.md

- 現掛：`five-most-important-questions` → `docs/01-what-is-our-mission/`
- 落空數字：1912年

## economics-note / econ-foundations/schools-of-economic-thought.md

- 現掛：`50-economics-ideas` → `docs/09-keynesianism/`、`50-economics-ideas` → `docs/10-monetarism/`、`50-economics-ideas` → `docs/13-supply-side-economics/`、`little-history-of-economics` → `docs/16-man-with-a-plan/`、`general-theory-of-employment-interest-and-money` → `docs/01-introduction/03-the-principle-of-effective-demand/`、`general-theory-of-employment-interest-and-money` → `docs/03-the-propensity-to-consume/03-the-marginal-propensity-to-consume-and-the-multiplier/`、`general-theory-of-employment-interest-and-money` → `docs/04-the-inducement-to-invest/02-the-state-of-long-term-expectation/`、`general-theory-of-employment-interest-and-money` → `docs/06-short-notes-suggested-by-the-general-theory/03-concluding-notes-on-social-philosophy/`、`animal-spirits` → `docs/introduction/`、`animal-spirits` → `docs/01-animal-spirits/01-confidence-and-its-multipliers/`
- 建議 anchor：`little-history-of-economics` → `docs/27-fill-up-the-bath/`「把浴缸注滿」（1 個數字）
- 落空數字：1964年、2500萬

## economics-note / financial-history/ascent-of-finance.md

- 現掛：`ascent-of-money` → `docs/01-dreams-of-avarice/`、`ascent-of-money` → `docs/02-of-human-bondage/`
- 建議 anchor：`ascent-of-money` → `docs/03-blowing-bubbles/`「吹泡泡」（1 個數字）
- 落空數字：1602年

## economics-note / financial-history/speculation-through-ages.md

- 現掛：`devil-take-the-hindmost` → `docs/01-this-bubble-world-origins-of-financial-speculation/`、`devil-take-the-hindmost` → `docs/02-stock-jobbing-in-change-alley/`、`devil-take-the-hindmost` → `docs/03-fools-gold-by-torchlight-south-sea-bubble-of-1720/`
- 落空數字：1871年

## economics-note / globalization-order/economics-for-the-planet.md

- 現掛：`how-economics-can-save-the-world` → `docs/01-eliminate-poverty/`、`how-economics-can-save-the-world` → `docs/02-raise-happy-children/`
- 建議 anchor：`how-economics-can-save-the-world` → `docs/03-fix-climate-change/`「如何解決氣候變遷」（1 個數字）、`how-economics-can-save-the-world` → `docs/05-give-people-what-they-need/`「如何給人們所需」（1 個數字）
- 落空數字：16次、1991年、3623人

## economics-note / money-central-banks/central-bank-privilege.md

- 現掛：`central-bank-privilege` → `docs/03-taiwan-interest-rate-policy/`、`central-bank-privilege` → `docs/04-taiwan-exchange-rate-policy/`、`central-bank-privilege` → `docs/06-profit-remittance/`、`central-bank-privilege` → `docs/08-summary-and-reform/`
- 建議 anchor：`central-bank-privilege` → `docs/preface/`「前言」（1 個數字）
- 落空數字：38.3%

## economics-note / money-central-banks/gold-standard-and-fetters.md

- 現掛：`lords-of-finance` → `docs/01-unexpected-storm/`、`lords-of-finance` → `docs/02-after-the-deluge/`
- 建議 anchor：`lords-of-finance` → `docs/03-sowing-a-new-wind/`「播下新風」（1 個數字）
- 落空數字：3.5%

## greene-note / power/daily-practice.md

- 現掛：`daily-laws` → `docs/00-preface/`
- 建議 anchor：`daily-laws` → `docs/09-september-the-grand-strategist/`「九月：偉大的戰略家」（1 個數字）、`daily-laws` → `docs/04-april-the-perfect-courtier/`「四月：完美的朝臣」（1 個數字）、`daily-laws` → `docs/12-december-the-cosmic-sublime/`「十二月：宇宙的崇高」（1 個數字）
- 落空數字：33條

## growth-note / deliberate-practice/role-of-the-teacher.md

- 現掛：`peak-secrets-from-the-new-science-of-expertise` → `docs/06-gold-standard/`
- 建議 anchor：`peak-secrets-from-the-new-science-of-expertise` → `docs/07-deliberate-practice-at-work/`「第 5 章：在工作上運用刻意練習原則」（1 個數字）
- 落空數字：2005年、62項

## growth-note / originals-potential/character-skills-over-talent.md

- 現掛：`hidden-potential` → `docs/01-skills-of-character/`
- 建議 anchor：`hidden-potential` → `docs/00-prologue/`「在水泥地長出玫瑰」（1 個數字）
- 落空數字：1980年、25歲

## growth-note / self-awareness/presence-before-performance.md

- 現掛：`presence` → `docs/01-what-is-presence/`、`presence` → `docs/02-believing-and-trusting-yourself/`
- 落空數字：1960年、1978年

## growth-note / self-awareness/think-like-sherlock.md

- 現掛：`mastermind-think-like-sherlock-holmes` → `docs/01-understanding-yourself/01-scientific-method-of-the-mind/`
- 落空數字：1834年

## growth-note / talent-grit/five-laws-of-success.md

- 現掛：`formula` → `docs/01-performance-drives-success/`、`formula` → `docs/02-when-performance-cant-be-measured-networks-determine-success/`、`formula` → `docs/03-past-success-x-fitness-equals-future-success/`、`formula` → `docs/05-with-persistence-success-can-come-at-any-time/`
- 建議 anchor：`formula` → `docs/04-team-success-needs-balance-and-diversity/`「團隊的成功需要平衡與多元」（1 個數字）
- 落空數字：23%

## habits-note / habit-loop/break-bad-habits.md

- 現掛：`atomic-habits` → `docs/the-2nd-law-make-it-attractive/10-how-to-find-and-fix-bad-habits/`、`atomic-habits` → `docs/the-1st-law-make-it-obvious/07-the-secret-to-self-control/`
- 建議 anchor：`atomic-habits` → `docs/advanced-tactics/`「如何從還不錯進化到真正卓越」（1 個數字）
- 落空數字：15%

## habits-note / habit-loop/change-by-obstacle.md

- 現掛：`how-to-change` → `docs/introduction`、`how-to-change` → `docs/01-getting-started`、`how-to-change` → `docs/03-procrastination/`、`how-to-change` → `docs/04-forgetfulness/`
- 建議 anchor：`how-to-change` → `docs/05-laziness/`「懶惰」（1 個數字）
- 落空數字：98%

## habits-note / habit-loop/hooked-model.md

- 現掛：`hooked` → `docs/02-trigger`、`hooked` → `docs/04-variable-reward`
- 建議 anchor：`hooked` → `docs/05-investment/`「投入」（1 個數字）
- 落空數字：63%

## hbr-note / communication-collab/smarter-networking.md

- 現掛：`hbr-guide-to-smarter-networking` → `docs/01-why-network/03-leaders-create-networks`、`hbr-guide-to-smarter-networking` → `docs/01-why-network/01-smarter-way`
- 建議 anchor：`hbr-guide-to-smarter-networking` → `docs/04-land-great-job/`「找到好工作」（1 個數字）
- 落空數字：100個

## hbr-note / communication-collab/toxic-workplace.md

- 現掛：`hbr-guide-to-navigating-the-toxic-workplace` → `docs/03-quit-or-stay/01-time-to-quit`、`hbr-guide-to-navigating-the-toxic-workplace` → `docs/04-managing-toxic-team/03-toxic-employee`、`hbr-guide-to-navigating-the-toxic-workplace` → `docs/02-toxic-boss/`、`hbr-guide-to-navigating-the-toxic-workplace` → `docs/06-action-from-top/`
- 建議 anchor：`hbr-guide-to-navigating-the-toxic-workplace` → `docs/01-harmful-environment/`「在有害環境中工作」（1 個數字）、`hbr-guide-to-navigating-the-toxic-workplace` → `docs/04-managing-toxic-team/`「在毒性職場帶團隊」（1 個數字、擴大）、`hbr-guide-to-navigating-the-toxic-workplace` → `docs/05-culture-toxicity/`「當文化導向毒性」（1 個數字）
- 落空數字：12000美元、70%、94%

## hbr-note / leadership-teams/hiring-for-fit.md

- 現掛：`hbr-guide-to-better-recruiting-and-hiring` → `docs/03-effective-interviews`、`hbr-guide-to-retaining-your-best-people` → `docs/01-getting-started/03-onboarding-make-or-break`
- 建議 anchor：`hbr-guide-to-better-recruiting-and-hiring` → `docs/01-understand-process/`「了解流程」（1 個數字）
- 落空數字：89%

## hbr-note / self-management/beating-burnout.md

- 現掛：`hbr-guide-to-beating-burnout` → `docs/01-protect-yourself/02-six-causes`、`hbr-guide-to-managing-stress-at-work` → `docs/04-tools-that-work/03-feel-overwhelmed`、`hbr-guide-to-better-mental-health-at-work` → `docs/04-supporting-as-manager/01-reduce-stigma`
- 建議 anchor：`hbr-guide-to-beating-burnout` → `docs/04-organization-action/`「組織的行動」（1 個數字）
- 落空數字：300美元

## hbr-note / strategy-innovation/ai-for-managers.md

- 現掛：`hbr-guide-to-ai-basics-for-managers` → `docs/01-ai-fundamentals/01-three-questions`、`hbr-guide-to-generative-ai-for-managers` → `docs/01-essentials/02-co-pilot-co-thinker`、`hbr-guide-to-ai-basics-for-managers` → `docs/05-ethics-and-bias/`、`hbr-guide-to-ai-basics-for-managers` → `docs/01-ai-fundamentals/04-ai-not-too-complicated/`、`hbr-guide-to-ai-basics-for-managers` → `docs/04-working-with-ai/02-employees-embrace-ai/`
- 建議 anchor：`hbr-guide-to-ai-basics-for-managers` → `docs/01-ai-fundamentals/`「AI基礎」（1 個數字、擴大）
- 落空數字：86%

## hbr-note / strategy-innovation/better-decisions.md

- 現掛：`hbr-guide-to-making-better-decisions` → `docs/01-getting-started/01-hidden-traps`、`hbr-guide-to-critical-thinking` → `docs/03-ask-questions/02-four-types-of-questions`
- 建議 anchor：`hbr-guide-to-making-better-decisions` → `docs/01-getting-started/`「入門」（1 個數字、擴大）
- 落空數字：10%

## hbr-note / strategy-innovation/manager-data-literacy.md

- 現掛：`hbr-guide-to-data-analytics-basics-for-managers` → `docs/01-getting-started/01-keep-up-with-quants`、`hbr-guide-to-finance-basics-for-managers` → `docs/01-the-key-financial-statements`、`hbr-guide-to-finance-basics-for-managers` → `docs/03-what-the-financial-statements-dont-tell-you/`、`hbr-guide-to-data-analytics-basics-for-managers` → `docs/02-gather-information/`
- 建議 anchor：`hbr-guide-to-finance-basics-for-managers` → `docs/02-making-good-decisions-and-moving-those-numbers/`「做好決策——推動那些數字」（1 個數字）
- 落空數字：1992年、72天

## hbr-note / strategy-innovation/unlocking-creativity.md

- 現掛：`hbr-guide-to-unlocking-creativity` → `docs/01-unleash-your-creativity/01-creative-confidence`、`hbr-guide-to-unlocking-creativity` → `docs/04-make-org-creative/03-culture-of-originality`、`hbr-guide-to-unlocking-creativity` → `docs/01-unleash-your-creativity/02-train-brain/`、`hbr-guide-to-unlocking-creativity` → `docs/04-make-org-creative/02-unlock-team-creativity/`
- 建議 anchor：`hbr-guide-to-unlocking-creativity` → `docs/04-make-org-creative/`「讓你的組織更有創意」（1 個數字、擴大）
- 落空數字：34%

## history-note / ancient-origins/axial-age-ideas.md

- 現掛：`greatest-minds-and-ideas-of-all-time` → `docs/01-shameless-worship-of-heroes/`、`greatest-minds-and-ideas-of-all-time` → `docs/02-ten-greatest-thinkers/`
- 建議 anchor：`greatest-minds-and-ideas-of-all-time` → `docs/06-twelve-vital-dates-in-history/`「世界史上的十二個關鍵日期」（1 個數字）
- 落空數字：1543年

## history-note / culture-society/table-manners-as-order.md

- 現掛：`rituals-of-dinner` → `docs/01-behaving/`、`rituals-of-dinner` → `docs/02-learning-to-behave/`
- 落空數字：1931年

## history-note / historical-thinking/factful-worldview.md

- 現掛：`how-i-learned-to-understand-the-world` → `docs/01-from-illiteracy-to-academic-excellence/`、`how-i-learned-to-understand-the-world` → `docs/02-discovering-the-world/`
- 建議 anchor：`how-i-learned-to-understand-the-world` → `docs/05-from-research-to-teaching/`「從研究到教學」（1 個數字）
- 落空數字：50%

## history-note / historical-thinking/history-of-risk.md

- 現掛：`against-the-gods` → `docs/01-beginnings/`、`against-the-gods` → `docs/02-thousand-outstanding-facts/`
- 建議 anchor：`against-the-gods` → `docs/03-measurement-unlimited/`「無限度量（1700-1900）」（1 個數字）、`against-the-gods` → `docs/introduction/`「前言」（1 個數字）
- 落空數字：1738年、1921年

## history-note / modern-history/digital-revolution.md

- 現掛：`innovators` → `docs/01-ada-lovelace/`、`innovators` → `docs/02-the-computer/`
- 落空數字：1959年

## history-note / war-military/why-wars-are-won.md

- 現掛：`how-to-fight-a-war` → `docs/01-strategy-and-intelligence/`、`how-to-fight-a-war` → `docs/02-logistics/`
- 落空數字：1945年

## investing-note / index-passive/cost-matters-and-the-index.md

- 現掛：`little-book-of-common-sense-investing` → `docs/01-the-parable-of-the-gotrocks-family/`、`little-book-of-common-sense-investing` → `docs/02-rational-exuberance/`
- 建議 anchor：`little-book-of-common-sense-investing` → `docs/18-asset-allocation-principles-and-strategies/`「資產配置一：原則與策略」（1 個數字）
- 落空數字：0.05%

## investing-note / index-passive/efficient-market-and-random-walk.md

- 現掛：`a-random-walk-down-wall-street` → `docs/1-stocks-and-their-value/`、`a-random-walk-down-wall-street` → `docs/2-how-the-pros-play-the-biggest-game-in-town/`、`man-who-solved-the-market` → `docs/10-this-isnt-science-its-gambling/`
- 建議 anchor：`man-who-solved-the-market` → `docs/11-im-doing-things-i-dont-need-to-do/`「我在做我不需要做的事」（1 個數字）
- 落空數字：11美元

## investing-note / index-passive/equities-for-the-long-run.md

- 現掛：`stocks-for-the-long-run` → `docs/01-verdict-of-history/01-stock-and-bond-returns`、`common-sense-on-mutual-funds` → `docs/01-strategy/02-the-nature-of-returns`、`unconventional-success` → `docs/02-asset-allocation`
- 建議 anchor：`stocks-for-the-long-run` → `docs/01-verdict-of-history/`「歷史的裁決」（1 個數字、擴大）
- 落空數字：1929年、2.6%

## investing-note / investor-psychology/overconfidence-and-hindsight.md

- 現掛：`little-book-of-behavioral-investing` → `docs/01-in-the-heat-of-the-moment/`、`little-book-of-behavioral-investing` → `docs/02-afraid-of-big-bad-market/`、`little-book-of-behavioral-investing` → `docs/05-folly-of-forecasting/`
- 落空數字：1814年

## investing-note / stock-picking/canslim-and-momentum.md

- 現掛：`how-to-make-money-in-stocks` → `docs/01-a-winning-system/`、`how-to-make-money-in-stocks` → `docs/02-can-slim-method/`
- 建議 anchor：`how-to-make-money-in-stocks` → `docs/03-buying-and-selling/`「一開始就要精明：買進賣出與資金管理」（1 個數字）
- 落空數字：200000美元

## investing-note / trading-speculation/position-sizing-and-ruin.md

- 現掛：`way-of-the-turtle` → `docs/03-risk-junkies/`、`way-of-the-turtle` → `docs/04-taming-the-turtle-mind/`
- 建議 anchor：`way-of-the-turtle` → `docs/18-appendix-original-turtle-rules/`「附錄：原版海龜交易規則」（1 個數字）、`way-of-the-turtle` → `docs/10-risk-and-money-management/`「風險與資金管理」（1 個數字）
- 落空數字：1.5%

## investing-note / value-investing/low-risk-high-uncertainty.md

- 現掛：`dhandho-investor` → `docs/13-low-risk-high-uncertainty`、`education-of-a-value-investor` → `docs/08-the-buffett-lunch/`、`snowball-warren-buffett` → `docs/03-the-racetrack/`
- 建議 anchor：`dhandho-investor` → `docs/10-few-bets-big-bets/`「少下注重下注」（1 個數字）
- 落空數字：77個

## kent-beck-note / smalltalk/why-patterns-work.md

- 現掛：`smalltalk-best-practice-patterns` → `docs/02-patterns/01-why-patterns-work/`
- 建議 anchor：`smalltalk-best-practice-patterns` → `docs/preface/`「前言」（1 個數字）、`smalltalk-best-practice-patterns` → `docs/01-introduction/`「導論」（1 個數字）
- 落空數字：92個

## kent-beck-note / tidy/first-after-later-never.md

- 現掛：`tidy-first` → `docs/02-managing/06-first-after-later-never/`、`tidy-first` → `docs/02-managing/03-batch-sizes/`
- 建議 anchor：`tidy-first` → `docs/02-managing/`「管理」（1 個數字、擴大）
- 落空數字：20%

## leadership-note / change/why-transformations-fail.md

- 現掛：`leading-change` → `docs/01-the-change-problem-and-its-solution/01-transforming-organizations-why-firms-fail/`、`leading-change` → `docs/01-the-change-problem-and-its-solution/02-successful-change-and-the-force-that-drives-it/`
- 落空數字：1994年、1995年

## leadership-note / coaching/seven-essential-questions.md

- 現掛：`coaching-habit` → `docs/03-the-seven-essential-questions/`、`coaching-habit` → `docs/03-the-seven-essential-questions/02-the-awe-question/`、`coaching-habit` → `docs/03-the-seven-essential-questions/05-the-lazy-question/`、`coaching-habit` → `docs/03-the-seven-essential-questions/06-the-strategic-question/`、`coaching-habit` → `docs/02-how-to-build-a-habit/`
- 建議 anchor：`coaching-habit` → `docs/01-you-need-a-coaching-habit/`「你需要一個教練習慣」（1 個數字）
- 落空數字：2006年、73%

## leadership-note / culture/belonging-cues.md

- 現掛：`culture-code` → `docs/01-build-safety/`、`culture-code` → `docs/02-share-vulnerability/02-the-vulnerability-loop/`、`culture-code` → `docs/03-establish-purpose/`
- 建議 anchor：`culture-code` → `docs/introduction/`「二加二等於十的時候」（1 個數字）
- 落空數字：756%

## leadership-note / culture/culture-is-behavior.md

- 現掛：`what-you-do-is-who-you-are` → `docs/07-be-yourself-design-your-culture/`、`what-you-do-is-who-you-are` → `docs/03-the-way-of-the-warrior/`、`what-you-do-is-who-you-are` → `docs/06-genghis-khan-master-of-inclusion/`
- 建議 anchor：`what-you-do-is-who-you-are` → `docs/08-edge-cases-and-object-lessons/`「邊界情境與案例教訓」（1 個數字）
- 落空數字：1999年、830億

## leadership-note / culture/values-into-rituals.md

- 現掛：`delivering-happiness` → `docs/03-profits-passion-and-purpose/01-taking-it-to-the-next-level/`、`delivering-happiness` → `docs/02-profits-and-passion/02-platform-for-growth/`
- 落空數字：1999年

## leadership-note / decisions/intelligent-failure.md

- 現掛：`right-kind-of-wrong` → `docs/01-failure-types/01-chasing-the-right-kind-of-wrong/`、`right-kind-of-wrong` → `docs/01-failure-types/02-eureka-intelligent-failure/`、`right-kind-of-wrong` → `docs/01-failure-types/03-to-err-is-human/`
- 落空數字：1992年

## leadership-note / mindset/adversity-quotient.md

- 現掛：`adversity-quotient` → `docs/02-ascend-mt-success/`、`adversity-quotient` → `docs/04-aq-and-learned-helplessness/`、`adversity-quotient` → `docs/07-the-aq-continuum/`、`adversity-quotient` → `docs/10-twelve-ways-to-nurture-aq/`
- 建議 anchor：`adversity-quotient` → `docs/03-aqs-scientific-building-blocks/`「AQ的科學基石」（1 個數字）
- 落空數字：25歲

## leadership-note / mindset/five-practices.md

- 現掛：`leadership-challenge` → `docs/01-when-leaders-are-at-their-best/`、`leadership-challenge` → `docs/02-model-the-way/`、`leadership-challenge` → `docs/07-leadership-is-everyones-business/`
- 建議 anchor：`leadership-challenge` → `docs/introduction/`「導論」（1 個數字）
- 落空數字：1982年、75萬

## leadership-note / mindset/how-leaders-fail.md

- 現掛：`ten-commandments-for-business-failure` → `docs/02-quit-taking-risks/`、`ten-commandments-for-business-failure` → `docs/04-isolate-yourself/`、`ten-commandments-for-business-failure` → `docs/05-never-admit-mistakes/`、`ten-commandments-for-business-failure` → `docs/07-dont-think/`、`ten-commandments-for-business-failure` → `docs/09-love-bureaucracy/`、`ten-commandments-for-business-failure` → `docs/03-be-inflexible/`
- 建議 anchor：`ten-commandments-for-business-failure` → `docs/08-trust-experts-blindly/`「第七誡：若要失敗，就盡信專家與外部顧問」（1 個數字）
- 落空數字：45%

## leadership-note / team/find-leverage-points.md

- 現掛：`reset` → `docs/01-find-the-leverage-points/`、`reset` → `docs/02-restack-the-resources/`、`reset` → `docs/05-engage-the-people-doing-the-work/`
- 建議 anchor：`reset` → `docs/introduction/`「前言」（1 個數字）
- 落空數字：76%

## leadership-note / team/hiring-and-keeping.md

- 現掛：`hbr-guide-to-better-recruiting-and-hiring` → `docs/01-understand-process/01-hire-top-talent/`、`hbr-guide-to-better-recruiting-and-hiring` → `docs/04-better-questions/01-seven-rules/`、`hbr-guide-to-better-recruiting-and-hiring` → `docs/05-assess-and-decide/03-scorecard/`、`hire-and-keep-the-best-people` → `docs/01-the-most-important-decision/`、`hire-and-keep-the-best-people` → `docs/15-retain-your-top-performers/`、`hbr-guide-to-retaining-your-best-people` → `docs/01-getting-started/01-why-employees-quit/`、`hbr-guide-to-retaining-your-best-people` → `docs/02-connect-with-team/02-mattering-is-key/`
- 建議 anchor：`hbr-guide-to-better-recruiting-and-hiring` → `docs/01-understand-process/`「了解流程」（1 個數字、擴大）
- 落空數字：89%

## leadership-note / vision/disruption-dilemma.md

- 現掛：`innovators-dilemma` → `docs/01-why-great-companies-can-fail/01-how-can-great-firms-fail/`、`innovators-dilemma` → `docs/01-why-great-companies-can-fail/02-value-networks/`、`innovators-dilemma` → `docs/02-managing-disruptive-change/05-give-responsibility/`
- 建議 anchor：`innovators-dilemma` → `docs/02-managing-disruptive-change/`「管理破壞式技術變革」（1 個數字、擴大）、`innovators-dilemma` → `docs/01-why-great-companies-can-fail/`「為什麼偉大的公司會失敗」（1 個數字、擴大）
- 落空數字：1986年、37%、90%

## leadership-note / vision/golden-circle.md

- 現掛：`start-with-why` → `docs/02-an-alternative-perspective/03-the-golden-circle/`、`start-with-why` → `docs/02-an-alternative-perspective/04-this-is-not-opinion-this-is-biology/`、`start-with-why` → `docs/03-leaders-need-a-following/06-the-emergence-of-trust/`
- 建議 anchor：`start-with-why` → `docs/03-leaders-need-a-following/`「領導者需要追隨者」（1 個數字、擴大）
- 落空數字：1903年、25萬

## leadership-note / vision/okr.md

- 現掛：`measure-what-matters` → `docs/01-okrs-in-action/02-father-of-okrs/`、`measure-what-matters` → `docs/01-okrs-in-action/03-operation-crush/`、`measure-what-matters` → `docs/02-new-world-of-work/15-continuous-performance/`、`high-output-management` → `docs/08-planning-todays-actions-for-tomorrows-output/`
- 建議 anchor：`measure-what-matters` → `docs/01-okrs-in-action/`「OKR實戰」（1 個數字、擴大）
- 落空數字：1999年、50%

## learning-note / metacognition/mental-models.md

- 現掛：`fifth-discipline` → `docs/01-diagnose-your-organization/`、`fifth-discipline` → `docs/02-new-thinking-new-vision/`
- 建議 anchor：`fifth-discipline` → `docs/03-four-core-disciplines/`「四項核心修煉」（1 個數字）
- 落空數字：38%

## learning-note / practice/deliberate-practice-basics.md

- 現掛：`peak-secrets-from-the-new-science-of-expertise` → `docs/03-purposeful-practice/`、`peak-secrets-from-the-new-science-of-expertise` → `docs/04-harnessing-adaptability/`
- 建議 anchor：`peak-secrets-from-the-new-science-of-expertise` → `docs/01-forewords/`「推薦序」（1 個數字）、`peak-secrets-from-the-new-science-of-expertise` → `docs/06-gold-standard/`「第 4 章：刻意練習的黃金法則」（1 個數字）
- 落空數字：7401小時

## learning-note / practice/feedback-loop-practice.md

- 現掛：`learn-better` → `docs/01-value/`、`learn-better` → `docs/02-target/`
- 建議 anchor：`learn-better` → `docs/03-develop/`「發展」（1 個數字）
- 落空數字：17歲

## learning-note / self-learning/directness.md

- 現掛：`ultralearning` → `docs/01-mit-education-without-mit/`、`ultralearning` → `docs/02-why-ultralearning-matters/`
- 落空數字：1901年

## life-meaning-note / body-wellness/first-90-minutes.md

- 現掛：`stanford-method-of-sleep` → `docs/04-golden-90-minutes/`
- 建議 anchor：`stanford-method-of-sleep` → `docs/06-wakefulness-strategy/`「史丹佛式清醒策略」（1 個數字）
- 落空數字：24.2小時

## life-meaning-note / body-wellness/sleep-pressure-and-rhythm.md

- 現掛：`why-we-sleep` → `docs/01-this-thing-called-sleep/03-defining-and-generating-sleep/`、`why-we-sleep` → `docs/01-this-thing-called-sleep/02-caffeine-jet-lag-and-melatonin/`
- 建議 anchor：`why-we-sleep` → `docs/02-why-should-you-sleep/`「你為什麼該睡覺？」（1 個數字）
- 落空數字：24小時

## life-meaning-note / emotion/let-them.md

- 現掛：`let-them-theory` → `docs/01-the-let-them-theory/`
- 建議 anchor：`let-them-theory` → `docs/introduction/`「前言：我的故事」（1 個數字）
- 落空數字：41歲

## life-meaning-note / emotion/paradox-of-choice.md

- 現掛：`paradox-of-choice` → `docs/03-why-we-suffer/`
- 建議 anchor：`paradox-of-choice` → `docs/02-how-we-choose/`「我們如何選擇」（1 個數字）、`paradox-of-choice` → `docs/01-when-we-choose/`「我們什麼時候選擇」（1 個數字）
- 落空數字：89美元

## life-meaning-note / meaning/attitude-is-a-choice.md

- 現掛：`difference-maker` → `docs/03-what-attitude-can-do/`、`difference-maker` → `docs/04-make-attitude-greatest-asset/`
- 落空數字：1978年

## life-meaning-note / meaning/redefine-retirement.md

- 現掛：`joy-of-not-working` → `docs/07-lighting-your-own-fire/`
- 建議 anchor：`joy-of-not-working` → `docs/08-dynamic-inaction/`「動態的不作為一事無成」（1 個數字）
- 落空數字：26小時

## management-note / org-people/centralization-and-decentralization.md

- 現掛：`concept-of-the-corporation` → `docs/02-corporation-as-human-effort/02-decentralization`、`concept-of-the-corporation` → `docs/02-corporation-as-human-effort/05-decentralization-as-a-model`、`concept-of-the-corporation` → `docs/03-corporation-as-social-institution/`
- 落空數字：1943年、1950年

## management-note / org-people/first-who-then-what.md

- 現掛：`good-to-great` → `docs/03-first-who-then-what/`、`built-to-last` → `docs/02-clock-building-not-time-telling/`、`no-rules-rules` → `docs/section-3-techniques-to-reinforce/07-the-keeper-test/`
- 建議 anchor：`good-to-great` → `docs/02-level-5-leadership/`「第五級領導」（1 個數字）
- 落空數字：2001年、21年

## management-note / org-people/trust-and-team-dysfunctions.md

- 現掛：`five-dysfunctions-of-a-team` → `docs/06-the-model/`、`crucial-conversations` → `docs/05-make-it-safe/`
- 建議 anchor：`crucial-conversations` → `docs/02-mastering-crucial-conversations/`「掌握關鍵對話」（1 個數字）
- 落空數字：100%

## marketing-note / demand-offer/money-models.md

- 現掛：`100m-money-models` → `docs/02-what-is-a-money-model/`、`100m-money-models` → `docs/07-make-your-money-model/`
- 建議 anchor：`100m-money-models` → `docs/04-upsell-offers/`「加售方案」（1 個數字）
- 落空數字：11.6倍

## marketing-note / growth-launch/marketing-as-warfare.md

- 現掛：`marketing-tracy` → `docs/11-four-principles-of-strategy/`、`marketing-tracy` → `docs/15-the-frontal-assault/`、`marketing-tracy` → `docs/16-hit-em-where-they-aint/`、`marketing-tracy` → `docs/17-dominate-a-niche/`
- 建議 anchor：`marketing-tracy` → `docs/12-choosing-the-battlefield/`「Choosing The Battlefield」（1 個數字）
- 落空數字：50%

## marketing-note / growth-launch/marketing-mix-4p.md

- 現掛：`marketing-tracy` → `docs/05-the-marketing-mix-product/`、`marketing-tracy` → `docs/06-the-marketing-mix-price/`、`marketing-tracy` → `docs/07-the-marketing-mix-place/`
- 建議 anchor：`marketing-tracy` → `docs/18-creative-growth-strategies/`「Creative Growth Strategies」（1 個數字）、`marketing-tracy` → `docs/08-the-marketing-mix-promotion/`「The Marketing Mix Promotion」（1 個數字）
- 落空數字：2007年、80%

## marketing-note / positioning/power-of-the-name.md

- 現掛：`positioning` → `docs/09-power-of-the-name/`、`positioning` → `docs/10-no-name-trap/`、`positioning` → `docs/12-line-extension-trap/`
- 建議 anchor：`positioning` → `docs/11-free-ride-trap/`「搭便車陷阱」（1 個數字）
- 落空數字：8440萬

## marketing-note / positioning/smallest-viable-market.md

- 現掛：`this-is-marketing` → `docs/04-smallest-viable-market/`
- 建議 anchor：`this-is-marketing` → `docs/08-more-of-the-who/`「更多的「誰」」（1 個數字）
- 落空數字：1000個

## marketing-note / positioning/ten-step-positioning.md

- 現掛：`obviously-awesome` → `docs/01-what-is-positioning/`、`obviously-awesome` → `docs/02-the-10-step-positioning-process/`
- 落空數字：1981年

## maxwell-note / growth/difference-maker.md

- 現掛：`difference-maker` → `docs/03-what-attitude-can-do/`、`difference-maker` → `docs/02-what-attitude-cannot-do/`
- 建議 anchor：`difference-maker` → `docs/10-difference-maker-in-your-life/`「成為他人生命中的關鍵」（1 個數字）
- 落空數字：21歲

## maxwell-note / leadership/leadership-gold.md

- 現掛：`leadership-gold` → `docs/02-toughest-person-yourself/`、`leadership-gold` → `docs/03-defining-moments/`
- 建議 anchor：`leadership-gold` → `docs/preface/`「序言」（1 個數字）、`leadership-gold` → `docs/15-leaders-during-tough-times/`「領導者在困境中脫穎而出」（1 個數字）
- 落空數字：15個、52週

## newport-note / deep-work/attention-capital-principle.md

- 現掛：`a-world-without-email` → `docs/03-principles-for-a-world-without-email/01-the-attention-capital-principle/`、`a-world-without-email` → `docs/03-principles-for-a-world-without-email/02-the-process-principle/`、`a-world-without-email` → `docs/03-principles-for-a-world-without-email/03-the-protocol-principle/`、`a-world-without-email` → `docs/03-principles-for-a-world-without-email/04-the-specialization-principle/`
- 建議 anchor：`a-world-without-email` → `docs/03-principles-for-a-world-without-email/`「打造一個沒有 Email 的世界的原則」（1 個數字、擴大）
- 落空數字：1500年

## nt-wright-note / theology/simply-jesus.md

- 現掛：`simply-jesus` → `docs/03-the-perfect-storm/`、`simply-jesus` → `docs/11-space-time-and-matter/`、`simply-jesus` → `docs/15-jesus-the-ruler-of-the-world/`
- 建議 anchor：`simply-jesus` → `docs/09-the-kingdom-present-and-future/`「國度的現在與未來」（1 個數字）
- 落空數字：160年

## peck-note / community/different-drum.md

- 現掛：`different-drum` → `docs/01-foundation/`、`different-drum` → `docs/02-bridge/`
- 落空數字：1984年

## peck-note / evil/possession-and-exorcism.md

- 現掛：`glimpses-of-the-devil` → `docs/01-jersey/`、`glimpses-of-the-devil` → `docs/02-beccah/`、`glimpses-of-the-devil` → `docs/03-perspectives/`、`people-of-the-lie` → `docs/06-of-possession-and-exorcism/`
- 建議 anchor：`glimpses-of-the-devil` → `docs/introduction/`「我的導師「Leprechaun」」（1 個數字）
- 落空數字：99.9%

## relationships-note / connection/winning-with-people.md

- 現掛：`winning-with-people` → `docs/01-readiness-question/`
- 建議 anchor：`winning-with-people` → `docs/03-trust-question/`「第三問：信任提問──我們可以彼此信任嗎？」（1 個數字）
- 落空數字：152年

## science-note / scientific-method/factfulness-instincts.md

- 現掛：`factfulness` → `docs/01-the-gap-instinct`、`factfulness` → `docs/11-factfulness-in-practice`、`factfulness` → `docs/05-the-size-instinct/`
- 建議 anchor：`factfulness` → `docs/00-introduction/`「導論」（1 個數字）
- 落空數字：12000人、1800年

## science-note / scientific-method/how-false-beliefs-form.md

- 現掛：`how-we-know-what-isnt-so` → `docs/02-cognitive-determinants/01-something-out-of-nothing`、`quirkology` → `docs/03-believing-impossible`
- 建議 anchor：`how-we-know-what-isnt-so` → `docs/03-motivational-social-determinants/`「不實認知的動機與社會決定因子」（1 個數字）
- 落空數字：94%

## science-note / scientific-method/refusing-to-reason.md

- 現掛：`irrational-ape` → `docs/08-schrodingers-bin-laden`、`irrational-ape` → `docs/21-a-healthy-scepticism`
- 建議 anchor：`irrational-ape` → `docs/01-an-indecent-proposition/`「理性的假象與形式謬誤」（1 個數字）
- 落空數字：1919年、1969年、897年

## startup-note / founder/10x-thinking.md

- 現掛：`10x-is-easier-than-2x` → `docs/01-10x-principles/01-surprising-simplicity-of-10x-growth/`
- 建議 anchor：`10x-is-easier-than-2x` → `docs/01-10x-principles/`「10倍原則」（1 個數字、擴大）
- 落空數字：250倍

## startup-note / money-exit/raise-or-bootstrap.md

- 現掛：`super-founders` → `docs/04-the-fundraising/01-vc-versus-bootstrapping/`、`art-of-the-start` → `docs/07-the-art-of-raising-capital/`
- 建議 anchor：`super-founders` → `docs/04-the-fundraising/`「第三部：募資」（1 個數字、擴大）
- 落空數字：70%

## startup-note / opportunity/market-beats-idea.md

- 現掛：`super-founders` → `docs/03-the-company/05-market/`、`super-founders` → `docs/03-the-company/07-competition/`
- 落空數字：1995年

## stott-note / foundations/incomparable-christ.md

- 現掛：`incomparable-christ` → `docs/01-the-original-jesus/`、`incomparable-christ` → `docs/03-the-influential-jesus/`
- 落空數字：2000年

## system-design-note / fundamentals/system-design-interview-framework.md

- 現掛：`system-design-interview` → `docs/04-a-framework-for-system-design-interviews/`
- 建議 anchor：`system-design-interview` → `docs/22-ad-click-event-aggregation/`「廣告點擊事件彙整」（1 個數字）、`system-design-interview` → `docs/28-digital-wallet/`「數位錢包」（1 個數字）、`system-design-interview` → `docs/02-scale-from-zero-to-millions-of-users/`「從零擴展到數百萬使用者」（1 個數字）
- 落空數字：12個

## system-design-note / reliability/stability-antipatterns.md

- 現掛：`release-it` → `docs/01-stability/02-introducing-stability/`、`release-it` → `docs/01-stability/03-stability-antipatterns/`、`release-it` → `docs/01-stability/04-stability-patterns/`
- 建議 anchor：`release-it` → `docs/01-stability/`「穩定性」（1 個數字、擴大）
- 落空數字：5475億

## taleb-note / asymmetry-practice/skin-in-the-game.md

- 現掛：`skin-in-the-game` → `docs/02-first-look-at-agency/`、`skin-in-the-game` → `docs/03-greatest-asymmetry/`、`bed-of-procrustes` → `docs/5-chance-success-happiness-and-stoicism/`、`bed-of-procrustes` → `docs/7-theseus-or-living-the-paleo-life/`
- 建議 anchor：`skin-in-the-game` → `docs/08-risk-and-rationality/`「風險與理性」（1 個數字）
- 落空數字：100次

## theology-note / historical/packer-life-and-thought.md

- 現掛：`j-i-packer-his-life-and-thought` → `docs/05-oxford-corpus-christi`、`j-i-packer-his-life-and-thought` → `docs/14-evaluation`
- 落空數字：1926年

## theology-note / historical/twentieth-century-theology-map.md

- 現掛：`theology-of-jurgen-moltmann` → `docs/05-hope-theology/`
- 建議 anchor：`theology-of-jurgen-moltmann` → `docs/06-theology-of-the-cross/`「十字架神學」（1 個數字）
- 落空數字：1518年

## thinking-note / judgment-bias/puzzle-vs-mystery.md

- 現掛：`what-the-dog-saw` → `docs/02-theories-and-predictions/01-open-secrets/`
- 建議 anchor：`what-the-dog-saw` → `docs/02-theories-and-predictions/`「第二部：理論、預測與診斷」（1 個數字、擴大）
- 落空數字：1995年、68000條

## thinking-note / self-knowledge/what-shapes-who-you-are.md

- 現掛：`pleased-to-meet-me` → `docs/01-meet-your-maker/`
- 建議 anchor：`pleased-to-meet-me` → `docs/02-meet-your-tastes/`「認識你的口味」（1 個數字）
- 落空數字：25%

## tools-note / focus-attention/brain-golden-time.md

- 現掛：`why-elites-are-time-masters` → `docs/ch02-utilize-morning/sec-1-golden-morning-time`、`peak-performance` → `docs/02-building-foundation-skills/04-manage-your-time`、`why-elites-are-time-masters` → `docs/ch03-utilize-daytime/`、`why-elites-are-time-masters` → `docs/ch01-maximize-brain-function/`
- 建議 anchor：`why-elites-are-time-masters` → `docs/ch04-exercise-sleep-reboot-evening/`「把夜晚時間利用到極致的運動與睡眠重啟術」（1 個數字）
- 落空數字：100%

## tools-note / focus-attention/internal-triggers-indistractable.md

- 現掛：`indistractable` → `docs/02-being-indistractable/`、`indistractable` → `docs/03-master-internal-triggers/`、`indistractable` → `docs/04-make-time-for-traction/`、`indistractable` → `docs/05-hack-back-external-triggers/`、`indistractable` → `docs/06-prevent-distraction-with-pacts/`
- 落空數字：1990年

## tools-note / habits/checklist-against-complexity.md

- 現掛：`checklist-manifesto` → `docs/01-problem-of-extreme-complexity/`、`checklist-manifesto` → `docs/02-the-checklist/`、`checklist-manifesto` → `docs/03-end-of-the-master-builder/`、`checklist-manifesto` → `docs/06-the-checklist-factory/`、`checklist-manifesto` → `docs/07-the-test/`、`checklist-manifesto` → `docs/09-the-save/`
- 落空數字：1970年

## tools-note / habits/systems-over-goals-atomic-habits.md

- 現掛：`atomic-habits` → `docs/the-fundamentals/`、`atomic-habits` → `docs/the-1st-law-make-it-obvious/`、`atomic-habits` → `docs/the-3rd-law-make-it-easy/`、`atomic-habits` → `docs/the-4th-law-make-it-satisfying/`、`atomic-habits` → `docs/advanced-tactics/`
- 建議 anchor：`atomic-habits` → `docs/introduction/`「我的故事」（1 個數字）
- 落空數字：170磅

## tools-note / habits/tiny-habits-behavior-design.md

- 現掛：`tiny-habits` → `docs/01-elements-of-behavior/`、`tiny-habits` → `docs/03-ability-easy-does-it/`、`tiny-habits` → `docs/04-prompts-power-of-after/`、`tiny-habits` → `docs/05-emotions-create-habits/`、`tiny-habits` → `docs/07-untangling-bad-habits/`
- 建議 anchor：`tiny-habits` → `docs/06-growing-tiny-to-transformative/`「從微小到改變一切」（1 個數字）
- 落空數字：12.7公分、2007年、2012年

## tools-note / note-systems/listful-thinking.md

- 現掛：`why-elites-are-checklist-masters` → `docs/ch01-what-lists-can-do`
- 建議 anchor：`why-elites-are-checklist-masters` → `docs/ch07-life-outsourcing/`「人生外包」（1 個數字）
- 落空數字：3000小時

## tools-note / note-systems/search-dont-file.md

- 現掛：`getting-organized-in-the-google-era` → `docs/02-new-organizing/01-search-matters`
- 落空數字：1975年

## tools-note / time-management/classic-time-management.md

- 現掛：`time-management` → `docs/06-set-priorities`、`how-to-get-control-of-your-time-and-your-life` → `docs/04-control-starts-with-planning`、`time-management` → `docs/05-plan-every-day-in-advance/`
- 建議 anchor：`how-to-get-control-of-your-time-and-your-life` → `docs/05-what-do-you-really-want-from-life/`「你真正想從人生得到什麼？」（1 個數字）
- 落空數字：15000人

## tools-note / time-management/life-leverage-outsource.md

- 現掛：`life-leverage` → `docs/04-blueprint/25-outsource-chores`、`life-leverage` → `docs/01-concept/`、`life-leverage` → `docs/02-strategy/`
- 建議 anchor：`life-leverage` → `docs/03-method/`「方法」（1 個數字）
- 落空數字：2080小時

## tracy-note / business/negotiation-basics.md

- 現掛：`negotiation` → `docs/01-everything-is-negotiable/`、`negotiation` → `docs/02-overcome-your-fears/`
- 建議 anchor：`negotiation` → `docs/21-the-successful-negotiator/`「The Successful Negotiator」（1 個數字）
- 落空數字：20%

## tracy-note / business/winning-edge.md

- 現掛：`100-absolutely-unbreakable-laws-of-business` → `docs/01-the-laws-of-life/`、`100-absolutely-unbreakable-laws-of-business` → `docs/02-the-laws-of-success/`
- 建議 anchor：`100-absolutely-unbreakable-laws-of-business` → `docs/introduction/`「前言：成功是可預測的」（1 個數字）
- 落空數字：90%

## tracy-note / goals/21-success-secrets.md

- 現掛：`21-success-secrets-of-self-made` → `docs/01-dream-big-dreams/`、`21-success-secrets-of-self-made` → `docs/02-develop-clear-direction/`
- 建議 anchor：`21-success-secrets-of-self-made` → `docs/06-work-longer-harder/`「工作得更久更努力」（1 個數字）、`21-success-secrets-of-self-made` → `docs/07-dedicate-to-lifelong-learning/`「投入終身學習」（1 個數字）、`21-success-secrets-of-self-made` → `docs/18-take-care-of-physical-health/`「好好照顧身體健康」（1 個數字）
- 落空數字：59小時、60分鐘

## tracy-note / productivity/time-management-basics.md

- 現掛：`time-management` → `docs/01-the-psychology-of-time-management/`、`time-management` → `docs/02-determine-your-values/`
- 建議 anchor：`time-management` → `docs/21-create-the-time-you-need/`「創造你需要的時間」（1 個數字）、`time-management` → `docs/09-delegate-to-others/`「授權給他人」（1 個數字）、`time-management` → `docs/introduction/`「前言」（1 個數字）
- 落空數字：21條、70%

## tracy-note / sales/power-of-charm.md

- 現掛：`power-of-charm` → `docs/01-the-quality-of-charm/`、`power-of-charm` → `docs/02-developing-the-charm-personality/`
- 建議 anchor：`power-of-charm` → `docs/introduction/`「前言」（1 個數字）
- 落空數字：85%

## uncle-bob-note / clean-code/functional-design.md

- 現掛：`functional-design-principles-patterns-practices` → `docs/01-functional-basics/`
- 建議 anchor：`functional-design-principles-patterns-practices` → `docs/06-case-study/`「案例研究」（1 個數字）
- 落空數字：5000萬

## uncle-bob-note / professionalism/agile-values.md

- 現掛：`clean-agile` → `docs/02-the-reasons-for-agile/`
- 落空數字：2001年

## uncle-bob-note / professionalism/craftsmanship.md

- 現掛：`clean-craftsmanship` → `docs/01-craftsmanship/`
- 建議 anchor：`clean-craftsmanship` → `docs/03-the-ethics/`「倫理」（1 個數字）
- 落空數字：1935年、75歲

## uncle-bob-note / professionalism/estimation-and-pressure.md

- 現掛：`clean-coder` → `docs/10-estimation/`、`clean-coder` → `docs/11-pressure/`、`clean-coder` → `docs/09-time-management/`、`clean-coder` → `docs/04-coding/`、`clean-coder` → `docs/13-teams-and-projects/`、`clean-coder` → `docs/14-mentoring-apprenticeship-and-craftsmanship/`
- 建議 anchor：`clean-coder` → `docs/06-practicing/`「練習」（1 個數字）
- 落空數字：2000000倍

## writing-note / craft-mindset/revision.md

- 現掛：`on-writing` → `docs/04-cv/`、`on-writing` → `docs/05-what-writing-is/`
- 建議 anchor：`on-writing` → `docs/07-on-writing/`「論寫作」（1 個數字）、`on-writing` → `docs/09-and-furthermore-part-i-door-shut-door-open/`「此外，第一部分：關上門，打開門」（1 個數字）
- 落空數字：10%

## writing-note / reading-input/composting.md

- 現掛：`writing-down-the-bones` → `docs/01-beginners-mind-pen-paper/`、`writing-down-the-bones` → `docs/02-first-thoughts/`
- 落空數字：1983年

## writing-note / style-clarity/nuts-and-bolts.md

- 現掛：`writing-tools` → `docs/01-nuts-and-bolts/01-begin-sentences-with-subjects-and-verbs/`、`writing-tools` → `docs/01-nuts-and-bolts/05-watch-those-adverbs/`、`writing-tools` → `docs/01-nuts-and-bolts/09-let-punctuation-control-pace-and-space/`、`writing-tools` → `docs/01-nuts-and-bolts/10-cut-big-then-small/`
- 建議 anchor：`writing-tools` → `docs/01-nuts-and-bolts/`「基本要點」（1 個數字、擴大）
- 落空數字：128個

## wujun-note / tech-civilization/wujun-information.md

- 現掛：`wujun-information-theory-40` → `docs/01-generating-information/`、`wujun-information-theory-40` → `docs/02-transmitting-information/`、`wujun-information-theory-40` → `docs/03-applying-information/`
- 落空數字：1948年

## wujun-note / wisdom/wujun-realm.md

- 現掛：`wujun-realm` → `docs/ch01-understanding-self-and-world/`
- 落空數字：2014年

