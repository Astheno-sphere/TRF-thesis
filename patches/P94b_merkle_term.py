# P94b — keep the defined term 'Merkle' in §7.2 (P94-29 dropped its only occurrence; trim_inspector flagged it).
EDITS = [
 dict(id='P94b-01', file='Chapter7_Conclusion_v1.md',
  old=r"""a legally grounded, attributed invalidation entry in a tamper-evident log, against whose root""",
  new=r"""a legally grounded, attributed invalidation entry in a tamper-evident Merkle log, against whose root""",
  why="restore defined term 'Merkle' in §7.2"),
]
