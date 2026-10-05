# P53 — PRES-2 (voice, hooks, readability) for Chapters 4 and 6, and M6a: the SPUHiN draft's logging
# requirements (P13, P14, P24, P31; SPUHiN, 2024, read 5 Oct 2026 at the helsedata.no URL in the
# reference list) traced in §4.11 and Table 4.1. Hooks open sections; long sentences are split.
# No claim, citation, number or hedge is removed.
C4 = 'Chapter4_TRF_Model_v1.md'
C6 = 'Chapter6_Discussion_v1.md'
E = []
def e(i, f, old, new, why):
    E.append(dict(id=f'P53-{i:02d}', file=f, old=old, new=new, why=why))

# ---------- Chapter 4 ----------
e(1, C4, "This chapter contains the analytical core of the thesis. It does three things in sequence, and the sequence matters because each step licenses the next.",
  "A patient asks for her data to be erased. The audit record of who looked at them must, on the reported deployment baseline, stay verifiable for ten years. In a research environment a third rule wants the data gone six months after the permit ends. Can one record obey all three? This chapter answers: not if verifiable means readable; yes if it means accountable. It gets there in three steps, and each step licenses the next.",
  'PRES-2 hook')
e(2, C4, "The decomposition that makes the model possible is not a modelling convenience. It is derived from",
  "Everything in this chapter rests on one split: the part of an audit record the law needs kept, and the part it does not. The split is not a modelling convenience. It is derived from",
  'PRES-2 hook')
e(3, C4, "within the meaning of Article 17(3)(b), and an erasure request reaches the payload but not the link, at least",
  "within the meaning of Article 17(3)(b). An erasure request then reaches the payload but not the link, at least",
  'PRES-2 split')
e(4, C4, "Let the time domain be discretised into months,",
  "The model is deliberately small: one record, one clock, and one question asked every month: can the payload still be read?\n\nLet the time domain be discretised into months,",
  'PRES-2 hook')
e(5, C4, "Each regime is now expressed as a constraint on the trajectory of $\\alpha$ and $V$.",
  "Each regime now becomes a constraint on the trajectory of $\\alpha$ and $V$: one floor that says how long a record must last, and two limits that say how soon its payload must go.",
  'PRES-2 hook')
e(6, C4, "## 4.5 Two Semantics of Verifiability\n\n",
  "## 4.5 Two Semantics of Verifiability\n\nEverything now turns on one undefined word: verifiable. Two definitions are available, and the propositions show that they lead to opposite answers.\n\n",
  'PRES-2 hook')
e(7, C4, "stored every received audit message whole, in a database column for the message content, with the patient identifier in a readable column and a further column for the participant-object query; it refused to modify a stored message, and its audit code",
  "stored every received audit message whole, in a database column for the message content. The patient identifier sat in a readable column, and a further column held the participant-object query. The repository refused to modify a stored message, and its audit code",
  'PRES-2 split')
e(8, C4, "## 4.6 Propositions 1 and 3: Infeasibility, and Where the Ceiling Is Anchored\n\n",
  "## 4.6 Propositions 1 and 3: Infeasibility, and Where the Ceiling Is Anchored\n\nUnder Semantics I the conflict is not bad luck or rare timing. It is a contradiction, and it can be located to the month.\n\n",
  'PRES-2 hook')
e(9, C4, "## 4.7 Proposition 2: Feasibility under Accountability-Preserving Verifiability\n\n",
  "## 4.7 Proposition 2: Feasibility under Accountability-Preserving Verifiability\n\nChange what verifiable means and the contradiction disappears, for every record, every pattern of requests and every floor. The proof builds the trajectory that does it, and that trajectory is the mechanism.\n\n",
  'PRES-2 hook')
e(10, C4, "The objection has force and the response is to concede its premise and deny its conclusion.",
  "The objection has force. The response concedes its premise and denies its conclusion.",
  'PRES-2 split')
e(11, C4, "The trajectory constructed in the proof of Proposition 2 is the specification of the mechanism. This section states it as an implementable design.",
  "The proof of Proposition 2 is also a build sheet: the trajectory it constructs is the specification of the mechanism. This section states it as an implementable design: what is encrypted, what is committed, what is destroyed, and what is logged when it is.",
  'PRES-2 hook')
e(12, C4, "Proposition 2 leaves a residue:",
  "A mechanism that erases by destroying keys is only as good as what it leaves behind. Proposition 2 leaves a residue:",
  'PRES-2 hook')
e(13, C4, "Six alternative designs are considered. Five are rejected",
  "If a simpler design solved the problem, this mechanism would be unnecessary. Six alternative designs are therefore tested against it. Five are rejected",
  'PRES-2 hook')
