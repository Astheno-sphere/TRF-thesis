# Viva preparation sheet: VERA-SNARK / TRF thesis

Candidate: Arshad Akhtar Abbasia (Tiger). Examiners: Prof. João Ferreira, Joel Curado. 15-minute talk, 30 minutes of questions.

**Conventions.**
- Thesis pages are printed page numbers of the submitted PDF (PDF page minus 14; front matter in roman). "Slide n (id)" is deck position. App links start from https://trfhimolde.streamlit.app/.
- The thesis says **Semantics I / II**; the deck says Reading I / II. Semantics I: verifiable means readable (V = α). Semantics II: verifiable means accountable.
- Say "in the model" and "generated" with every count. Say "attested", not "proven", for key destruction; "pseudonymised", not "anonymous"; "tamper-evident", not "tamper-proof". Propositions 1 to 3 are proved informally; Proposition 4 is argued from a stated premise. No theorems.
- "Since submission" marks facts that are not in the thesis.

**Numbers cold** (seed 20260915). 200 records: 100 cross-border (F = 120, illustrative), 100 SPE logs (F = 12). Semantics I: 95 violations, 90 records (37 cross-border, 53 SPE; 41 C2-only, 44 C3-only, 5 both). 39 of 78 SPE logs with no request collide (broad reading). Semantics II: 138 invalidated (52 under Art 17(1), 86 under Art 68(12)), 0 violations. Z3: 9 of 9. Floors in months: 72 (Norwegian pilot), 120 (illustrative), 36 (Art 9(2) EHDS), 12 (SPE).

---

## Group 1. Why this thesis, why now

### 1. Why this problem, and why now?

**Say it.** "The EU health data law is being built now. The detailed rules for research environments are due in March 2027 and apply from March 2029, and Norway's cross-border system is already in pilot. So the clash between audit logs and deletion rules can still be settled in the specification, not patched afterwards."

**Exactly.** Regulation (EU) 2025/327 entered into force 26 March 2025 and applies generally from 26 March 2027. Art 73(5) implementing acts for SPEs are due by 26 March 2027. Arts 68 and 73 apply from 26 March 2029. Norway's NCPeH pilot (Helsedirektoratet, Norsk Helsenett) is live at emergency clinics in Bodø and Stjørdal; no relevant patient had presented at the last report. Not claimed: that the collision is operative today.

**Example.** Record 3: clinician HP-003 via NCP FI looks up a Molde patient in month 11. The record must stay verifiable to month 131 (illustrative floor); an erasure request in month 115 sets the payload deadline at 116.

**Point to.** §1.1 p. 1; §1.2 p. 3; §2.2 p. 16; §6.8 p. 98. Slides 3 (record), 5 (research), 31 (q-adoption). App: ?p=norway

**Follow-up.** "A 2029 problem?" Yes, and that is the argument: a framework that arrives after infrastructure hardens is "archaeology" (§6.8).

---

## Group 2. Why Design Science Research

### 2. Which DSR framework, which artefacts, how evaluated?

**Say it.** "Design science means building something to solve a real problem and showing it works. Hevner gives the frame and the artefact types; Peffers gives the six steps. My artefact is a formal model plus a working sandbox, evaluated by argument and by running code, not in the field."

**Exactly.** Hevner et al. (2004): paradigm and artefact types (constructs, models, methods, instantiations). Peffers et al. (2007): six-activity process, problem-centred entry; the activities map onto Chapters 1 to 7, with a formal-modelling step between Activities 2 and 3 (§3.2). Artefacts: a model (TRF) and a partial instantiation (sandbox); nothing deployed. Evaluation (§3.7 p. 44): internal validity, compatibility with verified infrastructure (Table 4.1), determinism. §6.6 (p. 96) calls it artificial, not naturalistic (Venable et al. 2016); utility and acceptance are not evaluated. The thesis does not tabulate Hevner's seven guidelines, so have this oral mapping ready and say it is your mapping: G1 artefact (TRF model, the mechanism, the checker); G2 relevance (the EHDS collision, Norway's pilot, Ch1); G3 evaluation (proofs, exhaustive search and Z3, the 200-record demonstration, Ch5); G4 contribution (the field-level conflict criterion, the readable versus accountable distinction, the mechanism); G5 rigour (formal proofs, primary legal sources, reproducible code on Zenodo); G6 design as search (rival designs in Ch2, supervisor and red-team iterations); G7 communication (thesis, NORS 2025, app, archive).

**Example.** The SNARK design was dropped when the formal analysis showed commitments and a logged registry suffice (§3.2).

**Point to.** §3.1 to §3.3 pp. 37 to 38; §3.7 p. 44; §6.6 p. 96. Slide 19 (q-snark). App: ?p=ledger

**Follow-up.** "Circular evaluation?" Partly: Semantics II holds by construction (§5.8); the falsifiable part is the inclusion-proof check, which three tamper tests show can fail.

### 3. Why not a survey or interviews?

**Say it.** "Interviews give opinions, not a mechanism, and the central questions are legal, so only an authority can settle them. I designed a practitioner panel, Appendix C, but have not run it: it needs ethics notification and weeks of lead time."

**Exactly.** §3.1 rejects interviews (no mechanism), a literature review (no design) and pure formal methods (no artefact). Appendix C: eight experts, two each from data protection, health IT, SPE operation, information logistics; a semi-structured guide and 16 Likert items. Not run: it would process personal data about identifiable professionals, needing Sikt notification (four to six weeks) and revision of the no-human-participants statements.

**Example.** The ethics statement is accurate as submitted: only correspondence with public authorities, officials named in their official capacity (§3.9 p. 46).

**Point to.** §3.1 p. 37; §3.8 p. 46; Appendix C p. 160; §7.5 p. 107.

**Follow-up.** "So the evaluation is thin?" On utility and acceptance, yes; §6.6 says so.

