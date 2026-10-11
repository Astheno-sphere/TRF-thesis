# P61 — Round 5 wave 2: Jo R5[14]. Proposition 4 rests on a legal premise, not the model. Take Joao's
# offered alternative to relabelling — state the premise as an explicit assumption inside the proposition
# (lower ripple than renaming to "Observation 4" across ~14 sites and the "four results" framing).
EDITS = [
 dict(id='P61-01', file='Chapter4_TRF_Model_v1.md',
   old=r"""> *Proposition 4 (location and right).* Let a ceiling be anchored to a location, requiring data to be absent from that location after a deadline, and let a right be anchored to the data subject, requiring data to be inaccessible to any controller holding them after a deadline. Under Semantics I, relocating a record before the ceiling's deadline satisfies the ceiling and the floor together, while the floor and the right remain infeasible for every record satisfying the first disjunct of Proposition 1.""",
   new=r"""> *Proposition 4 (location and right).* *This result depends on a legal premise stated here as an explicit assumption, not derived from the model: that a controller receiving a relocated record receives the erasure obligation of Article 17(1) GDPR with it.* Let a ceiling be anchored to a location, requiring data to be absent from that location after a deadline, and let a right be anchored to the data subject, requiring data to be inaccessible to any controller holding them after a deadline. Under Semantics I, and granting that assumption, relocating a record before the ceiling's deadline satisfies the ceiling and the floor together, while the floor and the right remain infeasible for every record satisfying the first disjunct of Proposition 1.""",
   why="Jo R5[14]: elevate the legal premise into the proposition statement as an explicit assumption"),
]
LOST_OK = []
