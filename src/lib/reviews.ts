// 主動學習閉環的核心：把「複習活動」存在瀏覽器 localStorage。
// 設計原則：頁面 frontmatter 的 status/lastReviewed 是「基線種子」，
// 這裡的紀錄是使用者真實複習活動的「即時覆蓋層」，有紀錄時以這裡為準。
//
// 純瀏覽器端模組（會被當 client script 打包），不可使用 import.meta.env / Node API。
//
// ⚠️ 六站共用 nplus.wiki 網域 → 共用 localStorage。各站的 KEY 必須獨立，
// 否則複習紀錄會互相覆蓋。故以 factory 形式建立，由各站傳入唯一 namespace：
//   const reviews = createReviews("lk");   // → localStorage key "lk-reviews"

export interface ReviewRecord {
  /** 複習日期清單，'YYYY-MM-DD'，唯一且遞增排序 */
  dates: string[];
}
export type ReviewLog = Record<string, ReviewRecord>;

/** 本地時區的 YYYY-MM-DD（不要用 toISOString，那是 UTC 會跨日） */
export function todayStr(): string {
  const d = new Date();
  const z = (n: number) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${z(d.getMonth() + 1)}-${z(d.getDate())}`;
}

export interface Reviews {
  loadLog(): ReviewLog;
  saveLog(log: ReviewLog): void;
  lastReviewed(key: number | string, log?: ReviewLog): string | null;
  reviewCount(key: number | string, log?: ReviewLog): number;
  isReviewedToday(key: number | string, log?: ReviewLog): boolean;
  markReviewedToday(key: number | string): ReviewRecord;
  undoToday(key: number | string): void;
  todayStr(): string;
}

/**
 * 建立綁定到某 namespace 的複習紀錄工具。
 * @param namespace 各站唯一前綴（如 'lk' / 'cc' / 'dp'）；實際 localStorage key 為 `${namespace}-reviews`。
 */
export function createReviews(namespace: string): Reviews {
  const KEY = `${namespace}-reviews`;

  function loadLog(): ReviewLog {
    try {
      const raw = JSON.parse(localStorage.getItem(KEY) || "{}");
      const out: ReviewLog = {};
      for (const k of Object.keys(raw)) {
        const v = raw[k];
        if (v && Array.isArray(v.dates))
          out[k] = { dates: v.dates.filter((d: unknown) => typeof d === "string") };
      }
      return out;
    } catch {
      return {};
    }
  }

  function saveLog(log: ReviewLog): void {
    try {
      localStorage.setItem(KEY, JSON.stringify(log));
    } catch {
      /* 私密瀏覽/額度滿時靜默失敗 */
    }
  }

  function lastReviewed(key: number | string, log: ReviewLog = loadLog()): string | null {
    const r = log[String(key)];
    return r && r.dates.length ? r.dates[r.dates.length - 1] : null;
  }

  function reviewCount(key: number | string, log: ReviewLog = loadLog()): number {
    const r = log[String(key)];
    return r ? r.dates.length : 0;
  }

  function isReviewedToday(key: number | string, log: ReviewLog = loadLog()): boolean {
    return lastReviewed(key, log) === todayStr();
  }

  /** 記錄今天複習過此頁（同一天重複呼叫不會重複累計）。回傳更新後的紀錄。 */
  function markReviewedToday(key: number | string): ReviewRecord {
    const log = loadLog();
    const k = String(key);
    const t = todayStr();
    const r = log[k] ?? { dates: [] };
    if (!r.dates.includes(t)) {
      r.dates.push(t);
      r.dates.sort();
    }
    log[k] = r;
    saveLog(log);
    return r;
  }

  /** 取消今天的複習紀錄（撤銷誤觸）。 */
  function undoToday(key: number | string): void {
    const log = loadLog();
    const k = String(key);
    const t = todayStr();
    const r = log[k];
    if (!r) return;
    r.dates = r.dates.filter((d) => d !== t);
    if (r.dates.length === 0) delete log[k];
    else log[k] = r;
    saveLog(log);
  }

  return {
    loadLog,
    saveLog,
    lastReviewed,
    reviewCount,
    isReviewedToday,
    markReviewedToday,
    undoToday,
    todayStr,
  };
}
