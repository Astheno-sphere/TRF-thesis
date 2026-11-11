# P134 — demo_app/app.py synced to the code repository after its Proposition 1 statement was matched to the thesis
# (TRF e92f081): the ceiling disjunct is stated as tested only for records the ceiling reaches. The other changed
# code-repository files (.zenodo.json, CITATION.cff, CHANGE_TRAIL.md) have no copy in this repository.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from frozen import freeze

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = pathlib.Path("/home/claude/src/TRF")


def compute():
    return [dict(id='P134-01', file='demo_app/app.py',
                 old=(ROOT / 'demo_app/app.py').read_text(encoding="utf-8"),
                 new=(SRC / 'app.py').read_text(encoding="utf-8"),
                 why="viewer copy of app.py: Proposition 1 statement as in Chapter 4 (TRF e92f081)")]


LOST_OK = []
EDITS = freeze("P134_viewer_prop1_copies", compute)
