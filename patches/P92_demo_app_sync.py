# P92 — log the sync of demo_app/app.py to TRF 46a3fcd (the examiner's walk: Start here,
# The four propositions, Claim ledger; Thesis run on open). P91 copied it without logging;
# this records the edit in the md5 chain. Contents are taken from git blobs, so the patch
# replays deterministically: old = blob bdcfd40701e0754974e50e73cc6aa2965dda774e, new = blob 4ae07fdee0556b37435e4457369cff2d1f83c9d4.
import subprocess
_b = lambda sha: subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, text=True, check=True).stdout
EDITS = [
 dict(id='P92-01', file='demo_app/app.py', old=_b("bdcfd40701e0754974e50e73cc6aa2965dda774e"), new=_b("4ae07fdee0556b37435e4457369cff2d1f83c9d4"),
   why="sync demo_app/app.py to TRF 46a3fcd (walk pages, claim ledger, thesis run on open)"),
]
