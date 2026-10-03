# Appendix C. Expert Evaluation Instrument

*(v1, 18 September 2026. The instrument specified here was designed following supervisory feedback of September 2026 and constitutes the evaluation design for the next iteration of the design science cycle. Its execution status is stated in Chapter 3, Section 3.8. **This is a design, not a fielded instrument. Section C.1a states what is expected to change once it meets real respondents.**)*

---

## C.1 Purpose and status

Chapter 3, Section 3.7 sets out the analytical evaluation strategy adopted for this thesis: internal validity through logical consistency and executable checking, external validity through compatibility analysis against verified infrastructure, and reliability through deterministic execution. That strategy evaluates the artefact against the objectives stated in Chapter 1, Section 1.3, and it is the evaluation the thesis reports.

It does not collect stakeholder input. Design Science Research as elaborated by Hevner, March, Park, and Ram (2004) and Peffers, Tuunanen, Rothenberger, and Chatterjee (2007) treats evaluation as an activity that may be conducted through several methods, of which expert assessment is one, and a specification-and-demonstration study of the kind reported here frequently designs the evaluation that a subsequent cycle executes. This appendix is that design.

The instrument is specified in sufficient detail to be executed without further design work: panel composition and recruitment approach, session structure, demonstration script, semi-structured interview guide, a closed-response questionnaire, the analysis approach, and the data-protection arrangements execution would require. The four closed-response dimensions follow the structure proposed in supervisory feedback and are reproduced with their anchor statements intact.

---

## C.1a Status of this instrument, and what is expected to change

An instrument that has never been administered is a hypothesis about what respondents will
understand, not a measurement device. This one has been reviewed by a supervisor and
reasoned through against the thesis's claims; it has not been piloted, and no respondent
has yet tried to answer it. The distinction matters for how its results should be read if
it is executed, and it is stated here rather than discovered afterwards.

The following are expected to change, and changing them would not constitute a departure
from the design:

*Wording of the closed-response items.* The four dimensions and their anchor statements are
reproduced as proposed in supervisory feedback, with one already known to overstate what
the thesis claims: item A1 asserts that the mechanism gives auditors *full confidence*,
which Chapter 6, Section 6.3 explicitly does not claim. It is retained verbatim because it
was proposed as the anchor and because silently correcting a supervisor's wording would
misrepresent the record. A pilot is the proper place to resolve it.

*The panel.* Eight participants across four perspectives is a target, not a recruitment
outcome. Norwegian health-data governance is a small professional community and some of
the roles sought are held by very few people. If a perspective cannot be filled, the
analysis reports which voice is missing rather than redistributing its weight silently.

*Session length and the demonstration script.* Forty-five minutes is an estimate. The
demonstration walks through a live artefact, and the first session will establish whether
the script fits the time or whether the closed-response section must move to a follow-up.

*The coding frame.* The three areas derived from supervisory feedback (legal defensibility,
key custody and trust assumptions, operational viability) carry an open category precisely
because the frame is expected to be incomplete. Themes that recur outside it are a finding
about the frame, not noise to be forced into it.

*What would not change.* The instrument's purpose is to test whether practitioners find the
artefact defensible, not to elicit endorsement. Items are not to be reworded toward
agreement if early responses are unfavourable, and an unfavourable result is reportable as
a result. Any revision made after piloting is to be recorded with its reason, and the
version of the instrument actually administered is to be reproduced in the thesis that
reports it, rather than this one.

Should the evaluation be executed, this appendix stands as the pre-registered design
against which any subsequent version can be compared.

---

## C.2 Panel composition

Eight participants across four perspectives, two in each, chosen so that no single professional viewpoint dominates and so that legal, architectural, operational, and disciplinary assessments are each represented by more than one voice.

| # | Perspective | Profile sought | Assesses |
|---|---|---|---|
| P1, P2 | Data protection | Data Protection Officer or privacy counsel in a Norwegian health or research institution | Whether invalidation is defensible as satisfying retention; whether the surviving residue clears the anonymity threshold; the Article 68(12) scope question |
| P3, P4 | Health IT architecture | Architect or senior engineer at Norsk Helsenett or Helsedataservice with NCPeH or HDAB exposure | Whether the mechanism attaches at the right boundary; interoperability consequences; effect on the OpenNCP transmission flow |
| P5, P6 | Secure Processing Environment operation | Operator or technical lead at a NORTRE node (TSD, SAFE, or HUNT Cloud) | Key custody in practice; operational burden of per-record granularity; single-point-of-failure risk absent hardware security modules |
| P7, P8 | Information logistics | Academic or practitioner in logistics or supply-chain compliance | Whether the customs-ledger framing holds; transferability of the tri-lateral structure to other regulated flows |

Recruitment would proceed by direct approach through institutional channels, with the supervisor's introduction where available. A minimum of six completed sessions, with at least one from each perspective, would be treated as the threshold for reporting; below that the results would be reported as indicative commentary rather than as evaluation.

