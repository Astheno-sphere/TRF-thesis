# Review Tracker — Prof. Ferreira, 30 Sept 2026

One row per item in the emailed review (`supervisor_review/review_email_text_2026-09-30.txt`).
`handoff_tools/trail_check.py` reads this table. Rules it enforces:

- Status is one of `OPEN`, `BLOCKED`, `PARTIAL`, `CLOSED`, `DECLINED`.
- A `CLOSED` or `PARTIAL` row must name at least one patch ID, and every ID named must exist in `patches/APPLIED.log`.
- A `CLOSED` row whose guard (in `handoff_tools/guards.json`, `item` field) has not reached its goal is an error.
- `DECLINED` needs a reason in Evidence: we answer his point with evidence, we do not ignore it.

His authority is the emailed text. His tracked changes in the returned .docx are proposals, judged
passage by passage when the patch for that passage is written.

| Item | What he asked | Status | Patches | Evidence / note |
|---|---|---|---|---|
| M1 | Define p(a) per record class from the eHDSI audit spec and D7.4; revise the SPE record model in code | CLOSED | P04, P06, P12, P14, P42, P43 | SPE p(a) fields named and tied to D7.4 OPR-17; cross-border p(a) tied to ITI-55 and the patient-identification step, eHDSI audit spec stated as not obtained; Semantics I reframed as the semantics of a log that keeps its payload readable, no current-practice claim (P42); Synthea payloads stated as stand-ins (P43) |
| M2a | One reading of Art 68(12) carried through Cor 1.2, Thm 2, §4.8 | CLOSED | P04, P05, P07, P42 | Ceiling = electronic health data at every site; §6.2 consistent with Rival 6; §5.4 notes relocation removes the 39 (P42) |
| M2b | Rival 6: move the logs out of the SPE at permit closure | CLOSED | P06 | Rival 6 accepted for the ceiling and bounded by Proposition 4 (P06). Ch6/Ch7 echo in P07 |
| M2c | Rewrite §6.1's opening; lead with the robust result | CLOSED | P07 | §6.1 leads with the robust result, then Proposition 4, then the conditional SPE instance |
| M3a | Salt: text, code and change record agree | CLOSED | P02 | D-15: salt destroyed (Tiger, 22 Sept). Text in §4.8/§5.6/§4.9 must follow the code |
| M3b | Ciphertext: delete at invalidation or justify | CLOSED | P02, P12 | Text (P02) and code (P12): ciphertext deleted at invalidation |
| M3c | Remove the dead salt branch; seeded generator or `--reproducible` | CLOSED | P12 | make_salt() and --random-salts; dead branch gone (guard 1 → 0) |
| M4a | Theorems renamed Propositions; weight on the §4.2 necessity analysis | CLOSED | P15, P16, P17, P18, P42, P44 | 'propositions rather than theorems' (P42); repo README Propositions (P44, public R-26) |
| M4b | Promote the §6.9a anchoring result into Ch4 as a formal result | CLOSED | P15 | Proposition 3 in Ch4 §4.6, stated precisely (collision needs L ≤ F; anchor decides visibility); §6.9a corrected |
| M4c | V_II tests integrity: hash chain over m(a), ι(a); tamper test | CLOSED | P12, P14 | Merkle log (RFC 6962), inclusion proofs in V_II, two tamper tests fail V_II; reported in §5.7 |
| M4d | Shorten Ch5; violation rates are generator artefacts | PARTIAL | P31, P43, P46 | Rate interpretation removed (§5.3, §5.4); repetition cut. Ch5 is about 4,400 words including tables against 3,386 in the reviewed draft because of the integrity and envelope-encryption results he asked for in M4c/M3b |
| M5a | Ten-year floor: primary eHDSI source with section, or F=120 illustrative | CLOSED | P09, P42, P44 | Ten-year floor 'as reported' and illustrative at every site, code comment included |
| M5b | SPUHiN "finalised" claims aligned to what was inspected | CLOSED | P10 | Every claim limited to the hearing version inspected (P10, P10b) |
| M5c | Art 68(12) and Art 73(1)(e) quoted verbatim (OJ English); one more language version | PARTIAL | P04, P07, P08, P42 | Art 68(12) and Art 73(1)(e) both verbatim from the OJ English text (P42). Open: one further language version (his 'ideally'; T-10) |
| M5d | §2.2 EHDS dates fixed against Art 105; drop the EY source | CLOSED | P03 | Arts 19(1), 105(1)(a) verified 3 Oct |
| M5e | Table 2.1: preprint/practitioner sources in a separate band; Feng et al. 2022 peer-reviewed version? | CLOSED | P09, P20 | Feng peer-reviewed (P09); Table 2.1 bands (P20) |
| M6a | Traceability matrix against D7.4 and the SPUHiN checklist | PARTIAL | P22, P24, P53 | D7.4 traced row by row in Table 4.1; SPUHiN draft (2024) logging/termination requirements P13, P14, P24, P31 added (P53-15/16). Hearing-version numbering not re-checked (attachment URL too long for the fetcher) |
| M6b | Reword Appendix C item A1 ("full confidence"), record in one line | CLOSED | P19 | A1 reworded; one-line record in Appendix C |
| M7a | Logistics anchor (UCC customs record-keeping vs destruction orders); §1.4 overreach | CLOSED | P11, P43 | UCC anchor; seafarer and OECD material cut; §1.4 overreach rewritten (P43) |
| M7b | One sentence in §1.5 on the programme fit | CLOSED | P11 | One sentence in §1.5 |
| MIN-01 | §3.6 line counts inverted (checker 363, layer 152) | CLOSED | P01 | Prose points to Table 5.1 (formerly 5.0a); counts in Table 5.1 and Appendix A (534 for the checker, P56) |
| MIN-02 | §3.6 "tuples defined in Section 3.4" → 4.3 | CLOSED | P01 |  |
| MIN-03 | §1.6 drop "accumulator-based" | CLOSED | P01 |  |
| MIN-04 | §2.1.4 "four dated rounds" vs Appendix B five | CLOSED | P01 | Fork R1 merged rounds to 7 on the superseded branch; re-judge |
| MIN-05 | §3.4 / Cor 1.1 "ordinary"/"generic case" are frequency claims; soften | CLOSED | P21 | §3.4, Cor 1.1, Ch4 summary |
| MIN-06 | §4.4 C1 closed window spans F+1 months | CLOSED | P21 | Closed window justified in §4.4 |
| MIN-07 | Table 5.0a, A.9c, A.14: "Section 6.9" → 6.9a after renumbering | CLOSED | P14 | Table 5.0a and Appendix A ×3 |
| MIN-08 | Appendix C preamble: "Chapter 3, Section 3.9" → 3.8 | CLOSED | P01 |  |
| MIN-09 | "an separately written" ×3 → "a separately written" | CLOSED | P01 |  |
| MIN-10 | §5.3, §5.4, §5.6: witness lines in a code block, one per line | CLOSED | P14, P25 | §5.3, §5.4, §5.6 verbatim code blocks |
| MIN-11 | §6.1 "thirty-nine concrete witnesses" → "witnesses in the model" | CLOSED | P01 |  |
| MIN-12 | §1.5 "addendum to the thesis supervisor": remove or make an appendix | CLOSED | P01 |  |
| MIN-13 | Numbering: §5.5a, §6.9a, Appendix A sequence; regenerate TOC | CLOSED | P38, P41, P43 | Also C.1a folded into C.1 (P43) |
| MIN-14 | Title page logo placeholders must render | OPEN |  | Embed the logos; check in the PDF |
| MIN-15 | Cite a repository tag or commit, archive on Zenodo with a DOI | CLOSED | P89 | P89 (30 Oct): TRF v1.0.1, DOI 10.5281/zenodo.23819275, cited in A.1 + abstract footer. |
| PRES-1 | Cut defensive meta-commentary by at least half | CLOSED | P26 | 84 → 31 matches (−63%) with the widened detector; remaining hits carry argument or are PRES-3 process material |
| PRES-2 | Voice: prose in the candidate's own voice, esp. Ch4 and Ch6 | PARTIAL | P53 | Hooks and sentence splits in Ch4/Ch6 (P53-01..14, 17..23); final read in your own voice still yours (T-7) |
| PRES-3 | Process material: one statement in the Declaration; Version and Change Record to the repository | CLOSED | P27, P43, P44 | Process residue removed from §2.1.4, §2.9, §5.7, §6.8, the Declaration (one statement), the checker header (P43, P44) |
| PRES-4 | Repetition: NCPeH pilot details and the 68(12) reading said once, then cross-referred | CLOSED | P28, P29, P43, P46 | Pilot detail in §2.2 only (§1.1 now points there); §2.3 points to §4.6; Synthea limitations once in §3.5 (P43, P46) |
| PRES-5 | Length: check programme guidance; slim Appendix A to tag + SHA-256 + core functions | OPEN |  |  |
| R3-T | Review of 4 Oct (Google Doc v3): ten tracked wording changes | CLOSED | P47, P48 | Applied verbatim (P47); Sammendrag, §5.1, §6.1, §7.2 aligned with the abstract; Rival 4 point restated on the log (P48) |
| R3-M1 | Circular metadata/payload split; necessity per class; sensitivity result | CLOSED | P49 | Payload defined by source; necessity argued per class in §4.2; Corollary 2.3 with proof sketch |
| R3-M2 | Patient link on the cross-border path: argue necessity or remove | CLOSED | P49 | Option A (Tiger 5 Oct): kept and argued under Art 17(3)(b) with EHDS Art 9(1)-(2); carried into §4.8, §5.7, §7.1 |
| R3-M4 | Counts are generator-determined; independent bounded check (Z3/Alloy) | CLOSED | P47, P48, P50, P50b | Counts out of abstract, §6.1, §7.2, labelled in §5.1; ten-year permit note in §5.4; z3_check.py: 9 checks unsat, mutation refuted |
| R3-M5 | Art 68(12) reading; Cor 1.2 conditional throughout; Art 17(3)(d) and opt-out | CLOSED | P47, P48, P49, P56b-01 | 'conditional extension' in §1.2, §1.4, §2.9, §4.6, §6.1; Art 17(3)(d) and Art 71 in §4.4 |
| R3-M6 | Semantics I without a real system: check OpenNCP | CLOSED | P49 | OpenNCP source (2017) and Danish 9.1.0 deployment schema inspected: readable message content and patient ID, no retention or purge logic, modification refused |
| R3-LIT | Redactable signatures / chameleon-hash blockchains | CLOSED | P49 | Paragraph in §2.4 with seven verified references; pointer from §4.8 |
| R3-TT | Unimplemented terminal transition, nonce, consistency proofs, accumulator: say so in the summaries | CLOSED | P49 | §4.12 and §7.1 |
| R3-RS | Restructuring: trim Ch2; cut repeated limitation statements | PARTIAL | P51 | Ch2 repetition of Ch1 cut; §6.11 points to §3.7. Ch2 remains ~12,000 words pending the programme length limit (T-8) |
| R3-F10 | Ten-year floor source thin: ask Helsedirektoratet | CLOSED | P83 | Helsedirektoratet replied 19 Oct 2026 (Larsen, Avd.dir.): the requirements catalogue + specs fix no retention method or period, defer to national law; pilot set to 6 years, production figure undecided and reserved to Hdir as controller. Folded into §2.3 as a primary source (personal communication); converts the unsourced ten-year figure to a controller-confirmed unfixed parameter. Correspondence recorded in sources/helsedir_retention_correspondence_2026-10.md. Corollary 2.2: no result depends on the value |
| R3-PRL | Verify politiregisterloven § 17 wording | CLOSED | P54-07 | Consolidated Lovdata text supplied by Tiger (5 Oct; last amended LOV-2026-06-19-49): § 17 wording identical to §6.10; no amendment note on § 17 |
| R3-FIT | Programme fit beyond the customs analogy | CLOSED | P54-01, P54-02, P54-03, P54-04, P54-05, P54-06, P56-18, P56-19 | §2.7: CSCMP definition, perishable inventory (Nahmias, 1982), Elhub retention per data category; §1.5: IEA (2025) energy line, no saving claimed |
| R3-AI | AI-use declaration matches HiMolde rules; defence preparation | OPEN |  | Tiger confirms (5 Oct) HiMolde permits AI use under ethical use; Declaration names tool, uses and author's responsibility. Defence preparation remains Tiger's |

