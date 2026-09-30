# Patches — João Round 3

The working list. One entry per patch. **Nothing here is applied yet.**

**How to use this file.** Each patch has an ID, a status, the files it touches, and a
*cascade* line naming what else has to move when it does. Update the status line as you go
and add the verification actually run. When a patch changes something another patch depends
on, say so in the cascade of both.

**Status values:** `OPEN` · `BLOCKED (waiting on <decision>)` · `IN PROGRESS` · `APPLIED` ·
`VERIFIED` · `REJECTED (reason)`

**Rule carried from the failure ledger:** a patch is not `APPLIED` until the diff exists, and
not `VERIFIED` until a check was run and named. The trail has been wrong five times.

---

## Wave 0 — Decisions that gate everything

These are not patches. They are answers needed before patches can be written.

### DEC-1 · Which reading of Art. 68(12)? · **BLOCKING**
Tiger's call. `DECISION_RECORD.md` O-01. Option A (formalise C3 over m(a), concede SPE
infeasible under both semantics, present as a drafting defect) or Option B (Art. 73(1)(e) as
lex specialis). Either way Rival 6 must be answered.
**Blocks:** P-M2-*, P-M4-*, and all Chapter 4, 6 and 7 prose work.

### DEC-2 · Salt and ciphertext design?
Three sub-questions: destroy the salt at invalidation, keep it, or store it under k(a);
delete the ciphertext or justify keeping it; replace the `if False` branch with a seeded
generator or a `--reproducible` flag.
**Blocks:** P-M3-*.

### DEC-3 · Rename theorems to propositions, and promote §6.9a into Chapter 4?
Do both or neither. The V_II integrity test happens regardless.
**Blocks:** P-M4-1, P-M4-2.

---

## Wave 1 — M2, the Art. 68(12) reading · BLOCKED on DEC-1

### P-M2-1 · Carry one reading consistently through the model
**Files:** `Chapter4_TRF_Model_v1.md` §4.6, §4.8
**What:** If Option A, formalise C3 over the identifying fields of m(a), not payload
accessibility α alone. State that on the broad reading the SPE case is infeasible under both
semantics.
**Cascade:** Corollary 1.2's status changes → Ch5 §5.4 reports it → Ch6 §6.2 discusses it →
Ch7 §7.2 claims it → the Abstract and Statement of Contribution claim it. **Five downstream
locations.** Also: §4.8's sentence "the environment is thereby cleared of accessible personal
data at the ceiling while continuing to satisfy the floor" no longer follows and must go.
**Verify:** grep every occurrence of "Corollary 1.2" and confirm each states the same thing.

### P-M2-2 · Add Rival 6, log relocation
**Files:** `Chapter4_TRF_Model_v1.md` §4.10
**What:** If the ceiling is locational, exporting the access logs out of the SPE at permit
closure satisfies both provisions literally, with no cryptography. Say why that does not
dissolve Corollary 1.2.
**Cascade:** §4.10 currently says five rivals; the count appears in §1.6 and §7.3. Ch6 may
need a sentence. **This is viva question 3 and there is currently no written answer.**
**Verify:** grep "five rivals", "five alternatives".

### P-M2-3 · Rewrite §6.1's opening
**Files:** `Chapter6_Discussion_v1.md` §6.1
**What:** It opens on "two provisions that cannot both be satisfied" — the most contested
claim — and contradicts Theorem 2. Lead with the robust result.
**Cascade:** none outward. Depends on P-M2-1 being settled first.
**Also here:** "thirty-nine concrete witnesses" → "witnesses in the model" (minor table).

---

## Wave 2 — M1, grounding p(a) · BLOCKED on DEC-1, then research

