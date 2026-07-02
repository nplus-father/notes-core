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
