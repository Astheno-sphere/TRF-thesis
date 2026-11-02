# P114 — the thesis cites release 1.2.0 (Zenodo 10.5281/zenodo.23827275, archived 2 Nov 2026, API-read), the code
# Appendix A now reproduces (P107 to P111). Concept DOI unchanged.
LOST_OK = ["number 1.1.0", "number 23826911", "number 10.5281", "number 23819275"]
EDITS = [
 dict(id='P114-01', file='Front_Matter_v1.md',
  old=r"""(archived release 1.1.0: https://doi.org/10.5281/zenodo.23819274)""",
  new=r"""(archived release 1.2.0: https://doi.org/10.5281/zenodo.23827275; all versions: https://doi.org/10.5281/zenodo.23819274)""", why="release 1.2.0"),
 dict(id='P114-02', file='code_artefacts/README_Appendix_A.md',
  old=r"""| Archived release (cite this) | Version 1.1.0, Zenodo, https://doi.org/10.5281/zenodo.23826911 (this version) and https://doi.org/10.5281/zenodo.23819274 (all versions, resolving to the latest); version 1.0.1, https://doi.org/10.5281/zenodo.23819275, has the same result modules |""",
  new=r"""| Archived release (cite this) | Version 1.2.0, Zenodo, https://doi.org/10.5281/zenodo.23827275 (this version) and https://doi.org/10.5281/zenodo.23819274 (all versions, resolving to the latest); versions 1.0.1 and 1.1.0 produce the same figures |""", why="release 1.2.0"),
 dict(id='P114-03', file='code_artefacts/README_Appendix_A.md',
  old=r"""version 1.1.0 of the repository, deposited on Zenodo, is the exact code whose outputs this thesis reports and the viewer described below, and its result modules are identical to those of version 1.0.1,""",
  new=r"""version 1.2.0 of the repository, deposited on Zenodo, is the exact code whose outputs this thesis reports and the viewer described below; its result modules produce the same figures as versions 1.0.1 and 1.1.0 and differ from them only in comments, exit codes and one printed line of the optional encryption module,""", why="release 1.2.0"),
]
