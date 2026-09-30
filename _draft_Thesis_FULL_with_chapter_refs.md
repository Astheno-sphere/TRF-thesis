# Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the European Health Data Space

Arshad Akhtar Abbasia, MSc Sustainable Energy Logistics, Høgskolen i Molde

Supervisor: Prof. João Ferreira. Assembled 18 September 2026.

Artefact: https://github.com/Astheno-sphere/TRF

Demonstration: https://trfhimolde.streamlit.app/

---

# Front Matter

*(v1, 18 September 2026. Written fresh for the rebuilt thesis. No element of this front matter derives from the May 2026 draft, whose abstract, contribution statement, and ethics declaration are superseded in their entirety.)*

---

## Title Page

**Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the European Health Data Space**

*A Design Science Study of the Tri-Lateral Retention Feasibility Problem in the Norwegian Implementation Context*

Arshad Akhtar Abbasia

Master of Science in Sustainable Energy Logistics
Faculty of Logistics, Høgskolen i Molde — Vitenskapelig høgskole i logistikk

Supervisor: Prof. João Ferreira

Molde, November 2026

---

## Abstract

The European Health Data Space Regulation (EU) 2025/327 places cross-border health data audit records under three kinds of retention obligation simultaneously. Audit-retention floors require records to remain verifiable for fixed periods: ten years for MyHealth@EU audit repositories under the eHDSI deployment baseline, one year for Secure Processing Environment access logs under Article 73(1)(e). The right to erasure under Article 17 GDPR may be exercised at any point within those periods. And Article 68(12) EHDS requires data to be deleted from a Secure Processing Environment within six months of the expiry of a data permit. No instrument reconciles the three, the guidance drafted to implement them does not address their interaction, and the Commission implementing acts that must specify Secure Processing Environment requirements are not due until 26 March 2027.

This thesis formalises that conflict and resolves it by design. It develops the Tri-Lateral Retention Feasibility (TRF) Model, a constraint-satisfaction formulation in which each audit record is decomposed into event metadata and a committed personal-data payload, the three obligations are expressed as constraints over discretised time, and the semantics of *verifiability* is made an explicit parameter rather than an inherited assumption. Two results follow. Under plaintext-verifiability semantics, a record is verifiable while its payload remains readable, the constraint system is infeasible whenever an erasure deadline or a deletion-ceiling deadline falls inside a retention window. Under accountability-preserving semantics — a record is verifiable while its metadata is intact, its commitment survives, and any loss of payload accessibility is itself logged, grounded, and attributed: the system is jointly satisfiable for every arrival pattern of erasure requests and permit expiries and for every retention floor.

The mechanism that the feasibility proof exhibits, termed Crypto-Erasure by Invalidation, applies the cryptographic-erase technique recognised in NIST SP 800-88 Rev. 2 at the audit-trail boundary: the per-record key binding a record to its payload is destroyed, hiding commitments and event metadata are retained, the invalidation is appended to the audit trail as a first-class witnessed event, and a terminal transition at floor expiry discharges the storage-limitation obligation on the metadata itself.

Both results are demonstrated in a Python sandbox over two hundred records drawn from Synthea-generated FHIR R4 data. Under plaintext semantics the demonstration produces ninety-five constraint violations across ninety records; under accountability-preserving semantics it produces none. An independently written exhaustive search over all assignments of payload accessibility confirms that under plaintext semantics no assignment succeeds. Thirty-nine violations arise in Secure Processing Environment records that received no erasure request at all, through the interaction of Article 73(1)(e) with Article 68(12) — a collision internal to a single regulation, conditional on a reading of Article 68(12) that the thesis defends and marks as contestable.

The contribution is bounded. No cryptographic primitive is novel; the general method of treating legal compliance as a satisfiability problem is established; the proofs are informal rather than machine-checked; key destruction is simulated and attested rather than proven; and two interpretive steps at the centre of the argument rest on reasoning rather than on regulatory authority. What the thesis offers is the formal characterisation of a conflict that the most recent systematisation of the cryptographic-erasure literature names as an open problem, a minimal and principled semantic move that dissolves it, an executable witness of both results, and an integration analysis against Norwegian infrastructure verified as it currently operates.

**Keywords:** European Health Data Space; GDPR Article 17; cryptographic erasure; audit trail; data retention; design science research; Secure Processing Environment; MyHealth@EU; information logistics; Norway.

*(Approx. 520 words.)*

---

## Statement of Contribution

This thesis makes four contributions, each stated at the level it can be defended.

**1. A formal model of the tri-lateral retention conflict.** The TRF Model expresses audit-retention floors, the erasure right, and the deletion ceiling as constraints over a single binary variable per record, with verifiability semantics as an explicit parameter. The method of formalising legal compliance as satisfiability is established in the literature and is not claimed here; its application to a retention system combining floors, a right, and a ceiling, and the isolation of verifiability as the parameter determining feasibility, are new to the reviewed literature.

**2. Two feasibility results with an executable witness.** Theorem 1 establishes infeasibility under the semantics implicit in current audit practice. Theorem 2 establishes satisfiability under an alternative and exhibits the trajectory achieving it. Both are proved informally and demonstrated executably, with an independent exhaustive cross-check.

**3. A mechanism specification with its residue analysed against the applicable legal threshold.** Crypto-Erasure by Invalidation is specified in implementable detail. Its surviving residue is characterised as pseudonymised rather than anonymous by the Norwegian standard, and designed to the corridor established by the European Data Protection Board's finalised Guidelines 02/2025.

**4. An integration analysis against verified Norwegian infrastructure.** The mechanism is placed at the audit-repository step of the MyHealth@EU flow and the access-logging boundary of a Secure Processing Environment, and requires of the substrate nothing that the finalised national criteria do not already demand.

**What is not claimed.** No novel cryptographic primitive or construction. No novel formal method. No first-ever framework for anything. No deployed system, no performance result, no connection to any National Contact Point. No proof that key destruction occurred, as distinct from an attestation that it did. No empirical estimate of how often the conflict arises in practice. No regulatory authority for either of the two interpretive steps the argument depends upon, both of which are identified in Chapter 6 and proposed for resolution in Chapter 7.

---

## Declaration of Originality

This thesis is my own work. Where the work of others is used, it is cited. Where an argument originates in the supervisory relationship or in feedback on drafts, that is noted in the text.

Two declarations are made explicitly because the first version of this project, abandoned in May 2026, failed to make them truthfully.

**Ethics.** This research involved no human participants, no interviews, no surveys, no observation of persons, and no personal data of any kind. All data used are synthetic, generated by Synthea, and describe no real individual. No approval from the Norwegian Agency for Shared Services in Education and Research, from any regional research-ethics committee, or from any institutional review board was required for this work, and none was sought or obtained. Any claim to the contrary appearing in earlier drafts of this project is withdrawn.

**Sources.** Every factual claim in this thesis is traceable to a source retrievable at the time of writing. Where verification of a source remains incomplete, the incompleteness is flagged in the text rather than concealed. An audit conducted in May 2026 identified citations in the earlier draft to works that do not exist; that draft has been discarded in its entirety and every citation in the present work has been checked against a primary or retrievable source.

**Use of AI assistance.** Anthropic's Claude was used throughout this project as a research and drafting assistant: for literature search and source verification, for critique of the author's arguments, for drafting and redrafting prose to the author's direction, and for writing the Python code in Appendix A. All design decisions, the model's formulation, the interpretive legal arguments, and the acceptance or rejection of every suggestion are the author's own, and the author is answerable for the whole. This declaration is made in the form the institution's guidance requires and should be read alongside it.

---

## Nomenclature and Abbreviations

**Model notation**

| Symbol | Meaning |
|---|---|
| *a* | An audit record |
| *m*(*a*) | Event metadata — actor, contact point, patient pseudonym, document category, legal basis, outcome |
| *p*(*a*) | Personal-data payload of the record |
| *c*(*a*) | Hiding commitment to the payload, *c* = Commit(*p*, *r*) |
| *r*(*a*) | Per-record commitment salt |
| *k*(*a*) | Payload key |
| *ι*(*a*) | Invalidation entry — month, legal ground, authorising actor |
| *t*(*a*) | Month in which the access event occurred |
| *F*(*a*) | Retention floor, in months (120 cross-border; 12 for SPE access logs) |
| *σ*(*a*) | Pathway: primary or secondary |
| *t*ᵣ(*a*) | Month an erasure request arrives (∞ if none) |
| *t*π(*a*) | Month a data permit expires (∞ if not applicable) |
| *t*ᴵ(*a*) | Invalidation month, min(*t*ᵣ + δ, *t*π + 6) |
| δ | Erasure response period, in months (GDPR Art. 12(3)) |
| *α*(*a*, *t*) | Payload accessibility at month *t* — 1 if recoverable, 0 otherwise |
| *V*(*a*, *t*) | Whether the record counts as verifiable at month *t* |
| *V*ᴵ, *V*ᴵᴵ | Verifiability under Semantics I (plaintext) and Semantics II (accountability-preserving) |
| C1, C2, C3 | Retention floor, erasure right, and deletion ceiling constraints |

**Abbreviations**

| Term | Expansion |
|---|---|
| ATNA | Audit Trail and Node Authentication (IHE integration profile) |
| CEF | Coordinated Enforcement Framework (EDPB) |
| DSR | Design Science Research |
| EDPB | European Data Protection Board |
| EEA | European Economic Area |
| EEHRxF | European Electronic Health Record Exchange Format |
| eHDSI | eHealth Digital Service Infrastructure |
| eHMSEG | eHealth Member States Expert Group |
| eHOMB | eHealth Operational Management Board |
| EHDS | European Health Data Space |
| FHIR | Fast Healthcare Interoperability Resources (HL7) |
| GDPR | General Data Protection Regulation (EU) 2016/679 |
| HDAB | Health Data Access Body |
| HSM | Hardware Security Module |
| IHE | Integrating the Healthcare Enterprise |
| NCPeH | National Contact Point for eHealth |
| NHN | Norsk Helsenett SF |
| NIST | National Institute of Standards and Technology (US) |
| NORTRE | Norwegian Trusted Research Environments |
| OpenNCP | Open National Contact Point software stack |
| PoSE | Proof of Secure Erasure |
| SoK | Systematization of Knowledge |
| SPE | Secure Processing Environment |
| SPUHiN | Secure Provision and Use of Health Data in Norway (project) |
| TEHDAS2 | Towards European Health Data Space, Joint Action 2 |
| TRF | Tri-Lateral Retention Feasibility (Model) |
| zk-SNARK | Zero-Knowledge Succinct Non-Interactive Argument of Knowledge |

**A note on the project name.** This work has been presented in preliminary form under the name VERA-SNARK, which originates in an earlier design iteration that envisaged zero-knowledge succinct arguments as the enforcement machinery. The design-science process showed that the audit-trail retention problem requires no such machinery, and the mechanism specified here contains none. The name is retained for continuity with that earlier presentation, and the evolution is discussed in Chapter 1, Section 1.6. Chapter 7, Section 7.5 identifies the distinct problem for which zero-knowledge arguments do become necessary.

---

## Table of Contents

1. **Introduction** — background, problem statement, research questions, significance, scope, methodological approach, structure
2. **Literature Review and Theoretical Foundation** — review strategy; cross-border landscape; the audit-retention versus erasure tension; cryptographic approaches; formal approaches to compliance verification; Norwegian secondary-use infrastructure; information-logistics framing; comparative analysis; research gaps; conceptual positioning
3. **Methodology and Research Design** — design science paradigm; the adopted cycle; specification-and-demonstration with formal modelling; formal-modelling methodology; synthetic data; sandbox approach; validity, reliability and limitations; ethics
4. **The Tri-Lateral Retention Feasibility Model and the Crypto-Erasure by Invalidation Mechanism** — necessity analysis; model and notation; constraints; two semantics; Theorem 1 and corollaries; Theorem 2; mechanism specification; residue analysis; rival designs; Norwegian integration
5. **Demonstration** — implementation; results under each semantics; Corollary 1.2 witnesses; independent cross-check; payload-provenance comparison; what is and is not established
6. **Discussion** — what the thesis establishes; the authority problems; key destruction and assurance; the cost objection; synthetic data; practice and policy; theoretical implications; boundaries as contribution
7. **Conclusion** — problem and answer; contributions; limitations; open questions of authority; future work

**Appendix A** — Code artefacts, reproduction commands, data provenance, integrity record

**Appendix B** — Search query log: 59 queries across four dated rounds, with round purposes and coverage notes

**Appendix C** — Expert evaluation instrument: panel composition, session structure, demonstration script, semi-structured interview guide, closed-response questionnaire, analysis plan


\pagebreak

---

# Chapter 1. Introduction

---

## 1.1 Background and Context

The European Union's health sector is undergoing the most significant data-governance transformation in its history. Regulation (EU) 2025/327 on the European Health Data Space was adopted on 11 February 2025, published in the Official Journal on 5 March 2025, and entered into force on 26 March 2025, establishing the first Union-wide legal framework for the primary and secondary use of electronic health data across all Member States and European Economic Area countries (European Parliament and Council of the European Union, 2025). The regulation creates a binding architecture for cross-border exchange of patient summaries, electronic prescriptions, laboratory results, medical imaging, and hospital discharge reports, with primary-use exchange of patient summaries and ePrescriptions becoming mandatory across the EU and EEA by March 2029, and the remaining priority categories by March 2031 (European Commission, 2025a).

The technical infrastructure underpinning this regulatory shift is MyHealth@EU, the federated pull-based system that allows a clinician in one Member State to retrieve a patient summary or dispense an ePrescription issued in another Member State. Each participating country operates a single National Contact Point for eHealth (NCPeH), and all cross-border exchanges flow through a six-step gateway protocol implemented in the Open National Contact Point (OpenNCP) software stack. These six steps cover service discovery, patient discovery, document retrieval, pivot translation between national clinical document formats and a common European format, security and consent validation, and audit logging (Simjanoska Misheva et al., 2025).

Norway's integration with MyHealth@EU is no longer prospective but operational, though its scope remains deliberately narrow. The Norwegian connection project, coordinated jointly by the Norwegian Directorate of Health (Helsedirektoratet) and the Norwegian Health Network (Norsk Helsenett SF) since January 2023 with a planned duration of 41 months, has taken its pilot live at the emergency clinics (legevakter) in Bodø and Stjørdal, connected to Portugal, Czechia, and Finland for the receipt of patient summaries concerning citizens of those states who require care in Norway; the Bodø and Stjørdal clinics are in production with Czechia and Portugal, and emergency clinics in Trondheim and Ålesund operating on Helseplattformen have requested the service for the next stage of expansion (Helsedirektoratet, 2026a, 2026b). Two qualifications are material and are recorded rather than elided. The pilot is live in the sense that the infrastructure is in production and the legal basis, privacy notices, and data protection impact assessment were completed by 31 March 2025; but the Directorate's own portfolio reporting notes that no relevant patients had yet presented for the solution to be used in practice, so the volume of genuine cross-border audit records generated in Norway to date is minimal. Infrastructure for receiving ePrescriptions from other EU and EEA states has been planned and developed but is not yet in use. Norway's scenario of implementing ePrescription without the corresponding eDispensation service required the approval of the other participating states and was carried as a change proposal to the requirement catalogue, approved and decided in the eHealth Operational Management Board on 12 March (Helsedirektoratet, 2026a). As Norway is not a Member State of the European Union but an EEA member, EHDS implementation is being processed through the EEA Joint Committee, with Helsedirektoratet having delivered its formal EHDS gap analysis on 11 April 2025 (Helsedirektoratet, 2025a). The cross-border audit records with which this thesis is concerned are therefore beginning to be generated in Norwegian production, on infrastructure that is live rather than hypothetical, even though the present volume is small.

Within this regulatory transformation, the most consequential change for clinical practice is the new layer of patient rights established by EHDS. Citizens gain the right to access and download their electronic health data, to view logs of who has accessed it, to set granular restrictions on cross-border sharing, and to opt out of secondary use (European Parliament and Council of the European Union, 2025). These rights interact directly with two long-standing instruments. The first is the IHE Audit Trail and Node Authentication (ATNA) integration profile, which defines the technical structure through which access events are logged in cross-border exchanges. ATNA itself prescribes no retention period; the retention obligation arises from the deployment binding: under the eHDSI security framework adopted for MyHealth@EU operations, ATNA-compliant audit repositories must retain their logs for a minimum of ten years (Simjanoska Misheva et al., 2025; IHE International, 2024). The second is the General Data Protection Regulation (EU) 2016/679, whose Article 17 establishes the data subject's right to obtain erasure of personal data without undue delay under specified conditions (European Parliament and Council of the European Union, 2016).

A third constraint arises from the implementing infrastructure for EHDS secondary use. The TEHDAS2 Joint Action's guideline for Health Data Access Bodies specifies that personal data must be deleted from a Secure Processing Environment within six months of the expiry of the data permit, operationalising Article 68(12) of the EHDS Regulation (TEHDAS2, 2025).

Critically, the same regulation imposes a retention obligation on the same environment. Article 73(1)(e) EHDS requires that Secure Processing Environments keep identifiable logs of access to and activities within the environment for the period necessary to verify and audit all processing operations, and that logs of access be kept for at least one year (European Parliament and Council of the European Union, 2025). Identifiable access logs are personal data, and they are data within the environment. On the reading of Article 68(12) defended in Chapter 4, Section 4.6 — that the provision governs the data within the secure processing environment rather than only the dataset supplied under the permit: the Regulation therefore requires, of a single environment, that data be removed within six months of permit expiry and that identifiable logs be retained for at least twelve months. That reading is contestable, and the thesis states its grounds rather than assuming it; under the narrower alternative the conflict in the secondary-use pathway arises through Article 17 erasure requests instead, as it does in the cross-border pathway, and the thesis's results are unaffected.

Cross-border health data exchange therefore operates under three kinds of retention regime that do not yet have a documented technical reconciliation: audit-retention floors, instantiated as the ten-year floor imposed on cross-border audit repositories by the eHDSI deployment baseline and the one-year floor imposed on Secure Processing Environment access logs by Article 73(1)(e) EHDS; an erasure obligation for personal data exercisable at any time by the data subject; and a six-month deletion ceiling for processed data in Secure Processing Environments. This thesis is positioned within that unresolved tension.

## 1.2 Problem Statement

The European Health Data Space establishes legal rights and operational obligations, but it does not prescribe how the three retention regimes described above are to be reconciled in technical practice. The result is a structural conflict embedded in the cross-border audit trail.

When a Norwegian patient is treated in another Member State, the access event is logged in the local NCPeH's ATNA-compliant audit repository, retained for at least ten years under the eHDSI baseline, and accessible to the patient through the home country's audit-log interface (Simjanoska Misheva et al., 2025). If, during that ten-year window, the patient exercises the right to erasure under GDPR Article 17, the institution faces a choice between three positions, each of which violates one of the other regimes. Deleting the audit record honours Article 17 but destroys the integrity of the audit chain that the eHDSI framework, eIDAS-based access traceability, and EHDS patient rights all depend upon. Retaining the audit record in full preserves the chain but fails the erasure obligation. Pseudonymising the record creates ambiguity about whether the pseudonymisation is reversible, which under GDPR Recital 26 may not satisfy true anonymisation.

An apparent resolution must be confronted at the outset. Article 17(3)(b) GDPR exempts erasure to the extent that processing is necessary for compliance with a legal obligation to which the controller is subject. It could therefore be argued that the audit-retention obligation simply disapplies Article 17 for audit records, and that no conflict exists. This thesis takes the position, defended in Sections 2.3 and 4.2, that the conflict survives the exemption in a precise form. The exemption extends only as far as retention is *necessary* for the legal obligation, and the data-minimisation principle of Article 5(1)(c) GDPR requires that no more personal data be retained than the obligation demands. Retaining the full plaintext personal-data payload of an audit record for ten years exceeds what accountability requires, since the accountability function of the record can be preserved without continued access to that payload. Moreover, the six-month deletion ceiling under Article 68(12) EHDS admits no equivalent exemption. What may lawfully be retained is therefore the accountability skeleton of the record rather than its full personal-data content: and specifying, formalising, and demonstrating exactly that residue is the work of this thesis.

The same conflict arises in the secondary-use pathway, and there it is at its sharpest. When a researcher receives a data permit from the Norwegian Health Data Access Body, Helsedataservice (Folkehelseinstituttet, 2024), and processes the data within a Norwegian Secure Processing Environment such as those operated by the Trusted Research Environments collaboration NORTRE (Norwegian Trusted Research Environments, 2025), Article 68(12) EHDS as operationalised by TEHDAS2 requires deletion of personal data from the environment within six months of permit expiry. Article 73(1)(e) of the same regulation requires that identifiable access logs for that environment be kept for at least one year. On the broad reading, the environment must therefore be emptied of personal data at six months while continuing to hold, for a further six months at minimum, identifiable records of who accessed what within it. No provision resolves the two. Article 73(5) requires the Commission to lay down, by means of implementing acts and by 26 March 2027, the technical, organisational, information-security, confidentiality, data-protection and interoperability requirements for Secure Processing Environments; the secondary-use provisions themselves, Articles 68 and 73 among them, become applicable on 26 March 2029. The collision is therefore not yet operative, and the window in which its resolution could be specified rather than improvised closes with those implementing acts.

These conflicts are not theoretical, and the Norwegian policy process has moved while leaving them unresolved. The SPUHiN project, jointly led by Helsedirektoratet and the Norwegian Institute of Public Health, acknowledged in its November 2024 draft recommendations that Norway lacks a formal regulatory definition of a Secure Processing Environment (SPUHiN, 2024). Following a public hearing between July and October 2025, the recommendations have since been consolidated into final form, including separate compliance checklists for SPE providers and SPE user organisations, positioned as a national reference basis pending the EU implementing act (SPUHiN, 2025). The finalised criteria contain governance and functional requirements but no mechanism reconciling the retention and erasure regimes: the gap addressed here therefore survives against the final national document, not merely a draft.

A small but rapidly growing body of cryptographic research has begun to address adjacent problems. Albalwy (2026) demonstrates zero-knowledge policy enforcement for cross-institutional health data sharing within a single jurisdiction. Natsiavas et al. (2021) document KONFIDO, the most direct architectural ancestor for cross-border health data security, which combined trusted execution environments, homomorphic encryption, and blockchain-based auditing on the OpenNCP gateway. Bai et al. (2022) describe Health-zkIDM, a Hyperledger Fabric-based decentralised identity system for healthcare. None of these works addresses the audit-retention versus erasure tension at the cross-border audit layer, and none provides a formal account of the conditions under which the three regimes can be jointly satisfied.

The problem this thesis addresses is therefore twofold: the absence of a formal characterisation of the tri-lateral retention conflict in cross-border health data audit trails under EHDS, and the consequent absence of a technically specified, regulation-aligned mechanism for resolving it in a manner compatible with the operational reality of Norwegian implementation.

## 1.3 Research Objectives and Questions

The objective of this thesis is to formally characterise, and then resolve by design, the conflict between the three retention regimes identified in Section 1.2.

The analytical core of the thesis is the Tri-Lateral Retention Feasibility Model (TRF Model), a constraint-satisfaction formulation developed in Chapter 4 within the established tradition of formal legal-compliance verification (Feng, Marsso, Sabetzadeh, & Chechik, 2022). The model decomposes each cross-border audit record into an event-metadata component and a personal-data payload bound by a cryptographic commitment, expresses the three regimes as constraints over discretised time, and examines the satisfiability of the constraint system under two competing semantics of audit verifiability. The model is tri-lateral in its structure — floor, right, ceiling: rather than in the number of instruments it accommodates: the retention floor is parameterised, so that the ten-year cross-border audit floor and the one-year Secure Processing Environment log floor are two instances of one constraint rather than two separate constraints. Under the prevailing implicit semantics, in which a verifiable audit record is one whose payload remains accessible in plaintext, the system is shown to be infeasible whenever an erasure request or permit expiry falls within a record's retention window. Under an alternative semantics, in which verifiability is defined as accountability-preservation — intact metadata, a surviving commitment, and a logged, witnessed invalidation event: the system is shown to be jointly satisfiable for every arrival pattern of erasure requests and permit expiries. The mechanism that realises this feasibility, termed Crypto-Erasure by Invalidation, applies the cryptographic-erasure technique recognised in NIST Special Publication 800-88 Revision 2 at the audit-trail boundary: the key binding a record to its payload is destroyed, while the invalidation event itself is appended to the audit trail. The mechanism is thus the constructive witness of the model's feasibility result, not an independently posited design.

The thesis is guided by one primary research question.

**Primary research question.** How can a verifiable crypto-erasure mechanism be designed to reconcile the conflicting data-retention requirements of cross-border health data exchange under the European Health Data Space — specifically the tension between the audit-retention floors applying to the exchange, namely the ten-year minimum imposed on IHE ATNA audit repositories by the eHDSI deployment baseline and the one-year minimum imposed on Secure Processing Environment access logs by Article 73(1)(e) EHDS, GDPR Article 17's right to erasure, and the six-month Secure Processing Environment deletion ceiling under Article 68(12) EHDS as operationalised by TEHDAS2 — while preserving audit integrity in a Norwegian implementation context?

The primary question is decomposed into three sub-questions.

**SQ1.** What are the precise points of conflict between the audit-retention floors, GDPR Article 17, and the Article 68(12) deletion ceiling in the cross-border EHDS workflow, and under what formal conditions are the three regimes jointly satisfiable?

**SQ2.** Can a cryptographic invalidation mechanism — in which the references binding audit records to personal data are mathematically invalidated rather than the records being deleted — satisfy all three constraints simultaneously, across floors of differing duration?

**SQ3.** How would such a mechanism integrate with Norway's current cross-border infrastructure, specifically the NCPeH operated by Helsedirektoratet and Norsk Helsenett, the Health Data Access Body Helsedataservice, and the Secure Processing Environments operated under NORTRE?

SQ1 is addressed through Chapter 2's literature analysis and the formal characterisation in Chapter 4. SQ2 is addressed through the TRF Model's feasibility theorems, the mechanism specification in Chapter 4, and the executable demonstration in Chapter 5. SQ3 is addressed through Chapter 4's integration analysis and Chapter 6's discussion of implications for Norwegian implementing actors.

## 1.4 Significance and Relevance

The significance of this thesis rests on four convergent factors.

First, the timing is concrete rather than abstract. The Group One priority categories of EHDS become mandatory across the EU and EEA in March 2029, with Group Two following in March 2031, and the implementing acts specifying technical detail are due by March 2027 (European Commission, 2025a). Norway's NCPeH is in live pilot operation, exchanging records with Portugal, Czechia, and Finland, with its outbound capability under construction during 2026 (Helsedirektoratet, 2026a). Decisions about how cross-border audit trails will handle conflicting retention obligations will be made within the current implementation window, against a regulatory background that the European Data Protection Board's February 2026 Coordinated Enforcement Framework report on Article 17, spanning thirty-two supervisory authorities and 764 controllers, explicitly identifies as unsettled, naming the definition and implementation of retention periods among the recurring difficulties (European Data Protection Board, 2026a). In parallel, the Board's Guidelines 02/2025 on blockchain technologies accept, for the first time at Union level, that rendering personal data unrecoverable through cryptographic means can substitute for erasure where the controller documents the threat model: establishing the regulatory corridor within which the mechanism proposed here is designed (European Data Protection Board, 2026b).

Second, the Norwegian implementation context provides a concrete, named substrate: a designated Health Data Access Body in Helsedataservice (Folkehelseinstituttet, 2024); a developed Trusted Research Environment collaboration in NORTRE (Norwegian Trusted Research Environments, 2025); finalised national SPE criteria from the SPUHiN process that acknowledge, but do not resolve, the retention-erasure question (SPUHiN, 2025); and parallel legislative work on professional confidentiality and cross-organisational access (Stortinget, 2025).

Third, the contribution is positioned at a level the existing literature does not occupy. The general method of formalising legal compliance as a satisfiability problem is established (Feng et al., 2022), and the cryptographic-erasure technique is recognised in standards (National Institute of Standards and Technology, 2025) and critiqued in practice; but no published work formally models the specific tri-lateral conflict of the cross-border health audit trail, and no work derives a reconciling mechanism from such a model. This holds even for the conflict's sharpest instance: the collision between the six-month deletion ceiling of Article 68(12) and the one-year log-retention floor of Article 73(1)(e) is stated within a single regulation, yet the review conducted for this thesis found no treatment of it: including in the guidance published by the Joint Action drafting the specifications for both provisions. Part of the explanation is procedural: in the 2022 proposal these obligations sat in Articles 46 and 50 and were renumbered on adoption in 2025, so that much existing commentary discusses them under superseded numbering and in separate literatures. The gap is corroborated externally: the most recent systematisation of the cryptographic-erasure literature closes by naming erasure under multi-regime retention conflict among five open problems for the field (Aikebaier, 2026). Albalwy (2026) occupies the cross-institutional space within a single jurisdiction; KONFIDO (Natsiavas et al., 2021) addressed cross-border security without resolving the retention-erasure tension and depended on trusted hardware. The thesis's novelty claim is therefore layered and deliberately bounded: the formal characterisation of an unformalised conflict, expressed through an information-logistics lens that is itself new to this problem, with the mechanism as the derived solution: an application of recognised primitives, not a claim of foundational cryptographic novelty.

Fourth, the thesis frames the problem as one of information logistics, and the framing is structural rather than decorative. The reconciliation of conflicting retention regimes across jurisdictional boundaries is the same problem class that physical cross-border logistics manages through customs documentation retention, mandated destruction of restricted goods, and certified-destruction entries in the ledger. The audit log is the customs ledger of the digital consignment; invalidation is its certified destruction certificate. This situates the contribution within the disciplinary identity of Sustainable Energy Logistics at HiMolde and imports a solution structure that logistics has operated for decades into a domain that has not yet recognised the equivalence.

## 1.5 Scope and Out-of-Scope

This thesis is bounded by a deliberate and explicit scope. The bounding is not a limitation to be apologised for but a methodological commitment to defensibility within the time and resources available for an MSc thesis.

**The thesis contributes a formal model, a design-science specification derived from it, and an executable demonstration.** The TRF Model formalises the conflict; the Crypto-Erasure by Invalidation mechanism is specified as the model's constructive feasibility witness; and a Python-based sandbox using synthetic Synthea-generated FHIR data demonstrates both the infeasibility result under the status-quo semantics and the feasibility result under invalidation semantics. The model, the specification, and the demonstration together constitute the artefact.

The thesis explicitly does **not** include the following. First, it does not build a working zero-knowledge SNARK circuit; no component of the mechanism requires one, and the cryptographic machinery that an earlier design iteration envisaged is treated as future work. Second, it does not deploy to a real National Contact Point for eHealth; integration with Norwegian NCPeH operations remains an architectural mapping rather than a runtime test. Third, it does not conduct human-subject interviews, and no qualitative empirical data are reported. Fourth, it does not measure hardware energy consumption, and no sustainability metrics are claimed beyond conceptual framing. Fifth, it does not use real patient data; all sandbox data are synthetic and contain no information about real individuals. Sixth, it does not implement healthcare-professional authentication or consent-propagation protocols beyond the invalidation mechanism itself. Seventh, it does not provide machine-checked formal proofs; the two feasibility theorems are proved informally at the level of rigour standard for design-science work, and their executable check in the sandbox is a demonstration, not a verification in the proof-assistant sense. Eighth, it does not prove destruction of cryptographic keys; the mechanism's guarantees are conditional on honest key destruction, a limitation examined in Chapter 6. Ninth, it does not model the national retention laws of receiving jurisdictions beyond the Union-level instruments; the time horizon of the model is parameterised so that jurisdiction-specific floors can be substituted. Tenth, it does not address non-EU and non-EEA jurisdictions.

