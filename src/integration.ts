// Astro 整合器：把整套路由（首頁 / 概念 / 題庫 / 搜尋 / 404）注入消費站台，
// 消費站因此不需要任何 src/pages/**。站台專屬資料（身分、分類、路線圖、書架）
// 由整合器接收後，透過 virtual module `virtual:notes-core/site` 曝露給被注入的路由檔。
//
// 用法（各站 astro.config.mjs）：
//   import notesCore from "@nplus-father/notes-core/integration";
//   import { site } from "./src/site.config";
//   import { categories } from "./src/data/categories";
//   import { roadmap } from "./src/data/roadmap";
//   import { books } from "./src/data/books";
//   integrations: [notesCore({ site, categories, roadmap, books })]
//
// **markdown pipeline 不在這裡**（v0.21.0 起）：remark-sections 原本由本整合器用
// `updateConfig({ markdown: { remarkPlugins: [...] } })` 附加到站台陣列的尾巴，但
// `markdown.remarkPlugins` 已被 Astro 標為 deprecated，取代它的 `markdown.processor`
// 是單一物件、沒有「附加」語義——整條 pipeline 只能在同一個 `unified()` 裡宣告完。
// 因此 remark-sections 搬進 `astro-config.ts` 的 `unified()`，順序不變（仍在最後）。
// 代價：單獨用 `notesCore()` 而不經 `defineNotesAstroConfig()` 的站，不會拿到
// remark-sections——目前 68 站無人如此用（leetcode-note 是舊結構站，連整合器都沒用）。
import type { AstroIntegration } from "astro";
import type { SiteConfig } from "./lib/site-config";

export interface NotesCoreData {
  site: SiteConfig;
  books?: unknown[];
  domains?: unknown[];
  /** 藏書盤點（人物站 = 作者全集；主題站 = 領域經典）。給了它就不必再給 books——書架自動取其中 owned 項。 */
  bibliography?: unknown[];
  /** 主題站的領域地圖：defineSchools 物件（entries/kind/lede），或升版前的純 array（視同 schools 口味）。 */
  schools?: unknown[] | Record<string, unknown>;
  /** 人物站的思想側寫。 */
  profile?: unknown;
  /** 首頁總覽（v0.29.0）：defineOverview 物件（kind/lede/sections）。 */
  overview?: unknown;
}

const VIRTUAL_ID = "virtual:notes-core/site";
const RESOLVED_ID = "\0" + VIRTUAL_ID;
const ROUTES = "@nplus-father/notes-core/routes";

export default function notesCore(data: NotesCoreData): AstroIntegration {
  return {
    name: "@nplus-father/notes-core",
    hooks: {
      "astro:config:setup": ({ injectRoute, updateConfig }) => {
        // 把站台資料序列化成一個 ESM virtual module。皆為純資料（可 JSON 化）。
        updateConfig({
          vite: {
            plugins: [
              {
                name: "notes-core:virtual-site",
                resolveId(id: string) {
                  if (id === VIRTUAL_ID) return RESOLVED_ID;
                  return null;
                },
                load(id: string) {
                  if (id !== RESOLVED_ID) return null;
                  return [
                    `export const site = ${JSON.stringify(data.site)};`,
                    `export const books = ${JSON.stringify(data.books ?? [])};`,
                    `export const domains = ${JSON.stringify(data.domains ?? [])};`,
                    `export const domainBySlug = new Map(domains.map((d) => [d.slug, d]));`,
                    `export const bibliography = ${JSON.stringify(data.bibliography ?? [])};`,
                    `export const schools = ${JSON.stringify(data.schools ?? [])};`,
                    `export const profile = ${JSON.stringify(data.profile ?? null)};`,
                    `export const overview = ${JSON.stringify(data.overview ?? null)};`,
                  ].join("\n");
                },
              },
            ],
          },
        });

        const inject = (pattern: string, file: string) =>
          injectRoute({
            pattern,
            entrypoint: `${ROUTES}/${file}`,
            prerender: true,
          });

        inject("/", "index.astro");
        inject("/concepts", "concepts/index.astro");
        inject("/concepts/[category]", "concepts/[category]/index.astro");
        inject("/concepts/[category]/[slug]", "concepts/[category]/[slug].astro");
        // 檢核頁（出師條件）。恆注入——有沒有 mastery 資料是建置期內容問題，
        // 這裡不知道；沒資料時頁面出空狀態、nav 不出 ✅（見 BaseLayout / check.astro）。
        inject("/check", "check.astro");
        // 導覽頁（策展層長文）。恆注入，同 /check/ 的理由——有沒有 guide 內容是建置期
        // 內容問題；沒資料時頁面出空狀態、nav 不出 📖（見 BaseLayout / guide.astro）。
        inject("/guide", "guide.astro");
        // 藏書頁：盤點表＋開採度（v0.30.0 起自首頁遷出——收藏狀態是工作文件，不是門面）。
        inject("/library", "library.astro");
        inject("/search", "search.astro");
        inject("/404", "404.astro");
        // 本站概念的機器可讀索引，給站外消費者（每日書摘推播靠它選材）。
        inject("/index.json", "index.json.ts");
        // 橫式扉頁 /site-cover.svg 於 v0.36.0 退役：hero 改放直式站封面
        // （public/cover.png，portal 同一張），排版元素攤成活字進 index.astro。
        // 它是「用圖片印出來的文字」且唯一消費者就是 hero；portal 明確不用它。

        if (data.site.hasProblems) {
          inject("/problems", "problems/index.astro");
          inject("/problems/[domain]", "problems/[domain]/index.astro");
          inject("/problems/[domain]/[slug]", "problems/[domain]/[slug].astro");
        }
      },
    },
  };
}
