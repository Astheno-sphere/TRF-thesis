# P23 — optional real-cryptography module (Tiger, 3 Oct: "go ahead"). crypto_envelope.py encrypts
# every record under its own AES-256-GCM data key, wraps the keys under a key-encrypting key in a
# custody object, destroys the wrapped key at each record's invalidation month, and shows that
# exactly the invalidated records become unreadable. The new files (three copies of the module,
# results/crypto_envelope_output.txt) are added beside this patch (trail B-28); this patch wires
# them in. The checker and every reported figure are unchanged; the module reports no thesis figure.
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from frozen import freeze, at
PRE = "fa43b08"   # commit before P23
ROOT = pathlib.Path(__file__).resolve().parent.parent
A, C5, C4, RUN, REQ = ("code_artefacts/README_Appendix_A.md", "Chapter5_Demonstration_v1.md", "Chapter4_TRF_Model_v1.md",
                       "repro_package/run_all.sh", "repro_package/requirements.txt")


def compute():
    src = (ROOT / "demo_app/crypto_envelope.py").read_text(encoding="utf-8")
    out = (ROOT / "repro_package/results/crypto_envelope_output.txt").read_text(encoding="utf-8")
    n = len(src.splitlines())
    full = at(PRE, A)
    TAIL = full[full.index("## A.11b Console output"):]   # unique: from the last section to the end
    return [
        dict(id="P23-01", file=RUN,
             old='echo\necho "-----------------------------------------------------------------------"\necho "Now diff each rerun against its recorded run. All five should be identical;"',
             new='echo\necho "=== 5/5  Envelope encryption with real AES-256-GCM (optional; needs the cryptography package) ==="\n'
                 'if python3 -c "import cryptography" 2>/dev/null; then\n'
                 '  python3 crypto_envelope.py | tee results/crypto_envelope_rerun.txt\n'
                 'else\n'
                 '  echo "skipped: pip install cryptography to run it; no thesis figure depends on it"\n'
                 'fi\n\n'
                 'echo\necho "-----------------------------------------------------------------------"\necho "Now diff each rerun against its recorded run. All six should be identical;"',
             why="new optional step"),
        dict(id="P23-02", file=RUN,
             old='echo "  diff results/cross_sector_rerun.txt          results/expected_cross_sector_output.txt"',
             new='echo "  diff results/cross_sector_rerun.txt          results/expected_cross_sector_output.txt"\necho "  diff results/crypto_envelope_rerun.txt       results/crypto_envelope_output.txt"',
             why="diff line for the new run"),
        dict(id="P23-03", file=RUN,
             old='echo "against all 98 bundles. It differs from the subset run in two lines only, the"\necho "bundle count and the mean payload. Diff the two against each other to see that"',
             new='echo "against all 98 bundles, recorded on 28 September 2026 before the constructed"\necho "payloads were revised. Besides the bundle count and the mean payloads, no line"\necho "differs from the subset run. Diff the two against each other to see that"',
             why="the full-cohort file is historical (P12/P13)"),
        dict(id="P23-04", file=REQ, old="openpyxl>=3.1",
             new="openpyxl>=3.1\n#\n# The optional envelope-encryption module (crypto_envelope.py) requires:\ncryptography>=42",
             why="dependency of the optional module only"),
        dict(id="P23-05", file=A,
             old="| `app.py` | Five-tab demonstration viewer over the artefact, never a source of results | 530 |",
             new=f"| `app.py` | Five-tab demonstration viewer over the artefact, never a source of results | 530 |\n| `crypto_envelope.py` | Optional: the same lifecycle with real AES-256-GCM envelope encryption; needs the `cryptography` package and reports no thesis figure | {n} |",
             why="contents table"),
        dict(id="P23-06", file=A, old="```\n\n---\n\n## A.10 Console output of the reported run",
             new="```\n\n---\n\n## A.9e Source listing: `crypto_envelope.py`\n\nThe optional envelope-encryption module. Each record's payload is encrypted under its own AES-256-GCM data key; the data keys are wrapped under a key-encrypting key held in a custody object standing in for a hardware security module; at each record's invalidation month the wrapped key is destroyed; every record is then decrypted again. It is the only module with a dependency outside the standard library. Line count: " + str(n) + ".\n\n```python\n" + src + "```\n\n---\n\n## A.10 Console output of the reported run",
             why="new listing"),
        dict(id="P23-07", file=A, old=TAIL,
             new=TAIL + "\n\n---\n\n## A.15 Console output of the envelope-encryption module\n\nVerbatim output of `python3 crypto_envelope.py`. Keys are random on every run; the counts are the same on every run. All 200 records decrypt before invalidation; after the 138 data keys due for destruction are destroyed, those 138 records are refused and the other 62 still read, and the ciphertext of an invalidated record opens under none of the surviving keys.\n\n```text\n" + out + "```\n",
             why="new console output"),
        dict(id="P23-08", file=C5, old="| `app.py` | 530 | Five-tab viewer over the artefact; never a source of results | No |",
             new="| `app.py` | 530 | Five-tab viewer over the artefact; never a source of results | No |\n| `crypto_envelope.py` | " + str(n) + " | Optional: the same lifecycle with real AES-256-GCM envelope encryption (needs `cryptography`) | No |",
             why="Table 5.0a row"),
        dict(id="P23-09", file=C5,
             old="Key destruction is simulated by removing a reference in program state, which demonstrates the mechanism's logic and demonstrates nothing whatever about whether key destruction can be assured in deployment",
             new="Key destruction is simulated by removing a reference in program state, which demonstrates the mechanism's logic and demonstrates nothing whatever about whether key destruction can be assured in deployment. An optional module repeats the lifecycle with real AES-256-GCM envelope encryption (Appendix A, A.9e and A.15): after the 138 scheduled destructions exactly those records refuse to decrypt and the other 62 still read, so unreadability is executed rather than asserted; the keys are still destroyed in program memory, not in hardware",
             why="optional module reported where the limitation is stated"),
        dict(id="P23-10", file=C4,
             old="| Key destruction renders copies the store cannot delete at once unrecoverable | §4.8 *Ciphertext* | Met by specification; key destruction simulated (§4.9, §6.3) |",
             new="| Key destruction renders copies the store cannot delete at once unrecoverable | §4.8 *Ciphertext*; `crypto_envelope.py` | Met in the optional module with real AES-256-GCM (138 of 138 refused); destruction in program memory, not hardware (§4.9, §6.3) |",
             why="Table 4.1 OPR-6 row reflects the executed check"),
    ]


EDITS = freeze("P23_crypto_envelope", compute)
