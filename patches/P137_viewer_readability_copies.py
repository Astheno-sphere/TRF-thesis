# P137 — demo_app/app.py and demo_app/ui.py synced to the code repository after its readability pass (TRF 0c540b7):
# presentation only (reading column, type scale, contrast) and "in the model" on the start page. No computation touched.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from frozen import freeze

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = pathlib.Path("/home/claude/src/TRF")


def compute():
    return [dict(id=f'P137-0{i}', file=f'demo_app/{n}',
                 old=(ROOT / 'demo_app' / n).read_text(encoding="utf-8"),
                 new=(SRC / n).read_text(encoding="utf-8"),
                 why=f"viewer copy of {n} after the readability pass (TRF 0c540b7)")
            for i, n in enumerate(['app.py', 'ui.py'], 1)]


LOST_OK = []
EDITS = freeze("P137_viewer_readability_copies", compute)
