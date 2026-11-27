# Part C. Question bank

For: Arshad Akhtar Abbasia (Tiger). Examiners: Prof. João Ferreira (supervisor) and Joel Curado (external). Thirty minutes of questions.

## How to use this part

**Format of each entry.** The question as an examiner would phrase it, tagged with the likely asker. Then: **Short answer** (say this first), **Full answer** (the reasoning, for you and for a third reader), **Worked example** (a real record or number from the checker where it helps), **Concede and hold** (what to admit, and the line to keep), **Point to** (thesis section and printed page, deck slide, app page).

**The doctrine for every answer** (from the red-team notes):
1. Concede the true part first, in one sentence.
2. Bound it: say exactly how far the concession reaches and what still stands.
3. Point to where the thesis already says so. Never improvise a new claim under pressure.
4. Never overclaim: "attested", not "proven"; "pseudonymised", not "anonymous"; "in the model", not "the law requires".
5. Redirect to the weight-bearing walls: the necessity analysis (§4.2) and the mechanism (§4.8), not the proofs.

**Conventions.** Thesis pages are printed pages of the submitted PDF (PDF page minus 14). "Slide n" is the deck position (talk 1 to 16, backup 18 to 31). App links start from https://trfhimolde.streamlit.app/ . "Part B, section Bx" points to the section of Part B (B_explainer.md) chapter by topic. Items marked "not in the thesis" come from the repository, the correspondence or the article workstream, and the examiners have only the thesis: say where they come from.

**Code state.** Figures below were re-run for this part from `/home/claude/trf` at release 1.3.4 (the thesis cites 1.3.0). `python3 trf_checker.py` matches `docs/expected_trf_output.txt` byte for byte; `z3_check.py` gives 9 of 9 no counterexample; `crypto_envelope.py` gives 138 refused, 62 read; `cross_sector_check.py` gives 60 records, 7 violate, 0 without a request; the test suite passes (63 tests at 1.3.4; the thesis says 56 at 1.3.0).

**Index.** Q1 to Q3 motivation and timing. Q4 to Q6 method. Q7 to Q13 legal reading. Q14 to Q20 model and propositions. Q21 to Q28 mechanism and cryptography. Q29 to Q33 evidence and validity. Q34 to Q37 Norway. Q38 to Q39 programme fit. Q40 to Q41 novelty and competitors. Q42 to Q46 hostile and meta. Then: numbers, words, weaknesses, 30-second answers, the 60-second and 20-second theses, the checklist.

---

# 1. Motivation and timing

### Q1. [Either] "Why this problem, and why now? The rules do not apply until 2029."

**Short answer.** The timing is the argument. The detailed rules for research environments are due in March 2027 and apply from March 2029, and Norway's cross-border system is already in pilot, so the clash can be settled in the specification rather than patched after infrastructure hardens.

**Full answer.** Regulation (EU) 2025/327 entered into force on 26 March 2025 and applies generally from 26 March 2027 (Art 105). The secondary-use provisions of Chapter IV, which contain both the Art 68(12) ceiling and the Art 73(1)(e) floor, apply from 26 March 2029. Art 73(5) requires the Commission to lay down Secure Processing Environment requirements by implementing act by 26 March 2027. So the collision is not yet operative, and, because the acts are unwritten, nobody has yet decided how it is handled. The TEHDAS2 specification for these environments (D7.4, OPR-6) asks operators to balance deletion against "applicable legal obligations" and does not say how. A framework that arrives after infrastructure has hardened is archaeology; one that arrives while specifications are drafted can shape defaults. On the primary-use side Norway's NCPeH is live in pilot at the emergency clinics in Bodø and Stjørdal, so the audit stream is beginning now, though no relevant patient had presented when the Directorate last reported. The EDPB's coordinated enforcement report on Art 17 (18 February 2026, 32 authorities, 764 controllers) itself names the definition and implementation of retention periods as an unsettled difficulty.

**Worked example.** Record 3: a clinician HP-003 (via NCP FI) looks up a patient in month 11; the illustrative floor runs to month 131; an erasure request in month 115 sets the payload deadline at 116.

**Concede and hold.** Concede that nothing here is operative today and that for Norway the dates depend on incorporation of the Regulation into the EEA Agreement (the thesis says it is being processed through the EEA Joint Committee) [Under scrutiny for EEA incorporation per the EFTA register, 26 Nov 2026.]. Hold: lead with "it arrives while the specifications are open", not "it applies in 2029".

**Point to.** §1.1 p. 1; §1.4 p. 7; §2.2 pp. 15 to 16; §6.8 p. 98; §7.6 p. 108. Slides 5, 15, 31. App ?p=norway.

### Q2. [Either] "Is this a real problem today, who would adopt it, and what does it cost?"

**Short answer.** Not yet operative, and not measured. Per-record keys are a real burden. The cheapest step to adopt is logging every invalidation as a first-class event, which costs little.

**Full answer.** SecuPi (2025) argues that cryptographic erasure adds operational complexity and that auditable key management adds overhead. The thesis calls this "substantially correct on its own terms" (§6.4). Three things bound the burden without denying it. First, it falls on audit records, not on clinical stores: the mechanism sits at the sixth step of the MyHealth@EU flow or at a Secure Processing Environment's logging boundary, the smaller surface. Second, keys for invalidated records are destroyed, so the live registry shrinks as invalidations accumulate. Third, the verification cost grows slowly: an inclusion proof needs about log2 n hashes, some thirty for a billion entries. The critique's alternative, policy-based access control, governs who may read data and does not make it cease to exist, so it cannot meet Art 68(12) and offers nothing against Corollary 1.2. Per-record keys are the simplest construction, not the only one: a key-share design with one share per subject and one per permit has a registry that grows with subjects and permits (Cachin et al., 2013), and is not implemented. The accumulator layer scales worst and is dispensable: a scan of the registry gives the same answer without succinctness.

**Worked example.** In the envelope module 138 of 200 keys are destroyed at their invalidation months and 62 remain live: the live registry is smaller than the cumulative record count.

**Concede and hold.** Concede there is no performance measurement and no claim of one (§6.5). Hold: the burden is bounded and auditable, whereas residual copies under plaintext deletion are unbounded and uninspectable; and the invalidation entry alone is adoptable without the rest (§6.8).

**Point to.** §6.4 p. 95; §6.5 p. 96; §6.8 p. 98; §4.8 p. 63. Slides 15, 31. App ?p=norway.

### Q3. [Ferreira] "State your research question and sub-questions, and show me where each is answered."

**Short answer.** How can a verifiable crypto-erasure mechanism reconcile the conflicting retention requirements of cross-border health data exchange under the EHDS while preserving audit integrity in a Norwegian context? SQ1 is where they conflict and when all can hold; SQ2 is whether invalidation can satisfy all three; SQ3 is how it fits Norwegian infrastructure. All three are answered by name in §7.1.

**Full answer.** The primary question is in §1.3 (p. 6). SQ1 asks for the precise points of conflict and the formal conditions of joint satisfiability. It is answered by Proposition 1 with Corollaries 1.1 and 1.2 and by Proposition 3: the regimes conflict wherever an erasure deadline, or a ceiling that reaches the record, falls inside the retention window, and under plaintext verifiability they are then unsatisfiable; a ceiling can collide with a floor only if it is no longer than the floor, and its anchor decides whether the text shows it. The collision with no request holds on the broad reading of Art 68(12) only. SQ2 asks whether an invalidation mechanism can satisfy all three across floors of differing length: yes, within the model, by Proposition 2 and Corollary 2.2, witnessed in Chapter 5, with cryptography serving the copies the store cannot delete at once. SQ3 asks about integration with Norwegian infrastructure: the mechanism attaches at the audit-repository step of the MyHealth@EU flow and at the access-logging boundary of a Secure Processing Environment, adding no requirement of a new kind to the national criteria, a compatibility by specification (Table 4.1), not by deployment. The overall answer is hedged on purpose: the regimes can be reconciled within the model without amending any instrument, and whether that holds in law turns on the two authority questions of §7.4.

**Worked example.** SQ1 on record 3 (floor against right) and on record 100 (floor against ceiling); SQ2 on the same two records under Reading II.

**Concede and hold.** Concede the earlier draft of §7.1 stated the answer without the authority caveat; the submitted text carries it. Hold: the answer is "within the model, and lawful only if two authority questions go the right way".

**Point to.** §1.3 p. 6; §7.1 p. 103; Table 4.1 p. 74. Slide 2. App ?p=start.

---

# 2. Method (design science, evaluation, why not interviews)

### Q4. [Ferreira] "Which design science framework did you use, what are the artefacts, and how did you evaluate them?"

**Short answer.** Hevner et al. (2004) for the paradigm and artefact types, Peffers et al. (2007) for the six-activity process. The artefacts are a model (the TRF Model) and a partial instantiation (the sandbox). Evaluation is by argument and executable check, not in the field.

**Full answer.** DSR fits because the problem is real (binding instruments on live infrastructure), unsolved (no reviewed work models the tri-lateral conflict or derives a mechanism from it), admits an artefact as its answer (a design), and has a tractable evaluation (a claim about logical consistency, not deployed performance). The six activities map onto the chapters: problem (Ch 1 to 2), objectives (§1.3), design and development (Ch 4), demonstration (Ch 5), evaluation (Ch 5 to 6), communication (Ch 6 to 7). The thesis adds one step: formal modelling between objectives and design, so that the mechanism is derived as the constructive answer to a satisfiability question rather than assumed and justified afterwards. It uses a lighter formalism than the temporal-logic and SMT apparatus of Feng et al. (2023): one binary variable per record, in the constraint-modelling style of operations research, because the conflict turns on one semantic question and because an author trained in logistics modelling must be able to own and defend the machinery. The variant is "specification and demonstration". Evaluation (§3.7) is on internal validity, compatibility with verified infrastructure (Table 4.1) and determinism. §6.6 classifies it as artificial, not naturalistic (Venable et al., 2016).

The thesis does not tabulate Hevner's seven guidelines, so this oral mapping is yours: G1 artefact (model, mechanism, checker); G2 relevance (the EHDS collision, Norway's pilot); G3 evaluation (proofs, exhaustive search, Z3, the 200-record run); G4 contribution (the verifiability parameter, Proposition 3, the mechanism); G5 rigour (primary legal sources, reproducible code on Zenodo); G6 design as search (six rival designs in §4.10, red-team rounds); G7 communication (thesis, NORS 2025, app, archive).

**Worked example.** The SNARK design was dropped when the formal step showed commitments and a logged registry suffice (§3.2): the cycle working as intended.

**Concede and hold.** Concede utility and acceptance are not evaluated; the expert panel (Appendix C) is designed, not run. Hold: for a claim about logical consistency, analytic and executable evaluation is the proportionate one.

**Point to.** §3.1 to §3.3 pp. 37 to 40; §3.7 p. 44; §6.6 p. 96; Appendix C p. 160. Slide 19. App ?p=ledger.

### Q5. [Either] "Why not a survey or interviews? And what about ethics?"

**Short answer.** Interviews give opinions, not a mechanism, and the central questions are legal, so only an authority can settle them. I designed a practitioner panel (Appendix C) but did not run it: it needs Sikt notification and four to six weeks.

**Full answer.** §3.1 rejects three alternatives. An interview study would have produced descriptive knowledge but no mechanism and needed ethical clearance and access disproportionate to the contribution. A systematic review would consolidate knowledge when the gap is a missing design. A pure formal-methods study would give the model without the artefact and need proof-assistant expertise outside the programme. Appendix C specifies an eight-person panel (two each from data protection, health IT architecture, SPE operation, information logistics), a semi-structured guide and a sixteen-item questionnaire across utility, regulatory alignment, operational viability and audit integrity. It would process personal data about identifiable professionals, so it needs notification to Sikt and a revision of the no-human-participants statements before it runs. On ethics as submitted: no human participants and no real patient data; the only personal data are correspondence with public authorities, in which officials are named in their official capacity (§3.9). The thesis also discloses that an earlier draft, discarded in May 2026, contained citations to works that do not exist and an ethics statement that was never true; the present one is accurate.

**Worked example.** Appendix D reproduces the Helsedirektoratet reply with its author's permission, which is the one place a named official appears.

**Concede and hold.** Concede the evaluation is thin on utility and acceptance (§6.6). Hold: the panel is the first thing to run, and it is designed so the ethics wording changes only at that point.

**Point to.** §3.1 p. 37; §3.8 p. 46; §3.9 p. 46; §7.5 p. 107; Appendix C p. 160; Declaration p. xi.