## Group 3. Research question

### 4. Research question and sub-questions in one breath.

**Say it.** "How can a verifiable crypto-erasure mechanism reconcile the three retention rules on cross-border health audit records, keeping audit integrity, in Norway? One: where exactly do they conflict and when can all hold? Two: can invalidating the payload meet all three? Three: how does it fit Norwegian infrastructure?"

**Exactly.** §1.3 p. 6, verbatim: "How can a verifiable crypto-erasure mechanism be designed to reconcile the conflicting data-retention requirements of cross-border health data exchange under the European Health Data Space, while preserving audit integrity in a Norwegian implementation context?" Answers (§7.1 p. 104): SQ1 is Proposition 1, Corollaries 1.1 and 1.2, Proposition 3. SQ2 is yes, within the model (Proposition 2, Corollary 2.2). SQ3 is compatible by specification, not deployment (Table 4.1).

**Example.** Record 3 shows floor against right; record 100 shows floor against ceiling.

**Point to.** §1.3 p. 6; §7.1 p. 104. Slide 2 (promise). App: ?p=start

---

## Group 4. The TRF model

### 5. Walk me through the variables.

**Say it.** "For each audit record and month there is one yes-or-no question: can the payload still be read? Call it alpha. Everything else is a clock: when the record was made, how long it must be kept, when an erasure request arrives, when a research permit ends."

**Exactly.** §4.3 p. 51; Nomenclature p. xii. Record a: metadata m(a) = m_acc  ∪  m_subj, payload p(a), commitment c(a) = Commit(p(a), r(a)) with salt r(a), key k(a), creation month t(a), floor F(a), pathway σ(a). Events: erasure request t_r(a) (∞ if none), permit expiry t_π(a), response period δ (1, or 3 if extended; GDPR Art 12(3)), optional payload period P(a). States: α(a,t) payload recoverable; β(a,t) subject link readable; V(a,t) verifiable; ρ(a) = 1 where the ceiling reaches the record; ι(a) invalidation entry. Invalidation month t^I(a) = min(t_r + δ, t_π + 6, t + P).

**Example.** Record 3: t = 11, F = 120, t_r = 115, so t^I = 116. Record 100: t = 7, F = 12, t_π = 10, so t^I = 16.

**Point to.** §4.3 p. 51. Slide 7 (model; floor now reads "ten years illustrative, the Norwegian pilot sets six"). App: ?p=start

**Follow-up.** "Why one binary variable?" Deliberately minimal, so nothing hides the one question the conflict turns on.

### 6. What are C1 to C3, and what does "tri-lateral" mean?

**Say it.** "The floor says the record must stay checkable for its whole retention window. The erasure right says the payload must be unreadable a month after the request. The ceiling says research data must be gone six months after the permit ends. Tri-lateral means three kinds of rule, floor, right and ceiling, not three laws."

**Exactly.** C1: V(a,t) = 1 for t in [t(a), t(a) + F(a)], a closed window of F + 1 months (conservative for "at least"). C2: α = 0 for t ≥ t_r + δ. C3: for secondary records with ρ = 1, α = 0 and β = 0 for t ≥ t_π + 6. C1 is a lower bound on V; C2 and C3 are upper bounds on α. Whether they conflict depends on how V relates to α. The floor is one parameterised constraint with two instances, so tri-lateral counts constraint types, not instruments (§1.3, §3.4).

**Example.** Record 3: C1 needs V = 1 for months 11 to 131; C2 needs α = 0 from 116. If V = α, months 116 to 131 need both.

**Point to.** §4.4 p. 54. Slides 4 (strip), 7 (model). App: ?p=witness&r=3&m=116

---

## Group 5. The propositions

### 7. Proposition 1 and Corollary 1.1.

**Say it.** "If verifiable means readable, then whenever a deletion deadline falls inside the keep period, the payload must be readable and gone in the same month. That is impossible, however clever the design."

**Exactly.** Under Semantics I, {C1, C2, C3} is infeasible for any record with t_r + δ ≤ t + F, or t_π + 6 ≤ t + F (the second tested only where σ = secondary and ρ = 1). Proof: at t* the deadline month, C1 forces α = 1 and C2 or C3 forces α = 0. Converse (p. 57): no deadline inside the window means feasible, so the statement is exact. Corollary 1.1: at F = 72, a request in any of the 72 months t to t + 71 collides. Not claimed: how often requests arrive.

**Example.** Record 3: t* = 116 ≤ 131, so it fails. Record 38: t = 10, request month 138, deadline 139 > 130, so no collision: the one request outside its window, exactly what the proposition excludes (§5.3).

**Point to.** §4.6 p. 57. Slide 9 (result). App: ?p=propositions

**Follow-up.** "Trivial?" Yes, by design (§4.7). It shows some departure from readable-verifiability is unavoidable.

### 8. Corollary 1.2: the collision with no erasure request.

**Say it.** "In a research environment the same law says keep identifiable access logs for a year and delete health data six months after the permit ends. If a log entry near a permit's end counts as health data, the rules overlap and nobody asked for anything. That holds on one reading of the law only, and I say so."

**Exactly.** For SPE logs (F = 12) with t_π + 6 ≤ t + 12 and ρ = 1, C1 and C3 contradict at t_π + 6 under Semantics I. Condition: Art 68(12) reaches access logs kept at patient-record granularity (broad reading), and activity content is data concerning health. The run's 50 per cent comes from uniform 1 to 12 month permits; a five-year permit gives about one in ten.

**Example.** Record 100: created 7, permit expires 10, ceiling at 16, floor to 19; months 16 to 19 collide. 39 of 78 no-request SPE logs collide.

**Point to.** §4.6 pp. 57 to 59; §5.4 p. 84; Figure 5.2 p. 85. Slides 5 (research), 21 (q-reading). App: ?p=witness&r=100&m=16

**Follow-up.** "Narrow reading?" See Q23.