Components conceptually related to the broader research direction — a zero-knowledge assertion circuit for healthcare-professional authorisation, a sustainability indicator for proof systems, and a cross-border consent-revocation propagation protocol: are presented in a separate addendum to the thesis supervisor, signalling future research direction without claiming results that have not been produced.

## 1.6 Methodological Approach

The thesis adopts Design Science Research, as established by Hevner, March, Park, and Ram (2004) and elaborated by Peffers, Tuunanen, Rothenberger, and Chatterjee (2007), in its specification-and-demonstration variant, extended with a formal-modelling step. The DSR cycle of problem identification, objectives, design and development, demonstration, evaluation, and communication is mapped onto the thesis chapters, with the design phase anchored in the TRF Model: the mechanism is developed as the constructive answer to a formally stated feasibility question, following the tradition of formal compliance verification exemplified by Feng et al. (2022) while deliberately employing lighter machinery, a feasibility formulation over one binary state variable per record, suited to defence at Master's level and to the logistics-modelling training of the author's programme.

A note on nomenclature records the design's evolution honestly. The project name VERA-SNARK originates from an earlier design iteration, presented in preliminary form at the NORS 2025 conference, which envisaged zero-knowledge succinct arguments as the enforcement machinery. The design-science process — specifically, the formal analysis of what the three retention regimes actually require: showed that cryptographic commitments and accumulator-based invalidation suffice for the audit-trail problem, and that no SNARK is required. The project name is retained for continuity; the mechanism specified and demonstrated in this thesis contains no SNARK, and the evolution from the earlier architecture is itself an instance of the DSR cycle functioning as intended.

The demonstration is conducted in a controlled sandbox using synthetic data generated by Synthea, an open-source generator of synthetic patient records compliant with HL7 FHIR R4, the version reflected in the current Norwegian basisprofiler maintained by HL7 Norway (HL7 Norway, 2025). The sandbox has two layers: a feasibility checker that walks synthetic audit records through randomised arrivals of erasure requests and permit expiries, verifying that the constraint system fails under plaintext-verifiability semantics and holds under invalidation semantics; and a realism layer feeding Synthea-generated records into the checker. The evaluation strategy is analytical: internal validity through the logical consistency of the model and the coherence of mechanism and theorems; external validity through compatibility with verified existing infrastructure; reliability through deterministic execution with fixed random seeds. No empirical performance benchmarks are reported. The full methodological treatment is provided in Chapter 3.

## 1.7 Thesis Structure

The thesis is organised in seven chapters and appendices.

**Chapter 1** introduces the regulatory background, the problem, the research objectives, the significance of the study, the scope and explicit out-of-scope boundaries, and the methodological approach.

**Chapter 2** reviews the literature in five domains: the cross-border health data exchange landscape under EHDS; the audit-retention versus right-to-erasure tension, including the Article 17(3)(b) exemption argument; cryptographic approaches to audit compliance; formal approaches to regulatory-compliance verification; and the Norwegian secondary-use infrastructure. It identifies the research gaps and positions the contribution.

**Chapter 3** establishes the design science research paradigm, the specification-and-demonstration variant extended with formal modelling, the synthetic data methodology, the sandbox approach, and validity, reliability, and ethical considerations.

**Chapter 4** develops the TRF Model — sets, decomposition, constraints, the two verifiability semantics, and the infeasibility and feasibility theorems: and specifies the Crypto-Erasure by Invalidation mechanism derived from it, including the invalidation registry, audit-trail behaviour, a comparison against rival designs, and integration analysis with Norwegian NCPeH and NORTRE infrastructure.

**Chapter 5** presents the sandbox demonstration, including the executable feasibility check. **Chapter 6** discusses findings and their implications for practice, theory, and policy, and engages the principal counter-positions. **Chapter 7** concludes, summarises contributions, revisits limitations, and outlines future work.

---

## References (Chapter 1, v2)

Albalwy, F. (2026). Zero-knowledge-based policy enforcement for privacy-preserving cross-institutional health data sharing on blockchain. *Systems*, *14*(4), 385. https://doi.org/10.3390/systems14040385

Aikebaier, Y. (2026). *SoK: Cryptographic erasure on public ledgers: Application-layer architectures, key-lifecycle adversaries, and GDPR Art. 17 equivalence* (Cryptology ePrint Archive, Paper 2026/1109). https://eprint.iacr.org/2026/1109 [Preprint; not peer-reviewed]

Bai, T., Hu, Y., He, J., Fan, H., & An, Z. (2022). Health-zkIDM: A healthcare identity system based on Fabric blockchain and zero-knowledge proof. *Sensors*, *22*(20), 7716. https://doi.org/10.3390/s22207716

European Commission. (2025a). *European Health Data Space Regulation: Implementation calendar*. Directorate-General for Health and Food Safety. https://health.ec.europa.eu/

European Data Protection Board. (2026b). *Guidelines 02/2025 on the processing of personal data through blockchain technologies* (Version 2.0, adopted 7 July 2026 following public consultation). EDPB.

European Data Protection Board. (2026a). *Coordinated Enforcement Framework report on the implementation of the right to erasure under Article 17 GDPR* (18 February 2026). EDPB. https://www.edpb.europa.eu/

European Parliament and Council of the European Union. (2016). Regulation (EU) 2016/679 of 27 April 2016 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88.

European Parliament and Council of the European Union. (2025). Regulation (EU) 2025/327 of 11 February 2025 on the European Health Data Space. *Official Journal of the European Union*.

Feng, N., Marsso, L., Sabetzadeh, M., & Chechik, M. (2022). *Bounded satisfiability checking of metric first-order temporal logic*. arXiv:2209.04052.

Folkehelseinstituttet. (2024). *Helsedataservice: The national health data access body*. Norwegian Institute of Public Health. https://helsedata.no/

Helsedirektoratet. (2025a). *Europeisk helsedataområde (EHDS)*. Norwegian Directorate of Health. https://www.helsedirektoratet.no/

Helsedirektoratet. (2026a). *MyHealth@EU, Helsedirektoratet* [National e-health portfolio measure: status and deliverables]. Norwegian Directorate of Health. https://www.helsedirektoratet.no/digitalisering-og-e-helse/nasjonal-e-helseportefolje/tiltak-i-nasjonal-e-helseportefolje/myhealth-eu-helsedirektoratet

Helsedirektoratet. (2026b). *MyHealth@EU, Norsk helsenett* [National e-health portfolio measure: status and deliverables]. Norwegian Directorate of Health. https://www.helsedirektoratet.no/digitalisering-og-e-helse/nasjonal-e-helseportefolje/tiltak-i-nasjonal-e-helseportefolje/myhealth-eu-norsk-helsenett

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly*, *28*(1), 75–105.

HL7 Norway. (2025). *hl7.fhir.no.basis* (Version 2.2.2) [FHIR R4 national base profile package]. Simplifier.net.

IHE International. (2024). *Audit Trail and Node Authentication (ATNA) Integration Profile* — IT Infrastructure Technical Framework, Vol. 1, Ch. 9. https://profiles.ihe.net/ITI/TF/Volume1/ch-9.html

National Institute of Standards and Technology. (2025). *Special Publication 800-88 Revision 2: Guidelines for media sanitization* (R. Chandramouli & E. Hibbard). NIST. https://doi.org/10.6028/NIST.SP.800-88r2

Natsiavas, P., Mazzeo, G., Faiella, G., Campegiani, P., Dumortier, J., Stan, O., … Romano, L. (2021). Developing an infrastructure for secure patient summary exchange in the EU context: Lessons learned from the KONFIDO project. *Health Informatics Journal*, *27*(2). https://doi.org/10.1177/14604582211021459

Norwegian Trusted Research Environments. (2025). *NORTRE: A collaboration between TSD, SAFE, and HUNT Cloud*. https://nortre.no/

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems*, *24*(3), 45–77.

Simjanoska Misheva, M., Shahpaski, D., Dobreva, J., Bukovec, D., Gjorgjioski, B., Nikolov, M., … Gams, M. (2025). AI Act compliance within the MyHealth@EU framework: Tutorial. *Journal of Medical Internet Research*, *27*, e81184. https://doi.org/10.2196/81184

SPUHiN. (2024). *Recommendations for minimum requirements for Secure Processing Environments in Norway* (Draft, 29 November 2024). Helsedirektoratet & Folkehelseinstituttet.

SPUHiN. (2025). *Recommendations for minimum requirements for Secure Processing Environments in Norway* (D5.2, final, following public hearing July–October 2025) [Project deliverable]. Helsedirektoratet & Folkehelseinstituttet.

Stortinget. (2025). *Innst. 71 L (2025–2026)*. Norwegian Parliament.

TEHDAS2. (2025). *Guideline for Health Data Access Bodies on procedures and formats for data access* (D6.3). TEHDAS2 Joint Action.


\pagebreak

---

# Chapter 2. Literature Review and Theoretical Foundation

---

## 2.1 Review Protocol

### 2.1.1 Type of review and why it is named as such

This review is a structured narrative review conducted under a documented and dated protocol. It is not a systematic review, and the distinction is stated at the outset rather than left to inference. A systematic review executes a pre-registered search strategy in a single sweep, against a fixed set of indexed databases, with independent screening by more than one reviewer. This review proceeded iteratively across four dated rounds, used natural-language rather than Boolean queries, drew substantially on primary regulatory and government sources that are not indexed in bibliographic databases at all, and was screened by one reviewer. Calling it systematic would misdescribe it.

What the review can offer instead is replicability of a different and, for this subject, more appropriate kind: a complete record of what was searched and when, the criteria applied, the screening account, and a prospective Boolean protocol that a researcher may execute against indexed databases to test whether the conclusions survive a systematic sweep. Section 2.1.6 provides that protocol and states plainly that it was not the instrument used here.

### 2.1.2 What the review had to establish

The review is organised around the conceptual architecture of the thesis rather than around exhaustive coverage of a field. It had to establish four conditions on which the contribution depends: that the cross-border landscape under the European Health Data Space is advanced enough and Norwegian participation committed enough for the contribution to be timely; that the audit-retention versus erasure tension is real, named in primary sources, and unresolved; that cryptographic and formal approaches have matured enough to make the proposed mechanism plausible while leaving the specific conflict unaddressed; and that the Norwegian secondary-use infrastructure provides a concrete substrate. A search strategy optimised for recall across a defined corpus would not have served these conditions, three of which turn on primary legal and governmental material.

### 2.1.3 Sources searched

Academic literature was searched through Google Scholar, arXiv, the Cryptology ePrint Archive, PubMed and PubMed Central, and publisher platforms including Springer, IEEE Xplore, MDPI, Sage, JMIR, and BMC. Primary regulatory material was retrieved directly from EUR-Lex, the European Commission's Directorate-General for Health and Food Safety, and the European Data Protection Board. Standards material was retrieved from IHE International, NIST, and HL7 and HL7 Norway. Norwegian governmental and institutional material was retrieved from helsedirektoratet.no, helsedata.no, datatilsynet.no, nortre.no, and stortinget.no. Joint Action material was retrieved from tehdas.eu. Patent literature was searched through public patent databases in the final round.

### 2.1.4 Search rounds

| Round | Date | Purpose | Distinct queries |
|---|---|---|---|
| 0 | before 24 May 2026 | Exploratory reading and drafting, documented at artifact level only | not recoverable |
| 1 | 25 May 2026 | Landscape, infrastructure, regulatory baseline | 16 |
| 2 | 29 May 2026 | Verification and correction of the initial draft's claims | 10 |
| 3 | 15 September 2026 | Resumption; novelty audit and currency check | 10 |
| 4 | 16 September 2026 | Adversarial novelty testing, prior art, final currency | 23 |
| | | **Total** | **59** |

Round 0 requires explanation. An exploratory phase preceded the documented rounds and produced a full draft dated 24 May 2026, which survives as an artifact and is the reason the rebuild occurred. That draft contains no search strings, no inclusion criteria, no screening account, and no reference to any review protocol: a fact established by inspection of the file rather than by recollection. Its queries are not recoverable and are not reconstructed here. Round 0 is therefore reported at artifact level rather than query level, and contributes nothing to the absence claim of Section 2.9, which rests entirely on the four documented rounds.

Every query in rounds 1 to 4 is reproduced verbatim, by round, in Appendix B. The queries were natural-language rather than Boolean, which reflects both the mixed academic and governmental character of the corpus and the exploratory character of the early rounds.

Two features of the round structure bear on how the results should be read. Rounds 2 and 4 were adversarial in intent: round 2 tested the claims of an earlier draft and led to its abandonment, and round 4 sought work that would defeat the thesis's novelty claim rather than support it, which is how the closest prior art, a patent claiming key-expiry selection for retention-purge conflicts, was located and disclosed. Round 4 also produced a correction to the thesis's own headline claim, recorded in Chapter 4, Section 4.6.

### 2.1.5 Selection criteria and screening

Two criteria governed inclusion throughout. Every cited source must be retrievable through a public URL, a DOI, or a primary repository at the time of writing, so that any claim can be independently verified. And where secondary commentary conflicts with primary regulatory or standards text, the primary text prevails; secondary sources are cited for analysis or for evidence of practice, never for the factual content of an instrument.

Material was included where it was peer-reviewed work published between 2018 and 2026 bearing on cross-border health data exchange, cryptographic erasure, formal compliance verification, or the GDPR erasure right; primary regulatory, legislative, standards, or governmental material of any date; or practitioner and industry material where the claim being supported is one about industry practice rather than about law.

Material was excluded where it addressed data-protection regimes outside the European Union and European Economic Area without comparative bearing; where it was opinion writing without an identifiable evidential basis; where the work was not retrievable at the time of writing; and where a source could not be verified against a primary or publisher record. The last of these was applied to the thesis's own earlier draft. That draft carried twenty-eight distinct citations, of which approximately fourteen could not be verified against any primary or publisher record; the draft was discarded rather than repaired, and the verification audit that established this is recorded in the project's working log of 25 May 2026.

Screening proceeded from query results through title and abstract assessment to full-text or full-document assessment, with sources entering the working bibliography only after the verification step. Because the review was iterative rather than a single sweep, a PRISMA flow diagram reporting identification, screening, eligibility, and inclusion counts cannot be reconstructed honestly for rounds 1 and 2, whose intermediate counts were not retained. Reporting reconstructed counts would give the appearance of a systematic process that was not followed. What is retained and reported instead is the full query log, the working bibliography with its verification status per source, and the correction record.

### 2.1.6 Prospective Boolean protocol for replication

The following strings are offered so that a researcher may test this review's conclusions against a systematic sweep of indexed databases. They were not the instrument used here, and are stated prospectively.

| # | Target | String |
|---|---|---|
| B1 | Scopus, Web of Science | `TITLE-ABS-KEY(("crypto-shredding" OR "cryptographic erasure" OR "crypto erasure" OR "secure deletion" OR "data sanitization") AND ("GDPR" OR "right to erasure" OR "right to be forgotten"))` |
| B2 | Scopus, IEEE Xplore | `TITLE-ABS-KEY(("audit log" OR "audit trail" OR "access log") AND ("retention" OR "retention period") AND ("erasure" OR "deletion") AND ("conflict" OR "tension" OR "reconcil*"))` |
| B3 | Scopus, PubMed | `TITLE-ABS-KEY(("European Health Data Space" OR "EHDS" OR "MyHealth@EU" OR "eHDSI") AND ("secure processing environment" OR "audit" OR "retention" OR "erasure"))` |
| B4 | Scopus, IEEE Xplore, ACM | `TITLE-ABS-KEY(("formal verification" OR "satisfiability" OR "temporal logic" OR "constraint satisfaction") AND ("regulatory compliance" OR "legal compliance" OR "GDPR"))` |
| B5 | Scopus, Web of Science | `TITLE-ABS-KEY(("health data" OR "electronic health record") AND ("cross-border" OR "cross border") AND ("privacy" OR "data protection") AND ("Norway" OR "Nordic" OR "EEA"))` |
| B6 | IACR ePrint, arXiv | `("certified deletion" OR "proof of secure erasure" OR "provable deletion") AND ("verifiab*" OR "attestation")` |

Filters for replication: publication years 2018 to 2026 for B1, B2, B4 and B6; unrestricted for B3 and B5, since the relevant regulatory material predates the window. Document types: articles, conference papers, reviews, and preprints. Languages: English and Norwegian.

### 2.1.7 Limitations of the protocol

Four limitations follow from how the review was conducted and are stated so that they are not inferred from silence.

The exploratory phase preceding the documented rounds is acknowledged but not claimed as evidence, because its queries were never recorded; only the resulting draft survives, and it is used in this chapter solely as an artifact demonstrating the absence of a protocol. Screening was performed by a single reviewer, so no inter-rater reliability can be reported. Intermediate screening counts for the first two rounds were not retained, so no PRISMA flow diagram is offered. The queries were natural-language, so recall cannot be characterised in the way a Boolean strategy over an indexed corpus permits. And the absence of prior work on the central conflict, reported in Section 2.9, is established by four dated rounds including two adversarial ones together with an independent corroborating statement in the cryptographic literature: but an absence established by searching remains weaker evidence than a positive finding, and Section 2.9 states the additional reasons the gap is likely genuine rather than resting on the searches alone.

## 2.2 The Cross-Border Health Data Exchange Landscape

The European Union's cross-border health data infrastructure rests on a regulatory framework that has matured rapidly during the past three years, and on a technical platform that has been in operation, in voluntary form, for more than a decade. The two layers are now converging under the European Health Data Space Regulation, which establishes the legal architecture within which the existing technical platform must scale.

Regulation (EU) 2025/327 of 11 February 2025 establishing the European Health Data Space was published in the Official Journal on 5 March 2025 and entered into force on 26 March 2025, opening a multi-year transition during which Member States and European Economic Area countries must align their national infrastructures with binding Union-wide requirements (European Parliament and Council of the European Union, 2025). Entry into force and application must be distinguished, and the distinction bears directly on this thesis. Under Article 105 the Regulation applies generally from 26 March 2027, with staggered commencement thereafter: the secondary-use provisions of Chapter IV, which include both the Article 68(12) deletion ceiling and the Article 73(1)(e) log-retention floor, become applicable on 26 March 2029, and further milestones fall in March 2031 and March 2035. The regulation governs both primary use, meaning the use of electronic health data for the provision of healthcare to the data subject, and secondary use, meaning use for research, innovation, policy-making, regulatory activities, and public health (European Commission, 2025a). For primary use, the regulation establishes a calendar that the implementing acts must operationalise by 26 March 2027, with Group One priority categories of patient summaries and ePrescriptions becoming exchangeable across all Member States by 26 March 2029, and Group Two categories of laboratory results, medical imaging, and hospital discharge reports following by 26 March 2031 (Healthy Europe, 2026; European Commission, 2025a). Each Member State must designate a National Digital Health Authority by June 2025, and healthcare providers and electronic health record vendors must certify their systems for interoperability and security compliance by January 2026 (Ernst & Young, 2025).

The technical platform implementing cross-border primary use is MyHealth@EU, the operational successor to the eHealth Digital Service Infrastructure (eHDSI). MyHealth@EU connects national systems through National Contact Points for eHealth (NCPeH), each operated by the participating country's competent authority and funded historically through the Connecting Europe Facility Telecom Programme (2015–2020) and currently through the EU4Health Programme (2021–2027) (European Commission, 2025b). Governance is exercised by two coordinating bodies: the eHealth DSI EU countries Expert Group (eHMSEG), composed of managers responsible for NCPeH implementation in participating countries, and the eHealth Operational Management Board (eHOMB), composed of European Commission representatives and the eHMSEG Chairs (European Commission, 2025b).

The MyHealth@EU operational architecture follows a six-step transmission flow at the NCPeH gateway level, recently characterised in detail by Simjanoska Misheva et al. (2025). When a healthcare provider in a country of treatment requests cross-border data, the source country NCPeH performs service discovery to locate the patient's home country gateway; performs patient discovery against the patient's national identifier; retrieves the requested document, typically an International Patient Summary or an ePrescription, in the source country's native clinical document format; transforms it through a pivot transformer that converts national clinical document representations to the common European Electronic Health Record Exchange Format using SNOMED CT, LOINC, and other terminology bindings; applies the security and consent module, which validates the requesting clinician's eIDAS identity token and applies XACML-based consent policies; and finally logs the transaction in an IHE Audit Trail and Node Authentication compliant audit repository with a minimum ten-year retention period.

Norway's integration with MyHealth@EU is being implemented through a project that began in January 2023 under the joint operational responsibility of Helsedirektoratet and Norsk Helsenett SF, the national operator of the closed Norwegian health network, with a planned duration of 41 months. The pilot is live at the emergency clinics in Bodø and Stjørdal, connected to Portugal, Czechia, and Finland for the receipt of patient summaries concerning citizens of those states requiring care in Norway, with the Bodø and Stjørdal clinics in production with Czechia and Portugal and the emergency clinics in Trondheim and Ålesund, operating on Helseplattformen, having requested the service for the next stage (Helsedirektoratet, 2026a, 2026b). The Directorate's portfolio reporting records that no relevant patients had yet presented for the solution to be used in practice, so the infrastructure is operational while the volume of records generated remains small; this thesis relies on the former and does not claim the latter. Infrastructure for receiving ePrescriptions has been planned and developed but is not yet in use, and Norway's scenario of implementing ePrescription without eDispensation was carried as a change proposal to the requirement catalogue and approved in the eHealth Operational Management Board on 12 March (Helsedirektoratet, 2026a). Because Norway is a member of the European Economic Area rather than of the European Union, the EHDS Regulation does not apply directly but is being processed for incorporation through the EEA Joint Committee. The Norwegian Directorate of Health delivered its formal EHDS impact and gap analysis on 11 April 2025, identifying the principal areas in which Norwegian law and infrastructure will require alignment (Helsedirektoratet, 2025a).

Parallel to the primary-use track, the regulation establishes a secondary-use track through which national Health Data Access Bodies coordinate access to electronic health data for research, innovation, and policy purposes. The interconnecting infrastructure for secondary use is HealthData@EU, which complements MyHealth@EU and operates under different technical and governance arrangements. The technical, functional, and security specifications for the Secure Processing Environments through which secondary-use data must be processed have been developed under the TEHDAS2 Joint Action, a coordinated effort of twenty-nine countries running until December 2026 (Healthy Europe, 2026). TEHDAS2 published these specifications during 2026, setting out the minimum technical, functional, and security capabilities that Secure Processing Environments must offer, together with baseline interoperability requirements for federations of such environments, and positioning the document as input to standardisation work and to the European Commission's implementing acts (TEHDAS2, 2026). The implementing acts themselves, which will lay down the binding technical, organisational, information-security, confidentiality, data-protection, and interoperability requirements for Secure Processing Environments under Article 73(5) EHDS, are due by 26 March 2027 and had not been adopted at the time of writing. The Norwegian Health Data Access Body designated under this regime is Helsedataservice, hosted at the Folkehelseinstituttet (Norwegian Institute of Public Health), which since 2023 has held the decision-making authority for eleven statutory national health registries (Folkehelseinstituttet, 2024).

The historical context of these institutional arrangements is important for the present thesis. The Norwegian central analytics platform Helseanalyseplattformen was paused in December 2021 following legal challenges related to the Schrems II judgment on transatlantic data transfers, and was formally avviklet by the Ministry of Health and Care Services in February 2023. The Direktoratet for e-helse, which had led much of the early national e-health standards work, was itself dissolved in May 2023, with its core functions absorbed into Helsedirektoratet from 2024 onwards (Helsedirektoratet, 2023). The Norwegian secondary-use infrastructure that the EHDS will be implemented against is therefore not a centralised analytic platform but a distributed model resting on the three university-based trusted research environments — TSD at the University of Oslo, SAFE at the University of Bergen, and HUNT Cloud at NTNU: coordinated through the NORTRE collaboration (Norwegian Trusted Research Environments, 2025).

The cross-border landscape is therefore mature in its regulatory architecture, advancing in its technical infrastructure, and concretely defined in its Norwegian implementation. It is against this landscape that the audit-retention and erasure tensions become not abstract but operationally consequential, as Section 2.3 will demonstrate.

## 2.3 The Audit-Retention versus Right-to-Erasure Tension

The thesis is built around a specific structural tension between three retention regimes that operate concurrently on the same cross-border health data event. Each regime is grounded in primary sources: a technical integration profile, a binding regulation, and an evolving Joint Action specification. None resolves the others. This section examines each regime in turn, then characterises the resulting conflict, the principal legal objection to its existence, and the regulatory doctrine that has developed around what counts as erasure.

The first regime is technical. The IHE Audit Trail and Node Authentication (ATNA) profile, maintained in Volume 1 Chapter 9 of the IHE IT Infrastructure Technical Framework, specifies the foundational audit and security requirements for nodes participating in interoperable health information exchange (IHE International, 2024). ATNA establishes a Basic Secure Node that must authenticate other nodes, encrypt communications using TLS, log triggered events such as queries, views, additions, deletions, and changes within the security domain, and transmit those audit records to an Audit Record Repository. The IHE specification itself does not mandate a single global retention period, leaving that decision to the realm-specific or domain-specific deployment binding. The eHDSI security framework that operationalises ATNA within the MyHealth@EU infrastructure does specify retention in concrete terms. The framework adopted by the eHMSEG governance body for cross-border NCPeH operations requires audit repositories to retain records for a minimum of ten years, characterised by Simjanoska Misheva et al. (2025) as the binding deployment baseline. This retention floor exists because cross-border audit records support not only patient-facing access logs but also accountability for the eIDAS-based authentication of the requesting clinician, the consent validation step, and the audit trail required under the European Health Data Space patient-rights provisions.

The second regime is legal. Article 17 of the General Data Protection Regulation (Regulation (EU) 2016/679) establishes the data subject's right to obtain from the controller the erasure of personal data concerning them without undue delay, where one of the conditions in Article 17(1) applies (European Parliament and Council of the European Union, 2016). These conditions include the cessation of the original purpose, the withdrawal of consent without an alternative legal basis, an objection under Article 21 with no overriding legitimate interest, and unlawful processing. The data controller bears an independent obligation to erase in these conditions, irrespective of whether the data subject has formally exercised the right (European Data Protection Board, 2026a). Article 17(3) provides limited exemptions, of which two are directly relevant to the cross-border audit context. Article 17(3)(b) permits the controller to refuse erasure where processing is necessary for compliance with a legal obligation imposed by Union or Member State law. Article 17(3)(d) permits refusal where processing is necessary for scientific or historical research purposes or statistical purposes, in so far as erasure is likely to render impossible or seriously impair the achievement of those purposes. The European Data Protection Board's Coordinated Enforcement Framework report on Article 17, published on 18 February 2026 following an investigation involving 32 supervisory authorities and 764 controllers, identified the implementation of retention periods among the recurring issues, recommending further practical guidance on how to define and implement retention periods consistent with national legal obligations (European Data Protection Board, 2026a; Matheson, 2026).

The third regime is operational and emerging. The TEHDAS2 Joint Action's guideline for Health Data Access Bodies on procedures and formats for data access specifies that personal data must be deleted from a Secure Processing Environment within six months of the expiry of the data permit, under Article 68(12) of the European Health Data Space Regulation (TEHDAS2, 2025; European Parliament and Council of the European Union, 2025). This is a ceiling rather than a floor. After the six-month window, only anonymised analytical results may continue to exist outside the Secure Processing Environment, and personal data are not permitted to remain. The same TEHDAS2 deliverable specifies a five-phase user journey for data access that ends in a deletion event marking the closure of the permitted processing.

The regulation places a retention floor on that same environment. Article 73(1)(e) EHDS requires Secure Processing Environments to keep identifiable logs of access to and activities within the environment for the period necessary to verify and audit all processing operations, and specifies that logs of access be kept for at least one year (European Parliament and Council of the European Union, 2025). Identifiable access logs are personal data and are data within the environment. Article 68(12) governs, in terms, the data within the secure processing environment rather than only the dataset supplied under the permit; on that reading the Regulation requires of one environment both that data be removed within six months of permit expiry and that identifiable logs persist for at least twelve months. The reading is contestable — the provision sits within the data-permit article, and a narrower construction confines it to the permitted dataset: and Chapter 4, Section 4.6 states the grounds on both sides and shows which results depend on which. On the broad reading this is the audit-retention versus erasure tension in its purest form: not a conflict assembled across instruments of differing legal weight, but a floor and a ceiling stated in adjacent articles of the same chapter of the same regulation, and with the implementing acts that might reconcile them not due from the Commission until 26 March 2027 under Article 73(5), two years before the provisions themselves become applicable on 26 March 2029.

The standard practitioner heuristic for conflicting retention obligations cannot resolve this. Guidance for multi-framework environments routinely advises applying the longest applicable retention period across all frameworks: a rule that works when every obligation is a floor, and fails entirely when one obligation is a ceiling, since extending retention to satisfy the longer floor is precisely what the ceiling forbids. The absence of an applicable heuristic is one reason the conflict has remained open in practice as well as in the literature.

A further explanation is procedural and worth recording, because the apparent obviousness of the conflict otherwise invites the question of why it has not been addressed. In the Commission's 2022 proposal, the six-month deletion obligation appeared in Article 46 and the Secure Processing Environment provisions in Article 50; both were renumbered on adoption in 2025 to Articles 68 and 73 respectively. A substantial part of the published commentary on EHDS secondary use was written against the proposal numbering, with the deletion obligation and the environment's security requirements analysed in separate literatures that were never subsequently brought onto the same page.

The conflict is structural and operational. When a Norwegian patient is treated under MyHealth@EU in another Member State, the cross-border access event is logged in the foreign NCPeH's ATNA-compliant audit repository for at least ten years. During that window, the patient retains the right to request erasure of personal data under Article 17. If the erasure request is granted, the audit record loses its referential integrity: it points to data that no longer exist. If the erasure request is refused on Article 17(3)(b) grounds, the controller must demonstrate that the retention is genuinely necessary for compliance with a specific legal obligation, which is the recommendation the European Data Protection Board made in February 2026 (Matheson, 2026). When the same patient's data move through the secondary-use pathway and reach a Norwegian Secure Processing Environment under a Helsedataservice permit, the Article 68(12) deletion ceiling applies. Yet the same environment must retain identifiable access logs for at least one year under Article 73(1)(e), and the audit records of the cross-border exchange that initiated the secondary-use request remain subject to the eHDSI ten-year baseline. Practitioner and supervisory commentary consistently reads the erasure obligation as extending to all storage locations of the personal data, including backups and logs (see, e.g., the Norwegian legal commentary summarised in Berngaard, 2024), which is precisely why the audit trail cannot be quietly carved out of the conflict.

The most direct legal objection to the existence of the conflict must be addressed before its technical treatment. Article 17(3)(b) GDPR provides that the right to erasure does not apply to the extent that processing is necessary for compliance with a legal obligation to which the controller is subject. On a broad reading, the audit-retention obligation of the eHDSI baseline would simply disapply Article 17 for audit records, and the three regimes would never collide. This thesis argues that the exemption narrows the conflict without dissolving it, for three reasons grounded in the primary instruments. First, the exemption is bounded by necessity: it excuses only the processing that the legal obligation actually requires, and the storage-limitation and data-minimisation principles of Article 5(1)(c) and 5(1)(e) GDPR continue to apply to whatever is retained. The accountability function of a cross-border audit record — who accessed what, when, from where, under which legal basis, with what outcome: does not require continued controller access to the full personal-data payload of the underlying exchange; retention of the payload in accessible plaintext for ten years therefore exceeds the necessity that Article 17(3)(b) protects. Second, the Norwegian Data Protection Authority's internal-control guidance places precisely this balancing on the controller, requiring organisations to determine lawful retention periods and deletion deadlines through an explicit weighing of purpose, business need, and both retention rights and retention duties imposed by other law (Datatilsynet, n.d.-a) — a formulation that presupposes, rather than dissolves, the coexistence of retention obligations and deletion obligations on the same records. Third, the six-month deletion ceiling of Article 68(12) EHDS, as operationalised in the TEHDAS2 guidance for Health Data Access Bodies, contains no exemption parallel to Article 17(3)(b); within the secondary-use pathway the ceiling binds regardless of how the erasure-versus-retention balance is struck for the audit floor. The conflict therefore survives the exemption in a precise, narrowed form: the contested object is not whether audit records may be retained, but how much of a record may remain accessible, for how long, and in what state: exactly the question the mechanism developed in Chapter 4 formalises.

