# P15 — M4b (anchoring result promoted into Ch4 as Proposition 3) and M4a (weight moved to the
# necessity analysis and Propositions 3 and 4). Theorem names are renamed in P16; this patch writes
# the new material with the new names and leaves existing "Theorem" words for P16.
# Formal check of 3 Oct: for a ceiling of L months anchored at e(a) >= t(a), Semantics I floor and
# ceiling collide for record a iff e(a) + L <= t(a) + F. Collision therefore needs L <= F under ANY
# anchor; §6.9a's "structural rather than numerical" overstated it. What the anchor decides is
# whether the collision is visible in the text (same anchor) or record-dependent (external anchor).
C4, C6 = "Chapter4_TRF_Model_v1.md", "Chapter6_Discussion_v1.md"
PROP3 = r"""*Where the ceiling is anchored.* Corollary 1.2 and the cross-sector instance of Chapter 6, Section 6.9a are both cases of one condition, stated here because it is the structural content of the problem rather than a property of either instrument.

> *Proposition 3 (anchoring).* Let a record's floor of $F$ months run from its creation month $t(a)$, and let a ceiling of $L$ months run from an event at month $e(a) \ge t(a)$. Under Semantics I, the floor and the ceiling are jointly satisfiable for $a$ if and only if $e(a) + L > t(a) + F$. Hence (i) if the ceiling is anchored to the same event as the floor, $e(a) = t(a)$, they are satisfiable for every record if and only if $L > F$, a condition decidable from the text alone; and (ii) if the ceiling is anchored to an external event, then whenever $L \le F$ they fail for exactly those records with $e(a) - t(a) \le F - L$, a set that the text does not reveal and each record's history determines.

*Proof.* C1 under Semantics I requires $\alpha(a,t) = 1$ for every month $t$ up to $t(a) + F$; the ceiling requires $\alpha(a,t) = 0$ for every $t \ge e(a) + L$. Since $e(a) + L \ge t(a)$, some month of the window carries both demands if and only if $e(a) + L \le t(a) + F$. Cases (i) and (ii) substitute $e(a) = t(a)$ and rearrange. ∎

The proposition corrects as well as formalises. A collision needs a ceiling no longer than the floor whichever way it is anchored; what the anchor decides is whether the collision can be seen. A provision that measured both limits from one event and set the ceiling inside the floor would contradict itself on its face. Section 17 of politiregisterloven, a floor of twelve months and a ceiling of thirty-six from the same log entry, does not (Chapter 6, Section 6.9a). A ceiling measured from an external event can sit inside the floor with no visible contradiction, because whether the two clocks cross depends on when that event falls for each record. Article 68(12) is of the second kind: six months from permit expiry against twelve months from the log entry, with the collision arising for exactly the records whose permit expires within six months of the entry, which is the condition of Corollary 1.2. The diagnostic question for any candidate instance is therefore whether a ceiling no longer than the floor is anchored to an event other than the one the floor runs from.

"""
EDITS = [
    dict(id="P15-01", file=C4, old="\n\n## 4.7 Theorem 2: Feasibility", new="\n\n" + PROP3.rstrip("\n") + "\n\n## 4.7 Theorem 2: Feasibility",
         why="M4b: anchoring result promoted to Ch4 as Proposition 3, stated precisely (collision needs L <= F under any anchor)"),
    dict(id="P15-02", file=C4, old="*A note on what kind of result this is.* An objection",
         new="*A note on what kind of result this is.* The results of this chapter are stated as propositions rather than theorems, because their proofs are short once the semantics are fixed. The weight of the argument lies elsewhere: in Section 4.2's necessity analysis, which justifies Semantics II, and in Propositions 3 and 4, which say where the conflict arises and where cryptography is necessary. An objection",
         why="M4a: weight moved to the necessity analysis and Propositions 3 and 4"),
    dict(id="P15-03", file=C6, old="Two periods measured from one origin do not collide;",
         new="Two periods measured from one origin, the later longer than the earlier, do not collide;",
         why="M4b: same-anchor periods collide if the ceiling is not longer (Proposition 3)"),
    dict(id="P15-04", file=C6, old="Article 68(12) behaves differently for a structural reason rather than a numerical one.",
         new="Article 68(12) behaves differently for a structural reason as well as a numerical one: its ceiling is shorter than the floor, which any collision requires, and it is anchored where the shortfall cannot be seen.",
         why="M4b: 'rather than numerical' overstated; Proposition 3 shows both matter"),
    dict(id="P15-05", file=C6,
         old="That crossing is what Theorem 1 characterises, and Corollary 1.2 is the case where it happens with no erasure request present at all.",
         new="That crossing is what Theorem 1 characterises, Corollary 1.2 is the case where it happens with no erasure request present at all, and Chapter 4, Section 4.6 states the general condition as Proposition 3: floor and ceiling collide for a record exactly when the ceiling's end falls inside the floor, which needs a ceiling no longer than the floor and, under an external anchor, depends on each record's history.",
         why="M4b: cross-reference to the promoted result"),
    dict(id="P15-06", file=C6, old="and that a statute pairing a floor with a ceiling from a single origin does not produce it.",
         new="and that a statute pairing a floor with a longer ceiling from a single origin does not produce it.",
         why="M4b: same correction"),
]
