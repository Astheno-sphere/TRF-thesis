# P132 — copies and checksums after P131 (one repository link: TRF-thesis, branch joao-base). Blob-based.
import subprocess
_b = lambda sha: subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, text=True, check=True).stdout
LOST_OK = []
EDITS = [
 dict(id='P132-01', file='repro_package/docs/Appendix_A.md', old=_b("f71661e060d6e0cb3394465f80cb14fe120d9bba"), new=_b("89314a139f3bd66b3b3e1293ecaa397eb932fefc"), why="copy of Appendix A after P131"),
 dict(id='P132-02', file='repro_package/README.md', old=_b("47df6fdc80d656a6ea6c9d0e36766955d024ce13"), new=_b("30e120e7fbf8cfb9ac36242c775a29966449dc26"), why="source repository: TRF-thesis, branch joao-base"),
 dict(id='P132-03', file='CHECKSUMS.md', old=_b("3edf95f08972164325b8b01bcfaeabb7ef072d01"), new=_b("d24c5fdf61db35c07d2f8ac489c79cdf0af0dfcc"), why="checksums"),
]