A direct technical solution to this tension exists in the literature on cryptographic erasure, though its application to the cross-border health audit problem has not been systematically developed. The National Institute of Standards and Technology's Special Publication 800-88 Revision 2 recognises cryptographic erasure as a purge-grade sanitization technique, in which the encryption key used to protect the data is irreversibly destroyed while the encrypted data remain on the storage medium (National Institute of Standards and Technology, 2025). Practitioner implementation guidance asserts that cryptographic erasure is increasingly accepted as a means of satisfying Article 17 in distributed cloud environments, conditional on auditable key management and demonstrably irreversible key destruction (Oneuptime, 2026). That assertion is reported here as evidence of industry practice rather than as a statement of regulatory position; the authoritative position on cryptographic unrecoverability is the European Data Protection Board's, set out later in this section. The technique is not without criticism. SecuPi (2025) argues that cryptographic erasure introduces operational complexity in row-level encryption scenarios and that auditable key management adds rather than removes overhead, making it inappropriate as a general solution for the right to erasure in heavily distributed systems. Engaging with this critique is essential for the thesis to remain defensible; Chapter 6 returns to it explicitly.

Regulatory doctrine on what counts as erasure has moved substantially during the review period, in a direction that bears directly on this thesis. The Norwegian Data Protection Authority's privacy-by-design guidance states that anonymisation is equated with deletion of personal data ("anonymisering likestilles med sletting av personopplysninger"), so that rendering data irreversibly non-identifiable discharges the deletion obligation (Datatilsynet, n.d.-b). The same authority's anonymisation guidance, however, sets a deliberately high threshold: encryption is characterised as a means of protecting data, not of rendering it unidentifiable, and data remain personal as long as the controller retains any key or linkage capable of re-identification (Datatilsynet, 2015). At Union level, the European Data Protection Board's Guidelines 02/2025 on the processing of personal data through blockchain technologies accept that where physical overwriting is technically impossible, rendering the data unrecoverable through cryptographic means can constitute an adequate substitute for erasure, provided the controller documents the threat model under which the data are considered unrecoverable (European Data Protection Board, 2026b). Read together, these positions define the legal corridor within which any cryptographic-erasure mechanism must operate: key destruction can discharge the erasure obligation only if it is irreversible in the documented threat model, and any residue that survives, including hashes and commitments, must itself be assessed against the high anonymity threshold. Chapter 4 designs to this corridor explicitly, and Section 2.4 returns to the residue question.

What does not yet exist in the literature, and what this thesis addresses, is the specific design of a verifiable invalidation mechanism that operates at the cross-border audit-trail boundary defined by ATNA, the eHDSI ten-year retention baseline, GDPR Article 17(3)(b), and the TEHDAS2 six-month rule, in a manner that is both technically demonstrable and compatible with the operational reality of Norwegian NCPeH and Helsedataservice. The next section reviews the cryptographic literature that informs the design of such a mechanism.

## 2.4 Cryptographic Approaches to Audit Compliance

A growing body of cryptographic and systems research has developed mechanisms that address parts of the audit-compliance problem in cross-border and multi-institutional health data settings. The four most relevant strands are trusted-execution-environment-based architectures applied to OpenNCP, blockchain-based audit logging adapted to healthcare, zero-knowledge proofs applied to electronic health records and decentralised identity, and the underlying cryptographic primitives of commitment schemes and accumulators that make revocation mathematically tractable. This section reviews each strand in turn, together with the secure-deletion foundation on which cryptographic erasure rests and the adjacent literatures from which the present problem must be distinguished.

The KONFIDO project, funded under the Horizon 2020 programme between 2016 and 2019, remains the most directly relevant architectural ancestor for the present work. KONFIDO extended the OpenNCP cross-border health data exchange platform with a holistic security toolkit organised around four technical pillars: photonic Physical Unclonable Functions for hardware-rooted identity, homomorphic encryption for computation on encrypted patient summaries, a Security Information and Event Management system for distributed monitoring, and a blockchain-based auditing component for cross-border traceability and liability support (Diamantopoulos et al., 2019; Staffa et al., 2018). KONFIDO was piloted in Denmark, Italy, and Spain, and the lessons-learned synthesis published by Natsiavas et al. (2021) documented both the technical achievements and the substantive gaps in scaling the approach. Two of those gaps are directly relevant. First, the KONFIDO security architecture relied on Intel Software Guard Extensions trusted execution environments, creating a hardware dependency that complicates broad NCPeH deployment across heterogeneous Member State infrastructures. Second, KONFIDO's blockchain auditing component, designated as a "disruptive logging" mechanism in the project documentation, provided immutable traceability but did not engage the General Data Protection Regulation's right to erasure as a design constraint. The audit chain was treated as a feature whose value derived from its immutability, with the conflict between immutability and erasure left unresolved.

A second strand of work has explored zero-knowledge proofs applied to electronic health record access control, with the most direct comparator for the present thesis being Albalwy (2026). The ZK-EHR framework uses a Groth16 zk-SNARK circuit to enforce policy compliance for cross-institutional health data sharing, with three actor roles defined as the Patient as data owner, the Doctor as care provider, and the Researcher as authorised analyst. Encrypted records are stored on the InterPlanetary File System, with on-chain smart contracts handling policy enforcement and cryptographic verification. The architecture decouples authorisation from identity disclosure, allowing a requesting actor to prove they hold valid policy-compliant credentials without revealing their identity, role, or affiliations. The framework reports an on-chain verification latency of approximately 390 milliseconds and a gas consumption of 216,631 units per verification. Albalwy's contribution occupies the cross-institutional space within a single jurisdiction; the cross-border space addressed by MyHealth@EU, with its eIDAS-based authentication chains and its operational coupling to ATNA-compliant audit repositories spanning multiple national legal regimes, is genuinely distinct.

The Health-zkIDM system developed by Bai et al. (2022) provides a complementary perspective. Built on Hyperledger Fabric with zero-knowledge proof components implemented at the chaincode level, Health-zkIDM achieves throughput exceeding 400 transactions per second in Caliper benchmarking, demonstrating that decentralised identity management with cryptographic privacy guarantees is operationally viable in healthcare settings. The architecture targets identity verification rather than audit-trail erasure, but its performance evidence is informative for the design constraints of any cross-border verifiable compliance mechanism.

A more recent contribution is zkFL-Health (Sharma et al., 2025), which combines federated learning with zero-knowledge proofs and trusted execution environments for medical artificial intelligence training. Clients train locally and commit cryptographic representations of their updates; an aggregator operating within a trusted execution environment computes the global update and produces a succinct zero-knowledge proof, generated using Halo2 or Nova, that the aggregation used exactly the committed inputs and applied the prescribed rule, without revealing any individual client update. Verifier nodes record cryptographic commitments on-chain, creating what the authors explicitly characterise as an "immutable audit trail" removing the need to trust any single party. zkFL-Health is significant for the present thesis in two respects: it demonstrates that the combination of trusted execution environments and zero-knowledge proofs can produce verifiable audit trails compatible with healthcare data, and it provides a recent illustration of the design pattern where commitments on-chain reference data held off-chain: a pattern central to the cryptographic-erasure-by-invalidation mechanism this thesis proposes.

Within the Norwegian clinical context, the NewbornTime project provides a deployed precedent. Brunner et al. (2025) document the deployment of a Hyperledger-based digital consent platform at Stavanger University Hospital, used between November 2021 and June 2025 in the collection of 1,012 thermal videos of newborn resuscitation events. The platform stores consent status immutably on-chain while keeping personal data encrypted and off-chain, providing a protected API for authorised retrieval and a documented General Data Protection Regulation-compliant withdrawal mechanism. The clinical viability of blockchain-anchored consent infrastructure in a Norwegian regulated healthcare setting is therefore established, although the system addresses consent recording rather than the audit-trail erasure problem.

A fourth strand of work, less visible in the healthcare literature but foundational to the design of any verifiable invalidation mechanism, is the cryptographic accumulator and commitment scheme literature. Benaloh and de Mare (1993) introduced one-way accumulators as a means of accumulating elements from a finite set into a single short value supporting membership testing. Camenisch and Lysyanskaya (2002) extended this work to dynamic accumulators with efficient revocation of anonymous credentials, providing the mathematical machinery for verifiable membership and non-membership proofs in sets that change over time. Ren (2022) surveys the field, covering applications ranging from anonymous credentials and certificate revocation through to blockchain-based audit systems.

The technique this thesis applies sits within a mature secure-deletion literature whose central caution must be carried into the design. The canonical systematisation by Reardon, Basin, and Capkun (2013) defines secure deletion as rendering data irrecoverable from a physical medium, organises approaches by their interface to that medium, and demonstrates that the further an approach operates from the medium, the harder it becomes to assert that destruction has actually occurred. Cryptographic erasure is the limiting case of this observation: it operates entirely above the medium, reducing the deletion of arbitrarily large data to the deletion of a key, and thereby inheriting in concentrated form the problem that key destruction itself cannot be proven to an external party by inspection. This limitation is not fatal — NIST SP 800-88 Revision 2 recognises cryptographic erase as a purge-grade sanitization technique precisely because, within a documented key-management boundary, it offers high assurance: but it defines the honest boundary of any crypto-erasure guarantee: the mechanism's properties are conditional on honest and verifiable key-lifecycle management, a condition examined further in Chapter 6.

During the review-update period, the formal treatment of cryptographic erasure advanced significantly. Aikebaier's (2026) systematisation of cryptographic erasure on public ledgers organises the application-layer construction space along two axes, data locus and key custody, into a twelve-cell grid of canonical constructions from 2006 to 2026; extends IND-CCA security with a key-lifecycle adversary model parametrised by hardware-security-module side-channel leakage, coercion fraction over the custody committee, and algorithmic-break horizon; and establishes an equivalence proposition between the resulting Destruction-IND notion and the EDPB Guidelines 02/2025 criterion of rendering data unrecoverable. The work is a single-author preprint with industry affiliation and has not been peer-reviewed; it is treated here as a systematisation of the field rather than as settled result, and the thesis does not rest any legal conclusion on it.

Three features of that work matter for the positioning of this thesis. First, it demonstrates that the erasure side of the problem, under what cryptographic conditions key destruction constitutes erasure, now has a rigorous formal treatment on which this thesis can build rather than a gap it must fill. Second, the work confines itself to erasure under Article 17 and does not treat retention under sectoral law. Third, and most directly, among the five open problems it identifies for the field is *erasure under multi-regime retention conflict* — the problem this thesis formalises and resolves. The gap claimed in Section 2.9 is therefore not established solely by this author's failure to find prior work; it is named as open by the most recent systematisation of the relevant cryptographic literature.

Two adjacent bodies of work must finally be distinguished from the problem addressed here, one academic and one practitioner. The academic body is the extensive blockchain-and-GDPR literature. Finck's analyses for the European Parliament and in the data-protection literature established the canonical tension between ledger immutability and the right to erasure, together with two findings of continuing relevance: that the meaning of "erasure" and "anonymisation" under GDPR is itself legally uncertain, and that hashed or encrypted data likely remain personal data for GDPR purposes so long as re-identification is possible (Finck, 2018; Finck, 2019). A systematic review of 114 papers in this literature reports difficulties in exercising data-subject rights, the right to be forgotten foremost among them, as the first of three principal issue types arising from blockchain immutability (Belen-Saglam, Altuncu, Lu, & Li, 2023). That conflict is adjacent to, but distinct from, the one this thesis addresses: it arises from a technological property (immutability) chosen by the system designer, whereas the conflict here arises from regulatory instruments imposing simultaneous floors and ceilings on retention regardless of storage technology. The distinction matters for design: a blockchain-immutability conflict can be dissolved by choosing mutable storage, while the tri-lateral regulatory conflict cannot be dissolved by any storage choice at all. Finck's finding on hashes, however, applies with full force to this thesis's mechanism: a commitment that survives invalidation is a residue that must be assessed against the anonymity threshold, and Chapter 4 therefore specifies hiding (salted) commitments and treats the residue question as a first-class design constraint rather than a footnote.

A third adjacent body is the closest prior art to the mechanism proposed in this thesis, and honest scholarship requires it be surfaced rather than left for a reviewer to find. A research programme at DePaul University has addressed the reconciliation of retention and purging obligations in relational database systems across a sequence of publications and a granted patent. Scope, Rasin, Lenard, Heart, and Wagner (2022) formalise data-policy compliance rules for retention and purging and implement automated enforcement in a relational database; companion work extends the approach to database backups through cryptographic erasure (Scope, Rasin, Lenard, Wagner, & Heart, 2022); and the approach is claimed in United States Patent 12,425,209 (Scope & Rasin, 2025), which specifies shadow tables holding encrypted copies whose encryption keys are selected according to the purge date of the data they protect, with purging effected by destroying the corresponding key.

This is a substantial body of work and it converges independently on the same insight as the present thesis: that key-lifecycle control is the natural engineering response to conflicting retention obligations. Three differences bound the overlap, and the first is decisive.

The mechanism satisfies the retention obligation by keeping *recoverable* encrypted copies, the key still exists until the purge date arrives, in shadow tables and shadow backups. That is the correct design when both obligations are floors and the purge date is known in advance, because retention simply runs until the later date. It cannot work against a deletion ceiling. Keyed ciphertext remains personal data under the Norwegian threshold established in Section 2.3, since the controller retains the means of re-identification; holding recoverable copies to satisfy a retention floor is therefore precisely what Article 68(12) forbids of a Secure Processing Environment. The tri-lateral case inverts the design requirement rather than extending it.

Second, the work addresses per-value data within a database and its backups, not the audit trail of a cross-border exchange, and it supplies no verifiability semantics: nothing in the framework allows an external auditor to establish what was purged, when, or on what legal ground. Third, the erasure trigger in that work is a scheduled purge date fixed in advance, whereas the erasure right modelled here arrives at an arbitrary time chosen by the data subject, which is what makes the feasibility question non-trivial. The programme is prior art for the technique and for the retention–purge reconciliation problem in databases; it is not prior art for the tri-lateral conflict, for the audit-trail setting, or for the verifiability semantics.

A fourth body concerns whether erasure can be proven at all. Proof-of-Secure-Erasure protocols seek evidence that a prover has erased its memory, and recent formal work relaxes the isolation assumptions those protocols traditionally require (Bursuc, Gil-Pons, Mauw, & Trujillo-Rasua, 2024). In the quantum setting, encryption with certified deletion produces a deletion certificate, and its authors identify public verifiability, allowing parties other than the originator to verify such a certificate, as an open problem (Broadbent & Islam, 2020). This literature marks the outer boundary of the present thesis: the mechanism specified in Chapter 4 logs an *attested* invalidation, not a *proven* one, and the difference between those is the subject of an active research programme rather than something this thesis resolves.

The practitioner body is the rapidly consolidating industry pattern of crypto-shredding for reconciling erasure with record-keeping obligations, articulated most fully for the financial sector, where GDPR Article 17 collides with the five-to-seven-year retention obligations of MiFID II Article 16(7) and analogous instruments (VeritasChain Standards Organization, 2026). The pattern — encrypt per subject, destroy the key on request, retain the ciphertext and the structural record: is the same family of technique this thesis employs, and its cross-sector articulation confirms that the technique itself is established practice rather than a novel contribution. Three things distinguish the present work from this practitioner pattern. First, the financial formulation is bi-lateral (a retention floor against an erasure right); the EHDS setting adds a third, structurally different constraint, a deletion ceiling on Secure Processing Environments, producing a tri-lateral system whose joint satisfiability is not obvious and has not been analysed. Second, the practitioner pattern asserts reconciliation; it does not provide a formal model within which reconciliation is derived, nor verifiability semantics, commitments and accumulator witnesses, by which an external auditor can check that invalidation occurred and what it invalidated. Third, no articulation of the pattern addresses the cross-border health audit trail, its standards stack, or a national implementation substrate. These three deltas — the formal tri-lateral model, the verifiability semantics, and the cross-border health instantiation: are where the contribution of this thesis lies, and Section 2.9 states them as gaps with this precision.

Three observations emerge from this survey. First, the technical components required for a verifiable cryptographic-erasure mechanism for cross-border health audit trails exist in mature form: trusted execution environments at the OpenNCP layer (KONFIDO), zero-knowledge proof systems applied to healthcare (Albalwy 2026, Health-zkIDM, zkFL-Health), blockchain-anchored consent and audit infrastructures with Norwegian clinical validation (NewbornTime), cryptographic accumulators with revocation semantics (Camenisch and Lysyanskaya 2002 and the subsequent literature), and a formally grounded cryptographic-erasure foundation. Second, none of these works combines these components to address the specific tension between eHDSI-mandated audit retention, GDPR Article 17 erasure rights, and TEHDAS2 Secure Processing Environment deletion in the cross-border European context. Third, the broader policy literature on privacy-enhancing technologies under the European Health Data Space, including the research agenda published in Frontiers in Digital Health (2025), explicitly identifies this kind of governance-and-technology integration as an open research category. The contribution of this thesis is positioned at that named gap.

## 2.5 Formal Approaches to Regulatory-Compliance Verification

The thesis's analytical method belongs to a research tradition that treats legal compliance as a formal-verification problem, and this tradition must be reviewed both to anchor the method and to bound the novelty claim honestly.

The most direct methodological ancestor is the work of Feng, Marsso, Sabetzadeh, and Chechik (2022) on bounded satisfiability checking of legal properties expressed in Metric First-Order Temporal Logic. Their approach formalises obligations drawn from legal texts as temporal-logic properties, reduces satisfiability checking to Satisfiability Modulo Theories solving, and generates counterexamples that witness compliance violations, with case studies spanning regulated domains including healthcare. The significance for this thesis is double-edged and is stated plainly. On one side, the general method — regulatory obligations as formal constraints, compliance as a satisfiability question, violations as derivable counterexamples: is established, and this thesis claims no novelty for it. On the other side, the method has not been applied to the specific tri-lateral conflict of the cross-border health audit trail, and the instantiation developed in Chapter 4 deliberately employs lighter machinery than the MFOTL-and-SMT apparatus: a feasibility formulation over discretised time with one binary accessibility variable per record, in the constraint-modelling style of the operations-research tradition. The choice of lighter machinery is methodological, not accidental: the tri-lateral conflict turns on a single semantic question, what "verifiable" means for an audit record, and a formulation that isolates that question is more defensible, more communicable, and more faithful to the logistics-modelling identity of the thesis than a fully general temporal-logic encoding.

A second relevant strand is the formal treatment of erasure obligations in adjacent technical settings. In machine learning, formal accounts of the right to erasure have produced the machine-unlearning literature; these works formalise what it means to remove a data subject's influence from a trained model, a different erasure object from the audit record treated here, but methodologically kindred in deriving mechanisms from formally stated erasure requirements. In cryptography, the 2026 systematisation of cryptographic erasure discussed in Section 2.4 provides the formal foundation for the erasure side of the present problem, including a security notion and an equivalence argument to the regulatory unrecoverability test, while explicitly excluding sectoral retention law from its scope.

A third strand applies optimisation and operations-research methods to regulatory compliance itself. Mixed-integer and simulation models have been developed for supply-chain compliance under regulatory constraint sets, and compliance-management systems for cross-border data transfer have been proposed as engineering artefacts (Zhuang et al., 2024). This strand demonstrates that compliance reconciliation is a recognised object for the modelling tradition in which the author is trained; it has not, however, been applied to the reconciliation of data-retention regimes.

The synthesis of this section is a precise statement of what is and is not available. Available: a general formal method for legal-compliance satisfiability (Feng et al., 2022); a formal foundation for cryptographic erasure as Article 17 erasure (Aikebaier, 2026; European Data Protection Board, 2025); optimisation methods for regulatory compliance in physical supply chains. Not available anywhere in the reviewed literature: a formal feasibility analysis of the tri-lateral retention system — floor, right, and ceiling operating concurrently on the same records: in any sector; any formal treatment situated at the cross-border health audit boundary; and any treatment in information-logistics terms. The Tri-Lateral Retention Feasibility Model of Chapter 4 is constructed to occupy exactly this space, borrowing its method from the first strand, its erasure semantics from the second, and its modelling style from the third.

## 2.6 Norwegian Secondary-Use Infrastructure

Norway's secondary-use infrastructure for health data is the substrate against which the European Health Data Space will be implemented at the national level. The infrastructure has three layers: a governance and access-decision layer through Helsedataservice, a data-custodian layer through the major registry holders, and an analytical-processing layer through a set of Secure Processing Environments coordinated through the NORTRE collaboration but extending, in operational practice, well beyond it. Each layer presents a distinct compliance surface, and each interacts directly with the audit-retention versus erasure tension developed in Section 2.3.

Helsedataservice is the Norwegian Health Data Access Body designated under the emerging European Health Data Space governance architecture. It took on its current authority on 15 March 2023, when decision-making authority over data access from eleven central health registries was transferred to Helsedataservice under the statutory changes introduced through Prop. 63 L (Forskningsetikk, 2023; Helse- og omsorgsdepartementet, 2020). Applications are submitted through the helsedata.no portal; Helsedataservice registers and forwards each application to the relevant data custodian — including the Norwegian Institute of Public Health, the Norwegian Directorate of Health, and the Cancer Registry: who decide on access, with a two-stage cost structure mirroring the two-stage decision structure (Helsedataservice, 2024).

The Secure Processing Environment layer is where the operational reconciliation of EHDS Article 73 with Norwegian implementation must occur, and the national policy process has now completed its first full cycle there. The SPUHiN project's November 2024 draft recommendations documented the state of Norwegian SPE practice in a passage that remains the decisive empirical fact for mechanism design in this thesis. Based on applicants' own descriptions in permit applications to Helsedataservice during 2023, the drafting team observed that "it is however most common to use either an analysis infrastructure currently available from the universities... or some type of server, database, folder, area or zone most likely provided by the data controller's own IT provider. A few also refer to OneDrive, Office365, disconnected PC or a partner in another country" (SPUHiN, 2024, p. 4). The Norwegian SPE landscape is therefore not merely distributed across the three NORTRE university nodes but operationally fragmented, with substantial secondary-use processing occurring outside any trusted-research-environment substrate.

Following a public hearing conducted between July and October 2025, the recommendations were consolidated into final form as SPUHiN deliverable D5.2, *Recommendations for minimum requirements for Secure Processing*, comprising separate compliance checklists for SPE providers and SPE user organisations, each requirement graded as mandatory or recommended, developed in collaboration with researchers, data custodians, technology suppliers, and authorities, and positioned as a national reference basis for actors preparing for the coming EHDS requirements pending the Union implementing act (Helsedirektoratet, 2025b; SPUHiN, 2025). Inspection of the finalised checklists shows their scope to be information-security management, identity assurance, and access governance — an ISMS requirement graded mandatory, ISO 27001 certification recommended, eID-based login with defined assurance levels, personnel-security controls: with several recommended requirements explicitly anticipated to harden into expectations as EHDS is implemented (SPUHiN, 2025). What the finalised criteria do not contain, at any grade, is a requirement or mechanism addressing the reconciliation of audit-retention obligations with erasure and deletion obligations on the records the SPE generates. The gap identified by this thesis therefore survives contact with the final national document, not merely its draft: Norway now possesses finalised SPE criteria that govern how the environment is secured and who may enter it, while leaving unaddressed what happens when the retention regimes on its records collide.

The three primary NORTRE nodes — TSD at the University of Oslo (operational since 2012), SAFE at the University of Bergen (2015), and HUNT Cloud at NTNU (2013) — provide infrastructure meeting European trusted-research-environment standards and participate in the EOSC-ENTRUST federation blueprint (Norwegian Trusted Research Environments, 2025). On the primary-use side, the national infrastructure has moved from preparation into operation during the review period: the Norwegian NCPeH pilot is live at the Bodø and Stjørdal emergency clinics in exchange with Portugal, Czechia, and Finland, with the outbound NCP-A capability under construction during 2026 (Helsedirektoratet, 2026a), so that the cross-border audit records this thesis concerns are beginning to be generated in Norwegian production, at presently small volume.

The design consequence carried into Chapter 4 is unchanged and strengthened. A verifiable cryptographic-erasure mechanism that assumes a clean, homogeneous SPE substrate would fail against the documented fragmentation; a mechanism that assumes the substrate question will be settled by the national criteria would fail against their actual scope. The same holds at Union level: the Secure Processing Environment specification published by TEHDAS2 during 2026 as deliverable D7.4 define the minimum capabilities such environments must offer and the interoperability baseline for federating them, and the Joint Action's guidance on using data within such an environment treats deletion at permit closure as an operational service; neither connects that deletion obligation to the one-year identifiable-log retention floor imposed on the same environment by Article 73(1)(e) (TEHDAS2, 2025, 2026). The body drafting the specifications for both provisions has not addressed their interaction. A mechanism designed at the audit-trail boundary — operating identically whether the processing occurred in TSD, on a controller's own server, or on a disconnected PC, and requiring of the substrate nothing that the finalised criteria do not already demand: fits the Norwegian context as it actually is.

## 2.7 Information Logistics Framing

The thesis frames the audit-retention versus erasure problem as one of information logistics. This framing is not a metaphor but an analytical commitment that grounds the contribution within the disciplinary identity of Sustainable Energy Logistics at HiMolde and within an active academic literature on cross-border data movement under regulatory constraint.

The International Chamber of Commerce (2025) policy brief on data flows in supply chains documents that cross-border data flows are functionally equivalent to material flows in their structural role within global supply chain operations. They enable real-time coordination, traceability, customs clearance, and the deployment of digital tools across jurisdictional boundaries. They are also subject to the same kind of fragmented regulatory landscape that has historically constrained physical cross-border logistics through divergent national rules. The Organisation for Economic Co-operation and Development has estimated that full data autarky, defined as complete restriction of cross-border data flows, would reduce global gross domestic product by 4.5 percent and cut exports by 8.5 percent (International Chamber of Commerce, 2025). Restrictive and fragmented data policies act as non-tariff barriers in the same operational sense that documentation requirements, retention obligations, and audit rules act as non-tariff barriers in physical logistics.

The structural analogy is precise rather than loose. A Norwegian patient summary moving from a Norwegian National Contact Point for eHealth to a Spanish point of care is a digital good crossing a jurisdictional boundary. It must satisfy the originating jurisdiction's audit and retention rules, the destination jurisdiction's clinical and consent rules, and any superordinate Union-level provisions. The audit log of the cross-border access event is the digital equivalent of the customs documentation that accompanies physical goods. The ten-year retention floor for that audit log under the eHDSI security framework is the digital equivalent of mandatory customs record-keeping obligations under physical trade law. The right to erasure under General Data Protection Regulation Article 17 is the digital equivalent of the destruction-of-records requirements that apply to perishable or sensitive physical goods. The conflict between these regimes is the same kind of conflict that physical logistics has long managed through ledger-based reconciliation systems, certified destruction protocols, and chain-of-custody documentation.

The maritime sector provides a concrete Norwegian-context illustration of the information-logistics framing in operation. Norwegian regulations on the medical examination of seafarers, governed by the Norwegian Maritime Authority under the implementation of the International Convention on Standards of Training, Certification and Watchkeeping for Seafarers and the Maritime Labour Convention 2006, were amended specifically to implement the General Data Protection Regulation, restricting electronic registration of medical certificates by seafarer's doctors operating outside Norway and the European Economic Area (Norwegian Maritime Authority, 2023). The amendments demonstrate that cross-border health data flow is not a theoretical question for Norwegian maritime and offshore logistics; it is an operationally binding regulatory constraint that already shapes which doctors can submit which medical certifications electronically and which cannot.

A small but technically substantial literature has begun to address cross-border data flow compliance as a logistics and supply chain problem in its own right. Zhuang et al. (2024) propose a Compliance Management System for Cross-Border Data Transfer that integrates multiple legal frameworks into a unified real-time compliance engine, demonstrating that the operational complexity of cross-border data flow under fragmented regulatory regimes is sufficient to warrant a dedicated system-engineering response. The present thesis sits within this emerging literature, contributing a specific mechanism for the audit-retention component of the broader cross-border health data flow problem.

## 2.8 Comparative Analysis

The position of the proposed contribution within the existing literature is summarised in Table 2.1, which compares this thesis against the most directly relevant comparator systems and analytical neighbours on six dimensions: the scope of cross-border versus cross-institutional operation, the dependency on hardware-rooted trust, the engagement with the GDPR right to erasure as a design constraint, the targeting of primary use versus secondary use under the European Health Data Space, the grounding in Norwegian operational context, and the presence of a formal model of the retention–erasure conflict.

**Table 2.1 — Comparative Analysis of Cryptographic Compliance Approaches to Health Data Audit**

| System | Cross-Border or Cross-Institutional | Hardware Dependency | Addresses GDPR Article 17 Erasure | Primary or Secondary Use | Norwegian Context | Formal Model of the Retention–Erasure Conflict |
|---|---|---|---|---|---|---|
| KONFIDO (Natsiavas et al., 2021; Diamantopoulos et al., 2019) | Cross-border (OpenNCP) | Yes — Intel SGX | No — treats immutability as feature | Primary use | EU pilot; not Norway-specific | No |
| ZK-EHR (Albalwy, 2026) | Cross-institutional | No — software only | Partial — revocation, not the retention conflict | Primary use (clinical) | None | No |
| Health-zkIDM (Bai et al., 2022) | Identity (institutional) | No | No | Primary use (identity) | None | No |
| zkFL-Health (Sharma et al., 2025) | Cross-institutional federated | Yes — TEE aggregator | No | Secondary use (AI training) | None | No |
| NewbornTime (Brunner et al., 2025) | Single-institution (Stavanger) | No | Yes — consent withdrawal | Primary use (clinical research) | Yes — Norwegian deployment | No |
| SPUHiN D5.2 criteria (SPUHiN, 2025) | National policy framework | n/a — specification | No — not addressed at any grade | Secondary use (SPE) | Yes — Norwegian policy, final | No |
| Ledger crypto-erasure SoK (Aikebaier, 2026) | Storage-technology scope (public ledgers) | No | Yes — formalises erasure side only | n/a | None | Partial — formalises erasure, excludes retention law by stated scope |
| Practitioner crypto-shredding pattern (VeritasChain, 2026) | Sector pattern (finance) | No | Yes — asserted, bi-lateral | n/a | None | No — asserted reconciliation, no model, no verifiability semantics |
| **This thesis (TRF Model + Crypto-Erasure by Invalidation)** | **Cross-border** | **No — software only** | **Yes — derived from the model, within the EDPB 02/2025 corridor** | **Both, at the audit-trail boundary** | **Yes — designed against the finalised Norwegian substrate** | **Yes — tri-lateral feasibility model with infeasibility and feasibility results** |

