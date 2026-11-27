# Part A. The talk, slide by slide

Candidate: Arshad Akhtar Abbasia. Talk: 15 minutes, slides 1 to 16. Slide 17 is the break into questions; slides 18 to 31 are backup. Questions: 30 minutes, Prof. João Ferreira and Joel Curado.

**Conventions.**
- The script is the speaker notes from the deck files, word for word. A change for a factual slip is marked [corrected: was X]. Every note ends in a "Concordance:" line, which is not spoken and is omitted here; each card's Links line carries the same references with printed page numbers.
- Thesis pages are printed pages of the submitted PDF (PDF page minus 14). Deck footers link to one page, which can differ from the section's first page; section pages are given here.
- "Q25" means Part C, question 25. "Part B, section Bx" means a section of B_explainer.md.
- App links start from https://trfhimolde.streamlit.app/ . Deep links are read once per session: use a fresh tab for each.
- Say "in the model" and "generated" whenever a count leaves your mouth.

---

## Slide 1. Cover · 0:00 to 0:20 (20 s)

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

## Slide 2. Promise · 0:20 to 1:05 (45 s)

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

## Slide 3. Record · 1:05 to 1:55 (50 s)

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

## Slide 4. Strip · 1:55 to 2:55 (60 s)

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

## Slide 5. Research · 2:55 to 3:50 (55 s)

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

## Slide 6. Fixes · 3:50 to 4:45 (55 s)

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

## Slide 7. Model · 4:45 to 5:40 (55 s)

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

## Slide 8. Word · 5:40 to 6:30 (50 s)

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

## Slide 9. Result · 6:30 to 7:40 (70 s)

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

## Slide 10. Mechanism · 7:40 to 8:50 (70 s)

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

## Slide 11. Audit · 8:50 to 9:45 (55 s)

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

## Slide 12. Evidence · 9:45 to 10:50 (65 s)

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

## Slide 13. Demo · 10:50 to 12:05 (75 s)

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

## Slide 14. Limits · 12:05 to 12:55 (50 s)

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

## Slide 15. Forward · 12:55 to 13:50 (55 s)

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

## Slide 16. Close · 13:50 to 14:40 (50 s)

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

## Slide 17. Backup index (questions)

On screen: the list of slides 18 to 31 in two columns. Notes: "Index for the thirty-minute defence. Jump by slide number in present mode. Slides 18, 19 and 29 cover the ledger, zero-knowledge and log-rewrite questions; 28 and 30 the rival designs; 31 adoption and cost. Every answer: concession first, then what survives, then the section number."

---

## Backup slides 18 to 31

Open a backup only when the question arrives. Every answer: the limit first, then what survives, then the section.

### Slide 18. Why not a blockchain? (q-chain)
**Open when:** "Why not put this on a blockchain?" or immutable log versus erasure. Q24.
> Concede: an immutable ledger is exactly where erasure fails. Finck’s analyses set out that tension, and the systematic review of 114 papers puts the right to be forgotten first among the difficulties. Then: the design takes the one property a chain would add, tamper evidence, from a Merkle log with RFC 6962 hashing, the Certificate Transparency construction, with logarithmic inclusion proofs. The leaves hold accessor fields, the payload commitment, a salted subject commitment and invalidation entries, never the payload or subject fields, so the log never needs rewriting [corrected: was "so nothing on the log needs erasing"]. If asked about anchoring roots: consistency proofs need earlier roots published or countersigned (§4.9); the artefact implements inclusion proofs only, and where roots are published is a deployment choice the thesis does not make. Redactable blockchains and chameleon hashes give a key holder the power to rewrite, a trust assumption this design avoids. Norway has a clinical precedent: NewbornTime, a Hyperledger consent platform at Stavanger University Hospital (§2.4).

Links: §2.4 p. 21 (review p. 24); §4.8 p. 66; §4.9 p. 69. App ?p=built.

