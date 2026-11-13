export interface SplitTitle {
  main: string;
  latin: string | null;
}

const TRAILING_LATIN = /^(.*?\S)\s*[(（]\s*([^()（）]+?)\s*[)）]\s*$/;
const CJK = /[\p{Script=Han}　-〿＀-￯]/u;

export function splitTitle(title: string): SplitTitle {
  const m = title.match(TRAILING_LATIN);
  if (!m || !/[A-Za-z]/.test(m[2]) || CJK.test(m[2]) || !CJK.test(m[1])) {
    return { main: title, latin: null };
  }
  return { main: m[1], latin: m[2] };
}
