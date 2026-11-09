# P127 — files outside the thesis text after the sync audit (9 Nov): run_all.sh footer, data provenance, repro README citation, checksums. Blob-based.
import subprocess
_b = lambda sha: subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, text=True, check=True).stdout
LOST_OK = ["number 1,006", "number 39", "number 70"]
EDITS = [
 dict(id='P127-01', file='repro_package/run_all.sh', old=_b("560e68f99147f670d46ff68a4033d363293ca1fc"), new=_b("07864eead1ef5c349413c07cb3cc0a480b996b20"), why="footer: the full-cohort record also differs in its result wording"),
 dict(id='P127-02', file='Data_Provenance_Statement.md', old=_b("7ff84385db785b8f5d9999d6a128587c503743e9"), new=_b("f2d51d3fa2d5ae33e567e5e20f1930fa0891ea6e"), why="1,002 bytes for the October cohort; subset 40 MB"),
 dict(id='P127-03', file='repro_package/README.md', old=_b("5b979989d462f5a232178dbd5a1062f3d8ee22f2"), new=_b("47df6fdc80d656a6ea6c9d0e36766955d024ce13"), why="cite release 1.3.0 with the all-versions DOI"),
 dict(id='P127-04', file='CHECKSUMS.md', old=_b("466f4afb41bb56dc62c47bb0119d065ebcdac29b"), new=_b("4c85dfd3845961c34fc0dc91931aa532fe880901"), why="checksums after P125 and the copies"),
]
