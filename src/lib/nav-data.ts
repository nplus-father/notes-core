// 從 `categories` 內容集合（concepts/<cat>/_index.md 的 frontmatter）讀出分類設定，
// 供注入路由使用。slug = 分類資料夾名（由 collection id 去掉尾端 /_index 得到）。
import { getCollection } from "astro:content";

export interface CategoryData {
  slug: string;
  name: string;
  icon: string;
  order: number;
  intro: string;
  roadmap: { slug: string; title: string; tier: "basic" | "advanced" }[];
}

export async function getCategories() {
  const entries = await getCollection("categories");
  const categories: CategoryData[] = entries
    .map((e: any) => ({ slug: e.id.replace(/\/_index$/, ""), ...e.data }))
    .sort((a, b) => a.order - b.order);
  const categoryBySlug = new Map(categories.map((c) => [c.slug, c]));
  const roadmap = Object.fromEntries(
    categories.map((c) => [c.slug, c.roadmap]),
  );
  return { categories, categoryBySlug, roadmap };
}

export interface DomainData {
  slug: string;
  name: string;
  icon: string;
  order: number;
  intro: string;
}

export async function getDomains() {
  const entries = await getCollection("domains");
  const domains: DomainData[] = entries
    .map((e: any) => ({ slug: e.id.replace(/\/_index$/, ""), ...e.data }))
    .sort((a, b) => a.order - b.order);
  const domainBySlug = new Map(domains.map((d) => [d.slug, d]));
  return { domains, domainBySlug };
}