### 9. Proposition 2 and Corollaries 2.1, 2.2.

**Say it.** "If verifiable means accountable, meaning who acted, when, a binding fingerprint of the payload, and a logged note of invalidation, all three rules hold for any record, any timing and any retention period. The proof is also the recipe: destroy the payload at the earliest deadline, keep the accountability, log the deletion."

**Exactly.** Under Semantics II (V = 1 iff accessor fields intact, commitment present, every loss of readability logged), {C1, C2, C3} is satisfiable for every record, arrival pattern and F. Proof: α = 1 before t^I; at t^I destroy k(a), remove subject fields where C3 reaches them, append ι(a). C1 holds because nothing touches m_acc or c(a) and ι is logged. Corollaries: no coordination needed (2.1); no result depends on F (2.2). Not claimed: lawfulness or verifiable key destruction (§4.7 p. 63).

**Example.** Record 3: t^I = min(116, ∞, ∞) = 116, ground Art 17(1); patient link kept. Record 100: t^I = 16, ground Art 68(12); subject link removed at 16.

**Point to.** §4.7 pp. 60 to 61. Slides 9, 11 (audit). App: ?p=propositions

**Follow-up.** "You defined Semantics II to make this work." Conceded (§4.7 p. 62): the claim is that this semantics is a defensible reading, argued in §4.2.

### 10. Corollary 2.3: what if auditing needs part of the payload?

**Say it.** "If an auditor needs part of what was logged, I keep that part with the accessor fields. That works everywhere except where that part is itself health data inside a research environment."

**Exactly.** Split p = p_n  ∪  p_r; keep p_n. C1 and C2 hold (C2 via Art 17(3)(b), since p_n is necessary). C3 holds unless p_n is health data in the SPE on the broad reading; then C1 and C3 collide as in Proposition 3. Exits: relocation, dataset-granularity logs, the narrow reading, anonymising p_n.

**Example (illustration, not a run result).** If part of record 100's activity content were needed and counted as health data, it would collide over months 16 to 19.

**Point to.** §4.7 p. 62. Slide 21 (q-reading).

**Follow-up.** "Why assume nothing is needed?" §4.2 argues per record class; for SPE logs it is weaker, hence this corollary.

### 11. Proposition 3 (anchoring).

**Say it.** "A deletion limit can only clash with a keep-for limit if it is no longer than it. Whether the text shows the clash depends on where each clock starts. Same start: visible. Different start: only each record's own history shows it."

**Exactly.** Floor F runs from t(a), ceiling L from e(a) ≥ t(a). Under Semantics I they are jointly satisfiable iff e + L > t + F. (i) Same anchor: iff L > F. (ii) External anchor, L ≤ F: fail for exactly the records with e − t ≤ F − L. Proof: the floor needs α = 1 to t + F, the ceiling α = 0 from e + L.

**Example.** Art 68(12): L = 6, F = 12, F − L = 6. Record 100: e − t = 3, collides (Q13 gives the contrast).

**Point to.** §4.6 p. 60. Slide 30 (q-props34). App: ?p=anchor

**Follow-up.** "Verified?" Z3 checks both directions and both cases, and refutes an off-by-one version (§5.5 pp. 85 to 86).

### 12. Proposition 4 (location and right).

**Say it.** "A common fix is to export logs out of the research environment when the permit closes. That meets the deletion limit but not the erasure right, because the right follows the data to whoever holds it. This rests on one legal premise, which I state openly."

**Exactly.** Premise (not derived): a controller receiving a relocated record receives the Art 17(1) duty with it. Then, under Semantics I, relocation meets ceiling and floor, but the floor and right remain infeasible for records meeting Proposition 1's first disjunct. It is a legal argument in proposition form; the artefact does not execute it. Relocation moves subject fields to a second controller. Export is accepted as sufficient for Corollary 1.2.

**Example (from the checker, not named in the thesis).** Record 132: created 1, request month 4 (deadline 5), permit expiry 7 (ceiling 13). Export before 13 meets the ceiling; the month-5 deadline still sits inside the floor.

**Point to.** §4.10 p. 72. Slide 30 (q-props34).

**Follow-up.** "If the premise is wrong?" Rival 6 gets stronger; Propositions 1 to 3 stand.

---

## Group 6. The anchor condition

### 13. Explain e(a) − t(a) ≤ F − L, and why the ceiling's start matters.

(The brief's s is the thesis's t(a), the creation month.)

**Say it.** "Subtract the ceiling length from the floor length. A record collides if its permit ends within that many months of the log entry. Write an entry near a permit's end and the six-month deletion clock runs out before the twelve-month keep clock. The start matters because the clash hides in each record's timing, not in the law's wording."

**Exactly.** With F = 12, L = 6: collision iff the permit expires within 6 months of the entry. Any collision needs L ≤ F whichever anchor is used; the anchor decides only whether the text reveals it. Reading §17 politiregisterloven as anchoring both periods at the entry is a reading of the syntax (§6.10 pp. 100 to 101).

**Example.** Record 100: t = 7, permit 10, ceiling 16, floor to 19; e − t = 3 ≤ 6, collides. Record 102: t = 5, permit 12, ceiling 18, floor ends 17; e − t = 7 > 6, clear by one month. §17: floor 12 and ceiling 36 both from the entry, L > F, no collision (60 records, 7 violate, none without a request).

**Point to.** §4.6 p. 60; §6.10 p. 100. Slides 20, 30. App: ?p=anchor

**Follow-up.** "Does §17 anchor both at the entry?" A reading, stated as such. [CHECK] The Lovdata check of §17 is open in the RT2 report; bring the statute text.

## Group 7. The mechanism

### 14. What is kept, what is destroyed, when?

**Say it.** "At the earliest deadline I destroy the payload, its key and its salt. I keep who looked, when, under what authority, a sealed fingerprint of the payload, and a logged note of the invalidation. The log never holds what erasure reaches, so nothing on it needs erasing."