The table makes the position of the contribution explicit against both its architectural and its analytical neighbours. On the architectural axis, no comparator combines cross-border operation, software-only deployment, engagement with the erasure right, applicability across both use pathways, and Norwegian grounding. On the analytical axis, which the review update added, the two nearest neighbours are the 2026 ledger-erasure systematisation, which supplies a formal foundation for the erasure semantics this thesis consumes while excluding the retention conflict from its scope, and the practitioner crypto-shredding pattern, which asserts a bi-lateral reconciliation without a model, without verifiability semantics, and without the deletion-ceiling constraint that makes the EHDS setting tri-lateral. No entry in either axis contains a formal analysis of the joint satisfiability of a retention floor, an erasure right, and a deletion ceiling on the same records: the object the TRF Model supplies.

The thesis accordingly claims neither the cryptographic primitives, which are established (Section 2.4), nor the general formal method, which is established (Section 2.5), nor the reconciliation idea, which practitioner literature already asserts bi-laterally. It claims the formal tri-lateral characterisation, the verifiability semantics of invalidation, and the cross-border health instantiation on the Norwegian substrate: each verified above as unoccupied.

## 2.9 Identified Research Gaps

The literature reviewed in this chapter establishes four specific gaps that motivate the thesis contribution, stated with the boundaries the review imposes.

The first gap is formal-analytical, and it is the primary gap. No published work in any reviewed strand — the cross-border health security literature, the cryptographic-erasure literature including its 2026 systematisation, the blockchain-and-GDPR literature, the formal legal-compliance-verification literature, or the practitioner compliance literature: provides a formal model of the tri-lateral retention system in which an audit-retention floor, a subject-triggered erasure right, and a fixed deletion ceiling operate concurrently on the same records. The general method for such modelling exists (Feng et al., 2022); the erasure side has been formalised (Aikebaier, 2026); the bi-lateral floor-versus-right conflict has been named by regulators (European Data Protection Board, 2026a) and asserted resolved by practitioners (VeritasChain, 2026); the tri-lateral system, whose deletion ceiling changes the structure of the feasibility question, has not been formally characterised anywhere.

The strength of this gap is best demonstrated by its sharpest instance. The collision between the six-month deletion ceiling of Article 68(12) and the one-year identifiable-log retention floor of Article 73(1)(e) requires no synthesis across instruments of differing legal weight and no interpretive work by this author: it is stated by one regulation, in adjacent articles of one chapter, about one environment. The review conducted for this thesis located no treatment of it: not in the academic literature, not in the professional commentary on EHDS secondary use, and not in the guidance published by the Joint Action drafting the specifications for both provisions. Two factors explain the omission without diminishing it. Procedurally, these obligations were renumbered from Articles 46 and 50 of the 2022 proposal on adoption in 2025, so that much existing commentary analyses them under superseded numbering in separate literatures. Substantively, the standard practitioner heuristic for conflicting retention obligations, apply the longest applicable period, is inapplicable where one of the obligations is a ceiling, leaving practitioners without a default to reach for and therefore without an occasion to articulate the conflict. Neither factor makes the conflict any less binding on the environments that must satisfy both provisions from 26 March 2029, nor on the implementing acts that must specify how they are satisfied by 26 March 2027.

The gap does not rest on this author's search alone. Aikebaier's (2026) systematisation of the cryptographic-erasure literature closes by identifying five open problems for the field, of which the fifth is erasure under multi-regime retention conflict. The most recent survey of the relevant cryptographic literature therefore names the problem this thesis addresses as unresolved, which is stronger evidence for the gap than any absence of search results could be.

The second gap is application-specific. The cryptographic primitives required — cryptographic erasure as recognised in NIST Special Publication 800-88 Revision 2 and now formally grounded for Article 17 purposes, hiding commitments, and dynamic accumulators with efficient revocation (Camenisch & Lysyanskaya, 2002) — exist in mature form. None has been integrated into a mechanism designed for the cross-border European Health Data Space audit trail, spanning the primary-use NCPeH layer and the secondary-use Helsedataservice and SPE layer, with verifiability semantics that let an auditor confirm both that an event occurred and that its payload was lawfully invalidated, demonstrated against synthetic data representative of Norwegian conditions.

The third gap is contextual and has sharpened since the first version of this review. The finalised Norwegian SPE criteria (SPUHiN, 2025) govern environment security, identity, and access, and the documented operational reality beneath them remains fragmented to the level of consumer cloud services and disconnected personal computers (SPUHiN, 2024). A compliance mechanism for the retention conflict must therefore be substrate-independent, designed at the audit-trail boundary, and must demand of the processing environment nothing beyond what the finalised national criteria already require: a design constraint no reviewed proposal satisfies.

The fourth gap is legal-technical and was surfaced by the review update. The regulatory corridor for cryptographic erasure — the EDPB's conditional acceptance of cryptographic unrecoverability as erasure, the Norwegian equation of anonymisation with deletion, and the simultaneously high Norwegian threshold under which surviving keys, hashes, or linkages keep data personal: has not been mapped onto the audit-trail setting, where the mechanism's surviving residue (metadata, commitments, invalidation entries) must itself be shown to sit on the lawful side of the threshold. Treating this residue question as a first-class design constraint, rather than an afterthought, is a contribution requirement that the reviewed literature imposes on this thesis and that Chapter 4 discharges.

These four gaps converge on the research question stated in Chapter 1 and are addressed, respectively, by the formal model, the mechanism specification, the boundary-placement design decision, and the residue analysis of Chapter 4, with the demonstration of Chapter 5 witnessing the first two executably.

## 2.10 Conceptual Positioning of the Thesis

The contribution of this thesis is positioned at the intersection of the four identified gaps, and its architecture follows from that positioning. The analytical artefact is the Tri-Lateral Retention Feasibility Model: a constraint formulation, in the tradition of formal legal-compliance verification but in the modelling style of operations research, that decomposes each cross-border audit record into event metadata and a committed personal-data payload, expresses the audit-retention floors, the Article 17 erasure right, and the Article 68(12) deletion ceiling as constraints over discretised time, and examines joint satisfiability under two semantics of audit verifiability. The model is tri-lateral in structure rather than in instrument count: the floor is parameterised, so that the ten-year eHDSI cross-border audit floor and the one-year Article 73(1)(e) Secure Processing Environment log floor are two instances of a single constraint, and jurisdiction-specific floors can be substituted without reconstruction. Under the prevailing plaintext semantics the system is infeasible; under verifiability-as-accountability-preservation it is jointly satisfiable, and the mechanism that witnesses this feasibility, Crypto-Erasure by Invalidation, applies the NIST-recognised cryptographic-erase technique at the audit-trail boundary, within the regulatory corridor defined by the EDPB's unrecoverability test and the Norwegian anonymisation-equals-deletion doctrine, with hiding commitments and accumulator witnesses supplying the verifiability that the practitioner crypto-shredding pattern lacks.

The thesis does not claim novelty for any cryptographic primitive, for the general method of formalising compliance as satisfiability, or for the idea that key destruction can reconcile erasure with retention, each of which the reviewed literature already contains. It claims that the formal characterisation of the tri-lateral conflict, the expression of that conflict and its resolution in information-logistics terms, and the derivation and demonstration of the reconciling mechanism for the cross-border health audit trail on the finalised Norwegian substrate are together novel: a claim the comparative analysis of Section 2.8 supports entry by entry. The remaining chapters elaborate this claim through the methodology of Chapter 3, the model and specification of Chapter 4, and the executable demonstration of Chapter 5, with the counter-positions identified in this review — the unprovability of key destruction, the personal-data status of surviving residues, and the operational-complexity critique of crypto-shredding: engaged substantively in Chapter 6.

---

## References (Chapter 2 — consolidated)

Albalwy, F. (2026). Zero-knowledge-based policy enforcement for privacy-preserving cross-institutional health data sharing on blockchain. *Systems*, *14*(4), 385. https://doi.org/10.3390/systems14040385

Bai, T., Hu, Y., He, J., Fan, H., & An, Z. (2022). Health-zkIDM: A healthcare identity system based on Fabric blockchain and zero-knowledge proof. *Sensors*, *22*(20), 7716. https://doi.org/10.3390/s22207716

Benaloh, J., & de Mare, M. (1993). One-way accumulators: A decentralized alternative to digital signatures. In *Advances in Cryptology — EUROCRYPT '93* (LNCS 765, pp. 274–285). Springer.

Berngaard. (2024). *Ivaretar din teknologiske tjeneste kravet til innebygd personvern?* [Legal commentary]. berngaard.no

Brunner, S., Johannessen, A., García-Torres, J., Çatak, F. Ö., Meinich-Bache, Ø., Rettedal, S., & Engan, K. (2025). Consent-driven, semi-automated data collection during birth and newborn resuscitation: Insights from the NewbornTime study. *PLOS Digital Health*. https://doi.org/10.1371/journal.pdig.0000730

Broadbent, A., & Islam, R. (2020). Quantum encryption with certified deletion. In *Theory of Cryptography (TCC 2020)*. Springer. arXiv:1910.03551

Bursuc, S., Gil-Pons, R., Mauw, S., & Trujillo-Rasua, R. (2024). *Software-based memory erasure with relaxed isolation requirements* (Extended version). arXiv:2401.06626

Camenisch, J., & Lysyanskaya, A. (2002). Dynamic accumulators and application to efficient revocation of anonymous credentials. In *Advances in Cryptology — CRYPTO 2002* (LNCS 2442, pp. 61–76). Springer. https://doi.org/10.1007/3-540-45708-9_5

Datatilsynet. (2015). *Anonymisering av personopplysninger: veileder*. Norwegian Data Protection Authority.

Datatilsynet. (n.d.-a). *Etablere internkontroll* [Guidance]. Norwegian Data Protection Authority.

Datatilsynet. (n.d.-b). *Innebygd personvern og personvern som standard* [Guidance]. Norwegian Data Protection Authority.

Diamantopoulos, S., Karlsson, L., Karkaletsis, G., Tsoumas, V., Berler, A., Karkaletsis, K., et al. (2019). Secure cross-border exchange of health related data: The KONFIDO approach. In *Computer Security: ESORICS 2019 International Workshops* (pp. 318–333). Springer. https://doi.org/10.1007/978-3-030-34914-1_30

Ernst & Young. (2025). *Regulation (EU) 2025/327: Establishing the European Health Data Space (EHDS)* [Tax alert]. EY Greece.

European Commission. (2025a). *European Health Data Space Regulation*. Directorate-General for Health and Food Safety.

European Commission. (2025b). *Electronic cross-border health services*. Directorate-General for Health and Food Safety.

European Data Protection Board. (2026b). *Guidelines 02/2025 on the processing of personal data through blockchain technologies* (Version 2.0, adopted 7 July 2026 following public consultation). EDPB.

European Data Protection Board. (2026a). *Coordinated Enforcement Framework report on the implementation of the right to erasure under Article 17 GDPR* (18 February 2026). EDPB.

European Parliament and Council of the European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88.

European Parliament and Council of the European Union. (2025). Regulation (EU) 2025/327 of 11 February 2025 on the European Health Data Space. *Official Journal of the European Union*.

Feng, N., Marsso, L., Sabetzadeh, M., & Chechik, M. (2022). *Bounded satisfiability checking of metric first-order temporal logic*. arXiv:2209.04052.

Finck, M. (2018). Blockchains and data protection in the European Union. *European Data Protection Law Review, 4*(1), 17–35.

Finck, M. (2019). *Blockchain and the General Data Protection Regulation: Can distributed ledgers be squared with European data protection law?* European Parliament, Panel for the Future of Science and Technology (STOA), EPRS.

Folkehelseinstituttet. (2024). *Helsedataservice: The national health data access body*. Norwegian Institute of Public Health.

Forskningsetikk. (2023). *Helsedataservice takes over authority to process applications and grant access to health data*. Norwegian National Research Ethics Committees.

Frontiers in Digital Health. (2025). Secondary use under the European Health Data Space: Towards a research agenda on privacy-enhancing technologies. *Frontiers in Digital Health*, *7*, 1602101. https://doi.org/10.3389/fdgth.2025.1602101

Belen-Saglam, R., Altuncu, E., Lu, Y., & Li, S. (2023). A systematic literature review of the tension between the GDPR and public blockchain systems. *Blockchain: Research and Applications*, *4*(2), 100129. https://doi.org/10.1016/j.bcra.2023.100129

Healthy Europe. (2026). *EHDS: Europe's Health Data Space update*.

Helse- og omsorgsdepartementet. (2020). *Prop. 63 L (2019–2020): Endringer i helseregisterloven m.m.* Norwegian Ministry of Health and Care Services.

Helsedataservice. (2024). *Application workflow and fees*. helsedata.no.

Helsedirektoratet. (2023). *Årsrapport 2023* [Annual report — Direktoratet for e-helse merger]. Norwegian Directorate of Health.

Helsedirektoratet. (2025a). *Europeisk helsedataområde (EHDS)*. Norwegian Directorate of Health.

Helsedirektoratet. (2025b). *FAIR Secure provision and use of health data in Norway (SPUHiN)* [Project page]. Norwegian Directorate of Health.

Helsedirektoratet. (2026a). *MyHealth@EU, Helsedirektoratet* [National e-health portfolio measure]. Norwegian Directorate of Health. https://www.helsedirektoratet.no/digitalisering-og-e-helse/nasjonal-e-helseportefolje/tiltak-i-nasjonal-e-helseportefolje/myhealth-eu-helsedirektoratet

Helsedirektoratet. (2026b). *MyHealth@EU, Norsk helsenett* [National e-health portfolio measure]. Norwegian Directorate of Health. https://www.helsedirektoratet.no/digitalisering-og-e-helse/nasjonal-e-helseportefolje/tiltak-i-nasjonal-e-helseportefolje/myhealth-eu-norsk-helsenett

Aikebaier, Y. (2026). *SoK: Cryptographic erasure on public ledgers: Application-layer architectures, key-lifecycle adversaries, and GDPR Art. 17 equivalence* (Cryptology ePrint Archive, Paper 2026/1109). Nexum Ledger Ltd. https://eprint.iacr.org/2026/1109 [Preprint; not peer-reviewed]

IHE International. (2024). *Audit Trail and Node Authentication (ATNA) Integration Profile* — IT Infrastructure Technical Framework, Vol. 1, Ch. 9.

International Chamber of Commerce. (2025). *Data flows in supply chains: Practical realities and policy implications*. ICC.

Matheson. (2026). *EDPB publishes CEF report on the right to erasure* [Legal commentary]. Matheson LLP.

National Institute of Standards and Technology. (2025). *Special Publication 800-88 Revision 2: Guidelines for media sanitization* (R. Chandramouli & E. Hibbard). NIST. https://doi.org/10.6028/NIST.SP.800-88r2

Natsiavas, P., Mazzeo, G., Faiella, G., Campegiani, P., Dumortier, J., Stan, O., … Romano, L. (2021). Developing an infrastructure for secure patient summary exchange in the EU context: Lessons learned from the KONFIDO project. *Health Informatics Journal*, *27*(2). https://doi.org/10.1177/14604582211021459

Norwegian Maritime Authority. (2023). *Regulations on the medical examination of employees on Norwegian ships and mobile offshore units* (amendment). Sjøfartsdirektoratet.

Norwegian Trusted Research Environments. (2025). *NORTRE: A collaboration between TSD, SAFE, and HUNT Cloud*. nortre.no.

Oneuptime. (2026). *How to set up crypto-shredding for GDPR right-to-erasure compliance* [Implementation commentary].

Reardon, J., Basin, D., & Capkun, S. (2013). SoK: Secure data deletion. In *2013 IEEE Symposium on Security and Privacy* (pp. 301–315). IEEE. https://doi.org/10.1109/SP.2013.28

Ren, J. (2022). Cryptographic accumulator and its application: A survey. *Security and Communication Networks*, Article 5429195. https://doi.org/10.1155/2022/5429195

Sharma, S., Petrovic, G., & Kaushik, S. (2025). *zkFL-Health: Blockchain-enabled zero-knowledge federated learning for medical AI privacy*. arXiv:2512.21048.

Simjanoska Misheva, M., Shahpaski, D., Dobreva, J., Bukovec, D., Gjorgjioski, B., Nikolov, M., … Gams, M. (2025). AI Act compliance within the MyHealth@EU framework: Tutorial. *Journal of Medical Internet Research*, *27*, e81184. https://doi.org/10.2196/81184

SPUHiN. (2024). *Recommendations for minimum requirements for Secure Processing Environments in Norway* (Draft, 29 November 2024). Helsedirektoratet & Folkehelseinstituttet.

SPUHiN. (2025). *Recommendations for minimum requirements for Secure Processing Environments in Norway* (D5.2, final, following public hearing). Helsedirektoratet & Folkehelseinstituttet.

Staffa, M., Coppolino, L., Sgaglione, L., Gelenbe, E., Komnios, I., Grivas, E., Stan, O., & Castaldo, L. (2018). KONFIDO: An OpenNCP-based secure eHealth data exchange system. In *Security in Computer and Information Sciences — Euro-CYBERSEC 2018* (CCIS 821, pp. 11–27). Springer.

TEHDAS2. (2025). *Guideline for Health Data Access Bodies on procedures and formats for data access* (D6.3). TEHDAS2 Joint Action.

TEHDAS2. (2026). *Technical specification for health data access bodies on the implementation of secure processing environments* (D7.4). TEHDAS2 Joint Action. https://tehdas.eu/results/

VeritasChain Standards Organization. (2026). *Crypto-shredding: The technical foundation for reconciling GDPR and financial record-keeping obligations* [Industry analysis].

Scope, N., & Rasin, A. (2025). *Systems and methods for data retention and purging* (U.S. Patent No. 12,425,209). U.S. Patent and Trademark Office.

Scope, N., Rasin, A., Lenard, B., Heart, K., & Wagner, J. (2022). Harmonizing privacy regarding data retention and purging. In *Proceedings of the 34th International Conference on Scientific and Statistical Database Management (SSDBM 2022)* (pp. 1–12). ACM. https://doi.org/10.1145/3538712.3538718

Scope, N., Rasin, A., Lenard, B., Wagner, J., & Heart, K. (2022). Purging compliance from database backups by encryption. *Journal of Data Intelligence*, *3*(1).

Zhuang, Z., Lee, X., Wei, J., Fu, Y., & Zhang, A. (2024). *CBCMS: A compliance management system for cross-border data transfer*. arXiv:2412.08993.


\pagebreak

---

# Chapter 3. Methodology and Research Design

---

## 3.1 Research Paradigm

This thesis adopts Design Science Research (DSR) as its governing paradigm. DSR is the appropriate choice where the research objective is not to describe or explain an existing phenomenon but to create and evaluate an artefact that addresses a defined problem in an information-systems context. Hevner, March, Park, and Ram (2004) establish the canonical framing: design science produces and applies artefacts — constructs, models, methods, and instantiations: whose utility is assessed against the problem environment from which the problem was drawn and whose rigour is assessed against the knowledge base from which the design draws. Peffers, Tuunanen, Rothenberger, and Chatterjee (2007) operationalise this into a six-activity process model that supplies the procedural structure adopted here.

The problem addressed in this thesis satisfies the conditions under which DSR is the correct paradigm rather than a convenient label. The problem is real, arising from binding regulatory instruments operating concurrently on live cross-border infrastructure rather than from a theoretical puzzle. It is unsolved, in the precise sense established in Chapter 2: no reviewed work formally characterises the tri-lateral retention conflict or derives a mechanism from such a characterisation. It admits an artefact as its answer, since what is missing is a design: a way of organising audit records and their cryptographic bindings such that three concurrent obligations can be jointly satisfied. And its evaluation is tractable within the resources of a Master's thesis, because the artefact's central claim is a claim about logical consistency under stated constraints, which can be argued formally and checked executably, rather than a claim about performance in deployment, which could not.

Three alternative paradigms were considered and rejected. A qualitative interview study of Norwegian implementing actors would have produced descriptive knowledge about how practitioners currently perceive the retention conflict, but would not have produced a mechanism, and would have required ethical clearance and participant access disproportionate to the contribution. A systematic literature review would have consolidated the state of knowledge, a function partly discharged within Chapter 2, but the review itself established that the gap is the absence of a design, not the absence of a synthesis. A purely formal-methods study in the tradition of Feng, Marsso, Sabetzadeh, and Chechik (2022) would have produced the model without the artefact, and would have required proof-assistant machinery and expertise outside the scope of this programme. DSR, in the variant developed in Section 3.3, permits the model and the artefact to be produced together, with the model supplying the rigour and the artefact supplying the relevance.

## 3.2 The Design Science Cycle Adopted

The Peffers et al. (2007) six-activity model structures the thesis and maps onto its chapters as follows.

**Activity 1 — Problem identification and motivation.** The tri-lateral retention conflict is identified from primary regulatory and technical sources and shown to be unresolved in both the literature and Norwegian national policy. Chapters 1 and 2.

**Activity 2 — Definition of objectives for a solution.** The research question and three sub-questions state what a solution must achieve: joint satisfaction of the three regimes, preservation of audit accountability, verifiability by an external auditor, and compatibility with the Norwegian infrastructure as it actually operates. Chapter 1, Section 1.3.

**Activity 3 — Design and development.** The Tri-Lateral Retention Feasibility (TRF) Model is constructed, the two competing semantics of audit verifiability are defined, the infeasibility and feasibility results are established, and the Crypto-Erasure by Invalidation mechanism is specified as the constructive witness of feasibility. Chapter 4.

**Activity 4 — Demonstration.** The model and mechanism are instantiated in a software sandbox operating over synthetic patient records, which exhibits the infeasibility result under status-quo semantics and the feasibility result under invalidation semantics. Chapter 5.

**Activity 5, Evaluation.** The artefact is evaluated against the objectives of Activity 2 on three axes, internal consistency, external compatibility with verified infrastructure, and engagement with the principal counter-positions surfaced in Chapter 2. Chapters 5 and 6.

**Activity 6 — Communication.** The thesis itself, together with the supplementary addendum to the supervisor covering research directions deliberately excluded from the thesis scope. Chapters 6 and 7.

Peffers et al. (2007) distinguish several entry points into this cycle. This thesis is a problem-centred initiation: the work began from an observed conflict between instruments, not from an available technology in search of application. The distinction matters for the integrity of the contribution, because it is the reason the mechanism is derived from the model rather than assumed in advance and justified afterwards. An earlier iteration of this project did proceed from technology to problem, envisaging zero-knowledge succinct arguments as the enforcement machinery before the requirements were formally stated; the analysis reported in Chapter 4 showed that machinery to be unnecessary for the audit-trail problem. That correction is itself an instance of the design cycle operating as intended, and is recorded rather than concealed.

## 3.3 The Specification-and-Demonstration Variant, Extended with Formal Modelling

DSR admits artefacts at several levels of abstraction. Hevner et al. (2004) distinguish constructs, models, methods, and instantiations; March and Smith's earlier typology, on which that classification draws, makes the same separation. This thesis produces an artefact at two of these levels: a **model** (the TRF Model, a formal representation of the problem domain and its constraints) and a partial **instantiation** (the sandbox, which realises the model and its mechanism in executable form over synthetic data). It does not produce a deployed system, and it does not claim to.

The variant adopted is therefore specification-and-demonstration: the contribution is the specified artefact together with a demonstration that it behaves as specified, rather than a production implementation together with field evaluation. This variant is well-established in DSR practice for problems where deployment is infeasible within the research setting but where the design claim is nonetheless checkable.

The extension particular to this thesis is the insertion of a formal-modelling step between Activity 2 and Activity 3. Rather than proceeding directly from objectives to design, the thesis first formalises the problem as a constraint-satisfaction question and establishes what any solution must do in order to succeed. The mechanism is then derived as the constructive answer to that question. The methodological warrant for this step comes from the formal legal-compliance verification tradition reviewed in Chapter 2, Section 2.5, in which regulatory obligations are expressed as formal properties and compliance is decided as a satisfiability problem (Feng et al., 2022).

Three consequences follow from taking this step, and they shape the remainder of the methodology.

First, the design becomes falsifiable in a way that an asserted architecture is not. If the constraint system is satisfiable under the proposed semantics, the mechanism follows; if it is not, the mechanism fails, and the failure is visible in the model rather than only in deployment.

Second, the evaluation criteria are fixed in advance by the model rather than chosen afterwards to suit the artefact. The mechanism succeeds exactly when it renders the three constraints jointly satisfiable while preserving the accountability content of the audit record; no other success criterion is admitted.

Third, the machinery must be proportionate. This thesis deliberately employs a lighter formalism than the Metric First-Order Temporal Logic and Satisfiability Modulo Theories apparatus of Feng et al. (2022): a feasibility formulation over discretised time with one binary accessibility variable per audit record, in the constraint-modelling style of operations research. The justification is threefold. The conflict turns on a single semantic question, what "verifiable" means for an audit record, and a formulation that isolates that question communicates it more clearly than a general temporal-logic encoding. The lighter formulation is defensible at Master's level by an author trained in logistics modelling rather than formal methods, which matters for the integrity of a thesis that must be owned and defended by its author. And the formulation is executable in ordinary Python, which makes the theorems checkable by a reader with no proof-assistant background. The cost of this choice is expressive power: the model cannot represent obligations whose structure exceeds the chosen formalism, a limitation recorded in Section 3.7 and revisited in Chapter 6.

## 3.4 Formal-Modelling Methodology

This section states how the TRF Model is constructed. The model itself, with its full notation, theorems, and proofs, is developed in Chapter 4; what follows is the method by which it is built and the standard to which it is held.

**Step 1 — Decomposition of the object.** Each cross-border audit record is decomposed into components that the regulatory instruments treat differently. The event metadata comprises the accountability content: which actor accessed which category of record, at what time, from which national contact point, under which legal basis and consent policy, with what outcome. The personal-data payload comprises the content of the exchanged clinical document. A cryptographic commitment binds the second to the first, so that the record can attest to what was accessed without retaining it in accessible form, and a key governs access to the payload. This decomposition is the modelling move on which everything else rests, and it is derived from the legal analysis of Chapter 2, Section 2.3 rather than assumed: it is the necessity boundary of Article 17(3)(b), read with the minimisation principle of Article 5(1)(c), that separates what must be retained from what may not be.

**Step 2 — Translation of each regime into a constraint.** Each regime is expressed as a constraint over discretised monthly time on the state of a record. The retention floor requires that the record remain verifiable throughout its retention window. The Article 17 erasure right requires that, following a valid erasure request, the personal-data payload cease to be accessible within the response period. The Article 68(12) deletion ceiling requires that, following permit expiry, payload accessibility cease within six months for records arising in the secondary-use pathway. The model is tri-lateral in the number of constraint types, not in the number of legal instruments it accommodates: the floor is a single parameterised constraint with two instances in the present setting, the ten-year minimum imposed on cross-border audit repositories by the eHDSI deployment baseline and the one-year minimum imposed on Secure Processing Environment access logs by Article 73(1)(e) EHDS. Because the horizon is parameterised rather than hard-coded, the second instance required no structural change to the model, and jurisdiction-specific floors can be substituted on the same basis. The translation is documented claim by claim against the primary instruments, so that a reader can check each constraint against its source.

**Step 3 — Definition of the competing semantics.** The pivotal move is to make explicit an assumption that the operational status quo leaves implicit. Under *plaintext-verifiability semantics*, a record satisfies the retention constraint only while its payload remains accessible in recoverable form. Under *accountability-preservation semantics*, a record satisfies the retention constraint while its metadata is intact, its commitment survives, and any invalidation event is itself recorded and witnessed. Both are candidate readings of what an audit repository is for; the thesis argues that the second is the reading the instruments actually require and the first is an unexamined inheritance from systems designed before the erasure right existed.

**Step 4 — Establishing the two results.** Theorem 1 states that under plaintext-verifiability semantics the constraint system is infeasible whenever an erasure request or a permit expiry falls within a record's retention window: which, over a ten-year window, is the ordinary case rather than the exception. The second floor instance makes the result sharper rather than weaker: where a one-year log-retention floor operates against a six-month deletion ceiling on the same environment, infeasibility under plaintext semantics arises from the two retention provisions alone, with no erasure request required to trigger it. Theorem 2 states that under accountability-preservation semantics the system is jointly satisfiable for every arrival pattern of erasure requests and permit expiries, and exhibits the mechanism that achieves this as the constructive witness. Both are argued informally at the level of rigour standard for design-science work rather than machine-checked; Section 3.7 records what that means for the strength of the claim.

**Step 5 — Executable checking.** Because the formulation is deliberately light, both results can be checked by direct execution rather than only by argument. The checker described in Section 3.6 walks synthetic records through randomised arrivals of erasure requests and permit expiries and evaluates the constraints under each semantics in turn, producing violations under the first and none under the second. This does not constitute formal verification in the proof-assistant sense, and is not presented as such; it is a demonstration that the theorems hold on the instances examined, and its value is that it makes the argument inspectable by a reader who does not wish to take the proofs on trust.

## 3.5 Synthetic Data

The demonstration requires patient records with realistic structure. No real patient data are used at any point in this thesis, and none were requested or obtained.

Synthetic records are generated using Synthea, an open-source synthetic patient generator that simulates the lifetime medical histories of statistically realistic but entirely fictional individuals, producing records in standard health-data formats (Walonoski et al., 2018).¹ Synthea is appropriate here for three reasons. Its output conforms to HL7 FHIR, the interoperability standard underlying the European Electronic Health Record Exchange Format; its generation is seeded, so that a given seed reproduces a given population exactly; and it is established in the health-informatics literature as a substitute for real data in system-development contexts, which means its use requires no novel methodological defence.

Three configuration decisions are fixed, and one limitation of the generator must be recorded alongside them. The output conforms to **FHIR R4**, not R5, because the Norwegian national profile set (basisprofiler) maintained by HL7 Norway constrains R4; matching the Norwegian profile version is what makes the demonstration representative of the Norwegian setting rather than of a generic one. The population is approximately **one hundred synthetic patients**, a size chosen to be large enough to exercise the audit-record lifecycle across varied clinical encounter patterns and small enough to remain inspectable by hand when a result needs to be traced to its cause; because the thesis reports no statistical inference, no power calculation governs this choice. And **random seeds are fixed and reported** — population seed and clinician seed both set to 20260915: so that the entire demonstration is reproducible from the thesis text.

The limitation concerns profiles rather than versions. Synthea's default export conforms to the US Core implementation guide and draws its demographic, geographic, and care-pattern parameters from a United States population. The FHIR version therefore matches the version Norwegian basisprofiler constrain, but the profiles and the clinical content do not represent Norwegian practice, and this thesis makes no claim that they do. The consequence is bounded and is verified rather than assumed in Chapter 5, Section 5.7: because no constraint in the model reads the content of a payload, the demonstration's results are invariant to payload provenance, and Norwegian representativeness is required of the *infrastructure analysis* in Chapter 4 rather than of the generated records.

Synthea's fidelity has been independently validated, and the validation bounds what may be claimed for it. Chen, Chun, Patel, Chiang, and James (2019) computed four clinical quality measures over a 1.2-million-patient Synthea cohort and compared them against publicly reported state and national rates, finding Synthea reliable in modelling demographics and the probability of services being offered, but limited in modelling heterogeneous health outcomes following intervention and in reproducing regional variation in care quality. These limitations are real and are recorded here rather than omitted. They do not, however, bear on the use made of Synthea in this thesis: the demonstration requires structurally valid FHIR resources and plausible encounter events from which audit records are generated, not accurate post-intervention outcome distributions. Had this thesis made epidemiological or clinical-effectiveness claims, the validation findings would be disqualifying; because it makes claims only about the behaviour of audit records under constraint, they are not.

The records themselves are not the object of study. They are the realism layer: the demonstration's claims concern the behaviour of audit records and their cryptographic bindings under the three constraints, and the synthetic clinical data supply plausible content for the exchanges that generate those audit records. This distinction is important for interpreting the results reported in Chapter 5, and is restated there.

## 3.6 Sandbox Implementation Approach

