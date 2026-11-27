---
title: "Viva book: Verifiable Crypto-Erasure under the EHDS"
subtitle: ""
author: "Arshad Akhtar Abbasia · MSc defence, Molde University College · prepared 28 November 2026"
---

**How to use this book.** Part A is the 15-minute talk, slide by slide, with the script, the point each slide must land and the likely interruptions. Part B teaches the thesis in depth: the record, every symbol, each constraint, each proposition with its full proof, the mechanism, the method and the competitors. Part C is the question bank: a short answer to say first, the full reasoning behind it, what to concede and what to hold, and where to point in the thesis, deck and app. Items marked **[CHECK: ...]** need you to confirm a fact before the defence.

Reference conventions: thesis pages are the printed page numbers of the submitted PDF; "slide n" is the deck position; app links start at https://trfhimolde.streamlit.app/ (backup: trf-thesis-himolde.streamlit.app).

\newpage

# Part A. The talk, slide by slide

Candidate: Arshad Akhtar Abbasia. Talk: 15 minutes, slides 1 to 16. Slide 17 is the break into questions; slides 18 to 31 are backup. Questions: 30 minutes, Prof. João Ferreira and Joel Curado.

**Conventions.**
- The script is the speaker notes from the deck files, word for word. A change for a factual slip is marked [corrected: was X]. Every note ends in a "Concordance:" line, which is not spoken and is omitted here; each card's Links line carries the same references with printed page numbers.
- Thesis pages are printed pages of the submitted PDF (PDF page minus 14). Deck footers link to one page, which can differ from the section's first page; section pages are given here.
- "Q25" means Part C, question 25. "Part B, section Bx" means a section of B_explainer.md.
- App links start from https://trfhimolde.streamlit.app/ . Deep links are read once per session: use a fresh tab for each.
- Say "in the model" and "generated" whenever a count leaves your mouth.

---

### Slide 1. Cover · 0:00 to 0:20 (20 s)

**On screen:** Title, motto, app URL, Zenodo DOI; cover says "December 2026" [CHECK: confirm the defence date, window 3 to 14 December 2026].

**Script.**
> Good morning. My thesis is about one audit record that the law asks us to keep and to delete at the same time. In fifteen minutes you will see why those demands need not fight.

**Must land:** One record, two opposite demands, and a promise that they can be reconciled.

**If interrupted:**
- "What does "verifiable" in the title qualify?" The invalidation record, not the erasure. Q25.
- "Why VERA-SNARK?" Name from NORS 2025; no SNARK in the mechanism. Q43.

**Bridge:** "Let me make that promise concrete."

**Links:** Abstract pp. i to ii; Statement of Contribution pp. ix to x. App ?p=start.

---

### Slide 2. Promise · 0:20 to 1:05 (45 s)

**On screen:** Five-step ribbon; three outcomes.

**Script.**
> Here is my promise. In fifteen minutes you will be able to say why three European rules collide on one record, name the one assumption that causes it, and check the resolution yourself. The talk rests on one sentence, and you will hear it three times: the impossibility follows from an assumption about one word, not from the obligations. I assume no legal or cryptographic background. Every number I show can be rerun in the app or from the repository, with the same seed, so you can check me rather than trust me.

**Must land:** The one sentence, and that every number is checkable.

**If interrupted:**
- "Which assumption?" That "verifiable" means "readable". Q15.
- "Can I rerun it?" Yes: python3 trf_checker.py prints 95 violations across 90 records, then 0. Q33.

**Bridge:** "Start with one event."

**Links:** Abstract p. i; §7.6 p. 108. App ?p=start.

---

### Slide 3. Record · 1:05 to 1:55 (50 s)

**On screen:** Patient, clinician HP-003, two contact points, record 3 (gold accountability fields, rose personal fields).

**Script.**
> So what is the problem, concretely? Take one event. A patient from Molde falls ill while working in Helsinki. A clinician there asks for the patient summary. The request passes through the Finnish contact point, and the Norwegian contact point answers it and writes one line in its audit log. That line is the whole subject of this talk. It is not the health record. It is the record of who looked, when, and why. The gold lines say who acted and when; the rose lines are personal content. This is record 3 of the run, and you will see it again, live, in the app.