### P-M1-1 · Define p(a) per record class
**Files:** `Chapter4_TRF_Model_v1.md` §4.3
**What:** Name the fields, per record class, grounded in the eHDSI audit specification and
TEHDAS2 D7.4. Either cite evidence that audit repositories retain payload content
(`ParticipantObjectQuery`, `ParticipantObjectDetail`, retained query text or outputs in an
SPE), or reframe Semantics I as the semantics of a rich audit log and say how common that is.
**Research needed first:** the eHDSI audit specification. We have never cited it. It is also
the source M5 wants for the ten-year floor — **one retrieval closes two items**.
**Cascade:** if Semantics I is reframed, §4.5's definition changes → Theorem 1's scope changes
→ Ch5 §5.3's framing changes → Ch2 §2.3's problem statement may change → the Abstract. Rival
3 in §4.10 already concedes the point and will need rewording so it does not contradict the
new §4.3.
**Verify:** inspector on Ch4; grep "payload" across all chapters for statements that assume
clinical content.

### P-M1-2 · Revise the SPE record model in the code
**Files:** `demo_app/trf_checker.py` + the four other copies, `docs/expected_*.txt`
**What:** The SPE payload is currently the string `<FHIR:AuditEvent spe-access ...>` — the log
itself. Make it match whatever P-M1-1 establishes.
**Cascade:** **If the payload bytes change, the mean payload figure changes.** Chapter 5
reports 891 and 1,006 bytes. Commitments change. The recorded runs in `docs/` must be
regenerated and the repository re-pushed. Appendix A's listing must be re-synced.
**Verify:** `python3 trf_checker.py | diff - docs/expected_trf_output.txt` after regenerating;
`bash repro_package/run_all.sh`; fresh-clone check.

---

## Wave 3 — M3, salt and ciphertext · BLOCKED on DEC-2, but cheap and independent

### P-M3-1 · Make text, code and change record agree on the salt
**Files:** `Chapter4_TRF_Model_v1.md` §4.8 §4.9, `Chapter5_Demonstration_v1.md` §5.6,
`demo_app/trf_checker.py` line 119 + four copies, `code_artefacts/README_Appendix_A.md` A.4
A.13, `CHANGE_TRAIL.md`
**What:** Whichever way DEC-2 goes, all six locations must say it. The code comment currently
cites §4.8 as authority for the opposite of what §4.8 says.
**Cascade:** if the salt is destroyed, §4.9's residue list drops r(a) → the anonymisation
argument in §4.9 changes → §6.3's attestation discussion may change. If the salt is kept,
§4.9 must answer João's oracle objection, which §4.9 currently raises against itself.
**Verify:** grep "salt" across all chapters and all five code copies; console output in A.13.

### P-M3-2 · Decide the ciphertext
**Files:** same set
**What:** Nothing in Semantics II requires the payload ciphertext once the key is destroyed.
Deleting it removes the ten-year harvest-now-decrypt-later risk that §4.9 calls
"unavoidable". Either delete it or justify keeping it.
**Cascade:** §4.9 currently calls that risk unavoidable. If the ciphertext goes, **that
sentence becomes false and must change** — this is a strengthening, not a concession.
**Verify:** grep "unavoidable", "harvest".

### P-M3-3 · Remove the dead branch
**Files:** `demo_app/trf_checker.py` line 63 + four copies
**What:** `self.salt = os.urandom(16) if False else bytes([...])`. Replace with a seeded
generator or an explicit `--reproducible` flag.
**Cascade:** the salt derivation must stay deterministic or every commitment changes and
every recorded run must be regenerated. **Use a flag, do not change the default.**
**Verify:** checker output byte-identical to `docs/expected_trf_output.txt`.

---

## Wave 4 — M5, primary sources · independent, can run in parallel

### P-M5-1 · The ten-year floor
**Files:** `Chapter1`, `Chapter2` §2.3, `Chapter4` §4.4, `Chapter5` Table 5.1, Abstract
**What:** F = 120 rests on Simjanoska Misheva et al. (2025), a JMIR tutorial on AI Act
compliance. Cite the eHDSI/MyHealth@EU primary document with a section number, or present 120
months as illustrative.
**Cascade:** if it becomes illustrative, Corollary 1.1's framing softens and the Abstract's
headline figure changes. Corollary 2.2 makes results F-independent, so the model is safe —
**the headline is not.**
**Note:** the same retrieval serves P-M1-1.

