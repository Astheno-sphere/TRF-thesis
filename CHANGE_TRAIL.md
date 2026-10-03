# Change trail

## 3 October 2026 — optional real-cryptography module (Tiger: "go ahead")

| ID | Change | Verification |
|---|---|---|
| B-28 | New files: `crypto_envelope.py` (demo_app, repro_package, code_artefacts; 118 lines) and `repro_package/results/crypto_envelope_output.txt`. Each record's payload encrypted under its own AES-256-GCM data key (record id as associated data); data keys wrapped under a key-encrypting key in a custody object standing in for an HSM; wrapped key destroyed at the record's invalidation month; every record decrypted again | Two runs with fresh random keys give byte-identical output: 200/200 decrypt before; 138 keys destroyed; 138 refused, 62 read; the invalidated record's ciphertext opens under none of the 62 surviving keys; 62 ciphertexts kept after deletion. The checker and every reported figure untouched |
| P23-01 to P23-10 | `run_all.sh` optional step and diff line; full-cohort note corrected (it is historical, P12/P13); `requirements.txt` gains `cryptography>=42` (this module only); Appendix A contents row, new A.9e listing and A.15 output; Table 5.0a row; §5.7 limitation paragraph reports the executed check; Table 4.1 OPR-6 row now "met in the optional module", destruction still in program memory | `appendix_sync.py` 13/13 (two new blocks added to its map); `trail_check.py` checks the module's copies and its recorded run |
| P23b-01 | `run_all.sh`: the new step labelled "5 (optional)", the others being 1/4 to 4/4 | — |
| B-29 | Public repository commit `2b2dddb`: module, recorded output, requirements, README row and revision note, Appendix A, repository trail R-23, CHECKSUMS regenerated and copied here | All six recorded runs reproduced in the repository clone before pushing |

## 3 October 2026 — supervisor review, patches P19–P22 (A1, Table 2.1, frequency and window, traceability)

| ID | Change | Verification |
|---|---|---|
| P19-01 to P19-04 | M6b: Appendix C item A1 reworded to what the mechanism lets an auditor verify (logged, unaltered invalidation); the change recorded in one line, as the supervisor asked; A1/A2 note and §3.8 follow | patch.py: "does not" kept after the gate flagged its loss |
| P20-01, P20-02 | M5e: Table 2.1 in three bands (peer-reviewed systems; national policy; preprints and practitioner sources, now holding zkFL-Health (arXiv), Aikebaier (ePrint) and VeritasChain); one sentence on what the third band may carry. SPUHiN row "Norwegian policy, final" → "hearing version": P10's sweep searched for "finalis" and missed "final" | Venues checked in the bibliography |
| P21-01 to P21-04 | MIN-05: "the ordinary case" (§3.4) and "the generic case" (Cor 1.1) replaced by what the condition says and a pointer to §3.7; Ch4 summary made conditional on log granularity. MIN-06: the closed window kept and justified (conservative reading of "at least"; changing it would shorten every obligation and change every recorded figure) | patch.py: Article 17 kept after the gate flagged its loss |
| P22-01 | M6a: Table 4.1, the traceability matrix, at the end of §4.11: 14 requirements (EHDS Arts 68(12), 73(1)(e); D7.4 OPR-6, EHDSR-6/7/8; GDPR Arts 17(1), 12(3), 17(3)(b), 5(1)(c), 5(1)(e); EDPB 02/2025; ITI-55; SPUHiN hearing version ×2), each with what the mechanism does, where, and a status (met in the artefact, met by specification, no conflict, open) | Statuses checked against the code and the recorded run. D7.4 page references wait on TIGER_TASKS T-1 |

## 3 October 2026 — supervisor review, patches P15–P18 (propositions; anchoring result)

| ID | Change | Verification |
|---|---|---|
| P15-01 to P15-06 | M4b: §6.9a's anchoring result promoted into Ch4 (end of §4.6) as Proposition 3, with proof. Checked formally first: for a ceiling of L months anchored at e(a) ≥ t(a), floor and ceiling collide for a record iff e(a) + L ≤ t(a) + F, so a collision needs L ≤ F under any anchor; §6.9a's "structural rather than numerical" overstated it. Corrected in §6.9a ×3 ("as well as numerical"; "the later longer than the earlier"; "a longer ceiling"). What the anchor decides is visibility: a same-anchor collision would be a contradiction readable in the text; an external-anchor one depends on each record's history. M4a: the §4.7 note now says why the results are propositions and where the weight lies (§4.2, Propositions 3 and 4) | Derivation in the patch file; proof re-read |
| P16-* (58 edits) | M4a: Theorem → Proposition, theorems → propositions, Proposition L → Proposition 4, across front matter, Ch1–7 and Appendix C, one logged edit per changed line. Appendix B excluded (query 34 is a verbatim search string) | No "theorem" left in those files |
| P17-* (20 edits) | Same rename in the code (three checker copies, app) | Two printed header lines change; Synthea, Norwegian, cross-sector runs byte-identical |
| B-23 | `trf_output.txt` and `expected_delta_witness_output.txt` re-recorded (header lines only) | run_all 5/5 |
| P18-B*, P18-* | Appendix A: listings and the two outputs synced; prose renamed outside code fences | appendix_sync 11/11 |
| B-24 | Public repository commit `0f3c39e`: rename in code, README, Appendix A, two recorded runs; repository trail R-22; CHECKSUMS regenerated and copied here | 5/5 runs reproduced in the repository clone before pushing |
| B-25 | `TIGER_TASKS.md`: the tasks only Tiger can do (D7.4 page check with link, UCC on EUR-Lex, owning §4.6 and Propositions 3–4, live app check, Zenodo DOI, logos, voice pass, length guidance, two optional) | — |
| B-26 | Defect in my tooling, found when check 8 reported 28 unexplained lines after P16: generated patches (P12, P13, P16, P17, P18) computed their edits from the files at import, so once applied they replayed as nothing and the base-diff check could not see them. `patches/frozen.py` added: generated edits are frozen to `patches/<name>.edits.json`, rebuilt for the five patches from git history (pre-states `e1143af`, `e83e061`). New check 14 replays every patch since `joao-base-v1` in log order and requires the files on disk; check 3 accepts wildcard rows (`P16-*`) | Frozen edit IDs equal the log for all five; replay from git reproduces every logged after-md5 (22 of 22) |
| B-27 | Two faults found after commit `a554b51`. (1) P20 repeated B-26's flaw (edits computed from the working file at import), so check 14 crashed replaying it; P20 now frozen from `faa2a5e`. (2) The commit gate let `a554b51` through while `trail_check.py` crashed: it refused only on a "[FAIL]" line, and a crash prints none. `commit.sh` now also requires "TRAIL INTACT". The content of `a554b51` was complete (trail, tracker, register all in it) | Check 14 passes after freezing; gate tested: refuses when the inspector does not finish |

## 3 October 2026 — supervisor review, code wave: patches P12–P14 and the public repository

| ID | Change | Verification |
|---|---|---|
| P12-01 to P12-04 | `trf_checker.py` (three copies) and `app.py`. Metadata split into accessor and subject fields; SPE records name a researcher and a permit; subject link removed at the ceiling and logged (Ch4 §4.7 step 4); key, salt and payload removed at invalidation (D-15, D-17); payloads per record class (ITI-55 query, SPE activity); `V_II` checks each record against an append-only Merkle log (RFC 6962 hashing) and the run prints two tamper tests; C3 checked over the subject link; `make_salt()` and `--random-salts` replace the `if False` branch. New contents kept in `patches/P12_payloads/` | Before applying: Semantics I 90/200, 95, 39 witnesses, 138 invalidated, Semantics II 0, all unchanged; 200/200 records verify; both tamper tests make `V_II` fail; `--random-salts` same results; Norwegian and cross-sector runs byte-identical; Streamlit AppTest: every button, no exception. Code edits were first made directly, then reverted and replayed through `patch.py` so the md5 chain holds |
| B-20 | Recorded runs re-recorded from the P12 code: `trf_output.txt` (b0ba15484259), `expected_delta_witness_output.txt` (b5ee877549fc), `synthea_comparison_subset_output.txt` (f6eacf54972c). `synthea_comparison_full_cohort_output.txt` kept as the 28 Sept record (cannot be re-run without the 98-bundle cohort) and labelled as such in A.11 | `run_all.sh`: 5/5 match |
| P13-B01 to P13-B09 | Appendix A A.8, A.9d, A.10, A.11b, A.12 regenerated from their files by `handoff_tools/appendix_sync.py` (new) | `appendix_sync.py`: 11/11 equal |
| P13-01 to P13-12 | Appendix A prose: line counts (533, 530), record model, `check_semantics_II` and integrity description, `make_salt`, ciphertext deletion, payload means (43 → 891 subset; full cohort historical), integrity row and new reference commitment `678ade47c1e6dc03…` in A.6, A.11 marked as recorded before the revision | patch.py: declared losses are the old counts (363, 526), HP-026 from the old console line, and "§4.8" now written "s4.8" in a code comment |
| P14-01 to P14-14 | Ch5: module size (533 lines, 413 non-blank non-comment), Table 5.0a, record model (§5.2), ciphertext deletion, §5.6 auditor view as a code block with the SPE record's researcher and permit (the supervisor's M1 point about HP-026 and ncp=NO), new integrity paragraph with the tamper result (M4c), payload means. Table F.2: 533. MIN-07: "Section 6.9" → 6.9a in Table 5.0a and Appendix A ×3 | Figures copied from the re-recorded run |
| B-21 | Public repository `Astheno-sphere/TRF` commit `a6062e3` (pushed 3 Oct): code, three recorded runs, `docs/Appendix_A.md` replaced by the thesis's Appendix A (the copy there was older), README (counts, revision section), repository trail R-16 to R-21, CHECKSUMS regenerated from the files. `CHECKSUMS.md` here is now a copy of the repository's | All five recorded runs reproduced inside the repository clone before pushing. `trail_check.py --remote` now uses the push clone; new check 13 (Appendix A listings equal their files) |
| B-22 | Guard "dead salt branch in code" narrowed to the assignment (`= os.urandom(16) if False`): the commit gate refused M3c as closed because the pattern matched the new docstring that records the branch's removal | Guard 0 in all code files |

## 3 October 2026 — supervisor review, patch P11 (logistics anchor, programme fit)

| ID | Change | Verification |
|---|---|---|
| P11-01 to P11-04 | M7a. §2.7: the unsourced analogy ("destruction-of-records requirements that apply to perishable or sensitive physical goods") replaced by Union Customs Code Art 51 (records ≥ 3 years from declaration or discharge, extended for appeals) and Art 197 (destruction of goods). Finding: they do not collide, because destruction reaches the goods and record-keeping the documents; the record outlives the thing recorded, which is Semantics II in physical form. Tested against §6.9a (external anchor, different object) and the analogy's limit stated. §1.4 "imports a solution structure that logistics has operated for decades" replaced by that specific correspondence. M7b. §1.5: one sentence on the programme fit (logistics of information, not of energy). New reference: Regulation (EU) No 952/2013 | UCC Arts 51, 197 verbatim from legislation.gov.uk "as adopted" (RESEARCH_LOG rows 34–35). patch.py: one declared loss ("not yet", inside the overreach removed); Article 17 kept in §2.7 after the gate flagged it. Bibliography 68 → 69 |

## 3 October 2026 — supervisor review, patch P10 (SPUHiN as inspected)