**Exactly.** Kept: accessor fields, commitment c(a), ι(a), log leaf hashes; cross-border records keep the patient link through the floor. Destroyed at t^I: k(a), r(a), ciphertext. For patient-level SPE logs the subject fields go at t_π + 6, with a logged removal. Log leaves hold accessor fields, the payload commitment, a salted subject-field commitment and invalidation entries, never payload or subject fields. Specified, not implemented: terminal transition, per-entry nonce, proactive invalidation, consistency proofs, accumulator (§6.1). Per-record keys are the simplest construction, not the only one.

**Example.** Record 100 after invalidation: accessor fields True (R-008, permit DP-015); subject link removed month 16; commitment 678ade47c1e6dc03...; key, salt, ciphertext None; ι month 16, ground EHDS Art 68(12); payload readable False. Code: `apply_invalidation`, line 270.

**Point to.** §4.8 pp. 63 to 67; Figure 4.1 p. 64; §5.7 p. 87. Slides 10, 11. App: ?p=built

**Follow-up.** "What can an auditor check?" Access happened and by whom; a payload was bound, not swapped; when, why, by whom invalidated; no logged entry altered. Not that the key is gone (p. 66).

### 15. What is the hiding commitment, and why does it matter?

**Say it.** "It is a sealed fingerprint of the payload. A plain hash could be confirmed by anyone who guesses the payload, say a diagnosis code. So I add a secret random salt and destroy it with the key."

**Exactly.** c(a) must be hiding and binding; a bare unsalted hash is not allowed (§4.3, §4.9 p. 68). Before invalidation an auditor can open it and detect substitution. After, only a party that kept an opening (the patient, the home NCP) can; otherwise it fixes only that some payload was bound. Say first: in the reported run the salt is derived from the record identifier for reproducibility, so it is not hiding in that run; `--random-salts` uses os.urandom (§5.2 p. 80). The subject-link salt is derived too and pseudonyms come from a small space (RT2).

**Example.** Altering record 3's patient link makes V_II fail, since it no longer opens the logged commitment.

**Point to.** §4.8 p. 65; §4.9 p. 68. Slide 27 (q-residue).

### 16. What does the Merkle log prove? Can the operator rewrite it? Why not a blockchain?

**Say it.** "It lets an auditor check one entry is present and unchanged, with a short proof. It does not stop an operator rewriting everything. That needs earlier roots published outside the operator, which I specified but did not build."

**Exactly.** RFC 6962 hashing, as in Certificate Transparency; an inclusion proof needs about log₂ n hashes, roughly thirty for a billion entries (§6.5). Catches an altered entry, ground or patient link: three tamper tests, all make V_II false. Does not catch a wholesale rewrite; that needs published roots and consistency proofs (specified, not built). The operator is a named trusted party: alteration is detectable, not impossible. Once a root containing an invalidation entry is published, it cannot be withdrawn. Blockchain: an immutable ledger is where erasure fails (Finck); the design takes the one thing a chain adds, tamper evidence, and keeps erasable content off it.

**Example.** Record 100: change the actor and the access entry fails its proof; change the ground and the invalidation entry fails. The run has 438 entries; 200 of 200 records verify.

**Point to.** §4.8 p. 66; §4.9 p. 69; §5.7 p. 87; §2.4 p. 22. Slides 18 (q-chain), 29 (q-roots). App: ?p=run

### 17. Why does destroying a key count as unreadable, and is it erasure?

**Say it.** "Destroying the key makes the encrypted copy unintelligible, but the European Data Protection Board says encrypted personal data is still personal data. So I do not rely on the key for the main copy: the store deletes the payload. Keys cover copies I cannot delete at once, like backups, and I state them as a bounded residue."

**Exactly.** EDPB Guidelines 02/2025 para 51: unintelligible "at least until the algorithm is broken", yet still personal data; para 125: erasure needs the data erased or anonymised. The model cannot tell key destruction from deletion (both set α = 0); keys earn their place for copies, which TEHDAS2 OPR-6 reaches ("including any backups or redundant copies", §4.8 p. 65). NIST SP 800-88 Rev. 2 recognises cryptographic erase within a documented key-management boundary.

**Example.** The AES-256-GCM module: 138 scheduled destructions, exactly those records refuse to decrypt, 62 still read; destruction is in program memory.

**Point to.** §4.8 p. 65; §4.9 p. 69; §6.3 p. 94. Slide 25 (q-keys). App: ?p=robust

---

## Group 8. Novelty and competitors

### 18. What is new, what is borrowed?

**Say it.** "The cryptography and the method are borrowed. What is new is putting a keep rule, an erasure right and a deletion limit on one record in one model, finding that the word 'verifiable' decides whether all can hold, and showing where the clash hides. I also specify the mechanism and check its residue."

**Exactly.** Borrowed (§2.4 to §2.5): hash-chained logs (Schneier & Kelsey 1999); Merkle proofs (Crosby & Wallach 2009); Certificate Transparency (Laurie et al. 2013); hiding commitments; crypto-erase (NIST SP 800-88 Rev. 2); Ephemerizer, Vanish, policy-based deletion; formal compliance as satisfiability (Feng et al. 2023). Rejected log-editing family: chameleon hashes, redactable signatures and blockchains. New, in the reviewed literature (§2.10 p. 36): the formal tri-lateral characterisation, verifiability as the deciding parameter, Proposition 3, the information-logistics expression, the cross-border health instantiation on the Norwegian substrate, the residue analysis.

**Example.** DePaul keeps recoverable copies to a purge date. Record 100's readable copy must be gone at month 16, though the floor runs to 19.

**Point to.** Statement of Contribution pp. ix to x; §2.8 p. 32; §2.10 p. 36.

**Follow-up.** "Just framing?" A contribution of framing and feasibility, and p. x says so.

