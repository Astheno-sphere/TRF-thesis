# P97 — Red team round 2, wave 4: the formal model.
# examiner M-1: C3 bound alpha for every secondary record, while Corollary 1.2's legal condition (the entry is
#   electronic health data) was never in the model. Add the reach predicate rho(a); granularity is the sufficient
#   case, not the only one; the run sets rho = 1 (broad reading). Abstract and Rival 3 aligned.
# examiner m-1: unstated assumptions (t_r >= t, delta >= 1, arithmetic with infinity); a record written at or after
#   its own deadline in Prop 2's construction; Prop 3's condition also holds for e(a) < t(a).
# examiner m-2: say what kind of result Proposition 4 is.
EDITS = [
 dict(id='P97-01', file='Chapter4_TRF_Model_v1.md',
  old=r"""*C3: Deletion ceiling.* For every record $a$ with $\sigma(a)$ = secondary and every month $t \ge t_\pi(a) + 6$:""",
  new=r"""*C3: Deletion ceiling.* Let $\rho(a) = 1$ where the ceiling reaches record $a$, that is, where its log entry is itself electronic health data within the environment, and $\rho(a) = 0$ otherwise. On the broad reading of Article 68(12) set out in Section 4.6, $\rho(a) = 1$ for entries kept at patient-record granularity, and for entries kept at dataset granularity only where the activity content they retain is itself data concerning health; on the narrow reading, $\rho(a) = 0$ for every access log. For every record $a$ with $\sigma(a)$ = secondary and $\rho(a) = 1$, and every month $t \ge t_\pi(a) + 6$:""",
  why="M-1: the legal condition of Corollary 1.2 enters the model as the reach predicate rho"),
 dict(id='P97-02', file='Chapter4_TRF_Model_v1.md',
  old=r"""It does so when the log entry is itself electronic health data within the environment, which, on the reading set out below, is the case for logs kept at patient-record granularity and not for logs kept at dataset granularity.""",
  new=r"""It does so when the log entry is itself electronic health data within the environment ($\rho(a) = 1$, Section 4.4), which, on the reading set out below, is the case for logs kept at patient-record granularity and, for logs kept at dataset granularity, only where the activity content they retain is itself data concerning health.""",
  why="M-1: granularity is sufficient, not necessary"),
 dict(id='P97-03', file='Chapter4_TRF_Model_v1.md',
  old=r"""a log kept at dataset granularity carries no subject fields and falls outside Article 68(12) on either reading,""",
  new=r"""a log kept at dataset granularity carries no subject fields and falls outside Article 68(12) on the narrow reading, and on the broad reading unless the activity content it retains is itself data concerning health,""",
  why="M-1: Rival 3 no longer says 'on either reading'"),
 dict(id='P97-04', file='Chapter4_TRF_Model_v1.md',
  old=r"""if no request arrives, $t_r(a) = \infty$.""",
  new=r"""if no request arrives, $t_r(a) = \infty$. A request concerns personal data already recorded, so $t_r(a) \ge t(a)$; the response period satisfies $\delta \ge 1$; and arithmetic is over $\mathbb{N} \cup \{\infty\}$ with $\infty + n = \infty$.""",
  why="m-1: assumptions the proofs use, now stated in §4.3"),
 dict(id='P97-05', file='Chapter4_TRF_Model_v1.md',
  old=r"""It must be shown that this trajectory satisfies all three constraints.""",
  new=r"""Where $t^{I}(a) \le t(a)$, a record written at or after its own deadline, the payload is never held readable: set $\alpha(a,t) = 0$ from $t(a)$ and append $\iota(a)$ at $t(a)$. C1 still holds, because Semantics II does not read $\alpha$.

It must be shown that this trajectory satisfies all three constraints.""",
  why="m-1: Prop 2 construction for a record written after its own deadline"),
 dict(id='P97-06', file='Chapter4_TRF_Model_v1.md',
  old=r"""The proposition corrects as well as formalises.""",
  new=r"""The condition $e(a) + L > t(a) + F$ holds equally where the anchor event precedes creation, $e(a) < t(a)$; a ceiling already passed at creation then makes the record infeasible from $t(a)$. The hypothesis $e(a) \ge t(a)$ restricts the statement to the cases this thesis treats, and the bounded check of Chapter 5, Section 5.5 uses the same restriction.

The proposition corrects as well as formalises.""",
  why="m-1: Prop 3 for e(a) < t(a)"),
 dict(id='P97-07', file='Chapter4_TRF_Model_v1.md',
  old=r"""Two consequences follow. Ending payload accessibility within the floor is necessary""",
  new=r"""Proposition 4 is stated over the model extended informally with the location and the controller of each record, which Section 4.3 does not represent. It is a legal argument given the form of a proposition so that its premise is explicit, and the artefact does not execute it.

Two consequences follow. Ending payload accessibility within the floor is necessary""",
  why="m-2: say what kind of result Proposition 4 is"),
 dict(id='P97-08', file='Chapter5_Demonstration_v1.md',
  old=r"""Each carries a permit expiry at a uniformly distributed one to twelve months after creation. Erasure requests arrive with probability 0.25.""",
  new=r"""Each carries a permit expiry at a uniformly distributed one to twelve months after creation. Erasure requests arrive with probability 0.25. Every such record is treated as reached by the ceiling ($\rho(a) = 1$), which models the broad reading of Article 68(12) (Chapter 4, Section 4.4).""",
  why="M-1: the run's reach assumption stated"),
 dict(id='P97-09', file='Front_Matter_v1.md',
  old=r"""The collision that needs no erasure request arises only on a contestable broad reading of Article 68(12), and only for logs kept at patient-record granularity.""",
  new=r"""The collision that needs no erasure request arises only on a contestable broad reading of Article 68(12), and only for log entries that are themselves electronic health data, as entries kept at patient-record granularity are.""",
  why="M-1: abstract states the condition the model now carries"),
 dict(id='P97-10', file='Front_Matter_v1.md',
  old=r"""Kollisjonen som ikke krever noen slettebegjæring, oppstår bare under en omstridt, vid lesing av artikkel 68(12), og bare for logger som føres på nivå med den enkelte pasientjournal.""",
  new=r"""Kollisjonen som ikke krever noen slettebegjæring, oppstår bare under en omstridt, vid lesing av artikkel 68(12), og bare for loggposter som selv er elektroniske helsedata, slik poster som føres på nivå med den enkelte pasientjournal, er.""",
  why="M-1: Sammendrag matches the abstract"),
]
