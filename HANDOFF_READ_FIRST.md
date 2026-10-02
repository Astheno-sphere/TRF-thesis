# HANDOFF — READ THIS FIRST

**Project:** MSc thesis, *Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the European Health Data Space*
**Author:** Arshad Akhtar Abbasia ("Tiger"), MSc Sustainable Energy Logistics, Høgskolen i Molde
**Supervisor:** Prof. João Ferreira
**Submission:** 14 November 2026 · **Defence:** first week of December 2026
**Handoff written:** 21 September 2026. Rebuilt 30 September 2026 after the supervisor's review. **Rebased 2 October 2026 onto the draft the supervisor reviewed — read §00 first.**

---

## 00. STATE ON 2 OCTOBER 2026 — the base was reset

**The working copy is now the draft Prof. Ferreira reviewed**, not the 30 Sept migration zip.
The two differed in 29 content edits; the zip also carried the Bodø opening (H-01), added after
the draft was sent. Commit `0438daf`, tag `joao-base-v1`, branch `joao-base`. The returned file
and its text are in `supervisor_review/`. See `DECISION_RECORD.md` D-14 and `FAILURE_LEDGER.md`
F-0.

**What this means for every other section of this handoff.** Sections 3, 8a and 10 were written
about the zip. Where they describe the *text*, check the base with grep before relying on them.
Known differences on the base:
- The opening is the draft's ("the most significant data-governance transformation"). H-01 is
  proposal C-1 in `patches/` on branch `zip-base-superseded`, and its two versions disagree on
  whether Finland is connected: unverified.
- §2.2 still carries the EY "June 2025 / January 2026" dates; Art 68(12) is still paraphrased;
  §4.8 still says the salt is not destroyed; §2.1.4 still says four rounds. These are the
  draft's defects, kept because the review refers to them. Fixes are queued in `PATCHES.md`.
- The base already has five rivals, the accumulator caveats, the F+1 window, the corrected
  witness count, the addressee split and the Norwegian abstract.

**Work already done once and queued.** Patches F1–R1 and AS-01 (branch `zip-base-superseded`,
scripts in `patches/` there) answer much of M1, M2, M3 and M5 and were source-verified on 30
Sept–1 Oct. They are candidates in `PATCHES.md` Wave −1, to be re-run on this base and judged
with the supervisor's own tracked change for each passage.

**Order of work from here.** (1) Control documents and package brought into line with this
base: done 2 Oct, see `CHANGE_TRAIL.md`. (2) The supervisor's feedback, starting with the
three gating decisions DEC-1 to DEC-3 in `PATCHES.md`, with DEC-2's salt part already settled.

---

## 0a. THE LIVE WORK (as written 30 Sept)

**Prof. Ferreira delivered a detailed peer review on 30 September 2026. Nothing in it has
been actioned.** It is captured, verified against the files, and sequenced in
`SUPERVISOR_REVIEW_2026-09-30_Ferreira.md`. Four issues decide the verdict: M1, M2, M3, M5.

**Do not work down his numbered list in order.** M2 — which reading of Art. 68(12) the
thesis carries — is blocking and is the candidate's decision, not a research task. It
determines what Chapter 4 proves and whether Corollary 1.2 survives. Every Chapter 4, 6 and
7 edit is wasted until it is settled. See `DECISION_RECORD.md` O-01.

Two things his review found that none of our automated checks could see, and one that was
our own drift:

- **M2:** the thesis uses the *broad* reading of Art. 68(12) to generate Corollary 1.2 and
  the *narrow* reading to resolve it via Theorem 2. Our checks test code against stated
  model; nothing tested whether the model's halves are consistent under one reading.
- **M1:** the model splits a record into metadata and a clinical payload, and nothing ever
  established that a real audit record contains clinical content.
- **M3:** `trf_checker.py` destroys the salt at invalidation while §4.8 says it is *not*
  destroyed — and the code comment cites §4.8 as its authority. This was introduced on 28
  September by syncing the working set to the repository without checking the prose agreed.

---

## 0b. The document set, and what each is for