### Slide 19. Where is the SNARK? (q-snark)
**Open when:** "VERA-SNARK, where is the SNARK?" or any zero-knowledge question. Q43.
> Concede: the mechanism contains no SNARK. The name is kept for continuity with the NORS 2025 presentation, and the thesis says so. Then: once the three regimes were formalised, a hiding commitment, an attributed invalidation entry and a tamper-evident log were enough. Dropping the heavier machinery is the design-science cycle doing its job. The problem that does need zero knowledge is in §7.5: when the patient exercises Article 17, an auditor should be able to confirm that every one of her records was invalidated, but listing them would reveal her cross-border care history. Proving completeness without revealing the set is a zero-knowledge problem and future work. Comparator if asked: Albalwy (2026) uses a Groth16 zk-SNARK so a patient, doctor or researcher can prove policy-compliant credentials for cross-institutional sharing within one jurisdiction; it does not address retention.

Links: Statement of Contribution p. x; §1.6 p. 9; §7.5 p. 107.

### Slide 20. Where is the logistics? (q-logistics)
**Open when:** "This is a logistics degree" or "where is the energy". Q39, Q40.
> Concede: no optimisation, and no energy saving. Then: information is part of logistics flow and storage. A cross-border audit record is generated at one node, travels a six-step gateway protocol, comes to rest in a repository governed by one authority, and is bound by obligations from another jurisdiction. The borrowing is specific: customs law already keeps the record of goods after the goods are ordered destroyed, and separating the record from the thing recorded is the move of Chapter 4. Proposition 3 reads in the idiom of perishable inventory with two clocks (Nahmias, 1982). The energy sector schedules retention the same way: Elhub keeps customer data three years and 41 days after contracts end (§2.7). My four years in cross-border procurement across DACH, India and the UAE is where the framing comes from. Do not say logistics is broadly about flows; that sounds retrofitted.

Links: §1.4 p. 7; §1.5 p. 8; §2.7 pp. 30 to 31. App ?p=anchor.

### Slide 21. Does Art 68(12) reach the logs? (q-reading)
**Open when:** "Are the researcher's access logs data within the environment?" Q9. If pressed, add the third, harmonising reading (§4.6 p. 59): the ceiling yields to the floor.
> Concede immediately: the reading is contestable, and the thesis says so where it is used. The provision sits in the data-permit article, and a narrower construction confines it to the dataset made available under the permit. The broad reading rests on the text: its scope is set by location rather than provenance; it does not say “the data made available under the data permit”. Its object is electronic health data, and an entry kept at patient-record granularity reveals cohort membership, which is data concerning health. Then the map: reject the broad reading and you lose Corollary 1.2 and the conditional branch of Corollary 2.3. Everything else stands, and the researcher’s log then collides only through an erasure request, as the patient’s does. Do not say the Commission will clarify it.

Links: §4.6 pp. 58 to 59; §4.4 p. 54; §3.7 p. 44; §7.4 p. 106. App ?p=witness&r=100&m=16.

### Slide 22. Who endorses Semantics II? (q-authority)
**Open when:** "Your own definition; why would a regulator accept it?" Q10.
> Do not defend it as settled law. The EDPB Guidelines 02/2025, paragraph 51, say that once the key is deleted the data are unintelligible, at least until the algorithm is broken, and in the same paragraph that encrypted personal data are still personal data; paragraph 125 says an erasure request needs the data erased or rendered anonymous. So the Board describes what key deletion achieves without classifying it as erasure, which is why the mechanism deletes the payload from the store and relies on keys only for copies that cannot be deleted at once. The further condition that the controller document its threat model is Aikebaier’s interpretation, not the Board’s. Nothing says an invalidated record discharges a retention obligation: that is my argument from Article 17(3)(b), Article 5(1)(c) and the accountability purpose. Whether an authority accepts it is open, and I have put it to Datatilsynet. Do not say the EDPB endorses it.

Links: §4.2 p. 49; §4.9 pp. 68 to 70; §6.2 p. 92; §7.4 p. 106.

### Slide 23. Are the permits realistic? (q-permits)
**Open when:** "Permits of one to twelve months?" or "45 per cent". Q31, Q29.
> Concede the empirical gap plainly. Then the substance: a longer permit moves the ceiling later, so fewer records like the researcher’s collide, but Proposition 1 is stated for records whose deadline falls inside the window and is silent on the others. The 90 of 200 is a property of the generated population, and Chapter 5 says so in the same paragraph. Corollary 1.2’s fifty per cent follows directly from the permit draw: the collision occurs when the permit expiry plus six is within the floor, the condition of Proposition 3(ii) with F = 12 and L = 6. Tripling the response period from one month to three moves 95 violations to 94. Do not say the range is representative.

