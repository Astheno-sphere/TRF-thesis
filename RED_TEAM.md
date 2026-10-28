# RED TEAM — a panel built to fail VERA-SNARK, and how it holds

Purpose: stress every flank of the thesis as a hostile examination committee would, before João and
the real examiners do. For each attacker: the kill-shot in the words they'd actually use, the defence
drawn from what the thesis already says (section-cited), the residual risk, and the action to close it.
Run order for prep: internalise the **defence doctrine** (bottom) first, then drill R3 and R4 — the two
live flanks — until the one-sentence answers are reflex.

Anchor state: branch joao-base, body ~48k, REVIEW_TRACKER ~90% closed.

**PATCH STATUS (28 Oct 2026).** R4 residue → P85 (EDPB 02/2026). Overclaim #1/#3 (§6.1 rhetoric>math, correlated checks) → P86. R3b/R3c/R3d + R5-energy-framing (B) → P87 (narrow-reading concession + verifiability-semantics recentre; necessity hedged; cross-border Cor 2.3 concession; energy application made explicit). R5 resolved as **B+C** (framing sentence + viva defence; no new worked case near submission — João's call on adequacy). R1/R2/R6/R7 assessed as already-defended in text (no edit). Remaining = viva drilling of R3b/R3d + R5, and the non-text submission items (João on length, Zenodo DOI, logos, coordinator AI sign-off).

---

## R1 — The Cryptographer: "This is crypto-shredding with a new name."
**Kill-shot:** "NIST SP 800-88 and every cloud vendor already destroy a key to erase ciphertext. There
is no cryptographic contribution here."
**Defence:** Correct, and the thesis claims none (§2.4, §2.10 state the primitives are established). The
contribution is the *feasibility result* — when key-destruction jointly satisfies three concurrent legal
clocks — and the *verifiability semantics* that let an auditor confirm what was invalidated, when, and on
what ground. Crypto-shredding is the tool; the tri-lateral model and the invalidation semantics are the work.
**Residual:** low. **Action:** one-sentence answer ready: "novelty is the tri-lateral feasibility result and
the invalidation semantics, not the primitive."

## R2 — The Formal-Methods Purist: "Your propositions aren't proofs."
**Kill-shot:** "Informal arguments, no proof assistant. Calling them Propositions dresses up observations."
**Defence:** Deliberate and declared (§3.4, §4.1): the formalism is intentionally light because the conflict
is *definitional*, not deep. Proposition 1 is near-trivial by design — that is the point. The results are
checked three ways: executable checker, exhaustive search on small instances, and a bounded Z3 SMT check
that finds no counterexample and *does* refute deliberately broken variants (§5.5, Appendix A.23/A.24).
**Residual:** low-medium. **Action:** have the Z3 result and "elementary on purpose" framing crisp; concede
the ceiling, redirect to the §4.2 necessity analysis where the weight sits.

## R3 — The Data-Protection Lawyer: "You invented this conflict, and you're playing lawyer." (LIVE FLANK)
**Kill-shot:** "Article 68(12) reaching access logs is your guess. Read it narrowly and your headline
collapses to a bilateral floor-vs-right that practitioners already handle. You are a logistics student
issuing legal interpretations the EDPB has not."
**Defence, three moves:**
1. *The thesis never asserts the broad reading as settled.* §2.3 and §4.6 give both sides; Corollary 1.2
   is explicitly conditional; the headline is the *feasibility reframing* (semantics), which does not depend
   on the broad reading at all.
2. *The structural tri-lateral result survives the narrow reading.* Even narrowly, the cross-border floor +
   Article 17 right + the ceiling on the permitted dataset stand; Proposition 1 needs only that some valid
   erasure request fall inside a retention window.
3. *The interpretive steps are flagged as interpretive, with a route to settle them* — the Datatilsynet
   enquiry (sent 23 Sep 2026) and the now-answered Helsedirektoratet enquiry (19 Oct 2026). The thesis
   argues from primary instruments + Norwegian DPA guidance; it claims no authority it lacks.