| ID | Change | Verification |
|---|---|---|
| P10-01 to P10-19 | M5b. Every "finalised" claim about the Norwegian SPE criteria (Statement of Contribution, §1.2, §1.5, §2.6 ×4, §2.6a, §2.9 ×2 incl. Table 2.1, §3.7, §4.11 ×2, §6.8 ×2, §7.2, §7.6) now names the version inspected: the hearing version. §1.2 says the absence "is observed in that version and has not been checked against the deliverable as submitted". The guard "survives against the final national document" reached 0. P10-18/19 (`P10b`) were found by grepping after the first pass; EDPB "finalised" uses left, being correct | Helsedirektoratet SPUHiN page fetched 3 Oct (RESEARCH_LOG row 31): criteria "included in" D5.2, adaptation pending the Commission |

## 3 October 2026 — supervisor review, patch P09 (ten-year floor illustrative; Feng peer-reviewed)

| ID | Change | Verification |
|---|---|---|
| P09-01 to P09-09 | M5a. The ten-year floor is now "reported" (abstract, Sammendrag, Ch1 ×3, Ch4 §4.3) and §2.3 says what each source supports: Simjanoska Misheva et al. (2025) for the figure; the 2017 NCPeH agreement, clause II.4.2, for an audit-trail requirement without a stated period; F = 120 treated as illustrative, Corollary 2.2 cited for independence. New reference: eHealth Network (2017) | Searched 3 Oct (RESEARCH_LOG rows 22–26); no primary document stating ten years was reachable. The agreement's text retrieved and quoted |
| P09-F09 to P09-F23 | M5e (part). Feng et al. (2022, arXiv) → Feng et al. (2023), CAV 2023, LNCS 13966, pp. 374–396, in five chapter reference lists and every in-text citation | Springer page retrieved 3 Oct; it names arXiv 2209.04052 as its extended version. patch.py: all losses are the 2022 forms, each matched by a 2023 gain |
| B-18 | `assemble.py` dropped any reference starting with a lower-case letter, so "eHealth Network" never reached the bibliography. Filter widened for that entry. Checked every chapter list: no earlier entry had been lost this way | Bibliography 67 → 68 |
| B-19 | `trail_check.py` range rows: the parser accepted only `X-NN to X-MM`; P09's generated IDs (`P09-F09 to P09-F23`) were refused by the commit gate. Parser generalised to any prefix | Gate refused P09 first, as it should; check 3 PASS after the fix |

## 3 October 2026 — supervisor review, patches P07 and P08 (the reading carried through)