Links: §3.7 p. 44; §5.3 p. 83; §5.4 p. 85; §5.6 p. 87. App ?p=robust.

### Slide 24. Why believe informal proofs? (q-proofs)
**Open when:** "Your proofs are informal" or "break them". Q15, Q30.
> The proofs are informal in presentation and constructive in substance. Proposition 1: in the patient’s month 116 one constraint needs alpha equal to one and another needs zero, and no assignment satisfies both. Proposition 2 is proved by building the trajectory and checking the three constraints against it. You do not have to believe the prose. The brute-force function is written separately from the checker and shares only two constants; a test compares the two on 31 cases, including every boundary month of a twelve-month window. Z3 poses each proposition as a search for a counterexample, with floors up to 120 months, and finds none; it does find counterexamples to constructions without the invalidation entry or the commitment, and to an off-by-one Proposition 3. Do not say it was formalised in a proof assistant.

Links: §4.6 p. 57; §4.7 p. 60; §5.5 pp. 85 to 86; A.23 p. 150; A.24 p. 153. App ?p=propositions.

### Slide 25. Can you prove key destruction? (q-keys)
**Open when:** "You cannot prove the key was destroyed" or "what does an HSM give you". Q25.
> Agree first; the thesis says so in several places. The optional envelope module does use real AES-256-GCM per-record keys, and exactly the invalidated records refuse to decrypt through custody, but the custody object stands in for a hardware security module, so destruction there is destruction in program memory. In the specification the store deletes the payload, its key and its salt; key destruction matters for copies such as backups, which become unreadable and leave by rotation. The trust assumptions are named in §4.9. Reardon and colleagues show that the further an approach operates from the storage medium, the harder it is to assert that destruction occurred; cryptographic erasure is the limiting case. Certified deletion protocols are where proof could come from, and their public verifiability is open.

Links: §4.8 p. 63; §4.9 p. 69; §6.3 p. 94; §7.5 p. 107; A.15 p. 142; A.22 p. 149. App ?p=robust.

### Slide 26. Are the synthetic patients American? (q-synthea)
**Open when:** "Your synthetic data are American" or "realism". Q31.
> Agree: the generator is American by default, and the thesis does not imply otherwise. The data are genuine Synthea output, generated on Linux. Two points carry the answer. First, FHIR R4 is the version HL7 Norway’s basisprofiler constrain. Second, and decisive: the model never reads payload content; it reads when things happen and whether the payload can be read. Replacing the constructed payload strings with Synthea FHIR R4 resources changed all two hundred commitments and no reported figure, on the subset and on the full-cohort rerun in Appendix A.17. So the nationality of the synthetic patients cannot move any result.

Links: §3.5 pp. 41 to 42; §5.2 p. 79; Table 5.7 p. 90; A.17 p. 145. App ?p=synthea (needs the bundles; else docs/expected_synthea_full_cohort_rerun_2026-10-06.txt).

### Slide 27. Is what remains anonymous? (q-residue)
**Open when:** "Is the residue anonymous?" or identifiability. Q11.
> Say no, plainly; §4.9 says any claim of anonymisation would be false. What survives identifies the accessor, the clinician, and is pseudonymised as to the patient. Datatilsynet’s guidance holds that data are not anonymous while any key or linkage capable of re-identification is retained, and the EDPB’s draft Guidelines 02/2026 on anonymisation, adopted for consultation in July 2026, set the same bar. Then: the applicable test is erasure, and the store meets it by deleting the payload, its key and its salt. The salted commitment stops anyone confirming a guessed payload. Only the terminal transition after the floor aims at a non-identifiable residue, and whether it resists isolation, linkage and inference is for the documented threat model. The artefact does not implement it.

Links: §4.8 p. 67; §4.9 pp. 68 to 69. App ?p=witness&r=100&m=19.

