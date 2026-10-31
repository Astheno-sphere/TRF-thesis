# P93 — two new figures (NEXT_SESSION §G "diagrams"; red-team orientation for the reader of Ch1).
# Figure 1.1: whole-system map, Archify architecture (.archify/architecture-system-map-20261031-020000),
#   all four Archify gates passed; content drawn only from Chapter 4, Section 4.11.
# Figure 5.2: record 100 month by month, drawn by the viewer's own ui.life_strip() from the
#   checker's quantities (t_a=7, floor to 19, t_pi=10, ceiling from 16; detail line of §5.4).
EDITS = [
 dict(id='P93-01', file='Chapter1_Introduction_v2.md',
   old=r"""The collision is therefore not yet operative, and the window in which its resolution could be specified rather than improvised closes with those implementing acts.""",
   new=r"""The collision is therefore not yet operative, and the window in which its resolution could be specified rather than improvised closes with those implementing acts.

Figure 1.1 places both audit logs in the infrastructure, with the point at which the mechanism of Chapter 4 attaches to each.

![Figure 1.1. The two audit logs this thesis concerns and where the mechanism attaches. In primary use, each National Contact Point writes an audit record of the cross-border exchange to its own audit repository. In secondary use, a Secure Processing Environment operating under a data permit writes an access log, bound by the one-year floor of Article 73(1)(e) and, on the broad reading, the ceiling of Article 68(12). Crypto-Erasure by Invalidation (Figure 4.1) attaches at both logs, takes erasure requests from the data subject and each permit's expiry from the health data access body, and gives auditors inclusion proofs. Placement as specified in Chapter 4, Section 4.11.](figures/fig1_1_system_map.png){width=6.3in}""",
   why="Figure 1.1: whole-system map so the reader sees both logs and the attachment points before the argument"),
 dict(id='P93-02', file='Chapter5_Demonstration_v1.md',
   old=r"""Moving the logs out of the environment at permit closure would also remove these thirty-nine collisions, at the cost set out in Chapter 4, Section 4.10; it would not remove the erasure-driven ones.""",
   new=r"""Moving the logs out of the environment at permit closure would also remove these thirty-nine collisions, at the cost set out in Chapter 4, Section 4.10; it would not remove the erasure-driven ones.

![Figure 5.2. Record 100, month by month. The access log is created in month seven under a one-year floor, which runs to month nineteen; the permit expires in month ten, so the ceiling of Article 68(12) applies from month sixteen. No erasure request is made. Under Semantics I the floor requires the payload readable and the ceiling requires it gone in months sixteen to nineteen, the contradiction of Proposition 1. Under Semantics II the payload key is destroyed in month sixteen, the invalidation entry is logged, and the record stays verifiable to the end of the floor, the trajectory of Proposition 2. Drawn by the artefact's viewer from the checker's own quantities; the vertical line marks month sixteen.](figures/fig5_2_record_100_life_strip.png){width=6.3in}""",
   why="Figure 5.2: the Corollary 1.2 witness drawn, so Propositions 1 and 2 can be seen on one record"),
]
