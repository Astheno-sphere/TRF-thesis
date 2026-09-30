# Decision Record

Every decision that has been settled, with the alternatives rejected and why. A decision
recorded here is **not to be reopened** without the candidate saying so — the reasoning
exists so a fresh session does not re-litigate ground already covered.

Open decisions are at the end. Those are live and need an answer.

Format: **D-n** — the decision · context · alternatives rejected · consequences · status.

---

## Settled — model and scope

### D-01. The model is tri-lateral by constraint *type*, not by instrument count
**Decided** Sept 2026, after discovering Art. 73(1)(e).
**Context.** A second retention floor (the one-year SPE log floor) was found after the
"tri-lateral" name was set. The obvious move was to rename to quad-lateral.
**Rejected.** Renaming. The three constraint *types* — floor, subject-triggered right,
ceiling — are what the model distinguishes; a second instance of one type changes the
parameter, not the structure.
**Consequence.** F(a) is a per-record parameter, which is what makes Corollary 2.2
(F-independence) possible and what limits the damage from M5's weak ten-year source.
**Status.** Holds. Reinforced by João's review, which treats the floor parameterisation as
the load-bearing logistics contribution.

### D-02. Verifiability is an explicit parameter with two competing semantics
**Context.** Audit systems assume verifiable = readable without saying so.
**Rejected.** Treating verifiability as fixed, which makes the conflict unanalysable.
**Consequence.** The whole thesis. João calls it "the most transferable idea".
**Status.** Holds.

### D-03. Chapter 4 presents the cross-border case first, the SPE case second
**Decided** by the candidate. Matches the order of the chapters.
**Status.** Holds.

### D-04. The research question stays at 102 words
**Decided** by the candidate; supervisor-approved.
**Consequence.** It is the last prose in the thesis carrying em-dashes, left untouched for
this reason.
**Status.** Holds unless the candidate says otherwise.

### D-05. Synthetic data is Synthea, US Core, and the thesis says so
**Rejected.** Claiming Norwegian representativeness; trimming bundles to look tidier.
**Consequence.** The payload-independence demonstration exists precisely to show the
mismatch cannot affect a result. Verified at two cohort sizes.
**Status.** Holds. Not challenged in the review.

### D-06. Evaluation is analytical; the expert instrument is designed, not executed
**Status.** **Under pressure.** João accepts the framing for a specification-and-
demonstration MSc but warns the jury may see the Peffers cycle as incomplete, and asks for
a traceability matrix as the minimum. See open decision O-04.

---

## Settled — artefact and tooling

### D-10. The artefact is public, seeded, and self-verifying
`github.com/Astheno-sphere/TRF`, seed 20260915, five recorded runs, exhaustive cross-check
with a control case.
**Rejected.** Reporting figures without a runnable witness.
**Consequence.** Named a strength in the review. Also the reason five false change-trail
entries were caught.
**Status.** Holds. Must now be **tagged** — the thesis cites a moving `main`.

### D-11. The submission is generated, never hand-edited
`handoff_tools/assemble.py` rebuilds the bibliography from chapter reference lists and the
submission from chapter files.
**Rejected.** Editing `VERA-SNARK_Thesis_SUBMISSION.md` directly. It gets overwritten on the
next rebuild, which is why patches appeared to vanish.
**Consequence.** Every edit goes into a chapter file. A rebuild that comes back
byte-identical proves nothing was lost.
**Status.** Holds. **Known defect:** the dedup rule keeps the *longer* variant, so a long
unlinked reference line beats a short linked one. Unfixed.

### D-12. Word output uses `thesis_reference.docx`, not pandoc defaults
A4, 2.5 cm margins, Times New Roman 12 pt, 1.5 spacing, styled heading hierarchy, monospace
code, booktabs table rules.
**Rejected.** `breezedark` code highlighting — reversed on evidence: no thesis guideline,
style manual or publisher contemplates dark code backgrounds; APA prescribes only
monospace. Also rejected: Word's default table styles with banded shading, which violate
both APA and booktabs.
**Status.** Holds, provisionally. **The HiMolde template overrides all of it** and has not
been obtained.

### D-13. No text highlighting anywhere
**Context.** The candidate asked directly whether highlights are allowed.
**Evidence.** UNC's graduate school names "highlighting intended solely to draw a reader's
attention to a key phrase" as "extraneous or unprofessional". APA has no highlighting
device. Word's highlighter is a review tool and reads as uncleared draft markup.
**Consequence.** Emphasis by italics on first use and by heading hierarchy. Colour reserved
for figures, where it must survive greyscale.
**Status.** Holds.