| File | Read it when |
|---|---|
| **`SUPERVISOR_REVIEW_2026-09-30_Ferreira.md`** | First. It is the live work |
| **`PATCHES.md`** | To do the work. Seven waves, three gating decisions, and the cascade map |
| **`DECISION_RECORD.md`** | Before reopening anything. Settled decisions with alternatives rejected; ten open decisions |
| **`SUPERVISOR_FEEDBACK_HISTORY.md`** | For what he has asked before and the patterns across rounds |
| **`FAILURE_LEDGER.md`** | Before trusting any claim, including in this file |
| **`NUANCES.md`** | Before the first reply. How Tiger works and what he rejects |
| **`MASTER_MANIFEST.md`** | To find out what a file is or whether a copy is current |
| **`VERSION_REGISTER.md`** | To verify nothing has drifted. It is the contract |
| **`CHANGE_TRAIL.md`** | For the full history — but see the failure ledger first |
| **`CONVERSATION_LINEAGE.md`** | To find which session did what, and how to reference this one |
| **`RESUME_PROMPT.md`** | The paste-ready prompt for a new conversation |
| `Viva_Preparation_Notes.md` | Partly superseded — João supplies eight questions, four of them new |

---

## 0. How to resume in a new conversation

1. Attach this file, `VERSION_REGISTER.md`, and the canonical files it lists.
2. Read sections 1–5 before touching anything. They contain the locked decisions and the corrections that must not be reintroduced.
3. Reconcile against the register: every canonical file carries an md5 checksum. A mismatch means drift — resolve it before editing.
4. Use the tools in `handoff_tools/`. Every rewrite must pass `inspector.py` (section 7).
5. Continue from section 9, which lists open work in priority order.

The rule that governs everything: **every claim is anchored to a verifiable source, and nothing is reported as done unless it was checked.** When a check can't be run, say so.

---

## 1. The thesis in one paragraph

EHDS Regulation (EU) 2025/327 puts cross-border health audit records under three kinds of obligation at once: *retention floors* (ten years for MyHealth@EU audit repositories under the eHDSI baseline; one year for Secure Processing Environment access logs under Art 73(1)(e)), the *GDPR Art 17 erasure right*, and a *deletion ceiling* (Art 68(12): data out of an SPE within six months of permit expiry). The **Tri-Lateral Retention Feasibility (TRF) Model** treats these as constraints over a single binary variable per record — payload accessibility α(a,t) — with the meaning of "verifiable" as an explicit parameter. **Theorem 1:** under plaintext verifiability (verifiable = readable) the system is infeasible whenever a deadline falls inside a retention window. **Theorem 2:** under accountability-preserving verifiability (metadata intact + commitment survives + invalidation logged) it is satisfiable for every arrival pattern and every floor. The mechanism, **Crypto-Erasure by Invalidation**, destroys a per-record key, keeps a hiding commitment and metadata, logs the invalidation as a first-class event, and performs a terminal transition at floor expiry.

**The honest size of the contribution:** it is a *reframing* — the conflict comes from an unstated assumption about what "verifiable" means, and dropping it resolves the conflict. No cryptographic primitive is new; the formal method (Feng et al. 2022) is established; Theorem 2's mathematical content is modest (the thesis says so, §4.7). Theorem 1 carries the load: it shows *some* departure from current practice is unavoidable.

---

## 2. Locked decisions — do not relitigate

