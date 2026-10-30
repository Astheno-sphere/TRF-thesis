# P89 — cite the archived artefact release (closes P-22 / O-08 / NEXT_SESSION §G "Zenodo DOI").
# GitHub release v1.0.1 of Astheno-sphere/TRF (commit 0ad3865; code identical to v1.0.0 at ddd4041,
# only CITATION.cff/.zenodo.json version fields differ) archived on Zenodo 30 Oct 2026:
# DOI 10.5281/zenodo.23819275, record https://zenodo.org/records/23819275.
# The thesis previously cited a moving `main`; A.1 now names the frozen release as the citable artefact.
EDITS = [
 dict(id='P89-01', file='code_artefacts/README_Appendix_A.md',
   old=r"""| Source repository | https://github.com/Astheno-sphere/TRF |
| Live demonstration | https://trfhimolde.streamlit.app/ |""",
   new=r"""| Archived release (cite this) | Version 1.0.1, Zenodo, https://doi.org/10.5281/zenodo.23819275 |
| Source repository | https://github.com/Astheno-sphere/TRF |
| Live demonstration | https://trfhimolde.streamlit.app/ |""",
   why="A.1: add the Zenodo DOI of the frozen release"),
 dict(id='P89-02', file='code_artefacts/README_Appendix_A.md',
   old=r"""The repository is the citable artefact. It contains""",
   new=r"""The archived release is the citable artefact: version 1.0.1 of the repository, deposited on Zenodo, is the exact code whose outputs this thesis reports, whereas the repository's default branch may change after submission. It contains""",
   why="A.1: replace the moving-branch citation with the frozen release"),
 dict(id='P89-03', file='Front_Matter_v1.md',
   old=r"""Artefact: https://github.com/Astheno-sphere/TRF. Demonstration: https://trfhimolde.streamlit.app/""",
   new=r"""Artefact: https://github.com/Astheno-sphere/TRF (archived release 1.0.1: https://doi.org/10.5281/zenodo.23819275). Demonstration: https://trfhimolde.streamlit.app/""",
   why="Abstract footer: add the DOI next to the repository link"),
]
