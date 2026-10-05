# P56 — independent audit of 5 Oct (after P55): accuracy fixes to P53–P55 material and older slips.
C1='Chapter1_Introduction_v2.md'; C2='Chapter2_LitReview_v2_FINAL.md'; C4='Chapter4_TRF_Model_v1.md'
C5='Chapter5_Demonstration_v1.md'; C6='Chapter6_Discussion_v1.md'; CA='code_artefacts/README_Appendix_A.md'
E=[]
def e(i,f,o,n,w,count=1): E.append(dict(id=f'P56-{i:02d}',file=f,old=o,new=n,why=w,count=count))
e(1,C4,"A patient asks for her data to be erased. The audit record of who looked at them must, on the reported deployment baseline, stay verifiable for ten years. In a research environment a third rule wants the data gone six months after the permit ends. Can one record obey all three?",
 "A patient asks for her data to be erased. The audit record of who looked at them must stay verifiable for years: ten, on the reported cross-border baseline; one, in a research environment, where a third rule wants health data gone six months after the permit ends. Can an audit record obey all three?",
 'audit 2: no single record carries the ten-year floor and the ceiling')
e(2,C4,"The model is deliberately small: one record, one clock, and one question asked every month: can the payload still be read?",
 "The model is deliberately small: one record, one clock, and one main question asked every month. Can the payload still be read?",'audit 20')
e(3,C4,"Change what verifiable means and the contradiction disappears, for every record, every pattern of requests and every floor.",
 "Change what verifiable means and, in the model as formalised, the contradiction disappears for every record, every pattern of requests and every floor.",'audit 21')
e(4,C4,"nor that key destruction can be verified by an external party, which Section 4.10 concedes it cannot",
 "nor that key destruction can be verified by an external party, which Section 4.9 and Chapter 6, Section 6.3 concede it cannot",'audit 9')
e(5,C4,"it is defensible under the erasure test the European Data Protection Board has articulated provided the threat model is documented",
 "it is defensible under the erasure test the European Data Protection Board has articulated and, on Aikebaier's (2026) reading, provided the threat model is documented",'audit 10')
e(6,C4,"The November 2024 draft is specific on logging. It makes tamper-proof, identifiable logs of access to the environment mandatory \"for at least one year\" (P13), and likewise logs of when files are extracted and by whom, kept for one year (P24); it recommends tamper-proof, identifiable logs of activities inside the environment (P14); and it lists back-up and log files among the matters a termination procedure must cover (P31) (SPUHiN, 2024; requirement numbers as in the draft).",
 "The November 2024 draft is specific on logging (SPUHiN, 2024; requirement numbers as in the draft). Tamper-proof, identifiable logs of access to the environment are mandatory \"for at least one year\" (P13). Logs of when files are extracted and by whom are mandatory, kept for one year (P24). Logs of activities inside the environment are recommended (P14). A defined termination procedure is mandatory (P31), and its implementation examples include the handling of back-ups and log files.",'audit 6, 18')
e(7,C4,"| Tamper-proof, identifiable logs of access to the SPE, at least one year (mandatory); of file extraction, one year (mandatory); of activities (recommended) | SPUHiN (2024), draft, P13, P24, P14 | Accessor fields kept identifiable for the floor; every access event in the append-only Merkle log | §4.3, §4.8; `MerkleLog` | Met in the artefact ($F = 12$; both tamper tests fail $V^{II}$) |",
 "| Tamper-proof, identifiable logs of access to the SPE, at least one year (mandatory); of file extraction, one year (mandatory); of activities (recommended) | SPUHiN (2024), draft, P13, P24, P14 | Accessor fields kept identifiable for the floor; every access event in the append-only Merkle log | §4.3, §4.8; `MerkleLog` | Access logs met in the artefact ($F = 12$; both tamper tests fail $V^{II}$); extraction and activity logs covered by the same mechanism, not modelled separately |",'audit 7')
e(8,C4,"| Termination procedure covering deletion of files, back-ups and log files (mandatory) | SPUHiN (2024), draft, P31 |",
 "| Defined termination procedure (mandatory); implementation examples include back-ups and log files | SPUHiN (2024), draft, P31 |",'audit 6')
