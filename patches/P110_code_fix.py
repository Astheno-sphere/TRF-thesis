# P110 — trf_checker exit status moved after the --delta-witness block (P107 had exited before it; caught by the
# recorded-output test), copies synced; Appendix A.2 rows: line counts, the new cross-check test, pinned requirements.
import subprocess
_b = lambda sha: subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, text=True, check=True).stdout
LOST_OK = ["number 551", "number 118", "number 153", "number 1.50", "number 42", "number 4.12"]
EDITS = [
 dict(id='P110-01', file='demo_app/trf_checker.py', old=_b("d1a13aba57a223f149f34de63e413143eb93ba21"), new=_b("ed919db9c4441734e6a87a0439d1bc57ff8acc34"), why="exit status set after the optional delta witness"),
 dict(id='P110-02', file='repro_package/trf_checker.py', old=_b("d1a13aba57a223f149f34de63e413143eb93ba21"), new=_b("ed919db9c4441734e6a87a0439d1bc57ff8acc34"), why="exit status set after the optional delta witness"),
 dict(id='P110-03', file='code_artefacts/trf_checker.py', old=_b("d1a13aba57a223f149f34de63e413143eb93ba21"), new=_b("ed919db9c4441734e6a87a0439d1bc57ff8acc34"), why="exit status set after the optional delta witness"),
 dict(id='P110-04', file='code_artefacts/README_Appendix_A.md',
  old=r"""including the independent exhaustive cross-check and the audit-log integrity check | 551 |""",
  new=r"""including the exhaustive cross-check and the audit-log integrity check; exits non-zero if Semantics II reports any violation | 557 |""", why="A.2"),
 dict(id='P110-05', file='code_artefacts/README_Appendix_A.md',
  old=r"""needs the `cryptography` package and reports no thesis figure | 118 |""",
  new=r"""needs the `cryptography` package and reports no thesis figure; exits non-zero on a mismatch | 122 |""", why="A.2"),
 dict(id='P110-06', file='code_artefacts/README_Appendix_A.md',
  old=r"""bounded SMT check of Propositions 1–3 with the Z3 solver; needs the `z3-solver` package | 153 |""",
  new=r"""bounded SMT check of Propositions 1–3 with the Z3 solver; needs the `z3-solver` package; exits non-zero if any check, the sanity check or a mutation check fails | 155 |""", why="A.2"),
 dict(id='P110-07', file='code_artefacts/README_Appendix_A.md',
  old=r"""| `tests/test_app.py`, `.github/workflows/tests.yml` | Automated checks run on every change: every recorded run reproduces byte for byte, every viewer page renders, and the viewer's claim ledger matches Chapter 5; they report no thesis figure |""",
  new=r"""| `tests/test_app.py`, `tests/test_props.py`, `.github/workflows/tests.yml` | Automated checks run on every change: every recorded run reproduces byte for byte, every viewer page renders, the viewer's claim ledger matches Chapter 5, and the exhaustive cross-check agrees with the checker on 31 cases including every boundary month of a twelve-month window; they report no thesis figure |""", why="A.2: test_props.py"),
 dict(id='P110-08', file='code_artefacts/README_Appendix_A.md',
  old=r"""| `requirements.txt` | `streamlit>=1.50`, `cryptography>=42`, `z3-solver>=4.12`; the checker itself needs nothing | 3 |""",
  new=r"""| `requirements.txt` | Pinned to the tested versions: `streamlit==1.66.1`, `cryptography==50.0.1`, `z3-solver==5.3.3.0`; the checker itself needs nothing | 3 |""", why="A.2: pinned"),
]
