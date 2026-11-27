"""Post-process the pandoc docx: line numbers, booktabs-like real Word tables, reference list
layout, listing caption kept with its box, empty author metadata."""
import re, sys
from docx import Document
from docx.shared import Pt, Cm
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

src, dst = sys.argv[1], sys.argv[2]
doc = Document(src)

# line numbers (restart each page) on every section
for sec in doc.sections:
    sp = sec._sectPr
    for old in sp.findall(qn("w:lnNumType")):
        sp.remove(old)
    ln = OxmlElement("w:lnNumType")
    ln.set(qn("w:countBy"), "1"); ln.set(qn("w:distance"), "283"); ln.set(qn("w:restart"), "continuous")
    pgsz = sp.find(qn("w:pgSz"))
    (pgsz.addnext(ln) if pgsz is not None else sp.insert(0, ln))

def border(tag, val="single", sz="8"):
    e = OxmlElement(tag)
    e.set(qn("w:val"), val); e.set(qn("w:sz"), sz); e.set(qn("w:space"), "0"); e.set(qn("w:color"), "000000")
    return e

for t in doc.tables:
    tblPr = t._tbl.tblPr
    for old in tblPr.findall(qn("w:tblBorders")):
        tblPr.remove(old)
    b = OxmlElement("w:tblBorders")
    b.append(border("w:top", sz="8")); b.append(border("w:bottom", sz="8"))
    b.append(border("w:insideH", val="nil")); b.append(border("w:insideV", val="nil"))
    tblPr.append(b)
    w = tblPr.find(qn("w:tblW"))
    if w is None:
        w = OxmlElement("w:tblW"); tblPr.append(w)
    w.set(qn("w:type"), "pct"); w.set(qn("w:w"), "5000")
    hdr = t.rows[0]
    for c in hdr.cells:
        tcPr = c._tc.get_or_add_tcPr()
        tb = OxmlElement("w:tcBorders"); tb.append(border("w:bottom", sz="4")); tcPr.append(tb)
    for row in t.rows:
        for c in row.cells:
            for p in c.paragraphs:
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    r.font.size = Pt(10)

# air below each table (the rule would otherwise touch the next paragraph)
from docx.text.paragraph import Paragraph
for t in doc.tables:
    nxt = t._tbl.getnext()
    if nxt is not None and nxt.tag == qn("w:p"):
        Paragraph(nxt, t._parent).paragraph_format.space_before = Pt(10)

in_refs = False
paras = doc.paragraphs
for i, p in enumerate(paras):
    if p.style.name.lower().startswith("heading") and p.text.strip() == "References":
        in_refs = True; continue
    if in_refs and re.match(r"^\[\d+\]", p.text):
        pf = p.paragraph_format
        pf.left_indent, pf.first_line_indent = Cm(0.9), Cm(-0.9)
        pf.line_spacing, pf.space_after = 1.15, Pt(4)
        for r in p.runs:
            r.font.size = Pt(11)
    if p.text.startswith(("Fig. ", "Table ")) and p.style.name in ("Table Caption", "Image Caption"):
        p.paragraph_format.keep_together = True
    if p.style.name.startswith("Alg "):
        p.paragraph_format.widow_control = True

cp = doc.core_properties
cp.author = ""; cp.last_modified_by = ""; cp.comments = ""; cp.keywords = ""; cp.subject = ""
cp.category = ""; cp.content_status = ""; cp.identifier = ""; cp.revision = 1
doc.save(dst)

# app.xml: remove Company / Manager if present
import zipfile, shutil, os
tmp = dst + ".tmp"
with zipfile.ZipFile(dst) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
    for it in zi.infolist():
        data = zi.read(it.filename)
        if it.filename == "docProps/app.xml":
            s = data.decode()
            s = re.sub(r"<Company>.*?</Company>", "<Company></Company>", s)
            s = re.sub(r"<Manager>.*?</Manager>", "", s)
            data = s.encode()
        zo.writestr(it, data)
shutil.move(tmp, dst)
print("post-processed", dst)
