# Viva Preparation Notes (updated 20 November 2026)

**Thesis:** *Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the European Health Data Space*
**Candidate:** Arshad Akhtar Abbasia, MSc Sustainable Energy Logistics, HiMolde (LOG953)
**Format:** 15-minute talk, then 30 minutes of questions. Supervisor Prof. João Ferreira; external examiner Joel Curado.
**Checked against:** `VERA-SNARK_Thesis_SUBMISSION.md` as patched on 19 November (P139). Section numbers below are the ones in that file.

**What changed since the old notes (stop saying these):**
- There are no "Theorems". They are Propositions 1 to 4 (§4.1, §4.7 note: "stated as propositions rather than theorems").
- The cross-sector test is §6.10, not "§6.9a".
- "Four results proved" is wrong. Three proved (Props 1 to 3), Prop 4 argued from a stated legal premise (§1.5, §4.1, §7.1).
- Prop 1's ceiling disjunct only applies to records the ceiling reaches (σ = secondary, ρ = 1) (§4.6 scope sentence).
- The exhaustive search is a sanity check, not "the strongest kind" of evidence (§5.5). The bounded Z3 check carries robustness.
- "Cannot be rewritten without detection" holds only once a root containing the entry has been published outside the log (§6.3). Root publication and consistency proofs are specified, not implemented (§4.9, §5.7).

---

## 1. Numbers you must say right

