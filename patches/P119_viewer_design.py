# P119 — demo_app viewer synced to TRF 8f785e3 (release 1.3.0): grouped, numbered walk navigation, brand mark,
# palette alerts and fact cards, walk progress strip. Presentation only. Blob-based.
import subprocess
_b = lambda sha: subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, text=True, check=True).stdout
LOST_OK = []
EDITS = [
 dict(id='P119-01', file='demo_app/app.py', old=_b("6a8dba6d16998175cb74e483840a89b793eb7567"), new=_b("426c50aa0009b307655709f900a26f55c5900ac4"), why="viewer design pass, TRF 8f785e3"),
 dict(id='P119-02', file='demo_app/ui.py', old=_b("43a01c92f02a198d7a0fca4d626608f6bfce1103"), new=_b("45a0c0d7b32c75c60e6da5378c5b2b4ea0dd81e8"), why="viewer design pass, TRF 8f785e3"),
]