### 19. Competitors and alternatives: why does TRF differ?

**Say it.** "Others did pieces: blockchain audit logs, zero-knowledge access control, key destruction. None treats a keep rule, an erasure right and a deletion limit together, or says what an auditor can check once the payload is gone."

**Exactly.** Table 2.1 (§2.8 p. 32); Rivals (§4.10 pp. 70 to 72). Rejected there too: rely on Art 17(3)(b), anonymise (breaks C1), minimise at capture, export logs (Proposition 4). Aikebaier (2026), a preprint, formalises only erasure.

| Competitor | Does | TRF differs |
|---|---|---|
| KONFIDO (Natsiavas et al. 2021) | OpenNCP toolkit, SGX, blockchain audit | Erasure unresolved; hardware-bound |
| ZK-EHR (Albalwy 2026) | Groth16 credential proofs, one jurisdiction | Access control, not retention |
| DePaul (Scope & Rasin, US 12,425,209) | Recoverable encrypted copies, key destroyed at a purge date | Works for two floors; recoverable copies are what a ceiling forbids (Rival 5) |
| Crypto-shredding pattern (VeritasChain 2026) | Per-subject key destroyed on request | Bilateral, asserted, no model or verifiability semantics |
| Redactable chains, chameleon hashes | Editor rewrites content | This log is never edited |

**Example.** Rival 5 against record 100: holding recoverable ciphertext to month 19 is exactly what the month-16 ceiling forbids.

**Point to.** §2.4 pp. 21 to 25; §4.10 pp. 70 to 73. Slides 18, 28 (q-rival4).

**Follow-up.** "Delete the record and log the deletion: why more?" Conceded: for cross-border records it is "close to an equivalent design". The design adds an attributed, grounded, tamper-evidently bound entry and a commitment that detects substitution before invalidation, and afterwards where an opening was handed over. In SPE logs it does work deletion cannot (§4.10 p. 71).

---

## Group 9. The evidence

### 20. What do the 200 records show?

**Say it.** "Two hundred generated audit records. Read as 'verifiable means readable', ninety fail, ninety-five violations. Read as 'verifiable means accountable', none fail. The counts follow my generator, not real life. What is checked is the shape of the result."

**Exactly.** Table 5.2 p. 82: cross-border F = 120, request probability 0.40; SPE F = 12, permit expiry t + 1 to 12, request probability 0.25. Table 5.3 p. 83: 90 of 200 records (37 and 53); 95 violations because 5 SPE records collide with both C2 and C3. Proposition 1's conditional shape is reproduced: 38 cross-border requests, 37 inside the window, all 37 violate, the outside one does not. Table 5.6 p. 87: 138 invalidated (52 and 86), 0 violations.

**Example.** Record 3 is among the 37; record 100 among the 39 Corollary 1.2 witnesses.

**Point to.** §5.3 to §5.4 pp. 83 to 85; §5.7 p. 87. Slide 12 (evidence). App: ?p=ledger

**Follow-up.** "Zero under Semantics II means nothing." It holds by construction (§5.8 p. 89); the integrity check can fail, and does under tampering.

### 21. How was it checked?

**Say it.** "A checker can be wrong, so I ran three things: a search over every yes-no assignment on small cases, a solver hunting for counterexamples, and a swap of the payloads for generated health records. Honest limit: this shows my code matches my model, not independent proof."

**Exactly.** Exhaustive search: 2¹⁴ = 16,384 assignments per case, 4 cases (three conflicts infeasible, control feasible); a sanity check, since constraints are pointwise (§5.5 pp. 85 to 86). Z3: floor 1 to 120, δ 1 to 3, horizon 140; 9 of 9 no counterexample; refutes four broken variants (no ι, no commitment, no subject-link entry, Proposition 3 off by one). Synthea: 98 bundles; 200 of 200 commitments change, all six measures identical (Table 5.7 p. 90). All were written in the same AI-assisted process: they check code against encoding, not encoding against law.

**Example.** At δ = 3, Semantics I falls from 95 to 94 violations (90 to 89 records); the Corollary 1.2 count stays 39, since the ceiling does not involve δ (Table 5.5 p. 87).

**Point to.** §5.5 to §5.6 pp. 85 to 87; A.23 p. 150. Slides 12, 24 (q-proofs). App: ?p=robust

### 22. What can synthetic data show, and what not?

**Say it.** "It shows structure: when rules collide and when they do not. It cannot show how often this happens in Norway, and it says nothing about Norwegian clinical practice. The model reads timing, never content."

**Exactly.** Can show: Proposition 1's conditional shape; invariance to payload content; that the checks can fail. Cannot show: frequencies; real permit durations (none used; uniform 1 to 12 months is an assumption); valid-request share (all treated valid); Norwegian representativeness. Synthea's default is US Core; FHIR R4 matches the Norwegian basisprofiler.

**Example.** Tripling δ moves 95 violations to 94 and nothing structural.

**Point to.** §3.5 pp. 41 to 42; §5.8 p. 89; §6.7 p. 97. Slides 23 (q-permits), 26 (q-synthea). App: ?p=synthea

**Follow-up.** "Your patients are American." Yes; no figure moved when 200 of 200 commitments changed.

---

## Group 10. Limits and threats to validity

### 23. Does Art 68(12) reach access logs, and if not, what is left?

**Say it.** "That reading is contestable, and I say so. On a narrow reading the deletion rule covers only the research dataset and my no-request collision disappears. The semantics, the propositions and the mechanism stay, because Proposition 1 needs only that one valid erasure request falls inside a retention window."

**Exactly.** Broad: the text is framed by location ("within the secure processing environment"), and a patient-level entry reveals cohort membership. Narrow: it sits in the data-permit article and concerns the permit dataset. Harmonising: it reaches logs but yields to Art 73(1)(e). On the narrow reading Corollary 1.2 lapses (and the conditional branch of Corollary 2.3), along with the single-record three-way collision. Propositions 1 to 4, Corollary 1.1, the mechanism and the semantics stand. Do not say the three-way collision survives the narrow reading (RED_TEAM.md R3 "move 2" is superseded by §4.6).

