// 主題站封面的視覺參數 —— 每站一組主色與一個符號。
//
// 為什麼與 sites.ts 分開：sites.ts 被 62 個站台在建置期 import，那裡只該放站台
// runtime 真正需要的東西（互連、知識軸、顯示名）；封面配色只有 tools/cover 的
// 生成器會讀，塞進 sites.ts 會讓每一站的 build 都載入用不到的資料。
//
// 為什麼仍留在 core：這裡以 slug 關聯 sites.ts，中文名與英文名**不重複存一份**，
// 一律由 sites.ts 的 label / brand 推導。舊版的 note-cover/cover-gen.mjs 自己存了
// title 與 en，結果 35 站有 9 站的中文名跟 registry 對不上——封面上印「領導力」、
// 卡片上寫「領導」。同一個事實存兩份，遲早會漂移，所以這裡只存 registry 沒有的東西。
//
// 只有主題站有：人物站的封面是傳主的肖像照，不由生成器產出。

export interface SiteCover {
  /** 主色：符號、頁尾圓點、底部漸層線左端、右上角光暈 */
  accent: string;
  /** 副色：底部漸層線右端。同色相再暗一階，不要換色相 */
  accent2: string;
  /** tools/cover/motifs.mjs 裡的符號名。一個符號只能屬於一站（生成器會擋重複） */
  motif: string;
  cloth?: { hue?: number; tone?: number };
}

