#!/usr/bin/env python3
"""Typeset the thesis PDF with xelatex from the assembled Markdown.

    python3 handoff_tools/build_pdf.py        -> VERA-SNARK_Thesis_SUBMISSION.pdf

The text is VERA-SNARK_Thesis_SUBMISSION.md, unchanged: this script only decides layout.
Pipeline: Markdown -> (layout preprocessing) -> pandoc -> LaTeX -> (labels, links, captions) -> xelatex x3.
Template, title page, fonts (Libertinus, IBM Plex Mono; SIL OFL) and code colours live in thesis_pdf/.
"""
import re, subprocess, sys, shutil, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "VERA-SNARK_Thesis_SUBMISSION.md"
DIR = ROOT / "thesis_pdf"
BUILD = DIR / "build"
OUT = ROOT / "VERA-SNARK_Thesis_SUBMISSION.pdf"
FRONT = {"Abstract", "Sammendrag", "Statement of Contribution", "Declaration of Originality",
         "Nomenclature and Abbreviations"}


# ------------------------------------------------------------------ Markdown, layout only
def col_widths(rows):
    """Relative column widths from content: no column narrower than its longest word, the rest by text mass."""
    n = max(len(r) for r in rows)
    maxw, mass = [3] * n, [1.0] * n
    for r in rows:
        for j, c in enumerate(r):
            t = re.sub(r"[*`$\\]", "", c).strip()
            if not t:
                continue
            maxw[j] = max(maxw[j], max(len(w) for w in re.split(r"[\s/]+", t)))
            mass[j] += min(len(t), 160)
    floor = [min(m + 2, 40) for m in maxw]
    total = 100.0
    rest = total - sum(floor) * 0.9
    if rest <= 0:
        w = [f / sum(floor) * total for f in floor]
    else:
        w = [f * 0.9 + rest * m / sum(mass) for f, m in zip(floor, mass)]
    return [max(4, int(round(x))) for x in w]


def split_row(line):
    s = line.strip()
    if s.startswith("|"): s = s[1:]
    if s.endswith("|"): s = s[:-1]
    cells, cur, code, math = [], "", False, False
    for i, ch in enumerate(s):
        if ch == "`": code = not code
        if ch == "$" and not code: math = not math
        if ch == "|" and not code and not math and (i == 0 or s[i - 1] != "\\"):
            cells.append(cur); cur = ""
        else:
            cur += ch
    cells.append(cur)
    return cells


URL = re.compile(r"(?<![<(\[`/])\b(https?://[^\s<>()`|]+[^\s<>()`|.,;:])")
def autolink(l):
    """bare URLs outside code spans become <autolinks>, so LaTeX can break them"""
    parts = re.split(r"(`[^`]*`)", l)
    return "".join(p if p.startswith("`") else URL.sub(r"<\1>", p) for p in parts)


def preprocess(md):
    lines = md.split("\n")
    start = next(i for i, l in enumerate(lines) if l.strip() == "# Front Matter")
    lines = lines[start + 1:]
    out, skip, fence = [], False, False
    i = 0
    while i < len(lines):
        l = lines[i]; s = l.strip()
        if s.startswith("```"):
            fence = not fence
        if fence or s.startswith("```"):
            out.append(l); i += 1; continue
        if s in ("\\pagebreak", "---"):
            i += 1; continue
        if s in ("## Title Page", "## Table of Contents"):
            skip = True; i += 1; continue
        if skip:
            if s.startswith("## ") or s.startswith("# "):
                skip = False
            else:
                i += 1; continue
        m = re.match(r"^## (.+)$", l)
        if m and m.group(1) in FRONT:
            if m.group(1) == "Statement of Contribution":
                out += ["", "```{=latex}", "\\cleardoublepage\\tableofcontents\\listoffigures\\listoftables", "```", ""]
            out.append("# " + m.group(1) + " {.unnumbered}")
            i += 1; continue
        if s.startswith("# Chapter 1."):
            out += ["", "```{=latex}", "\\mainmatter", "```", ""]
        if s == "# References":
            out += [l, "", "```{=latex}", "\\begingroup\\small\\setstretch{1.08}\\setlength{\\parindent}{-1.5em}"
                    "\\setlength{\\leftskip}{1.5em}\\setlength{\\parskip}{0.45em}\\RaggedRight", "```", ""]
            i += 1
            while i < len(lines) and not lines[i].startswith("# "):
                out.append(autolink(lines[i])); i += 1
            out += ["", "```{=latex}", "\\endgroup", "```", ""]
            continue
        # table caption line -> pandoc caption (before the table)
        m = re.match(r"^\*(Table [A-Z0-9]+\.\d+[a-z]?\.? .+?)\*$", s)
        if m:
            out += ["", ": " + m.group(1), ""]
            i += 1; continue
        # pipe table: rewrite the separator with content-based widths
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?\s*:?-{3,}", lines[i + 1].strip()):
            j = i
            block = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                block.append(lines[j]); j += 1
            rows = [split_row(b) for k, b in enumerate(block) if k != 1]
            w = col_widths(rows)
            seps = split_row(block[1])
            new = []
            for k, x in enumerate(w):
                sp = seps[k].strip() if k < len(seps) else "-"
                left, right = sp.startswith(":"), sp.endswith(":")
                new.append((":" if left else "") + "-" * x + (":" if right else ""))
            block[1] = "|" + "|".join(new) + "|"
            out += block
            i = j; continue
        out.append(autolink(l.replace("](figures/", "](../figures/")))
        i += 1
    return "\n".join(out)


