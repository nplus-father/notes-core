// 內容集合 schema factory：星系內所有站共用同一份 concepts / problems schema。
// 各站 src/content.config.ts 只需：
//   import { defineNoteCollections } from "@nplus-father/notes-core/content";
//   import { site } from "./site.config";
//   export const collections = defineNoteCollections({ hasProblems: site.hasProblems });
//
// 技術站群 seeAlso.site 走 sites.ts 的 siteKeys enum；人文站群傳 openSeeAlso:true 用開放 string。
import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";
import { siteKeys } from "./lib/sites";

// lastReviewed frontmatter 的日期格式：YYYY-MM-DD
const DATE_RE = /^\d{4}-\d{2}-\d{2}$/;

// 延伸閱讀：連到已部署的線上書 https://nplus.wiki/<book>/<anchor?>
const furtherReading = z
  .array(
    z.object({
      book: z.string(), // 書本 repo slug（= nplus.wiki 子路徑）
      label: z.string(), // 顯示文字（書名 + 章節）
      anchor: z.string().optional(), // 書內路徑，如 'docs/2-distributed-data/replication/'
    })
  )
  .default([]);

// concepts / problems 共用的一般欄位。
const commonItemFields = {
  importance: z.number().int().min(1).max(5).default(3),
  status: z.enum(["draft", "studied", "reviewed"]).default("draft"),
  related: z.array(z.string()).default([]), // 其他同型別 slug
  lastReviewed: z.string().regex(DATE_RE).optional(),
};

// 跨站連結：連到姊妹筆記站的某一頁。
// 預設 site 走 sites.ts 的 siteKeys enum（技術站群，可抓拼字錯）；
// 人文站群姊妹不在此 registry，傳 openSeeAlso:true 改用開放 string。
function makeSeeAlso(open: boolean) {
  return z
    .array(
      z.object({
        site: open ? z.string() : z.enum(siteKeys),
        path: z.string(), // 站內路徑，如 'concepts/data-distribution/replication/'
        label: z.string(),
      })
    )
    .default([]);
}

/**
 * 建立本站的內容集合。
 * @param opts.hasProblems 是否含題庫（problems）集合，純概念站傳 false（預設）。
 * @param opts.openSeeAlso seeAlso.site 用開放 string（人文站群）而非 siteKeys enum（技術站群，預設）。
 */
export function defineNoteCollections(opts: { hasProblems?: boolean; openSeeAlso?: boolean } = {}) {
  const seeAlso = makeSeeAlso(opts.openSeeAlso ?? false);

  // 分類設定：每個分類資料夾一個 _index.md，frontmatter 當 config（name/icon/order/intro/roadmap）。
  const categories = defineCollection({
    loader: glob({ pattern: "**/_index.md", base: "./src/content/concepts" }),
    schema: z.object({
      name: z.string(),
      icon: z.string(),
      order: z.number().int().default(999),
      intro: z.string().default(""),
      sister: z.string().optional(), // 選用：此分類的姊妹站 key（深潛連結）
      // 學習路徑：由基礎→進階排序；planned（未寫）節點也列在這，總覽頁畫「待寫」。
      roadmap: z
        .array(
          z.object({
            slug: z.string(),
            title: z.string().default(""),
            tier: z.enum(["basic", "advanced"]).default("basic"),
          })
        )
        .default([]),
      // 檢核清單：「認定讀完此分類時該具備的知識」，一句一條（書本位，須可溯源）。
      // /check/ 頁依分類分組渲染；roadmap 說讀什麼、mastery 說讀完該會什麼。
      // slug = 教這一條的概念頁（同分類內），渲染成「複習 →」回連；省略則無回連。
      mastery: z
        .array(
          z.object({
            text: z.string(),
            slug: z.string().optional(),
          })
        )
        .default([]),
    }),
  });

  // 導覽（v0.30.0）：策展層長文，一章一個 md（src/content/guide/NN-<slug>.md，檔名 NN 定序）。
  // base 釘在 src/content（必存在）而非 src/content/guide——後者在 72 個沒有導覽的站
  // 每次 build 都會印一條 "base directory does not exist" 警語。代價是 id 帶 guide/ 前綴，
  // 消費端（guide.astro / index.json）自行剝掉。
  const guide = defineCollection({
    loader: glob({ pattern: "guide/**/*.md", base: "./src/content" }),
    schema: z.object({
      title: z.string(),
      // 章的撰寫日（時效訊號，流進 index.json 供 /note-check 比對 enrichedAt）。
      // YAML 會把不加引號的 2026-08-14 解析成 Date——這裡收成字串，別讓引號成為每輪
      // /note-guide 產出的隱形地雷。
      writtenAt: z.preprocess(
        (v) => (v instanceof Date ? v.toISOString().slice(0, 10) : v),
        z.string().regex(DATE_RE)
      ),
      furtherReading,
    }),
  });

  // 概念：一頁一個觀念（排除 _index.md，那是分類設定不是概念頁）
  const concepts = defineCollection({
    loader: glob({
      pattern: ["**/*.md", "!**/_index.md"],
      base: "./src/content/concepts",
    }),
    schema: z.object({
      title: z.string(),
      category: z.string(), // 對應 src/data/categories.ts
      problems: z.array(z.string()).default([]), // 用到此概念的 problem slug（反向連結）
      ...commonItemFields,
      furtherReading,
      seeAlso,
    }),
  });

  if (!opts.hasProblems) {
    return { concepts, categories, guide };
  }

  // 領域設定：每個領域資料夾一個 _index.md，frontmatter 當 config（name/icon/order/intro）。
  const domains = defineCollection({
    loader: glob({ pattern: "**/_index.md", base: "./src/content/problems" }),
    schema: z.object({
      name: z.string(),
      icon: z.string(),
      order: z.number().int().default(999),
      intro: z.string().default(""),
    }),
  });

  // 題目：一頁一道題（排除 _index.md，那是領域設定不是題目頁）
  const problems = defineCollection({
    loader: glob({
      pattern: ["**/*.md", "!**/_index.md"],
      base: "./src/content/problems",
    }),
    schema: z.object({
      title: z.string(),
      domain: z.string(), // 對應 src/data/domains.ts
      difficulty: z.enum(["Easy", "Medium", "Hard"]).default("Medium"),
      concepts: z.array(z.string()).default([]), // 練到的 concept slug（雙向）
      ...commonItemFields,
      furtherReading,
      seeAlso,
    }),
  });

  return { concepts, categories, guide, problems, domains };
}
