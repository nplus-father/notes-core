// 技術筆記星系 registry —— 星系內部（建置期）跨站連結、姊妹站選單、sitemap 的 single source of truth。
//
// 遠端撈取（批次腳本 / CI）另有 GitHub topic `nplus-note`：
//   gh repo list nplus-father --topic nplus-note
// 本檔則是「站與站互連」用的權威清單；新站請 append（new-note.sh 會自動插在 __NEW_SITE__ 之前）。
export interface Site {
  key: string; // seeAlso 用的短鍵（= slug 去掉 -note），亦即跨站連結的識別子
  slug: string; // GitHub repo 名 = nplus.wiki 子路徑（如 system-design-note）
  brand: string; // 英文顯示名（topnav / 站縮圖 cover.svg）
  ns: string; // 複習紀錄 localStorage 前綴，各站唯一
}

export const sites: Site[] = [
  { key: "system-design", slug: "system-design-note", brand: "SysDesign Notes", ns: "sd" },
  { key: "data-systems", slug: "data-systems-note", brand: "Data Systems Notes", ns: "ds" },
  { key: "cloud-infra", slug: "cloud-infra-note", brand: "Cloud-Infra Notes", ns: "ci" },
  { key: "clean-code", slug: "clean-code-note", brand: "Clean Code Notes", ns: "cc" },
  { key: "design-patterns", slug: "design-patterns-note", brand: "Design Patterns Notes", ns: "dp" },
  { key: "leet-code", slug: "leet-code-note", brand: "LeetKode", ns: "lk" },
  { key: "behaviour-interview", slug: "behaviour-interview-note", brand: "Behaviour Interview Notes", ns: "bi" },
  // __NEW_SITE__ (new-note.sh 會在此行前插入新站)
];

// 跨站連結（seeAlso）合法的 site key 清單；各站 content.config.ts 的 z.enum 應吃這個。
export const siteKeys = sites.map((s) => s.key) as [string, ...string[]];

export const siteBySlug = new Map(sites.map((s) => [s.slug, s]));
export const siteByKey = new Map(sites.map((s) => [s.key, s]));