# ------------------------------------------------------------------ LaTeX, after pandoc
def short_caption(c):
    m = re.match(r"((?:Figure|Table) [A-Z0-9]+\.\d+[a-z]?\.?)\s*(.*)", c, re.S)
    if not m:
        return c, c
    lab, rest = m.groups()
    first = re.split(r"(?<=[a-z0-9)])\.\s", rest, 1)[0].rstrip(".")
    return lab, first


def balanced(s, i):
    """index just after the {...} group starting at s[i] == '{'"""
    d = 0
    for k in range(i, len(s)):
        if s[k] == "{" and s[k - 1] != "\\": d += 1
        elif s[k] == "}" and s[k - 1] != "\\":
            d -= 1
            if d == 0:
                return k + 1
    raise ValueError("unbalanced")


def postprocess(tex):
    labels = {}
    # captions: bold label, short entry in the lists, \label for links
    out, pos = [], 0
    for m in re.finditer(r"\\caption\{", tex):
        if m.start() < pos:
            continue
        end = balanced(tex, m.end() - 1)
        body = tex[m.end():end - 1]
        lab, first = short_caption(body)
        if lab != body:
            kind = "fig" if lab.startswith("Figure") else "tbl"
            num = re.search(r"([A-Z0-9]+\.\d+[a-z]?)", lab).group(1)
            name = "%s:%s" % (kind, num)
            labels[("Figure " if kind == "fig" else "Table ") + num] = name
            rest = body[len(lab):].lstrip()
            new = "\\caption[%s %s]{\\textbf{%s} %s}\\label{%s}" % (lab, first, lab, rest, name)
            out.append(tex[pos:m.start()]); out.append(new); pos = end
    out.append(tex[pos:]); tex = "".join(out)
    # headings: labels for "Section 4.3" and "Chapter 4"; a short running head for long chapter titles
    def head(m):
        cmd, title, lab = m.group(1), m.group(2), m.group(3)
        n = re.match(r"(?:Chapter )?(\d+|[A-Z])(?:\.(\d+))?[. ]", title + " ")
        if cmd == "chapter":
            c = re.match(r"(Chapter \d+|Appendix [A-D])", title)
            if c: labels[c.group(1)] = lab
            short = title if len(title) <= 62 else title[:62].rsplit(" ", 1)[0] + " …"
            return "\\%s{%s}\\label{%s}\\chaptermark{%s}" % (cmd, title, lab, short)
        s = re.match(r"(\d+\.\d+|[A-D]\.\d+)\s", title)
        if s: labels["Section " + s.group(1)] = lab
        return m.group(0)
    tex = re.sub(r"\\(chapter|section)\{(.+?)\}\\label\{([^}]+)\}", head, tex)
    # header rows of tables in bold
    def bold_head(m):
        return m.group(0).replace("\\raggedright\n", "\\raggedright\\bfseries\n")
    tex = re.sub(r"\\toprule\\noalign\{\}\n.*?\\midrule", bold_head, tex, flags=re.S)
    tex = re.sub(r"\\toprule\n.*?\\midrule", bold_head, tex, flags=re.S)
    # cross-references in running text become links (not inside code, headings, captions)
    ref = re.compile(r"(?<![\w{])((?:Tables?|Figures?) ([A-Z0-9]+\.\d+[a-z]?)|Sections? (\d+\.\d+|[A-D]\.\d+)|§ ?(\d+\.\d+)|Chapter (\d)(?![\d.]\d)|Appendix ([A-D])(?![\w.]\d))")
    def link(m):
        txt = m.group(0)
        if m.group(2):
            key = ("Figure " if txt.startswith("Fig") else "Table ") + m.group(2)
        elif m.group(3):
            key = "Section " + m.group(3)
        elif m.group(4):
            key = "Section " + m.group(4)
        elif m.group(5):
            key = "Chapter " + m.group(5)
        else:
            key = "Appendix " + m.group(6)
        return "\\hyperref[%s]{%s}" % (labels[key], txt) if key in labels else txt
    chunks = re.split(r"(\\begin\{Highlighting\}.*?\\end\{Highlighting\}|\\begin\{verbatim\}.*?\\end\{verbatim\})", tex, flags=re.S)
    n = 0
    for k in range(0, len(chunks), 2):
        lines = chunks[k].split("\n")
        for i, l in enumerate(lines):
            if re.match(r"\s*\\(chapter|section|subsection|caption|label|addcontentsline|hypertarget)", l) or "\\caption[" in l:
                continue
            new = ref.sub(link, l)
            n += new != l
            lines[i] = new
        chunks[k] = "\n".join(lines)
    tex = "".join(chunks)
    # unnumbered front-matter chapters: pandoc writes \chapter*{..}\addcontentsline; give them a running head
    tex = re.sub(r"(\\chapter\*\{([^}]+)\}(?:\\label\{[^}]+\})?)", lambda m: m.group(1) + "\\markboth{%s}{}" % m.group(2), tex)
    tex = re.sub(r"∎", r"\\ensuremath{∎}", tex)
    tex = re.sub(r"\\includegraphics\[width=[\d.]+in(,height=\\textheight)?\]", r"\\includegraphics[width=\\linewidth]", tex)
    def sideways(m):
        f = m.group(0)
        if not re.search(r"fig(1_1|4_1|5_1)_", f):
            return f
        f = f.replace("\\begin{figure}", "\\begin{sidewaysfigure}").replace("\\end{figure}", "\\end{sidewaysfigure}")
        return f.replace("\\includegraphics[width=\\linewidth]", "\\includegraphics[width=\\linewidth,height=0.66\\textwidth,keepaspectratio]")
    tex = re.sub(r"\\begin\{figure\}.*?\\end\{figure\}", sideways, tex, flags=re.S)
    def bands(m):
        body = m.group(0)
        ncol = len(re.findall(r"(?:>\{[^}]*\})?p\{", m.group(1))) or None
        if not ncol:
            return body
        def row(r):
            cells = re.split(r"(?<!\\)&", r.group(1))
            if len(cells) == ncol and cells[0].strip() and all(not c.strip() for c in cells[1:]):
                return "\\multicolumn{%d}{@{}l}{\\rule{0pt}{1.1em}\\small\\itshape %s} \\\\" % (ncol, cells[0].strip())
            return r.group(0)
        return re.sub(r"^(.*?) \\\\$", row, body, flags=re.M)
    tex = re.sub(r"\\begin\{longtable\}\[\]\{@\{\}(.*?)@\{\}\}.*?\\end\{longtable\}", bands, tex, flags=re.S)
    return tex, labels, n


