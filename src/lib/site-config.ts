// 各站身分設定：把「因站而異」的少數字串集中成一個型別安全的物件。
// 版面（layouts / components / global.scss）現由 notes-core 提供，各站只需給這份設定 +
// src/data/*.ts（分類/領域資料）+ src/content/**（內容）。
//
// 用法（各站 src/site.config.ts）：
//   import { defineSite } from "@nplus-father/notes-core/site";
//   export const site = defineSite({ brand: "…", titleBase: "…", hasProblems: false });

export interface NavLink {
  // base-relative，如 "/concepts/"（會經 withBase 前綴 base）；
  // 若為絕對 http(s) 網址（如姊妹 handbook 站），則原樣輸出並以新分頁開啟。
  href: string;
  label: string; // 顯示文字（標準四項為 emoji，見 buildNav）
  /** hover／aria-label 用的英文全名（emoji 項必填；extraNav 可省略） */
  title?: string;
}

export interface SiteConfig {
  /** topnav 品牌字，如 "SysDesign Notes" */
  brand: string;
  /** <title> 主幹，如 "系統設計"；layout 會補「概念」/「題」後綴 */
  titleBase: string;
  /**
   * 選用：完全覆寫 topnav 連結。多數站不用填——nav 由 buildNav() 自動生成
   * 固定 emoji 項（🧠 /（📝）/（✅）/ 🔍，不含首頁，左上人像已連 home）。
   * 只有需要完全掌控順序/內容的特例才給這個。
   */
  nav?: NavLink[];
  /** 選用：額外 nav 連結（如姊妹 handbook），插在 Search 之前。想配 emoji 自己寫進 label。 */
  extraNav?: NavLink[];
  /** 選用：概念區的英文標籤，預設 "Concepts"（如 design-patterns 設 "Patterns"）。v0.19.0 起只用於麵包屑／頁標題，不再影響 nav（nav 一律 emoji）。 */
  conceptLabelEn?: string;
  /** 選用：題庫區的英文標籤，預設 "Problems"（如 behaviour 設 "Competencies"）。v0.19.0 起只用於麵包屑／頁標題，不再影響 nav（nav 一律 emoji）。 */
  problemLabelEn?: string;
  /**
   * @deprecated 原為複習紀錄的 localStorage 命名空間；該機制已移除，core 內已無人讀取。
   * v0.11.0 起轉 optional，各站 site.config.ts 已於 2026-07-30 全數清除此欄；
   * 型別暫留給零星未升版的消費者，下個 major 移除。
   */
  ns?: string;
  /** 是否有題庫（problems）集合。純概念站為 false。 */
  hasProblems: boolean;
  /** 頁尾文字，預設「© 2026 Andrew」 */
  footer?: string;
  /**
   * 選用：頁尾「回母站」連結（技術筆記星系入口）。各站同屬 nplus.wiki 底下，故預設即連母站——
   * 不填 → 用預設 `{ href: "https://nplus.wiki/", label: "nplus.wiki 筆記星系" }`（零設定即有）；
   * 設 `null` → 隱藏；給物件 → 覆寫文字／網址。回母站採同分頁導覽（不開新頁）。
   */
  parentSite?: { href: string; label: string } | null;
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

/**
 * 生成 topnav 連結。統一在 core，各站不再手寫 nav：
 *   🧠 Concepts /（📝 Problems，僅 hasProblems）/（✅ Check，僅 hasCheck）/ …extraNav / 🔍 Search
 * 全星系固定這四個詞彙、只出 emoji（hover／aria-label 帶英文全名）——
 * conceptLabelEn / problemLabelEn 不再影響 nav。不含「首頁」——左上人像已連 home。
 * hasCheck 由 BaseLayout 依 categories 的 mastery 判定（有檢核資料才出 ✅）。
 * 若站台給了 `nav` 則原樣採用（完全覆寫的逃生口）。
 */
export function buildNav(c: SiteConfig, opts: { hasCheck?: boolean } = {}): NavLink[] {
  if (c.nav) return c.nav;
  return [
    { href: "/concepts/", label: "🧠", title: "Concepts" },
    ...(c.hasProblems ? [{ href: "/problems/", label: "📝", title: "Problems" }] : []),
    ...(opts.hasCheck ? [{ href: "/check/", label: "✅", title: "Check" }] : []),
    ...(c.extraNav ?? []),
    { href: "/search/", label: "🔍", title: "Search" },
  ];
}