e(14, C4, "The mechanism is specified against the Norwegian infrastructure as verified in Chapter 2, Section 2.6, not against an idealisation of it.",
  "A mechanism is only as useful as the point at which it can be installed. This one is specified against the Norwegian infrastructure as verified in Chapter 2, Section 2.6, not against an idealisation of it.",
  'PRES-2 hook')
e(15, C4, "and require eID-based authentication at defined assurance levels (SPUHiN, 2025). The mechanism requires nothing beyond these:",
  "and require eID-based authentication at defined assurance levels (SPUHiN, 2025). The November 2024 draft is specific on logging. It makes tamper-proof, identifiable logs of access to the environment mandatory \"for at least one year\" (P13), and likewise logs of when files are extracted and by whom, kept for one year (P24); it recommends tamper-proof, identifiable logs of activities inside the environment (P14); and it lists back-up and log files among the matters a termination procedure must cover (P31) (SPUHiN, 2024; requirement numbers as in the draft). That is the one-year floor of Article 73(1)(e) in national form. None of the requirements inspected says how those logs are to be reconciled with deletion. The mechanism requires nothing beyond these:",
  'M6a: SPUHiN draft logging requirements')
e(16, C4, "| Reconciliation of log retention with deletion | SPUHiN (2025), hearing version |",
  "| Tamper-proof, identifiable logs of access to the SPE, at least one year (mandatory); of file extraction, one year (mandatory); of activities (recommended) | SPUHiN (2024), draft, P13, P24, P14 | Accessor fields kept identifiable for the floor; every access event in the append-only Merkle log | §4.3, §4.8; `MerkleLog` | Met in the artefact ($F = 12$; both tamper tests fail $V^{II}$) |\n"
  "| Termination procedure covering deletion of files, back-ups and log files (mandatory) | SPUHiN (2024), draft, P31 | Supplies the rule for the log files: invalidation at the ceiling, terminal transition after the floor | §4.8 | Met by specification; the terminal transition is not implemented (§6.1) |\n"
  "| Reconciliation of log retention with deletion | SPUHiN (2025), hearing version |",
  'M6a: SPUHiN draft rows')

# ---------- Chapter 6 ----------
e(17, C6, "The thesis establishes that the conflict between audit-retention floors",
  "Read one way, three obligations cannot be met together. Read another, they can. The thesis establishes that the conflict between audit-retention floors",
  'PRES-2 hook')
e(18, C6, "The second objection is the one the thesis has carried since Chapter 2, and it is the ceiling of the contribution.",
  "Nobody can watch a key being destroyed. That is the second objection, the one the thesis has carried since Chapter 2, and it is the ceiling of the contribution.",
  'PRES-2 hook')
e(19, C6, "SecuPi (2025) argues that cryptographic erasure introduces operational complexity in row-level encryption scenarios, that",
  "Per-record keys cost something, and the question is whether the cost is worth paying. SecuPi (2025) argues that cryptographic erasure introduces operational complexity in row-level encryption scenarios, that",
  'PRES-2 hook')
e(20, C6, "The evaluation reported in this thesis is analytical, and Section 3.7 states its criteria.",
  "A model can be right and still be refused by the people who would have to run it. The evaluation reported in this thesis is analytical, and Section 3.7 states its criteria.",
  'PRES-2 hook')
e(21, C6, "Substituting real FHIR R4 resources for constructed payload strings",
  "The patients in this thesis do not exist, and no result depends on who they are. Substituting real FHIR R4 resources for constructed payload strings",
  'PRES-2 hook')
e(22, C6, "The timing argument is the strongest claim to practical relevance this thesis makes.",
  "The provisions that create this collision do not yet apply, and that is the opportunity. The timing argument is the strongest claim to practical relevance this thesis makes.",
  'PRES-2 hook')
e(23, C6, "The thesis establishes that audit-retention floors, the right to erasure and the deletion ceiling conflict only under an assumption about verifiability, and not because of the obligations themselves; that, on the broad reading of Article 68(12) and for logs kept at patient-record granularity, the conflict arises inside the European Health Data Space Regulation with no data subject acting; that a ceiling collides with a floor exactly when Proposition 3 says, and that relocation escapes the ceiling but not the right (Proposition 4).",
  "The thesis establishes four things. Audit-retention floors, the right to erasure and the deletion ceiling conflict only under an assumption about verifiability, and not because of the obligations themselves. On the broad reading of Article 68(12) and for logs kept at patient-record granularity, the conflict arises inside the European Health Data Space Regulation with no data subject acting. A ceiling collides with a floor exactly when Proposition 3 says. And relocation escapes the ceiling but not the right (Proposition 4).",
  'PRES-2 split')
EDITS = E
LOST_OK = []
