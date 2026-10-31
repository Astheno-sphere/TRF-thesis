# P100 — sync demo_app/app.py to TRF 4b8942b (release 1.1.0: walk Previous/Next; Start page matches the corrected
# thesis text). Old blob 4ae07fdee0556b37435e4457369cff2d1f83c9d4, new blob f7b3f7cfe2198326b7a225abd8250269c47cbc9b (written to the object store), so the patch replays deterministically.
import subprocess
_b = lambda sha: subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, text=True, check=True).stdout
EDITS = [
 dict(id='P100-01', file='demo_app/app.py', old=_b("4ae07fdee0556b37435e4457369cff2d1f83c9d4"), new=_b("f7b3f7cfe2198326b7a225abd8250269c47cbc9b"),
   why="sync demo_app/app.py to TRF release 1.1.0"),
]
