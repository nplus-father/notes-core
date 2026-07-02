// virtual:notes-core/site 由 integration.ts 的 Vite plugin 在建置期產生，
// 內容 = 消費站台傳入整合器的身分與資料。此宣告讓路由檔的 import 有型別。
declare module "virtual:notes-core/site" {
  import type { SiteConfig } from "./lib/site-config";
  export const site: SiteConfig;
  export const books: any[];
  export const domains: any[];
  export const domainBySlug: Map<string, any>;
}
