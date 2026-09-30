# Patch Queue — João's Review

Live working list. Updated as we go. Every item records what it touches and what it drags
with it, because these fixes cascade and a fix applied in one chapter and not its dependents
is how this project has failed before.

**Status key:** `OPEN` · `BLOCKED` · `IN PROGRESS` · `DONE` · `NEEDS TIGER`

**Cascade counts are grepped, not estimated.** Where a number appears it is the count of
occurrences found in that file today.

---

## BLOCKING — nothing in Ch4, Ch6 or Ch7 should be touched until this is answered

### P-01 · M2 · Which reading of Art. 68(12) does the thesis carry? · **NEEDS TIGER**

The thesis uses the **broad** reading to generate Corollary 1.2 and the **narrow** reading
to resolve it via Theorem 2. One of them has to go.

**Cascade — grepped today:**
- Front Matter: 2 mentions of 68(12), 1 of Corollary 1.2 — the abstract and contribution statement both claim the result
- Ch1: 7 · Ch2: 8 · Ch4: 8 with 6 Corollary 1.2 and 5 broad/narrow passages · Ch5: 7 with 6 · Ch6: 10 with 4 · Ch7: 4 with 1
- Code: C3 is formalised over payload accessibility α alone. Option A changes `check_semantics_II` and the reported figures
- **Tab 1 of the Streamlit app self-asserts 95/39/0.** If the figures move, the app's pass banner flips to a failure banner until updated

**Option A (my recommendation).** Formalise C3 over m(a)'s identifying fields too. Concede
that on the broad reading the SPE case is infeasible under *both* semantics. The thesis stops
claiming it solved the SPE case and instead proves the Regulation cannot be satisfied as
drafted — a drafting defect the Art. 73(5) implementing acts must resolve by 26 March 2027.
Corollary 1.2 survives and gets sharper. Theorem 2 is re-scoped to the cross-border case.
Costs: Ch4 §4.8, §6.1, the abstract and Ch7 all need rewriting, and the SPE figures change.

**Option B.** Art. 73(1)(e) as *lex specialis* to Art. 68(12) for logs. The collision is
resolved by interpretation, not by the mechanism. Corollary 1.2 lapses. Cheaper to write,
weaker result, and it concedes the thesis's sharpest finding.

**Either way — P-02 below is mandatory.**

---

## REQUIRED

### P-02 · M2 · Add Rival 6: relocate the logs out of the SPE · OPEN
If the ceiling is locational, exporting access logs to an HDAB-held store at permit closure
satisfies both provisions literally with no cryptography. **The thesis must say why this does
not dissolve Corollary 1.2.** Goes in Ch4 §4.10 beside the existing five rivals.
**Cascade:** Ch4 §4.10; cross-ref from §6.2. João's viva question 3 is exactly this.
**Blocked by:** P-01, because the answer depends on which reading is carried.

### P-03 · M2 · Rewrite §6.1's opening · OPEN
It opens on "two provisions that cannot both be satisfied" — the most contested claim — and
contradicts Theorem 2. Lead with the robust result.
**Cascade:** Ch6 only. **Blocked by:** P-01.

### P-04 · M1 · Ground p(a) in a real audit-record format · OPEN
Nothing establishes that an audit record contains clinical content. IHE ATNA records
participant objects, not documents. Research task first: the eHDSI audit specification and
TEHDAS2 D7.4 logging requirements. Then either cite evidence that repositories retain payload
content, or reframe Semantics I as the semantics of a rich audit log and say how common that
is.
**Cascade:** Ch4 (8 × `p(a)`, 24 × payload) is the definition site. Ch3 6 × payload, Ch5 13 ×,
Ch6 3 ×. Also `trf_checker.py` — the SPE record's payload is currently the log string itself,
which João noticed. And Rival 3 in §4.10 already concedes the point, so that passage needs
reconciling with whatever we decide.
**Note:** if p(a) cannot be grounded, the cross-border instance of Theorem 1 weakens. Do this
after P-01, before any Ch4 prose work.

### P-05 · M3 · Salt and ciphertext design · OPEN · **do this first, it is cheap**
Three sub-items, independent of everything else:
- **P-05a** Decide: destroy the salt at invalidation, keep it, or store it under k(a). João's
  substantive point is that a salt beside the metadata is a guess-confirmation oracle for
  low-entropy payloads — exactly the threat §4.9 says it defends against.
- **P-05b** Decide the ciphertext: nothing in Semantics II needs it once the key is gone.
  Deleting it removes the ten-year harvest-now-decrypt-later risk §4.9 calls "unavoidable".
- **P-05c** Remove the dead branch at `trf_checker.py` line 63:
  `self.salt = os.urandom(16) if False else bytes([...])`. Replace with a seeded generator or
  an explicit `--reproducible` flag.

