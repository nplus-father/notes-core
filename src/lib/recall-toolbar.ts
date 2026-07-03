// 複習工具列的 client 端接線：讀 `.recall-toolbar` 的 data-*（ns / key / seed-last），
// 綁定「今天複習過 / 撤銷」按鈕與「上次複習」顯示。ConceptLayout / ProblemLayout 共用。
//
// 純瀏覽器端模組（由 RecallToolbar.astro 的 <script> 匯入打包），不可用 Node API。
import { createReviews } from "./reviews";

export function initRecallToolbar(): void {
  const toolbar = document.querySelector<HTMLElement>(".recall-toolbar");
  const btn = document.getElementById("review-btn");
  const undo = document.getElementById("review-undo");
  const meta = document.getElementById("review-meta");
  if (!(toolbar && btn && undo && meta)) return;

  const { lastReviewed, reviewCount, isReviewedToday, markReviewedToday, undoToday } =
    createReviews(toolbar.dataset.ns!);
  const key = toolbar.dataset.key!;
  const seedLast = toolbar.dataset.seedLast || "";
  const render = () => {
    const last = lastReviewed(key) ?? (seedLast || null);
    const count = reviewCount(key);
    const doneToday = isReviewedToday(key);
    btn.hidden = false;
    btn.classList.toggle("is-done", doneToday);
    undo.hidden = !doneToday;
    if (count > 0) meta.textContent = `Last reviewed: ${last} (${count}×)`;
    else if (seedLast) meta.textContent = `Last reviewed: ${seedLast} (from notes)`;
    else meta.textContent = "Not reviewed yet";
  };
  btn.addEventListener("click", () => {
    markReviewedToday(key);
    render();
  });
  undo.addEventListener("click", () => {
    undoToday(key);
    render();
  });
  render();
}
