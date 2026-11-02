# Master Manifest

**Every file, where it lives, what state it is in, and what is going on with it.**
Generated 28 September 2026 by reading the files, not from recollection. Updated the same day after the citation link pass.

Read `HANDOFF_READ_FIRST.md` first in a new conversation. Read this when you need
to know what a particular file is, or whether a copy somewhere is the current one.

---

## 0. Update, 2 October 2026 — read before section 1

**The source of truth for the thesis text is now the draft the supervisor reviewed**, held as
the chapter files on git branch `joao-base` (tag `joao-base-v1`). Section 1's "working set is
the source of truth" referred to the 30 Sept files, which were not that draft.

| Place | What it is |
|---|---|
| Chapter `.md` files, branch `joao-base` | The thesis text, equal to the reviewed draft in every prose paragraph |
| `supervisor_review/` | The returned .docx (template, 47 tracked changes, 27 comments); its text with changes rejected (= the base) and accepted; the email review; the raw review |
| `patches/` | `D0_rebase_to_draft.py` and `APPLIED.log` (every applied edit with before/after md5) |
| `handoff_tools/patch.py` | All-or-nothing exact-match patcher |
| `handoff_tools/verify_base.py` | Compares every prose line of the chapters with the reviewed draft; 0 differences on the base, and after patching every difference must match a logged patch |
| `VERA-SNARK_Thesis_SUBMISSION.docx` | Rebuilt 2 Oct from the base (176 equations, 25 tables). The 29 Sept build carried pre-rebase text |
| Branch `zip-base-superseded` | F1–R1 replays, AS-01 sort fix, two figures, merge review; candidates in `PATCHES.md` Wave −1 |
| `conversation_history/2026-05-22_to_09-30_main_chat_Norwegian_health_records.txt` | Full export of the MAIN chat |

Code, data, the reproduction package and the public repository are unchanged by the rebase.
The checker output is byte-identical to the recorded run.

## 1. Where things live

The work exists in four places. They are not copies of one another and each has a job.

| Place | What it is | Who sees it |
|---|---|---|
| `/mnt/user-data/outputs/` | The working set. Every chapter, appendix, tool and package. The source of truth for the thesis text. | You and me |
| `github.com/Astheno-sphere/TRF` | The published artefact: runnable code, the data subset, the recorded runs, Appendix A. What a reader clones. | Anyone you give the link to |
| `trfhimolde.streamlit.app` | The live demonstration, deployed from that repository. | Anyone with the link |
| Google Drive substrate sheet | The research substrate, 17+ subsheets, plus the patch workbooks. | You |

**Rule that has already caught one failure:** a change is not applied until it is
applied in every place it belongs. On 28 September the repository turned out to be
*ahead* of the working set, with four change-trail entries marked applied that
existed only in the pushed copy. Reconciliation now diffs against the repository,
not only within the working set.

---

## 2. What changed today, in order

| # | Change | Effect on the thesis |
|---|---|---|
| 1 | Eight Synthea bundles committed to `data/synthea_subset/` on GitHub | Tab 3 works. Chapter 5's 891 bytes is now verifiable by anyone who clones. |
| 2 | `requirements.txt`, `docs/expected_trf_output.txt`, `norwegian_docs/HOW_TO_RUN.md` restored | The 23 September web upload had flattened directories and silently dropped these. |
| 3 | Working set resynced to the repository | The checker gains the section 4.8 salt destruction, 362 to 363 lines. |
| 4 | Appendix A corrected in all four copies **and in the assembled submission** | Removed a false claim about a CSPRNG comment that does not exist in the code, fixed the line count and the data description. |
| 5 | Reproducibility package flattened and repaired | It could not previously run its own realism layer, and `run_all.sh` skipped that step entirely. |
| 6 | App Tab 5 added: exhaustive cross-check and delta witness | Two results the thesis reports had no viewer anywhere. |
| 7 | A recorded run committed per command, five in total | A reader can now tell a changed file from a changed result for every command, not just the checker. |
| 8 | 88 MB of duplicate data removed | The eight bundles existed in three working-set copies plus GitHub. Now one working copy plus GitHub. |
| 9 | Citation link pass: 41 of 68 linked → 66 of 66 | Every entry now carries a DOI or URL that was fetched, not constructed. |
| 10 | Two entries removed as non-existent documents | European Commission "Implementation calendar" is a section of another page; Helsedirektoratet "MyHealth@EU, Norsk helsenett" 404s and has no live equivalent. |
| 11 | Six citations corrected on year, title or author | IHE 2024→2023, Helsedirektoratet 2023→2024, Deloitte n.d.→2020, plus title corrections against the sources' own wording. |

