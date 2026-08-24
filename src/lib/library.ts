// 首頁「藏書盤點 / 學派地圖 / 人物側寫」的資料契約。
// 各站在 src/data/*.ts 用 defineBibliography / defineSchools / defineProfile 建資料，
// 經 astro.config 傳入整合器（integration.ts），由首頁（routes/index.astro）渲染：
//   - bibliography：人物站 = 該作者全集盤點；主題站 = 該領域公認經典盤點。
//     已收錄的連書站，缺口（wanted / unavailable）顯示出來，兼作收書 roadmap。
//   - schools：主題站的流派地圖——每派的主張、代表人物（有作者站就跨站連結）、站內分類。
//   - profile：人物站的思想側寫——中心思想、特定貢獻（連站內概念頁）、閱讀路徑、思想脈絡。
//   - overview：首頁總覽（v0.29.0）——一長段散文，讓人一次讀懂「這個領域／這個人」的樣貌。
//     側寫與地圖是結構化的卡片（快速掃），總覽是連貫敘事（讀懂）；兩者互補，不是二選一。

export type BibliographyStatus = "owned" | "wanted" | "unavailable" | "skipped";

/**
 * 要點收錄判層（v0.38.0）——「收進書庫」與「織進要點」是兩回事，這一欄記後者的承諾：
 *   spine 脊梁＝領域正典，該被概念頁引用，0 引用＝真欠債（enrich 的火力目標）
 *   support 支架＝既有頁或導覽一句帶到即可，不欠概念頁
 *   tool 工具書層＝合集／系列書，列盤點即可，不必被引用
 *   delegated 姊妹站分工＝深挖歸 delegatedTo 那站（如 leadership 站的 Drucker 冊歸 drucker）
 * 未標＝待判層（Coverage 圖視同待挖）。判層在 /note-guide 第三章寫經典導讀時回填；
 * note-check audit 只對「spine 且 0 引用」開罰——未挖 ≠ 欠債，先分層再判讀。
 */
export type BibliographyTier = "spine" | "support" | "tool" | "delegated";

/**
 * 四層的語彙正本（v0.43.0）。
 *
 * **為什麼要有這張表**：在這之前，「支架——一句帶到即可，不設專頁」這種句子是各消費端
 * 自己寫的字面值，`/library/` 裡就硬編碼了兩處。結果是 leadership 站那 26 本豁免書，
 * 同一句理由被印了 12 次（約 370 字純重複），而且要改用詞就得四處找。
 * 語彙跟資料一樣需要正本：**這句話只有一個地方能改。**
 *
 * `reason` 寫在**群組標題**上，一層只講一次——不是每一列都掛一次。
 * `dot` 是 CSS 類名：前三層同一族由重到輕（脊梁→支架→工具書是一個深度尺度），
 * 姊妹站另給暖褐（它不在那個尺度上，意思是「帳記到別本去了」）。
 * 刻意不用紅／黃／綠：那是嚴重度語意，而判層不是好壞，是分工。
 */
export const TIER_META: Record<BibliographyTier, { label: string; reason: string; dot: string }> = {
  spine: {
    label: "脊梁",
    reason: "領域正典，該有專屬概念頁",
    dot: "tier-spine",
  },
  support: {
    label: "支架",
    reason: "導覽一句帶到，不設專頁",
    dot: "tier-support",
  },
  tool: { label: "工具書", reason: "查閱用，列盤點即可", dot: "tier-tool" },
  delegated: { label: "姊妹站", reason: "深挖歸別站", dot: "tier-delegated" },
};

