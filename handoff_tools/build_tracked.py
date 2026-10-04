#!/usr/bin/env python3
"""Tracked-changes comparison against the draft Prof. Ferreira reviewed (4 Oct 2026, B-40).

    python3 handoff_tools/build_tracked.py   -> VERA-SNARK_Thesis_TRACKED_vs_30Sept.docx

Old text: supervisor_review/draft_as_reviewed_tracked_rejected.txt (the draft as he reviewed it,
his own tracked proposals rejected). New text: the assembled submission, front matter to the end of
Chapter 7. Paragraphs are aligned, and each changed paragraph is shown as word-level insertions and
deletions under one author, so Word's Review pane lists every change and he can accept or reject.
The appendices (code listings and console outputs) and the reference list are left out: they are
regenerated from the code and the chapter lists and are checked by trail_check, not read for prose.
Tables and equations are compared as text, so their layout here is plain; the formatted thesis is
VERA-SNARK_Thesis_SUBMISSION.docx.
"""
import difflib, html, os, re, subprocess, tempfile, zipfile, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
OLD = ROOT / "supervisor_review" / "draft_as_reviewed_tracked_rejected.txt"
NEW = ROOT / "VERA-SNARK_Thesis_SUBMISSION.md"
OUT = ROOT / "VERA-SNARK_Thesis_TRACKED_vs_30Sept.docx"
AUTHOR = "Arshad Akhtar Abbasia"
DATE = datetime.datetime(2026, 10, 4, 12, 0).strftime("%Y-%m-%dT%H:%M:%SZ")


def old_paragraphs():
    lines = OLD.read_text(encoding="utf-8").split("\n")
    a = next(i for i, l in enumerate(lines) if l.strip() == "Abstract")
    b = next(i for i, l in enumerate(lines) if l.strip() == "References" and i > 1000)
    paras, buf = [], []
    for l in lines[a:b] + [""]:
        if l.strip():
            buf.append(l.strip())
        elif buf:
            paras.append(" ".join(buf)); buf = []
    out = []
    in_toc = False
    for p in paras:
        if p in ("Contents", "Table of Contents"):
            in_toc = True; continue
        if in_toc and re.search(r"\s[ivxlc\d]+$", p) and len(p) < 140:
            continue
        in_toc = False
        out.append(p)
    # the Version and Change Record (moved to the repository) stays in as deleted text
    return out


BASE = None          # set by --base <commit>: compare against that commit's assembled submission (B-44)


def new_paragraphs(md=None):
    md = NEW.read_text(encoding="utf-8") if md is None else md
    md = md[md.index("## Abstract"):md.index("\n# References")]
    md = re.sub(r"^\\pagebreak\s*$|^---\s*$", "", md, flags=re.M)
    # drop the generated contents list (the old one is dropped too)
    md = re.sub(r"## Table of Contents\n.*?(?=\n# )", "", md, flags=re.S)
    md = re.sub(r"^(#{1,3}) (.+)$", lambda m: "%s HDR%d %s" % (m.group(1), len(m.group(1)), m.group(2)), md, flags=re.M)
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, "n.md"); open(p, "w", encoding="utf-8").write(md)
        txt = subprocess.run(["pandoc", p, "-t", "plain", "--wrap=none"], capture_output=True,
                             text=True, check=True).stdout
    paras = [re.sub(r"\s+", " ", x).strip() for x in re.split(r"\n\s*\n", txt)]
    out = []
    for x in paras:
        if not x:
            continue
        m = re.match(r"^HDR(\d) (.*)$", x)
        out.append((int(m.group(1)), m.group(2)) if m else (0, x))
    return out


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def esc(s):
    return html.escape(s, quote=False)

_id = [0]
def nid():
    _id[0] += 1; return _id[0]

def r_plain(t):
    return '<w:r><w:t xml:space="preserve">%s</w:t></w:r>' % esc(t)

def r_ins(t):
    return '<w:ins w:id="%d" w:author="%s" w:date="%s"><w:r><w:t xml:space="preserve">%s</w:t></w:r></w:ins>' % (nid(), AUTHOR, DATE, esc(t))

def r_del(t):
    return '<w:del w:id="%d" w:author="%s" w:date="%s"><w:r><w:delText xml:space="preserve">%s</w:delText></w:r></w:del>' % (nid(), AUTHOR, DATE, esc(t))

def ppr(level, mark=None):
    st = {0: "BodyText", 1: "Heading1", 2: "Heading2", 3: "Heading3"}[level]
    m = ""
    if mark == "ins":
        m = '<w:rPr><w:ins w:id="%d" w:author="%s" w:date="%s"/></w:rPr>' % (nid(), AUTHOR, DATE)
    elif mark == "del":
        m = '<w:rPr><w:del w:id="%d" w:author="%s" w:date="%s"/></w:rPr>' % (nid(), AUTHOR, DATE)
    return '<w:pPr><w:pStyle w:val="%s"/>%s</w:pPr>' % (st, m)

