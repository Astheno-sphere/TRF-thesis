# P122 — CHECKSUMS.md regenerated after P119 to P121. Blob-based.
import subprocess
_b = lambda sha: subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, text=True, check=True).stdout
LOST_OK = ["number 1125", "number 136"]   # superseded md5s and counts
EDITS = [
 dict(id='P122-01', file='CHECKSUMS.md', old=_b("43f94da8da80752a6bde6b192a95b34d928b0411"), new=_b("66ad3d10c91baa2741016b8029c2f458b0130f79"), why="checksums after the viewer sync"),
]