The sandbox is implemented in Python and has two layers, separated deliberately so that the load-bearing claim rests on the smaller and more inspectable component.

The **feasibility checker** is the primary layer and the executable witness of the theorems. It constructs audit records as the tuples defined in Section 3.4 in two classes — cross-border audit records carrying the ten-year floor, and Secure Processing Environment access-log records carrying the one-year floor and the six-month ceiling: generates randomised arrivals of erasure requests and permit expiries across a monthly time horizon, and evaluates the three constraints under each semantics in turn, reporting violations. The two classes differ only in their floor parameter and in whether the ceiling applies, which is what makes them instances of one model rather than two models. The checker is deliberately small, on the order of fifty to one hundred lines, because its purpose is to be read and checked rather than to be impressive. A reader who doubts Theorem 1 can find in its output the specific record, month, and constraint at which plaintext semantics fails; a reader who doubts Theorem 2 can confirm that no violation arises under invalidation semantics across the generated instances.

The **realism layer** wraps the checker so that its inputs derive from Synthea-generated FHIR bundles rather than from abstract record identifiers, computing commitments over the actual payloads and constructing metadata from the actual encounter events. It is larger, on the order of two to four hundred lines, but it is not load-bearing: if the wrapper were removed, the theorems and their executable check would stand unchanged. Its function is to demonstrate that the model's abstractions correspond to the structure of real health-data artefacts rather than only to a convenient idealisation, and to test, by execution rather than assertion, whether any reported result depends on payload provenance.

Both layers, together with a demonstration viewer that executes them unmodified, are published in a public repository listed in Appendix A, so that the sandbox described here can be inspected and run rather than only read about.

Cryptographic operations use standard library primitives: salted commitments constructed with a standard hash function, and simulated key destruction implemented as irreversible removal of key material from the sandbox's state. The commitments are hiding by construction, which is a design requirement rather than an implementation detail, since Chapter 2 established that an unsalted hash of personal data may itself remain personal data. **No zero-knowledge proof system is implemented at any point**, and none is required: the mechanism's verifiability rests on commitments and on the recorded invalidation event, not on succinct arguments.

A satisfiability solver may optionally be used to cross-check the constraint system on small instances, as an independent confirmation that the hand-written checker implements the constraints as stated. This is a robustness measure rather than a component of the contribution, and the thesis does not depend on it.

What the sandbox does not do bounds what Chapter 5 may claim. It does not connect to any National Contact Point, real or test. It does not implement the OpenNCP transmission flow. It does not implement authentication or consent evaluation. It does not measure execution time, memory, throughput, or energy, and no such measurements are reported anywhere in this thesis.

## 3.7 Validity, Reliability, and Limitations

The evaluation strategy is analytical rather than empirical, and its criteria are stated here in advance of the results.

**Internal validity** concerns whether the artefact is internally coherent: whether the constraints faithfully represent the instruments they translate, whether the two semantics are stated precisely enough to be distinguished, whether the theorems follow from the definitions, and whether the mechanism specified in Chapter 4 is in fact the witness the feasibility result requires. This is assessed by argument and by the executable check of Section 3.6, and it is the axis on which the contribution principally stands or falls.

**External validity** concerns whether the artefact would fit the environment from which the problem was drawn. It is assessed by compatibility analysis against verified infrastructure: the audit-logging boundary of the MyHealth@EU transmission flow, the Norwegian NCPeH as it is now operating in live pilot, the Helsedataservice access pathway, the finalised Norwegian Secure Processing Environment criteria, and the Secure Processing Environment specification published by TEHDAS2 during 2026 as deliverable D7.4. The last of these is a moving baseline: the binding requirements are to be laid down by Commission implementing acts due on 26 March 2027, after this thesis is submitted, so compatibility is assessed against the best-specified state of the infrastructure available at the time of writing rather than against its final form. Compatibility analysis is weaker evidence than deployment, and is not presented as equivalent to it.

**Reliability** is addressed through determinism. Fixed seeds, reported parameters, and a fully specified checker mean that another researcher can reproduce every reported result exactly. Because no timing or performance claims are made, no repeated-run averaging is required.

Four limitations are recorded at the outset rather than deferred to the conclusion, because each bounds what the later chapters may assert.

The first is the **proof standard**. The theorems are argued informally and checked executably on generated instances; they are not machine-checked, and the executable check confirms the results on the instances examined rather than establishing them for all instances. The claim made in this thesis is correspondingly bounded.

The second is the **expressiveness of the formalism**. The deliberate lightness described in Section 3.3 means the model cannot represent obligations whose structure exceeds a monthly-discretised binary-accessibility formulation: conditional obligations with complex temporal nesting, for instance, or interactions with instruments not included in the three modelled.

The third is the **key-destruction assumption**. The mechanism's guarantees are conditional on honest and irreversible destruction of key material. As Chapter 2 established through the secure-deletion literature, no approach operating above the storage medium can prove to an external observer that destruction occurred; the guarantee is conditional on a documented key-management boundary, which is the same condition the regulatory guidance on cryptographic unrecoverability imposes. This limitation is structural rather than incidental, and Chapter 6 engages the practitioner critique that builds on it.

The fourth is **scope**. The thesis models Union-level instruments and the Norwegian implementation; it does not model the national retention laws of other receiving jurisdictions, though the parameterisation of the retention horizon is designed to accommodate them. It addresses neither non-EEA jurisdictions nor the authentication and consent-propagation problems adjacent to the one examined.

## 3.8 Evaluation Design for the Next Cycle

The evaluation reported in this thesis is analytical, as Section 3.7 sets out. Design Science Research also admits expert assessment as an evaluation method, and a specification-and-demonstration study of this kind commonly designs the evaluation that a subsequent cycle executes (Hevner, March, Park, & Ram, 2004; Peffers, Tuunanen, Rothenberger, & Chatterjee, 2007). That design has been produced and is specified in full in Appendix C.

The instrument comprises an eight-person expert panel drawn from four perspectives: data protection, health IT architecture, Secure Processing Environment operation, and information logistics, two participants each; a forty-five minute session structure in which participants describe current practice before being shown the proposed mechanism; a demonstration script that runs the artefact live and states its limitations before participants are asked to find them; a thirteen-question semi-structured interview guide; a closed-response questionnaire of sixteen five-point Likert items across four dimensions, being perceived utility, regulatory alignment, operational viability, and audit integrity; and a thematic analysis plan with an explicit route by which findings would revise the trust model, the residue analysis, and the direction of the next design iteration.

Two features of the design are worth stating here rather than leaving to the appendix. Interview question seven asks practitioners directly whether Article 68(12) reaches the access logs an environment generates — the interpretive question on which Corollary 1.2 depends, identified in Chapter 4, Section 4.6: because practitioner readings of that provision are evidence this author cannot generate analytically. And the questionnaire retains verbatim an anchor statement asserting that the mechanism gives auditors full confidence that data was lawfully deleted, which is stronger than the thesis's own claim; a paired item captures the distinction between attestation and proof, and disagreement with the anchor would be an accurate response rather than an instrument failure.

The instrument has not been executed. Executing it would process personal data about identifiable professionals, requiring notification to Sikt and a lead time of four to six weeks, and would require revision of the scope statement in Chapter 1, Section 1.5, of Section 3.9 below, and of the Declaration of Originality, each of which states that this research involves no human participants. Those statements are accurate for the thesis as submitted. Chapter 7, Section 7.5 carries execution of this instrument as the immediate next step in the research programme.

## 3.9 Ethical Considerations

The ethical profile of this thesis is unusually simple, and the simplicity is a consequence of deliberate design choices rather than an absence of reflection.

No personal data are processed at any stage. All records are synthetically generated and describe no real individual. No human participants are involved: no interviews, surveys, observations, or usability studies were conducted, and no data about identifiable persons were collected. Consequently no approval from the Norwegian Agency for Shared Services in Education and Research, from a regional research-ethics committee, or from any institutional review board was required, and none is claimed. This is stated explicitly because an earlier draft of this project asserted an institutional review board approval that did not exist; the correction is recorded here as a matter of research integrity.

The choice of synthetic data is itself ethically grounded rather than merely convenient, and the grounding rests on a Norwegian supervisory decision rather than on commentary. In its decision of 11 May 2021 imposing an administrative fine of NOK 1,250,000 on the Norwegian Confederation of Sports (Norges idrettsforbund), the Norwegian Data Protection Authority held that the organisation had no lawful basis for testing a cloud migration using the personal data of 3.2 million individuals, reasoning that processing must be necessary for its purpose and that the purpose could not be pursued where it was achievable by less privacy-invasive means; the authority further found the scale of personal data used in testing to be unnecessary (Datatilsynet, 2021). The general position that testing should proceed on anonymised or, preferably, synthetic data, attributed to both the Norwegian authority and the European Data Protection Supervisor, is set out in the Norwegian professional literature summarising this line of practice (Deloitte Advokatfirma, n.d.). A thesis that proposes a mechanism for protecting personal data in audit trails would sit poorly with itself if it used real patient data to demonstrate that mechanism. The methodological choice and the ethical position coincide.

Two further commitments govern the reporting of results. Every claim of fact is traceable to a retrievable primary source, and where verification remains incomplete the incompleteness is flagged rather than smoothed over. No quantitative result is reported that was not produced by the procedures described in this chapter, and no capability is claimed that was not built: the components excluded from scope in Chapter 1, Section 1.5 are described as future work and never as achievements. These commitments respond directly to the failures identified in the earlier draft of this project, and their explicit statement here is intended to make them checkable by the examiner rather than merely asserted.

---

¹ Synthea is documented in Walonoski et al. (2018), *Journal of the American Medical Informatics Association*, 25(3), 230–238, https://doi.org/10.1093/jamia/ocx079.

---

## References (Chapter 3)

Chen, J., Chun, D., Patel, M., Chiang, E., & James, J. (2019). The validity of synthetic clinical data: A validation study of a leading synthetic data generator (Synthea) using clinical quality measures. *BMC Medical Informatics and Decision Making*, *19*, 44. https://doi.org/10.1186/s12911-019-0793-0

Datatilsynet. (2021, 11 May). *Vedtak om overtredelsesgebyr til Norges idrettsforbund for mangelfull testing* [Administrative decision]. Norwegian Data Protection Authority. https://www.datatilsynet.no/regelverk-og-verktoy/lover-og-regler/avgjorelser-fra-datatilsynet/2021/vedtak-om-overtredelsesgebyr-til-norges-idrettsforbund-for-mangelfull-testing/

Deloitte Advokatfirma. (n.d.). *Syntetiske testdata eller personopplysninger ved testing?* [Legal commentary]. deloitte.com/no

Feng, N., Marsso, L., Sabetzadeh, M., & Chechik, M. (2022). *Bounded satisfiability checking of metric first-order temporal logic*. arXiv:2209.04052.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly*, *28*(1), 75–105.

HL7 Norway. (2025). *hl7.fhir.no.basis* (Version 2.2.2) [FHIR R4 national base profile package]. Simplifier.net. https://simplifier.net/organization/hl7norway

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems*, *24*(3), 45–77.

Walonoski, J., Kramer, M., Nichols, J., Quina, A., Moesel, C., Hall, D., Duffett, C., Dube, K., Gallagher, T., & McLachlan, S. (2018). Synthea: An approach, method, and software mechanism for generating synthetic patients and the synthetic electronic health care record. *Journal of the American Medical Informatics Association*, *25*(3), 230–238. https://doi.org/10.1093/jamia/ocx079


\pagebreak

---

# Chapter 4. The Tri-Lateral Retention Feasibility Model and the Crypto-Erasure by Invalidation Mechanism

*Theorem statements and proofs in this chapter are the author's own. Regulatory claims are anchored to the primary instruments cited at each point.*

---

## 4.1 Purpose and Structure of the Chapter

This chapter contains the analytical core of the thesis. It does three things in sequence, and the sequence matters because each step licenses the next.

First, it establishes what the law actually requires to be retained, as distinct from what current practice retains. This is the necessity analysis begun in Chapter 2, Section 2.3, and it produces the decomposition on which the model rests.

Second, it constructs the Tri-Lateral Retention Feasibility (TRF) Model: a formal representation of the retention regimes as constraints over discretised time, together with two candidate semantics for what it means for an audit record to be verifiable. Within that model it states and proves two results. Theorem 1 establishes that under the semantics implicit in current practice the constraint system is infeasible. Theorem 2 establishes that under an alternative semantics the system is jointly satisfiable, and its proof is constructive: it exhibits the mechanism that achieves satisfaction.

Third, it specifies that mechanism, Crypto-Erasure by Invalidation, in enough detail to be implemented, analyses the residue it leaves behind against the legal threshold that residue must clear, compares it against the rival designs a reviewer would propose instead, and maps it onto the Norwegian infrastructure verified in Chapter 2.

The order of exposition follows the order in which the thesis has developed the problem: the cross-border primary-use case is treated first throughout, with the Secure Processing Environment case following as the second and sharper instance.

A note on what the theorems are and are not. They are mathematical statements about a model, proved informally at the standard of rigour normal for design-science work, and checked executably in Chapter 5. They are not machine-checked, and they are not claims about the world independent of the model's fidelity. Their force depends entirely on whether the constraints faithfully translate the instruments, which is why Section 4.2 documents that translation claim by claim rather than asserting it.

## 4.2 What Must Be Retained: The Necessity Analysis

The decomposition that makes the model possible is not a modelling convenience. It is derived from the legal position established in Chapter 2, Section 2.3, and it must be stated precisely because everything downstream inherits it.

Article 17(3)(b) GDPR exempts from erasure processing that is necessary for compliance with a legal obligation. The audit-retention obligations are such obligations. But the exemption is bounded by necessity, and Article 5(1)(c) requires that personal data be adequate, relevant, and limited to what is necessary for the purposes of processing. The question is therefore not whether an audit record may be retained, but which parts of it necessity protects.

The purpose that the retention obligations serve is accountability: establishing, after the fact, that a particular access occurred, by whom, when, under what authority, and with what result. That purpose is served by the event metadata. It is not served by continued controller access to the clinical content of the document that was exchanged. A supervisory authority investigating whether a Spanish clinician's access to a Norwegian patient summary in March 2027 was lawful needs to know that the access occurred, which clinician performed it, under which eIDAS assertion, against which consent policy, and whether it succeeded. It does not need to read the patient's medication list to answer that question.

This yields the central claim of the necessity analysis: **the accountability function of a cross-border audit record is discharged by its metadata and by a binding commitment to its payload, and does not require the payload to remain accessible.** Retention of accessible plaintext payload for ten years therefore exceeds what Article 17(3)(b) protects, and Article 5(1)(c) positively requires that it not be retained where the purpose can be achieved without it.

Two supports and one limit should be recorded. The Norwegian Data Protection Authority's internal-control guidance places exactly this weighing on the controller, requiring determination of lawful retention periods and deletion deadlines through explicit balancing of purpose, business need, and both retention rights and retention duties (Datatilsynet, n.d.-a). The Authority's privacy-by-design guidance equates anonymisation with deletion (Datatilsynet, n.d.-b), which is what permits a transformed record to satisfy an erasure obligation at all. The limit is that the same Authority sets a high threshold for when data cease to be personal: encryption protects data rather than rendering them unidentifiable, and data remain personal while any key or linkage capable of re-identification is retained (Datatilsynet, 2015). The residue left by the mechanism must therefore be analysed against that threshold rather than assumed to clear it, which is the work of Section 4.9.

## 4.3 The Model: Objects and Notation

Let the time domain be discretised into months, indexed by *t* ∈ ℕ, with *t* = 0 the month in which the system begins operation. Monthly granularity is chosen because every obligation in the system is expressed in months or years, and because the shortest deadline in the system, the erasure response period, is one month.

Let *A* be the set of audit records. Each record *a* ∈ *A* is generated by a single access event and is represented as a tuple

> *a* = ( *m*(*a*), *p*(*a*), *c*(*a*), *k*(*a*), *t*(*a*), *F*(*a*), *σ*(*a*) )

where:

- *m*(*a*) is the **event metadata**: the actor identifier, the actor's national contact point, the patient pseudonym, the document category accessed, the legal basis and consent policy applied, the timestamp, and the outcome. Metadata contains no clinical content.
- *p*(*a*) is the **personal-data payload**: the content of the clinical document exchanged.
- *c*(*a*) is a **commitment** to the payload, *c*(*a*) = Commit(*p*(*a*), *r*(*a*)), where *r*(*a*) is a per-record random salt. The commitment scheme is required to be *hiding* (the commitment reveals nothing about the payload to an adversary without the salt) and *binding* (no second payload can be opened against the same commitment). The requirement that it be hiding rather than a bare hash is a consequence of Section 4.9 and is not optional.
- *k*(*a*) is the **payload key**: the key material under which *p*(*a*) is stored.
- *t*(*a*) is the month in which the access event occurred.
- *F*(*a*) ∈ ℕ is the **retention floor** applying to the record, expressed in months.
- *σ*(*a*) ∈ {primary, secondary} is the **pathway** in which the record arose.

The floor is a parameter of the record rather than a constant of the model. In the present setting it takes two values:

- *F*(*a*) = 120 for cross-border audit records held in ATNA-compliant audit repositories, this being the ten-year minimum imposed by the eHDSI deployment baseline for MyHealth@EU operations (Simjanoska Misheva et al., 2025). The IHE ATNA profile itself prescribes no retention period; the floor arises from the deployment binding, and the model is correct only if this distinction is preserved.
- *F*(*a*) = 12 for access and activity logs of Secure Processing Environments, this being the one-year minimum imposed by Article 73(1)(e) of Regulation (EU) 2025/327 (European Parliament and Council of the European Union, 2025).

Two event processes act on records. An **erasure request** arrives for record *a* at month *t*ᵣ(*a*) if the data subject exercises Article 17 in respect of the personal data underlying that record; if no request arrives, *t*ᵣ(*a*) = ∞. A **permit expiry** occurs at month *t*π(*a*) for records with *σ*(*a*) = secondary, being the month in which the data permit under which the processing occurred expires; for primary-pathway records *t*π(*a*) = ∞.

Finally, let *α*(*a*, *t*) ∈ {0, 1} be the **payload-accessibility variable**: *α*(*a*, *t*) = 1 if the controller can recover *p*(*a*) in intelligible form at month *t*, and 0 otherwise. This single binary variable per record per month is the entire state space of the model, and its minimality is deliberate: the conflict turns on exactly one question, which is whether the payload is readable, and a formulation that admits no other state variable cannot obscure that question behind modelling detail.

Let *V*(*a*, *t*) ∈ {0, 1} denote whether record *a* **counts as verifiable** at month *t*. *V* is not defined yet; defining it is the subject of Section 4.5, and the two competing definitions are what the theorems distinguish.

## 4.4 The Three Constraints

Each regime is now expressed as a constraint on the trajectory of *α* and *V*.

**C1 — Retention floor.** For every record *a* and every month *t* with *t*(*a*) ≤ *t* ≤ *t*(*a*) + *F*(*a*):

> *V*(*a*, *t*) = 1.

The record must count as verifiable throughout its retention window. Source: eHDSI deployment baseline for *F* = 120; Article 73(1)(e) EHDS for *F* = 12.

**C2 — Erasure right.** For every record *a* for which a valid erasure request arrives at *t*ᵣ(*a*) < ∞, and for every month *t* ≥ *t*ᵣ(*a*) + δ:

> *α*(*a*, *t*) = 0.

The payload must cease to be accessible within the response period δ. Source: Article 17(1) GDPR, with δ determined by Article 12(3) GDPR, which requires the controller to act without undue delay and in any event within one month of receipt, extendable by two further months for complex or numerous requests provided the data subject is informed within the first month. The model takes δ = 1 as the baseline and admits δ = 3 as the extended case; results are stated for arbitrary finite δ and do not depend on which is chosen.

**C3 — Deletion ceiling.** For every record *a* with *σ*(*a*) = secondary and every month *t* ≥ *t*π(*a*) + 6:

> *α*(*a*, *t*) = 0.

Personal data must not remain accessible in the Secure Processing Environment more than six months after permit expiry. Source: Article 68(12) EHDS as operationalised by TEHDAS2 (2025).

The structural asymmetry between C1 on one hand and C2–C3 on the other is the whole problem. C1 is a lower bound on the persistence of a property; C2 and C3 are upper bounds on the persistence of accessibility. Whether they conflict depends entirely on whether *V* is defined in terms of *α* — which is the question Section 4.5 makes explicit.

## 4.5 Two Semantics of Verifiability

**Semantics I — plaintext verifiability.** A record counts as verifiable exactly when its payload is accessible:

> *V*ᴵ(*a*, *t*) = *α*(*a*, *t*).

This is the semantics implicit in the design of audit systems that predate the erasure right. Under it, an audit record whose payload cannot be produced is treated as an incomplete or broken record, and audit integrity is understood as the continued producibility of what was accessed. No instrument in the system states this semantics; it is inherited from practice, which is precisely why it has not been examined.

**Semantics II — accountability-preserving verifiability.** A record counts as verifiable when its accountability content is intact and any loss of payload accessibility is itself accounted for:

> *V*ᴵᴵ(*a*, *t*) = 1 if and only if all of the following hold at month *t*:
> (i) *m*(*a*) is intact and unmodified;
> (ii) *c*(*a*) is present and binding;
> (iii) if *α*(*a*, *t*′) = 1 for some *t*′ < *t* and *α*(*a*, *t*) = 0, then an invalidation entry *ι*(*a*) recording the transition — its month, its legal ground, and its authorising actor: is present in the audit trail and is itself covered by (i).

Under Semantics II an audit record that has lost its payload is not a broken record. It is a complete record of an access event *and* of the lawful invalidation of that event's payload. The audit trail grows rather than shrinks when erasure occurs.

Neither semantics is stipulated by the instruments. Section 4.10 argues that Semantics II is the better reading of what the instruments require; the theorems below establish what follows from each.

## 4.6 Theorem 1 — Infeasibility under Plaintext Verifiability

> **Theorem 1.** Under Semantics I, the constraint system {C1, C2, C3} is infeasible for any record *a* such that either *t*ᵣ(*a*) + δ ≤ *t*(*a*) + *F*(*a*) or *t*π(*a*) + 6 ≤ *t*(*a*) + *F*(*a*).

**Proof.** Take a record *a* satisfying the first disjunct, and let *t*\* = *t*ᵣ(*a*) + δ. By hypothesis *t*\* ≤ *t*(*a*) + *F*(*a*), and since erasure requests arrive after the access that generates the record, *t*\* ≥ *t*(*a*). Hence *t*\* lies within the retention window, so C1 requires *V*(*a*, *t*\*) = 1. Under Semantics I, *V*ᴵ(*a*, *t*\*) = *α*(*a*, *t*\*), so C1 requires *α*(*a*, *t*\*) = 1. But C2 requires *α*(*a*, *t*) = 0 for all *t* ≥ *t*ᵣ(*a*) + δ = *t*\*, so C2 requires *α*(*a*, *t*\*) = 0. The two requirements are contradictory, and no assignment of *α* satisfies both. The argument for the second disjunct is identical with *t*\* = *t*π(*a*) + 6 and C3 in place of C2. ∎

**Corollary 1.1 (cross-border case).** For cross-border audit records, *F*(*a*) = 120. The system is infeasible for record *a* whenever an erasure request arrives at any month *t*ᵣ(*a*) ≤ *t*(*a*) + 120 − δ: that is, at any point in the first nine years and eleven months of a ten-year window under the baseline response period. Infeasibility is therefore not an edge case arising from unusual timing; it is the generic case, avoided only if no data subject exercises Article 17 in respect of any record for essentially the whole of its retention life.

**Corollary 1.2 (Secure Processing Environment case).** For Secure Processing Environment access logs, *F*(*a*) = 12 and *σ*(*a*) = secondary. Suppose the permit expires at or before the eleventh month of the record's retention window, so that *t*π(*a*) + 6 ≤ *t*(*a*) + 12. Then C1 and C3 are contradictory at *t*\* = *t*π(*a*) + 6 by the argument above. **On the broad reading of Article 68(12) defended below, no erasure request is required.** The infeasibility then follows from two provisions of a single regulation acting on a single environment: Article 73(1)(e) requires the identifiable log to remain verifiable for twelve months, and Article 68(12) requires personal data to be gone from the environment six months after permit expiry. Where the remaining permit duration at the time the log is written is six months or less, the two windows necessarily overlap. The model makes no claim about how often this occurs in practice; the collision's existence, not its frequency, is what Corollary 1.2 asserts.

Corollary 1.2 is the sharpest form of the thesis's problem statement. It shows that the conflict does not depend on the exercise of a data-subject right, on the eHDSI deployment baseline, or on any synthesis across instruments of differing legal weight. It is internal to Regulation (EU) 2025/327.

**The interpretive condition on which Corollary 1.2 depends.** The corollary holds if, and only if, the deletion obligation of Article 68(12) reaches the identifiable access logs that Article 73(1)(e) requires to be kept. That condition is contestable and must be stated as such rather than assumed, because the corollary is the sharpest claim in this thesis and a reader is entitled to see its weakest joint.

The textual case for the broad reading is that the provision governs *the data within the secure processing environment* — a formulation defined by location rather than by provenance. It does not say "the data made available under the data permit," though the Regulation uses that narrower formulation freely elsewhere, and the access logs are indisputably data within the environment. On that reading Article 68(12) reaches them, and Corollary 1.2 follows.

The contextual case for the narrow reading is that the provision sits within the data-permit article, adjacent to provisions on permit duration, extension, and storage fees, and that the mischief it addresses is the indefinite retention of permitted datasets after the purpose that justified them has lapsed. On that reading the obligation attaches to the permit dataset, the access logs fall outside it, and no collision between Articles 68(12) and 73(1)(e) arises.

This thesis adopts the broad reading and states the grounds rather than asserting the conclusion. But the architecture of the results is deliberately such that little turns on which reading prevails, and that should be made explicit. Under the narrow reading, Corollary 1.2 lapses, and with it the claim that infeasibility arises without any data-subject action. Theorem 1 itself is untouched, because its first disjunct concerns erasure requests rather than permit expiry: identifiable access logs remain personal data whoever provided them, they remain within the scope of Article 17, and a request arriving inside the twelve-month floor collides with Article 73(1)(e) exactly as the cross-border case collides with the eHDSI floor. Corollary 1.1 is untouched entirely. Theorem 2, the mechanism, and the residue analysis are untouched, since they are indifferent to which instrument generates the deadline.

The narrow reading therefore costs the thesis its sharpest instance and none of its results. The broad reading, if correct, adds a collision that requires no data subject to act. Chapter 6 treats the resolution of this interpretive question as a matter for supervisory authority rather than for this author, alongside the authority question concerning verifiability itself.

## 4.7 Theorem 2 — Feasibility under Accountability-Preserving Verifiability

> **Theorem 2.** Under Semantics II, the constraint system {C1, C2, C3} is jointly satisfiable for every record *a* ∈ *A*, for every arrival pattern of erasure requests {*t*ᵣ(*a*)} and permit expiries {*t*π(*a*)}, and for every floor parameter *F*(*a*) ∈ ℕ.

**Proof (constructive).** Define the following trajectory for an arbitrary record *a*. Let

> *t*ᴵ(*a*) = min( *t*ᵣ(*a*) + δ, *t*π(*a*) + 6 )

be the **invalidation month**, with the convention min(∞, ∞) = ∞. Construct the trajectory:

1. For *t* < *t*ᴵ(*a*): set *α*(*a*, *t*) = 1. Retain *m*(*a*), *c*(*a*), *k*(*a*), and *p*(*a*).
2. At *t* = *t*ᴵ(*a*), if finite: destroy *k*(*a*) irreversibly; append to the audit trail an invalidation entry *ι*(*a*) recording the month, the legal ground (Article 17(1) or Article 68(12) as applicable), and the authorising actor; retain *m*(*a*) and *c*(*a*) unchanged.
3. For *t* > *t*ᴵ(*a*): set *α*(*a*, *t*) = 0. Retain *m*(*a*), *c*(*a*), and *ι*(*a*).

It must be shown that this trajectory satisfies all three constraints.

*C2 is satisfied.* If *t*ᵣ(*a*) < ∞ then *t*ᴵ(*a*) ≤ *t*ᵣ(*a*) + δ by construction, and by steps 2–3, *α*(*a*, *t*) = 0 for all *t* ≥ *t*ᴵ(*a*), hence for all *t* ≥ *t*ᵣ(*a*) + δ. If *t*ᵣ(*a*) = ∞, C2 is vacuous.

*C3 is satisfied.* If *σ*(*a*) = secondary and *t*π(*a*) < ∞ then *t*ᴵ(*a*) ≤ *t*π(*a*) + 6, and by the same steps *α*(*a*, *t*) = 0 for all *t* ≥ *t*π(*a*) + 6. Otherwise C3 is vacuous.

*C1 is satisfied.* Let *t* be any month in the retention window, *t*(*a*) ≤ *t* ≤ *t*(*a*) + *F*(*a*). Condition (i) holds because no step of the construction modifies or removes *m*(*a*). Condition (ii) holds because no step removes *c*(*a*); the commitment is not derived from *k*(*a*) and its persistence is unaffected by key destruction. For condition (iii): if *α*(*a*, *t*) = 1 the condition is vacuous; if *α*(*a*, *t*) = 0 then *t* ≥ *t*ᴵ(*a*), and step 2 has placed *ι*(*a*) in the audit trail, where step 3 retains it, and *ι*(*a*) is covered by (i). Hence *V*ᴵᴵ(*a*, *t*) = 1 throughout the window.

All three constraints are satisfied, for arbitrary arrival times and arbitrary *F*(*a*). ∎

**Corollary 2.1.** The construction requires no coordination between the erasure process and the retention process, and no knowledge at the time a record is created of whether an erasure request will ever arrive. The invalidation month is determined entirely by events as they occur.

**Corollary 2.2.** Because *F*(*a*) is arbitrary in the proof, the result holds simultaneously for the ten-year cross-border floor and the one-year Secure Processing Environment floor, and for any national floor substituted for either. The model is tri-lateral in constraint type and indifferent to the number of floor instances.

**A note on what kind of result this is.** An objection should be anticipated rather than left for a reader to formulate: that Theorem 2 proves little, because Semantics II was defined in full knowledge of the trajectory that satisfies it. The objection has force and the response is to concede its premise and deny its conclusion. The mathematical content of Theorem 2 is indeed modest: once verifiability is decoupled from payload accessibility, the existence of a satisfying trajectory is close to immediate, and the proof is a verification rather than a discovery. But the substantive claim of this chapter was never that a satisfying trajectory exists under some semantics; any number of semantics would admit one, including trivial semantics under which every record counts as verifiable always. The claim is that *this* semantics is a defensible reading of what the retention obligations require — grounded in the necessity boundary of Article 17(3)(b), the minimisation principle of Article 5(1)(c), and the accountability purpose the obligations serve: and that it is the weakest departure from current practice that achieves feasibility, preserving every element of the audit record that the accountability purpose needs and discarding only what it does not. Theorem 1 carries the load that Theorem 2 does not: it establishes that *some* departure is unavoidable, because the status quo admits no solution at all. Theorem 2 then shows that a principled and minimal departure suffices. The legal defensibility of Semantics II is argued in Section 4.2 and its want of authority is confronted in Chapter 6, Section 6.2; it is not established by the theorem, and no reader should take the theorem as establishing it.

