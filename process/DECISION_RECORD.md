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

### D-14. The working base is the draft the supervisor reviewed
**Decided** by the candidate, 2 Oct 2026.
**Context.** The 30 Sept migration zip differed from the draft sent to Prof. Ferreira in 29
content edits (see `FAILURE_LEDGER.md` F-0). His review and his 47 tracked changes are against
that draft, so any other base makes his anchors miss and silently drops work he already saw.
**Rejected.** Continuing on the zip; merging the zip and the draft by judgement.
**Consequence.** Commit `0438daf`, tag `joao-base-v1`. The chapter files equal the draft in
every content paragraph; the remaining differences are template and rendering only (title-page
fields, Word's automatic TOC, equation spacing, code-listing wrapping, chapter-level reference
variants). `supervisor_review/` holds the returned file and its text with tracked changes
rejected and accepted. The Bodø opening (H-01, added after the draft was sent) is a proposal,
not base text.
**Status.** Holds.

### D-15. Salt is destroyed at invalidation (the A3 design)
**Decided** by the candidate on 22 Sept in the fork chat (turn 12, "yes Please"), before
Prof. Ferreira's review. The code already does this; §4.8 of the base text still says the
opposite. The supervisor's M3 asks for the same design. What remains open under O-03 is the
ciphertext and the dead branch, not the salt.
**Status.** Holds. Prose to be aligned in the M3 patch.

### D-16. Art. 68(12): the partition reading, with Proposition L (resolves O-01, O-02's framing)
**Decided** by the candidate, 3 Oct 2026, on the rule "the supervisor's option if it is better,
ours if our research is better". Ours was judged better because it contains his Option A and
rests on the Regulation's own text rather than on an interpretive claim with no authority.
**Evidence (retrieved 3 Oct, streamlex mirror of OJ L 2025/327).**
- Art. 68(12): "The electronic health data within the secure processing environment shall be
  deleted within six months of the expiry of the data permit." The same paragraph is about the
  permit dataset: storage costs, "a storage system with reduced capabilities", "the formula for
  the creation of the requested dataset".
- Art. 2(2)(a), (c): electronic health data are "data concerning health and genetic data,
  processed in an electronic form", personal or non-personal.
- Art. 73(1)(e): "the keeping of identifiable logs of access to and activities in the secure
  processing environment for the period necessary to verify and audit all processing
  operations in that environment; logs of access shall be kept for at least one year".
  Art. 73(1)(a) and (c) tie identifiability to the persons who access: "authorised natural
  persons listed in the data permit", "authorised identifiable individuals".
**The decision.**
1. Partition the metadata: m(a) = m_acc(a) ∪ m_subj(a). m_acc identifies who accessed, when and
   under which permit; this is what Art. 73(1)(e) requires to be identifiable, and it is not
   data concerning health. m_subj links the event to a data subject (patient pseudonym,
   record references); at patient-record granularity inside a health dataset it reveals health
   information and falls under Art. 68(12) on the broad reading.
2. C3 is formalised over p(a) *and* m_subj(a) (the supervisor's Option 1). The mechanism
   invalidates both at t_π + 6 and keeps m_acc, c and ι. On the broad reading both provisions
   are then met; on the narrow reading C3 does not reach the log and nothing changes.
3. Corollary 1.2 is restated as conditional on log granularity: logs kept at patient-record
   granularity collide with the ceiling without any request under Semantics I; logs kept at
   dataset granularity do not reach it.
4. Rival 6 (move the logs out at permit closure) is answered by **Proposition L**: a ceiling
   anchored to a location can be met by relocation, without cryptography; a right that follows
   the data (Art. 17) cannot, because it attaches to whoever holds the data. Cryptographic
   invalidation is therefore necessary for the request-driven conflict and optional for the
   location-anchored one. The thesis says so plainly.
**Rejected.** Option B (Art. 73(1)(e) as *lex specialis*): no authority, and the text does not
say 73(1)(e) derogates from 68(12); the partition makes it unnecessary. Option A unmodified:
concedes SPE infeasibility under both semantics, which the partition shows is not forced.
**Open within it.** Whether auditing "all processing operations" after t_π + 6 needs the
subject link is an interpretive question for the §7.4 Datatilsynet enquiry; stated as a
limitation. The partition is our reading, not an authority's.
**Consequence.** Unblocks M1, M2a–c, M4a–b. Code: SPE records carry m_acc and m_subj.

### D-17. Ciphertext deleted at invalidation; dead branch replaced (resolves O-03)
**Decided** by the candidate, 3 Oct 2026 ("if it is of no use, trim it").
**Reasoning.** Nothing in Semantics II uses the ciphertext once k(a) is destroyed, so keeping it
satisfies no constraint and the supervisor's M3 accepts deletion. Keeping it carries a
ten-year harvest-now-decrypt-later exposure, including against future quantum capability.
Deleting it does not make crypto-erasure redundant: key destruction remains the operative
erasure for copies the store cannot reach promptly (replicas, backups), which become
unreadable at t^I and leave by ordinary rotation. The salt is destroyed with the key (D-15);
a party that legitimately holds its own copy of the payload and must later prove
correspondence keeps its own opening.
**Code.** The `if False` branch is replaced by an explicit, documented deterministic salt for
reproducible runs and a `--random-salts` flag using `os.urandom`. Done in the code wave,
together with M1 and M4c, so the recorded runs are re-recorded once.

### D-18. Theorems become Propositions; anchoring result and Proposition L enter Chapter 4 (resolves O-06)
**Decided** by the candidate, 3 Oct 2026. Weight moves to the §4.2 necessity analysis, the
anchoring result of §6.9a (promoted), the partition (D-16) and Proposition L. V_II gains a
real integrity test (Merkle log over m, c, ι with a tamper test), not a presence check.

---

## OPEN — these need an answer before work continues

### O-01. RESOLVED 3 Oct by D-16. Which reading of Art. 68(12) does the thesis carry?
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

### O-02. Framing settled by D-16; grounding is patch M1. Can p(a) be grounded in a real audit-record format?
Raised by M1. Research first, then a decision. If eHDSI audit repositories hold no clinical
content, Semantics I must be reframed as the semantics of a rich audit log, and the
cross-border instance of Theorem 1 weakens. Resolve after O-01, before Chapter 4 prose.

### O-03. RESOLVED 3 Oct by D-17. Ciphertext and dead branch (salt settled, see D-15)
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

### O-06. RESOLVED 3 Oct by D-18. Rename theorems to propositions?
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
