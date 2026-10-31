# P99 — cite TRF release 1.1.0 through the Zenodo concept DOI 10.5281/zenodo.23819274 (read from the Zenodo API,
# 31 Oct; resolves to the latest version), so the archived viewer matches the eleven pages A.1 describes
# (RT2 consistency M4, examiner m-4). Result modules are unchanged since 1.0.1 (DOI 10.5281/zenodo.23819275).
# app.py is now 1122 lines (walk navigation, quote sync); A.14 still said 825.
LOST_OK = ["number 23819275", "number 1.0.1", "number 1108", "number 825"]
EDITS = [
 dict(id='P99-01', file='code_artefacts/README_Appendix_A.md',
  old=r"""| Archived release (cite this) | Version 1.0.1, Zenodo, https://doi.org/10.5281/zenodo.23819275 |""",
  new=r"""| Archived release (cite this) | Version 1.1.0, Zenodo, https://doi.org/10.5281/zenodo.23819274 (resolves to the latest version; version 1.0.1, https://doi.org/10.5281/zenodo.23819275, has the same result modules) |""",
  why="M4: cite the release that contains the viewer A.1 describes"),
 dict(id='P99-02', file='code_artefacts/README_Appendix_A.md',
  old=r"""version 1.0.1 of the repository, deposited on Zenodo, is the exact code whose outputs this thesis reports,""",
  new=r"""version 1.1.0 of the repository, deposited on Zenodo, is the exact code whose outputs this thesis reports and the viewer described below, and its result modules are identical to those of version 1.0.1,""",
  why="M4"),
 dict(id='P99-03', file='code_artefacts/README_Appendix_A.md',
  old=r"""never a source of results | 1108 + 133 |""",
  new=r"""never a source of results | 1122 + 133 |""",
  why="A.2 line count"),
 dict(id='P99-04', file='code_artefacts/README_Appendix_A.md',
  old=r"""`app.py` (825 lines) holds the pages""",
  new=r"""`app.py` (1122 lines) holds the pages""",
  why="examiner m-4: A.14 line count"),
 dict(id='P99-05', file='Chapter5_Demonstration_v1.md',
  old=r"""| `app.py`, `ui.py` | 1108 + 133 | Eleven-page viewer""",
  new=r"""| `app.py`, `ui.py` | 1122 + 133 | Eleven-page viewer""",
  why="Table 5.1 line count"),
 dict(id='P99-06', file='Front_Matter_v1.md',
  old=r"""(archived release 1.0.1: https://doi.org/10.5281/zenodo.23819275)""",
  new=r"""(archived release 1.1.0: https://doi.org/10.5281/zenodo.23819274)""",
  why="abstract footer cites the concept DOI and release 1.1.0"),
]