def tokens(s):
    return re.findall(r"\S+\s*", s)

def word_diff(a, b):
    ta, tb = tokens(a), tokens(b)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            out.append(r_plain("".join(ta[i1:i2])))
        else:
            if i2 > i1: out.append(r_del("".join(ta[i1:i2])))
            if j2 > j1: out.append(r_ins("".join(tb[j1:j2])))
    return "".join(out)


def build():
    if BASE:
        base_md = subprocess.run(["git", "show", f"{BASE}:VERA-SNARK_Thesis_SUBMISSION.md"], cwd=ROOT,
                                 capture_output=True, text=True, check=True).stdout
        old = [t for _, t in new_paragraphs(base_md)]
    else:
        old = old_paragraphs()
    new = new_paragraphs()
    A = [norm(x) for x in old]
    B = [norm(t) for _, t in new]
    sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
    body, stats = [], dict(same=0, changed=0, inserted=0, deleted=0)
    def emit_del(i):
        body.append('<w:p>%s%s</w:p>' % (ppr(0, "del"), r_del(old[i]))); stats["deleted"] += 1
    def emit_ins(j):
        lvl, t = new[j]
        body.append('<w:p>%s%s</w:p>' % (ppr(lvl, "ins"), r_ins(t))); stats["inserted"] += 1
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for j in range(j1, j2):
                lvl, t = new[j]
                body.append('<w:p>%s%s</w:p>' % (ppr(lvl), r_plain(t))); stats["same"] += 1
            continue
        # pair old and new paragraphs inside the block by similarity, in order
        olds, news = list(range(i1, i2)), list(range(j1, j2))
        oi = 0
        for j in news:
            best, bi = 0.0, None
            for k in range(oi, min(len(olds), oi + 6)):
                r = difflib.SequenceMatcher(None, A[olds[k]], B[j], autojunk=False).quick_ratio()
                if r > best:
                    best, bi = r, k
            if bi is not None and best >= 0.55 and difflib.SequenceMatcher(None, A[olds[bi]], B[j], autojunk=False).ratio() >= 0.45:
                for k in range(oi, bi):
                    emit_del(olds[k])
                lvl, t = new[j]
                body.append('<w:p>%s%s</w:p>' % (ppr(lvl), word_diff(old[olds[bi]], t)))
                stats["changed"] += 1
                oi = bi + 1
            else:
                emit_ins(j)
        for k in range(oi, len(olds)):
            emit_del(olds[k])
    return body, stats


def main():
    global BASE, OUT
    import sys
    if "--base" in sys.argv:
        BASE = sys.argv[sys.argv.index("--base") + 1]
        OUT = ROOT / sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else OUT
    body, stats = build()
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, "s.md"); d = os.path.join(td, "s.docx")
        open(p, "w").write("# H\n\n## H2\n\n### H3\n\nText\n")
        subprocess.run(["pandoc", p, "-o", d, "--reference-doc", str(ROOT / "thesis_reference.docx")], check=True)
        z = zipfile.ZipFile(d); files = {n: z.read(n) for n in z.namelist()}
    doc = files["word/document.xml"].decode()
    head = doc[:doc.index("<w:body>") + len("<w:body>")]
    sect = re.search(r"<w:sectPr.*?</w:sectPr>", doc, re.S)
    intro = ('<w:p><w:pPr><w:pStyle w:val="Title"/></w:pPr>%s</w:p>'
             '<w:p><w:pPr><w:pStyle w:val="BodyText"/></w:pPr>%s</w:p>') % (
        r_plain("Revisions since the draft reviewed on 30 September 2026" if not BASE else
                "Revisions since the version reviewed on 4 October 2026 (commit %s), including the reviewer's tracked changes" % BASE),
        r_plain("Every change to the front matter and Chapters 1–7 is shown as a tracked insertion or deletion "
                "(Review → Track Changes → All Markup). Appendices and the reference list are regenerated from the "
                "code and the chapter lists and are not compared here. Tables and equations are compared as text; "
                "the formatted thesis is the separate file VERA-SNARK_Thesis_SUBMISSION.docx. "
                "Paragraphs unchanged: %d; revised: %d; new: %d; removed: %d."
                % (stats["same"], stats["changed"], stats["inserted"], stats["deleted"])))
    files["word/document.xml"] = (head + intro + "".join(body) + (sect.group(0) if sect else "") + "</w:body></w:document>").encode()
    import sys; sys.path.insert(0, str(ROOT / "handoff_tools"))
    from build_docx import reorder, SETTINGS_ORDER
    from lxml import etree
    sroot = etree.fromstring(files["word/settings.xml"]); reorder(sroot, SETTINGS_ORDER)
    files["word/settings.xml"] = etree.tostring(sroot, xml_declaration=True, encoding="UTF-8", standalone=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for n, b in files.items():
            z.writestr(n, b)
    print(OUT.name, stats)


if __name__ == "__main__":
    main()
