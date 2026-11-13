import puppeteer from "puppeteer-core";
import { createRequire } from "node:module";
import { writeFileSync } from "node:fs";

const require = createRequire(import.meta.url);
const AXE_PATH = require.resolve("axe-core/axe.min.js");

const args = process.argv.slice(2);
let base = "http://localhost:8820";
let jsonOut = null;
const stations = [];
for (let i = 0; i < args.length; i++) {
  if (args[i] === "--base") base = args[++i];
  else if (args[i] === "--json") jsonOut = args[++i];
  else stations.push(args[i]);
}
base = base.replace(/\/+$/, "");
if (!stations.length) {
  console.error("usage: node audit.mjs [--base http://localhost:8820] [--json out.json] <station> [<station>...]");
  process.exit(2);
}

const WIDTHS = [320, 390, 768, 1440];
const THEMES = ["light", "dark"];
const FAMILIES = ["Newsreader", "Noto Serif TC", "Inter", "JetBrains Mono"];
const CHECKS = ["overflow", "console", "emoji", "cls", "axe", "tap", "head", "fonts"];
const MAX_DETAIL_LINES = 110;

const status = async (url) => {
  try {
    const r = await fetch(url, { redirect: "follow" });
    return { status: r.status, text: r.status === 200 ? await r.text() : "" };
  } catch {
    return { status: 0, text: "" };
  }
};

const hrefs = (html, prefix) => {
  const out = [];
  for (const m of html.matchAll(/href="([^"#?]+)"/g)) {
    const h = m[1];
    if (h.startsWith(prefix) && !out.includes(h)) out.push(h);
  }
  return out;
};

async function discover(station) {
  const root = `/${station}/`;
  const pages = [{ name: "home", path: root }];
  const concepts = await status(`${base}${root}concepts/`);
  if (concepts.status === 200) {
    pages.push({ name: "concepts", path: `${root}concepts/` });
    const links = hrefs(concepts.text, `${root}concepts/`).filter((h) => h !== `${root}concepts/`);
    const depth = (h) => h.slice(`${root}concepts/`.length).split("/").filter(Boolean).length;
    const cat = links.find((h) => depth(h) === 1);
    const cons = links.filter((h) => depth(h) === 2).slice(0, 2);
    if (cat) pages.push({ name: "category", path: cat });
    cons.forEach((h, i) => pages.push({ name: `concept${i + 1}`, path: h }));
  }
  for (const seg of ["guide", "check", "library", "search", "problems"]) {
    const r = await status(`${base}${root}${seg}/`);
    if (r.status !== 200) continue;
    pages.push({ name: seg, path: `${root}${seg}/` });
    if (seg === "problems") {
      const sub = hrefs(r.text, `${root}problems/`).find((h) => h !== `${root}problems/`);
      if (sub) pages.push({ name: "problem", path: sub });
    }
  }
  pages.push({ name: "404", path: `${root}404.html`, allowNon200: true });
  return pages;
}

const overflowProbe = () => {
  const vw = window.innerWidth;
  const doc = document.documentElement;
  const failed = doc.scrollWidth > vw + 1;
  if (!failed) return { failed, scrollWidth: doc.scrollWidth, offenders: [] };
  const cssPath = (el) => {
    const parts = [];
    let n = el;
    while (n && n.nodeType === 1 && n !== document.body && parts.length < 4) {
      let s = n.tagName.toLowerCase();
      if (n.id) s += "#" + n.id;
      else if (typeof n.className === "string" && n.className.trim()) s += "." + n.className.trim().split(/\s+/).slice(0, 2).join(".");
      parts.unshift(s);
      n = n.parentElement;
    }
    return parts.join(" > ");
  };
  const scrollableAncestor = (el) => {
    for (let p = el.parentElement; p && p !== document.body && p !== doc; p = p.parentElement) {
      const ox = getComputedStyle(p).overflowX;
      if (ox === "auto" || ox === "scroll") return true;
    }
    return false;
  };
  const depthOf = (el) => {
    let d = 0;
    for (let p = el; p; p = p.parentElement) d++;
    return d;
  };
  const found = [];
  for (const el of document.querySelectorAll("body *")) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    if (r.right <= vw + 1) continue;
    if (getComputedStyle(el).position === "fixed") continue;
    if (scrollableAncestor(el)) continue;
    found.push({ el, d: depthOf(el), right: Math.round(r.right) });
  }
  found.sort((a, b) => b.d - a.d);
  return {
    failed,
    scrollWidth: doc.scrollWidth,
    offenders: found.slice(0, 5).map((f) => `${cssPath(f.el)} (right=${f.right})`),
  };
};