/**
 * 作者叢集用的姓氏鍵：**只取第一作者的最後一個詞**。
 *
 * 不能拿整串作者字串去 group——同一位作者的寫法根本不統一（leadership 站上的杜拉克有
 * 「Peter F. Drucker」「…with Joseph A. Maciariello」「…& Joseph A. Maciarello」
 * 「…(edited by Rick Wartzman)」四種），直接比對會把一叢裂成四叢。
 *
 * 也不能拿 token 集合比對：2026-08-24 實測，那會把 David M. Dodson／David Heinemeier
 * Hansson／David Cottrell **三個不同的人**併成一叢（撞名 David），還會把共同作者
 * Maciariello 當成叢主。姓氏才是識別鍵，名字不是。
 *
 * 中文作者沒有可切的姓名結構，整串當鍵。
 */
export function authorKey(author?: string): string {
  const primary = (author ?? "").split(/\s+with\s+|\s*&\s*|\s*\(|\s*（/)[0].trim();
  if (!primary) return "";
  if (!/[A-Za-z]/.test(primary)) return primary;
  const toks = primary.match(/[A-Za-z][A-Za-z'’-]*/g);
  return toks ? toks[toks.length - 1].toLowerCase() : "";
}

export interface BibliographyEntry {
  /** 書名（有中譯用中譯；未收錄的可用原文） */
  title: string;
  /** 原文書名（title 已是原文時省略） */
  original?: string;
  /**
   * 作者（v0.27.0 加）。**目前不渲染**，但請照填——這是星系盤點工具的比對鍵，
   * 不是裝飾欄位。`export-wanted.py` 拿它跟書 repo description 的作者欄做**第二因子**
   * 比對：書名對上還不夠，作者也要對上才算「這本已經有書站了」。
   *
   * 為什麼非有不可：同名不同書會讓人買錯書。portal 上的 `understanding-the-bible`
   * 是 Dorothy L. Johns 的函授查經課程，不是斯托得 1972 年的《認識聖經》；
   * `servant-leadership` 是 Larry W. Boone 的教科書，不是 Greenleaf 的原典。
   * 只比書名的話，這種錯要拿到書才會發現。
   *
   * 寫法不必統一（`John Stott` / `Kent Beck & Martin Fowler` / `馮唐` 都可以），
   * 比對走姓氏 token 交集。合著列到能識別即可，不必抄滿版權頁。
   */
  author?: string;
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
  /** 要點收錄判層（見 BibliographyTier）；未標＝待判層 */
  tier?: BibliographyTier;
  /** tier="delegated" 時：歸屬姊妹站的站代號（sites.ts 的 key，如 "uncle-bob"） */
  delegatedTo?: string;
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

/**
 * 首頁總覽的口味。決定 Overview 的標題與各段的預設骨架（詞彙表收在 Overview.astro，
 * 站台只挑 enum）：`domain` 主題站＝這個領域現在長什麼樣｜`person` 人物站＝這個人是誰。
 */
export type OverviewKind = "domain" | "person";

export interface OverviewSection {
  /** 小標（如「這個領域現在的樣貌」「主要論點」） */
  heading: string;
  /** 段落本文（允許行內 HTML，如 <strong>/<a>）。一段連貫敘事，不要寫成條列。 */
  body: string;
}

export interface SiteOverview {
  kind: OverviewKind;
  /** 一句話把形狀講完，顯示在總覽最前面（允許行內 HTML） */
  lede: string;
  sections: OverviewSection[];
  /**
   * 選配：這份總覽是依「哪一版的站況」寫的，YYYY-MM-DD。書單再進新書、概念頁再翻修，
   * 判讀就會過期——記日期而非布林，跟 site.curation 同一個理由（見 site-config.ts）。
   * `/note-overview` 重寫時蓋上當天日期。
   */
  writtenAt?: string;
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
export function defineOverview(overview: SiteOverview): SiteOverview {
  return overview;
}

/** 首頁書架封面列 = 盤點表中已收錄的書（單一資料源，取代各站手維護的 books.ts）。 */
export function shelfFromBibliography(
  entries: BibliographyEntry[]
): { slug: string; title: string }[] {
  return entries
    .filter((e): e is BibliographyEntry & { slug: string } => e.status === "owned" && !!e.slug)
    .map((e) => ({ slug: e.slug, title: e.title }));
}
