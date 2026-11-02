# P108 — Appendix A listings synced to the P107 code (A.10 trf_checker, A.15 crypto_envelope, A.22 its console output,
# A.23 z3_check). Frozen.
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "handoff_tools"))
import appendix_sync
from frozen import freeze
EDITS = freeze("P108_appendix_sync", lambda: appendix_sync.block_edits("P108-B"))
LOST_OK = []
