# P131 — the thesis points to one repository: TRF-thesis, branch joao-base (code in demo_app/), alongside the Zenodo
# archive. The separate code repository stays the source of the archived release but is no longer the link given.
LOST_OK = []
EDITS = [
 dict(id='P131-01', file='Front_Matter_v1.md', old=r"""Artefact: https://github.com/Astheno-sphere/TRF (archived release 1.3.0:""", new=r"""Artefact: https://github.com/Astheno-sphere/TRF-thesis, branch `joao-base`, code in `demo_app/` (archived release 1.3.0:""", why="one repository link"),
 dict(id='P131-02', file='code_artefacts/README_Appendix_A.md', old=r"""| Source repository | https://github.com/Astheno-sphere/TRF |""", new=r"""| Source repository | https://github.com/Astheno-sphere/TRF-thesis, branch `joao-base` (code in `demo_app/`, reproduction package in `repro_package/`) |""", why="one repository link"),
 dict(id='P131-03', file='code_artefacts/README_Appendix_A.md', old=r"""Both files are in the repository (https://github.com/Astheno-sphere/TRF""", new=r"""Both files are in the repository (https://github.com/Astheno-sphere/TRF-thesis, `demo_app/`""", why="one repository link"),
]