**Example.** On the narrow reading in the generated set, 44 ceiling-only collisions lapse (39 witnesses plus 5 with requests outside the window), leaving 9 SPE records.

**Point to.** §4.6 pp. 58 to 59; §6.2 p. 92; §7.4 p. 106. Slide 21 (q-reading). App: ?p=witness&r=100&m=16

**Follow-up.** "Will the Commission clarify it?" Do not say so; it is for an authority or court, and the EHDS-side question is not yet asked.

### 24. Is the residue anonymous?

**Say it.** "No. It names the clinician and, until the end, links to the patient: pseudonymised. The legal test I rely on is erasure, not anonymisation, and the store meets it by deleting the payload, key and salt."

**Exactly.** Datatilsynet (2015): data stay personal while any re-identifying key or linkage is held. EDPB draft Guidelines 02/2026 (adopted 7 July 2026): isolation, linkage, inference; encryption is not anonymisation. CJEU (2025, paras 73, 76 to 77): for the controller holding the additional information, pseudonymised data stay personal. The terminal transition (t + F + 1) and per-entry leaf nonce are specified, not implemented. Any claim of anonymisation "would be false" (§4.9).

**Example.** Record 100 still carries actor R-008 and permit DP-015, as Art 73(1)(e) requires identifiable logs.

**Point to.** §4.9 pp. 68 to 69. Slide 27. App: ?p=witness&r=100&m=19

### 25. You cannot prove the key was destroyed.

**Say it.** "Correct. Nobody can verify key destruction from outside. The entry is an attestation: who destroyed which key, when, on what ground. An auditor can check the claim was made and not altered, not that it is true."

**Exactly.** The entry holds a hash of the key's identifier. Reardon et al. (2013): crypto-erase is the limiting case of how hard destruction is to assert. Trust assumptions (§4.9 p. 69): controller destroys as stated; custody boundary keeps nothing; log operator does not rewrite (detectable only with published roots); hash and cipher hold over the horizon. A FIPS 140-3 HSM attests design, not a particular destruction (§6.3). Proof needs proof-of-secure-erasure or certified deletion, where public verifiability is open (Broadbent & Islam 2020).

**Example.** The custody object stands in for an HSM; none of the 62 surviving keys opens record 3.

**Point to.** §6.3 p. 94; §4.9 p. 69. Slide 25.

**Follow-up.** "Is attestation enough?" No, never claimed; it improves on unlogged deletion, and against logged deletion the edge is the commitment.

### 26. What does the model leave out, and what is not deployed?

**Say it.** "A month is the unit because every law here speaks in months or years. The model treats every erasure request as valid and a payload as one block, so frequencies are unreliable, not the propositions. And nothing is deployed: no contact point, no performance figures, keys destroyed only in program memory."

**Exactly.** C1 is closed (conservative); C2 binds from the start of month t_r + δ, so boundary months can be grid artefacts (RT2 drill V-7). Seventh and eighth limitations: all requests valid; payload one unit (§3.7 p. 45). Not done: NCPeH connection, OpenNCP flow, authentication, consent, timing, hardware custody. Specified, not built: published roots, nonce, terminal transition, proactive invalidation, accumulator (§6.1). Integration is by specification (Table 4.1).

**Example.** Record 3 at δ = 3: deadline 118, still inside the window.

**Point to.** §3.7 pp. 44 to 45; §4.3 p. 51; §6.1 p. 91; §7.5 p. 107. Slide 14 (limits).

---

## Group 11. Norway

### 27. Helsedirektoratet: six years against your ten.

**Say it.** "I asked Helsedirektoratet for the source of the log retention period. They said no specification fixes one, it is left to national law, and for the pilot they chose six years. The production figure is their decision as controller. So I treat the floor as a parameter and use ten years only as an illustration."

**Exactly.** Enquiry Mon 5 Oct 2026; reply Mon 19 Oct 2026 from Hans Löwe Larsen, Avdelingsdirektør (Appendix D, with permission). Ten years is an unsourced secondary-literature figure; no result depends on F (Corollary 2.2). §4.2: the six-year period is a controller decision; absent a national legal basis it is a policy floor, so before Art 9 EHDS applies in 2029, keeping the patient link against a request has no secure Art 17(3)(b) basis. **Since submission:** Helsedirektoratet's public privacy notice (revised 30 June 2026) states six years for the accessor fields: name, HPR number, role, institution, place, time of lookup. The article source check records it citing GDPR Art 6(1)(c) with pasientjournalloven §22 as the legal basis for the logging. Precision: the Directorate's privacy notice names §22 as the legal basis for the logging; it does not say §22 itself sets six years. The thesis found no national provision fixing the period, and Larsen's reply says the period was a pilot decision.

**Example.** At six years record 3's floor ends at month 83, so its month-116 request falls after it: no collision.

**Point to.** §2.3 pp. 17 to 18; §4.2 pp. 50 to 51; Appendix D p. 168. Slides 4, 14, 31. App: ?p=norway

**Follow-up.** "Which Norwegian law fixes it?" None identified in the thesis; the specifications defer to national law.

### 28. NCPeH, HDAB, FHI: where does it attach?

**Say it.** "At two narrow points: the last step of the cross-border exchange, where the audit record is written, and the logging boundary of a research environment. It asks nothing new of Norway's systems."

