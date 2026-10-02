# Failure Ledger

Every failure mode observed in this project, what it cost, and the rule that came out of
it. This exists because the same classes of error recur, and because a handoff that records
only successes teaches a new session nothing.

Read this before trusting any claim in any other document, including this one.

---

## 2 October 2026: two corrections that override what follows

### F-0. Building on a base that is not the version the supervisor reviewed (the costliest failure)
On 30 Sept–1 Oct the work was built on the chapter files of the 30 Sept migration zip. That zip
was **not** the draft sent to Prof. Ferreira. The draft he reviewed (his tracked file,
`supervisor_review/Master_thesis_Abbasia_tracked_JF.docx`, read with tracked changes rejected)
differs from the zip in 29 content edits: a rewritten abstract, a Norwegian abstract, "five
rivals", the accumulator caveats, the F+1 window, the corrected witness count, the
Datatilsynet/EHDS addressee split, the narrow-reading hedges, two Chapter 5 paragraphs and more.
The zip also carried one edit made *after* the draft was sent (the Bodø opening, H-01). The
divergence was noticed on 30 Sept, flagged, and then not acted on. Patches F1–R1 were built on
the wrong base and are now on branch `zip-base-superseded`.

The register reported 0 mismatches throughout. **A register verifies that the package agrees
with itself, not that it is the version anyone else has seen.**

**Rule.** The base is the last version that left the building: the draft the supervisor
reviewed, recovered from the file he returned. Before any patch, diff the working copy against
that file and reconcile every difference. Record the base's provenance in the register.

### Correction to the governing lesson below
The five entries in the table below (D-05, A-04, A3-l, P8-03, H-01) were **not** false. They
were applied on 22 Sept in a separate chat (claude.ai `2a87fc70-ba56-4c97-9960-fcca3b03ed36`,
"File reconciliation and checksum mismatch resolution") that worked from the 21 Sept package.
Its chapters never returned to the main line; only its change trail and code did, through the
23 Sept GitHub push. The main line then read a trail describing chapters it did not have.

**Rule.** One working copy. A second chat that edits thesis files is a fork, and a fork's trail
is not evidence about this copy. The underlying lesson below (diff the artefact, not the
record) still stands.

---

## The governing lesson (written 30 Sept; see the correction above)

**A record that a thing was done is not evidence that it was done.**

Five change-trail entries have been found marked applied but absent from the canonical
files. Each was written in a session that ended before delivering its work; the entry
survived, the edit did not.

| Entry | Claimed | Actually |
|---|---|---|
| D-05 | False CSPRNG sentence removed from Appendix A | Still present in four files including the submission |
| A-04 | `repro_package/docs/Appendix_A.md` replaced | Still the 16 Sept text, 144 lines against 769 |
| A3-l | Checker 362 → 363 lines, salt line added to the listing | Working set still 362 |
| P8-03 | Appendix A contents table updated | Not updated |
| H-01 | Unsourced superlative replaced with a sourced hook | Still the opening sentence of the thesis, 9 days later |

**Rule.** Diff against the artefact, never against the trail. For a claim about the
repository, clone it and diff. For a claim about a file, grep it. The trail is a record of
intent.

---

## Failures of verification method

### F-1. Byte-identical output proves self-consistency, not correctness
On 28 Sept I found `rec.salt = None` in the repository but not the working set, concluded
"the repository is ahead", and propagated it to all five copies. I logged it as safe
because "the line changes no reported figure, which the byte-identical output establishes".

That was true and irrelevant. Chapter 4 §4.8 says the salt is **not** destroyed at
invalidation. The code destroys it and the comment cites §4.8 as its authority. João found
it (M3); no check we built could have.

**Rule.** Every check we have tests whether the code matches the *stated* model. Nothing
tests whether the code matches the *prose*. When code and specification disagree, output
determinism says nothing about which is right. Build a spec-to-code reconciliation, or at
minimum grep the chapter for every behaviour the code implements.

### F-2. Detectors narrower than the thing they detect
- An em-dash pass corrupted 48 sentences into dash-then-colon pairs. Word-invariance checks
  missed it because punctuation is not words.
- I then reported "zero dash corruptions remaining" when the detector's window caught one of
  three shapes. One survivor was still in Appendix B on 29 September.
