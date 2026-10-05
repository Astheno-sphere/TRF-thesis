# P57b — the redesigned viewer's code (app.py; requirements). Frozen: edits in P57b_app_code.edits.json.
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from frozen import freeze
EDITS = freeze("P57b_app_code", lambda: None)
LOST_OK = []
