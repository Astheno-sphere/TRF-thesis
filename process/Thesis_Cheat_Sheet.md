# Thesis Cheat Sheet

*Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the European Health Data Space.* Plain-language companion to the viva notes. Section numbers in brackets refer to `VERA-SNARK_Thesis_SUBMISSION.md` as of 19 November 2026.

---

## 1. The thesis in one paragraph

A cross-border health data access leaves an audit record of who looked. Three rules bind it: keep it for years; erase personal data when the patient asks; delete health data from a research environment six months after the permit ends. The thesis turns the three rules into a small mathematical model and shows that whether they can all be obeyed depends on one undefined word: *verifiable*. If verifiable means "the content is still readable", the rules contradict each other for any record whose deadline falls inside its retention window. If verifiable means "who acted, when and why is intact, the content is bound by a commitment, and its removal is logged", every record can obey all three. The proof of that second result is also the design, Crypto-Erasure by Invalidation. All of this holds *in the model*; whether it holds in law is still an open question [§4.1, §7.1].

---

## 2. The story of one audit record

**Record 3.** A patient from Molde falls ill while working in Helsinki. A clinician there asks for the patient summary. The request passes through the Finnish contact point; the Norwegian National Contact Point answers it and writes one line in its audit log. That line is not the health record. It is the record of who looked, when and why. In the run it is created in month 11 under the illustrative ten-year floor, so it must stay verifiable until month 131. In month 115 the patient asks for erasure; with one month to respond, the payload must be gone from month 116. If verifiable means readable, months 116 to 131 demand the payload be readable and gone at once [§5.3; story framing from the deck].

**Record 100.** A researcher works under a data permit inside a Secure Processing Environment (SPE). The SPE logs the access in month 7; the one-year floor keeps the log to month 19. The permit expires in month 10, so the six-month ceiling wants health data gone from month 16. Nobody asked for anything, yet months 16 to 19 carry two opposite demands [§5.4, Figure 5.2].

---

## 3. The three rules, and what each actually says

**The floor (keep).** For SPE access logs, Article 73(1)(e) EHDS requires "identifiable logs of access to and activities in the secure processing environment" and says "logs of access shall be kept for at least one year" [§1.1]. For the cross-border audit repository, no eHDSI specification fixes a period; it is left to national law. The Norwegian pilot uses six years (72 months), decided by Helsedirektoratet as controller; the literature reports ten (120 months), used illustratively in the run. From 2029, Article 9(2) EHDS gives a binding three years (36 months) wherever the audit record feeds the patient's right to see who accessed their data [§4.3].

**The right (erase).** Article 17(1) GDPR gives the data subject a right to erasure "without undue delay". Article 12(3) sets one month, extendable by two [§4.4]. Article 17(3)(b) exempts processing necessary for a legal obligation, but only as far as it is *necessary*, and Article 5(1)(c) requires minimisation. Accountability, the thesis argues, needs who, when, on what basis and with what outcome, not readable content [§4.2].

**The ceiling (delete).** Article 68(12) EHDS: "the electronic health data within the secure processing environment shall be deleted within six months of the expiry of the data permit" [§1.1]. It has no exemption like 17(3)(b). On the broad reading it reaches SPE log entries kept at patient-record granularity, since such an entry reveals cohort membership, which is health data. That reading is contestable [§4.6].

---

## 4. The one word: verifiable

The floor says the record must stay *verifiable*. Nobody defines the word [§4.5].

**Semantics I, plaintext verifiability.** A record is verifiable exactly when its payload can be read. The 2017 OpenNCP reference source behaves this way. No instrument states it; it is a de facto habit [§4.5].

**Semantics II, accountability-preserving verifiability.** A record is verifiable when (i) the accessor fields are intact, and so are the subject fields unless their removal is logged; (ii) a binding commitment to the payload survives; and (iii) any loss of readability is recorded in an invalidation entry giving month, legal ground and authorising actor. A record with no readable payload is then not broken: it records an access and its lawful erasure [§4.5].

---

## 5. The model in plain words

One record, one clock in months, one question each month: can the payload still be read? [§4.3]

- **a** is an audit record, created in month **t(a)**, with floor **F(a)** months. It holds metadata **m(a)** split into accessor fields (who, when, permit, outcome) and subject fields (the patient link), a payload **p(a)**, a commitment **c(a)**, and a key **k(a)**.
- **alpha(a,t)** is the whole state space: 1 if the controller can read the payload in month t, 0 if not. A second variable, **beta(a,t)**, tracks whether the patient link is readable; it matters only for SPE logs on the broad reading.
- **V(a,t)** says whether the record counts as verifiable.
- **t_r(a)** is the month an erasure request arrives; **delta** is the response period; **t_pi(a)** is permit expiry. Either is infinite if it never happens.