**What the theorem does and does not establish.** It establishes that the constraint system as formalised admits a solution, and exhibits one. It does not establish that the exhibited solution is lawful — that depends on whether the residue it leaves clears the legal threshold, which Section 4.9 addresses: nor that key destruction can be verified by an external party, which Section 4.10 concedes it cannot. The invalidation entry specified in Section 4.8 is an *attested* record of destruction, not a *proof* of it; the proof-of-secure-erasure and certified-deletion literatures reviewed in Chapter 2, Section 2.4 mark that boundary, and Chapter 6 treats it as the outer limit of the contribution. Theorem 2 is a mathematical result about a model, and its value is that it converts a question that has been debated qualitatively into one with a definite answer under stated assumptions.

## 4.8 The Mechanism: Crypto-Erasure by Invalidation

The trajectory constructed in the proof of Theorem 2 is the specification of the mechanism. This section states it as an implementable design.

**Key hierarchy.** Each record's payload is encrypted under a per-record data key *k*(*a*). Per-record rather than per-subject or per-dataset granularity is required because the invalidation events of Theorem 2 occur at record granularity: a permit expiry invalidates the records of one permit, while an erasure request invalidates the records relating to one data subject, and these sets intersect without nesting. Data keys are themselves held under a key-encrypting key in a hardware security module or equivalent custody boundary. Destruction of *k*(*a*) is effected by destruction of the wrapped data key and any cached copies, within the documented custody boundary.

**Commitment.** *c*(*a*) = Commit(*p*(*a*), *r*(*a*)) with a per-record salt *r*(*a*). The salt is stored with the metadata and is *not* destroyed at invalidation; destroying it would break the binding property and with it the auditor's ability to verify an opened payload during the pre-invalidation period, while retaining it does not restore readability of the payload, which depends on *k*(*a*). The scheme must be hiding: an adversary holding *c*(*a*) and lacking *r*(*a*) must learn nothing about *p*(*a*). A bare unsalted hash of the payload does not satisfy this and must not be used, for the reason given in Section 4.9.

**The invalidation registry.** Invalidation entries are appended to the audit trail as first-class records. Each entry *ι*(*a*) contains the identifier of the invalidated record, the invalidation month, the legal ground, the authorising actor, and a commitment to the destroyed key's identifier: not to the key itself. The registry is append-only. Invalidation is an event that is logged, not an event that erases the log.

**Accumulator-based validity witnesses.** The set of currently valid (non-invalidated) records is maintained in a dynamic cryptographic accumulator supporting efficient revocation (Camenisch & Lysyanskaya, 2002). This provides an auditor with a succinct proof that a given record either is or is not currently valid, without the auditor enumerating the registry. The accumulator is an efficiency and verifiability layer, not a load-bearing component of the theorems: Theorem 2 holds if validity is established by linear scan of the registry, and the accumulator makes that check succinct.

**The auditor's view.** After invalidation, an external auditor examining record *a* can establish: that the access event occurred, with all its accountability attributes, from *m*(*a*); that a specific payload was bound to that event, from *c*(*a*); that the payload was invalidated, when, on what legal ground, and by whom, from *ι*(*a*); and that the record's current validity status is as claimed, from the accumulator witness. What the auditor cannot do is read the payload. This is the intended state, and it is the difference between this mechanism and the practitioner crypto-shredding pattern reviewed in Chapter 2, Section 2.4: that pattern retains ciphertext and asserts that erasure occurred, whereas this mechanism produces a verifiable record of what was invalidated and under what authority.

**End of life at floor expiry.** The constraints of Section 4.4 govern the record's behaviour through its retention window, but the window ends, and the model would be incomplete if it said nothing about what follows. At *t* = *t*(*a*) + *F*(*a*) the retention obligation lapses, and with it the necessity that justified retaining *m*(*a*) under Article 17(3)(b). Because the metadata contains the patient pseudonym and the actor identifier, it is personal data, and the storage-limitation principle of Article 5(1)(e) GDPR requires that it not be kept in identifiable form longer than the purpose demands. The mechanism therefore specifies a terminal transition: at floor expiry the record undergoes a second invalidation, in which the identifying fields of *m*(*a*) and the salt *r*(*a*) are destroyed, leaving a non-identifiable residue — the event type, the document category, the outcome, and the commitment: sufficient for statistical and assurance purposes and insufficient to relate the record to any data subject. The terminal transition is itself logged, and the record's final state is the only state in the mechanism that is intended to be anonymous rather than pseudonymous in the sense of Section 4.9. Where a longer-running obligation applies to the same record — a national archival duty, or litigation hold: the terminal transition is deferred and the floor parameter *F*(*a*) is set to the longer period, which is the parameterisation the model already supports.

**Applying the mechanism to the two cases.** For the cross-border primary-use case, the mechanism operates at the audit repository of the National Contact Point, at the point where the ATNA audit record is written. For the Secure Processing Environment case, it operates at the environment's access-logging boundary: the identifiable log required by Article 73(1)(e) is written with its personal-data content committed rather than retained in plaintext beyond the ceiling, so that at *t*π(*a*) + 6 the environment holds a complete, identifiable, verifiable log of access with no recoverable personal-data payload. The environment is thereby cleared of accessible personal data at the ceiling while continuing to satisfy the floor to its full twelve months.

## 4.9 Residue Analysis

Theorem 2 leaves a residue: *m*(*a*), *c*(*a*), *r*(*a*), *ι*(*a*), the accumulator state, and the ciphertext of *p*(*a*). Whether the mechanism is lawful depends on whether this residue sits on the correct side of the threshold at which data cease to be personal. This section performs that analysis, and it is included because Chapter 2 identified its absence as the fourth gap in the literature.

**The threat.** Finck's analysis for the European Parliament establishes that hashed or encrypted data likely remain personal data under GDPR so long as re-identification remains possible (Finck, 2019; Finck, 2018). Applied to this mechanism, the threat is direct: if *c*(*a*) is an unsalted hash of the payload, then an adversary who can guess candidate payloads can confirm a guess by recomputing the hash. For clinical documents drawn from a constrained space — a diagnosis code, a medication from a formulary: the guessing space may be small enough to make this practical. An unsalted commitment would therefore be a surviving item of personal data, and the mechanism would have relocated the erasure problem rather than solved it.

**The response.** This is why the hiding property is a requirement of the design and not an implementation preference. With a per-record salt *r*(*a*) of adequate length, confirming a guessed payload requires the salt; the commitment alone leaks nothing. The salt is retained, which means the residue is not unconditionally unlinkable: a party holding *r*(*a*) and a candidate payload can still confirm a match. What has been destroyed is the ability to *recover* the payload, which depends on *k*(*a*).

**The honest limit.** The residue therefore does not meet the strict Norwegian anonymisation threshold. Datatilsynet's guidance holds that encryption protects rather than anonymises, and that data remain personal while any key or linkage capable of re-identification is retained (Datatilsynet, 2015). By that standard the ciphertext, held together with a retained salt and metadata identifying the access event, is best characterised as pseudonymised rather than anonymous. This thesis does not claim otherwise, and any claim that the mechanism achieves anonymisation would be false.

**Why the mechanism is nonetheless defensible.** The applicable legal test is not anonymisation but erasure, and the European Data Protection Board's Guidelines 02/2025 accept that where physical overwriting is not technically possible, rendering data unrecoverable by cryptographic means can constitute an adequate substitute for erasure, provided the controller documents the threat model under which the data are considered unrecoverable (European Data Protection Board, 2026b). The final version 2.0, adopted on 7 July 2026 after public consultation, sharpens rather than softens the constraint this places on the present mechanism: it confirms that both metadata and content may in principle constitute personal data, and that this may extend to encrypted and hashed data. The residue characterisation of this section is therefore the one the Board's final position requires, and a thesis claiming anonymisation for that residue would now be contradicted by the guidance it relies upon. Aikebaier's (2026) systematisation formalises this correspondence, establishing an equivalence proposition between a Destruction-IND security notion and the Board's unrecoverability criterion. The design consequence is that the mechanism's lawfulness rests on a documented threat model, which must state: the custody boundary within which key destruction occurs; the assumed adversary's access to that boundary; the leakage assumptions for the hardware holding key material; and the algorithmic-break horizon over which the ciphertext's confidentiality is assumed to hold. A mechanism deployed without that documentation would not satisfy the Board's condition however sound its cryptography.

**The unavoidable residual risk.** Over a ten-year floor, the algorithmic-break horizon is a live concern rather than a formality: ciphertext retained for a decade must be assumed to face cryptanalytic capability that does not exist at the time of encryption. The mechanism mitigates this by ensuring that what is retained long-term is metadata and commitments rather than payload ciphertext wherever the retention purpose permits, but it does not eliminate the risk. This is recorded as a limitation in Chapter 6 rather than resolved here.

## 4.10 Rival Designs

A reviewer will propose alternatives. Four are treated here, and each is rejected for a stated reason rather than by assertion.

**Rival 1 — Rely on the Article 17(3)(b) exemption and retain in full.** This is the dissolution argument answered in Chapter 2, Section 2.3 and Section 4.2 above. It fails on the necessity boundary: the exemption protects retention that the legal obligation requires, and Section 4.2 established that the accountability purpose does not require payload accessibility. It fails additionally and decisively in the Secure Processing Environment case, where Article 68(12) admits no exemption parallel to Article 17(3)(b), so that Corollary 1.2's infeasibility survives the argument entirely.

**Rival 2 — Anonymise the audit record instead.** If the record were genuinely anonymised, Datatilsynet's equation of anonymisation with deletion would discharge the erasure obligation (Datatilsynet, n.d.-b). But genuine anonymisation of a cross-border audit record destroys its accountability function: an audit trail that cannot identify which clinician accessed which patient's record is not an audit trail, and Article 73(1)(e) requires the logs to be *identifiable* in terms. Anonymisation satisfies C2 and C3 by violating C1.

**Rival 3 — Minimise the payload at capture, so that nothing needs erasing.** Recording less at the outset is good practice and is compatible with this mechanism. It does not solve the problem, because the metadata that the accountability purpose requires, the patient pseudonym linking the access to a data subject, is itself personal data, and is precisely what an erasure request targets. Minimisation shrinks the payload; it does not remove the record from the scope of Article 17.

**Rival 4 — Delete the record and log the deletion.** This is the closest rival and deserves the most care. Deleting the audit record while logging that a deletion occurred satisfies C2 and C3, and preserves a trace. It fails C1 under both semantics: under Semantics I trivially, and under Semantics II because condition (ii) fails: no commitment survives, so the auditor can establish that *something* was deleted but not that the deleted item was the payload bound to that specific access event. The distinction matters in adversarial conditions. A controller who deletes records and logs deletions can conceal the substitution of one record for another; a controller bound to a surviving commitment cannot. The mechanism's advantage over Rival 4 is precisely the verifiability that Chapter 2 identified as absent from the practitioner crypto-shredding pattern.

**Rival 5 — Retain recoverable encrypted copies until the later date.** This is the resolution developed in the closest prior art, the DePaul retention-and-purging programme reviewed in Chapter 2, Section 2.4: hold encrypted copies in shadow tables and backups, with each copy's key selected to expire on the governing purge date, and effect purging by destroying that key (Scope, Rasin, Lenard, Heart, & Wagner, 2022; Scope & Rasin, 2025). Where both obligations are floors and the purge date is fixed in advance, this is the right design.

It cannot work against a ceiling, and the reason is the residue analysis of Section 4.9 applied in reverse. A copy whose key still exists is recoverable, and recoverable ciphertext held together with the means of decryption remains personal data under the threshold set out in Chapter 2, Section 2.3. Retaining such copies to satisfy the Article 73(1)(e) floor is therefore exactly what the Article 68(12) ceiling forbids of the environment holding them. The prior art satisfies a retention obligation by preserving recoverability; the mechanism specified here satisfies one by destroying recoverability and preserving accountability instead. That inversion, rather than any difference in cryptographic technique, is what the tri-lateral case requires.

**The critique that is not a rival.** SecuPi (2025) argues that cryptographic erasure introduces operational complexity in row-level encryption scenarios and that auditable key management adds rather than removes overhead. This is not an alternative design for the problem; it is a cost objection, and it is partly correct. Per-record key granularity in a high-volume audit repository is an operational burden. The response is that the burden is the price of a solution to a problem that has none otherwise, and that the burden falls on audit records rather than on clinical data stores, which is the smaller of the two surfaces. Chapter 6 engages this critique at length rather than dismissing it.

## 4.11 Integration with the Norwegian Infrastructure

The mechanism is specified against the Norwegian infrastructure as verified in Chapter 2, Section 2.6, not against an idealisation of it.

**Primary use: the National Contact Point.** Norway's NCPeH is in live pilot operation at the Bodø and Stjørdal emergency clinics, receiving patient summaries from Portugal, Czechia, and Finland, with expansion to further emergency clinics requested (Helsedirektoratet, 2026a, 2026b). The mechanism attaches at the sixth step of the OpenNCP transmission flow, where the ATNA audit record is written to the audit repository. It requires no change to service discovery, patient discovery, document retrieval, pivot translation, or the security and consent module. This placement is deliberate: it is the narrowest point of the flow at which the intervention achieves its purpose, and interventions at the other five steps would touch the interoperability surface that Member States have agreed and Norway has implemented.

**Secondary use — Helsedataservice and the Secure Processing Environments.** Helsedataservice holds decision authority for eleven central health registries (Folkehelseinstituttet, 2024). The mechanism attaches at the access-logging boundary of the Secure Processing Environment rather than inside the environment's analytical machinery. This placement is forced by the empirical finding that the Norwegian environment landscape is fragmented well beyond the three NORTRE nodes, extending to controller-provided servers, folders, and in some cases consumer cloud services and disconnected personal computers (SPUHiN, 2024). A mechanism requiring capabilities of the environment would fail against that reality; a mechanism operating on the log the environment must in any case produce does not.

**Compatibility with the national criteria.** The finalised Norwegian criteria for Secure Processing Environments require an information-security management system as mandatory, recommend ISO 27001 certification, and require eID-based authentication at defined assurance levels (SPUHiN, 2025). The mechanism requires nothing beyond these: key custody within a documented boundary is an information-security-management concern of exactly the kind the mandatory requirement already covers. It adds no requirement that the criteria do not already impose, which was the design constraint derived from Chapter 2's third gap.

**Relation to the pending implementing acts.** The binding technical requirements for Secure Processing Environments are to be laid down by Commission implementing acts under Article 73(5) EHDS, due by 26 March 2027 (European Parliament and Council of the European Union, 2025), after the submission of this thesis; the secondary-use provisions they will operationalise become applicable on 26 March 2029 under Article 105. The specification published by TEHDAS2 during 2026 as deliverable D7.4 is the best available anticipation of their content (TEHDAS2, 2026). The mechanism is therefore specified against a moving target, and the appropriate claim is compatibility with the infrastructure as currently specified rather than compliance with requirements not yet adopted. Chapter 6 treats the implications of this timing for the thesis's policy relevance.

## 4.12 Summary

This chapter formalised the tri-lateral retention conflict as a constraint-satisfaction problem over a single binary accessibility variable per record, with the retention floor parameterised so that the ten-year cross-border audit floor and the one-year Secure Processing Environment log floor are instances of one constraint. It proved that under the plaintext-verifiability semantics implicit in current practice the system is infeasible, generically so in the cross-border case and, critically, without any erasure request at all in the Secure Processing Environment case, where two retention provisions of a single regulation collide over a single environment. It proved that under an accountability-preserving semantics the system is jointly satisfiable for every arrival pattern and every floor, and the proof exhibited the trajectory that achieves satisfaction. That trajectory, specified as Crypto-Erasure by Invalidation, retains metadata and a hiding commitment, destroys the payload key at the earlier of the erasure deadline and the deletion ceiling, appends the invalidation to the audit trail as a first-class, witnessed event, and at floor expiry performs a terminal transition that destroys the identifying metadata and the salt, leaving a non-identifiable statistical residue: so that the record's whole life cycle, not merely its retention window, is accounted for under the storage-limitation principle.

The mechanism's residue was analysed rather than assumed: it is pseudonymised rather than anonymous by the strict Norwegian standard, it is defensible under the erasure test the European Data Protection Board has articulated provided the threat model is documented, and its long-horizon cryptographic risk is real and recorded. Four rival designs were considered and rejected on stated grounds, and the principal cost objection was acknowledged rather than dismissed. The integration analysis placed the mechanism at the two narrowest points of the Norwegian infrastructure at which it achieves its purpose, requiring nothing of the substrate that the finalised national criteria do not already require.

Chapter 5 demonstrates both theorems executably, over synthetic records generated as described in Chapter 3.

---

## References (Chapter 4)

Aikebaier, Y. (2026). *SoK: Cryptographic erasure on public ledgers: Application-layer architectures, key-lifecycle adversaries, and GDPR Art. 17 equivalence* (Cryptology ePrint Archive, Paper 2026/1109). https://eprint.iacr.org/2026/1109 [Preprint; not peer-reviewed]

Camenisch, J., & Lysyanskaya, A. (2002). Dynamic accumulators and application to efficient revocation of anonymous credentials. In *Advances in Cryptology — CRYPTO 2002* (LNCS 2442, pp. 61–76). Springer. https://doi.org/10.1007/3-540-45708-9_5

Datatilsynet. (2015). *Anonymisering av personopplysninger: veileder*. Norwegian Data Protection Authority.

Datatilsynet. (n.d.-a). *Etablere internkontroll* [Guidance]. Norwegian Data Protection Authority.

Datatilsynet. (n.d.-b). *Innebygd personvern og personvern som standard* [Guidance]. Norwegian Data Protection Authority.

European Data Protection Board. (2026b). *Guidelines 02/2025 on the processing of personal data through blockchain technologies* (Version 2.0, adopted 7 July 2026 following public consultation). EDPB.

European Parliament and Council of the European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88.

European Parliament and Council of the European Union. (2025). Regulation (EU) 2025/327 of 11 February 2025 on the European Health Data Space. *Official Journal of the European Union*.

Finck, M. (2018). Blockchains and data protection in the European Union. *European Data Protection Law Review, 4*(1), 17–35.

Finck, M. (2019). *Blockchain and the General Data Protection Regulation: Can distributed ledgers be squared with European data protection law?* European Parliament, STOA/EPRS.

Folkehelseinstituttet. (2024). *Helsedataservice: The national health data access body*. Norwegian Institute of Public Health.

Helsedirektoratet. (2026a). *MyHealth@EU, Helsedirektoratet* [National e-health portfolio measure]. Norwegian Directorate of Health.

Helsedirektoratet. (2026b). *MyHealth@EU, Norsk helsenett* [National e-health portfolio measure]. Norwegian Directorate of Health.

National Institute of Standards and Technology. (2025). *Special Publication 800-88 Revision 2: Guidelines for media sanitization* (R. Chandramouli & E. Hibbard). NIST. https://doi.org/10.6028/NIST.SP.800-88r2

Scope, N., & Rasin, A. (2025). *Systems and methods for data retention and purging* (U.S. Patent No. 12,425,209). U.S. Patent and Trademark Office.

Scope, N., Rasin, A., Lenard, B., Heart, K., & Wagner, J. (2022). Harmonizing privacy regarding data retention and purging. In *Proceedings of the 34th International Conference on Scientific and Statistical Database Management (SSDBM 2022)* (pp. 1–12). ACM. https://doi.org/10.1145/3538712.3538718

SecuPi. (2025). *Crypto-shredding is not nirvana for right of erasure or RTBF compliance* [Industry commentary]. https://secupi.com/crypto-shredding-is-not-nirvana-for-right-of-erasure-or-rtbf-compliance/

Simjanoska Misheva, M., et al. (2025). AI Act compliance within the MyHealth@EU framework: Tutorial. *Journal of Medical Internet Research*, *27*, e81184. https://doi.org/10.2196/81184

SPUHiN. (2024). *Recommendations for minimum requirements for Secure Processing Environments in Norway* (Draft, 29 November 2024). Helsedirektoratet & Folkehelseinstituttet.

SPUHiN. (2025). *Recommendations for minimum requirements for Secure Processing Environments in Norway* (D5.2, final, following public hearing). Helsedirektoratet & Folkehelseinstituttet.

TEHDAS2. (2025). *Guideline for Health Data Access Bodies on procedures and formats for data access* (D6.3). TEHDAS2 Joint Action.

TEHDAS2. (2026). *Technical specification for health data access bodies on the implementation of secure processing environments* (D7.4). TEHDAS2 Joint Action.


\pagebreak

---

# Chapter 5. Demonstration

*Every figure reported in this chapter was produced by the code listed in Appendix A, executed under seed 20260915. No number here was written before the code that produced it was run.*

---

## 5.1 Purpose and Claim

This chapter discharges Activity 4 of the design science cycle set out in Chapter 3, Section 3.2: demonstration. Its function is narrow and should be stated before the results, so that the results are not read as establishing more than they do.

The chapter demonstrates that the two theorems of Chapter 4 hold on the instances examined. It does not verify them in the proof-assistant sense, it does not measure performance, and it does not deploy anything. Theorem 1 predicts that under plaintext-verifiability semantics the constraint system fails whenever an erasure deadline or a deletion-ceiling deadline falls inside a record's retention window. Theorem 2 predicts that under accountability-preserving semantics the invalidation trajectory satisfies all three constraints for every arrival pattern. The demonstration's job is to make both predictions checkable by execution rather than only by argument.

A subsidiary claim is made for Corollary 1.2, which is the sharpest result in the thesis: that Secure Processing Environment access-log records become infeasible under plaintext semantics *without any erasure request at all*, through the collision of the Article 73(1)(e) one-year retention floor with the Article 68(12) six-month deletion ceiling. If the demonstration produces no witnesses of this kind, the corollary is in trouble. It produces thirty-nine.

## 5.2 Implementation

The checker is a single Python module of 322 lines including documentation and the independent cross-check, of which 246 are non-blank, non-comment lines and the constraint-evaluation logic proper occupies approximately ninety. It depends only on the Python standard library: `hashlib` for commitments, `random` for seeded generation, and `itertools` for the exhaustive cross-check. No cryptographic library, no solver, and no zero-knowledge proof system is used, consistent with the scope commitments of Chapter 1, Section 1.5.

Records are represented exactly as the model specifies. Each carries metadata `m` containing the actor identifier, the national contact point, the patient pseudonym, the document category, the legal basis, and the outcome; a payload; a hiding commitment `c = SHA-256(salt ‖ payload)` with a per-record sixteen-byte salt; a payload key `k`; a creation month `t_a`; a floor parameter `F`; and a pathway marker. Key destruction is modelled as irreversible removal of the key reference from the record's state, which is the sandbox's analogue of destruction within a custody boundary and is not a claim that the simulation destroys anything cryptographically.

Two record classes are generated, implementing the two floor instances that Chapter 4 absorbed into one parameterised constraint:

- **Cross-border audit records**, `F = 120` months, primary pathway. Erasure requests arrive for a given record with probability 0.40, at a uniformly distributed offset of one to one hundred and thirty months after creation. The offset range deliberately exceeds the window so that some requests fall outside it and the checker is not rigged to find violations.
- **Secure Processing Environment access-log records**, `F = 12` months, secondary pathway. Each carries a permit expiry at a uniformly distributed one to twelve months after creation. Erasure requests arrive with probability 0.25.

One hundred records of each class are generated, matching the population scale fixed in Chapter 3, Section 3.5. Seed 20260915 is fixed and reported; the run is deterministic and reproduces identically.

**Table 5.0 — Generation parameters (complete)**

| Parameter | Cross-border audit | SPE access log |
|---|---|---|
| Records generated | 100 | 100 |
| Retention floor *F* | 120 months (eHDSI baseline) | 12 months (Art 73(1)(e)) |
| Pathway σ | primary | secondary |
| Creation month *t_a* | uniform [0, 11] | uniform [0, 11] |
| Erasure-request probability | 0.40 | 0.25 |
| Erasure offset from *t_a* | uniform [1, 130] months | uniform [1, 18] months |
| Permit expiry *t_π* | not applicable | *t_a* + uniform [1, 12] months |
| Response period δ | 1 month (GDPR Art 12(3)) | 1 month |
| Deletion ceiling | not applicable | 6 months (Art 68(12)) |

Erasure-request assignment is drawn independently of permit length, so no record is steered toward violation by the generator.

Payloads are drawn from FHIR R4 resources in patient bundles generated by Synthea (Walonoski et al., 2018), produced with `java -jar synthea.jar -s 20260915 -cs 20260915 -p 100` and yielding 98 usable bundles. One clinical resource — a Condition, Observation, MedicationRequest, AllergyIntolerance, Immunization, or Procedure: is taken per bundle and serialised as the payload, giving a mean payload of 1,006 bytes against 35 bytes for the constructed strings used during development. Section 5.7 reports the comparison between the two.

## 5.3 Results under Semantics I

Under plaintext-verifiability semantics, `V(a,t) = α(a,t)`, so constraint C1 requires the payload to remain accessible throughout the retention window while C2 and C3 require it to become inaccessible from their respective deadlines. The checker reports every month at which both are required at once.

**Table 5.1 — Violations under Semantics I (seed 20260915, n = 200)**

| Record class | Records | With ≥1 violation | Share |
|---|---|---|---|
| Cross-border audit (F = 120) | 100 | 37 | 37% |
| SPE access log (F = 12) | 100 | 53 | 53% |
| **Total** | **200** | **90** | **45%** |

Total constraint violations: 95 across 90 records. The two counts differ because five SPE records collide with both C2 and C3; each is counted once in the per-record column and twice in the violation total. The full decomposition is 41 records violating C2 only, 44 violating C3 only, and 5 violating both: all five necessarily in the secondary pathway, since only that pathway carries both constraints.

Three features of this table require comment, and the third is the one that matters.

First, the violation rate is not one hundred per cent, and this is the correct behaviour rather than a weakness of the result. Theorem 1 is conditional: it states infeasibility for records whose erasure or ceiling deadline falls inside the retention window. A cross-border record for which no data subject ever exercises Article 17 has no second constraint to collide with C1, and is trivially feasible. Of the one hundred cross-border records, thirty-eight received an erasure request; of those, thirty-seven had a deadline landing inside the one-hundred-and-twenty-month window, and all thirty-seven are among the violations. The single exception is the record whose request arrived beyond the window, which is precisely the case the theorem excludes. The checker therefore reproduces the theorem's conditional structure exactly, including its boundary.

Second, the witnesses are specific and inspectable, which is the property Chapter 3 required of this component. Three examples, verbatim from the run:

> C1 requires V=1 (⇒ α=1) at t=116 within [11,131]; C2 requires α=0 from t=116
> C1 requires V=1 (⇒ α=1) at t=120 within [4,124]; C2 requires α=0 from t=120
> C1 requires V=1 (⇒ α=1) at t=41 within [0,120]; C2 requires α=0 from t=41

Each names the record, the collision month, the two constraints in conflict, and the window within which the conflict arises. A reader who doubts Theorem 1 can take any of these lines and check the arithmetic by hand.

Third, and most consequentially, the Secure Processing Environment class violates at a higher rate than the cross-border class, fifty-three per cent against thirty-seven, despite receiving erasure requests at a *lower* probability. The mechanism behind the inversion should be stated plainly, because an examiner's first reaction will be that the secondary pathway simply carries more constraints. That reaction is correct, and it is the point. Every SPE record faces the Article 68(12) ceiling by construction, while only forty per cent of cross-border records ever face any second constraint at all; the decomposition bears this out, with 49 of the SPE violations structural and only 4 request-driven, against all 37 cross-border violations being request-driven. The inversion is therefore not a sampling accident but the direct signature of a collision that the secondary pathway inherits from Regulation (EU) 2025/327 alone, without any data-subject action. Section 5.4 isolates it.

## 5.4 Corollary 1.2 — Infeasibility Without an Erasure Request

Seventy-eight of the one hundred Secure Processing Environment records received no erasure request. Under the received account of the retention–erasure problem, these records should be unproblematic: no data subject has asked for anything, so there is nothing for the retention obligation to conflict with.

**Thirty-nine of them are infeasible under Semantics I. That is exactly half of the records with no erasure request.**

The witnesses, verbatim:

> rid=100: t_a=7, permit expires t_pi=10 → C3 from t=16, C1 to t=19 | collision at t=16
> rid=103: t_a=7, permit expires t_pi=10 → C3 from t=16, C1 to t=19 | collision at t=16
> rid=104: t_a=3, permit expires t_pi=4 → C3 from t=10, C1 to t=15 | collision at t=10

Take the first. The access-log record is created in month seven. Article 73(1)(e) requires the identifiable log to remain verifiable until month nineteen. The data permit expires in month ten, so Article 68(12) requires personal data to be gone from the environment by month sixteen. Months sixteen through nineteen are therefore months in which the same regulation requires the same environment both to retain an identifiable access log and to hold no personal data. No data subject has exercised any right. No deployment baseline is involved. No synthesis across instruments of differing legal weight has occurred. On the reading of Article 68(12) adopted in Chapter 4, Section 4.6, the conflict is internal to Regulation (EU) 2025/327. Under the narrower reading canvassed there, these thirty-nine witnesses lapse and the secondary-use collisions reduce to the twenty-two records in this population that received erasure requests; Theorem 1, Corollary 1.1, and every Semantics II result are unaffected.

The fifty per cent figure has a straightforward structural explanation, and stating it guards against reading the number as more precise than it is. The collision occurs when `t_π + 6 ≤ t_a + 12`, that is when the permit runs six months or less. Permit lengths were drawn uniformly from one to twelve months, so half the draws fall at or below six. The figure is therefore a direct consequence of the permit-length distribution and is not an empirical estimate of how often this occurs in Norwegian practice. What the demonstration establishes is that the collision arises under ordinary parameters rather than contrived ones.

The obvious attack on this figure is that the twelve-month horizon was chosen to produce it. The response is structural: the collision rate scales as 6/π_max under a uniform permit horizon, so a longer horizon attenuates the rate without altering the existence of the collision, which Theorem 1 establishes independently of any distribution. The twelve-month horizon models the remaining permit duration at the moment an access event is logged, not total project length, and a record created late in a multi-year permit has a short remaining horizon regardless of the project's overall size. No figure in this chapter depends on the rate; the thesis's claim is that the collision occurs, not that it occurs with any particular frequency.

## 5.5 Independent Cross-Check

A checker that implements the constraints incorrectly would produce violations that reflect the implementation rather than the model. To guard against this, the sandbox includes a second, independently written procedure that takes the constraint definitions directly and searches exhaustively over every possible assignment of the accessibility variable across a fourteen-month horizon — 2¹⁴ = 16,384 assignments per case: reporting whether *any* assignment satisfies C1 under Semantics I together with C2 and C3.

**Table 5.2 — Exhaustive search over α assignments (horizon = 14 months)**

| Case | Feasible assignment exists? |
|---|---|
| SPE, no erasure request, permit 3 months | **False** |
| SPE, erasure request at t = 2 | **False** |
| Cross-border (floor scaled to 12 for tractability), erasure at t = 4 | **False** |
| Control: no erasure request, no permit expiry | **True** |

The three conflict cases admit no satisfying assignment whatsoever, which is a stronger statement than the main checker makes: it establishes not merely that the trajectory the checker examined fails, but that no trajectory succeeds. The control case, in which neither C2 nor C3 is active, is feasible: confirming that the search is capable of returning True and that the infeasibility results are not an artefact of a procedure that never succeeds.

The cross-border floor is scaled from one hundred and twenty months to twelve for this check, because exhaustive search over 2¹²⁰ assignments is not computable. The scaling does not affect the logic: Theorem 1's argument depends on the deadline falling inside the window, not on the window's length, and the scaled case preserves that relation. This substitution is noted rather than hidden, and it is the one place in the demonstration where a parameter was altered for tractability.

## 5.6 Results under Semantics II

The invalidation trajectory from the constructive proof of Theorem 2 was then applied to every record: destroy the payload key at `t_I = min(t_r + δ, t_π + 6)`, append an invalidation entry recording the month, the legal ground, and the authorising actor, and retain metadata, commitment, and salt unchanged.

