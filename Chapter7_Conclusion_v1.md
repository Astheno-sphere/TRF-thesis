# Chapter 7. Conclusion

---

## 7.1 The Problem and the Answer

This thesis began from a conflict that the European Health Data Space Regulation does not resolve. Cross-border health data exchange generates audit records subject to retention floors: ten years under the eHDSI deployment baseline for MyHealth@EU audit repositories, one year under Article 73(1)(e) for the access logs of Secure Processing Environments. The same records are subject to the erasure right of Article 17 GDPR, exercisable at any moment within those windows, and to the deletion ceiling of Article 68(12) EHDS, which requires data to be gone from a Secure Processing Environment within six months of permit expiry. No instrument reconciles them, no guidance addresses their interaction, and the technical specifications that will have to handle them are not due until 26 March 2027.

The thesis answered the question in three movements.

It formalised the conflict as the Tri-Lateral Retention Feasibility Model, a constraint-satisfaction problem over a single binary variable per record: the accessibility of its personal-data payload. The model has three constraint types, being a parameterised retention floor, an erasure deadline, and a deletion ceiling, and it makes the semantics of *verifiability* an explicit parameter rather than an unexamined assumption.

It proved two results within that model. Under plaintext-verifiability semantics, in which a record is verifiable while its payload remains readable, the constraint system is infeasible whenever an erasure deadline or a ceiling deadline falls inside a retention window. Under accountability-preserving semantics, in which a record is verifiable while its metadata is intact, its commitment survives, and any loss of payload accessibility is itself logged and attributed, the system is jointly satisfiable for every arrival pattern of erasure requests and permit expiries and for every floor parameter.

It specified the mechanism that the second proof exhibits. Crypto-Erasure by Invalidation retains event metadata and a hiding commitment, and destroys the per-record payload key at the earlier of the erasure deadline and the deletion ceiling. It appends the invalidation to the audit trail as a first-class event carrying its month, legal ground, and authorising actor. At floor expiry it performs a terminal transition that destroys the identifying metadata and leaves a non-identifiable statistical residue.

The answer to the research question is therefore that the three regimes can be reconciled, that the reconciliation requires no amendment to any instrument, and that what it requires instead is abandoning an assumption about audit records that no instrument states and that predates the right to erasure.

## 7.2 Contributions

Four contributions are claimed, each bounded.

*A formal characterisation of the tri-lateral retention conflict.* The general method of treating legal compliance as a satisfiability problem is established (Feng, Marsso, Sabetzadeh, & Chechik, 2022) and is not claimed here. What is new is its application to a retention system combining floors, a subject-triggered right, and a ceiling, and the isolation of verifiability semantics as the parameter that determines feasibility. The most recent systematisation of the cryptographic-erasure literature, an unreviewed preprint cited here as corroboration rather than authority, names erasure under multi-regime retention conflict among five open problems for the field (Aikebaier, 2026); this thesis addresses that problem in one regulatory setting.

*Two feasibility results with an executable witness.* Theorem 1 establishes infeasibility under the status-quo semantics; Theorem 2 establishes satisfiability under the alternative and exhibits the trajectory that achieves it. Both were demonstrated over two hundred records, producing ninety infeasible records and ninety-five violations under the first semantics and none under the second, with an separately written exhaustive search confirming that under the first semantics no assignment of payload accessibility whatsoever succeeds. The proofs are informal and the demonstration covers generated instances; neither is presented as more.

*A mechanism specification with its residue analysed.* The mechanism applies established primitives (cryptographic erasure as recognised in NIST SP 800-88 Revision 2, hiding commitments, and, without implementing them, dynamic accumulators) and claims no cryptographic novelty. What it adds to the practitioner crypto-shredding pattern is verifiability: an auditor can establish what was invalidated, when, on what ground, and by whom. The residue it leaves is characterised honestly as pseudonymised rather than anonymous by the Norwegian threshold, and designed to the corridor that the European Data Protection Board's finalised Guidelines 02/2025 establish.

