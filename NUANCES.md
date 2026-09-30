# Nuances — how this work runs

The things that are not in any other document because they are not facts about the thesis.
A new session that reads only the manifest and the register will produce technically
correct work that Tiger sends back. This file is why.

---

## Who

**Tiger** (Arshad Akhtar Abbasia). MSc Sustainable Energy Logistics, Høgskolen i Molde,
2024–2026. Supervisor **Prof. João Ferreira**. Submission **14 November 2026**, defence
first week of December 2026. Four years of cross-border procurement and logistics across
DACH, India and UAE. Runs START Molde. GitHub `Astheno-sphere`.

He is not a cryptographer and says so. He decided he could own the TRF model and teach
himself the equations, and he has. He knows the regulatory material better than the
mathematics, and questions about Art. 68(12) get sharper answers from him than questions
about commitments.

---

## How he wants to be worked with

**Compressed and direct. No flattery, no padding.** This is a saved preference and it is
real. Openers like "Great question" get a worse response than silence.

**One question maximum per turn.** He has said so. Batch decisions or decide and flag.

**Push back rather than agree.** Explicit standing instruction: *"remember to push back
rather than agree when you have a better argument."* He means it. Twice he has asserted
something wrong — that `cross_sector_check` was not on GitHub, that the thesis had many
redundant paragraphs — and the right response was evidence, not accommodation. He did not
object either time. **Agreeing with a wrong premise wastes his run.**

**Never proceed until everything connected is updated.** Standing rule since the beginning,
originally about the Google Sheet substrate: *"never forget or proceed until we make sure
our excel is also updated with new finding, pending fetches, rebuild papers."* It has
widened to mean: a change is not done until it is applied in the chapter file, the
assembly, the repository, the register and the change trail.

**Surgical patches with a change trail, not repackaged deliverables.** He wants to see what
changed and why, not a new zip with no diff.

**He will say "amazing" and then immediately list ten problems.** The praise is genuine and
the list is the actual message. Do not spend the reply on the praise.

---

## What he reacts badly to

- **Claiming something is done when it is not.** This has happened five times via the change
  trail and it is the fastest way to lose his trust. See `FAILURE_LEDGER.md`.
- **Repackaging instead of patching.** He notices.
- **Long replies that recap the process.** State the outcome, the evidence, the open
  question.
- **Being told an audit was run without the numbers.** "Register: 36 files, 0 stale" is
  worth more than a paragraph.

## What he reacts well to

- Being told he is wrong, with the grep output that shows it.
- Findings he did not ask for, when they are real — the five false trail entries, the
  LibreOffice equation blindness, the 27 unlinked references.
- Work delivered against his exact words. He quotes himself back.

---

## Standing technical rules

1. **The submission is generated.** Edit chapter files, then run `assemble.py`. Editing
   `VERA-SNARK_Thesis_SUBMISSION.md` directly is wiped on rebuild — this is probably why he
   has twice thought patches "were never delivered".
2. **Anti-drift and anti-hallucination on every change.** His phrasing: *"invoke anti drift,
   anti hallucination mechanism at all time and self correcting loop anchored to latest
   verifiable truths."* In practice: `inspector.py` gates rewrites, and nothing is asserted
   that was not executed or retrieved.
3. **Every claim anchored to a source that was actually fetched.** Not "this is probably at
   this URL".
4. **The version register is the contract.** Any file changed without its row updated is a
   defect.
5. **Checksums computed after the final edit, never before.** Stale registration has bitten
   twice.

---

## Things that look like errors and are not

- **12 prose em-dashes remain.** Deliberate: 7 inside source titles that may not be altered,
  1 verbatim console output, 2 in the supervisor-approved research question, 2 in an
  appositive whose aside already ends in a parenthetical.
- **~50 dash-then-colon corruptions in `_draft_Thesis_FULL_with_chapter_refs.md`.**
  Non-canonical, kept as the record of what was corrected. Do not repair them.
- **`norwegian_docs/HOW_TO_RUN.md` differs from the checksum record.** The 116-line original
  was never uploaded and no copy survives; the replacement is 103 lines, written from actual
  module runs. Recorded as R-07.
- **SPUHiN D5.2 has no direct locator.** The consultation page was withdrawn and 404s. The
  entry says so rather than substituting a nearby link. This is correct behaviour, and João's
  M5 asks us to go further in the same direction.
- **Table cells containing "—".** That is "not applicable", not an em-dash to be cleaned.

---

## Decisions he has reversed, and the current position

- **Expert evaluation.** Originally designed-not-executed by agreement. He then reversed and
  wants it run. João's M6 now offers a middle path (traceability matrix as the minimum).
  Current position: unresolved, see `DECISION_RECORD.md` O-04.
- **Code highlighting.** He originally asked for code in coloured boxes with black
  backgrounds. Reversed on evidence — no thesis guideline, style manual or publisher
  contemplates dark code backgrounds; APA prescribes monospace only. Now `tango` on light.
  He accepted the reversal without argument when shown the sources.
- **Length.** He accepted the overrun: *"getting over page is not an issue if we are doing
  true good work"*, and later *"for length a lot of our components are table, codes,
  appendixes. all good."* João nonetheless flags ~38,000 words with a 30% literature review.
  Open.

---

## The relationship to the supervisor

João is a serious reviewer who reads the code. His 30 September review found two things
none of our automated checks could see (the Art. 68(12) inconsistency; the ungrounded
payload), and one that was our own drift (the salt). He also names §6.9a "the best
analytical result in the thesis", which is a strong signal about where the contribution
actually is.

He supplies his own viva questions and explicitly releases the candidate from a constraint
we had imposed on ourselves (Appendix C item A1). **Read his review as collaboration, not
as a defence to be mounted.**

---

## Tone for the work itself

The thesis has a habit the review names precisely: *defensive meta-commentary* — "stated
rather than buried", "recorded rather than concealed", "a reader is entitled to", roughly 50
occurrences. That habit came from this working relationship, where stating the limit
explicitly was the right move in conversation. **It does not transfer to the document.** In
the thesis it reads as pre-empting examiners rather than arguing with them.

Keep the habit in replies to Tiger. Cut it from the prose.