const emojiProbe = () => {
  const re = /\p{Extended_Pictographic}/gu;
  const out = [];
  for (const sel of ["nav.topnav", "footer", ".crumbs", "h1"]) {
    for (const el of document.querySelectorAll(sel)) {
      const text = el.textContent || "";
      const hits = [];
      for (const m of text.matchAll(re)) {
        const ch = m[0];
        const cp = ch.codePointAt(0);
        const next = text.codePointAt(m.index + ch.length);
        const vs16 = next === 0xfe0f;
        if (!vs16 && (cp === 0xa9 || cp === 0xae || cp === 0x2122 || (cp >= 0x2190 && cp <= 0x21ff))) continue;
        hits.push({ i: m.index, ch, cp });
      }
      if (hits.length) {
        const i = hits[0].i;
        const ctx = text.slice(Math.max(0, i - 8), i + 8).replace(/\s+/g, " ").trim();
        out.push(`${sel}: ${hits.map((h) => h.ch + " U+" + h.cp.toString(16).toUpperCase()).join(" ")} near "${ctx}"`);
      }
    }
  }
  return out;
};

const tapProbe = () => {
  const out = [];
  for (const el of document.querySelectorAll("nav.topnav :is(a, button, input, summary, [role=tab])")) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    const cs = getComputedStyle(el);
    if (cs.visibility === "hidden" || cs.display === "none") continue;
    if (r.width < 36 || r.height < 36) {
      const label = (el.getAttribute("aria-label") || el.textContent || el.getAttribute("href") || "").trim().replace(/\s+/g, " ").slice(0, 24);
      out.push(`${el.tagName.toLowerCase()} "${label}" ${Math.round(r.width)}x${Math.round(r.height)}`);
    }
  }
  return out;
};

const headProbe = () => {
  const out = [];
  const h1 = document.querySelectorAll("h1").length;
  if (h1 !== 1) out.push(`h1 count ${h1}`);
  if (!document.title.trim()) out.push("empty title");
  if (!document.querySelector('meta[name="description"]')?.content?.trim()) out.push("missing meta description");
  if (!document.querySelector('meta[property="og:image"]')?.content?.trim()) out.push("missing og:image");
  if (!document.documentElement.getAttribute("lang")) out.push("missing html[lang]");
  return out;
};