---

## 3. Verification run today

Every line below was produced by executing something, not by reading it.

| Check | Method | Result |
|---|---|---|
| Checker reproduces the thesis figures | Fresh clone of the public repository, then `python3 trf_checker.py` | Byte-identical to `docs/expected_trf_output.txt` |
| Payload independence | `python3 synthea_layer.py` against the committed subset | 8 bundles, 891 bytes, six measures identical, 200/200 commitments differing |
| Delta witness | `python3 trf_checker.py --delta-witness` | 90 records and 95 violations at delta 1, 89 and 94 at delta 3, matching Table 5.2a |
| Exhaustive cross-check | `brute_force_semantics_I()` over the four cases | All four agree with the recorded run; the control returns feasible |
| Reproduction package | `bash run_all.sh` | Exit 0. All five reruns identical to their recorded runs |
| App | Streamlit headless, five tabs | HTTP 200, zero errors in the log |
| Assembly | `handoff_tools/assemble.py` rebuild | Byte-identical to the existing submission, so the assembly is reproducible from the chapter files |
| Assembly integrity | `handoff_tools/inspector.py` old against rebuilt | **ADMIT.** Citations, numerals, article references, hedges and the reference list all identical |
| Version register | Every registered md5 recomputed | 30 files, 0 mismatches |

---

## 4. Pending work, verified 28 September 2026

Each row was checked against the files, not copied from an earlier list. Items that
earlier lists still showed as open but are in fact closed are marked so and should
not be repeated.

### Closed, do not redo

| Item | Evidence |
|---|---|
| Four DOIs (Finck 2019, Staffa 2018, Scope et al. 2022, Scope and Rasin patent) | All four now carry a locator in the bibliography. Closed by the citation pass |
| 27 unlinked bibliography entries | 67 entries, 67 linked, 0 unlinked |
| Synthea subset on GitHub | Verified from a fresh clone |
| Em-dash reduction | 230 to 110; prose 117 to 12, headings 15 to 0 |
| Dash-then-colon corruption in canonical files | Corpus sweep returns 0 in the submission and every canonical chapter |
| Word conversion toolchain | `VERA-SNARK_Thesis_SUBMISSION.docx` builds clean: 191 native Word equations, 24 tables, zero LaTeX leakage |

### I can do these without you

| # | Item | Why it is still open | Effort |
|---|---|---|---|
| 1 | Read and integrate aiAuthZ (arXiv 2607.05518) and the 2026 privacy-engineering SLR (arXiv 2606.23696) | Both discovered and never read. They belong in Ch2 §2.4 as converging practice | One run |
| 2 | Two figures: regulatory timeline for §6.8, record-state diagram for §4.8 reprised at §5.6 | The thesis has **no figures at all** and no `Figure N.N` callouts. For a model with a terminal state transition, a state diagram is close to expected | One run |
| 3 | A proper citation parser, then the orphan audit | The regex mis-parses `(Hevner, March, Park, & Ram, 2004)`. Until it is replaced, "every citation resolves" is unproven rather than false | One run |
| 4 | Fix the `assemble.py` dedup rule | It keeps the longer variant, so a long unlinked line beats a short linked one. That is why link coverage was under-reported | Small |
| 5 | Viva preparation notes, five hard questions | Where is the logistics; do access logs count as data within the environment; are 1 to 12 month permits realistic; Semantics II has no authority; why informal proofs | One run |

### Blocked on you

