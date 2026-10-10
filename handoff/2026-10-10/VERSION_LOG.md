# Version log — 10 October 2026

Every commit in both repositories, with the documents delivered to Tiger and their hashes. Regenerate the commit lists with `git log --reverse --format='%h %ad %s' --date=short`.

## Delivered documents (latest first)

| Date | File | sha256 | Basis |
|---|---|---|---|
| 2026-10-06 | `VERA-SNARK_Thesis_SUBMISSION.docx` | `2ded452d2114cc5b594b67a89eb16edc4d79e60e6264bf3695c80f88ce3fd62f` | built from HEAD at that date |
| 2026-10-06 | `VERA-SNARK_Thesis_TRACKED_vs_5Oct.docx` | `ccbb7afa402fe7c7352ada8f28db0014773339718e609472cc6acff72c1bb5b4` | built from HEAD at that date |
| 2026-10-05 | `VERA-SNARK_Thesis_TRACKED_vs_4Oct.docx` | `d821c03e03d9e7dd08c5b428407144dee02959445a543c9e7478fb9064c2b451` | built from HEAD at that date |
| 2026-10-06 | `figures/fig4_1_cei_mechanism.png` | `7f574ac9d59902065bca41cb1f7ea8d07981c9b64094ca6b914a5797e7daba13` | built from HEAD at that date |
| 2026-10-06 | `figures/fig5_1_trf_artefact.png` | `94e366ad4de08ad3bdd7670c99c136895d8d6eb73dc5332d5679c767c16c0d6b` | built from HEAD at that date |

## Supervisor files received

| Round | File | sha256 |
|---|---|---|
| | `supervisor_review/Master_thesis_Abbasia_tracked_JF.docx` | `d2ff214add8a32f586ef1bb91d1fde648a689c19bf06d0dae95907a770367086` |
| | `supervisor_review/review3_JF_2026-10-04.docx` | `118fc0bfdaa462709f8e1738917601b2b34c9d875fecf3a66f970343d40feb92` |
| | `supervisor_review/review4_JF_2026-10-06.docx` | `e7239d403d082718338d5d0651d3928f94029d0f3cfba502d5d660000c90c792` |
| | `supervisor_review/review3_gdoc_2026-10-04.json` | `999a5a43bdf9dd1e79f05f82450a9b8c12909d913d94b6aaf7581faebd7b675b` |

## Tags

- checkpoint-2026-10-04 P28: NCPeH pilot details said once (§2.2), cross-referred elsewhere (PRES-4)
- checkpoint-2026-10-04b B-37: public repo R-24/R-25 pushed; CHECKSUMS copied back
- joao-base-v1    D0: rebase onto the draft Joao reviewed (29 content edits ported from Master_thesis_Abbasia_tracked_JF.docx, tracked changes rejected)

## Thesis repo commits (branch joao-base)

