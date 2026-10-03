# P18 — Appendix A after P17: listings and the two re-recorded outputs synced (block edits), then
# "Theorem" -> "Proposition" in prose lines outside code fences. Prose edits are computed on the
# text as it will stand after the block edits, so their counts are exact.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "handoff_tools"))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import appendix_sync
from frozen import freeze, at
PRE = "e83e061"   # commit before P15-P18; the new blocks are the files as P17 left them
A = appendix_sync.APPENDIX


def compute():
    root = pathlib.Path(__file__).resolve().parent.parent
    text = at(PRE, A)
    block = appendix_sync.block_edits_text(text, lambda f: (root / f).read_text(encoding="utf-8"), "P18-B")
    for e in block:
        text = text.replace(e["old"], e["new"])
    rules = [(r"\bTheorems 1 and 2\b", "Propositions 1 and 2"), (r"\bTheorem ([12])\b", r"Proposition \1"),
             (r"\btheorems\b", "propositions"), (r"\btheorem's\b", "proposition's"), (r"\btheorem\b", "proposition")]
    lines, fence, seen = text.split("\n"), False, {}
    for ln in lines:
        if ln.startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        new = ln
        for a, b in rules:
            new = re.sub(a, b, new)
        if new != ln and ln not in seen:
            seen[ln] = new
    prose = [dict(id=f"P18-{i:02d}", file=A, old=o, new=n, count=lines.count(o), why="M4a: theorems renamed propositions")
             for i, (o, n) in enumerate(seen.items(), 1)]
    return block + prose


EDITS = freeze("P18_appendixA_propositions", compute)