*An integration analysis against verified Norwegian infrastructure.* The mechanism is placed at the two narrowest points at which it achieves its purpose: the audit-repository step of the MyHealth@EU transmission flow, and the access-logging boundary of a Secure Processing Environment. It requires of the substrate nothing that the finalised national criteria do not already demand. That constraint was derived from the documented fragmentation of Norwegian practice rather than assumed.

## 7.3 What the Thesis Does Not Establish

The limitations bounding this contribution are stated canonically in Chapter 3, Section 3.7, and engaged where they bite. They are the informal proof standard, the single-seed demonstration, the simulation of key destruction, the US Core profiles of the synthetic cohort, the unquantified operational cost of per-record key management, and the absence of regulatory authority behind two interpretive steps. They are not restated here, because each was priced into the claim before the claim was made and a conclusion that re-enumerates them adds length rather than candour.

Two deserve a final word because they bound the contribution rather than merely qualifying it. The invalidation entry is an attested record of destruction and not a proof of one, and no approach operating above the storage medium can supply the latter (Reardon, Basin, & Capkun, 2013). And the two interpretive steps are the subject of the next section, which is the honest statement of where this thesis is weakest.

## 7.4 The Two Open Questions of Authority

Both questions are legal rather than technical, and neither can be settled by better modelling.

The first concerns verifiability. No regulator or court has held that an audit record whose payload has been cryptographically invalidated continues to satisfy a retention obligation. The thesis argues that it does, from the necessity boundary of Article 17(3)(b) read with the data-minimisation principle of Article 5(1)(c), and from the Norwegian Data Protection Authority's own framing of retention as a balancing duty on the controller. If a supervisory authority instead reads "identifiable logs" in Article 73(1)(e) as requiring logs whose subject matter remains readable, Theorem 2 remains true of the model and inert in practice.

The second concerns scope. Article 68(12) governs *the data within the secure processing environment*. The thesis reads that as reaching the identifiable access logs the environment generates, on the grounds that the provision is framed by location rather than provenance and that the Regulation uses the narrower "made available under the data permit" formulation elsewhere when it means it. The competing construction, supported by the provision's placement within the data-permit article, confines it to the permitted dataset. Chapter 4, Section 4.6 shows that Corollary 1.2 stands or falls with this question and that nothing else in the thesis does.

Both questions are decidable by asking, and asking is the single highest-value action available to this research programme. A request to the competent authorities (Datatilsynet on the GDPR side; Helsedirektoratet, the Ministry of Health and Care Services or the Commission on the EHDS side) on whether accountability-preserving verifiability discharges a retention obligation, and whether Article 68(12) reaches access logs, has a determinate answer. A favourable answer converts the thesis's central interpretive moves from argument into authority. An unfavourable answer refutes them cleanly and identifies precisely what would have to change. Either outcome is worth more than the present uncertainty, and neither requires further modelling to obtain.

## 7.5 Future Work

Four lines follow, the first immediate and the remainder in ascending order of difficulty.

*Execution of the expert evaluation.* The instrument specified in Appendix C is designed and ready to execute. It comprises an eight-person panel across data protection, health IT architecture, Secure Processing Environment operation, and information logistics; a live demonstration of the artefact; a semi-structured guide; and a sixteen-item closed-response questionnaire across utility, regulatory alignment, operational viability, and audit integrity. It requires notification to Sikt and a lead time of four to six weeks, and it would supply exactly the evidence this thesis cannot generate analytically: practitioner readings of the Article 68(12) scope question, operator judgements on whether attested key destruction is sufficient in their context, and architectural assessment of the boundary placement. Together with the two authority questions of Section 7.4, this is the shortest route from the present contribution to a validated one.

*Selective disclosure of invalidation completeness.* The mechanism creates a problem it does not solve. When a data subject exercises Article 17, every record relating to them is invalidated, and an auditor should be able to confirm that *all* of them were. But identifying which records those are reveals the subject's cross-border care history, which is precisely what the erasure was meant to protect. Proving completeness of invalidation without revealing the invalidated set is a zero-knowledge problem, and it corresponds to the fourth of the five open problems identified by Aikebaier (2026), composition with zero-knowledge selective disclosure. This is where succinct arguments become necessary rather than decorative. The project name carried by this work originates in an earlier design that assumed zero-knowledge machinery would enforce the retention conflict; the analysis showed it unnecessary there, and shows it unavoidable here.

