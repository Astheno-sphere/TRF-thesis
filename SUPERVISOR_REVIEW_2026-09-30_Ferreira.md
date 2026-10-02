# Supervisor Peer Review — Prof. João Ferreira, 30 September 2026

**Status: UNRESOLVED. Nothing in this review has been actioned yet.**

**Added 2 Oct 2026.** The review came in two parts. The email text (`supervisor_review/review_email_text_2026-09-30.txt`) is his review and carries his authority. The returned Word file (`supervisor_review/Master_thesis_Abbasia_tracked_JF.docx`) is **our own draft** placed in the HiMolde template, carrying **47 tracked revisions and 27 comments** under his account, dated 29 Sept. Those revisions are drafted patches for his own points (Rival 6 and log relocation in §4.8/§4.10, salt and ciphertext text in §4.8–4.9, a new §6.1 opening, the A1 rewording, the SPUHiN "as published for consultation" wording, §1.4/§1.5 programme fit, the minor fixes). They are proposals, judged on evidence, not adopted on his name. The working copy is now exactly the text his revisions were made against (tag `joao-base-v1`), so every tracked change can be applied or rejected against its own anchor. The file also gives us the HiMolde template (company HSM, A4, logo, title page); its two logos are *linked* to paths on his machine and must be embedded before any PDF export.
This file captures the review, records what I verified against the files, and states
what each item actually demands. It is the primary input to the next work session.

**Verdict structure.** Four issues decide the outcome: M1, M2, M3, M5. Each is fixable
within the candidate's reach. M2 is the one that can cost the contribution if handled
badly, and it is the one to start with.

---

## What the review gets right that we did not see

Read this section first. These are not opinions, they are findings I checked.

### M2 is correct, and it is the most serious thing in the review

The argument: Corollary 1.2 requires the **broad** reading of Art. 68(12) — the ceiling
reaches all personal data within the SPE, including identifiable access logs. But the
mechanism retains m(a), which the thesis itself calls personal data (§4.8, §1.1, §6.1),
until month 12. So at t_π + 6 the SPE still holds personal data, and the ceiling is
breached **on the very reading that creates the corollary**.

Theorem 2 escapes only because C3 is formalised over payload accessibility α alone —
which is, functionally, the narrow reading. So the thesis uses the broad reading to
generate its sharpest result and the narrow reading to resolve it.

This is a real inconsistency. It was not caught by any check we ran because every check
we built tests whether the *code* matches the *stated* model. Nothing tested whether the
model's two halves are mutually consistent under one legal reading.

João's three options, and my read of them:

1. **Formalise C3 over m(a)'s identifying fields too, and concede that on the broad
   reading the SPE case is infeasible under both semantics.** This is the strongest
   option. It converts an inconsistency into a finding: the Regulation has a drafting
   defect that the Art. 73(5) implementing acts must resolve by 26 March 2027. The
   thesis loses "we solved it" for the SPE case and gains "we proved it cannot be solved
   as drafted", which is a better result and fits the policy-relevance argument already
   made.
2. Argue Art. 73(1)(e) is *lex specialis* to Art. 68(12) for logs. Resolves by
   interpretation, not by mechanism. Re-scopes every SPE claim.
3. Whichever is chosen, **Rival 6 must be answered**: if the ceiling is locational,
   exporting the logs out of the SPE at permit closure satisfies both provisions
   literally, with no cryptography at all. The thesis must say why that does not dissolve
   Corollary 1.2. This is the single question most likely to be asked in the viva and we
   have no answer written down.