**Exactly.** NCPeH: Helsedirektoratet and Norsk Helsenett; the mechanism attaches at step six of the OpenNCP flow. Folkehelseinstituttet (FHI) is the Ministry-designated coordinating Health Data Access Body; Helsedataservice, within FHI, decides access for eleven central registries; how many bodies Norway will have is not settled (§2.6 p. 28). SPEs (TSD, SAFE, HUNT Cloud under NORTRE) are fragmented down to disconnected PCs (SPUHiN 2024), so the mechanism works on the log every environment must produce. It adds no requirement of a new kind to the national criteria (ISMS, tamper-proof logs)..

**Example.** Record 3 is written at the NCPeH audit repository; record 100 at an SPE logging boundary under permit DP-015.

**Point to.** §4.11 pp. 73 to 74; Table 4.1 p. 74; §2.2 p. 16. Slide 15 (forward). App: ?p=norway

### 29. Which authorities have you asked, and what is open?

**Say it.** "Two letters. Datatilsynet got the GDPR questions on 23 September, no reply at submission. Helsedirektoratet answered the retention-floor question on 19 October. The question about Articles 68(12) and 73 is still to ask, on the EHDS side."

**Exactly.** Do not merge these. Datatilsynet (23 Sep 2026): GDPR-side questions, including whether an invalidated record discharges a retention obligation (§7.4; Appendix D.2 p. 169). Helsedirektoratet: the floor only (Q27). Still to ask (Helsedirektoratet, the Ministry or the Commission): whether Art 68(12) reaches patient-level logs, and whether Art 73(1)(e) needs the subject link after the ceiling. Status: no reply from Datatilsynet as of submission; say so plainly unless one has arrived.

**Example.** If an authority says "identifiable logs" must stay readable, Proposition 2 stays true of the model and becomes "practically inert" (§6.2 p. 92).

**Point to.** §6.2 p. 92; §7.4 p. 106. Slides 14, 22. App: ?p=start

**Follow-up.** "If they say no?" That refutes the move cleanly and shows what would have to change.

---

## Group 12. Hard and hostile questions

### 30. Why VERA-SNARK if there are no SNARKs?

**Say it.** "There is no SNARK, and the thesis says so. The name comes from my NORS 2025 presentation, where I planned zero-knowledge proofs. The formal analysis showed commitments and a logged registry are enough, so I dropped them. That is the design cycle working."

**Exactly.** Statement of Contribution note on the name (p. x); §1.6 p. 9; §3.2 p. 38. Zero knowledge returns at one point: proving all of a patient's records were invalidated without revealing which (§7.5 p. 107; Aikebaier's fourth open problem).

**Example.** An auditor seeing record 3's invalidation is fine; proving "every record of hers was invalidated" without listing them would expose her care history.

**Point to.** Slide 19 (q-snark). App: ?p=built

**Follow-up.** "Why keep the name?" Continuity with NORS 2025, stated on p. x.

### 31. Isn't this just crypto-shredding?

**Say it.** "The technique is crypto-shredding and I claim no new cryptography. I add a model showing when it can meet three rules together, a precise meaning of 'verifiable' that makes it possible, and a record an auditor can check."

**Exactly.** Concede the pattern is established (NIST SP 800-88). Differences: it is bilateral and asserted; this adds a ceiling, a model and verifiability semantics (§2.4 p. 25). Own the weak spot: the model cannot tell key destruction from deleting the payload, so keys rest on copies (OPR-6), not a proposition (§4.8 p. 65). Rival 4: for cross-border records delete-and-log is close to equivalent; the weight is in the semantics and necessity analysis, not the commitment. DePaul keeps recoverable copies, which a ceiling forbids (Rival 5).

**Example.** Record 100: under Rival 5 keys survive to month 19 and the ciphertext stays personal data, which the month-16 ceiling forbids.

**Point to.** §2.4 p. 25; §4.10 pp. 70 to 71; §7.2 p. 104. Slides 28, 19.

### 32. Propositions trivial, proofs informal, Semantics I a straw man.

**Say it.** "Yes, they are short, and I say so. Proposition 1 is a pigeonhole on one yes-or-no variable. The weight is in the analysis of what the law needs kept, and in the mechanism. And Semantics I is not invented: the reference gateway behaves that way."

**Exactly.** §4.7 p. 62: propositions, not theorems, "because their proofs are short once the semantics are fixed". No proof assistant; the checks guard against implementation error, not model error. Semantics I: the 2017 OpenNCP source stores each audit message whole, refuses to modify it, and has no purge logic; the 2026 schema (9.1.0) keeps the columns; other deployments not inspected (§4.5 p. 56). No instrument states either semantics.

**Example.** Exhaustive search finds no satisfying α for SPE with a 3-month permit and no request; the control case is feasible.

**Point to.** §4.5 pp. 55 to 56; §4.7 p. 62; §5.5 p. 85. Slides 8 (word), 24 (q-proofs).

**Follow-up.** "Why believe Proposition 1?" In month 116 one constraint needs α = 1, another α = 0.

### 33. Semantics II is your own definition. Why would a regulator accept it?

**Say it.** "No regulator has said so, and I will not pretend otherwise. I argue it from two points: the exemption protects only what is necessary, and minimisation says keep no more than the purpose needs. An audit record's purpose is who looked, when, why, not readable payload."

**Exactly.** Art 17(3)(b) covers necessary retention only; Art 5(1)(c); accountability needs who, when, basis, outcome (§4.2 p. 49). No regulator or court has held that an invalidated record satisfies a retention obligation (§6.2 p. 92). Why it may be accepted: the alternatives are worse (export moves data to a second controller); OPR-6 asks for a balance it does not define. Datatilsynet is asked. Do not say the EDPB endorses it.

**Example.** Record 100 after invalidation: who, when, which permit and the invalidation survive; the payload does not.

**Point to.** §4.2 pp. 49 to 51; §6.2 p. 92. Slide 22 (q-authority).

**Follow-up.** "A logistics student playing lawyer?" Both interpretive steps are flagged as interpretive, with a route to settle them.

### 34. Where is the logistics, and where is the energy?

