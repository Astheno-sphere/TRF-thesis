# Thesis Cheat Sheet

*Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the European Health Data Space.* Plain-language companion to the viva notes, synced slide by slide with the defence deck (slides 1 to 31), the live app and the thesis PDF.

**How to read the references.** [§x.y, p. N] gives the thesis section and the PRINTED page number shown on the PDF page (arabic in the body, roman in the front matter). In the body, printed page = PDF page index minus 14 (PDF page 71 is printed page 57). Wording is checked against `VERA-SNARK_Thesis_SUBMISSION.md`; page numbers against the PDF text of 183 pages.

**App deep links.** `https://trfhimolde.streamlit.app/?p=<slug>&r=<record>&m=<month>`. Slugs: start, witness, propositions, anchor, built, ledger, robust, run, synthea, norway. `r` and `m` act only on witness, and are read once per session (open a fresh tab for a new link). Record 3 and record 100 were checked against the generator (seed 20260915): record 3 is t(a) = 11, F = 120, t_r = 115, actor HP-003 via NCP FI; record 100 is t(a) = 7, F = 12, t_pi = 10, actor R-008, permit DP-015.

---

## 1. The thesis in one paragraph

A cross-border health data access leaves an audit record of who looked. Three rules bind it: keep it for years; erase personal data when the patient asks; delete health data from a research environment six months after the permit ends. The thesis turns the three rules into a small mathematical model and shows that whether they can all be obeyed depends on one undefined word: *verifiable*. If verifiable means "the content is still readable", the rules contradict each other for any record whose deadline falls inside its retention window. If verifiable means "who acted, when and why is intact, the content is bound by a commitment, and its removal is logged", every record can obey all three. The proof of that second result is also the design, Crypto-Erasure by Invalidation. All of this holds *in the model*; whether it holds in law is still an open question [§4.1, p. 48; §7.1, p. 103].

---

## 2. The story of one audit record

**Record 3.** A patient from Molde falls ill while working in Helsinki. A clinician there asks for the patient summary. The request passes through the Finnish contact point; the Norwegian National Contact Point answers it and writes one line in its audit log. That line is not the health record. It is the record of who looked, when and why. In the run it is created in month 11 under the illustrative ten-year floor, so it must stay verifiable until month 131. In month 115 the patient asks for erasure; with one month to respond, the payload must be gone from month 116. If verifiable means readable, months 116 to 131 demand the payload be readable and gone at once. The thesis prints the witness line verbatim: "C1 requires V=1 (=> alpha=1) at t=116 within [11,131]; C2 requires alpha=0 from t=116" [§5.3, p. 83]. The Molde and Helsinki framing is the deck's.

**Record 100.** A researcher works under a data permit inside a Secure Processing Environment (SPE). The SPE logs the access in month 7; the one-year floor keeps the log to month 19. The permit expires in month 10, so the six-month ceiling wants health data gone from month 16. Nobody asked for anything, yet months 16 to 19 carry two opposite demands. Witness, verbatim: "rid=100: t_a=7 permit expires t_pi=10 -> C3 from t=16, C1 to t=19 | collision at t=16" [§5.4, p. 84; Figure 5.2, p. 85].

---

## 3. The three rules, and what each actually says

**The floor (keep).** For SPE access logs, Article 73(1)(e) EHDS requires "identifiable logs of access to and activities in the secure processing environment" and says "logs of access shall be kept for at least one year" [§1.1, p. 2]. For the cross-border audit repository, no eHDSI specification fixes a period; it is left to national law. The Norwegian pilot uses six years (72 months), decided by Helsedirektoratet as controller (Appendix D, section 4 below); the literature reports ten (120 months), used illustratively in the run [§4.3, p. 53]. Once Article 9 applies on 26 March 2029, Article 9(2) EHDS gives a binding three years (36 months) wherever the audit record is what the patient's access information is produced from [§4.3, p. 53; §4.2, p. 51].

**The right (erase).** Article 17(1) GDPR gives the data subject a right to erasure "without undue delay". Article 12(3) sets one month, extendable by two [§4.4, p. 54]. Article 17(3)(b) exempts processing necessary for a legal obligation, but only as far as it is *necessary*, and Article 5(1)(c) requires minimisation. Accountability, the thesis argues, needs who, when, on what basis and with what outcome, not readable content [§4.2, p. 49].

**The ceiling (delete).** Article 68(12) EHDS: "the electronic health data within the secure processing environment shall be deleted within six months of the expiry of the data permit" [§1.1, p. 2; §4.6, p. 58]. It has no exemption like 17(3)(b). On the broad reading it reaches SPE log entries kept at patient-record granularity, since such an entry reveals cohort membership, which is health data. That reading is contestable; its scope "is set by location rather than by provenance" [§4.6, p. 58].

---

## 4. Backing our facts: the data controller's answer

The one figure in the thesis that rests on correspondence is the six-year pilot floor. Appendix D reproduces the reply in full, with the sender's permission [Appendix D.1, pp. 168-169].

**Who and when.** Enquiry sent Monday 5 October 2026 to Helsedirektoratet's central mailbox (postmottak), asking for the source and duration of the NCPeH audit-repository retention requirement. Reply received Monday 19 October 2026 from Hans Löwe Larsen, Avdelingsdirektør (Director of Department), Division of Information Management and Method, Helsedirektoratet [p. 168].