### Q6. [Either] "You fixed the success criterion as 'Proposition 2 holds', then admit it holds by construction. What is falsifiable?"

**Short answer.** The infeasibility claim is falsifiable; the feasibility claim is constructive and is verified rather than tested. In the code the falsifiable part is the inclusion-proof check, and three tamper tests show it can fail.

**Full answer.** §3.3 now says it directly: the infeasibility claim is falsifiable, the feasibility claim is verified, not tested (§4.7). Proposition 1 could have failed on the checker: if any record satisfying a disjunct had a feasible assignment, the exhaustive search or Z3 would have found it, and the converse (no deadline inside the window means feasible) is exercised by the control case. The Semantics II zero is different: C2 and C3 follow from the invalidation month, because readability in the checker is derived from that month, so zero violations holds by construction (§5.7, §5.8). What can fail is condition (i): each access event, invalidation and subject-link removal is an entry in a Merkle log and V^II requires an inclusion proof against the root. Altering record 100's actor, its invalidation ground, or record 3's patient link each makes V^II false, and restoring them makes it true. Before the salted subject-link commitment was added a changed link went undetected, which is why the third test exists. FEDS classification (Venable et al., 2016): ex ante, artificial, formative.

**Worked example.** `python3 trf_checker.py`: "tamper test, rid=100 actor altered: V_II=False (access entry fails its inclusion proof)"; after restoring all three, V_II=True.

**Concede and hold.** Concede the evaluation is analytical and the evaluation is circular in the sense that the success criterion is fixed by the model. Hold: the thesis says so in §4.7, §5.8 and §6.6, and the weight of the contribution is not in the check.

**Point to.** §3.3 p. 38; §4.7 p. 62; §5.7 p. 88; §5.8 p. 89; §6.6 p. 96. Slides 12, 24. App ?p=run.

---

# 3. Legal reading

### Q7. [Either] "Walk me through the three obligations. Which articles, what do they say, and where exactly is the conflict?"

**Short answer.** A floor says keep the record: Art 73(1)(e) EHDS for research environments (at least one year); for the cross-border repository a period the specifications leave to national law (six years in the Norwegian pilot). A right says erase on request (Art 17 GDPR, one month under Art 12(3)). A ceiling says research data must be gone six months after permit expiry (Art 68(12) EHDS). They collide if "verifiable" means "readable".

**Full answer.** The floor. Art 73(1)(e) requires Secure Processing Environments to keep "identifiable logs of access to and activities in the secure processing environment for the period necessary to verify and audit all processing operations in that environment; logs of access shall be kept for at least one year". For the MyHealth@EU audit repository no eHDSI instrument fixes a period: the IHE ATNA profile prescribes none, the secondary literature reports ten years (illustrative here), and Helsedirektoratet reports six years for the pilot. Once Art 9 EHDS applies, Art 9(2) gives patients information on access for at least three years from each access, a binding 36 months for the record the information is produced from. The right. Art 17(1) GDPR requires erasure "without undue delay" where a condition applies; Art 12(3) allows one month, extendable by two. The ceiling. Art 68(12): "the electronic health data within the secure processing environment shall be deleted within six months of the expiry of the data permit". The conflict is not between the obligations as such. C1 asks for the record to remain verifiable; C2 and C3 ask for the payload to stop being accessible. If verifiable means accessible, the two bounds meet in the same month with opposite demands. If it means accountable, they do not.

**Worked example.** Record 3: floor to month 131, deadline 116. Record 100: ceiling month 16, floor to month 19.

**Concede and hold.** Concede the ten-year floor is a literature figure and the six-year pilot floor is a controller decision, not a statute. Hold: Corollary 2.2 makes every result independent of the floor value.

**Point to.** §1.1 p. 2; §4.3 p. 53; §4.4 p. 54; §2.3 pp. 17 to 18. Slides 4, 5, 7. App ?p=start.

### Q8. [Either] "Article 17(3)(b) already exempts audit retention. What conflict is left? And what about 17(3)(c) and (d)?"

**Short answer.** Half of that I concede: 17(3)(b) lets necessary retention survive. It does not say what is necessary, and with Art 5(1)(c) it protects only what the obligation needs. I argue accountability needs who, when, on what basis and outcome, plus the patient link where Art 9 applies, not the payload.

**Full answer.** The exemption has three conditions that do the work. It needs a legal obligation imposed by Union or Member State law; it protects only processing necessary for that obligation; and minimisation (Art 5(1)(c)) limits what may be kept. §4.2 argues the purpose of an audit record is accountability: that an access occurred, by whom, when, under what authority, with what result. That is served by the accessor fields and a binding commitment, and not by continued readable access to the demographic query. So a request reaches the payload, and Proposition 1's request-driven case follows. Two limits. First, if a supervisory authority holds part of the payload necessary, Corollary 2.3 applies: keep that part with the accessor fields. Second, the six-year pilot floor is a decision by Helsedirektoratet as controller; unless a national legal basis is identified it is a policy floor, so before Art 9 applies on 26 March 2029, and beyond 36 months after, keeping the patient link against a request has no secure 17(3)(b) basis. That is a finding for the controller, not a limit on the model, since a lower floor removes collisions and creates none. Art 17(3)(c) (public interest in public health) and 17(3)(d) (research) narrow C2 further in the same direction; for the SPE's own logs, which serve Art 73(1)(e) rather than the research, the exemption that applies is 17(3)(b). Not in the thesis: EDPB draft Guidelines 1/2026 on scientific research treat 17(3)(d) as case by case, not blanket [From RED_TEAM.md, not in the thesis.].

**Worked example.** On record 3 the request in month 115 reaches the payload; the accessor fields and patient link stay through the floor because Art 9(2) EHDS needs them.

**Concede and hold.** Concede the argument is mine and unconfirmed by any authority; Datatilsynet has the question. Hold: if the exemption covered the payload, C2 would not reach it and only the ceiling case would remain (§4.6).

**Point to.** §4.2 pp. 49 to 51; §4.4 p. 54; §6.2 p. 92; §7.4 p. 106. Slides 4, 6, 22. 

### Q9. [Either] "Does Article 68(12) really reach the environment's own access logs? That reading is a guess, and without it your headline collapses."

**Short answer.** The reading is contestable and I state it as a condition. If it falls I lose Corollary 1.2 and one branch of Corollary 2.3, and nothing else. Propositions 1 to 4, the mechanism and the verifiability semantics stand.

**Full answer.** Three readings are in §4.6. Broad: the provision's scope is set by location ("within the secure processing environment"), not by provenance, so it does not say "the data made available under the data permit". But its object is electronic health data, so a log entry that only records a researcher opening a dataset concerns the researcher, not anyone's health, and is not reached. An entry at patient-record granularity reveals cohort membership, which is data concerning health, so it is reached; for dataset-granularity logs only where the retained activity content is itself health data. Narrow: the provision sits in the data-permit article beside permit duration and storage fees and concerns the permit dataset. Harmonising: it reaches the logs but yields to Art 73(1)(e) as an exception mandated by law, and the TEHDAS2 specification points that way ("exceptions mandated by applicable law"). Under the harmonising reading the contradiction does not arise, but the question moves to what the floor requires: if plaintext, subject health data stay for the whole floor; if accountability, only accessor fields stay and the rest goes at the ceiling, which is the partition Proposition 2 already applies. So even then the weight falls on the necessity analysis. On the narrow reading, Corollary 1.2 lapses with the single record bound by all three regimes at once; Proposition 1 is untouched because its first disjunct concerns erasure requests, and identifiable logs remain personal data within Art 17.

**Worked example.** In the generated set, on the narrow reading 44 ceiling-only collisions lapse (the 39 witnesses and 5 records whose requests fall outside the window); 9 SPE records remain (4 colliding with C2 only, 5 also with C3; 22 SPE records received requests). With the ceiling excluded the sensitivity script gives 46 violating records, all request-driven (not in the thesis; release 1.3.4).

**Concede and hold.** Concede the reading is not settled by any authority or court. Do not use the older red-team line that the three-way collision survives the narrow reading: §4.6 now concedes it does not. Do not say the Commission will clarify it. Hold: the dependency is confined, and the EHDS-side question is not yet asked.

**Point to.** §4.6 pp. 58 to 59; §6.2 p. 93; §7.4 p. 106; §5.4 p. 84. Slide 21. App ?p=witness&r=100&m=16.

### Q10. [Either] "Semantics II is your own definition. Why would a regulator accept it? You are a logistics student issuing legal interpretations."

**Short answer.** No regulator has said so and I do not pretend otherwise. I argue it from two points: the exemption protects only what is necessary, and minimisation says keep no more than the purpose needs. The thesis proves feasibility under the definition and labels it a reading. The question is put to Datatilsynet.

**Full answer.** §6.2 calls this the most serious objection and it is not technical. Nothing says an invalidated record satisfies a retention obligation. The argument runs: Art 17(3)(b) protects only necessary processing; Art 5(1)(c) requires no more than the purpose demands; the accountability purpose is who, when, on what basis, with what outcome; therefore readable payload is beyond what necessity protects; Datatilsynet's guidance places exactly that balancing on the controller. If an authority reads "identifiable logs" in Art 73(1)(e) as logs whose subject matter remains readable, Proposition 2 stays true of the model and becomes practically inert. Why that outcome is unlikely, as reasons rather than reassurance: the alternatives are worse (on the broad reading the only way to honour both articles under plaintext is to export the logs, which moves the subject fields to a second controller and leaves the right untouched, Proposition 4; for cross-border records there is no export route at all); the regulatory direction is compatible (EDPB Guidelines 02/2025 para 51: key deletion makes data unintelligible, yet encrypted data remain personal data; para 125: erasure requires the data erased or anonymised); and a specification that asks for a balance (TEHDAS2 OPR-6) has not adopted plaintext verifiability. The question is decidable by asking. The EDPB does not endorse Semantics II: the further condition that the controller document its threat model is Aikebaier's (2026) interpretation, not the Board's.

**Worked example.** After invalidation record 100 still shows who (R-008), under which permit (DP-015), when, a commitment, and the invalidation entry (month 16, ground Art 68(12)); only the payload is gone.

**Concede and hold.** Concede it is argued and unconfirmed. Hold: an unfavourable answer "refutes them cleanly and identifies precisely what would have to change" (§7.4), and either outcome is worth more than the present uncertainty.

**Point to.** §4.2 p. 49; §6.2 pp. 92 to 93; §7.4 p. 106. Slides 8, 14, 22. 

### Q11. [Either] "Is what remains of the patient's record anonymous? Does your residue escape the GDPR?"

**Short answer.** No. It identifies the accessor and is pseudonymised as to the patient, so it is pseudonymised, not anonymous, until a terminal transition that is specified and not implemented. The test I rely on is erasure, not anonymisation, and the store meets it by deletion.

**Full answer.** Identifiability turns on whether anyone can re-identify by means reasonably likely to be used. Datatilsynet (2015) holds that data are not anonymous while any key or linkage capable of re-identification is kept. The EDPB's draft Guidelines 02/2026 set the same bar at Union level with a three-part test (isolation, linkage, inference) and hold that encryption is by nature reversible and is not anonymisation. The Court of Justice (EDPS v SRB, C-413/23 P, 4 September 2025, paras 73 and 76 to 77) holds that pseudonymised data are not personal data in all cases and for every person: possibly not for a recipient who cannot lift the pseudonymisation, but still personal data for the controller who holds the additional information. The repository controller holds the subject link and the accessor identity, so for it the residue is personal data. Why the mechanism is still defensible: the legal test is erasure, and at invalidation the ciphertext, key and salt are deleted from the store. Key destruction is relied on only for copies that cannot be deleted at once, a bounded residue unreadable from invalidation and personal data until it leaves by rotation. The salted commitment stops anyone confirming a guessed payload. The terminal transition after the floor destroys identifying metadata and aims at a non-identifiable remainder, but the invalidation entries carry the record identifier and authorising actor, which must be generalised or destroyed too, and whether the remainder resists the three-part test is for the documented threat model.

**Worked example.** Record 100 after invalidation still carries actor R-008 and permit DP-015, as Art 73(1)(e) requires identifiable logs.

**Concede and hold.** Any claim of anonymisation "would be false" (§4.9). Hold: the claim is erasure of the payload, with an honestly bounded residue.

**Point to.** §4.8 p. 67; §4.9 pp. 68 to 69. Slide 27. App ?p=witness&r=100&m=19.

