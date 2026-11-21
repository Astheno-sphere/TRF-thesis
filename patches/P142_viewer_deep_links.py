# P142 — viewer copy synced to TRF e2d342a (R-45): deep links ?p, ?r, ?m for the defence deck. Blob-based.
import subprocess
_b = lambda sha: subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, text=True, check=True).stdout
LOST_OK = ['number 1126']  # app.py line count in CHECKSUMS: 1126 -> 1148
EDITS = [
 dict(id='P142-01', file='demo_app/app.py', old=_b("ee968c22fa5411e057502dc016894b1c61eda984"), new=_b("26ddf2bb912fb7a53e8e904dfa22552ba2025e92"), why="viewer copy synced to TRF e2d342a (R-45, deck deep links)"),
 dict(id='P142-02', file='CHECKSUMS.md', old=_b("13472c245d26c5b3ae8941b5adce82c53abc3b45"), new=_b("28160c312bb5afb617c3e55f84535db3f4b51071"), why="checksums"),
]