| Figure | What it is | Where |
|---|---|---|
| 200 records | 100 cross-border (F = 120, primary) + 100 SPE access logs (F = 12, secondary) | §5.2, Table 5.2 |
| Seed 20260915 | Fixed; one code version throughout | Ch5 header, §5.2 |
| 95 violations across 90 of 200 records (45%) | Semantics I; 37 cross-border (37%), 53 SPE (53%) | §5.3, Table 5.3 |
| 41 / 44 / 5 | C2 only / C3 only / both; the 5 "both" are all SPE, so 95 = 90 + 5 | §5.3 |
| 38 requests, 37 inside, 1 outside | Cross-border; the one outside the window is the case Prop 1 excludes | §5.3 |
| 49 + 4 = 53 | SPE violators: ceiling-driven + request-only | §5.3 |
| 39 of 78 | SPE records with no erasure request that still collide (Corollary 1.2, broad reading, ρ = 1) | §5.1, §5.4 |
| 22 SPE requests, 9 inside the window (4 + 5) | What survives under the narrow reading; the 44 ceiling-only collisions lapse | §5.4 |
| Record 100 | t_a = 7, permit expires 10, C3 from 16, C1 to 19, collision at 16 | §5.4, Figure 5.2 |
| 0 / 200, 0 violations | Semantics II | §5.7, Table 5.6 |
| 138 invalidated = 52 + 86 | 52 on GDPR Art 17(1), 86 on EHDS Art 68(12); 4 same-month cases recorded under Art 17(1) | §5.7, Table 5.6 |
| 678ade47c1e6dc03... | Commitment c(a) of record 100 in the auditor view; actor R-008, permit DP-015, invalidated month 16 | §5.7 |
| 200 / 200 verify; 3 tamper tests fail | Altered accessor field (rec 100), altered invalidation ground (rec 100), altered patient link (rec 3) all make V^II fail | §5.7, Table 4.1 |
| δ = 3: 89 / 94 / 39 / 138 / 0 | One record moves out of violation; Cor 1.2 count unchanged | §5.6, Table 5.5 |
| 2^14 = 16,384 per case, 4 cases | Exhaustive search, horizon 14 months, cross-border floor scaled to 12; 65,536 in all, 65,535 evaluated | §5.5, Table 5.4, §5.8 |
| 9 of 9 Z3 checks, no counterexample | Bounds: creation 0 to 12, floor 1 to 120, δ 1 to 3, horizon 140, ceiling 1 to 120; four broken variants refuted | §5.5, A.24 |
| 98 bundles; 43 / 891 / 1,002 bytes | Synthea cohort (2 of 100 not exported); mean payload constructed / 8-bundle subset / full cohort | §5.2, §5.8 |
| 200 / 200 commitments differ, 0 figures change | Payload-independence test | §5.8, Table 5.7 |
| 138 refuse, 62 read | Optional AES-256-GCM module after scheduled destructions | §5.8, §6.3 |
| 601 lines, 466 non-blank, about 100 of constraint logic | `trf_checker.py`; standard library only | §5.2 |
| 8 Python files; app.py + ui.py 1124 + 217 | Line counts are for release 1.3.0; current viewer is 1126 + 233 | Table 5.1, A.14 |
| 56 tests, Python 3.11 to 3.13, 31 cross-check cases | 7 of 8 recorded runs re-run byte for byte; A.17 needs the uncommitted cohort | A.2 |
| Release 1.3.0, DOI 10.5281/zenodo.23989242 | The cited artefact; its viewer quotes Prop 1 without the scope sentence | A.1 |
| Release 1.3.1, DOI 10.5281/zenodo.24148156 | Carries the scoped Prop 1; no computed figure changed | A.1 |
| Release 1.3.2, DOI 10.5281/zenodo.24399784 | What the live app runs (20 Nov); no computed figure changed | CODE_REVIEW.md |
| Concept DOI 10.5281/zenodo.23819274 | All versions | A.1 |
| Floors 72 / 120 / 36 / 12 months | Norwegian pilot / illustrative literature value / Art 9(2) from 2029 / SPE Art 73(1)(e) | §4.3, Nomenclature |
| δ = 1, extended 3 | GDPR Art 12(3) | §4.4 |
| 60 records, 7 violate, 0 without a request | politiregisterloven § 17 (floor 12, ceiling 36, same anchor) | §6.10 |
| 6 / π_max; about 1 in 10 | Cor 1.2 rate for a five-year permit, instead of the generator's one half | §5.4 |
| 2 principal steps + 4 subsidiary premises | Without regulatory authority | §3.7, Abstract |
| 8 limitations; 6 rival designs | | §3.7; §4.10 |
| 26 Mar 2027 / 26 Mar 2029 | Implementing acts due (Art 73(5)) / Arts 68 and 73 apply | §1.2, §6.8 |
| 23 Sep 2026; 19 Oct 2026 | Datatilsynet enquiry sent, no reply at submission; Helsedirektoratet answered on the floor | §7.4 |
| 32 SAs, 764 controllers | EDPB CEF report on Art 17 (Feb 2026) | §1.4 |

Say "in the model" and "generated" every time a count leaves your mouth.

---

## 2. Words to use, words never to use

| Use | Never | Why (section) |
|---|---|---|
| "attested" destruction | "proven" or "verified" destruction | §4.7, §6.3: the entry is an attestation, not a proof |
| "pseudonymised" residue | "anonymous", "anonymised" | §4.9: for the repository controller it remains personal data (C-413/23 P) |
| "proved" for Props 1 to 3, "argued" for Prop 4 | "four results proved" | §1.5, §4.10 |
| "in the model", "within the model" | "the law requires", "is lawful" | §4.7 "does not establish that the exhibited solution is lawful" |
| "tamper-evident" | "tamper-proof", "immutable" | §4.9, SoC 4, §7.2 |
| "published root: specified, not implemented" | "the log cannot be rewritten" (unqualified) | §5.7, §6.3, Table 4.1 |
| "synthetic", "Synthea-generated" | "real FHIR data", "realistic frequencies" | §5.8, §6.7 |
| "counts set by the generator", "not frequency estimates" | "45% of records violate", "half of research logs collide" (as facts) | §5.3, §5.4, Abstract |
| "on the broad reading, for logs at patient-record granularity" | Cor 1.2 without its condition | §4.6 |
| "a defensible reading", "argued, not confirmed by any authority" | "the reading the law requires" | §3.2 Step 3, §4.2, §6.2 |
| "sanity check" (exhaustive search), "separate code" | "independent verification" | §5.5 |
| "simulated in program memory" | "keys destroyed" (unqualified) | §5.2, §5.8 |
| "the Board recognises key deletion makes data unintelligible" | "the EDPB endorses crypto-erasure as erasure" | §1.4, §4.9: still personal data |
| "the 2017 OpenNCP reference source" | "deployed repositories behave this way" | §4.5 |
| "Verifiable qualifies the invalidation record" | "erasure is verifiable" | §1.4 |
| "no optimisation, no objective function" | "a logistics optimisation model" | stated defence, §2.7 |

