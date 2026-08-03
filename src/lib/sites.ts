// 筆記星系 registry —— 星系內部（建置期）跨站連結、姊妹站選單、sitemap，
// 以及「主題站 / 人物站」知識軸的 single source of truth。
//
// 兩個彼此獨立的軸，別再混用同一個欄位：
//   - axis        知識軸：主題站（schools 學派地圖）／人物站（profile 思想側寫）。
//                 這是內容的分類，nplus.wiki portal 依此把筆記分成兩區呈現。
//   - seeAlsoMode 技術軸：seeAlso.site 要走 siteKeys enum（"strict"，可抓拼字錯）
//                 還是開放 string（"open"，各站 content.config.ts 傳 openSeeAlso:true）。
// （v0.12.0 前這兩件事被同一個 `kind: "tech" | "humanities"` 蓋住，故拆開。）
//
// 註：判斷「某 repo 是否用 core」的權威依據是其 package.json 是否依賴 @nplus-father/notes-core，
// 不是本清單的長度——本清單負責「站與站互連」與盤點，新站請 append（new-note.sh 插在對應 __NEW_*_SITE__ 前）。
export type NoteAxis = "topic" | "person";
export type SeeAlsoMode = "strict" | "open";

export interface Site {
  key: string; // seeAlso 用的短鍵（= slug 去掉 -note），亦即跨站連結的識別子
  slug: string; // GitHub repo 名 = nplus.wiki 子路徑（如 system-design-note）
  brand: string; // 英文顯示名（topnav）
  /**
   * 顯示名，一處定義、到處沿用（站縮圖大字、portal 卡片、跨站連結 siteLabel）。
   *   - 主題站：中文短名（如「哲學」「系統設計」）
   *   - 人物站：該人物**通行的寫法**——西方作者用英文全名（Peter Drucker），
   *     華文作者用中文（馮唐、劉潤、萬維鋼、吳軍）。不硬譯成中文。
   * （v0.13.x 曾有 subject: { nameZh, nameEn } 這組欄位強制人物站取中文名，
   *  那是過度中文化，v0.14.0 收回成這一個欄位。）
   */
  label: string;
  axis: NoteAxis;
  seeAlsoMode: SeeAlsoMode;
}