**Say it.** "There is no optimisation and no energy saving, and I claim none. A record is information in storage with a planned exit. Customs keeps the record after the goods are destroyed; that is the move I make. Proposition 3 is a two-clock perishable-stock result."

**Exactly.** §2.7: CSCMP defines logistics as flow and storage of goods, services and related information. The per-record floor parameter comes from chain-of-custody practice (§4.3). Energy: none claimed (§1.5). Elhub keeps customer data three years and 41 days after contracts end; floor-against-right applies; whether a ceiling collides is the Proposition 3 test, not yet run, and the programme-native next step. The framing comes from my four years in cross-border procurement (§1.4).

**Example.** Record 3 is a consignment: made at one node, carried through a six-step gateway, held under rules set elsewhere.

**Point to.** §2.7 pp. 30 to 31; §1.4 p. 7; §1.5 p. 8; §6.9 p. 99. Slide 20 (q-logistics).

**Follow-up.** "What method?" Constraint modelling in the operations-research style and the two-clock reading.

### 35. Cost, adoption, is it real today?

**Say it.** "Not yet operative; the rules apply from 2029. Per-record keys are a real burden and I have not measured it. The cheapest step is logging every invalidation as a first-class event, which costs little."

**Exactly.** SecuPi (2025) is substantially correct (§6.4 p. 95). The burden falls on audit records, not clinical stores; the live key registry shrinks as invalidations accumulate. No performance figure is claimed (§6.5 p. 96). Three bodies could act (§6.8): the Commission, Health Data Access Bodies, TEHDAS2. **Since submission:** Helsedirektoratet's privacy notice (revised 30 June 2026) states six years for accessor fields: the same fields the mechanism keeps for the floor.

**Example.** Access control is no answer to a deletion ceiling: the data remain, protected by policy.

**Point to.** §6.4 to §6.5 pp. 95 to 96; §6.8 p. 98. Slides 15, 31 (q-adoption). App: ?p=norway

### 36. What would you do differently?

**Say it.** "I would ask the authorities earlier, because no modelling replaces their answers. I would run the expert panel. And I would build what I only specified, starting with published roots so the log cannot be quietly rewritten."

**Exactly.** Authority questions (§7.4); Appendix C panel (§7.5). Reported-run salts are derived, not random. Real permit durations; the Proposition 3 test on Elhub. Process lesson: an earlier draft, discarded in May 2026, cited works that do not exist (p. xi); every citation now is checked.

**Example.** The record-100 commitment in the reported run is not hiding; `--random-salts` fixes it.

**Point to.** §7.4 p. 106; §7.5 p. 107; §5.2 p. 80; Declaration p. xi.

### 37. How did you use AI, and can you explain the code?

**Say it.** "Claude was my research and drafting assistant and wrote the Python code, Archify made the diagrams, Parallel AI helped with research. All design decisions, the model, the legal arguments and every accept-or-reject choice are mine, and I am answerable for the whole. I can walk you through each function."

**Exactly.** Declaration p. xi: Claude for literature search and verification, critique, drafting to my direction, and the Appendix A code; Archify for figures; Parallel AI for retrieval. The thesis text (p. xi) names Claude, Archify and Parallel AI; your submission-form declaration also lists K-Dense skill instructions run inside Claude. If asked, say both, and that every modelling and legal decision is yours. Plain-English walks (trf_checker.py):
- `alpha` (line 296): readable before the earliest deadline, not after.
- `apply_invalidation` (line 270): log the access; delete key, salt, payload; write ι with month, ground ("Art 17(1)" wins a tie) and DPO; remove the subject link for SPE records only.
- `V_II` (line 305): checks the log proof, the commitment, and an entry for every loss of payload and link.
- `MerkleLog.proof` (line 104): collects sibling hashes up the tree; `verify` rehashes and compares to the root.

**Example.** `python3 trf_checker.py` prints 95 violations across 90 records, then 0.

**Point to.** Declaration p. xi; A.10 pp. 124 to 129 (MerkleLog p. 125, `apply_invalidation` p. 128, `V_II` p. 129). App: ?p=run

## Group 13. The whole thesis

### 38. Sixty-second version.

"A patient from Molde is treated in Helsinki, and the clinician's lookup is written to an audit log. Three European rules touch that log. One says keep it: six years in Norway's pilot. One lets the patient demand erasure. In research environments a third says health data must be gone six months after the permit ends. If 'verifiable' means 'readable', these cannot all hold: whenever a deletion deadline falls inside the keep period, the payload must be readable and gone in the same month. If 'verifiable' means 'accountable', so we can still show who looked, when, and that the payload was lawfully invalidated, they all hold, for any record and any timing. The mechanism: destroy the payload at the earliest deadline, keep the accountability, log the deletion. I check it on 200 generated records, with an exhaustive search and a solver. I do not claim key destruction is proven, the legal reading is settled, or the counts are real frequencies. Two questions need an authority; I have asked the first."

### 39. Twenty-second version.

"Three European rules collide on one audit record: keep it, erase it, delete it from the research environment. They collide only if 'verifiable' means 'readable'. If it means 'accountable', all three hold. Delete the payload. Keep the accountability. Log the deletion."

---

## Before you walk in

- App links above give only the query part; prefix https://trfhimolde.streamlit.app/. Wake the app ten minutes ahead; fallback is a ledger screenshot and Figure 5.2 (p. 85).
- Saved deck copies predate four changes: model slide floor now "ten years illustrative (the Norwegian pilot sets six)"; limits and forward slides name Helsedirektoratet's 19 Oct answer and Datatilsynet's 23 Sep enquiry; q-adoption privacy notice is "since submission".
- Slide 12's counters animate from zero when presented live; in a PDF export they read 0. If the animation does not run, say 90 / 200 and 39 / 78.
- One open [CHECK]: the Lovdata text of politiregisterloven §17 (Q13); bring it or avoid the detail.
