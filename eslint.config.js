// 星系共用 ESLint flat config。各站 eslint.config.mjs 只需：
//   import config from "@nplus-father/notes-core/eslint";
//   export default config;
// 所需外掛（@eslint/js / typescript-eslint / eslint-plugin-astro）由各站 devDependencies 提供，
// 於各站執行 eslint 時就地解析。
import js from "@eslint/js";
import tseslint from "typescript-eslint";
import astro from "eslint-plugin-astro";

export default [
  js.configs.recommended,
  ...tseslint.configs.recommended,
  ...astro.configs.recommended,
  {
    ignores: ["dist/", ".astro/", "node_modules/", "scripts/", "pagefind/"],
  },
  {
    rules: {
      // 允許以 _ 開頭的未用變數
      "@typescript-eslint/no-unused-vars": ["warn", { argsIgnorePattern: "^_" }],
      // Astro frontmatter 對 content collection 的 map/filter 常用 any；警告不阻擋
      "@typescript-eslint/no-explicit-any": "warn",
      // Astro frontmatter 條件渲染會用 var
      "no-var": "off",
      "no-redeclare": "off",
      "prefer-rest-params": "off",
    },
  },
];
