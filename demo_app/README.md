# TRF Feasibility Checker — online demonstration

A viewer over the verified artefact of Chapter 5. Tab 1 executes `trf_checker.py` unmodified under seed 20260915 and reproduces Tables 5.1 to 5.3. Tab 3 executes `synthea_layer.py` unmodified and reproduces Table 5.4. Tab 2 varies population parameters and is explicitly outside the thesis claims.

**The app is never the authority.** If a figure here disagrees with the thesis, either the thesis text is wrong or the app is wrong. The artefact decides, not the viewer. Tab 1 enforces this in code: it asserts the run produced 95 violations, 39 Corollary 1.2 witnesses, and 0 violations under Semantics II, and displays a red failure banner rather than a result if it did not.

---

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Opens at `http://localhost:8501`. No Java required. No network required.

---

## Deploy online, free

**Streamlit Community Cloud** — the simplest route.

1. Push this folder to a public GitHub repository. Include `app.py`, `trf_checker.py`, `synthea_layer.py`, `requirements.txt`, and — for Tab 3 — the committed cohort at `synthea_run/output/fhir/`.
2. Go to `share.streamlit.io`, choose New app, select the repository, set the main file to `app.py`, deploy.

The cohort must be committed because the deployment host has no Java. That is by design: generation is an offline step, and committing the output makes the demonstration reproducible by anyone without a toolchain.

**Alternative:** Hugging Face Spaces, SDK Streamlit, same file layout.

### A note on repository size

The full 98-bundle cohort is roughly 314 MB, which exceeds what is comfortable in a Git repository. Two workable options:

- Commit a **subset** — twenty to thirty bundles is ample, since the layer draws one clinical resource per bundle and the invariance result does not depend on cohort size. State the subset size in Appendix A.
- Or commit the full cohort using Git LFS.

If you commit a subset, run `synthea_layer.py` locally against that same subset and confirm the six measures still match before deploying. They should: the payloads change, the timings do not.

---

## Before you present, one mandatory check

The mean payload figure quoted in Chapter 5, Section 5.7 and Chapter 6, Section 6.5 must be what this script actually prints against your committed cohort.

```bash
python3 synthea_layer.py
```

Read the line beginning `payload bytes (mean)`. Whatever number it shows for the Synthea side is the number the thesis quotes. If it prints 940, the thesis says 940. The constructed-side figure of 35 bytes has been verified; the Synthea-side figure is a property of your cohort and must be taken from the run, never carried over.

---

## Viva protocol, in order of preference

1. **Local run.** Clone the repository, `streamlit run app.py`, present from your own machine. Never depend on venue wifi.
2. **Online URL** as backup, in case the machine fails.
3. **Screen recording** of a complete Tab 1 and Tab 3 run as the final fallback, in case both fail.

Have all three ready. The demonstration is the strongest thing in the defence and it should not be the thing that breaks.

### What to say while Tab 1 runs

Show the Corollary 1.2 witnesses rather than the headline metrics. The metrics prove the code ran; the witnesses prove the argument. Read one aloud: record created in month 7, permit expires month 10, Article 68(12) requires the environment clear of personal data from month 16, Article 73(1)(e) requires the identifiable log verifiable to month 19. No data subject asked for anything.

Then state the interpretive condition before anyone asks: this depends on Article 68(12) reaching the access logs, which Chapter 4, Section 4.6 defends and marks contestable, and under the narrower reading these thirty-nine witnesses lapse while Theorem 1, Corollary 1.1, and every Semantics II result stand.

Conceding the weak joint yourself, in front of the examiner, is worth more than defending it under questioning.

---

## Known properties a code-reading examiner may raise

**Payload sampling.** The layer takes the first clinical resource from each bundle and assigns payloads by `rid % len(payloads)`. With a 98-bundle cohort and 200 records, each payload is used approximately twice. This is sampling with replacement and is harmless: no constraint in the model reads payload identity, and the invariance result is precisely the demonstration that it does not. Appendix A states this.

**Deterministic salts.** Salts are derived from the record identifier so that runs reproduce byte-identically. The code says at that line that a production deployment must use a cryptographically secure random source.

**Simulated key destruction.** Setting a reference to `None` demonstrates the mechanism's logic and demonstrates nothing about deployment assurance. Chapter 6, Section 6.3 treats this as the honest ceiling of the contribution.

---

## Files

```
app.py              Three-tab Streamlit viewer
trf_checker.py      The artefact — unmodified from Appendix A
synthea_layer.py    The realism layer — unmodified from Appendix A
requirements.txt    streamlit only
synthea_run/        Committed FHIR cohort (add before deploying Tab 3)
```
