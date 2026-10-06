# P59c — Appendix A.17 is now the full-cohort comparison re-run on 6 Oct with the final code and the
# regenerated cohort (pinned Synthea jar); intro rewritten and listing synced. Frozen.
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "handoff_tools"))
import appendix_sync
from frozen import freeze
A = "code_artefacts/README_Appendix_A.md"
def compute():
    t = (pathlib.Path(__file__).resolve().parent.parent / A).read_text(encoding="utf-8")
    i = t.index("Produced by command 4 against the regenerated 98-bundle cohort.")
    j = t.index("\n", i)
    e = [dict(id="P59c-01", file=A, old=t[i:j],
              new="Produced by command 4 against the 98-bundle cohort regenerated on 6 October 2026 with the pinned jar (commands 2 and 3) and the final code. It is the source of Chapter 5, Table 5.7, at a mean payload of 1,002 bytes; the September cohort it replaces gave the same six measures at 1,006 bytes. Reproducing it requires regenerating the cohort with command 3, because the full cohort is about 315 MB and is not committed.",
              why="C9: one code version")]
    t2 = t.replace(e[0]["old"], e[0]["new"], 1)
    e += appendix_sync.block_edits_text(t2, lambda f: (pathlib.Path(__file__).resolve().parent.parent / f).read_text(encoding="utf-8"), "P59c-B")
    return e
EDITS = freeze("P59c_a17", compute)
LOST_OK = ["number 5.8", "number 98", "number 21", "number 28", "number 35", "number 314", "number 3", "number 1006", "number 0", "hedge may "]
