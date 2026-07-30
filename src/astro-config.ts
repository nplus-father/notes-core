// 站台 astro.config 工廠：把 49 站完全相同的 markdown pipeline（remark 外掛順序、
// shiki、sitemap）收進 core，站台只剩 base 與資料。Astro 升版（如 markdown.remarkPlugins
// 的 deprecation）從此只需改這一處。
//
// 用法（各站 astro.config.mjs）：
//   import { defineNotesAstroConfig } from "@nplus-father/notes-core/astro-config";
//   import { site } from "./src/site.config";
//   import { bibliography } from "./src/data/bibliography";
//   import { profile } from "./src/data/profile";   // 或主題站的 schools
//   export default defineNotesAstroConfig({ base: "/drucker-note", site, bibliography, profile });
//
// 依賴解析：sitemap / remark-directive / remark-alert 由消費站的 node_modules 提供
// （versions.json 統一版本，notes-doctor 對齊），core 以 peerDependencies 聲明。
import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import remarkDirective from "remark-directive";
import { remarkAlert } from "remark-github-blockquote-alert";
// @ts-expect-error — .mjs remark 外掛無型別宣告
import remarkDetails from "./plugins/remark-details.mjs";
// @ts-expect-error — .mjs remark 外掛無型別宣告
import remarkResponse from "./plugins/remark-response.mjs";
import notesCore, { type NotesCoreData } from "./integration";

export interface NotesAstroConfigOptions extends NotesCoreData {
  /** 站台 base 路徑 = "/<repo-slug>"（GitHub Pages project page） */
  base: string;
  /** 部署網域，預設 https://nplus.wiki */
  siteUrl?: string;
}

export function defineNotesAstroConfig(opts: NotesAstroConfigOptions) {
  const { base, siteUrl = "https://nplus.wiki", ...data } = opts;
  return defineConfig({
    site: siteUrl,
    base,
    integrations: [sitemap(), notesCore(data)],
    markdown: {
      // 順序重要：directive 先把 ::: 解析成節點，details 再轉成 <details>；
      // integration 會在此之後再附加 remark-sections。
      remarkPlugins: [remarkDirective, remarkDetails, remarkResponse, remarkAlert],
      shikiConfig: {
        themes: { light: "github-light", dark: "github-dark-dimmed" },
        wrap: false,
      },
    },
  });
}
