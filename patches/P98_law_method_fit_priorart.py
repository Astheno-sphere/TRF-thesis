# P98 — Red team round 2, wave 5: law, method, programme fit, prior art. All new sources verified 31 Oct:
#   Arfelt, Basin & Debois (2019) ESORICS, LNCS pp. 681-699, doi 10.1007/978-3-030-29959-0_33 (MFOTL + MonPoly; Art 17(1)
#     deletion within 30 days; single obligations checked against logs, no joint satisfiability) — full text read.
#   Perlman (2005) J. Information Systems Security 1(1) 51-68 (ephemerizer destroys keys at expiry).
#   Geambasu, Kohno, Levy & Levy (2009) USENIX Security (Vanish, self-destructing data).
#   Venable, Pries-Heje & Baskerville (2016) EJIS 25(1) 77-89, doi 10.1057/ejis.2014.36 (FEDS).
#   TEHDAS2 D7.4 printed p. 39: termination "while allowing for exceptions mandated by applicable law" (from the PDF).
# examiner M-10 harmonising reading; M-11 falsifiability + FEDS; M-9 energy transfer + §7.5; M-8 prior art.
EDITS = [
 dict(id='P98-01', file='Chapter4_TRF_Model_v1.md',
  old=r"""This thesis states Corollary 1.2 conditionally""",
  new=r"""A third, harmonising reading is also available. On it, Article 68(12) reaches the logs but yields to the specific retention duty of Article 73(1)(e) as an exception mandated by law; the Joint Action's specification points this way when it requires termination procedures that allow "for exceptions mandated by applicable law" (TEHDAS2, 2026b, p. 39). On that reading Corollary 1.2's contradiction does not arise, because the ceiling yields to the floor for whatever the floor requires. The question then becomes what the floor requires. If it is plaintext verifiability, the subject's health data stay in the environment for the whole floor despite Article 68(12) and the minimisation principle; if it is accountability, only the accessor fields stay, and the subject fields and the payload still go at the ceiling, which is the partition Proposition 2 applies. The harmonising reading therefore removes the contradiction without removing the question, and moves it to the necessity analysis of Section 4.2, where this thesis places the weight.

This thesis states Corollary 1.2 conditionally""",
  why="M-10: the harmonising reading stated, and where it leaves the argument"),
 dict(id='P98-02', file='Chapter4_TRF_Model_v1.md',
  old=r"""It fails additionally and decisively in the Secure Processing Environment case, where Article 68(12) admits no exemption parallel to Article 17(3)(b), so that Corollary 1.2's infeasibility survives the argument entirely.""",
  new=r"""It fails additionally in the Secure Processing Environment case, where Article 68(12) admits no exemption parallel to Article 17(3)(b), so that on the broad and unharmonised reading Corollary 1.2's infeasibility survives the argument entirely (Section 4.6).""",
  why="M-10: Rival 1 no longer says 'decisively'"),
 dict(id='P98-03', file='Chapter3_Methodology_v1.md',
  old=r"""First, the design becomes falsifiable in a way that an asserted architecture is not.""",
  new=r"""First, the infeasibility claim becomes falsifiable in a way that an asserted architecture is not, and the feasibility claim, being constructive, is verified rather than tested (Chapter 4, Section 4.7).""",
  why="M-11: §3.3 no longer says a by-construction result is falsifiable"),
 dict(id='P98-04', file='Chapter6_Discussion_v1.md',
  old=r"""and those are different questions that analytical evaluation cannot answer.""",
  new=r"""and those are different questions that analytical evaluation cannot answer. In the terms of Venable, Pries-Heje and Baskerville's (2016) framework for evaluation in design science research, the evaluation reported here is artificial rather than naturalistic: it tests the design against a formal model, an infrastructure analysis and generated data, not in use. Utility, efficacy in operation and acceptance by those who would run the mechanism are therefore not evaluated, and naturalistic evaluation is the purpose of the instrument described next.""",
  why="M-11: classify the evaluation; name what is unevaluated"),
 dict(id='P98-05', file='Chapter2_LitReview_v2_FINAL.md',
  old=r"""so the TRF Model transfers to energy-sector data-retention conflicts without modification — the application in which this programme's logistics-of-information framing is most directly its own.""",
  new=r"""so the floor-against-right part of the TRF Model applies there directly. Whether a ceiling collision also arises, whether some deletion duty no longer than a floor is anchored to a different event, is the test of Proposition 3, which this thesis has not run for the energy sector; it is the application in which this programme's logistics-of-information framing is most directly its own.""",
  why="M-9: no untested 'without modification' transfer claim"),
 dict(id='P98-06', file='Chapter7_Conclusion_v1.md',
  old=r"""Applying it across regulated sectors, financial record-keeping first,""",
  new=r"""Applying it across regulated sectors, the Norwegian energy data hub first and financial record-keeping next,""",
  why="M-9: the programme-native application first"),
 dict(id='P98-07', file='Chapter2_LitReview_v2_FINAL.md',
  old=r"""But it defines the boundary of any crypto-erasure guarantee: the mechanism's properties are conditional on honest and verifiable key-lifecycle management, a condition examined further in Chapter 6.""",
  new=r"""But it defines the boundary of any crypto-erasure guarantee: the mechanism's properties are conditional on honest and verifiable key-lifecycle management, a condition examined further in Chapter 6. Deadline- and policy-driven key destruction has its own lineage. The Ephemerizer destroys each key at its data's expiry, so that data which expired before a later compromise stay unrecoverable (Perlman, 2005); Vanish makes data self-destruct after a set time by holding shares of the key in a distributed hash table, where they expire (Geambasu, Kohno, Levy, & Levy, 2009); and policy-based secure deletion destroys key components so that every item matching a deletion policy becomes unreadable at once (Cachin, Haralambiev, Hsiao, & Sorniotti, 2013). Each meets a deletion deadline by destroying keys. None treats a retention floor that must be honoured alongside the deadline, and none specifies what an auditor can still verify once the key is gone.""",
  why="M-8: deadline/policy-driven key destruction prior art placed"),
 dict(id='P98-08', file='Chapter2_LitReview_v2_FINAL.md',
  old=r"""A formulation that isolates that question is more defensible, more communicable, and more faithful to the logistics-modelling identity of the thesis than a fully general temporal-logic encoding.""",
  new=r"""A formulation that isolates that question is more defensible, more communicable, and more faithful to the logistics-modelling identity of the thesis than a fully general temporal-logic encoding. The closest work on the GDPR itself is Arfelt, Basin and Debois (2019), who formalise the monitorable GDPR obligations in the same logic and check them against system logs with the MonPoly tool; their formula for Article 17(1) requires deletion within thirty days of a request. Like Feng et al., they check single obligations against what a system did. Neither asks whether a floor, a right and a ceiling can be met together, which is the question of this thesis.""",
  why="M-8: formal GDPR monitoring prior art placed"),
 dict(id='P98-09', file='Chapter2_LitReview_v2_FINAL.md',
  old=r"""Albalwy, F.""",
  new=r"""Arfelt, E., Basin, D., & Debois, S. (2019). Monitoring the GDPR. In *Computer Security – ESORICS 2019* (Lecture Notes in Computer Science, pp. 681–699). Springer. https://doi.org/10.1007/978-3-030-29959-0_33

Cachin, C., Haralambiev, K., Hsiao, H.-C., & Sorniotti, A. (2013). Policy-based secure deletion. In *Proceedings of the 2013 ACM SIGSAC Conference on Computer and Communications Security (CCS '13)* (pp. 259–270). ACM. https://eprint.iacr.org/2013/152

Geambasu, R., Kohno, T., Levy, A. A., & Levy, H. M. (2009). Vanish: Increasing data privacy with self-destructing data. In *Proceedings of the 18th USENIX Security Symposium*. USENIX Association. https://www.usenix.org/conference/usenixsecurity09/technical-sessions/presentation/vanish-increasing-data-privacy-self

Perlman, R. (2005). The Ephemerizer: Making data disappear. *Journal of Information Systems Security*, *1*(1), 51–68. https://jissec.org/Contents/V1/N1/V1N1-Perlman.html

Albalwy, F.""",
  why="M-8: reference entries, each verified"),
 dict(id='P98-10', file='Chapter6_Discussion_v1.md',
  old=r"""Aikebaier, Y.""",
  new=r"""Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A framework for evaluation in design science research. *European Journal of Information Systems*, *25*(1), 77–89. https://doi.org/10.1057/ejis.2014.36

Aikebaier, Y.""",
  why="M-11: reference entry, verified"),
]
