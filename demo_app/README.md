# TRF viewer and tests (mirror of the deployed app)

A viewer over the verified artefact of Chapter 5, with the automated tests. The hosted copy runs from the code repository, https://github.com/Astheno-sphere/TRF, at https://trfhimolde.streamlit.app/. This folder mirrors it so the viewer and the tests run from the thesis repository too.

**The app is never the authority.** The Thesis run page executes `trf_checker.py` unmodified under seed 20260915 and reproduces Tables 5.3 and 5.6; the Synthea realism page executes `synthea_layer.py` and reproduces Table 5.7. If a figure disagrees with the thesis, the page shows a red notice with the expected and the computed values instead of the result.

---

## Run the tests

```bash
pip install -r requirements.txt pytest
python3 -m pytest -q tests/        # 56 passed
```

The tests check that every recorded run in `docs/` reproduces byte for byte, that every page of the viewer renders, that the claim ledger matches Chapter 5, that the exhaustive cross-check agrees with the checker at every boundary month, and that the propositions and the "not claimed" paragraph the viewer quotes are verbatim from the thesis one folder up.

The realism layer reads the Synthea subset from `../repro_package/data/synthea_subset/`, the one copy kept in this repository.

## Run the viewer

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`. No Java needed. The interface loads its fonts from Google Fonts when online and falls back to system fonts offline.

---

## Before you present: one check

```bash
python3 synthea_layer.py
```

The line `payload bytes (mean)` must read 43 for the constructed payloads and 891 for the eight-bundle Synthea subset. With the full 98-bundle cohort the Synthea figure is 1,002 (Chapter 5, Section 5.8). No other figure changes with the cohort.

---

## Viva protocol, in order of preference

1. **Local run.** `streamlit run app.py` on your own machine. Do not depend on venue wifi.
2. **Hosted URL** as backup.
3. **Screen recording** of the Thesis run and Witness pages as the final fallback.

### What to say while the Thesis run page runs

Show the Corollary 1.2 witnesses rather than the headline counts. The counts show the code ran; the witnesses show the argument. Read one aloud: record created in month 7, permit expires in month 10, the ceiling requires deletion from month 16, the floor requires the record verifiable until month 19.

Then state the condition before anyone asks: this depends on Article 68(12) reaching the access logs and on the activity content being itself health data (Chapter 4, Section 4.6). Conceding the premise yourself is worth more than defending it under questioning.

---

## Known properties a code-reading examiner may raise

- **Payload sampling.** The realism layer takes the first clinical resource of each bundle and assigns payloads by `rid % len(payloads)`, so payloads repeat; no figure depends on payload content.
- **Deterministic salts.** Derived from the record id so that runs reproduce; they repeat with period 256. A deployment must use `os.urandom` (`--random-salts`).
- **Simulated key destruction.** Removing a reference in program state demonstrates the mechanism's logic, not deployment assurance: attested, not proven (Chapter 6, Section 6.3).
- **Audit log scope.** The log detects divergence between a record and its logged events. A rewrite of the log itself needs a root published outside it (Chapter 6, Section 6.1).
- **Semantics II.** C2 and C3 hold by construction once invalidation is applied; the part that can fail is C1, through the integrity check of every logged event (Chapter 5, Section 5.7).

---

## Files

```
app.py, ui.py           The viewer
trf_checker.py          The checker, unmodified from Appendix A
synthea_layer.py        The realism layer
norwegian_layer.py      Norwegian context classes (illustrative)
cross_sector_check.py   politiregisterloven § 17 instance (illustrative)
crypto_envelope.py      AES-256-GCM envelope encryption
z3_check.py             Bounded SMT check
assets/                 Diagrams the viewer embeds
docs/expected_*.txt     Recorded console runs the tests compare against
tests/                  The automated tests
requirements.txt        streamlit, cryptography, z3-solver, pinned to the tested versions
```