### Q12. [Either] "Why do you keep the patient link after an erasure request? And what of the clinician's own Article 17 right?"

**Short answer.** The link is not payload; it is the other half of the accountability question. Art 9(2) EHDS gives patients information on who accessed their data for at least three years, and that cannot be produced from a record that no longer says whose data were accessed. The clinician's own right does not empty the log either, for the same necessity reason.

**Full answer.** Art 9(1) to (2) EHDS gives natural persons information on the provider who accessed their data, the date and time, and which data, available for at least three years from each access. For the controller that must provide it, keeping the link is necessary for compliance with a legal obligation within Art 17(3)(b), so a request reaches the payload but not the link, for the Art 9(2) period and once Art 9 applies. The argument has limits that the thesis states. Art 9 is framed around the health professional access service, so whether it binds the controller of a foreign NCPeH's audit repository, and covers every cross-border event, is a subsidiary premise without authority. Beyond the 36 months the link is kept for the rest of the floor only on whatever national provision fixes the repository's retention, which the thesis has not identified, so its retention after a request is as contestable as the floor. In an SPE, Art 9 does not apply, and the link is kept after a request until the ceiling only if auditing "all processing operations" needs it. The accessor's fields are the clinician's or researcher's own personal data; their Art 17 right is met by the same necessity reasoning (Art 73(1)(e); for cross-border records Art 9(2) and national law), and a period an operator sets without a Union or Member State legal basis would not engage the exemption. What necessity does not protect is not kept: the accessor fields are destroyed at the terminal transition.

**Worked example.** Record 3 keeps its patient link through the floor; record 100 loses its link at month 16 and the removal is a logged entry.

**Concede and hold.** Two of the four subsidiary premises (§3.7) are exactly these. Hold: they bound specific results, not the model.

**Point to.** §4.2 pp. 50 to 51; §3.7 p. 45; §7.4 p. 106. Slides 10, 11.

### Q13. [Either] "Norway is not an EU member. Does the EHDS even apply, and who is the controller?"

**Short answer.** Not directly. Norway is an EEA state, the Regulation is being processed for incorporation through the EEA Joint Committee, and the dates for Norway depend on that. The controller of a national contact point's audit repository is that point's own national authority.

**Full answer.** The thesis is explicit (§2.2, §1.4): as an EEA member rather than an EU Member State, Norway receives the EHDS Regulation only on incorporation into the EEA Agreement, and Helsedirektoratet delivered its formal impact and gap analysis on 11 April 2025. So the Norwegian instrument date for Arts 68 and 73 is not the Union date. The analysis is nonetheless coherent for two reasons: the model takes the floor and ceiling as parameters, so an incorporation date changes when the constraints bind, not whether the structure exists; and the cross-border audit records already exist in the live pilot under the eHDSI framework. On the controller: Commission Implementing Decision (EU) 2019/1765, which the thesis states is incorporated into the EEA Agreement, makes the participating states, through their national authorities or designated bodies, the controllers of data they process through the infrastructure, with the Commission a processor with no access to patients' personal data (Art 7). The Art 17 request lands on that authority, for Norway the operator of the NCPeH (Helsedirektoratet is data controller per its own reply).

**Worked example.** Larsen's reply: "Hdir er dataansvarlig og vil ta den beslutningen" (Appendix D).

**Concede and hold.** The reviewer notes said to confirm the EEA incorporation of 2019/1765 at the viva: bring the source if asked [Since submission: EHDS Regulation is under scrutiny for EEA incorporation per the EFTA register (26 Nov 2026); say "being processed".]. Hold: nothing in the propositions depends on the date.

**Point to.** §1.4 p. 7; §2.2 pp. 15 to 16; §4.2 p. 51; Appendix D p. 168. Slides 14, 15.

---

# 4. Model and propositions (compact; the full derivations are in Part B)

### Q14. [Either] "Walk me through the variables and the three constraints. Why one binary variable, why months, and what does 'tri-lateral' mean?"

**Short answer.** For each record and month there is one yes-or-no question: can the payload still be read? That is alpha. Everything else is a clock: when the record was made, how long it must be kept, when a request arrives, when a permit ends. "Tri-lateral" means three kinds of constraint (floor, right, ceiling), not three laws. Full definitions: Part B, section B2.

**Full answer.** A record a has a creation month t(a), a floor F(a), a pathway sigma(a) (primary or secondary), metadata split into accessor fields and subject fields (the patient link), a payload p(a), a commitment c(a), a key k(a). Events: an erasure request t_r(a) (infinite if none), the response period delta (1 month, 3 if extended, Art 12(3) GDPR), a permit expiry t_pi(a), an optional payload period P(a). States: alpha(a,t) payload readable; beta(a,t) patient link readable; V(a,t) verifiable. The reach indicator rho(a) is 1 where the ceiling reaches the record. The invalidation month is t^I = min(t_r + delta, t_pi + 6, t + P). C1 says V = 1 for every month t(a) to t(a) + F(a), a closed window of F + 1 months, conservative for "at least". C2 says alpha = 0 from t_r + delta. C3, for secondary records with rho = 1, says alpha = 0 (and beta = 0 where the link is health data) from t_pi + 6. C1 is a lower bound on a property; C2 and C3 are upper bounds on accessibility. Whether they clash depends on whether V is defined in terms of alpha. One variable is deliberate: it isolates the one question the conflict turns on, and it is conservative, since a mechanism that satisfies the constraints for a whole payload satisfies them for any part. "Tri-lateral" counts constraint types: the floor is one parameterised constraint with two instances, so the model is indifferent to the number of floors (Corollary 2.2). Months are the unit because every instrument speaks in months or years.

**Worked example.** Record 3: t = 11, F = 120, t_r = 115, so the window is months 11 to 131 and t^I = 116. Record 100: t = 7, F = 12, t_pi = 10, so the window is 7 to 19 and t^I = 16.

**Concede and hold.** Discretisation can create boundary artefacts: C2 binds from the start of month t_r + delta, stricter than "one month from receipt". Edge cases are handled: requests arrive at or after creation, delta is at least 1, arithmetic is over the naturals plus infinity, and a record written at or after its own deadline never holds a readable payload. The model cannot express field-level redaction (eighth limitation); Corollary 2.3 adds a variable per payload part for the one case where it matters.

**Point to.** §4.3 pp. 51 to 53; §4.4 p. 54; §3.7 p. 45; Nomenclature p. xii. Slide 7. App ?p=start.

### Q15. [Either] "Proposition 1 is trivial, and Semantics I is a straw man nobody holds. What does it earn?"

**Short answer.** Yes, it is short, and I say so: a pigeonhole on one yes-or-no variable. What it earns is a negative result about deployed designs, and it pins down exactly which records collide. Semantics I is not invented: the reference gateway behaves that way. See Part B, section B3.1.

**Full answer.** Statement: under Semantics I (V = alpha) the system {C1, C2, C3} is infeasible for any record with t_r + delta <= t + F, or with t_pi + 6 <= t + F where the ceiling reaches the record. Proof: take t* the deadline month; it lies inside the window, so C1 needs alpha = 1 there while C2 or C3 needs alpha = 0. The converse is exact: if neither disjunct holds, keep alpha = 1 through the window and 0 after, and the system is feasible. So the proposition is a characterisation, which is what the control case in the exhaustive search exercises. It earns three things. It marks as unworkable any design that keeps the payload readable for the length of the floor wherever a deadline falls inside it. It makes the collision locatable to a month (Corollary 1.1: at a 72-month floor a request in any of the 72 months from creation collides; at 120 months, in all but the last month). And it shows that some departure from readable-verifiability is unavoidable, so the real question is which departure is defensible, which is §4.2. On straw man: no instrument states Semantics I, but in the 2017 OpenNCP source the audit repository stored every received audit message whole in a database column, kept the patient identifier in a readable column and the participant-object query in another, refused to modify a stored message, and had no scheduled purge logic; the schema deployed with OpenNCP 9.1.0 in 2026 keeps the same columns. Whether other deployments configure retention differently was not inspected.

**Worked example.** Record 3: t* = 116 <= 131, infeasible. Record 38: created month 10, request month 138, deadline 139 is later than the window's last month 130, so it is feasible: the one cross-border request outside its window (record number 38 and "38 requests" are a coincidence).

**Concede and hold.** The propositions are "stated as propositions rather than theorems, because their proofs are short once the semantics are fixed". Propositions 1 to 3 are proved informally; none is machine-checked. Hold: the weight lies in the necessity analysis (§4.2) and the mechanism, which the abstract says.

**Point to.** §4.5 pp. 55 to 56; §4.6 p. 57; §4.7 p. 62; §5.3 p. 83. Slides 8, 9, 24. App ?p=propositions.

### Q16. [Either] "Explain the collision that needs no erasure request. Where does 'half of research logs' come from?"

**Short answer.** In a research environment the same regulation says keep identifiable access logs for a year (Art 73(1)(e)) and delete the environment's health data six months after the permit ends (Art 68(12)). If a log written near a permit's end counts as health data, the two overlap and nobody asked for anything. It is conditional on the broad reading. See Part B, section B3.3.

**Full answer.** For SPE logs F = 12 and sigma = secondary. If t_pi + 6 <= t + 12, that is, the permit expires within six months of the entry, then C1 and C3 are contradictory at t* = t_pi + 6 under Semantics I, provided C3 reaches the record. The corollary also assumes the activity content, not only the subject fields, is data concerning health; were it not, Semantics I could keep the payload readable and delete only the link, and no collision would arise. For patient-level activity (which records and variables a researcher touched) the thesis states the premise rather than deriving it. The "half" is a property of the generator: permits are drawn uniformly 1 to 12 months, so about half fall within six months of the entry. Over a five-year permit with the remaining duration uniform, the rate is about 6 over the maximum permit length, about one in ten; but the structural fact does not depend on the distribution: any entry written in the last six months of a permit has a floor that outlasts its ceiling.

**Worked example.** Record 100: created month 7, permit expires month 10, ceiling month 16, floor to 19; months 16 to 19 collide. Contrast record 102: created month 5, permit expires month 12, ceiling month 18, floor ends month 17: clear by one month. Of 78 SPE records with no request, 39 collide.

**Concede and hold.** The frequency is a generator output and no frequency is claimed; the corollary asserts existence, not frequency. It holds only on the broad reading (Q9). Hold: it needs no data-subject action and involves no deployment baseline; it is internal to Regulation 2025/327 where it holds.

**Point to.** §4.6 pp. 57 to 59; §5.4 pp. 84 to 85; Figure 5.2 p. 85. Slides 5, 21, 23. App ?p=witness&r=100&m=16.

### Q17. [Either] "You defined Semantics II in full knowledge of the trajectory that satisfies it. What does Proposition 2 prove?"

**Short answer.** Little mathematically, and the thesis says so: it is a verification, not a discovery. The claim is that Semantics II is a defensible reading of the law, argued in §4.2. The proof is the build sheet for the mechanism. See Part B, section B3.5.

