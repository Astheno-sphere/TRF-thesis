# Reproducibility Package

**Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the European Health Data Space**
Arshad Akhtar Abbasia · MSc Sustainable Energy Logistics, Høgskolen i Molde · Supervisor: Prof. João Ferreira

This package reproduces every numerical result reported in the thesis. The checker and the realism layer need the Python standard library only.

---

## Which copy is which

| Folder in this repository | Holds | Use it to |
|---|---|---|
| `repro_package/` (this folder) | the result modules, the recorded runs in `results/`, the one copy of the Synthea subset in `data/` | reproduce the numbers with `./run_all.sh` |
| `demo_app/` | the same modules plus the viewer, its tests and the recorded runs in `docs/` | run the viewer and the 56 automated tests |
| `code_artefacts/` | the source files as Appendix A lists them | read the code beside the appendix |

The modules are byte-identical across the three folders and with the archived release. The citable artefact is the release on Zenodo: https://doi.org/10.5281/zenodo.23819274 (all versions).

## Availability

| Form | Location |
|---|---|
| Source repository | https://github.com/Astheno-sphere/TRF-thesis, branch `joao-base` |
| Live demonstration | https://trfhimolde.streamlit.app/ |

## Quick start

```bash
./run_all.sh
```

Or, for the load-bearing result alone:

```bash
python3 trf_checker.py
```

Python 3 (tested 3.11 to 3.13). Java 17 or later only if you regenerate the full Synthea cohort. The automated tests run from `demo_app/`:

```bash
cd ../demo_app && pip install -r requirements.txt pytest && python3 -m pytest -q tests/   # 56 passed
```

---

## What you should see

The checker ends with:

```
RESULT  Semantics I : 95 violations across 90 records  -> INFEASIBLE
RESULT  Semantics II: 0 violations across 0 records  -> FEASIBLE
```

It exits 0 only if Semantics II reports no violation. The run is deterministic under seed 20260915 and byte-identical to `results/trf_output.txt` on any machine; `run_all.sh` prints the diff commands.

---

## Contents

```
run_all.sh                 Reruns every module and tees output to results/*_rerun.txt
requirements.txt           Pinned optional packages (cryptography, z3-solver); none needed for the thesis results
trf_checker.py             Feasibility checker: Propositions 1 and 2, the exhaustive cross-check, the audit log
synthea_layer.py           Realism layer: swaps in Synthea FHIR R4 payloads and compares every figure
norwegian_layer.py         Norwegian context classes (illustrative; no thesis figure depends on them)
cross_sector_check.py      Cross-sector instance, politiregisterloven § 17 (illustrative)
crypto_envelope.py         AES-256-GCM envelope encryption (optional; needs cryptography)
z3_check.py                Bounded SMT check of Propositions 1 to 3 (optional; needs z3-solver)
data/synthea_subset/       Eight Synthea bundles from the reported cohort
results/                   Recorded runs (trf_output.txt and the others) and the reruns run_all.sh writes
docs/Appendix_A.md         The thesis's Appendix A: commands, provenance, listings, limitations
src/                       Bookkeeping scripts for the research substrate; no thesis result depends on them
```

---

## Integrity record

Every value below is printed by the code in this folder (`results/trf_output.txt` unless stated) and appears in the thesis where indicated.

| Result | Value | Thesis location |
|---|---|---|
| Semantics I, records with at least one violation | 90 / 200 (37 cross-border, 53 SPE) | Table 5.3 |
| Semantics I, total violations | 95 | §5.3 |
| Violation decomposition | 41 C2 only, 44 C3 only, 5 both | §5.3 |
| Corollary 1.2 witnesses (no erasure request) | 39 | §5.4 |
| Exhaustive cross-check, three conflict cases | no satisfying assignment | Table 5.4 |
| Exhaustive cross-check, control case | satisfying assignment exists | Table 5.4 |
| δ = 3 witness (`--delta-witness`) | see `results/expected_delta_witness_output.txt` | Table 5.5 |
| Semantics II, records invalidated | 138 (52 Art. 17, 86 Art. 68(12)) | Table 5.6 |
| Semantics II, total violations | 0 | Table 5.6 |
| Audit log, records verifying | 200 / 200; three tamper tests fail as they should | §5.7 |
| Synthea comparison, figures changed | none | Table 5.7 |
| Reference commitment, record 100 | `678ade47c1e6dc03…` | `results/trf_output.txt`, auditor view |

The reference commitment is the fastest single check: if it matches, your run is the reported run.

---

## Regenerating the Synthea cohort

The full cohort (98 bundles, about 314 MB) is not distributed here. Appendix A, A.5 gives the exact Synthea commit and command. The layer reads `synthea_run/output/fhir/` in preference to the subset. Against the subset the mean Synthea payload is 891 bytes; against the full cohort, 1,002 bytes (Chapter 5, Section 5.8). No other figure moves with cohort size.

---

## Data statement

All data are synthetic and describe no real individual. No real patient data was requested, obtained or processed at any stage.

Synthea's default export conforms to the US Core implementation guide with United States demographic and care-pattern parameters. The FHIR version is R4, the version the Norwegian basisprofiler constrain, but the profiles are not Norwegian and no claim of Norwegian clinical representativeness is made. No constraint in the model reads payload content, so substituting real FHIR resources changes every commitment and no reported figure.

---

## What this package does not contain

- No deployed system. The checker connects to no National Contact Point and implements no part of the OpenNCP transmission flow.
- No performance benchmark.
- No proof of key destruction. In the checker, destruction removes a reference in program state; in `crypto_envelope.py` the wrapped key leaves custody. Either way destruction is attested, not proven.
- No anchored log root. The Merkle log detects divergence between a record and its logged events; detecting a rewrite of the log itself needs a root published outside it (Chapter 6, Section 6.1).
- No accumulator implementation and no zero-knowledge proof system; neither proposition depends on them.

---

## Licence and citation

MIT. Cite release 1.3.0 (https://doi.org/10.5281/zenodo.23989242; all versions: https://doi.org/10.5281/zenodo.23819274) or the thesis.

The salts in `trf_checker.py` are derived from record identifiers so that runs reproduce exactly. A deployment must use a cryptographically secure random source (`--random-salts` uses `os.urandom`).