## Round 4 — João's review of 6 Oct 2026 (`supervisor_review/review4_JF_2026-10-06.docx`, extraction `review4_changes.txt`)

| Item | What he asked | Status | Patches | Evidence / note |
|---|---|---|---|---|
| R4-TT | His tracked changes (77 marked paragraphs) | CLOSED | P59, P59b, P59i, P59j | 53 verbatim, rest adapted (P58 implemented the link commitment); audit 6 Oct |
| R4-C1 | Length: abstract and main text against programme limits; cut repeated authority-problem restatements; Appendix A listings to a tagged release | OPEN |  | Deferred by Tiger to the end. Abstract now 421 words |
| R4-C2 | AI-use declaration and Sources disclosure confirmed with the coordinator | PARTIAL | P84 | Declaration now names Archify as the diagram/figure generator (P84); Tiger confirmed (20 Oct) HiMolde permits Archify and other design/image tools. Formal confirmation with the coordinator remains Tiger's |
| R4-C3 | Helsedataservice sentence against helsedata.no | CLOSED | P59b, P59h | FHI since 1 Jan 2024; 11 registries incl. Cancer Registry; forwarding claim removed; two fees |
| R4-C4 | Rak (2024) supports the sentence; pinpoint page | PARTIAL | P59b | Full text paywalled; sentence limited to the abstract (p. 928). Get PDF via HiMolde library |
| R4-C5 | P(a) in the notation table; t_I with the third trigger in §4.7 | CLOSED | P59b, P59i | Notation, §4.7 formula, proof steps 2 and 4 |
| R4-C6 | Proactive invalidation paragraph; report P as optional run if implemented | PARTIAL | P59b | Specified in §4.8; not implemented (artefact runs with P = ∞); Z3 does not encode the third trigger |
| R4-C7 | Implement subject-field commitment, third tamper test, re-record outputs, update §5.7, Table 4.1, Fig 4.1, not-implemented lists | CLOSED | P58, P58b, P58c, P58d, P59b | Third test fails as required; outputs re-recorded |
| R4-C8 | Regenerate Figure 5.1 (eight pages), thesis legend categories; Figure 4.1 with m_acc storage and link commitment | CLOSED | P59e | Archify finalize pass (B-50, B-52) |
| R4-C9 | Re-run full-cohort Table 5.7 with final code; simplify notes | CLOSED | P59b, P59c | 1,002 bytes; six measures identical |
| R4-C10 | Pin Synthea; record jar SHA-256; tag the repository release and cite it in A.1 | CLOSED | P59b | Commit d9d07a6 and SHA-256 recorded. Release tag and A.1 citation pending (end, with Zenodo) Release tag v1.0.1 + DOI cited in A.1 (P89). |
| R4-C11 | Datatilsynet enquiry: date and status | CLOSED | P59b, P84 | Send date confirmed by Tiger (20 Oct): 23 September 2026, response pending at submission (Ch7 §7.4). Same sentence updated to record the Helsedirektoratet reply of 19 Oct (P84) |
| R4-C12 | Cite TEHDAS2 D6.3 v2.0; re-check quotes and pages | PARTIAL | P59b | v2.0 cited as 2026a, Section 7.2; two unsupported claims removed. Page number unverified (PDF not downloadable here) |
| R4-C13 | Restore truncated queries 12, 13, 17 | CLOSED | P59b | Restored from the 22 May chat record, marked |
| R4-C14 | Note removed sources (#75, EY in #77) | CLOSED | P59b | Reasons stated |
| R4-C15 | Appendix C R1 double-barrelled | CLOSED | P59b | Kept verbatim, limitation in C.7 |
| R4-C16 | Merge §6.11 into the Summary | CLOSED | P59b, P59i | Contents entries updated |
