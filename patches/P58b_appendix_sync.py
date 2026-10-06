# P58b — Appendix A listings synced to the checker with the patient-link commitment (P58) and its recorded
# runs (A.10, A.16, A.18). Frozen. Line-count prose is updated when João's 6 Oct edits are merged.
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "handoff_tools"))
import appendix_sync
from frozen import freeze
EDITS = freeze("P58b_appendix_sync", lambda: appendix_sync.block_edits("P58b-B"))
LOST_OK = []