| # | Item | What is needed |
|---|---|---|
| 6 | HiMolde template | The site blocks automated fetch. Download it, then the .docx is restyled to it. The conversion itself already works |
| 7 | Confirm the live demonstration | Streamlit is unreachable from this container. Open Tab 3 and Tab 5 and confirm 891 bytes and the two robustness checks |
| 8 | Zenodo DOI | Mint it from the GitHub repository once it stops moving |
| 9 | Sikt notification and interviewee outreach | You reversed the earlier decision and want the expert evaluation run |
| 10 | Datatilsynet informal sounding | Whether accountability-preserving verifiability discharges a retention obligation. Would strengthen §6.2 and §7.4 |
| 11 | SPUHiN D5.2 stable locator | The consultation page was withdrawn and 404s. Ask Helsedirektoratet, or leave the project-page citation the entry now carries |

### Your decisions, not mine to take

| # | Decision | The two options |
|---|---|---|
| 12 | VeritasChain | Keep it with the accurate caveat it now carries, or drop it and let me rewrite Ch2 §2.5, the §2.8 table and the §2.9 gap statement without it |
| 13 | Length | 57,969 words, roughly 165 pages against an 80-page guideline. You said overrun is acceptable for good work. Confirm, or say what to cut |
| 14 | The research question | 102 words, supervisor-approved, and the last place in the prose carrying em-dashes. I left it untouched as you instructed |
| 15 | Expert evaluation status in the text | Ch3 and Ch7 state it was not executed. If you run it, those passages and Appendix C change |
| 16 | NORS 2025 | Whether a notice is owed to that audience about the abandoned draft. Yours and Joao's call |

### Deliberately left alone

| Item | Why |
|---|---|
| ~50 dash-then-colon corruptions in `_draft_Thesis_FULL_with_chapter_refs.md` and 1 in `_superseded_Chapter2_RETROFIT.md` | Non-canonical. Repairing them would destroy the record of what was corrected |
| `norwegian_docs/HOW_TO_RUN.md` differs from the lost original | The 116-line original was never uploaded and no copy survives. Recorded as R-07 |
| 12 prose em-dashes | 7 inside source titles that may not be altered, 1 verbatim console output, 2 in the locked research question, 2 in an appositive whose aside ends in a parenthetical |

## 5. What is on GitHub

22 tracked files plus the 8 data bundles, across five commits. `CHECKSUMS.md`
in the repository carries the md5 of each.

| Path | Purpose |
|---|---|
| `trf_checker.py` | The load-bearing artefact: Theorems 1 and 2, plus the independent exhaustive cross-check |
| `synthea_layer.py` | Payload-provenance comparison |
| `norwegian_layer.py` | Three Norwegian record classes, illustrative |
| `cross_sector_check.py` | politiregisterloven section 17 instance. **On GitHub since 23 September and wired into Tab 4 since then** |
| `app.py` | Five-tab Streamlit viewer |
| `requirements.txt` | `streamlit>=1.30` |
| `data/synthea_subset/` | 8 untrimmed bundles plus a provenance README |
| `docs/Appendix_A.md` | Appendix A |
| `docs/Data_Provenance_Statement.md` | Where the data came from and how to check it |
| `docs/expected_*.txt` | Five recorded runs, one per command |
| `norwegian_docs/` | Module documentation and the run guide |
| `CHANGE_TRAIL.md`, `CHECKSUMS.md`, `README.md` | The record |

---

## 6. Every file in the working set

