# P86 — red-team fix (breadth agent threats #1 rhetoric>math, #3 correlated checks; overclaims O1/O3).
# §6.1's summary sentence overstates what the thesis itself concedes: §4.7 calls the proofs elementary,
# and §5.5 calls the exhaustive search a scaled-down sanity check sharing the Chapter 4 encoding, not
# independent evidence. Align the summary with those concessions. Honesty fix; no result withdrawn.
EDITS = [
 dict(id='P86-01', file='Chapter6_Discussion_v1.md',
   old=r"""Chapter 4 proves both results; Chapter 5 witnesses them executably, and a separately written exhaustive search confirms that under the first semantics no assignment of payload accessibility whatsoever could succeed.""",
   new=r"""Chapter 4 establishes both results by arguments it concedes are elementary (Section 4.7); Chapter 5 witnesses them executably, and a separately written exhaustive search — a scaled-down sanity check on the implementation rather than independent evidence, since it shares the Chapter 4 encoding (Section 5.5) — finds no satisfying assignment of payload accessibility in the conflict cases under the first semantics.""",
   why="align §6.1 summary with the thesis's own concessions in §4.7 (proofs elementary) and §5.5 (search is a scaled sanity check sharing the encoding); removes the rhetoric-exceeds-substance overclaim"),
]
LOST_OK = []
