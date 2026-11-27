"""Style pandoc's default reference.docx for an Elsevier-friendly single-column manuscript."""
import sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_LINE_SPACING, WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

src, dst = sys.argv[1], sys.argv[2]
doc = Document(src)
SERIF, MONO = "Times New Roman", "Courier New"

def font(style, name=SERIF, size=12, bold=None, italic=None, color=RGBColor(0, 0, 0)):
    f = style.font
    f.name, f.size = name, Pt(size)
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts"); rpr.append(rfonts)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(a), name)
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        if rfonts.get(qn(a)) is not None:
            del rfonts.attrib[qn(a)]
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
    f.color.rgb = color

def para(style, before=0, after=6, spacing=1.5, align=None, keep=False):
    pf = style.paragraph_format
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    pf.line_spacing = spacing
    if align is not None: pf.alignment = align
    if keep: pf.keep_with_next = True

st = doc.styles
from docx.enum.style import WD_STYLE_TYPE
class _S:
    def __getitem__(self, name):
        for x in doc.styles:
            if x.name == name or x.style_id == name.replace(" ", ""):
                return x
        if name == "Source Code":
            s_ = doc.styles.add_style("Source Code", WD_STYLE_TYPE.PARAGRAPH)
            s_.base_style = doc.styles["Normal"]
            return s_
        raise KeyError(name)
    def __iter__(self):
        return iter(doc.styles)
st = _S()
for name in ("Normal", "Body Text", "First Paragraph", "Compact"):
    if name in [s.name for s in st]:
        font(st[name]); para(st[name], after=6)
for name, size in (("Heading 1", 12), ("Heading 2", 12), ("Heading 3", 12)):
    font(st[name], size=size, bold=True, italic=(name == "Heading 2"))
    para(st[name], before=12, after=6, keep=True)
font(st["Title"], size=16, bold=True); para(st["Title"], before=0, after=12, align=WD_ALIGN_PARAGRAPH.LEFT)
font(st["Abstract Title"], size=12, bold=True); para(st["Abstract Title"], before=6, after=6, align=WD_ALIGN_PARAGRAPH.LEFT)
for name in ("Abstract",):
    if name in [s.name for s in st]:
        font(st[name], size=12); para(st[name], after=6)
for name in ("Image Caption", "Table Caption", "Caption"):
    if name in [s.name for s in st]:
        font(st[name], size=10, italic=False); para(st[name], before=4, after=10, spacing=1.15)
# Source Code: monospace, single spacing, boxed
sc = st["Source Code"]
font(sc, name=MONO, size=9); para(sc, before=0, after=0, spacing=1.0)
ppr = sc.element.get_or_add_pPr()
bdr = OxmlElement("w:pBdr")
for side in ("top", "left", "bottom", "right"):
    e = OxmlElement(f"w:{side}")
    e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "6"); e.set(qn("w:space"), "4"); e.set(qn("w:color"), "1B1C20")
    bdr.append(e)
ppr.append(bdr)
if "Verbatim Char" in [s.name for s in st]:
    font(st["Verbatim Char"], name=MONO, size=9)
for name in ("Hyperlink",):
    if name in [s.name for s in st]:
        st[name].font.color.rgb = RGBColor(0, 0, 0)
