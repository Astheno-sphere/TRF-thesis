# Open cases

Single tracker for everything not yet closed. Updated 2 Nov 2026 after the end check (P107 to P111).
Each case: what it is, why it matters, the reasoning so far, the recommended move, and who decides.
Close a case by moving it to the bottom with the commit that closed it.

Submission: 14 Nov 2026.

---

## A. Decisions for Tiger (argument, not wording)

The examiner's round-3 attack raised these. They are not wording slips; each changes what the thesis claims. The text is consistent as it stands, so none is a blocker, but each will be asked at the defence.

### D1. The pilot floor has no statute behind it
- **The point.** Six years is Helsedirektoratet's decision as controller (Appendix D), not a legal minimum. Art. 17(3)(b) exempts only what is necessary "for compliance with a legal obligation". Until Art. 9 applies (26 March 2029), and for months 37 to 72 after it, keeping the patient link after an erasure request may have no 17(3)(b) basis.
- **Why it matters.** The abstract speaks of "three retention obligations at once". For the cross-border record before 2029, one of the three may not be an obligation.
- **Reasoning.** This does not hurt the model: the floor is a parameter (Corollary 2.2), and a smaller or absent floor only removes collisions. It sharpens the finding: Norway's controller may be keeping, for six years, data the law does not require it to keep. That is a finding for Helsedirektoratet, and it fits §7.4.
- **Recommended.** Add two sentences to §4.2: the pilot period is a controller decision; whether it engages 17(3)(b) depends on a national legal basis not identified; until Art. 9 applies the cross-border floor is therefore a policy floor. Soften the abstract to "retention requirements". Effort: small. Risk: low.
- **Decides:** Tiger.

### D2. Proposition 1 depends on §4.2
- **The point.** If the floor really required plaintext (Semantics I), Art. 17(3)(b) would exempt the payload and the erasure request would never bind (C2 would not fire). The request-driven half of Proposition 1 therefore assumes what §4.2 argues: that the payload is not necessary.
- **Reasoning.** This is circular only if stated as unconditional. The thesis's structure is in fact: §4.2 argues necessity does not reach the payload; Proposition 1 then shows that a system that keeps the payload readable anyway cannot meet the right. Stated that way it is sound.
- **Recommended.** One sentence in §3.7 (as a fifth subsidiary premise, or folded into the first principal step) and one in §4.6: "Proposition 1's request-driven case holds for payload that §4.2 shows is not necessary." Effort: small. Note: adding a fifth premise changes "four subsidiary premises" at nine sites; folding it into principal step 1 avoids that.
- **Decides:** Tiger.

### D3. Corollary 1.2's premise on activity content
- **The point.** A log entry counts as electronic health data (ρ = 1) because of its subject fields. C3 then forces the payload unreadable. If the activity content alone is not health data, Semantics I is feasible: keep the payload, delete the subject fields.
- **Reasoning.** For patient-level SPE logs the activity content (which records, which variables) is itself health data about the patient. That is a defensible premise, not a theorem.
- **Recommended.** State it as a premise in §4.6 next to Corollary 1.2 (it belongs with the "patient-record granularity" qualifier already there). Effort: one sentence.
- **Decides:** Tiger.

### D4. ITI-55 identifier-based lookup
- **The point.** §4.3 says name and birth time are required "unless an identifier is supplied"; Rival 3 and §6.1 drop the qualifier. With identifier-based patient discovery the payload is just the identifier, which the mechanism keeps as the subject link, so cross-border erasure removes little.
- **Reasoning.** True, and honest to concede. The SPE case is unaffected.
- **Recommended.** Add "where demographic matching is used" in Rival 3 and §6.1; one sentence conceding the identifier case. Effort: small.
- **Decides:** Tiger (wording is mechanical once agreed).

### D5. "Verifiable" in the title
- **The point.** An auditor cannot verify that a key is gone (§4.9). What is verifiable is the attributed invalidation entry and its inclusion proof.
- **Recommended.** Keep the title; add one sentence in §1.4: "verifiable" qualifies the invalidation record, not the erasure. Effort: one sentence.
- **Decides:** Tiger.

## B. Smaller gaps

### G1. External-auditor verifiability: objective set, never reported
- §3.2 Activity 2 sets "verifiability by an external auditor" as a design objective; Chapter 7 does not report against it.
- **Recommended.** One sentence in §7.1 or §7.3: met for the invalidation record (inclusion proofs checked in the artefact, §5.x); not met for destruction itself (§4.9). Effort: one sentence.

### G2. Programme fit: no optimisation
- A logistics examiner will notice there is no objective function.
- **Recommended.** Do not add optimisation now. Defend: information logistics (§2.7), chain-of-custody parameter (§4.3), two-clock perishability (Proposition 3); concede the absence. Already in the viva notes.

## C. Release and archive

### R1. Zenodo version 1.2.0
- **Why.** Appendix A listings now reproduce the end-check code (P107 to P111). The thesis cites version 1.1.0 (DOI 10.5281/zenodo.23826911), whose code differs in comments, exit codes and one printed line. A reader following the version DOI would find code that does not match Appendix A.
- **Prepared.** CITATION.cff and .zenodo.json at 1.2.0; the supervisor contributor and the related-work link to the thesis repository (held back since 31 Oct) go in with it.
- **Needs.** Tiger's go-ahead to publish the GitHub release (publishing is public and mints a permanent DOI). Then: patch A.1 and the abstract footer to the new version DOI; rebuild docx.

## D. Tiger-only, outside the text
- Length: chapters 1 to 7 are about 56,000 words; no HiMolde limit found. Ask João.
- Title-page logos (MIN-14).
- Coordinator sign-off on the AI declaration (R4-C2).
- Rak (2024) page and TEHDAS2 D6.3 page (HiMolde library).
- Datatilsynet enquiry text (23 Sept) for Appendix D.2, if wanted.
- `joao-base` branch: keep in step with `main` or retire after João has read.
- Make both repositories private before the defence (viva notes are public).
- NORS correction note: send or not (`process/NORS_correction_note_DRAFT.md`).

## E. Known, accepted
- trail_check 14 (full replay from joao-base-v1) fails on P01 to P30 anchors: historical drift, unchanged since before P92.
- trail_check 4 warns that some patches share a commit.

---

## Closed
- P102/P103 João's 2 Nov feedback, verified items: 41cfece.
- P104 Appendix D: 41cfece. P106 whipper round: c5ce6f3.
- Branch: joao-base made main; old upload kept as archive-upload-2026-10-04: 880c630.
- P107 to P111 end check (code audit, examiner round 3, novelty sweep): 9d69d7c.