Also required: rewrite §6.1, which opens on the most contested claim ("two provisions
that cannot both be satisfied") and contradicts Theorem 2.

### M3 is correct, and the contradiction is mine

Verified in the files on 30 September:

| Location | Says |
|---|---|
| Ch4 §4.8, line 182 | "The salt is stored with the metadata and is **not** destroyed at invalidation; destroying it would break the binding property" |
| Ch4 §4.9, line 196 | Residue includes r(a) |
| `trf_checker.py` line 119 | `rec.salt = None   # salt destroyed with the key (Ch4 §4.8)` |
| Appendix A.4, A.13 console | salt=None |

**The code comment cites §4.8 as its authority for doing the opposite of what §4.8 says.**

Provenance, stated plainly because the next session needs to know it was not a drafting
slip: on 28 September I diffed the public repository against the working set, found
`rec.salt = None` present only in the repository, concluded "the repository is ahead",
and propagated it to all five copies of the file. I logged it as safe on the grounds that
"the line changes no reported figure, which the byte-identical output establishes". That
was true and irrelevant. Byte-identical output proves the code is self-consistent, not
that it matches the specification. **No check we built compares code behaviour to the
prose model, and that is the gap this exposed.**

João's substantive point is separate and also right: a salt stored beside the metadata
turns the commitment into a guess-confirmation oracle for low-entropy clinical payloads,
which is exactly the threat §4.9 says the salt defends against. §4.8's justification may
be backwards. Decide the design, then make text, code, appendix and change record agree.

Also flagged and confirmed: `self.salt = os.urandom(16) if False else bytes([...])` at
line 63 is a dead branch. Replace with a seeded generator or an explicit
`--reproducible` flag.

### M1 is correct and we never questioned the premise

The entire model splits a record into m(a) and a clinical payload p(a). **Nowhere does
the thesis establish that a real audit record contains clinical content.** IHE ATNA
records participant objects — patient identifier, document identifiers, sometimes query
parameters — not the retrieved document. If eHDSI audit repositories hold no payload,
Semantics I describes a practice nobody follows and the cross-border instance of
Theorem 1 is vacuous.

Note the internal evidence João spotted: Rival 3 in §4.10 already concedes this, and the
SPE record's payload in the code is the string `<FHIR:AuditEvent spe-access ...>` — the
log itself, not a clinical document.

This is the deepest of the four, because it questions the object of study rather than a
claim about it.

### M5 is correct on the ten-year floor

F = 120 drives the abstract, Corollary 1.1 and Table 5.1, and rests on a single secondary
source (Simjanoska Misheva et al. 2025, a JMIR tutorial on AI Act compliance). Either
cite the eHDSI/MyHealth@EU primary document with a section number, or present 120 months
as illustrative. Corollary 2.2 makes results F-independent so the damage is contained,
but the headline figure is not.

The SPUHiN "finalised" claims are the same failure we already logged from the other
direction: our Round 5 verification established that D5.2's hearing version has no stable
locator and the consultation page 404s. The thesis nonetheless says the gap "survives the
final national document" in §1.2, §2.6, §4.11 and the Statement of Contribution. Align
every claim to what was actually inspected.

---

## Items where I would push back, for the candidate to decide

**M4, "the theorems are definitional."** João is right that Theorem 1 follows quickly from
V_I = α and that renaming to Propositions is defensible. But his own review calls §6.9a
"the best analytical result in the thesis" and asks for it to be promoted into Chapter 4
as a formal result. Those two moves together are the right response: demote what is
definitional, promote what is not. Do both or neither; doing only the demotion weakens the
thesis for no gain.

His concrete technical request is unambiguous and should simply be done: **V_II never
tests condition (i), "intact and unmodified".** Chain m(a) and ι(a) with a hash chain, add
a tamper test that makes V_II fail when metadata is altered. That is a few lines of code
and it converts a check that passes by construction into one that can fail. It also
answers the viva question "what does the formal apparatus add".

**Appendix C item A1.** João explicitly releases us: "The candidate may reword A1, and it
should be reworded. Keeping an item known to overstate the claim is unnecessary." Our
§C.1a reasoning — that silently correcting a supervisor's wording would misrepresent the
record — is now superseded by the supervisor saying so in writing. Reword A1, record the
change in one line, and cite this review.

**Length.** He measures the main text at ~38,000 words with the literature review at ~30%
of it, and Appendix A adding ~12,000 words of listings. He suggests replacing full
listings with the tagged repository plus SHA-256 hashes and only the core functions. That
is a clean win: it cuts roughly 12,000 words without losing anything a reader can't fetch,
and it forces the repository tag we need anyway.

---

## The review, as given

### Major concerns

- **M1** — p(a) not grounded in a real audit-record format. Define p(a) per record class
  with fields named, grounded in the eHDSI audit specification and TEHDAS2 D7.4. Either
  cite evidence that audit repositories retain payload content, or reframe Semantics I as
  the semantics of a rich audit log and say how common that is. Revise the SPE record
  model in the code to match.
- **M2** — On the broad reading, the mechanism does not satisfy the ceiling. Choose one
  reading and carry it through Corollary 1.2, Theorem 2, §4.8 and §6.1. Add Rival 6 (log
  relocation). Rewrite §6.1's opening.
- **M3** — Salt and ciphertext: specification, code and justification disagree. Decide the
  design; make text, code and change record agree. Nothing in Semantics II requires the
  ciphertext once the key is destroyed — deleting it removes the ten-year
  harvest-now-decrypt-later risk §4.9 calls "unavoidable". Fix the dead branch.
- **M4** — Theorems are definitional. Rename to Propositions; move weight to the necessity
  analysis (§4.2); promote §6.9a's anchoring result into Chapter 4 as a formal result; make
  V_II test integrity via hash chain plus tamper test; shorten Chapter 5.
- **M5** — Load-bearing claims need primary sources: the ten-year floor; SPUHiN
  "finalised"; verbatim quotation of Art. 68(12) and Art. 73(1)(e) from the OJ, ideally
  checking a second language version; the §2.2 EHDS dates sourced to an EY tax alert that
  conflict with the Art. 105 dates in the same paragraph; non-peer-reviewed sources given
  rows in Table 2.1 alongside peer-reviewed systems.
- **M6** — DSR evaluation thin. Minimum recommended: a requirement-by-requirement
  traceability matrix against TEHDAS2 D7.4 and the SPUHiN checklist. Optional: two or three
  written expert walkthroughs; check with Sikt and the HiMolde research office rather than
  assuming. Reword Appendix C A1.
- **M7** — Programme fit (LOG953). §1.4 overreaches ("imports a solution structure that
  logistics has operated for decades"). Add one or two concrete logistics anchors — Union
  Customs Code record-keeping (floor anchored to the declaration) against destruction
  orders for seized goods (externally anchored ceiling) is a candidate worth testing
  against §6.9a. State plainly in §1.5 how the thesis sits within Sustainable Energy
  Logistics.

### Strengths he names

Well-posed timely problem with real policy relevance via the Art. 73(5) deadline · making
"verifiable" an explicit parameter, called the most transferable idea · honest prior-art
handling of DePaul and US 12,425,209 · source discipline, every reference with a locator,
dated search log, correctly labelled structured narrative review · reproducibility with
public repo, fixed seeds, recorded runs, exhaustive cross-check with control · **§6.9a
called the best analytical result in the thesis** · rival designs in §4.10, Rival 4
handled particularly well.

### Minor and consistency issues

| Location | Issue | Fix |
|---|---|---|
| §3.6 vs Table F.2 / 5.0a | Checker "fifty to one hundred lines", realism layer "two to four hundred"; actual 363 and 152, inverted | Update the text |
| §3.6 | "tuples defined in Section 3.4" | Section 4.3 |
| §1.6 | "commitments and accumulator-based invalidation suffice"; accumulator unimplemented | Drop "accumulator-based" |
| §2.1.4 vs Appendix B | Text says four dated rounds; Appendix B now lists five | Mention round 5 in the table |
| §3.4, Cor 1.1 vs §3.7 | "the ordinary case", "the generic case" are frequency claims; §3.7 says no result is a frequency | Soften both |
| §4.4 C1 | Closed window [t(a), t(a)+F] spans F+1 months | Justify or use half-open |
| Table 5.0a, A.9c, A.14 | Refer to "Section 6.9" for politiregisterloven | Section 6.9a |
| Appendix C preamble | "execution status … Section 3.9" | Section 3.8 |
| §5.7, §6.1, §7.2 | "an separately written" (3×) | "a separately written" |
| §5.3, §5.4, §5.6 | Verbatim witness lines run together in one quote block | Code block, one line per witness |
| §6.1 | "thirty-nine concrete witnesses" reads as evidence about the world | "witnesses in the model" |
| §1.5 | Refers to a separate addendum examiners will not see | Remove or add as an appendix |
| Numbering | §5.5a, §6.9a unnumbered; Appendix A runs A.1, A.1b … A.14, A.11b | Renumber sequentially; regenerate TOC (Ch7 shows p. 102, same as §6.11) |
| Title page | Logo placeholders `N:\ADMARKIV\…`, `C:\Users\lovold\…` | Check images render in the PDF |
| Repository | Figures depend on the artefact but cite a moving `main` | Cite tag or commit `0d855a7`; archive on Zenodo with a DOI |

### Presentation, voice and length

- **Defensive meta-commentary.** "stated rather than buried", "recorded rather than
  concealed", "a reader is entitled to", "an examiner's first reaction will be",
  "honest/honestly" — roughly 50 occurrences. Cut by at least half; let §3.7 do the work.
- **Voice and ownership.** The declaration is appropriate, but the oral defence will test
  ownership. Bring the prose into the candidate's own voice, especially Chapters 4 and 6.
- **Self-referential process material.** The abandoned May draft, its fabricated citations,
  the withdrawn ethics claim, "reviewer-found" gaps. Keep one concise statement in the
  Declaration in HiMolde's required form; **move the Version and Change Record to the
  repository.**
- **Repetition.** Norwegian NCPeH pilot details appear in §1.1, §2.2, §2.6, §4.11, §6.8,
  §7.6. The Art. 68(12) reading is argued in full in §1.1, §2.3, §4.6, §6.2, §7.4. Say each
  once, then cross-refer.
- **Length.** ~38,000 words main text; lit review ~12,000 (~30%); Appendix A ~12,000 of
  listings. Check programme guidance; consider replacing full listings with the tagged
  repository, file SHA-256 hashes, and core functions only.

### Viva questions he supplies

1. What fields does an eHDSI audit record actually contain, and where in it is the payload?
2. On your broad reading of Art. 68(12), why is the identifiable metadata you retain not
   "data within the SPE"?
3. Why not simply move the access logs out of the SPE at permit closure?
4. After invalidation, what does the retained salt (or ciphertext) let anyone do, and who
   needs that?
5. Is Theorem 1 more than a restatement of the definition of Semantics I?
6. What does the information-logistics lens add beyond making the floor a per-record
   parameter? How does the thesis belong in Sustainable Energy Logistics?
7. If Datatilsynet answered your §7.4 question negatively, what would remain of the
   contribution?
8. Which parts of the text and code did you write yourself, and how did you verify the
   AI-assisted parts?

**Note:** these supersede `Viva_Preparation_Notes.md`, which was written before this review
and answers only three of the eight. Questions 1, 2, 3 and 4 are new and are the hard ones.
Q5 and Q6 are covered; Q7 and Q8 are partially covered.

### His priority order

Required: 1–5. Strongly recommended: 6–10.

1. Define p(a) per record class from the eHDSI audit spec and TEHDAS2 D7.4; revise the SPE record model and code (M1)
2. Resolve the Art. 68(12) reading consistently across Corollary 1.2, Theorem 2, §4.8, §6.1; add the log-relocation rival (M2)
3. Decide salt and ciphertext design; make text, code and change record agree (M3)
4. Replace the ten-year floor source with the eHDSI primary document, or re-present F = 120 as illustrative (M5)
5. Align SPUHiN "finalised" claims; quote Art. 68(12) and Art. 73(1)(e) verbatim; fix §2.2 EHDS dates (M5)
6. Rename theorems as propositions; promote §6.9a into Chapter 4; add hash-chain integrity to V_II (M4)
7. Add a TEHDAS2 D7.4 / SPUHiN traceability matrix; reword Appendix C A1 (M6)
8. Strengthen or trim the logistics framing; state programme fit in §1.5 (M7)
9. Cut meta-commentary and repetition; move the change record to the repository; slim Appendix A
10. Work the minor-issues table; renumber sections and appendices; tag and archive the repository

---

## Sequencing note for whoever picks this up

Do **not** start at item 1 and work down. The dependency runs the other way.

**M2 decides the shape of the thesis.** Which reading is carried through determines what
Chapter 4 proves, what Chapter 6 discusses, whether Corollary 1.2 survives, and what the
abstract claims. Every other edit to Chapters 4, 6 and 7 is wasted if it is made before M2
is settled. Settle M2 first, with the candidate, as a decision — it is his call, not a
research task.

**M1 may change the model.** If p(a) cannot be grounded, Semantics I must be reframed. That
touches Chapter 4's definitions. Resolve after M2 and before any Chapter 4 prose work.

**M3 is independent and small.** It can be done at any time and should be done early
because it is embarrassing and cheap.

**M5, minor issues, meta-commentary and length are mechanical.** They can run in parallel
with anything and should be last in priority but can be done by a session that has spare
capacity.

There are approximately six weeks to the 14 November submission.
