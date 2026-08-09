// 主題站封面的符號庫。每個符號是一支 400x400 的 inline SVG，接一個顏色參數。
//
// 一個符號只能屬於一站——cover-gen.mjs 啟動時會對帳 site-covers.ts 並擋掉重複。
// 少了那道檢查，tools-note 與 business-strategy-note 曾同時用 target、
// spiritual-formation-note 與 life-meaning-note 同時用 mountain，兩組封面只有顏色
// 不同，在 /notes/ 的格狀排列裡一眼就看得出是同一張圖。

export const MOTIFS = {
  // </> code brackets — clean-code
  code: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g stroke="${c}" stroke-width="18" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <polyline points="150,130 80,200 150,270"/>
      <polyline points="250,130 320,200 250,270"/>
      <line x1="222" y1="120" x2="178" y2="280"/></g></svg>`,

  // arranged shapes grid — design-patterns
  patterns: (
    c,
  ) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="7">
      <rect x="92" y="92" width="96" height="96" rx="14"/>
      <circle cx="260" cy="140" r="48"/>
      <circle cx="140" cy="260" r="48"/>
      <rect x="212" y="212" width="96" height="96" rx="14"/></g>
    <g fill="${c}"><rect x="120" y="120" width="40" height="40" rx="6"/><circle cx="260" cy="308" r="0"/></g></svg>`,

  // connected nodes — system-design
  network: (
    c,
  ) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g stroke="${c}" stroke-width="7" opacity=".9" stroke-linecap="round">
      <line x1="200" y1="88" x2="108" y2="228"/><line x1="200" y1="88" x2="292" y2="228"/>
      <line x1="108" y1="228" x2="292" y2="228"/><line x1="200" y1="88" x2="200" y2="312"/>
      <line x1="108" y1="228" x2="200" y2="312"/><line x1="292" y1="228" x2="200" y2="312"/></g>
    <g fill="${c}"><circle cx="200" cy="88" r="30"/><circle cx="108" cy="228" r="30"/>
      <circle cx="292" cy="228" r="30"/><circle cx="200" cy="312" r="30"/></g></svg>`,

  // database stack — data-systems
  db: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <path d="M110 132 v136 a90 30 0 0 0 180 0 v-136" fill="none" stroke="${c}" stroke-width="7"/>
    <ellipse cx="200" cy="132" rx="90" ry="30" fill="${c}"/>
    <path d="M110 178 a90 30 0 0 0 180 0" fill="none" stroke="${c}" stroke-width="7"/>
    <path d="M110 224 a90 30 0 0 0 180 0" fill="none" stroke="${c}" stroke-width="7"/></svg>`,

  // cloud — cloud-infra
  cloud: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <path d="M142 286 a58 58 0 0 1 -4 -116 a78 78 0 0 1 150 -14 a52 52 0 0 1 -6 130 z" fill="${c}"/></svg>`,

  // speech bubble w/ dots — behaviour-interview
  chat: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <path d="M104 120 h192 a26 26 0 0 1 26 26 v96 a26 26 0 0 1 -26 26 h-104 l-58 46 v-46 h-30 a26 26 0 0 1 -26 -26 v-96 a26 26 0 0 1 26 -26 z"
      fill="none" stroke="${c}" stroke-width="7" stroke-linejoin="round"/>
    <g fill="${c}"><circle cx="152" cy="194" r="13"/><circle cx="200" cy="194" r="13"/><circle cx="248" cy="194" r="13"/></g></svg>`,

  // target + dart — business-strategy
  target: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="7"><circle cx="188" cy="212" r="118"/><circle cx="188" cy="212" r="74"/></g>
    <circle cx="188" cy="212" r="28" fill="${c}"/>
    <g stroke="${c}" stroke-width="10" stroke-linecap="round"><line x1="316" y1="84" x2="200" y2="200"/></g>
    <path d="M320 80 l-10 40 l-30 -30 z" fill="${c}"/></svg>`,

  // briefcase — career
  briefcase: (
    c,
  ) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <path d="M158 146 v-18 a18 18 0 0 1 18 -18 h48 a18 18 0 0 1 18 18 v18" fill="none" stroke="${c}" stroke-width="7"/>
    <rect x="90" y="146" width="220" height="158" rx="18" fill="none" stroke="${c}" stroke-width="7"/>
    <line x1="90" y1="212" x2="310" y2="212" stroke="${c}" stroke-width="7"/>
    <rect x="176" y="196" width="48" height="32" rx="6" fill="${c}"/></svg>`,

  // compass — leadership
  compass: (
    c,
  ) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <circle cx="200" cy="200" r="120" fill="none" stroke="${c}" stroke-width="7"/>
    <path d="M200 96 L236 200 L200 214 L164 200 Z" fill="${c}"/>
    <path d="M200 304 L164 200 L200 186 L236 200 Z" fill="${c}" opacity=".45"/>
    <circle cx="200" cy="200" r="12" fill="${c}"/></svg>`,

  // rocket — startup
  rocket: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
      <path d="M200 72 c44 46 56 104 56 158 h-112 c0 -54 12 -112 56 -158 z"/>
      <circle cx="200" cy="164" r="24"/>
      <path d="M144 214 l-36 42 l42 -6"/>
      <path d="M256 214 l36 42 l-42 -6"/>
      <path d="M174 300 q26 44 52 0"/></g></svg>`,

  // megaphone — marketing
  megaphone: (
    c,
  ) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <path d="M96 172 h56 l128 -64 v184 l-128 -64 h-56 a0 0 0 0 1 0 0 z" fill="${c}"/>
    <rect x="96" y="172" width="56" height="56" rx="10" fill="${c}"/>
    <path d="M152 228 h34 l6 60 h-28 z" fill="${c}"/>
    <g stroke="${c}" stroke-width="9" fill="none" stroke-linecap="round"><path d="M300 156 q34 44 0 88"/></g></svg>`,

  // two speech bubbles — communication
  chat2: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <path d="M84 108 h150 a20 20 0 0 1 20 20 v68 a20 20 0 0 1 -20 20 h-84 l-42 34 v-34 h-24 a20 20 0 0 1 -20 -20 v-68 a20 20 0 0 1 20 -20 z"
      fill="none" stroke="${c}" stroke-width="7" stroke-linejoin="round"/>
    <path d="M182 196 h118 a20 20 0 0 1 20 20 v68 a20 20 0 0 1 -20 20 h-18 v32 l-40 -32 h-60 a20 20 0 0 1 -20 -20 v-24"
      fill="${c}"/></svg>`,

  // ascending bars + arrow — growth
  growth: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="${c}">
      <rect x="96" y="240" width="56" height="72" rx="8"/>
      <rect x="172" y="192" width="56" height="120" rx="8"/>
      <rect x="248" y="132" width="56" height="180" rx="8"/></g>
    <g stroke="${c}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <polyline points="110,196 200,150 300,96"/>
      <polyline points="262,96 300,96 300,134"/></g></svg>`,

  // line chart up — investing
  chart: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g stroke="${c}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <polyline points="88,286 164,214 224,252 312,116"/>
      <polyline points="262,116 312,116 312,166"/></g>
    <g fill="${c}"><circle cx="88" cy="286" r="13"/><circle cx="164" cy="214" r="13"/><circle cx="224" cy="252" r="13"/></g></svg>`,

  // banknote — personal-finance
  bill: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <rect x="76" y="128" width="248" height="144" rx="16" fill="none" stroke="${c}" stroke-width="7"/>
    <circle cx="200" cy="200" r="42" fill="none" stroke="${c}" stroke-width="7"/>
    <line x1="200" y1="176" x2="200" y2="224" stroke="${c}" stroke-width="7" stroke-linecap="round"/>
    <g fill="${c}"><circle cx="108" cy="200" r="9"/><circle cx="292" cy="200" r="9"/></g></svg>`,

  // supply/demand cross — economics
  econ: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g stroke="${c}" stroke-width="7" fill="none" stroke-linecap="round">
      <line x1="104" y1="92" x2="104" y2="304"/><line x1="104" y1="304" x2="312" y2="304"/>
      <path d="M132 132 L288 272"/><path d="M132 272 L288 132"/></g>
    <circle cx="210" cy="202" r="13" fill="${c}"/></svg>`,

  // greek column — philosophy
  column: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="${c}"><rect x="116" y="104" width="168" height="24" rx="6"/><rect x="106" y="288" width="188" height="26" rx="6"/></g>
    <g fill="none" stroke="${c}" stroke-width="7" stroke-linecap="round">
      <line x1="148" y1="138" x2="148" y2="282"/><line x1="182" y1="138" x2="182" y2="282"/>
      <line x1="218" y1="138" x2="218" y2="282"/><line x1="252" y1="138" x2="252" y2="282"/></g></svg>`,

  // hourglass — history
  hourglass: (
    c,
  ) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="8" stroke-linejoin="round" stroke-linecap="round">
      <line x1="120" y1="92" x2="280" y2="92"/><line x1="120" y1="308" x2="280" y2="308"/>
      <path d="M134 92 q0 74 66 108 q66 -34 66 -108"/>
      <path d="M134 308 q0 -74 66 -108 q66 34 66 108"/></g>
    <path d="M162 124 q38 36 76 0 z" fill="${c}"/></svg>`,

  // lightbulb — thinking
  bulb: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
      <path d="M200 84 a88 88 0 0 1 54 158 q-14 12 -16 36 h-76 q-2 -24 -16 -36 a88 88 0 0 1 54 -158 z"/>
      <line x1="166" y1="300" x2="234" y2="300"/><line x1="176" y1="322" x2="224" y2="322"/></g></svg>`,

  // open book — learning
  book: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="7" stroke-linejoin="round">
      <path d="M200 128 q-52 -30 -108 -20 v168 q56 -10 108 20 z"/>
      <path d="M200 128 q52 -30 108 -20 v168 q-56 -10 -108 20 z"/></g></svg>`,

  // pen nib — writing
  pen: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="7" stroke-linejoin="round">
      <path d="M200 84 l56 160 l-56 46 l-56 -46 z"/>
      <line x1="200" y1="150" x2="200" y2="250"/></g>
    <circle cx="200" cy="212" r="11" fill="${c}"/></svg>`,

  // circular arrow — habits
  cycle: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="10" stroke-linecap="round">
      <path d="M296 200 a96 96 0 1 1 -40 -78"/></g>
    <path d="M256 78 l4 68 l-60 -22 z" fill="${c}"/></svg>`,

  // interlocking rings — relationships
  link: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="10"><circle cx="156" cy="200" r="82"/><circle cx="244" cy="200" r="82"/></g></svg>`,

  // mountain + sun — life-meaning
  mountain: (
    c,
  ) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <circle cx="288" cy="126" r="30" fill="${c}"/>
    <path d="M72 308 l78 -134 l52 74 l46 -80 l80 140 z" fill="${c}"/></svg>`,

  // coat hanger — image-style
  hanger: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round">
      <path d="M200 118 a26 26 0 0 1 26 26 q0 18 -26 26"/>
      <path d="M200 170 l-114 82 a10 10 0 0 0 6 20 h216 a10 10 0 0 0 6 -20 z"/></g></svg>`,

  // curly braces { • } — leetcode
  braces: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round">
      <path d="M180 104 q-36 0 -36 40 v22 q0 22 -26 34 q26 12 26 34 v22 q0 40 36 40"/>
      <path d="M220 104 q36 0 36 40 v22 q0 22 26 34 q-26 12 -26 34 v22 q0 40 -36 40"/></g>
    <circle cx="200" cy="200" r="14" fill="${c}"/></svg>`,

  // ECG heartbeat line — wellness
  pulse: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <polyline points="64,208 148,208 176,132 214,288 244,208 336,208"
      fill="none" stroke="${c}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/></svg>`,

  // vertical scroll — biblical-studies（讀經＝展開的卷軸，與 book 的「翻開的書」分開）
  scroll: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
      <path d="M126 104 h148 a22 22 0 0 1 0 44 h-148 a22 22 0 0 1 0 -44 z"/>
      <path d="M126 252 h148 a22 22 0 0 1 0 44 h-148 a22 22 0 0 1 0 -44 z"/>
      <line x1="126" y1="148" x2="126" y2="252"/>
      <line x1="274" y1="148" x2="274" y2="252"/>
      <line x1="160" y1="184" x2="240" y2="184"/>
      <line x1="160" y1="216" x2="240" y2="216"/></g></svg>`,

  // celtic cross — theology（十字＋環，明確是神學而非泛靈性）
  // 環必須明顯小於橫臂、交點靠上，否則會讀成準星而不是十字架。
  celtic: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="15" stroke-linecap="round">
      <line x1="200" y1="66" x2="200" y2="334"/>
      <line x1="108" y1="158" x2="292" y2="158"/></g>
    <circle cx="200" cy="158" r="46" fill="none" stroke="${c}" stroke-width="9"/></svg>`,

  // journal issue — hbr（期刊＝有刊頭的一期，與 book/bill 都不同）
  journal: (
    c,
  ) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <rect x="94" y="70" width="212" height="268" rx="16" fill="none" stroke="${c}" stroke-width="8"/>
    <path d="M94 86 a16 16 0 0 1 16 -16 h180 a16 16 0 0 1 16 16 v46 h-212 z" fill="${c}"/>
    <g stroke="${c}" stroke-width="8" stroke-linecap="round">
      <line x1="130" y1="192" x2="270" y2="192"/>
      <line x1="130" y1="234" x2="270" y2="234"/>
      <line x1="130" y1="276" x2="216" y2="276"/></g></svg>`,

  // org chart — management（層級＝方塊樹；network 是圓節點的網，兩者不會看混）
  org: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="7" stroke-linejoin="round">
      <rect x="156" y="84" width="88" height="62" rx="10"/>
      <rect x="78" y="254" width="88" height="62" rx="10"/>
      <rect x="234" y="254" width="88" height="62" rx="10"/></g>
    <g fill="none" stroke="${c}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">
      <line x1="200" y1="146" x2="200" y2="200"/>
      <path d="M122 254 v-54 h156 v54"/></g></svg>`,

  // puzzle piece — problem-solving（缺口與凸榫＝把問題接起來）
  puzzle: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <path d="M112 112 h72 a26 26 0 0 1 52 0 h52 v72 a26 26 0 0 1 0 52 v52 h-52 a26 26 0 0 0 -52 0 h-72 z"
      fill="none" stroke="${c}" stroke-width="7" stroke-linejoin="round"/></svg>`,

  // erlenmeyer flask — science（實驗＝可證偽，比原子模型更不會跟 network 撞）
  flask: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <path d="M146 252 h108 l44 66 a18 18 0 0 1 -15 28 h-166 a18 18 0 0 1 -15 -28 z" fill="${c}" opacity=".5"/>
    <g fill="none" stroke="${c}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
      <path d="M170 88 v96 l-76 134 a18 18 0 0 0 15 28 h182 a18 18 0 0 0 15 -28 l-76 -134 v-96"/>
      <line x1="154" y1="88" x2="246" y2="88"/></g>
    <g fill="${c}"><circle cx="178" cy="296" r="9"/><circle cx="214" cy="320" r="7"/></g></svg>`,

  // checked list — tools/productivity（原本與 business-strategy 共用 target，撞圖）
  // 線要對齊框的中線、且不要拉太長，否則兩行會散成四個各自為政的元素。
  checklist: (
    c,
  ) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="8" stroke-linejoin="round">
      <rect x="104" y="112" width="64" height="64" rx="13"/>
      <rect x="104" y="224" width="64" height="64" rx="13"/></g>
    <g fill="none" stroke="${c}" stroke-width="10" stroke-linecap="round">
      <line x1="198" y1="144" x2="296" y2="144"/>
      <line x1="198" y1="256" x2="296" y2="256"/></g>
    <g fill="none" stroke="${c}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round">
      <polyline points="122,144 136,160 160,126"/>
      <polyline points="122,256 136,272 160,238"/></g></svg>`,

  // sprout — spiritual-formation（原本與 life-meaning 共用 mountain，撞圖；
  // 「塑造」是被栽種養成，不是登頂）
  sprout: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <line x1="200" y1="192" x2="200" y2="318" stroke="${c}" stroke-width="10" stroke-linecap="round"/>
    <path d="M194 202 c-6 -64 -50 -90 -94 -88 c-2 48 36 92 94 88 z" fill="${c}"/>
    <path d="M206 202 c6 -64 50 -90 94 -88 c2 48 -36 92 -94 88 z" fill="${c}" opacity=".55"/></svg>`,

  // kanban board — agile（三欄與一張正在流動的卡；刻意不用 cycle，
  // 那是 habits 的迴路，敏捷要表達的是「卡片橫向移動」而不是「重複」）
  board: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="${c}" stroke-width="7">
      <rect x="72" y="96" width="76" height="208" rx="12"/>
      <rect x="162" y="96" width="76" height="208" rx="12"/>
      <rect x="252" y="96" width="76" height="208" rx="12"/></g>
    <g fill="${c}">
      <rect x="86" y="118" width="48" height="30" rx="7"/>
      <rect x="86" y="162" width="48" height="30" rx="7" opacity=".55"/>
      <rect x="176" y="118" width="48" height="30" rx="7"/></g>
    <g stroke="${c}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <line x1="248" y1="230" x2="300" y2="230"/>
      <polyline points="286,216 300,230 286,244"/></g></svg>`,

  // alignment grid + nib — design（強調「對齊」這條線，而不是畫筆本身；
  // patterns 是排列好的形狀，屬 design-patterns，這裡刻意分開）
  nib: (c) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <g stroke="${c}" stroke-width="5" opacity=".4">
      <line x1="132" y1="76" x2="132" y2="324"/>
      <line x1="76" y1="268" x2="324" y2="268"/></g>
    <g fill="none" stroke="${c}" stroke-width="7" stroke-linejoin="round">
      <path d="M132 268 L250 130 L296 168 L178 306 Z"/>
      <line x1="132" y1="268" x2="214" y2="197"/></g>
    <path d="M132 268 l46 -40 l22 18 l-46 40 z" fill="${c}"/>
    <circle cx="132" cy="268" r="9" fill="${c}"/></svg>`,

  // shepherd's crook over a heart — pastoral-psychology（牧杖護心＝牧養人心；
  // 心是被牧養的對象，與 pulse 的心電圖、link 的圓環、celtic 的十字都分得開）
  shepherd: (
    c,
  ) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <path d="M120 332 L120 152 a56 56 0 0 1 112 0 v14" fill="none" stroke="${c}" stroke-width="12" stroke-linecap="round"/>
    <path d="M232 298 c-38 -32 -62 -54 -62 -84 a31 31 0 0 1 62 -19 a31 31 0 0 1 62 19 c0 30 -24 52 -62 84 z" fill="${c}"/></svg>`,
};