**Residual: this is the flank.** **Action:** drill move 2 ("even on the narrow reading, here is what
survives") to reflex. HARDEN with current authority (see Research Hardening below): EDPB Guidelines
1/2026 on scientific research (Art 17(3)(d) is a case-by-case, not blanket, refusal) and the Sidley/
academic commentary confirming the EHDS↔GDPR tension is real and widely recognised, not invented.

## R4 — The Systems/Deployment Engineer: "You demonstrated nothing real."
**Kill-shot:** "200 synthetic records, no NCPeH, key destruction you *simulate*. You showed the code runs,
not that the mechanism works; and your surviving residue is still personal data."
**Defence:** §5.8 proves no result depends on payload content (real FHIR changed every commitment, zero
figures); the sandbox validates *implementation*, and representativeness is required of the *infrastructure
analysis* (Ch4), not the records. Key destruction is scoped exactly as NIST SP 800-88 and the EDPB scope
it — conditional on a documented key-management boundary, stated as *attested, not proven* (§3.7, §6.3).
The residue is explicitly treated as *pseudonymised, not anonymous* (§4.9) and assessed against the
threshold rather than assumed to clear it.
**Residual: medium** (the residue sub-attack). **Action:** HARDEN §4.9 with EDPB Guidelines 02/2026 on
Anonymisation (the current three-criteria test; encryption ≠ anonymisation; risk rises over time) — see below.

## R5 — The Logistics Professor: "Is this even a logistics thesis?"
**Kill-shot:** "This is law-and-cryptography wearing a Sustainable Energy Logistics badge."
**Defence:** §2.7 — the CSCMP definition makes logistics the forward/reverse flow *and storage* of goods,
services, **and related information**; perishable-inventory theory gives the two-clock structure; the
customs-record analogy and Elhub's retention-per-category ground it in practice. An audit record is related
information with a storage-and-disposal problem. This is the home flank — win it in 30 seconds.
**Residual:** low. **Action:** rehearse the one-paragraph "why this is logistics."

## R6 — The Prior-Art Hunter: "DePaul already did this."
**Kill-shot:** "US Patent 12,425,209 keys records by purge date and destroys the key. What is actually yours?"
**Defence:** §2.4 distinguishes it on three axes — DePaul is *bilateral* (two floors, known purge date),
operates on database values not the cross-border audit trail, and supplies *no verifiability semantics*.
The tri-lateral case *inverts* the design (a ceiling not a second floor; an erasure request at an arbitrary
subject-chosen time), which is what makes joint satisfiability non-trivial.
**Residual:** low. **Action:** know the three deltas cold.

## R7 — The Relevance Skeptic: "You're solving a 2029 problem."
**Kill-shot:** "The secondary-use provisions don't apply until 26 March 2029. This is premature."
**Defence:** that is the *opportunity*, not a weakness (§6.8): the Article 73(5) implementing acts are due
26 March 2027 and the TEHDAS2 SPE specifications are being drafted now. A framework that arrives before the
infrastructure hardens can shape the defaults; one that arrives after is archaeology. The Norwegian NCPeH is
already in live pilot, so the cross-border audit stream is beginning now.
**Residual:** low. **Action:** lead with "arrives while the specs are open," not "applies in 2029."

---

## Defence doctrine (the method, for every question)
1. **Concede the true part first.** The thesis's honesty is the armour — an examiner who finds the limitation
   already stated in the text has nothing left to swing.
2. **Then bound it.** Say exactly how far the concession reaches and where the result still stands.
3. **Then point to where the thesis already says so** (section number). Never improvise a new claim under pressure.
4. **Never over-claim.** No "proven" for what is attested; no "anonymous" for what is pseudonymised; no
   "established requirement" for what is illustrative.
5. **Redirect to the weight-bearing wall:** the §4.2 necessity analysis and the mechanism design, not the proofs.

## Research hardening (current authority located 28 Oct 2026 — fold in as gated edits)
- **EDPB Guidelines 02/2026 on Anonymisation** (Version 1.0, adopted 7 July 2026): the current three-criteria
  test (No Record Isolation / No Linkage / No Inference); encryption is "by its very nature reversible" and
  is not anonymisation (para 91); technical measures "not by themselves sufficient" (para 90); re-identification
  risk rises over time, and data that is no longer anonymous "should again be considered personal" (para 35).
  → Hardens §4.9 (R4 residue flank) and §2.3 corridor: cite as the live standard against which the invalidation
  residue is assessed; confirms the thesis's "pseudonymised not anonymous" framing. Status: FINAL, citeable.
- **EDPB Guidelines 1/2026 on scientific research** (adopted 15 April 2026, in public consultation to 25 June
  2026): Article 17(3)(d) erasure refusal is a fact-specific, case-by-case assessment, not a blanket exemption.
  → Supports §4.4. Status: DRAFT — cite as draft/in-consultation, per the thesis's source-standing rule.
- The EHDS↔GDPR retention/erasure tension is treated as real and open across 2026 professional and peer-reviewed
  commentary (law-firm analyses; a 2026 peer-reviewed study of the EHDS/GDPR interplay) → corroborates the
  conflict premise against R3's "you invented it." Verify each before citing.
