# P68 — length cut, Chapter 1 §1.1-1.2 (first trim patch; TRIM_RATIONALE.md governs).
#  A  remove unsupported superlative opener (slop)
#  B  drop editorial "most consequential change for clinical practice" ranking (scaffolding)
#  C  §1.2 researcher paragraph re-derives the Art 68(12)/73(1)(e) collision that §1.1 states
#     verbatim; compress to a cross-reference, keeping both "broad reading" hedges, the researcher
#     scenario, the timing and the dates (de-dup, not substance). Home of the collision stays §1.1.
#  D  drop intensifier "Critically,"
# Preservation agent ADMITted A and B (ripple flag on B cleared: "most consequential" occurs only here).
EDITS = [
 dict(id='P68-01', file='Chapter1_Introduction_v2.md',
   old=r"""The European Union's health sector is undergoing the most significant data-governance transformation in its history. Regulation (EU) 2025/327""",
   new=r"""Regulation (EU) 2025/327""", why="slop: unsupported superlative opener"),
 dict(id='P68-02', file='Chapter1_Introduction_v2.md',
   old=r"""Within this regulatory transformation, the most consequential change for clinical practice is the new layer of patient rights established by EHDS. Citizens gain""",
   new=r"""EHDS also establishes a new layer of patient rights. Citizens gain""", why="editorial ranking removed (no downstream pointer)"),
 dict(id='P68-03', file='Chapter1_Introduction_v2.md',
   old=r"""Critically, the same regulation imposes a retention obligation on the same environment.""",
   new=r"""The same regulation imposes a retention obligation on the same environment.""", why="intensifier"),
 dict(id='P68-04', file='Chapter1_Introduction_v2.md',
   old=r"""Article 68(12) EHDS, as operationalised by TEHDAS2, then requires deletion of the electronic health data within the environment within six months of permit expiry. Article 73(1)(e) of the same regulation requires that identifiable access logs for that environment be kept for at least one year. On the broad reading, the environment must therefore be emptied of electronic health data at six months while continuing to hold, for a further six months at minimum, identifiable records of who accessed what within it. No provision resolves the two.""",
   new=r"""On the broad reading the environment must therefore be emptied of electronic health data six months after permit expiry, under Article 68(12) as operationalised by TEHDAS2, while continuing to hold, for at least a further six months, identifiable records of who accessed what within it, exactly as Section 1.1 sets out; no provision resolves the two.""",
   why="de-dup: the Art 73(1)(e) retention re-statement is cross-referenced to 1.1; Art 68(12)/TEHDAS2 kept (preservation agent catch)"),
]
LOST_OK = ["article 73(1)(e)", "number 1", "number 73"]  # the Art 73(1)(e) retention re-statement removed from 1.2; stated verbatim in 1.1