```
184c91d 2026-09-30 Baseline: 30 Sept migration package (29 Sept canonical line)
0438daf 2026-10-02 D0: rebase onto the draft Joao reviewed (29 content edits ported from Master_thesis_Abbasia_tracked_JF.docx, tracked changes rejected)
3ef05f1 2026-10-02 B: control documents, register and Word build brought onto the Joao base
fea8504 2026-10-02 Untrack compiled Python caches (tracked since the baseline; .gitignore already excludes them)
913527f 2026-10-02 B2: trail inspector, guards, review tracker; patcher gated by inspector
80648b2 2026-10-03 DEC: D-16 partition reading + Proposition L, D-17 ciphertext deleted, D-18 propositions
705b2db 2026-10-03 P01: minor issues from the 30 Sept review (MIN-01..04, 08, 09, 11, 12)
cfa1b71 2026-10-03 P02: salt destroyed with the key, ciphertext deleted at invalidation (M3a; M3b text)
742683d 2026-10-03 P03: EHDS dates from Arts 19(1) and 105; EY source dropped (M5d)
ec6742e 2026-10-03 B3: trail parser accepts multi-ID cells; gated commit.sh (P03 had been committed with check 3 failing)
5bb829c 2026-10-03 P04: Chapter 4 core — p(a) grounded in ITI-55, m_acc/m_subj partition, Corollary 1.2 conditional, Art 68(12) verbatim (M1, M2a, M5c partial) P05: proof gap in P04 closed (trajectory step 4)
f6a53a6 2026-10-03 B4: check 4 reads full commit messages
785d408 2026-10-03 P06: Rival 6 and Proposition L; D7.4 EHDSR-7 and OPR-6; Rival 3 aligned with §4.2 (M2b)
0e62818 2026-10-03 P07: D-16 reading carried through Ch1, Ch2, Ch6, Ch7; §6.1 leads with the robust result; unverified usage claim removed (M2a, M2c, M5c) P08: Appendix C item 7 verbatim (M5c)
9bb80af 2026-10-03 P09: ten-year floor presented as illustrative with its sources (M5a); Feng et al. to CAV 2023 (M5e part); assemble.py accepts eHealth Network
02f7852 2026-10-03 P10: SPUHiN claims limited to the hearing version inspected (M5b)
e1143af 2026-10-03 P11: Union Customs Code anchor (Arts 51, 197) tested against §6.9a; §1.4 overreach removed; programme fit in §1.5 (M7a, M7b) P10b: (committed with P10) Table 2.1 and §2.9 'finalised Norwegian substrate'
e83e061 2026-10-03 P12: code wave — accessor/subject split, ciphertext deletion, make_salt, Merkle-log integrity with tamper test (M1, M3b, M3c, M4c) P13: Appendix A synced to the code (appendix_sync.py); prose follows P14: Chapter 5 and Table F.2 follow the code wave; MIN-07 B5: public repository pushed (Astheno-sphere/TRF a6062e3); CHECKSUMS copied from it; trail check 13
faa2a5e 2026-10-03 P15: Proposition 3 (anchoring) promoted into Ch4, §6.9a corrected (M4b) P16: theorems renamed propositions in the prose (M4a) P17: same rename in the code (M4a) P18: Appendix A synced and renamed B6: repository 0f3c39e; TIGER_TASKS.md; generated patches frozen (frozen.py); trail check 14 (full replay)
a554b51 2026-10-03 P19: Appendix C item A1 reworded (M6b) P20: Table 2.1 in three bands; SPUHiN row corrected (M5e) P21: frequency claims softened, closed window justified (MIN-05, MIN-06) P22: traceability matrix, Table 4.1 (M6a)
fa43b08 2026-10-03 B7: P20 frozen from git; commit gate requires TRAIL INTACT (inspector crash had passed the gate)
8364256 2026-10-03 P23: optional real AES-256-GCM envelope-encryption module wired in (run_all, Appendix A A.9e/A.15, Table 5.0a, §5.7, Table 4.1) P23b: run_all step label B8: repository 2b2dddb
83676e7 2026-10-03 P24: D7.4 read in full (T-1): pages, OPR-6 balance, OPR-17 proportionality, OPR-18 five years, Annex 7 open question; gap claim corrected and sharpened B9: sources/ (D7.4, UCC) added; T-1, T-2 done; research log corrected
243be20 2026-10-03 P25: §5.3 and §5.4 witness lines as verbatim code blocks (MIN-10)
e9b0ce7 2026-10-03 P26: defensive meta-commentary cut 84 → 31 (PRES-1); Rival count and §6.9a diagnostic aligned with Propositions 3–4
dd1e30e 2026-10-03 P27: process material stated once in the Declaration; Version and Change Record to the repository (PRES-3) B10: check 8 normalises replayed lines
083a217 2026-10-03 P28: NCPeH pilot details said once (§2.2), cross-referred elsewhere (PRES-4) P29: Art 68(12) grounds argued once (§4.6); §6.2, §7.4 point there (PRES-4) P30: front matter level with body: proposisjon, Props 3-4, partition, log, Cor 1.2 conditions P31: Ch5 tightened (M4d): meta cut, rate caveat once, §5.4 conditional, Prop 3 link; docx rebuilt
eeda10a 2026-10-03 P32: D7.4 printed page numbers throughout P33: Ch4 key hierarchy, tamper-evident log in body, leaf-hash residue, D7.4 architecture, Props 3-4 in 4.1/4.12 P34: Ch2 tamper-evident logging strand; Boneh & Lipton P35: Ch6 meta cut, links to Ch4/Ch5/Table 4.1, D7.4 OPR-6/Annex 7, Prop 3 drafting test P36: Ch7 level with Ch4-6; zk-SNARK future work concrete P37: Ch1/Ch3 links, roadmap, exhaustive search not solver B-35: APA bibliography order
edb4d77 2026-10-03 P38: MIN-13 renumbering (sections 5.6/6.10, Ch5 tables 5.1-5.7, Appendix A.1-A.22) P39: Streamlit app: integrity + tamper tests, envelope encryption, Proposition 3 tab P39b: deprecated width parameter; requirements P40: Appendix A app listing and tab prose P41: TOC regenerated B-36: appendix_sync keys
a8e02ac 2026-10-03 B-37: public repo R-24/R-25 pushed; CHECKSUMS copied back
9c3dd73 2026-10-03 B-38: independent audit; tracker statuses corrected
6d85a23 2026-10-03 B-39: formatted Word build; B-40: tracked-changes comparison against the reviewed draft
86ce041 2026-10-03 P42: consistency (M1, M2a, M4a, M5a, M5c) P43: cuts and pointers (PRES-1/3/4, M4d, M7a, M1c) P44: checker header, appendix, README; P44b: A.10 sync P45: meta, headings; P46: Synthea limitations once B-41: tracker
83fd319 2026-10-03 P44b: Appendix A.10 listing synced to the checker (applied in 86ce041) P46: Synthea limitations stated once, in §3.5 (applied in 86ce041)
aa86290 2026-10-03 B-42: public repo R-26; CHECKSUMS copied back
6a6225f 2026-10-04 P47: João's tracked changes of 4 Oct, verbatim P48: alignment (Sammendrag, counts, conditional extension, Rival 4) P49: patient link (Option A), payload by source + Corollary 2.3, Art 17(3)(d)/Art 71, OpenNCP, redactable literature P50: bounded SMT check carried in P50b: A.24 note P51: Ch2 trim, limitations once B-43: z3_check.py; B-44: tracked against reviewed commit
8978a78 2026-10-04 P52: fixes from the independent check (Rival 4 verbatim, patient-link limits, Cor 2.3, OpenNCP scope, Z3 text, cross-refs) P52b: Appendix A.23/A.24 synced B-45: z3_check.py Semantics II encoded in full, F up to 120
9034623 2026-10-04 B-46: public repo R-27 (z3_check.py); CHECKSUMS copied back
bef2270 2026-10-05 P53: voice and hooks in Ch4/Ch6 (PRES-2); SPUHiN draft P13/P14/P24/P31 traced in §4.11 and Table 4.1 (M6a); tracker: R3-F10 waiting; SEL anchors in TIGER_DRAFTS
3126832 2026-10-05 P54: SEL framing anchored (CSCMP, Nahmias, Elhub, IEA); politiregisterloven § 17 checked against consolidated text
1983c11 2026-10-05 P55: Figures 4.1 and 5.1 (Archify architecture diagrams, HD)
12349eb 2026-10-05 P56: audit fixes (hooks, SPUHiN grades, Elhub quote, Prop 3 idiom, counts, figures redrawn) P56b: §1.2 SPE extension with both conditions; B-47 trail_check check 10 sees every tracker row
c07856a 2026-10-05 P57: viewer described in Appendix A.14, Table 5.1 and A.1/A.2; B-48 appendix_sync P57b: redesigned eight-page viewer with live Archify diagrams (app.py, ui.py, assets)
638b9b7 2026-10-05 B-49: public repo R-28 pushed; CHECKSUMS regenerated; documents rebuilt
2c89b4d 2026-10-06 P58: patient-link commitment in each log leaf; third tamper test P58b: Appendix A listings synced P58c: viewer third tamper test P58d: viewer text; B-50 recorded runs, Figure 5.1, cached contents page numbers
a07f361 2026-10-06 B-51: Synthea pinned, reproducibility claim corrected, full-cohort re-run; public repo R-29
7c6b0d4 2026-10-06 P59: João 6 Oct tracked changes applied verbatim P59b: remaining changes by hand and his comments (P(a), D6.3 v2.0, Helsedataservice, Rak, Table 5.7 one version, Appendix B/C) P59c: A.17 re-run listing P59d: line counts P59e: Figure 4.1 caption P59f: viewer mismatch diagnostics P59g: viewer line count P59h: fee reference P59i: audit fixes P59j: RQ paragraph; B-52 figures and appendix_sync
bca1712 2026-10-06 B-53: public repo R-30; CHECKSUMS
```

