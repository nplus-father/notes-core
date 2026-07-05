// 筆記星系 registry —— 星系內部（建置期）跨站連結、姊妹站選單、sitemap 的 single source of truth。
//
// 收錄「所有使用 notes-core 的站」，分兩群（kind）：
//   - "tech"       技術站群：seeAlso 走 siteKeys enum（嚴格、可抓拼字錯）。
//   - "humanities" 人文站群（作者/書評/靈修站）：seeAlso 用開放 string（各站 content.config.ts 傳 openSeeAlso:true）。
// 兩群都在本清單，讓「哪些站用 core」有單一權威來源；enum 只約束技術站（見 siteKeys）。
//
// 註：判斷「某 repo 是否用 core」的權威依據是其 package.json 是否依賴 @nplus-father/notes-core，
// 不是本清單的長度——本清單負責「站與站互連」與盤點，新站請 append（new-note.sh 插在對應 __NEW_*_SITE__ 前）。
export interface Site {
  key: string; // seeAlso 用的短鍵（= slug 去掉 -note），亦即跨站連結的識別子
  slug: string; // GitHub repo 名 = nplus.wiki 子路徑（如 system-design-note）
  brand: string; // 英文顯示名（topnav / 站縮圖 cover.svg）
  label: string; // 中文短名（跨站連結 siteLabel）
  ns: string; // 複習紀錄 localStorage 前綴，各站唯一
  kind: "tech" | "humanities"; // 站群：技術站走 siteKeys enum；人文站用開放 seeAlso
}

// 注意：key 一律 = slug 去掉 -note（如 leetcode-note → leetcode），跨站 URL 才組得對。
export const sites: Site[] = [
  // ── 技術站群（seeAlso 走 siteKeys enum）───────────────────────────
  { key: "system-design", slug: "system-design-note", brand: "SysDesign Notes", label: "系統設計", ns: "sd", kind: "tech" },
  { key: "data-systems", slug: "data-systems-note", brand: "Data Systems Notes", label: "資料系統", ns: "ds", kind: "tech" },
  { key: "cloud-infra", slug: "cloud-infra-note", brand: "Cloud-Infra Notes", label: "雲端維運", ns: "ci", kind: "tech" },
  { key: "clean-code", slug: "clean-code-note", brand: "Clean Code Notes", label: "程式碼工藝", ns: "cc", kind: "tech" },
  { key: "design-patterns", slug: "design-patterns-note", brand: "Design Patterns Notes", label: "設計模式", ns: "dp", kind: "tech" },
  { key: "leetcode", slug: "leetcode-note", brand: "LeetKode", label: "LeetCode", ns: "lk", kind: "tech" },
  { key: "behaviour-interview", slug: "behaviour-interview-note", brand: "Behaviour Interview Notes", label: "行為面試", ns: "bi", kind: "tech" },
  // __NEW_SITE__ (new-note.sh 會在此行前插入新技術站)

  // ── 人文站群（作者/書評/靈修站；seeAlso 用開放 string）─────────────
  { key: "bogle", slug: "bogle-note", brand: "Bogle Notes", label: "柏格", ns: "jb", kind: "humanities" },
  { key: "damodaran", slug: "damodaran-note", brand: "Damodaran Notes", label: "達摩德蘭", ns: "ad", kind: "humanities" },
  { key: "de-botton", slug: "de-botton-note", brand: "Alain de Botton Notes", label: "狄波頓", ns: "ab", kind: "humanities" },
  { key: "drucker", slug: "drucker-note", brand: "Drucker Notes", label: "杜拉克", ns: "dr", kind: "humanities" },
  { key: "fromm", slug: "fromm-note", brand: "Erich Fromm Notes", label: "佛洛姆", ns: "ef", kind: "humanities" },
  { key: "greene", slug: "greene-note", brand: "Robert Greene Notes", label: "葛林", ns: "rg", kind: "humanities" },
  { key: "keller", slug: "keller-note", brand: "Keller Notes", label: "凱勒", ns: "tk", kind: "humanities" },
  { key: "lewis", slug: "lewis-note", brand: "C.S. Lewis Notes", label: "路易斯", ns: "cl", kind: "humanities" },
  { key: "maxwell", slug: "maxwell-note", brand: "Maxwell Notes", label: "麥斯威爾", ns: "jm", kind: "humanities" },
  { key: "nt-wright", slug: "nt-wright-note", brand: "N.T. Wright Notes", label: "賴特", ns: "nw", kind: "humanities" },
  { key: "peck", slug: "peck-note", brand: "Scott Peck Notes", label: "派克", ns: "sp", kind: "humanities" },
  { key: "peterson", slug: "peterson-note", brand: "Jordan Peterson Notes", label: "彼得森", ns: "jp", kind: "humanities" },
  { key: "schwager", slug: "schwager-note", brand: "Schwager Notes", label: "史瓦格", ns: "sw", kind: "humanities" },
  { key: "stott", slug: "stott-note", brand: "Stott Notes", label: "斯托得", ns: "js", kind: "humanities" },
  { key: "tracy", slug: "tracy-note", brand: "Brian Tracy Notes", label: "崔西", ns: "bt", kind: "humanities" },
  { key: "uncle-bob", slug: "uncle-bob-note", brand: "Uncle Bob Notes", label: "Uncle Bob", ns: "rm", kind: "humanities" },
  { key: "wan-weigang", slug: "wan-weigang-note", brand: "Wan Weigang Notes", label: "萬維鋼", ns: "ww", kind: "humanities" },
  { key: "wujun", slug: "wujun-note", brand: "Wu Jun Notes", label: "吳軍", ns: "wj", kind: "humanities" },
  // __NEW_HUMANITIES_SITE__ (new-note.sh 會在此行前插入新人文站)
];

// 跨站連結（seeAlso）合法的 site key 清單——只約束「技術站群」；
// 各技術站 content.config.ts 的 z.enum 吃這個。人文站群用開放 string，不在此列。
export const siteKeys = sites.filter((s) => s.kind === "tech").map((s) => s.key) as [
  string,
  ...string[],
];

// slug / key 對照涵蓋全部站群（姊妹站連結 links.ts 可查技術站與人文站）。
export const siteBySlug = new Map(sites.map((s) => [s.slug, s]));
export const siteByKey = new Map(sites.map((s) => [s.key, s]));