---

## C.3 Session structure

Forty-five minutes, conducted in Norwegian or English at the participant's preference, remotely or in person.

| Minutes | Segment | Content |
|---|---|---|
| 0–5 | Framing | Purpose, voluntariness, recording and anonymity arrangements, participant's right to withdraw. No thesis conclusions stated at this point. |
| 5–12 | Problem presentation | The three retention regimes and their sources, presented from the primary instruments without the thesis's resolution. Participants are asked how their institution currently handles the conflict, before being shown any proposed answer. |
| 12–22 | Demonstration | Live execution of the feasibility checker (Section C.4). |
| 22–35 | Semi-structured discussion | Interview guide, Section C.5. |
| 35–43 | Closed-response instrument | Questionnaire, Section C.6, completed by the participant. |
| 43–45 | Close | Opportunity to add anything not asked; follow-up arrangements. |

The ordering is deliberate. Participants describe current practice before seeing the proposed mechanism, so that their account of the status quo is not shaped by the solution. The closed-response instrument follows the open discussion so that numerical responses are informed rather than first impressions.

---

## C.4 Demonstration script

The demonstration runs the artefact rather than describing it. Approximately ten minutes.

1. *Show the record structure.* One audit record: metadata, payload, commitment, key. Identify which parts the accountability purpose needs and which it does not.
2. *Run the checker under plaintext semantics.* `python3 trf_checker.py`. Show the output: ninety-five violations across ninety of two hundred records. Open one witness line and walk through the arithmetic: the collision month, the two constraints, the window.
3. *Isolate the Corollary 1.2 cases.* Thirty-nine Secure Processing Environment records with no erasure request at all. Show record 100: created month 7, permit expires month 10, ceiling from month 16, floor to month 19. State the interpretive condition (Chapter 4, Section 4.6) explicitly rather than glossing it.
4. *Show the exhaustive cross-check.* Sixteen thousand three hundred and eighty-four assignments per case; no satisfying assignment in the three conflict cases; the control case passes.
5. *Run under invalidation semantics.* Zero violations. Show the auditor's view of record 100 after invalidation: metadata intact, commitment present, key destroyed, invalidation entry with month and legal ground, payload unreadable.
6. *State the limits before being asked.* Key destruction is simulated in program state; the invalidation entry is an attestation, not a proof; no National Contact Point is connected; no performance claim is made.

Step 6 is not optional. A demonstration that presents only strengths invites participants to spend their time finding the weaknesses instead of assessing the design.

---

## C.5 Semi-structured interview guide

Thirteen questions across four themes. Prompts are used only where a participant's answer is brief; the guide is not a script to be read verbatim.

### Current practice and problem recognition

1. How does your institution currently handle a request to erase personal data that is also subject to an audit-retention obligation? Is there a documented position, or is it decided case by case?
2. Before today, had you encountered the interaction between Article 68(12) and Article 73(1)(e)? *(Prompt: if not, does it look like a real problem or an artefact of how it has been presented?)*
3. Where in your organisation would responsibility for resolving this sit?

### Legal defensibility

4. The mechanism treats an audit record as verifiable when its metadata is intact, its commitment survives, and the invalidation is logged: without the payload remaining readable. Is that defensible as satisfying a retention obligation, in your judgement?
5. What would a supervisory authority need to see before accepting it?
6. The surviving residue is characterised as pseudonymised rather than anonymous. Does that characterisation match your reading of the Norwegian threshold?
7. Article 68(12) provides that "the electronic health data within the secure processing environment shall be deleted within six months of the expiry of the data permit." Does that reach access logs kept at patient-record granularity, or only the dataset supplied under the permit? And does auditing "all processing operations" under Article 73(1)(e) after that point need the link to the patient, or only the identity of the person who accessed?

### Trust and key custody

8. The invalidation entry attests that a key was destroyed; it does not prove it. Is attestation sufficient in your operating context, and if not, what would make it sufficient?
9. Where would key custody sit in your architecture, and what failure modes concern you most?
10. Does per-record key granularity create a single point of failure you would be unwilling to accept without hardware-backed attestation?

### Operational viability

11. What would implementing this at your institution actually require: systems, process, people?
12. At what record volume would the per-record key registry become a problem?
13. What would you change about the design before deploying it?

Question 7 is included because the thesis's sharpest result depends on the answer, and practitioner readings of it are evidence this author cannot generate.

---

## C.6 Closed-response questionnaire

Five-point Likert scale throughout: 1 = strongly disagree, 2 = disagree, 3 = neither agree nor disagree, 4 = agree, 5 = strongly agree. A sixth option, *not able to judge*, is offered on every item and is reported separately rather than treated as a midpoint.

Each dimension opens with the anchor statement proposed in supervisory feedback, reproduced verbatim, followed by items that decompose it.

### Dimension 1: Perceived utility