| ID | Change | Verification |
|---|---|---|
| P07-01 to P07-07 | Ch1 §1.1, Ch2 §2.3: Art 68(12) quoted verbatim and the reading stated as in §4.6 (reaches logs at patient-record granularity on the broad reading). Ch6 §6.1 rewritten to lead with the robust result (supervisor's M2c), then Proposition L, then the SPE instance stated conditionally; the opening "two provisions that cannot both be satisfied" is gone. Ch6 §6.2 and Ch7 §7.4: "the thesis adopts the broad reading" → Corollary 1.2 stated conditionally; §7.4 now poses the open joint (does auditing need the subject link after the ceiling) and puts it in the request to the authorities. Removed in §6.2 and §7.4: "the Regulation uses the narrower 'made available under the data permit' formulation freely elsewhere", never verified (no instance found on 3 Oct) and no longer needed | patch.py: one declared loss ("narrower" in the removed claim). Guard "cannot both be satisfied" 1 → 0; paraphrase guard 6 → 1 (Appendix C, P08) |
| P08-01 | Appendix C item 7: verbatim Art 68(12); the item now asks both questions the thesis depends on | Paraphrase guard 1 → 0 |

## 3 October 2026 — supervisor review, patch P06 (Rival 6, Proposition L, D7.4)

| ID | Change | Verification |
|---|---|---|
| P06-01 to P06-05 | §4.6: D7.4 EHDSR-7 ("All SPE logs MUST identify the actor") added to the textual case for the partition. §4.8 *Ciphertext*: D7.4 OPR-6 ("deleted or rendered unrecoverable … including any backups or redundant copies") supports key destruction for unreachable copies. §4.10: six rivals; Rival 3 rewritten (no longer says Art 17 targets the pseudonym, which contradicted §4.2; the cross-border payload is put there by ITI-55; dataset-level logging conceded as a real alternative for the ceiling); Rival 6 (move the logs out at permit closure) accepted as an answer to Corollary 1.2 and bounded by Proposition L, stated and proved: a location-anchored ceiling yields to relocation, a controller-anchored right does not | D7.4 v1.2 retrieved 3 Oct via tehdas.eu (four fetches; see `RESEARCH_LOG_2026-10.md`, row 20, including one disagreement on OPR-6). patch.py: gained TEHDAS2 (2026) citation and Arts 17(1), 68(12), 73(1), 73(1)(e); "Article 17" kept in Rival 3 after the gate flagged its loss |
| B-17 | `RESEARCH_LOG_2026-10.md`: every search and fetch of 3 Oct (20 rows), with outcomes and what still needs confirming in the D7.4 PDF | — |

## 3 October 2026 — supervisor review, patches P04 and P05 (Chapter 4 core: M1, M2a, M5c)

| ID | Change | Verification |
|---|---|---|
| P04-01 to P04-16 | §4.2 example and claim: payload is what the record carries beyond accountability (demographic query; document content only where a deployment keeps it). §4.3: m(a) = m_acc ∪ m_subj; p(a) defined per record class, cross-border grounded in IHE ITI-55; new variable β (subject link), confined to the SPE case. §4.4 C3: Art 68(12) quoted verbatim; extends to β where the subject fields are electronic health data. §4.5 Semantics II (i) over m_acc, (iii) covers β. §4.6: Corollary 1.2 conditional on log granularity; the textual case rebuilt on Art 68(12)'s object ("electronic health data"), Art 2(2)(a),(c), Art 73(1)(a),(c); contextual case strengthened from the paragraph's own text; "adopts the broad reading" withdrawn; Theorem 2 resolves both readings. §4.7: trajectory removes the subject link at the ceiling. §4.8 SPE application rewritten (the supervisor showed the old conclusion did not follow on the broad reading); open joint stated. New reference IHE International (2024), ITI TF-2 Rev 20.1 | Sources retrieved 3 Oct: Art 68(12), 2(2), 73(1) (streamlex mirror of OJ L 2025/327); ITI-55 §3.55.4.1.2.1, §3.55.5.1 (profiles.ihe.net, Rev 20.1, 12 Dec 2024). patch.py: gained Arts 2(2)(a), 68(12), 73(1), 73(1)(e) and the Regulation citation; one declared loss ("narrower", in a dropped clause about the Regulation's usage elsewhere that was never verified). "Broad reading" kept as the term. Word build: 209 equations, no LaTeX leakage. Bibliography 66 → 67 |
| P05-01, P05-02 | Gap in P04's proof found on re-reading before commit: when an erasure request fixes t^I before the ceiling, nothing removed the subject fields at t_π + 6, yet the C3 argument said they were gone. Step 4 added to the trajectory; C3 argument cites it | Proof re-read in full after the patch |

## 3 October 2026 — supervisor review, patch P03 (EHDS dates)

| ID | Change | Verification |
|---|---|---|
| P03-01, P03-02 | §2.2: "designate a National Digital Health Authority by June 2025 … certify their systems … by January 2026 (Ernst & Young, 2025)" replaced by Art 19(1) (designate and inform the Commission by 26 March 2027) and the Art 105(1)(a) schedule (EHR-system requirements from 26 March 2029 for the first priority categories), cited to the Regulation. Ernst & Young entry removed | Arts 19(1) and 105 retrieved 3 Oct (streamlex mirror of OJ L 2025/327). patch.py: declared losses (EY citation; 2025, 2026 from the wrong dates); gained citation to the Regulation and Arts 19(1), 105. Bibliography 67 → 66 entries, all with locators |
| B-14 | `assemble.py` now regenerates `Consolidated_Bibliography.Rmd` from the same body. The hand-kept twin had drifted: it lacked the Politiregisterloven (2010) entry. `trail_check.py` check 6 now also compares the `.Rmd`. Guard "EY" narrowed to the in-text citation and the reference entry (it had also matched Appendix B's locator log, which is history) | `.Rmd` body identical to `.md` after rebuild; Politiregisterloven present |
| B-15 | P03 was committed (`git log`: "P03: EHDS dates…") while `trail_check.py` check 3 failed: the checker did not parse a trail cell listing two IDs ("P03-01, P03-02"). The row was right, the parser was narrow. Parser fixed; `handoff_tools/commit.sh` added, which refuses to commit on any FAIL. Rule: commit only through `commit.sh` | Re-run after the fix: check 3 PASS |
| B-16 | `trail_check.py` check 4 read only commit subjects; P05 was committed in the same commit as P04 with its own message line. Check 4 now reads full messages | Check 4 PASS |

## 3 October 2026 — supervisor review, patch P02 (salt and ciphertext)

| ID | Change | Verification |
|---|---|---|
| P02-01 to P02-08 | §4.8: new *Ciphertext* item (deleted at t^I; key destruction still governs replicas and backups) and *Commitment* rewritten (salt destroyed with the key; binding unaffected; a party needing to prove correspondence keeps its own opening). §4.8 terminal transition now also removes key, salt and ciphertext for records never invalidated. §4.9 residue list, guess-confirmation response, pseudonymisation finding and residual-risk paragraph ("unavoidable" → reduced, with the three exposures that remain) follow the design. §4.12 summary and §5.6 trajectory follow the code. Decisions D-15, D-17 | Text now agrees with `trf_checker.py` (`rec.salt = None`) and Appendix A §A.4. patch.py: one declared loss, hedge "conditional" from "not unconditionally unlinkable", which described the retained-salt oracle that no longer exists; pseudonymised status kept (P02-05). Guard "salt *not* destroyed": 1 → 0. Open: the code still keeps the payload after invalidation (code wave, M3b). Noted, not fixed: §4.9 says the residual risk "is recorded as a limitation in Chapter 6", but Chapter 6 only touches it at §6.2 (EDPB "until the algorithm is broken"); to settle in PRES-4 |

## 3 October 2026 — supervisor review, patch P01 (minor issues)

| ID | Change | Verification |
|---|---|---|
| P01-01 to P01-16 | MIN-01 §3.6 line counts (wrong and inverted) replaced by a reference to Table 5.0a; MIN-02 §3.6 cross-reference → Chapter 4, Section 4.3; MIN-03 §1.6 "accumulator-based invalidation" → "a logged invalidation registry", accumulator stated optional and unimplemented; MIN-04 round 5 named in §2.1 text, Table of rounds and the appendix list; MIN-08 Appendix C → §3.8; MIN-09 "a separately written" ×3; MIN-11 "witnesses in the model" in §5.7 and §6.1; MIN-12 the supervisor addendum removed from §1.5 and §3.2 (scope statement kept). Supervisor's tracked wording adopted for MIN-02, -03 (substance), -08, -09. Per-edit reasons in `patches/P01_minor_batch.py` | patch.py inspection: 2 declared losses (section numbers 3.4, 3.9), no undeclared loss. trail_check: 11 wording differences from the reviewed draft, all replayed from logged edits. Guards: 8/17 targets met. `trail_check.py` check 8 now replays every logged edit on the draft line before falling back to shingles (a 4-word edit had been reported unexplained) |

## 2 October 2026 — base reset to the draft the supervisor reviewed (read this first)

The 30 Sept working set was not the draft sent to Prof. Ferreira. The draft he reviewed is our
draft, returned in the HiMolde template with his tracked changes. Read with tracked changes
rejected, it differs from the 30 Sept files in 29 content edits, and the 30 Sept files carry
one edit made after it was sent (H-01). Work from 30 Sept to 1 Oct was built on the wrong base
and is preserved on branch `zip-base-superseded` (commits F1–R1, AS-01, and the merge review).

| ID | Change | Verification |
|---|---|---|
| D0-01 to D0-29 | Chapter files brought to the reviewed draft: abstract and Sammendrag; Ch1 opening; Ch2 ×2; Ch4 ×9; Ch5 ×6; Ch6 ×7; Ch7 ×3. Full list in `PATCH_LOG.md` | Every prose paragraph compared against `supervisor_review/draft_as_reviewed_tracked_rejected.txt`; 13 residual differences, all template or rendering. Checker byte-identical; bibliography 67/67 |
| B-01 | Git repository; branch `joao-base`, tag `joao-base-v1` at `0438daf`; superseded work kept on `zip-base-superseded` | `git log`, `git tag` |
| B-02 | `handoff_tools/patch.py`: exact-match patcher that writes nothing if any anchor fails, and logs every edit with before/after md5 to `patches/APPLIED.log` | Used for D0 (29 edits, 0 failures) |
| B-03 | `supervisor_review/`: the returned .docx; its text with tracked changes rejected and accepted; the email review text; the raw review | md5 in the register |
| B-04 | `conversation_history/`: full export of the MAIN chat (22 May – 30 Sept) | md5 in the register |
| B-05 | Control documents corrected: `FAILURE_LEDGER.md` F-0 and the correction to the "five false entries" lesson (they were applied on the fork); `DECISION_RECORD.md` D-14 (base) and D-15 (salt settled); `CONVERSATION_LINEAGE.md` (MAIN, FORK, UNKNOWN, THIS); `NUANCES.md` rules 6–8; `HANDOFF_READ_FIRST.md` §00; `PATCHES.md` Wave −1; `PATCH_LOG.md` D0 entry; `PATCH_QUEUE.md` marked superseded by `PATCHES.md`; `SUPERVISOR_REVIEW…` and `SUPERVISOR_FEEDBACK_HISTORY.md` describe the returned file | Each statement about the base checked with grep on 2 Oct |
| B-06 | `handoff_tools/verify_base.py`: renders every prose line of the front matter and Ch1–7 with pandoc and compares it with the reviewed draft's text; after patching, every difference it lists must correspond to a logged patch | Base: 621 lines, 0 differences. Negative test on `184c91d`: 28 |
| B-07 | `VERA-SNARK_Thesis_SUBMISSION.docx` rebuilt from the base submission (`pandoc --reference-doc=thesis_reference.docx --toc`). The 29 Sept build carried the pre-rebase text | 176 native equations (175 + `$t(a) + F(a) + 1$` from the draft's F+1 wording, D0-08/09), 25 tables, 0 LaTeX leaks. Same command on `184c91d` gives 175 / 25 |
| B-08 | `review/TRF_Thesis_merged_2026-10-01.zip` removed from `joao-base`. It was the 1 Oct review copy of zip-base work, committed into D0 by accident | The merge review stays on `zip-base-superseded` (`53b77e3`) |
| B-09 | `supervisor_review_RAW_2026-09-30.txt` moved into `supervisor_review/`; register path updated | md5 unchanged `bb280bd623ae` |
| B-10 | `VERSION_REGISTER.md` recomputed for every row; new rows for B-01..B-09; `RESUME_PROMPT.md` rewritten for the 2 Oct package with five verification commands; package `TRF_Thesis_Migration_Package_02Oct.zip` built with `.git` (both branches, tag) | Register check: 0 mismatches. Archive unpacked and re-checked |
| B-11 | `CHECKSUMS.md`: `README.md` row updated to the public repository's HEAD `dba9c56` | A fresh clone on 3 Oct matched every other row. Two commits after `0d855a7` (28 Sept 11:10) changed one README table cell, the `app.py` line count 524 → 526; `b15679678845` is `0d855a7`'s README |
| B-12 | Trail inspector. `handoff_tools/trail_check.py` (12 checks: git, md5 chain against `APPLIED.log`, trail rows, commits, code copies, fresh assembly, register, base diff explained by patches, guards, review tracker, recorded runs, public repository); `handoff_tools/guards.json` (7 regression patterns held at 0, 17 review targets that may only fall); `REVIEW_TRACKER.md` (40 items from the 30 Sept review); `patch.py` now refuses reused IDs and any undeclared loss of a citation, number, article reference or hedge; `verify_base.py` exposes `collect()` | Planted test (an unlogged edit reintroducing "Haque et al" in Ch3): 4 checks failed (md5 chain, assembly, base diff, guards). Planted patch dropping "800-88 Revision 2": aborted, 3 undeclared losses. Clean state: TRAIL INTACT |
| B-13 | Decisions recorded: `DECISION_RECORD.md` D-16 (Art 68(12) partition reading m = m_acc ∪ m_subj, Corollary 1.2 conditional on log granularity, Proposition L answers Rival 6, lex specialis rejected), D-17 (ciphertext deleted at invalidation; dead branch replaced in the code wave), D-18 (Propositions; anchoring result and Proposition L into Ch4; Merkle integrity test). O-01, O-03, O-06 resolved. `PATCHES.md` Wave 0 marked answered; `REVIEW_TRACKER.md` all items unblocked. Guard narrowed: the 'accumulator-based' pattern matched Ch6's accurate statement that the specification provides accumulator witnesses; it now matches only §1.6's "accumulator-based invalidation" (baseline 1) | Verbatim Art 68(12), Art 2(2)(a),(c), Art 73(1)(a),(c),(e) retrieved 3 Oct (streamlex mirror of OJ L 2025/327) and quoted in D-16 |

**Rows below this section describe earlier states.** The 22 Sept rows describe edits made on the
fork. They are not in the base unless re-applied from Wave −1.


Every change to a canonical file, with the chapters it affects. Newest session first.
Columns: ID · file · section · chapters affected · change · reason and source · inspector verdict.
A REJECT is acceptable only when every *lost* item is the intended removal; each is listed.

## Session 22 September 2026, pass 8 — Datatilsynet enquiry finalised for a single sender

| ID | File | Affects | Change | Reason | Status |
|---|---|---|---|---|---|
| P8-01 | Datatilsynet_Enquiry_DRAFT.md | none (not thesis text) | Rewritten from "we" to "jeg"/"I" throughout; supervisor's signature line removed; institution, programme, supervisor's name and institutional email carried in the body instead, so the enquiry still shows its provenance | Tiger's decision, 22 Sept: send from the author alone | Ready to send. Prof. Ferreira to be informed before it goes, not after |
| P8-03 | Datatilsynet_Enquiry_DRAFT.md | none (not thesis text) | Short version added at the top and marked "send this one": provisions quoted inline, two numbered questions, stated submission date, explicit permission to answer informally or to say the point is unsettled. Long version kept below for the record | Tiger's request for a version more likely to be answered. Nothing overstated: no invented urgency, no flattery, same two questions | Ready to send |
| P8-02 | same | Ch7 §7.4 (pending) | Note added: once sent, §7.4 changes from "decidable by asking" to a record that the enquiry was made, by whom and on what date. Not written yet, because it is not true yet | Trail rule: nothing reported as done before it is done | Waiting on the send date |

No chapter changed in this pass. Checker untouched.

## Session 22 September 2026, pass 8 — repository fix, Norwegian tab, Appendix A aligned to the repo

Context: the first upload to github.com/Astheno-sphere/TRF landed `trf_checker.py` (363 lines, correct), `app.py`, `synthea_layer.py` and a placeholder README. The data subset, the Norwegian modules and the docs did not land, so Tab 3 was still broken. Verified by fetching the repository.

| ID | File | Affects | Change | Reason | Verification |
|---|---|---|---|---|---|
| P8-01 | demo_app/synthea_layer.py (+ repro_package/src, code_artefacts copies) | code, App A §A.9 | Bundle directory resolved from a search list: the regenerated cohort first, then `data/synthea_subset/`, then `./synthea_subset/`. Error message lists all three | The repo ships the 8-bundle subset, not a `synthea_run` tree, so Tab 3 could never find bundles | Ran from the new path: 8 bundles, mean 891 bytes, all six measures identical, 200/200 commitments differ. 132 → 152 lines. Three copies identical |
| P8-02 | demo_app/app.py | app only, no thesis text | New Tab 4, Norwegian context: the three classes with their floors and sources, a per-class results table, one case walkthrough per class, and the politiregisterloven cross-sector run with its no-structural-collision finding. Footer updated | Tiger's request for a plug-and-play exploring scenario in the app | Parses; tab logic smoke-tested outside Streamlit (160 records, 68 Sem I, 0 Sem II; cross-sector 7 violations, 0 structural). 275 → 404 lines |
| P8-03 | code_artefacts/README_Appendix_A.md | App A §A.1b, §A.2 note, §A.3, §A.5 | Contents table now lists `data/synthea_subset/` (8 untrimmed bundles) and the two Norwegian modules instead of three trimmed bundles; synthea_layer line count 132 → 152; §A.3 records the fallback path; §A.5 replaces the trimming note with the 891 vs 1,006 byte comparison | The appendix described files the repository does not contain | REJECT, intended: lost 132 and the two 25s, gained the new counts. §A.9 listing re-synced and verified identical to the file |
| P8-04 | 10_GitHub_Push/ | delivery | Rebuilt flat: every Python file at the root, because Streamlit Cloud runs `app.py` from there. README and push instructions rewritten for that layout; CHECKSUMS.md carries md5 and line counts | First upload showed the folder layout was not used | — |
| A-13 | Submission, bibliography | all | Rebuilt | — | Appendix A present verbatim; checker byte-identical |

The app's Tab 4 is explicitly labelled illustrative and not a thesis claim, in the tab text and in the footer.

## Session 22 September 2026, pass 7 — D7.2 read in full; Datatilsynet enquiry drafted

Source: TEHDAS2 D7.2, final version accepted 24 March 2026, DOI 10.5281/zenodo.20269109. Four findings bear on the thesis; all four are now in the text or acted on.

| ID | File | Section | Affects | Change | Source passage | Inspector |
|---|---|---|---|---|---|---|
| P7-01 | Chapter2 | §2.6 | Ch2 | D7.2 treats archival of pseudonymised data in an SPE as subject to Art 68(12), time-limited to permit validity and not open-ended: the obligation applied by location to data sitting in the environment, though to the permitted dataset rather than the logs. Also records that D7.2 expressly excludes the Digital Omnibus proposal of 19 Nov 2025 as undetermined, and that this thesis takes the same course | D7.2 §4.3 finalisation phase; §2.1 scope note | REJECT, gains only |
| P7-03 | Chapter4 | §4.9 | Ch4 | New paragraph: D7.2 holds that an unsalted hash of direct identifiers does not qualify as pseudonymisation, and requires the salt to be kept separate and secure as part of the pseudonymisation secrets. These are the same two requirements §4.8 places on the commitment and its salt. D7.2 also holds that irreversible pseudonymisation does not automatically meet the Recital 26 anonymisation threshold, which is this section's own conclusion by another route | D7.2 §4.4; §4.4 closing | REJECT, gains only |
| P7-04 | Chapter4 | §4.6 | Ch4 | D7.2's archival provision added as further evidence on the location reading, with its limit stated | D7.2 §4.3 | gains |
| P7-02, P7-05 | Chapter2, Chapter4 | References | Ch2, Ch4, bibliography | TEHDAS2 (2026c) added | — | reference list |
| P7-06 | Datatilsynet_Enquiry_DRAFT.md | new | — | Enquiry drafted in Norwegian and English: Q1 on accountability-preserving verifiability, Q2 on whether Art 68(12) reaches health data in the environment's own logs. States it is not an Art 36 prior consultation, sets expectations that any answer is an administrative view, and tabulates what changes in the thesis for each outcome | Ch6 §6.2, Ch7 §7.4 | not thesis text; needs João's approval before sending |
| A-11 | Submission, bibliography | all | all | Rebuilt | 73 entries, 51 with DOI/URL; all bodies present; 177 equations; both figures embedded; checker byte-identical | verified |
| A-12 | 07_Highlighted/PASS7_* | new | — | Highlighted copies of the two changed chapters plus combined HTML | — | not canonical |

Still unread: D7.1. Its deletion-at-closure content is partly visible through D7.2's citation of it on archival, and the thesis no longer attributes that claim to it.

## Session 22 September 2026, pass 6 — Rak, D6.3 final, two figures

| ID | File | Section | Affects | Change | Verified against | Inspector |
|---|---|---|---|---|---|---|
| P6-01 | Chapter1, Chapter2, Chapter4, Chapter6 | References and all in-text cites | Ch1, Ch2, Ch4, Ch6, bibliography | D6.3 cited as the final version: TEHDAS2 (2026a), DOI 10.5281/zenodo.20199187. D7.4 becomes TEHDAS2 (2026b). All six in-text citations renumbered | Zenodo record 20199187 and tehdas.eu results pages; the 2025 text was the draft that went to public consultation Oct–Nov 2025 | REJECT, intended: lost "TEHDAS2, 2025" and "TEHDAS2, 2026" throughout, gained 2026a and 2026b |
| P6-02 | Chapter2 | §2.3 | Ch2, bibliography | Rak (2024) cited: the Regulation is ambiguously drafted and its definition of electronic health data is singled out, which is the term on which the reach of Art 68(12) turns | EJRR 15(4), 928–938, DOI 10.1017/err.2024.67 | gains |
| P6-03 | Chapter4 | §4.6 | Ch4, bibliography | Rak (2024) added to the interpretive block: the peer-reviewed literature independently expects this ambiguity, which is a reason to put the question to a supervisory authority rather than settle it by argument | Same | gains |
| P6-04 | figures/figure1_regulatory_timeline.(svg\|png) + Chapter6 §6.8 | §6.8 | Ch6 | Figure 1, the implementation window: in force 26 Mar 2025, general application and Art 73(5) acts 26 Mar 2027, Chapter IV and Group One 26 Mar 2029, Group Two 2031, with the submission date marked | Regulation (EU) 2025/327 Arts 73(5), 105 | gains (figure reference) |
| P6-05 | figures/figure2_record_states.(svg\|png) + Chapter4 §4.8 | §4.8 | Ch4 | Figure 2, the three record states: LIVE, INVALIDATED (key and salt destroyed, commitment surviving, entry logged), TERMINAL at floor expiry | Ch4 §§4.7–4.9 as written | gains |
| A-10 | Submission, bibliography | all | all | Rebuilt | 72 entries, 50 with DOI/URL; 177 equations; both figures embed as PNG in the Word conversion (SVG needs rsvg-convert, which the build box lacks, so PNG is the referenced form and SVG ships as the source) | verified |

Checker byte-identical after the pass.

## Session 22 September 2026, pass 5 — adopted after verification (items 1, 2, 5)

Provenance note. These chapter edits were produced by an interrupted run earlier in the session and were found in the working copies without trail rows, while the delivered folder still held the clean pass-3 state. Tiger confirmed the run was his. Every addition was therefore verified against its source before being adopted, and each file was then gated through the inspector against the delivered pass-3 baseline. Nothing was adopted on the strength of it already being there.

| ID | File | Section | Affects | Change | Verified against | Inspector |
|---|---|---|---|---|---|---|
| P5-01 | Chapter6_Discussion_v1.md | §6.9 | Ch6, bibliography | MiFID II guess replaced by the politiregisterloven instance and the origin-anchoring finding: floor at 12 months, ceiling at 36, both from one origin, so no structural collision; the EHDS pair collides because Art 68(12) anchors its ceiling to permit expiry. Claim restated as "conflict when their origins differ" | Lovdata LOV-2010-05-28-16 § 17, §§ 50–51; the pass-4 run (0 of 60 structural, 7 erasure-driven) | REJECT, intended: lost hedge "candidate" with the removed MiFID guess, which a verified instance replaces |
| P5-02 | Chapter7_Conclusion_v1.md | §7.5 | Ch7, bibliography | Generalisation paragraph rewritten to the sharper question: which sectors anchor floor and ceiling differently, and whether a record-level ceiling can be discharged at all | Same | REJECT, intended: "is not obviously specific" → "is not specific", justified by the instance; lost "or that it does not" with the superseded sentence |
| P5-03 | Chapter2, Chapter3, Chapter4, Chapter5 | §2.1, §3.1, §4.1, §5.1 | Ch2–Ch5 | Opening hooks applied from `Opening_Hooks_Proposals.md`: the renumbering (Arts 46 and 50 → 68 and 73), the abandoned draft (28 citations, ~14 unverifiable), the supervisory-authority example, and record 100 | Each hook restates a claim already sourced in the thesis | gains only |
| P5-04 | Chapter2, Chapter4 | References | Ch2, Ch4, bibliography | Finck (2019): Study PE 634.445 added, and DOI 10.2861/535 | Publications Office record: ISBN 978-92-846-5044-6, DOI 10.2861/535, PE 634.445, July 2019 | reference list |
| P5-05 | Chapter2 | References | Ch2, bibliography | Staffa et al. (2018) DOI 10.1007/978-3-319-95189-8_2 | Springer chapter record, CCIS 821, pp. 11–27 | reference list |
| P5-06 | Chapter2, Chapter4 | References | Ch2, Ch4, bibliography | Scope et al. JDI (2022): pages 149–168 and DOI 10.26421/JDI3.1-4 | Rinton Press issue and NSF-PAR record | reference list |
| P5-07 | — | — | verification register | Scope & Rasin patent: no DOI exists for a US patent; the USPTO number 12,425,209 is the identifier. Item closed as not applicable | — | — |
| A-08 | Submission, bibliography (.md, .Rmd) | all | all | Rebuilt | 71 entries, 48 with DOI/URL (up from 70 and 44); all bodies present verbatim; 177 equations; checker byte-identical | verified |
| A-09 | 07_Highlighted/PASS5_* | new | — | Highlighted copies of the six changed files plus combined HTML, 14 marked blocks | — | not canonical |

Still open from the same request: D7.2 and D7.1 unread; the two figures not built; Zenodo DOI needs Tiger's account. Rak (2024) verified as EJRR 15(4), 928–938, DOI 10.1017/err.2024.67, and not yet cited: it argues the EHDS definition of "electronic health data" is drafted ambiguously, which is peer-reviewed support for the §4.6 hinge and should go in next.

## Session 22 September 2026, pass 4 — Norwegian context module (parallel, not in the thesis)

Canonical checker untouched and verified byte-identical afterwards. Both modules import `trf_checker.py` unmodified; no chapter changed in this pass.

| ID | File | Affects | Change | Reason / source | Verification |
|---|---|---|---|---|---|
| NO-01 | norwegian_module/norwegian_layer.py | none (parallel) | Three Norwegian record classes: NO-XB (F=120, Bodo/Stjordal inbound from PT/CZ/FI), NO-SPE (F=12, ceiling 6, Helsedataservice permit, NORTRE node or controller server), NO-JOURNAL (indefinite floor) | Tiger's request for a demo in Norwegian context; floors from eHDSI baseline, Art 73(1)(e), Art 68(12), pasientjournalloven s 25 | Runs; 160 records, 68 infeasible under Sem I, 0 under Sem II |
| NO-02 | same | none | NO-JOURNAL floor left INDEFINITE rather than numeric, truncated at 600 months for computation and labelled as such | Norwegian law sets no fixed period: journalforskriften s 14 and pasientjournalloven s 25 are purpose-based, and the government consultation paper states the ten-year figure is indicative only and as a rule cannot be applied | No number invented |
| NO-03 | norwegian_module/cross_sector_check.py | none | Cross-sector instance: politiregisterloven s 17, floor 12 months and ceiling 36 months on the same log, with ss 50-51 subject rights | Chapter 6 s 6.9 flags generalisation as uninvestigated | Verified at Lovdata (LOV-2010-05-28-16 s 17; FOR-2013-09-20-1097 ch. 40) |
| NO-04 | same | **candidate for Ch6 s 6.9, Ch7 s 7.5** | FINDING, contrary to expectation: the police provision produces NO structural collision. Floor and ceiling run from the same origin (t_a + 12, t_a + 36), defining a bounded window; only erasure requests inside it collide. The EHDS pair collides because Art 68(12) anchors its ceiling to an external event, permit expiry, which can precede the floor | Executed, not assumed | 0 of 60 structural, 7 of 60 erasure-driven |
| NO-05 | norwegian_module/NORWEGIAN_MODULE_README.md | none | Module documentation: what varies, what does not, run outputs, limits, sources | Demo for João | — |
| NO-06 | 08_Norwegian_Module/ | delivery | Modules plus captured run outputs | — | Canonical `trf_checker.py` byte-identical to the recorded run after the pass |

Correction made during the pass: my first version of the cross-sector module asserted a structural collision and crashed selecting a witness for one that does not exist. Both the code and its framing were rewritten around the actual result.

Stated limits carried with the module: illustrative not empirical; no Norwegian patient data, since Synthea has no Norwegian module; the police ceiling attaches to the whole record rather than a payload, so whether the mechanism transfers is unanswered.

## Session 22 September 2026, pass 3 — Article 68(12) primary text, D7.4 full text, case-law currency

Sources read this pass: TEHDAS2 D7.4 in full (24 Feb 2026, DOI 10.5281/zenodo.20266473) — requirements EHDSR-8 (all SPE logs kept at least one year), OPR-6 (electronic health data deleted **or rendered unrecoverable** within six months of permit expiry, backups included, subject to applicable legal obligations and traceability), §5.5 (termination and deletion balanced against logging and auditability), SPER-8 and OPR-17 (logging proportionate, no unnecessary user-behaviour detail). Article 68(12) primary text. CJEU, *EDPS v SRB*, C-413/23 P, 4 September 2025.

**The correction that drove the pass.** Six places quoted Article 68(12) as governing "the data within the secure processing environment". The text reads "the electronic health data within the secure processing environment". The broad reading survives on the location framing, but its object is electronic health data, so Corollary 1.2 is now stated for log records that carry such data, not for access logs at large. The division this forces — Art 73(1)(e) over the metadata, Art 68(12) over the health-data payload — coincides with the model's own decomposition, which strengthens §4.6 rather than weakening it.

| ID | File | Section | Affects | Change | Reason / source | Inspector |
|---|---|---|---|---|---|---|
| T-01 | Front_Matter_v1.md | Abstract | Front | Corollary 1.2 result scoped to log records carrying electronic health data | Art 68(12) text | ADMIT (with T-34) |
| T-02 | Chapter1 | §1.1 hook | Ch1 | Hook's second provision restated with the correct object | Art 68(12) text | ADMIT |
| T-03 | Chapter1 | §1.1 | Ch1 | Provision quoted verbatim; reading restated as location-based over electronic health data | Art 68(12) text | ADMIT |
| T-04, T-05 | Chapter1 | §1.2 | Ch1 | "personal data" → "electronic health data"; the emptying sentence scoped to log content | Art 68(12) text | ADMIT |
| T-06 | Chapter2 | §2.3 | Ch2 | Same correction, with the counter-argument (a bare log identifies the health data user, not the patient) stated | Art 68(12) text | REJECT, gains only |
| T-07, T-07b | Chapter2 | §2.6 | Ch2 | "Neither connects that deletion obligation …" replaced: D7.4 states both obligations and defers to legal exceptions without a mechanism; its "rendered unrecoverable" wording and its logging-minimisation caution recorded as support. Misattributed guideline name corrected to D6.3 | D7.4 read in full | REJECT: lost the sentence "has not addressed their interaction" and one Art 73(1)(e) reference — both the overclaim being removed |
| T-08 | Chapter2 | §2.9 | Ch2 | Absence claim narrowed to absence of a resolution, not of awareness | D7.4 | gains |
| T-09, T-10 | Chapter4 | §4.4 C3, §4.6 | Ch4 | Constraint C3 and Corollary 1.2 restated over electronic health data | Art 68(12) text | gains |
| T-11 | Chapter4 | §4.6 | Ch4 | Interpretive block rewritten: verbatim provision, the two features of its wording, the narrower claim, and the mapping of the two provisions onto m(a) and p(a) | Art 68(12) text | gains (+2 native equations) |
| T-12 | Chapter4 | §4.6 | Ch4 | D7.4's handling added as evidence of practice, consistent with either reading | D7.4 | gains |
| T-13 | Chapter4 | §4.9 | Ch4 | New paragraph: *EDPS v SRB* relative test (asymmetric, modest consequence) and D7.4's "deleted or rendered unrecoverable" | CJEU C-413/23 P; D7.4 | gains |
| T-14 | Chapter4 | §4.11 | Ch4 | D7.4's permissive deletion wording noted at the integration analysis | D7.4 | gains |
| T-15 | Chapter4 | References | Ch4, bibliography | CJEU judgment added (ECLI:EU:C:2025:645) | For T-13 | reference list |
| T-16, T-17, T-18 | Chapter5 | §5.2, §5.4 | Ch5 | SPE record class described as payload = health-data content, metadata = identifiable element; witnesses scoped | Art 68(12) text | gains |
| T-19, T-20, T-21 | Chapter6 | §6.1, §6.4 | Ch6 | Headline claim and the access-control rebuttal restated over electronic health data; scope of the claim stated | Art 68(12) text | gains |
| T-22 | Chapter6 | §6.8 | Ch6 | TEHDAS2 implication rewritten: both obligations stated, modes of discharge accepted, the health-data-in-logs case left unspecified | D7.4 | gains |
| T-23, T-24 | Chapter7 | §7.4 | Ch7 | Second authority question restated with the correct text and narrower scope; the Datatilsynet question reworded to match | Art 68(12) text | ADMIT |
| T-25, T-26 | Appendix_C | §C.5 Q7, §C.6 R3 | App C | Interview question and questionnaire item quote the provision correctly and ask about health-data content of logs | Art 68(12) text | ADMIT |
| T-27 to T-35 | Appendix_B, Chapter2, Front_Matter | App B, §2.1.1, §2.1.4, §2.1.7, §2.9, TOC | App B, Ch2, Front | Round 6 logged (7 queries, including the ITI-55 retrieval used in pass 2); 63 → 70 queries; five → six rounds; round purpose recorded | Queries run must be in the log | REJECT, intended: 63 → 70 |
| A-06 | Submission, bibliography (.md, .Rmd) | all | all | Rebuilt | 70 entries, 44 with DOI/URL; all bodies present verbatim; 177 native equations (up 2 from the new m(a)/p(a) spans in §4.6), no LaTeX leak; checker byte-identical | verified |
| A-07 | 07_Highlighted/ | new | — | Highlighted copies of the nine changed files plus one combined HTML; 35 marked spans, one per edit | Tiger's visual check | not canonical |

Cross-verification against the pass-2 state: Front 2 hunks, Ch1 3, Ch2 10, Ch4 7, Ch5 2, Ch6 4, Ch7 2, App B 1, App C 2. Every hunk carries an ID; the misquote now appears nowhere in the assembly (0 occurrences), and "electronic health data within the secure processing environment" appears 6 times. Ch3, Appendix A and the code are untouched in this pass.

## Session 22 September 2026, pass 2 — attack-and-strengthen (A1–A5)

Source fetched for A1: IHE ITI Technical Framework Vol. 2, rev. 20.1 (12 Dec 2024), §3.55 [ITI-55]: §3.55.4.1.2.1 (required query elements name and birth time; optional address, telecom, mother's maiden name) and §3.55.5.1.1 (audit message must carry ParticipantObjectQuery = QueryByParameter segment, base64-encoded).
Design decision A3 approved by Tiger before the pass.

| ID | File | Section | Affects | Change | Reason / source | Inspector |
|---|---|---|---|---|---|---|
| C-01a/b | Chapter1_Introduction_v2.md | §1.1, References | Ch1, bibliography | IHE International (2024) → (2024a) | Same author and year as the new ITI-55 source | REJECT, intended: label only |
| C-01c/d/e | Chapter2_LitReview_v2_FINAL.md | §2.3, References | Ch2, bibliography | (2024) → (2024a); IHE International (2024b) ITI-55 added | Same. An insertion bug of mine fused the two entries on one line; caught on read-back and repaired; ATNA entry verified identical except its label | REJECT, intended |
| A1-a | Chapter2 | §2.3 | Ch2 | New sentences: an audit record is not the clinical document; ITI-55 audit carries the encoded demographic query | A1 | (in the Ch2 reject above; gains only) |
| A1-b | Chapter4_TRF_Model_v1.md | §4.2 | Ch4 | Medication-list example replaced: what ATNA actually holds, and why accountability does not need the typed demographics | A1: previous example was inaccurate | REJECT, intended |
| A2-a | Chapter4 | §4.2 | Ch4 | New paragraph: the valid ground for erasure of an audit record (17(1)(b) and Art 21(1) unavailable under 6(1)(c); 17(3)(b) shields the required part; 17(1)(d) reaches the excess via 5(1)(c)); marked as carrying the same want of authority as §6.2 | A2 | gains |
| A2-b | Chapter4 | §4.6 Cor 1.1 | Ch4 | "Generic case" claim replaced by conditional statement pointing to §4.2 and §3.7 | A2: overclaim | lost "Article 17" (intended) |
| A1-c | Chapter4 | §4.3 | Ch4 | p(a) redefined as personal data beyond the accountability skeleton (encoded query; SPE activity detail); abstract, never read | A1 | gains |
| A5-a/b | Chapter4 | §4.5, §4.12 | Ch4 | Semantics I no longer "implicit in current practice"; stated as the unattributed default of whole-record retention | A5: no source existed | — |
| A4-a | Chapter4 | §4.7 | Ch4 | "Theorem 1 carries the load" replaced: both theorems immediate; contribution is the translation they make checkable | A4 | lost one "2" (intended) |
| A3-a…i | Chapter4 | §4.8, §4.9, §4.12 | Ch4 | Salt destroyed with the key at invalidation; commitment survives as unopenable chained seal; optional opening to data subject (unspecified); residue list, threat example, response, honest limit, auditor view, terminal transition, summary aligned | A3 design change | hedges "unconditionally" and one "candidate" removed with the retained-salt sentence (intended; the pseudonymisation limit is kept in "The honest limit") |
| C-01f | Chapter4 | References | Ch4, bibliography | ITI-55 entry added | A1 citation | intended |
| A1-d | Chapter5_Demonstration_v1.md | §5.2 | Ch5 | States that clinical resources are not ATNA content and why they are used | A1 | gains |
| A3-j | Chapter5 | §5.6 | Ch5 | Trajectory description: salt destroyed with the key | A3 | — |
| D-07a/b | Chapter5 | §5.2 | Ch5 | 362 → 363 lines; 275 → 276 non-blank non-comment | One code line added | intended |
| D-08a | Chapter3_Methodology_v1.md | §3.6 | Ch3 | "fifty to one hundred lines" → "constraint logic on the order of ninety lines" | Contradicted Ch5 (363 lines) | gains |
| D-08b | Chapter3 | §3.6 | Ch3 | Realism layer: "constructing metadata from encounter events" and "two to four hundred lines" corrected to what the code does (labels document category) and its size (132 lines) | Overclaim found while reading the code | gains |
| A1-e | Chapter3 | §3.6 | Ch3 | Realism layer's function restated as the invariance test only | A1 | gains |
| A3-k | Chapter3 | §3.6 | Ch3 | Simulated destruction covers key and salt | A3 | — |
| A3-l, D-07c/d, A3-m | code_artefacts/README_Appendix_A.md | §A.4, §A.1b, §A.8 | App A | Trajectory text; 362 → 363; source listing gains the salt line | A3 | intended; §A.8 listing verified identical to the file |
| A3-n | demo_app/, repro_package/src/, code_artefacts/ trf_checker.py | apply_invalidation | code | `rec.salt = None` after key destruction (1 line) | A3 | three copies identical; main output byte-identical to recorded run; δ-witness unchanged (90/95/39/0/138; 89/94/39/0/138); realism layer on 8-bundle subset identical, 200/200 commitments differ; 138 invalidated records have key and salt None, 62 live records keep both |
| A-04 | repro_package/docs/Appendix_A.md | all | repro package | Replaced with current App A | Was already stale at session start (16 Sept text) | n/a |
| A-05 | Submission, bibliography (.md, .Rmd) | all | all | Rebuilt | 69 entries (+ITI-55), 43 with DOI/URL; order otherwise unchanged; all bodies present verbatim; 175 equations, 0 LaTeX leak | verified |

Cross-verification against the folder delivered earlier today: Ch1 2 hunks (C-01a, C-01b); Ch2 2 (A1-a+C-01c; C-01d/e); Ch3 3 (D-08a; D-08b+A1-e; A3-k); Ch4 15 (A1-b, A2-a, A1-c, A5-a, A2-b, A4-a, A3-a, A3-b, A3-c, A3-d, A3-e, A3-f, A3-g, A5-b+A3-h+A3-i, C-01f); Ch5 3 (D-07a/b; A1-d; A3-j); App A 4 (A3-l, D-07c, D-07d, A3-m); code 1 line (A3-n). Front matter, Ch6, Ch7, App B, App C unchanged. Every hunk has an ID; every ID has its hunk.

## Session 22 September 2026, pass 1

| ID | File | Section | Affects | Change | Reason / source | Inspector |
|---|---|---|---|---|---|---|
| D-01 | Chapter2_LitReview_v2_FINAL.md | §2.2 | Ch2 (+ bibliography) | "designate a National Digital Health Authority by June 2025 … certify … by January 2026 (Ernst & Young, 2025)" → Art 19(1): inform Commission of digital health authorities by 26 March 2027, cited to the Regulation | Secondary source contradicted the primary text (OJ L 2025/327, Art 19(1), retrieved via EUR-Lex). Certification clause removed: no primary date verified | REJECT, intended: lost EY citation, June 2025, Jan 2026; gained Regulation citation, Art 19(1), 26 March 2027 |
| D-01b | Chapter2 | References | Ch2, bibliography | Ernst & Young (2025) entry removed | No longer cited anywhere | REJECT, intended (reference list) |
| D-02 | Chapter2 | §2.5 | Ch2 | "European Data Protection Board, 2025" → "2026b" | Phantom citation: no 2025 entry exists; Guidelines 02/2025 are 2026b (v2.0) | REJECT, intended |
| D-03a/b | Chapter4_TRF_Model_v1.md | §4.10, §4.12 | Ch4 | "Four are treated here" / "Four rival designs" → "Five" | §4.10 treats five rivals since DePaul (Rival 5) was added | ADMIT on prose; REJECT only for N-05b |
| D-04a | Chapter5_Demonstration_v1.md | §5.2 | Ch5 | 322 lines / 246 → 362 lines / 275 neither blank nor comment | `wc -l` = 362; δ-witness block added after text written | REJECT, intended: 322, 246 → 362, 275 |
| D-04b | code_artefacts/README_Appendix_A.md | §A.1b | App A | 322 → 362 | Matches §A.8 and file | REJECT, intended |
| D-05 | README_Appendix_A.md | §A.4 | App A | False claim "code states in a comment … CSPRNG" replaced by an accurate statement of the salt's reproducibility-only status | No such comment exists (line 63). Text fixed, code untouched, so checksums and outputs unchanged | (same file as D-04b) |
| D-06a/b | Appendix_C_Evaluation_Instrument.md | header, §C.8 | App C | §3.9 ↔ §3.8 cross-references swapped to correct targets | Execution status is §3.8; ethics statement is §3.9 | ADMIT |
| N-01 | Chapter2 | §2.4 | Ch2 | New paragraph: aiAuthZ (Kodathala, 2026) as convergent practice; "verifiability semantics" delta narrowed | Round 5 jeopardy check; paper read in full (arXiv HTML §1.4, §3.4) | REJECT, gains only |
| N-02 | Chapter2 | §2.9 | Ch2 | New paragraph: Borovits, Tamburri & van den Heuvel (2026) SLR as independent academic corroboration of the gap | Round 5; read §1, §3.2, §3.3.12 | REJECT, gains only |
| N-03, N-04 | Chapter2 | References | Ch2, bibliography | Borovits et al. (2026) and Kodathala (2026) added, arXiv DOIs | For N-01, N-02 | REJECT, gains only |
| N-05a/b/c | Chapter2, Chapter4, Chapter6 | References | Ch2, Ch4, Ch6, bibliography | TEHDAS2 (2026) D7.4: date 24 Feb 2026, lead author, DOI 10.5281/zenodo.20266473 | Zenodo record retrieved | REJECT, reference list only |
| N-06a–j | Chapter2, Front_Matter_v1.md, Appendix_B_Search_Log.md | §2.1.1, §2.1.4, §2.1.7, §2.9, TOC, App B | Ch2, Front, App B | Round 5 (22 Sept, 4 queries) logged; 59 → 63 queries; four → five rounds; three adversarial | Queries run this session must be in the log | REJECT, intended: 59 → 63 |
| A-01 | VERA-SNARK_Thesis_SUBMISSION.md, Consolidated_Bibliography.md | all | all | Rebuilt with assemble.py | Bibliography 67 → 68 entries (−EY, +2), 42 with DOI/URL | Verified: 175 native equations, 0 LaTeX leak; checker output byte-identical |
| H-01 | Chapter1_Introduction_v2.md | §1.1, first paragraph | Ch1 (+ assembly) | Unsourced superlative ("most significant data-governance transformation in its history") replaced by a merged Norwegian-context hook: Bodø/Stjørdal gateway live but nearly empty, then the Art 73(1)(e)/68(12) collision, conditional on one reading and on EEA incorporation | Supervisor request; Tiger chose a mix of Options A and B. Sources already in thesis: Helsedirektoratet (2026a), §1.1, §4.6 | REJECT, gains only: +(Helsedirektoratet, 2026a). Assembly diff: 1 paragraph replaced, nothing else changed; 175 equations; checker byte-identical |
| N-05d | Chapter2, Chapter4, Chapter6 | References | Ch2, Ch4, Ch6, bibliography | TEHDAS2 (2026) entry: "(2026, 24 February)" → "(2026)" with "published 24 February 2026" moved inside the bracket | Regression caught in cross-verification: the dated form sorted D7.4 (2026) before D6.3 (2025), breaking APA same-author year order | REJECT, reference list only; order restored (2025 at line 150, 2026 at 152) |
| A-02 | Consolidated_Bibliography.Rmd | all | bibliography (knit copy) | Body re-synced from the .md; YAML header kept | Was already stale at session start (19 Sept vs .md 21 Sept); now 68 = 68 entries | n/a (generated) |
| A-03 | VERA-SNARK_Thesis_SUBMISSION.md, Consolidated_Bibliography.md | all | all | Final rebuild after N-05d | Every current chapter and appendix verified present verbatim in the assembly | 175 equations; checker byte-identical |
| M-01 | HANDOFF_READ_FIRST.md | §0, §6, §8a, §9 | control | Resume step 6 (trail rule); file table (App B 63/5, bibliography 68/42, new files); completed list; open work re-prioritised | Keep handoff truthful | n/a (control file) |
| M-02 | VERSION_REGISTER.md | table, reconciled line, non-canonical list | control | Checksums recomputed after final edit; CHANGE_TRAIL and hooks rows added; stale top-level code copies listed as non-canonical | Register must match files | 0 mismatches |
| M-03 | CHANGE_TRAIL.md, Opening_Hooks_Proposals.md | new | control | Created; hooks file marks Ch1 as applied (H-01) | Tiger's trail rule; supervisor request | n/a |
| P-01 | Opening_Hooks_Proposals.md | new | Ch1–5 (proposed) | Hook drafts for approval; nothing applied | Supervisor request | n/a |

## Cross-verification, 22 September 2026

Every canonical file was diffed against the session-start archive (`files__2_.zip`). Each changed line is mapped to a trail ID; no change exists without one, and no ID exists without its change.

| File | Status | Diff hunks | Trail IDs |
|---|---|---|---|
| Front_Matter_v1.md | patched | 1 | N-06h |
| Chapter1_Introduction_v2.md | patched | 1 | H-01 |
| Chapter2_LitReview_v2_FINAL.md | patched | 14 | N-06b, N-06a, N-06c, N-06d, N-06e, N-06f, D-01, N-01, D-02, N-06g + N-02 (same paragraph), N-03, D-01b + N-04 (adjacent), N-05a/N-05d |
| Chapter3_Methodology_v1.md | unchanged | 0 | — |
| Chapter4_TRF_Model_v1.md | patched | 3 | D-03a, D-03b, N-05b/N-05d |
| Chapter5_Demonstration_v1.md | patched | 1 | D-04a |
| Chapter6_Discussion_v1.md | patched | 1 | N-05c/N-05d |
| Chapter7_Conclusion_v1.md | unchanged | 0 | — |
| Appendix A (README_Appendix_A.md) | patched | 2 | D-04b, D-05 |
| Appendix_B_Search_Log.md | patched | 2 | N-06i, N-06j |
| Appendix_C_Evaluation_Instrument.md | patched | 2 | D-06a, D-06b |
| Consolidated_Bibliography.md / .Rmd | regenerated | — | A-01, A-02, A-03 |
| VERA-SNARK_Thesis_SUBMISSION.md | regenerated | — | A-01, A-03 (every chapter verified present verbatim) |
| trf_checker.py, synthea_layer.py, app.py | unchanged | 0 | — |

Checks after the last edit: checker output byte-identical to the recorded run; 175 native Word equations, no LaTeX leakage; bibliography 68 entries, 42 with DOI/URL, APA order intact.

## Repository completion, 28 September 2026

The 23 September push was made through GitHub's web uploader, which flattens directory structure. Three effects followed: `docs/Appendix_A.md` and `norwegian_docs/NORWEGIAN_MODULE_README.md` landed at the repository root under different names, `norwegian_docs/HOW_TO_RUN.md` and `requirements.txt` were dropped entirely, and `data/synthea_subset/` was never uploaded. `README.md` and `CHECKSUMS.md` described the intended layout, so both documented paths that did not exist. Tab 3 of the deployed app therefore reported no bundles found.

This entry records the repair. No Python source was edited.

| ID | File | Change | Reason | Verification |
|---|---|---|---|---|
| R-01 | `data/synthea_subset/*.json` | Added the 8 untrimmed Synthea bundles, 40 MB, unmodified | Tab 3 had no data; README and CHECKSUMS both listed the directory | `python3 synthea_layer.py` reads 8 bundles, mean payload 891 bytes, six measures identical to the constructed run, 200/200 commitments differing |
| R-02 | `data/synthea_subset/README.md` | New. Generation command, the 98-from-100 count, the six provenance markers, the invariance table, the 891 vs 1,006 byte statement | Provenance must travel with the data, not only with the thesis | Every claim carried over from `Data_Provenance_Statement.md`, which was verified by inspection on 18 September |
| R-03 | `requirements.txt` | Restored: `streamlit>=1.30` | Streamlit Cloud installs from it; its absence left the deployment on whatever the platform defaulted to | md5 `944269ad914f`, matching the value CHECKSUMS.md recorded before the upload |
| R-04 | `docs/expected_trf_output.txt` | Restored by running `python3 trf_checker.py` and capturing stdout | README instructs the reader to diff against it; the file was missing | md5 `41b56742d35d`, matching the recorded value, and byte-identical to `repro_package/results/trf_output.txt` |
| R-05 | `README_Appendix_A.md` → `docs/Appendix_A.md` | Moved, contents untouched | README and PUSH_INSTRUCTIONS both reference the `docs/` path | md5 `71d1eb8f91c5` before and after, matching CHECKSUMS |
| R-06 | `NORWEGIAN_MODULE_README.md` → `norwegian_docs/NORWEGIAN_MODULE_README.md` | Moved, contents untouched | README references the `norwegian_docs/` path | md5 `75a47ac43d91` before and after, matching CHECKSUMS |
| R-07 | `norwegian_docs/HOW_TO_RUN.md` | Rewritten. The original 116-line file was not uploaded and no copy survives in the working set | README links to it; a dangling link is worse than a rewrite | Every figure in it was taken from an actual run of the three modules on 28 September, not from recollection. The file differs from the lost original: its md5 is `70bce00b2315`, not the recorded `6cb6ce1b710a`, and it is 103 lines, not 116 |
| R-08 | `CHECKSUMS.md` | Regenerated from the files actually present | It recorded `app.py` at 404 lines and md5 `52bf6c71ffd7`; the repository holds 418 lines and `b74ec9905035`, so the record was stale for that file and wrong about six paths | Generated by reading the files, not by editing the table |

Checks after the last edit: `python3 trf_checker.py` byte-identical to `docs/expected_trf_output.txt`; `python3 synthea_layer.py` reports 891 bytes and six identical measures; `norwegian_layer.py` and `cross_sector_check.py` both run clean. The canonical thesis figures are unchanged: 90/200 records, 95 violations, 39 Corollary 1.2 witnesses, 138 invalidations, 0 Semantics II violations, reference commitment `11087780fd192c8f`.

One divergence is recorded rather than resolved: `trf_checker.py` in this repository carries `rec.salt = None` at invalidation, implementing the salt destruction of Chapter 4 §4.8, which the copy in the working set does not. The repository is ahead. The line changes no reported figure, which the byte-identical output above establishes.

| R-09 | `docs/Appendix_A.md` | Contents table: `norwegian/norwegian_layer.py` → `norwegian_layer.py`, same for `cross_sector_check.py` | Both files sit at the repository root, as README.md states and as Streamlit Cloud requires; the appendix described a directory that does not exist | Applied identically to all four copies: the repository, `code_artefacts/`, `repro_package/docs/`, and the assembled thesis. All four carry md5 `2f4323a8545f` for the standalone file |
| R-10 | reproducibility package | `trf_checker.py`, `synthea_layer.py`, `norwegian_layer.py`, `cross_sector_check.py` moved from `src/` and `src/norwegian/` to the package root; `data/synthea_sample/` (3 trimmed bundles) replaced by `data/synthea_subset/` (8 untrimmed); `run_all.sh` and `README.md` rewritten | The layer resolves its data directory relative to its own file, so from `src/` it looked for `src/data/synthea_subset/` and found nothing; the Norwegian modules under `src/norwegian/` could not `import trf_checker`; and `run_all.sh` skipped the realism layer entirely unless the full 314 MB cohort was present | `bash run_all.sh` runs all four steps clean. Checker output byte-identical to `results/trf_output.txt` |
| R-11 | `repro_package/results/` | `synthea_comparison_output.txt` → `synthea_comparison_full_cohort_output.txt`; new `synthea_comparison_subset_output.txt` | The recorded comparison was the 98-bundle run at 1,006 bytes, but the package ships the 8-bundle subset at 891, so `run_all.sh` told the reader to expect a byte-identical diff that cannot be identical | Both runs recorded. They differ in exactly two lines, the bundle count and the mean payload; no reported measure moves |

## Feature completion and recorded runs, 28 September 2026

An audit of the app against what `trf_checker.py` exposes found two reported results with no viewer anywhere. Both are the results a reader presses hardest on, and neither was reachable from the demonstration.

| ID | File | Change | Reason | Verification |
|---|---|---|---|---|
| R-12 | `app.py` | New Tab 5, "Robustness and cross-checks". Runs `brute_force_semantics_I()` over the four cases and `delta_witness()` over δ = 1 and δ = 3, each with a pass or fail banner, then restates the artefact's limits | `brute_force_semantics_I()` answers the objection that infeasibility rests on one implementation, and the δ witness answers the objection that it rests on a one-month response period. Chapter 5 §5.4 and §5.2a report both; the app showed neither | Four cases run: all agree with `docs/expected_trf_output.txt`, control returns feasible. δ witness returns 90/95 at δ = 1 and 89/94 at δ = 3, matching Table 5.2a exactly. App serves HTTP 200 headless with no errors |
| R-12a | `app.py` | Cross-check case parameters taken verbatim from `trf_checker.main()` | I first wrote them from memory and two were wrong: case 1 returned feasible=True against a recorded False. Caught by executing before committing, not by reading | The four now reproduce the recorded line for line |
| R-13 | `docs/expected_delta_witness_output.txt`, `expected_synthea_subset_output.txt`, `expected_norwegian_output.txt`, `expected_cross_sector_output.txt` | New. One recorded run per command | Only the checker had a recorded output to diff against. The other four commands had none, so a reader could not tell a changed file from a changed result | Each generated by running its command and capturing stdout |
| R-14 | `docs/Data_Provenance_Statement.md` | Added to the repository | It answers the supervisor's data blocker and lives where a reader who clones can find it, not only in the thesis working set | Byte-identical to the working-set copy |
| R-15 | `README.md` | Documents Tab 5, the recorded-run table, and the robustness section; `app.py` line count 404 → 524 | The README described four tabs and one recorded output | Line count read from the file |

Not changed, and why: `cross_sector_check.py` was already committed on 23 September and already wired into Tab 4 at line 378 with its own button and result banner. Verified by `git ls-tree`, by reading the file, and by importing and running `cs.build()` headless: 60 records, 7 Semantics I violations, 0 structural. The gap was the two results above, not this module.

## Citation link pass and source verification, 28 September 2026

The bibliography carried 68 entries of which 41 had a DOI or URL and 27 had neither. Four parallel searches were run to close that gap, each instructed to fetch and quote page evidence and to report NOT FOUND rather than construct a plausible locator. The pass closed the gap and also found that several entries cited documents that do not exist as described. The most consequential of those were re-verified by direct fetch before anything was changed.

All edits were made to the chapter reference lists, which are the source `handoff_tools/assemble.py` regenerates the bibliography from. Editing the bibliography directly would have been overwritten by the next rebuild.

| ID | Entry | Change | Evidence |
|---|---|---|---|
| C-01 | 30 entries across all seven chapters | DOI or URL added | Each fetched and matched on title, issuer and year before use |
| C-02 | VeritasChain Standards Organization (2026), Ch2 | Author to `VeritasChain`; annotation records that it is a self-declared standards initiative founded 24 November 2025, operationally supported by VeritasChain Inc., not accredited by any recognised standards body. In-text form standardised to `(VeritasChain, 2026)` | Their own company page, fetched directly by me: founded "November 24, 2025", "aspiring to be an organization with authority comparable to ISO, IEEE, and IETF" — aspiration, not accreditation; no officers, staff or members listed; a disclaimer distancing them from a similarly-named entity on investor warning lists. Kept rather than dropped because Ch2 §2.5, the §2.8 comparison table and the §2.9 gap statement all rest on it as the practitioner pattern; the fix is accurate attribution, not removal |
| C-03 | European Commission (2025c), *Implementation calendar*, Ch1 and Ch2 | **Entry removed.** In-text merged into `(European Commission, 2025a)` | No such publication exists. Fetched directly by me: the milestones are a section of the 2025a page headed "Key milestones towards full implementation". The facts the citation supported are unchanged and correctly sourced to 2025a |
| C-04 | Helsedirektoratet (2026b), *MyHealth@EU, Norsk helsenett*, Ch1, Ch2, Ch4, Ch6 | **Entry removed.** Remaining 2026a relabelled 2026 | The page returns HTTP 404, confirmed by my own fetch. The live portfolio lists MyHealth@EU measures for Helsedirektoratet and for KS; no Norsk helsenett measure exists |
| C-04a | `(Helsedirektoratet, 2026a, 2026b)` in Ch1, Ch2, Ch4, Ch6 | Collapsed to `(Helsedirektoratet, 2026)` | **Found by the inspector, not by me.** My own grep searched for `Helsedirektoratet, 2026b` and missed the combined form, leaving four citations pointing at a deleted reference. The narrow-detector failure again |
| C-05 | IHE International (2024), Ch1 and Ch2 | Year corrected to 2023; revision stated | Fetched directly by me: the ATNA chapter header reads "Revision 20.0, August 4, 2023 – Final Text". The current volume revision is 20.2, November 2025. 2024 is neither |
| C-06 | Helsedataservice (2024), *Application workflow and fees*, Ch2 | Retitled *Fees and processing times*, year to n.d. with a retrieval date | No page of that title exists on helsedata.no; the real page is "Fees and Processing Times" and carries no publication year |
| C-07 | TEHDAS2 (2025) D6.3, Ch1, Ch2, Ch4 | Identified as Version 1.5, final draft, 17 September 2025 | The final D6.3 is v2.0 dated 24 February 2026. Keeping the 2025 dating required naming the draft status, which is what the document is |
| C-08 | Scope et al. (2022), Ch2 | Page range 149–168 added | Publisher PDF. Note: the PDF header prints 2021 while the publisher's contents page dates the issue February 2022. The 2022 in the thesis matches the publisher's issue date; the discrepancy is Rinton Press's |
| C-09 | Deloitte Advokatfirma (n.d.), Ch3 | Year 2020 | The page states "Publisert 24.08.2020", so n.d. was avoidable |
| C-10 | Norsk forening for allmennmedisin (2025), Ch2 | "analyserum" corrected to "analyserom"; full title restored | Transcription error against the source document |
| C-11 | Norwegian Maritime Authority (2023), Ch2 | Retitled to the amending circular, *Amendments to the Health Regulations reflecting the GDPR* (RSR 2-2023) | The cited title was the regulations' name, not the instrument that amended them |
| C-12 | Healthy Europe (2026), Ch2 | Retitled *EHDS progress report: Where does Europe's Health Data Space stand?* | The cited title was the page's SEO title, not its headline |
| C-13 | EDPB (2026a) and (2026b), all chapters | Titles corrected to the EDPB's own wording | "Coordinated Enforcement Action, implementation of the right to erasure by controllers"; "on processing", not "on the processing" |
| C-14 | Norwegian Trusted Research Environments, Ch1 and Ch2 | Year to n.d. with a retrieval date | The site carries no date, copyright year or version marker |
| C-15 | Helsedirektoratet (2023) → (2024), Ch2 | Year corrected, title corrected, chapter-level URL | The annual report covers 2023 but was published 25 April 2024; the merger claim it supports is in the *Styring og kontroll i virksomheten* chapter |
| C-16 | SPUHiN (2025) D5.2 | Left without a direct locator; the entry now says so and links the project page instead | The consultation page has been withdrawn and returns 404; the attachment URL exceeds the fetcher's length limit. The deliverable number and the July–October 2025 hearing window are confirmed on the project page. **Reporting this honestly rather than substituting a nearby link** |
| C-17 | Four entries in Ch1, Ch2 and Ch3 | Redundant second URL trimmed | My own patch appended a locator to lines that already carried one in that chapter's variant. See the note below |

**Defect found in `assemble.py`, not yet fixed.** The deduplication rule keeps the *longer* of two variants of the same entry. Where one chapter carried a short line with a URL and another carried a longer annotated line without one, the longer unlinked variant won, and the bibliography reported an entry as unlinked while a working link existed elsewhere in the thesis. That is why C-17 was needed and why the original count of 27 was slightly overstated. The rule should prefer a variant that contains a locator, then length.

**Result.** 68 entries with 41 linked, to **66 entries with 66 linked**. Two entries were removed because the documents do not exist as cited. Nothing was linked that was not fetched.

**Inspector, per chapter, old against new.** Six chapters REJECT and Chapter 7 ADMITs. Every rejection is accounted for and each is intended: the reference-list check fails because rewriting reference lists is the entire change; the citation and numeral checks fail only on the year tokens listed above, each with its replacement present. Hedges passed in all seven chapters, sentence counts above forty words are unchanged in all seven, and the word delta is between zero and three per chapter, entirely from `2026a, 2026b` collapsing to `2026`. No prose was rewritten and no claim was altered.

**Not done, and why.** An orphan-citation audit (every in-text citation has a reference and every reference is cited) was attempted and abandoned: the regular expression mis-parses multi-author and multi-work citations such as `(Hevner, March, Park, & Ram, 2004)`, producing false positives at a rate that makes the output unusable. It needs a proper citation parser and is recorded as open work rather than reported as a result.

## Em-dash reduction and citation repair, 28 September 2026 (second pass)

Raised against the assembled submission: too many em-dashes, a broken inline citation, and several items reported as unpatched. Each claim was checked against the file before any edit. Note first that the chapter files, front matter, Appendix A and the bibliography were modified at 08:34–08:35 by work from outside this conversation; eleven of the register's checksums no longer matched when this pass began, and several items reported missing were already present in the file on disk.

| ID | Change | Method | Verification |
|---|---|---|---|
| E-01 | Structural labels: `*C1 — Retention floor.*` to `*C1: Retention floor.*`, and the same for Activity, Step, Rival, Semantics and Secondary use | Regex over prose lines only; code fences, table rows and blockquotes excluded | Word sequence identical; only the standalone dash token removed |
| E-02 | Table and figure captions: `*Table 5.1 — Violations…*` to `*Table 5.1. Violations…*` | As above | 6 captions; the detector's sentence-boundary count rose by exactly 6, which is what the transform produces |
| E-03 | Table-of-contents glosses and appendix labels to colons | As above | 10 in front matter |
| E-04 | 15 headings de-dashed; the `## References` heading deliberately left alone because `assemble.py` splits chapters on that exact string | Regex, heading lines only | Assembly verified working afterwards |
| E-05 | Six paired asides converted to parentheses or commas, each judged individually | Hand-written, gated on word-sequence identity | Every word preserved in each |
| E-06 | Appendix A, B and C step labels | As E-01 | Word sequence identical |
| C-18 | **Broken citation.** Chapter 2 cited `(European Data Protection Board, 2025)`; no such entry exists. Resolved to `2026b` | 2026b is the Guidelines accepting key deletion as serving the erasure obligation, which is the claim the sentence makes; 2026a is the enforcement report and does not support it | One of 77 citation keys; the other 76 resolve |
| E-07 | **Surviving corruption from the earlier em-dash pass, found in a canonical file.** Appendix B read "The closest prior art — the DePaul retention-and-purging programme and United States Patent 12,425,209: was located" — an opening dash whose partner had become a colon | Repaired to commas | A corpus-wide sweep for the pattern now returns **0** in the submission and in every canonical chapter. Roughly fifty instances remain in `_draft_Thesis_FULL_with_chapter_refs.md` and one in `_superseded_Chapter2_RETROFIT.md`, both marked non-canonical and deliberately left as the record of what was corrected |

**Result.** Em-dashes 230 to 110. Prose 117 to 12, headings 15 to 0. Tables (51) and code blocks (47) untouched, correctly: table cells use the dash to mean "not applicable" and code is verbatim.

The 12 remaining prose dashes are each defensible and are left on purpose: 7 are inside source titles in the reference list (*Advances in Cryptology — EUROCRYPT '93*, *Security in Computer and Information Sciences — Euro-CYBERSEC 2018*, the Norwegian *Høring — Oversikt…*), which may not be altered; 1 is verbatim console output inside a blockquote; 2 are in the supervisor-approved research question, which is not to be altered without the author's decision; and 2 form an appositive whose aside already ends in a parenthetical citation, where nesting parentheses would read worse than the dash pair.

**Inspector, old against new, all eight files.** Seven ADMIT. Chapter 2 alone rejects, on exactly the C-18 citation change and nothing else. Reference lists, hedges and sentence counts passed in all eight; sentences over forty words are unchanged in every file.

**Figures re-verified against the live artefact, not against the document.** Ran the checker, the delta witness and the realism layer, then compared: 90/200 records, 95 violations, 39 Corollary 1.2 witnesses, 138 invalidated (52 GDPR, 86 EHDS), 0 under Semantics II, 90/95 at δ=1 against 89/94 at δ=3, 891 bytes on 8 bundles, 200/200 commitments differing, module line counts 363/152/135/110/526. Every one matches what the thesis states.

**One error of my own, recorded.** Correcting the repository README's `app.py` line count, I used `len(text.split("\n"))`, which counts the trailing empty element, and wrote 527. `wc -l` is 526, which is what the thesis says. Caught and corrected in the next commit rather than left standing.

## Appendices, formatting system and the highlighting question, 29 September 2026

| ID | Change | Reason | Verification |
|---|---|---|---|
| X-01 | Appendix B: **Round 5 added**, the 28 September locator-verification and source-standing audit, 18 targets | The appendix states it is a complete log "including those that produced nothing usable". Its last round was 16 September, so the round that removed two bibliography entries was absent and the completeness claim was false | Recorded by target rather than by verbatim query string, because the round was executed as four parallel verification sweeps. Inventing query strings would be worse than reporting none, and the appendix says so |
| X-02 | Appendix C: **new §C.1a**, status of the instrument and what is expected to change | An instrument that has never been administered is a hypothesis about what respondents will understand, not a measurement device. Nothing in the appendix said so | Names five things expected to change (item wording, panel, session length, coding frame) and one that is not: items are not to be reworded toward agreement if early responses are unfavourable. Records item A1's known overstatement of the thesis's own claim |
| X-03 | Appendix A: `docs/Data_Provenance_Statement.md` added to the contents table | The repository ships it; the appendix did not list it | Contents table now matches the repository |
| X-04 | `thesis_yaml_header.yml`: code highlighting **breezedark → tango** | breezedark is a dark IDE theme. No thesis guideline, style manual or publisher instruction contemplates dark code backgrounds; APA prescribes only "a monospace font such as 10-point Lucida Console or 10-point Courier New". A dark field wrecks greyscale printing and reads as a slide deck pasted into a thesis. **This reverses an earlier decision in this project, on evidence** | Rebuilt and inspected |
| X-05 | `thesis_reference.docx` built: A4, 2.5 cm margins, Times New Roman 12 pt, 1.5 spacing, justified body, styled heading hierarchy, captions kept with their object, monospace 9 pt code | The Word build previously used pandoc defaults, and page size was unset, so Word would apply its locale default (Letter in some installs) rather than A4 | Verified by reopening: A4 21.0 × 29.7 cm, 16.0 cm usable text width |
| X-06 | Tables: 11 wide tables set to 8 pt, 14 to 9.5 pt, all autofit, header rows repeat across page breaks | Five tables exceeded the 16 cm text block, one at 7 columns and 365 characters per row. The markdown was valid; the defect was overflow, not syntax | 25 tables, 0 malformed, header repetition verified in the XML |
| X-07 | Table style carries no vertical rules and no shading | APA: "Do not use vertical borders to separate data"; "Avoid the use of shading in tables". booktabs: "Never, ever use vertical rules. Never use double rules" | Pandoc's default table style already complies; confirmed rather than assumed |

**On highlighting, researched rather than assumed.** HiMolde's own template and guidelines are unreachable from this environment (403 on every himolde.no URL), so the binding constraint could not be read and must be obtained by the author. What was read: UNC-Chapel Hill's graduate school names "highlighting intended solely to draw a reader's attention to a key phrase" as "extraneous or unprofessional", and restricts colour to "tables, figures, illustrations, and active website or document links". APA offers no highlighting device at all; its emphasis toolkit is italics and bold headings. Aalto: "In academic writing such highlighting tools as italics, underlining and bolding are rarely used" and "the layout and design are good when nothing disturbs the reader." Conclusion carried into the formatting system: no background highlighting anywhere; emphasis by italics on first use and by heading hierarchy; colour reserved for figures, where it must survive greyscale.

**Redundancy, measured rather than assumed.** A scan for section-announcing openers and for sentences repeated near-verbatim across chapters returns **1 opener and 6 repeated sentences**, of which two pairs are legitimate structure (Chapter 1 introducing what Chapter 2 develops; Chapter 4's mechanism restated in Chapter 7's conclusion). Four are genuine candidates: a paragraph shared between Chapter 1 and Chapter 2 §79, and two passages Chapter 6 restates verbatim from Chapter 2 rather than building on. This is a much smaller problem than a reading impression suggests; the density of the prose, not its repetition, is what makes it heavy going.

## Table rules, the H-01 finding, and viva notes, 29 September 2026

| ID | Change | Reason | Verification |
|---|---|---|---|
| T-10 | Every table given booktabs rules: 1.5 pt top, 1 pt under the header, 1.5 pt bottom, no vertical or inside-horizontal rules, bold repeating header, full text-block width, real cell padding | Rendering the Word file to PDF and **looking at it** showed the defect: Table 2.1 had no rules at all and read as floating columns; Table 5.1 had a header rule but no bottom rule and trailed off into the body text; no table spanned the text block. The markdown was valid, so no text-level check could have found this | Re-rendered and inspected visually. 25 tables ruled |
| H-01 (applied at last) | Chapter 1 §1.1: the unsourced superlative "the most significant data-governance transformation in its history" replaced by the sourced Norwegian opening, the near-empty Bodø and Stjørdal gateway, attributed to Helsedirektoratet (2026) | **The trail recorded H-01 as applied on 21 September. It was not.** The superlative was still the opening sentence of the chapter file, the assembled submission and the draft. Found by reading the chapter openings during a hooks audit, not by any automated check | Inspector: gains only. Gained `(Helsedirektoratet, 2026)` and two dates; nothing lost. Sentences over forty words unchanged at 21 |
| V-01 | `Viva_Preparation_Notes.md` created: five hard questions with the concession first, the surviving claim second, the evidence location, and what not to say | On the open-work list since 21 September and never written | Each answer traced to a section that already states the limit; no new claim introduced |

**Finding that matters more than the fixes.** H-01 is the fifth trail entry found marked
applied but absent from the canonical files, after D-05, A-04, A3-l and P8-03 on 28
September. The pattern is now established rather than incidental: entries written in a
session that ended before its work was delivered are recorded as done. Failure mode 2 in the
handoff already says to diff rather than trust the trail; it now needs to say that the trail
is unreliable specifically for the 21 September and 08:34 28 September sessions.

**Equations do not survive a LibreOffice PDF export.** The Word file contains 191 native
OMML equations, confirmed in the XML. LibreOffice renders none of them: extracted text from
its PDF reads "C1: Retention floor. For every record and every month with :" where the
markup carries the full expression. The document is correct and Word displays it correctly.
The consequence is practical and belongs in the submission checklist: **export the PDF from
Word, never from LibreOffice, Google Docs or any converter that does not support OMML.**
It also means the visual verification method used for the tables is blind to mathematics,
which is stated here so that a future session does not mistake a clean render for a clean
document.

## Supervisor peer review received and handoff rebuilt, 30 September 2026

Prof. Ferreira returned a detailed peer review. **Nothing in it has been actioned.** The
session was approaching its limit, so the priority was preserving the review and rebuilding
the handoff around it rather than starting fixes that would be lost.

| ID | Change | Reason |
|---|---|---|
| S-01 | `SUPERVISOR_REVIEW_2026-09-30_Ferreira.md` created | The review captured in full, each major item verified against the files, with a sequencing note that contradicts his own numbering because the dependency runs the other way |
| S-02 | `DECISION_RECORD.md` created | Settled decisions with the alternatives rejected, so a fresh session does not re-litigate them; ten open decisions, O-01 blocking |
| S-03 | `FAILURE_LEDGER.md` created | Every failure mode with the rule from it, including the two the review exposed that no check of ours could see |
| S-04 | `NUANCES.md` created | Working method, standing rules, reversed decisions, things that look like errors and are not |
| S-05 | `CONVERSATION_LINEAGE.md` created | Seven sessions mapped, with this one's identifier recorded so a future session can be pointed at it |
| S-06 | `RESUME_PROMPT.md` created | Paste-ready, with the four verification commands and the M2-first sequencing |
| S-07 | `HANDOFF_READ_FIRST.md` rebuilt | New §0a (the live work) and §0b (document set); §9 replaced with the review-driven sequence |

**Verified against the files while capturing the review, not taken on trust:**

- **M3 confirmed, and the contradiction is ours.** Ch4 §4.8 line 182: "The salt is stored
  with the metadata and is *not* destroyed at invalidation". `trf_checker.py` line 119:
  `rec.salt = None   # salt destroyed with the key (Ch4 §4.8)`. The comment cites the
  section it contradicts. Introduced on 28 September when the working set was synced to the
  repository on the finding that the repository was "ahead", without checking the prose
  agreed. Logged then as safe because output stayed byte-identical — which proved the code
  self-consistent, not correct.
- **The `if False` dead branch confirmed** at line 63.
- **M2 confirmed by reading**: §4.8 calls m(a) personal data; C3 is formalised over payload
  accessibility α alone. The broad reading generates Corollary 1.2; the narrow reading
  resolves it.

**The structural lesson, recorded because it outlives this review.** Every check built in
this project verifies internal consistency: code against stated model, file against
register, rebuild against previous output. None can verify a *premise*. M1 questions whether
an audit record contains a clinical payload at all, and M2 questions whether the model's two
halves are consistent under one legal reading. Both needed a domain reader. Budget for that
earlier next time rather than discovering it at review.

| S-08 | `PATCHES.md` created | The working list for Joao Round 3: seven waves, three gating decisions, per-patch cascade lines naming what else moves, and a cross-cutting cascade map. Nothing applied |
| S-09 | `SUPERVISOR_FEEDBACK_HISTORY.md` created | Every supervisory round from Round 0 to Round 3, what each asked, what was delivered, and what went wrong. Records that the SPUHiN reference has now been raised twice, and that H-01 was recorded applied in Round 1 and found unapplied nine days later |
