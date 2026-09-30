# Session log — 15 to 21 September 2026

The transcripts in this folder run to 15 September. This log records the session that followed, in which most of the rebuild was done. Read `HANDOFF_READ_FIRST.md` for the resulting state; this file records how it got there.

## Chapters written and rebuilt

- Chapter 1 retrofitted (v2): TRF framing, Art 17(3)(b) defence, landscape updates.
- Chapter 2 assembled in full; §2.1 later rewritten as a documented review protocol, with Appendix B (59 queries across four dated rounds).
- Chapter 3 written: DSR paradigm, formal-modelling method, Synthea, sandbox, validity, ethics. Later: §3.8 evaluation design, eight-item limitations register.
- Chapter 4 written: both theorems with proofs, mechanism, residue analysis, five rival designs, Norwegian integration.
- Chapter 5 written *after* the checker ran — every figure from executed code.
- Chapter 6 written: authority problem, key destruction, cost, scalability, evaluation design, policy timing.
- Chapter 7 written.
- Front matter written fresh, with nothing carried from the May draft; the ethics declaration withdraws the earlier IRB claim by name.

## Artefact

- `trf_checker.py` built and run: 95 violations under Semantics I, 0 under Semantics II, 39 Corollary 1.2 witnesses. Independent exhaustive cross-check over 2^14 assignments.
- Real Synthea installed, 98-bundle cohort generated under seed 20260915; realism layer showed every figure invariant under real FHIR payloads.
- Tiger built a Streamlit demo; a `NameError` bug in its third tab was found and fixed; deployed at trfhimolde.streamlit.app, source at github.com/Astheno-sphere/TRF.
- δ = 3 witness added after supervisor feedback.

## Major findings

- **EHDS Art 73(1)(e)** — a one-year identifiable-log floor on the same SPE that Art 68(12) empties at six months. The collision sits within one regulation. Absorbed as a second floor instance.
- **Art 68(12) is contestable.** "The data within the SPE" is broad by location but sits in the data-permit article. Corollary 1.2 was made conditional; nothing else depends on it.
- **Aikebaier (2026)** names "erasure under multi-regime retention conflict" as an open problem — corroboration, weighed as an unreviewed preprint.
- **DePaul research programme** found as closest prior art; its design keeps recoverable copies, which a ceiling forbids.

## Supervisor feedback, two rounds

Round 1 asked for a template, no bold, APA at the end, an evaluation framework, a replicable literature review, and draft-marker cleanup. Round 2 flagged reference collisions, the weight placed on the Aikebaier preprint, disciplinary fit, repetition of limitations, and the Datatilsynet question; it also raised a hard blocker on the synthetic data. That blocker was answered by inspecting the bundles, which proved to be genuine Synthea output.

## Integrity passes

- Em-dash reduction (334 → ~169) — later found to have **corrupted** 48 sentences into broken dash-colon pairs and comma splices. All repaired.
- Math: 175 native Word equations, verified through pandoc.
- Sentence pass 1: every prose sentence over 55 words resolved, bar three deliberate exclusions.
- Citations: DOIs and URLs rose from 27 to 40 of 67, using verified or deterministic identifiers only.

## Errors made in this session, and caught

Recorded so they are not repeated. See HANDOFF §4.

- Claimed items done that weren't (scalability, trust assumptions).
- Reported "zero corruptions remaining" with a detector too narrow to see them.
- Removed a true NCP-A claim as "unverified".
- Inferred "12 March 2025" from page age; the page is updated in place. Withdrawn, including from advice given to the supervisor.
- A duplicated clause from two alternative edits both firing.
- Misattributed the EDPB threat-model condition in three chapters after fixing it in one.
- Misattributed arXiv 2210.04541 to Haque et al.

## Decisions Tiger made

Absorb Art 73(1)(e); generalise the RQ; cross-border case first; leave the evaluation designed rather than executed; accept exceeding 80 pages if the work is good; don't shorten the RQ without his decision; migrate to a new conversation carrying this package.
