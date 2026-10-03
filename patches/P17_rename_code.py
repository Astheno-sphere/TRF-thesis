# P17 — M4a in the code: "Theorem" -> "Proposition" in comments, docstrings and printed headers of
# trf_checker.py (three copies) and app.py. Printed output changes in two header lines only.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from frozen import freeze, at
PRE = "e83e061"   # commit before P15-P18
RULES = [(r"\bTheorems 1 and 2\b", "Propositions 1 and 2"), (r"\bTheorem ([12])\b", r"Proposition \1"),
         (r"\btheorems\b", "propositions")]
def rename(s):
    for a, b in RULES:
        s = re.sub(a, b, s)
    return s
def compute():
    edits = []
    for f in ["demo_app/trf_checker.py", "repro_package/trf_checker.py", "code_artefacts/trf_checker.py", "demo_app/app.py"]:
        lines = at(PRE, f).split("\n")
        seen = {}
        for ln in lines:
            if rename(ln) != ln and ln not in seen:
                seen[ln] = rename(ln)
        for i, (o, n) in enumerate(seen.items(), 1):
            edits.append(dict(id=f"P17-{f.split('/')[0][:4]}-{pathlib.Path(f).stem[:3]}-{i:02d}", file=f, old=o, new=n,
                              count=lines.count(o), why="M4a: theorems renamed propositions in code"))
    return edits


EDITS = freeze("P17_rename_code", compute)
