# P52b — Appendix A.23/A.24 synced to the corrected z3_check.py (Semantics II fully encoded, F up to 120,
# mutations of the Proposition 2 construction) and its recorded output; A.2 line count. Frozen.
import pathlib, sys, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "handoff_tools"))
import appendix_sync
from frozen import freeze
def compute():
    e = appendix_sync.block_edits("P52b-B")
    e.append(dict(id="P52b-01", file=appendix_sync.APPENDIX,
                  old="needs the `z3-solver` package | 135 |", new="needs the `z3-solver` package | 153 |", why="line count"))
    return e
EDITS = freeze("P52b_appendix_z3", compute)
LOST_OK = ["hedge may ", "number 135", "number 24", "number 64", "number 1..24"]   # old module text, bounds and line count in the listing
