// 各站身分設定：把「因站而異」的少數字串集中成一個型別安全的物件。
// 版面（layouts / components / global.scss）現由 notes-core 提供，各站只需給這份設定 +
// src/data/*.ts（分類/領域資料）+ src/content/**（內容）。
//
// 用法（各站 src/site.config.ts）：
//   import { defineSite } from "@nplus-father/notes-core/site";
//   export const site = defineSite({ brand: "…", titleBase: "…", nav: […], ns: "cc", hasProblems: false });

export interface NavLink {
  href: string; // base-relative，如 "/concepts/"（會經 withBase 前綴 base）
  label: string; // 顯示文字
}

export interface SiteConfig {
  /** topnav 品牌字，如 "SysDesign Notes" */
  brand: string;
  /** <title> 主幹，如 "系統設計"；layout 會補「概念」/「題」後綴 */
  titleBase: string;
  /** topnav 連結（順序與是否含題庫因站而異） */
  nav: NavLink[];
  /** 複習紀錄 localStorage 命名空間（各站唯一，如 "sd"）。實際 key 為 `${ns}-reviews`。 */
  ns: string;
  /** 是否有題庫（problems）集合。純概念站為 false。 */
  hasProblems: boolean;
  /** 頁尾文字，預設「© 2026 Andrew」 */
  footer?: string;
  /** 選用：覆寫品牌主色（--accent），不填則用共用設計系統的預設 indigo。 */
  accentOverride?: string;
  /** 選用：概念區的顯示標籤（麵包屑），預設「概念」；有些站叫「主題」。 */
  conceptLabel?: string;
  /** 選用：概念頁 <title> 後綴（預設「概念」）；設 "" 則 title 只到 titleBase。 */
  conceptSuffix?: string;
  /** 首頁 <title> 副標，組成 `${brand} · ${tagline}`。 */
  tagline?: string;
  /** 首頁 hero 段落（允許行內 HTML，如 <strong>/<a>）。 */
  heroLede?: string;
  /** 選用：搜尋頁說明（允許行內 HTML）。 */
  searchLede?: string;
  /** 選用：搜尋框 placeholder（預設「搜尋筆記…」）。 */
  searchPlaceholder?: string;
  /** 選用：首頁是否顯示分類卡片格（純概念站常用；雙集合站常關）。 */
  homeShowCategories?: boolean;
  /** 選用：題庫區顯示標籤（麵包屑 / 標題），預設「題庫」。 */
  problemLabel?: string;
  /** 選用：題庫首頁說明（允許行內 HTML）。 */
  problemsLede?: string;
  /** 選用：題庫頁 <title> 後綴（預設「題」）。 */
  problemSuffix?: string;
}

/** 身分設定 helper：純粹回傳原物件，提供型別檢查與 IDE 補全。 */
export function defineSite(c: SiteConfig): SiteConfig {
  return c;
}
