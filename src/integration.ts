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
import type { AstroIntegration } from "astro";
import type { SiteConfig } from "./lib/site-config";
// @ts-expect-error — .mjs remark 外掛無型別宣告
import remarkSections from "./plugins/remark-sections.mjs";

export interface NotesCoreData {
  site: SiteConfig;
  books?: unknown[];
  domains?: unknown[];
}

const VIRTUAL_ID = "virtual:notes-core/site";
const RESOLVED_ID = "\0" + VIRTUAL_ID;
const ROUTES = "@nplus-father/notes-core/routes";

export default function notesCore(data: NotesCoreData): AstroIntegration {
  return {
    name: "@nplus-father/notes-core",
    hooks: {
      "astro:config:setup": ({ injectRoute, updateConfig }) => {
        // 標準區塊 heading（::core / ::case / ::takeaways）由 core 統一注入，
        // 附加在各站 astro.config 的 remarkPlugins 之後（故必在 remarkDirective 之後執行）。
        updateConfig({
          markdown: { remarkPlugins: [remarkSections] },
        });

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
        inject(
          "/concepts/[category]/[slug]",
          "concepts/[category]/[slug].astro",
        );
        inject("/search", "search.astro");
        inject("/404", "404.astro");

        if (data.site.hasProblems) {
          inject("/problems", "problems/index.astro");
          inject("/problems/[domain]", "problems/[domain]/index.astro");
          inject("/problems/[domain]/[slug]", "problems/[domain]/[slug].astro");
        }
      },
    },
  };
}