---

## 3. Twelve hard questions, model answers

Rule: first sentence is the concession, second is what survives.

### Q1 (Curado). "Can the operator rewrite your log? Merkle trees give you nothing without published roots."

"Correct, and the thesis says so. The artefact recomputes the root from the leaves the log itself holds, so it detects divergence between a record and its logged events, and that is what the three tamper tests show. It does not detect a rewrite of the whole log. That needs roots published or countersigned outside the log, and consistency proofs between an earlier root and the current one, as Certificate Transparency does. Both are specified and not implemented. So the claim is tamper-evident against a published root, not tamper-proof, and that is the wording now in the contribution statement."

Point to: §5.7 (last paragraph), §4.9 trust assumptions, Table 4.1 tampering row.

### Q2 (Curado). "Why not just put this on a blockchain?"

"Because the problem is not where the log lives but what an entry contains. KONFIDO used blockchain auditing on OpenNCP and left the immutability-versus-erasure conflict unresolved, because personal data went into the chain. Redactable chains solve it by giving someone power to rewrite history. I take the other route: the log is never edited, and erasable content never enters it. Leaves hold accessor fields, the payload commitment and a salted commitment to the subject link. The thesis also argues the tri-lateral conflict cannot be dissolved by any storage choice. A public ledger could be one place to publish roots; I did not specify or evaluate that."

Point to: §2.4 (KONFIDO, redactable designs, Finck distinction), §4.8 Tamper evidence.

### Q3 (Curado). "How do you prove a key was destroyed? What does an HSM actually give you?"

"I cannot, and nobody can by inspection from outside. The invalidation entry records who destroyed which key, when, on what legal ground, with a hash of the key identifier, and binds that claim into the log. An auditor can check the claim was made; not that it is true. A FIPS 140-3 validated module places destruction inside a tested boundary, but validation attests the module's design, not any particular destruction. In my artefact the custody object stands in for the HSM, so destruction is in program memory. The AES module shows unreadability follows from destruction, not that destruction happened. Proof of secure erasure is future work."

Point to: §6.3, §4.9 trust assumptions, §4.8 Key hierarchy, §7.5.

### Q4 (Curado). "What is your threat model? And is your commitment even hiding?"

"The thesis names five trusted parties or assumptions: the controller executes destruction when it says it did; the custody boundary keeps no recoverable key material; the log operator does not rewrite history, which is detectable only with published roots; the accumulator manager, if used; and that the hash and cipher hold over the horizon. On hiding: the design requires a random per-record salt. In the reported run the salt is derived from the record identifier so the run reproduces, which means it is not hiding in that run; `--random-salts` draws it from os.urandom. The per-leaf nonce against accessor guessing is specified, not implemented."

Point to: §4.9 trust assumptions and leaf nonce, §5.2 (salt sentence), §4.8 Commitment.

### Q5 (legal). "Does Article 68(12) really reach the environment's own access logs?"

"That reading is contestable and I state it as a condition. The provision is framed by location, 'the electronic health data within the secure processing environment', not by provenance. But its object is electronic health data, so an entry that only records a researcher opening a dataset is not reached. An entry at patient-record granularity reveals cohort membership, which is health data. On that broad reading Corollary 1.2 follows. The narrow reading confines it to the permit dataset; a harmonising reading lets the floor prevail. If the broad reading falls, I lose Corollary 1.2 and one branch of Corollary 2.3, and nothing else."