**Table 5.3 — Results under Semantics II (same 200 records, same seed)**

| Measure | Value |
|---|---|
| Records invalidated | 138 / 200 |
| — on ground GDPR Article 17(1) | 52 |
| — on ground EHDS Article 68(12) | 86 |
| Records with ≥1 constraint violation | **0 / 200** |
| Total constraint violations | **0** |

Every record that was infeasible under Semantics I is feasible under Semantics II, and no record is made worse. The ninety violating records become zero.

The distribution of invalidation grounds is itself informative. Eighty-six invalidations are triggered by permit expiry under Article 68(12) and only fifty-two by erasure requests under Article 17(1). The majority of invalidation events in this population arise from the regulation's own deletion ceiling rather than from data-subject action: which is consistent with Section 5.4 and reinforces the point that the tri-lateral problem is not reducible to a right-to-be-forgotten problem.

The auditor's view of a record that was infeasible before invalidation, verbatim from the run for record 100:

> metadata intact : True — actor=HP-026, ncp=NO, outcome=success
> commitment c(a) : 11087780fd192c8fdaa237081ee0bb11…
> payload key k(a) : None ← destroyed
> invalidation ι(a) : month=16, ground=EHDS Art 68(12)
> payload readable? : False

This is the state the mechanism is designed to produce, and it is worth reading against what Semantics I would have demanded. The access event is fully established: which health professional, at which contact point, with what outcome. The binding to a specific payload survives in the commitment. The invalidation is itself a logged, grounded, attributed event rather than a silent absence. And the payload is unreadable, at month nineteen as at month sixteen. An auditor examining this record learns everything accountability requires and nothing the erasure obligation forbids.

## 5.7 What the Demonstration Establishes, and What It Does Not

**Established.** Both theorems hold on all two hundred generated instances. Theorem 1's conditional structure is reproduced exactly, including the boundary case of the request falling outside the window. Corollary 1.2 has thirty-nine concrete witnesses in which two provisions of one regulation collide over one environment with no data-subject action involved. The infeasibility results survive an independently written exhaustive search that considers every possible accessibility assignment rather than only the trajectory the main checker examines. The invalidation trajectory eliminates every violation without introducing any.

**Not established, and not claimed.** The demonstration does not prove the theorems for all instances; it checks them on the instances generated under one seed, and the exhaustive cross-check covers four small cases rather than the general result. The proofs in Chapter 4, not this chapter, carry the general claim. No performance measurement was taken, and no statement about execution time, throughput, or storage overhead appears anywhere in this thesis. The sandbox does not connect to any National Contact Point, implement the OpenNCP transmission flow, or evaluate consent policies. Key destruction is simulated by removing a reference in program state, which demonstrates the mechanism's logic and demonstrates nothing whatever about whether key destruction can be assured in deployment: the limitation that Chapter 2 drew from the secure-deletion literature and that Chapter 6 engages.

**Payload provenance, tested rather than assumed.** Chapter 3, Section 3.6 specifies a realism layer feeding Synthea-generated records into the checker. That layer was built and executed, and its result is reported here because it bears on how much the demonstration's figures depend on the fixtures chosen.

The layer substitutes real FHIR R4 resources for the constructed payload strings and leaves every timing quantity — creation month, erasure arrival, permit expiry, floor, response period: exactly as generated. Mean payload size rises from 35 bytes to 1,006. All two hundred commitments change, confirming that the payloads genuinely differ.

**Table 5.4 — Constructed against Synthea-generated payloads (same seed, same timings)**

| Measure | Constructed | Synthea | 
|---|---|---|
| Semantics I: records with violation | 90 | 90 |
| Semantics I: total violations | 95 | 95 |
| Corollary 1.2 witnesses (no erasure request) | 39 | 39 |
| Records invalidated | 138 | 138 |
| Semantics II: records with violation | 0 | 0 |
| Semantics II: total violations | 0 | 0 |
| Commitments differing between runs | — | 200 / 200 |

Every reported figure is identical while every commitment differs. This is the expected result and the model would be defective if it were otherwise: no constraint in the TRF Model reads the content of a payload, so the results are functions of timing and accessibility alone. The value of running the comparison rather than asserting the invariance is that a reader can see the claim tested against a case where the inputs demonstrably changed.

One limitation of the generated cohort is carried forward. Synthea's default export conforms to US Core profiles with United States demographics and care patterns, not to the Norwegian basisprofiler (HL7 Norway, 2025). The FHIR version matches Norway's, the resource structure is genuine, and the invariance result above establishes that the mismatch cannot affect any figure in this chapter; but no claim of Norwegian clinical representativeness is made for the records, and the thesis's Norwegian grounding rests on the infrastructure analysis of Chapter 4, Section 4.11 rather than on the synthetic population.

The complete run, including the exhaustive cross-check over 65,536 assignments, completes in under one-twentieth of a second on ordinary hardware, which is stated only to indicate that reproduction costs a reader nothing and is not offered as a performance result.

The artefact is publicly available, which converts the reproducibility claim from an assertion into something a reader can test while reading. The source repository and a hosted demonstration are listed in Appendix A. The hosted application executes the same unmodified source and verifies, at the point of execution, that its run reproduces the figures reported in this chapter; it reports a failure notice rather than results if it does not. No claim in this thesis depends on the hosted application remaining available, and the repository, not the hosting, is the artefact.

The demonstration therefore supports precisely the claim Chapter 1 made for it: the artefact behaves as specified, and the specification's central results are checkable by a reader who declines to take the proofs on trust.

---

## Appendix A — Checker source and run output

The complete source of `trf_checker.py` and the verbatim console output of the run reported in this chapter are reproduced in Appendix A of the thesis. The run is reproduced by executing `python trf_checker.py` with no arguments; seed 20260915 is set in the module header, and the output is byte-identical across runs.


---

## References (Chapter 5)

HL7 Norway. (2025). *hl7.fhir.no.basis* (Version 2.2.2) [FHIR R4 national base profile package]. Simplifier.net.

Walonoski, J., Kramer, M., Nichols, J., Quina, A., Moesel, C., Hall, D., Duffett, C., Dube, K., Gallagher, T., & McLachlan, S. (2018). Synthea: An approach, method, and software mechanism for generating synthetic patients and the synthetic electronic health care record. *Journal of the American Medical Informatics Association*, *25*(3), 230–238. https://doi.org/10.1093/jamia/ocx079


\pagebreak

---

# Chapter 6. Discussion

---

## 6.1 What the Thesis Establishes

Before the limitations, the claim. Stating it precisely is what makes the limitations affordable.

The thesis establishes that the European Health Data Space Regulation contains, within a single chapter, two provisions that cannot both be satisfied by a Secure Processing Environment under ordinary operating conditions. Article 73(1)(e) requires identifiable logs of access to and activity in the environment to be kept for at least one year. Article 68(12) requires personal data to be deleted from that environment within six months of the expiry of the data permit. Identifiable access logs are personal data. Where the remaining permit duration at the time a log is written is six months or less, the two requirements overlap, and no state of the environment satisfies both.

That claim rests on one contestable interpretive step, stated here rather than buried: Article 68(12) governs *the data within the secure processing environment*, and the thesis reads that as reaching the identifiable access logs the environment generates rather than only the dataset supplied under the permit. Chapter 4, Section 4.6 sets out the grounds on both sides and identifies exactly which results depend on the reading: the answer being this claim alone. Given that step, the claim requires no data subject to exercise any right, no deployment baseline external to the Regulation, and no synthesis across instruments of different legal weight. Chapter 5 produced thirty-nine concrete witnesses of it in a population of one hundred Secure Processing Environment records, and the same conditions produced ninety infeasible records across the full population of two hundred when the cross-border audit floor is included.

The thesis further establishes that this infeasibility is not a property of the obligations but of an assumption about what satisfies them. Under the semantics implicit in audit systems designed before the right to erasure existed, a record is verifiable while its payload is readable, the constraint system has no solution. Under a semantics in which a record is verifiable while its accountability content is intact and any loss of payload accessibility is itself logged, grounded, and attributed, the system is satisfiable for every arrival pattern of erasure requests and permit expiries, and for every retention floor. Chapter 4 proves both results; Chapter 5 witnesses them executably, and an independently written exhaustive search confirms that under the first semantics no assignment of payload accessibility whatsoever could succeed.

Finally, the thesis specifies the mechanism that the feasibility proof exhibits: per-record keys, hiding commitments, invalidation entries carrying month, legal ground, and authorising actor, and a terminal transition at floor expiry that discharges the storage-limitation obligation on the metadata itself. Two clarifications of status belong here. The specification also provides for accumulator-based validity witnesses, which are an efficiency and verifiability layer rather than a component of either theorem, Theorem 2 holds if validity is established by linear scan, and they are specified but not implemented: the demonstration of Chapter 5 exercises keys, commitments, and invalidation entries, and no accumulator was built or run.

What follows engages the objections to all of this in the order of their seriousness.

## 6.2 The Authority Problem

The most serious objection to this thesis is not technical, and it has not been raised by any reviewer of the work. It is that Semantics II is an argument, not an authority.

No regulator, court, or supervisory authority has held that an audit record whose payload has been cryptographically invalidated continues to satisfy a retention obligation. The thesis argues that it does, and the argument is a good one: Article 17(3)(b) protects only processing that is *necessary* for the legal obligation; Article 5(1)(c) requires that no more personal data be retained than the purpose demands; the accountability purpose of an audit record is served by knowing who accessed what, when, and under what authority, not by continued readability of the clinical payload. The Norwegian Data Protection Authority's internal-control guidance places exactly this balancing on the controller (Datatilsynet, n.d.-a), and its privacy-by-design guidance equates anonymisation with deletion (Datatilsynet, n.d.-b). But none of this amounts to a holding that invalidation discharges retention.

The consequence must be stated without softening. If a supervisory authority takes the view that Article 73(1)(e)'s requirement of "identifiable logs" entails logs whose subject matter remains readable, then Theorem 2 remains mathematically true and becomes practically inert: the mechanism would satisfy a constraint system that does not describe the law. The thesis would still have established the collision, which is textual and survives any reading, and would still have established that the collision is *dissolvable in principle* by a semantic move. It would not have established that the move is available.

Three considerations bear on how likely that outcome is, and they are offered as reasons rather than reassurance.

First, the alternative readings are worse. If verifiability requires readability, then Article 73(1)(e) and Article 68(12) are in irreconcilable conflict and one must simply be disapplied: an outcome a supervisory authority is unlikely to prefer to a reading under which both can be honoured.

Second, the direction of regulatory travel favours the argument. The European Data Protection Board's Guidelines 02/2025, finalised as version 2.0 on 7 July 2026, accept that where physical deletion is not technically possible, deleting the decryption key can render the data unintelligible and so serve the erasure obligation, while maintaining that encrypted and hashed data may themselves remain personal data and that the unintelligibility holds at least until the algorithm is broken (European Data Protection Board, 2026b). The further qualification that such a substitution depends on a *documented threat model* is not the Board's formulation but Aikebaier's (2026), whose equivalence proposition connects a Destruction-IND security notion to the Board's criterion; the distinction is preserved here because the two carry different authority. What the Guidelines themselves supply is a functional rather than literal reading of an obligation: the same move Semantics II makes on the retention side.

Third, the question is decidable by asking. Chapter 7 proposes, as the highest-value next step, seeking an opinion from Datatilsynet on whether accountability-preserving verifiability discharges the retention obligation in Article 73(1)(e). That is a tractable request with a determinate answer, and it would convert the thesis's central interpretive move from argument to authority or else refute it cleanly. Either outcome is worth more than the present uncertainty.

A second authority question sits beside the first and is narrower. Whether Article 68(12) reaches the access logs is a question of statutory construction that a supervisory authority or, ultimately, a court will settle, and that this author cannot. The thesis adopts the broad reading on textual grounds — the provision is framed by location rather than provenance, and the Regulation uses the narrower "made available under the data permit" formulation freely elsewhere when it means it: while conceding that the provision's placement within the data-permit article supports the narrower construction. What makes this tolerable rather than fatal is that the dependency is confined: Corollary 1.2 stands or falls with it, and nothing else in the thesis does. A request to Datatilsynet on the verifiability question could reasonably carry this one alongside it.

## 6.3 Key Destruction and the Limits of Assurance

The second objection is the one the thesis has carried since Chapter 2, and it is the honest ceiling of the contribution.

The mechanism's guarantees are conditional on the irreversible destruction of key material. The canonical systematisation of secure deletion establishes that the further a deletion approach operates from the physical storage medium, the harder it becomes to assert that destruction actually occurred (Reardon, Basin, & Capkun, 2013). Cryptographic erasure is the limiting case: it operates entirely above the medium, reducing the deletion of arbitrary data to the deletion of a key, and inheriting in concentrated form the problem that key destruction cannot be confirmed by inspection.

The thesis's response is to be precise about what the invalidation entry is. It is an *attested* record of destruction, not a *proof* of it. The entry records that a named actor destroyed a named key at a named month on a named legal ground, and binds that claim into an append-only audit trail alongside a commitment to the destroyed key's identifier. An auditor can establish that the claim was made, by whom, and when; an auditor cannot establish that the claim is true. The difference between attestation and proof is the boundary of this contribution.

That boundary is where an active research programme sits, and naming it locates the thesis honestly within the field rather than overstating its reach. Proof-of-secure-erasure protocols seek evidence that a prover has erased its memory, with recent work relaxing the isolation assumptions such protocols traditionally require (Bursuc, Gil-Pons, Mauw, & Trujillo-Rasua, 2024). In the quantum setting, encryption with certified deletion produces a deletion certificate, and its authors identify *public verifiability* — enabling parties other than the originator to verify such a certificate: as an open problem (Broadbent & Islam, 2020). Were public verifiability of deletion certificates achieved, the invalidation entry specified in Chapter 4 could carry a proof rather than an attestation, and the mechanism's guarantee would strengthen from conditional to demonstrable without any change to the model.

One further consideration limits the practical weight of this objection. The alternative to attested key destruction is not proven deletion; it is unattested deletion. A controller who deletes an audit record and logs that a deletion occurred is making exactly the same kind of unverifiable claim, with strictly less structure: there is no surviving commitment, so an auditor cannot even establish *what* was destroyed. The mechanism does not solve the assurance problem. It does improve on every available alternative with respect to it.

## 6.4 The Cost Objection

SecuPi (2025) argues that cryptographic erasure introduces operational complexity in row-level encryption scenarios, that auditable key management adds rather than removes overhead, and that policy-based access control is a better answer to the right to erasure in heavily distributed systems. This critique is substantially correct on its own terms and must be engaged rather than dismissed.

The mechanism specified in Chapter 4 requires per-record key granularity, and Section 4.8 explains why: invalidation events occur at record granularity, because a permit expiry invalidates the records of one permit while an erasure request invalidates the records relating to one data subject, and those sets intersect without nesting. Coarser granularity would make some invalidations impossible to perform without over-invalidating. Per-record keys in a high-volume audit repository are an operational burden, and the thesis does not pretend otherwise.

Three observations bound that burden without denying it.

The burden falls on audit records rather than on clinical data stores. The mechanism operates at the audit-trail boundary — the sixth step of the MyHealth@EU transmission flow, or the access-logging boundary of a Secure Processing Environment: not on the electronic health records themselves. This is the smaller of the two surfaces by a wide margin, and the placement was chosen for that reason as much as for substrate independence.

The burden is bounded and auditable in a way the alternative's is not. Key-management overhead is a known quantity that scales with record volume and can be budgeted, monitored, and inspected. The residual-copy problem that plaintext deletion faces — establishing that no backup, cache, replica, or derived index retains the deleted data: is unbounded and largely uninspectable. Trading an unbounded and invisible cost for a bounded and visible one is a defensible engineering choice, and it is the choice the mechanism makes.

The critique's proposed alternative does not address the problem this thesis identifies. Policy-based and attribute-based access control govern *who may read* data; they do not cause data to cease to be readable. Against Article 68(12), which requires that personal data not remain in the environment, an access-control answer does not satisfy the obligation: the data remain, protected by policy. Against the collision of Corollary 1.2, access control offers nothing at all. The critique is well-aimed at crypto-shredding as a general answer to the right to erasure, which is the claim SecuPi is addressing; it is not aimed at the tri-lateral retention problem, and does not reach it.

## 6.5 Synthetic Data and the Limits of the Demonstration

Chapter 3 specified a two-layer sandbox: a feasibility checker carrying the load-bearing claim, and a realism layer feeding it Synthea-generated FHIR records. Both were built and both were run, and the result of running the second is more informative than its mere existence.

Substituting real FHIR R4 resources for constructed payload strings changed every commitment in the population, all two hundred, and changed no reported figure whatsoever. Mean payload size rose from thirty-five bytes to one thousand and six. Violations, witnesses, invalidation counts, and grounds were identical. This is the expected outcome and the model would be defective otherwise, since no constraint in the TRF Model reads payload content; the value of running the comparison rather than asserting the invariance is that the claim was tested against a case where the inputs demonstrably moved.

Two limitations of the generated cohort are carried forward rather than resolved.

Synthea's default export conforms to the US Core implementation guide, with United States demographic, geographic, and care-pattern parameters. The FHIR version matches the version the Norwegian basisprofiler constrain, and the resource structure is genuine, but the profiles are not Norwegian and no claim of Norwegian clinical representativeness is made for the records. The invariance result establishes that this cannot affect any figure, and the thesis's Norwegian grounding rests on the infrastructure analysis of Chapter 4, Section 4.11 rather than on the synthetic population. Had the thesis made epidemiological or clinical claims, this limitation would be disqualifying; because its claims concern the behaviour of audit records under constraint, it is not.

Synthea's validity has itself been assessed. Chen and colleagues found the generator reliable in modelling demographics and the probability of services being offered, and limited in modelling heterogeneous outcomes following intervention and regional variation in care quality (Chen, Chun, Patel, Chiang, & James, 2019). The same reasoning applies: the limitations are in dimensions this thesis does not use.

The deeper limitation is that a demonstration over generated instances is not a proof over all instances. The general claims rest on the arguments in Chapter 4, and those arguments are informal rather than machine-checked. The executable check and the exhaustive cross-check reduce the probability that an error in the proofs has gone unnoticed; they do not eliminate it.

## 6.6 Implications for Practice and Policy

The timing argument is the strongest claim to practical relevance this thesis makes, and it is worth stating with the calendar in front of it.

Regulation (EU) 2025/327 entered into force on 26 March 2025. Under Article 105 it applies generally from 26 March 2027, and the secondary-use provisions of Chapter IV, which contain both Article 68(12) and Article 73(1)(e), apply from 26 March 2029. Article 73(5) requires the Commission, by means of implementing acts and by 26 March 2027, to lay down the technical, organisational, information-security, confidentiality, data-protection, and interoperability requirements for Secure Processing Environments.

The collision this thesis characterises is therefore not yet operative, and the specifications that will determine how it is handled are not yet written. That is an unusually favourable position for a piece of academic work to occupy. A framework that arrives after infrastructure has hardened around a problem is archaeology; one that arrives while the specifications are being drafted can affect defaults. The Norwegian position sharpens this further: the national criteria for Secure Processing Environments were finalised through the SPUHiN process after a public hearing running from July to October 2025, and are positioned explicitly as a national reference basis pending the Union implementing act (SPUHiN, 2025). The finalised compliance checklists, as inspected, address information-security management, identity assurance, and access governance — an information-security management system graded mandatory, ISO 27001 certification recommended, eID-based authentication at defined assurance levels: and no requirement addressing the reconciliation of retention with erasure and deletion appears among them. This is an absence observed in the published checklists rather than established against the full deliverable, which remains on the verification register; the claim is stated at that strength deliberately.

The corrected picture of Norwegian cross-border operations reinforces rather than weakens this. Norway's National Contact Point is in live pilot operation at the Bodø and Stjørdal emergency clinics, connected to Portugal, Czechia, and Finland, with the Directorate's own portfolio reporting noting that no relevant patients had yet presented for the solution to be used in practice (Helsedirektoratet, 2026a, 2026b). The cross-border audit stream has effectively not begun. A design element proposed now would shape how those records are structured from the outset rather than requiring their retrospective reconstruction.

Three concrete implications follow for the bodies that will write the specifications.

For the Commission drafting the Article 73(5) implementing acts, the reconciliation of Article 73(1)(e) with Article 68(12) is a question the acts must answer, and this thesis offers a candidate answer that does not require amending either provision. Silence in the implementing acts would leave every Health Data Access Body to resolve the collision independently, which is the outcome that produces the fragmentation the EHDS exists to prevent.

For Health Data Access Bodies including Helsedataservice, the invalidation entry is the practical takeaway even if the full mechanism is not adopted: recording *what was invalidated, when, on what legal ground, and by whom* as a first-class audit event costs little and converts an unexplained absence into an accountable one.

For TEHDAS2 and its successors, whose Secure Processing Environment specifications published during 2026 define minimum capabilities and the interoperability baseline for federating environments, the collision is presently unaddressed in guidance that treats deletion at permit closure as an operational service.

A word of restraint is owed here. This thesis is a Master's dissertation proposing a design, not a regulatory impact assessment. The policy implications above are offered as an argument to the bodies concerned, not as advice they are obliged to weigh, and their force depends entirely on the authority question of Section 6.2 being resolved favourably.

## 6.7 Theoretical Implications

Three contributions to the scholarly conversation follow from the work, each modest and each stated at its actual size.

The first is the formalisation itself. Treating a retention conflict as a constraint-satisfaction problem over a single binary accessibility variable per record, and making the semantics of verifiability an explicit parameter of the model rather than an unexamined assumption, is a way of stating retention problems that appears not to have been used before in this domain. The general method of formalising legal compliance as satisfiability is established (Feng, Marsso, Sabetzadeh, & Chechik, 2022); its application here is what is new, and the applicability of the formulation beyond health data is an open question the thesis does not settle. The structure — one or more floors, a subject-triggered right, a ceiling: is not obviously specific to health. Financial record-keeping under MiFID II is a candidate instance, flagged here for future analysis rather than established: the practitioner literature reviewed in Chapter 2 treats that setting as a floor-against-right conflict, and whether any ceiling analogous to Article 68(12) operates there is a question this thesis has not investigated.

The second is the identification of the semantic assumption as the locus of the problem. The literature treats the retention-erasure tension as a conflict between obligations. The model locates it instead in an interpretive assumption that neither obligation states, and shows that the assumption is doing the work: with it, infeasibility; without it, satisfiability. This reframing suggests a general question for regulatory-compliance modelling, namely how many apparent conflicts between legal obligations are artefacts of implicit operational semantics inherited from systems built under earlier law.

The third is the positioning of the contribution relative to the cryptographic literature. Aikebaier's (2026) systematisation of cryptographic erasure closes by naming five open problems, of which the fifth is erasure under multi-regime retention conflict. This thesis addresses that problem in one regulatory setting, with the reservations of Sections 6.2 and 6.3 attached. The fourth open problem on the same list, composition with zero-knowledge selective disclosure, is a problem this thesis creates rather than solves, and Chapter 7 treats it accordingly.

## 6.8 Boundaries as Contribution

An unusual amount of this thesis consists of statements about what it does not do. That is a deliberate methodological position and not an apology, and it is worth defending explicitly because an examiner may read it either way.

The first version of this project, abandoned in May 2026, claimed six original contributions, a first-ever framework, institutional review board approval that had not been obtained, and a zero-knowledge architecture that was never built. Its bibliography contained a series of citations to works that do not exist, identified during the audit that led to the rebuild. None of those claims could survive a determined reader, and the breadth of the claims was precisely what made them fragile: a claim to have done six things fails if any one of them fails.

The rebuilt thesis makes one bounded claim and prices every limitation into it in advance. The proofs are informal, not machine-checked. The demonstration covers generated instances under one seed, not all instances. Key destruction is simulated in program state and says nothing about deployment assurance. The synthetic records carry US Core profiles, not Norwegian ones. The cryptographic primitives are established technique, not novel construction. The closest prior art is a patent claiming key-expiry selection for retention-purge conflicts, disclosed and distinguished rather than omitted. The interpretive move at the centre of the thesis is an argument without authority behind it.

Each of those concessions costs nothing, because none of them was ever claimed. That is the practical value of a narrow claim, and it is the methodological lesson of the rebuild: a contribution that states its boundaries can be checked at those boundaries and found sound, whereas a contribution that does not can only be found wanting.

## 6.9 Summary

The thesis establishes a collision internal to the European Health Data Space Regulation, proves that it follows from an assumption about verifiability rather than from the obligations themselves, exhibits the mechanism that dissolves it, and demonstrates both results executably with an independent cross-check.

Its principal vulnerability is that the interpretive move at its centre has no regulatory authority behind it, and resolving that is the most valuable next step available. Its honest ceiling is that attested key destruction is not proven key destruction, a boundary marked by an active research programme in proof-of-secure-erasure and certified deletion. Its principal cost is per-record key management, bounded and auditable where the alternative's residual-copy problem is neither. Its demonstration is a witness rather than a proof, and its synthetic records are structurally genuine but not Norwegian.

Against those, the collision is textual and survives any reading; the field's own systematisation names the problem class as open; the specifications that will determine the outcome are not yet written; and the Norwegian cross-border audit stream has barely begun. Chapter 7 draws the conclusions and states the work that follows.

---

## References (Chapter 6)

Aikebaier, Y. (2026). *SoK: Cryptographic erasure on public ledgers: Application-layer architectures, key-lifecycle adversaries, and GDPR Art. 17 equivalence* (Cryptology ePrint Archive, Paper 2026/1109). https://eprint.iacr.org/2026/1109 [Preprint; not peer-reviewed]

Broadbent, A., & Islam, R. (2020). Quantum encryption with certified deletion. In *Theory of Cryptography (TCC 2020)* (LNCS 12552, pp. 92–122). Springer. https://doi.org/10.1007/978-3-030-64381-2_4

Bursuc, S., Gil-Pons, R., Mauw, S., & Trujillo-Rasua, R. (2024). Software-based memory erasure with relaxed isolation requirements. In *2024 IEEE 37th Computer Security Foundations Symposium (CSF)*. IEEE. arXiv:2401.06626

Chen, J., Chun, D., Patel, M., Chiang, E., & James, J. (2019). The validity of synthetic clinical data: A validation study of a leading synthetic data generator (Synthea) using clinical quality measures. *BMC Medical Informatics and Decision Making*, *19*, 44. https://doi.org/10.1186/s12911-019-0793-0

Datatilsynet. (n.d.-a). *Etablere internkontroll* [Guidance]. Norwegian Data Protection Authority.

Datatilsynet. (n.d.-b). *Innebygd personvern og personvern som standard* [Guidance]. Norwegian Data Protection Authority.

European Data Protection Board. (2026a). *Coordinated Enforcement Framework report on the implementation of the right to erasure under Article 17 GDPR* (18 February 2026). EDPB.

European Data Protection Board. (2026b). *Guidelines 02/2025 on the processing of personal data through blockchain technologies* (Version 2.0, adopted 7 July 2026 following public consultation). EDPB.

European Parliament and Council of the European Union. (2025). Regulation (EU) 2025/327 of 11 February 2025 on the European Health Data Space. *Official Journal of the European Union*.

Feng, N., Marsso, L., Sabetzadeh, M., & Chechik, M. (2022). *Bounded satisfiability checking of metric first-order temporal logic*. arXiv:2209.04052.

Helsedirektoratet. (2026a). *MyHealth@EU, Helsedirektoratet* [National e-health portfolio measure]. Norwegian Directorate of Health.

Helsedirektoratet. (2026b). *MyHealth@EU, Norsk helsenett* [National e-health portfolio measure]. Norwegian Directorate of Health.

Reardon, J., Basin, D., & Capkun, S. (2013). SoK: Secure data deletion. In *2013 IEEE Symposium on Security and Privacy* (pp. 301–315). IEEE. https://doi.org/10.1109/SP.2013.28

SecuPi. (2025). *Crypto-shredding is not nirvana for right of erasure or RTBF compliance* [Industry commentary]. https://secupi.com/crypto-shredding-is-not-nirvana-for-right-of-erasure-or-rtbf-compliance/

SPUHiN. (2025). *Recommendations for minimum requirements for Secure Processing Environments in Norway* (D5.2, final, following public hearing July–October 2025) [Project deliverable]. Helsedirektoratet & Folkehelseinstituttet.

TEHDAS2. (2026). *Technical specification for health data access bodies on the implementation of secure processing environments* (D7.4). TEHDAS2 Joint Action.


\pagebreak

---

# Chapter 7. Conclusion

---

## 7.1 The Problem and the Answer

This thesis began from a conflict that the European Health Data Space Regulation does not resolve. Cross-border health data exchange generates audit records subject to retention floors: ten years under the eHDSI deployment baseline for MyHealth@EU audit repositories, one year under Article 73(1)(e) for the access logs of Secure Processing Environments. The same records are subject to the erasure right of Article 17 GDPR, exercisable at any moment within those windows, and to the deletion ceiling of Article 68(12) EHDS, which requires data to be gone from a Secure Processing Environment within six months of permit expiry. No instrument reconciles them, no guidance addresses their interaction, and the technical specifications that will have to handle them are not due until 26 March 2027.

The thesis answered the question in three movements.

It formalised the conflict as the Tri-Lateral Retention Feasibility Model: a constraint-satisfaction problem over a single binary variable per record, the accessibility of its personal-data payload, with three constraint types — a parameterised retention floor, an erasure deadline, and a deletion ceiling: and with the semantics of *verifiability* made an explicit parameter rather than an unexamined assumption.

It proved two results within that model. Under plaintext-verifiability semantics, in which a record is verifiable while its payload remains readable, the constraint system is infeasible whenever an erasure deadline or a ceiling deadline falls inside a retention window. Under accountability-preserving semantics, in which a record is verifiable while its metadata is intact, its commitment survives, and any loss of payload accessibility is itself logged and attributed, the system is jointly satisfiable for every arrival pattern of erasure requests and permit expiries and for every floor parameter.

It specified the mechanism that the second proof exhibits. Crypto-Erasure by Invalidation retains event metadata and a hiding commitment, destroys the per-record payload key at the earlier of the erasure deadline and the deletion ceiling, appends the invalidation to the audit trail as a first-class event carrying its month, legal ground, and authorising actor, and performs a terminal transition at floor expiry that destroys the identifying metadata and leaves a non-identifiable statistical residue.

The answer to the research question is therefore that the three regimes can be reconciled, that the reconciliation requires no amendment to any instrument, and that what it requires instead is abandoning an assumption about audit records that no instrument states and that predates the right to erasure.

## 7.2 Contributions

Four contributions are claimed, each bounded.

**A formal characterisation of the tri-lateral retention conflict.** The general method of treating legal compliance as a satisfiability problem is established (Feng, Marsso, Sabetzadeh, & Chechik, 2022) and is not claimed here. What is new is its application to a retention system combining floors, a subject-triggered right, and a ceiling, and the isolation of verifiability semantics as the parameter that determines feasibility. The most recent systematisation of the cryptographic-erasure literature names erasure under multi-regime retention conflict among five open problems for the field (Aikebaier, 2026); this thesis addresses that problem in one regulatory setting.

**Two feasibility results with an executable witness.** Theorem 1 establishes infeasibility under the status-quo semantics; Theorem 2 establishes satisfiability under the alternative and exhibits the trajectory that achieves it. Both were demonstrated over two hundred records, producing ninety infeasible records and ninety-five violations under the first semantics and none under the second, with an independently written exhaustive search confirming that under the first semantics no assignment of payload accessibility whatsoever succeeds. The proofs are informal and the demonstration covers generated instances; neither is presented as more.

