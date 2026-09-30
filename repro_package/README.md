# Reproducibility Package

**Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the European Health Data Space**
Arshad Akhtar Abbasia · MSc Sustainable Energy Logistics, Høgskolen i Molde · Supervisor: Prof. João Ferreira

This package reproduces every numerical result reported in the thesis. It is self-contained, has no third-party dependencies for the results that matter, and runs in under a second.

---

## Availability

| Form | Location |
|---|---|
| Source repository | https://github.com/Astheno-sphere/TRF |
| Live demonstration | https://trfhimolde.streamlit.app/ |

## Quick start

```bash
./run_all.sh
```

Or, for the load-bearing result alone:

```bash
python3 src/trf_checker.py
```

Requires Python 3 and nothing else. Java 17+ is needed only if you choose to regenerate the full Synthea cohort.

---

## What you should see

The checker prints a table of violations under each semantics and ends with:

```
RESULT  Semantics I : 95 violations across 90 records  -> INFEASIBLE
RESULT  Semantics II: 0 violations across 0 records  -> FEASIBLE
```

If your run produces different numbers, something is wrong — the run is deterministic under seed 20260915 and should be byte-identical to `results/trf_output.txt` on any machine.

---

## Contents

```
run_all.sh                    Reproduces everything; tees output to results/
requirements.txt              Empty for the thesis results; openpyxl for the bookkeeping scripts
trf_checker.py                Feasibility checker — Theorems 1 and 2, plus the independent
                              exhaustive cross-check over all 2^14 accessibility assignments
synthea_layer.py              Realism layer — swaps in real FHIR R4 payloads and compares
                              every reported figure against the constructed-payload run
norwegian_layer.py            Norwegian context classes, parallel to the thesis
cross_sector_check.py         Cross-sector instance, politiregisterloven § 17
data/synthea_subset/          Eight untrimmed Synthea bundles from the reported cohort, so the
                              realism layer runs without regenerating all 98
results/trf_output.txt        Captured console output of the reported run
results/synthea_comparison_subset_output.txt      Payload-provenance comparison, 8-bundle subset
results/synthea_comparison_full_cohort_output.txt  The same comparison, all 98 bundles
docs/Appendix_A.md            Full appendix: commands, provenance, integrity record, limitations
src/                          Bookkeeping scripts for the research substrate; no thesis result
                              depends on them
```

---

## Integrity record

Every number below was produced by the code in `src/` and appears in the thesis at the section indicated. This table is the contract between the document and the artefact.

| Result | Value | Thesis location |
|---|---|---|
| Semantics I — records with ≥1 violation | 90 / 200 | Table 5.1 |
| Semantics I — total violations | 95 | §5.3 |
| Violation decomposition | 41 C2-only, 44 C3-only, 5 both | §5.3 |
| Corollary 1.2 witnesses (no erasure request) | 39 | §5.4 |
| Exhaustive cross-check, three conflict cases | no satisfying assignment | Table 5.2 |
| Exhaustive cross-check, control case | satisfying assignment exists | Table 5.2 |
| Semantics II — records invalidated | 138 (52 Art. 17, 86 Art. 68(12)) | Table 5.3 |
| Semantics II — total violations | 0 | Table 5.3 |
| Synthea comparison — figures changed | none | Table 5.4 |
| Synthea comparison — commitments changed | 200 / 200 | Table 5.4 |
| Reference commitment, record 100 | `11087780fd192c8f…` | §5.6 |
| Runtime, full run | 0.019 s | §5.7 |

The reference commitment is the fastest single check: if it matches, your run is the reported run.

---

## Regenerating the Synthea cohort

The full cohort is 314 MB and is not distributed here. It is deterministic and regenerable:

```bash
curl -sL -o synthea.jar \
  https://github.com/synthetichealth/synthea/releases/download/master-branch-latest/synthea-with-dependencies.jar

mkdir -p synthea_run && cd synthea_run
java -jar ../synthea.jar \
  -s 20260915 -cs 20260915 -p 100 \
  --exporter.fhir.export=true \
  --exporter.hospital.fhir.export=false \
  --exporter.practitioner.fhir.export=false \
  --generate.only_alive_patients=true
```

This yields 98 usable patient bundles. Both the population seed (`-s`) and the clinician seed (`-cs`) are fixed to the thesis seed.

---

## Data statement

All data are synthetic and describe no real individual. No real patient data was requested, obtained, or processed at any stage of this research.

Synthea's default export conforms to the **US Core** implementation guide with United States demographic and care-pattern parameters. The FHIR version is **R4**, matching the version the Norwegian basisprofiler constrain, but the profiles are not Norwegian and no claim of Norwegian clinical representativeness is made for these records. The comparisons in `results/synthea_comparison_subset_output.txt` and `results/synthea_comparison_full_cohort_output.txt` establish why this cannot affect any result: no constraint in the model reads payload content, so substituting real FHIR resources changes every commitment and no reported figure.

---

## What this package does not contain

Stated so that nothing is inferred from silence:

- No deployed system. The checker connects to no National Contact Point and implements no part of the OpenNCP transmission flow.
- No performance benchmark. The runtime figure indicates only that reproduction is cheap.
- No cryptographic library. Commitments use `hashlib`; key destruction is modelled as removing a reference in program state and says nothing about deployment assurance.
- No accumulator implementation. Accumulator-based validity witnesses are specified in Chapter 4 as an efficiency and verifiability layer and were deliberately not built; neither theorem depends on them.
- No zero-knowledge proof system. None is required by the mechanism, and none is claimed anywhere in the thesis.

---

## Licence and citation

Code is released for academic scrutiny and reuse. If you use it, please cite the thesis.

The salts in `trf_checker.py` are derived deterministically from record identifiers so that runs reproduce exactly. **A production deployment must use a cryptographically secure random source** (`os.urandom`); the code says so at the point where it matters.