**Cascade:** Ch4 §4.8 and §4.9 (7 × salt) · Ch5 §5.6 (2 ×) · Appendix A (19 ×) ·
`trf_checker.py` (6 ×, in 5 copies) · the recorded console output in A.13 · the 21 Sept change
record entry · `CHANGE_TRAIL.md`.
**Own it in the text:** the contradiction is ours, introduced 28 Sept. Whatever we decide, the
change record should say so rather than presenting it as a clean choice.

### P-06 · M5 · The ten-year floor source · OPEN
F = 120 drives the abstract, Corollary 1.1 and Table 5.1, sourced only to Simjanoska Misheva
et al. (2025), a JMIR tutorial on AI Act compliance. Find the eHDSI/MyHealth@EU primary
document adopted by eHMSEG with a section number, or present 120 months as illustrative.
**Cascade:** Ch1 4 × · Ch2 3 × · Ch4 1 ×. If it becomes illustrative, the abstract and
Corollary 1.1 wording change, and Corollary 2.2 (F-independence) becomes the load-bearing
defence rather than a supporting one.

### P-07 · M5 · Align the SPUHiN "finalised" claims · OPEN
The thesis says the gap "survives the final national document"; we established on 28 Sept
that D5.2's hearing version has no stable locator and the consultation page 404s. §6.8 already
concedes the absence is "observed in the published checklists rather than established against
the full deliverable". Make every claim match what was actually inspected.
**Cascade:** Front Matter 2 × (Statement of Contribution) · Ch1 2 × · Ch2 5 × · Ch4 2 ×.

### P-08 · M5 · Quote Art. 68(12) and Art. 73(1)(e) verbatim · OPEN
The location-versus-provenance argument in §4.6 turns on exact wording, and the provisions are
only paraphrased. Quote the Official Journal English text. João suggests checking one further
language version since CJEU interpretation compares them — worth doing for Art. 68(12) given
P-01 rests on it.
**Cascade:** Ch4 §4.6 primarily; Ch1 and Ch2 where the provisions are introduced.

### P-09 · M5 · Fix the §2.2 EHDS dates · OPEN
"Designate a digital health authority by June 2025" and "certify systems by January 2026",
sourced to an EY tax alert, conflict with the Art. 105 dates in the same paragraph. Verify
against the Regulation and drop the law-firm source.
**Cascade:** Ch2 §2.2. Removing EY may leave it uncited elsewhere — check before deleting the
bibliography entry.

---

## STRONGLY RECOMMENDED

### P-10 · M4 · Hash-chain integrity in V_II, plus a tamper test · OPEN
`V_II` never tests condition (i), "intact and unmodified" — it only checks that m(a), c(a) and
ι(a) are present, so it passes by construction. Chain m(a) and ι(a) entries with a hash chain
and add a test showing V_II fails when metadata is altered.
**Do this regardless of the renaming decision.** It is a few lines of code and it answers the
viva question "what does the formal apparatus add".
**Cascade:** `trf_checker.py` in 5 copies · Ch4 §4.7 definition of V_II · Ch5 §5.5 results ·
Appendix A listing · the recorded runs · possibly a new app tab.

### P-11 · M4 · Rename theorems to propositions · NEEDS TIGER
Only if P-12 is done too. João calls the results definitional; doing the demotion without the
promotion weakens the thesis for nothing.
**Cascade:** everywhere "Theorem 1", "Theorem 2", "Corollary" appears — all seven chapters,
both appendices, the code comments, the app.

### P-12 · M4 · Promote §6.9a's anchoring result into Chapter 4 · OPEN
João calls it "the best analytical result in the thesis" and it sits in an unnumbered
subsection of the Discussion. The result: a floor and a ceiling anchored to the same event are
jointly satisfiable under Semantics I whenever the ceiling is at least as long as the floor; a
ceiling anchored to an external event can cross the floor.
**Cascade:** new formal result in Ch4 · §6.9a becomes a cross-reference · Ch7 contributions ·
the abstract. This is also the answer to João's M7 (logistics framing) — see P-14.

### P-13 · M6 · Traceability matrix against TEHDAS2 D7.4 and the SPUHiN checklist · OPEN
The minimum evaluation strengthening he recommends. Turns the prose integration analysis of
§4.11 into something checkable.
**Cascade:** Ch4 §4.11 · Ch3 §3.7/§3.8 evaluation framing · possibly a new appendix.

### P-14 · M7 · Logistics framing · OPEN
§1.4 overreaches: "imports a solution structure that logistics has operated for decades". Add
one or two concrete anchors — João suggests Union Customs Code record-keeping (floor anchored
to the declaration) against destruction orders for seized goods (externally anchored ceiling),
tested against the §6.9a anchoring result. State plainly in §1.5 how the thesis sits within
Sustainable Energy Logistics.
**Cascade:** Ch1 §1.4 and §1.5 · Ch2 §2.7 · connects to P-12.

### P-15 · M6 · Reword Appendix C item A1 · OPEN
A1 asserts the mechanism gives auditors "full confidence", which §6.3 does not claim. **João
has released us in writing:** "the candidate may reword A1, and it should be reworded."
Reword, record in one line, cite the review.
**Cascade:** Appendix C §C.6 · our own §C.1a, which currently gives the superseded reasoning
for keeping it.