| Item | Statement |
|---|---|
| U1 | *The key-invalidation mechanism effectively resolves the conflict between retention floors and erasure ceilings.* |
| U2 | The problem this mechanism addresses is one my institution will face in practice. |
| U3 | The mechanism addresses the problem more effectively than the approach my institution currently uses or would default to. |
| U4 | The distinction between plaintext verifiability and accountability-preserving verifiability is one I had not previously considered explicitly. |

### Dimension 2: Regulatory alignment

| Item | Statement |
|---|---|
| R1 | *The residual audit log provides sufficient verification without violating GDPR Article 17 or EDPB guidelines.* |
| R2 | The surviving residue — metadata, commitment, invalidation entry — would be defensible to a supervisory authority. |
| R3 | Article 68(12) should be read as reaching the access logs generated within a Secure Processing Environment. |
| R4 | The mechanism's characterisation of its residue as pseudonymised rather than anonymous is the correct characterisation. |

### Dimension 3: Operational viability

| Item | Statement |
|---|---|
| O1 | *The proposed key registry structure is practical to implement within current Norwegian health data infrastructure (SPUHiN / NORTRE).* |
| O2 | Per-record key granularity is operationally sustainable at the record volumes my institution handles. |
| O3 | The mechanism requires nothing of the processing environment beyond what the finalised national criteria already demand. |
| O4 | Placing the mechanism at the audit-logging boundary, rather than inside the processing environment, is the right architectural choice. |

### Dimension 4: Audit integrity

| Item | Statement |
|---|---|
| A1 | *The cryptographic proof gives auditors full confidence that data was lawfully deleted at the required timestamp.* |
| A2 | An attested invalidation entry, without hardware-backed proof of key destruction, is sufficient for audit purposes in my context. |
| A3 | The mechanism provides stronger audit assurance than deleting the record and logging that a deletion occurred. |
| A4 | An external auditor could establish, from the surviving record alone, what was invalidated and on what legal ground. |

### Open items

| Item | Prompt |
|---|---|
| X1 | The single change you would most want made to the design. |
| X2 | The assumption in the design you consider least safe. |
| X3 | Anything the questions above did not ask about. |

A note on item A1. The anchor statement asserts that the mechanism gives auditors *full confidence*, which the thesis itself does not claim: Chapter 6, Section 6.3 states that the invalidation entry is an attestation rather than a proof. The item is retained verbatim because it was proposed as the anchor and because disagreement with it would be an accurate response rather than a failure of the instrument. Item A2 exists to capture that distinction directly, and analysis would read A1 and A2 together rather than A1 alone.

---

## C.7 Analysis

Closed responses would be reported as medians with full distributions rather than means, given ordinal data and a panel of eight; no inferential statistics would be computed, and none would be meaningful at this size. *Not able to judge* responses would be reported by item, since a concentration of them is itself a finding about which audiences can assess which dimensions.

Open responses and interview transcripts would be analysed thematically following a coding frame derived from the three areas supervisory feedback identified (legal defensibility, key custody and trust assumptions, operational feasibility) with an open category for themes not anticipated. Coding by a single researcher would be stated as a limitation, as it is for the literature review in Chapter 2, Section 2.1.7.

Integration into the thesis would follow the design science cycle rather than being appended to it:

*Misalignments* between the design and operational reality would be documented as findings, not smoothed over. If Secure Processing Environment operators identify key custody as a single point of failure absent hardware security modules, that becomes a stated limitation of the mechanism and a design requirement for the next iteration.

*Assumption revision.* Legal responses to items R2, R3 and R4, and to interview questions 4 through 7, would revise the trust model and the residue analysis of Chapter 4, Section 4.9: in particular whether attestation of key destruction is treated as adequate.

*Future iterations.* Responses to A2 would inform whether the next design iteration should move from software-attested key destruction to hardware-backed attestation through a hardware security module or secure enclave, which Chapter 7, Section 7.5 already identifies as the direction in which the assurance boundary would move.

Disconfirming responses would be reported with the same prominence as confirming ones. An evaluation that can only strengthen the artefact is not an evaluation.

---

## C.8 Data protection, if executed

Execution would process personal data about identifiable professionals and would therefore require notification to Sikt (Norwegian Agency for Shared Services in Education and Research) before any participant is approached. Typical processing time is four to six weeks.

The arrangements would be: written information and consent obtained before each session; audio recording only with consent, transcribed and the recording deleted on transcription; participants identified in reporting by perspective and number only (P1 through P8), with institutions named only where a participant expressly agrees; no special-category data collected; storage on institutional infrastructure for the duration of the project and deletion on completion; and withdrawal permitted at any point up to the completion of analysis.

Executing this instrument would change the thesis's ethics position materially. Chapter 1, Section 1.5, Chapter 3, Section 3.8, and the Declaration of Originality each state that this research involves no human participants and required no ethical approval. Those statements are accurate for the thesis as submitted and would require revision if the instrument were executed. This appendix does not revise them.

---

## References (Appendix C)

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly*, *28*(1), 75–105.

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems*, *24*(3), 45–77.
