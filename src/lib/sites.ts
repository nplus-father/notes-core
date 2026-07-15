// 技術筆記星系 registry —— 星系內部（建置期）跨站連結、姊妹站選單、sitemap 的 single source of truth。
//
// 遠端撈取（批次腳本 / CI）另有 GitHub topic `nplus-note`：
//   gh repo list nplus-father --topic nplus-note
// 本檔則是「站與站互連」用的權威清單；新站請 append（new-note.sh 會自動插在 __NEW_SITE__ 之前）。
export interface Site {
  key: string; // seeAlso 用的短鍵（= slug 去掉 -note），亦即跨站連結的識別子
  slug: string; // GitHub repo 名 = nplus.wiki 子路徑（如 system-design-note）
  brand: string; // 英文顯示名（topnav / 站縮圖 cover.svg）
  label: string; // 中文短名（跨站連結 siteLabel）
  /** @deprecated 原為複習紀錄的 localStorage 前綴；該機制已移除，已無人讀取。待與 SiteConfig.ns 一併清掉。 */
  ns: string;
}

// 注意：key 一律 = slug 去掉 -note（如 leetcode-note → leetcode），跨站 URL 才組得對。
export const sites: Site[] = [
  { key: "system-design", slug: "system-design-note", brand: "SysDesign Notes", label: "系統設計", ns: "sd" },
  { key: "data-systems", slug: "data-systems-note", brand: "Data Systems Notes", label: "資料系統", ns: "ds" },
  { key: "cloud-infra", slug: "cloud-infra-note", brand: "Cloud-Infra Notes", label: "雲端維運", ns: "ci" },
  { key: "clean-code", slug: "clean-code-note", brand: "Clean Code Notes", label: "程式碼工藝", ns: "cc" },
  { key: "design-patterns", slug: "design-patterns-note", brand: "Design Patterns Notes", label: "設計模式", ns: "dp" },
  { key: "leetcode", slug: "leetcode-note", brand: "LeetKode", label: "LeetCode", ns: "lk" },
  { key: "behaviour-interview", slug: "behaviour-interview-note", brand: "Behaviour Interview Notes", label: "行為面試", ns: "bi" },
  // __NEW_SITE__ (new-note.sh 會在此行前插入新站)
];

// 跨站連結（seeAlso）合法的 site key 清單；各站 content.config.ts 的 z.enum 應吃這個。
export const siteKeys = sites.map((s) => s.key) as [string, ...string[]];

export const siteBySlug = new Map(sites.map((s) => [s.slug, s]));
export const siteByKey = new Map(sites.map((s) => [s.key, s]));