---

## MECHANICAL — parallel, no dependencies

### P-16 · Minor issues · OPEN
- §3.6: checker "fifty to one hundred lines", realism layer "two to four hundred" — actual 363
  and 152, and inverted
- §3.6: "tuples defined in Section 3.4" → Section 4.3
- §1.6: drop "accumulator-based" — the accumulator is unimplemented
- §2.1.4: text says four dated rounds; Appendix B now has five
- §3.4 and Cor 1.1: "the ordinary case", "the generic case" are frequency claims that §3.7
  forbids — soften both
- §4.4 C1: the closed window [t(a), t(a)+F] spans F+1 months — justify or make half-open
- Table 5.0a, A.9c, A.14: "Section 6.9" → §6.9a
- Appendix C preamble: "Section 3.9" → §3.8
- §5.7, §6.1, §7.2: "an separately written" → "a separately written" (3 ×)
- §5.3, §5.4, §5.6: witness lines run together in one quote block → code block, one per line
- §6.1: "thirty-nine concrete witnesses" → "witnesses in the model"
- §1.5: remove the reference to a separate addendum examiners will not see, or add it as an
  appendix

### P-17 · Renumbering · OPEN
§5.5a and §6.9a are unnumbered; Appendix A runs A.1, A.1b … A.14, A.11b. Renumber sequentially
and regenerate the TOC — Ch7 currently shows p. 102, the same as §6.11.
**Do this last.** Every cross-reference in the thesis points at the current numbers, and P-12
adds a new Ch4 result which shifts them again.

### P-18 · Cut defensive meta-commentary · OPEN
"stated rather than buried", "recorded rather than concealed", "a reader is entitled to", "an
examiner's first reaction will be", "honest/honestly" — roughly 50 occurrences. Cut by at
least half; let §3.7 do the work.
**Note for whoever does this:** the habit came from how this project works, where stating the
limit explicitly is right in conversation. It does not transfer to the document.

### P-19 · Cut repetition · OPEN
Norwegian NCPeH pilot details appear in §1.1, §2.2, §2.6, §4.11, §6.8 and §7.6. The Art. 68(12)
reading is argued in full in §1.1, §2.3, §4.6, §6.2 and §7.4. Say each once, then cross-refer.
**Blocked by P-01** for the 68(12) passages — no point deduplicating an argument that is about
to change.

### P-20 · Move the Version and Change Record to the repository · OPEN
Also trim the self-referential process material: the abandoned May draft, its fabricated
citations, the withdrawn ethics claim, the "reviewer-found" gaps. Keep one concise statement in
the Declaration in HiMolde's required form.
**Cascade:** Front Matter · Ch2 §2.1 · Ch3 §3.9 · Ch6 §6.10 · the repository gains the record.

### P-21 · Slim Appendix A · OPEN
~12,000 words of source listings. Replace with the tagged repository, file SHA-256 hashes and
the core functions of `trf_checker.py` only.
**Blocked by P-22** — needs the tag to exist first.

### P-22 · Tag the repository and mint a Zenodo DOI · OPEN
The thesis cites a moving `main`. Tag at `dba9c56` or later, archive on Zenodo, cite the DOI.
**Cascade:** every repository citation in the thesis · Appendix A · the README.

### P-23 · Title page logo placeholders · NEEDS TIGER
`N:\ADMARKIV\…` and `C:\Users\lovold\…` appear as placeholders. Check the images render in the
PDF. This came from the HiMolde template, so it resolves when the template is obtained.

---

## Carried forward, not from João

- Two unread sources: aiAuthZ (arXiv 2607.05518), privacy-engineering SLR (arXiv 2606.23696)
- Two figures: record-state diagram (§4.8, reprised §5.6), regulatory timeline (§6.8). The
  thesis still has **zero figures**
- HiMolde template — unobtainable from this environment, blocks all formatting decisions
- Datatilsynet informal sounding
- Sikt notification, if the evaluation is run
- `assemble.py` dedup rule keeps the longer variant, so a long unlinked reference beats a short
  linked one

---

## Working rules for this queue

1. **Nothing is DONE until it is applied in the chapter file, the assembly rebuilt, the
   register updated and the change trail written.** A patch in one place is not a patch.
2. **Run `inspector.py` before and after every prose change.** Gains-only is the pass; losses
   need explaining.
3. **Grep the cascade before editing, not after.** The counts above are from today and will
   drift as we work.
4. **When a fix changes a reported figure**, the app's Tab 1 self-assertion, the recorded runs
   in `docs/`, and `repro_package/results/` all need regenerating, and the fresh-clone check
   must pass again.
5. **P-01 gates P-02, P-03, P-04 and the 68(12) half of P-19.** Do not start those.
6. **P-17 goes last.** Renumbering before the content settles means doing it twice.
