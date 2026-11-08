"""從書稿產生 book/llms.txt（llmstxt.org 格式）。

只讀 book/_quarto.yml 的 site-url 與各章 .qmd 的標題和 description，
不需要額外套件。輸出的網址對應 Quarto 的 HTML 輸出路徑。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "book"

TITLE = "化學資訊學入門：用 Python 與 RDKit 動手學"
SUMMARY = (
    "繁體中文的化學資訊學入門書，寫給化學、材料背景、對程式還不熟悉的讀者。"
    "用 Python 與 RDKit 處理真實的分子資料，涵蓋分子表示、化學資料庫、描述符、"
    "量子化學計算、分子指紋、化學空間、QSAR 建模與評估、模型解釋、小數據與實驗設計、"
    "研究資料管理，以及兩個實戰專題。每一節附可在 Google Colab 執行的 notebook。"
)


def site_url() -> str:
    text = (BOOK / "_quarto.yml").read_text(encoding="utf-8")
    m = re.search(r"^\s*site-url:\s*(\S+)", text, re.M)
    if not m:
        sys.exit("book/_quarto.yml 找不到 site-url")
    return m.group(1).rstrip("/") + "/"


def read(path: Path):
    text = path.read_text(encoding="utf-8")
    desc = ""
    fm = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if fm:
        m = re.search(r'^description:\s*"(.*)"\s*$', fm.group(1), re.M)
        if m:
            desc = m.group(1).replace('\\"', '"')
    h1 = re.search(r"^# (.+?)(?:\s*\{#.*\})?\s*$", text, re.M)
    title = h1.group(1).strip() if h1 else path.stem
    return title, desc


def link(base: str, rel: Path, title: str, desc: str) -> str:
    url = base + rel.with_suffix(".html").as_posix()
    line = f"- [{title}]({url})"
    return f"{line}: {desc}" if desc else line


def main() -> None:
    base = site_url()
    out = [f"# {TITLE}", "", f"> {SUMMARY}", ""]
    out += [
        "書稿與程式碼採 CC BY 4.0；隨附資料維持各自授權。"
        f"原始碼與 notebook：https://github.com/517justin/cheminfo-intro",
        "",
    ]
    for chapter in sorted((BOOK / "chapters").glob("ch*")):
        index = chapter / "index.qmd"
        if not index.exists():
            continue
        ctitle, cdesc = read(index)
        out += [f"## {ctitle}", ""]
        if cdesc:
            out += [cdesc, ""]
        for qmd in sorted(chapter.glob("*.qmd")):
            if qmd.name == "index.qmd":
                continue
            title, desc = read(qmd)
            m = re.match(r"(\d+)-(\d+)-", qmd.name)
            if m:
                title = f"{int(m.group(1))}.{int(m.group(2))} {title}"
            out.append(link(base, qmd.relative_to(BOOK), title, desc))
        out.append("")
    glossary = BOOK / "glossary.qmd"
    if glossary.exists():
        title, desc = read(glossary)
        out += ["## 附錄", "", link(base, glossary.relative_to(BOOK), title, desc), ""]
    (BOOK / "llms.txt").write_text("\n".join(out), encoding="utf-8")
    print(f"寫入 {BOOK / 'llms.txt'}，{len(out)} 行")


if __name__ == "__main__":
    main()
