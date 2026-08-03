// 主題站封面產生器 —— Style A（深色編輯風）、3:4 直式書封、900x1200。
//
// 資料一律取自 registry，這裡不再自己存一份：
//   sites.ts        中文大字 = label；英文副題 = brand 去掉結尾的 " Notes"
//   site-covers.ts  主色、副色、符號
//
// 舊版（notes/note-cover/cover-gen.mjs）自己存了 title 與 en，結果 35 站有 9 站的
// 中文名跟 registry 對不上——封面上印「領導力」、portal 卡片上寫「領導」。同一個
// 事實存兩份必然漂移，所以那兩個欄位在這一版被刪掉，只能從 sites.ts 推導。
//
// 用法：node cover-gen.mjs <slug> <outHtmlPath>
//   <slug> = 站台資料夾名（如 clean-code-note）
// 產出 HTML 而非直接產圖：中文字型要靠瀏覽器排版，交給 render.sh 用 headless
// Chrome 截圖成 PNG，字型就烘進點陣，不必擔心讀者端沒有同一套字。

import { writeFileSync } from "node:fs";
import { sites } from "../../src/lib/sites.ts";
import { siteCovers } from "../../src/lib/site-covers.ts";
import { MOTIFS } from "./motifs.mjs";

const siteBySlug = new Map(sites.map((s) => [s.slug, s]));
const topicSlugs = sites.filter((s) => s.axis === "topic").map((s) => s.slug);

// ── 啟動對帳：三份資料必須完全對得起來，否則就地停住 ──────────────
const problems = [];

// 1. 每個主題站都要有封面參數；反之封面參數不能指向不存在或非主題站的 slug
for (const slug of topicSlugs) {
  if (!siteCovers[slug]) problems.push(`${slug}: 是主題站但 site-covers.ts 沒有它`);
}
for (const slug of Object.keys(siteCovers)) {
  const s = siteBySlug.get(slug);
  if (!s) problems.push(`${slug}: site-covers.ts 有它但 sites.ts 沒有`);
  else if (s.axis !== "topic") problems.push(`${slug}: 是人物站，不該有封面參數（人物站用肖像照）`);
}

// 2. 一個符號只能屬於一站
const seen = new Map();
for (const [slug, c] of Object.entries(siteCovers)) {
  if (!MOTIFS[c.motif]) problems.push(`${slug}: 符號 '${c.motif}' 不在 motifs.mjs 裡`);
  if (seen.has(c.motif)) problems.push(`符號撞圖：'${c.motif}' 同時被 ${seen.get(c.motif)} 與 ${slug} 使用`);
  seen.set(c.motif, slug);
}

if (problems.length) {
  console.error("registry 對帳失敗：\n  " + problems.join("\n  "));
  process.exit(1);
}

// ── 產出 ────────────────────────────────────────────────────────
const slug = process.argv[2];
const out = process.argv[3];
const site = siteBySlug.get(slug);
if (!site) {
  console.error("unknown slug", slug);
  process.exit(1);
}
if (site.axis !== "topic") {
  console.error(`${slug} 是人物站，封面請用傳主肖像照，不由生成器產出`);
  process.exit(1);
}
const c = siteCovers[slug];

const title = site.label;
const en = site.brand.replace(/\s*Notes$/, "");

// 中文大字按字數縮級，字多就降一階——溢出比小一級難看得多。
const n = [...title].length;
const titleSize = n <= 4 ? 156 : n <= 5 ? 136 : n <= 6 ? 116 : n <= 7 ? 100 : n <= 8 ? 88 : 78;

const html = `<!doctype html><html><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:900px;height:1200px;overflow:hidden}
body{font-family:'Noto Sans CJK TC',sans-serif;background:#0e1220;position:relative}
.wrap{width:900px;height:1200px;position:relative;padding:88px 76px}
.glow{position:absolute;top:-160px;right:-140px;width:620px;height:620px;
  background:radial-gradient(circle,${c.accent}3d 0%,transparent 62%)}
.grid{position:absolute;inset:0;opacity:.5;
  background-image:radial-gradient(#ffffff10 1.4px,transparent 1.4px);background-size:30px 30px}
.motif{position:absolute;left:50%;top:432px;transform:translate(-50%,-50%);
  width:420px;height:420px;opacity:.95;filter:drop-shadow(0 0 60px ${c.accent}55)}
.title-block{position:absolute;left:76px;right:76px;bottom:232px}
h1{color:#fff;font-size:${titleSize}px;font-weight:900;line-height:1.08;letter-spacing:.02em}
.en{color:#8b93a7;font-size:32px;font-weight:500;letter-spacing:.12em;margin-top:26px;text-transform:uppercase}
.foot{position:absolute;left:76px;bottom:104px;display:flex;align-items:center;gap:18px;
  color:#5a6274;font-size:26px;font-weight:600;letter-spacing:.05em}
.foot .dot{font-size:11px;color:${c.accent}}
.baseline{position:absolute;left:0;bottom:0;width:100%;height:12px;
  background:linear-gradient(90deg,${c.accent} 0%,${c.accent2} 100%)}
</style></head><body><div class="wrap">
  <div class="glow"></div><div class="grid"></div>
  <div class="motif">${MOTIFS[c.motif](c.accent)}</div>
  <div class="title-block">
    <h1>${title}</h1>
    <div class="en">${en}</div>
  </div>
  <div class="foot"><span>NOTES</span><span class="dot">●</span><span>nplus.wiki</span></div>
  <div class="baseline"></div>
</div></body></html>`;

writeFileSync(out, html);
console.log("ok", slug, `"${title}" / "${en}"`, "titleSize", titleSize);