**Must land:** The object is the audit line, not the health record. (Molde and Helsinki are the deck's illustration; the thesis does not name the cities.)

**If interrupted:**
- "Why is a log line personal data?" It names the clinician, links the patient and carries the demographic query. Q7, Q12.
- "Whose log is it?" The Norwegian NCPeH repository: Helsedirektoratet and Norsk Helsenett. Q38.

**Bridge:** "Now put the rules on the clock."

**Links:** §1.1 p. 1; §2.2 p. 15; Figure 1.1 p. 5. App ?p=witness&r=3&m=11.

---

### Slide 4. Strip · 1:55 to 2:55 (60 s)

**On screen:** Record 3 timeline: floor to 131, deadline 116, red collision stretch.

**Script.**
> Now put the three rules on the clock. This is record 3 as the app draws it. The amber row is the retention floor: the record must stay verifiable until month 131. The violet row is the erasure right. A request arrives in month 115 and the controller has one month, so from month 116 the payload must be gone. If verifiable means readable, then in months 116 to 131 the payload must be readable and gone at once. The red stretch is the collision. One honest note: the run uses an illustrative ten-year floor, and the Norwegian pilot sets six years. Under six years this request would arrive after the floor ends, so what matters is whether a deadline falls inside the window.

**Must land:** The collision is a stretch of months, and exists only if a deadline falls inside the window.

**If interrupted:**
- "Is ten years real?" No, illustrative; Helsedirektoratet says no specification fixes it, pilot six. Q35.
- "Would 17(3)(b) refuse the request?" Only if the payload is necessary; §4.2 argues it is not. Q8.

**Bridge:** "That was a request. The third rule needs none."

**Links:** §4.4 p. 54; §5.3 p. 83; Corollary 1.1 p. 57. App ?p=witness&r=3&m=116.

---

### Slide 5. Research · 2:55 to 3:50 (55 s)

**On screen:** Record 100 timeline (months 7, 10, 16, 19); banner "broad reading of Art 68(12)".

**Script.**
> There is a third rule, and it needs no request at all. A researcher works inside a Secure Processing Environment under a data permit, and every access is logged. The permit expires in month 10, so six months later, in month 16, the data must be deleted from the environment. But the log must stay verifiable to month 19. Months 16 to 19 collide, and nobody asked for erasure. This holds on the broad reading of the ceiling, the one where research logs count as data in the environment, and I will come back to who decides that. The implementing acts are due in March 2027; the rules apply from March 2029.

**Must land:** Two articles of one regulation can collide with no data subject acting, on one stated reading.

**If interrupted:**
- "Does Art 68(12) reach logs?" Contestable; narrow reading drops only Corollary 1.2 and one branch of 2.3. Q9.
- "Are 1 to 12 month permits real?" An assumption; longer permits change how many, not whether. Q31.

**Bridge:** "You may already have a quick fix in mind."

**Links:** §4.6 pp. 57 to 59; §5.4 p. 84; Figure 5.2 p. 85; §6.8 p. 98. App ?p=witness&r=100&m=16.

---

### Slide 6. Fixes · 3:50 to 4:45 (55 s)

**On screen:** Four near-miss fixes; the necessity point; the append-only wall.

**Script.**
> You may already have a quick fix in mind. Good. These four are what a practitioner tries first, and each is a near miss: it meets one rule by breaking another. One deserves a sentence. Moving the log meets the ceiling, but not the erasure right, provided the controller that receives the log receives the erasure duty with it. That premise is legal, and I state it as one: Proposition 4. The gold line is the wall every append-only system meets, a blockchain included, and I will come back to it. The panel shows the way out: the law exempts retention only as far as necessary. So what does the floor actually protect? That question is the model.

**Must land:** No obvious fix works; the exit is the necessity boundary of Art 17(3)(b).

**If interrupted:**
- "Why not a blockchain?" It is where erasure fails; the Merkle log takes only tamper evidence. Q24.
- "Just export the logs." Meets the ceiling, not the right, on a stated premise. Q19.

**Bridge:** "To answer that, I need a model, and it needs one variable."

**Links:** §1.2 p. 3; §2.3 p. 17; §2.4 p. 21; §4.2 p. 49; §4.10 pp. 70 to 72. App ?p=built.

---

### Slide 7. Model · 4:45 to 5:40 (55 s)

**On screen:** alpha(a,t); C1 on V, C2 and C3 on alpha; floors 10 years illustrative, 6 in the pilot, 12 months for research logs.

**Script.**
> That is the problem. Now the model, and it takes one variable. For each record a and month t, alpha says whether the payload can be read. Each rule becomes a constraint, in the colours you have seen. The floor, C1, keeps the record verifiable through its window. Erasure, C2, and the ceiling, C3, force alpha to zero from their deadlines; the ceiling only for the research logs it reaches, on the broad reading. Now look at what each is written on. C1 speaks about V, verifiability. C2 and C3 speak about alpha, readability. Whether a record can comply depends on how V and alpha relate, and the law does not say.

**Must land:** C1 is written on V; C2 and C3 on alpha; how they relate is open.

**If interrupted:**
- "One binary variable is too crude." Deliberate; eighth limitation; Corollary 2.3 refines it. Q14.
- "Why months?" Instruments speak in months; the closed window is conservative. Q14.

**Bridge:** "So everything turns on one word."

**Links:** §4.3 p. 51; §4.4 p. 54. App ?p=start.

---

### Slide 8. Word · 5:40 to 6:30 (50 s)

**On screen:** Reading I: V = alpha. Reading II: accessor fields intact, commitment, losses logged.

**Script.**
> So everything turns on one word. The floor asks for logs kept to verify and audit, and the law never defines what verifiable must mean [corrected: was "The law says verifiable and never defines it"; Art 73(1)(e) says "identifiable logs ... to verify and audit", and "verifiable" is the thesis's term, as the slide title uses it], which leaves two readings, and I treat both as candidates. Reading I: verifiable means readable. No statute says it, but the reference implementation of the gateway behaves this way. Reading II: verifiable means accountable. Who acted and when stays intact, a binding commitment to the payload survives, and every loss of readability is itself logged. The practical difference is what an erased payload is. Under Reading I it is a broken record. Under Reading II it is the record of a lawful erasure. The next slide puts both readings on the same record.

**Must land:** Two candidate readings; an erased payload is a broken record or a record of lawful erasure.

**If interrupted:**
- "Semantics I is a straw man." It is the reference gateway's behaviour (2017 source; 9.1.0 schema keeps the columns). Q15.
- "Who accepts Semantics II?" No authority yet; argued, and put to Datatilsynet. Q10.

**Bridge:** "Put both readings on record 3."

**Links:** §4.5 pp. 55 to 56; §4.2 p. 49. App ?p=start.

---

### Slide 9. Result · 6:30 to 7:40 (70 s)

**On screen:** Record 3 sweep; Propositions 1 and 2; invalidation entry at month 116.

**Script.**
> This is the core result, so I will slow down. [pause] Record 3 again; watch the sweep. Under Reading I the third row turns crimson in month 116: the erasure deadline arrives while the floor still runs, and one binary variable cannot be one and zero in the same month. That is Proposition 1, deliberately elementary. Its consequence is not: under that reading, no schedule satisfies the three constraints for any record [corrected: was "no schedule is lawful"; the claim is about the model, not lawfulness] whose deadline falls inside its window. [pause] Under Reading II the payload row ends in month 116, the record row stays teal to month 131, and the line under the axis is the log entry. Proposition 2: in the model, every record, request pattern and floor has a solution, and its proof is the build sheet for the mechanism. Propositions 3 and 4 are in the backup. So: the impossibility follows from an assumption about one word, not from the obligations.

**Must land:** The sentence, second time. Proposition 1 is a pigeonhole; Proposition 2 is a witness that is also the design.

**If interrupted:**
- "This is trivial." Agreed and stated (§4.7); the weight is the necessity analysis and the mechanism. Q15.
- "You defined Semantics II to make it work." Conceded; the claim is that it is a defensible reading. Q17.

**Bridge:** "The proof is also the build sheet. Here is what it builds."

**Links:** §4.6 p. 57; §4.7 pp. 60 to 61; §5.3 p. 83; §5.7 p. 87. App ?p=propositions.

---

### Slide 10. Mechanism · 7:40 to 8:50 (70 s)

**On screen:** The data path and three triggers.

**Script.**
> That was the model. Now the mechanism the proof builds. Follow the green line. The audit writer splits the record into accessor fields and subject fields. The payload is encrypted under its own key, and a salted commitment binds it without revealing it. The accessor fields and the commitment go into a Merkle log, the construction behind Certificate Transparency. Then the violet lines: an erasure request, a permit ending or a payload period the controller sets, whichever comes first, fixes the invalidation month. The crimson lines: the key is destroyed, and the ciphertext and salt are deleted. The key matters for copies, such as backups, that cannot be deleted at once. Finally an invalidation entry goes to the registry and the log. The gold line is the answer to the append-only wall: the log never holds what erasure reaches, so the log never needs rewriting [corrected: was "so nothing on it ever needs erasing"; accessor fields leave at the terminal transition, and thesis §4.8 says "never needs rewriting"].

**Must land:** The payload goes, the accountability stays, the deletion is logged.

**If interrupted:**
- "Can the operator rewrite the log?" Alteration is caught; a wholesale rewrite needs published roots, not built. Q23.
- "Why keys at all?" The model cannot tell key destruction from deletion; keys serve backups and replicas. Q26.

**Bridge:** "Now stand where the auditor stands, afterwards."

**Links:** §4.8 pp. 63 to 67; Figure 4.1 p. 64; §4.9 p. 68. App ?p=built.

---

### Slide 11. Audit · 8:50 to 9:45 (55 s)

**On screen:** Printout for record 100 after invalidation; four ticks, one warning.

**Script.**
> Now the auditor who arrives after the fact. The dark panel is what the run prints for research log record 100 after invalidation. The first three checks hold as written. The fourth needs care: each inclusion proof checks against the root, so no entry has been altered. Catching a rewrite of the whole log needs the roots published outside it, with consistency proofs between them. That is specified, not built, and it is the open edge of this design. The fifth thing cannot be checked at all: that the key is really gone. That rests on attestation. So verifiable means the record of the erasure, not the erasure itself.

**Must land:** What "verifiable" means in the title, and the honest edge.

**If interrupted:**
- "You cannot prove key destruction." Correct; simulated in program memory. Q25.
- "Is the residue anonymous?" No: pseudonymised. Q11.

**Bridge:** "Does it hold beyond two records?"

**Links:** §1.4 p. 7; §4.8; §4.9 pp. 68 to 70; §5.7 pp. 87 to 88; Table 4.1 p. 74. App ?p=witness&r=100&m=16.

---

### Slide 12. Evidence · 9:45 to 10:50 (65 s)

**On screen:** 200 dots; counters animate to 90 / 200, 39 / 78, 0 / 200 [Counters animate live; in a PDF export they read 0. If the animation fails, say the figures.].

**Script.**
> That is the mechanism. Now the evidence. Record 3 and record 100 are two dots among two hundred: a hundred cross-border records with the illustrative ten-year floor, a hundred research logs with the one-year floor. Read as readable, ninety records violate, ninety-five violations in all, because five research logs hit both deadlines. Thirty-nine research logs with no request still collide, on the broad reading. Read as accountable: 138 invalidations and zero violations. These counts follow the generator; they are not how often this happens in Norway. A checker can be wrong, so three separate checks do not trust it: an exhaustive search, a bounded Z3 check, and synthetic FHIR payloads from Synthea that change every commitment and no figure. The limit, plainly: this shows the code implements the model. It is not independent evidence for the propositions.

**Must land:** The counts are generator outputs; what is checked is structure, with the limit stated first.

**If interrupted:**
- "45 per cent is a generator artefact." Yes; the boundary and the zero are the findings. Q29.
- "Is the check independent?" No; separate code, same AI-assisted process. Q30.

**Bridge:** "Do not trust me; let me recompute it in front of you."

**Links:** §5.3 p. 83; §5.4 p. 84; §5.5 pp. 85 to 86; §5.7 p. 87; §5.8 p. 89. App ?p=ledger.

---

### Slide 13. Demo · 10:50 to 12:05 (75 s)

**On screen:** "Live: record 3 and every figure, recomputed in front of you"; the seven-page walk; two stops, Witness a record and Claim ledger.

**Script, as in the notes (stage direction, not speech, except the quoted sentences).**
> [PREP, not spoken: rehearse on the live URL the day before, screenshot the Claim ledger as fallback, wake the app ten minutes ahead because it sleeps when idle.] Let me show you, seventy-five seconds, two stops. Stop one, Witness a record: choose the preset for record 3 and slide to month 116. Say one sentence: under the first reading, the collision; under the second, the invalidation. Stop two, Claim ledger: let it recompute and point at 90, 95, 39, 138 and 0, each matching the thesis. If the Synthea row reads bundles not deployed, say that row needs the bundles and move on. If the network fails, show the ledger screenshot and Figure 5.2. Then back to the deck.

**Say aloud:** "Let me show you, seventy-five seconds, two stops." / "Under the first reading, the collision; under the second, the invalidation." / "Ninety, ninety-five, thirty-nine, a hundred and thirty-eight, zero. Each matches the thesis." / if the Synthea row fails, "That row needs the bundles."

**Steps and clicks (time split is mine).**
| Step | Where | Click | Say |
|---|---|---|---|
| 0 (5 s) | Deck, browser present mode | Click "Open in app" in a fresh tab: ?p=witness&r=3&m=116 | Opening line |
| 1 (30 s) | Sidebar, Witness a record | If the link did not set it: preset "Cross-border record with an erasure request, record 3", drag Month to 116. Show the crimson row (first reading), then the payload row ending and the entry (second) | Stop 1 sentence |
| 2 (30 s) | Sidebar, Claim ledger (or fresh tab ?p=ledger) | Wait for the recompute. Point at 90, 95, 39, 138, 0 in turn | Stop 2 sentence |
| 3 (10 s) | Deck | Switch tab, advance to slide 14 | Bridge |

**If the app does not load** (never wait more than 15 s at a step):
1. Asleep: it can take up to a minute. Keep talking over slide 13 ("the walk follows the thesis order") while it wakes.
2. Still down: switch to the pre-opened backup, https://trf-thesis-himolde.streamlit.app/ . Same code per the demo walkthrough. Use the sidebar by hand [CHECK: whether the ?p=, r= and m= deep links work on the backup URL].
3. Neither loads, last resort: the pre-taken Claim ledger screenshot, then Figure 5.2 (thesis p. 85, record 100 month by month). Say: "The network has failed me, so here is the recorded run."
4. Whatever happens: the Zenodo tab (doi.org/10.5281/zenodo.23989242) stays open; "python3 trf_checker.py prints these figures offline."

**If you are late:** over 45 s behind, do stop 2 only (saves about 35 s).

**Must land:** every figure can be recomputed by the audience.

**If interrupted:**
- "Which version is running?" The thesis cites release 1.3.0 and Appendix A counts it; the live app is a later release with byte-identical result modules [CHECK: the walkthrough says 1.3.2; the repository is now at 1.3.4]. Q33.
- "Show me a research log with no request." Preset "Research log, no erasure request (Corollary 1.2)", record 100, month 16. Q16.

**Bridge:** "That is what the model and the code say. Now what they do not say."

**Links:** §5.2 p. 79; Figure 5.2 p. 85; Table 5.7 p. 90; Appendix A.1 p. 116. App ?p=witness&r=3&m=116, then ?p=ledger. Zenodo release 1.3.0.

---

### Slide 14. Limits · 12:05 to 12:55 (50 s)

**On screen:** NOT CLAIMED list; two authority questions; status of the letters.

**Script.**
> That is the evidence. Now the forward look, and it starts with limits, stated before you ask. I will not read the left column; each line has its section in the footer. On the right are two questions no model can settle, because they are legal. The first decides whether Reading II holds in law. The second decides Corollary 1.2 and the conditional branch of Corollary 2.3, and nothing else. Both can be settled by asking, and asking already works: Helsedirektoratet answered my retention question on 19 October. No period in the eHDSI specifications, six years decided for the pilot, the production period its own decision as controller. Datatilsynet has had the first question since 23 September. The second, how Articles 68(12) and 73 meet, is still to put to the Directorate and the Ministry.

**Must land:** Two questions only an authority can settle, and that asking works. [CHECK: any Datatilsynet reply since submission.]

**If interrupted:**
- "If the authority says no?" Propositions 1, 3, 4 and the model stand; Proposition 2 stays true but inert. Q46.
- "Who have you asked?" Datatilsynet (GDPR) 23 Sep, no reply; Helsedirektoratet (floor only) answered 19 Oct. Q37.

**Bridge:** "So what could change, and who can change it?"

**Links:** §3.7 p. 44; §6.2 p. 92; §6.3 p. 94; §7.3, §7.4 p. 106; Appendix D pp. 168 to 169. App ?p=start.

---

### Slide 15. Forward · 12:55 to 13:50 (55 s)

**On screen:** "What could be"; three bodies; the letters.

**Script.**
> Picture the rules in force. A patient asks for erasure. Within a month her payload is gone, yet she can still learn who looked at her record, and an auditor can still check who deleted what, when, and on what ground. That is what could be. Section 6.8 names three bodies who can make it the default while the specifications are still being written. The Commission can write the reconciliation into the implementing acts. Health Data Access Bodies, Helsedataservice among them, can log every invalidation as a first-class event; that alone costs little. TEHDAS2 can read Table 4.1 as a proposal against its own requirements. None of this has been done yet. The Directorate has answered on retention, and Datatilsynet has the GDPR question.

**Must land:** The specifications are still open, and the cheapest step is the invalidation entry alone.

**If interrupted:**
- "Who pays for per-record keys?" A real burden, unmeasured; it falls on audit records. Q2.
- "Which law fixes the six years?" None identified; the controller's pilot decision. Q35.

**Bridge:** "To close."

**Links:** §6.8 p. 98; §4.8; §7.4 p. 106; Table 4.1 p. 74; Appendix D p. 168. App ?p=norway.

---

### Slide 16. Close · 13:50 to 14:40 (50 s)

**On screen:** Four contributions, the sentence, the motto; point at the links, do not click.

**Script.**
> To close, four contributions, each bounded. A formal model in which verifiability decides feasibility. Feasibility results: the impossibility and the possibility are proved informally and checked in code; relocation is a legal argument on a premise I state. A mechanism specification with its residue analysed. And an integration analysis against Norwegian infrastructure. Go back to the opening record. The patient’s payload is gone, as the right requires. Who looked, when, and the deletion itself remain on record, so the auditor can still do the job. The impossibility follows from an assumption about one word, not from the obligations. Delete the payload. Keep the accountability. Log the deletion.

**Must land:** The sentence a third time, and the motto.

**If interrupted:**
- "Where is the SNARK?" None. Q43.
- "Where is the logistics?" Information in storage with a planned exit; no optimisation claimed. Q39.

**Bridge:** "I am happy to take questions. (Leave slide 17 up; open backups by number.)"

**Links:** §7.2 p. 104; §7.6 p. 108; Appendix A.1 p. 116. Repository github.com/Astheno-sphere/TRF-thesis (branch joao-base).

---

### Slide 17. Backup index (questions)

On screen: the list of slides 18 to 31 in two columns. Notes: "Index for the thirty-minute defence. Jump by slide number in present mode. Slides 18, 19 and 29 cover the ledger, zero-knowledge and log-rewrite questions; 28 and 30 the rival designs; 31 adoption and cost. Every answer: concession first, then what survives, then the section number."

---

### Backup slides 18 to 31

Open a backup only when the question arrives. Every answer: the limit first, then what survives, then the section.

#### Slide 18. Why not a blockchain? (q-chain)
**Open when:** "Why not put this on a blockchain?" or immutable log versus erasure. Q24.
> Concede: an immutable ledger is exactly where erasure fails. Finck’s analyses set out that tension, and the systematic review of 114 papers puts the right to be forgotten first among the difficulties. Then: the design takes the one property a chain would add, tamper evidence, from a Merkle log with RFC 6962 hashing, the Certificate Transparency construction, with logarithmic inclusion proofs. The leaves hold accessor fields, the payload commitment, a salted subject commitment and invalidation entries, never the payload or subject fields, so the log never needs rewriting [corrected: was "so nothing on the log needs erasing"]. If asked about anchoring roots: consistency proofs need earlier roots published or countersigned (§4.9); the artefact implements inclusion proofs only, and where roots are published is a deployment choice the thesis does not make. Redactable blockchains and chameleon hashes give a key holder the power to rewrite, a trust assumption this design avoids. Norway has a clinical precedent: NewbornTime, a Hyperledger consent platform at Stavanger University Hospital (§2.4).

Links: §2.4 p. 21 (review p. 24); §4.8 p. 66; §4.9 p. 69. App ?p=built.

#### Slide 19. Where is the SNARK? (q-snark)
**Open when:** "VERA-SNARK, where is the SNARK?" or any zero-knowledge question. Q43.
> Concede: the mechanism contains no SNARK. The name is kept for continuity with the NORS 2025 presentation, and the thesis says so. Then: once the three regimes were formalised, a hiding commitment, an attributed invalidation entry and a tamper-evident log were enough. Dropping the heavier machinery is the design-science cycle doing its job. The problem that does need zero knowledge is in §7.5: when the patient exercises Article 17, an auditor should be able to confirm that every one of her records was invalidated, but listing them would reveal her cross-border care history. Proving completeness without revealing the set is a zero-knowledge problem and future work. Comparator if asked: Albalwy (2026) uses a Groth16 zk-SNARK so a patient, doctor or researcher can prove policy-compliant credentials for cross-institutional sharing within one jurisdiction; it does not address retention.

Links: Statement of Contribution p. x; §1.6 p. 9; §7.5 p. 107.

#### Slide 20. Where is the logistics? (q-logistics)
**Open when:** "This is a logistics degree" or "where is the energy". Q39, Q40.
> Concede: no optimisation, and no energy saving. Then: information is part of logistics flow and storage. A cross-border audit record is generated at one node, travels a six-step gateway protocol, comes to rest in a repository governed by one authority, and is bound by obligations from another jurisdiction. The borrowing is specific: customs law already keeps the record of goods after the goods are ordered destroyed, and separating the record from the thing recorded is the move of Chapter 4. Proposition 3 reads in the idiom of perishable inventory with two clocks (Nahmias, 1982). The energy sector schedules retention the same way: Elhub keeps customer data three years and 41 days after contracts end (§2.7). My four years in cross-border procurement across DACH, India and the UAE is where the framing comes from. Do not say logistics is broadly about flows; that sounds retrofitted.

Links: §1.4 p. 7; §1.5 p. 8; §2.7 pp. 30 to 31. App ?p=anchor.

#### Slide 21. Does Art 68(12) reach the logs? (q-reading)
**Open when:** "Are the researcher's access logs data within the environment?" Q9. If pressed, add the third, harmonising reading (§4.6 p. 59): the ceiling yields to the floor.
> Concede immediately: the reading is contestable, and the thesis says so where it is used. The provision sits in the data-permit article, and a narrower construction confines it to the dataset made available under the permit. The broad reading rests on the text: its scope is set by location rather than provenance; it does not say “the data made available under the data permit”. Its object is electronic health data, and an entry kept at patient-record granularity reveals cohort membership, which is data concerning health. Then the map: reject the broad reading and you lose Corollary 1.2 and the conditional branch of Corollary 2.3. Everything else stands, and the researcher’s log then collides only through an erasure request, as the patient’s does. Do not say the Commission will clarify it.

Links: §4.6 pp. 58 to 59; §4.4 p. 54; §3.7 p. 44; §7.4 p. 106. App ?p=witness&r=100&m=16.

#### Slide 22. Who endorses Semantics II? (q-authority)
**Open when:** "Your own definition; why would a regulator accept it?" Q10.
> Do not defend it as settled law. The EDPB Guidelines 02/2025, paragraph 51, say that once the key is deleted the data are unintelligible, at least until the algorithm is broken, and in the same paragraph that encrypted personal data are still personal data; paragraph 125 says an erasure request needs the data erased or rendered anonymous. So the Board describes what key deletion achieves without classifying it as erasure, which is why the mechanism deletes the payload from the store and relies on keys only for copies that cannot be deleted at once. The further condition that the controller document its threat model is Aikebaier’s interpretation, not the Board’s. Nothing says an invalidated record discharges a retention obligation: that is my argument from Article 17(3)(b), Article 5(1)(c) and the accountability purpose. Whether an authority accepts it is open, and I have put it to Datatilsynet. Do not say the EDPB endorses it.

Links: §4.2 p. 49; §4.9 pp. 68 to 70; §6.2 p. 92; §7.4 p. 106.

#### Slide 23. Are the permits realistic? (q-permits)
**Open when:** "Permits of one to twelve months?" or "45 per cent". Q31, Q29.
> Concede the empirical gap plainly. Then the substance: a longer permit moves the ceiling later, so fewer records like the researcher’s collide, but Proposition 1 is stated for records whose deadline falls inside the window and is silent on the others. The 90 of 200 is a property of the generated population, and Chapter 5 says so in the same paragraph. Corollary 1.2’s fifty per cent follows directly from the permit draw: the collision occurs when the permit expiry plus six is within the floor, the condition of Proposition 3(ii) with F = 12 and L = 6. Tripling the response period from one month to three moves 95 violations to 94. Do not say the range is representative.

Links: §3.7 p. 44; §5.3 p. 83; §5.4 p. 85; §5.6 p. 87. App ?p=robust.

#### Slide 24. Why believe informal proofs? (q-proofs)
**Open when:** "Your proofs are informal" or "break them". Q15, Q30.
> The proofs are informal in presentation and constructive in substance. Proposition 1: in the patient’s month 116 one constraint needs alpha equal to one and another needs zero, and no assignment satisfies both. Proposition 2 is proved by building the trajectory and checking the three constraints against it. You do not have to believe the prose. The brute-force function is written separately from the checker and shares only two constants; a test compares the two on 31 cases, including every boundary month of a twelve-month window. Z3 poses each proposition as a search for a counterexample, with floors up to 120 months, and finds none; it does find counterexamples to constructions without the invalidation entry or the commitment, and to an off-by-one Proposition 3. Do not say it was formalised in a proof assistant.

Links: §4.6 p. 57; §4.7 p. 60; §5.5 pp. 85 to 86; A.23 p. 150; A.24 p. 153. App ?p=propositions.

#### Slide 25. Can you prove key destruction? (q-keys)
**Open when:** "You cannot prove the key was destroyed" or "what does an HSM give you". Q25.
> Agree first; the thesis says so in several places. The optional envelope module does use real AES-256-GCM per-record keys, and exactly the invalidated records refuse to decrypt through custody, but the custody object stands in for a hardware security module, so destruction there is destruction in program memory. In the specification the store deletes the payload, its key and its salt; key destruction matters for copies such as backups, which become unreadable and leave by rotation. The trust assumptions are named in §4.9. Reardon and colleagues show that the further an approach operates from the storage medium, the harder it is to assert that destruction occurred; cryptographic erasure is the limiting case. Certified deletion protocols are where proof could come from, and their public verifiability is open.

Links: §4.8 p. 63; §4.9 p. 69; §6.3 p. 94; §7.5 p. 107; A.15 p. 142; A.22 p. 149. App ?p=robust.

#### Slide 26. Are the synthetic patients American? (q-synthea)
**Open when:** "Your synthetic data are American" or "realism". Q31.
> Agree: the generator is American by default, and the thesis does not imply otherwise. The data are genuine Synthea output, generated on Linux. Two points carry the answer. First, FHIR R4 is the version HL7 Norway’s basisprofiler constrain. Second, and decisive: the model never reads payload content; it reads when things happen and whether the payload can be read. Replacing the constructed payload strings with Synthea FHIR R4 resources changed all two hundred commitments and no reported figure, on the subset and on the full-cohort rerun in Appendix A.17. So the nationality of the synthetic patients cannot move any result.

Links: §3.5 pp. 41 to 42; §5.2 p. 79; Table 5.7 p. 90; A.17 p. 145. App ?p=synthea (needs the bundles; else docs/expected_synthea_full_cohort_rerun_2026-10-06.txt).

#### Slide 27. Is what remains anonymous? (q-residue)
**Open when:** "Is the residue anonymous?" or identifiability. Q11.
> Say no, plainly; §4.9 says any claim of anonymisation would be false. What survives identifies the accessor, the clinician, and is pseudonymised as to the patient. Datatilsynet’s guidance holds that data are not anonymous while any key or linkage capable of re-identification is retained, and the EDPB’s draft Guidelines 02/2026 on anonymisation, adopted for consultation in July 2026, set the same bar. Then: the applicable test is erasure, and the store meets it by deleting the payload, its key and its salt. The salted commitment stops anyone confirming a guessed payload. Only the terminal transition after the floor aims at a non-identifiable residue, and whether it resists isolation, linkage and inference is for the documented threat model. The artefact does not implement it.

Links: §4.8 p. 67; §4.9 pp. 68 to 69. App ?p=witness&r=100&m=19.

#### Slide 28. Why not delete and log it? (q-rival4)
**Open when:** "Delete the record and log that you deleted it. Why more?" Q28.
> Concede first. For cross-border records, where the patient link is kept through the floor and nobody is handed an opening, “delete the record and log the deletion” is close to an equivalent design. It fails C1 under Semantics II only because there is no commitment, which is true by definition. What the design adds is three things: the invalidation entry is attributed and grounded; it is bound tamper-evidently with the access record; and the commitment detects substitution of one record’s payload for another’s before invalidation, and afterwards wherever an opening was handed to the patient or the home contact point. In the Secure Processing Environment case it does work deletion cannot. The weight of the thesis lies in the semantics and the necessity analysis, not the commitment.

Links: §4.10 p. 71 (Rival 4); §4.5 p. 56; §4.8 p. 65. App ?p=witness&r=3&m=116.

#### Slide 29. Can the operator rewrite the log? (q-roots)
**Open when:** "The operator controls the Merkle log." Q23.
> Concede: on its own, nothing does, and the thesis says so. The artefact checks inclusion proofs against a root recomputed from the log’s own leaves. Three tamper tests show what that catches: an altered accessor field, an altered legal ground, an altered patient link, each makes the Semantics II check fail. It does not catch a wholesale rewrite. That needs consistency proofs between an earlier root and the current one, with earlier roots published or countersigned outside the operator’s control, as in Certificate Transparency. Those are specified, not implemented. The operator is named in the trust assumptions: alteration is detectable but not impossible. What does hold: once a root containing an invalidation entry is published, the claim cannot be withdrawn.

Links: §4.9 p. 69; §5.7 p. 88; Table 4.1 p. 74; §6.1 p. 91; §6.3 p. 94. App ?p=run.

#### Slide 30. Why not export the logs? (q-props34)
**Open when:** "Just export the logs at permit closure" or anything on Proposition 3 or 4. Q19, Q18.
> Concede the ceiling: the thesis accepts export as a sufficient answer to Corollary 1.2. It does not answer the erasure right. Proposition 4: the ceiling binds a location, the right binds whichever controller holds the data. On the stated legal premise that a receiving controller receives the Article 17 duty with the record, relocation leaves C1 against C2 exactly as before. It also moves the subject fields to a second controller rather than reducing them. Proposition 3 explains why the SPE collision is invisible in the text. The ceiling, six months from permit expiry, is anchored to a different event from the floor, twelve months from the entry, so only each record’s history shows the clash. Politiregisterloven section 17, a longer ceiling from the same event, produces none.

Links: §4.10 pp. 71 to 72; §4.6 p. 60; §6.10 p. 100. App ?p=anchor.

#### Slide 31. Is it real, and what does it cost? (q-adoption)
**Open when:** "Is this a real problem today, who would adopt it, what does it cost?" Q2. Privacy-notice follow-up: Q36.
> Concede: not yet operative. Articles 68 and 73 apply from 26 March 2029, and Norway’s contact point is in live pilot with no relevant patient when the Directorate last reported. That timing is the argument: the implementing acts for Secure Processing Environments are due 26 March 2027, so the design can be specified before infrastructure hardens. On cost, SecuPi’s critique is correct on its own terms: per-record keys are a real burden. But it falls on audit records, not clinical stores; live keys shrink as invalidations accumulate; and an inclusion proof grows as log two of n, some thirty hashes for a billion entries. None of this is measured, and no performance claim is made. The cheapest adoption step is the invalidation entry alone, which section 6.8 says costs little. Not in the thesis [corrected: was "Since submission"; the notice is dated 30 June 2026, before submission, and the thesis does not cite it], one public anchor: the Directorate's privacy notice, revised 30 June 2026, states that the MyHealth@EU search-and-view log keeps the health professional's name, HPR number, role, institution type, place and time of lookup for six years, under GDPR Article 6(1)(c) and pasientjournalloven section 22, with the Directorate as controller and Norsk helsenett as processor. That is the accessor evidence my mechanism keeps; the patient payload is what it lets go.

Links: §6.4 p. 95; §6.5 p. 96; §6.8 p. 98; §2.2 p. 15; Appendix D p. 168. App ?p=norway.


---

### Timing

Words are counted from the notes (Concordance line and slide 13 PREP direction removed; corrections included). Seconds at 140 words a minute. Margin is window minus spoken time.

| Slide | Start | End | Window (s) | Words | Spoken (s) | Margin (s) |
|---|---|---|---|---|---|---|
| 1 Cover | 0:00 | 0:20 | 20 | 35 | 15 | +5 |
| 2 Promise | 0:20 | 1:05 | 45 | 93 | 40 | +5 |
| 3 Record | 1:05 | 1:55 | 50 | 106 | 45 | +5 |
| 4 Strip | 1:55 | 2:55 | 60 | 124 | 53 | +7 |
| 5 Research | 2:55 | 3:50 | 55 | 112 | 48 | +7 |
| 6 Fixes | 3:50 | 4:45 | 55 | 118 | 51 | +4 |
| 7 Model | 4:45 | 5:40 | 55 | 112 | 48 | +7 |
| 8 Word | 5:40 | 6:30 | 50 | 118 | 51 | -1 |
| 9 Result (two pauses, +4 s) | 6:30 | 7:40 | 70 | 153 | 70 | 0 |
| 10 Mechanism | 7:40 | 8:50 | 70 | 145 | 62 | +8 |
| 11 Audit | 8:50 | 9:45 | 55 | 109 | 47 | +8 |
| 12 Evidence | 9:45 | 10:50 | 65 | 137 | 59 | +6 |
| 13 Demo | 10:50 | 12:05 | 75 | 91 (stage direction) | about 40 spoken | clicks fill the rest |
| 14 Limits | 12:05 | 12:55 | 50 | 135 | 58 | -8 |
| 15 Forward | 12:55 | 13:50 | 55 | 124 | 53 | +2 |
| 16 Close | 13:50 | 14:40 | 50 | 107 | 46 | +4 |
| **Total** | 0:00 | **14:40** | **880** | 1,819 | | |

**Check against 15:00.** The windows end at 14:40: under 15:00, 20 s spare. A slide that overruns cannot borrow from the next, so the realistic finish is the sum of the larger of window and spoken time: about 14:49 at 140 words a minute, about 15:02 at 130 (slides 8, 9, 14, 15 overrun), which is over. Rehearse once with a stopwatch; if you finish after 14:50, use the cut list.

**Cut list, in order (exact sentences, seconds saved).**
1. Slide 14: "I will not read the left column; each line has its section in the footer." About 6 s.
2. Slide 15: "None of this has been done yet. The Directorate has answered on retention, and Datatilsynet has the GDPR question." About 8 s; slide 14 said it.
3. Slide 5: "The implementing acts are due in March 2027; the rules apply from March 2029." About 6 s; the slide shows both dates.
4. Slide 7: "Each rule becomes a constraint, in the colours you have seen." About 5 s.
5. Slide 10: "Follow the green line." About 2 s.
6. Slide 13: skip stop 1, ledger only. About 35 s.

Cuts 1 to 3 (about 20 s) bring the 130 wpm case to about 14:42; cut 6 is the emergency brake. Never cut the "in the model" and "generated" qualifiers (slides 9, 12), the ten-year note (slide 4) or the limit sentence (slide 12).


\newpage

# Part B. The thesis in depth

Read in order: each chapter defines its symbols before using them. Worked examples use the values `trf_checker.py` produces under seed 20260915; records the thesis does not name (38, 97, 102, 132, 133) are marked "from the checker". Pages are printed pages (body = PDF page minus 14). "Slide n (id)" is the deck position and file. The `r` and `m` link parameters act only on the `witness` page. Semantics I and II in the thesis are Reading I and II on the slides.

## B1. The problem in one record

### B1.1 Record 3: a cross-border audit record, month by month

**The event.** A Norwegian patient falls ill abroad; a clinician there requests her patient summary through the local National Contact Point for eHealth (NCPeH); the Norwegian NCPeH answers and writes one audit record. That record, not the health record, is the subject (§1.2, p. 3).

**What is created.** Record 3 in the generated run: created in month $t(a) = 11$ under the illustrative floor $F = 120$; actor `HP-003` via contact point `FI`; patient pseudonym `PSN-0003`; payload `<ITI-55 QBP name=N003 birthTime=1943 rid=3>`, standing for the demographic query that the IHE patient-discovery transaction (ITI-55) requires both gateways to record (§4.3, p. 52); commitment beginning `358f2a6ab39376d7`. An erasure request arrives in month $t_r = 115$. There is no permit: $t_\pi = \infty$.

| Month | What happens | What each rule demands |
|---|---|---|
| 11 | Access; record written to the audit repository | Floor starts: the record must be verifiable in every month from 11 to $11 + 120 = 131$ |
| 12 to 114 | Nothing new | Floor only. No conflict: the payload may stay readable |
| 115 | Patient asks for erasure under Art 17 GDPR | The controller has $\delta = 1$ month to act |
| 116 | Erasure deadline $t_r + \delta = 116$ | Erasure: payload unreadable from 116 onwards. Floor: record still verifiable |
| 116 to 131 | Both rules bind | If "verifiable" means "readable", the payload must be readable and unreadable in each of these 16 months ($131 - 116 + 1 = 16$) |
| 132 | Floor window has closed | No rule demands readability; the specified terminal transition would remove identifying metadata here (not implemented) |

**Where the demands collide.** The first collision month is 116. The checker prints this witness verbatim (§5.3, p. 83):

`C1 requires V=1 (=> alpha=1) at t=116 within [11,131]; C2 requires alpha=0 from t=116`

**The Norwegian value changes the timing, not the logic.** Under the pilot's six years ($F = 72$, Appendix D, p. 168) record 3's window is months 11 to 83, so its month-115 request falls outside and it does not collide. A request in any month 11 to 82 would (Corollary 1.1, B3.2).

Point to: §1.2, p. 3; §5.3, p. 83; slides 3 (record) and 4 (strip); <https://trfhimolde.streamlit.app/?p=witness&r=3&m=116>

### B1.2 Record 100: a research-environment log, month by month

**The event.** A researcher with a data permit works inside a Secure Processing Environment (SPE), which logs every access.

**What is created.** Record 100 in the generated run: created in month $t(a) = 7$ under $F = 12$ (Art 73(1)(e)); secondary pathway, reached by the ceiling ($\rho = 1$, which the generator sets for every SPE record to model the broad reading, §5.2, p. 80); actor `R-008` under permit `DP-015`; pseudonym `PSN-0000`; payload `<SPE-activity query=cohort-extract rid=100>`; commitment beginning `678ade47c1e6dc03`. The permit expires in month $t_\pi = 10$. No request ever arrives: $t_r = \infty$.

| Month | What happens | What each rule demands |
|---|---|---|
| 7 | Researcher's query logged | Floor: verifiable in every month 7 to $7 + 12 = 19$ |
| 8 to 9 | Nothing new | Floor only |
| 10 | Data permit expires | Ceiling clock starts: six months |
| 11 to 15 | Ceiling running | Floor only binds |
| 16 | Ceiling deadline $t_\pi + 6 = 16$ | Ceiling: electronic health data gone from the SPE from 16. Floor: identifiable log still verifiable |
| 16 to 19 | Both bind | Under "verifiable means readable": readable and gone in 4 months ($19 - 16 + 1 = 4$) |
| 20 | Floor window has closed | Nothing demands readability |

**Where the demands collide.** Months 16 to 19. The checker's witness (§5.4, p. 84):

`rid=100: t_a=7 permit expires t_pi=10 -> C3 from t=16, C1 to t=19 | collision at t=16`

**Why it is sharper than record 3.** Nobody asked for anything: two articles of one regulation collide in one environment. That is Corollary 1.2 (B3.3), on the broad reading of Art 68(12) only.

Point to: §5.4, p. 84; Figure 5.2, p. 85; slide 5 (research); <https://trfhimolde.streamlit.app/?p=witness&r=100&m=16>

### B1.3 Where each rule comes from

**The erasure right: Art 17 GDPR, with Art 12(3).** Article 17(1) GDPR gives the data subject the right to obtain erasure of personal data concerning her "without undue delay" where one of its grounds applies, and the controller has its own duty to erase on those grounds (§2.3, p. 18). Article 12(3) sets the response time: within one month of receipt, extendable by two further months for complex or numerous requests. The model writes this as $\delta = 1$, with $\delta = 3$ as the extended case (§4.4, p. 54). Of the Art 17(3) exemptions, (b) legal obligation, (c) public health and (d) research matter here. The model treats every request as valid, which inflates how often collisions occur in the run, not whether they can (§3.7, p. 45).

**The deletion ceiling: Art 68(12) EHDS.** Regulation (EU) 2025/327 provides that "the electronic health data within the secure processing environment shall be deleted within six months of the expiry of the data permit" (§4.4, p. 55; quoted at §2.3, p. 19). It is a ceiling: a latest date by which something must be gone. It has no exemption parallel to Art 17(3)(b) (§2.3, p. 20). It applies from 26 March 2029 (§6.8, p. 98).

**The SPE floor: Art 73(1)(e) EHDS.** The same Regulation requires of an SPE "the keeping of identifiable logs of access to and activities in the secure processing environment for the period necessary to verify and audit all processing operations in that environment; logs of access shall be kept for at least one year" (§2.3, p. 19). This gives $F = 12$. The Joint Action's specification recommends five years (OPR-18), and by Corollary 2.2 no result depends on the value (§4.3, p. 53).

**The cross-border floor: eHDSI and ATNA.** The IHE ATNA profile prescribes no retention period; the floor comes from the deployment binding (§2.3, p. 17). A tutorial article reports ten years as the eHDSI baseline but gives no source (Simjanoska Misheva et al., 2025). The contact-point agreement requires audit trails and states no period (eHealth Network, 2017, clause II.4.2), nor does Implementing Regulation (EU) 2026/2083 (§2.3, p. 18). Helsedirektoratet replied on 19 October 2026 that the specifications leave the period to national law and the pilot uses six years, production undecided (Appendix D, p. 168). From 26 March 2029, Art 9(2) EHDS gives three years where the audit record is what a patient's access information is produced from (§4.3, p. 53). So the floor is a parameter: 120 illustrative, 72 pilot, 36 under Art 9(2), 12 for SPE logs.

**Which reading is contested.** Two things are contested, and the thesis says so.

1. *Whether Art 68(12) reaches the SPE's own access logs.* Broad reading: scope is set by location ("within the secure processing environment"), and a patient-level entry reveals cohort membership, which is health data. Narrow reading: the provision sits in the data-permit article and concerns the permit dataset. Harmonising reading: it reaches the logs but yields to Art 73(1)(e) (§4.6, pp. 58 to 59). Only Corollary 1.2 and the conditional branch of Corollary 2.3 depend on this (§6.2, p. 93).
2. *Whether an invalidated record still satisfies a retention obligation.* No regulator or court has said so (§6.2, p. 92). This is the authority question behind Semantics II.

Point to: §2.3, pp. 17 to 20; §4.4, pp. 54 to 55; §4.6, pp. 58 to 59; Appendix D, p. 168; slides 14 (limits) and 21 (q-reading); <https://trfhimolde.streamlit.app/?p=start>

### B1.4 Why Article 17(3)(b) does not make the problem vanish

The first objection any lawyer raises: Art 17(3)(b) exempts processing "necessary for compliance with a legal obligation". Audit retention is a legal obligation. So erasure never reaches the audit record, and there is no conflict.

The thesis answers in three steps (§2.3, pp. 19 to 20; §4.2, p. 49).

1. *The exemption is bounded by necessity.* It protects only what the obligation needs. Article 5(1)(c) GDPR (data minimisation) still applies to whatever is kept.
2. *What does the obligation need?* Its purpose is accountability: that an access happened, by whom, when, under what authority, with what result. The accessor fields answer that. The patient's name and birth date as typed into the query do not add to the answer. So keeping the payload readable for the whole floor exceeds what Art 17(3)(b) protects. This is "a reading argued here from the primary instruments, not one a supervisory authority has yet confirmed" (§4.2, p. 49).
3. *The ceiling has no such exemption.* Article 68(12) binds whatever balance is struck for the floor.

So the conflict survives in a narrowed form: not "may the record be kept?" but "how much of it may stay readable, for how long?" (§2.3, p. 20).

The patient link differs. Art 9(1) to (2) EHDS lets patients see who accessed their data "for at least three years from each date of access", which needs the link; so keeping it is necessary for a legal obligation, once Art 9 applies and where it binds this controller (§4.2, p. 50). Hence cross-border records keep the link through the floor; SPE logs lose it at the ceiling.

Point to: §2.3, pp. 19 to 20; §4.2, pp. 49 to 50; slide 6 (fixes); <https://trfhimolde.streamlit.app/?p=start>

## B2. The TRF model, symbol by symbol

### B2.1 The symbol table

The model is "one record, one clock, and one main question asked every month. Can the payload still be read?" (§4.3, p. 51). Time is counted in whole months $t \in \mathbb{N}$, with $t = 0$ the month the system starts.

| Symbol | Plain meaning | Unit | Where it comes from | Record 3 | Record 100 |
|---|---|---|---|---|---|
| $m_{\mathrm{acc}}(a)$ | Accessor fields: who acted, when, under which basis or permit, outcome | fields | Accountability purpose (§4.2) | HP-003, FI, PatientSummary, Art9(2)(h), success | R-008, DP-015, SPE-AccessLog, DataPermit, success |
| $m_{\mathrm{subj}}(a)$ | Subject fields: the link to the patient | fields | Design partition (§4.3) | PSN-0003 | PSN-0000 |
| $p(a)$ | Payload: what the record carries about what was accessed | bytes | ITI-55 query (cross-border); logged activity (SPE) | ITI-55 query string | SPE-activity string |
| $c(a)$ | Hiding, binding commitment to the payload, $\mathrm{Commit}(p(a), r(a))$ | hash value | Design (§4.3, §4.9) | `358f2a6a...` | `678ade47...` |
| $r(a)$ | Per-record salt for the commitment | 16 bytes in the code | Design | derived from rid in the reported run | same |
| $k(a)$ | Payload key | key | Envelope encryption (§4.8) | `KEY-000003` (toy) | `KEY-000100` (toy) |
| $t(a)$ | Month of the access event | month | The event | 11 | 7 |
| $F(a)$ | Retention floor | months | National law or pilot decision; Art 73(1)(e) | 120 (illustrative; pilot 72) | 12 |
| $\sigma(a)$ | Pathway: primary or secondary use | label | Where the record arose | primary | secondary |
| $t_r(a)$ | Month an erasure request arrives; $\infty$ if none | month | Art 17 GDPR | 115 | $\infty$ |
| $\delta$ | Erasure response period | months | Art 12(3) GDPR | 1 | 1 |
| $t_\pi(a)$ | Month the data permit expires; $\infty$ for primary records | month | Data permit | $\infty$ | 10 |
| $\rho(a)$ | 1 if the ceiling reaches the record (its entry is itself electronic health data in the SPE) | 0 or 1 | Reading of Art 68(12) | not defined (primary) | 1 (broad reading) |
| $P(a)$ | Payload retention period the controller may set; $\infty$ if none | months | Art 5(1)(c) and (e) GDPR | $\infty$ (artefact) | $\infty$ (artefact) |
| $t^{I}(a)$ | Invalidation month, $\min(t_r + \delta,\ t_\pi + 6,\ t + P)$ | month | Proof of Proposition 2 | 116 | 16 |
| $\alpha(a,t)$ | 1 if the controller can read the payload in month $t$ | 0 or 1 | The model's state variable | 1 up to 115, 0 from 116 (Sem. II run) | 1 up to 15, 0 from 16 |
| $\beta(a,t)$ | 1 if the subject fields can be read in the SPE in month $t$ | 0 or 1 | Broad reading only | unconstrained, stays 1 through floor | 1 up to 15, 0 from 16 |
| $V(a,t)$ | Whether the record counts as verifiable in month $t$ | 0 or 1 | Defined by the semantics | must be 1 for months 11 to 131 | must be 1 for months 7 to 19 |
| $\iota(a)$ | Invalidation entry: record, month, legal ground, authorising actor, hash of key identifier | log entry | Design (§4.8) | month 116, GDPR Art 17(1), DPO | month 16, EHDS Art 68(12), DPO |
| $e(a)$, $L$ | Anchor month of a ceiling, and its length (Proposition 3) | months | Any ceiling | not applicable | $e = 10$, $L = 6$ |
| $p_n(a)$, $p_r(a)$ | Part of the payload auditing needs; the rest (Corollary 2.3) | bytes | Extension of the model | $p_n$ empty in the run | $p_n$ empty in the run |

Notes on the table.

- The record is the tuple $a = (m(a), p(a), c(a), k(a), t(a), F(a), \sigma(a))$, with metadata $m(a) = m_{\mathrm{acc}}(a) \cup m_{\mathrm{subj}}(a)$ and no clinical content (§4.3, p. 51).
- Arithmetic is over $\mathbb{N} \cup \{\infty\}$ with $\infty + n = \infty$. A request concerns data already recorded, so $t_r(a) \ge t(a)$, and $\delta \ge 1$ (§4.3, p. 53).
- The floor is a parameter of the record, a form taken from chain-of-custody practice in logistics (§4.3, p. 52; §2.7, p. 31).
- In the checker the key is a reference that is removed; `crypto_envelope.py` uses real AES-256-GCM keys (§5.2, p. 80).

Point to: §4.3, pp. 51 to 53; Nomenclature, p. xii; slide 7 (model); <https://trfhimolde.streamlit.app/?p=start>

### B2.2 C1, the retention floor

**The rule in English.** For as long as the retention period runs, the record must count as verifiable.

**The formula.**
$$
V(a,t) = 1 \qquad \forall\, t \in \big[\, t(a),\; t(a) + F(a) \,\big]
$$

**Why the window is closed, so it spans $F + 1$ months.** The obligations are minimums: "at least one year". A record written during month $t(a)$ has completed $F$ full months only during month $t(a) + F$. So the conservative reading of "at least" demands verifiability through that month too. The window $[t(a), t(a)+F(a)]$ contains the integers $t(a), t(a)+1, \dots, t(a)+F(a)$: that is $F + 1$ of them. A half-open window $[t(a), t(a)+F(a))$ would end one month earlier and "would shorten every obligation by up to a month" (§4.4, p. 54).

*Worked example where it matters (record 97, from the checker, not named in the thesis).* Record 97 is cross-border: $t(a) = 7$, $F = 120$, so the closed window is months 7 to 127. Its request arrives in month 126, so with $\delta = 1$ the deadline is $126 + 1 = 127$: the last month of the window. On the closed window, month 127 needs both readable and gone: a collision. On a half-open window ending at 126 there would be none. With $\delta = 3$ the deadline moves to 129, which is outside 127, so the collision disappears. Record 97 is exactly the one record that leaves violation in Table 5.5 (90 to 89 generated records, 95 to 94 violations; §5.6, p. 87).

**C1 is a lower bound on $V$.** It says $V$ may not drop to 0 before the window ends. It sets a minimum duration for a property. It says nothing about $\alpha$ directly.

Point to: §4.4, p. 54; Table 5.5, p. 87; slide 7 (model); <https://trfhimolde.streamlit.app/?p=witness&r=3&m=116>

### B2.3 C2, the erasure right

**The rule in English.** After a valid erasure request, the payload must stop being readable within the response period, and stay unreadable.

**The formula.** For every record with $t_r(a) < \infty$:
$$
\alpha(a,t) = 0 \qquad \forall\, t \ge t_r(a) + \delta
$$

**Reading it.** The deadline month is $t_r + \delta$. From the start of that month onwards, $\alpha$ must be 0. If $t_r = \infty$, the condition "for every $t \ge \infty$" covers no month: C2 is vacuous.

**C2 is an upper bound on $\alpha$.** It caps how long the payload may remain readable. It says nothing about $V$.

*Record 3.* $t_r + \delta = 115 + 1 = 116$, so $\alpha(3,t) = 0$ for every $t \ge 116$.

Point to: §4.4, p. 54; slide 7 (model); <https://trfhimolde.streamlit.app/?p=witness&r=3&m=116>

### B2.4 C3, the deletion ceiling, with $\rho$ and $\beta$

**The rule in English.** In a research environment, health data must be gone six months after the permit ends. On the broad reading, this reaches log entries that are themselves health data.

**The switch $\rho$.** $\rho(a) = 1$ where the log entry is itself electronic health data within the environment. Broad reading: $\rho = 1$ for entries at patient-record granularity, and for dataset-granularity entries only where their activity content is health data. Narrow reading: $\rho = 0$ for every access log (§4.4, p. 55).

**The formula.** For every record with $\sigma(a) = \text{secondary}$ and $\rho(a) = 1$:
$$
\alpha(a,t) = 0 \qquad \forall\, t \ge t_\pi(a) + 6
$$
and, where the subject fields are electronic health data within the environment,
$$
\beta(a,t) = 0 \qquad \forall\, t \ge t_\pi(a) + 6 .
$$

**Why $\beta$ exists.** The single variable $\alpha$ covers the payload. On the broad reading the ceiling also reaches the patient link in an SPE log. So the model needs one more yes-or-no: can the subject fields still be read? Where the broad reading does not apply, $\beta$ is unconstrained and plays no part in any result (§4.3, p. 53).

**C3 is an upper bound on $\alpha$** (and on $\beta$).

*Record 100.* $t_\pi + 6 = 10 + 6 = 16$, so $\alpha(100,t) = 0$ and $\beta(100,t) = 0$ for every $t \ge 16$.

Point to: §4.4, p. 55; §4.3, p. 53; slides 7 (model) and 21 (q-reading); <https://trfhimolde.streamlit.app/?p=witness&r=100&m=16>

### B2.5 Lower bound on V, upper bound on alpha, and why "tri-lateral"

The thesis states the whole problem in one sentence: "C1 is a lower bound on the persistence of a property; C2 and C3 are upper bounds on the persistence of accessibility. Whether they conflict depends entirely on whether $V$ is defined in terms of $\alpha$" (§4.4, p. 55).

C1 says $V = 1$ *at least until* $t + F$; C2 and C3 say $\alpha = 0$ *no later than* their deadlines. If $V$ is $\alpha$, both act on one variable and contradict whenever a "gone by" deadline falls inside the "keep until" window. If $V$ is not $\alpha$, they act on different variables and need never meet.

**Why "tri-lateral".** The model has three constraint *types*: a floor (keep), a right (erase on request), a ceiling (delete after an external event). It is not a count of legal instruments. The floor is one parameterised constraint with two instances: the long cross-border floor and the one-year SPE floor. A national floor can be substituted without changing the model (§3.4, p. 40; Corollary 2.2, p. 61).

Point to: §4.4, p. 55; §3.4, p. 40; slide 7 (model); <https://trfhimolde.streamlit.app/?p=start>

### B2.6 Why a monthly grid, and what that convention costs

**Why months.** Every obligation in the system is stated in months or years, and the shortest deadline, the Art 12(3) response period, is one month (§4.3, p. 51). A coarser grid would lose that deadline. A finer one would add nothing the law states.

**What it costs.** Three things.

1. *Boundary months can be grid artefacts.* The law counts a month from the day of receipt; the model makes the deadline bind from the start of month $t_r + \delta$, so requests on the first and the last day of a month get the same model deadline. A record whose deadline lands within a month of the window's end (like record 97) could classify differently on a day grid. That moves boundary counts, not the propositions.
2. *The window convention is a choice.* The closed window is the conservative reading of "at least" (B2.2). It can only add a collision in the last month, never remove one.
3. *Expressiveness.* One binary variable cannot express field-level redaction or nested timing (§3.7, p. 45); Corollary 2.3 relaxes this once.

Point to: §4.3, p. 51; §4.4, p. 54; §3.7, pp. 44 to 45; slide 14 (limits); <https://trfhimolde.streamlit.app/?p=start>

### B2.7 The two semantics of "verifiable"

No instrument defines "verifiable", and neither semantics is stipulated by the instruments (§4.5, p. 56). The thesis states both precisely.

**Semantics I (plaintext verifiability).**
$$
V^{I}(a,t) = \alpha(a,t)
$$
A record is verifiable exactly when its payload can be read. A record whose payload cannot be produced counts as broken.

*Not a straw man.* The 2017 OpenNCP reference source stored every audit message whole and readable, refused modification and had no purge logic; the 2026 schema (9.1.0) keeps the columns, deployments not inspected. So Semantics I is "the de facto semantics of deployed audit repositories ... rather than ... a legal requirement" (§4.5, p. 56).

**Semantics II (accountability-preserving verifiability).**
$$
V^{II}(a,t) = 1 \iff \text{(i)} \wedge \text{(ii)} \wedge \text{(iii)}
$$
where, at month $t$:

- (i) $m_{\mathrm{acc}}(a)$ is intact and unmodified, and so is $m_{\mathrm{subj}}(a)$ unless its removal is recorded under (iii);
- (ii) $c(a)$ is present and binding;
- (iii) if $\alpha(a,t') = 1$ for some $t' < t$ and $\alpha(a,t) = 0$, or likewise for $\beta$, then an invalidation entry $\iota(a)$ recording the transition, its month, its legal ground and its authorising actor is present in the audit trail and is itself covered by (i).

**Why each condition is there.**

- Without (i), a record with altered "who and when" would still count. The accountability content is the point of the record.
- Without (ii), nothing ties the access event to one specific payload. An auditor could not tell, even before invalidation, whether one record's content had been swapped for another's. Dropping (ii) turns the design into Rival 4 (B6.3).
- Without (iii), a silent disappearance of the payload would count as verifiable. That is the "trivial semantics under which every record counts as verifiable always" which the thesis itself rejects (§4.7, p. 62).

**An accurate analogy: customs records.** Customs authorities may order presented goods to be destroyed (Union Customs Code, Article 197), while the declaration documents must be kept for at least three years (Article 51). The two do not collide, because destruction reaches the goods and record-keeping reaches the documents. The record of a destroyed consignment, including the fact of its destruction, is kept for the full period (§2.7, p. 31). Semantics II does the same for an audit record: accountability attaches to the record of the access and of its payload's invalidation, not to the payload's continued existence. Semantics I is the customs rule that would say "the declaration counts only while the goods are still in the warehouse". Where the analogy stops: in customs the goods and the documents are different objects by design; in an audit record they begin in the same record, so the mechanism has to separate them (§2.7, p. 31).

Point to: §4.5, pp. 55 to 56; §2.7, p. 31; slide 8 (word); <https://trfhimolde.streamlit.app/?p=start>

## B3. The propositions and corollaries, in depth

The thesis calls these propositions because "their proofs are short once the semantics are fixed" (§4.7, p. 62). Propositions 1 to 3 are proved informally; Proposition 4 is argued from a stated legal premise (§1.5, p. 9). The order below follows the thesis: Proposition 1 and its corollaries, Proposition 3, then Proposition 2 and its corollaries, then Proposition 4.

### B3.1 Proposition 1 (infeasibility under Semantics I)

**(a) Formal statement** (§4.6, p. 57).

> *Proposition 1.* Under Semantics I, the constraint system $\{C1, C2, C3\}$ is infeasible for any record $a$ such that
> $$ t_r(a) + \delta \le t(a) + F(a) \quad\text{ or }\quad t_\pi(a) + 6 \le t(a) + F(a). $$
> The second disjunct is tested only for records the ceiling reaches, that is, with $\sigma(a)$ = secondary and $\rho(a) = 1$.

**(b) Plain reading.** If readable is what verifiable means, then any record whose erasure deadline falls on or before the last month of its retention window, or (for a record the ceiling reaches) whose ceiling deadline does, has no possible schedule of readability that obeys all three rules.

"Infeasible" means: no assignment of 0s and 1s to $\alpha(a,t)$, month by month, satisfies all the constraints at once.

**(c) Proof, step by step.**

1. Take a record satisfying the first disjunct. Define $t^{*} = t_r(a) + \delta$.
2. By hypothesis, $t^{*} \le t(a) + F(a)$.
3. Requests arrive after the access that created the record, so $t_r(a) \ge t(a)$; with $\delta \ge 1$, $t^{*} \ge t(a) + 1 > t(a)$.
4. From steps 2 and 3, $t(a) \le t^{*} \le t(a) + F(a)$: month $t^{*}$ lies inside the closed window.
5. C1 therefore requires $V(a,t^{*}) = 1$.
6. Under Semantics I, $V^{I}(a,t^{*}) = \alpha(a,t^{*})$, so C1 requires $\alpha(a,t^{*}) = 1$.
7. C2 requires $\alpha(a,t) = 0$ for every $t \ge t_r(a) + \delta = t^{*}$; in particular $\alpha(a,t^{*}) = 0$.
8. $\alpha(a,t^{*})$ is a single number. It cannot be 1 and 0. No assignment satisfies C1 and C2 together, so none satisfies $\{C1, C2, C3\}$.
9. Second disjunct: repeat with $t^{*} = t_\pi(a) + 6$ and C3 in place of C2. This needs C3 to bind, which is why $\sigma = \text{secondary}$ and $\rho = 1$ are required. If the ceiling deadline fell before creation ($t_\pi + 6 < t(a)$), the contradiction arises at $t(a)$ itself, where C1 and C3 both bind. $\blacksquare$

**The converse** (§4.6, p. 57). If neither disjunct holds, set $\alpha = 1$ on every month of the window and $\alpha = 0$ afterwards. C1 holds. C2 and C3, where they bind at all, bind only after the window. So Proposition 1 is an exact characterisation: infeasible if and only if a binding deadline falls inside the window.

**(d) Why each hypothesis is needed.**

- *The deadline must fall inside the window ($\le$, not $<$).* Counterexample when dropped: record 38 (from the checker; the thesis describes it without naming it), cross-border, $t = 10$, window 10 to 130, has its request in month 138, deadline 139. Since $139 > 130$, the converse schedule works: readable to 130, unreadable from 131. Record 38 is the single cross-border request outside its window, "precisely the case the proposition excludes" (§5.3, p. 83). The $\le$ (rather than $<$) matters because the window is closed: record 97's deadline equals the window's last month and it does collide (B2.2).
- *$\sigma = \text{secondary}$ and $\rho = 1$ on the ceiling disjunct.* Counterexample: take record 100 but suppose the narrow reading, so $\rho = 0$. Then $t_\pi + 6 = 16 \le 19$ still holds arithmetically, but C3 does not bind. Set $\alpha = 1$ on months 7 to 19 and 0 afterwards: C1 holds and there is no C2 (no request). The record is feasible. A Proposition 1 without the scope sentence would therefore declare a feasible record infeasible. Likewise C3 is defined only for secondary records, so a primary record has no ceiling to collide with. The code shows the effect at population level: `sensitivity.py` with the ceiling excluded gives 46 violating records at $F = 120$, which is $37 + 9$, the cross-border collisions plus the nine SPE erasure-driven ones the thesis gives for the narrow reading (§5.4, p. 84). (The sensitivity outputs are code output, not thesis claims.)
- *Semantics I.* Under Semantics II, step 6 fails: $V$ no longer equals $\alpha$. That is the whole of Proposition 2.

**(e) Worked example by hand.** Record 3: $t^{*} = 115 + 1 = 116$; window end $11 + 120 = 131$; $116 \le 131$, so infeasible. In month 116, C1 says $\alpha = 1$ and C2 says $\alpha = 0$. Population check, in the model: of 100 generated cross-border records, 38 received a request, 37 had deadlines inside the window, all 37 violate (§5.3, p. 83). Record 132 (SPE, from the checker, not named in the thesis) satisfies both disjuncts: $t = 1$, window 1 to 13, request month 4 so deadline 5, permit month 7 so ceiling 13. It is one of the five records violating both C2 and C3, which is why 90 records carry 95 violations.

**(f) What it does NOT claim.**

- Nothing about how often requests arrive or how often permits end near a log entry (§4.6, p. 57; §3.7, p. 45).
- That the law requires Semantics I. It is the de facto semantics of one reference implementation (§4.5, p. 56).
- The request-driven case presupposes §4.2's conclusion that the payload is not necessary for the floor's purpose. Were it necessary, Art 17(3)(b) would exempt it and only the ceiling case would remain (§4.6, p. 57).

**(g) Likely attack and reply.**

*"This is trivial. A binary variable cannot be 0 and 1."* Reply: "Yes, and the thesis says so: it resolves to a month in which $\alpha$ must be both 1 and 0 (§4.7, p. 62). Its value is as a negative result. It shows that any design keeping the payload readable for the length of the floor is unworkable wherever a binding deadline falls inside the window. So some departure from readability is unavoidable. Proposition 2 then shows a minimal departure suffices."

Point to: §4.6, p. 57; §5.3, p. 83; slides 9 (result) and 24 (q-proofs); <https://trfhimolde.streamlit.app/?p=propositions>

### B3.2 Corollary 1.1 (cross-border case)

**(a) Statement** (§4.6, p. 57).

> *Corollary 1.1 (cross-border case).* For cross-border audit records, $F(a)$ is the period left to national law: 72 months in the Norwegian pilot, as set by Helsedirektoratet as controller, 120 as reported in the literature and used illustratively in Chapter 5. The system is infeasible for record $a$ whenever an erasure request arrives at any month $t_r(a) \le t(a) + F(a) - \delta$: that is, at any point but the last $\delta$ months of the window, whatever its length, so, under the baseline response period, a request in any of the 72 months from $t(a)$ to $t(a) + 71$ collides with the pilot's six-year floor.

**(b) Plain reading.** Under the pilot floor, a request in any but the window's last month collides.

**(c) Derivation.**

1. Proposition 1's first disjunct: $t_r + \delta \le t + F$.
2. Subtract $\delta$: $t_r \le t + F - \delta$.
3. Requests satisfy $t_r \ge t$. So colliding request months are $t, t+1, \dots, t + F - \delta$: that is $F - \delta + 1$ months.
4. With $F = 72$, $\delta = 1$: $72 - 1 + 1 = 72$ months, from $t$ to $t + 71$.
5. The window has $F + 1 = 73$ months, $t$ to $t + 72$. A request in month $t + 72$ has deadline $t + 73$, outside. $\blacksquare$

**(e) Worked example.** Record 3 under $F = 72$: colliding request months 11 to 82. Its actual request (115) is outside, so no collision. Under $F = 120$: colliding months 11 to 130; 115 is inside.

**(f) Not claimed.** How often patients exercise Art 17 (§4.6, p. 57).

**(g) Attack.** *"Your ten years is unsourced."* Reply: "Agreed, it is illustrative. The operator wrote that no specification fixes a period and the pilot uses six years (Appendix D). The corollary holds at any value."

Point to: §4.6, p. 57; Appendix D, p. 168; slide 4 (strip); <https://trfhimolde.streamlit.app/?p=witness&r=3&m=116>

### B3.3 Corollary 1.2 (SPE case, no erasure request)

**(a) Statement** (§4.6, p. 57), first four sentences:

> *Corollary 1.2 (Secure Processing Environment case).* For Secure Processing Environment access logs, $F(a) = 12$ and $\sigma(a)$ = secondary. Suppose the permit expires at or before the sixth month of the record's retention window, so that $t_\pi(a) + 6 \le t(a) + 12$. Then C1 and C3 are contradictory at $t^{*} = t_\pi(a) + 6$ by the argument above, provided C3 reaches the record. *Where it does, no erasure request is required.*

The corollary also assumes, as a stated premise, that the activity content, not only the subject fields, is data concerning health.

**(b) Plain reading.** If a researcher's log entry is written in the last six months of a permit, the one-year keep rule outlasts the six-month delete rule. Under readable-verifiability that is a contradiction, and no patient had to do anything.

**(c) Proof.**

1. Rearrange the hypothesis: $t_\pi + 6 \le t + 12 \iff t_\pi - t \le 6$. The remaining permit duration when the entry is written is at most six months.
2. Let $t^{*} = t_\pi + 6$. With $t_\pi \ge t$ (permit live when the entry is written), $t^{*} > t$, so $t^{*}$ is inside $[t, t+12]$.
3. C1 under Semantics I: $\alpha(a,t^{*}) = 1$.
4. C3 (with $\rho = 1$): $\alpha(a,t^{*}) = 0$.
5. Contradiction, with $t_r = \infty$ throughout. $\blacksquare$

**(d) Why each hypothesis is needed.**

- *$\rho = 1$.* On the narrow reading C3 does not bind and the record is feasible (B3.1(d)).
- *Activity content is health data.* If only the subject fields were health data, Semantics I could keep the payload readable and delete only the subject fields at the ceiling. The collision would not arise (§4.6, p. 57).
- *Remaining duration $\le 6$.* Counterexample: record 102 (from the checker, not named in the thesis): $t = 5$, $t_\pi = 12$, ceiling $18$, floor end $17$. Since $18 > 17$, the floor ends one month before the ceiling binds; feasible.

**(e) Worked example and the count.** Record 100: $t_\pi - t = 10 - 7 = 3 \le 6$; collision months 16 to 19. In the generated run, 78 SPE records had no request, and 39 of them collide (§5.4, p. 84).

*Why exactly half.* The generator draws the permit length $t_\pi - t$ uniformly from $\{1, \dots, 12\}$. Collision needs a length of at most 6: 6 values out of 12, so one half (§5.4, p. 85). That 39 of 78 is exactly one half is how this seed fell. With a five-year permit and the remaining duration drawn uniformly over 60 months, the share is $6/60 = 1/10$. In general it falls as $6/\pi_{\max}$, but never to zero: "every permit used in its final six months produces colliding entries, whatever the distribution of permit lengths" (§5.4, p. 85).

*The decomposition (generated records).* Of 53 violating SPE records, 49 are ceiling-driven (44 C3 only, 5 both) and 4 request-only. The 44 are the 39 witnesses plus 5 with requests after their windows; on the narrow reading they lapse, leaving 9 (§5.3, p. 83; §5.4, p. 84).

**(f) Not claimed.** Frequency; that the broad reading is correct; reach over dataset-level logs without health content. It is "a conditional extension" (§4.6, p. 58).

**(g) Attack.** *"Article 68(12) is about the permit dataset, not the logs."* Reply: "That is the narrow reading, and it is respectable; I state Corollary 1.2 conditionally. If it wins, I lose Corollary 1.2 and the conditional branch of Corollary 2.3, and nothing else: an SPE log then collides only through an erasure request (§4.6, p. 59; §6.2, p. 93)." Do not say the three-way collision survives the narrow reading.

Point to: §4.6, pp. 57 to 59; §5.4, pp. 84 to 85; Figure 5.2, p. 85; slides 5 (research), 21 (q-reading) and 23 (q-permits); <https://trfhimolde.streamlit.app/?p=witness&r=100&m=16>

### B3.4 Proposition 3 (anchoring) and the anchor condition

**(a) Statement** (§4.6, p. 60).

> *Proposition 3 (anchoring).* Let a record's floor of $F$ months run from its creation month $t(a)$, and let a ceiling of $L$ months run from an event at month $e(a) \ge t(a)$. Under Semantics I, the floor and the ceiling are jointly satisfiable for $a$ if and only if $e(a) + L > t(a) + F$. Hence (i) if the ceiling is anchored to the same event as the floor, $e(a) = t(a)$, they are satisfiable for every record if and only if $L > F$, a condition decidable from the text alone; and (ii) if the ceiling is anchored to an external event, then whenever $L \le F$ they fail for exactly those records with $e(a) - t(a) \le F - L$, a set that the text does not reveal and each record's history determines.

The brief's "$e - s \le F - L$" is this condition with $s = t(a)$, the creation month.

**(b) Plain reading.** A ceiling clashes with a floor only if it ends on or before the floor ends. With one shared start, the statute shows the clash on its face. With a different start, the statute can look harmless, and only each record's dates reveal it.

**(c) Proof, step by step.**

1. C1 under Semantics I demands $\alpha = 1$ on the set $A_1 = \{t(a), \dots, t(a)+F\}$.
2. The ceiling demands $\alpha = 0$ on the set $A_0 = \{e(a)+L, e(a)+L+1, \dots\}$.
3. A contradiction exists if and only if $A_1 \cap A_0 \neq \emptyset$.
4. Since $e(a) \ge t(a)$ and $L \ge 1$, the first month of $A_0$ satisfies $e(a) + L > t(a)$, so $A_0$ starts after $A_1$ starts.
5. Two sets of consecutive months, the second starting after the first starts, overlap if and only if the second starts no later than the first ends: $e(a) + L \le t(a) + F$.
6. So they are jointly satisfiable if and only if $e(a) + L > t(a) + F$; then the schedule "readable before $e + L$, unreadable from $e + L$" meets both.
7. Case (i): put $e = t$. The condition becomes $t + L > t + F$, that is $L > F$. It does not mention any record's history, so it can be read off the text.
8. Case (ii): rearrange the failure condition $e + L \le t + F$ into $e - t \le F - L$. The left side is each record's own delay between log entry and anchor event. $\blacksquare$

**Why (ii) needs $L \le F$.** If $L > F$ then $F - L < 0$. Since $e \ge t$, the left side $e - t \ge 0$. A non-negative number cannot be at most a negative one, so no record ever fails. A collision of any kind therefore needs a ceiling no longer than the floor, whichever way it is anchored. "What the anchor decides is whether the collision can be seen" (§4.6, p. 60).

**(d) Why the hypotheses are needed.**

- *$e(a) \ge t(a)$.* It restricts the statement to the cases treated. If the anchor event preceded creation, the condition $e + L > t + F$ still holds, and a ceiling already passed at creation makes the record infeasible from $t(a)$ (§4.6, p. 60). The Z3 check uses the same restriction.
- *Semantics I.* Under Semantics II the floor does not read $\alpha$, so there is nothing to collide.

**(e) Worked examples by hand.**

- *Record 100.* $F = 12$, $L = 6$, $e = t_\pi = 10$, $t = 7$. $F - L = 6$; $e - t = 3 \le 6$: collides. Equivalently $e + L = 16 \le 19$. Overlap length $19 - 16 + 1 = 4$ months.
- *Record 102.* $e - t = 12 - 5 = 7 > 6$: clear, by one month ($18 > 17$).
- *Politiregisterloven §17* (§6.10, p. 100). In the thesis's Norwegian, "lagres i minst 1 år og slettes senest etter 3 år" (candidate's translation: stored for at least one year and deleted at the latest after three years): $F = 12$, $L = 36$, both from the log entry (a reading of the sentence's syntax, which the provision does not state in words). Case (i): $L = 36 > 12 = F$, so no collision without a request. The generated run: 60 records, 7 violate, none without an erasure request (§6.10, p. 100). The cross-sector module's printed witness, rid 906, is erasure-driven: log at month 0, erasure deadline 11, inside the floor. [CHECK: §17 text not verified against Lovdata; flagged open in the existing notes.]

**(f) Not claimed.** Frequency. That §17 expressly anchors both limbs at the entry: it is a reading (§6.10, p. 101). That other sectors have external-anchor ceilings: MiFID II and Elhub are candidates not yet tested (§6.10, p. 101; §2.7, p. 30).

**(g) Attack.** *"This is just interval overlap."* Reply: "Yes. Its value is diagnostic: it corrected my own expectation that any floor plus ceiling collides (§17 does not), and it gives the implementing acts a drafting test: look for a ceiling no longer than a floor, anchored to a different event (§6.8, p. 98)."

Point to: §4.6, p. 60; §6.10, pp. 100 to 101; slides 20 (q-logistics) and 30 (q-props34); <https://trfhimolde.streamlit.app/?p=anchor>

### B3.5 Proposition 2 (feasibility under Semantics II)

**(a) Statement** (§4.7, p. 60).

> *Proposition 2.* Under Semantics II, the constraint system $\{C1, C2, C3\}$ is jointly satisfiable for every record $a \in A$, for every arrival pattern of erasure requests $\{t_r(a)\}$ and permit expiries $\{t_\pi(a)\}$, and for every floor parameter $F(a) \in \mathbb{N}$.

**(b) Plain reading.** If verifiable means accountable, every record has a schedule obeying all three rules, whatever the dates and the floor.

**(c) Proof (constructive), step by step.** Define the invalidation month
$$
t^{I}(a) = \min\big(\, t_r(a) + \delta,\;\; t_\pi(a) + 6,\;\; t(a) + P(a) \,\big),
$$
with the minimum of infinite terms equal to $\infty$. Build this trajectory:

1. For $t < t^{I}(a)$: $\alpha(a,t) = 1$. Keep $m(a)$, $c(a)$, $k(a)$, $p(a)$.
2. At $t = t^{I}(a)$, if finite: destroy $k(a)$; where the ground is Art 68(12) and C3 reaches the subject fields, remove $m_{\mathrm{subj}}(a)$ and set $\beta = 0$; append $\iota(a)$ with month, ground (Art 17(1), Art 68(12), or Art 5(1)(c) and (e) where $P$ fixed the month), what was removed, and the authorising actor; keep $m_{\mathrm{acc}}(a)$ and $c(a)$ unchanged.
3. For $t > t^{I}(a)$: $\alpha = 0$, and $\beta = 0$ where step 2 removed the subject fields. Keep $m_{\mathrm{acc}}(a)$, $c(a)$, $\iota(a)$.
4. If C3 reaches the subject fields and $t^{I}(a) < t_\pi(a) + 6$ (a request or $P$ came first), remove $m_{\mathrm{subj}}(a)$ at $t_\pi(a) + 6$, set $\beta = 0$ from then, and append a second entry recording it.

Edge case: if $t^{I}(a) \le t(a)$, the payload is never held readable; set $\alpha = 0$ from $t(a)$ and append $\iota(a)$ at $t(a)$. C1 still holds, because Semantics II does not read $\alpha$.

Now check each constraint.

- *C2.* If $t_r < \infty$, then $t^{I} \le t_r + \delta$ because a minimum is no larger than any of its terms. From $t^{I}$ onwards $\alpha = 0$, so $\alpha = 0$ for all $t \ge t_r + \delta$. If $t_r = \infty$, C2 is vacuous.
- *C3.* If $\sigma = \text{secondary}$ and $t_\pi < \infty$, then $t^{I} \le t_\pi + 6$, so $\alpha = 0$ from $t_\pi + 6$. $\beta = 0$ from $t_\pi + 6$, by step 2 if the ceiling fixed $t^{I}$, by step 4 if something earlier did. Otherwise vacuous.
- *C1.* Take any $t$ in $[t(a), t(a) + F(a)]$. (i) holds: no step modifies $m_{\mathrm{acc}}$, and the only removal of $m_{\mathrm{subj}}$ is recorded. (ii) holds: no step removes $c(a)$, and $c(a)$ is not derived from $k(a)$, so destroying the key does not affect it. (iii): if $\alpha(a,t) = 1$, vacuous; if $\alpha(a,t) = 0$, then $t \ge t^{I}$, and step 2 put $\iota(a)$ in the trail, step 3 keeps it, and it is covered by (i). Same for $\beta$ through steps 2 and 4. So $V^{II}(a,t) = 1$ throughout the window. $\blacksquare$

Nothing in the argument depends on the value of $F(a)$ or on the arrival times. That is where "for every" comes from.

**(d) Why each element is needed.**

- *The minimum over all triggers.* If invalidation waited for a later deadline, the earlier constraint would fail in between. Record 132 (from the checker, not named in the thesis): erasure deadline 5, ceiling 13. Invalidating at 13 would leave the payload readable in months 5 to 12, violating C2.
- *Step 4.* Without it, record 132's subject link would survive after month 13, because the month-5 invalidation was on the Art 17(1) ground and did not remove it. C3 over $\beta$ would fail. The checker logs a separate entry: month 13, removed `patient_pseudonym`, ground EHDS Art 68(12).
- *Keeping $c(a)$ and logging $\iota(a)$.* Without them, Z3 finds counterexamples (B3.9).
- *Semantics II itself.* Under Semantics I, the record 3 schedule above fails C1 in months 116 to 131.

**(e) Worked examples by hand.**

- *Record 3.* $t^{I} = \min(115 + 1, \infty, \infty) = 116$. Ground GDPR Art 17(1). Patient link kept (cross-border). Readable months 11 to 115; from 116 key, salt and ciphertext gone; $\iota$ logged at 116.
- *Record 100.* $t^{I} = \min(\infty, 10 + 6, \infty) = 16$. Ground EHDS Art 68(12). Subject link removed at 16 with its own logged entry. Months 16 to 19 now satisfy C1, because (i), (ii), (iii) all hold.
- *Record 133 (tie, from the checker).* $t = 11$, request 25, permit 20: $\min(26, 26) = 26$. The code records a tie under Art 17(1) "since it is the act that triggered erasure". Four such ties exist in the generated run (§5.7, p. 88). On a tie, step 2 as worded removes subject fields only on the Art 68(12) ground and step 4 needs a strict $<$, so read the two together: the code removes the link at month 26 anyway, under its own Art 68(12) entry, and C3 over $\beta$ holds.
- *Population (generated).* 138 invalidated: all 38 cross-border records with requests plus all 100 SPE records. 52 on Art 17(1), 86 on Art 68(12). Zero violations (Table 5.6, p. 87).

**(f) Not claimed** (§4.7, p. 63). That the solution is lawful (that needs the residue analysis). That key destruction can be verified externally: $\iota(a)$ is an attested record, not a proof. That the semantics is endorsed by any authority.

**(g) Attack.** *"You defined Semantics II so that this works."* Reply: "The objection has force, and the thesis concedes its premise and denies its conclusion (§4.7, p. 62). The mathematics is modest. Any number of semantics admit a solution, including a trivial one where everything is verifiable always. The claim is that this semantics is a defensible reading, grounded in the necessity limit of Art 17(3)(b), the minimisation principle of Art 5(1)(c), and the accountability purpose. It keeps every element accountability needs and discards only what it does not. Proposition 1 carries the other half: some departure is unavoidable."

Point to: §4.7, pp. 60 to 63; Table 5.6, p. 87; slides 9 (result) and 11 (audit); <https://trfhimolde.streamlit.app/?p=propositions>

### B3.6 Corollaries 2.1 and 2.2

**(a) Statements** (§4.7, p. 61).

- *Corollary 2.1.* "The construction requires no coordination between the erasure process and the retention process, and no knowledge at the time a record is created of whether an erasure request will ever arrive. The invalidation month is determined entirely by events as they occur."
- *Corollary 2.2.* "Because $F(a)$ is arbitrary in the proof, the result holds simultaneously for an illustrative ten-year cross-border floor, the six-year floor of the Norwegian pilot and the one-year Secure Processing Environment floor, and for any national floor substituted for either. The model is tri-lateral in constraint type and indifferent to the number of floor instances."

**(b) Plain reading.** 2.1: the system does not need to predict the future; it reacts when a request or expiry happens. 2.2: whatever floor the law or the controller picks, the same mechanism works.

**(c) Proof.** 2.1: $t^{I}$ is a minimum of event times. Each term becomes known when its event occurs (or when the controller sets $P$), and until then the record is simply readable. 2.2: $F(a)$ appears in the C1 check only as the end of the window, and the C1 argument holds for any $t$ in any window. $\blacksquare$

**(e) Example.** Record 3 was written in month 11 with no knowledge of month 115. `sensitivity.py` shows zero Semantics II violations at floors 120, 72 and 36 (code output, not in the thesis). Section 4.2 adds that "a lower or absent floor removes collisions and creates none" (p. 51).

**(f) Not claimed.** That the floor value never matters: it drives the Semantics I counts.

**(g) Attack.** *"Then why argue about six versus ten years?"* Reply: "It changes which requests collide under readable-verifiability, not whether the mechanism works. That the six-year period has no identified national legal basis is a finding for the controller, not a limit on the model (§4.2, p. 51)."

Point to: §4.7, p. 61; §4.2, p. 51; slide 9 (result); <https://trfhimolde.streamlit.app/?p=propositions>

### B3.7 Corollary 2.3 (sensitivity to what auditing needs)

**(a) Statement** (§4.7, p. 62).

> *Corollary 2.3 (sensitivity to what auditing needs).* Extend the model with one accessibility variable per part of the payload, which the single-variable model of Section 4.3 cannot express, and partition the payload as $p(a) = p_n(a) \cup p_r(a)$, where $p_n(a)$ is any part that auditing turns out to need, and retain $p_n(a)$ with the accessor fields. The trajectory of Proposition 2, with $p_r(a)$ in place of $p(a)$, satisfies C1 and C2, and it satisfies C3 unless $p_n(a)$ is itself electronic health data within the environment on the broad reading of Article 68(12). In that case C1 and C3 collide over $p_n(a)$, by the argument of Proposition 3, for exactly the records it identifies under case (ii).

Exits named: relocation (Rival 6), dataset-granularity logging, the narrow reading, or anonymising $p_n(a)$.

**(b) Plain reading.** If an auditor needs part of what was logged, keep that part. That works everywhere except where the kept part is health data inside a research environment, where the old collision returns for that part.

**(c) Proof sketch, step by step.**

1. Replace $p$ by $p_r$ in steps 1 to 4 of Proposition 2; add $p_n$ to what condition (i) keeps intact.
2. C1 holds as before.
3. C2 holds for $p_r$ as before; for $p_n$ through Art 17(3)(b), which applies because $p_n$ is by assumption necessary.
4. C3: if $p_n$ is not electronic health data, it is not reached; met. If it is, C3 needs it gone from $t_\pi + 6$, while C1 needs it intact to $t + F$. By Proposition 3 these overlap for exactly the records with $t_\pi - t \le F - 6$. $\blacksquare$

**(d) Why the extension is needed.** The base model has one $\alpha$ per record, so it cannot keep part of a payload. Why the collision arises: $p_n$ is kept under condition (i) "without the logged-removal exception that the subject fields have" (§4.7, p. 62).

**(e) Example (hypothetical, not a run result).** If part of record 100's activity content were needed and counted as health data, it would collide over months 16 to 19, as in B1.2.

**(f) Not claimed.** That auditing does need part of the payload. For cross-border records the thesis argues it does not; for SPE logs the argument is weaker, which is why this corollary exists (§4.2, p. 50).

**(g) Attack.** *"So your solution fails exactly where it matters?"* Reply: "Only for a needed part that is also health data inside an SPE on the broad reading, exactly as Corollary 1.2 fails, with the same exits (§4.7, p. 62)."

Point to: §4.7, p. 62; slide 21 (q-reading); <https://trfhimolde.streamlit.app/?p=propositions>

### B3.8 Proposition 4 (location and right), argued from a stated premise

**(a) Statement** (§4.10, p. 72).

> *Proposition 4 (location and right).* *This result depends on a legal premise stated here as an explicit assumption, not derived from the model: that a controller receiving a relocated record receives the erasure obligation of Article 17(1) GDPR with it.* Let a ceiling be anchored to a location, requiring data to be absent from that location after a deadline, and let a right be anchored to the data subject, requiring data to be inaccessible to any controller holding them after a deadline. Under Semantics I, and granting that assumption, relocating a record before the ceiling's deadline satisfies the ceiling and the floor together, while the floor and the right remain infeasible for every record satisfying the first disjunct of Proposition 1.

**(b) Plain reading.** Exporting the logs out of the SPE when the permit closes gets past the delete-from-here rule. It does not get past the right to erasure, because that right follows the data to whoever holds them.

**(c) Argument, step by step.**

1. The ceiling quantifies over a place; after relocation the record is not there, so the ceiling holds.
2. On the rival's premise (Art 73(1)(e) fixes how long, not where), the floor is met at the new location.
3. The right quantifies over a controller: Art 17(1) binds whoever holds the data. Premise: the receiver inherits it.
4. So C1 and C2 bind the new holder as before, and Proposition 1's first-disjunct argument applies unchanged. $\blacksquare$

**(d) Why the premise is needed, and its status.** Step 5 is a legal claim, not mathematics. If it were false, relocation would also escape the right, and Rival 6 would become stronger; Propositions 1 to 3 would stand (§4.10, p. 72). The proposition is stated over the model extended informally with location and controller, which §4.3 does not represent; the artefact does not execute it (§4.10, p. 72). Hence "argued from a stated premise", not "proved".

**(e) Worked example (record 132, from the checker, not named in the thesis).** $t = 1$, window 1 to 13, request month 4 (deadline 5), permit month 7 (ceiling 13). Export before month 13 satisfies the ceiling. The month-5 erasure deadline still sits inside the window at the new controller, so readable-verifiability still fails in months 5 to 13.

**(f) Not claimed.** That relocation is unlawful: it is accepted as a sufficient answer to Corollary 1.2. Nor that it is free: the subject fields move to a second controller, so data are moved, not reduced (§4.10, p. 72).

**(g) Attack.** *"This is an assumption with a proof attached."* Reply: "Largely yes: it is a legal argument given the form of a proposition so its premise is explicit (§4.10, p. 72). It shows which part of the conflict no relocation escapes: the request-driven part."

Point to: §4.10, p. 72; §6.1, p. 91; slides 6 (fixes) and 30 (q-props34); <https://trfhimolde.streamlit.app/?p=anchor>

### B3.9 What exhaustive search and Z3 check, and what they do not

**Exhaustive search** (§5.5, p. 85). A separate function, `brute_force_semantics_I`, enumerates every assignment of $\alpha$ over a 14-month horizon: $2^{14} = 16{,}384$ assignments per case. It asks whether any assignment satisfies C1 (under Semantics I), C2 and C3.

| Case | Feasible? |
|---|---|
| SPE, no request, permit 3 months | False |
| SPE, request at $t = 2$ | False |
| Cross-border, floor scaled to 12, request at $t = 4$ | False |
| Control: no request, no expiry | True |

"No trajectory succeeds" is stronger than "the checker's trajectory fails", and the control shows the search can say True. But every constraint is pointwise in time, so enumeration equals checking each month in turn: "a sanity check rather than independent evidential weight" (§5.5, p. 85). Its value is separate code sharing only $\delta$ and the ceiling, with a test comparing the two on every boundary month. The floor is scaled to 12 because $2^{120}$ assignments cannot be enumerated. In all $4 \times 16{,}384 = 65{,}536$ assignments; 65,535 are evaluated, as the control stops at its first success (§5.8, p. 90).

**Z3 bounded check** (§5.5, p. 86). `z3_check.py` poses each claim as a request for a counterexample within bounds: creation 0 to 12, floor 1 to 120, $\delta$ 1 to 3, request and anchor up to a horizon of 140, ceiling 1 to 120. "Unsat" means no counterexample exists within the bounds. Run output: 9 of 9 checks unsat (Proposition 1 both directions; Proposition 2; Proposition 3 general and both cases in both directions); the sanity check is sat; four broken variants are refuted (Proposition 2 without $\iota$, without $c$, without the subject-link entry; Proposition 3 shifted by one month).

**What the Proposition 2 check really checks.** The code comment says the accountability conjuncts are set true by construction, "so this check verifies the timing of the trajectory, not that accountability is preserved". Its evidential weight lies in the refuted mutations: remove an element and the check fails (§5.5, p. 86).

**The honest limit.** All three were written in the same AI-assisted process from the §4.4 constraints. They check the code against the encoding, and the propositions against the constraints as encoded, not the constraints against the law (§5.5, p. 86; §6.7, p. 97). In one line: "The checks test my code against my model, not my model against the law."

Point to: §5.5, pp. 85 to 86; Appendix A.23 to A.24, pp. 150 to 153; slides 12 (evidence) and 24 (q-proofs); <https://trfhimolde.streamlit.app/?p=robust>

## B4. The mechanism: Crypto-Erasure by Invalidation

"The proof of Proposition 2 is also a build sheet" (§4.8, p. 63). Each step below exists because the proof, or the residue analysis, needs it.

### B4.1 Envelope encryption with a data key per record

**What it is.** Each record's payload is encrypted under its own data key $k(a)$. The data keys are themselves encrypted ("wrapped") under a key-encrypting key held in a hardware security module (HSM) or an equivalent custody boundary. Destroying $k(a)$ means destroying the wrapped key and any cached copies inside that boundary (§4.8, p. 63; Barker, 2020).

**Why per record.** A permit expiry invalidates one permit's records; an erasure request, one person's. The sets intersect without nesting, so no per-person or per-permit key serves both (§4.8, p. 63). A key-share design (a share per subject and per permit) would avoid per-record keys; named, not built (Cachin et al., 2013).

**Why keys at all, when the store deletes the ciphertext.** "Nothing in the TRF Model distinguishes key destruction from deletion of the payload: both set $\alpha$ to zero" (§4.8, p. 65). Keys earn their place for copies the store cannot delete at once, such as backups, which the specification reaches: data "MUST be deleted or rendered unrecoverable within six months of permit expiry, including any backups or redundant copies" (TEHDAS2, 2026b, OPR-6, p. 43). For those copies key destruction secures unintelligibility, not erasure (EDPB Guidelines 02/2025).

**In the artefact.** The checker removes a key reference. The optional `crypto_envelope.py` uses real per-record AES-256-GCM keys, wrapped under a key-encrypting key. Run output on the 200 generated records: all decrypt before invalidation; 138 keys destroyed; 138 refuse; 62 still read; record 3's ciphertext tried under the 62 surviving keys opens 0 times (§5.8, p. 89). The custody object stands in for an HSM, so destruction is in program memory.

Point to: §4.8, pp. 63 to 65; §5.8, p. 89; slides 10 (mechanism) and 25 (q-keys); <https://trfhimolde.streamlit.app/?p=built>

### B4.2 The hiding and binding commitment, and the salt

**Definitions.** A commitment $c = \mathrm{Commit}(p, r)$ is a short value fixed at write time:

- *Hiding:* someone who holds $c$ but not the salt $r$ learns nothing about $p$.
- *Binding:* nobody can find a second payload $p' \neq p$ and salt $r'$ with $\mathrm{Commit}(p', r') = c$.

The code uses $c = \mathrm{SHA\text{-}256}(r \Vert p)$ with a 16-byte salt (§5.2, p. 80): binding rests on collision resistance, hiding on a random, secret salt.

**Why a bare hash of a name leaks.** Suppose $c = H(p)$, unsalted, with $p$ a name and birth date. An adversary need not invert $H$: she hashes candidate payloads (names from a register; a century has about 36,525 birth dates) until one matches $c$. The same works for a diagnosis code or a formulary medicine: the space is small (§4.9, p. 68). An unsalted hash would therefore be surviving personal data, and the mechanism "would have relocated the erasure problem rather than solved it" (p. 68). With a random 128-bit salt, each guess must also guess the salt: $2^{128}$ possibilities.

**Why the salt is destroyed with the key.** Before invalidation the salt lets an auditor open the commitment, which detects substitution. After invalidation a retained salt would let anyone with a candidate payload confirm a guess, so it goes at $t^{I}$. Binding is unaffected: it is a property of $c$ (§4.8, p. 65). A party that must later prove its own copy (the patient, the home contact point) has to be handed the opening at write time.

**The honest caveat.** In the reported run the salt is derived from the record identifier, `bytes[(rid*7 + i) % 256]`, so every run reproduces exactly; that commitment is therefore not hiding in that run. The flag `--random-salts` draws salts from `os.urandom`, as a deployment must (§5.2, p. 80). The salt of the subject-field commitment is derived the same way.

Point to: §4.8, p. 65; §4.9, p. 68; §5.2, p. 80; slides 10 (mechanism) and 27 (q-residue); <https://trfhimolde.streamlit.app/?p=built>

### B4.3 The Merkle log, inclusion proofs, and what a root proves

**What it is.** Every access event, invalidation and subject-link removal is appended to a Merkle log with RFC 6962 hashing (§4.8, p. 66):
$$
\text{leaf} = H(\texttt{0x00} \Vert \text{data}), \qquad \text{node} = H(\texttt{0x01} \Vert \text{left} \Vert \text{right}).
$$
The two prefixes keep a leaf from ever being confused with an internal node. The root is the single hash at the top.

**What enters a leaf.** Accessor fields, creation month, payload commitment, salted subject commitment; never the payload or subject fields, so the log never needs rewriting (p. 66).

**Inclusion proof.** To show one entry is in the log, give the sibling hash at each level from the leaf to the root. The verifier rehashes upwards and compares with the root. The proof length is about $\log_2 n$. In the generated run the log has 438 entries: 200 access events + 138 invalidations + 100 subject-link removals. Each inclusion proof has 9 sibling hashes (from the code). For a billion entries it is about thirty (§6.5, p. 96).

**What a root proves.** Given a root the auditor trusts, a valid proof shows that an entry with exactly these bytes sits in the log. Alter one byte and the proof fails. The run's three tamper tests: altering record 100's actor, record 100's invalidation ground, or record 3's patient link each makes $V^{II}$ false; restoring them makes it true (§5.7, p. 88).

**What it does not prove.** The artefact recomputes the root from its own leaves. That detects divergence between a record and its logged events, not a rewrite of the whole log by the operator. Catching a rewrite needs earlier roots published or countersigned outside the operator, and consistency proofs between roots (Laurie et al., 2013): specified, not implemented (§4.9, p. 69; §5.7, p. 88). Hence "tamper-evident", not stronger.

Point to: §4.8, p. 66; §4.9, p. 69; §5.7, p. 88; §6.5, p. 96; slides 11 (audit) and 29 (q-roots); <https://trfhimolde.streamlit.app/?p=run>

### B4.4 The invalidation entry

**What it is.** $\iota(a)$ holds the record identifier, the invalidation month, the legal ground, the authorising actor, and a hash of the destroyed key's identifier, not of the key (§4.8, p. 65). It is appended, never edited: "Invalidation is an event that is logged, not an event that erases the log." Key-management guidance anticipates such a record: after destruction a key's "previous existence may be recorded (e.g., in metadata or audit logs)" (Barker, 2020, §7.6; thesis p. 66).

**Why it is there.** It is condition (iii) of Semantics II. Even alone it is worth adopting: it "costs little and converts an unexplained absence into an accountable one" (§6.8, p. 98).

*Record 100's entry in the generated run:* month 16, ground EHDS Art 68(12), authorised by DPO; a second entry records the subject-link removal at month 16. (In the toy code the key-identifier hash is not hiding, since the toy key names are predictable.)

Point to: §4.8, pp. 65 to 66; §6.8, p. 98; slide 11 (audit); <https://trfhimolde.streamlit.app/?p=witness&r=100&m=16>

### B4.5 What survives, and why that gives $V = 1$ under Semantics II

| What survives | Which condition it serves |
|---|---|
| Accessor fields $m_{\mathrm{acc}}(a)$, checked by inclusion proof | (i) |
| Subject fields, while kept (cross-border: whole floor), checked by their salted commitment | (i) |
| Commitment $c(a)$, in the log leaf | (ii) |
| $\iota(a)$ and any subject-link removal entry, in the log | (iii), and covered by (i) |

What goes at $t^{I}$: key, salt, ciphertext; and for patient-level SPE logs, the subject fields at the ceiling.

So in every month of the window, (i), (ii) and (iii) hold, and $V^{II} = 1$ while $\alpha = 0$. The auditor can then establish four things: the access happened, with its attributes; some payload was bound at write time and has not been swapped; it was invalidated, when, on what ground, by whom; each entry is as first written. The auditor cannot read the payload, and cannot verify that the key is gone (§4.8, p. 66).

Point to: §4.8, p. 66; §5.7, p. 88; slide 11 (audit); <https://trfhimolde.streamlit.app/?p=witness&r=100&m=19>

### B4.6 One record through the mechanism: record 100

| Month | State of record 100 | $\alpha$ | $\beta$ | $V^{II}$ |
|---|---|---|---|---|
| 7 | Access logged. Payload encrypted under its own key; commitment `678ade47...` and salted subject commitment computed; access leaf appended | 1 | 1 | 1 |
| 8 to 9 | Unchanged | 1 | 1 | 1 |
| 10 | Permit DP-015 expires; the Health Data Access Body's portal supplies the date (§4.11, p. 73); ceiling deadline 16 fixed, so $t^{I} = 16$ unless an earlier request arrives | 1 | 1 | 1 |
| 11 to 15 | Unchanged; payload still readable to an authorised auditor | 1 | 1 | 1 |
| 16 | Invalidation: key destroyed, salt destroyed, ciphertext deleted; subject field PSN-0000 and its salt removed; two entries appended (ground EHDS Art 68(12), DPO) | 0 | 0 | 1 |
| 17 to 19 | Accessor fields, commitment and entries remain; inclusion proofs verify | 0 | 0 | 1 |
| 20 | Floor over. Specified terminal transition: identifying metadata destroyed, logged (not implemented) | 0 | 0 | not required |

*Variant:* record 132 (from the checker) loses its payload at month 5 on Art 17(1) and its subject link at month 13 on Art 68(12): step 4 of Proposition 2.

Point to: §4.7, pp. 60 to 61; §4.8, p. 67; Figure 5.2, p. 85; slide 11 (audit); <https://trfhimolde.streamlit.app/?p=witness&r=100&m=16>

### B4.7 The honest boundary: key custody, backups, HSM

**Attested, not proven.** The entry records that a named actor destroyed a named key in a named month on a named ground. An auditor can check that the claim was made, by whom and when, and that it has not been altered. An auditor cannot check that the claim is true (§6.3, p. 94). The further from the storage medium an approach works, the harder destruction is to assert, and cryptographic erasure is the limiting case (Reardon et al., 2013).

**An HSM narrows the gap without closing it.** A FIPS 140-3 validated module puts destruction inside a tested boundary, but validation attests the module's design, not any particular destruction (§6.3, p. 94).

**Backups.** Copies the store cannot delete at once become unreadable at $t^{I}$ and leave by rotation. Until then they remain personal data: a bounded residue, stated as such (§4.9, p. 69).

**The trust assumptions** (§4.9, p. 69): the controller destroys when it says and kept no outside copy; the custody boundary retains and leaks nothing; the log operator does not rewrite history (detectable only with published roots); the accumulator manager, if used; hash and cipher hold over the horizon.

**What would close it.** Proof of secure erasure, or certified deletion, whose public verifiability is open (Broadbent & Islam, 2020); the entry could then carry a proof with no change to the model (§7.5, p. 108). Against deletion logged in the same log, the mechanism's edge is the commitment (§6.3, p. 95).

Point to: §4.9, pp. 69 to 70; §6.3, pp. 94 to 95; slide 25 (q-keys); <https://trfhimolde.streamlit.app/?p=robust>

### B4.8 Residual identifiability

**The finding.** The residue is pseudonymised, not anonymous, until the terminal transition. "Any claim that the mechanism achieves anonymisation would be false" (§4.9, p. 69).

**The sources.**

- Datatilsynet (2015): encryption protects rather than anonymises; data stay personal while any key or linkage capable of re-identification is kept.
- EDPB draft Guidelines 02/2026 (version 1.0, adopted 7 July 2026, for consultation): anonymous only if the data resist isolation, linkage and inference by means reasonably likely to be used; encryption is reversible and is not anonymisation (§4.9, p. 68).
- CJEU, *EDPS v SRB* (C-413/23 P, 4 September 2025), paras 73 and 76 to 77: pseudonymised data may not be personal for a recipient who cannot lift the pseudonymisation, but remain personal for the controller who holds the additional information. The repository controller holds both the subject link and the accessor's identity, so for it the residue is personal data (§4.9, p. 69).
- *Breyer* (C-582/14) is the earlier case on identification through a third party's additional data. [CHECK: Breyer is not cited in the thesis; background only, do not attribute it to the thesis.]

**Why it is nonetheless defensible.** The test is erasure, not anonymisation, and the store meets it by deletion (§4.9, p. 69). Against enumerating a small set of accessors against a surviving leaf hash, the specification adds a per-entry nonce, destroyed at the terminal transition: not implemented (§4.9, p. 68).

Point to: §4.9, pp. 68 to 69; §4.8, p. 67; slide 27 (q-residue); <https://trfhimolde.streamlit.app/?p=witness&r=100&m=19>

### B4.9 Why this is not "just crypto-shredding", a blockchain, or redactable signatures

**Crypto-shredding.** The technique is established; no new cryptography is claimed. The practitioner pattern is bilateral and "asserts that erasure occurred" (§4.8, p. 66); the thesis adds the ceiling, a model, a verifiability semantics and a checkable record (§2.4, p. 25). Concede: the model cannot tell key destruction from deletion, so keys rest on backups (OPR-6), not a proposition.

**Blockchain and redactable structures.** A ledger never forgets, which is where erasure fails (Finck); redactable designs let an editor rewrite history. This log keeps a chain's tamper evidence, is never edited, and never holds erasable content (§2.4, pp. 23 to 25). Row-by-row comparison: B6.2.

Point to: §2.4, pp. 21 to 25; §4.8, p. 66; slides 18 (q-chain) and 28 (q-rival4); <https://trfhimolde.streamlit.app/?p=built>

## B5. Why the method fits: Design Science Research

### B5.1 Hevner (2004) and Peffers (2007) as the thesis uses them

**Hevner et al. (2004)** supply the paradigm. Design science builds and evaluates artefacts (constructs, models, methods, instantiations). Utility is judged against the problem environment; rigour against the knowledge base (§3.1, p. 37).

**Peffers et al. (2007)** supply the six-activity process, mapped onto chapters (§3.2, p. 38):

| Activity | Thesis |
|---|---|
| 1 Problem identification and motivation | Chapters 1 and 2 |
| 2 Objectives of a solution | §1.3: joint satisfaction, accountability kept, auditor-verifiable, fits Norway |
| (inserted) Formal modelling | §3.3: the problem stated as a feasibility question before design |
| 3 Design and development | Chapter 4: model, semantics, propositions, mechanism |
| 4 Demonstration | Chapter 5 |
| 5 Evaluation | Chapters 5 and 6 |
| 6 Communication | The thesis; Chapters 6 and 7 |

The entry point is problem-centred. An earlier iteration went from technology (zero-knowledge SNARKs) to problem; the formal analysis showed that machinery unnecessary, and dropping it "is itself an instance of the design cycle operating as intended" (§3.2, p. 38). Hence the name VERA-SNARK (p. x).

**Why DSR** (§3.1, p. 37). Interviews give description, not a mechanism; a systematic review gives synthesis, but the gap is a missing design; a pure formal-methods study (Feng et al., 2023) gives a model without an artefact.

Point to: §3.1 to §3.3, pp. 37 to 39; slide 19 (q-snark); <https://trfhimolde.streamlit.app/?p=start>

### B5.2 Which artefact types the work produces

The thesis claims two of Hevner's four levels (§3.3, p. 38):

- a **model**: the TRF Model, a formal representation of the domain and its constraints;
- a partial **instantiation**: the sandbox (checker, realism layer, viewer, optional modules), over synthetic data.

It claims no deployed system. The candidate's own reading, not the thesis's: the mechanism specification (§4.8) could also be described as a **method**, and the notation and two semantics as **constructs**. Say this only as a reading, since §3.3 names two levels.

Point to: §3.3, p. 38; §5.2, p. 79; slide 16 (close); <https://trfhimolde.streamlit.app/?p=built>

### B5.3 What was evaluated, and how

The evaluation is analytical (§3.7, p. 44):

- *Internal validity:* do the constraints translate the instruments, are the semantics distinct, do the propositions follow, is the mechanism the witness? Assessed by proof and by the executable checks (B3.9).
- *External validity:* compatibility with verified infrastructure, requirement by requirement in Table 4.1 (p. 74). Weaker than deployment, and not presented as equivalent.
- *Reliability:* determinism; fixed seed 20260915; every command has a recorded output.

In Venable et al.'s (2016) terms, the evaluation is artificial, not naturalistic. Utility, efficacy in operation and acceptance are not evaluated (§6.6, p. 96). The falsifiable part of the Semantics II result is the inclusion-proof check (§5.7, p. 88).

Point to: §3.7, p. 44; Table 4.1, p. 74; §6.6, p. 96; slide 12 (evidence); <https://trfhimolde.streamlit.app/?p=ledger>

### B5.4 Why interviews were designed but not run

Appendix C specifies the instrument: eight experts, two each from data protection, health IT architecture, SPE operation and information logistics; a semi-structured guide; 16 Likert items over utility, regulatory alignment, operational viability and audit integrity (§3.8, p. 46). Interview question seven asks whether Art 68(12) reaches the logs; item A2 asks whether attested destruction suffices (§6.6, p. 97).

It was not run because it would process personal data about identifiable professionals, needing Sikt notification with four to six weeks' lead time, and a revision of the scope, ethics and originality statements, which are accurate as submitted (§3.8, p. 46). It is the first item of future work (§7.5, p. 107).

Point to: §3.8, p. 46; Appendix C, p. 160; §7.5, p. 107; no slide; <https://trfhimolde.streamlit.app/?p=start>

### B5.5 Hevner's seven guidelines mapped to the thesis

The thesis does not tabulate Hevner's seven guidelines. **This is the candidate's own mapping.**

| Guideline (Hevner et al., 2004) | Where the thesis meets it |
|---|---|
| 1 Design as an artefact | TRF Model; mechanism specification; sandbox (Ch 4 to 5) |
| 2 Problem relevance | EHDS collision; Norway's live NCPeH pilot; rules apply 2029 (Ch 1, §6.8) |
| 3 Design evaluation | Proofs; exhaustive search and Z3; 200-record demonstration; Table 4.1 (Ch 5, §4.11) |
| 4 Research contributions | Four bounded contributions (Statement of Contribution, pp. ix to x) |
| 5 Research rigour | Primary legal sources; stated proofs; reproducible code with fixed seed (Ch 3, App A) |
| 6 Design as a search process | Six rival designs tested (§4.10); SNARK design dropped (§3.2) |
| 7 Communication of research | Thesis; NORS 2025 presentation; public app and archive (§1.6, App A) |

Point to: §3.1 to §3.3, pp. 37 to 39; Statement of Contribution, pp. ix to x; slide 16 (close); <https://trfhimolde.streamlit.app/?p=ledger>

## B6. Novelty and the competitors

### B6.1 What is new, and what is borrowed

**New, in the reviewed literature** (Statement of Contribution, p. ix; §2.8, p. 34; §2.10, p. 36):

1. The formal characterisation of a floor, a right and a ceiling acting together on one record, with verifiability as the parameter that decides feasibility.
2. The finding that the conflict lies in an implicit semantic assumption, not in the obligations (§6.9, p. 99).
3. Proposition 3: a ceiling collides only if no longer than the floor, and its anchor decides whether the text shows it.
4. The mechanism specified for the cross-border health audit trail, with its residue analysed and placed on the Norwegian substrate.
5. The information-logistics expression of the problem (§2.10, p. 36).

**Borrowed, with source** (§2.4 to §2.5, pp. 21 to 27):

| Element | Source |
|---|---|
| Compliance as satisfiability, counterexamples as violations | Feng et al. (2023); Arfelt et al. (2019) for GDPR monitoring |
| Hash-chained tamper-evident logs | Schneier & Kelsey (1999) |
| Merkle trees; logarithmic proofs | Merkle (1988); Crosby & Wallach (2009) |
| Public append-only logs, RFC 6962 hashing | Laurie et al. (2013), Certificate Transparency |
| Cryptographic erase; key hierarchies | NIST SP 800-88 Rev. 2; Barker (2020) |
| Deleting by forgetting keys, on deadlines or policies | Boneh & Lipton (1996); Perlman (2005); Geambasu et al. (2009); Cachin et al. (2013) |
| Dynamic accumulators (specified, not built) | Camenisch & Lysyanskaya (2002) |

**Not claimed** (p. x): no new primitive, no new formal method, no "first-ever" framework, no deployment, no proof of key destruction.

Point to: Statement of Contribution, pp. ix to x; §2.8, pp. 32 to 34; §2.10, p. 36; slide 16 (close); <https://trfhimolde.streamlit.app/?p=ledger>

### B6.2 The rival designs compared

| Rival | What it gives | Why it fails here | How TRF differs |
|---|---|---|---|
| Do nothing: rely on Art 17(3)(b) (Rival 1) | Floor met | Exemption covers only what is necessary; Art 68(12) has none (p. 70) | Keeps only what necessity protects |
| Anonymise the record (Rival 2) | C2 and C3 met | Destroys accountability; Art 73(1)(e) requires identifiable logs. Breaks C1 (p. 70) | Keeps accessor fields identifiable |
| Pseudonymise only (§1.2) | Looks like a middle way | Reversible, so still personal data (Recital 26); erasure not met (§1.2, p. 3) | Deletes payload, key, salt; residue stated as pseudonymised |
| Minimise at capture (Rival 3) | Less to erase; compatible | ITI-55 puts the query in the audit message, so the standard, not the deployment, sets the payload (p. 71) | Works alongside it; handles what must be captured |
| Delete the whole entry and log it (Rival 4) | C2, C3; a trace | Fails C1: no commitment, so (ii) fails, by definition (p. 71) | Conceded "close to an equivalent design" for cross-border; edge is the bound, attributed entry and substitution detection; real work in SPE logs |
| Recoverable encrypted copies, DePaul (Rival 5) | Right for two floors with a known purge date | Keyed copies stay personal data: what the ceiling forbids (pp. 71 to 72) | Destroys recoverability, keeps accountability |
| Move the logs out at permit closure (Rival 6) | Meets the ceiling; accepted for Corollary 1.2 | Leaves the right untouched (Proposition 4); moves subject fields to a second controller (p. 72) | Meets ceiling and right in place |
| Crypto-shredding pattern (VeritasChain, 2026) | Per-subject key destroyed on request | Bilateral; asserted; no model or verifiability semantics (§2.4, p. 25) | Adds ceiling, model, semantics, checkable record |
| Redactable blockchain, chameleon hash, redactable or sanitizable signatures | Erasure inside an integrity structure | Weakens binding; an editor can rewrite history (§2.4, p. 23) | Log never edited; erasable content never enters it |
| Blockchain audit log (KONFIDO) | Immutable cross-border traceability | Immutability against erasure left unresolved; SGX hardware dependency (§2.4, p. 21) | Software only; personal data kept off the log |
| SNARK designs (ZK-EHR, Albalwy 2026; early VERA-SNARK) | Credential proofs hiding identity | Access control in one jurisdiction, not retention (p. 22); unnecessary here (§3.2) | Commitments and a logged registry suffice; ZK only for proving completeness of invalidation (§7.5) |
| Access control (SecuPi, 2025) | Restricts who may read | Data remain, so no ceiling is met (p. 95) | Makes data unreadable |
| Ledger crypto-erasure SoK (Aikebaier, 2026, preprint) | Erasure-side security notion | Excludes retention law by scope (p. 24) | Treats all three; its fifth open problem |

Point to: §4.10, pp. 70 to 73; §2.4, pp. 21 to 25; Table 2.1, p. 32; slides 6 (fixes), 18 (q-chain), 28 (q-rival4) and 30 (q-props34); <https://trfhimolde.streamlit.app/?p=witness&r=3&m=116>

### B6.3 The two strongest novelty attacks

*"This is framing, not a contribution."* Reply: "It is a contribution of framing and feasibility, and the Statement of Contribution says so on its first line (p. ix). The framing has teeth: Proposition 1 rules out a whole class of designs, Proposition 3 gives a drafting test that corrected my own expectation on §17, and the mechanism follows from the proof."

*"DePaul already did key-lifecycle reconciliation."* Reply: "It reaches the same engineering insight, and the thesis credits it. The decisive difference is direction: it meets a floor by keeping recoverable copies, which a ceiling forbids. It also lacks verifiability semantics, and its purge date is fixed in advance, whereas a request comes when the patient chooses (§2.4, p. 24)."

Point to: Statement of Contribution, p. ix; §2.4, p. 24; §4.10, pp. 71 to 72; slide 28 (q-rival4); <https://trfhimolde.streamlit.app/?p=anchor>


\newpage

# Part C. Question bank

For: Arshad Akhtar Abbasia (Tiger). Examiners: Prof. João Ferreira (supervisor) and Joel Curado (external). Thirty minutes of questions.

### How to use this part

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

## 1. Motivation and timing

#### Q1. [Either] "Why this problem, and why now? The rules do not apply until 2029."

**Short answer.** The timing is the argument. The detailed rules for research environments are due in March 2027 and apply from March 2029, and Norway's cross-border system is already in pilot, so the clash can be settled in the specification rather than patched after infrastructure hardens.

**Full answer.** Regulation (EU) 2025/327 entered into force on 26 March 2025 and applies generally from 26 March 2027 (Art 105). The secondary-use provisions of Chapter IV, which contain both the Art 68(12) ceiling and the Art 73(1)(e) floor, apply from 26 March 2029. Art 73(5) requires the Commission to lay down Secure Processing Environment requirements by implementing act by 26 March 2027. So the collision is not yet operative, and, because the acts are unwritten, nobody has yet decided how it is handled. The TEHDAS2 specification for these environments (D7.4, OPR-6) asks operators to balance deletion against "applicable legal obligations" and does not say how. A framework that arrives after infrastructure has hardened is archaeology; one that arrives while specifications are drafted can shape defaults. On the primary-use side Norway's NCPeH is live in pilot at the emergency clinics in Bodø and Stjørdal, so the audit stream is beginning now, though no relevant patient had presented when the Directorate last reported. The EDPB's coordinated enforcement report on Art 17 (18 February 2026, 32 authorities, 764 controllers) itself names the definition and implementation of retention periods as an unsettled difficulty.

**Worked example.** Record 3: a clinician HP-003 (via NCP FI) looks up a patient in month 11; the illustrative floor runs to month 131; an erasure request in month 115 sets the payload deadline at 116.

**Concede and hold.** Concede that nothing here is operative today and that for Norway the dates depend on incorporation of the Regulation into the EEA Agreement (the thesis says it is being processed through the EEA Joint Committee) [Under scrutiny for EEA incorporation per the EFTA register, 26 Nov 2026.]. Hold: lead with "it arrives while the specifications are open", not "it applies in 2029".

**Point to.** §1.1 p. 1; §1.4 p. 7; §2.2 pp. 15 to 16; §6.8 p. 98; §7.6 p. 108. Slides 5, 15, 31. App ?p=norway.

#### Q2. [Either] "Is this a real problem today, who would adopt it, and what does it cost?"

**Short answer.** Not yet operative, and not measured. Per-record keys are a real burden. The cheapest step to adopt is logging every invalidation as a first-class event, which costs little.

**Full answer.** SecuPi (2025) argues that cryptographic erasure adds operational complexity and that auditable key management adds overhead. The thesis calls this "substantially correct on its own terms" (§6.4). Three things bound the burden without denying it. First, it falls on audit records, not on clinical stores: the mechanism sits at the sixth step of the MyHealth@EU flow or at a Secure Processing Environment's logging boundary, the smaller surface. Second, keys for invalidated records are destroyed, so the live registry shrinks as invalidations accumulate. Third, the verification cost grows slowly: an inclusion proof needs about log2 n hashes, some thirty for a billion entries. The critique's alternative, policy-based access control, governs who may read data and does not make it cease to exist, so it cannot meet Art 68(12) and offers nothing against Corollary 1.2. Per-record keys are the simplest construction, not the only one: a key-share design with one share per subject and one per permit has a registry that grows with subjects and permits (Cachin et al., 2013), and is not implemented. The accumulator layer scales worst and is dispensable: a scan of the registry gives the same answer without succinctness.

**Worked example.** In the envelope module 138 of 200 keys are destroyed at their invalidation months and 62 remain live: the live registry is smaller than the cumulative record count.

**Concede and hold.** Concede there is no performance measurement and no claim of one (§6.5). Hold: the burden is bounded and auditable, whereas residual copies under plaintext deletion are unbounded and uninspectable; and the invalidation entry alone is adoptable without the rest (§6.8).

**Point to.** §6.4 p. 95; §6.5 p. 96; §6.8 p. 98; §4.8 p. 63. Slides 15, 31. App ?p=norway.

#### Q3. [Ferreira] "State your research question and sub-questions, and show me where each is answered."

**Short answer.** How can a verifiable crypto-erasure mechanism reconcile the conflicting retention requirements of cross-border health data exchange under the EHDS while preserving audit integrity in a Norwegian context? SQ1 is where they conflict and when all can hold; SQ2 is whether invalidation can satisfy all three; SQ3 is how it fits Norwegian infrastructure. All three are answered by name in §7.1.

**Full answer.** The primary question is in §1.3 (p. 6). SQ1 asks for the precise points of conflict and the formal conditions of joint satisfiability. It is answered by Proposition 1 with Corollaries 1.1 and 1.2 and by Proposition 3: the regimes conflict wherever an erasure deadline, or a ceiling that reaches the record, falls inside the retention window, and under plaintext verifiability they are then unsatisfiable; a ceiling can collide with a floor only if it is no longer than the floor, and its anchor decides whether the text shows it. The collision with no request holds on the broad reading of Art 68(12) only. SQ2 asks whether an invalidation mechanism can satisfy all three across floors of differing length: yes, within the model, by Proposition 2 and Corollary 2.2, witnessed in Chapter 5, with cryptography serving the copies the store cannot delete at once. SQ3 asks about integration with Norwegian infrastructure: the mechanism attaches at the audit-repository step of the MyHealth@EU flow and at the access-logging boundary of a Secure Processing Environment, adding no requirement of a new kind to the national criteria, a compatibility by specification (Table 4.1), not by deployment. The overall answer is hedged on purpose: the regimes can be reconciled within the model without amending any instrument, and whether that holds in law turns on the two authority questions of §7.4.

**Worked example.** SQ1 on record 3 (floor against right) and on record 100 (floor against ceiling); SQ2 on the same two records under Reading II.

**Concede and hold.** Concede the earlier draft of §7.1 stated the answer without the authority caveat; the submitted text carries it. Hold: the answer is "within the model, and lawful only if two authority questions go the right way".

**Point to.** §1.3 p. 6; §7.1 p. 103; Table 4.1 p. 74. Slide 2. App ?p=start.

---

## 2. Method (design science, evaluation, why not interviews)

#### Q4. [Ferreira] "Which design science framework did you use, what are the artefacts, and how did you evaluate them?"

**Short answer.** Hevner et al. (2004) for the paradigm and artefact types, Peffers et al. (2007) for the six-activity process. The artefacts are a model (the TRF Model) and a partial instantiation (the sandbox). Evaluation is by argument and executable check, not in the field.

**Full answer.** DSR fits because the problem is real (binding instruments on live infrastructure), unsolved (no reviewed work models the tri-lateral conflict or derives a mechanism from it), admits an artefact as its answer (a design), and has a tractable evaluation (a claim about logical consistency, not deployed performance). The six activities map onto the chapters: problem (Ch 1 to 2), objectives (§1.3), design and development (Ch 4), demonstration (Ch 5), evaluation (Ch 5 to 6), communication (Ch 6 to 7). The thesis adds one step: formal modelling between objectives and design, so that the mechanism is derived as the constructive answer to a satisfiability question rather than assumed and justified afterwards. It uses a lighter formalism than the temporal-logic and SMT apparatus of Feng et al. (2023): one binary variable per record, in the constraint-modelling style of operations research, because the conflict turns on one semantic question and because an author trained in logistics modelling must be able to own and defend the machinery. The variant is "specification and demonstration". Evaluation (§3.7) is on internal validity, compatibility with verified infrastructure (Table 4.1) and determinism. §6.6 classifies it as artificial, not naturalistic (Venable et al., 2016).

The thesis does not tabulate Hevner's seven guidelines, so this oral mapping is yours: G1 artefact (model, mechanism, checker); G2 relevance (the EHDS collision, Norway's pilot); G3 evaluation (proofs, exhaustive search, Z3, the 200-record run); G4 contribution (the verifiability parameter, Proposition 3, the mechanism); G5 rigour (primary legal sources, reproducible code on Zenodo); G6 design as search (six rival designs in §4.10, red-team rounds); G7 communication (thesis, NORS 2025, app, archive).

**Worked example.** The SNARK design was dropped when the formal step showed commitments and a logged registry suffice (§3.2): the cycle working as intended.

**Concede and hold.** Concede utility and acceptance are not evaluated; the expert panel (Appendix C) is designed, not run. Hold: for a claim about logical consistency, analytic and executable evaluation is the proportionate one.

**Point to.** §3.1 to §3.3 pp. 37 to 40; §3.7 p. 44; §6.6 p. 96; Appendix C p. 160. Slide 19. App ?p=ledger.

#### Q5. [Either] "Why not a survey or interviews? And what about ethics?"

**Short answer.** Interviews give opinions, not a mechanism, and the central questions are legal, so only an authority can settle them. I designed a practitioner panel (Appendix C) but did not run it: it needs Sikt notification and four to six weeks.

**Full answer.** §3.1 rejects three alternatives. An interview study would have produced descriptive knowledge but no mechanism and needed ethical clearance and access disproportionate to the contribution. A systematic review would consolidate knowledge when the gap is a missing design. A pure formal-methods study would give the model without the artefact and need proof-assistant expertise outside the programme. Appendix C specifies an eight-person panel (two each from data protection, health IT architecture, SPE operation, information logistics), a semi-structured guide and a sixteen-item questionnaire across utility, regulatory alignment, operational viability and audit integrity. It would process personal data about identifiable professionals, so it needs notification to Sikt and a revision of the no-human-participants statements before it runs. On ethics as submitted: no human participants and no real patient data; the only personal data are correspondence with public authorities, in which officials are named in their official capacity (§3.9). The thesis also discloses that an earlier draft, discarded in May 2026, contained citations to works that do not exist and an ethics statement that was never true; the present one is accurate.

**Worked example.** Appendix D reproduces the Helsedirektoratet reply with its author's permission, which is the one place a named official appears.

**Concede and hold.** Concede the evaluation is thin on utility and acceptance (§6.6). Hold: the panel is the first thing to run, and it is designed so the ethics wording changes only at that point.

**Point to.** §3.1 p. 37; §3.8 p. 46; §3.9 p. 46; §7.5 p. 107; Appendix C p. 160; Declaration p. xi.

#### Q6. [Either] "You fixed the success criterion as 'Proposition 2 holds', then admit it holds by construction. What is falsifiable?"

**Short answer.** The infeasibility claim is falsifiable; the feasibility claim is constructive and is verified rather than tested. In the code the falsifiable part is the inclusion-proof check, and three tamper tests show it can fail.

**Full answer.** §3.3 now says it directly: the infeasibility claim is falsifiable, the feasibility claim is verified, not tested (§4.7). Proposition 1 could have failed on the checker: if any record satisfying a disjunct had a feasible assignment, the exhaustive search or Z3 would have found it, and the converse (no deadline inside the window means feasible) is exercised by the control case. The Semantics II zero is different: C2 and C3 follow from the invalidation month, because readability in the checker is derived from that month, so zero violations holds by construction (§5.7, §5.8). What can fail is condition (i): each access event, invalidation and subject-link removal is an entry in a Merkle log and V^II requires an inclusion proof against the root. Altering record 100's actor, its invalidation ground, or record 3's patient link each makes V^II false, and restoring them makes it true. Before the salted subject-link commitment was added a changed link went undetected, which is why the third test exists. FEDS classification (Venable et al., 2016): ex ante, artificial, formative.

**Worked example.** `python3 trf_checker.py`: "tamper test, rid=100 actor altered: V_II=False (access entry fails its inclusion proof)"; after restoring all three, V_II=True.

**Concede and hold.** Concede the evaluation is analytical and the evaluation is circular in the sense that the success criterion is fixed by the model. Hold: the thesis says so in §4.7, §5.8 and §6.6, and the weight of the contribution is not in the check.

**Point to.** §3.3 p. 38; §4.7 p. 62; §5.7 p. 88; §5.8 p. 89; §6.6 p. 96. Slides 12, 24. App ?p=run.

---

## 3. Legal reading

#### Q7. [Either] "Walk me through the three obligations. Which articles, what do they say, and where exactly is the conflict?"

**Short answer.** A floor says keep the record: Art 73(1)(e) EHDS for research environments (at least one year); for the cross-border repository a period the specifications leave to national law (six years in the Norwegian pilot). A right says erase on request (Art 17 GDPR, one month under Art 12(3)). A ceiling says research data must be gone six months after permit expiry (Art 68(12) EHDS). They collide if "verifiable" means "readable".

**Full answer.** The floor. Art 73(1)(e) requires Secure Processing Environments to keep "identifiable logs of access to and activities in the secure processing environment for the period necessary to verify and audit all processing operations in that environment; logs of access shall be kept for at least one year". For the MyHealth@EU audit repository no eHDSI instrument fixes a period: the IHE ATNA profile prescribes none, the secondary literature reports ten years (illustrative here), and Helsedirektoratet reports six years for the pilot. Once Art 9 EHDS applies, Art 9(2) gives patients information on access for at least three years from each access, a binding 36 months for the record the information is produced from. The right. Art 17(1) GDPR requires erasure "without undue delay" where a condition applies; Art 12(3) allows one month, extendable by two. The ceiling. Art 68(12): "the electronic health data within the secure processing environment shall be deleted within six months of the expiry of the data permit". The conflict is not between the obligations as such. C1 asks for the record to remain verifiable; C2 and C3 ask for the payload to stop being accessible. If verifiable means accessible, the two bounds meet in the same month with opposite demands. If it means accountable, they do not.

**Worked example.** Record 3: floor to month 131, deadline 116. Record 100: ceiling month 16, floor to month 19.

**Concede and hold.** Concede the ten-year floor is a literature figure and the six-year pilot floor is a controller decision, not a statute. Hold: Corollary 2.2 makes every result independent of the floor value.

**Point to.** §1.1 p. 2; §4.3 p. 53; §4.4 p. 54; §2.3 pp. 17 to 18. Slides 4, 5, 7. App ?p=start.

#### Q8. [Either] "Article 17(3)(b) already exempts audit retention. What conflict is left? And what about 17(3)(c) and (d)?"

**Short answer.** Half of that I concede: 17(3)(b) lets necessary retention survive. It does not say what is necessary, and with Art 5(1)(c) it protects only what the obligation needs. I argue accountability needs who, when, on what basis and outcome, plus the patient link where Art 9 applies, not the payload.

**Full answer.** The exemption has three conditions that do the work. It needs a legal obligation imposed by Union or Member State law; it protects only processing necessary for that obligation; and minimisation (Art 5(1)(c)) limits what may be kept. §4.2 argues the purpose of an audit record is accountability: that an access occurred, by whom, when, under what authority, with what result. That is served by the accessor fields and a binding commitment, and not by continued readable access to the demographic query. So a request reaches the payload, and Proposition 1's request-driven case follows. Two limits. First, if a supervisory authority holds part of the payload necessary, Corollary 2.3 applies: keep that part with the accessor fields. Second, the six-year pilot floor is a decision by Helsedirektoratet as controller; unless a national legal basis is identified it is a policy floor, so before Art 9 applies on 26 March 2029, and beyond 36 months after, keeping the patient link against a request has no secure 17(3)(b) basis. That is a finding for the controller, not a limit on the model, since a lower floor removes collisions and creates none. Art 17(3)(c) (public interest in public health) and 17(3)(d) (research) narrow C2 further in the same direction; for the SPE's own logs, which serve Art 73(1)(e) rather than the research, the exemption that applies is 17(3)(b). Not in the thesis: EDPB draft Guidelines 1/2026 on scientific research treat 17(3)(d) as case by case, not blanket [From RED_TEAM.md, not in the thesis.].

**Worked example.** On record 3 the request in month 115 reaches the payload; the accessor fields and patient link stay through the floor because Art 9(2) EHDS needs them.

**Concede and hold.** Concede the argument is mine and unconfirmed by any authority; Datatilsynet has the question. Hold: if the exemption covered the payload, C2 would not reach it and only the ceiling case would remain (§4.6).

**Point to.** §4.2 pp. 49 to 51; §4.4 p. 54; §6.2 p. 92; §7.4 p. 106. Slides 4, 6, 22. 

#### Q9. [Either] "Does Article 68(12) really reach the environment's own access logs? That reading is a guess, and without it your headline collapses."

**Short answer.** The reading is contestable and I state it as a condition. If it falls I lose Corollary 1.2 and one branch of Corollary 2.3, and nothing else. Propositions 1 to 4, the mechanism and the verifiability semantics stand.

**Full answer.** Three readings are in §4.6. Broad: the provision's scope is set by location ("within the secure processing environment"), not by provenance, so it does not say "the data made available under the data permit". But its object is electronic health data, so a log entry that only records a researcher opening a dataset concerns the researcher, not anyone's health, and is not reached. An entry at patient-record granularity reveals cohort membership, which is data concerning health, so it is reached; for dataset-granularity logs only where the retained activity content is itself health data. Narrow: the provision sits in the data-permit article beside permit duration and storage fees and concerns the permit dataset. Harmonising: it reaches the logs but yields to Art 73(1)(e) as an exception mandated by law, and the TEHDAS2 specification points that way ("exceptions mandated by applicable law"). Under the harmonising reading the contradiction does not arise, but the question moves to what the floor requires: if plaintext, subject health data stay for the whole floor; if accountability, only accessor fields stay and the rest goes at the ceiling, which is the partition Proposition 2 already applies. So even then the weight falls on the necessity analysis. On the narrow reading, Corollary 1.2 lapses with the single record bound by all three regimes at once; Proposition 1 is untouched because its first disjunct concerns erasure requests, and identifiable logs remain personal data within Art 17.

**Worked example.** In the generated set, on the narrow reading 44 ceiling-only collisions lapse (the 39 witnesses and 5 records whose requests fall outside the window); 9 SPE records remain (4 colliding with C2 only, 5 also with C3; 22 SPE records received requests). With the ceiling excluded the sensitivity script gives 46 violating records, all request-driven (not in the thesis; release 1.3.4).

**Concede and hold.** Concede the reading is not settled by any authority or court. Do not use the older red-team line that the three-way collision survives the narrow reading: §4.6 now concedes it does not. Do not say the Commission will clarify it. Hold: the dependency is confined, and the EHDS-side question is not yet asked.

**Point to.** §4.6 pp. 58 to 59; §6.2 p. 93; §7.4 p. 106; §5.4 p. 84. Slide 21. App ?p=witness&r=100&m=16.

#### Q10. [Either] "Semantics II is your own definition. Why would a regulator accept it? You are a logistics student issuing legal interpretations."

**Short answer.** No regulator has said so and I do not pretend otherwise. I argue it from two points: the exemption protects only what is necessary, and minimisation says keep no more than the purpose needs. The thesis proves feasibility under the definition and labels it a reading. The question is put to Datatilsynet.

**Full answer.** §6.2 calls this the most serious objection and it is not technical. Nothing says an invalidated record satisfies a retention obligation. The argument runs: Art 17(3)(b) protects only necessary processing; Art 5(1)(c) requires no more than the purpose demands; the accountability purpose is who, when, on what basis, with what outcome; therefore readable payload is beyond what necessity protects; Datatilsynet's guidance places exactly that balancing on the controller. If an authority reads "identifiable logs" in Art 73(1)(e) as logs whose subject matter remains readable, Proposition 2 stays true of the model and becomes practically inert. Why that outcome is unlikely, as reasons rather than reassurance: the alternatives are worse (on the broad reading the only way to honour both articles under plaintext is to export the logs, which moves the subject fields to a second controller and leaves the right untouched, Proposition 4; for cross-border records there is no export route at all); the regulatory direction is compatible (EDPB Guidelines 02/2025 para 51: key deletion makes data unintelligible, yet encrypted data remain personal data; para 125: erasure requires the data erased or anonymised); and a specification that asks for a balance (TEHDAS2 OPR-6) has not adopted plaintext verifiability. The question is decidable by asking. The EDPB does not endorse Semantics II: the further condition that the controller document its threat model is Aikebaier's (2026) interpretation, not the Board's.

**Worked example.** After invalidation record 100 still shows who (R-008), under which permit (DP-015), when, a commitment, and the invalidation entry (month 16, ground Art 68(12)); only the payload is gone.

**Concede and hold.** Concede it is argued and unconfirmed. Hold: an unfavourable answer "refutes them cleanly and identifies precisely what would have to change" (§7.4), and either outcome is worth more than the present uncertainty.

**Point to.** §4.2 p. 49; §6.2 pp. 92 to 93; §7.4 p. 106. Slides 8, 14, 22. 

#### Q11. [Either] "Is what remains of the patient's record anonymous? Does your residue escape the GDPR?"

**Short answer.** No. It identifies the accessor and is pseudonymised as to the patient, so it is pseudonymised, not anonymous, until a terminal transition that is specified and not implemented. The test I rely on is erasure, not anonymisation, and the store meets it by deletion.

**Full answer.** Identifiability turns on whether anyone can re-identify by means reasonably likely to be used. Datatilsynet (2015) holds that data are not anonymous while any key or linkage capable of re-identification is kept. The EDPB's draft Guidelines 02/2026 set the same bar at Union level with a three-part test (isolation, linkage, inference) and hold that encryption is by nature reversible and is not anonymisation. The Court of Justice (EDPS v SRB, C-413/23 P, 4 September 2025, paras 73 and 76 to 77) holds that pseudonymised data are not personal data in all cases and for every person: possibly not for a recipient who cannot lift the pseudonymisation, but still personal data for the controller who holds the additional information. The repository controller holds the subject link and the accessor identity, so for it the residue is personal data. Why the mechanism is still defensible: the legal test is erasure, and at invalidation the ciphertext, key and salt are deleted from the store. Key destruction is relied on only for copies that cannot be deleted at once, a bounded residue unreadable from invalidation and personal data until it leaves by rotation. The salted commitment stops anyone confirming a guessed payload. The terminal transition after the floor destroys identifying metadata and aims at a non-identifiable remainder, but the invalidation entries carry the record identifier and authorising actor, which must be generalised or destroyed too, and whether the remainder resists the three-part test is for the documented threat model.

**Worked example.** Record 100 after invalidation still carries actor R-008 and permit DP-015, as Art 73(1)(e) requires identifiable logs.

**Concede and hold.** Any claim of anonymisation "would be false" (§4.9). Hold: the claim is erasure of the payload, with an honestly bounded residue.

**Point to.** §4.8 p. 67; §4.9 pp. 68 to 69. Slide 27. App ?p=witness&r=100&m=19.

#### Q12. [Either] "Why do you keep the patient link after an erasure request? And what of the clinician's own Article 17 right?"

**Short answer.** The link is not payload; it is the other half of the accountability question. Art 9(2) EHDS gives patients information on who accessed their data for at least three years, and that cannot be produced from a record that no longer says whose data were accessed. The clinician's own right does not empty the log either, for the same necessity reason.

**Full answer.** Art 9(1) to (2) EHDS gives natural persons information on the provider who accessed their data, the date and time, and which data, available for at least three years from each access. For the controller that must provide it, keeping the link is necessary for compliance with a legal obligation within Art 17(3)(b), so a request reaches the payload but not the link, for the Art 9(2) period and once Art 9 applies. The argument has limits that the thesis states. Art 9 is framed around the health professional access service, so whether it binds the controller of a foreign NCPeH's audit repository, and covers every cross-border event, is a subsidiary premise without authority. Beyond the 36 months the link is kept for the rest of the floor only on whatever national provision fixes the repository's retention, which the thesis has not identified, so its retention after a request is as contestable as the floor. In an SPE, Art 9 does not apply, and the link is kept after a request until the ceiling only if auditing "all processing operations" needs it. The accessor's fields are the clinician's or researcher's own personal data; their Art 17 right is met by the same necessity reasoning (Art 73(1)(e); for cross-border records Art 9(2) and national law), and a period an operator sets without a Union or Member State legal basis would not engage the exemption. What necessity does not protect is not kept: the accessor fields are destroyed at the terminal transition.

**Worked example.** Record 3 keeps its patient link through the floor; record 100 loses its link at month 16 and the removal is a logged entry.

**Concede and hold.** Two of the four subsidiary premises (§3.7) are exactly these. Hold: they bound specific results, not the model.

**Point to.** §4.2 pp. 50 to 51; §3.7 p. 45; §7.4 p. 106. Slides 10, 11.

#### Q13. [Either] "Norway is not an EU member. Does the EHDS even apply, and who is the controller?"

**Short answer.** Not directly. Norway is an EEA state, the Regulation is being processed for incorporation through the EEA Joint Committee, and the dates for Norway depend on that. The controller of a national contact point's audit repository is that point's own national authority.

**Full answer.** The thesis is explicit (§2.2, §1.4): as an EEA member rather than an EU Member State, Norway receives the EHDS Regulation only on incorporation into the EEA Agreement, and Helsedirektoratet delivered its formal impact and gap analysis on 11 April 2025. So the Norwegian instrument date for Arts 68 and 73 is not the Union date. The analysis is nonetheless coherent for two reasons: the model takes the floor and ceiling as parameters, so an incorporation date changes when the constraints bind, not whether the structure exists; and the cross-border audit records already exist in the live pilot under the eHDSI framework. On the controller: Commission Implementing Decision (EU) 2019/1765, which the thesis states is incorporated into the EEA Agreement, makes the participating states, through their national authorities or designated bodies, the controllers of data they process through the infrastructure, with the Commission a processor with no access to patients' personal data (Art 7). The Art 17 request lands on that authority, for Norway the operator of the NCPeH (Helsedirektoratet is data controller per its own reply).

**Worked example.** Larsen's reply: "Hdir er dataansvarlig og vil ta den beslutningen" (Appendix D).

**Concede and hold.** The reviewer notes said to confirm the EEA incorporation of 2019/1765 at the viva: bring the source if asked [Since submission: EHDS Regulation is under scrutiny for EEA incorporation per the EFTA register (26 Nov 2026); say "being processed".]. Hold: nothing in the propositions depends on the date.

**Point to.** §1.4 p. 7; §2.2 pp. 15 to 16; §4.2 p. 51; Appendix D p. 168. Slides 14, 15.

---

## 4. Model and propositions (compact; the full derivations are in Part B)

#### Q14. [Either] "Walk me through the variables and the three constraints. Why one binary variable, why months, and what does 'tri-lateral' mean?"

**Short answer.** For each record and month there is one yes-or-no question: can the payload still be read? That is alpha. Everything else is a clock: when the record was made, how long it must be kept, when a request arrives, when a permit ends. "Tri-lateral" means three kinds of constraint (floor, right, ceiling), not three laws. Full definitions: Part B, section B2.

**Full answer.** A record a has a creation month t(a), a floor F(a), a pathway sigma(a) (primary or secondary), metadata split into accessor fields and subject fields (the patient link), a payload p(a), a commitment c(a), a key k(a). Events: an erasure request t_r(a) (infinite if none), the response period delta (1 month, 3 if extended, Art 12(3) GDPR), a permit expiry t_pi(a), an optional payload period P(a). States: alpha(a,t) payload readable; beta(a,t) patient link readable; V(a,t) verifiable. The reach indicator rho(a) is 1 where the ceiling reaches the record. The invalidation month is t^I = min(t_r + delta, t_pi + 6, t + P). C1 says V = 1 for every month t(a) to t(a) + F(a), a closed window of F + 1 months, conservative for "at least". C2 says alpha = 0 from t_r + delta. C3, for secondary records with rho = 1, says alpha = 0 (and beta = 0 where the link is health data) from t_pi + 6. C1 is a lower bound on a property; C2 and C3 are upper bounds on accessibility. Whether they clash depends on whether V is defined in terms of alpha. One variable is deliberate: it isolates the one question the conflict turns on, and it is conservative, since a mechanism that satisfies the constraints for a whole payload satisfies them for any part. "Tri-lateral" counts constraint types: the floor is one parameterised constraint with two instances, so the model is indifferent to the number of floors (Corollary 2.2). Months are the unit because every instrument speaks in months or years.

**Worked example.** Record 3: t = 11, F = 120, t_r = 115, so the window is months 11 to 131 and t^I = 116. Record 100: t = 7, F = 12, t_pi = 10, so the window is 7 to 19 and t^I = 16.

**Concede and hold.** Discretisation can create boundary artefacts: C2 binds from the start of month t_r + delta, stricter than "one month from receipt". Edge cases are handled: requests arrive at or after creation, delta is at least 1, arithmetic is over the naturals plus infinity, and a record written at or after its own deadline never holds a readable payload. The model cannot express field-level redaction (eighth limitation); Corollary 2.3 adds a variable per payload part for the one case where it matters.

**Point to.** §4.3 pp. 51 to 53; §4.4 p. 54; §3.7 p. 45; Nomenclature p. xii. Slide 7. App ?p=start.

#### Q15. [Either] "Proposition 1 is trivial, and Semantics I is a straw man nobody holds. What does it earn?"

**Short answer.** Yes, it is short, and I say so: a pigeonhole on one yes-or-no variable. What it earns is a negative result about deployed designs, and it pins down exactly which records collide. Semantics I is not invented: the reference gateway behaves that way. See Part B, section B3.1.

**Full answer.** Statement: under Semantics I (V = alpha) the system {C1, C2, C3} is infeasible for any record with t_r + delta <= t + F, or with t_pi + 6 <= t + F where the ceiling reaches the record. Proof: take t* the deadline month; it lies inside the window, so C1 needs alpha = 1 there while C2 or C3 needs alpha = 0. The converse is exact: if neither disjunct holds, keep alpha = 1 through the window and 0 after, and the system is feasible. So the proposition is a characterisation, which is what the control case in the exhaustive search exercises. It earns three things. It marks as unworkable any design that keeps the payload readable for the length of the floor wherever a deadline falls inside it. It makes the collision locatable to a month (Corollary 1.1: at a 72-month floor a request in any of the 72 months from creation collides; at 120 months, in all but the last month). And it shows that some departure from readable-verifiability is unavoidable, so the real question is which departure is defensible, which is §4.2. On straw man: no instrument states Semantics I, but in the 2017 OpenNCP source the audit repository stored every received audit message whole in a database column, kept the patient identifier in a readable column and the participant-object query in another, refused to modify a stored message, and had no scheduled purge logic; the schema deployed with OpenNCP 9.1.0 in 2026 keeps the same columns. Whether other deployments configure retention differently was not inspected.

**Worked example.** Record 3: t* = 116 <= 131, infeasible. Record 38: created month 10, request month 138, deadline 139 is later than the window's last month 130, so it is feasible: the one cross-border request outside its window (record number 38 and "38 requests" are a coincidence).

**Concede and hold.** The propositions are "stated as propositions rather than theorems, because their proofs are short once the semantics are fixed". Propositions 1 to 3 are proved informally; none is machine-checked. Hold: the weight lies in the necessity analysis (§4.2) and the mechanism, which the abstract says.

**Point to.** §4.5 pp. 55 to 56; §4.6 p. 57; §4.7 p. 62; §5.3 p. 83. Slides 8, 9, 24. App ?p=propositions.

#### Q16. [Either] "Explain the collision that needs no erasure request. Where does 'half of research logs' come from?"

**Short answer.** In a research environment the same regulation says keep identifiable access logs for a year (Art 73(1)(e)) and delete the environment's health data six months after the permit ends (Art 68(12)). If a log written near a permit's end counts as health data, the two overlap and nobody asked for anything. It is conditional on the broad reading. See Part B, section B3.3.

**Full answer.** For SPE logs F = 12 and sigma = secondary. If t_pi + 6 <= t + 12, that is, the permit expires within six months of the entry, then C1 and C3 are contradictory at t* = t_pi + 6 under Semantics I, provided C3 reaches the record. The corollary also assumes the activity content, not only the subject fields, is data concerning health; were it not, Semantics I could keep the payload readable and delete only the link, and no collision would arise. For patient-level activity (which records and variables a researcher touched) the thesis states the premise rather than deriving it. The "half" is a property of the generator: permits are drawn uniformly 1 to 12 months, so about half fall within six months of the entry. Over a five-year permit with the remaining duration uniform, the rate is about 6 over the maximum permit length, about one in ten; but the structural fact does not depend on the distribution: any entry written in the last six months of a permit has a floor that outlasts its ceiling.

**Worked example.** Record 100: created month 7, permit expires month 10, ceiling month 16, floor to 19; months 16 to 19 collide. Contrast record 102: created month 5, permit expires month 12, ceiling month 18, floor ends month 17: clear by one month. Of 78 SPE records with no request, 39 collide.

**Concede and hold.** The frequency is a generator output and no frequency is claimed; the corollary asserts existence, not frequency. It holds only on the broad reading (Q9). Hold: it needs no data-subject action and involves no deployment baseline; it is internal to Regulation 2025/327 where it holds.

**Point to.** §4.6 pp. 57 to 59; §5.4 pp. 84 to 85; Figure 5.2 p. 85. Slides 5, 21, 23. App ?p=witness&r=100&m=16.

#### Q17. [Either] "You defined Semantics II in full knowledge of the trajectory that satisfies it. What does Proposition 2 prove?"

**Short answer.** Little mathematically, and the thesis says so: it is a verification, not a discovery. The claim is that Semantics II is a defensible reading of the law, argued in §4.2. The proof is the build sheet for the mechanism. See Part B, section B3.5.

**Full answer.** Proposition 2: under Semantics II the system is satisfiable for every record, every arrival pattern of requests and permit expiries, and every floor. The proof is constructive. Let t^I = min(t_r + delta, t_pi + 6, t + P). Before t^I keep alpha = 1 with everything retained. At t^I destroy the key; for SPE logs at the ceiling remove the subject fields; append an invalidation entry (month, legal ground, authorising actor, a hash of the key's identifier); keep the accessor fields and the commitment. After t^I alpha = 0. C2 and C3 hold because t^I is at most each deadline. C1 holds because no step touches the accessor fields or commitment and condition (iii) is met by the entry. Corollary 2.1: no coordination between the erasure process and the retention process, and no foresight at creation. Corollary 2.2: F is arbitrary, so 120, 72, 36 and 12 months are covered at once. Corollary 2.3: if auditing needs part of the payload, keep that part with the accessor fields; it satisfies C1 and C2 (via 17(3)(b)) and C3 unless that part is itself health data in the SPE on the broad reading. Honest edges: alpha identically zero also satisfies Semantics II (conceded in §4.7); condition (ii), "binding", is a property of the scheme and exists so that Rival 4 fails by definition, which §4.10 concedes; and the Z3 check of Proposition 2 holds by construction, so its evidential weight lies in the refuted mutations (construction without the invalidation entry, without the commitment, without the subject-link entry all yield counterexamples).

**Worked example.** Record 3: t^I = min(116, infinity, infinity) = 116, ground Art 17(1), patient link kept. Record 100: t^I = 16, ground Art 68(12), subject link removed at 16.

**Concede and hold.** Concede the objection has force: "the response concedes its premise and denies its conclusion". Hold: any number of semantics would admit a trajectory; the question is whether this one is what the instruments require, and Proposition 1 shows plaintext cannot be.

**Point to.** §4.7 pp. 60 to 62; §4.10 p. 71; §5.5 p. 86. Slides 9, 24. App ?p=propositions.

#### Q18. [Either] "Explain the anchor condition e(a) minus t(a) is at most F minus L, and why the start of the ceiling's clock matters. Is politiregisterloven section 17 really anchored at the entry?"

**Short answer.** A ceiling collides with a floor only if it is no longer than the floor. Whether you can see that in the text depends on where each clock starts: same start, visible; different start, only each record's history shows it. See Part B, section B3.4.

**Full answer.** Proposition 3: let the floor F run from creation t(a) and a ceiling L from an event at e(a) >= t(a). Under Semantics I they are jointly satisfiable iff e + L > t + F. Proof: C1 needs alpha = 1 up to t + F, the ceiling needs alpha = 0 from e + L; some month carries both iff e + L <= t + F. Case (i), same anchor (e = t): satisfiable for every record iff L > F, decidable from the text alone. Case (ii), external anchor with L <= F: they fail for exactly the records with e - t <= F - L, a set the text does not reveal. For Art 68(12) (L = 6, F = 12) the set is records whose permit expires within six months of the entry, which is the condition of Corollary 1.2. A provision that measured both limits from one event and set the ceiling inside the floor would contradict itself on its face. Section 17 of politiregisterloven ("lagres i minst 1 år og slettes senest etter 3 år") puts a floor of 12 and a ceiling of 36 on one log; read as running from the entry, L > F and no collision arises without a request. The cross-sector run: 60 records, 7 violate, none without a request; under Semantics II none. The provision does not say in words when either period begins; that both run from the entry is a reading of its syntax, stated as such. The same diagnostic applies to any statute: look for a ceiling no longer than a floor and anchored to a different event.

**Worked example.** Record 100: e - t = 10 - 7 = 3 <= 6, collides. Record 102: e - t = 12 - 5 = 7 > 6, clear. Z3 checks both directions and both cases, and refutes an off-by-one version.

**Concede and hold.** Concede [CHECK: Lovdata text of politiregisterloven section 17 not verified; bring it or avoid the detail]. The instance is illustrative, not empirical, and its Semantics II zero is narrower than the health case's: § 17 reaches the whole entry and the module tests only payload and link. Energy and MiFID II remain untested; the thesis says so.

**Point to.** §4.6 p. 60; §6.10 pp. 100 to 101; §7.5 p. 107; A.13 p. 139. Slides 20, 30. App ?p=anchor.

#### Q19. [Either] "Just export the logs out of the research environment at permit closure. Problem solved? And Proposition 4 is not a proposition, it is an assumption with a proof attached."

**Short answer.** Export meets the ceiling and I accept it as sufficient for Corollary 1.2. It does not meet the erasure right, because the right follows the data to whoever holds it. That rests on one legal premise, which I state, and the thesis calls Proposition 4 "a legal argument given the form of a proposition". See Part B, section B3.8.

**Full answer.** Rival 6 (§4.10): exporting access logs at permit closure to a store outside the environment satisfies Art 68(12) literally, on the premise that Art 73(1)(e) fixes how long logs are kept, not where. The ceiling is anchored to a location, requiring data to be absent from it after a deadline; the right is anchored to the data subject and obliges whichever controller holds the data. The premise, not derived from the model, is that a controller receiving a relocated record receives the Art 17(1) obligation with it. Given it, relocation leaves C1 and C2 as they were and the argument of Proposition 1 applies unchanged. Relocation is not free: the exported log still carries its subject fields, now held by a second controller for the rest of the floor, so the personal data have been moved rather than reduced, and where those fields are health data they sit outside the measures Art 73(1) prescribes. For cross-border records there is no environment to leave, so there is no export route at all. The proposition is stated over the model extended informally with a location and a controller, which §4.3 does not represent, and the artefact does not execute it.

**Worked example.** Not in the thesis, from the checker: record 132 (created month 1, request month 4 so deadline 5, permit expiry 7 so ceiling 13, floor to 13). Exporting before 13 meets the ceiling; the month-5 deadline still falls inside the floor.

**Concede and hold.** Concede it is argued from a premise and could be called an observation. If the premise is wrong, Rival 6 becomes stronger; Propositions 1 to 3 are untouched. Hold: "Ending payload accessibility within the floor is necessary for the request-driven conflict, which no relocation escapes."

**Point to.** §4.10 pp. 71 to 72; §3.7 p. 45; §6.2 p. 93. Slides 6, 30. App ?p=anchor.

#### Q20. [Either] "Proposition 1 was restated late. Why does the ceiling disjunct need rho = 1, and which version am I examining? Your legal condition is about the patient link but your collision is over the payload."

**Short answer.** The ceiling C3 binds only secondary records with rho = 1, where the log entry is itself electronic health data; a proof cannot use a constraint on a record it does not bind. Nothing in Chapter 5 moves, because every SPE record is generated with rho = 1. The submitted thesis carries the scoped statement.

**Full answer.** rho(a) = 1 where the entry is itself electronic health data within the environment. On the broad reading rho = 1 for entries at patient-record granularity, and for dataset-granularity entries only where the retained activity content is itself data concerning health; on the narrow reading rho = 0 for every access log. Patient-record granularity is sufficient, not necessary. Under Semantics I, V = alpha, so the Corollary 1.2 collision is over the payload (the logged activity); the patient link beta matters to C3 only where the subject fields are health data. The corollary therefore needs two things: that C3 reaches the record, and that the activity content is health data. The thesis states the second as a premise. §5.2 states the run sets rho = 1 for every SPE record, which models the broad reading. On versions: release 1.3.0 is the cited code and its figures; its viewer quotes Proposition 1 before the scope sentence was added; release 1.3.1 carries the scoped statement; later releases change viewer wording and metadata only. The six result modules are byte-identical across them [CHECK: the walkthrough says the live app is 1.3.2; the repository is at 1.3.4].

**Worked example.** `ceiling_deadline()` in the checker takes no reach flag: every secondary record gets t_pi + 6, which is exactly the rho = 1 modelling choice.

**Concede and hold.** Concede the earlier abstract wording tied the condition to granularity alone; the submitted abstract reads "only for log entries that are themselves electronic health data, as entries kept at patient-record granularity are". Hold: the legal condition and the formal collision now concern the same variables.

**Point to.** §4.4 p. 54; §4.6 pp. 57 to 59; §5.2 p. 80; Appendix A.1 p. 116. Slides 5, 21.

---

## 5. Mechanism and cryptography

#### Q21. [Either] "What exactly is kept, what is destroyed, and when? What can an auditor check afterwards?"

**Short answer.** At the earliest deadline I destroy the payload, its key and its salt. I keep who looked, when, under what authority, a sealed fingerprint of the payload, and a logged invalidation entry. The log never holds what erasure reaches, so it never needs rewriting.

**Full answer.** The audit writer splits each record into accessor fields, subject fields (the patient link) and payload. The payload is encrypted under a per-record data key held under a key-encrypting key in a hardware security module or equivalent. A salted commitment c(a) = Commit(p, r) binds the payload without revealing it. The Merkle log (RFC 6962 hashing, as in Certificate Transparency) takes leaves holding the accessor fields, the creation month, the payload commitment, a salted commitment to the subject fields and the invalidation entries; never the payload, never the subject fields. The invalidation month is the earliest of the erasure deadline, the ceiling deadline and a controller-set payload period. At that month the key, salt and ciphertext are deleted; for patient-level SPE logs the subject fields go at the ceiling. The invalidation entry carries the record identifier, the month, the legal ground, the authorising actor and a hash of the destroyed key's identifier. After invalidation an auditor can establish four things: the access happened, by whom, with all its accountability attributes; some payload was bound at write time and has not been substituted (opening needs a party that kept an opening); the payload was invalidated, when, on what ground, by whom; and each entry is in the log as first written, by inclusion proof. The auditor cannot read the payload and cannot check that the key is gone.

**Worked example.** The run's printout for record 100: accessor fields True (R-008, permit DP-015, success); subject link removed month 16; commitment 678ade47c1e6dc03296175e056fd8116...; key, salt, ciphertext None; invalidation month 16, ground EHDS Art 68(12); payload readable False. Code: `apply_invalidation` (trf_checker.py line 270), `alpha` (296), `V_II` (305).

**Concede and hold.** Specified, not implemented: terminal transition, per-leaf nonce, proactive invalidation (the run has P infinite), published roots with consistency proofs, the accumulator. Hold: none is part of either executed proposition.

**Point to.** §4.8 pp. 63 to 67; Figure 4.1 p. 64; §5.7 pp. 87 to 88; Table 4.1 p. 74. Slides 10, 11. App ?p=built.

#### Q22. [Curado] "Is your commitment even hiding? Where do the salts come from?"

**Short answer.** The design requires a random per-record salt. In the reported run the salt is derived from the record identifier so the run reproduces exactly, so it is not hiding in that run. `--random-salts` draws it from os.urandom.

**Full answer.** A commitment must be hiding (reveals nothing without the salt) and binding (no second payload opens it). A bare unsalted hash does not hide: for clinical content from a constrained space, such as a diagnosis code or a formulary medication, an adversary can confirm a guess by recomputing the hash, so an unsalted commitment would be a surviving item of personal data and the mechanism would have relocated the erasure problem. With a random salt of adequate length the commitment alone leaks nothing, and because the salt is destroyed with the key no party can confirm a guess from the audit store after invalidation unless it kept its own opening. Destroying the salt does not weaken binding, which is a property of the commitment value. After invalidation, an auditor can open the commitment only through a party that was handed the opening at write time (the data subject or the patient's home contact point); otherwise it fixes only that some payload was bound. In the reported run c = SHA-256(salt || payload) with a 16-byte salt derived from the record identifier. Two further points are in the code but not in the thesis text: the derived salts repeat with period 256 in the record identifier, and the salt of the subject-link commitment is derived from the identifier plus 100000 while pseudonyms come from a 100-value space (PSN followed by the identifier modulo 100), so in the reported run that link commitment is brute-forceable. The leaf-level analogue (a per-entry nonce so a surviving leaf hash confirms nothing) is specified, not implemented.

**Worked example.** Run `python3 trf_checker.py --random-salts`: record 100's commitment becomes 483ca80edb4c686ca63db33c3081d47c... instead of 678ade47c1e6dc03...; every count is unchanged.

**Concede and hold.** Say the salt caveat first, before it is asked. Hold: the property is a requirement of the design, not an implementation preference, and no figure depends on it.

**Point to.** §4.8 p. 65; §4.9 p. 68; §5.2 p. 80; A.6 p. 121. Slide 27.

#### Q23. [Curado] "Can the operator rewrite your log? Merkle trees give you nothing without published roots."

**Short answer.** Correct, and the thesis says so. The artefact recomputes the root from the leaves the log itself holds, so it detects divergence between a record and its logged events. It does not detect a rewrite of the whole log. That needs roots published or countersigned outside the log and consistency proofs between an earlier root and the current one, as in Certificate Transparency. Both are specified and not implemented.

**Full answer.** What the check does catch: an inclusion proof is the logarithmic list of sibling hashes from a leaf to the root; `MerkleLog.proof` collects them and `verify` rehashes and compares to the root. Altering record 100's actor makes its access entry fail its proof; altering its invalidation ground makes the invalidation entry fail; altering record 3's patient link means the link no longer opens the salted commitment its leaf carries. Each makes V^II false, and restoring them makes it true. What it cannot catch: the operator who rewrites everything and recomputes the root, because nothing outside the operator's control holds an earlier root. The operator is a named trusted party in §4.9: alteration is detectable, not impossible. The claim "cannot be rewritten without detection" therefore holds only once a root containing the entry has been published outside the log, and the contribution statement now says tamper-evident against a published root, not tamper-proof. What does hold: once a root containing an invalidation entry is published, the claim cannot be withdrawn. Where roots are published (a public ledger, a regulator, a countersigning party) is a deployment choice the thesis does not make.

**Worked example.** The run's log has 438 entries; 200 of 200 records verify; three tamper tests fail V^II and all pass after restoring.

**Concede and hold.** The Norwegian SPUHiN draft requires "tamper-proof" logs (P13); the mechanism's log is tamper-evident, which addresses that by detection against a published root. Use "tamper-proof" only when quoting that requirement. Hold: this is the open edge and it is named on slide 11.

**Point to.** §4.8 p. 66; §4.9 p. 69; §5.7 p. 88; Table 4.1 p. 74; §6.1 p. 91. Slides 11, 29. App ?p=run.

#### Q24. [Curado] "Why not just put this on a blockchain?"

**Short answer.** The problem is not where the log lives but what an entry contains. A ledger copies every entry to every node and never forgets, so personal data written there meets the erasure right head on. The Merkle log gives what a chain would add, tamper evidence and inclusion proofs, and its leaves never hold what erasure reaches.

**Full answer.** KONFIDO (2016 to 2019) extended OpenNCP with a blockchain auditing component valued for immutability, and left the immutability-versus-erasure conflict unresolved; it also depended on Intel SGX hardware. Finck's analyses set out the tension; a review of 114 papers reports the right to be forgotten first among the difficulties; and the EDPB's Guidelines 02/2025 on blockchain treat it as an unsettled constraint. Redactable blockchains and chameleon-hash designs resolve it the other way, by giving a key holder the power to rewrite history, which is a trust assumption this design avoids. My route: the log is never edited, and erasable content never enters it. Leaves hold the accessor fields, the payload commitment, a salted commitment to the subject link and invalidation entries. The thesis also argues the tri-lateral conflict cannot be dissolved by any storage choice. Norway has a clinical precedent for blockchain-anchored consent (NewbornTime, a Hyperledger platform at Stavanger University Hospital, which addresses consent recording rather than audit-trail erasure). A public ledger could be one place to publish roots; the thesis neither specifies nor evaluates that.

**Worked example.** In the run, record 100's leaf holds R-008, DP-015 and 678ade47c1e6dc03...; the diagnosis-like payload and the patient link are in the record store, and are destroyed there.

**Concede and hold.** The remark that a public ledger could host published roots is a framing of mine; the thesis does not say where roots go. Hold: no log needs rewriting if it never held what erasure reaches.

**Point to.** §2.4 pp. 21 to 25; §4.8 p. 66; §4.9 p. 69. Slides 6, 18. App ?p=built.

#### Q25. [Curado] "You cannot prove a key was destroyed. What does an HSM give you? And then what does 'verifiable' in your title mean?"

**Short answer.** I cannot, and nobody can by inspection from outside. The entry is an attestation: who destroyed which key, when, on what ground, bound into the log. An auditor can check the claim was made and not altered, not that it is true. So "verifiable" qualifies the invalidation record, not the erasure.

**Full answer.** Reardon and colleagues' systematisation shows that the further a deletion approach operates from the storage medium, the harder it is to assert that destruction occurred; cryptographic erasure is the limiting case. The entry records a named actor, a named key identifier (hashed), a month and a ground, and binds it into the Merkle log so the claim cannot be altered without detection, nor withdrawn once a root containing it is published. Key-management guidance treats such a record as the normal trace of a destroyed key (NIST SP 800-57, section 7.6). A FIPS 140-3 validated module places destruction inside a tested boundary, but validation attests the module's design, not any particular destruction. In the artefact, a custody object stands in for the HSM: the optional module uses real AES-256-GCM with per-record data keys wrapped under a key-encrypting key, and after the 138 scheduled destructions exactly those records refuse to decrypt through custody while 62 still read; that shows unreadability follows from destruction, not that destruction happened. Proof would need proof-of-secure-erasure protocols (Bursuc et al., 2024) or certified deletion, where public verifiability is an open problem (Broadbent and Islam, 2020). The alternative is not proven deletion but unattested deletion: "delete and log" is the same kind of unverifiable claim with less structure.

**Worked example.** `python3 crypto_envelope.py`: 138 refused, 62 decryptable, and record 3's ciphertext opened by none of the 62 surviving keys.

**Concede and hold.** "Refusal" in the module is the custody object's missing wrapped key (a dictionary removal); the cross-key test is the cryptographic check. In the checker, the key identifier whose hash goes into the entry is a placeholder. Hold: §1.4 says verifiable qualifies "the invalidation record ... not the erasure itself, which no auditor can verify".

**Point to.** §1.4 p. 7; §4.9 pp. 69 to 70; §6.3 p. 94; §7.5 p. 107; A.15 p. 142; A.22 p. 149. Slides 11, 25. App ?p=robust.

#### Q26. [Curado] "Why keys at all? Your model cannot tell destroying a key from deleting the payload. And is destroying a key even erasure?"

**Short answer.** Agreed: nothing in the model distinguishes them; both set alpha to zero. The store deletes the payload. Key destruction is for copies the store cannot delete at once, backups and replicas, and for those it secures unintelligibility, not erasure.

**Full answer.** EDPB Guidelines 02/2025 (final, 7 July 2026), para 51: after deletion of the decryption key the encrypted data will be unintelligible, at least until the algorithm is broken; in the same paragraph, encrypted personal data is still personal data; para 125: an erasure request requires the data erased or rendered anonymous. So the Board describes what key deletion achieves without classifying it as erasure, and the thesis never says the EDPB endorses crypto-erasure. The mechanism therefore deletes the ciphertext, key and salt from the store at invalidation. The case for keys rests on copies, which the model does not represent and the TEHDAS2 specification expressly reaches: electronic health data "MUST be deleted or rendered unrecoverable within six months of permit expiry, including any backups or redundant copies" (OPR-6). Such copies become unreadable at the invalidation month and leave by ordinary rotation, a bounded residue stated as such. NIST SP 800-88 Rev. 2 recognises cryptographic erase within a documented key-management boundary. Per-record keys are the simplest construction, not required: a record encrypted so that a subject share and a permit share are each needed to read it becomes unreadable when either is destroyed, with a registry growing with subjects and permits (policy-based secure deletion, Cachin et al., 2013); not implemented. The documented threat model condition is Aikebaier's (2026) interpretation, adopted as a design discipline, not the Board's formulation.

**Worked example.** Permit expiry invalidates the records of one permit; an erasure request invalidates the records of one subject; these sets intersect without nesting, so no single per-subject or per-permit key serves both.

**Concede and hold.** Concede the title's "crypto" rests on copies, not on a proposition. A "crypto" mechanism without backups would reduce to delete-and-log (Q28). Hold: OPR-6 asks for exactly this balance and does not say how.

**Point to.** §4.8 pp. 63 to 65; §4.9 p. 69; §6.4 p. 95; §2.4 p. 23. Slides 10, 22, 25.

#### Q27. [Curado] "What is your threat model? Why keep an accumulator that needs a trusted manager and is not built?"

**Short answer.** The thesis names five trusted parties or assumptions. The accumulator is optional and not load-bearing, and I am willing to drop it.

**Full answer.** §4.9 lists: (1) the controller executes destruction when the entry says it did, and had no copy of the key outside the custody boundary at that moment; (2) the custody boundary, an HSM or equivalent, retains no recoverable key material after a destruction instruction and does not leak it through side channels; (3) the audit-trail operator does not remove or alter entries, which the append-only construction makes detectable but not impossible, a rewritten history needing published roots and consistency proofs (artefact: inclusion proofs only); (4) where the optional accumulator is used, its manager, who holds a trapdoor and could forge validity witnesses; (5) the cryptographic assumption that the commitment stays binding and hiding and the payload cipher unbroken across the horizon. The horizon matters over a ten-year floor: deleting the ciphertext at invalidation removes that exposure for the store's own copy, but copies awaiting rotation, and records with no invalidation event, keep ciphertext until the terminal transition. What an auditor can verify without any of that trust: internal consistency of the metadata, that an invalidation entry exists with month, ground and actor, that it is bound into the log, and that a commitment survives. The accumulator (Camenisch and Lysyanskaya type) would add a succinct proof that a record has not been invalidated; Proposition 2 holds if validity is checked by scanning the registry.

**Worked example.** With no accumulator the run still answers "is record 100 invalidated?" by scanning the registry: entry month 16.

**Concede and hold.** The accumulator is "the most dispensable" component (§6.5); offer to drop it. Hold: every trust assumption is named, and the thesis does not claim more.

**Point to.** §4.8 p. 66; §4.9 pp. 69 to 70; §6.5 p. 96. Slides 11, 25.

#### Q28. [Either] "Isn't this just crypto-shredding with a new name? Why not delete the record and log the deletion?"

**Short answer.** The technique is crypto-shredding and I claim no new cryptography. I add a model showing when it can meet three rules together, a precise meaning of "verifiable" that makes it possible, and a record an auditor can check. For cross-border records, delete-and-log is close to equivalent, and I concede that.

**Full answer.** The practitioner pattern (per-subject key destroyed on request) is bilateral and asserted: no model, no verifiability semantics, ciphertext retained. Rival 4, "delete the record and log the deletion", satisfies C2 and C3 and preserves a trace, and it fails C1 under Semantics II only because no commitment survives, which is true by definition. So what does the commitment add? Before invalidation an auditor can open it against the payload and detect substitution of one record's content for another's. After invalidation it can be opened only by a party that kept an opening; otherwise it fixes only that some payload was bound. The advantage is therefore real but bounded, lying chiefly in the logged, attributed, tamper-evidently bound invalidation entry and only partly in the commitment. For cross-border records, where the patient link is kept and nobody is handed an opening by default, the advantage narrows to the entry. In SPE logs the subject link and payload go at the ceiling while the accessor fields stay, and there the commitment does work deletion cannot. The sixth §7.2 statement is calibrated to match: what it adds to the practitioner pattern is a combination whose parts are standard (NIST SP 800-57 section 7.6 already records destroyed keys in audit logs; Crosby and Wallach for tamper-evident logs), plus the partition into accessor fields and what erasure and the ceiling reach. Against unlogged deletion it improves on assurance; against deletion logged in the same tamper-evident log, its advantage is confined to the commitment.

**Worked example.** Record 100 after invalidation: under delete-and-log the auditor learns something was deleted; under the mechanism the auditor also holds c(a) = 678ade47c1e6dc03... bound at write time.

**Concede and hold.** Concede it plainly: the weight of the thesis lies in the semantics and the necessity analysis, not the commitment. Hold: the contribution is a feasibility characterisation and verifiability parameter, which crypto-shredding as practised does not have.

**Point to.** §2.4 pp. 23 to 25; §4.10 p. 71; §6.3 p. 94; §7.2 p. 104. Slides 18, 28.

---

## 6. Evidence and validity

#### Q29. [Either] "What do your 200 records actually show?"

**Short answer.** Read "verifiable" as "readable" and 90 records fail, with 95 violations. Read it as "accountable" and none fail. The counts follow my generator; what is checked is the shape of the result, not a frequency.

**Full answer.** The run generates 200 audit records: 100 cross-border (floor 120 months, request probability 0.40) and 100 from research environments (floor 12, permit expiry 1 to 12 months after creation, request probability 0.25), seed 20260915. Under Semantics I, 90 records violate: 37 cross-border (all C2) and 53 SPE. The 95 violations count 5 SPE records twice, because they collide with both the erasure deadline and the ceiling. By cause: 41 C2 only, 44 C3 only, 5 both. Of the 78 SPE records with no request, 39 collide with the ceiling alone, which is Corollary 1.2. The conditional shape of Proposition 1 is reproduced: 38 cross-border requests, 37 inside the window and all 37 violate; the one outside the window does not. Under Semantics II, 138 records are invalidated (52 cross-border, 86 SPE) and violations are zero. The generator is built so that the structure is visible, not so that the rates are realistic, and the thesis says so at each table.

**Worked example.** Record 3 is one of the 37; record 100 is one of the 39; record 38 is the cross-border request outside its window.

**Concede and hold.** Concede the zero under Semantics II holds by construction (Q6). Hold: the integrity check can fail, and does under tampering.

**Point to.** §5.3 to §5.4 pp. 83 to 85; §5.7 p. 87; Tables 5.3, 5.6. Slide 12. App ?p=ledger.

#### Q30. [Either] "How was it checked? Is any of it independent?"

**Short answer.** Three checks: an exhaustive search over every yes-or-no assignment on small cases, a Z3 solver hunting for counterexamples, and a swap of the payloads for generated health records. None is independent of me, and the thesis declares that. They check my code against my encoding, not my encoding against the law.

**Full answer.** The exhaustive search enumerates 2^14 = 16,384 assignments per case on four cases: three conflicts are infeasible and the control is feasible. It is a sanity check, since the constraints are pointwise, and it shares two constants with the checker, so it is not independent. Z3 is a bounded check over floors 1 to 120, response periods 1 to 3 and a horizon of 140 months: 9 of 9 properties return no counterexample, and four deliberately broken variants (no invalidation entry, no commitment, no subject-link entry, Proposition 3 off by one) each return a counterexample, which is what gives the check evidential weight. The Synthea swap replaces payloads with 98 generated FHIR R4 bundles: all 200 commitments change and all six result measures are identical, because no constraint reads content. The checker, the cross-check and the Z3 script were written in the same AI-assisted process (declared on p. xi). The tests pass (63 at release 1.3.4; the thesis reports 56 at 1.3.0).

**Worked example.** At response period 3, Semantics I falls from 95 to 94 violations (90 to 89 records); the Corollary 1.2 count stays 39, because the ceiling does not involve the response period.

**Concede and hold.** Concede there is no proof assistant and no independent implementation. Hold: the propositions are short enough to be checked by hand (Part B), and the mutations show the checks can fail.

**Point to.** §5.5 to §5.6 pp. 85 to 87; A.23 p. 150; Declaration p. xi. Slides 12, 24. App ?p=robust.

#### Q31. [Either] "Synthetic data. What can it show, and your patients are American."

**Short answer.** It shows structure: when rules collide and when they do not. It cannot show how often this happens in Norway. The model reads timing, never content, so which patients are generated does not move any figure, and the swap proves it.

**Full answer.** What synthetic data can show here: Proposition 1's conditional shape; invariance to payload content; that the checks can fail. What it cannot: frequencies, real permit durations (the uniform 1 to 12 months is an assumption), the share of valid requests (all are treated as valid), or Norwegian clinical practice. The choice is also an ethical one, grounded in Datatilsynet's 2021 decision on testing with real data (the Norges idrettsforbund case, §3.5), and no real data were used. Synthea's default profile is US Core, and FHIR R4 matches the Norwegian basisprofiler, so format fits; content is irrelevant to the constraints. When 200 of 200 commitments changed after the swap and no figure moved, that was the intended result: it shows the constraints are about time and rights, not about what the record says.

**Worked example.** Record 100's commitment changes with its payload (678ade47... to a different value) and its violation status does not.

**Concede and hold.** Concede that frequencies cannot be inferred; the thesis never infers them. Hold: a feasibility claim needs witnesses, not a sample.

**Point to.** §3.5 pp. 41 to 42; §5.8 p. 89; §6.7 p. 97; Table 5.7 p. 90. Slide 26. App ?p=synthea.

#### Q32. [Either] "Is your result sensitive to the numbers you chose: floor, response period, ceiling?"

**Short answer.** The pattern is not; the counts are, and they are not claimed. Corollary 2.2 says no result depends on the floor, and Semantics II gives zero violations at every setting I ran.

**Full answer.** Proposition 1 gives the condition for collision as t_r + delta <= t + F, so shrinking F shrinks the set of colliding records without changing the form. The thesis reports one sensitivity (response period 3: 95 to 94 violations; Table 5.5). The repository's `sensitivity.py` (not in the thesis; run it once yourself before the defence) gives a floor sweep: with the ceiling applying, floor 120 gives 95 violations over 90 records, floor 72 gives 83 over 78, floor 36 gives 66 over 61; with the ceiling excluded (the narrow reading) they are 46, 34 and 17 records; Semantics II gives zero violations in every row and 138 invalidations with the ceiling applying, 60 without. The six-year Norwegian pilot floor is 72 months, so the sweep covers it.

**Worked example.** At six years record 3's floor ends at month 83, its deadline is 116, no collision. The rows above show how many records behave like it.

**Concede and hold.** The sweep is not in the submitted thesis: say "the repository's sensitivity script" and no more [Since submission: sensitivity.py is in code releases 1.3.3/1.3.4, made for the journal article; the thesis cites 1.3.0.]. Hold: Corollary 2.2 (F arbitrary) is in the thesis, p. 62.

**Point to.** §4.7 p. 62; §5.6 p. 87; Table 5.5. Slide 24. App ?p=robust.

#### Q33. [Either] "What does the model leave out, and what is not deployed?"

**Short answer.** Every request is treated as valid, a payload is one block, a month is the unit, and nothing is deployed: no contact point, no performance figures, keys destroyed only in memory. Frequencies are unreliable; the propositions are not.

**Full answer.** The model's declared limits (§3.7): (1) C1 is closed and so conservative; (2) C2 binds from the start of month t_r + delta, so boundary months can be grid artefacts; (3) all requests are treated as valid, which inflates frequencies, since an invalid request would not set a deadline; (4) the payload is one unit, so field-level redaction is outside the model (Corollary 2.3 covers one case). Not done in the artefact: the NCPeH connection, the OpenNCP flow, authentication, consent, timing, hardware custody. Specified, not built: published roots with consistency proofs, the leaf nonce, the terminal transition, proactive invalidation, the accumulator (§6.1). Integration with Norway is by specification (Table 4.1), not by test. Appendix A.9 lists five known limitations of the artefact itself. The expert panel (Appendix C) is designed, not run, and awaits Sikt notification.

**Worked example.** Record 3 at response period 3: deadline 118, still inside the window, so the result survives the grid choice.

**Concede and hold.** Concede all of it; the list is in the thesis. Hold: a feasibility result survives imperfect frequencies, because it is an existence statement.

**Point to.** §3.7 pp. 44 to 45; §4.3 p. 51; §6.1 p. 91; §7.5 p. 107; A.9. Slide 14.

---

## 7. Norway

#### Q34. [Either] "Helsedirektoratet's six years against your ten. Where does the floor come from?"

**Short answer.** I asked. Helsedirektoratet replied on 19 October 2026 that no specification fixes a period, that it is left to national law, and that for the pilot they decided six years, with the production figure still to be decided by them as controller. So I treat the floor as a parameter and use ten years only as an illustration.

**Full answer.** The enquiry went to Helsedirektoratet's central mailbox on Monday 5 October 2026; the reply came from Hans Löwe Larsen, Avdelingsdirektør, Division of Information Management and Method, and is reproduced with permission in Appendix D (D.1, p. 168). He finds no retention length in the requirements catalogue or the named specifications (Security Services, System Architecture, NCPeH Architecture, Audit Trail Profile), which refer to national law without fixing a period or manner of storage. Ten years was an unsourced figure from secondary literature, so I do not use it as a fact. Because the reply attributes six years to the pilot decision of a controller, §4.2 draws the consequence: absent a national legal basis, six years is a policy floor, so before Art 9 EHDS applies in 2029, keeping the patient link against an erasure request has no secure Art 17(3)(b) basis. The thesis does not say any Norwegian law sets six years.

**Worked example.** At six years record 3's floor ends at month 83; its request at month 116 falls after, so no collision. At ten years it falls inside.

**Concede and hold.** Concede the reply is one email, from one officer, and the production period is undecided. Hold: no result depends on F (Corollary 2.2).

**Point to.** §2.3 pp. 17 to 18; §4.2 pp. 50 to 51; Appendix D p. 168. Slides 4, 14, 31. App ?p=norway.

#### Q35. [Either] "Where does this attach to Norway's systems, and who decides?"

**Short answer.** At two narrow points: the last step of the cross-border exchange, where the audit record is written, and the logging boundary of a research environment. It asks nothing new of Norway's systems.

**Full answer.** The NCPeH is run jointly by Helsedirektoratet and Norsk Helsenett; the mechanism attaches at step six of the OpenNCP flow, where the audit message is stored. Because Norway is not an EU member, the Regulation reaches it only once incorporated into the EEA Agreement, so these attachment points are where the national authorities would act, not where any duty already binds them. Folkehelseinstituttet is the Ministry-designated coordinating Health Data Access Body; Helsedataservice, within FHI, decides access for eleven central registries; how many bodies Norway will have is not settled (§2.6). Secure processing environments (TSD, SAFE, HUNT Cloud under NORTRE) are fragmented, down to disconnected PCs (SPUHiN 2024), so the mechanism works on the log every environment must produce. It adds no requirement of a new kind to the national criteria (an information security management system, tamper-proof logs). The thesis reads Table 4.1 as the integration map: component by component, what each party would do.

**Worked example.** Record 3 is written at the NCPeH audit repository; record 100 at an SPE logging boundary under permit DP-015.

**Concede and hold.** Concede integration is specified, not tested; no Norwegian operator has seen this. Hold: nothing here needs a new system.

**Point to.** §4.11 pp. 73 to 74; Table 4.1 p. 74; §2.2 p. 16; §2.6 p. 28. Slide 15. App ?p=norway.

#### Q36. [Either] "Which authorities have you asked, and what is still open?"

**Short answer.** Two letters. Datatilsynet got the GDPR-side questions on 23 September 2026, with no reply at submission. Helsedirektoratet answered the floor question on 19 October. The EHDS-side question, whether Art 68(12) reaches patient-level logs, is still to ask.

**Full answer.** Keep the two apart; they answer different questions and must not be merged into "the authorities were asked". Datatilsynet (23 September, Appendix D.2 p. 169) was asked the GDPR-side questions of §7.4, including whether an invalidated record discharges a retention obligation. Helsedirektoratet was asked the floor only (Q34). Still to ask, of Helsedirektoratet, the Ministry or the Commission: whether Art 68(12) reaches patient-level logs, and whether Art 73(1)(e) needs the subject link after the ceiling. If an authority says identifiable logs must stay readable, Proposition 2 stays true of the model and becomes "practically inert" (§6.2). If Datatilsynet has replied since submission, say what it says and nothing more than it says. [CHECK: the status of the Datatilsynet reply as at the defence date; the thesis records none at submission.]

**Worked example.** A "no" on the first question makes the move fail cleanly and shows exactly what would have to change: the semantics, not the arithmetic.

**Concede and hold.** Concede that the legal argument is incomplete without them, and that I should have asked earlier (Q42). Hold: the thesis labels both questions open in §7.4.

**Point to.** §6.2 p. 92; §7.4 p. 106; Appendix D pp. 168 to 169. Slides 14, 22. App ?p=start.

#### Q37. [Either] "What does Helsedirektoratet's own privacy notice say? And what Norwegian law applies?"

**Short answer.** The notice is not in the thesis, so I treat it as extra evidence from my article source check, not a thesis claim. It states six years for the accessor fields and cites GDPR Art 6(1)(c) with pasientjournalloven section 22 as the basis for the logging. Say exactly that and no more.

**Full answer.** Helsedirektoratet's public privacy notice, revised 30 June 2026 [Since submission: Helsedirektoratet privacy notice, last revised 30 June 2026, checked 27 Nov 2026. Not in the thesis; say "since submission".], states six years for the accessor fields: name, HPR number, role, institution, place and time of lookup. These are the same fields the mechanism keeps for the floor. Precision matters: the notice names section 22 as the legal basis for the logging; it does not say section 22 itself sets six years, and Larsen's reply says the period was a pilot decision. Do not write "since submission": the notice predates it. On the wider question, the thesis finds no national provision that fixes the period, and §4.2 states the consequence (Q34). EEA status: the Regulation is being processed for incorporation into the EEA Agreement, and the thesis dates are subject to that [Since submission: the EFTA register (26 Nov 2026) lists the EHDS Regulation as under scrutiny for incorporation, not yet incorporated.].

**Worked example.** The six-year floor for accessor fields matches what record 3 keeps after invalidation: actor, role, institution, time, and the logged invalidation.

**Concede and hold.** Concede the notice is secondary evidence for a figure the thesis rests on a letter for. Hold: the two sources agree on six years, and neither claims it is law.

**Point to.** Not in the thesis; §2.3 p. 17 and Appendix D p. 168 for the six years; §1.1 p. 1 for EEA. Slides 4, 31.

---

## 8. Programme fit

#### Q38. [Ferreira] "This is a logistics degree. Where is the logistics?"

**Short answer.** There is no optimisation and no objective function, and I do not claim one. The logistics is in the object and in one design decision. An audit record is information in storage with a planned exit, and customs keeps the record after the goods are destroyed; Semantics II does the same.

**Full answer.** CSCMP defines logistics as the flow and storage of goods, services and related information (§2.7). An audit record is related information, and the thesis is about its storage and its exit. The floor is a per-record parameter, taken from chain-of-custody practice, which is why the cross-border floor and the SPE floor are one constraint with two instances (§4.3). Proposition 3 is a two-clock perishability result: a record held against a floor, while a deletion clock runs from an external event, collides exactly when the event comes soon enough, and the text alone does not reveal which records. The method is constraint modelling in the operations-research tradition, and the framing comes from four years in cross-border procurement (§1.4). Record 3 behaves like a consignment: made at one node, carried through a six-step gateway, held under rules set elsewhere.

**Worked example.** Customs: goods are destroyed under order, the declaration stays for years. Record 3: payload destroyed at month 116, accessor record stays to 131.

**Concede and hold.** Concede no logistics metric is optimised. Hold: the thesis says so in §1.5 and §2.7, and the claim is about information logistics, not freight.

**Point to.** §2.7 pp. 30 to 31; §1.4 p. 7; §1.5 p. 8; §6.9 p. 99. Slide 20. App ?p=anchor.

#### Q39. [Ferreira] "The programme is about sustainable energy. Where is the energy?"

**Short answer.** There is none in the result, and §1.5 says so: no energy measurement and no saving is claimed. The fit is the logistics of information. The nearest energy case is Elhub, whose retention rule has the same form as my floor, and testing it is the next step.

**Full answer.** The fourth exclusion in §1.5 states that the thesis claims no energy result. Elhub, Norway's electricity data hub, keeps customer data for three years and 41 days after a contract ends (Elhub, privacy statement, 31 March 2026): a floor anchored to an event, which is the same form as my floor parameter, so the floor-against-right part of the model applies directly. Whether Elhub also has a deletion ceiling that collides with the floor is exactly the Proposition 3 test, which I have not run, and §7.5 names it as the first application. Smart-meter data are personal data under the same regime, so the problem is not remote from the programme's subject. Do not say the thesis shows anything about energy.

**Worked example.** An event-anchored floor of three years and 41 days against an erasure right is Proposition 1's shape; a ceiling from the same contract end would be Proposition 3's.

**Concede and hold.** Concede nothing in the thesis is about energy, and that Elhub as it stands is floor against right, the bilateral case I say is not the contribution; the ceiling test is the open part. Hold: the generalisation is stated as future work (§7.5), not as a result.

**Point to.** §1.5 p. 8; §2.7 pp. 30 to 31; §7.5 p. 107. Slide 20.

---

## 9. Novelty and competitors

#### Q40. [Either] "What is new, and what is borrowed?"

**Short answer.** The cryptography and the method are borrowed. What is new is putting a keep rule, an erasure right and a deletion limit on one record in one model, finding that the word "verifiable" decides whether all can hold, and showing where the clash hides. I also specify the mechanism and check its residue.

**Full answer.** Borrowed, and credited (§2.4 to §2.5): hash-chained logs (Schneier and Kelsey, 1999), Merkle proofs (Crosby and Wallach, 2009), Certificate Transparency (Laurie et al., 2013), hiding commitments, cryptographic erase (NIST SP 800-88 Rev. 2), the Ephemerizer, Vanish and policy-based deletion, and formal compliance as satisfiability (Feng et al., 2023). The log-editing family (chameleon hashes, redactable signatures, blockchains) is rejected, not borrowed. What the thesis claims as new in the reviewed literature (§2.10, p. 36): the formal tri-lateral characterisation, verifiability as the deciding parameter, the anchor condition (Proposition 3), the information-logistics expression of the problem, the cross-border health instantiation on the Norwegian substrate, and the residue analysis. The Statement of Contribution (pp. ix to x) states the claim as one of framing and feasibility, and the sixth §7.2 statement was calibrated down for the combination.

**Worked example.** DePaul keeps recoverable copies to a purge date; record 100's readable copy must be gone at month 16 though its floor runs to month 19.

**Concede and hold.** Concede "just framing" if pressed: a contribution of framing and feasibility, and p. x says so. On prior art (formal GDPR erasure deadlines, deadline-triggered key destruction, keys for intersecting deletion sets, all seven or more years old): the claim is bounded to the reviewed literature, the search is logged in Appendix B, and policy-based deletion (2013) is credited in §4.8 (see Q26). Hold: what is claimed as new is the combination over a floor, a right and a ceiling.

**Point to.** Statement of Contribution pp. ix to x; §2.8 p. 32; §2.10 p. 36; §7.2 p. 104. Slides 18, 28.

#### Q41. [Either] "Who else has done this? Why does yours differ?"

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

## 10. Hostile or meta

#### Q42. [Either] "What would you do differently? If you had another year, what first?"

**Short answer.** I would ask the authorities earlier, because no modelling replaces their answers. I would run the expert panel. And I would build what I only specified, starting with published roots so the log cannot be quietly rewritten.

**Full answer.** First, the two authority questions: Datatilsynet on whether accountability-preserving verifiability discharges retention (asked 23 September, no reply at submission), and, on the EHDS side, Helsedirektoratet, the Ministry or the Commission on whether Art 68(12) reaches patient-level logs. A "no" from either would refute a specific step cleanly. Second, the Appendix C panel, after Sikt notification: utility and acceptance are not evaluated, and that is a real gap in a design science thesis. Third, technically: published roots with consistency proofs, the per-leaf nonce and the terminal transition, which a cryptographer would close first. The research problem I would take next is proving completeness of invalidation for one subject without revealing the set, where a zero-knowledge argument over the published root becomes necessary rather than decorative (§7.5). Also real permit durations, and the Proposition 3 test on Elhub. Process lesson: an earlier draft, discarded in May 2026, cited works that do not exist (p. xi), and every citation has since been checked.

**Worked example.** The record-100 commitment in the reported run is not hiding; `--random-salts` fixes it, and I would make that the default.

**Concede and hold.** Concede the late authority questions. Hold: they are stated as open in §7.4, not hidden.

**Point to.** §7.4 p. 106; §7.5 p. 107; §5.2 p. 80; Declaration p. xi.

#### Q43. [Either] "How did you use AI, and can you explain the code line by line?"

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

#### Q44. [Either] "Why 'VERA-SNARK' if there are no SNARKs?"

**Short answer.** There is no SNARK, and the thesis says so. The name comes from my NORS 2025 presentation, where I planned zero-knowledge proofs. The formal analysis showed that commitments and a logged registry are enough, so I dropped them. That is the design cycle working.

**Full answer.** The Statement of Contribution (p. x) carries a note on the name, and §1.6 and §3.2 record the step: Hevner and Peffers expect the artefact to change as evaluation teaches something. The mechanism is named Crypto-Erasure by Invalidation, and nothing in it needs a succinct proof: inclusion proofs on a Merkle log, a salted commitment and a logged registry give an auditor everything Proposition 2 requires. Zero knowledge returns at one point, which is a future problem: proving that all of one patient's records were invalidated without revealing which they are (§7.5; Aikebaier's fourth open problem). An auditor seeing record 3's invalidation is fine; proving "every record of hers was invalidated" without listing them would otherwise expose her care history.

**Worked example.** The point at which zero knowledge would matter: record 3 is one of a patient's many records; completeness over all of them is the open proof.

**Concede and hold.** Concede the name is a historical label. Hold: continuity with NORS 2025 is why it stays, and p. x says so.

**Point to.** Statement of Contribution p. x; §1.6 p. 9; §3.2 p. 38; §7.5 p. 107. Slide 19. App ?p=built.

#### Q45. [Either] "Your invalidation entry names the right that was exercised, and keeps the record identifier. Doesn't the log itself need erasing at the end?"

**Short answer.** Yes, at the end. The terminal transition, one month after the floor, destroys the identifying fields and generalises or destroys what the entries carry. It is specified, not implemented, and whether the residue then resists isolation, linkage and inference is for a documented threat model to establish, not something the thesis assumes.

**Full answer.** The entry carries the record identifier, the ground, the month and the authorising actor, so a ground of "GDPR Art 17(1)" reveals that someone exercised a right, and the registry would hold it for ever if nothing ended it. The thesis agrees that the storage-limitation principle (Art 5(1)(e)) forbids keeping identifiable metadata beyond its purpose. At t + F + 1 the terminal transition destroys the identifying fields, the key, the salt and any remaining ciphertext, leaving only event type, document category, outcome and commitment. It is itself logged. §4.8 says what remains is the one state intended to be anonymous rather than pseudonymous, but conditionally: the record identifier and actor in the entries "must be generalised or destroyed", and the residue must pass the Board's isolation, linkage and inference test (draft Guidelines 02/2026). Where a longer obligation applies (archival duty, litigation hold) the transition is deferred by raising F, which the model already supports. In the reported run there is no terminal transition, so the entries do carry the ground.

**Worked example.** Record 3's entry (month 116, Art 17(1)) lives to month 132, when the terminal transition would remove the identifying fields.

**Concede and hold.** Concede the run does not implement it, and that "anonymous" is claimed only for the final state and conditionally. Hold: the thesis names the problem and its test.

**Point to.** §4.8 p. 67; §4.9 pp. 68 to 69; §6.1 p. 91. Slide 27.

#### Q46. [Either] "What would refute you? What if an authority says no?"

**Short answer.** Two things refute parts, and I say which. If an authority holds that identifiable logs must stay readable, Proposition 2 stays true of the model and becomes practically inert. If Art 68(12) does not reach logs, Corollary 1.2 falls. The propositions, the mechanism and the semantics stand either way.

**Full answer.** The thesis is a conditional argument with the conditions named: two principal interpretive steps (that the right and the ceiling reach the audit record, and that an accountability reading of verifiable is defensible) and four subsidiary premises, with no regulatory authority behind any (§3.7, Abstract). A no on the first question makes the move fail, and shows what would have to change: the semantics, not the arithmetic. A no on Art 68(12) removes the single-record three-way collision: of the 90 violating records, 46 remain (37 cross-border and 9 SPE). Cross-border requests still collide under Proposition 1. Technically, a counterexample to Proposition 2's trajectory, an invalidation entry that fails its proof without tampering, or a record on which the checker and Z3 disagree would refute the artefact, and four deliberate mutations show those can be found. What would not refute it: a regulator who dislikes the word "verifiable"; that is a rival semantics, argued in §4.2.

**Worked example.** Under the narrow reading the 44 ceiling-only collisions lapse; 5 SPE records that also have a request inside the window stay violating.

**Concede and hold.** Concede there is no authority yet. Hold: the thesis lists what each answer would do, in §7.4.

**Point to.** §3.7 p. 44; §4.6 pp. 58 to 59; §6.2 p. 92; §7.4 p. 106. Slides 14, 22.

---

## Numbers you must say right

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

## Words to use, words never to use

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

## Known weaknesses (own them first)

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

## Thirty-second answers

**What is the contribution?** "Cross-border health audit records face a retention floor, the right to erasure and, in research environments, a six-month deletion ceiling. I model the three as constraints over one variable: can the payload still be read. If verifiable means readable, the system is infeasible whenever a deadline falls inside the record's window. If verifiable means the accountability fields, a commitment and a logged invalidation are intact, it is satisfiable for every pattern and floor. The proof's trajectory is the mechanism: delete payload and key, keep the accessor fields, log the invalidation. All of this is in the model, not yet in law."

**What is novel?** "Not the cryptography and not the method. What is new in the reviewed literature is applying satisfiability to a floor, a right and a ceiling together, isolating verifiability as the deciding parameter, and Proposition 3: a ceiling collides with a floor only if it is no longer, and the anchor decides whether you can see it in the text. Plus a mechanism whose residue is analysed against Norwegian infrastructure."

**What are the limitations?** "Three. The central interpretive move, that an invalidated record still discharges retention, has no authority behind it, and nor has the broad reading of Article 68(12). Key destruction is attested, not proven, and simulated in my artefact. And the proofs are informal, the demonstration is synthetic, and the counts come from the generator. Published roots, the terminal transition and the accumulator are specified, not built."

**Why should anyone care?** "Because the rules are written and the systems are in pilot, and today a plaintext audit store cannot satisfy them together. The argument costs little to adopt: log every invalidation as an attributed event."

**What did the authorities say?** "Helsedirektoratet: no specification fixes a period, national law decides, six years in the pilot, final decision theirs as controller. Datatilsynet: asked on 23 September, no reply at submission [CHECK: any reply since]."

## The thesis in 60 seconds

"A patient from Molde is treated in Helsinki, and the clinician's lookup is written to an audit log. Three European rules touch that log. One says keep it: six years in Norway's pilot. One lets the patient demand erasure. In research environments a third says health data must be gone six months after the permit ends. If 'verifiable' means 'readable', these cannot all hold: whenever a deletion deadline falls inside the keep period, the payload must be readable and gone in the same month. If 'verifiable' means 'accountable', so we can still show who looked, when, and that the payload was lawfully invalidated, they all hold, for any record and any timing. The mechanism: destroy the payload at the earliest deadline, keep the accountability, log the deletion. I check it on 200 generated records, with an exhaustive search and a solver. I do not claim key destruction is proven, the legal reading is settled, or the counts are real frequencies. Two questions need an authority; I have asked the first."

## The thesis in 20 seconds

"Three European rules collide on one audit record: keep it, erase it, delete it from the research environment. They collide only if 'verifiable' means 'readable'. If it means 'accountable', all three hold. Delete the payload. Keep the accountability. Log the deletion."

## Before the defence

- Open https://trfhimolde.streamlit.app/ the day before; confirm it loads and shows the scoped Proposition 1; keep a screenshot of the ledger and Figure 5.2 (p. 85) as a fallback; backup URL trf-thesis-himolde.streamlit.app.
- Run `python3 trf_checker.py` once on the machine; the output should match `docs/expected_trf_output.txt`.
- Old notes sit in `process/` on a public branch: make the repository private or move them before the examiners open it [CHECK: current state].
- Bring the Lovdata text of politiregisterloven section 17 or avoid the detail (Q18).
- Slide 12's counters animate from zero when presented live; in a PDF export they read 0. If they do not run, say 90 of 200 and 39 of 78.
