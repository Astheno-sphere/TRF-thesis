# P120 — the thesis cites release 1.3.0 (Zenodo 10.5281/zenodo.23989242, archived 6 Nov 2026, API-read), the code
# Appendix A reproduces after the code review (P115 to P119). Concept DOI unchanged.
LOST_OK = ["number 1.2.0", "number 23827275", "number 1.1.0"]
EDITS = [
 dict(id='P120-01', file='Front_Matter_v1.md',
  old=r"""(archived release 1.2.0: https://doi.org/10.5281/zenodo.23827275;""",
  new=r"""(archived release 1.3.0: https://doi.org/10.5281/zenodo.23989242;""", why="release 1.3.0"),
 dict(id='P120-02', file='code_artefacts/README_Appendix_A.md',
  old=r"""| Archived release (cite this) | Version 1.2.0, Zenodo, https://doi.org/10.5281/zenodo.23827275 (this version) and https://doi.org/10.5281/zenodo.23819274 (all versions, resolving to the latest); versions 1.0.1 and 1.1.0 produce the same figures |""",
  new=r"""| Archived release (cite this) | Version 1.3.0, Zenodo, https://doi.org/10.5281/zenodo.23989242 (this version) and https://doi.org/10.5281/zenodo.23819274 (all versions, resolving to the latest); versions 1.0.1 to 1.2.0 produce the same figures |""", why="release 1.3.0"),
 dict(id='P120-03', file='code_artefacts/README_Appendix_A.md',
  old=r"""version 1.2.0 of the repository, deposited on Zenodo, is the exact code whose outputs this thesis reports and the viewer described below; its result modules produce the same figures as versions 1.0.1 and 1.1.0 and differ from them only in comments, exit codes and one printed line of the optional encryption module,""",
  new=r"""version 1.3.0 of the repository, deposited on Zenodo, is the exact code whose outputs this thesis reports and the viewer described below; its result modules produce the same figures as versions 1.0.1 to 1.2.0 and differ from them in the corrections of the code review (an audit log per population, fuller exit codes, two reworded output lines), recorded in `CODE_REVIEW.md` of the thesis repository,""", why="release 1.3.0"),
]
