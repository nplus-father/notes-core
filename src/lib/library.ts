// 首頁「藏書盤點 / 學派地圖 / 人物側寫」的資料契約。
// 各站在 src/data/*.ts 用 defineBibliography / defineSchools / defineProfile 建資料，
// 經 astro.config 傳入整合器（integration.ts），由首頁（routes/index.astro）渲染：
//   - bibliography：人物站 = 該作者全集盤點；主題站 = 該領域公認經典盤點。
//     已收錄的連書站，缺口（wanted / unavailable）顯示出來，兼作收書 roadmap。
//   - schools：主題站的流派地圖——每派的主張、代表人物（有作者站就跨站連結）、站內分類。
//   - profile：人物站的思想側寫——中心思想、特定貢獻（連站內概念頁）、閱讀路徑、思想脈絡。

export type BibliographyStatus = "owned" | "wanted" | "unavailable" | "skipped";

export interface BibliographyEntry {
  /** 書名（有中譯用中譯；未收錄的可用原文） */
  title: string;
  /** 原文書名（title 已是原文時省略） */
  original?: string;
  /** 初版年 */
  year?: number;
  /** 書 repo slug（nplus.wiki/<slug>/）；status = "owned" 時必填，據此連結＋抓封面 */
  slug?: string;
  /** owned 已收錄｜wanted 待收錄｜unavailable 暫無來源（絕版/無中譯）｜skipped 刻意略過 */
  status: BibliographyStatus;
  /** 註記：為何重要／為何略過／來源狀況 */
  note?: string;
  /** 分組（人物站常用分期，主題站常用流派）；依首次出現順序渲染 */
  group?: string;
}

export interface SchoolFigure {
  name: string;
  /** 姊妹作者站的站代號（sites.ts 的 key，如 "bogle"）；有站才填，渲染成跨站連結 */
  site?: string;
}

export interface School {
  name: string;
  /**
   * @deprecated v0.13.0 起不再渲染——學派卡改用序號記號（與站縮圖的 N° 同一裝置），
   * 不再用 emoji 圖示。型別暫留讓 35 個主題站的 schools.ts 不必同步改動，下個 major 移除。
   */
  icon?: string;
  /** 一句話主張（允許行內 HTML） */
  claim: string;
  figures?: SchoolFigure[];
  /** 對應的站內概念分類 slug（/concepts/<categorySlug>/）；沒有對應分類則省略 */
  categorySlug?: string;
}

/**
 * 領域地圖的口味——決定首頁綜覽區的標題與副標（詞彙表收在 SchoolsMap，要新口味改 core 一處）：
 *   schools（預設）學派地圖＝流派互相對立｜methods 方法地圖＝方法體系並存｜themes 主題地圖＝核心命題分區
 */
export type SchoolsKind = "schools" | "methods" | "themes";

export interface SchoolsData {
  entries: School[];
  kind: SchoolsKind;
  /** 選配：地圖上方一句話提綱挈領（允許行內 HTML） */
  lede?: string;
}

export interface Contribution {
  title: string;
  /** 一句話說明這項貢獻（允許行內 HTML） */
  summary: string;
  /** 站內概念頁路徑 "category/slug"，作為研讀這項貢獻的主軸入口 */
  conceptPath?: string;
}

export interface ReadingStage {
  /** 階段名（如「入門」「核心」「視野」） */
  stage: string;
  /** 這一階段讀的書（bibliography 的 slug；標題由 bibliography 反查） */
  slugs: string[];
  /** 為什麼先讀這些 */
  why: string;
}

export interface Influence {
  name: string;
  /** 姊妹站站代號（sites.ts 的 key）；有站才填 */
  site?: string;
  /** 關係說明（如「創新理論的經濟學源頭」「自稱杜拉克傳人」） */
  note: string;
}

export interface AuthorProfile {
  /** 一句話中心思想（允許行內 HTML），顯示在首頁最顯眼處 */
  thesis: string;
  /** 特定貢獻——讀者研究此人的幾條主軸 */
  contributions: Contribution[];
  readingPath?: ReadingStage[];
  /** 思想脈絡：受誰影響／影響了誰 */
  influences?: Influence[];
}

/** 純 identity helpers：提供型別檢查與 IDE 補全。 */
export function defineBibliography(entries: BibliographyEntry[]): BibliographyEntry[] {
  return entries;
}
export function defineSchools(
  schools: School[],
  meta: { kind?: SchoolsKind; lede?: string } = {}
): SchoolsData {
  return { entries: schools, kind: meta.kind ?? "schools", lede: meta.lede };
}

/** 整合器兩收 array（升版前的舊 schools.ts）｜object：這裡歸一成 SchoolsData。 */
export function normalizeSchools(data: unknown): SchoolsData {
  if (Array.isArray(data)) return { entries: data as School[], kind: "schools" };
  if (data && typeof data === "object" && "entries" in data) return data as SchoolsData;
  return { entries: [], kind: "schools" };
}
export function defineProfile(profile: AuthorProfile): AuthorProfile {
  return profile;
}

/** 首頁書架封面列 = 盤點表中已收錄的書（單一資料源，取代各站手維護的 books.ts）。 */
export function shelfFromBibliography(
  entries: BibliographyEntry[]
): { slug: string; title: string }[] {
  return entries
    .filter((e): e is BibliographyEntry & { slug: string } => e.status === "owned" && !!e.slug)
    .map((e) => ({ slug: e.slug, title: e.title }));
}
