# P23b — run_all.sh step label: the existing steps read 1/4 .. 4/4, so the optional step is "5 (optional)", not "5/5".
EDITS = [dict(id="P23b-01", file="repro_package/run_all.sh",
              old='echo "=== 5/5  Envelope encryption with real AES-256-GCM (optional; needs the cryptography package) ==="',
              new='echo "=== 5 (optional)  Envelope encryption with real AES-256-GCM; needs the cryptography package ==="',
              why="label consistent with steps 1/4 to 4/4")]
