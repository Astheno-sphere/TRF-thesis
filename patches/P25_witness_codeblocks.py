# P25 — MIN-10: the witness lines in §5.3 and §5.4 were set as quotation lines with typographic
# substitutions (⇒, α, →); they are now code blocks, one line per witness, verbatim from the
# recorded run (repro_package/results/trf_output.txt, lines 17-19 and 22-24).
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from frozen import freeze, at
PRE, C5 = "83676e7", "Chapter5_Demonstration_v1.md"


def compute():
    t = at(PRE, C5).split("\n")
    out = at(PRE, "repro_package/results/trf_output.txt").split("\n")
    old1, old2 = "\n".join(t[80:83]), "\n".join(t[96:99])
    assert old1.startswith("> C1 requires") and old2.startswith("> rid=100")
    new1 = "```text\n" + "\n".join(l.strip() for l in out[21:24]) + "\n```"
    new2 = "```text\n" + "\n".join(l.strip() for l in out[16:19]) + "\n```"
    return [dict(id="P25-01", file=C5, old=old1, new=new1, why="MIN-10: §5.3 witnesses verbatim, one per line"),
            dict(id="P25-02", file=C5, old=old2, new=new2, why="MIN-10: §5.4 witnesses verbatim, one per line")]


EDITS = freeze("P25_witness_codeblocks", compute)
