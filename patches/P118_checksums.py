# P118 — CHECKSUMS.md regenerated after the final code sync of P115 (44 files). Blob-based.
import subprocess
_b = lambda sha: subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, text=True, check=True).stdout
LOST_OK = ["number 110", "number 1124", "number 133", "number 135", "number 154", "number 1851", "number 28", "number 585", "number 8"]   # superseded md5s and line counts
EDITS = [
 dict(id='P118-01', file='CHECKSUMS.md', old=_b("9595134037f30d65581461222afe448b32870de6"), new=_b("43f94da8da80752a6bde6b192a95b34d928b0411"), why="checksums at the final code"),
]
