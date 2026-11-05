# P116 — Appendix A listings synced to the P115 code (frozen).
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "handoff_tools"))
import appendix_sync
from frozen import freeze
EDITS = freeze("P116_appendix_sync", lambda: appendix_sync.block_edits("P116-B"))
LOST_OK = []
