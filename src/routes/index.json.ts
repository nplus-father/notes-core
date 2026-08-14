// 本站概念的機器可讀索引，供站外消費者取用（第一個是每日書摘推播：
// nplus-backend 逐站抓取後選出當天要推的一則）。
//
// 契約與 nplus.wiki 上其他公開 JSON 一致：靜態產生、無執行期後端。
// 各欄位皆取自 frontmatter，不做加工——它是筆記內容的忠實投影，
// 消費端要怎麼排序、怎麼呈現由消費端決定。
import type { APIRoute } from "astro";
import { getCollection } from "astro:content";
import { site } from "virtual:notes-core/site";
import { withBase } from "../lib/url";
import { siteBySlug } from "../lib/sites";

export const prerender = true;

/**
 * 概念頁開頭的 blockquote —— 全篇的精華，作者自己寫的一句話。
 * 只取開頭連續的 `>` 行；抓不到就回空字串（消費端自行退回用 title）。
 * 保留 markdown 原樣，不做 strip：這裡是索引，不是呈現層。
 */
function essence(body: string): string {
  const lines: string[] = [];
  for (const line of body.trimStart().split("\n")) {
    if (line.startsWith(">")) lines.push(line.replace(/^>\s?/, "").trim());
    else if (lines.length)
      break; // 引言結束
    else if (line.trim()) break; // 開頭不是引言
  }
  return lines.join(" ").trim();
}

/** base 是 '/clean-code-note/' 這種形式 → 取站台 slug（= nplus.wiki 子路徑）。 */
function stationSlug(): string {
  return import.meta.env.BASE_URL.replace(/^\/|\/$/g, "") || "";
}

export const GET: APIRoute = async (ctx) => {
  const concepts = await getCollection("concepts");
  // 雙集合站（hasProblems）另有題庫；索引要一併輸出，消費端才能算全站進度。
  const problems = site.hasProblems ? await getCollection("problems") : [];
  // 導覽（v0.30.0）：章數＋最新 writtenAt。/note-check 拿它比對 enrichedAt——
  // 站再深化過而導覽沒跟上，就該列 warning；portal 也能看出哪些站有導覽。
  const guide = await getCollection("guide");
  const guideWrittenAt = guide.reduce<string>(
    (acc, e) => ((e.data as { writtenAt: string }).writtenAt > acc ? (e.data as { writtenAt: string }).writtenAt : acc),
    ""
  );

  // 星系 registry（sites.ts）是知識軸的正本；站台不重複宣告，這裡查表帶出去，
  // 讓 nplus.wiki portal 不必靠 GitHub repo description（那 62 個 repo 全是空的）
  // 就能把筆記分成「主題 / 人物」兩區。查不到（尚未入列）就給 null，消費端自行退回。
  const entry = siteBySlug.get(stationSlug()) ?? null;

  const payload = {
    station: stationSlug(),
    brand: site.brand,
    label: entry?.label ?? site.titleBase,
    tagline: site.tagline ?? null,
    axis: entry?.axis ?? null,
    // 保養戳記（/note-check 收工日）。portal 拿它顯示「這站體檢／補齊過沒、多久前」；
    // 沒蓋過章就是 null，消費端自行退回不顯示。
    curation: site.curation ?? null,
    // 導覽戳記：沒有導覽的站為 null，消費端自行退回不顯示。
    guide: guide.length > 0 ? { chapters: guide.length, writtenAt: guideWrittenAt } : null,
    conceptCount: concepts.length,
    concepts: concepts.map((entry) => {
      // glob loader 的 id 就是 '<category>/<slug>'，與概念頁路由同源。
      const [category, slug] = entry.id.split("/");
      const d = entry.data;
      return {
        id: entry.id,
        title: d.title,
        category,
        importance: d.importance,
        status: d.status,
        lastReviewed: d.lastReviewed ?? null,
        url: new URL(withBase(`concepts/${category}/${slug}/`), ctx.site).href,
        essence: essence(entry.body ?? ""),
        related: d.related,
        furtherReading: d.furtherReading,
      };
    }),
    ...(site.hasProblems
      ? {
          problemCount: problems.length,
          problems: problems.map((entry) => {
            const [domain, slug] = entry.id.split("/");
            const d = entry.data;
            return {
              id: entry.id,
              title: d.title,
              domain,
              importance: d.importance,
              status: d.status,
              lastReviewed: d.lastReviewed ?? null,
              url: new URL(withBase(`problems/${domain}/${slug}/`), ctx.site).href,
              essence: essence(entry.body ?? ""),
              related: d.related,
            };
          }),
        }
      : {}),
  };

  return new Response(JSON.stringify(payload, null, 2), {
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
};
