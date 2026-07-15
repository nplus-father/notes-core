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
    else if (lines.length) break; // 引言結束
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

  const payload = {
    station: stationSlug(),
    brand: site.brand,
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
  };

  return new Response(JSON.stringify(payload, null, 2), {
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
};
