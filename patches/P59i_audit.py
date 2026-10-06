# P59i — independent audit of the review-4 merge (6 Oct): JF [39] tail restored; Appendix A three tamper
# tests and 1,002 bytes; stale contents entries for Chapter 6; P = infinity noted where the artefact's schedule
# is given; proof step 4 with the third trigger; §2.4 strands in their stated order. Frozen.
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from frozen import freeze
EDITS = freeze("P59i_audit", lambda: None)
LOST_OK = ["number 1,006", "number 6.12"]