Point to: §4.6 interpretive condition, §6.2 last paragraph, §7.4.

### Q6 (legal). "Article 17(3)(b) already exempts audit retention. What conflict is left? And no regulator backs Semantics II."

"Half of that I concede: Article 17(3)(b) says necessary content survives. It does not say what that content is, and read with Article 5(1)(c) it protects only what the obligation needs. My argument is that accountability needs who, when, under what basis and with what outcome, plus the patient link where Article 9 applies, not the demographic query. That is a reading argued from the instruments; no authority has confirmed it. If an authority says identifiable logs must stay readable, Proposition 2 stays true of the model and becomes inert in practice. I asked Datatilsynet on 23 September; no reply at submission."

Point to: §4.2, §6.2, §7.4.

### Q7 (Ferreira, programme fit). "This is a logistics degree. Where is the logistics?"

"There is no optimisation and no objective function, and I do not claim one. The logistics is in the object and in one design decision. Logistics covers the flow and storage of goods and related information; an audit record is related information, and the thesis concerns its storage and planned exit. The floor is a per-record parameter, taken from chain-of-custody practice, which is why a cross-border floor and the SPE floor are one constraint. Proposition 3 is a two-clock perishability result: a record held against a floor while a deletion clock runs from an external event. Customs keeps the record after the goods are destroyed; Semantics II does the same."

Point to: §2.7, §4.3 (floor as parameter), Prop 3 in §4.6, §6.9 last paragraph.

### Q8 (Ferreira, programme fit). "Your programme is Sustainable Energy Logistics. Where is the energy?"

"There is none in the result, and §1.5 says so: no energy measurement and no energy saving claimed. The fit is the logistics of information. The nearest energy instance is Elhub, which keeps customer data for three years and 41 days after contracts end: a floor anchored to an event, the same form as my floor parameter. The floor-against-right part of the model applies there directly. Whether Elhub also has a ceiling collision is exactly the Proposition 3 test, and I have not run it. That is the first application I would take on next."

Point to: §1.5 fourth exclusion, §2.7 Elhub paragraph, §7.5 Generalisation.

### Q9 (Prop 1 scope). "Proposition 1 was restated late. Why does the ceiling disjunct need ρ = 1, and which version am I examining?"

"The ceiling constraint C3 binds only secondary records with ρ = 1, where the log entry is itself electronic health data. A proof cannot use a constraint on a record it does not bind, so the second disjunct is tested only there. Nothing in Chapter 5 moves: every SPE record is generated with ρ = 1. On versions: release 1.3.0 is the cited code and its figures; its viewer quotes Proposition 1 before the scope sentence. Release 1.3.1 carries the scoped statement. All six result modules are byte-identical across them."

Point to: §4.6 Proposition 1 and scope sentence, §4.4 C3, §5.2 SPE bullet, A.1.

### Q10 (Prop 4 premise). "Proposition 4 is not a proposition. It is an assumption with a proof attached."

"Largely yes, and the thesis says so: it is a legal argument given the form of a proposition so the premise is explicit. The premise is that a controller receiving a relocated record receives the Article 17 obligation with it. Given that, the ceiling quantifies over a location and the right over a controller, so relocation meets the first and leaves C1 against C2 exactly where Proposition 1 left it. It sits over an informal extension of the model with location and controller, and the artefact does not execute it. If the premise is wrong, Rival 6 becomes stronger; Propositions 1 to 3 are untouched."

Point to: §4.10 Proposition 4 and the paragraph after it, §3.7 sixth limitation.

### Q11 (validity of synthetic data). "Your 45 per cent and 39 of 78 are artefacts of your generator. What does the demonstration show?"

