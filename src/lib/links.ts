// 對外連結（線上書 + 姊妹站）。皆部署在 https://nplus.wiki/<repo>/ 子路徑下，
// 與本站的 base 無關，所以一律組成絕對 URL，不經 withBase()。
//
// 姊妹站的 slug / 中文短名皆取自 sites.ts registry（single source of truth），
// 各站不再各自維護一份 SITE_REPO / siteLabel 對照表。
import { siteByKey } from "./sites";

const WIKI = "https://nplus.wiki";

/** 線上書連結：book = 書本 repo slug，anchor = 書內路徑。 */
export function bookUrl(book: string, anchor = ""): string {
  const a = anchor.replace(/^\//, "");
  return `${WIKI}/${book}/${a}`;
}

/**
 * 書封縮圖 URL：經 wsrv.nl 代理縮放並轉成 WebP。
 *
 * 為何不直接指 `bookUrl(slug, "cover.png")`：那是書 repo 的 900×1200 原始 PNG，
 * 實測平均 280KB，而書架只顯示 132×190。書多的站（leadership-note 有 77 本）
 * 光書架就要吃 21MB；代理後每張約 15KB，同一頁降到約 0.9MB。
 *
 * **原圖仍然是 SSOT**——圖歸書 repo 管，這裡只改「取用時的尺寸與格式」，
 * 書 repo 一個位元都不用動。這也是不能在 build 時處理的原因：圖在別的 repo、
 * 別的網域，build 時去抓等於讓 62 站的建置綁死 1391 個書站的可用性。
 *
 * 代理掛掉時由 Bookshelf 的 error 監聽退回原圖——會變慢，但不會破圖。
 * 不帶 `v=` 版本參數：書封極少改，換來的是所有站共用同一份代理快取。
 */
export function bookCoverUrl(book: string, width = 264): string {
  const target = `${WIKI}/${book}/cover.png`.replace(/^https?:\/\//, "");
  const params = new URLSearchParams({
    url: target,
    w: String(width),
    output: "webp",
    q: "80",
  });
  return `https://wsrv.nl/?${params.toString()}`;
}

/** 姊妹站連結：site = 站代號（sites.ts 的 key），path = 站內路徑。 */
export function siteUrl(site: string, path = ""): string {
  const repo = siteByKey.get(site)?.slug ?? site;
  const p = path.replace(/^\//, "");
  return `${WIKI}/${repo}/${p}`;
}

/** 姊妹站中文短名：site = 站代號；未知時回傳代號本身。 */
export function siteLabel(site: string): string {
  return siteByKey.get(site)?.label ?? site;
}

/**
 * 拆 furtherReading 的 `label`（慣例「書名 — 章節」）成書名與章節，供頁尾卡片
 * （章節當子標題、書名退小字）與頁首 byline（只取書名）共用同一套拆法。
 *
 * **分隔號只認 em/en dash，或前後有空白的 ASCII hyphen。** 不能無條件拆 `-`——
 * 書名本身常含連字號（The Non-Designer's…／High-Performance…／Test-Driven…），
 * 那樣會把書名攔腰斬成「The Non」，且錯的那半正好是卡片最大的字。
 * 沒有分隔號時：整句當章節、書名留空（卡片不出小字）。
 */
export function splitBookLabel(label: string): { book: string; chapter: string } {
  const m = label.match(/\s*[—–]\s*|\s+-\s+/);
  if (!m || m.index === undefined) return { book: "", chapter: label.trim() };
  return {
    book: label.slice(0, m.index).trim(),
    chapter: label.slice(m.index + m[0].length).trim(),
  };
}