**Full answer.** Proposition 2: under Semantics II the system is satisfiable for every record, every arrival pattern of requests and permit expiries, and every floor. The proof is constructive. Let t^I = min(t_r + delta, t_pi + 6, t + P). Before t^I keep alpha = 1 with everything retained. At t^I destroy the key; for SPE logs at the ceiling remove the subject fields; append an invalidation entry (month, legal ground, authorising actor, a hash of the key's identifier); keep the accessor fields and the commitment. After t^I alpha = 0. C2 and C3 hold because t^I is at most each deadline. C1 holds because no step touches the accessor fields or commitment and condition (iii) is met by the entry. Corollary 2.1: no coordination between the erasure process and the retention process, and no foresight at creation. Corollary 2.2: F is arbitrary, so 120, 72, 36 and 12 months are covered at once. Corollary 2.3: if auditing needs part of the payload, keep that part with the accessor fields; it satisfies C1 and C2 (via 17(3)(b)) and C3 unless that part is itself health data in the SPE on the broad reading. Honest edges: alpha identically zero also satisfies Semantics II (conceded in §4.7); condition (ii), "binding", is a property of the scheme and exists so that Rival 4 fails by definition, which §4.10 concedes; and the Z3 check of Proposition 2 holds by construction, so its evidential weight lies in the refuted mutations (construction without the invalidation entry, without the commitment, without the subject-link entry all yield counterexamples).

**Worked example.** Record 3: t^I = min(116, infinity, infinity) = 116, ground Art 17(1), patient link kept. Record 100: t^I = 16, ground Art 68(12), subject link removed at 16.

**Concede and hold.** Concede the objection has force: "the response concedes its premise and denies its conclusion". Hold: any number of semantics would admit a trajectory; the question is whether this one is what the instruments require, and Proposition 1 shows plaintext cannot be.

**Point to.** §4.7 pp. 60 to 62; §4.10 p. 71; §5.5 p. 86. Slides 9, 24. App ?p=propositions.

### Q18. [Either] "Explain the anchor condition e(a) minus t(a) is at most F minus L, and why the start of the ceiling's clock matters. Is politiregisterloven section 17 really anchored at the entry?"

**Short answer.** A ceiling collides with a floor only if it is no longer than the floor. Whether you can see that in the text depends on where each clock starts: same start, visible; different start, only each record's history shows it. See Part B, section B3.4.

**Full answer.** Proposition 3: let the floor F run from creation t(a) and a ceiling L from an event at e(a) >= t(a). Under Semantics I they are jointly satisfiable iff e + L > t + F. Proof: C1 needs alpha = 1 up to t + F, the ceiling needs alpha = 0 from e + L; some month carries both iff e + L <= t + F. Case (i), same anchor (e = t): satisfiable for every record iff L > F, decidable from the text alone. Case (ii), external anchor with L <= F: they fail for exactly the records with e - t <= F - L, a set the text does not reveal. For Art 68(12) (L = 6, F = 12) the set is records whose permit expires within six months of the entry, which is the condition of Corollary 1.2. A provision that measured both limits from one event and set the ceiling inside the floor would contradict itself on its face. Section 17 of politiregisterloven ("lagres i minst 1 år og slettes senest etter 3 år") puts a floor of 12 and a ceiling of 36 on one log; read as running from the entry, L > F and no collision arises without a request. The cross-sector run: 60 records, 7 violate, none without a request; under Semantics II none. The provision does not say in words when either period begins; that both run from the entry is a reading of its syntax, stated as such. The same diagnostic applies to any statute: look for a ceiling no longer than a floor and anchored to a different event.

**Worked example.** Record 100: e - t = 10 - 7 = 3 <= 6, collides. Record 102: e - t = 12 - 5 = 7 > 6, clear. Z3 checks both directions and both cases, and refutes an off-by-one version.

**Concede and hold.** Concede [CHECK: Lovdata text of politiregisterloven section 17 not verified; bring it or avoid the detail]. The instance is illustrative, not empirical, and its Semantics II zero is narrower than the health case's: § 17 reaches the whole entry and the module tests only payload and link. Energy and MiFID II remain untested; the thesis says so.

**Point to.** §4.6 p. 60; §6.10 pp. 100 to 101; §7.5 p. 107; A.13 p. 139. Slides 20, 30. App ?p=anchor.

### Q19. [Either] "Just export the logs out of the research environment at permit closure. Problem solved? And Proposition 4 is not a proposition, it is an assumption with a proof attached."

**Short answer.** Export meets the ceiling and I accept it as sufficient for Corollary 1.2. It does not meet the erasure right, because the right follows the data to whoever holds it. That rests on one legal premise, which I state, and the thesis calls Proposition 4 "a legal argument given the form of a proposition". See Part B, section B3.8.

**Full answer.** Rival 6 (§4.10): exporting access logs at permit closure to a store outside the environment satisfies Art 68(12) literally, on the premise that Art 73(1)(e) fixes how long logs are kept, not where. The ceiling is anchored to a location, requiring data to be absent from it after a deadline; the right is anchored to the data subject and obliges whichever controller holds the data. The premise, not derived from the model, is that a controller receiving a relocated record receives the Art 17(1) obligation with it. Given it, relocation leaves C1 and C2 as they were and the argument of Proposition 1 applies unchanged. Relocation is not free: the exported log still carries its subject fields, now held by a second controller for the rest of the floor, so the personal data have been moved rather than reduced, and where those fields are health data they sit outside the measures Art 73(1) prescribes. For cross-border records there is no environment to leave, so there is no export route at all. The proposition is stated over the model extended informally with a location and a controller, which §4.3 does not represent, and the artefact does not execute it.

**Worked example.** Not in the thesis, from the checker: record 132 (created month 1, request month 4 so deadline 5, permit expiry 7 so ceiling 13, floor to 13). Exporting before 13 meets the ceiling; the month-5 deadline still falls inside the floor.

**Concede and hold.** Concede it is argued from a premise and could be called an observation. If the premise is wrong, Rival 6 becomes stronger; Propositions 1 to 3 are untouched. Hold: "Ending payload accessibility within the floor is necessary for the request-driven conflict, which no relocation escapes."

**Point to.** §4.10 pp. 71 to 72; §3.7 p. 45; §6.2 p. 93. Slides 6, 30. App ?p=anchor.

### Q20. [Either] "Proposition 1 was restated late. Why does the ceiling disjunct need rho = 1, and which version am I examining? Your legal condition is about the patient link but your collision is over the payload."

**Short answer.** The ceiling C3 binds only secondary records with rho = 1, where the log entry is itself electronic health data; a proof cannot use a constraint on a record it does not bind. Nothing in Chapter 5 moves, because every SPE record is generated with rho = 1. The submitted thesis carries the scoped statement.

**Full answer.** rho(a) = 1 where the entry is itself electronic health data within the environment. On the broad reading rho = 1 for entries at patient-record granularity, and for dataset-granularity entries only where the retained activity content is itself data concerning health; on the narrow reading rho = 0 for every access log. Patient-record granularity is sufficient, not necessary. Under Semantics I, V = alpha, so the Corollary 1.2 collision is over the payload (the logged activity); the patient link beta matters to C3 only where the subject fields are health data. The corollary therefore needs two things: that C3 reaches the record, and that the activity content is health data. The thesis states the second as a premise. §5.2 states the run sets rho = 1 for every SPE record, which models the broad reading. On versions: release 1.3.0 is the cited code and its figures; its viewer quotes Proposition 1 before the scope sentence was added; release 1.3.1 carries the scoped statement; later releases change viewer wording and metadata only. The six result modules are byte-identical across them [CHECK: the walkthrough says the live app is 1.3.2; the repository is at 1.3.4].

**Worked example.** `ceiling_deadline()` in the checker takes no reach flag: every secondary record gets t_pi + 6, which is exactly the rho = 1 modelling choice.

**Concede and hold.** Concede the earlier abstract wording tied the condition to granularity alone; the submitted abstract reads "only for log entries that are themselves electronic health data, as entries kept at patient-record granularity are". Hold: the legal condition and the formal collision now concern the same variables.

**Point to.** §4.4 p. 54; §4.6 pp. 57 to 59; §5.2 p. 80; Appendix A.1 p. 116. Slides 5, 21.

---

# 5. Mechanism and cryptography

### Q21. [Either] "What exactly is kept, what is destroyed, and when? What can an auditor check afterwards?"

**Short answer.** At the earliest deadline I destroy the payload, its key and its salt. I keep who looked, when, under what authority, a sealed fingerprint of the payload, and a logged invalidation entry. The log never holds what erasure reaches, so it never needs rewriting.

**Full answer.** The audit writer splits each record into accessor fields, subject fields (the patient link) and payload. The payload is encrypted under a per-record data key held under a key-encrypting key in a hardware security module or equivalent. A salted commitment c(a) = Commit(p, r) binds the payload without revealing it. The Merkle log (RFC 6962 hashing, as in Certificate Transparency) takes leaves holding the accessor fields, the creation month, the payload commitment, a salted commitment to the subject fields and the invalidation entries; never the payload, never the subject fields. The invalidation month is the earliest of the erasure deadline, the ceiling deadline and a controller-set payload period. At that month the key, salt and ciphertext are deleted; for patient-level SPE logs the subject fields go at the ceiling. The invalidation entry carries the record identifier, the month, the legal ground, the authorising actor and a hash of the destroyed key's identifier. After invalidation an auditor can establish four things: the access happened, by whom, with all its accountability attributes; some payload was bound at write time and has not been substituted (opening needs a party that kept an opening); the payload was invalidated, when, on what ground, by whom; and each entry is in the log as first written, by inclusion proof. The auditor cannot read the payload and cannot check that the key is gone.

**Worked example.** The run's printout for record 100: accessor fields True (R-008, permit DP-015, success); subject link removed month 16; commitment 678ade47c1e6dc03296175e056fd8116...; key, salt, ciphertext None; invalidation month 16, ground EHDS Art 68(12); payload readable False. Code: `apply_invalidation` (trf_checker.py line 270), `alpha` (296), `V_II` (305).

**Concede and hold.** Specified, not implemented: terminal transition, per-leaf nonce, proactive invalidation (the run has P infinite), published roots with consistency proofs, the accumulator. Hold: none is part of either executed proposition.

**Point to.** §4.8 pp. 63 to 67; Figure 4.1 p. 64; §5.7 pp. 87 to 88; Table 4.1 p. 74. Slides 10, 11. App ?p=built.

### Q22. [Curado] "Is your commitment even hiding? Where do the salts come from?"

**Short answer.** The design requires a random per-record salt. In the reported run the salt is derived from the record identifier so the run reproduces exactly, so it is not hiding in that run. `--random-salts` draws it from os.urandom.

**Full answer.** A commitment must be hiding (reveals nothing without the salt) and binding (no second payload opens it). A bare unsalted hash does not hide: for clinical content from a constrained space, such as a diagnosis code or a formulary medication, an adversary can confirm a guess by recomputing the hash, so an unsalted commitment would be a surviving item of personal data and the mechanism would have relocated the erasure problem. With a random salt of adequate length the commitment alone leaks nothing, and because the salt is destroyed with the key no party can confirm a guess from the audit store after invalidation unless it kept its own opening. Destroying the salt does not weaken binding, which is a property of the commitment value. After invalidation, an auditor can open the commitment only through a party that was handed the opening at write time (the data subject or the patient's home contact point); otherwise it fixes only that some payload was bound. In the reported run c = SHA-256(salt || payload) with a 16-byte salt derived from the record identifier. Two further points are in the code but not in the thesis text: the derived salts repeat with period 256 in the record identifier, and the salt of the subject-link commitment is derived from the identifier plus 100000 while pseudonyms come from a 100-value space (PSN followed by the identifier modulo 100), so in the reported run that link commitment is brute-forceable. The leaf-level analogue (a per-entry nonce so a surviving leaf hash confirms nothing) is specified, not implemented.

**Worked example.** Run `python3 trf_checker.py --random-salts`: record 100's commitment becomes 483ca80edb4c686ca63db33c3081d47c... instead of 678ade47c1e6dc03...; every count is unchanged.

**Concede and hold.** Say the salt caveat first, before it is asked. Hold: the property is a requirement of the design, not an implementation preference, and no figure depends on it.

**Point to.** §4.8 p. 65; §4.9 p. 68; §5.2 p. 80; A.6 p. 121. Slide 27.

### Q23. [Curado] "Can the operator rewrite your log? Merkle trees give you nothing without published roots."

**Short answer.** Correct, and the thesis says so. The artefact recomputes the root from the leaves the log itself holds, so it detects divergence between a record and its logged events. It does not detect a rewrite of the whole log. That needs roots published or countersigned outside the log and consistency proofs between an earlier root and the current one, as in Certificate Transparency. Both are specified and not implemented.

**Full answer.** What the check does catch: an inclusion proof is the logarithmic list of sibling hashes from a leaf to the root; `MerkleLog.proof` collects them and `verify` rehashes and compares to the root. Altering record 100's actor makes its access entry fail its proof; altering its invalidation ground makes the invalidation entry fail; altering record 3's patient link means the link no longer opens the salted commitment its leaf carries. Each makes V^II false, and restoring them makes it true. What it cannot catch: the operator who rewrites everything and recomputes the root, because nothing outside the operator's control holds an earlier root. The operator is a named trusted party in §4.9: alteration is detectable, not impossible. The claim "cannot be rewritten without detection" therefore holds only once a root containing the entry has been published outside the log, and the contribution statement now says tamper-evident against a published root, not tamper-proof. What does hold: once a root containing an invalidation entry is published, the claim cannot be withdrawn. Where roots are published (a public ledger, a regulator, a countersigning party) is a deployment choice the thesis does not make.

**Worked example.** The run's log has 438 entries; 200 of 200 records verify; three tamper tests fail V^II and all pass after restoring.

**Concede and hold.** The Norwegian SPUHiN draft requires "tamper-proof" logs (P13); the mechanism's log is tamper-evident, which addresses that by detection against a published root. Use "tamper-proof" only when quoting that requirement. Hold: this is the open edge and it is named on slide 11.

**Point to.** §4.8 p. 66; §4.9 p. 69; §5.7 p. 88; Table 4.1 p. 74; §6.1 p. 91. Slides 11, 29. App ?p=run.

### Q24. [Curado] "Why not just put this on a blockchain?"

**Short answer.** The problem is not where the log lives but what an entry contains. A ledger copies every entry to every node and never forgets, so personal data written there meets the erasure right head on. The Merkle log gives what a chain would add, tamper evidence and inclusion proofs, and its leaves never hold what erasure reaches.

**Full answer.** KONFIDO (2016 to 2019) extended OpenNCP with a blockchain auditing component valued for immutability, and left the immutability-versus-erasure conflict unresolved; it also depended on Intel SGX hardware. Finck's analyses set out the tension; a review of 114 papers reports the right to be forgotten first among the difficulties; and the EDPB's Guidelines 02/2025 on blockchain treat it as an unsettled constraint. Redactable blockchains and chameleon-hash designs resolve it the other way, by giving a key holder the power to rewrite history, which is a trust assumption this design avoids. My route: the log is never edited, and erasable content never enters it. Leaves hold the accessor fields, the payload commitment, a salted commitment to the subject link and invalidation entries. The thesis also argues the tri-lateral conflict cannot be dissolved by any storage choice. Norway has a clinical precedent for blockchain-anchored consent (NewbornTime, a Hyperledger platform at Stavanger University Hospital, which addresses consent recording rather than audit-trail erasure). A public ledger could be one place to publish roots; the thesis neither specifies nor evaluates that.

**Worked example.** In the run, record 100's leaf holds R-008, DP-015 and 678ade47c1e6dc03...; the diagnosis-like payload and the patient link are in the record store, and are destroyed there.

**Concede and hold.** The remark that a public ledger could host published roots is a framing of mine; the thesis does not say where roots go. Hold: no log needs rewriting if it never held what erasure reaches.

**Point to.** §2.4 pp. 21 to 25; §4.8 p. 66; §4.9 p. 69. Slides 6, 18. App ?p=built.

### Q25. [Curado] "You cannot prove a key was destroyed. What does an HSM give you? And then what does 'verifiable' in your title mean?"

**Short answer.** I cannot, and nobody can by inspection from outside. The entry is an attestation: who destroyed which key, when, on what ground, bound into the log. An auditor can check the claim was made and not altered, not that it is true. So "verifiable" qualifies the invalidation record, not the erasure.

**Full answer.** Reardon and colleagues' systematisation shows that the further a deletion approach operates from the storage medium, the harder it is to assert that destruction occurred; cryptographic erasure is the limiting case. The entry records a named actor, a named key identifier (hashed), a month and a ground, and binds it into the Merkle log so the claim cannot be altered without detection, nor withdrawn once a root containing it is published. Key-management guidance treats such a record as the normal trace of a destroyed key (NIST SP 800-57, section 7.6). A FIPS 140-3 validated module places destruction inside a tested boundary, but validation attests the module's design, not any particular destruction. In the artefact, a custody object stands in for the HSM: the optional module uses real AES-256-GCM with per-record data keys wrapped under a key-encrypting key, and after the 138 scheduled destructions exactly those records refuse to decrypt through custody while 62 still read; that shows unreadability follows from destruction, not that destruction happened. Proof would need proof-of-secure-erasure protocols (Bursuc et al., 2024) or certified deletion, where public verifiability is an open problem (Broadbent and Islam, 2020). The alternative is not proven deletion but unattested deletion: "delete and log" is the same kind of unverifiable claim with less structure.

**Worked example.** `python3 crypto_envelope.py`: 138 refused, 62 decryptable, and record 3's ciphertext opened by none of the 62 surviving keys.

**Concede and hold.** "Refusal" in the module is the custody object's missing wrapped key (a dictionary removal); the cross-key test is the cryptographic check. In the checker, the key identifier whose hash goes into the entry is a placeholder. Hold: §1.4 says verifiable qualifies "the invalidation record ... not the erasure itself, which no auditor can verify".

**Point to.** §1.4 p. 7; §4.9 pp. 69 to 70; §6.3 p. 94; §7.5 p. 107; A.15 p. 142; A.22 p. 149. Slides 11, 25. App ?p=robust.

### Q26. [Curado] "Why keys at all? Your model cannot tell destroying a key from deleting the payload. And is destroying a key even erasure?"

**Short answer.** Agreed: nothing in the model distinguishes them; both set alpha to zero. The store deletes the payload. Key destruction is for copies the store cannot delete at once, backups and replicas, and for those it secures unintelligibility, not erasure.

**Full answer.** EDPB Guidelines 02/2025 (final, 7 July 2026), para 51: after deletion of the decryption key the encrypted data will be unintelligible, at least until the algorithm is broken; in the same paragraph, encrypted personal data is still personal data; para 125: an erasure request requires the data erased or rendered anonymous. So the Board describes what key deletion achieves without classifying it as erasure, and the thesis never says the EDPB endorses crypto-erasure. The mechanism therefore deletes the ciphertext, key and salt from the store at invalidation. The case for keys rests on copies, which the model does not represent and the TEHDAS2 specification expressly reaches: electronic health data "MUST be deleted or rendered unrecoverable within six months of permit expiry, including any backups or redundant copies" (OPR-6). Such copies become unreadable at the invalidation month and leave by ordinary rotation, a bounded residue stated as such. NIST SP 800-88 Rev. 2 recognises cryptographic erase within a documented key-management boundary. Per-record keys are the simplest construction, not required: a record encrypted so that a subject share and a permit share are each needed to read it becomes unreadable when either is destroyed, with a registry growing with subjects and permits (policy-based secure deletion, Cachin et al., 2013); not implemented. The documented threat model condition is Aikebaier's (2026) interpretation, adopted as a design discipline, not the Board's formulation.

**Worked example.** Permit expiry invalidates the records of one permit; an erasure request invalidates the records of one subject; these sets intersect without nesting, so no single per-subject or per-permit key serves both.

**Concede and hold.** Concede the title's "crypto" rests on copies, not on a proposition. A "crypto" mechanism without backups would reduce to delete-and-log (Q28). Hold: OPR-6 asks for exactly this balance and does not say how.

**Point to.** §4.8 pp. 63 to 65; §4.9 p. 69; §6.4 p. 95; §2.4 p. 23. Slides 10, 22, 25.

### Q27. [Curado] "What is your threat model? Why keep an accumulator that needs a trusted manager and is not built?"

**Short answer.** The thesis names five trusted parties or assumptions. The accumulator is optional and not load-bearing, and I am willing to drop it.

**Full answer.** §4.9 lists: (1) the controller executes destruction when the entry says it did, and had no copy of the key outside the custody boundary at that moment; (2) the custody boundary, an HSM or equivalent, retains no recoverable key material after a destruction instruction and does not leak it through side channels; (3) the audit-trail operator does not remove or alter entries, which the append-only construction makes detectable but not impossible, a rewritten history needing published roots and consistency proofs (artefact: inclusion proofs only); (4) where the optional accumulator is used, its manager, who holds a trapdoor and could forge validity witnesses; (5) the cryptographic assumption that the commitment stays binding and hiding and the payload cipher unbroken across the horizon. The horizon matters over a ten-year floor: deleting the ciphertext at invalidation removes that exposure for the store's own copy, but copies awaiting rotation, and records with no invalidation event, keep ciphertext until the terminal transition. What an auditor can verify without any of that trust: internal consistency of the metadata, that an invalidation entry exists with month, ground and actor, that it is bound into the log, and that a commitment survives. The accumulator (Camenisch and Lysyanskaya type) would add a succinct proof that a record has not been invalidated; Proposition 2 holds if validity is checked by scanning the registry.

**Worked example.** With no accumulator the run still answers "is record 100 invalidated?" by scanning the registry: entry month 16.

**Concede and hold.** The accumulator is "the most dispensable" component (§6.5); offer to drop it. Hold: every trust assumption is named, and the thesis does not claim more.

**Point to.** §4.8 p. 66; §4.9 pp. 69 to 70; §6.5 p. 96. Slides 11, 25.

### Q28. [Either] "Isn't this just crypto-shredding with a new name? Why not delete the record and log the deletion?"

**Short answer.** The technique is crypto-shredding and I claim no new cryptography. I add a model showing when it can meet three rules together, a precise meaning of "verifiable" that makes it possible, and a record an auditor can check. For cross-border records, delete-and-log is close to equivalent, and I concede that.

**Full answer.** The practitioner pattern (per-subject key destroyed on request) is bilateral and asserted: no model, no verifiability semantics, ciphertext retained. Rival 4, "delete the record and log the deletion", satisfies C2 and C3 and preserves a trace, and it fails C1 under Semantics II only because no commitment survives, which is true by definition. So what does the commitment add? Before invalidation an auditor can open it against the payload and detect substitution of one record's content for another's. After invalidation it can be opened only by a party that kept an opening; otherwise it fixes only that some payload was bound. The advantage is therefore real but bounded, lying chiefly in the logged, attributed, tamper-evidently bound invalidation entry and only partly in the commitment. For cross-border records, where the patient link is kept and nobody is handed an opening by default, the advantage narrows to the entry. In SPE logs the subject link and payload go at the ceiling while the accessor fields stay, and there the commitment does work deletion cannot. The sixth §7.2 statement is calibrated to match: what it adds to the practitioner pattern is a combination whose parts are standard (NIST SP 800-57 section 7.6 already records destroyed keys in audit logs; Crosby and Wallach for tamper-evident logs), plus the partition into accessor fields and what erasure and the ceiling reach. Against unlogged deletion it improves on assurance; against deletion logged in the same tamper-evident log, its advantage is confined to the commitment.

**Worked example.** Record 100 after invalidation: under delete-and-log the auditor learns something was deleted; under the mechanism the auditor also holds c(a) = 678ade47c1e6dc03... bound at write time.

**Concede and hold.** Concede it plainly: the weight of the thesis lies in the semantics and the necessity analysis, not the commitment. Hold: the contribution is a feasibility characterisation and verifiability parameter, which crypto-shredding as practised does not have.

**Point to.** §2.4 pp. 23 to 25; §4.10 p. 71; §6.3 p. 94; §7.2 p. 104. Slides 18, 28.

---

# 6. Evidence and validity

### Q29. [Either] "What do your 200 records actually show?"

**Short answer.** Read "verifiable" as "readable" and 90 records fail, with 95 violations. Read it as "accountable" and none fail. The counts follow my generator; what is checked is the shape of the result, not a frequency.

**Full answer.** The run generates 200 audit records: 100 cross-border (floor 120 months, request probability 0.40) and 100 from research environments (floor 12, permit expiry 1 to 12 months after creation, request probability 0.25), seed 20260915. Under Semantics I, 90 records violate: 37 cross-border (all C2) and 53 SPE. The 95 violations count 5 SPE records twice, because they collide with both the erasure deadline and the ceiling. By cause: 41 C2 only, 44 C3 only, 5 both. Of the 78 SPE records with no request, 39 collide with the ceiling alone, which is Corollary 1.2. The conditional shape of Proposition 1 is reproduced: 38 cross-border requests, 37 inside the window and all 37 violate; the one outside the window does not. Under Semantics II, 138 records are invalidated (52 cross-border, 86 SPE) and violations are zero. The generator is built so that the structure is visible, not so that the rates are realistic, and the thesis says so at each table.

**Worked example.** Record 3 is one of the 37; record 100 is one of the 39; record 38 is the cross-border request outside its window.

**Concede and hold.** Concede the zero under Semantics II holds by construction (Q6). Hold: the integrity check can fail, and does under tampering.

**Point to.** §5.3 to §5.4 pp. 83 to 85; §5.7 p. 87; Tables 5.3, 5.6. Slide 12. App ?p=ledger.

### Q30. [Either] "How was it checked? Is any of it independent?"

**Short answer.** Three checks: an exhaustive search over every yes-or-no assignment on small cases, a Z3 solver hunting for counterexamples, and a swap of the payloads for generated health records. None is independent of me, and the thesis declares that. They check my code against my encoding, not my encoding against the law.

**Full answer.** The exhaustive search enumerates 2^14 = 16,384 assignments per case on four cases: three conflicts are infeasible and the control is feasible. It is a sanity check, since the constraints are pointwise, and it shares two constants with the checker, so it is not independent. Z3 is a bounded check over floors 1 to 120, response periods 1 to 3 and a horizon of 140 months: 9 of 9 properties return no counterexample, and four deliberately broken variants (no invalidation entry, no commitment, no subject-link entry, Proposition 3 off by one) each return a counterexample, which is what gives the check evidential weight. The Synthea swap replaces payloads with 98 generated FHIR R4 bundles: all 200 commitments change and all six result measures are identical, because no constraint reads content. The checker, the cross-check and the Z3 script were written in the same AI-assisted process (declared on p. xi). The tests pass (63 at release 1.3.4; the thesis reports 56 at 1.3.0).

**Worked example.** At response period 3, Semantics I falls from 95 to 94 violations (90 to 89 records); the Corollary 1.2 count stays 39, because the ceiling does not involve the response period.

**Concede and hold.** Concede there is no proof assistant and no independent implementation. Hold: the propositions are short enough to be checked by hand (Part B), and the mutations show the checks can fail.

**Point to.** §5.5 to §5.6 pp. 85 to 87; A.23 p. 150; Declaration p. xi. Slides 12, 24. App ?p=robust.

### Q31. [Either] "Synthetic data. What can it show, and your patients are American."

**Short answer.** It shows structure: when rules collide and when they do not. It cannot show how often this happens in Norway. The model reads timing, never content, so which patients are generated does not move any figure, and the swap proves it.

**Full answer.** What synthetic data can show here: Proposition 1's conditional shape; invariance to payload content; that the checks can fail. What it cannot: frequencies, real permit durations (the uniform 1 to 12 months is an assumption), the share of valid requests (all are treated as valid), or Norwegian clinical practice. The choice is also an ethical one, grounded in Datatilsynet's 2021 decision on testing with real data (the Norges idrettsforbund case, §3.5), and no real data were used. Synthea's default profile is US Core, and FHIR R4 matches the Norwegian basisprofiler, so format fits; content is irrelevant to the constraints. When 200 of 200 commitments changed after the swap and no figure moved, that was the intended result: it shows the constraints are about time and rights, not about what the record says.

**Worked example.** Record 100's commitment changes with its payload (678ade47... to a different value) and its violation status does not.

**Concede and hold.** Concede that frequencies cannot be inferred; the thesis never infers them. Hold: a feasibility claim needs witnesses, not a sample.

**Point to.** §3.5 pp. 41 to 42; §5.8 p. 89; §6.7 p. 97; Table 5.7 p. 90. Slide 26. App ?p=synthea.

### Q32. [Either] "Is your result sensitive to the numbers you chose: floor, response period, ceiling?"

**Short answer.** The pattern is not; the counts are, and they are not claimed. Corollary 2.2 says no result depends on the floor, and Semantics II gives zero violations at every setting I ran.

**Full answer.** Proposition 1 gives the condition for collision as t_r + delta <= t + F, so shrinking F shrinks the set of colliding records without changing the form. The thesis reports one sensitivity (response period 3: 95 to 94 violations; Table 5.5). The repository's `sensitivity.py` (not in the thesis; run it once yourself before the defence) gives a floor sweep: with the ceiling applying, floor 120 gives 95 violations over 90 records, floor 72 gives 83 over 78, floor 36 gives 66 over 61; with the ceiling excluded (the narrow reading) they are 46, 34 and 17 records; Semantics II gives zero violations in every row and 138 invalidations with the ceiling applying, 60 without. The six-year Norwegian pilot floor is 72 months, so the sweep covers it.

**Worked example.** At six years record 3's floor ends at month 83, its deadline is 116, no collision. The rows above show how many records behave like it.

**Concede and hold.** The sweep is not in the submitted thesis: say "the repository's sensitivity script" and no more [Since submission: sensitivity.py is in code releases 1.3.3/1.3.4, made for the journal article; the thesis cites 1.3.0.]. Hold: Corollary 2.2 (F arbitrary) is in the thesis, p. 62.

**Point to.** §4.7 p. 62; §5.6 p. 87; Table 5.5. Slide 24. App ?p=robust.

### Q33. [Either] "What does the model leave out, and what is not deployed?"

**Short answer.** Every request is treated as valid, a payload is one block, a month is the unit, and nothing is deployed: no contact point, no performance figures, keys destroyed only in memory. Frequencies are unreliable; the propositions are not.

**Full answer.** The model's declared limits (§3.7): (1) C1 is closed and so conservative; (2) C2 binds from the start of month t_r + delta, so boundary months can be grid artefacts; (3) all requests are treated as valid, which inflates frequencies, since an invalid request would not set a deadline; (4) the payload is one unit, so field-level redaction is outside the model (Corollary 2.3 covers one case). Not done in the artefact: the NCPeH connection, the OpenNCP flow, authentication, consent, timing, hardware custody. Specified, not built: published roots with consistency proofs, the leaf nonce, the terminal transition, proactive invalidation, the accumulator (§6.1). Integration with Norway is by specification (Table 4.1), not by test. Appendix A.9 lists five known limitations of the artefact itself. The expert panel (Appendix C) is designed, not run, and awaits Sikt notification.

**Worked example.** Record 3 at response period 3: deadline 118, still inside the window, so the result survives the grid choice.

**Concede and hold.** Concede all of it; the list is in the thesis. Hold: a feasibility result survives imperfect frequencies, because it is an existence statement.

**Point to.** §3.7 pp. 44 to 45; §4.3 p. 51; §6.1 p. 91; §7.5 p. 107; A.9. Slide 14.

---

# 7. Norway

### Q34. [Either] "Helsedirektoratet's six years against your ten. Where does the floor come from?"

**Short answer.** I asked. Helsedirektoratet replied on 19 October 2026 that no specification fixes a period, that it is left to national law, and that for the pilot they decided six years, with the production figure still to be decided by them as controller. So I treat the floor as a parameter and use ten years only as an illustration.

**Full answer.** The enquiry went to Helsedirektoratet's central mailbox on Monday 5 October 2026; the reply came from Hans Löwe Larsen, Avdelingsdirektør, Division of Information Management and Method, and is reproduced with permission in Appendix D (D.1, p. 168). He finds no retention length in the requirements catalogue or the named specifications (Security Services, System Architecture, NCPeH Architecture, Audit Trail Profile), which refer to national law without fixing a period or manner of storage. Ten years was an unsourced figure from secondary literature, so I do not use it as a fact. Because the reply attributes six years to the pilot decision of a controller, §4.2 draws the consequence: absent a national legal basis, six years is a policy floor, so before Art 9 EHDS applies in 2029, keeping the patient link against an erasure request has no secure Art 17(3)(b) basis. The thesis does not say any Norwegian law sets six years.

**Worked example.** At six years record 3's floor ends at month 83; its request at month 116 falls after, so no collision. At ten years it falls inside.

**Concede and hold.** Concede the reply is one email, from one officer, and the production period is undecided. Hold: no result depends on F (Corollary 2.2).

**Point to.** §2.3 pp. 17 to 18; §4.2 pp. 50 to 51; Appendix D p. 168. Slides 4, 14, 31. App ?p=norway.

### Q35. [Either] "Where does this attach to Norway's systems, and who decides?"

**Short answer.** At two narrow points: the last step of the cross-border exchange, where the audit record is written, and the logging boundary of a research environment. It asks nothing new of Norway's systems.

**Full answer.** The NCPeH is run jointly by Helsedirektoratet and Norsk Helsenett; the mechanism attaches at step six of the OpenNCP flow, where the audit message is stored. Because Norway is not an EU member, the Regulation reaches it only once incorporated into the EEA Agreement, so these attachment points are where the national authorities would act, not where any duty already binds them. Folkehelseinstituttet is the Ministry-designated coordinating Health Data Access Body; Helsedataservice, within FHI, decides access for eleven central registries; how many bodies Norway will have is not settled (§2.6). Secure processing environments (TSD, SAFE, HUNT Cloud under NORTRE) are fragmented, down to disconnected PCs (SPUHiN 2024), so the mechanism works on the log every environment must produce. It adds no requirement of a new kind to the national criteria (an information security management system, tamper-proof logs). The thesis reads Table 4.1 as the integration map: component by component, what each party would do.

**Worked example.** Record 3 is written at the NCPeH audit repository; record 100 at an SPE logging boundary under permit DP-015.

**Concede and hold.** Concede integration is specified, not tested; no Norwegian operator has seen this. Hold: nothing here needs a new system.

**Point to.** §4.11 pp. 73 to 74; Table 4.1 p. 74; §2.2 p. 16; §2.6 p. 28. Slide 15. App ?p=norway.

### Q36. [Either] "Which authorities have you asked, and what is still open?"

**Short answer.** Two letters. Datatilsynet got the GDPR-side questions on 23 September 2026, with no reply at submission. Helsedirektoratet answered the floor question on 19 October. The EHDS-side question, whether Art 68(12) reaches patient-level logs, is still to ask.

**Full answer.** Keep the two apart; they answer different questions and must not be merged into "the authorities were asked". Datatilsynet (23 September, Appendix D.2 p. 169) was asked the GDPR-side questions of §7.4, including whether an invalidated record discharges a retention obligation. Helsedirektoratet was asked the floor only (Q34). Still to ask, of Helsedirektoratet, the Ministry or the Commission: whether Art 68(12) reaches patient-level logs, and whether Art 73(1)(e) needs the subject link after the ceiling. If an authority says identifiable logs must stay readable, Proposition 2 stays true of the model and becomes "practically inert" (§6.2). If Datatilsynet has replied since submission, say what it says and nothing more than it says. [CHECK: the status of the Datatilsynet reply as at the defence date; the thesis records none at submission.]

**Worked example.** A "no" on the first question makes the move fail cleanly and shows exactly what would have to change: the semantics, not the arithmetic.

**Concede and hold.** Concede that the legal argument is incomplete without them, and that I should have asked earlier (Q42). Hold: the thesis labels both questions open in §7.4.

**Point to.** §6.2 p. 92; §7.4 p. 106; Appendix D pp. 168 to 169. Slides 14, 22. App ?p=start.

### Q37. [Either] "What does Helsedirektoratet's own privacy notice say? And what Norwegian law applies?"

**Short answer.** The notice is not in the thesis, so I treat it as extra evidence from my article source check, not a thesis claim. It states six years for the accessor fields and cites GDPR Art 6(1)(c) with pasientjournalloven section 22 as the basis for the logging. Say exactly that and no more.

**Full answer.** Helsedirektoratet's public privacy notice, revised 30 June 2026 [Since submission: Helsedirektoratet privacy notice, last revised 30 June 2026, checked 27 Nov 2026. Not in the thesis; say "since submission".], states six years for the accessor fields: name, HPR number, role, institution, place and time of lookup. These are the same fields the mechanism keeps for the floor. Precision matters: the notice names section 22 as the legal basis for the logging; it does not say section 22 itself sets six years, and Larsen's reply says the period was a pilot decision. Do not write "since submission": the notice predates it. On the wider question, the thesis finds no national provision that fixes the period, and §4.2 states the consequence (Q34). EEA status: the Regulation is being processed for incorporation into the EEA Agreement, and the thesis dates are subject to that [Since submission: the EFTA register (26 Nov 2026) lists the EHDS Regulation as under scrutiny for incorporation, not yet incorporated.].

**Worked example.** The six-year floor for accessor fields matches what record 3 keeps after invalidation: actor, role, institution, time, and the logged invalidation.

**Concede and hold.** Concede the notice is secondary evidence for a figure the thesis rests on a letter for. Hold: the two sources agree on six years, and neither claims it is law.

**Point to.** Not in the thesis; §2.3 p. 17 and Appendix D p. 168 for the six years; §1.1 p. 1 for EEA. Slides 4, 31.

---

# 8. Programme fit

### Q38. [Ferreira] "This is a logistics degree. Where is the logistics?"

**Short answer.** There is no optimisation and no objective function, and I do not claim one. The logistics is in the object and in one design decision. An audit record is information in storage with a planned exit, and customs keeps the record after the goods are destroyed; Semantics II does the same.

**Full answer.** CSCMP defines logistics as the flow and storage of goods, services and related information (§2.7). An audit record is related information, and the thesis is about its storage and its exit. The floor is a per-record parameter, taken from chain-of-custody practice, which is why the cross-border floor and the SPE floor are one constraint with two instances (§4.3). Proposition 3 is a two-clock perishability result: a record held against a floor, while a deletion clock runs from an external event, collides exactly when the event comes soon enough, and the text alone does not reveal which records. The method is constraint modelling in the operations-research tradition, and the framing comes from four years in cross-border procurement (§1.4). Record 3 behaves like a consignment: made at one node, carried through a six-step gateway, held under rules set elsewhere.

**Worked example.** Customs: goods are destroyed under order, the declaration stays for years. Record 3: payload destroyed at month 116, accessor record stays to 131.

**Concede and hold.** Concede no logistics metric is optimised. Hold: the thesis says so in §1.5 and §2.7, and the claim is about information logistics, not freight.

**Point to.** §2.7 pp. 30 to 31; §1.4 p. 7; §1.5 p. 8; §6.9 p. 99. Slide 20. App ?p=anchor.

### Q39. [Ferreira] "The programme is about sustainable energy. Where is the energy?"

**Short answer.** There is none in the result, and §1.5 says so: no energy measurement and no saving is claimed. The fit is the logistics of information. The nearest energy case is Elhub, whose retention rule has the same form as my floor, and testing it is the next step.

**Full answer.** The fourth exclusion in §1.5 states that the thesis claims no energy result. Elhub, Norway's electricity data hub, keeps customer data for three years and 41 days after a contract ends (Elhub, privacy statement, 31 March 2026): a floor anchored to an event, which is the same form as my floor parameter, so the floor-against-right part of the model applies directly. Whether Elhub also has a deletion ceiling that collides with the floor is exactly the Proposition 3 test, which I have not run, and §7.5 names it as the first application. Smart-meter data are personal data under the same regime, so the problem is not remote from the programme's subject. Do not say the thesis shows anything about energy.

**Worked example.** An event-anchored floor of three years and 41 days against an erasure right is Proposition 1's shape; a ceiling from the same contract end would be Proposition 3's.

**Concede and hold.** Concede nothing in the thesis is about energy, and that Elhub as it stands is floor against right, the bilateral case I say is not the contribution; the ceiling test is the open part. Hold: the generalisation is stated as future work (§7.5), not as a result.

**Point to.** §1.5 p. 8; §2.7 pp. 30 to 31; §7.5 p. 107. Slide 20.

---

# 9. Novelty and competitors

### Q40. [Either] "What is new, and what is borrowed?"

**Short answer.** The cryptography and the method are borrowed. What is new is putting a keep rule, an erasure right and a deletion limit on one record in one model, finding that the word "verifiable" decides whether all can hold, and showing where the clash hides. I also specify the mechanism and check its residue.

**Full answer.** Borrowed, and credited (§2.4 to §2.5): hash-chained logs (Schneier and Kelsey, 1999), Merkle proofs (Crosby and Wallach, 2009), Certificate Transparency (Laurie et al., 2013), hiding commitments, cryptographic erase (NIST SP 800-88 Rev. 2), the Ephemerizer, Vanish and policy-based deletion, and formal compliance as satisfiability (Feng et al., 2023). The log-editing family (chameleon hashes, redactable signatures, blockchains) is rejected, not borrowed. What the thesis claims as new in the reviewed literature (§2.10, p. 36): the formal tri-lateral characterisation, verifiability as the deciding parameter, the anchor condition (Proposition 3), the information-logistics expression of the problem, the cross-border health instantiation on the Norwegian substrate, and the residue analysis. The Statement of Contribution (pp. ix to x) states the claim as one of framing and feasibility, and the sixth §7.2 statement was calibrated down for the combination.

**Worked example.** DePaul keeps recoverable copies to a purge date; record 100's readable copy must be gone at month 16 though its floor runs to month 19.

**Concede and hold.** Concede "just framing" if pressed: a contribution of framing and feasibility, and p. x says so. On prior art (formal GDPR erasure deadlines, deadline-triggered key destruction, keys for intersecting deletion sets, all seven or more years old): the claim is bounded to the reviewed literature, the search is logged in Appendix B, and policy-based deletion (2013) is credited in §4.8 (see Q26). Hold: what is claimed as new is the combination over a floor, a right and a ceiling.

**Point to.** Statement of Contribution pp. ix to x; §2.8 p. 32; §2.10 p. 36; §7.2 p. 104. Slides 18, 28.

### Q41. [Either] "Who else has done this? Why does yours differ?"

**Short answer.** Others did pieces: blockchain audit logs, zero-knowledge access control, key destruction. None treats a keep rule, an erasure right and a deletion limit together, or says what an auditor can check once the payload is gone.

**Full answer.** Table 2.1 (§2.8, p. 32) and the six rivals of §4.10 give the comparison.

| Competitor | What it does | How TRF differs |
|---|---|---|
| KONFIDO (Natsiavas et al., 2021) | OpenNCP toolkit, SGX, blockchain audit | Erasure unresolved; hardware-bound |
| ZK-EHR (Albalwy, 2026) | Groth16 credential proofs, one jurisdiction | Access control, not retention |
| DePaul (Scope and Rasin, US 12,425,209) | Recoverable encrypted copies, key destroyed at a purge date | Fine for two floors; recoverable copies are what a ceiling forbids (Rival 5) |
| Crypto-shredding pattern (VeritasChain, 2026) | Per-subject key destroyed on request | Bilateral, asserted, no model or verifiability semantics |
| Redactable chains, chameleon hashes | Editor rewrites content | This log is never edited |

Also rejected in §4.10: rely on Art 17(3)(b) alone, anonymise (breaks C1), minimise at capture, export logs (Proposition 4). Aikebaier (2026), a preprint, formalises erasure only.

**Worked example.** Rival 5 on record 100: holding recoverable ciphertext to month 19 is exactly what the month-16 ceiling forbids.

**Concede and hold.** Concede that against deletion logged in the same tamper-evident log the advantage is confined to the commitment (Q28). Hold: no reviewed work models the three constraints together.

**Point to.** §2.4 pp. 21 to 25; §2.8 p. 32; §4.10 pp. 70 to 73. Slides 18, 28.

---

# 10. Hostile or meta

### Q42. [Either] "What would you do differently? If you had another year, what first?"

**Short answer.** I would ask the authorities earlier, because no modelling replaces their answers. I would run the expert panel. And I would build what I only specified, starting with published roots so the log cannot be quietly rewritten.

**Full answer.** First, the two authority questions: Datatilsynet on whether accountability-preserving verifiability discharges retention (asked 23 September, no reply at submission), and, on the EHDS side, Helsedirektoratet, the Ministry or the Commission on whether Art 68(12) reaches patient-level logs. A "no" from either would refute a specific step cleanly. Second, the Appendix C panel, after Sikt notification: utility and acceptance are not evaluated, and that is a real gap in a design science thesis. Third, technically: published roots with consistency proofs, the per-leaf nonce and the terminal transition, which a cryptographer would close first. The research problem I would take next is proving completeness of invalidation for one subject without revealing the set, where a zero-knowledge argument over the published root becomes necessary rather than decorative (§7.5). Also real permit durations, and the Proposition 3 test on Elhub. Process lesson: an earlier draft, discarded in May 2026, cited works that do not exist (p. xi), and every citation has since been checked.

**Worked example.** The record-100 commitment in the reported run is not hiding; `--random-salts` fixes it, and I would make that the default.

**Concede and hold.** Concede the late authority questions. Hold: they are stated as open in §7.4, not hidden.

**Point to.** §7.4 p. 106; §7.5 p. 107; §5.2 p. 80; Declaration p. xi.

### Q43. [Either] "How did you use AI, and can you explain the code line by line?"

**Short answer.** Claude was my research and drafting assistant and wrote the Python code, Archify made the diagrams, Parallel AI helped with retrieval. All design decisions, the model, the legal arguments and every accept-or-reject choice are mine, and I answer for the whole. I can walk you through each function.

**Full answer.** The Declaration (p. xi) names Claude for literature search and verification, critique, drafting to my direction and the Appendix A code; Archify for figures; Parallel AI for retrieval. The submission-form declaration also lists K-Dense skill instructions run inside Claude; if asked, say both [Submission-form declaration listed Claude, Parallel AI, Archify and K-Dense; the thesis text p. xi names Claude, Archify and Parallel AI.]. Ownership is the highest-risk viva item (RT2 V-5), so know the functions in `trf_checker.py` (release 1.3.4 line numbers; A.10 prints the listing):
- `alpha` (line 296): the payload is readable before the earliest deadline and not after.
- `apply_invalidation` (270): log the access; delete key, salt and payload; write the invalidation entry with month, ground ("Art 17(1)" wins a tie) and authorising actor; remove the subject link for SPE records only.
- `V_II` (305): checks the log proof, the commitment, and an entry for every loss of payload and link.
- `MerkleLog.proof` (104) collects the sibling hashes up the tree; `verify` (114) rehashes and compares to the root.
- `check_semantics_II` (321) applies V_II to every record.

**Worked example.** `python3 trf_checker.py` prints 95 violations across 90 records, then 0.

**Concede and hold.** Concede the code was written with AI. Hold: I can run it, change a constant and predict the effect, and the checks guard against implementation error, not model error.

**Point to.** Declaration p. xi; A.10 pp. 124 to 129; §5.2 p. 80. App ?p=run.

### Q44. [Either] "Why 'VERA-SNARK' if there are no SNARKs?"

**Short answer.** There is no SNARK, and the thesis says so. The name comes from my NORS 2025 presentation, where I planned zero-knowledge proofs. The formal analysis showed that commitments and a logged registry are enough, so I dropped them. That is the design cycle working.

**Full answer.** The Statement of Contribution (p. x) carries a note on the name, and §1.6 and §3.2 record the step: Hevner and Peffers expect the artefact to change as evaluation teaches something. The mechanism is named Crypto-Erasure by Invalidation, and nothing in it needs a succinct proof: inclusion proofs on a Merkle log, a salted commitment and a logged registry give an auditor everything Proposition 2 requires. Zero knowledge returns at one point, which is a future problem: proving that all of one patient's records were invalidated without revealing which they are (§7.5; Aikebaier's fourth open problem). An auditor seeing record 3's invalidation is fine; proving "every record of hers was invalidated" without listing them would otherwise expose her care history.

**Worked example.** The point at which zero knowledge would matter: record 3 is one of a patient's many records; completeness over all of them is the open proof.

**Concede and hold.** Concede the name is a historical label. Hold: continuity with NORS 2025 is why it stays, and p. x says so.

**Point to.** Statement of Contribution p. x; §1.6 p. 9; §3.2 p. 38; §7.5 p. 107. Slide 19. App ?p=built.

### Q45. [Either] "Your invalidation entry names the right that was exercised, and keeps the record identifier. Doesn't the log itself need erasing at the end?"

**Short answer.** Yes, at the end. The terminal transition, one month after the floor, destroys the identifying fields and generalises or destroys what the entries carry. It is specified, not implemented, and whether the residue then resists isolation, linkage and inference is for a documented threat model to establish, not something the thesis assumes.

**Full answer.** The entry carries the record identifier, the ground, the month and the authorising actor, so a ground of "GDPR Art 17(1)" reveals that someone exercised a right, and the registry would hold it for ever if nothing ended it. The thesis agrees that the storage-limitation principle (Art 5(1)(e)) forbids keeping identifiable metadata beyond its purpose. At t + F + 1 the terminal transition destroys the identifying fields, the key, the salt and any remaining ciphertext, leaving only event type, document category, outcome and commitment. It is itself logged. §4.8 says what remains is the one state intended to be anonymous rather than pseudonymous, but conditionally: the record identifier and actor in the entries "must be generalised or destroyed", and the residue must pass the Board's isolation, linkage and inference test (draft Guidelines 02/2026). Where a longer obligation applies (archival duty, litigation hold) the transition is deferred by raising F, which the model already supports. In the reported run there is no terminal transition, so the entries do carry the ground.

**Worked example.** Record 3's entry (month 116, Art 17(1)) lives to month 132, when the terminal transition would remove the identifying fields.

**Concede and hold.** Concede the run does not implement it, and that "anonymous" is claimed only for the final state and conditionally. Hold: the thesis names the problem and its test.

**Point to.** §4.8 p. 67; §4.9 pp. 68 to 69; §6.1 p. 91. Slide 27.

### Q46. [Either] "What would refute you? What if an authority says no?"

**Short answer.** Two things refute parts, and I say which. If an authority holds that identifiable logs must stay readable, Proposition 2 stays true of the model and becomes practically inert. If Art 68(12) does not reach logs, Corollary 1.2 falls. The propositions, the mechanism and the semantics stand either way.

**Full answer.** The thesis is a conditional argument with the conditions named: two principal interpretive steps (that the right and the ceiling reach the audit record, and that an accountability reading of verifiable is defensible) and four subsidiary premises, with no regulatory authority behind any (§3.7, Abstract). A no on the first question makes the move fail, and shows what would have to change: the semantics, not the arithmetic. A no on Art 68(12) removes the single-record three-way collision: of the 90 violating records, 46 remain (37 cross-border and 9 SPE). Cross-border requests still collide under Proposition 1. Technically, a counterexample to Proposition 2's trajectory, an invalidation entry that fails its proof without tampering, or a record on which the checker and Z3 disagree would refute the artefact, and four deliberate mutations show those can be found. What would not refute it: a regulator who dislikes the word "verifiable"; that is a rival semantics, argued in §4.2.

**Worked example.** Under the narrow reading the 44 ceiling-only collisions lapse; 5 SPE records that also have a request inside the window stay violating.

**Concede and hold.** Concede there is no authority yet. Hold: the thesis lists what each answer would do, in §7.4.

**Point to.** §3.7 p. 44; §4.6 pp. 58 to 59; §6.2 p. 92; §7.4 p. 106. Slides 14, 22.

---

# Numbers you must say right

Say "in the model" and "generated" every time a count leaves your mouth. All re-run at release 1.3.4 unless stated.

| Figure | What it is | Where |
|---|---|---|
| 200 records | 100 cross-border (F = 120, primary) + 100 SPE access logs (F = 12, secondary); seed 20260915 | §5.2, Table 5.2 |
| 95 violations across 90 of 200 (45%) | Semantics I; 37 cross-border, 53 SPE | §5.3, Table 5.3 |
| 41 / 44 / 5 | C2 only / C3 only / both (all SPE), so 95 = 90 + 5 | §5.3 |
| 38 requests, 37 inside, 1 outside | Cross-border; record 38 is the one outside | §5.3 |
| 39 of 78 | SPE records with no request that still collide (Cor 1.2, broad reading) | §5.4 |
| 22 SPE requests; 9 survive narrow reading | 4 + 5; the 44 ceiling-only collisions lapse | §5.4 |
| Record 100 | created 7, permit expires 10, C3 from 16, C1 to 19, collision 16 to 19 | Figure 5.2 |
| Record 3 | created 11, floor to 131, request 115, deadline 116 | §5.3 |
| 0 violations | Semantics II; 200 of 200 verify; 3 tamper tests fail | §5.7, Table 5.6 |
| 138 invalidated = 52 + 86 | Art 17(1) and Art 68(12) grounds; four same-month ties recorded under Art 17(1) | Table 5.6 |
| Commitment 678ade47c1e6dc03... | Record 100; with `--random-salts`, 483ca80e... | §5.7 |
| delta = 3 | 94 violations, 89 records, 39 unchanged, 138, 0 | Table 5.5 |
| 2^14 = 16,384 per case, 4 cases | Exhaustive search, sanity check | §5.5 |
| 9 of 9 Z3, four mutations refuted | Bounds: floor 1 to 120, delta 1 to 3, horizon 140 | §5.5, A.24 |
| 98 bundles; 200 of 200 commitments change; 0 figures | Synthea swap | Table 5.7 |
| 138 refuse, 62 read | AES-256-GCM module | §5.8, §6.3 |
| 60 records, 7 violate, 0 without request | politiregisterloven section 17 | §6.10 |
| Floors 72 / 120 / 36 / 12 months | Pilot / illustrative / Art 9(2) from 2029 / SPE Art 73(1)(e) | §4.3 |
| delta 1, extended 3 | GDPR Art 12(3) | §4.4 |
| 26 Mar 2027 / 26 Mar 2029 | General application and implementing acts (Art 73(5)) / Arts 68 and 73 apply | §1.2, §6.8 |
| 5 Oct / 19 Oct 2026; 23 Sep 2026 | Helsedirektoratet enquiry and reply; Datatilsynet enquiry | App D |
| 8 limitations; 6 rival designs | | §3.7; §4.10 |
| 56 tests (thesis, 1.3.0); 63 tests (1.3.4) | | A.2 |
| Release 1.3.0 cited; app 1.3.2 | [CHECK: repository is at 1.3.4; the app's current release was not verified] | A.1 |

# Words to use, words never to use

| Use | Never | Why |
|---|---|---|
| "attested" destruction | "proven", "verified" destruction | §4.7, §6.3 |
| "pseudonymised" residue | "anonymous", "anonymised" | §4.9 |
| "proposition"; "proved" for 1 to 3, "argued" for 4 | "theorem"; "four results proved" | §4.7, §4.10 |
| "in the model" | "the law requires", "is lawful" | §4.7 |
| "tamper-evident against a published root" | "tamper-proof", "immutable", "cannot be rewritten" | §4.9, §7.2 |
| "specified, not implemented" | "the system does" | §6.1 |
| "synthetic", "generated", "counts set by the generator" | "real", "45% of records violate" as a fact | §5.3, §6.7 |
| "on the broad reading, for entries that are themselves electronic health data" | Cor 1.2 without its condition | §4.6 |
| "a defensible reading, argued, not confirmed" | "the reading the law requires" | §4.2, §6.2 |
| "sanity check", "separate code" | "independent verification" | §5.5 |
| "simulated in program memory" | "keys destroyed", unqualified | §5.8 |
| "the Board describes key deletion as making data unintelligible" | "the EDPB endorses crypto-erasure" | EDPB 02/2025 paras 51, 125 |
| "the 2017 OpenNCP reference source" | "deployed repositories behave this way" | §4.5 |
| "verifiable qualifies the invalidation record" | "erasure is verifiable" | §1.4 |
| "no optimisation, no objective function" | "a logistics optimisation model" | §2.7 |
| "the pilot decided six years" | "Norwegian law requires six years" | App D |

# Known weaknesses (own them first)

Open with the concession, bound it in one sentence, point to the page.

| # | Weakness | Honest line | Where |
|---|---|---|---|
| 1 | Props 1 and 3 near-immediate; Prop 2 by construction | "Yes. The weight is in the necessity analysis and the mechanism." | §4.7 |
| 2 | Semantics II zero holds by construction | "Falsifiable part is the integrity check; three tamper tests fail it." | §5.7 |
| 3 | Exhaustive search not independent | "A sanity check; Z3 with refuted mutations carries robustness." | §5.5 |
| 4 | Code, cross-check and Z3 from one AI-assisted process | "Declared; they check code against encoding, not encoding against law." | p. xi |
| 5 | No published roots | "Tamper-evident against a published root; specified, not built." | §4.9 |
| 6 | Reported run's salts not hiding (and the link salt brute-forceable from a 100-value pseudonym space) | "Derived for reproducibility; `--random-salts` exists; the design requires hiding." | §5.2, A.10 |
| 7 | Terminal transition, leaf nonce, proactive invalidation, accumulator unimplemented | "Specified, not implemented; none is in an executed proposition." | §6.1 |
| 8 | Key destruction simulated | "Program memory; AES shows unreadability, not destruction." | §5.8 |
| 9 | Prop 4 argued, not proved or run | "A legal argument in the form of a proposition." | §4.10 |
| 10 | Two principal interpretive steps, four premises, no authority | "Listed in one place and put to the authorities." | §3.7, §7.4 |
| 11 | Six-year floor is a controller decision | "No national legal basis identified; a finding for the controller." | §4.2 |
| 12 | ITI-55 identifier case | "Where an identifier is used, cross-border invalidation removes little." | §4.10 Rival 3 |
| 13 | Rival 4 close to equivalent for cross-border | "Conceded: the edge is the attributed entry; the commitment bites in the SPE case." | §4.10 |
| 14 | Every request valid, per record not per subject | "Inflates frequencies; no result is a frequency." | §3.7 |
| 15 | Synthea is US Core | "No constraint reads content; the swap proves it." | §5.8 |
| 16 | Semantics I evidenced by one reference implementation | "2017 source and 2026 schema; others not inspected." | §4.5 |
| 17 | Code version: 1.3.0 cited, later viewer hosted | "Result modules byte-identical across releases." | A.1 |
| 18 | Run A.17 needs an uncommitted cohort | "Seven of eight recorded runs re-run byte for byte." | A.2 |
| 19 | Evaluation artificial; panel not run | "Designed in App C; utility not evaluated." | §3.8, §6.6 |
| 20 | No optimisation in a logistics thesis | "Conceded; the fit is the object and Prop 3." | §2.7 |
| 21 | SPUHiN hearing page withdrawn; final D5.2 unchecked | "Stated as an exception in the Declaration." | p. xi |
| 22 | Per-record keys vs per-subject/permit shares (policy-based deletion, 2013) | "A simpler construction exists; per-record is the simplest, not required; not implemented." | §4.8 |
| 23 | Invalidation entry names the right exercised | "The terminal transition is the end; not built." | §4.8 |
| 24 | Stated but untested: Elhub, "without modification" | "First application; Prop 3 test not run." | §7.5 |
| 25 | Whether the institution confirms the declaration wording | [Thesis submitted 27 Nov 2026 with the declaration as written.] | Declaration |

# Thirty-second answers

**What is the contribution?** "Cross-border health audit records face a retention floor, the right to erasure and, in research environments, a six-month deletion ceiling. I model the three as constraints over one variable: can the payload still be read. If verifiable means readable, the system is infeasible whenever a deadline falls inside the record's window. If verifiable means the accountability fields, a commitment and a logged invalidation are intact, it is satisfiable for every pattern and floor. The proof's trajectory is the mechanism: delete payload and key, keep the accessor fields, log the invalidation. All of this is in the model, not yet in law."

**What is novel?** "Not the cryptography and not the method. What is new in the reviewed literature is applying satisfiability to a floor, a right and a ceiling together, isolating verifiability as the deciding parameter, and Proposition 3: a ceiling collides with a floor only if it is no longer, and the anchor decides whether you can see it in the text. Plus a mechanism whose residue is analysed against Norwegian infrastructure."

**What are the limitations?** "Three. The central interpretive move, that an invalidated record still discharges retention, has no authority behind it, and nor has the broad reading of Article 68(12). Key destruction is attested, not proven, and simulated in my artefact. And the proofs are informal, the demonstration is synthetic, and the counts come from the generator. Published roots, the terminal transition and the accumulator are specified, not built."

**Why should anyone care?** "Because the rules are written and the systems are in pilot, and today a plaintext audit store cannot satisfy them together. The argument costs little to adopt: log every invalidation as an attributed event."

**What did the authorities say?** "Helsedirektoratet: no specification fixes a period, national law decides, six years in the pilot, final decision theirs as controller. Datatilsynet: asked on 23 September, no reply at submission [CHECK: any reply since]."

# The thesis in 60 seconds

"A patient from Molde is treated in Helsinki, and the clinician's lookup is written to an audit log. Three European rules touch that log. One says keep it: six years in Norway's pilot. One lets the patient demand erasure. In research environments a third says health data must be gone six months after the permit ends. If 'verifiable' means 'readable', these cannot all hold: whenever a deletion deadline falls inside the keep period, the payload must be readable and gone in the same month. If 'verifiable' means 'accountable', so we can still show who looked, when, and that the payload was lawfully invalidated, they all hold, for any record and any timing. The mechanism: destroy the payload at the earliest deadline, keep the accountability, log the deletion. I check it on 200 generated records, with an exhaustive search and a solver. I do not claim key destruction is proven, the legal reading is settled, or the counts are real frequencies. Two questions need an authority; I have asked the first."

# The thesis in 20 seconds

"Three European rules collide on one audit record: keep it, erase it, delete it from the research environment. They collide only if 'verifiable' means 'readable'. If it means 'accountable', all three hold. Delete the payload. Keep the accountability. Log the deletion."

# Before the defence

- Open https://trfhimolde.streamlit.app/ the day before; confirm it loads and shows the scoped Proposition 1; keep a screenshot of the ledger and Figure 5.2 (p. 85) as a fallback; backup URL trf-thesis-himolde.streamlit.app.
- Run `python3 trf_checker.py` once on the machine; the output should match `docs/expected_trf_output.txt`.
- Old notes sit in `process/` on a public branch: make the repository private or move them before the examiners open it [CHECK: current state].
- Bring the Lovdata text of politiregisterloven section 17 or avoid the detail (Q18).
- Slide 12's counters animate from zero when presented live; in a PDF export they read 0. If they do not run, say 90 of 200 and 39 of 78.