"The rates are generator outputs and not frequency estimates; the thesis says so at each table. The model treats every request as valid, which inflates frequencies, and permits are drawn from one to twelve months, which gives the one-half rate; a five-year permit gives about one in ten. What the run shows is structure: Proposition 1's conditional form reproduced, including the one request outside the window; zero violations under Semantics II; and Synthea payloads changing all 200 commitments and no figure, because no constraint reads content. Semantics II holds by construction; the integrity check is the part that can fail."

Point to: §5.3, §5.4, §5.7, §5.8 Table 5.7, §3.7 seventh limitation.

### Q12 (next). "If you had another year, what would you do first?"

"First, get the two authority answers, because no modelling replaces them: Datatilsynet on whether accountability-preserving verifiability discharges retention, and the EHDS side, Helsedirektoratet, the Ministry or the Commission, on Article 68(12) and the logs. Second, run the Appendix C panel after Sikt notification. Technically, the gaps a cryptographer would close first are published roots with consistency proofs, the leaf nonce and the terminal transition. The research problem is proving completeness of invalidation for one subject without revealing the set: that is where a zero-knowledge argument over the published root becomes necessary rather than decorative."

Point to: §7.4, §7.5, §6.1 (what is not implemented).

---

## 4. Known weaknesses: own them first

| # | Weakness | One-line honest answer | Where |
|---|---|---|---|
| 1 | Props 1 and 3 are near-immediate; Prop 2 holds by construction | "Yes. The weight is in the necessity analysis and the mechanism; Prop 1 earns its place by showing some departure is unavoidable." | §4.7 note |
| 2 | Semantics II zero holds by construction in the checker | "C2 and C3 follow from the invalidation month; the falsifiable part is the inclusion-proof check, and three tamper tests show it can fail." | §5.7, §5.8 |
| 3 | Exhaustive search is not independent | "It is a sanity check sharing two constants; the bounded Z3 check with refuted mutations carries robustness." | §5.5 |
| 4 | Checker, cross-check and Z3 written in the same AI-assisted process | "Declared. They check the code against the encoding, not the encoding against the law." | §5.5, Declaration |
| 5 | No published roots or consistency proofs | "Tamper-evident against a published root; that part is specified, not built." | §4.9, §5.7 |
| 6 | Reported run's salts are not hiding | "Derived from the record ID for reproducibility; random salts exist as an option. The design requires hiding." | §5.2 |
| 7 | Terminal transition, leaf nonce, proactive invalidation, accumulator not implemented | "Specified, not implemented; none is part of either executed proposition." | §6.1, §7.1 |
| 8 | Key destruction simulated | "In program memory; real AES-256-GCM shows unreadability, not destruction." | §5.8, §6.3 |
| 9 | Prop 4 is argued, not proved or executed | "Stated as a legal argument with its premise explicit." | §4.10 |
| 10 | Two principal interpretive steps, four subsidiary premises, no authority | "Listed in one place, put to the authorities; one enquiry sent, unanswered at submission." | §3.7, §7.4 |
| 11 | The six-year pilot floor is a controller decision | "No national legal basis identified; before 2029, and beyond 36 months after, keeping the link against a request has no secure 17(3)(b) basis. A finding for the controller." | §4.2 |
| 12 | ITI-55 identifier case | "Where an identifier is used, cross-border invalidation removes little; the demographic case is the one that bites." | §4.10 Rival 3 |
| 13 | Rival 4 is close to equivalent for cross-border | "Conceded: there the advantage narrows to the attributed, tamper-evidently bound entry; the commitment does real work in the SPE case or where an opening is handed over." | §4.10 Rival 4, §6.3 |
| 14 | Every request treated as valid; requests per record, not per subject | "Inflates frequencies, leaves the propositions untouched; no result is stated as a frequency." | §3.7, §5.2 |
| 15 | Synthea is US Core | "Profiles and content are not Norwegian; no constraint reads content, and the invariance test confirms it." | §3.5, §5.8 |
| 16 | Semantics I evidenced by one reference implementation | "2017 OpenNCP source and the 2026 schema; other deployments not inspected." | §4.5 |
| 17 | Which code: 1.3.0 cited, later viewer hosted | "Figures from 1.3.0; viewer wording changed in 1.3.1 and 1.3.2, which the app runs; result modules byte-identical." | A.1, CODE_REVIEW.md |
| 18 | Full-cohort run (A.17) not re-runnable from the repo | "Seven of eight recorded runs re-run; A.17 needs the uncommitted 98-bundle cohort." | A.2 |
| 19 | Evaluation is artificial, not naturalistic; panel not executed | "Designed in Appendix C, needs Sikt notification; utility and acceptance are not evaluated." | §3.8, §6.6 |
| 20 | No optimisation in a logistics thesis | "Conceded; the fit is the object, the per-record floor parameter and Prop 3." | §2.7 |
| 21 | SPUHiN hearing page withdrawn; final D5.2 not checked | "Stated as an exception in the Declaration; absence observed in the hearing version only." | Declaration, §1.2 |

