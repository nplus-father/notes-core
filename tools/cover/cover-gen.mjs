// 主題站封面產生器 —— 印刷風（Style B）、3:4 直式書封、900x1200。
//
// v2（2026-08）：捨棄深色編輯風（Style A：#0e1220 底、glow、點陣格、漸層 baseline、
// 黑體 900 大字）——那套正是 site-cover 扉頁改版時點名要擺脫的「AI 生成感」語彙。
// 改與站內首頁同一套印刷語彙：紙色底＋髮絲外框＋襯線大字＋N° 編號，62 站讀起來
// 是一套書系；站台身分色只留給符號與短橫線（同色系不同 accent，正是書系的做法）。
// portal 的占位卡（StationCard 無圖 fallback）早就先走了這個樣子，這一版是把正式
// 封面補齊成同一套。
//
// 資料一律取自 registry，這裡不再自己存一份：
//   sites.ts        中文大字 = label；英文副題 = brand 去掉結尾的 " Notes"；
//                   N° = 主題站群內的順位（append 新站不動既有編號，同 site-cover 舊制）
//   site-covers.ts  主色、副色、符號——印刷風只用 accent2（副色，較深一階；亮色在
//                   紙上對比不足），accent 僅供對帳，不再上場
//
// 舊版（notes/note-cover/cover-gen.mjs）自己存了 title 與 en，結果 35 站有 9 站的
// 中文名跟 registry 對不上——封面上印「領導力」、portal 卡片上寫「領導」。同一個
// 事實存兩份必然漂移，所以那兩個欄位只能從 sites.ts 推導。
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
// 主題站群內順位——與退役的 site-cover.svg 同一套編法，新站 append 不動既有編號。
const serial = String(topicSlugs.indexOf(slug) + 1).padStart(2, "0");

// 中文大字按字數縮級，字多就降一階——溢出比小一級難看得多。
// 襯線體同字級略寬於黑體，整體比 Style A 低一階。
const n = [...title].length;
const titleSize = n <= 4 ? 148 : n <= 5 ? 128 : n <= 6 ? 108 : n <= 7 ? 94 : n <= 8 ? 82 : 72;

// 紙色與墨階——與 site-cover 扉頁同一組值（PAPER/RULE/TEXT/TEXT_SOFT/TEXT_FAINT）。
const PAPER = "#faf9f7";
const RULE = "#dcd8d2";
const TEXT = "#31302e";
const TEXT_SOFT = "#6b665f";
const TEXT_FAINT = "#a39e98";

// generic serif 在 Linux 解析中文會落到 Noto Sans CJK，襯線意圖靜默失效——
// 必須明確列 'Noto Serif CJK TC'（見 site-cover.svg.ts 同一個教訓）。
const SERIF = "'Noto Serif TC','Noto Serif CJK TC','Source Han Serif TC',Georgia,serif";
const SANS = "'Noto Sans TC','Noto Sans CJK TC',sans-serif";

const html = `<!doctype html><html><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:900px;height:1200px;overflow:hidden}
body{background:${PAPER};position:relative}
.frame{position:absolute;inset:26px;border:1px solid ${RULE}}
.kicker{position:absolute;left:76px;top:88px;font-family:${SANS};font-size:22px;font-weight:600;
  letter-spacing:9px;color:${TEXT_FAINT}}
.serial{position:absolute;right:76px;top:84px;font-family:${SERIF};font-size:30px;color:${TEXT_FAINT}}
.motif{position:absolute;left:50%;top:420px;transform:translate(-50%,-50%);width:340px;height:340px}
.title-block{position:absolute;left:76px;right:76px;bottom:212px}
h1{font-family:${SERIF};color:${TEXT};font-size:${titleSize}px;font-weight:700;line-height:1.12;
  letter-spacing:.04em}
.rule{width:96px;height:3px;background:${c.accent2};margin-top:36px}
.en{font-family:${SANS};color:${TEXT_SOFT};font-size:29px;font-weight:500;letter-spacing:.16em;
  margin-top:34px;text-transform:uppercase}
.foot{position:absolute;left:76px;right:76px;bottom:92px;display:flex;justify-content:space-between;
  font-family:${SANS};font-size:21px;font-weight:500;color:${TEXT_FAINT}}
.foot .l{letter-spacing:.3em}.foot .r{letter-spacing:.14em}
</style></head><body>
  <div class="frame"></div>
  <div class="kicker">主題</div>
  <div class="serial">N°${serial}</div>
  <div class="motif">${MOTIFS[c.motif](c.accent2)}</div>
  <div class="title-block">
    <h1>${title}</h1>
    <div class="rule"></div>
    <div class="en">${en}</div>
  </div>
  <div class="foot"><span class="l">NOTES</span><span class="r">nplus.wiki</span></div>
</body></html>`;

writeFileSync(out, html);
console.log("ok", slug, `"${title}" / "${en}"`, "N°" + serial, "titleSize", titleSize);
