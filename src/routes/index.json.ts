// 本站概念的機器可讀索引，供站外消費者取用（第一個是每日書摘推播：
// nplus-backend 逐站抓取後選出當天要推的一則）。
//
// 契約與 nplus.wiki 上其他公開 JSON 一致：靜態產生、無執行期後端。
// 各欄位皆取自 frontmatter，不做加工——它是筆記內容的忠實投影，
// 消費端要怎麼排序、怎麼呈現由消費端決定。
import type { APIRoute } from "astro";
import { getCollection } from "astro:content";
import { site, bibliography, overview } from "virtual:notes-core/site";
import type { BibliographyEntry } from "../lib/library";
import { auditStation, type Citation } from "../lib/audit";
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
    (acc, e) =>
      (e.data as { writtenAt: string }).writtenAt > acc
        ? (e.data as { writtenAt: string }).writtenAt
        : acc,
    "",
  );

  // 星系 registry（sites.ts）是知識軸的正本；站台不重複宣告，這裡查表帶出去，
  // 讓 nplus.wiki portal 不必靠 GitHub repo description（那 62 個 repo 全是空的）
  // 就能把筆記分成「主題 / 人物」兩區。查不到（尚未入列）就給 null，消費端自行退回。
  const entry = siteBySlug.get(stationSlug()) ?? null;

  // 判層稽核（v0.42.0）——在站台這裡算，因為空頭支票要比對導覽散文，而散文只有
  // 站台有。算完發佈結論，portal 與 CLI 消費同一份，不各寫一份實作。
  const guideBooks = new Set(
    guide.flatMap((e) =>
      (
        (e.data as { furtherReading?: { book: string }[] }).furtherReading ?? []
      ).map((f) => f.book),
    ),
  );
  // 導覽散文要連首頁總覽一起算——那是讀者最先看到的策展文字，一本書在那裡被介紹過，
  // 就不是「從導覽消失」。漏掉它會多報空頭支票：2026-08-24 的實作對帳就抓到 4 筆
  // （cloud-infra／design-patterns／investing／writing），全是只在 overview 提過的書。
  const guideProse = [
    JSON.stringify(overview ?? null),
    ...guide.map((e) => e.body ?? ""),
  ].join("\n");
  const cites: Record<string, Citation> = {};
  for (const e of [...concepts, ...problems]) {
    const seen = new Set<string>();
    for (const f of (e.data as { furtherReading?: { book: string }[] })
      .furtherReading ?? []) {
      cites[f.book] ??= { n: 0, pages: 0 };
      cites[f.book].n += 1;
      if (!seen.has(f.book)) {
        seen.add(f.book);
        cites[f.book].pages += 1;
      }
    }
  }
  const library = (bibliography as BibliographyEntry[]).map((b) => ({
    slug: b.slug ?? null,
    title: b.title,
    original: b.original,
    status: b.status,
    tier: b.tier ?? null,
    delegatedTo: b.delegatedTo ?? null,
  }));
  const audit = auditStation({
    bibliography: library,
    citations: cites,
    guideBooks,
    guideProse,
    guideWrittenAt,
    enrichedAt: site.curation?.enrichedAt ?? null,
  });

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
    // `books` = 導覽章節 furtherReading 掛到的書（去重）。這是**強訊號**——導覽正文
    // 另外會用書名提到書，那個弱訊號只有站台看得到原文，所以判空頭支票是在上面的
    // audit 裡算完才發佈的，消費端不必也不該拿這串自己重算。
    guide:
      guide.length > 0
        ? {
            chapters: guide.length,
            writtenAt: guideWrittenAt,
            books: [...guideBooks],
          }
        : null,
    // 盤點表（v0.40.0）：本站收了哪些書、各判什麼層。**這是判層稽核的另一半**——
    // 另一半（誰引了誰）本來就在下面的 concepts[].furtherReading 裡。兩半都在同一份
    // JSON 之後，nplus.wiki portal 每天抓 /index.json 時就能算出全星系的判層違約
    // （脊梁零引用＝真欠債、支架沒被導覽提到＝空頭支票、姊妹站沒接住＝漏接），
    // 不必 clone 76 個 repo 才跑得動 tier-audit.py。
    //
    // 只吐判層需要的欄位，不吐 note/year——那些是站內呈現用的，
    // 讓消費端拿 slug 回頭查書 repo 比較誠實（書名的正本在書那邊，不在這裡）。
    library,
    // 每本書被幾頁引用（n＝次數、pages＝散在幾個不同的頁）。判「跨頁承重」看 pages，
    // 不看 n；聚合端另外要用它判姊妹站有沒有接住 delegated 的書。
    citations: cites,
    // 判層稽核結論（站台自己算，見 lib/audit.ts）。`delegated` 那欄不是違約清單，
    // 是「請聚合端去問姊妹站」的待判項——本站無從得知別站收了沒。
    audit,
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
              url: new URL(withBase(`problems/${domain}/${slug}/`), ctx.site)
                .href,
              essence: essence(entry.body ?? ""),
              related: d.related,
              // 題目頁一樣會掛書（v0.40.0 補上）。少了它，有題庫的站在站外算判層
              // 會少算引用，把「其實有題目在引它」的脊梁誤報成真欠債。
              furtherReading: d.furtherReading,
            };
          }),
        }
      : {}),
  };

  return new Response(JSON.stringify(payload, null, 2), {
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
};