/** slug → 封面參數。鍵必須是 sites.ts 裡 axis === "topic" 的站（生成器會對帳）。 */
export const siteCovers: Record<string, SiteCover> = {
  // ── 技術 ──────────────────────────────────────────────
  "system-design-note": {
    accent: "#4d9dff",
    accent2: "#2a6ac9",
    motif: "network",
    cloth: { hue: 255, tone: -0.05 },
  },
  "data-systems-note": {
    accent: "#2fbf9e",
    accent2: "#1c8a72",
    motif: "db",
    cloth: { hue: 178, tone: -0.05 },
  },
  "data-science-note": {
    accent: "#b9d43c",
    accent2: "#7f9a1f",
    motif: "scatter",
    cloth: { hue: 118 },
  },
  "travel-note": {
    accent: "#f0a04b",
    accent2: "#b8701f",
    motif: "route",
    cloth: { hue: 51, tone: -0.05 },
  },
  "hr-note": {
    accent: "#4f8cf0",
    accent2: "#2f5fb8",
    motif: "badge",
    cloth: { hue: 247, tone: 0.05 },
  },
  "cloud-infra-note": {
    accent: "#35c6d6",
    accent2: "#1f8fa0",
    motif: "cloud",
    cloth: { tone: 0.025 },
  },
  "clean-code-note": {
    accent: "#a678ff",
    accent2: "#6f47c9",
    motif: "code",
    cloth: { hue: 297, tone: 0.05 },
  },
  "design-patterns-note": {
    accent: "#6d8cff",
    accent2: "#3a52cc",
    motif: "patterns",
    cloth: { hue: 258, tone: 0.025 },
  },
  "leetcode-note": {
    accent: "#8b7cff",
    accent2: "#4f46e5",
    motif: "braces",
    cloth: { hue: 273, tone: 0.05 },
  },
  "behaviour-interview-note": {
    accent: "#ff7a9c",
    accent2: "#d64d72",
    motif: "chat",
    cloth: { hue: 5, tone: -0.05 },
  },
  "agile-note": {
    accent: "#3fc4b0",
    accent2: "#22897a",
    motif: "board",
    cloth: { hue: 185, tone: 0.025 },
  },
  // 技術站群唯一的紅：其餘七站佔滿藍綠紫，格狀排列裡要一眼分得出防禦這一站。
  "security-note": {
    accent: "#ff5f57",
    accent2: "#c93a33",
    motif: "shield",
    cloth: { hue: 30, tone: 0.025 },
  },

  // ── 商業 ──────────────────────────────────────────────
  "business-strategy-note": {
    accent: "#e8a23d",
    accent2: "#c06f1c",
    motif: "target",
    cloth: { hue: 58, tone: -0.025 },
  },
  "management-note": {
    accent: "#c9923a",
    accent2: "#96661f",
    motif: "org",
    cloth: { hue: 86, tone: -0.05 },
  },
  "hbr-note": {
    accent: "#e0574e",
    accent2: "#b03a33",
    motif: "journal",
    cloth: { hue: 15, tone: -0.04 },
  },
  "career-note": {
    accent: "#d9a441",
    accent2: "#a9781f",
    motif: "briefcase",
    cloth: { hue: 76, tone: 0.02 },
  },
  "leadership-note": {
    accent: "#4fc26b",
    accent2: "#2f8f46",
    motif: "compass",
    cloth: { hue: 158, tone: 0.025 },
  },
  "startup-note": {
    accent: "#ff8a5c",
    accent2: "#d6552c",
    motif: "rocket",
    cloth: { hue: 43, tone: 0.04 },
  },
  "marketing-note": {
    accent: "#ff8a3d",
    accent2: "#d6631c",
    motif: "megaphone",
    cloth: { hue: 37, tone: -0.05 },
  },
  "communication-note": {
    accent: "#38b6c9",
    accent2: "#1f8090",
    motif: "chat2",
    cloth: { hue: 205, tone: -0.025 },
  },

  // ── 財經 ──────────────────────────────────────────────
  "investing-note": {
    accent: "#5ec26b",
    accent2: "#2f8f46",
    motif: "chart",
    cloth: { hue: 144, tone: -0.05 },
  },
  "personal-finance-note": {
    accent: "#e8b23d",
    accent2: "#c0871c",
    motif: "bill",
    cloth: { hue: 91 },
  },
  "economics-note": {
    accent: "#2fbf9e",
    accent2: "#1c8a72",
    motif: "econ",
    cloth: { hue: 178 },
  },

  // ── 人文與心智 ────────────────────────────────────────
  "philosophy-note": {
    accent: "#a678ff",
    accent2: "#6f47c9",
    motif: "column",
    cloth: { hue: 305 },
  },
  "history-note": {
    accent: "#d9a441",
    accent2: "#a9781f",
    motif: "hourglass",
    cloth: { hue: 83, tone: 0.05 },
  },
  "thinking-note": {
    accent: "#c264d6",
    accent2: "#8f3fa0",
    motif: "bulb",
    cloth: { tone: -0.025 },
  },
  "problem-solving-note": {
    accent: "#9b6dff",
    accent2: "#6538c9",
    motif: "puzzle",
    cloth: { hue: 295, tone: -0.05 },
  },
  "learning-note": {
    accent: "#4d9dff",
    accent2: "#2a6ac9",
    motif: "book",
    cloth: { hue: 245, tone: -0.025 },
  },
  "science-note": {
    accent: "#3db8e8",
    accent2: "#1f7fa8",
    motif: "flask",
    cloth: { tone: -0.025 },
  },
  "writing-note": {
    accent: "#6d8cff",
    accent2: "#3a52cc",
    motif: "pen",
    cloth: { hue: 280 },
  },
  "design-note": {
    accent: "#ff9f43",
    accent2: "#cc6f1a",
    motif: "golden",
    cloth: { hue: 64, tone: 0.045 },
  },

  // ── 個人 ──────────────────────────────────────────────
  "growth-note": {
    accent: "#4fc26b",
    accent2: "#2f8f46",
    motif: "growth",
    cloth: { hue: 142, tone: 0.05 },
  },
  "habits-note": {
    accent: "#4fc26b",
    accent2: "#2f8f46",
    motif: "cycle",
    cloth: { hue: 130, tone: 0.04 },
  },
  "relationships-note": {
    accent: "#ff7a9c",
    accent2: "#d64d72",
    motif: "link",
    cloth: { hue: 5 },
  },
  "life-meaning-note": {
    accent: "#c264d6",
    accent2: "#8f3fa0",
    motif: "mountain",
    cloth: { hue: 322, tone: 0.025 },
  },
  "image-style-note": {
    accent: "#38b6c9",
    accent2: "#1f8090",
    motif: "hanger",
    cloth: { hue: 219, tone: -0.05 },
  },
  "tools-note": {
    accent: "#7c6dff",
    accent2: "#4f46e5",
    motif: "checklist",
    cloth: { hue: 269, tone: -0.025 },
  },
  "wellness-note": {
    accent: "#34c98a",
    accent2: "#1f8f63",
    motif: "pulse",
    cloth: { hue: 159, tone: -0.025 },
  },

  // ── 信仰（同一金色家族，各自不同符號）────────────────
  "biblical-studies-note": {
    accent: "#d9903d",
    accent2: "#a86a1f",
    motif: "scroll",
    cloth: { hue: 56, tone: 0.025 },
  },
  "theology-note": {
    accent: "#e0b04a",
    accent2: "#a8781f",
    motif: "celtic",
    cloth: { hue: 88, tone: 0.025 },
  },
  "spiritual-formation-note": {
    accent: "#e0a93c",
    accent2: "#a8781f",
    motif: "sprout",
    cloth: { hue: 70, tone: -0.05 },
  },
  "pastoral-psychology-note": {
    accent: "#dda545",
    accent2: "#a8781f",
    motif: "shepherd",
    cloth: { hue: 70 },
  },
};
