import puppeteer from "puppeteer-core";
import { readFileSync } from "node:fs";
const jobs = JSON.parse(readFileSync(process.argv[2], "utf8"));
const browser = await puppeteer.launch({ executablePath: "/usr/bin/google-chrome", headless: true, args: ["--no-sandbox", "--hide-scrollbars"] });
for (const j of jobs) {
  const page = await browser.newPage();
  const w = j.w ?? 1440, h = j.h ?? 900;
  await page.setViewport({ width: w, height: h, deviceScaleFactor: j.dpr ?? 1, isMobile: !!j.mobile, hasTouch: !!j.mobile });
  await page.emulateMediaFeatures([{ name: "prefers-color-scheme", value: j.dark ? "dark" : "light" }, ...(j.reduced ? [{ name: "prefers-reduced-motion", value: "reduce" }] : [])]);
  const errs = [];
  page.on("pageerror", (e) => errs.push(String(e)));
  page.on("console", (m) => m.type() === "error" && errs.push(m.text()));
  await page.goto(j.url, { waitUntil: "networkidle0", timeout: 30000 });
  if (j.eval) await page.evaluate(j.eval);
  if (j.scroll != null) await page.evaluate((y) => window.scrollTo(0, y), j.scroll);
  await new Promise((r) => setTimeout(r, j.wait ?? 400));
  const total = await page.evaluate(() => document.documentElement.scrollHeight);
  if (j.slices) {
    const n = Math.min(j.slices, Math.ceil(total / h));
    for (let i = 0; i < n; i++) {
      await page.evaluate((y) => window.scrollTo(0, y), i * h);
      await new Promise((r) => setTimeout(r, 250));
      await page.screenshot({ path: `${j.out}-${i}.png` });
    }
  } else {
    await page.screenshot({ path: `${j.out}.png`, fullPage: !!j.full });
  }
  console.log(j.out, "height", total, errs.length ? "ERRORS " + errs.join(" | ") : "");
  await page.close();
}
await browser.close();