---

## Settled — how claims are handled

### D-20. Nothing is cited that was not retrieved
**Consequence.** The 28 Sept locator round removed two entries as documents that do not
exist as cited (European Commission "Implementation calendar"; Helsedirektoratet
"MyHealth@EU, Norsk helsenett"), and left SPUHiN D5.2 without a direct locator rather than
substituting a nearby link.
**Status.** Holds. João's M5 asks for more of the same, not less.

### D-21. Non-existent or weak sources are named, not quietly dropped
VeritasChain is retained with its standing stated — a self-declared initiative founded 24
November 2025, not accredited — because Ch2 §2.5, the §2.8 table and the §2.9 gap statement
rest on it as the practitioner pattern.
**Status.** **Under pressure.** João asks for it and other non-peer-reviewed sources to move
to a footnote row or a separate practitioner band in Table 2.1. See O-05.

### D-22. A correction is recorded with its reason, never silently applied
**Consequence.** `CHANGE_TRAIL.md`. **Caveat learned the hard way:** the trail has been
wrong five times. See `FAILURE_LEDGER.md`.

---

## OPEN — these need an answer before work continues

### O-01 (BLOCKING). Which reading of Art. 68(12) does the thesis carry?
Raised by João's M2. **This is the candidate's decision, not a research task**, and it
determines what Chapter 4 proves, whether Corollary 1.2 survives, and what the abstract
claims. Every other Chapter 4/6/7 edit is wasted until it is settled.

- **Option A (recommended).** Formalise C3 over m(a)'s identifying fields too. Concede
  that on the broad reading the SPE case is infeasible under *both* semantics. Converts an
  inconsistency into a finding: a drafting defect the Art. 73(5) implementing acts must
  resolve by 26 March 2027. Loses "we solved it" for the SPE case, gains "we proved it
  cannot be solved as drafted".
- **Option B.** Art. 73(1)(e) as *lex specialis* to Art. 68(12) for logs. Resolves by
  interpretation rather than mechanism; re-scopes every SPE claim.
- **Either way:** Rival 6 (export the logs out of the SPE at permit closure) must be
  answered. It satisfies both provisions literally with no cryptography.

### O-02 (BLOCKING). Can p(a) be grounded in a real audit-record format?
Raised by M1. Research first, then a decision. If eHDSI audit repositories hold no clinical
content, Semantics I must be reframed as the semantics of a rich audit log, and the
cross-border instance of Theorem 1 weakens. Resolve after O-01, before Chapter 4 prose.

### O-03. Salt and ciphertext design
Raised by M3. Three sub-decisions: destroy the salt at invalidation, keep it, or store it
under k(a); delete the ciphertext at invalidation or justify keeping it; fix the `if False`
dead branch. Currently **text and code contradict each other and the code cites the text it
contradicts**. Independent of O-01 and cheap — do it early.

### O-04. Does the evaluation step get strengthened?
Raised by M6. Minimum recommended: a requirement-by-requirement traceability matrix against
TEHDAS2 D7.4 and the SPUHiN checklist. Optional: two or three expert walkthroughs, which
need a Sikt check with a four-to-six-week lead time against six weeks remaining.

### O-05. Table 2.1 treatment of non-peer-reviewed sources
Raised by M5. Move Aikebaier, VeritasChain, SecuPi and OneUptime to a footnote row or a
separate practitioner band, or leave them inline with their caveats.

### O-06. Rename theorems to propositions?
Raised by M4. If yes, also promote §6.9a's anchoring result into Chapter 4 as a formal
result — do both or neither. The V_II hash-chain integrity test should be done regardless.

### O-07. Length and Appendix A
~38,000 words main text, ~12,000 in Appendix A listings. Replace full listings with the
tagged repository, SHA-256 hashes and core functions only? Cuts ~12,000 words.

### O-08. Zenodo DOI and repository tag
The thesis cites a moving `main`. Tag `0d855a7` or later and archive.

### O-09. HiMolde template
Unobtainable from this environment (403 on every himolde.no URL). The candidate must
download `document_template-masters_thesis.dotx` and the *Guidelines Master Thesis* PDF.
Until then every formatting decision is an informed guess.

### O-10. Figures
Two identified as earning their place: the record-state diagram (§4.8, reprised §5.6) and
the regulatory timeline (§6.8). The candidate has said not to rush them. The thesis
currently has **zero figures**.
