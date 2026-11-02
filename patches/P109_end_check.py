# P109 — end check (2 Nov): independent code audit, examiner red team (round 3) and novelty sweep, each finding
# verified against the code, the Official Journal or EUR-Lex before applying. Code-description accuracy (Ch5);
# Art 73(1)(e) one-year floor confined to access logs; residue never called non-identifiable outright; "minimal" /
# "weakest" withdrawn (Rival 4 is weaker); Corollary 1.1 month count; §1.3 floor attribution; §6.1/§6.10 hedges;
# App C question; abstract mechanism order. New law: EDPS v SRB (C-413/23 P) in §4.9; Implementing Regulation
# (EU) 2026/2083 Art 15(1)(f)(ii) in §2.3; FHI designated coordinating HDAB in §2.6.
LOST_OK = ["hedge presumptive", "number 65,536", "number 2", "number 11", "number 5"]
EDITS = [
 # ---- Chapter 5: what the code does
 dict(id='P109-01', file='Chapter5_Demonstration_v1.md',
  old=r"""The checker reports every month at which both are required at once.""",
  new=r"""For each record the checker reports, per conflicting constraint, the first month at which both are required at once; a violation is therefore a (record, constraint) pair, not a month.""", why="code audit A3: the checker breaks at the first colliding month"),
 dict(id='P109-02', file='Chapter5_Demonstration_v1.md',
  old=r"""Its value is that it is written separately and shares no code with the main checker, so it can catch an implementation error that the checker and its own tests would share.""",
  new=r"""Its value is that it is a separate function sharing only the constants $\delta$ and the ceiling with the main checker, and an automated test compares the two on every boundary month of a twelve-month window, so a boundary error in either shows up as a disagreement (Appendix A, A.2).""", why="code audit A2: it shared constants and was never compared; now compared by tests/test_props.py"),
 dict(id='P109-03', file='Chapter5_Demonstration_v1.md',
  old=r"""so unreadability is executed rather than asserted""",
  new=r"""so unreadability is exercised in code rather than only asserted""", why="code audit B: destruction attested, not proven"),
 dict(id='P109-04', file='Chapter5_Demonstration_v1.md',
  old=r"""The exhaustive cross-check of Section 5.5 covers 65,536 assignments in all.""",
  new=r"""The exhaustive cross-check of Section 5.5 searches a space of 65,536 assignments in all; it evaluates 65,535, because the control case stops at its first satisfying assignment.""", why="code audit A4"),
 dict(id='P109-05', file='Chapter5_Demonstration_v1.md',
  old=r"""The majority of invalidation events in this population arise from the regulation's own deletion ceiling rather than from data-subject action: which is consistent with Section 5.4 and reinforces the point that the tri-lateral problem is not reducible to a right-to-be-forgotten problem.""",
  new=r"""The split follows from the generator's parameters, every Secure Processing Environment record carrying a permit expiry while erasure requests are drawn by probability, and is not evidence about practice. What it does show is that the ceiling alone, without any data-subject action, triggers invalidation in the model, consistent with Section 5.4.""", why="red team B1: synthetic counts used as evidence"),
 # ---- residue never asserted non-identifiable
 dict(id='P109-06', file='Chapter4_TRF_Model_v1.md',
  old=r"""What remains is a non-identifiable residue, being the event type""",
  new=r"""What remains is a residue intended to be non-identifiable, subject to the isolation, linkage and inference test below, being the event type""", why="red team B2"),
 dict(id='P109-07', file='Chapter4_TRF_Model_v1.md',
  old=r"""leaving a non-identifiable statistical residue""",
  new=r"""leaving a statistical residue intended to be non-identifiable""", why="red team B2"),
 dict(id='P109-08', file='Chapter7_Conclusion_v1.md',
  old=r"""leaves a non-identifiable statistical residue""",
  new=r"""leaves a statistical residue intended to be non-identifiable""", why="red team B2"),
 # ---- "minimal" / "weakest" withdrawn
 dict(id='P109-09', file='Front_Matter_v1.md',
  old=r"""while Proposition 2 verifies that a minimal principled departure suffices.""",
  new=r"""while Proposition 2 verifies that a principled departure suffices.""", why="red team M4: Semantics II without the commitment is weaker and also feasible (Rival 4)"),
 dict(id='P109-10', file='Chapter4_TRF_Model_v1.md',
  old=r"""It is also the weakest departure from plaintext verifiability that achieves feasibility, preserving""",
  new=r"""It is a departure from plaintext verifiability that achieves feasibility while preserving""", why="red team M4"),
 # ---- Art 73(1)(e): one year binds access logs only
 dict(id='P109-11', file='Chapter4_TRF_Model_v1.md',
  old=r"""- $F(a) = 12$ for access and activity logs of Secure Processing Environments, this being the one-year minimum imposed by Article 73(1)(e)""",
  new=r"""- $F(a) = 12$ for access logs of Secure Processing Environments, this being the one-year minimum imposed by Article 73(1)(e); activity logs are kept "for the period necessary to verify and audit", which the model takes as at least the same year""", why="red team M3, verified against the OJ text quoted in §2.2"),
 dict(id='P109-12', file='Chapter6_Discussion_v1.md',
  old=r"""Article 73(1)(e) requires identifiable logs of access to and activity in a Secure Processing Environment to be kept for at least one year.""",
  new=r"""Article 73(1)(e) requires identifiable logs of access to and activity in a Secure Processing Environment to be kept for the period necessary to verify and audit, and logs of access for at least one year.""", why="red team M3"),
 dict(id='P109-13', file='Chapter6_Discussion_v1.md',
  old=r"""On either reading the mechanism meets both provisions,""",
  new=r"""On either reading the mechanism is designed to meet both provisions, subject to the questions of Chapter 7, Section 7.4,""", why="red team minor 4"),
 dict(id='P109-14', file='Chapter6_Discussion_v1.md',
  old=r"""The zero is the finding. Section 17 fixes""",
  new=r"""The zero is the finding, and Proposition 3(i) predicts it, since the three-year limit is longer than the one-year floor. Section 17 fixes""", why="red team minor 2"),
 # ---- Corollary 1.1 month count; §1.3 floor attribution
 dict(id='P109-15', file='Chapter4_TRF_Model_v1.md',
  old=r"""so in the first five years and eleven months of the pilot's six-year floor under the baseline response period.""",
  new=r"""so, under the baseline response period, a request in any of the 72 months from $t(a)$ to $t(a) + 71$ collides with the pilot's six-year floor.""", why="red team minor 1: the window is closed, so 72 request months collide"),
 dict(id='P109-16', file='Chapter1_Introduction_v2.md',
  old=r"""and the longer minimum national law sets for IHE ATNA audit repositories, reported as ten years and set at six for the Norwegian pilot)""",
  new=r"""and, for IHE ATNA audit repositories, a longer period the specifications leave to national law, reported as ten years in the literature and decided at six for the Norwegian pilot by Helsedirektoratet as controller)""", why="red team M2 / whipper 1"),
 dict(id='P109-17', file='Chapter1_Introduction_v2.md',
  old=r"""Chapter 4 proves the system infeasible under plaintext verifiability""",
  new=r"""Chapter 4 proves the system infeasible under plaintext verifiability whenever a deadline falls inside a retention window""", why="red team minor 8"),
 dict(id='P109-18', file='Chapter4_TRF_Model_v1.md',
  old=r"""In the present setting it takes two values:""",
  new=r"""In the present setting it takes one value per record class, with the cross-border value a parameter:""", why="red team minor 5"),
 # ---- Appendix C; abstract mechanism order
 dict(id='P109-19', file='Appendix_C_Evaluation_Instrument.md',
  old=r"""whether the surviving residue clears the anonymity threshold;""",
  new=r"""whether the surviving residue is personal data, and for whom;""", why="red team minor 7: §4.9 says it does not clear the threshold"),
 dict(id='P109-20', file='Front_Matter_v1.md',
  old=r"""Crypto-Erasure by Invalidation, destroys a per-record payload key and, for Secure""",
  new=r"""Crypto-Erasure by Invalidation, deletes each record's payload with its per-record key and, for Secure""", why="red team minor 6: since P94 the store deletes the payload; key destruction covers copies"),
 # ---- new law
 dict(id='P109-21', file='Chapter4_TRF_Model_v1.md',
  old=r"""(European Data Protection Board, 2026c). By that standard the residue, which keeps metadata identifying the access event, is best characterised as pseudonymised rather than anonymous until the terminal transition.""",
  new=r"""(European Data Protection Board, 2026c). The Court of Justice has since held that pseudonymised data are not personal data in all cases and for every person: for a recipient who cannot lift the pseudonymisation they may not be, while for the controller who holds the additional information they remain personal data (Court of Justice of the European Union, 2025, paras 73 and 76–77). The repository controller holds both the subject link and the accessor's identity, so for it the residue remains personal data. By that standard the residue, which keeps metadata identifying the access event and identifies the accessor, is best characterised as pseudonymised rather than anonymous until the terminal transition.""", why="novelty sweep: EDPS v SRB, verified on EUR-Lex (CELEX 62023CJ0413)"),
 dict(id='P109-22', file='Chapter4_TRF_Model_v1.md',
  old=r"""Crosby, S. A., & Wallach, D. S. (2009).""",
  new=r"""Court of Justice of the European Union. (2025). *European Data Protection Supervisor v Single Resolution Board* (Case C‑413/23 P, judgment of 4 September 2025). https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62023CJ0413

Crosby, S. A., & Wallach, D. S. (2009).""", why="reference"),
 dict(id='P109-23', file='Chapter2_LitReview_v2_FINAL.md',
  old=r"""the reply is reproduced, with permission, in Appendix D.""",
  new=r"""the reply is reproduced, with permission, in Appendix D. The implementing regulation on MyHealth@EU adopted since, Commission Implementing Regulation (EU) 2026/2083, which applies from 26 March 2027, requires the national contact points, as joint controllers, to log exchanges of personal data systematically, recording the actors involved, the categories of data and the purposes (Article 15(1)(f)(ii)); it too sets no period for keeping those logs (European Commission, 2026).""", why="novelty sweep: 2026/2083, read on EUR-Lex (OJ L 2026/2083, 21.9.2026)"),
 dict(id='P109-24', file='Chapter2_LitReview_v2_FINAL.md',
  old=r"""European Parliament and Council of the European Union. (2013).""",
  new=r"""European Commission. (2026). Commission Implementing Regulation (EU) 2026/2083 of 18 September 2026 on MyHealth@EU. *Official Journal of the European Union*, L 2026/2083. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202602083

European Parliament and Council of the European Union. (2013).""", why="reference"),
 dict(id='P109-26', file='Chapter2_LitReview_v2_FINAL.md',
  old=r"""Forskningsetikk. (2023).""",
  new=r"""Folkehelseinstituttet. (2026, October 19). *FHIs rolle og oppdrag i EHDS*. Norwegian Institute of Public Health. https://www.fhi.no/hd/det-europeiske-helsedataomradet/fhis-rolle-og-oppdrag-i-ehds/

Forskningsetikk. (2023).""", why="reference"),
 dict(id='P109-25', file='Chapter2_LitReview_v2_FINAL.md',
  old=r"""Helsedataservice is the national body through which access to health data for secondary use is decided, and is the presumptive Health Data Access Body for the purposes of the European Health Data Space. Formal designation has not yet occurred.""",
  new=r"""Helsedataservice is the national body through which access to health data for secondary use is decided. The Ministry of Health and Care Services has since designated Folkehelseinstituttet as Norway's national coordinating Health Data Access Body; how many access bodies Norway will have is not yet settled (Folkehelseinstituttet, 2026).""", why="novelty sweep: FHI page 19 Oct 2026, read"),
]
