# P105 — sync demo_app/app.py to TRF 4d3ee63 (Start page quotes the P102 Statement of Contribution; concept DOI).
# Old blob f7b3f7cfe2198326b7a225abd8250269c47cbc9b, new blob 69e932186d6aebf1886c2afd0be77712d405c497 (written to the object store), so the patch replays deterministically.
import subprocess
_b = lambda sha: subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, text=True, check=True).stdout
LOST_OK = ["number 1.0.1", "number 23819275"]
EDITS = [
 dict(id='P105-01', file='demo_app/app.py', old=_b("f7b3f7cfe2198326b7a225abd8250269c47cbc9b"), new=_b("69e932186d6aebf1886c2afd0be77712d405c497"),
   why="sync demo_app/app.py to TRF 4d3ee63"),
]
