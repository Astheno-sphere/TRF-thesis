# P44b — Appendix A.10 (source listing of trf_checker.py) synced after P44. Block edit built by
# appendix_sync, frozen.
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "handoff_tools"))
import appendix_sync
from frozen import freeze
EDITS = freeze("P44b_appendixA_sync", lambda: appendix_sync.block_edits("P44b-B"))
LOST_OK = ["number 2026", "number 17", "number 30", "number 15..", "number 16"]   # the removed header: "Revised 3 Oct 2026 ... 30 Sept ... P04, P06; D-15..D-17"