---

## 5. Thirty-second answers

**Summary of the contribution.**
"Cross-border health audit records face a retention floor, the right to erasure and, in research environments, a six-month deletion ceiling. I model the three as constraints over one variable: can the payload still be read. If verifiable means readable, the system is infeasible whenever a deadline the record is bound by falls inside its window. If verifiable means the accountability fields, a commitment and a logged invalidation are intact, it is satisfiable for every pattern and every floor. The proof's trajectory is the mechanism: delete payload and key, keep the accessor fields, log the invalidation in a tamper-evident log. All of this is in the model, not yet in law."

**What is novel.**
"Not the cryptography and not the method. Formalising compliance as satisfiability is established, and crypto-shredding is practice. What is new in the reviewed literature is applying it to a floor, a right and a ceiling together, isolating verifiability as the parameter that decides feasibility, and Proposition 3: a ceiling collides with a floor only if it is no longer, and the anchor decides whether you can see the collision in the text. Plus a mechanism whose residue is analysed and placed against Norwegian infrastructure."

**Limitations.**
"Three that matter. The central interpretive move, that an invalidated record still discharges retention, has no authority behind it, and nor does the broad reading of Article 68(12). Key destruction is attested, not proven, and in my artefact it is simulated. And the proofs are informal, the demonstration is synthetic, and the counts come from the generator. Published roots, the terminal transition and the accumulator are specified, not built."

---

## 6. Before the defence

- G21: the old notes are in `process/` on a public branch. Make the repository private or move them out before the examiners open the link.
- G20: open https://trfhimolde.streamlit.app/ the day before and confirm it shows the scoped Proposition 1; screenshot the claim ledger as a fallback.
- Have the repository, `docs/expected_trf_output.txt` and the live app open. If a number is challenged, run it.

## 7. Could not verify

- Defence date: memory gives a window of 3 to 14 December 2026; the old notes said first week of December. Not checked against any confirmed schedule.
- Whether Datatilsynet has replied since submission (thesis §7.4 says no reply at submission).
- Zenodo record contents for 1.3.0 and 1.3.1 (proxy blocked; DOIs checked only against repo files, per CODE_REVIEW.md).
- The live app's current state (G20).
- Open citation items not re-checked: Rak (2024) page 928 (§2.3, G17), TEHDAS2 (2026a) Section 7.2 page (§1.1, §2.3, G18), reference-list items in G19.
- SPUHiN P13 exact wording ("tamper-proof"): SPUHiN source text is not in the repository.
- I did not re-run the tests or the checker; the 56 tests and byte-identical runs come from review_audit_report.md and CODE_REVIEW.md, and all figures above were checked against the thesis text only.
- Q2's remark that a public ledger could host published roots is my framing; the thesis does not say where roots are published.