# Algorithm blocks (Algorithm 1): booktabs-style rules, no box, no monospace, numbered lines
MATH_SERIF = SERIF
def alg_style(name, left_cm, top=False, bottom=None, after=1, before=0, caption=False, right_tab=True):
    try:
        s_ = doc.styles[name]
    except KeyError:
        s_ = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    s_.base_style = doc.styles["Normal"]
    font(s_, size=10 if caption else 10.5)
    pf = s_.paragraph_format
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    pf.line_spacing = 1.15 if caption else 1.1
    pf.keep_with_next = bottom is None
    pf.keep_together = True
    pf.widow_control = True
    pf.left_indent, pf.first_line_indent = Cm(left_cm), Cm(-left_cm) if left_cm else Cm(0)
    pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
    ppr = s_.element.get_or_add_pPr()
    for old in ppr.findall(qn("w:pBdr")) + ppr.findall(qn("w:tabs")):
        ppr.remove(old)
    bd = OxmlElement("w:pBdr")
    for side, sz in (("top", "8" if top else None), ("bottom", {"thin": "4", "thick": "8"}.get(bottom))):
        if sz:
            e = OxmlElement(f"w:{side}")
            e.set(qn("w:val"), "single"); e.set(qn("w:sz"), sz); e.set(qn("w:space"), "3"); e.set(qn("w:color"), "000000")
            bd.append(e)
    if len(bd):
        ppr.append(bd)
    tabs = OxmlElement("w:tabs")
    if left_cm:
        t1 = OxmlElement("w:tab"); t1.set(qn("w:val"), "left"); t1.set(qn("w:pos"), str(int(left_cm * 567))); tabs.append(t1)
    if right_tab:
        t2 = OxmlElement("w:tab"); t2.set(qn("w:val"), "right"); t2.set(qn("w:pos"), str(int(16.0 * 567))); tabs.append(t2)
    ppr.append(tabs)
    ppr.append(OxmlElement("w:suppressLineNumbers"))
    ORDER = ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr", "widowControl", "numPr",
             "suppressLineNumbers", "pBdr", "shd", "tabs", "suppressAutoHyphens", "kinsoku", "wordWrap",
             "overflowPunct", "topLinePunct", "autoSpaceDE", "autoSpaceDN", "bidi", "adjustRightInd",
             "snapToGrid", "spacing", "ind", "contextualSpacing", "mirrorIndents", "suppressOverlap",
             "jc", "textDirection", "textAlignment", "textboxTightWrap", "outlineLvl", "divId", "cnfStyle",
             "rPr", "sectPr", "pPrChange"]
    kids = list(ppr)
    for k in kids:
        ppr.remove(k)
    for k in sorted(kids, key=lambda e: ORDER.index(e.tag.split("}")[1])):
        ppr.append(k)
    return s_
alg_style("Alg Title", 0, top=True, bottom="thin", before=10, after=3, caption=True, right_tab=False)
alg_style("Alg Head", 1.6)
alg_style("Alg L0", 0.9)
alg_style("Alg L1", 1.6)
alg_style("Alg L0 End", 0.9, bottom="thick", after=12)
alg_style("Alg L1 End", 1.6, bottom="thick", after=12)
# keep figure with its caption (below) and table caption with its table (above)
for name in ("Table Caption",):
    if name in [x.name for x in st]:
        st[name].paragraph_format.keep_with_next = True
for name in ("Figure", "Captioned Figure"):
    if name in [x.name for x in st]:
        st[name].paragraph_format.keep_with_next = True
for name in ("Normal", "Body Text", "First Paragraph", "Compact"):
    if name in [x.name for x in st]:
        st[name].paragraph_format.widow_control = True
# page setup: A4, 2.5 cm margins, page number in footer
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
for m in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
    setattr(sec, m, Cm(2.5))
fp = sec.footer.paragraphs[0] if sec.footer.paragraphs else sec.footer.add_paragraph()
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = fp.add_run()
for tag, attr in (("w:fldChar", {"w:fldCharType": "begin"}), ("w:instrText", None), ("w:fldChar", {"w:fldCharType": "end"})):
    e = OxmlElement(tag)
    if attr:
        for k, v in attr.items(): e.set(qn(k), v)
    else:
        e.set(qn("xml:space"), "preserve"); e.text = " PAGE "
    run._r.append(e)
run.font.name, run.font.size = SERIF, Pt(10)
# empty metadata
cp = doc.core_properties
cp.author = ""; cp.last_modified_by = ""; cp.title = ""; cp.comments = ""; cp.keywords = ""; cp.subject = ""
doc.save(dst)
print("ok")