// 注意：key 一律 = slug 去掉 -note（如 leetcode-note → leetcode），跨站 URL 才組得對。
export const sites: Site[] = [
  // ══ 主題站群（首頁走 schools 學派地圖）════════════════════════════════
  //
  // ── seeAlsoMode: "strict"（技術站群，seeAlso 走 siteKeys enum）──────
  { key: "system-design", slug: "system-design-note", brand: "System Design Notes", label: "系統設計", axis: "topic", seeAlsoMode: "strict" },
  { key: "data-systems", slug: "data-systems-note", brand: "Data Systems Notes", label: "資料系統", axis: "topic", seeAlsoMode: "strict" },
  { key: "cloud-infra", slug: "cloud-infra-note", brand: "Cloud & Infra Notes", label: "雲端維運", axis: "topic", seeAlsoMode: "strict" },
  { key: "clean-code", slug: "clean-code-note", brand: "Clean Code Notes", label: "程式碼工藝", axis: "topic", seeAlsoMode: "strict" },
  { key: "design-patterns", slug: "design-patterns-note", brand: "Design Patterns Notes", label: "設計模式", axis: "topic", seeAlsoMode: "strict" },
  { key: "leetcode", slug: "leetcode-note", brand: "LeetCode", label: "解題筆記", axis: "topic", seeAlsoMode: "strict" },
  { key: "behaviour-interview", slug: "behaviour-interview-note", brand: "Behaviour Interview Notes", label: "行為面試", axis: "topic", seeAlsoMode: "strict" },
  // __NEW_SITE__ (new-note.sh 會在此行前插入新技術站)

  // ── seeAlsoMode: "open"（其餘主題站）───────────────────────────────
  { key: "biblical-studies", slug: "biblical-studies-note", brand: "Biblical Studies Notes", label: "解經", axis: "topic", seeAlsoMode: "open" },
  { key: "business-strategy", slug: "business-strategy-note", brand: "Business Strategy Notes", label: "商業策略", axis: "topic", seeAlsoMode: "open" },
  { key: "career", slug: "career-note", brand: "Career Notes", label: "職涯經營", axis: "topic", seeAlsoMode: "open" },
  { key: "communication", slug: "communication-note", brand: "Communication Notes", label: "溝通", axis: "topic", seeAlsoMode: "open" },
  { key: "economics", slug: "economics-note", brand: "Economics Notes", label: "經濟學", axis: "topic", seeAlsoMode: "open" },
  { key: "growth", slug: "growth-note", brand: "Growth Notes", label: "成長", axis: "topic", seeAlsoMode: "open" },
  { key: "habits", slug: "habits-note", brand: "Habits Notes", label: "習慣", axis: "topic", seeAlsoMode: "open" },
  { key: "hbr", slug: "hbr-note", brand: "HBR Notes", label: "哈佛商業評論", axis: "topic", seeAlsoMode: "open" },
  { key: "history", slug: "history-note", brand: "History Notes", label: "歷史", axis: "topic", seeAlsoMode: "open" },
  { key: "image-style", slug: "image-style-note", brand: "Image & Style Notes", label: "形象與風格", axis: "topic", seeAlsoMode: "open" },
  { key: "investing", slug: "investing-note", brand: "Investing Notes", label: "投資思維", axis: "topic", seeAlsoMode: "open" },
  { key: "leadership", slug: "leadership-note", brand: "Leadership Notes", label: "領導力", axis: "topic", seeAlsoMode: "open" },
  { key: "learning", slug: "learning-note", brand: "Learning Notes", label: "學習方法", axis: "topic", seeAlsoMode: "open" },
  { key: "life-meaning", slug: "life-meaning-note", brand: "Life & Meaning Notes", label: "意義與韌性", axis: "topic", seeAlsoMode: "open" },
  { key: "management", slug: "management-note", brand: "Management Notes", label: "管理", axis: "topic", seeAlsoMode: "open" },
  { key: "marketing", slug: "marketing-note", brand: "Marketing Notes", label: "行銷", axis: "topic", seeAlsoMode: "open" },
  { key: "personal-finance", slug: "personal-finance-note", brand: "Personal Finance Notes", label: "個人理財", axis: "topic", seeAlsoMode: "open" },
  { key: "philosophy", slug: "philosophy-note", brand: "Philosophy Notes", label: "哲學", axis: "topic", seeAlsoMode: "open" },
  { key: "problem-solving", slug: "problem-solving-note", brand: "Problem Solving Notes", label: "問題解決", axis: "topic", seeAlsoMode: "open" },
  { key: "relationships", slug: "relationships-note", brand: "Relationships Notes", label: "關係", axis: "topic", seeAlsoMode: "open" },
  { key: "science", slug: "science-note", brand: "Science Notes", label: "科學", axis: "topic", seeAlsoMode: "open" },
  { key: "spiritual-formation", slug: "spiritual-formation-note", brand: "Spiritual Formation Notes", label: "靈命塑造", axis: "topic", seeAlsoMode: "open" },
  { key: "startup", slug: "startup-note", brand: "Startup Notes", label: "創業實戰", axis: "topic", seeAlsoMode: "open" },
  { key: "theology", slug: "theology-note", brand: "Theology Notes", label: "神學", axis: "topic", seeAlsoMode: "open" },
  { key: "thinking", slug: "thinking-note", brand: "Thinking Notes", label: "思考與心智", axis: "topic", seeAlsoMode: "open" },
  { key: "tools", slug: "tools-note", brand: "Productivity Notes", label: "生產力", axis: "topic", seeAlsoMode: "open" },
  { key: "wellness", slug: "wellness-note", brand: "Wellness Notes", label: "身心健康", axis: "topic", seeAlsoMode: "open" },
  { key: "writing", slug: "writing-note", brand: "Writing Notes", label: "寫作工藝", axis: "topic", seeAlsoMode: "open" },
  { key: "agile", slug: "agile-note", brand: "Agile Notes", label: "敏捷開發", axis: "topic", seeAlsoMode: "open" },
  { key: "design", slug: "design-note", brand: "Design Notes", label: "設計思考", axis: "topic", seeAlsoMode: "open" },
  // __NEW_TOPIC_SITE__ (new-note.sh 會在此行前插入新主題站)

  // ══ 人物站群（首頁走 profile 思想側寫）════════════════════════════════
  { key: "bogle", slug: "bogle-note", brand: "Bogle Notes", label: "John C. Bogle", axis: "person", seeAlsoMode: "open" },
  { key: "cloud", slug: "cloud-note", brand: "Henry Cloud Notes", label: "Henry Cloud", axis: "person", seeAlsoMode: "open" },
  { key: "damodaran", slug: "damodaran-note", brand: "Damodaran Notes", label: "Aswath Damodaran", axis: "person", seeAlsoMode: "open" },
  { key: "de-botton", slug: "de-botton-note", brand: "Alain de Botton Notes", label: "Alain de Botton", axis: "person", seeAlsoMode: "open" },
  { key: "drucker", slug: "drucker-note", brand: "Drucker Notes", label: "Peter Drucker", axis: "person", seeAlsoMode: "open" },
  { key: "fengtang", slug: "fengtang-note", brand: "Feng Tang Notes", label: "馮唐", axis: "person", seeAlsoMode: "open" },
  { key: "fromm", slug: "fromm-note", brand: "Erich Fromm Notes", label: "Erich Fromm", axis: "person", seeAlsoMode: "open" },
  { key: "gardner", slug: "gardner-note", brand: "Howard Gardner Notes", label: "Howard Gardner", axis: "person", seeAlsoMode: "open" },
  { key: "greene", slug: "greene-note", brand: "Robert Greene Notes", label: "Robert Greene", axis: "person", seeAlsoMode: "open" },
  { key: "keller", slug: "keller-note", brand: "Keller Notes", label: "Timothy Keller", axis: "person", seeAlsoMode: "open" },
  { key: "kiyosaki", slug: "kiyosaki-note", brand: "Kiyosaki Notes", label: "Robert Kiyosaki", axis: "person", seeAlsoMode: "open" },
  { key: "lewis", slug: "lewis-note", brand: "C.S. Lewis Notes", label: "C.S. Lewis", axis: "person", seeAlsoMode: "open" },
  { key: "liurun", slug: "liurun-note", brand: "Liu Run Notes", label: "劉潤", axis: "person", seeAlsoMode: "open" },
  { key: "maxwell", slug: "maxwell-note", brand: "Maxwell Notes", label: "John C. Maxwell", axis: "person", seeAlsoMode: "open" },
  { key: "newport", slug: "newport-note", brand: "Cal Newport Notes", label: "Cal Newport", axis: "person", seeAlsoMode: "open" },
  { key: "nouwen", slug: "nouwen-note", brand: "Nouwen Notes", label: "Henri Nouwen", axis: "person", seeAlsoMode: "open" },
  { key: "nt-wright", slug: "nt-wright-note", brand: "N.T. Wright Notes", label: "N.T. Wright", axis: "person", seeAlsoMode: "open" },
  { key: "peck", slug: "peck-note", brand: "Scott Peck Notes", label: "M. Scott Peck", axis: "person", seeAlsoMode: "open" },
  { key: "peterson", slug: "peterson-note", brand: "Jordan Peterson Notes", label: "Jordan Peterson", axis: "person", seeAlsoMode: "open" },
  { key: "schwager", slug: "schwager-note", brand: "Schwager Notes", label: "Jack Schwager", axis: "person", seeAlsoMode: "open" },
  { key: "stott", slug: "stott-note", brand: "Stott Notes", label: "John Stott", axis: "person", seeAlsoMode: "open" },
  { key: "taleb", slug: "taleb-note", brand: "Taleb Notes", label: "Nassim Nicholas Taleb", axis: "person", seeAlsoMode: "open" },
  { key: "tracy", slug: "tracy-note", brand: "Brian Tracy Notes", label: "Brian Tracy", axis: "person", seeAlsoMode: "open" },
  { key: "uncle-bob", slug: "uncle-bob-note", brand: "Uncle Bob Notes", label: "Robert C. Martin", axis: "person", seeAlsoMode: "open" },
  { key: "wan-weigang", slug: "wan-weigang-note", brand: "Wan Weigang Notes", label: "萬維鋼", axis: "person", seeAlsoMode: "open" },
  { key: "willard", slug: "willard-note", brand: "Dallas Willard Notes", label: "Dallas Willard", axis: "person", seeAlsoMode: "open" },
  { key: "wujun", slug: "wujun-note", brand: "Wu Jun Notes", label: "吳軍", axis: "person", seeAlsoMode: "open" },
  { key: "covey", slug: "covey-note", brand: "Covey Notes", label: "Stephen R. Covey", axis: "person", seeAlsoMode: "open" },
  // __NEW_PERSON_SITE__ (new-note.sh 會在此行前插入新人物站)
];

// 跨站連結（seeAlso）合法的 site key 清單——只約束 seeAlsoMode "strict" 的站；
// 那些站的 content.config.ts 用它建 z.enum。"open" 的站用開放 string，不在此列。
export const siteKeys = sites
  .filter((s) => s.seeAlsoMode === "strict")
  .map((s) => s.key) as [string, ...string[]];

/** 知識軸分群——portal 分區與 core 首頁（schools／profile）都依這個軸。 */
export const topicSites = sites.filter((s) => s.axis === "topic");
export const personSites = sites.filter((s) => s.axis === "person");

// slug / key 對照涵蓋全部站群（姊妹站連結 links.ts 可查任一站）。
export const siteBySlug = new Map(sites.map((s) => [s.slug, s]));
export const siteByKey = new Map(sites.map((s) => [s.key, s]));
