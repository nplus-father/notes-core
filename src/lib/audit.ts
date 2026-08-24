// 判層履約稽核（v0.42.0）：四層各是一個承諾，這裡檢查有沒有兌現。
//
//   spine      該有專屬概念頁        違約 → 真欠債
//   support    guide 要一句帶到      違約 → 空頭支票
//   tool       列進盤點表即可        恆真（體裁對不對只能人工看）
//   delegated  深挖歸姊妹站          違約 → 漏接
//
// **真欠債是「知道要做還沒做」，空頭支票與漏接是「以為做過了其實沒有」。**
// 後兩者才會靜靜把缺口藏起來：判錯一本脊梁只是多寫一頁，判錯一本豁免，
// 那個洞就再也不會有人看見。所以稽核的重點在豁免那一邊。
//
// **為什麼算在站台這裡，而不是在 nplus.wiki portal？** 因為空頭支票要比對導覽
// 「散文」有沒有提到那本書，而散文只有站台自己有（index.json 不會、也不該把
// 五章長文全文吐出去）。其餘幾項本來就是站內資料。唯一算不了的是漏接——那要問
// 姊妹站有沒有接住，屬於跨站資訊，交給聚合端（portal / CLI）用各站的 citations 判。
//
// 結果透過 index.json 發佈，portal 與 CLI 消費同一份，**不各寫一份實作**。
// 稽核結論本身是衍生物，衍生物只該被算一次。

export type Tier = "spine" | "support" | "tool" | "delegated";

export type AuditEntry = {
  slug: string | null;
  title: string;
  original?: string;
  status: string;
  tier?: Tier | null;
  delegatedTo?: string | null;
};

/** 每本書被概念頁／題目頁引用的次數，以及**散在幾個不同的頁**。 */
export type Citation = { n: number; pages: number };

export type Audit = {
  owned: number;
  /** 判過層、且不是 spine 的本數＝刻意不在本站深挖的。 */
  excused: number;
  /** 判 spine 卻一頁未引——唯一「知道要做還沒做」的一類。 */
  debt: string[];
  /** 判 support、導覽卻連提都沒提。 */
  empty: string[];
  /** 被 ≥3 個不同的頁引用卻判成非 spine：站上自己的頁面已經投過票了。 */
  conflict: string[];
  /** owned 但沒有 tier 欄——缺一本就是缺一個決定。 */
  untiered: string[];
  /** 判 delegated 的書，交給聚合端去問姊妹站接住了沒。 */
  delegated: { slug: string; to: string | null }[];
  /** 導覽落後：內容補過了，策展層還在講舊帳。null＝沒落後或無從判斷。 */
  guideLag: { guideWrittenAt: string; enrichedAt: string } | null;
};

/**
 * 書名在導覽散文裡可能長什麼樣。
 *
 * 盤點表的 title 常把中英名串在一起（「Head First Design Patterns 深入淺出設計模式」），
 * 導覽行文卻只用其中一半——拿整串去比對會漏掉，把談了整段的書誤判成空頭支票。
 * 所以要把雙語名拆成可獨立辨識的片段。長度下限是防誤命中：太短的片段
 * （「重構」「高手」「Design」）會在散文裡到處撞到，反而把真的空頭支票蓋掉。
 */
export function nameCandidates(e: AuditEntry): string[] {
  const out = new Set<string>();
  for (const t of [e.title, e.original]) {
    const s = (t ?? "").trim();
    if (!s) continue;
    out.add(s);
    out.add(s.split(/[:：（(]/)[0].trim());
    for (const m of s.match(/[A-Za-z][A-Za-z0-9 '’&.,:!?-]{9,}/g) ?? [])
      out.add(m.replace(/^[\s,.:-—]+|[\s,.:-—]+$/g, ""));
    for (const m of s.match(/[一-鿿]{4,}/g) ?? []) out.add(m);
  }
  return [...out].filter((c) => c.length >= 4);
}

/** 導覽有沒有碰過這本書：furtherReading 的 slug（強訊號）或散文提及（弱訊號）。 */
export function touchedByGuide(
  e: AuditEntry,
  guideBooks: Set<string>,
  prose: string,
): boolean {
  if (e.slug && guideBooks.has(e.slug)) return true;
  if (e.slug && prose.includes(`/${e.slug}/`)) return true;
  return nameCandidates(e).some((c) => prose.includes(c));
}

export function auditStation(input: {
  bibliography: AuditEntry[];
  citations: Record<string, Citation>;
  guideBooks: Set<string>;
  guideProse: string;
  guideWrittenAt: string;
  enrichedAt?: string | null;
}): Audit {
  const {
    bibliography,
    citations,
    guideBooks,
    guideProse,
    guideWrittenAt,
    enrichedAt,
  } = input;
  const owned = bibliography.filter((b) => b.status === "owned");

  const debt: string[] = [];
  const empty: string[] = [];
  const conflict: string[] = [];
  const untiered: string[] = [];
  const delegated: { slug: string; to: string | null }[] = [];
  let excused = 0;

  for (const b of owned) {
    const slug = b.slug ?? b.title;
    const cite = (b.slug && citations[b.slug]) || { n: 0, pages: 0 };
    if (!b.tier) {
      untiered.push(slug);
      continue;
    }
    if (b.tier !== "spine") excused += 1;

    if (b.tier === "spine") {
      if (cite.pages === 0) debt.push(slug);
    } else {
      // 載重看「散在幾頁」，不看次數——同一頁掛四個錨就是四次，那本書仍只撐一頁。
      // 用次數當門檻時（2026-08-24 實測）12 筆警報有 9 筆是這種假象。
      if (cite.pages >= 3) conflict.push(slug);
      if (b.tier === "support" && !touchedByGuide(b, guideBooks, guideProse))
        empty.push(slug);
      if (b.tier === "delegated")
        delegated.push({ slug, to: b.delegatedTo ?? null });
    }
  }

  // 還債會把導覽寫過時——第三章白紙黑字寫著「這本還沒挖」，而那本書昨天剛開了頁。
  // **同日打平抓不到**：導覽若當天因別的原因被動過，日期會一樣新，這裡就報 null，
  // 但正文可能還寫著那本書「未挖」。所以 null 只代表日期沒落後，不代表內容同步過。
  const guideLag =
    guideWrittenAt && enrichedAt && guideWrittenAt < enrichedAt
      ? { guideWrittenAt, enrichedAt }
      : null;

  return {
    owned: owned.length,
    excused,
    debt,
    empty,
    conflict,
    untiered,
    delegated,
    guideLag,
  };
}
