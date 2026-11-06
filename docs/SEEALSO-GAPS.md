# 跨站連結缺口（同書同章、卻沒有互相 seeAlso）

> **生成於 2026-11-06T10:36:39+08:00**｜由 `tools/export-seealso-gaps.py` 產生，**不要手改**——改資料源再重跑。

**這份是什麼**：兩個站的概念頁掛了**同一本書的同一章**，來源頁卻沒有任何 `seeAlso` 指到對方那一站。
由 `notes-core/tools/export-seealso-gaps.py` 生成，**不要手改**——補各站的 seeAlso 再重跑。

**為什麼要補**：契約層全綠之後，星系最薄的是站與站之間。同一章同時撐著主題站的一頁與人物站的一頁，
讀者在任一邊都看不到另一邊——79 個站各自封閉，首頁 schools 卡的跨站門是唯一通道。
頁級的「Dive Deeper」就是為這件事存在的，它的使用率卻只有一成。

**判準只收 strong**：同書**同章**。同書不同章只列數字（weak），不開單——不同章可能講完全不同的事。

目前：2247 個概念頁，有 seeAlso 的 **621 頁（28%）**；一條跨站連結都沒有的站 **7**。
strong 缺口 **0 筆**（來源頁 0，分佈在 0 站）；全部補上後有 seeAlso 的頁變成 **621（28%）**。weak（同書不同章）另有 423 筆，只供參考。
另有 **0 筆被 schema 擋住**（strict 站指向非技術站，見下節）。

> [!NOTE]
> 目前零跨站連結的站：`gardner`、`image-style`、`kiyosaki`、`pastoral-psychology`、`personal-finance`、`security`、`wujun`

## 各站缺口（當來源）

缺越多排越前；缺 0 的站略去。軸別來自 sites.ts。

| 站 | 軸 | 缺口 | 主要去向 |
| --- | --- | ---: | --- |

軸向：主題→人物 0、人物→主題 0、主題→主題 0、人物→人物 0。

## 逐筆清單

格式：來源頁 → 目標站：要掛的 path（label）。分類頁＝該分類 ≥3 頁同時命中，連分類不連單頁。

## 被 schema 擋住的缺口（strict 站 → 非技術站）

技術站群的 `seeAlso.site` 走 `siteKeys` enum，目前只含技術站自己的 key。這些缺口**真實存在**
（同書同章），但寫進 frontmatter build 會紅。要放行得改 notes-core：讓 enum 涵蓋全部 79 個 key
（仍是封閉集合，拼錯照樣抓得到），升版後重跑本工具它們就會進決策 JSON。

無。

## 套用

```bash
notes-core/tools/export-seealso-gaps.py --json > /tmp/seealso.json
notes-core/tools/apply-seealso.py /tmp/seealso.json            # 乾跑
notes-core/tools/apply-seealso.py /tmp/seealso.json --apply    # 寫入各站 frontmatter
```

寫入後各站 `npm run format`，抽幾站 build（strict 站的 `seeAlso.site` 走 siteKeys enum，拼錯 build 會紅），
`galaxy-checkup.py` 的 dead-seealso 必須維持 0。補完重跑本工具，該站就會從這裡消失。
