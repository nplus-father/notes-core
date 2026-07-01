// 站台部署在 GitHub Pages project page 的子路徑（消費端 astro.config 的 base，如 '/system-design-note'）。
// 所有「站內絕對連結」與資源路徑都必須前綴 base，否則上線會 404。
// import.meta.env.BASE_URL 由各消費站台的 Astro/Vite 建置時代換（以「消費端」的 base 為準）：
// base='/' 時為 '/'，project page 時為 '/<repo>/'。

const BASE = import.meta.env.BASE_URL;

/**
 * 把站內路徑接上 base 前綴。傳入可帶或不帶開頭斜線，結果保證單一斜線銜接。
 *   withBase('/')          → '/<base>/'
 *   withBase('concepts/')  → '/<base>/concepts/'
 *   withBase('/search/')   → '/<base>/search/'
 */
export function withBase(path: string = ""): string {
  const clean = path.replace(/^\//, "");
  return BASE.replace(/\/$/, "") + "/" + clean;
}