- I grepped for `Helsedirektoratet, 2026b` and found nothing, because the in-text form was
  `(Helsedirektoratet, 2026a, 2026b)`. Four citations were left pointing at a deleted
  reference. **The inspector caught it, not me.**

**Rule.** Before claiming absence, widen the detector until it catches a known instance.
Then claim.

### F-3. Visual verification is blind to mathematics
Rendering the Word file to PDF caught real table defects that no text check could find —
Table 2.1 had no rules at all. The same render shows **every equation as missing**, because
LibreOffice does not render OMML. 191 equations are present in the file.

**Rule.** The render is authoritative for layout and blind to maths. And practically:
**export the submission PDF from Word, never from LibreOffice or any non-OMML converter.**

### F-4. Assuming the direction of drift
On 28 Sept the public repository turned out to be *ahead* of the working set, not behind.
Reconciliation had only ever diffed within the working set.

**Rule.** Reconcile against every location the work lives in: working set, repository,
Drive, deployed app.

### F-5. Self-referential checksums cannot converge
The version register recorded the archive's md5; the archive contains the register.

**Rule.** Do not record a container's checksum inside it. Verify by unpacking and checking
the contents.

---

## Failures of judgement

### F-6. Over-correcting
I removed a true NCP-A claim as "unverified" because I had not read that paragraph of the
source. Removing is not automatically the safe move.

### F-7. Invalid inference from metadata
I dated a sentence from its source page's age. The page is updated in place. Withdrawn from
the chapters, the action plan and the published artifact.

### F-8. Trusting and dismissing a reviewer in the same session
A reviewer claimed §4.7 stated something it did not; grep found nothing. I took the remedy
and rejected the premise — correct. But in the same period I accepted other claims without
checking. **Verify either way.**

### F-9. Arithmetic asserted rather than run
Fixing the repository README's line count I used `len(text.split("\n"))`, which counts the
trailing empty element, and wrote 527. `wc -l` is 526.

**Rule.** Run the count. Then write it.

### F-10. Prefixing instead of replacing
Marking an item COMPLETE while leaving its old "Remaining: …" text produced a
self-contradicting entry that a fresh session read as still open.

**Rule.** Replace status text. Never append to it.

---

## Failures the supervisor found that our process could not

Recorded separately because these are not process slips — they are limits of what our
checks are capable of seeing.

### F-11. Nothing tested the model's internal legal consistency
The thesis uses the **broad** reading of Art. 68(12) to generate Corollary 1.2 and the
**narrow** reading to resolve it via Theorem 2. Every check we built tests code against
stated model. None tests whether the model's halves are consistent under one reading.
(João's M2 — the most serious item in the review.)

### F-12. Nothing questioned the object of study
The entire model splits a record into metadata and a clinical payload. Nothing established
that a real audit record contains clinical content. IHE ATNA records participant objects,
not documents. If it holds no payload, Semantics I describes a practice nobody follows.
(M1.)

**Rule from F-11 and F-12 together.** Automated checks verify internal consistency and
cannot verify premises. A premise gets checked by a person who knows the domain, or not at
all. Budget for that, and ask for it early rather than at review.

---

## Standing checks that have earned their place

| Check | Catches | Command |
|---|---|---|
| Register verification | Any file changed without being recorded | see `VERSION_REGISTER.md` |
| `inspector.py` before/after | Citations, numerals, article refs, hedges, reference lists altered by a rewrite | `python3 handoff_tools/inspector.py <before> <after> <label>` |
| Assembly rebuild | Whether the submission still regenerates from the chapter files | `python3 handoff_tools/assemble.py` — byte-identical is the pass |
| Fresh-clone run | Whether the published artefact actually reproduces the thesis figures | clone, then `python3 trf_checker.py \| diff - docs/expected_trf_output.txt` |
| `run_all.sh` | All five recorded runs still match | `bash repro_package/run_all.sh` |
| PDF render + read the images | Table rules, overflow, layout | `soffice --convert-to pdf` then `pdftoppm` then Read |
| Corpus sweep for dash-colon | Surviving em-dash corruption | regex `—[^—\n]{5,200}:\s+[a-z]` |