**A mechanism specification with its residue analysed.** The mechanism applies established primitives — cryptographic erasure as recognised in NIST SP 800-88 Revision 2, hiding commitments, dynamic accumulators: and claims no cryptographic novelty. What it adds to the practitioner crypto-shredding pattern is verifiability: an auditor can establish what was invalidated, when, on what ground, and by whom. The residue it leaves is characterised honestly as pseudonymised rather than anonymous by the Norwegian threshold, and designed to the corridor that the European Data Protection Board's finalised Guidelines 02/2025 establish.

**An integration analysis against verified Norwegian infrastructure.** The mechanism is placed at the two narrowest points at which it achieves its purpose — the audit-repository step of the MyHealth@EU transmission flow, and the access-logging boundary of a Secure Processing Environment: and requires of the substrate nothing that the finalised national criteria do not already demand. That constraint was derived from the documented fragmentation of Norwegian practice rather than assumed.

## 7.3 What the Thesis Does Not Establish

Six limitations bound the contribution, and each was priced into the claim before it was made.

The proofs are argued informally at the standard normal for design-science work, not machine-checked. The demonstration covers instances generated under one seed, and the exhaustive cross-check covers four small cases at a scaled horizon.

Key destruction is simulated as the removal of a reference in program state. The invalidation entry is an attested record of destruction, not a proof of one, and no approach operating above the storage medium can supply the latter (Reardon, Basin, & Capkun, 2013).

The synthetic records conform to US Core profiles with United States demographics rather than to the Norwegian basisprofiler. The comparison reported in Chapter 5 establishes that this cannot affect any result, since no constraint in the model reads payload content, but no Norwegian clinical representativeness is claimed for the records.

No performance measurement is offered as a result anywhere in this thesis, and no system was deployed. The sandbox connects to no National Contact Point, implements no part of the OpenNCP transmission flow, evaluates no consent policy, and contains no zero-knowledge proof system.

The mechanism's per-record key granularity imposes an operational cost that the critique reviewed in Chapter 6, Section 6.4 identifies correctly. The thesis argues that the cost is bounded and auditable where the alternative's residual-copy problem is neither, but does not quantify it.

And two interpretive steps at the centre of the work rest on argument rather than authority. That is the subject of the next section, and it is the honest statement of where this thesis is weakest.

## 7.4 The Two Open Questions of Authority

Both questions are legal rather than technical, and neither can be settled by better modelling.

The first concerns verifiability. No regulator or court has held that an audit record whose payload has been cryptographically invalidated continues to satisfy a retention obligation. The thesis argues that it does, from the necessity boundary of Article 17(3)(b) read with the data-minimisation principle of Article 5(1)(c), and from the Norwegian Data Protection Authority's own framing of retention as a balancing duty on the controller. If a supervisory authority instead reads "identifiable logs" in Article 73(1)(e) as requiring logs whose subject matter remains readable, Theorem 2 remains true of the model and inert in practice.

The second concerns scope. Article 68(12) governs *the data within the secure processing environment*. The thesis reads that as reaching the identifiable access logs the environment generates, on the grounds that the provision is framed by location rather than provenance and that the Regulation uses the narrower "made available under the data permit" formulation elsewhere when it means it. The competing construction, supported by the provision's placement within the data-permit article, confines it to the permitted dataset. Chapter 4, Section 4.6 shows that Corollary 1.2 stands or falls with this question and that nothing else in the thesis does.

Both questions are decidable by asking, and asking is the single highest-value action available to this research programme. A request to Datatilsynet — whether accountability-preserving verifiability discharges a retention obligation, and whether Article 68(12) reaches access logs: has a determinate answer. A favourable answer converts the thesis's central interpretive moves from argument into authority. An unfavourable answer refutes them cleanly and identifies precisely what would have to change. Either outcome is worth more than the present uncertainty, and neither requires further modelling to obtain.

## 7.5 Future Work

Four lines follow, the first immediate and the remainder in ascending order of difficulty.

**Execution of the expert evaluation.** The instrument specified in Appendix C — an eight-person panel across data protection, health IT architecture, Secure Processing Environment operation, and information logistics; a live demonstration of the artefact; a semi-structured guide; and a sixteen-item closed-response questionnaire across utility, regulatory alignment, operational viability, and audit integrity: is designed and ready to execute. It requires notification to Sikt and a lead time of four to six weeks, and it would supply exactly the evidence this thesis cannot generate analytically: practitioner readings of the Article 68(12) scope question, operator judgements on whether attested key destruction is sufficient in their context, and architectural assessment of the boundary placement. Together with the two authority questions of Section 7.4, this is the shortest route from the present contribution to a validated one.

**Selective disclosure of invalidation completeness.** The mechanism creates a problem it does not solve. When a data subject exercises Article 17, every record relating to them is invalidated, and an auditor should be able to confirm that *all* of them were. But identifying which records those are reveals the subject's cross-border care history, which is precisely what the erasure was meant to protect. Proving completeness of invalidation without revealing the invalidated set is a zero-knowledge problem, and it corresponds to the fourth of the five open problems identified by Aikebaier (2026), composition with zero-knowledge selective disclosure. This is where succinct arguments become necessary rather than decorative. The project name carried by this work originates in an earlier design that assumed zero-knowledge machinery would enforce the retention conflict; the analysis showed it unnecessary there, and shows it unavoidable here.

**Public verifiability of deletion certificates.** The boundary identified in Chapter 6, Section 6.3 would move if a deletion could be proven rather than attested. Proof-of-secure-erasure protocols pursue this in the classical setting under relaxed isolation assumptions (Bursuc, Gil-Pons, Mauw, & Trujillo-Rasua, 2024), and quantum encryption with certified deletion produces a certificate whose public verifiability its authors identify as open (Broadbent & Islam, 2020). Were public verifiability achieved, the invalidation entry specified here could carry a proof in place of an attestation, and the mechanism's guarantee would strengthen from conditional to demonstrable with no change to the model.

**Generalisation beyond health data.** The structure the model captures — one or more retention floors, a subject-triggered erasure right, and a deletion ceiling: is not obviously specific to health. Whether other regulated sectors present genuine tri-lateral instances, as distinct from the bi-lateral floor-against-right conflicts documented in financial record-keeping, is a question this thesis has flagged rather than investigated. Establishing that the formulation transfers, or that it does not, would determine whether the contribution is a result about one regulation or a method for a class of them.

## 7.6 Closing

The European Health Data Space is being built now. Norway's National Contact Point is in live pilot at two emergency clinics with the cross-border audit stream barely begun; the implementing acts that will specify how Secure Processing Environments handle their records are due in March 2027; the secondary-use provisions they will operationalise apply from March 2029; and the Norwegian national criteria, finalised after public hearing, govern how such environments are secured and who may enter them while saying nothing about what happens when the retention regimes on their records collide.

This thesis does not claim to have found something no one could have seen. The provisions it sets against each other are public, short, and adjacent in the same chapter of the same regulation. What it claims is to have set them against each other formally, to have shown that the resulting impossibility follows from an assumption rather than from the obligations, to have exhibited and demonstrated the mechanism that dissolves it, and to have done all of that while the specifications are still being written rather than after infrastructure has hardened around the problem.

The contribution is small, bounded, and checkable. Every number in it was produced by code that runs in under a twentieth of a second and that any reader can execute. Every limitation was stated before it was found. The two places where the argument outruns its authority are named rather than concealed, and the means of settling them is a letter rather than a research programme.

That is the thesis. What remains is to ask the questions it cannot answer itself.

---

## References (Chapter 7)

Aikebaier, Y. (2026). *SoK: Cryptographic erasure on public ledgers: Application-layer architectures, key-lifecycle adversaries, and GDPR Art. 17 equivalence* (Cryptology ePrint Archive, Paper 2026/1109). https://eprint.iacr.org/2026/1109 [Preprint; not peer-reviewed]

Broadbent, A., & Islam, R. (2020). Quantum encryption with certified deletion. In *Theory of Cryptography (TCC 2020)* (LNCS 12552, pp. 92–122). Springer. https://doi.org/10.1007/978-3-030-64381-2_4

Bursuc, S., Gil-Pons, R., Mauw, S., & Trujillo-Rasua, R. (2024). Software-based memory erasure with relaxed isolation requirements. In *2024 IEEE 37th Computer Security Foundations Symposium (CSF)*. IEEE. arXiv:2401.06626

Feng, N., Marsso, L., Sabetzadeh, M., & Chechik, M. (2022). *Bounded satisfiability checking of metric first-order temporal logic*. arXiv:2209.04052.

National Institute of Standards and Technology. (2025). *Special Publication 800-88 Revision 2: Guidelines for media sanitization* (R. Chandramouli & E. Hibbard). NIST. https://doi.org/10.6028/NIST.SP.800-88r2

Reardon, J., Basin, D., & Capkun, S. (2013). SoK: Secure data deletion. In *2013 IEEE Symposium on Security and Privacy* (pp. 301–315). IEEE. https://doi.org/10.1109/SP.2013.28


\pagebreak

---

# Appendix A — Code Artefacts and Reproduction Record

**Thesis:** Verifiable Crypto-Erasure for Cross-Border Health Data Audit Trails under the European Health Data Space
**Author:** Arshad Akhtar Abbasia, MSc Sustainable Energy Logistics, Høgskolen i Molde
**Supervisor:** Prof. João Ferreira
**Artefact date:** 18 September 2026

This appendix contains every piece of code written for the thesis, the exact commands used to produce every reported result, and the provenance of all data. Nothing reported in Chapters 4 or 5 was produced by code not listed here.

---

## A.1 Availability

The artefact is publicly available in two forms.

| Form | Location |
|---|---|
| Source repository | https://github.com/Astheno-sphere/TRF |
| Live demonstration | https://trfhimolde.streamlit.app/ |

The repository is the citable artefact and contains the checker, the realism layer, and the demonstration viewer. The live application is a convenience for readers who prefer not to clone and run: it executes the same unmodified source, and its first tab asserts that the run reproduces the figures reported in Chapter 5, displaying a failure notice rather than results if it does not.

A note on durability. Hosted applications are not archival objects: the live demonstration may be withdrawn or may sleep after inactivity, and no claim in this thesis depends on its availability. Every result reported here is reproducible from the code listed below by executing a single command on any machine with Python installed, which is the form in which the artefact should be assessed.

## A.1b Contents

| File | Purpose | Lines |
|---|---|---|
| `trf_checker.py` | Feasibility checker — executable witness for Theorems 1 and 2, including the independent exhaustive cross-check | 322 |
| `synthea_layer.py` | Realism layer — substitutes Synthea-generated FHIR R4 payloads and compares every reported figure against the constructed-payload run | 132 |
| `synthea_sample/` | Three representative Synthea bundles, trimmed to 25 entries each, included so a reader can inspect the payload structure without regenerating the cohort | — |
| `build_substrate_patch1.py` | Generator for the research-substrate patch workbook (September 2026, round 1) | — |
| `build_substrate_patch2.py` | Generator for the research-substrate patch workbook (round 2: corrections CORR-015–021, fetch register) | — |

Two files are *not* included and the reason is stated rather than omitted: the full 98-bundle Synthea cohort (314 MB) and the Synthea jar (197 MB). Both are regenerable from the commands in A.3, deterministically, under the seeds given.

---

## A.2 Environment

```
OS            Ubuntu 24.04
Python        3.x, standard library only (hashlib, random, itertools, glob, json, os)
Java          OpenJDK 21.0.10 (required for Synthea only)
Dependencies  none for the checker; openpyxl for the substrate patch generators
```

The checker has no third-party dependencies. This is deliberate: a reader should be able to run it on any machine with Python installed, without a package manager, and confirm the thesis's central results for themselves.

---

## A.3 Exact commands

**1 — Run the feasibility checker (produces every figure in Chapter 5, Sections 5.3–5.6):**

```bash
python3 trf_checker.py
```

Deterministic. Seed 20260915 is set in the module header. Output is byte-identical across runs and across machines. Runtime measured at 0.019 s.

**2 — Obtain Synthea (required only for the realism layer):**

```bash
curl -sL -o synthea.jar \
  https://github.com/synthetichealth/synthea/releases/download/master-branch-latest/synthea-with-dependencies.jar
```

**3 — Generate the synthetic cohort:**

```bash
mkdir -p synthea_run && cd synthea_run
java -jar ../synthea.jar \
  -s 20260915 -cs 20260915 -p 100 \
  --exporter.fhir.export=true \
  --exporter.hospital.fhir.export=false \
  --exporter.practitioner.fhir.export=false \
  --generate.only_alive_patients=true
```

`-s` sets the population seed and `-cs` the clinician seed; both are fixed to the thesis seed so the cohort is reproducible. The run yields 98 usable patient bundles from 100 requested. Output lands in `synthea_run/output/fhir/`.

**4 — Run the realism layer and the payload-provenance comparison (produces Table 5.4):**

```bash
python3 synthea_layer.py
```

Expects the cohort at `./synthea_run/output/fhir/`. Reports both runs side by side and flags any divergence.

---

## A.4 What the code does

### `trf_checker.py`

Implements the TRF Model of Chapter 4 directly. Records are the seven-element tuples of Section 4.3. Two record classes are generated: cross-border audit records with a 120-month floor, and Secure Processing Environment access-log records with a 12-month floor and the Article 68(12) ceiling. Generation parameters are listed in full in Chapter 5, Table 5.0.

Three components matter for the thesis's claims:

- `check_semantics_I()` evaluates the constraint system under plaintext verifiability, reporting for each record the first month at which C1 and C2, or C1 and C3, are simultaneously required. These are the witnesses for Theorem 1.
- `check_semantics_II()` applies the constructive trajectory from the proof of Theorem 2 — destroy the payload key at `min(t_r + δ, t_π + 6)`, append a grounded invalidation entry, retain metadata and commitment: and then verifies all three constraints.
- `brute_force_semantics_I()` is written independently of the first function, taking the constraint definitions directly and enumerating all 2¹⁴ assignments of the accessibility variable over a fourteen-month horizon. It exists so that the infeasibility results do not rest on the correctness of a single implementation. The control case, in which neither C2 nor C3 is active, returns feasible: confirming the search can succeed when it should.

Cryptographic operations use `hashlib` only. Commitments are salted (`SHA-256(salt ‖ payload)`) because Chapter 4, Section 4.9 establishes that an unsalted hash of a low-entropy clinical payload would itself remain personal data. Salts are derived deterministically from the record identifier so that runs reproduce exactly; the code states in a comment that production deployments must use a CSPRNG.

Key destruction is modelled as setting the key reference to `None`. This demonstrates the mechanism's logic and demonstrates nothing about deployment assurance: a limitation stated in Chapter 5, Section 5.7 and treated in Chapter 6.

### `synthea_layer.py`

Replaces the constructed payload strings with real FHIR R4 resources drawn from Synthea bundles — one clinical resource per bundle, from `Condition`, `Observation`, `MedicationRequest`, `AllergyIntolerance`, `Immunization`, or `Procedure` — recomputes each commitment over the real payload, and leaves every timing quantity untouched. It then runs both populations through the same checks and prints them side by side.

The expected result, and the observed one, is that every reported figure is identical while all 200 commitments differ. Mean payload size rises from 35 bytes to 1,006. The model reads timing and accessibility, never payload content; running the comparison rather than asserting the invariance lets a reader see the claim tested against inputs that demonstrably changed.

---

## A.5 Data provenance

All data used anywhere in this thesis is synthetic. No real patient data was requested, obtained, or processed at any point.

The cohort is generated by Synthea (Walonoski et al., 2018), an open-source synthetic patient generator. Synthea's default export conforms to the **US Core** implementation guide with United States demographic, geographic, and care-pattern parameters. The FHIR version is **R4**, which matches the version the Norwegian basisprofiler constrain; the *profiles* are not Norwegian, and no claim of Norwegian clinical representativeness is made for these records. The invariance result of Table 5.4 establishes that this mismatch cannot affect any reported figure. The thesis's Norwegian grounding rests on the infrastructure analysis of Chapter 4, Section 4.11.

The three bundles in `synthea_sample/` are trimmed to their first 25 entries purely to keep the appendix a reasonable size; the trimming is cosmetic and affects nothing, since the layer draws a single resource per bundle.

---

## A.6 Integrity record

Results reported in Chapters 4 and 5 and confirmed by execution:

| Result | Value | Where reported |
|---|---|---|
| Semantics I — records with ≥1 violation | 90 / 200 | Table 5.1 |
| Semantics I — total violations | 95 | §5.3 |
| Violation decomposition | 41 C2-only, 44 C3-only, 5 both | §5.3 |
| Corollary 1.2 witnesses (no erasure request) | 39 | §5.4 |
| Exhaustive cross-check, three conflict cases | no satisfying assignment | Table 5.2 |
| Exhaustive cross-check, control case | satisfying assignment exists | Table 5.2 |
| Semantics II — records invalidated | 138 (52 Art 17, 86 Art 68(12)) | Table 5.3 |
| Semantics II — total violations | 0 | Table 5.3 |
| Synthea comparison — figures changed | none | Table 5.4 |
| Synthea comparison — commitments changed | 200 / 200 | Table 5.4 |
| Reference commitment, record 100 | `11087780fd192c8f…` | §5.6 |

The reference commitment is included so that a reader re-running the checker can confirm in one glance that their run matches the one reported. It is unchanged across the salt-handling refactor documented in the thesis change log, which is the intended behaviour.

---

## A.7 Known limitations of the artefact

Stated here so that they are not inferred from silence:

1. The demonstration checks the theorems on the instances generated under one seed. The general claims rest on the proofs in Chapter 4, not on this code.
2. The exhaustive cross-check covers four small cases at a fourteen-month horizon. The cross-border floor is scaled from 120 months to 12 for that check because 2¹²⁰ assignments are not enumerable; Theorem 1's argument depends on the deadline falling inside the window, not on the window's length.
3. No performance measurement is offered as a result. The runtime figure in Chapter 5 indicates only that reproduction is cheap.
4. Key destruction is simulated in program state. The artefact demonstrates the mechanism's logic and says nothing about whether destruction can be assured in deployment.
5. The checker does not connect to any National Contact Point, implement the OpenNCP transmission flow, evaluate consent policies, or implement any zero-knowledge proof system. None of these is claimed anywhere in the thesis.


\pagebreak

---

# Appendix B — Search Query Log

This log records every search query executed in the course of the literature review, recovered from the working record of each session. Queries are reproduced as run, including those that produced nothing usable, since a curated log would be less credible than a complete one.

Some entries are document-retrieval or verification queries rather than discovery queries: targeting a known citation, a regulation's text, or a specific document's status. These are marked **[R]**. Discovery queries, which sought literature not already known to the review, are unmarked. Both are reported because the distinction matters for interpreting what the log evidences: only discovery queries bear on the absence claim of Chapter 2, Section 2.9. They are natural-language queries rather than Boolean strings, which is what the review actually used; Chapter 2, Section 2.1 states this and gives a Boolean replication protocol separately.


## Round 1 — 25 May 2026 (landscape, infrastructure, regulatory baseline)

1. `Norway electronic health record EHR infrastructure 2026 new regulations`
2. `MyHealth@EU cross-border patient summary how it works national contact point`
3. `eHDSI OpenNCP audit trail consent data minimisation HCP authorization IHE XCA`
4. `Norway Helsenorge kjernejournal architecture FHIR HL7 helseplattformen DIPS`
5. `European Health Data Space EHDS regulation 2025 primary secondary use timeline`
6. `Norway health data research innovation Helseanalyseplattformen Norwegian Centre HUNT BigMed`
7. `Norway Helsedataservice secondary use health data 2025 application portal Direktoratet for e-helse`
8. `Norwegian patient gets treated Spain ePrescription patient summary how process works`
9. `Norway MyHealth@EU national contact point eHealth go-live status 2025 2026`
10. `Norway AI medical imaging research 2025 federated learning health data`
11. `ZK-EHR zk-SNARK blockchain electronic health records MDPI Systems 2026`
12. `MDPI Systems \`
13. `KONFIDO project \`
14. `Helsedirektoratet EHDS European Health Data Space gap analysis Norway 2025`
15. `OpenNCP github repository ehdsi.europa.eu source code documentation NCP gateway`
16. `Norway AI Act implementation Nkom DigDir consultation 2025 h\u00f8ring Regulation 2024/1689`

## Round 2 — 29 May 2026 (verification and correction round)

17. `SPUHiN \`
18. `EHDS implementation 2026 cross-border patient summary technical infrastructure Member State`
19. `IHE ATNA Audit Trail Node Authentication integration profile retention requirement`
20. `eHDSI MyHealth@EU audit log retention period years requirement`
21. `eHDSI security framework audit log retention specification cross-border European`
22. `GDPR Article 17 right erasure audit log retention healthcare EDPB guidance`
23. `cryptographic erasure audit log healthcare GDPR right to be forgotten academic`
24. `KONFIDO project OpenNCP architecture cross-border 2018 technical paper Natsiavas`
25. `zero-knowledge proof healthcare audit log verifiable revocation 2024 2025 2026`
26. `cryptographic accumulator commitment scheme revocation healthcare audit hash chain`

## Round 3 — 15 September 2026 (resumption; novelty and currency)

27. `Helsedataservice Norway secondary use access body workflow data permit registry`
28. `information logistics digital supply chain cross-border data flow regulatory compliance academic`
29. `Norwegian offshore workers health records cross-border medical exchange maritime logistics`
30. `formal model conflict audit log retention GDPR right to erasure constraint satisfaction`
31. `formal verification regulatory compliance conflicting retention requirements temporal logic healthcare audit`
32. `operations research optimization model data governance compliance reconciliation supply chain regulatory constraints`
33. `thesis chapter 3 TRF model formal specification VERA-SNARK`
34. `TRF model gate feasibility theorem crypto-erasure invalidation chapter 4`
35. `Norge EHDS E\u00d8S gjennomf\u00f8ring helsedata juni 2026`
36. `Google Drive read file content`

## Round 4 — 16 September 2026 (adversarial novelty, prior art, currency)

37. `EHDS secondary use audit log retention erasure 2026 IEEE Scopus formal compliance health data`
38. `"retention conflict" OR "conflicting retention" cryptographic erasure formal model 2026 arXiv`
39. `EUR-Lex 2025/327 Article 73 secure processing environment "keeping of identifiable logs" access activities year`
40. `Regulation 2025/327 EHDS entry into force 26 March 2025 application date Article 105 staggered 2029`
41. `EDPB Guidelines 02/2025 blockchain personal data final version adopted after public consultation`
42. `TEHDAS2 deliverable secure processing environment technical specifications 2026 D7 tehdas.eu`
43. `eHOMB eHealth Operational Management Board Norway ePrescription without eDispensation change proposal requirement catalogue approved`
44. `EHDS Article 68 paragraph 12 "data permit" delete personal electronic health data secure processing environment six months expiry`
45. `Walonoski Synthea synthetic patient generator JAMIA 2018 25(3) 230-238`
46. `validity synthetic clinical data Synthea validation clinical quality measures limitations`
47. `HL7 Norway basisprofiler FHIR R4 no-basis 2026 status`
48. `Datatilsynet NIF Norges idrettsforbund vedtak syntetiske testdata personopplysninger test`
49. `Peffers Tuunanen Rothenberger Chatterjee design science research methodology Journal of Management Information Systems 2007 24 3 45-77`
50. `NIST SP 800-88 Revision 2 media sanitization published date 2025 draft final`
51. `Norge MyHealth@EU pasientsammendrag pilot Bodø Stjørdal legevakt Portugal Tsjekkia Finland`
52. `EHDS implementing acts 2026 secure processing environment specifications adopted status`
53. `eprint 2026/1109 SoK cryptographic erasure public ledgers Destruction-IND`
54. `GDPR Article 12(3) one month respond erasure request extension two months`
55. `SPUHiN D5.2 recommendations minimum requirements secure processing final helsedirektoratet`
56. `Reardon Basin Capkun SoK secure data deletion 2013 IEEE`
57. `Finck blockchain GDPR European Parliament study 2019 can distributed ledgers be squared right erasure`
58. `Datatilsynet sletting anonymisering kryptering personopplysninger krav`
59. `formal model audit retention versus erasure crypto-shredding paper 2026`

---

**Total distinct queries logged: 59** across four dated rounds.

## Note on coverage

The log records queries executed through the review's search tooling. Two categories of source entered the review by other routes and are noted here so that the log is not read as exhaustive of how sources were found.

Backward snowballing from reference lists supplied several sources, including the Camenisch and Lysyanskaya accumulator work and the Benaloh and de Mare original, which were reached from Ren's survey rather than by query.

The closest prior art — the DePaul retention-and-purging programme and United States Patent 12,425,209: was located during the adversarial round 4 through patent-database searching, which sits outside the query tooling this log records. That search is noted here rather than omitted, because a log claiming completeness while containing no query capable of finding the most important prior-art item in the review would misrepresent itself.


\pagebreak

---

# Appendix C — Expert Evaluation Instrument

*(v1, 18 September 2026. The instrument specified here was designed following supervisory feedback of September 2026 and constitutes the evaluation design for the next iteration of the design science cycle. Its execution status is stated in Chapter 3, Section 3.9.)*

---

## C.1 Purpose and status

Chapter 3, Section 3.7 sets out the analytical evaluation strategy adopted for this thesis: internal validity through logical consistency and executable checking, external validity through compatibility analysis against verified infrastructure, and reliability through deterministic execution. That strategy evaluates the artefact against the objectives stated in Chapter 1, Section 1.3, and it is the evaluation the thesis reports.

It does not collect stakeholder input. Design Science Research as elaborated by Hevner, March, Park, and Ram (2004) and Peffers, Tuunanen, Rothenberger, and Chatterjee (2007) treats evaluation as an activity that may be conducted through several methods, of which expert assessment is one, and a specification-and-demonstration study of the kind reported here frequently designs the evaluation that a subsequent cycle executes. This appendix is that design.

The instrument is specified in sufficient detail to be executed without further design work: panel composition and recruitment approach, session structure, demonstration script, semi-structured interview guide, a closed-response questionnaire, the analysis approach, and the data-protection arrangements execution would require. The four closed-response dimensions follow the structure proposed in supervisory feedback and are reproduced with their anchor statements intact.

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

1. **Show the record structure.** One audit record: metadata, payload, commitment, key. Identify which parts the accountability purpose needs and which it does not.
2. **Run the checker under plaintext semantics.** `python3 trf_checker.py`. Show the output: ninety-five violations across ninety of two hundred records. Open one witness line and walk through the arithmetic: the collision month, the two constraints, the window.
3. **Isolate the Corollary 1.2 cases.** Thirty-nine Secure Processing Environment records with no erasure request at all. Show record 100: created month 7, permit expires month 10, ceiling from month 16, floor to month 19. State the interpretive condition (Chapter 4, Section 4.6) explicitly rather than glossing it.
4. **Show the exhaustive cross-check.** Sixteen thousand three hundred and eighty-four assignments per case; no satisfying assignment in the three conflict cases; the control case passes.
5. **Run under invalidation semantics.** Zero violations. Show the auditor's view of record 100 after invalidation: metadata intact, commitment present, key destroyed, invalidation entry with month and legal ground, payload unreadable.
6. **State the limits before being asked.** Key destruction is simulated in program state; the invalidation entry is an attestation, not a proof; no National Contact Point is connected; no performance claim is made.

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
7. Article 68(12) governs "the data within the secure processing environment." Does that reach the access logs the environment generates, or only the dataset supplied under the permit?

### Trust and key custody

8. The invalidation entry attests that a key was destroyed; it does not prove it. Is attestation sufficient in your operating context, and if not, what would make it sufficient?
9. Where would key custody sit in your architecture, and what failure modes concern you most?
10. Does per-record key granularity create a single point of failure you would be unwilling to accept without hardware-backed attestation?

### Operational viability

11. What would implementing this at your institution actually require — systems, process, people?
12. At what record volume would the per-record key registry become a problem?
13. What would you change about the design before deploying it?

Question 7 is included because the thesis's sharpest result depends on the answer, and practitioner readings of it are evidence this author cannot generate.

---

## C.6 Closed-response questionnaire

Five-point Likert scale throughout: 1 = strongly disagree, 2 = disagree, 3 = neither agree nor disagree, 4 = agree, 5 = strongly agree. A sixth option, *not able to judge*, is offered on every item and is reported separately rather than treated as a midpoint.

Each dimension opens with the anchor statement proposed in supervisory feedback, reproduced verbatim, followed by items that decompose it.

### Dimension 1 — Perceived utility

| Item | Statement |
|---|---|
| U1 | *The key-invalidation mechanism effectively resolves the conflict between retention floors and erasure ceilings.* |
| U2 | The problem this mechanism addresses is one my institution will face in practice. |
| U3 | The mechanism addresses the problem more effectively than the approach my institution currently uses or would default to. |
| U4 | The distinction between plaintext verifiability and accountability-preserving verifiability is one I had not previously considered explicitly. |

### Dimension 2 — Regulatory alignment

| Item | Statement |
|---|---|
| R1 | *The residual audit log provides sufficient verification without violating GDPR Article 17 or EDPB guidelines.* |
| R2 | The surviving residue — metadata, commitment, invalidation entry — would be defensible to a supervisory authority. |
| R3 | Article 68(12) should be read as reaching the access logs generated within a Secure Processing Environment. |
| R4 | The mechanism's characterisation of its residue as pseudonymised rather than anonymous is the correct characterisation. |

### Dimension 3 — Operational viability

| Item | Statement |
|---|---|
| O1 | *The proposed key registry structure is practical to implement within current Norwegian health data infrastructure (SPUHiN / NORTRE).* |
| O2 | Per-record key granularity is operationally sustainable at the record volumes my institution handles. |
| O3 | The mechanism requires nothing of the processing environment beyond what the finalised national criteria already demand. |
| O4 | Placing the mechanism at the audit-logging boundary, rather than inside the processing environment, is the right architectural choice. |

### Dimension 4 — Audit integrity

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

A note on item A1. The anchor statement asserts that the mechanism gives auditors *full confidence*, which the thesis itself does not claim — Chapter 6, Section 6.3 states that the invalidation entry is an attestation rather than a proof. The item is retained verbatim because it was proposed as the anchor and because disagreement with it would be an accurate response rather than a failure of the instrument. Item A2 exists to capture that distinction directly, and analysis would read A1 and A2 together rather than A1 alone.

---

## C.7 Analysis

Closed responses would be reported as medians with full distributions rather than means, given ordinal data and a panel of eight; no inferential statistics would be computed, and none would be meaningful at this size. *Not able to judge* responses would be reported by item, since a concentration of them is itself a finding about which audiences can assess which dimensions.

Open responses and interview transcripts would be analysed thematically following a coding frame derived from the three areas supervisory feedback identified — legal defensibility, key custody and trust assumptions, operational feasibility: with an open category for themes not anticipated. Coding by a single researcher would be stated as a limitation, as it is for the literature review in Chapter 2, Section 2.1.7.

Integration into the thesis would follow the design science cycle rather than being appended to it:

**Misalignments** between the design and operational reality would be documented as findings, not smoothed over. If Secure Processing Environment operators identify key custody as a single point of failure absent hardware security modules, that becomes a stated limitation of the mechanism and a design requirement for the next iteration.

**Assumption revision.** Legal responses to items R2, R3 and R4, and to interview questions 4 through 7, would revise the trust model and the residue analysis of Chapter 4, Section 4.9: in particular whether attestation of key destruction is treated as adequate.

**Future iterations.** Responses to A2 would inform whether the next design iteration should move from software-attested key destruction to hardware-backed attestation through a hardware security module or secure enclave, which Chapter 7, Section 7.5 already identifies as the direction in which the assurance boundary would move.

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
