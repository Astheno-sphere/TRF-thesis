# P41 — MIN-13: the Table of Contents regenerated from the chapter and appendix headings after
# the renumbering (P38). It lists every numbered section with its number, so a reader can check
# the cross-references; the Word build adds page numbers with pandoc --toc. Generated, frozen.
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from frozen import freeze
FM = "Front_Matter_v1.md"
CHS = ["Chapter1_Introduction_v2.md", "Chapter2_LitReview_v2_FINAL.md", "Chapter3_Methodology_v1.md",
       "Chapter4_TRF_Model_v1.md", "Chapter5_Demonstration_v1.md", "Chapter6_Discussion_v1.md",
       "Chapter7_Conclusion_v1.md"]
APPS = [("Appendix A", "code_artefacts/README_Appendix_A.md"), ("Appendix B", "Appendix_B_Search_Log.md"),
        ("Appendix C", "Appendix_C_Evaluation_Instrument.md")]


def compute():
    fm = pathlib.Path(FM).read_text(encoding="utf-8")
    old = fm[fm.index("## Table of Contents"):].rstrip("\n")
    out = ["## Table of Contents", ""]
    for f in CHS:
        t = pathlib.Path(f).read_text(encoding="utf-8")
        title = re.search(r"^# (Chapter \d+\.[^\n]*)", t, re.M).group(1)
        out.append(f"**{title}**")
        out.append("")
        for h in re.findall(r"^## (\d+\.\d+ [^\n]*)", t, re.M):
            out.append(f"- {h}")
        out.append("")
    out.append("**References**")
    out.append("")
    for name, f in APPS:
        t = pathlib.Path(f).read_text(encoding="utf-8")
        title = re.search(r"^# ([^\n]*)", t, re.M).group(1)
        out.append(f"**{title}**")
        out.append("")
        secs = re.findall(r"^## ([A-C]\.\d+ [^\n]*)", t, re.M)
        out += [f"- {h}" for h in secs]
        if secs:
            out.append("")
    new = "\n".join(out).rstrip("\n")
    return [dict(id="P41-01", file=FM, old=old, new=new, why="MIN-13: TOC regenerated from headings")]


EDITS = freeze("P41_toc", compute)
LOST_OK = ["number 59", "number 18", "hedge not established"]   # prose TOC replaced by the generated section list
