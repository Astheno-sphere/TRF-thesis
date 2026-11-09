# P129 — typesetting fixes in the source from whipper round 1: nomenclature symbols written as math (raw underscores
# printed), m_acc/m_subj subscripts upright, a spaced "or" in a display equation, Table B.1 caption punctuation. Blob-based.
import subprocess
_b = lambda sha: subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, text=True, check=True).stdout
LOST_OK = []
EDITS = [
 dict(id='P129-01', file='Front_Matter_v1.md', old=_b("4d588a18eda7e6cff06c93c01c500a5b68ab07ad"), new=_b("f98835ad262dd8f34c140d164ad8433bc28cc978"), why="nomenclature symbols as math, as in the body"),
 dict(id='P129-02', file='Chapter4_TRF_Model_v1.md', old=_b("79df7c5050abcb7de581abc49d9005bce9d120d6"), new=_b("a2361df4ae2e1ce5a5b87a9be3addf4366263f52"), why="upright multi-letter subscripts; spaced 'or' in the display"),
 dict(id='P129-03', file='Appendix_B_Search_Log.md', old=_b("4eaabfb7eb558a4289931aed30d5149172fa63c3"), new=_b("d3855881b92b31236f83d4b96dc58cbc76abcdc2"), why="caption punctuation as in the other tables"),
]