The three constraints [§4.4]:

- **C1, floor:** V(a,t) = 1 for every month from t(a) to t(a) + F(a).
- **C2, erasure:** alpha(a,t) = 0 for every month from t_r(a) + delta onward.
- **C3, ceiling:** for secondary records the ceiling reaches, alpha(a,t) = 0 (and beta = 0 where the subject fields are health data) from t_pi(a) + 6 onward.

C1 is written on V; C2 and C3 on alpha. Whether they clash depends on whether V is defined in terms of alpha [§4.4].

---

## 6. The propositions and corollaries

The thesis is candid that these are elementary once the semantics are fixed. Propositions 1 to 3 are proved informally and checked in code; Proposition 4 is a legal argument given the form of a proposition [§4.7 note, §1.5].

**Proposition 1 (infeasibility).** Under Semantics I, C1 to C3 are infeasible for any record where t_r + delta is at most t + F, or, for records the ceiling reaches, where t_pi + 6 is at most t + F [§4.6].
*Plain meaning:* if an erasure deadline, or a deletion deadline for a record the ceiling reaches, falls inside the retention window, no schedule works.
*Why true:* at the deadline month, C1 needs alpha = 1 and C2 or C3 needs alpha = 0. One binary variable cannot be both. Record 3 fails at month 116.
*What it does not say:* how often. Conversely, with no deadline inside the window the record is feasible even under Semantics I. The request-driven case presupposes the payload is not necessary for the floor [§4.6, §3.7].

**Corollary 1.1 (cross-border).** A request in any month except the last delta months of the window collides; under the pilot's six-year floor, any request in months t(a) to t(a) + 71 [§4.6].

**Corollary 1.2 (SPE, no request).** For an SPE log with a one-year floor, if the permit expires by the sixth month of the window, C1 and C3 collide with no erasure request at all, provided the ceiling reaches the record [§4.6].
*Plain meaning:* two articles of one regulation contradict each other in one environment. Record 100 is the example.
*What it does not say:* it holds only on the broad reading, for patient-record granularity logs. On the narrow reading it lapses; nothing else in the thesis does [§4.6, §6.2].

**Proposition 2 (feasibility).** Under Semantics II, C1 to C3 are jointly satisfiable for every record, every arrival pattern of requests and permit expiries, and every floor [§4.7].
*Why true:* the proof builds the schedule. Set the invalidation month t^I = min(t_r + delta, t_pi + 6, t + P). Before it, the payload is readable. At it, destroy the key, remove the patient link if the ceiling reaches it, and log an invalidation entry. After it, keep accessor fields, commitment and entry. C2 and C3 hold because readability ends at or before each deadline. C1 holds because Semantics II never reads alpha.
*What it does not say:* that the schedule is lawful, or that key destruction can be checked by anyone. The thesis concedes the proof is "a verification rather than a discovery"; the substance is whether Semantics II is a defensible reading, argued in §4.2 and unconfirmed by any authority [§4.7].

**Corollary 2.1.** No coordination is needed, and nobody must know at creation whether a request will come [§4.7].
**Corollary 2.2.** Because F is arbitrary, the result holds at once for 120, 72, 36 and 12 months, and for any national floor. [§4.7].
**Corollary 2.3 (if auditing needs part of the payload).** Split the payload into a needed part and the rest. Feasibility survives, except where the needed part is itself health data inside an SPE on the broad reading; then C1 and C3 collide over it, with the same exits [§4.7].

**Proposition 3 (anchoring).** With a floor of F months from creation and a ceiling of L months from an event at month e, the two are jointly satisfiable under Semantics I if and only if e + L is greater than t + F [§4.6].
*Plain meaning:* a ceiling can collide with a floor only if it is no longer than the floor. If both run from the same event, you can see the clash in the text. If the ceiling runs from an outside event, the clash depends on each record's history and is invisible in the text.
*Why true:* the window demands readability up to t + F; the ceiling forbids it from e + L. They overlap exactly when e + L is at most t + F. For record 100: 10 + 6 = 16, which is not greater than 7 + 12 = 19, so it collides.
*What it does not say:* anything about frequency. Politiregisterloven § 17 (floor 12, ceiling 36, same anchor) produced no collision without a request, as predicted [§6.10].

**Proposition 4 (location and right).** On the premise that a controller receiving a relocated record receives the Article 17 obligation with it: under Semantics I, moving a record out before the ceiling satisfies ceiling and floor, but floor and right remain infeasible for every record meeting Proposition 1's first condition [§4.10].
*Plain meaning:* exporting the logs dodges Article 68(12), not the right to erasure.
*Why true:* the ceiling is about a place; the right is about whoever holds the data. Relocation changes the place, not the holder's duty.
*What it does not say:* it is argued from a stated legal premise, not derived, and the artefact does not execute it. If the premise fails, relocation gets stronger; Propositions 1 to 3 are untouched [§4.10].

