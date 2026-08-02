// 站縮圖（首頁 hero）。由 core 產生，不再是各站 public/cover.svg 那張靜態檔——
// 62 站原本共用同一張 indigo→violet 對角漸層 + 白 sheen + 四顆隨機小圓點 + Inter 800
// 負字距，那正是「AI 生成感」最集中的一處：62 個站台放在一起看就是同一個模板。
//
// 改走印刷語彙，讓 62 站讀起來像一套書系而不是一批生成圖：
//   - 紙色底 + 髮絲外框，不用漸層、不用光暈、不用裝飾圓點
//   - 中文站名走襯線體大字（人物站 = 傳主中文名），英文 brand 走寬字距小字當副題
//   - 右上角編號 N°，同軸內依 registry 順序編（append 新站不會動到既有編號）
//   - 主題站 / 人物站各一種墨色，其餘一律相同——刻意的一致，這是套書不是個展
//
// 路由刻意叫 /site-cover.svg 而不是 /cover.svg：各站 public/cover.svg 還在時會蓋掉
// 同名注入路由，那會讓 core 改了卻看不出變化（靜默無效比壞掉更糟）。舊檔留著無害，
// 之後掃掉即可。
import type { APIRoute } from "astro";
import { site } from "virtual:notes-core/site";
import { siteBySlug, topicSites, personSites } from "../lib/sites";

export const prerender = true;

const W = 1200;
const H = 630;
const PAD = 90;

/** 紙色與墨色。主題站偏冷灰藍，人物站偏暖褐——只差這一階，仍是同一套。 */
const INK = {
  topic: "#2f4858",
  person: "#5c4433",
} as const;
const PAPER = "#faf9f7";
const RULE = "#dcd8d2";
const TEXT = "#31302e";
const TEXT_SOFT = "#6b665f";
const TEXT_FAINT = "#a39e98";

function esc(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

/** base 是 '/drucker-note/' 這種形式 → 取站台 slug。 */
function stationSlug(): string {
  return import.meta.env.BASE_URL.replace(/^\/|\/$/g, "") || "";
}

/**
 * 粗估字串的 em 寬（CJK 全寬算 1，其餘算 0.55），用來把大字塞進版面寬度內。
 * 不求精準，只要不溢出——溢出比小一級難看得多。
 */
function emWidth(s: string): number {
  let w = 0;
  for (const ch of s) {
    w += /[　-鿿＀-￯]/.test(ch) ? 1 : 0.55;
  }
  return w;
}

/** 讓 text 在 maxPx 內的最大字級（上限 108、下限 48）。 */
function fitSize(text: string, maxPx: number): number {
  const em = emWidth(text) || 1;
  return Math.max(48, Math.min(108, Math.floor(maxPx / em)));
}

function truncate(s: string, max: number): string {
  return s.length > max ? s.slice(0, max - 1) + "…" : s;
}

export const GET: APIRoute = () => {
  const slug = stationSlug();
  const entry = siteBySlug.get(slug);
  const axis = entry?.axis ?? "topic";
  const ink = INK[axis];

  // 主標：人物站用傳主中文名，主題站用中文短名；registry 查不到就退回站台 titleBase。
  const heading =
    (axis === "person" ? entry?.subject?.nameZh : entry?.label) ??
    site.titleBase ??
    site.brand;
  // 同軸內編號——新站 append 在該軸尾端，既有編號因此穩定。
  const pool = axis === "person" ? personSites : topicSites;
  const idx = pool.findIndex((s) => s.slug === slug);
  const serial = idx >= 0 ? String(idx + 1).padStart(2, "0") : "";

  const headingSize = fitSize(heading, W - PAD * 2 - 120);
  const brand = truncate(site.brand, 40);
  const tagline = truncate(site.tagline ?? "", 34);

  // 必須明確列出 'Noto Serif CJK TC'：generic `serif` 在 Linux（含 CI runner）解析
  // 中文字時會落到 Noto Sans CJK，襯線意圖會靜默失效——實測 Chrome 上 font-family:serif
  // 的中文與 sans-serif 完全同一套字。'Noto Serif TC' 才是 macOS/Windows 那邊的名字。
  const serifStack =
    "'Noto Serif TC','Noto Serif CJK TC','Source Han Serif TC','Songti TC','Songti SC',Georgia,'Times New Roman',serif";
  const sansStack =
    "'Inter',-apple-system,'Segoe UI','Noto Sans TC','PingFang TC',sans-serif";

  const baseline = 372;

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(site.brand)}">
  <rect width="${W}" height="${H}" fill="${PAPER}"/>
  <rect x="28.5" y="28.5" width="${W - 57}" height="${H - 57}" fill="none" stroke="${RULE}" stroke-width="1"/>

  <text x="${PAD}" y="128" font-family="${sansStack}" font-size="22" font-weight="600" letter-spacing="9" fill="${TEXT_FAINT}">${axis === "person" ? "人物" : "主題"}</text>
  ${serial ? `<text x="${W - PAD}" y="128" text-anchor="end" font-family="${serifStack}" font-size="30" fill="${TEXT_FAINT}">N°${serial}</text>` : ""}

  <text x="${PAD}" y="${baseline}" font-family="${serifStack}" font-size="${headingSize}" font-weight="600" letter-spacing="4" fill="${TEXT}">${esc(heading)}</text>
  <rect x="${PAD}" y="${baseline + 46}" width="104" height="2" fill="${ink}"/>
  <text x="${PAD}" y="${baseline + 108}" font-family="${sansStack}" font-size="28" font-weight="500" letter-spacing="6" fill="${TEXT_SOFT}">${esc(brand)}</text>

  ${tagline ? `<text x="${PAD}" y="${H - 78}" font-family="${sansStack}" font-size="22" font-weight="400" letter-spacing="1" fill="${TEXT_FAINT}">${esc(tagline)}</text>` : ""}
  <text x="${W - PAD}" y="${H - 78}" text-anchor="end" font-family="${sansStack}" font-size="20" font-weight="500" letter-spacing="4" fill="${TEXT_FAINT}">nplus.wiki</text>
</svg>
`;

  return new Response(svg, {
    headers: { "Content-Type": "image/svg+xml; charset=utf-8" },
  });
};