def main():
    md = preprocess(SRC.read_text())
    BUILD.mkdir(parents=True, exist_ok=True)
    (BUILD / "body.md").write_text(md)
    subprocess.run(["pandoc", str(BUILD / "body.md"), "-f", "markdown-implicit_figures+implicit_figures",
                    "-t", "latex", "--standalone", "--template", str(DIR / "template.tex"),
                    "--top-level-division=chapter", "--highlight-style", str(DIR / "thesis.theme"),
                    "--columns=20", "--wrap=none", "-V", "title=Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the EHDS",
                    "-V", "author=Arshad Akhtar Abbasia", "-o", str(BUILD / "thesis.tex")], check=True)
    tex, labels, n = postprocess((BUILD / "thesis.tex").read_text())
    (BUILD / "thesis.tex").write_text(tex)
    for k in range(3):
        r = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory=build",
                            "build/thesis.tex"], cwd=DIR, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:]); sys.exit("xelatex failed")
    log = (BUILD / "thesis.log").read_text(errors="replace")
    missing = sorted(set(re.findall(r"Missing character: There is no (.) ", log)))
    over = len(re.findall(r"Overfull \\hbox \((\d+\.\d+)pt", log))
    shutil.copy(BUILD / "thesis.pdf", OUT)
    pages = re.search(r"Output written on .*?\((\d+) pages", log)
    print("%s: %s pages, %d labels, %d lines with cross-reference links; missing glyphs %s; overfull boxes %d"
          % (OUT.name, pages.group(1) if pages else "?", len(labels), n, missing or "none", over))


if __name__ == "__main__":
    main()
