# P130 — whipper round 2: Table A.2 placeholders (P125 turned the em dash into a colon), note on the project name moved
# into the Statement of Contribution (it spilled onto a page of its own). Blob-based.
import subprocess
_b = lambda sha: subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, text=True, check=True).stdout
LOST_OK = []
EDITS = [
 dict(id='P130-01', file='code_artefacts/README_Appendix_A.md', old=_b("3e380e25251960c48c82b3d997d037b6793fc1aa"), new=_b("f71661e060d6e0cb3394465f80cb14fe120d9bba"), why="A.2 Lines column: n/a, not a stray colon (P125 dash replacement)"),
 dict(id='P130-02', file='repro_package/docs/Appendix_A.md', old=_b("3e380e25251960c48c82b3d997d037b6793fc1aa"), new=_b("f71661e060d6e0cb3394465f80cb14fe120d9bba"), why="copy of Appendix A"),
 dict(id='P130-03', file='Front_Matter_v1.md', old=_b("f98835ad262dd8f34c140d164ad8433bc28cc978"), new=_b("c2b389047fd49c5b6fc41dfcb2590d6238543e5c"), why="note on the project name moved into the Statement of Contribution"),
 dict(id='P130-04', file='CHECKSUMS.md', old=_b("4c85dfd3845961c34fc0dc91931aa532fe880901"), new=_b("3edf95f08972164325b8b01bcfaeabb7ef072d01"), why="checksums"),
]
