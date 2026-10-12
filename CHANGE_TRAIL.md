# Change trail

## 10 October 2026 — handoff package

| ID | Change | Verification |
|---|---|---|
| B-55 | handoff/2026-10-10/CHECKSUMS_SHA256.txt: SHA-256 of every tracked file at B-54 plus every file of Astheno-sphere/TRF at 169c99a | `sha256sum -c` all verify |
| B-54 | Handoff: HANDOFF_READ_FIRST §000 (state, open items, rules, Round 5 procedure); CONVERSATION_LINEAGE chat trail + landmarks; RESUME_PROMPT; SUPERVISOR_FEEDBACK_HISTORY rounds 3–4; REVIEW_TRACKER R4-* rows; handoff/2026-10-10/ (AUDIT_STATUS, VERSION_LOG, CHECKSUMS_SHA256); session transcripts exported to conversation_history/; tools extract_review.py, locate_edits.py, render_figure.py | trail_check; extract_review.py reproduces review4_changes.txt |

## 6 October 2026 — João's review of 5 Oct draft (review4_JF_2026-10-06.docx): P59–P59g

| ID | Change | Verification |
|---|---|---|
| P59-01 to P59-92 | His tracked changes, located word by word in the sources and applied verbatim (abstract and Sammendrag open with the one-year floor; Art 17(3)(c); EEA incorporation; NCPeH roles; Direktoratet for e-helse merger date; literature strands renumbered; Art 9(2) three-year binding value; Semantics I as de facto practice; opening handed to the patient or home NCP; Rival 4 bounded; §5.4 permits in their last six months; Appendix B/C wording) | Extraction `supervisor_review/review4_changes.txt`; inspector: losses declared (May 2023, A.2) |
| P59b-01 to P59b-65 | His remaining changes placed by hand (RQ split, Table 2.1 cell, March & Smith 1995, four references, proactive invalidation paragraph, §6.9 logistics paragraph) and his comments: P(a) in notation and §4.7; 'not yet implemented' text adapted to P58; D6.3 cited at v2.0 (2026a; D7.4 now 2026b) with two claims the guideline does not make removed; Helsedataservice corrected against helsedata.no; Rak limited to the abstract (p. 928); §6.11 merged into §6.11 Summary; Datatilsynet enquiry sent; Table 5.7 on one code version (1,002 bytes; Synthea d9d07a6, -r 20260916); queries 12, 13, 17 restored from the session record; removed sources noted; R1 limitation | helsedata.no, Zenodo 10.5281/zenodo.20199187, Cambridge Core abstract read 6 Oct |
| P59c-01 to P59c-01 | A.17 intro: re-run with final code and pinned cohort | appendix_sync |
| P59c-B07 to P59c-B07 | A.17 listing synced to synthea_comparison_full_cohort_rerun_2026-10-06.txt | appendix_sync |
| P59d-01 to P59d-08 | Line counts after P58: checker 551 (430 code lines), viewer 812 + 133 | wc -l |
| P59e-01 to P59e-01 | Figure 4.1 caption for the redrawn figure (three triggers, opening holder, leaf contents) | Archify finalize pass; legend in thesis categories for both figures |
| P59f-01 to P59f-01 | Viewer: on a mismatch, a table of which check failed and a stale-module warning (the live app showed 'does NOT match' after R-29: the cloud process kept the old trf_checker, which cannot see a changed link) | Local run: 'Matches the thesis' |
| P59g-01 to P59g-03 | Viewer line count 825 | wc -l |
| P59h-01 to P59h-01 | Fee reference re-pointed to helsedata.no/no/priser (read 6 Oct) | — |
| P59i-01 to P59i-09 | Independent audit of the merge: JF [39] tail restored ('and its inclusion in the log; which payload … opening'); Appendix A three tamper tests; A.21 1,002; contents entries for Chapter 6 after the merge; P = ∞ noted in §5.6 and A.6; proof step 4 names the payload retention period; §2.4 strands in their stated order | Audit report (subagent, 6 Oct); Rak pinpoint p. 928 is the abstract page, full text not read |
| P59j-01 to P59j-01 | JF [9]: the three requirements as their own paragraph | — |
| P76-01 to P76-01 | Length cut, Ch2 §2.4 KONFIDO (Option-2 content cut): collapsed the four-pillar enumeration to the load-bearing blockchain-auditing pillar + the two relevant gaps (Intel SGX hardware dependency; blockchain auditing didn't engage the erasure right, immutability-vs-erasure unresolved), keeping all three cites (Diamantopoulos 2019, Staffa 2018, Natsiavas 2021), Horizon 2020 2016–2019, OpenNCP. Shed photonic PUFs, SIEM, pilot countries (Denmark/Italy/Spain), "disruptive logging". Gates: floor ADMIT (0 losses); trim_inspector ADMIT (59w); global xref clean. Preservation agent ADMIT + grep (dropped specifics absent from Ch1/3–7; Table 2.1 KONFIDO row still supported). Ch2 11862→11803 words. Ch1 frozen | preservation agent (full-context + grep, ADMIT); trim_inspector; patch.py |
| P75-01 to P75-02 | Length cut, Ch2 §2.2 + §2.6 (Option-2 content cut): collapsed two Norwegian-infrastructure background blocks. §2.2 Norway-pilot: kept the live/in-production claim (Bodø/Stjørdal retained so Ch1's "§2.2 gives the details" pointer holds), NCP-A, the low-volume honesty caveat, EEA incorporation route, all dates (Jan 2023, 41mo, 31 Mar 2025, 11 Apr 2025) + cites; shed partner-country names, Trondheim/Ålesund/Helseplattformen, and the ePrescription-without-eDispensation change-proposal (+12 March eHOMB). §2.6 Helsedataservice: kept the eleven-registry access-decision authority; shed the Cancer-Registry example, Directorate-of-Health nuance, cost/invoice split. Gates: floor ADMIT (LOST_OK: number 12, number 2026, citation Helsedirektoratet 2026 [3→2], citation Helsedataservice n.d.-b singleton [grouped kept]); trim_inspector ADMIT (121w cut); global xref clean. Full-context preservation agent ADMIT + repo grep (dropped specifics occur nowhere else in Ch1/3–7; operational claim corroborated at §2.6 L178 & Ch1 §1.1; names survive in Appendix B search log). Ch2 11983→11862 words. Ch1 frozen | preservation agent (full-context + grep, ADMIT); trim_inspector; patch.py |
| P74-01 to P74-03 | Length cut, Ch2 §2.4 (Option-2 content cut): compressed three literature-survey paragraphs — the chameleon/sanitizable/redactable signature survey (kept all 7 cites + the "weakens the binding" claim + the opposite-route/trust-in-key-destruction contrast with §6.3 ref), the accumulator/commitment survey (kept Benaloh&de Mare 1994 / Camenisch&Lysyanskaya 2002 / Ren 2022 + the verifiable-membership machinery §4.8 rests on), and the audit-log-integrity survey (kept Schneier&Kelsey 1999 / Merkle 1988 / Crosby&Wallach 2009 / Laurie 2013,2014 + Merkle + the §4.8 resolution hook). Gates: floor ADMIT (LOST_OK: 5 narrative→parenthetical cite REFORMATTINGS — each reference preserved in parenthetical form, bibliography unchanged); trim_inspector ADMIT (81w cut); global xref clean. Full-context preservation agent ADMIT (verified §4.8 optional-accumulator layer + §6.5 logarithmic-proof + §6.3 all still supported). Ch2 12064→11983 words. Ch1 frozen | preservation agent (full-context, ADMIT); trim_inspector; patch.py |
| P73-01 to P73-02 | Length cut, Ch2 §2.2 (Option-2 content cut; Tiger locked Option 2 → ~42k target). EDIT 1: compressed the six-step MyHealth@EU transmission narration to one enumerated sentence, keeping Simjanoska 2025, eIDAS auth, the ATNA audit-log step, and the retention→§2.3 hook; dropped terminology-binding specifics (SNOMED CT/LOINC/XACML), national identifier, native clinical document format. EDIT 2: compressed the primary-use Article 105 calendar connective prose, keeping all dates (26 Mar 2027/2029/2031), Article 105, Article 19(1), both cites, and the Group One/Two category names. Gates: floor ADMIT (LOST_OK: article 105, number 105, grouped cite "Article 105 EHDS; European Commission, 2025a" — all survive elsewhere in §2.2); trim_inspector ADMIT (107w cut; declared term drops binding 9→8 [= "terminology bindings", HL7 sense not crypto] and National Contact Point 4→3 [survives §2.2 L76/80]); global xref clean. Full-context preservation agent ADMIT (grep-verified SNOMED/LOINC/XACML absent from rest of thesis body; Ch1 L9 already narrates the flow generically). Ch2 12171→12064 words. Ch1 frozen | preservation agent (full-context + repo grep, ADMIT); trim_inspector; patch.py |
| P72-01 to P72-01 | Length cut, Ch2 §2.4 (trim 2): the section-closing "Three observations" paragraph re-cited and re-named every system already discussed at length earlier in §2.4; kept the three observations verbatim (incl. the distinctive TEHDAS2 2026b Annex 7 p.96 named-gap cite), stripped the re-citation list + system names to "each reviewed above". Gates: floor ADMIT (LOST_OK: grouped cite Albalwy/Bai/Sharma + Natsiavas/Brunner/Camenisch singletons + years 2021/2022/2025/2026/2002 — all survive in §2.4 narrative + Table 2.1); trim_inspector ADMIT (43w cut, headroom 781w); global xref clean. Full-context preservation agent ADMIT (each removed system homed at §2.4 lines 118-128; observations 2-3 byte-identical). Ch2 12214→12171 words. Ch1 frozen | preservation agent (full-context, ADMIT); trim_inspector; patch.py floor gate |
| P71-01 to P71-01 | Length cut, Ch2 §2.10 (trim 1): the "Conceptual Positioning" opener re-derived the whole Ch4 model (decomposition, three regimes as constraints, both semantics, infeasible/satisfiable results, mechanism, corridor); compressed to a positioning statement naming the TRF Model + Crypto-Erasure by Invalidation, keeping the two features that matter for positioning (parameterised floor with both floor values; mechanism within the §2.3 corridor, not mere assertion) and cross-referencing Ch4 and §2.3. The novelty-claim paragraph (§2.10 para 2) untouched. Gates: floor 0 undeclared (LOST_OK: article 17, article 68(12), numbers 17/68/12 — all developed in §2.3/§2.9); trim_inspector ADMIT with declared term-mention drops (payload 6→5, commitment 11→10, hiding 3→2, invalidation 9→8, deletion ceiling 10→9, erasure right 8→7 — de-dup, agent confirmed not paraphrase); global xref intact. Full-context preservation agent ADMIT (homed all four removed clusters incl. accumulator "specified but not implemented" caveat → Ch4 §4.8/§4.9/§4.12). Ch2 12291→12214 words. Ch1 frozen | preservation agent (full-context, ADMIT); trim_inspector; patch.py floor gate |
| P70-01 to P70-01 | Length cut, Ch2 §2.3 (trim 1): compressed the §2.3 intro signpost (scaffolding). Three further §2.2/§2.3 framing-sentence candidates were preservation-agent REJECTED as carrying claims/requirements and withdrawn — strict calibration confirmed by Tiger; strategy pivoted to whole-restatement-paragraph dedup for the real tonnage. Ch1 untouched (frozen). Gates: floor 0 lost, trim_inspector ADMIT, global xref 703/703 | preservation agent (4-edit batch, 1 ADMIT / 3 REJECT) |
| P69-01 to P69-01 | Length cut, Ch1 §1.3 (trim 2): the research-objectives paragraph re-derived the whole Ch4 model (both semantics in full, mechanism mechanics, Prop 1-4); compressed to an objective-level preview cross-referencing Ch4, keeping TRF name + Feng cite, the tri-lateral-by-structure clause, both floor values, the two semantics, the "every arrival pattern" scope, Crypto-Erasure by Invalidation + NIST SP 800-88, and Propositions 3-4. Gates: floor 0 lost; trim_inspector ADMIT with declared term-mention drops (payload 6→4, binding 5→4, invalidation 8→7 — de-dup, agent confirmed not paraphrase); global xref 703/703. Ch1 4350→4245 words | preservation agent (full-context, ADMIT); trim_inspector defined-term declaration added (critical fix) |
| P68-01 to P68-04 | Length cut, Ch1 §1.1-1.2 (trim 1 of the Round-5 length pass; TRIM_RATIONALE.md): removed unsupported superlative opener [A] and editorial "most consequential change" ranking [B] (preservation agent ADMIT; ripple grep clear); dropped intensifier "Critically," [D]; de-duplicated §1.2's re-derivation of the Art 68(12)/73(1)(e) collision to a cross-reference to §1.1, keeping both "broad reading" hedges, the researcher scenario, Art 68(12)/TEHDAS2 and the timing [C] (preservation agent REJECT→fix→ADMIT: Art 68(12)/TEHDAS2 folded back). Gates: floor ADMIT (LOST_OK: article 73(1)(e), numbers 1/73), trim_inspector ADMIT (58w cut, headroom 350w), global xref 702/702. Ch1 4408→4350 words | preservation agent (2 subagent passes), trim_inspector, concordance --check |
| P67-01 to P67-02 | Round 5: dropped the defensive IEA energy quote in §1.5, kept the no-energy-saving scope point and the information-logistics framing; removed the now-uncited International Energy Agency (2025) reference (JF R5[5]) | dry-run inspector: IEA citation + numbers 1.5/2024/415/2025 + one "does not" declared lost |
| P65-01 to P65-02 | Round 5 legal (quick): Datatilsynet enquiry dated 23 Sept 2026 and recorded unanswered, Helsedirektoratet ten-year enquiry likewise unanswered (JF R5[16], Tiger 11 Oct); staggered EHDS dates re-anchored on Article 105 + European Commission (2025a), "Healthy Europe" news site demoted off the legal dates (kept for commentary) (JF R5[6]) | dry-run inspector: Healthy Europe citation unit + number 2026 declared lost at the one site |
| P66-01 to P66-02 | Round 5 legal (JF R5[9], Tiger authorised): §4.2 — accessor fields are the professionals'/researchers' own personal data, their Art 17 right is covered by Art 17(3)(b) for the floor (1); the erasure duty's controller named via Commission Implementing Decision (EU) 2019/1765 Art 7 (Member-State national authority = controller, Commission = processor with no patient-data access), so it lands on the NCPeH's national authority (2); bibliography entry for 2019/1765 added to Ch4 list. Art 7 structure confirmed via two independent sources; OJ L 270 + ELI certain, exact page range to be confirmed by Tiger at EUR-Lex | dry-run inspector 0 lost / +4 article refs |
| P64-01 to P64-14 | Round 5 — Joao's R5 tracked wording edits applied verbatim (his point 5): drop redundant "Supervisor:" on the keywords footer [2]; Sikt gloss in Ethics [4]; "discontinued (avviklet)" [18]; "That tutorial article" [19]; practitioner-heuristic rewording [20]; renumbering sentence removed, point kept in §1.4 [21]; Art 5 word order [22]; "Activity 5:" colon [23]; third invalidation trigger "earliest … and any payload retention period" in §4.12 and §7.1 [32][37]; `os` import line [33]; salt-provenance clause in §5.2 (code carries `--random-salts`/os.urandom) [34]; Synthea byte-identical overclaim corrected in A.7 [40]; four nomenclature rows (m_acc/m_subj, β, p_n/p_r, e/L) [7]-[14] | dry-run inspector: §2 renumbering sentence removed whole (LOST_OK: articles 46/50/68/73, numbers, hedge 'may'); all else 0 lost |
| P62-01 to P62-02 | Round 5 wave 3: Rival 4 — commitment's real value stated plainly (substitution detection before invalidation; later checkability only with an opening) and the cross-border near-equivalence of "delete + logged deletion" conceded (JF R5[13]); exhaustive cross-check reframed as a sanity check with the bounded SMT check carrying robustness, independence rationale kept (JF R5[15], adversarial E2) | dry-run inspector 0 lost |
| P63-01 to P63-01 | Round 5 wave 3: §5.2 module count aligned to the eight .py files of Table 5.1 / Appendix A.2 — "Six further modules" → "Seven further modules … eight Python files in all", viewer split across app.py/ui.py explained (JF R5[17]) | dry-run inspector 0 lost |
| P61-01 to P61-01 | Round 5 wave 2: Proposition 4's legal premise (a controller receiving a relocated record receives the Art 17(1) erasure obligation) elevated into the proposition statement as an explicit assumption (JF R5[14]; Joao's offered alternative to relabelling, taken for lower ripple) | dry-run inspector 0 lost / +1 article ref |
| P60-01 to P60-04 | Round 5 wave 1: Prop 1 second-disjunct assumption t_π+6≥t(a) with the t(a) edge case (JF R5[11]); §6.9 "three contributions"→"three theoretical implications", cross-referring the four contributions in §7.2 (JF R5[3]); §4.7 states Props 1 and 3 follow near-immediately from the definitions and relocates the weight to the legal analysis and mechanism (JF R5[12], adversarial A1); abstract states the formal results are deliberately elementary and reading-independent, Prop 1 carries the argument (adversarial A1/A2) | dry-run inspector 0 lost / +2 article refs; `ADVERSARIAL_REVIEW_2026-10-11.md`, `REVISION_PLAN_R5_2026-10-11.md` |
| B-53 | Public repo R-30 pushed (viewer diagnostics, figures, Appendix A, README counts and three tamper tests); CHECKSUMS regenerated | trail_check --remote 12 |
| B-52 | appendix_sync A.17 points at the 6 Oct re-run; Figures 4.1 and 5.1 redrawn (Archify, legend entries named for the thesis) | trail_check 13 |

## 5 October 2026 — review of 4 Oct (Google Doc v3): P47–P51, B-43, B-44

| ID | Change | Verification |
|---|---|---|
| P47-01 to P47-10 | His ten tracked changes applied verbatim (abstract ×3, §3.6, §4.6, §4.10 ×2, §5.7, §7.2, §7.5); docx export kept as `supervisor_review/review3_JF_2026-10-04.docx`, comments as `review3_gdoc_2026-10-04.json` | Each located uniquely in the source by its preceding context |
| P48-01 to P48-13 | Sammendrag aligned; counts out of §6.1/§7.2, labelled in §5.1; ten-year permit note (§5.4); Corollary 1.2 a conditional extension in §1.2, §1.4, §2.9, §4.6, §6.1; Rival 4 restated on the log; 'status quo' out of §4.7 | Inspector: two losses declared |
| P49-01 to P49-17 | Patient link kept and argued (Option A, EHDS Art 9(1)–(2), verified on a mirror of the OJ text, T-14 to confirm); payload by source, necessity per class, Corollary 2.3; Art 17(3)(d) and Art 71; Semantics I anchored in OpenNCP (khypponen/openncp c8a82d8; Sundhedsdatastyrelsen/ehdsi 61094e6, OpenNCP 9.1.0 schema); redactable/chameleon-hash prior art (7 references verified by a separate agent); unimplemented parts named in §4.12 and §7.1 | OpenNCP claims re-checked in the clones: schema columns, 'audit messages cannot be modified', no retention/purge in audit code |
| B-43 | `z3_check.py` (bounded SMT check of Propositions 1–3) with copies, recorded output, run_all step 6, requirements; trail_check COPIES and appendix_sync BLOCKS extended | 9/9 checks unsat; sanity sat; off-by-one mutations of Proposition 3 refuted; 0.2 s |
| P50-01 to P50-14 | Appendix A.23/A.24; the SMT result in §3.6, §5.5, Table 5.1, §5.8, §6.7, §7.2, Statement of Contribution, roadmap | appendix_sync 15/15 |
| P50b-01 to P50b-01 | A.24 note: Z3 version as installed (5.1.0); sanity check described correctly | — |
| P53-01 to P53-23 | PRES-2: section hooks and sentence splits in Ch4 (§4.1–4.11) and Ch6 (§6.1, 6.3, 6.4, 6.6–6.8, 6.12); M6a: SPUHiN draft (2024) P13, P14, P24, P31 quoted in §4.11 and two rows in Table 4.1 | Inspector: 0 lost; SPUHiN draft read 5 Oct at the helsedata.no URL in the reference list |
| P54-01 to P54-07 | R3-FIT: §2.7 three paragraphs (CSCMP definition; Nahmias 1982 perishable inventory and Proposition 3; Elhub retention per category); §1.5 IEA energy line; four references. R3-PRL: politiregisterloven reference records the consolidated text checked | CSCMP FAQ and Elhub page read 5 Oct; Nahmias via Crossref; IEA executive summary; Lovdata text supplied by the author |
| P55-01 to P55-02 | Figure 4.1 (mechanism at the audit boundary, §4.8) and Figure 5.1 (artefact modules and data path, §5.2), drawn with Archify; HD PNG at 3x in `figures/`, interactive HTML and candidate JSON in `.archify/` and `demo_app/assets/` | Archify finalize: validate, deliver, strict check and browser check pass for both; page render checked in the PDF |
| P56-01 to P56-24 | Independent audit of 5 Oct: §4.1 hook no longer puts the ten-year floor and the ceiling on one record; P31 and Table 4.1 SPUHiN rows stated at their grade; Elhub quote limited to undisputed words with translation; Prop 3 idiom includes L ≤ F; SPUHiN scope sentences mention logging (§2.6, §6.8); §6.8 hook dated; §4.7 and §4.12 cross-reference/attribution; line counts 534/414; 'six further modules'; Figure 4.1 caption | Auditor report (subagent, 5 Oct); figures redrawn and re-finalized with Archify |
| P56b-01 to P56b-01 | §1.2: SPE extension stated with both conditions (R3-M5 evidence) | — |
| P57-01 to P57-06 | Demonstration viewer redesigned: eight pages, record life strip, live Figure 4.1 with the acting components lit per month, both Archify diagrams embedded; presentation split into `ui.py`. Appendix A.14 describes the viewer instead of listing it (never a source of results); A.1/A.2 and Table 5.1 updated; requirements `streamlit>=1.50` | Every page loaded headless with no exception; Thesis run page asserts 'Matches the thesis'; robustness page 'Both implementations agree' |
| B-48 | appendix_sync: A.14 block removed (viewer no longer listed) | appendix_sync 14/14 |
| P57b-01 to P57b-02 | `demo_app/app.py` rewritten as the eight-page viewer (logic of the six former tabs unchanged); `requirements.txt` streamlit>=1.50. New file `demo_app/ui.py` (presentation only) and `demo_app/assets/` (Archify diagrams), `.streamlit/config.toml` theme | Same checks as P57 |
| B-49 | Public repository R-28 pushed (viewer redesign, Archify assets, Appendix A synced); CHECKSUMS.md regenerated for every tracked file; docx and tracked docx rebuilt | trail_check --full --remote: checks 11–14 pass; repository app tested from its root, all pages, Synthea invariance holds |
| P58-01 to P58-18 | João 6 Oct (comment to Arshad): salted commitment to the patient link in every log leaf; integrity() checks the held link opens it; link salt destroyed with the link; third tamper test (link altered) in main(). Same edits on both copies | Run: 95/90/39/138 unchanged; 200/200 verify; all three tamper tests fail; log root changes to a91c0793… |
| P58b-B01 to P58b-B01 | A.10 synced | appendix_sync |
| P58b-B06 to P58b-B06 | A.16 synced | appendix_sync |
| P58b-B09 to P58b-B09 | A.18 synced; together: Appendix A.10, A.16, A.18 synced to the new checker and its recorded runs | appendix_sync 14/14 |
| P58c-01 to P58c-05 | Viewer Thesis run page: third tamper test and self-check | Headless run: 'Matches the thesis' |
| P58d-01 to P58d-01 | Viewer text: leaves hold a salted link commitment | — |
| B-50 | Recorded runs trf_output.txt and expected_delta_witness_output.txt regenerated (root, third tamper line); Figure 5.1 relabelled (eight pages, three tamper tests) and re-finalized; build_docx --pages caches contents page numbers from a LibreOffice render, so the contents show numbers, not '#' | trail_check 11 6/6; Archify gates pass; contents checked against the PDF (4.8 → p. 88) |
| B-51 | Synthea pinned: bundles record commit d9d07a6 (verified on GitHub); the September cohort regenerated with that jar under the same seeds and -r 20260916: same patients but one, same events, constant time-of-day shift, no byte-identical bundle; 'deterministic, byte-identical' claim corrected in the subset README and Data_Provenance_Statement; full-cohort comparison re-run with the final code (`results/synthea_comparison_full_cohort_rerun_2026-10-06.txt`: six measures identical, 200/200 commitments differ, mean 1,002 bytes). Public repo R-29 pushed | Thesis prose (Ch3 §3.5, Ch5 §5.8, Appendix A) to follow with João's 6 Oct docx |
| B-47 | trail_check check 10: ID pattern covers R3-* and suffixed IDs; WAITING status; any unparsed row fails. Tracker: stale evidence fixed (M4c, M4d, MIN-01, M2b/M2c 'Proposition 4'), R3-AI back to OPEN | Check 10 now sees 53 rows |
| P51-01 to P51-04 | Ch2 repetition of Ch1 cut (renumbering note, scenario, SecuPi); §6.11 limitations list replaced by a pointer to §3.7 | Inspector: losses declared (stated in §1.2, §1.4, §3.7) |
| B-45 | `z3_check.py` corrected after the independent check: Proposition 2 now encodes Semantics II in full (m_acc, c, iota, beta, iota_subj; C3 on beta), with three mutations of the construction that must be refuted; bounds widened to F ≤ 120 and H = 140 so the cross-border floor is covered; copies and recorded output refreshed | 9/9 unsat; all mutations sat; 0.9 s. The first version's Proposition 2 check was a tautology for C1 (found by the independent check) |
| P52-01 to P52-38 | Independent check of 5 Oct: his Rival 4 text restored verbatim; patient-link argument bounded (who holds the Art 9 duty, the years beyond Art 9(2), SPE); Option A in the Statement of Contribution, §7.1, §7.5; Corollary 2.3 as an extension, 'argument of Proposition 3', other exits named, §3.7 updated; Proposition 2's SPE premise in §4.12, Ch1; §6.2/§7.4 dependency statement accurate; OpenNCP claims tied to the 2017 source and the 2026 schema, 'verification' answered (sender signs, repository does not verify); Z3 paragraph moved below the scaled-floor paragraph and rewritten; §5.1 consistency; Ch7 unimplemented list; cross-references; TOC A.23/A.24; 'independent' → 'separately written'; Proposition 3 'only if' in §7.1; 'personal-data payload' → 'payload'; Ch2 causal claim hedged; Ch3 status-quo wording | Signing and repository non-verification spot-checked in the 2017 clone (AuditTrailUtils.java:1048–1050; no signature validation in openatna) |
| P52b-B01 to P52b-B24 | Appendix A.23/A.24 synced to the corrected module and output; A.2 line count (P52b-01) | appendix_sync 15/15 |
| P52b-01 to P52b-01 | A.2 line count 153 | — |
| B-46 | Public repo R-27 pushed (398d62b): z3_check.py, recorded output, Appendix A, README; CHECKSUMS copied back | GitHub API head 398d62b; Z3 output identical to the recorded run |
| B-44 | `build_tracked.py --base <commit>`: tracked comparison against the version he reviewed (aa86290) | — |

## 4 October 2026 — fix round after the independent audit (P42–P46)

| ID | Change | Verification |
|---|---|---|
| P42-01 to P42-39 | M4a "propositions rather than theorems"; M2a ceiling = electronic health data at every site, §6.2 consistent with Rival 6, §5.4 notes relocation; M5a ten-year floor as reported and illustrative everywhere; M5c Art 73(1)(e) verbatim (OJ wording recorded in DECISION_RECORD at primary source, matching D7.4's quotation p. 51); M1a SPE payload fields and D7.4 OPR-17; M1b Semantics I without the current-practice claim | Inspector: one hedge declared (the removed practice claim) |
| P43-01 to P43-31 | Cuts and pointers: §1.1 pilot detail to §2.2; §1.4 overreach; §2.3 to §4.6; §2.4 ZK paragraphs compressed; §2.7 OECD and seafarer material cut (Norwegian Maritime Authority reference removed); process residue (§2.1.4, §2.9, §5.7, §6.8, Declaration); §4.9 duplicate; Ch5 header discloses the 28 Sept full-cohort run; §5.2 stale 35 bytes and Synthea payloads as stand-ins (M1c); §5.3/§5.4 rate interpretation removed (M4d); §6.9 MiFID duplicate; Appendix C C.1a folded, §3.9 reference, header | Inspector: each loss checked and declared in the patch (details stated elsewhere, or cut material) |
| P44-01 to P44-15 | Checker header without patch IDs or review references (three copies); FLOOR_XBORDER comment illustrative; Appendix A date, module and component counts, A.16 claim, A.17 intro; README_repo Propositions, 533 lines, current commitment, 43 bytes | Checker output byte-identical to the recorded run |
| P44b-B01 to P44b-B13 | Appendix A.10 listing synced to the checker | appendix_sync 13/13 |
| P45-01 to P45-09 | Remaining meta phrases (§1.5, §2.1.7, §4.1, §6.8); §4.6 and §4.10 headings name Propositions 3 and 4, TOC follows | — |
| P46-01 to P46-03 | Synthea limitations stated once (§3.5); §5.8 and §6.7 point there | Inspector: losses declared |
| B-42 | Public repo R-26 pushed (b8b90bf): checker header, Appendix A, README commitment; CHECKSUMS copied back | GitHub API head b8b90bf; checker output byte-identical |
| B-41 | Tracker updated: 33 closed, 3 partial (M4d length, M5c language version, M6a SPUHiN row by row), 4 open (Tiger's) | Body text 44,690 words (45,605 before the round) |

## 4 October 2026 — Word build and tracked-changes comparison (B-39, B-40)

| ID | Change | Verification |
|---|---|---|
| B-39 | `handoff_tools/build_docx.py` replaces the bare pandoc call (Tiger: tables unruled, code unreadable, no page structure). Title page; every chapter, appendix and front-matter part on a new page; contents and list of tables with clickable entries and PAGEREF page numbers; tables with thin rules, shaded repeating header row, 10 pt, rows not split; captions bold-labelled, kept with their table, bookmarked; 446 clickable cross-references (Table X.Y, Section N.M, §N.M, Chapter N; the Joint Action's own tables excluded); code in bordered shaded Consolas 8.5 pt with token colours; references with hanging indent; A4, 2.5 cm margins, page numbers in the footer, none on the title page. Text unchanged | OOXML validation clean (pandoc's math and numbering ordering faults repaired); rendered to PDF (LibreOffice Math installed so equations render) and pages inspected: title, contents, Table 4.1, Table 5.3, Proposition 3, code listing |
| B-40 | `handoff_tools/build_tracked.py`: `VERA-SNARK_Thesis_TRACKED_vs_30Sept.docx`, the front matter and Chapters 1–7 against the draft he reviewed, as word-level tracked insertions and deletions under the author's name | OOXML validation clean; 319 paragraphs unchanged, 267 revised, 79 new, 93 removed (before the fix round); rendered and inspected |

## 4 October 2026 — independent audit against the 30 Sept review

| ID | Change | Verification |
|---|---|---|
| B-38 | A separate agent audited every point of the emailed review against the current text and code, without trusting the tracker. Nine items marked CLOSED were found only partly done (M1, M2a, M4a, M4d, M5a, M6a, M7a, PRES-3, PRES-4) and M5c's note was wrong. Tracker statuses corrected to PARTIAL with the audit's finding in each row | Key findings spot-checked: 'propositions rather than propositions' in Ch4 §4.7; no verbatim Art 73(1)(e); 'Theorems' in README_repo; body text 45,605 words |

## 4 October 2026 — patches P38–P41 (numbering, app, Appendix A, TOC) and B-36

| ID | Change | Verification |
|---|---|---|
| P38-001 to P38-120 | MIN-13: §5.5a→5.6 (5.6→5.7, 5.7→5.8); §6.9a→6.10 (6.10→6.11, 6.11→6.12); Chapter 5 tables in order of appearance (5.0a, 5.0, 5.1, 5.2, 5.2a, 5.3, 5.4 → 5.1–5.7); Appendix A sections in order of appearance (A.1b, A.2b, A.9b–e, A.11b gone; A.1–A.22). Every reference in prose, appendices, code docstrings, app labels, run_all.sh and the repo README follows. D7.4's own tables untouched | Generated and frozen (`P38_renumber.edits.json`); a check found no D7.4 table reference altered; 13/13 Appendix listings still equal their files |
| B-36 | `appendix_sync.py`: BLOCKS keyed by the new Appendix A headings | 13/13 equal |
| P39-01 to P39-12 | Streamlit app: Tab 1 shows integrity (200/200) and both tamper tests and includes them in the match check; Tab 5 runs the AES-256-GCM module (138 refused, 62 read); new Tab 6 explores Proposition 3 with Art 68(12) and politiregisterloven § 17 presets; Corollary 1.2 label conditional; cross-check label corrected (§5.5, was §5.4); deprecated `use_container_width` replaced; requirements streamlit>=1.45, cryptography>=42 | Run headless with `streamlit.testing.v1.AppTest`: no exceptions; Tab 1 success message with 95/90/39/0, 200/200, both tamper tests fail; crypto 138/62; Tab 6 all three presets render |
| P40-01 to P40-05 | Appendix A.14 listing synced to app.py; Appendix A, Ch5 Table 5.1 and repo README: six tabs, 671 lines | appendix_sync 13/13 |
| P39b-01 to P39b-02 | `use_container_width` replaced by width="stretch"; requirements streamlit>=1.45, cryptography>=42 | AppTest re-run: no exceptions |
| P40-B01 to P40-B13 | Appendix A.14 listing block synced to app.py (block edit built by appendix_sync, frozen) | appendix_sync 13/13 |
| B-37 | Public repo pushed: R-24 (`docs/VERSION_RECORD.md`, b99aa5f) and R-25 (app, checker docstrings, requirements, README, Appendix A; 94b099f). `CHECKSUMS.md` copied back | GitHub API shows 94b099f as head of main; checker and δ-witness output byte-identical to the recorded files |
| P41-01 | MIN-13: Table of Contents regenerated from the headings, every numbered section listed | Generated and frozen |

## 4 October 2026 — patches P32–P37 (D7.4 pages, cross-chapter links, references) and B-35

| ID | Change | Verification |
|---|---|---|
| P32-01 to P32-10 | D7.4 page numbers made the printed page throughout (EHDSR-6/7/8 p. 31; OPR-8 p. 46; OPR-17/18 p. 51; Annex 7 p. 96; OPR-6 p. 43 unchanged). The earlier p. 32/47/52/97 were PDF indices | Each passage located in the uploaded PDF (`sources/TEHDAS2_D7.4_v1.2.pdf`, added) with pdftotext; printed number read from the page header |
| P33-01 to P33-18 | Ch4: four propositions announced (§4.1); key hierarchy anchored in NIST SP 800-57 and SP 800-38D and tied to `crypto_envelope.py`; SP 800-57 §7.6 for the invalidation record; new *Tamper evidence* paragraph (Schneier & Kelsey 1999, Merkle 1988, Crosby & Wallach 2009, RFC 6962) with the design point that the log never holds what erasure reaches; auditor's view adds integrity; §4.9 leaf-hash residue and per-entry nonce (new finding); consistency proofs named, not implemented; §4.11 placement in D7.4 Figure 5.13 (p. 60); Table 4.1 key-hierarchy row corrected; §4.12 six rivals, Props 3–4, the log | Inspector: lost 0, gained 5 citations. Leaf contents checked in `_creation_entry()`: accessor fields, t_a, commitment; no payload, no subject field. References verified by a separate agent against Crossref/RFC Editor/NIST/USENIX |
| P34-01 to P34-08 | Ch2 §2.4: tamper-evident logging strand set against KONFIDO's immutability-vs-erasure tension; Boneh & Lipton (1996) as the origin of crypto-erasure; stray duplicated URL line removed | Inspector: lost 0, gained 6 citations |
| P35-01 to P35-18 | Ch6: meta cut (6.1, 6.2, 6.10); §6.1 count conflation fixed; mechanism list and status level with Ch4; D7.4 OPR-6 and Annex 7 as corroboration (§6.2); §6.3 log, SP 800-57, FIPS 140-3, envelope-encryption result; §6.5 Merkle scaling and log-vs-accumulator; §6.7 repetition of Ch5 cut; §6.8 Proposition 3 as drafting test, TEHDAS2 paragraph updated; §6.10 shortened, abandoned-draft mention left to the Declaration; §6.11 conditional and complete | Inspector: 2 hedge false positives declared ("has not been raised by any reviewer", "May 2026") |
| P36-01 to P36-12 | Ch7: Annex 7 open question; four propositions; mechanism as specified; contributions 2–4 level with the Statement of Contribution; zk-SNARK future work made concrete against the Merkle log (Groth 2016; PLONK 2019); generalisation updated to §6.9a and Proposition 3; closing meta cut | Inspector: 1 hedge declared (replaced sentence) |
| P37-01 to P37-13 | Ch1 and Ch3: partition, log, Props 3–4, forward links; §1.7 roadmap matches the chapters; Ch3 solver sentence replaced by the exhaustive search actually used; Table 4.1 named as the instrument of external validity; sixth limitation stated conditionally | Inspector: 2 hedges declared (the replaced solver sentence) |
| B-35 | `assemble.py`: bibliography sorted in APA 7 order (author, n.d. first, year, suffix). The old key sorted whole strings: Finck 2019 before 2018, SPUHiN 2025 before 2024, Datatilsynet n.d. after dated works | Rebuilt: 80 entries (69 before P33–P36); same-author runs checked |

## 4 October 2026 — patches P28–P31 (repetition, front matter, Chapter 5)

| ID | Change | Verification |
|---|---|---|
| P28-01 to P28-06 | PRES-4 (part 1): NCPeH pilot details (dates, scope, DPIA) said once, in §2.2; §1.1, §1.4, §2.6, §4.11, §6.8 cite (Helsedirektoratet, 2026) and point to §2.2 | patch.py inspector: no citation, number, article or hedge lost |
| P29-01 to P29-02 | PRES-4 (part 2): the Art 68(12) broad/narrow grounds argued once, in §4.6; §6.2 and §7.4 state the question and point there | inspector: lost 0 |
| P30-01 to P30-07 | Front matter level with the body: Sammendrag "teorem 1/2" → "proposisjon 1/2" (D-18); Abstract, Sammendrag and Statement of Contribution add Propositions 3–4, the accessor/patient-link partition (D-16), the tamper-evident log; Corollary 1.2 stated with both conditions (broad reading, patient-record granularity) | inspector: lost 0; figures 95/90/39/138 checked against repro_package/results |
| P31-01 to P31-14 | M4d + PRES-3 in Ch5: meta commentary cut; rate disclaimer said once (§5.3); §5.4 no longer says the reading is "adopted" (now conditional, as §4.6); Proposition 3(ii) linked where its condition is computed; "no cryptographic library" confined to the checker (crypto_envelope.py exists); closing bridge to Ch6 | inspector: lost 0, gained Art 68(12) mention |

## 3 October 2026 — patch P27 (process material)

| ID | Change | Verification |
|---|---|---|
| P27-01 to P27-09 | PRES-3: the earlier draft (unverifiable citations, ethics approval never obtained) stated once, in the Declaration. Removed or reduced: Round 0 paragraph (§2.1.4), the criterion sentence about the earlier draft (§2.1.5), the exploratory-phase limitation (§2.1.6), "Round 2 … led to its abandonment", two sentences in §3.9. The Version and Change Record (Tables F.1, F.2) removed from the front matter; its content goes to the repository as `docs/VERSION_RECORD.md` | patch.py: every declared loss lies in removed text (dates, line and equation counts, "approximately fourteen"; "may" was the month in "May 2026"), listed from the dry run and checked |

## 3 October 2026 — patch P26 (meta-commentary)

| ID | Change | Verification |
|---|---|---|
| P26-01 to P26-47 | PRES-1: the detector widened to 16 phrase families (84 matches in 74 sentences); every sentence read; 47 cut or shortened across the front matter and Ch1–7. Kept where the phrase carries argument (Datatilsynet's "deliberately high threshold", the NCPeH's "deliberately narrow" scope, "honest key destruction" as the trust assumption, Aikebaier's interpretation "rather than asserted as a regulatory requirement"). Two substantive fixes found while reading: §4.10 said every rival is rejected, but Rival 6 is accepted for the ceiling; §6.9a's diagnostic question restated to agree with Proposition 3 | Meta-commentary 84 → 31 (−63%; the supervisor asked for at least half). patch.py: one declared loss ("may", inside "an examiner may read it either way") |
| B-33 | Guard PRES1 widened to the 16-family pattern, baseline 84, goal 42 | Now 31 |
| B-34 | `trail_check.py` check 8 compared the replayed draft line without normalising it; a patch deleting a whole sentence leaves a double space, so four lines read as unexplained after P27. The replayed line is now normalised before comparison | Check 8: 0 unexplained |

## 3 October 2026 — patch P25 (witness lines)

| ID | Change | Verification |
|---|---|---|
| P25-01, P25-02 | MIN-10: §5.3 and §5.4 witness lines were quotation lines labelled "verbatim" but typographically altered (⇒, α, →). Now code blocks, one line per witness, copied from the recorded run | Lines 17–19 and 22–24 of `repro_package/results/trf_output.txt` |
| B-32 | T-10 (German Art 68(12)) attempted: streamlex has no German page; the Council's German PDF arrived truncated. Left to Tiger (EUR-Lex multilingual display) | Research log row 38 |

## 3 October 2026 — D7.4 and the Union Customs Code read in full (Tiger's T-1, T-2), patch P24

| ID | Change | Verification |
|---|---|---|
| B-30 | `sources/TEHDAS2_D7.4_v1.2_2026-02-24.md` and `sources/UCC_Regulation_952_2013_OJ_text.md` added: the two texts Tiger supplied, kept so every quotation can be checked against them | Research log rows 36–37 |
| P24-01 to P24-08 | Table 4.1: D7.4 page numbers (EHDSR-6/7/8 p. 32; OPR-6 p. 43; OPR-8 p. 47; OPR-17/18 p. 52) and three new rows (tamper protection, proportionate logging, OPR-6's own "balance"). §4.6: EHDSR-7 page. §4.8: OPR-6 quoted in full; the specification asks for a balance between deletion and retention and leaves its form open. §4.10 Rival 3: OPR-17 quoted; no granularity requirement anywhere in D7.4. §4.3: OPR-18 five-year recommendation, with Proposition 3 and Corollary 2.2. **Corrections:** Ch1 §1.4 and Ch2 §2.9 said the review found "no treatment" of the collision "including in the guidance published by the Joint Action"; D7.4 asks for the deletion–retention balance and its Annex 7 names "open questions about how accountability and anonymisation obligations intersect". Both passages now say so; Ch2's "no interpretive work by this author" removed (the collision is conditional since D-16) | patch.py: one declared loss ("inspected", the hedge on a claim now checked against the full text). Three fetch errors from 3 Oct corrected in the research log (p. 31→32, p. 19→20, five-year recommendation kept in the final) |
| B-31 | TIGER_TASKS T-1 and T-2 marked done | — |

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