*Public verifiability of deletion certificates.* The boundary identified in Chapter 6, Section 6.3 would move if a deletion could be proven rather than attested. Proof-of-secure-erasure protocols pursue this in the classical setting under relaxed isolation assumptions (Bursuc, Gil-Pons, Mauw, & Trujillo-Rasua, 2024), and quantum encryption with certified deletion produces a certificate whose public verifiability its authors identify as open (Broadbent & Islam, 2020). Were public verifiability achieved, the invalidation entry specified here could carry a proof in place of an attestation, and the mechanism's guarantee would strengthen from conditional to demonstrable with no change to the model.

*Generalisation beyond health data.* The structure the model captures (one or more retention floors, a subject-triggered erasure right, and a deletion ceiling) is not obviously specific to health. Whether other regulated sectors present genuine tri-lateral instances, as distinct from the bi-lateral floor-against-right conflicts documented in financial record-keeping, is a question this thesis has flagged rather than investigated. Establishing that the formulation transfers, or that it does not, would determine whether the contribution is a result about one regulation or a method for a class of them.

## 7.6 Closing

The European Health Data Space is being built now. Norway's National Contact Point is in live pilot at two emergency clinics, with the cross-border audit stream barely begun. The implementing acts that will specify how Secure Processing Environments handle their records are due in March 2027, and the secondary-use provisions they will operationalise apply from March 2029. The Norwegian national criteria, finalised after public hearing, govern how such environments are secured and who may enter them, while saying nothing about what happens when the retention regimes on their records collide.

This thesis does not claim to have found something no one could have seen. The provisions it sets against each other are public, short, and adjacent in the same chapter of the same regulation. What it claims is to have set them against each other formally, and to have shown that the resulting impossibility follows from an assumption rather than from the obligations. It claims to have exhibited and demonstrated the mechanism that dissolves it. And it claims to have done all of that while the specifications are still being written, rather than after infrastructure has hardened around the problem.

The contribution is small, bounded, and checkable. Every number in it was produced by code that runs in under a twentieth of a second and that any reader can execute. Every limitation was stated before it was found. The two places where the argument outruns its authority are named rather than concealed, and the means of settling them is a letter rather than a research programme.

That is the thesis. What remains is to ask the questions it cannot answer itself.

---

## References (Chapter 7)

Aikebaier, Y. (2026). *SoK: Cryptographic erasure on public ledgers: Application-layer architectures, key-lifecycle adversaries, and GDPR Art. 17 equivalence* (Cryptology ePrint Archive, Paper 2026/1109). https://eprint.iacr.org/2026/1109 [Preprint; not peer-reviewed]

Broadbent, A., & Islam, R. (2020). Quantum encryption with certified deletion. In *Theory of Cryptography (TCC 2020)* (LNCS 12552, pp. 92–122). Springer. https://doi.org/10.1007/978-3-030-64381-2_4

Bursuc, S., Gil-Pons, R., Mauw, S., & Trujillo-Rasua, R. (2024). Software-based memory erasure with relaxed isolation requirements. In *2024 IEEE 37th Computer Security Foundations Symposium (CSF)*. IEEE. https://doi.org/10.48550/arXiv.2401.06626

Feng, N., Marsso, L., Sabetzadeh, M., & Chechik, M. (2022). *Bounded satisfiability checking of metric first-order temporal logic*. arXiv. https://doi.org/10.48550/arXiv.2209.04052

National Institute of Standards and Technology. (2025). *Special Publication 800-88 Revision 2: Guidelines for media sanitization* (R. Chandramouli & E. Hibbard). NIST. https://doi.org/10.6028/NIST.SP.800-88r2

Reardon, J., Basin, D., & Capkun, S. (2013). SoK: Secure data deletion. In *2013 IEEE Symposium on Security and Privacy* (pp. 301–315). IEEE. https://doi.org/10.1109/SP.2013.28
