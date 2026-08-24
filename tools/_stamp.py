"""生成型文件的新鮮度戳記。

**為什麼需要**：docs/ 底下那幾份是生成物，而生成物一旦停更就會開始騙人——它看起來
跟剛跑完一模一樣。2026-08-24 就發生過：拿 8/21 算的 ORPHAN-BOOKS.md 當證據判斷
「刪掉某份清單不會失去資訊」，結論剛好對，但當時**沒有任何辦法從檔案本身看出它多舊**，
要去翻 git log 才知道。讀的人（包括 AI）不會去翻。

所以每份生成物在 H1 底下掛一行戳記，寫明「什麼時候算的、誰算的、不要手改」。

**戳記會讓每次重算都產生 diff**，這會打壞 refresh-galaxy-docs.sh 的「無落差」檢查——
那支腳本因此用 `git diff -I'^> \\*\\*生成於'` 忽略這一行，只比真正的內容。改戳記格式時
要一起改那個正規表達式，否則落差檢查會從此永遠報「有變動」。
"""

STAMP_RE = r"^> \*\*生成於"


def stamp(text: str, generator: str, when: str) -> str:
    """在 markdown 的 H1 底下插入（或更新）戳記行。

    `when` 由呼叫端給，不在這裡取現在時間——生成器各自已經有自己的時間來源，
    而且測試時要能餵固定值。
    """
    line = f"> **生成於 {when}**｜由 `{generator}` 產生，**不要手改**——改資料源再重跑。"
    lines = text.split("\n")
    # 找 H1；找不到就掛在最前面（總比沒有好）。
    i = next((n for n, s in enumerate(lines) if s.startswith("# ")), -1)
    if i < 0:
        return line + "\n\n" + text
    # 已經有戳記就換掉，不要愈疊愈多。
    j = i + 1
    while j < len(lines) and not lines[j].strip():
        j += 1
    if j < len(lines) and lines[j].startswith("> **生成於"):
        lines[j] = line
        return "\n".join(lines)
    return "\n".join(lines[: i + 1] + ["", line] + lines[i + 1 :])