| Decision | Where |
|---|---|
| Art 73(1)(e) absorbed as a second *floor instance*; model stays tri-lateral by **constraint type**, not instrument count | Ch1 §1.3, Ch3 §3.4, Ch4 §4.3 |
| Research question generalised to "audit-retention floors" | Ch1 §1.3 |
| Research question (102 words) **not shortened** without Tiger's decision | Ch1 §1.3 |
| Ch4: cross-border case first, SPE case second | Ch4 |
| Evaluation instrument stays **designed, not executed** (supervisor's recommendation, accepted). No Sikt, ethics position unchanged | Ch3 §3.8, Ch6 §6.6, App C |
| Page count over 80 acceptable if work is good | — |
| Corollary 1.2 is **conditional** on the broad reading of Art 68(12); only Cor 1.2 depends on it | Ch4 §4.6 |
| Semantics II is an *argument*, not an authority; stated as the thesis's main vulnerability | Ch6 §6.2 |
| Accumulators are **specified, not implemented** | Ch4 §4.8, Ch6 §6.1 |
| Invalidation entry is an **attestation**, not a proof | Ch4 §4.7, Ch6 §6.3 |
| Literature review is a **structured narrative review**, not systematic. No PRISMA diagram (counts not retained) | Ch2 §2.1 |
| Boolean strings in §2.1.6 are **prospective**, not a record of what ran | Ch2 §2.1.6 |
| VERA-SNARK name retained; thesis contains no SNARK; ZKP returns as future work (Aikebaier open problem 4) | Ch1 §1.6, Ch7 §7.5 |

---

## 3. Corrections already made — never reintroduce

*Facts, not a claim about the base's text: several of these are not yet in the reviewed draft. Grep before relying on one (see §00).*

These were each found, verified and fixed. A future edit that reverses any of them is a regression.

**Facts**
- NIST SP 800-88 Rev 2 is **2025** (26 Sept 2025, Chandramouli & Hibbard), not 2024.
- EHDS: adopted 11 Feb 2025, OJ 5 Mar 2025, **in force 26 Mar 2025**, applies generally **26 Mar 2027**, secondary-use Chapter IV (Arts 68, 73) applies **26 Mar 2029**. SPE implementing acts due **26 Mar 2027** (Art 73(5)).
- Helsedataservice is the **presumptive** HDAB, **not yet formally designated** (Norway had not appointed a coordinating HDAB under Arts 55–59 per the 2025 hearing response). Never "designated".
- SPUHiN D5.2 published checklists **do not address** the retention–erasure question. Never "acknowledge".
- D5.2 title: *Recommendations for minimum requirements for Secure Processing Environments in Norway*, Deliverable D5.2, Milestone M10, project 101128232. João's alternative title was not verified.
- Norwegian NCPeH pilot: live at Bodø and Stjørdal, receiving from Portugal, Czechia and (per the fork; the main line says only Portugal and Czechia; unverified) Finland; **no relevant patients had yet presented**. In 2026 the project began establishing **NCP-A** (outbound contact point). Both claims are sourced to Helsedirektoratet (2026a).
- eHOMB approval date: **12 March, year not recoverable** from the public record. Dateless is final. An earlier inference of "2025" was invalid and has been withdrawn.
- arXiv 2210.04541 is **Belen-Saglam, Altuncu, Lu & Li (2023)**, *Blockchain: Research and Applications* 4(2):100129 — **not** Haque et al.
- Benaloh & de Mare is **1994** (proceedings publication year), not 1993.
- EDPB Guidelines 02/2025 **v2.0 adopted 7 July 2026**. The "documented threat model" condition is **Aikebaier's (2026) interpretation**, not the Board's wording — attributed correctly in Ch1, Ch2, Ch4, Ch6.
- Aikebaier (2026) is a **single-author, industry-affiliated, non-peer-reviewed preprint**; the caveat travels with every use. The gap claim rests on the search rounds and regulatory silence, not on it.
- Closest prior art is the **DePaul research programme** (Scope et al., SSDBM 2022; JDI 2022; US Patent 12,425,209, 2025), not "a patent". It keeps *recoverable* keyed copies — which a ceiling forbids.
- Synthea output conforms to **US Core** profiles with US demographics, not Norwegian basisprofiler. FHIR **R4** matches Norway's version. No Norwegian clinical representativeness claimed.
- Synthetic data is **genuine Synthea output** (see `Data_Provenance_Statement.md`).
- Original May draft: **28 citations, ~14 unverifiable**.

**Structure and prose**
- Every chapter header is clean: no version stamps, no "Word count ≈", no retrofit notes.
- Limitations register is canonical in **§3.7 (eight items)**; §4.12 and §7.3 cross-reference rather than restate.
- A single APA reference list goes at the end in the submission assembly.

---

## 4. My own failure modes in this project — watch for them

Stated so the next conversation guards against the same errors.

1. **Reporting "done" before checking.** Twice I marked items "accepted" and never executed them (scalability, trust assumptions). Always grep for the change.
2. **Trusting the change trail instead of diffing.** On 28 September the public repository turned out to be *ahead* of the working set: four trail entries marked applied (D-05, A-04, A3-l, P8-03) existed only in the pushed copy, so the working set still carried a 362-line checker and an Appendix A repeating a claim D-05 had removed as false. A trail entry marked applied is a claim to check, not a fact. Diff against the repository, not only within the working set.
3. **Narrow detectors, then claiming zero.** I reported "zero dash corruptions remaining" when the detector's window was too narrow and only caught one of three shapes. Widen before claiming absence.
4. **Over-correcting.** I removed a true NCP-A claim as "unverified" because I hadn't read that paragraph of the source. Removing is not automatically safe.
5. **Invalid inference from metadata.** I dated a sentence by its page's age; the page was updated in place. Page age does not date its contents.
6. **Automated passes that corrupt punctuation.** The em-dash reduction broke paired asides into dash-then-colon and comma splices. Word-invariance checks don't catch punctuation damage.
7. **Two alternative edits both firing**, producing a duplicated clause (Ch5 §5.2). When writing alternative `replace()` calls, make them mutually exclusive.
8. **Assuming a file is empty** when the viewer just can't render its format (`.Rmd`). Ship a `.md` twin.
9. **Trusting a reviewer's claim, or dismissing it.** Both happened. Verify either way.
10. **Registering a file's checksum, then editing it.** The register went stale for the handoff itself. Compute checksums only after the final edit.
11. **Prefixing instead of replacing.** Marking an item 'COMPLETE' while leaving its old 'Remaining: …' text produced a self-contradicting entry that a fresh conversation read as still open. Replace status text; never append to it.

---

## 5. Working method Tiger requires

- Anti-drift and anti-hallucination on every change. Every claim traceable.
- Every rewrite gated by `inspector.py`. A rejection that shows only *gains* is a deliberate logged correction; a rejection showing *losses* is a regression.
- The inspector guards citations, numerals, article references, hedges and the reference list. It **cannot** see a changed meaning in plain words ("designated" → "presumptive" passes). So **every sentence is read**, not just checked.
- The inspector counts totals, so an offsetting removal and addition cancel. Check such cases by hand.
- Update `VERSION_REGISTER.md` whenever a file changes.
- Hard rule: never move to the next chapter until the research substrate (Google Sheet) reflects new findings.
- Tone: compressed, direct, no flattery. One question at most per turn. Mutual criticism licensed.

---

## 6. Where everything lives

See `VERSION_REGISTER.md` for checksums. Canonical files:

| File | Contents |
|---|---|
| `VERA-SNARK_Thesis_SUBMISSION.md` | Assembled: front matter, Ch1–7, single bibliography, App A–C |
| `Front_Matter_v1.md` | Title, abstract, contribution, declarations (incl. AI-assistance), nomenclature, TOC |
| `Chapter1_…` to `Chapter7_…` | Seven chapters, each with its own reference list for drafting |
| `code_artefacts/README_Appendix_A.md` | Appendix A: provenance, commands, full source listings, console output |
| `Appendix_B_Search_Log.md` | 59 queries, 4 dated rounds, [R] annotations |
| `Appendix_C_Evaluation_Instrument.md` | Designed, unexecuted evaluation instrument |
| `Consolidated_Bibliography.md` / `.Rmd` | 67 entries; read `.md`, knit `.Rmd` |
| `demo_app/` | **Canonical** `trf_checker.py`, `synthea_layer.py`, `app.py`, `norwegian_layer.py`, `cross_sector_check.py` |
| `repro_package/` | Self-verifying reproduction package. Modules sit at its root, data at `data/synthea_subset/`, bookkeeping scripts in `src/`. `bash run_all.sh` runs all four steps |
| `repo_synthea_subset/` | 8 untrimmed real Synthea bundles. Committed to GitHub 28 Sept; the same 8 now also in `repro_package/data/synthea_subset/` and `code_artefacts/synthea_subset/` |
| `Data_Provenance_Statement.md` | Answer to João's data blocker |
| `thesis_yaml_header.yml` | YAML: breezedark code, Word template hook |
| `handoff_tools/` | Inspector, math converter, assembly and bibliography scripts |
| `MASTER_MANIFEST.md` | **Every file, where it lives, its state and what is going on with it.** Read this when you need to know whether a copy is current |

**External:** repo github.com/Astheno-sphere/TRF · demo trfhimolde.streamlit.app · substrate Google Sheet (ID in memory) · EUR-Lex ELI http://data.europa.eu/eli/reg/2025/327/oj

**Non-canonical, kept for provenance only:** `_superseded_Chapter2_RETROFIT.md`, `_draft_Thesis_FULL_with_chapter_refs.md`.

---

## 7. Tools — in `handoff_tools/`

| Tool | Use |
|---|---|
| `inspector.py OLD NEW LABEL` | Gates a rewrite. Exit 0 = admit. Checks citations (parenthetical + narrative), numerals, article refs, hedges, reference list. Negative-tested against five corruption types. |
| `mathconv.py IN OUT` | Converts `*t*ᵣ(*a*)`-style italic unicode math to LaTeX. Skips headings, tables, code, lines with `$`. **Inspect output before committing**; it does not know about backticks. |
| `assemble.py` | Rebuilds the consolidated bibliography from chapter reference lists and the submission assembly. |

Verify Word conversion with: `pandoc FILE.md -o out.docx` then count `<m:oMath>` in `word/document.xml`. Current state (base, 2 Oct): **176 native equations, zero LaTeX or `$` leaking** (175 before the rebase; the draft adds `$t(a) + F(a) + 1$`).

---

## 8. Verification register

| ID | Item | Status |
|---|---|---|
| F-01 | SPUHiN D5.2 | Title, milestone, project number resolved from document cover |
| F-02 | EDPB CEF full report | Open, not load-bearing; recurring-issue count deliberately removed |
| F-03 | EDPB Guidelines 02/2025 | Closed: v2.0, 7 July 2026 |
| F-04 | Aikebaier SoK | Closed |
| F-05 | Haque venue | Closed as a misattribution: it is Belen-Saglam et al. 2023 |
| F-06 | TEHDAS2 SPE deliverable | Closed: D7.4 |
| F-08 | Implementing acts | Closed: due 26 Mar 2027 |
| F-09 | Walonoski Synthea | Closed |
| F-10 | eHOMB year | **Closed: not recoverable; dateless final** |
| F-11 | EUR-Lex Art 73(1)(e) | **Closed at primary source**: official OJ text retrieved, and Tiger read the page |
| F-12 | In-force vs applies-from | Closed |

---

## 8a. Completed — do NOT redo

Each item below is finished and verified. A fresh conversation must not repeat it.

| Item | Result |
|---|---|
| Sentence pass 1 | Every prose sentence over 55 words resolved. Three deliberate exclusions: the TOC list, the research question, the Semantics II formal definition |
| Sentence pass 2 | **Complete across all chapters.** Every 41–55-word sentence screened; structurally complex ones read in full and 21 split; parallel lists left. Simple sentences screened by structure, not read individually |
| Math to LaTeX | 176 native Word equations (base, 2 Oct), zero LaTeX or `$` leakage (verified via pandoc) |
| Em-dash corruption repair | 48 broken dash pairs and comma splices found and repaired |
| P2E2 source | Read and integrated into Ch2 §2.5 as Chakraborty et al. (2025), PVLDB, peer-reviewed |
| F-10, F-11 | Both closed (see §8) |
| DOIs | Hevner, Finck 2018, Benaloh (and year corrected to 1994), arXiv items, Peffers, EU regulations |
| Supervisor feedback, two rounds | All accepted items applied; evaluation left designed-not-executed by agreement |
| Synthea subset on GitHub | **Done 28 Sept.** Eight untrimmed bundles at `data/synthea_subset/` in `github.com/Astheno-sphere/TRF`, with `requirements.txt`, `docs/expected_trf_output.txt` and `norwegian_docs/HOW_TO_RUN.md`, all of which the 23 Sept web upload had silently dropped. Verified from a fresh clone: checker byte-identical to `docs/expected_trf_output.txt`, layer reads 8 bundles, mean payload 891 bytes, six measures identical, 200/200 commitments differing. Do not regenerate Synthea: these are the files Chapter 5's 891 was measured on |
| Working set resynced to the repository | **Done 28 Sept.** The repository was ahead. `trf_checker.py` 362 → 363 lines with the §4.8 salt destruction, `synthea_layer.py` gains the three-directory fallback, Appendix A corrected in all four copies including the assembled submission. See failure mode 2 |
| App feature audit | **Done 28 Sept.** Two reported results had no viewer anywhere: the independent exhaustive cross-check (Ch5 §5.4) and the δ witness (§5.5a). Both now run from Tab 5 with pass/fail banners. Cross-check agrees with the recorded run on all four cases; δ witness returns 90/95 and 89/94, matching Table 5.2a. `cross_sector_check.py` needed nothing — it has been on GitHub and wired into Tab 4 since 23 Sept |
| Recorded run per command | **Done 28 Sept.** Five files in `docs/`, one per command. Previously only the checker had one, so a reader could not tell a changed file from a changed result for the other four |
| Redundancy sweep | **Done 28 Sept.** The eight bundles existed in three working-set copies plus GitHub; now one working copy plus GitHub. Stray root duplicates of the code, the two stray result files and the stale migration zip removed. 133 MB → 45 MB, 95 → 78 files |
| Assembly reproducibility proven | **Done 28 Sept.** `handoff_tools/assemble.py` rebuilt the submission and the bibliography; both came back **byte-identical**. `handoff_tools/inspector.py` returned **ADMIT** on old-against-rebuilt: citations, numerals, article references, hedges and reference list all identical |
| Reproducibility package repaired | **Done 28 Sept.** Modules moved to the package root so the layer resolves `data/synthea_subset/` and the Norwegian modules can import the checker; `run_all.sh` no longer skips the realism layer; both cohort runs recorded separately. `bash run_all.sh` exits clean |

## 9. Open work, in priority order

**Superseded by the supervisor review.** The authoritative list is now
`SUPERVISOR_REVIEW_2026-09-30_Ferreira.md` with the open decisions in `DECISION_RECORD.md`.
Sequence, which is *not* his numbering:

1. **O-01 / M2 — settle the Art. 68(12) reading.** BLOCKING. Candidate's decision. Put the
   options to him; do not decide it alone.
2. **O-02 / M1 — ground p(a) in a real audit-record format**, or reframe Semantics I.
   Research, then a decision. May change the model.
3. **O-03 / M3 — salt and ciphertext design.** Independent, cheap, embarrassing. Do early.
4. **M5 — primary sources**: the ten-year floor; SPUHiN "finalised" claims; verbatim
   Art. 68(12) and 73(1)(e) from the OJ; the §2.2 EHDS dates.
5. **M4 — propositions, promote §6.9a into Chapter 4, hash-chain integrity in V_II.** The
   V_II tamper test should be done regardless of the renaming decision.
6. **M6 — traceability matrix** against TEHDAS2 D7.4 and the SPUHiN checklist. Reword
   Appendix C item A1; João has released us from our own constraint in writing.
7. **M7 — logistics framing**; state programme fit in §1.5.
8. **Meta-commentary, repetition, length**; move the Version and Change Record to the
   repository; slim Appendix A.
9. **Minor-issues table**; renumber sections and appendices; regenerate the TOC.
10. **Tag the repository and mint a Zenodo DOI.** The thesis cites a moving `main`.

Carried forward and unchanged by the review: two unread arXiv sources (aiAuthZ 2607.05518,
privacy-engineering SLR 2606.23696); two figures (record-state diagram §4.8/§5.6, regulatory
timeline §6.8) — the thesis still has **zero**; the HiMolde template, unobtainable from this
environment; Datatilsynet sounding; Sikt notification if the evaluation is run.

**Closed, do not redo:** the four DOIs; bibliography link coverage (67/67); the Synthea
subset on GitHub; em-dash reduction; the Word conversion toolchain.

---

## 10. Key figures — verified, reproduce exactly

| Result | Value |
|---|---|
| Semantics I: records with violation | 90 / 200 |
| Semantics I: total violations | 95 (41 C2-only, 44 C3-only, 5 both) |
| Corollary 1.2 witnesses (no erasure request) | 39 |
| Semantics II: violations | 0 |
| Records invalidated | 138 (52 Art 17, 86 Art 68(12)) |
| δ = 3 witness | 89 records / 94 violations; Cor 1.2 still 39; Sem II still 0 |
| Synthea payload mean | 1,006 bytes (98-bundle cohort); 891 bytes (8-bundle subset); all six measures identical in both |
| Reference commitment, record 100 | `11087780fd192c8f…` |
| Seed | 20260915 |

`python3 demo_app/trf_checker.py` must reproduce these byte-for-byte.