### P-M5-2 · Align the SPUHiN "finalised" claims
**Files:** `Chapter1` §1.2, `Chapter2` §2.6, `Chapter4` §4.11, Statement of Contribution,
`Chapter6` §6.8
**What:** Four locations say the gap "survives the final national document". The reference is
the hearing version with no stable locator, and §6.8 already concedes the absence is
"observed in the published checklists rather than established against the full deliverable".
Align every claim to what was actually inspected.
**Cascade:** this weakens a contribution claim in the Statement of Contribution. Expect it to
read less strongly and be correct. **Raised by João twice now — Round 1 and Round 3.**

### P-M5-3 · Quote Art. 68(12) and Art. 73(1)(e) verbatim
**Files:** `Chapter4` §4.6, `Chapter1` §1.1
**What:** The location-versus-provenance argument turns on exact wording, yet the provisions
are paraphrased. Quote the OJ English text. Ideally check one further language version, since
CJEU interpretation compares them.
**Cascade:** feeds directly into P-M2-1. Do this *before* deciding DEC-1 — **the wording is
the evidence for the decision.**

### P-M5-4 · Fix the §2.2 EHDS dates
**Files:** `Chapter2` §2.2
**What:** "designate a digital health authority by June 2025" and "certify systems by January
2026", sourced to an EY tax alert, conflict with the Art. 105 dates in the same paragraph.
Verify against the Regulation and drop the law-firm source.
**Cascade:** removes an Ernst & Young reference from the bibliography if it is not cited
elsewhere. Check before removing.

### P-M5-5 · Table 2.1 source bands
**Files:** `Chapter2` §2.8
**What:** Aikebaier (unreviewed ePrint), VeritasChain, SecuPi and OneUptime have rows
alongside peer-reviewed systems. Move to a footnote row or a separate practitioner band. Also
check whether Feng et al. (2022, arXiv) has a peer-reviewed version.
**Cascade:** §2.9's gap statement cites the table. VeritasChain is load-bearing for §2.5.

---

## Wave 5 — M4, what the formal apparatus adds · BLOCKED on DEC-3 except P-M4-3

### P-M4-1 · Rename theorems to propositions
**Cascade:** "Theorem 1", "Theorem 2", "Corollary 1.1", "Corollary 1.2", "Corollary 2.2"
appear across **all seven chapters, both appendices, the code comments and the repository
README**. This is the single widest-touching patch in the list. Do it with a script and the
inspector, not by hand.

### P-M4-2 · Promote §6.9a's anchoring result into Chapter 4
**What:** A floor and a ceiling anchored to the same event are jointly satisfiable under
Semantics I whenever the ceiling is at least as long as the floor. A ceiling anchored to an
external event can cross the floor.
**Cascade:** new numbered result in Ch4 → §6.9a becomes a discussion of it rather than the
result itself → §7.2 contributions list gains an item → Abstract may gain a clause.
**This is the one João calls the best analytical result in the thesis.**

### P-M4-3 · Make V_II test integrity · **not blocked, do it**
**Files:** `demo_app/trf_checker.py` + four copies, `Chapter5` §5.5
**What:** V_II only checks that m(a), c(a) and ι(a) are present. Condition (i), "intact and
unmodified", is never tested. Chain m(a) and ι(a) with a hash chain; add a tamper test that
makes V_II fail when metadata is altered.
**Cascade:** a new test means a new recorded run in `docs/` and a new figure in Ch5. It
converts a check that passes by construction into one that can fail — **which is the answer
to viva question 5.**
**Verify:** the tamper test must actually fail. A test that cannot fail is the defect being
fixed.

---

## Wave 6 — M6 and M7

### P-M6-1 · Traceability matrix
**Files:** new appendix or `Chapter4` §4.11
**What:** Requirement-by-requirement matrix of the mechanism against TEHDAS2 D7.4 and the
SPUHiN checklist. Turns §4.11's prose integration analysis into something checkable.
**Cascade:** strengthens the DSR evaluation step; Ch3 §3.8's evaluation description gains a
line.

