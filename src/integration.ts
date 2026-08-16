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
import { existsSync, readFileSync } from "node:fs";
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

/**
 * dev 熱更新（v0.37.0）：各 export 對應的站台檔案，用來把 virtual module 從
 * 「啟動時的 JSON 快照」換成「轉發到真檔案」——見 devReexport 的說明。
 * 站台沒有的檔案（人物站沒 schools.ts、主題站沒 profile.ts）自動退回快照。
 */
const DEV_SOURCES: Record<string, string> = {
  site: "src/site.config.ts",
  books: "src/data/books.ts",
  domains: "src/data/domains.ts",
  bibliography: "src/data/bibliography.ts",
  schools: "src/data/schools.ts",
  profile: "src/data/profile.ts",
  overview: "src/data/overview.ts",
};

/**
 * 若站台真的有這個檔案、且確實 export 同名變數，回傳給 Vite 用的 root 相對路徑；
 * 否則回 null（呼叫端退回 JSON 快照）。
 *
 * 用正則確認 export 名稱，是因為轉發的前提是「config 只是原封不動把該檔案的同名
 * export 轉交給整合器」——這是 68 站現行寫法，但整合器無法強制。名稱對不上就不轉發，
 * 寧可維持舊行為（不熱更新）也不要在 dev 給出跟 build 不一樣的值。
 */
function devReexport(root: URL, key: string): string | null {
  const rel = DEV_SOURCES[key];
  if (!rel) return null;
  const url = new URL(rel, root);
  if (!existsSync(url)) return null;
  const src = readFileSync(url, "utf8");
  if (!new RegExp(`export\\s+(?:const|let|var|function)\\s+${key}\\b`).test(src)) return null;
  return "/" + rel;
}

export default function notesCore(data: NotesCoreData): AstroIntegration {
  return {
    name: "@nplus-father/notes-core",
    hooks: {
      "astro:config:setup": ({ injectRoute, updateConfig, command, config }) => {
        // dev 熱更新（v0.37.0）。問題：這個 virtual module 原本是在**整合器執行的那一刻**
        // 把站台資料 JSON.stringify 成字串，之後那份快照不再更新——所以 dev 時改
        // src/data/*.ts 或 src/site.config.ts，畫面不會動，而且沒有任何提示，看起來就像壞掉。
        // 那些檔案只被 astro.config.mjs import，從沒進過 Vite 的 module graph，連 watch 都沒有。
        //
        // 解法：dev 時不 inline 快照，改成**轉發到站台的真檔案**（`export { x } from "/src/..."`）。
        // 真模組進了 module graph，Vite 自己就會監看它、失效它、推 HMR，改完約 1 秒可見。
        //
        // 為什麼不用 addWatchFile 讓 dev server 重啟：實測 Astro 7.0.7 在 config restart
        // 之後，content layer 的檔案監看不會重新掛上——markdown 從此靜悄悄不再熱更新，
        // 直到完整重跑 npm run dev。那等於拿「改 markdown 不更新」換「改 data 會更新」，
        // 而 markdown 才是改動主力。轉發法不重啟，所以沒有這個代價。
        //
        // build 完全走原本的快照路徑（下面的 snapshot），行為零變動：build 每次都重新
        // 載入 config，本來就拿得到最新值，不需要也不該引入額外的模組相依。
        // 快照：build 用全部，dev 只用轉發不成立的那幾個。順序即產出順序。
        const snapshot: Record<string, string> = {
          site: `export const site = ${JSON.stringify(data.site)};`,
          books: `export const books = ${JSON.stringify(data.books ?? [])};`,
          domains: `export const domains = ${JSON.stringify(data.domains ?? [])};`,
          bibliography: `export const bibliography = ${JSON.stringify(data.bibliography ?? [])};`,
          schools: `export const schools = ${JSON.stringify(data.schools ?? [])};`,
          profile: `export const profile = ${JSON.stringify(data.profile ?? null)};`,
          overview: `export const overview = ${JSON.stringify(data.overview ?? null)};`,
        };
        // domainBySlug 是衍生值，兩條路徑都由 domains 就地算出。
        const derived = `export const domainBySlug = new Map(domains.map((d) => [d.slug, d]));`;

        const body = () => {
          if (command !== "dev") return [...Object.values(snapshot), derived].join("\n");
          // 轉發用 `import` + 集中 `export`，不用 `export ... from`：後者不會在本模組
          // 留下 binding，下面 derived 的 domains.map 會 ReferenceError。
          const imports: string[] = [];
          const inlined: string[] = [];
          const forwarded: string[] = [];
          for (const [key, inlineLine] of Object.entries(snapshot)) {
            const from = devReexport(config.root, key);
            if (from) {
              imports.push(`import { ${key} } from "${from}";`);
              forwarded.push(key);
            } else {
              inlined.push(inlineLine);
            }
          }
          const reexport = forwarded.length ? [`export { ${forwarded.join(", ")} };`] : [];
          return [...imports, ...inlined, ...reexport, derived].join("\n");
        };

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
                  return body();
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