**The essential lines (verbatim Norwegian, then the author's translation, as reproduced):**

1. "Jeg finner ingen spesifikk henvisning til lengden på oppbevaring i requirements catalouge eller tilhørende dokumentasjon" ... "Det henvises til nasjonal lovgivning, men konkretiserer ikke lagringsmåte eller lagringstid." [p. 168]
   Translation: "I find no specific reference to the length of retention in the requirements catalogue or the associated documentation (Security Services Specification, System Architecture Specifications, NCPeH Architecture Specifications, Audit Trail Profile, etc.). Reference is made to national legislation, but neither the manner nor the period of storage is specified." [p. 168]
2. "Under utprøvingen er det besluttet en lagringstid på 6 år, men en endelig beslutning når det går i full produksjon er ikke tatt. Hdir er dataansvarlig og vil ta den beslutningen." [p. 168]
   Translation: "During the pilot, a retention period of 6 years has been decided, but a final decision for when it goes into full production has not been taken. Hdir is the data controller and will take that decision." [p. 169]

(The spelling "catalouge" is the sender's and is reproduced as written.)

**What it supports.**
- *The six-year pilot figure.* F = 72 months is the controller's pilot decision, not a statute. The thesis calls it a policy floor unless a national legal basis is identified [§4.2, p. 51]. It appears in Corollary 1.1: a request in any of the 72 months from t(a) to t(a) + 71 collides with the pilot floor [§4.6, p. 57].
- *The floor is a parameter.* Because the specifications fix no period and production is undecided, the model takes the cross-border floor as a parameter and uses ten years only as an illustrative long value [Appendix D, p. 169; §4.3, p. 53].
- *Corollary 2.2.* Whatever the directorate decides for production, Proposition 2 already covers it: "Because F(a) is arbitrary in the proof, the result holds simultaneously for an illustrative ten-year cross-border floor, the six-year floor of the Norwegian pilot and the one-year Secure Processing Environment floor, and for any national floor substituted for either" [§4.7, p. 61].

**What it does not support.** Semantics II, Article 68(12) or the GDPR side. The Datatilsynet enquiry (23 September 2026) had no reply at submission [Appendix D.2, p. 169].

**How to say it.** "The ten-year figure is from the literature. The controller told me in writing that the specifications leave the period to national law and the pilot uses six years, production undecided: Appendix D. So the floor is a parameter, and Corollary 2.2 makes feasibility independent of it."

---

## 5. The one word: verifiable

The floor says the record must stay *verifiable*. Nobody defines the word [§4.5, p. 55].

**Semantics I, plaintext verifiability.** A record is verifiable exactly when its payload can be read: V^I(a,t) = alpha(a,t). The 2017 OpenNCP reference source behaves this way. No instrument states it; it is a de facto habit [§4.5, pp. 55-56].

**Semantics II, accountability-preserving verifiability.** A record is verifiable when (i) the accessor fields are intact, and so are the subject fields unless their removal is logged; (ii) a binding commitment to the payload survives; and (iii) any loss of readability is recorded in an invalidation entry giving month, legal ground and authorising actor. A record with no readable payload is then not broken: it records an access and its lawful erasure [§4.5, p. 56].

---

## 6. The model in plain words

One record, one clock in months, one question each month: can the payload still be read? [§4.3, pp. 51-53]

- **a** is an audit record, created in month **t(a)**, with floor **F(a)** months. It holds metadata **m(a)** split into accessor fields (who, when, permit, outcome) and subject fields (the patient link), a payload **p(a)**, a commitment **c(a)**, and a key **k(a)**.
- **alpha(a,t)** is the whole state space: 1 if the controller can read the payload in month t, 0 if not. A second variable, **beta(a,t)**, tracks whether the patient link is readable; it matters only for SPE logs on the broad reading.
- **V(a,t)** says whether the record counts as verifiable.
- **t_r(a)** is the month an erasure request arrives; **delta** is the response period; **t_pi(a)** is permit expiry. Either is infinite if it never happens [§4.3, p. 53].

The three constraints [§4.4, p. 54]:

- **C1, floor:** V(a,t) = 1 for every month from t(a) to t(a) + F(a).
- **C2, erasure:** alpha(a,t) = 0 for every month from t_r(a) + delta onward.
- **C3, ceiling:** for secondary records the ceiling reaches (rho(a) = 1), alpha(a,t) = 0 (and beta = 0 where the subject fields are health data) from t_pi(a) + 6 onward.

C1 is written on V; C2 and C3 on alpha. Whether they clash depends on whether V is defined in terms of alpha [§4.4, p. 54].

---

## 7. The propositions and corollaries

The thesis is candid that these are elementary once the semantics are fixed. Propositions 1 to 3 are proved informally and checked in code; Proposition 4 is argued from a stated legal premise [§1.6, p. 9; §3.7, p. 44].

**Proposition 1 (infeasibility)** [§4.6, p. 57].
*Exact:* "Under Semantics I, the constraint system {C1, C2, C3} is infeasible for any record a such that t_r(a) + delta <= t(a) + F(a) or t_pi(a) + 6 <= t(a) + F(a). The second disjunct is tested only for records the ceiling reaches, that is, with sigma(a) = secondary and rho(a) = 1."
*Plain meaning:* if an erasure deadline, or a deletion deadline for a record the ceiling reaches, falls inside the retention window, no schedule works.
*Why true:* at the deadline month C1 needs alpha = 1 and C2 or C3 needs alpha = 0 (record 3, month 116).
*What it does not say:* how often. With no deadline inside the window the record is feasible even under Semantics I. The request-driven case presupposes the payload is not necessary for the floor [§4.6, p. 57; §3.7, p. 44].

**Corollary 1.1 (cross-border)** [§4.6, p. 57]. A request in any month except the last delta months of the window collides: "a request in any of the 72 months from t(a) to t(a) + 71 collides with the pilot's six-year floor."

**Corollary 1.2 (SPE, no request)** [§4.6, p. 57]. For an SPE log with F = 12, if t_pi(a) + 6 <= t(a) + 12, C1 and C3 collide at t_pi + 6, "provided C3 reaches the record. *Where it does, no erasure request is required.*"
*Plain meaning:* two articles of one regulation contradict each other in one environment (record 100).
*What it does not say:* it holds only on the broad reading, for patient-record granularity logs, with activity content that is itself health data. On the narrow reading it lapses; nothing else in the thesis does [§4.6, pp. 57-59; §6.2, p. 92].

**Proposition 2 (feasibility)** [§4.7, p. 60].
*Exact:* "Under Semantics II, the constraint system {C1, C2, C3} is jointly satisfiable for every record a in A, for every arrival pattern of erasure requests {t_r(a)} and permit expiries {t_pi(a)}, and for every floor parameter F(a) in N."
*Why true:* the proof builds the schedule. At t^I = min(t_r + delta, t_pi + 6, t + P) destroy the key, remove the patient link if the ceiling reaches it, and log an invalidation entry; keep accessor fields, commitment and entry. C2 and C3 hold because readability ends by each deadline; C1 holds because Semantics II never reads alpha. (The artefact runs with P infinite [§5.7, p. 87].)
*What it does not say:* that the schedule is lawful, or that key destruction can be checked by anyone. The proof is "a verification rather than a discovery"; the substance is whether Semantics II is a defensible reading, argued in §4.2 and unconfirmed by any authority [§4.7, p. 62].

**Corollary 2.1** [§4.7, p. 61]. "The construction requires no coordination between the erasure process and the retention process, and no knowledge at the time a record is created of whether an erasure request will ever arrive."
**Corollary 2.2** [§4.7, p. 61]. F is arbitrary, so the result holds at once for 120, 72, 36 and 12 months, and any national floor. Backed by Appendix D (section 4).
**Corollary 2.3 (if auditing needs part of the payload)** [§4.7, p. 62]. Split the payload into a needed part p_n and the rest p_r. Feasibility survives, except where p_n is itself health data inside an SPE on the broad reading; then C1 and C3 collide over it, "by the argument of Proposition 3". Exits: relocation, dataset-granularity logging, the narrow reading, or anonymising p_n.

**Proposition 3 (anchoring)** [§4.6, p. 60].
*Exact:* "Let a record's floor of F months run from its creation month t(a), and let a ceiling of L months run from an event at month e(a) >= t(a). Under Semantics I, the floor and the ceiling are jointly satisfiable for a if and only if e(a) + L > t(a) + F." Case (i): same anchor, satisfiable for every record iff L > F, "decidable from the text alone". Case (ii): external anchor with L <= F, they fail for exactly the records with e(a) - t(a) <= F - L, "a set that the text does not reveal and each record's history determines."
*Plain meaning:* a ceiling collides with a floor only if it is no longer; an outside anchor hides the clash in each record's history.
*Record 100:* e = 10, L = 6: 10 + 6 = 16, not greater than 7 + 12 = 19, so it collides; e - t = 3 <= F - L = 6.
*What it does not say:* anything about frequency. Politiregisterloven § 17 (floor 12, ceiling 36, same anchor) gives no collision without a request, as case (i) predicts [§6.10, p. 100].

**Proposition 4 (location and right)** [§4.10, p. 72].
*Exact (core):* "This result depends on a legal premise stated here as an explicit assumption, not derived from the model: that a controller receiving a relocated record receives the erasure obligation of Article 17(1) GDPR with it." Under Semantics I, "relocating a record before the ceiling's deadline satisfies the ceiling and the floor together, while the floor and the right remain infeasible for every record satisfying the first disjunct of Proposition 1."
*Plain meaning:* exporting the logs dodges Article 68(12), not the right to erasure.
*What it does not say:* it is argued from a premise, not derived, and the artefact does not execute it. If the premise fails, relocation gets stronger; Propositions 1 to 3 are untouched [§4.10, p. 72].

---

## 8. The mechanism: Crypto-Erasure by Invalidation

The proof of Proposition 2 is the build sheet [§4.8, pp. 63-67; Figure 4.1, p. 64].

1. **Split the record** into accessor fields, subject fields (the patient link) and payload. For record 3 the payload is the demographic query that the IHE patient-discovery transaction (ITI-55) requires gateways to log; for record 100 it is the logged activity [§4.3, p. 52].
2. **Encrypt.** The payload is encrypted under its own per-record key, held under a key-encrypting key in a hardware security module or equivalent [§4.8, p. 63].
3. **Commit.** c(a) = Commit(payload, salt) with a per-record salt. Hiding (reveals nothing without the salt) and binding (no second payload opens it); an unsalted hash would let guesses be confirmed [§4.8, p. 65].
4. **Log.** Every access, invalidation and link removal goes into an append-only Merkle log with RFC 6962 hashing, the construction behind Certificate Transparency. Leaves hold the accessor fields, the payload commitment and a salted commitment to the subject fields; never the payload or the subject fields. So the log never needs rewriting [§4.8, p. 66].
5. **Trigger.** The invalidation month is the earliest of: erasure deadline, ceiling deadline, or a payload retention period P the controller sets [§4.8].
6. **Invalidate.** The key is destroyed, salt and ciphertext deleted. For patient-level SPE logs at the ceiling, the subject fields are removed. An invalidation entry records record ID, month, legal ground, authorising actor and a hash of the key's identifier. The key matters for backups that cannot be deleted at once [§4.8].
7. **Terminal transition.** After the floor ends, the identifying metadata is destroyed too, leaving a residue intended to be non-identifiable. Specified, not implemented [§4.8, p. 67; §6.1, p. 91].

Cross-border records keep the patient link through the floor: Article 9 EHDS lets patients see who accessed their data [§4.2, p. 50].

**What an auditor can check after invalidation:** the access happened and by whom; some payload was bound at write time and not substituted; it was invalidated, when, on what ground, by whom; and each entry is in the log as first written, by inclusion proof [§4.8; §5.7, p. 88].
**What an auditor cannot check:** the payload, and that the key is really gone. The invalidation entry is *attested, not proven* [§4.9, pp. 69-70; §6.3, p. 94]. Rewriting the whole log is caught only against a root published outside it: specified, not implemented [§4.9; §5.7, p. 88]. The residue is *pseudonymised, not anonymous* until the terminal transition [§4.9, p. 68]. "Verifiable" in the title "qualifies the invalidation record ... not the erasure itself, which no auditor can verify" [§1.4, p. 7].

---

## 9. The evidence

All figures come from one seeded run (seed 20260915) over 200 synthetic records: 100 cross-border (F = 120, primary) and 100 SPE access logs (F = 12, secondary, all treated as reached by the ceiling) [§5.2, p. 79; Table 5.2, p. 82]. Permit lengths are drawn uniformly from 1 to 12 months [Table 5.2, p. 82]. The counts are *synthetic, not frequency estimates*: "The rates in this chapter are functions of the generator parameters in Table 5.2 and are not estimates of real frequency" [§5.3, p. 83].

- **Semantics I:** 95 violations across 90 records (45%): 37 cross-border, 53 SPE. Five SPE records hit both C2 and C3, so 95 = 90 + 5 (41 C2 only, 44 C3 only, 5 both) [§5.3, Table 5.3, p. 83].
- **Boundary reproduced:** 38 cross-border records got a request; 37 fell inside the window and all 37 violate; the one outside does not [§5.3, p. 83].
- **No request needed:** 39 of the 78 SPE records with no erasure request still collide (Corollary 1.2, broad reading). Half, because permits run 1 to 12 months; over a five-year permit about one log in ten would fall in the window [§5.4, pp. 84-85].
- **Semantics II:** 138 invalidations (52 on Article 17(1), 86 on Article 68(12); four same-month cases recorded under Article 17(1)); 0 violations across 200 [§5.7, Table 5.6, pp. 87-88].
- **At delta = 3:** 89 records, 94 violations, 39, 138, 0 [§5.6, Table 5.5, p. 87].
- **Log integrity:** 200 of 200 verify. Altering record 100's actor, its invalidation ground, or record 3's patient link each makes V^II fail; restoring makes it hold [§5.7, p. 88].

**Three cross-checks** [§5.5, pp. 85-86; §5.8, p. 89]:
1. *Exhaustive search:* all 2^14 = 16,384 alpha assignments per case over 14 months, four cases. Three conflict cases have no solution; the control case does [Table 5.4, p. 86]. A sanity check, not independent evidence.
2. *Z3 bounded SMT check:* nine checks of Propositions 1 to 3 within bounds; no counterexample, and deliberately broken variants are caught [§5.5, p. 86].
3. *Synthea payloads:* Synthea-generated FHIR R4 resources replace the payloads; all 200 commitments change and no figure does, because no constraint reads content [Table 5.7, p. 90].

**What this proves:** the code implements the model; not independent evidence, not performance, not deployment. Semantics II's zero holds by construction; the falsifiable part is the inclusion-proof check. Key destruction is simulated in program memory; the optional AES-256-GCM module shows 138 records refuse to decrypt and 62 still read, and none of the 62 surviving keys opens record 3 [§5.8, p. 89; §6.3, p. 94].

**One honesty point.** The reported run derives salts from record IDs so it reproduces exactly; in that run the commitments are therefore not hiding. `--random-salts` draws real random salts [§5.2, p. 80].

---

## 10. Norway: where it lands

- **Primary use.** Helsedirektoratet and Norsk Helsenett run the NCPeH, in live pilot at two emergency clinics, no relevant patient yet [§1.1, p. 1; §2.2, p. 16]. The mechanism attaches at the sixth OpenNCP step, where the audit record is written [§4.11, p. 73].
- **Secondary use.** Helsedataservice is the presumptive Health Data Access Body (eleven central registries). The mechanism sits at the SPE access-logging boundary, because Norwegian SPEs are fragmented well beyond the three NORTRE nodes, and takes permit expiry from the access body [§4.11, p. 73].
- **National criteria.** The SPUHiN criteria require identifiable access logs for at least one year and an information-security management system; none says how logs reconcile with deletion. The mechanism adds no requirement of a new kind [§4.11, p. 73; Table 4.1, p. 74].
- **Timing.** Implementing acts due 26 March 2027 (Article 73(5)); Articles 68 and 73 apply from 26 March 2029. The collision is not yet operative, which is why designing it now matters [§6.8, p. 98].

---

## 11. Limitations, owned

- **No authority behind Semantics II.** If a supervisory authority reads "identifiable logs" as requiring readable content, Proposition 2 stays true *in the model* and becomes inert in practice [§6.2, p. 92]. Datatilsynet enquiry sent 23 September 2026, unanswered at submission [§7.4, p. 106].
- **Broad reading of Article 68(12)** is contestable; Corollary 1.2 and one branch of Corollary 2.3 depend on it, nothing else [§4.6, p. 59; §6.2, p. 92].
- **Four subsidiary premises** without authority, including Proposition 4's premise and whether auditing after the ceiling needs the patient link [§3.7, p. 45].
- **Not implemented:** terminal transition, per-leaf nonce, proactive invalidation, published roots with consistency proofs, accumulator [§6.1, p. 91].
- **Informal proofs**, one seed, every request treated as valid, payload as one unit; data *synthetic, not frequency estimates*, US-based Synthea output [§3.7, pp. 44-45; §6.7, p. 97].
- **Six-year pilot floor** is a controller decision (Appendix D); no national legal basis identified [§4.2, p. 51].
- **Rival 4** (delete and log the deletion) is close to equivalent for cross-border records [§4.10, p. 71].
- **Evaluation** is analytical; the expert panel is designed, not run [§6.6, pp. 96-97; Appendix C, p. 160].

---

## 12. Slide by slide: what each slide teaches

Talk: slides 1 to 16, fifteen minutes. One live stop, slide 13. Slide 17 breaks into questions; 18 to 31 are backup.

### Slide 1. Cover
**Teaches:** one audit record must be kept and deleted at once, and the answer is in the subtitle: delete the payload, keep the accountability, log the deletion.
**Say:** "My thesis is about one audit record that the law asks us to keep and to delete at the same time." Name the app and the Zenodo DOI once; do not open them.
**Page:** Abstract, p. i. **App:** https://trfhimolde.streamlit.app/?p=start

### Slide 2. Promise
**Teaches:** the three outcomes for the listener and the one sentence heard three times: "the impossibility follows from an assumption about one word, not from the obligations."
**Say:** Five steps, problem to forward. "Every number I show can be rerun, with the same seed." No background assumed.
**Page:** Abstract, p. i; §7.6, p. 108. **App:** https://trfhimolde.streamlit.app/?p=start

### Slide 3. Record
**Teaches:** the subject is the audit line written by the Norwegian NCPeH, not the health record.
**Say:** Patient from Molde, clinician in Helsinki (actor HP-003), request through NCP Finland, Norway answers and logs. Gold fields are accountability (who, when, on what basis); rose fields (subject link, payload) are what an erasure request reaches. "This is record 3; you will see it live."
**Month on screen:** month 11, creation; the floor starts running.
**Page:** §1.1, p. 1; §2.2, p. 15; Figure 1.1, p. 5. **App:** https://trfhimolde.streamlit.app/?p=witness&r=3&m=11

### Slide 4. Strip
**Teaches:** put the rules on the clock and the collision is a stretch of months, 116 to 131.
**Say:** Amber row: floor to month 131 (11 + 120). Violet row: request in month 115, one month to act, payload gone from 116. Red stretch: readable and gone, both required. Honest note: under the pilot's six years the floor ends at month 83, before the request, so record 3 would not collide; what matters is whether a deadline falls inside the window (Corollary 1.1).
**Page:** §4.4, p. 54; §5.3, p. 83; Corollary 1.1, p. 57. **App:** https://trfhimolde.streamlit.app/?p=witness&r=3&m=116

### Slide 5. Research
**Teaches:** a research log can collide with no erasure request at all, because two articles of one regulation run on different clocks.
**Explain:**
1. A researcher, R-008, works inside a Secure Processing Environment under data permit DP-015, and every access is logged.
2. The log entry is made in month 7, and the one-year floor keeps it verifiable until month 19.
3. The permit expires in month 10, so the ceiling wants the health data gone from month 16.
4. Months 16 to 19 carry two opposite demands, and nobody asked for anything.
5. This holds on the broad reading, where a patient-level log entry counts as health data in the environment; who decides that is slide 14.
**Regulation:** Article 73(1)(e) EHDS, "logs of access shall be kept for at least one year" [p. 2]: binds months 7 to 19. Article 68(12) EHDS, "shall be deleted within six months of the expiry of the data permit" [p. 2]: bites from month 16.
**Carries:** Corollary 1.2. Plain: C1 and C3 clash with no request. Exact: if t_pi(a) + 6 <= t(a) + 12, C1 and C3 are contradictory at t_pi + 6, "provided C3 reaches the record" [§4.6, p. 57].
**Months on screen:** 7 query; 10 permit ends; 16 ceiling bites (10 + 6); 19 floor ends (7 + 12). 16 <= 19, so collision at 16.
**App:** Witness a record, preset "Research log, no erasure request (Corollary 1.2), record 100", month 16. https://trfhimolde.streamlit.app/?p=witness&r=100&m=16
**Thesis:** §4.6, p. 57; §5.4, p. 84; Figure 5.2, p. 85; §1.2, p. 3; §6.8, p. 98.
**Objection:** "Do research logs really count as data within the environment?" Answer: contestable; the narrow reading confines Article 68(12) to the permit dataset. Only Corollary 1.2 and one branch of Corollary 2.3 depend on it. Backup slide 21.

### Slide 6. Fixes
**Teaches:** each obvious fix meets one rule by breaking another, and the way out is the necessity boundary of Article 17(3)(b).
**Explain:**
1. Delete the record and the audit chain goes; keep it whole and the right is not met.
2. Pseudonymise it, and it is reversible, so still personal data under GDPR Recital 26.
3. Move the log elsewhere, and you meet the ceiling but not the right, if the receiving controller inherits Article 17: that is Proposition 4, a legal premise.
4. The law exempts retention only as far as necessary, and accountability needs who, when and on what basis, not the payload.
**Regulation:** Article 17(3)(b) GDPR exempts erasure "to the extent that processing is necessary for compliance with a legal obligation" [§1.2, p. 3; §4.2, p. 49]; Article 5(1)(c) minimisation; Recital 26 [p. 3]. No single month: these are the escape routes tested against record 3 at month 116.
**Carries:** Proposition 4 (relocation). Plain: export dodges the ceiling, not the right. Exact: see section 7 [§4.10, p. 72].
**App:** none needed; for the append-only wall, How it is built. https://trfhimolde.streamlit.app/?p=built
**Thesis:** §1.2, p. 3; §2.3, p. 17; §2.4, p. 21; §4.2, p. 49; §4.10, pp. 70-72.
**Objection:** "Why not a blockchain?" Answer: every append-only log meets the erasure wall (Finck; review of 114 papers, p. 24); the Merkle log gives tamper evidence and keeps erasable content off it. Backup slide 18. "Just export the logs." Backup slide 30.

### Slide 7. Model
**Teaches:** the whole model is one binary variable, alpha, and three constraints, two of which are written on a different symbol from the third.
**Explain:**
1. For each record a and month t, alpha says whether the payload can be read: 1 or 0.
2. C1, the floor, keeps the record verifiable through its window: six years in the pilot, 12 months for research logs.
3. C2, erasure, forces alpha to zero from the request month plus delta, one month.
4. C3, the ceiling, forces alpha to zero six months after permit expiry, only for research logs it reaches.
5. C1 speaks about V; C2 and C3 about alpha; how V and alpha relate decides everything, and the law does not say.
**Regulation:** Article 12(3) GDPR, one month, extendable by two: gives delta = 1 (or 3) [§4.4, p. 54]. Floor values 72 / 120 / 36 / 12 [§4.3, p. 53].
**Carries:** no proposition; this is the formal object they are about.
**App:** Start here. https://trfhimolde.streamlit.app/?p=start
**Thesis:** §4.3, pp. 51-53; §4.4, p. 54.
**Objection:** "One binary variable is too crude; real systems redact fields." Answer: conceded as a limitation (eighth abstraction); minimality is deliberate, and Corollary 2.3 extends to a split payload [§4.3, p. 53; §3.7, p. 44; p. 62]. Backup slide 24.

### Slide 8. Word
**Teaches:** "verifiable" is undefined, and there are two candidate readings.
**Explain:**
1. The floor says verifiable and never defines it, so I treat two readings as candidates.
2. Reading I: verifiable means readable, V = alpha. No statute says so, but the 2017 OpenNCP reference source stores every audit message whole and readable.
3. Reading II: verifiable means accountable: who acted and when intact, a binding commitment to the payload, and every loss of readability logged as an invalidation entry.
4. Under Reading I an erased payload is a broken record; under Reading II it is the record of a lawful erasure.
**Regulation:** the floors in Article 73(1)(e) and the national cross-border floor, which use "verifiable" or "identifiable" without definition [§4.5, p. 55].
**Carries:** the definitions of Semantics I and II [§4.5, pp. 55-56].
**App:** Start here. https://trfhimolde.streamlit.app/?p=start
**Thesis:** §4.5, pp. 55-56; §4.2, p. 49.
**Objection:** "Semantics II is your own definition." Answer: yes; it is argued from Article 17(3)(b) necessity and Article 5(1)(c), labelled a reading, and put to Datatilsynet. Backup slide 22.

### Slide 9. Result
**Teaches:** the core result: read as readable, any deadline inside the window is a contradiction; read as accountable, none is.
**Explain:**
1. Record 3 again. Under Reading I the third row turns crimson in month 116: the erasure deadline arrives while the floor runs to 131.
2. One binary variable cannot be one and zero in the same month; that is Proposition 1, elementary, but it means no lawful schedule exists for any record with a deadline inside its window.
3. Under Reading II the payload row ends at 116, the record row stays teal to 131, and the line under the axis is the invalidation entry: ground GDPR Article 17(1), authorised by the DPO.
4. Proposition 2: in the model, every record, request pattern and floor has a solution, and the proof is the build sheet.
**Regulation:** Article 17(1) with Article 12(3): bites month 116 (115 + 1). The floor runs to month 131.
**Carries:** Proposition 1 (plain: a deadline inside the window means no schedule) and Proposition 2 (plain: under Reading II every record has one); exact statements in section 7 [pp. 57, 60]. Witness t^I = min(t_r + delta, t_pi + 6, t + P).
**Months on screen:** 116 = 115 + 1 <= 131 = 11 + 120, so Proposition 1 applies; t^I = min(116, infinity, infinity) = 116.
**App:** The four propositions. https://trfhimolde.streamlit.app/?p=propositions
**Thesis:** §4.6, p. 57; §4.7, pp. 60-61; §5.3, p. 83; §5.7, p. 87.
**Objection:** "This is trivial." Answer: the thesis says so; the proof is "a verification rather than a discovery" [p. 62]. The contribution is the parameter, not the arithmetic. Backup slide 24. "What about Propositions 3 and 4?" Backup slide 30.

### Slide 10. Mechanism
**Teaches:** the payload goes, the accountability stays, the deletion is logged, and the log never holds what erasure reaches.
**Explain:**
1. The audit writer splits the record into accessor fields, subject fields and payload.
2. The payload is encrypted under its own key, held in key custody, and a salted commitment binds it without revealing it.
3. Accessor fields and commitments go into a Merkle log, the construction behind Certificate Transparency.
4. An erasure request, a permit ending or a controller-set period, whichever comes first, fixes the invalidation month; the key is destroyed, ciphertext and salt deleted, and an invalidation entry appended.
**Regulation:** Article 17(1) GDPR and Article 68(12) EHDS are the two triggers; NIST SP 800-88 Rev. 2 recognises cryptographic erase [p. 23]. Bites at t^I: month 116 for record 3, month 16 for record 100.
**Carries:** Proposition 2's construction, steps 1 to 4 of the proof [§4.7, p. 60]; Corollary 2.1, no coordination needed [p. 61].
**App:** How it is built. https://trfhimolde.streamlit.app/?p=built
**Thesis:** §4.8, pp. 63-67; Figure 4.1, p. 64; §4.9, p. 68.
**Objection:** "The operator controls the log." Answer: an altered entry is caught; a wholesale rewrite needs published roots and consistency proofs, specified, not implemented. Backup slide 29. "Is the commitment even hiding?" In the reported run salts derive from record IDs for reproducibility, so not hiding there; `--random-salts` fixes it [p. 80].

### Slide 11. Audit
**Teaches:** what an auditor can check after invalidation (four things) and what stays on trust (one).
**Explain:**
1. The dark panel is the run's printout for record 100 after invalidation: actor and permit intact, link removed, key gone, entry at month 16 on Article 68(12).
2. The first three checks hold as written: the access and actor, a payload bound at write time, and the grounded invalidation.
3. The fourth needs care: inclusion proofs against the root catch an altered entry; a rewritten log needs roots published outside it, specified, not built.
4. The fifth cannot be checked at all: that the key is gone. Attested, not proven.
**Regulation:** Article 68(12) EHDS, bites month 16 for record 100; Article 73(1)(e) floor still runs to month 19, now met by the accountable record.
**Carries:** Semantics II conditions (i) to (iii) [§4.5, p. 56]; "Verifiable" qualifies the invalidation record [§1.4, p. 7].
**Months on screen:** 16 invalidation and link removal; at 19 the payload is still unreadable and the record still verifies.
**App:** Witness a record, record 100, expander "What the auditor holds for this record now". https://trfhimolde.streamlit.app/?p=witness&r=100&m=16
**Thesis:** §1.4, p. 7; §4.8; §4.9, pp. 68-70; §5.7, p. 88; Table 4.1, p. 74.
**Objection:** "You cannot prove the key was destroyed." Answer: correct; simulated in program memory, the entry is an attestation; proof would need certified deletion, open research. Backup slide 25. "Is what remains anonymous?" No: pseudonymised, not anonymous. Backup slide 27.

### Slide 12. Evidence
**Teaches:** 200 records: 90 fail read as readable, none read as accountable, and the code is checked three ways.
**Explain:**
1. Records 3 and 100 are two dots among 200 (100 cross-border at F = 120, 100 research logs at F = 12). Read as readable: 90 records violate, 95 violations in all, because five research logs hit both deadlines.
2. 39 research logs with no request still collide, on the broad reading.
3. Read as accountable: 138 invalidations, zero violations.
4. These counts follow the generator; they are synthetic, not frequency estimates. The checks show the code implements the model, not independent evidence for the propositions.
**Regulation:** all three, across the population; no single month.
**Carries:** Proposition 1's conditional boundary (37 of 38 requests inside, all 37 violate) [p. 83]; Corollary 1.2 (39 of 78) [p. 84]; Proposition 2 (0 of 200) [p. 87].
**App:** Claim ledger. https://trfhimolde.streamlit.app/?p=ledger
**Thesis:** §5.3, Table 5.3, p. 83; §5.4, p. 84; §5.5, pp. 85-86; §5.7, p. 87; §5.8, p. 89.
**Objection:** "45 per cent is an artefact of your generator." Answer: yes, by design; the rate follows Table 5.2; the boundary and the zero are the findings. Backup slide 23 (permits), 26 (Synthea).

### Slide 13. Demo
**Teaches:** every figure is recomputed live; the audience can check rather than trust.
**Explain:**
1. Stop one, Witness a record, preset "Cross-border record with an erasure request, record 3", month 116: "Under the first reading, the collision; under the second, the invalidation."
2. Stop two, Claim ledger: point at 90, 95, 39, 138 and 0. If the Synthea row says bundles not deployed, say so and move on.
3. Network failure: ledger screenshot, then Figure 5.2. Seventy-five seconds in all.
**Regulation:** Article 17(1) and 12(3) at month 116 for record 3.
**Carries:** Propositions 1 and 2 on one record.
**Months on screen:** 116.
**App:** https://trfhimolde.streamlit.app/?p=witness&r=3&m=116 then https://trfhimolde.streamlit.app/?p=ledger . Wake the app ten minutes ahead; deep links are read once per session, so use fresh tabs.
**Thesis:** §5.2, p. 79; §5.4, Figure 5.2, p. 85; Table 5.7, p. 90; Appendix A.1, p. 116.
**Objection:** "Which version is the thesis?" Answer: 1.3.0 is cited (Appendix A); the live app runs 1.3.2, viewer wording and metadata only, result modules unchanged (Demo_Walkthrough). Not in the thesis itself.

### Slide 14. Limits
**Teaches:** what is not claimed, and the two questions only an authority can answer.
**Explain:**
1. Not claimed: destruction is attested, not proven; the residue is pseudonymised, not anonymous; informal proofs; synthetic data; no new cryptography; no deployment.
2. Question one: does an invalidated record still satisfy a retention obligation? That decides whether Reading II holds in law.
3. Question two: does Article 68(12) reach patient-level access logs? Corollary 1.2 and one branch of Corollary 2.3 stand or fall with it; nothing else does.
4. Datatilsynet has had the GDPR side since 23 September 2026; the EHDS side, Helsedirektoratet and the Ministry, is not yet asked. Helsedirektoratet has answered one factual question, the floor (Appendix D).
**Regulation:** Article 17(3)(b) GDPR (question one); Article 68(12) EHDS (question two).
**Carries:** the conditions under which Proposition 2 is inert in practice and Corollary 1.2 lapses.
**App:** Start here, expander "What the thesis does not claim". https://trfhimolde.streamlit.app/?p=start
**Thesis:** §3.7, p. 44; §6.2, p. 92; §6.3, p. 94; §7.3, p. 106; §7.4, p. 106; Appendix D, pp. 168-169.
**Objection:** "If the authority says no, what is left?" Answer: the model, Propositions 1, 3 and 4, and a precise question for the authority; Proposition 2 stays true in the model. Backup slide 22.

### Slide 15. Forward
**Teaches:** three bodies can make this the default before the rules apply in 2029, and the first step is a letter.
**Explain:**
1. Picture the rules in force: a patient asks for erasure, within a month her payload is gone, and she can still learn who looked, and an auditor can still check who deleted what, when and on what ground.
2. The Commission can write the reconciliation of Articles 73(1)(e) and 68(12) into the Article 73(5) implementing acts, due 26 March 2027.
3. Health Data Access Bodies, Helsedataservice among them, can log every invalidation as a first-class event; that alone costs little.
4. TEHDAS2 can read Table 4.1, written in its own requirement identifiers, as a proposal against the SPE specification.
**Regulation:** Article 73(5) EHDS, implementing acts by 26 March 2027; Chapter IV applies 26 March 2029 [§6.8, p. 98].
**Carries:** Corollary 2.1 (no coordination; the entry can be adopted alone).
**App:** Norwegian context (illustrative). https://trfhimolde.streamlit.app/?p=norway
**Thesis:** §6.8, p. 98; §4.8; §7.4, p. 106; Table 4.1, p. 74; Appendix D, p. 168.
**Objection:** "Who would pay for per-record keys?" Answer: a real burden, not measured; it falls on audit records, live keys shrink as invalidations accumulate, and the cheapest step is the entry alone. Backup slide 31.

### Slide 16. Close
**Teaches:** four contributions, each bounded and checkable.
**Explain:**
1. A formal model in which verifiability decides feasibility; feasibility results, Propositions 1 to 3 proved informally and checked in code, Proposition 4 argued from a stated premise.
2. A mechanism specification with its residue analysed, and an integration analysis against Norwegian infrastructure.
3. "The impossibility follows from an assumption about one word, not from the obligations. Delete the payload. Keep the accountability. Log the deletion."
**Regulation:** all three, resolved.
**Carries:** the full set.
**App:** point, do not click. https://trfhimolde.streamlit.app/?p=start
**Thesis:** §7.2, p. 104; §7.6, p. 108; Appendix A.1, p. 116.
**Objection:** "Where is the SNARK?" Backup slide 19. "Where is the logistics?" Backup slide 20.

### Slide 17. Backup index
**Teaches:** every answer leads with the limit, then what survives, then the section.
**Use:** jump by slide number in present mode. Map: 18 blockchain, 19 SNARK, 20 logistics, 21 Article 68(12) reach, 22 authority, 23 permits, 24 proofs, 25 keys, 26 Synthea, 27 residue, 28 Rival 4, 29 log rewrite, 30 export and Props 3 and 4, 31 adoption and cost.

### Backup slides 18 to 31

| # | Question | One-line answer (limit first) | Thesis | App |
|---|---|---|---|---|
| 18 | Why not a blockchain? | A ledger never forgets, so it meets the erasure right head on; the Merkle log gives tamper evidence without holding payload or subject fields. | §2.4, p. 24; §4.8, p. 66 | ?p=built |
| 19 | Where is the SNARK? | None; the name is from the NORS 2025 iteration. Zero knowledge is needed only to prove all of a patient's records were invalidated without revealing which. | p. ix; §1.6, p. 9; §7.5, p. 107 | none |
| 20 | Where is the logistics? | No optimisation and no energy claim. The record is a consignment under custody rules; Proposition 3 is a two-clock perishability result. | §1.4, p. 7; §2.7, p. 30 | ?p=anchor |
| 21 | Does Art 68(12) reach the logs? | Contestable. Only Corollary 1.2 and one branch of Corollary 2.3 depend on it. | §4.6, pp. 58-59; §7.4, p. 106 | ?p=witness&r=100&m=16 |
| 22 | Who endorses Semantics II? | No regulator or court. Argued from Art 17(3)(b) necessity and Art 5(1)(c); EDPB 02/2025 para 51: unintelligible, still personal data. | §4.2, p. 49; §2.3, p. 20; §6.2, p. 92 | none |
| 23 | Are 1 to 12 month permits realistic? | A stated assumption. Longer permits change how many, not whether: five-year permits give about one in ten. | §3.7, p. 44; §5.4, p. 85; §5.6, p. 87 | ?p=robust |
| 24 | Why believe informal proofs? | No proof assistant. Prop 1 is a pigeonhole; 2^14 search agrees; Z3 9 of 9, broken variants refuted. | §4.6, p. 57; §5.5, pp. 85-86; A.24, p. 153 | ?p=propositions |
| 25 | Can you prove key destruction? | No: simulated, attested, not proven. Ciphertext is deleted; AES-GCM module: 138 refuse, 62 read. | §4.9, p. 69; §6.3, p. 94; A.22, p. 149 | ?p=robust |
| 26 | Are the synthetic patients American? | Yes, US-based Synthea. Its FHIR payloads change all 200 commitments and no figure. | §3.5, pp. 41-42; Table 5.7, p. 90 | ?p=synthea |
| 27 | Is what remains anonymous? | No: pseudonymised, not anonymous, until the terminal transition (specified, not implemented). | §4.8, p. 67; §4.9, p. 68 | ?p=witness&r=100&m=19 |
| 28 | Why not delete and log it (Rival 4)? | Conceded: near equivalent for cross-border records. The commitment and grounded entry add tamper evidence; in SPE logs they do work deletion cannot. | §4.10, p. 71 | ?p=witness&r=3&m=116 |
| 29 | Can the operator rewrite the log? | Not stopped by the artefact: it catches an altered entry, not a rewrite. Published roots with consistency proofs: specified, not implemented. | §4.9, p. 69; §5.7, p. 88; §6.1, p. 91 | ?p=run |
| 30 | Why not export the logs (Props 3, 4)? | Conceded for the ceiling. Prop 4, on its premise: the right follows the holder. Prop 3: an outside anchor hides the clash. | §4.10, p. 72; §4.6, p. 60; §6.10, p. 100 | ?p=anchor |
| 31 | Is it real, and what does it cost? | Not yet operative (2029) and not measured. Acts due 26 March 2027; the cheapest step is the entry alone. | §6.4, p. 95; §6.5, p. 96; §6.8, p. 98 | ?p=norway |

All app cells are relative to `https://trfhimolde.streamlit.app/`; full links are in `slide_links.json`.

---

## 13. Glossary

- **Audit record:** the log line saying who accessed what, when, why, with what outcome.
- **Payload:** content in the record about *what* was accessed, such as the demographic query.
- **Subject fields / patient link:** the fields tying the event to a patient.
- **alpha(a,t):** 1 if the payload is readable in month t, else 0.
- **V(a,t):** whether the record counts as verifiable.
- **delta:** erasure response period, 1 month (3 if extended).
- **rho(a):** 1 if the ceiling reaches the record.
- **P:** a payload retention period the controller may set; infinite in the artefact.
- **t^I:** invalidation month, min(t_r + delta, t_pi + 6, t + P).
- **Semantics I / II:** verifiable means readable / accountable.
- **Invalidation entry (iota):** logged record of a payload's removal: month, ground, actor.
- **Commitment:** a value that binds the payload without revealing it.
- **Merkle log:** append-only log where any entry can be checked against one root hash.
- **Inclusion proof:** short proof that an entry is in the log under a given root.
- **Published root:** root held outside the log so rewrites can be caught.
- **Terminal transition:** destruction of identifying metadata after the floor ends.
- **Pseudonymised:** still personal data for whoever can re-link it.
- **SPE:** Secure Processing Environment, where researchers work on permitted data.
- **HDAB:** Health Data Access Body; in Norway, presumptively Helsedataservice.
- **Broad / narrow reading:** Article 68(12) reaches patient-level logs / only the permit dataset.
- **Hdir:** Helsedirektoratet, data controller for the Norwegian NCPeH pilot.

---

## 14. Five sentences to remember

1. The impossibility follows from an assumption about one word, verifiable, not from the obligations.
2. If verifiable means readable, any record with a deadline inside its window has no lawful schedule (Proposition 1, p. 57).
3. If verifiable means accountable, every record has one, and the proof is the mechanism (Proposition 2, p. 60).
4. A ceiling collides with a floor only if it is no longer, and an outside anchor hides the clash in each record's history (Proposition 3, p. 60).
5. Destruction is attested, not proven; the residue is pseudonymised, not anonymous; the counts are synthetic, not frequency estimates; all of it holds in the model.

---

## Not verified

- The Molde and Helsinki framing of record 3 is the deck's; the thesis does not name the cities. Record 3's and record 100's timings and actors were checked against the generator in `demo_app/trf_checker.py` (seed 20260915), not only the thesis.
- Deep links were checked against the slug table in `demo_app/app.py`, not opened live. The app's on-screen colours and expander names come from the deck and the source, not a live view.
- Release 1.3.2 on the live app comes from Demo_Walkthrough, not from the thesis.
- Section-level pages without a printed page (for example §4.8 steps 5 and 6) cite the section start range only.