### P-M6-2 · Reword Appendix C item A1
**Files:** `Appendix_C_Evaluation_Instrument.md` §C.6, §C.1a
**What:** A1 asserts "full confidence", which §6.3 does not claim. João has released us in
writing. Reword, record in one line, cite the review.
**Cascade:** §C.1a currently explains why A1 was *kept* verbatim. **That paragraph must be
rewritten or it will contradict the change.**

### P-M7-1 · Logistics framing
**Files:** `Chapter1` §1.4, §1.5, `Chapter2` §2.7
**What:** §1.4 overreaches ("imports a solution structure that logistics has operated for
decades"). Add a concrete anchor — Union Customs Code record-keeping (floor anchored to the
declaration) against destruction orders for seized goods (externally anchored ceiling), which
tests directly against §6.9a. State plainly in §1.5 how the thesis sits within Sustainable
Energy Logistics.
**Cascade:** if the customs anchor works it becomes a second instance of the anchoring result
→ feeds P-M4-2. If it does not, say so; a failed test of your own result is reportable.

---

## Wave 7 — Presentation, mechanical, last

### P-PRES-1 · Cut defensive meta-commentary by at least half
~50 occurrences of "stated rather than buried", "recorded rather than concealed", "a reader is
entitled to", "an examiner's first reaction will be", "honest/honestly".
**Cascade:** inspector will flag hedge changes. Hedges must not *weaken* — this is cutting
throat-clearing, not concessions. Check each individually.

### P-PRES-2 · Cut repetition
Norwegian NCPeH pilot in §1.1, §2.2, §2.6, §4.11, §6.8, §7.6. Art. 68(12) reading argued in
full in §1.1, §2.3, §4.6, §6.2, §7.4. Say once, then cross-refer.
**Cascade:** **do this after DEC-1**, or you will cut the version that survives and keep one
that does not.

### P-PRES-3 · Move the Version and Change Record to the repository
Front matter currently carries it. João wants the thesis to stand on its own with one concise
statement in the Declaration in HiMolde's required form.

### P-PRES-4 · Slim Appendix A
Replace full source listings with the tagged repository, file SHA-256 hashes and the core
functions of `trf_checker.py` only. Cuts roughly 12,000 words.
**Cascade:** requires the repository tag (P-REPO-1) to exist first.

### P-MIN-1 · The minor-issues table
Thirteen items from the review: line counts inverted in §3.6; "Section 3.4" → 4.3; drop
"accumulator-based" from §1.6; §2.1.4 four rounds → five; soften "the ordinary case" and "the
generic case"; C1's closed window spans F+1 months; "Section 6.9" → 6.9a in three places;
Appendix C preamble "Section 3.9" → 3.8; "an separately written" ×3; witness lines into code
blocks; §1.5's separate addendum; renumber §5.5a, §6.9a and Appendix A; title-page logo
placeholders.
**Cascade:** renumbering touches cross-references everywhere. Regenerate the TOC after.

### P-REPO-1 · Tag the repository and mint a Zenodo DOI
The thesis cites a moving `main`. Tag at or after `dba9c56`, archive, cite the DOI.
**Cascade:** every repository citation in the thesis and in Appendix A changes. Blocks
P-PRES-4.

---

## Cross-cutting cascade map

Read this before starting any patch.

- **DEC-1 touches:** Ch4 §4.6 §4.8 §4.10, Ch5 §5.4, Ch6 §6.1 §6.2, Ch7 §7.2, Abstract,
  Statement of Contribution. **Nine locations.**
- **P-M1-1 may touch:** Ch4 §4.3 §4.5, Theorem 1's scope, Ch5 §5.3, Ch2 §2.3, Abstract.
- **Any code change touches:** five copies of the file, the five recorded runs in `docs/`,
  Appendix A's listing, the repository, and possibly Ch5's reported figures.
- **P-M4-1 touches:** every chapter, both appendices, code comments, README.
- **Anything that changes a reported number touches:** Ch5 tables, the Abstract, the README's
  expected-output table, and `docs/expected_trf_output.txt`.

**The standing rule:** after any patch, run `assemble.py` and confirm the rebuild, run the
inspector on every chapter touched, and update `VERSION_REGISTER.md` and `CHANGE_TRAIL.md`
before moving on.