## Public repo Astheno-sphere/TRF commits (main)

```
dba9c56 2026-09-28 Fix the line count I just got wrong: 526, not 527
a6062e3 2026-10-03 Revision for the supervisor review: record model, ciphertext deletion, Merkle-log integrity
0f3c39e 2026-10-03 State the results as propositions (supervisor's M4)
2b2dddb 2026-10-03 Optional module: real AES-256-GCM envelope encryption of the record lifecycle
b99aa5f 2026-10-03 Version and Change Record moved from the thesis front matter (R-24)
94b099f 2026-10-03 App: integrity and tamper tests, real envelope encryption, Proposition 3 tab; thesis renumbering (R-25)
b8b90bf 2026-10-03 Checker header and Appendix A corrections; README commitment (R-26)
398d62b 2026-10-04 Optional bounded SMT check of Propositions 1-3 (z3_check.py); Appendix A.23/A.24 (R-27)
20fd2fe 2026-10-05 Viewer redesign: eight pages, record life strip, live architecture diagrams (Archify); README and Appendix A synced (R-28)
047c411 2026-10-05 CHECKSUMS and change trail for R-28
511501d 2026-10-06 Patient-link commitment and third tamper test; Synthea pinned (d9d07a6); full-cohort re-run (R-29)
169c99a 2026-10-06 Supervisor review 6 Oct merged: viewer diagnostics, figures redrawn, Appendix A synced (R-30)
```

