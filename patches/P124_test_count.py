# P124 — test count 55 -> 56 in demo_app/README.md and repro_package/README.md (test_props added); CHECKSUMS.md regenerated. Blob-based.
import subprocess
_b = lambda sha: subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, text=True, check=True).stdout
LOST_OK = ['number 55']   # superseded test count
EDITS = [
 dict(id='P124-01', file='demo_app/README.md', old=_b("236f1489e280007ef35437244ec188c0693d8290"), new=_b("00eb267baa7399c8fd9362f260f879467a601df9"), why="test count 56"),
 dict(id='P124-02', file='repro_package/README.md', old=_b("a898917fc3a97cb057704f10779bf32236179049"), new=_b("5b979989d462f5a232178dbd5a1062f3d8ee22f2"), why="test count 56"),
 dict(id='P124-03', file='CHECKSUMS.md', old=_b("15d824efbbfe0032525567e4eb0c00c4d01b05e0"), new=_b("466f4afb41bb56dc62c47bb0119d065ebcdac29b"), why="test count 56"),
]
