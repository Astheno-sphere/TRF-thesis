# Supervisor Feedback History — Prof. João Ferreira

Every round of supervisory feedback, what it asked, what was done, and what it changed.
Chronological. This is the record of how the thesis was shaped by review, separate from the
change trail, which records *what* changed rather than *why it was asked for*.

**Cross-reference:** Claude Code session `session_01FPbdSPsPKYDLpxAt9wbLiy`
(`https://claude.ai/code/session_01FPbdSPsPKYDLpxAt9wbLiy`) holds the working detail for
rounds 2 and 3.

---

## Round 0 — Supervision established (pre-September 2026)

**What he gave.** Confirmed support for the formal-model approach. Called a sandbox demo
"gold".

**Effect.** Set the direction: a formal model with a runnable artefact rather than a purely
analytical thesis. Everything in `demo_app/` and the public repository descends from this.

**Status.** Settled. Recorded as decision D-02 and D-10 in `DECISION_RECORD.md`.

---

## Round 1 — First written feedback (September 2026)

Captured in `Supervisor_Feedback_Action_Plan.Rmd`.

**What he asked for.**

- A replicable literature-review methodology. The review was a structured narrative review
  presented without a protocol a reader could re-run.
- An evaluation instrument. The DSR cycle had no stakeholder-facing evaluation step.
- A scalability discussion.
- A threat model for key destruction.
- Opening hooks for the chapters.

**Two things he raised that I could not apply as asked**, recorded at the time as queries
rather than silently resolved:

- **The eHOMB date.** I had inferred a date from a source page's age. The page is updated in
  place, so its age cannot date its contents. The inference was invalid and was withdrawn;
  the dateless form is final. Closed as F-10, not recoverable from the public record.
- **The SPUHiN reference.** The document's status could not be established from the
  reference as cited. This became a live issue again in Round 3 (M5) and is *still* open.

**The decision he forced.** Conduct the expert evaluation, or specify it as designed and
unconducted? Two readings were written out with their consequences. The outcome at the time
was Reading B — designed, not executed. Tiger later reversed this and now wants it run.
João's Round 3 offers a middle path.

**What was delivered.** §2.1 review protocol with a prospective Boolean replication string ·
Appendix C evaluation instrument, eight participants across four perspectives · scalability
discussion · threat model in §4.9 · opening hooks drafted for Ch1–Ch5.

**What went wrong, discovered later.** The hooks were recorded as applied. **H-01 was not** —
the unsourced superlative it was meant to replace was still the opening sentence of the
thesis on 29 September, nine days after the trail said it had been fixed. Applied at last on
29 September. See `FAILURE_LEDGER.md`.

---

## Round 2 — Data provenance challenge (September 2026)

**What he asked.** Where did the synthetic data actually come from? The question implied the
data might not be genuine Synthea output.

**What was done.** `Data_Provenance_Statement.md` written and verified by inspection rather
than recollection: the exact generation command with seeds, the 98-usable-from-100 count with
the reason two patients were not exported, and six markers a reader can check in any bundle
(`synthetichealth`/`synthea` identifier namespaces, the `disability-adjusted-life-years`
extension, us-core profile conformance, Massachusetts addresses, Synthea's name-plus-numeral
convention, `transaction` bundle type).

**What it exposed.** The repository shipped no dataset at all — the demonstration's third tab
reported "no bundles found". The eight-bundle subset was committed on 28 September, which in
turn exposed that the 23 September web upload had flattened directories and silently dropped
three files.

**Effect on the thesis.** Chapter 5 now reports the mean payload at **both** cohort sizes,
891 bytes for the eight-bundle subset and 1,006 for the full 98-bundle cohort, because the
invariance holding across cohort size and payload-repetition frequency is a stronger result
than a single substitution.

**Status.** Closed. The statement is now in the repository at `docs/`.

---

## Round 3 — Full peer review, 30 September 2026

The substantial one. Captured in full in `SUPERVISOR_REVIEW_2026-09-30_Ferreira.md`; the
unedited original is `supervisor_review_RAW_2026-09-30.txt`.

**Format.** Applied the university template, ran a peer review, and returned it with track
changes. Four issues decide the verdict: M1, M2, M3, M5. Seven major concerns in total, a
minor-issues table, presentation notes, eight viva questions, and a ten-item priority list.

**What he named as strengths.** Source discipline, transparency and reproducibility called
"exemplary". Honest prior-art handling of the DePaul programme and US Patent 12,425,209.
Making "verifiable" an explicit parameter, called the most transferable idea. **§6.9a called
the best analytical result in the thesis**, with a request to promote it into Chapter 4.

**The three things his review caught that our process could not.**

1. **M2 — an internal legal inconsistency.** The thesis uses the *broad* reading of Art.
   68(12) to generate Corollary 1.2 and the *narrow* reading to resolve it via Theorem 2.
   Every check built in this project tests code against stated model; none tested whether
   the model's two halves cohere under one reading.
2. **M1 — an unexamined premise.** The model splits a record into metadata and a clinical
   payload, and nothing ever established that a real audit record contains clinical content.
   IHE ATNA records participant objects, not documents.
3. **M3 — our own drift, which he found and we had logged as safe.** `trf_checker.py`
   destroys the salt at invalidation while §4.8 says it is *not* destroyed, and the code
   comment cites §4.8 as its authority. Introduced on 28 September by syncing the working set
   to the repository on the finding that the repository was "ahead", without checking the
   prose agreed.

**Something he explicitly released us from.** Appendix C item A1 overstates what the thesis
claims ("full confidence"). We had kept it verbatim on the reasoning that silently correcting
a supervisor's wording would misrepresent the record. He wrote: *"The candidate may reword A1,
and it should be reworded. Keeping an item known to overstate the claim … is unnecessary.
Record the change in one line."* Our own constraint is superseded in writing.

**Status.** **OPEN. Nothing actioned.** Patch list in `PATCHES.md`; blocking decisions in
`DECISION_RECORD.md` O-01 through O-10.

---

## Patterns across the rounds

**He reads the code.** Round 3 quotes `trf_checker.py` line numbers, spots a dead `if False`
branch, and notices that the SPE record's payload in the code is the log itself. Feedback is
not going to be about prose alone.

**He asks for primary sources and means it.** The SPUHiN reference was raised in Round 1 and
is still unresolved in Round 3 as part of M5. It has now been raised twice. The Round 5
locator verification established why it is hard — the consultation page was withdrawn and
returns 404 — but "hard" is not an answer he has accepted.

**He gives decisions rather than instructions where the call is the candidate's.** Round 1
gave two readings of the evaluation question with consequences. Round 3 gives three options
for M2. Treat these as decisions to be made and recorded, not tasks to be executed.

**He names the contribution back.** Round 3 identifies §6.9a as the best result and asks for
it to be promoted. When a supervisor tells you where your contribution is, that is the
strongest signal in the document.

---

## What to carry into the next round

- The SPUHiN claim has been raised twice. Resolve it properly or state plainly what was
  inspected.
- Anything recorded as "applied" needs the diff attached. The trail has been wrong five
  times and one of those was a hook he asked for.
- If M2 is resolved by Option A, tell him it converts his objection into a finding rather
  than defending the original position. He is a reviewer who rewards that.