---

## 7. The mechanism: Crypto-Erasure by Invalidation

The proof of Proposition 2 is the build sheet [§4.8].

1. **Split the record** into accessor fields, subject fields (the patient link) and payload. For record 3 the payload is the demographic query that the IHE patient-discovery transaction (ITI-55) requires gateways to log; for record 100 it is the logged activity [§4.3].
2. **Encrypt.** The payload is encrypted under its own per-record key, held under a key-encrypting key in a hardware security module or equivalent [§4.8].
3. **Commit.** c(a) = Commit(payload, salt) with a per-record salt. It must be hiding (reveals nothing without the salt) and binding (no second payload opens it); an unsalted hash would let guesses be confirmed [§4.8, §4.9].
4. **Log.** Every access, invalidation and link removal goes into an append-only Merkle log with RFC 6962 hashing. Leaves hold the accessor fields, the payload commitment and a salted commitment to the subject fields; never the payload or the subject fields. So the log never needs rewriting [§4.8].
5. **Trigger.** The invalidation month is the earliest of: erasure deadline, ceiling deadline, or a payload retention period the controller sets [§4.8].
6. **Invalidate.** At that month the key is destroyed, and the salt and ciphertext are deleted. For patient-level SPE logs at the ceiling, the subject fields are removed. An invalidation entry records record ID, month, legal ground, authorising actor and a hash of the key's identifier. The key matters for backups that cannot be deleted at once [§4.8].
7. **Terminal transition.** After the floor ends, the identifying metadata is destroyed too, leaving a residue intended to be non-identifiable. Specified, not implemented [§4.8, §6.1].

Cross-border records keep the patient link through the floor: Article 9 EHDS lets patients see who accessed their data [§4.2].

**What an auditor can check after invalidation:** the access happened and by whom; some payload was bound at write time and not substituted; it was invalidated, when, on what ground, by whom; and each entry is in the log as first written, by inclusion proof [§4.8].
**What an auditor cannot check:** the payload, and that the key is really gone. The invalidation entry is *attested, not proven* [§4.9, §6.3]. Rewriting the whole log is caught only against a root published outside it: specified, not implemented [§4.9, §5.7]. The residue is *pseudonymised, not anonymous* until the terminal transition [§4.9]. "Verifiable" in the title qualifies the invalidation record, not the erasure [§1.4].

---

## 8. The evidence

All figures come from one seeded run (seed 20260915) over 200 synthetic records: 100 cross-border (F = 120, primary) and 100 SPE access logs (F = 12, secondary, all treated as reached by the ceiling) [§5.2]. The counts are *synthetic, not frequency estimates*: they follow from generator parameters [§5.3].

- **Semantics I:** 95 violations across 90 records (45%): 37 cross-border, 53 SPE. Five SPE records hit both C2 and C3, so 95 = 90 + 5 (41 C2 only, 44 C3 only, 5 both) [§5.3].
- **Boundary reproduced:** 38 cross-border records got a request; 37 fell inside the window and all 37 violate; the one outside does not [§5.3].
- **No request needed:** 39 of the 78 SPE records with no erasure request still collide (Corollary 1.2, broad reading). Half, because permits run 1 to 12 months in the generator; a five-year permit gives about one in ten [§5.4].
- **Semantics II:** 138 invalidations (52 on Article 17(1), 86 on Article 68(12)); 0 violations across 200 [§5.7]. At delta = 3: 89 records, 94 violations, 39, 138, 0 [§5.6].
- **Log integrity:** 200 of 200 verify. Altering record 100's actor, its invalidation ground, or record 3's patient link each makes V^II fail [§5.7].

**Three cross-checks** [§5.5, §5.8]:
1. *Exhaustive search:* all 2^14 = 16,384 alpha assignments per case over 14 months, four cases. Three conflict cases have no solution; the control case does. A sanity check, not independent evidence.
2. *Z3 bounded SMT check:* nine checks of Propositions 1 to 3 over all parameters within bounds; no counterexample, and four deliberately broken variants are caught.
3. *Synthea payloads:* Synthea-generated FHIR R4 resources replace the payloads; all 200 commitments change and no figure does, because no constraint reads content.

**What this proves:** the code implements the model. **What it does not:** independent evidence for the propositions, a proof for all instances, performance, deployment. Semantics II's zero holds by construction; the falsifiable part is the inclusion-proof check. Key destruction is simulated in program memory; the optional AES-256-GCM module shows 138 records refuse to decrypt and 62 still read [§5.8, §6.3].