### Slide 28. Why not delete and log it? (q-rival4)
**Open when:** "Delete the record and log that you deleted it. Why more?" Q28.
> Concede first. For cross-border records, where the patient link is kept through the floor and nobody is handed an opening, “delete the record and log the deletion” is close to an equivalent design. It fails C1 under Semantics II only because there is no commitment, which is true by definition. What the design adds is three things: the invalidation entry is attributed and grounded; it is bound tamper-evidently with the access record; and the commitment detects substitution of one record’s payload for another’s before invalidation, and afterwards wherever an opening was handed to the patient or the home contact point. In the Secure Processing Environment case it does work deletion cannot. The weight of the thesis lies in the semantics and the necessity analysis, not the commitment.

Links: §4.10 p. 71 (Rival 4); §4.5 p. 56; §4.8 p. 65. App ?p=witness&r=3&m=116.

### Slide 29. Can the operator rewrite the log? (q-roots)
**Open when:** "The operator controls the Merkle log." Q23.
> Concede: on its own, nothing does, and the thesis says so. The artefact checks inclusion proofs against a root recomputed from the log’s own leaves. Three tamper tests show what that catches: an altered accessor field, an altered legal ground, an altered patient link, each makes the Semantics II check fail. It does not catch a wholesale rewrite. That needs consistency proofs between an earlier root and the current one, with earlier roots published or countersigned outside the operator’s control, as in Certificate Transparency. Those are specified, not implemented. The operator is named in the trust assumptions: alteration is detectable but not impossible. What does hold: once a root containing an invalidation entry is published, the claim cannot be withdrawn.

Links: §4.9 p. 69; §5.7 p. 88; Table 4.1 p. 74; §6.1 p. 91; §6.3 p. 94. App ?p=run.

### Slide 30. Why not export the logs? (q-props34)
**Open when:** "Just export the logs at permit closure" or anything on Proposition 3 or 4. Q19, Q18.
> Concede the ceiling: the thesis accepts export as a sufficient answer to Corollary 1.2. It does not answer the erasure right. Proposition 4: the ceiling binds a location, the right binds whichever controller holds the data. On the stated legal premise that a receiving controller receives the Article 17 duty with the record, relocation leaves C1 against C2 exactly as before. It also moves the subject fields to a second controller rather than reducing them. Proposition 3 explains why the SPE collision is invisible in the text. The ceiling, six months from permit expiry, is anchored to a different event from the floor, twelve months from the entry, so only each record’s history shows the clash. Politiregisterloven section 17, a longer ceiling from the same event, produces none.

Links: §4.10 pp. 71 to 72; §4.6 p. 60; §6.10 p. 100. App ?p=anchor.

### Slide 31. Is it real, and what does it cost? (q-adoption)
**Open when:** "Is this a real problem today, who would adopt it, what does it cost?" Q2. Privacy-notice follow-up: Q36.
> Concede: not yet operative. Articles 68 and 73 apply from 26 March 2029, and Norway’s contact point is in live pilot with no relevant patient when the Directorate last reported. That timing is the argument: the implementing acts for Secure Processing Environments are due 26 March 2027, so the design can be specified before infrastructure hardens. On cost, SecuPi’s critique is correct on its own terms: per-record keys are a real burden. But it falls on audit records, not clinical stores; live keys shrink as invalidations accumulate; and an inclusion proof grows as log two of n, some thirty hashes for a billion entries. None of this is measured, and no performance claim is made. The cheapest adoption step is the invalidation entry alone, which section 6.8 says costs little. Not in the thesis [corrected: was "Since submission"; the notice is dated 30 June 2026, before submission, and the thesis does not cite it], one public anchor: the Directorate's privacy notice, revised 30 June 2026, states that the MyHealth@EU search-and-view log keeps the health professional's name, HPR number, role, institution type, place and time of lookup for six years, under GDPR Article 6(1)(c) and pasientjournalloven section 22, with the Directorate as controller and Norsk helsenett as processor. That is the accessor evidence my mechanism keeps; the patient payload is what it lets go.

Links: §6.4 p. 95; §6.5 p. 96; §6.8 p. 98; §2.2 p. 15; Appendix D p. 168. App ?p=norway.


---

## Timing

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