const fontProbe = async (families) => {
  await document.fonts.ready;
  const loaded = new Set();
  document.fonts.forEach((f) => {
    if (f.status === "loaded") loaded.add(f.family.replace(/^["']|["']$/g, ""));
  });
  return families.filter((f) => !loaded.has(f));
};

async function auditPage(page, station, pg, collect) {
  const url = `${base}${pg.path}`;
  const rec = { page: pg.name, path: pg.path, status: null, runs: [] };
  for (const theme of THEMES) {
    for (const w of WIDTHS) {
      const mobile = w <= 390;
      await page.setViewport({ width: w, height: 900, deviceScaleFactor: 1, isMobile: mobile, hasTouch: mobile });
      await page.emulateMediaFeatures([{ name: "prefers-color-scheme", value: theme }]);
      const consoleErrors = [];
      const onConsole = (m) => {
        if (m.type() !== "error") return;
        const loc = m.location()?.url || "";
        if (loc.includes("/pagefind/")) return;
        if (pg.allowNon200 && loc === url) return;
        consoleErrors.push(m.text().slice(0, 200) + (loc ? ` [${loc.replace(base, "")}]` : ""));
      };
      const onPageError = (e) => consoleErrors.push("pageerror: " + String(e.message || e).slice(0, 200));
      page.on("console", onConsole);
      page.on("pageerror", onPageError);
      const t0 = Date.now();
      let resp;
      try {
        resp = await page.goto(url, { waitUntil: "load", timeout: 30000 });
      } catch (e) {
        page.off("console", onConsole);
        page.off("pageerror", onPageError);
        rec.runs.push({ theme, width: w, error: "navigation: " + e.message });
        continue;
      }
      rec.status = resp.status();
      const run = { theme, width: w };
      if (rec.status !== 200 && !pg.allowNon200) run.httpStatus = rec.status;
      run.overflow = await page.evaluate(overflowProbe);
      run.emoji = await page.evaluate(emojiProbe);
      if (w <= 390) run.tap = await page.evaluate(tapProbe);
      if (w === 1440 && theme === "light") {
        run.head = await page.evaluate(headProbe);
        run.missingFonts = await page.evaluate(fontProbe, FAMILIES);
      }
      if (w === 1440 || w === 390) {
        try {
          await page.addScriptTag({ path: AXE_PATH });
          const res = await page.evaluate(async () => {
            const r = await window.axe.run(document, { resultTypes: ["violations"] });
            return r.violations
              .filter((v) => v.impact === "serious" || v.impact === "critical")
              .map((v) => ({ id: v.id, impact: v.impact, help: v.help, nodes: v.nodes.length, targets: v.nodes.slice(0, 3).map((n) => n.target.join(" ")) }));
          });
          run.axe = res;
        } catch (e) {
          run.axe = [{ id: "axe-error", impact: "critical", help: String(e.message).slice(0, 120), nodes: 0, targets: [] }];
        }
      }
      const wait = 1500 - (Date.now() - t0);
      if (wait > 0) await new Promise((r) => setTimeout(r, wait));
      run.cls = await page.evaluate(() => Math.round((window.__cls || 0) * 10000) / 10000);
      run.console = consoleErrors.slice();
      page.off("console", onConsole);
      page.off("pageerror", onPageError);
      rec.runs.push(run);
    }
  }
  return rec;
}

function evaluate(rec) {
  const fails = [];
  const warns = [];
  const tag = (r) => `${r.width}${r.theme === "dark" ? "D" : "L"}`;
  for (const r of rec.runs) {
    if (r.error) {
      fails.push({ check: "console", msg: r.error, at: tag(r) });
      continue;
    }
    if (r.httpStatus) fails.push({ check: "console", msg: `HTTP ${r.httpStatus}`, at: tag(r) });
    if (r.overflow?.failed) fails.push({ check: "overflow", msg: `scrollWidth ${r.overflow.scrollWidth} > ${r.width}: ${r.overflow.offenders.join(" | ") || "no offending element found"}`, at: tag(r) });
    for (const c of r.console || []) fails.push({ check: "console", msg: c, at: tag(r) });
    for (const e of r.emoji || []) fails.push({ check: "emoji", msg: e, at: tag(r) });
    if (r.cls >= 0.05) fails.push({ check: "cls", msg: `CLS ${r.cls}`, at: tag(r) });
    for (const v of r.axe || []) fails.push({ check: "axe", msg: `${v.id} [${v.impact}] ${v.help} (${v.nodes} nodes) ${v.targets.join(" ; ")}`, at: tag(r) });
    for (const t of r.tap || []) warns.push({ check: "tap", msg: t, at: tag(r) });
    for (const h of r.head || []) fails.push({ check: "head", msg: h, at: tag(r) });
    for (const f of r.missingFonts || []) warns.push({ check: "fonts", msg: `font not loaded: ${f}`, at: tag(r) });
  }
  return { fails, warns };
}

function group(items) {
  const m = new Map();
  for (const it of items) {
    const k = `${it.check}\u0000${it.msg}`;
    if (!m.has(k)) m.set(k, { check: it.check, msg: it.msg, at: [] });
    m.get(k).at.push(it.at);
  }
  return [...m.values()];
}

const pad = (s, n) => String(s).padEnd(n);

function report(station, recs) {
  const lines = [];
  lines.push(`=== ${station} ===`);
  const header = pad("page", 10) + CHECKS.map((c) => pad(c, 9)).join("");
  lines.push(header);
  for (const rec of recs) {
    const { fails, warns } = rec.eval;
    const cell = (c) => {
      const f = fails.filter((x) => x.check === c).length;
      const w = warns.filter((x) => x.check === c).length;
      if (f) return String(f);
      if (w) return `w${w}`;
      return ".";
    };
    lines.push(pad(rec.page + (rec.status && rec.status !== 200 ? `(${rec.status})` : ""), 10) + CHECKS.map((c) => pad(cell(c), 9)).join(""));
  }
  lines.push("(number = failing runs, wN = warnings, . = ok; L/D = light/dark)");
  const detail = [];
  const merged = (kind, label) => {
    const m = new Map();
    for (const rec of recs) {
      for (const g of group(rec.eval[kind])) {
        const k = `${g.check}\u0000${g.msg}`;
        if (!m.has(k)) m.set(k, { check: g.check, msg: g.msg, pages: [], at: new Set() });
        m.get(k).pages.push(rec.page);
        g.at.forEach((a) => m.get(k).at.add(a));
      }
    }
    for (const g of m.values()) {
      const pg = g.pages.length > 4 ? `${g.pages.slice(0, 4).join(",")}+${g.pages.length - 4}` : g.pages.join(",");
      detail.push(`${label} [${g.check}] ${g.msg} | ${pg} @ ${[...g.at].join(",")}`);
    }
  };
  merged("fails", "FAIL");
  merged("warns", "warn");
  const shown = detail.slice(0, MAX_DETAIL_LINES);
  if (shown.length) lines.push("", "details:");
  for (const d of shown) lines.push(d.length > 300 ? d.slice(0, 297) + "..." : d);
  if (detail.length > shown.length) lines.push(`... ${detail.length - shown.length} more detail lines (use --json)`);
  return lines.join("\n");
}

const browser = await puppeteer.launch({ executablePath: "/usr/bin/google-chrome", headless: true, args: ["--no-sandbox", "--hide-scrollbars"] });
const all = {};
let failed = false;
try {
  const page = await browser.newPage();
  await page.setCacheEnabled(false);
  await page.evaluateOnNewDocument(() => {
    try {
      localStorage.clear();
    } catch {}
    window.__cls = 0;
    try {
      new PerformanceObserver((list) => {
        for (const e of list.getEntries()) if (!e.hadRecentInput) window.__cls += e.value;
      }).observe({ type: "layout-shift", buffered: true });
    } catch {}
  });
  for (const station of stations) {
    const started = Date.now();
    const home = await status(`${base}/${station}/`);
    if (home.status !== 200) {
      console.log(`=== ${station} ===\nFAIL station not served at ${base}/${station}/ (HTTP ${home.status})`);
      failed = true;
      all[station] = { error: `HTTP ${home.status}` };
      continue;
    }
    const pages = await discover(station);
    const recs = [];
    for (const pg of pages) {
      const rec = await auditPage(page, station, pg);
      rec.eval = evaluate(rec);
      if (rec.eval.fails.length) failed = true;
      recs.push(rec);
    }
    all[station] = { seconds: Math.round((Date.now() - started) / 1000), pages: recs };
    console.log(report(station, recs));
    console.log(`(${all[station].seconds}s, ${pages.length} pages)`);
  }
} finally {
  await browser.close();
}
if (jsonOut) writeFileSync(jsonOut, JSON.stringify(all, null, 2));
console.log(failed ? "FAIL" : "PASS");
process.exit(failed ? 1 : 0);
