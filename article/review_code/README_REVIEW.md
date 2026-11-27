# Code archive for review

Purpose: executable artefact accompanying the submitted article. It reproduces every
reported result from deterministic code. Authorship and institutional details are
withheld for double-anonymised review.

Python: 3.11 or later (tested on 3.12 and 3.13).

    pip install -r requirements.txt
    python3 -m pytest -q
    python trf_checker.py
    python sensitivity.py > sens.txt
    diff sens.txt docs/expected_sensitivity_output.txt     # must print nothing
    python sensitivity_secondary.py > sec.txt
    diff sec.txt docs/expected_secondary_output.txt        # must print nothing

Where each reported result comes from:

| Article | Script |
|---|---|
| Fig. 1, Section 5.2 baseline counts (95 / 90, 138 invalidations) | `trf_checker.py` |
| Table 3 and Fig. 3 (floors 120 / 72 / 36, ceiling applies / excluded) | `sensitivity.py` |
| Section 5.2 secondary-use counts, five-year floor, endpoint convention, permit labels | `sensitivity_secondary.py` |
| Section 5.1 Synthea payload comparison | `synthea_layer.py` |
| Propositions 1 and 2 counterexample search | `z3_check.py` |
| Supporting checks (Norwegian scenario, cross-sector, key envelope) | `norwegian_layer.py`, `cross_sector_check.py`, `crypto_envelope.py` |

Other recorded runs: each `docs/expected_*.txt` is the console output of the
corresponding module, reproduced byte for byte by `pytest -q`.

Data: synthetic only. The Synthea FHIR bundles in `data/synthea_subset/` are generated
synthetic patients (generator seed 20260915); no real patient data is included.
Provenance: `docs/Data_Provenance_Statement.md`.

Note: the interactive viewer of the original archive is omitted from this review copy; `streamlit` in requirements.txt is not needed to reproduce the results;
the checker modules use the standard library, plus `cryptography` and `z3-solver`
for the optional cross-checks.