## Public repo change records (R-rows)

| R-01 | `data/synthea_subset/*.json` | Added the 8 untrimmed Synthea bundles, 40 MB, unmodified | Tab 3 had no data; README and CHECKSUMS both listed the directory | `python3 synthea_layer.py` reads 8 bundles, mean payload 891 bytes, six measures identical to
| R-02 | `data/synthea_subset/README.md` | New. Generation command, the 98-from-100 count, the six provenance markers, the invariance table, the 891 vs 1,006 byte statement | Provenance must travel with the data, not only with the thesis | Every claim carried 
| R-03 | `requirements.txt` | Restored: `streamlit>=1.30` | Streamlit Cloud installs from it; its absence left the deployment on whatever the platform defaulted to | md5 `944269ad914f`, matching the value CHECKSUMS.md recorded before the upload |
| R-04 | `docs/expected_trf_output.txt` | Restored by running `python3 trf_checker.py` and capturing stdout | README instructs the reader to diff against it; the file was missing | md5 `41b56742d35d`, matching the recorded value, and byte-identical to `repro_p
| R-05 | `README_Appendix_A.md` → `docs/Appendix_A.md` | Moved, contents untouched | README and PUSH_INSTRUCTIONS both reference the `docs/` path | md5 `71d1eb8f91c5` before and after, matching CHECKSUMS |
| R-06 | `NORWEGIAN_MODULE_README.md` → `norwegian_docs/NORWEGIAN_MODULE_README.md` | Moved, contents untouched | README references the `norwegian_docs/` path | md5 `75a47ac43d91` before and after, matching CHECKSUMS |
| R-07 | `norwegian_docs/HOW_TO_RUN.md` | Rewritten. The original 116-line file was not uploaded and no copy survives in the working set | README links to it; a dangling link is worse than a rewrite | Every figure in it was taken from an actual run of the thre
| R-08 | `CHECKSUMS.md` | Regenerated from the files actually present | It recorded `app.py` at 404 lines and md5 `52bf6c71ffd7`; the repository holds 418 lines and `b74ec9905035`, so the record was stale for that file and wrong about six paths | Generated by 
| R-09 | `docs/Appendix_A.md` | Contents table: `norwegian/norwegian_layer.py` → `norwegian_layer.py`, same for `cross_sector_check.py` | Both files sit at the repository root, as README.md states and as Streamlit Cloud requires; the appendix described a dir
| R-10 | reproducibility package | `trf_checker.py`, `synthea_layer.py`, `norwegian_layer.py`, `cross_sector_check.py` moved from `src/` and `src/norwegian/` to the package root; `data/synthea_sample/` (3 trimmed bundles) replaced by `data/synthea_subset/` (8 
| R-11 | `repro_package/results/` | `synthea_comparison_output.txt` → `synthea_comparison_full_cohort_output.txt`; new `synthea_comparison_subset_output.txt` | The recorded comparison was the 98-bundle run at 1,006 bytes, but the package ships the 8-bundle s
| R-12 | `app.py` | New Tab 5, "Robustness and cross-checks". Runs `brute_force_semantics_I()` over the four cases and `delta_witness()` over δ = 1 and δ = 3, each with a pass or fail banner, then restates the artefact's limits | `brute_force_semantics_I()` 
| R-12a | `app.py` | Cross-check case parameters taken verbatim from `trf_checker.main()` | I first wrote them from memory and two were wrong: case 1 returned feasible=True against a recorded False. Caught by executing before committing, not by reading | The f
| R-13 | `docs/expected_delta_witness_output.txt`, `expected_synthea_subset_output.txt`, `expected_norwegian_output.txt`, `expected_cross_sector_output.txt` | New. One recorded run per command | Only the checker had a recorded output to diff against. The other
| R-14 | `docs/Data_Provenance_Statement.md` | Added to the repository | It answers the supervisor's data blocker and lives where a reader who clones can find it, not only in the thesis working set | Byte-identical to the working-set copy |
| R-15 | `README.md` | Documents Tab 5, the recorded-run table, and the robustness section; `app.py` line count 404 → 524 | The README described four tabs and one recorded output | Line count read from the file |
| R-16 | `trf_checker.py` | Accessor/subject split of the metadata; subject link removed at the ceiling and logged; payload deleted with key and salt; payloads per record class; Merkle-log integrity in `V_II` with two tamper tests; `make_salt()` and `--random-
| R-17 | `app.py` | Auditor view shows accessor fields, permit, subject link, salt and ciphertext; Synthea sample read before invalidation deletes the payload | Follows R-16 | Every button run headless (Streamlit AppTest): no exception |
| R-18 | `docs/expected_trf_output.txt`, `docs/expected_delta_witness_output.txt`, `docs/expected_synthea_subset_output.txt` | Re-recorded | R-16 changes the auditor view, adds the integrity section, and changes the constructed payload mean (35 → 43) | `expe
| R-19 | `docs/Appendix_A.md` | Replaced by the thesis's Appendix A | The copy here was older than the thesis's | Every source listing and console output in it equals the file it reproduces (`appendix_sync.py` in the thesis tools) |
| R-20 | `README.md` | Line counts, payload mean, a section on this revision | Follows R-16 | — |
| R-21 | `CHECKSUMS.md` | Regenerated from the files present | README had changed after the last regeneration (28 Sept, 11:10: `app.py` line count) | Generated, not typed |
| R-22 | `trf_checker.py`, `app.py`, `README.md`, `docs/Appendix_A.md`, `docs/expected_trf_output.txt`, `docs/expected_delta_witness_output.txt` | "Theorem" renamed "Proposition" in comments, printed headers and text | The thesis now states its results as prop
| R-23 | `crypto_envelope.py`, `docs/expected_crypto_envelope_output.txt`, `requirements.txt`, `README.md`, `docs/Appendix_A.md` | New optional module with real AES-256-GCM envelope encryption; `cryptography>=42` added to requirements (used by this module only
| R-24 | `docs/VERSION_RECORD.md` | Version and Change Record (thesis Tables F.1, F.2) moved here from the thesis front matter, with a note on why | Supervisor PRES-3: process history belongs with the artefact, not in the thesis | Text identical to the front-m
| R-25 | `app.py`, `trf_checker.py`, `requirements.txt`, `README.md`, `docs/Appendix_A.md` | App: integrity and tamper tests in Tab 1, envelope encryption in Tab 5, new Tab 6 (Proposition 3); deprecated `use_container_width` replaced; streamlit>=1.45. Thesis r
| R-26 | `trf_checker.py`, `docs/Appendix_A.md`, `README.md` | Checker header without patch references; ten-year floor comment marked illustrative; Appendix A prose corrected (date, counts, A.16/A.17); README reference commitment updated to the current run | S
| R-27 | `z3_check.py`, `docs/expected_z3_check_output.txt`, `docs/Appendix_A.md`, `README.md` | New optional module: bounded SMT check of Propositions 1-3 (Z3); Appendix A.23/A.24 | Supervisor review of 4 Oct asked for an independent bounded check (Z3 or Allo
| R-28 | `app.py`, `ui.py` (new), `assets/` (new), `.streamlit/config.toml` (new), `docs/architecture/` (new), `requirements.txt`, `README.md`, `docs/Appendix_A.md` | Viewer redesign: eight pages, record life strip, live Archify diagrams of Figures 4.1 and 5.1
| R-29 | `trf_checker.py`, `app.py`, `docs/expected_trf_output.txt`, `docs/expected_delta_witness_output.txt`, `docs/Appendix_A.md`, `assets/`, `docs/architecture/trf-artefact.archify.json`, `data/synthea_subset/README.md`, `docs/Data_Provenance_Statement.md`,
| R-30 | `app.py`, `assets/`, `docs/Appendix_A.md`, `docs/architecture/`, `README.md` | Supervisor review 6 Oct merged: viewer mismatch diagnostics and stale-module warning; Figures 4.1 and 5.1 redrawn (opening holder, payload retention period, leaf contents; 
