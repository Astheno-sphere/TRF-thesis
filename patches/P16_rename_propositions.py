# P16 — M4a: Theorems -> Propositions everywhere in the prose; Proposition L -> Proposition 4
# (with Proposition 3 from P15, the four results are numbered 1-4). Line-level edits, generated
# from the files as they stand after P15, so every changed line is its own logged edit.
# Excluded: Appendix B (query 34 is a verbatim search string, history) and Appendix A (its code
# listings must stay equal to the code; renamed with the code in P17).
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from frozen import freeze, at
PRE = "e83e061"   # commit before P15-P18
FILES = ["Front_Matter_v1.md", "Chapter1_Introduction_v2.md", "Chapter2_LitReview_v2_FINAL.md",
         "Chapter3_Methodology_v1.md", "Chapter4_TRF_Model_v1.md", "Chapter5_Demonstration_v1.md",
         "Chapter6_Discussion_v1.md", "Chapter7_Conclusion_v1.md", "Appendix_C_Evaluation_Instrument.md"]
RULES = [(r"\bTheorems 1 and 2\b", "Propositions 1 and 2"), (r"\bTheorem ([12])\b", r"Proposition \1"),
         (r"\bTheorem statements\b", "Proposition statements"), (r"\btheorems\b", "propositions"),
         (r"\btheorem's\b", "proposition's"), (r"\btheorem\b", "proposition"),
         (r"\bProposition L\b", "Proposition 4")]

def rename(line):
    for a, b in RULES:
        line = re.sub(a, b, line)
    return line

def compute():
    import importlib.util
    spec = importlib.util.spec_from_file_location("p15", pathlib.Path(__file__).parent / "P15_anchoring_proposition.py")
    p15 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p15)
    edits = []
    for f in FILES:
        text = at(PRE, f)
        for e in p15.EDITS:                       # the state P16 was computed against: after P15
            if e["file"] == f:
                text = text.replace(e["old"], e["new"])
        lines = text.split("\n")
        seen = {}
        for ln in lines:
            new = rename(ln)
            if new != ln and ln not in seen:
                seen[ln] = new
        for i, (old, new) in enumerate(seen.items(), 1):
            edits.append(dict(id=f"P16-{f[:9].replace('_', '')}-{i:02d}", file=f, old=old, new=new,
                              count=lines.count(old), why="M4a: theorems renamed propositions"))
    return edits


EDITS = freeze("P16_rename_propositions", compute)
