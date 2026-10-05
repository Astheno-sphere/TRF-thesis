# P55 — Figures 4.1 and 5.1: architecture diagrams drawn with Archify (showcase gates and browser check
# passed), rendered at 3x to figures/*.png. Sources: .archify/*/candidate.json.
EDITS = [
 dict(id='P55-01', file='Chapter4_TRF_Model_v1.md',
  old="what is encrypted, what is committed, what is destroyed, and what is logged when it is.\n\n",
  new="what is encrypted, what is committed, what is destroyed, and what is logged when it is. Figure 4.1 shows the whole of it on one page.\n\n"
      "![Figure 4.1. Crypto-Erasure by Invalidation at the audit boundary. Solid arrows are writes at access time; red dashed arrows are the invalidation at the earlier of the erasure deadline and the deletion ceiling. The Merkle log holds accessor fields, commitments and invalidation entries, never the payload or the subject fields.](figures/fig4_1_cei_mechanism.png){width=6.3in}\n\n",
  why='figure'),
 dict(id='P55-02', file='Chapter5_Demonstration_v1.md',
  old="Four further modules accompany it, none of which alters anything the checker reports. Their line counts, and the full source of each, are given in Appendix A.",
  new="Four further modules accompany it, none of which alters anything the checker reports. Their line counts, and the full source of each, are given in Appendix A. Figure 5.1 maps the modules and the path a record takes through them.\n\n"
      "![Figure 5.1. The artefact's modules and data path. Records enter from the generator or one of the optional layers, are invalidated on schedule, and are checked under both semantics; the optional cryptographic module and the bounded SMT check sit beside the checker and report separately.](figures/fig5_1_trf_artefact.png){width=6.3in}",
  why='figure'),
]
LOST_OK = []