**One honesty point.** The reported run derives salts from record IDs so it reproduces exactly; in that run the commitments are therefore not hiding. `--random-salts` draws real random salts [§5.2].

---

## 9. Norway: where it lands

- **Primary use.** Helsedirektoratet and Norsk Helsenett run the NCPeH, in live pilot at two emergency clinics, no relevant patient yet. The mechanism attaches at the sixth OpenNCP step, where the audit record is written [§1.1, §4.11].
- **Secondary use.** Helsedataservice is the presumptive Health Data Access Body (eleven central registries). The mechanism sits at the SPE access-logging boundary, because Norwegian SPEs are fragmented well beyond the three NORTRE nodes, and takes permit expiry from the access body [§4.11].
- **National criteria.** The SPUHiN criteria (hearing 2025, draft 2024) require mandatory identifiable access logs for at least one year and an information-security management system; none says how logs reconcile with deletion. The mechanism adds no requirement of a new kind [§4.11, Table 4.1].
- **Timing.** Implementing acts due 26 March 2027; Articles 68 and 73 apply from 26 March 2029. The collision is not yet operative, which is why designing it now matters [§6.8].

---

## 10. Limitations, owned

- **No authority behind Semantics II.** If a supervisory authority reads "identifiable logs" as requiring readable content, Proposition 2 stays true *in the model* and becomes inert in practice [§6.2]. A Datatilsynet enquiry was sent on 23 September 2026, unanswered at submission [§7.4].
- **Broad reading of Article 68(12)** is contestable; Corollary 1.2 and one branch of Corollary 2.3 depend on it, nothing else [§6.2].
- **Four subsidiary premises** without authority, including Proposition 4's premise and whether auditing after the ceiling needs the patient link [§3.7].
- **Attested, not proven** destruction; simulated in the artefact [§6.3].
- **Not implemented:** terminal transition, per-leaf nonce, proactive invalidation, published roots with consistency proofs, accumulator [§6.1].
- **Informal proofs**, one seed, every request treated as valid, payload as one unit; data *synthetic, not frequency estimates*, US Core profiles [§3.7, §6.7].
- **Six-year pilot floor** is a controller decision; no national legal basis identified [§4.2].
- **Rival 4** (delete and log the deletion) is close to equivalent for cross-border records [§4.10].
- **Evaluation** is analytical; the expert panel is not run [§6.6].

---

## 11. Glossary

- **Audit record:** the log line saying who accessed what, when, why, with what outcome.
- **Payload:** content in the record about *what* was accessed, such as the demographic query.
- **Subject fields / patient link:** the fields tying the event to a patient.
- **alpha(a,t):** 1 if the payload is readable in month t, else 0.
- **V(a,t):** whether the record counts as verifiable.
- **delta:** erasure response period, 1 month (3 if extended).
- **rho(a):** 1 if the ceiling reaches the record.
- **Semantics I / II:** verifiable means readable / accountable.
- **Invalidation entry (iota):** logged record of a payload's removal: month, ground, actor.
- **Commitment:** a value that binds the payload without revealing it.
- **Salt:** per-record random value inside the commitment.
- **Merkle log:** append-only log where any entry can be checked against one root hash.
- **Inclusion proof:** short proof that an entry is in the log under a given root.
- **Published root:** root held outside the log so rewrites can be caught.
- **Crypto-erasure:** making data unreadable by destroying its key.
- **Terminal transition:** destruction of identifying metadata after the floor ends.
- **Pseudonymised:** still personal data for whoever can re-link it.
- **SPE:** Secure Processing Environment, where researchers work on permitted data.
- **NCPeH:** National Contact Point for eHealth.
- **HDAB:** Health Data Access Body; in Norway, Helsedataservice.
- **Broad / narrow reading:** Article 68(12) reaches patient-level logs / only the permit dataset.
- **Synthea:** generator of synthetic patient records in FHIR R4.

---

## 12. Five sentences to remember

1. The impossibility follows from an assumption about one word, verifiable, not from the obligations.
2. If verifiable means readable, any record with a deadline inside its window has no lawful schedule (Proposition 1).
3. If verifiable means accountable, every record has one, and the proof is the mechanism (Proposition 2).
4. A ceiling collides with a floor only if it is no longer, and an outside anchor hides the clash in each record's history (Proposition 3).
5. Destruction is attested, not proven; the residue is pseudonymised, not anonymous; the counts are synthetic, not frequency estimates; all of it holds in the model.

---

## Not verified

- The Molde and Helsinki framing of record 3, and its request month 115, come from the deck speaker notes; the thesis prints the witness line ("t=116 within [11,131]") but does not label it record 3 or name the cities.
- No code was re-run; all figures were checked against the thesis text only.
