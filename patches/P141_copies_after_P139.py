# P141 — copies after P139/P140: viewer app.py synced to TRF 854b2a6 (R-43, Proposition 1 summary scoped), Appendix A copy, checksums. Blob-based.
import subprocess
_b = lambda sha: subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, text=True, check=True).stdout
LOST_OK = []
EDITS = [
 dict(id='P141-01', file='demo_app/app.py', old=_b("1b6015b3b45e4643a09c72e8437b48795e5b2f48"), new=_b("ee968c22fa5411e057502dc016894b1c61eda984"), why="viewer copy synced to TRF 854b2a6 (R-43)"),
 dict(id='P141-02', file='repro_package/docs/Appendix_A.md', old=_b("89314a139f3bd66b3b3e1293ecaa397eb932fefc"), new=_b("649580f9c1aba2714f9788c6fa011a477c6140c6"), why="copy of Appendix A after P139"),
 dict(id='P141-03', file='CHECKSUMS.md', old=_b("8b2a02f4b425c9cabc6a6bc9fa0eda7e4a65481e"), new=_b("13472c245d26c5b3ae8941b5adce82c53abc3b45"), why="checksums"),
]