e(9,C4,"Commit($p(a), r(a)$)","$\\mathrm{Commit}(p(a), r(a))$",'audit 19',count=2)
e(10,C4,"with the convention min($\\infty, \\infty) = \\infty$.","with the convention $\\min(\\infty, \\infty) = \\infty$.",'audit 19')
e(11,C4,"Figure 4.1. Crypto-Erasure by Invalidation at the audit boundary. Solid arrows are writes at access time; red dashed arrows are the invalidation at the earlier of the erasure deadline and the deletion ceiling.",
 "Figure 4.1. Crypto-Erasure by Invalidation at the audit boundary. Green arrows are writes at access time; purple dashed arrows are the two triggers; red dashed arrows are the destruction at the earlier of the erasure deadline and the deletion ceiling, which the invalidation entry then records in the registry and the log. The subject fields are removed only for patient-level Secure Processing Environment logs, at the ceiling.",'audit 11, 16')
e(12,C5,"single Python module of 533 lines","single Python module of 534 lines",'audit 4')
e(13,C5,"of which 413 are non-blank, non-comment lines","of which 414 are non-blank, non-comment lines",'audit 4')
e(14,C5,"| `trf_checker.py` | 533 |","| `trf_checker.py` | 534 |",'audit 4')
e(15,CA,"Line count: 533.","Line count: 534.",'audit 4')
e(16,C5,"Four further modules accompany it","Six further modules accompany it",'audit 3')
e(17,C5,"the optional envelope-encryption module below is the only component that imports one","the optional envelope-encryption module below is the only component that imports a cryptographic library",'audit 22')
e(18,C2,"Proposition 3 (Chapter 4, Section 4.6) states the condition in that idiom: when the expiry clock starts at a different event from the holding clock",
 "Proposition 3 (Chapter 4, Section 4.6) can be read in that idiom: when the expiry period is no longer than the holding period and its clock starts at a different event from the holding clock",'audit 14')
e(19,C2,"keeps a customer's personal data for \"ytterligere 3 år og 41 dager\" after both the supply and the grid contract end, \"for eventuell feilretting og mulighet for å korrigere økonomiske oppgjør\", and keeps metering values for ten years only where the customer asks (Elhub, 2026). That is a retention period per data category, anchored to an event, with an extension the data subject controls: the parameters of the model in Chapter 4, Section 4.3, in a different sector.",
 "keeps a customer's personal data for a further three years and 41 days after both the supply and the grid contract end, \"for eventuell feilretting og mulighet for å korrigere økonomiske oppgjør\" [for any correction of errors and to allow financial settlements to be corrected], and keeps metering values for ten years only where the customer asks (Elhub, 2026). That is a retention period per data category, anchored to an event: the form of the floor parameter in Chapter 4, Section 4.3, in a different sector. The extension the data subject controls has no counterpart in the model.",'audit 5, 8')
e(20,C2,"Elhub. (2026). *Elhubs personvernerklæring* [Privacy statement;","Elhub. (2026). *Elhubs personvernerklæring* [Elhub's privacy statement;",'audit 5')
e(21,C2,"Inspection of the checklists in the hearing version shows their scope to be information-security management, identity assurance, and access governance.",
 "Inspection of the checklists in the hearing version shows their scope to be information-security management, identity assurance, and access governance, with identifiable access logs kept for at least one year (P13 and P24 in the 2024 draft; Chapter 4, Section 4.11).",'audit 12')
e(22,C6,"The compliance checklists, in the hearing version inspected, address information-security management, identity assurance, and access governance.",
 "The compliance checklists, in the hearing version inspected, address information-security management, identity assurance, and access governance, and the 2024 draft makes identifiable access logs mandatory for at least one year (Chapter 4, Section 4.11).",'audit 12')
e(23,C6,"The provisions that create this collision do not yet apply, and that is the opportunity.",
 "The EHDS provisions that create the collision in Secure Processing Environments do not apply until 26 March 2029, and that is the opportunity.",'audit 13')
e(24,C6,"The collision this thesis characterises is therefore not yet operative,",
 "The collision in Secure Processing Environments is therefore not yet operative,",'audit 13')
EDITS=E
LOST_OK=["number 4.10","number 533","number 413","number 3","hedge not yet"]  # wrong cross-ref, corrected line counts, the Norwegian "3 år" now in English, hook now dated
