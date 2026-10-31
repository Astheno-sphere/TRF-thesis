# Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the EHDS

MSc thesis, Sustainable Energy Logistics, Høgskolen i Molde (2026) · Arshad Akhtar Abbasia · Supervisor: Prof. João Ferreira

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23819274.svg)](https://doi.org/10.5281/zenodo.23819274) · **Live demonstration:** https://trfhimolde.streamlit.app/ · **Code:** https://github.com/Astheno-sphere/TRF

## The problem
One cross-border health audit record is bound by three obligations at once: a retention floor (keep it verifiable), the GDPR Article 17 right to erasure, and the six-month deletion ceiling of EHDS Article 68(12). No instrument reconciles them.

## The result
- **Proposition 1:** if *verifiable* means *readable*, the three cannot be met together whenever a deadline falls inside the retention window.
- **Proposition 2:** if *verifiable* means *accountable* (who acted, when, a commitment, a logged invalidation entry), they can always be met together.
- **Propositions 3–4:** a ceiling collides with a floor only if it is no longer than the floor, and its anchor decides whether the collision is visible; relocating a record meets the ceiling but not the right.
- **Mechanism:** Crypto-Erasure by Invalidation, placed at the NCPeH audit repository and the SPE access-logging boundary, analysed against Norwegian infrastructure.

Bounded by design: no new cryptographic primitive, informal proofs checked by code and a bounded Z3 check, synthetic data, key destruction attested not proven, residue pseudonymised not anonymous.

## Read
| What | Where |
|---|---|
| Full thesis (Word) | [`VERA-SNARK_Thesis_SUBMISSION.docx`](VERA-SNARK_Thesis_SUBMISSION.docx) |
| Full thesis (one file) | [`VERA-SNARK_Thesis_SUBMISSION.md`](VERA-SNARK_Thesis_SUBMISSION.md) |
| Chapters | [Front](Front_Matter_v1.md) · [1](Chapter1_Introduction_v2.md) · [2](Chapter2_LitReview_v2_FINAL.md) · [3](Chapter3_Methodology_v1.md) · [4](Chapter4_TRF_Model_v1.md) · [5](Chapter5_Demonstration_v1.md) · [6](Chapter6_Discussion_v1.md) · [7](Chapter7_Conclusion_v1.md) · [App. A](code_artefacts/README_Appendix_A.md) |
| Adversarial review | [`RED_TEAM.md`](RED_TEAM.md), [`red_team_round2/`](red_team_round2/) |

## Reproduce
```bash
git clone https://github.com/Astheno-sphere/TRF && cd TRF
python3 trf_checker.py          # Semantics I: 95 violations / 90 of 200 records; Semantics II: 0
python3 -m pytest -q tests/     # 23 checks, incl. every Chapter 5 figure
```

## How this repository is kept
Every change to the thesis text goes through a gated patch (`patches/`, `handoff_tools/patch.py`): citations, numbers, legal articles and hedges cannot change silently, and every cross-reference is re-checked (`handoff_tools/concordance.py`). Each edit is logged in `CHANGE_TRAIL.md`. AI assistance is declared in the Front Matter.
