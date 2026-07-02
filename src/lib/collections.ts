// 內容集合的共用小工具：slug 正規化、建索引、排序。
// 各注入路由 / layout 共用，避免重複 `new Map(...pop())` 與 importance 排序樣板。

/** collection id（形如 "naming/foo"）取最後一段作為 bare slug。 */
export const bareSlug = (id: string): string => id.split("/").pop()!;

/** 用 bare slug 當 key 建索引，供反向 / 交叉連結查找。 */
export function bySlug<T extends { id: string }>(items: T[]): Map<string, T> {
  return new Map(items.map((x) => [bareSlug(x.id), x]));
}

/** 排序 comparator：importance 高→低，同分再依 title 本地化排序。 */
export function byImportance<
  T extends { data: { importance: number; title: string } },
>(a: T, b: T): number {
  return b.data.importance - a.data.importance || a.data.title.localeCompare(b.data.title);
}