| # | File | Group | State | md5 | Size | What is going on with it |
|---|---|---|---|---|---|---|
| 1 | `Appendix_B_Search_Log.md` | APPENDIX | Current | `369606115f4b` | 7 KB | 59 queries across four dated rounds with [R] annotations. Your evidence that the review was systematic. |
| 2 | `Appendix_C_Evaluation_Instrument.md` | APPENDIX | Current | `bc84393969c4` | 15 KB | The expert evaluation instrument. Designed and not yet executed. You have since decided to run it, which means a Sikt notification and interviewee outreach. |
| 3 | `CHANGE_TRAIL.md` | CONTROL | Current | `0fd1a33b8771` | 41 KB | Every change with an ID, a reason and a verification. R-01 to R-15 are today's. Synced with the copy in the repository. |
| 4 | `CHECKSUMS.md` | CONTROL | Current | `9261b088033a` | 1 KB | Checksums of what is actually pushed to GitHub. Regenerated from the files rather than edited by hand. |
| 5 | `Chapter1_Introduction_v2.md` | THESIS | Current | `4b448490575a` | 35 KB | Problem, audit-retention floors, the generalised research question of 102 words that your supervisor approved and you have asked not to shorten. |
| 6 | `Chapter2_LitReview_v2_FINAL.md` | THESIS | Current | `e8fe35908049` | 93 KB | Review protocol in 2.1, then the gap. The largest chapter at roughly 14,000 words; you accepted the overrun as the price of doing the review properly. |
| 7 | `Chapter3_Methodology_v1.md` | THESIS | Current | `de86b8f4a39a` | 35 KB | Design Science with the specification-and-demonstration variant, and the canonical limitations register at 3.7 with eight items. |
| 8 | `Chapter4_TRF_Model_v1.md` | THESIS | Current | `f4c954b9c447` | 50 KB | The model, Theorems 1 and 2, Corollaries 1.1 and 1.2, the mechanism, the terminal transition at 4.8. All mathematics in LaTeX, 159 equations. |
| 9 | `Chapter5_Demonstration_v1.md` | THESIS | Current | `e04f2d71c2be` | 24 KB | Execution results. Table 5.2a carries the delta witness, Table 5.4 the payload invariance, 5.7 the limits. Reports 891 bytes for the subset and 1,006 for the full cohort, both now verifiable from the public repository. |
| 10 | `Chapter6_Discussion_v1.md` | THESIS | Current | `992a0b550d12` | 33 KB | Eleven sections. Regulatory implications, what Semantics II does and does not discharge, the implementing-act timing at 6.8. |
| 11 | `Chapter7_Conclusion_v1.md` | THESIS | Current | `2bcba5e9ba5d` | 14 KB | Contribution, limits, further work. |
| 12 | `Consolidated_Bibliography.Rmd` | THESIS | KNIT THIS ONE | `c5c564250569` | 15 KB | Same content in R Markdown. It looks empty in a plain viewer because the viewer cannot render .Rmd; that is why the .md twin exists. |
| 13 | `Consolidated_Bibliography.md` | THESIS | READ THIS ONE | `13365f8f7d7a` | 15 KB | 68 entries, chapter-tagged, regenerated from the chapter reference lists today and byte-identical to before. 41 carry a DOI or URL; 27 carry neither, which is the largest remaining citation-quality gap. |
| 14 | `Data_Provenance_Statement.md` | SUPPORT | Current | `36aeddac1f9c` | 6 KB | The answer to your supervisor's data question. Updated today: the repository now ships the subset, so the section that said it contained no dataset was rewritten rather than left standing. |
| 15 | `Front_Matter_v1.md` | THESIS | Current | `8cc073dcdb92` | 14 KB | Title, abstract, contribution statement, declarations including AI assistance, nomenclature, table of contents. |
| 16 | `HANDOFF_READ_FIRST.md` | CONTROL | Read first in a new chat | `e307e6213b59` | 17 KB | Locked decisions, corrections never to reintroduce, my failure modes, working method, open work. Failure mode 2 is new today: trusting the change trail instead of diffing against the repository. |
| 17 | `Substrate_ARTEFACT_PATCH_28Sept.xlsx` | SUPPORT | In your Drive | `1bca2c5e07cf` | 12 KB | Six tabs of artefact-integrity findings for the substrate sheet. Uploaded to the same Drive folder as the master sheet. |
| 18 | `Substrate_FINAL_PATCH.xlsx` | SUPPORT | Superseded for artefact rows | `b78d09fbc53c` | 13 KB | The 16 September patch. Still the right source for its own round; today's patch adds to it rather than replacing it. |
| 19 | `Supervisor_Feedback_Action_Plan.Rmd` | SUPPORT | Current | `e318cfab1ca8` | 13 KB | Response plan to the first feedback round. |
| 20 | `VERA-SNARK_Thesis_SUBMISSION.md` | THESIS | SUBMIT THIS | `c2529689892b` | 346 KB | Front matter, Chapters 1-7, one APA bibliography, Appendices A-C. Rebuilt today by handoff_tools/assemble.py and came back byte-identical to the hand-patched copy, which proves the assembly is reproducible from the chapter files and that nothing was lost in the Appendix A surgery. |
| 21 | `VERSION_REGISTER.md` | CONTROL | Reconciled today | `5998ca2ee9eb` | 12 KB | Every canonical file with its md5. Thirty files, zero mismatches at last check. The md5 column is the one to trust; the Words column was about four per cent high before today and is now len(text.split()). |
| 22 | `_draft_Thesis_FULL_with_chapter_refs.md` | SUPERSEDED | DO NOT USE | `de3ea61dbb97` | 313 KB | Kept only for provenance. Still contains the false CSPRNG sentence and the old Appendix A; that is deliberate, since correcting a superseded draft would destroy the record of what was corrected. |
| 23 | `_superseded_Chapter2_RETROFIT.md` | SUPERSEDED | DO NOT USE | `8bbd1fbdf485` | 35 KB | Kept only for provenance. |
| 24 | `artifact/action_plan.html` | SUPPORT | Current | `3603600b8214` | 16 KB | The published action-plan page. The invalid 12 March 2025 date was withdrawn from it. |
| 25 | `code_artefacts/DATA_LOCATION.md` | PACKAGE | New today | `cc6163282194` | 1 KB | Explains that the bundles are not duplicated here and where they are instead. |
| 26 | `code_artefacts/README_Appendix_A.md` | APPENDIX | Canonical Appendix A | `2f4323a8545f` | 38 KB | Provenance, exact commands, full source listings, console output. Corrected today: line count 362 to 363, the salt-destruction line added to the listing, the three trimmed sample bundles replaced by the eight untrimmed ones, and the false CSPRNG sentence removed. Identical in all four places it lives. |
| 27 | `code_artefacts/build_substrate_master_patch.py` |  | Current | `ddf112330e28` | 11 KB |  |
| 28 | `code_artefacts/build_substrate_patch1.py` |  | Current | `38204a16bd1b` | 18 KB |  |
| 29 | `code_artefacts/build_substrate_patch2.py` |  | Current | `126b72ff3a56` | 8 KB |  |
| 30 | `code_artefacts/build_substrate_patch3.py` |  | Current | `299d9d136a7d` | 7 KB |  |
| 31 | `code_artefacts/norwegian/cross_sector_check.py` |  | Current | `86deaf873464` | 6 KB | The two Norwegian modules, mirrored from the canonical copies. |
| 32 | `code_artefacts/norwegian/norwegian_layer.py` |  | Current | `3e2ff91225ac` | 7 KB | The two Norwegian modules, mirrored from the canonical copies. |
| 33 | `code_artefacts/synthea_layer.py` |  | Current | `2b4a53730227` | 6 KB |  |
| 34 | `code_artefacts/trf_checker.py` |  | Current | `d0496883a669` | 15 KB |  |
| 35 | `conversation_history/2026-05-25-23-16-30-vera-snark-thesis-build.txt` |  | Current | `5a2db509a5d4` | 798 KB | Four raw transcripts plus the session log and journal. Provenance for how the thesis was built. |
| 36 | `conversation_history/2026-05-29-18-12-42-vera-snark-thesis-build.txt` |  | Current | `e4b1007bfe61` | 730 KB | Four raw transcripts plus the session log and journal. Provenance for how the thesis was built. |
| 37 | `conversation_history/2026-09-15-02-29-25-vera-snark-thesis-resume-retrofit.txt` |  | Current | `35df15e4aea8` | 750 KB | Four raw transcripts plus the session log and journal. Provenance for how the thesis was built. |
| 38 | `conversation_history/2026-09-15-02-42-38-trf-thesis-sheet-patch-ch3-unblock.txt` |  | Current | `38123f4a7fc9` | 1.2 MB | Four raw transcripts plus the session log and journal. Provenance for how the thesis was built. |
| 39 | `conversation_history/SESSION_LOG_15-21_Sept_2026.md` | HISTORY | Current | `db9552b1cc61` | 4 KB | Chronological log of the 15-21 September session, which is in no transcript. |
| 40 | `conversation_history/journal.txt` |  | Current | `26fb1f47a063` | 3 KB | Four raw transcripts plus the session log and journal. Provenance for how the thesis was built. |
| 41 | `demo_app/README.md` | CODE | Local note | `044b8f200f1f` | 5 KB | The demo folder's own note. |
| 42 | `demo_app/README_repo.md` | CODE | Mirror of the repo README | `b15679678845` | 6 KB | Copied from GitHub so the working set carries what a reader sees first. |
| 43 | `demo_app/app.py` | CODE | Current, 5 tabs | `b07777129395` | 24 KB | The Streamlit viewer. Tab 5 is new today and runs the exhaustive cross-check and the delta witness, neither of which had a viewer anywhere before. |
| 44 | `demo_app/cross_sector_check.py` | CODE | Current | `86deaf873464` | 6 KB | The politiregisterloven section 17 instance. Already on GitHub since 23 September and already wired into Tab 4; it did not need pushing. |
| 45 | `demo_app/norwegian_layer.py` | CODE | Current | `3e2ff91225ac` | 7 KB | NO-XB, NO-SPE and NO-JOURNAL classes. Illustrative, not empirical, and states so. |
| 46 | `demo_app/requirements.txt` | CODE | Current | `944269ad914f` | 0 KB | streamlit>=1.30. Its absence from GitHub was why Streamlit Cloud had no pinned dependency. |
| 47 | `demo_app/synthea_layer.py` | CODE | CANONICAL | `2b4a53730227` | 6 KB | 152 lines. Reads the full cohort if present, otherwise the committed subset. |
| 48 | `demo_app/trf_checker.py` | CODE | CANONICAL | `d0496883a669` | 15 KB | 363 lines. The load-bearing artefact. Identical in four places and on GitHub. |
| 49 | `handoff_tools/README.md` | TOOL | Current | `e6bf67cb913d` | 1 KB | How to run the three tools. |
| 50 | `handoff_tools/assemble.py` | TOOL | Current | `2c05f3f9b4ad` | 3 KB | Rebuilds the bibliography and the submission from the chapter files. Today's rebuild was byte-identical to the existing file. |
| 51 | `handoff_tools/inspector.py` | TOOL | Current | `463739871d29` | 4 KB | Gates every rewrite on citations, numerals, article references, hedges and the reference list. Ran ADMIT on today's rebuild. |
| 52 | `handoff_tools/mathconv.py` | TOOL | Current | `a731f3cb5ca1` | 2 KB | Italic-unicode mathematics to LaTeX. |
| 53 | `repro_package/README.md` | PACKAGE | Current | `acfc7f872bf5` | 6 KB | The package's own guide, updated for the flattened layout. |
| 54 | `repro_package/cross_sector_check.py` |  | Current | `86deaf873464` | 6 KB |  |
| 55 | `repro_package/data/synthea_subset/README.md` |  | Current | `c2c9564cf734` | 3 KB | The eight untrimmed Synthea bundles, 40 MB. The single working-set copy; the other copy is on GitHub. Chapter 5's 891-byte figure was measured on exactly these files. |
| 56 | `repro_package/docs/Appendix_A.md` | PACKAGE | Mirror | `2f4323a8545f` | 38 KB | Identical to the canonical Appendix A. |
| 57 | `repro_package/norwegian_layer.py` |  | Current | `3e2ff91225ac` | 7 KB |  |
| 58 | `repro_package/requirements.txt` |  | Current | `7ebd6817e2cc` | 0 KB |  |
| 59 | `repro_package/results/expected_cross_sector_output.txt` |  | Current | `b61cd4e6b6e6` | 1 KB | One recorded run per command, so a reader can tell a changed file from a changed result. Both cohort sizes recorded separately, because the subset cannot produce the full cohort's mean. |
| 60 | `repro_package/results/expected_delta_witness_output.txt` |  | Current | `78dd53188713` | 3 KB | One recorded run per command, so a reader can tell a changed file from a changed result. Both cohort sizes recorded separately, because the subset cannot produce the full cohort's mean. |
| 61 | `repro_package/results/expected_norwegian_output.txt` |  | Current | `5c45219369b7` | 2 KB | One recorded run per command, so a reader can tell a changed file from a changed result. Both cohort sizes recorded separately, because the subset cannot produce the full cohort's mean. |
| 62 | `repro_package/results/synthea_comparison_full_cohort_output.txt` |  | Current | `94bbf0435582` | 1 KB | One recorded run per command, so a reader can tell a changed file from a changed result. Both cohort sizes recorded separately, because the subset cannot produce the full cohort's mean. |
| 63 | `repro_package/results/synthea_comparison_subset_output.txt` |  | Current | `64e8c21c4f4d` | 1 KB | One recorded run per command, so a reader can tell a changed file from a changed result. Both cohort sizes recorded separately, because the subset cannot produce the full cohort's mean. |
| 64 | `repro_package/results/trf_output.txt` |  | Current | `41b56742d35d` | 3 KB | One recorded run per command, so a reader can tell a changed file from a changed result. Both cohort sizes recorded separately, because the subset cannot produce the full cohort's mean. |
| 65 | `repro_package/run_all.sh` | PACKAGE | Current | `e53b50904052` | 3 KB | Four steps, all five diffs. Exits clean and every rerun matches its recorded run. |
| 66 | `repro_package/src/build_substrate_master_patch.py` |  | Current | `ddf112330e28` | 11 KB | Bookkeeping scripts for the research substrate. No thesis result depends on them. |
| 67 | `repro_package/src/patch_final.py` |  | Current | `db9391416a9f` | 8 KB | Bookkeeping scripts for the research substrate. No thesis result depends on them. |
| 68 | `repro_package/synthea_layer.py` |  | Current | `2b4a53730227` | 6 KB |  |
| 69 | `repro_package/trf_checker.py` |  | Current | `d0496883a669` | 15 KB |  |
| 70 | `thesis_yaml_header.yml` | SUPPORT | Current | `574e4ae50cfd` | 0 KB | Pandoc YAML: breezedark code highlighting and the Word template hook, for the conversion. |
| 71 | `repro_package/data/synthea_subset/*.json` (8 files) | DATA | Current | see `data/synthea_subset/README.md` | 39.3 MB | The eight untrimmed Synthea bundles, 40 MB. The single working-set copy; the other copy is on GitHub. Chapter 5's 891-byte figure was measured on exactly these files. |
---

## 7. Copies that must stay identical

Drift between copies is the failure this project keeps having, so each set is listed
with the checksum they must all carry.

| File | md5 all copies must carry | Where it lives |
|---|---|---|
| `trf_checker.py` | `d0496883a669` | `demo_app/`, `repro_package/`, `code_artefacts/`, GitHub |
| `synthea_layer.py` | `2b4a53730227` | same four |
| `norwegian_layer.py` | `3e2ff91225ac` | `demo_app/`, `repro_package/`, `code_artefacts/norwegian/`, GitHub |
| `cross_sector_check.py` | `86deaf873464` | same four |
| `app.py` | `b07777129395` | `demo_app/`, GitHub |
| Appendix A | `2f4323a8545f` | `code_artefacts/README_Appendix_A.md`, `repro_package/docs/Appendix_A.md`, GitHub `docs/Appendix_A.md`, and inside the submission |

To check them all at once:

```bash
cd /mnt/user-data/outputs
find . -name "trf_checker.py" -o -name "synthea_layer.py" \
       -o -name "norwegian_layer.py" -o -name "cross_sector_check.py" | xargs md5sum
```

Four distinct checksums and nothing else means no drift.
