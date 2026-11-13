// 各站身分設定：把「因站而異」的少數字串集中成一個型別安全的物件。
// 版面（layouts / components / global.scss）現由 notes-core 提供，各站只需給這份設定 +
// src/data/*.ts（分類/領域資料）+ src/content/**（內容）。
//
// 用法（各站 src/site.config.ts）：
//   import { defineSite } from "@nplus-father/notes-core/site";
//   export const site = defineSite({ brand: "…", titleBase: "…", hasProblems: false });

import type { IconName } from "./icons";

export interface NavLink {
  // base-relative，如 "/concepts/"（會經 withBase 前綴 base）；
  // 若為絕對 http(s) 網址（如姊妹 handbook 站），則原樣輸出並以新分頁開啟。
  href: string;
  label: string;
  title?: string;
  icon?: IconName;
}

export interface ResolvedNavLink {
  href: string;
  text: string;
  title: string;
  icon: IconName;
  external: boolean;
}

export interface SiteConfig {
  /** topnav 品牌字，如 "SysDesign Notes" */
  brand: string;
  /** <title> 主幹，如 "系統設計"；layout 會補「概念」/「題」後綴 */
  titleBase: string;
  /**
   * 選用：完全覆寫 topnav 連結。多數站不用填——nav 由 buildNav() 自動生成
   * 固定項（Concepts /（Problems）/（Check）/ Search，不含首頁，左上人像已連 home）。
   * 只有需要完全掌控順序/內容的特例才給這個。
   */
  nav?: NavLink[];
  /** 選用：額外 nav 連結（如姊妹 handbook），插在 Search 之前。 */
  extraNav?: NavLink[];
  /** 選用：概念區的英文標籤，預設 "Concepts"（如 design-patterns 設 "Patterns"）。v0.19.0 起只用於麵包屑／頁標題，不再影響 nav。 */
  conceptLabelEn?: string;
  /** 選用：題庫區的英文標籤，預設 "Problems"（如 behaviour 設 "Competencies"）。v0.19.0 起只用於麵包屑／頁標題，不再影響 nav。 */
  problemLabelEn?: string;
  /**
   * @deprecated 原為複習紀錄的 localStorage 命名空間；該機制已移除，core 內已無人讀取。
   * v0.11.0 起轉 optional，各站 site.config.ts 已於 2026-07-30 全數清除此欄；
   * 型別暫留給零星未升版的消費者，下個 major 移除。
   */
  ns?: string;
  /** 是否有題庫（problems）集合。純概念站為 false。 */
  hasProblems: boolean;
  showStationInNav?: boolean;
  /** 頁尾文字，預設「© 2026 Andrew」 */
  footer?: string;
  /**
   * 選用：站台保養戳記（`/note-check` 收工時蓋）。記日期而非布林——「做完了」會過期
   * （書單再進新書、內容再翻修，落差就重新打開），日期自帶時效判讀；AI 端還能拿它對
   * `git log --since` 算出「戳記之後動過什麼」。流向：頁尾徽章（BaseLayout）＋
   * `/index.json`（portal 匯總各站顯示）。
   */
  curation?: {
    /** 最近一次全站體檢（`/note-check`）收工日，YYYY-MM-DD */
    checkedAt?: string;
    /** 最近一次內容補齊（`--enrich` 批次）收工日，YYYY-MM-DD */
    enrichedAt?: string;
  };
  /**
   * 選用：「回母站」連結（筆記星系入口），同時出現在 topnav 最左與頁尾。各站同屬
   * nplus.wiki 底下，故預設即連母站——不填 → 用 `DEFAULT_PARENT_SITE`（零設定即有）；
   * 設 `null` → 兩處都隱藏；給物件 → 覆寫文字／網址。回母站採同分頁導覽（不開新頁）。
   * `short` 是 topnav 用的短名（省略則沿用 `label`）——導覽列塞不下全名。
   */
  parentSite?: { href: string; label: string; short?: string } | null;
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

/**
 * 母站預設值：連 `/notes/` 這個筆記索引頁，而非 nplus.wiki 根。
 * 根頁是整個 wiki（書站 + 筆記站 + 其他）的門面；從一個筆記站往上一層，該落回的是
 * 「主題 37 站 / 人物 28 站」那張索引——上一層就是筆記星系本身，不是整個站群。
 */
export const DEFAULT_PARENT_SITE = {
  href: "https://nplus.wiki/notes/",
  label: "nplus.wiki 筆記星系",
  short: "筆記星系",
};

/** 身分設定 helper：純粹回傳原物件，提供型別檢查與 IDE 補全。 */
export function defineSite(c: SiteConfig): SiteConfig {
  return c;
}

export function buildNav(
  c: SiteConfig,
  opts: { hasCheck?: boolean; hasGuide?: boolean; hasLibrary?: boolean } = {}
): NavLink[] {
  if (c.nav) return c.nav;
  return [
    ...(opts.hasGuide
      ? [{ href: "/guide/", label: "Guide", title: "Guide", icon: "guide" as const }]
      : []),
    { href: "/concepts/", label: "Concepts", title: "Concepts", icon: "concepts" },
    ...(c.hasProblems
      ? [{ href: "/problems/", label: "Problems", title: "Problems", icon: "problems" as const }]
      : []),
    ...(opts.hasCheck
      ? [{ href: "/check/", label: "Check", title: "Check", icon: "check" as const }]
      : []),
    ...(c.extraNav ?? []),
    { href: "/search/", label: "Search", title: "Search", icon: "search" },
    ...(opts.hasLibrary
      ? [{ href: "/library/", label: "Library", title: "Library", icon: "library" as const }]
      : []),
  ];
}

const EMOJI_ICON: Record<string, IconName> = {
  "📖": "guide",
  "🧠": "concepts",
  "📝": "problems",
  "✅": "check",
  "🔍": "search",
  "🔎": "search",
  "📚": "library",
  "📘": "handbook",
  "📗": "handbook",
  "📙": "handbook",
  "📕": "handbook",
  "🗄": "archive",
};

const EMOJI = /\p{Extended_Pictographic}|\u{FE0F}|\u{200D}|\u{20E3}/gu;

export function stripEmoji(text: string): string {
  return text.replace(EMOJI, "").replace(/\s+/g, " ").trim();
}

export function resolveNavLink(l: NavLink): ResolvedNavLink {
  const external = /^https?:\/\//.test(l.href);
  const glyph = [...l.label].find((ch) => EMOJI_ICON[ch]);
  const icon: IconName =
    l.icon ?? (glyph ? EMOJI_ICON[glyph] : external ? "arrow-up-right" : "bookmark");
  const title = stripEmoji(l.title ?? "") || stripEmoji(l.label) || l.href;
  const short = icon === "handbook" ? "Handbook" : title.replace(/\s+Notes$/, "");
  const text = stripEmoji(l.label) || short;
  return { href: l.href, text, title, icon, external };
}
