# P80 — length cut, Ch2 §2.1 (low-value process prose). Tighten the verbose "The first is… the
# second is…" list constructions in §2.1.1 (systematic-review contrast) and §2.1.5 (inclusion /
# exclusion categories). Every fact kept: the structured-narrative-review classification, the
# systematic-review contrast, single-reviewer, all three inclusion categories (with 2018–2026), all
# four exclusion categories, and the primary-prevails rule.
EDITS = [
 dict(id='P80-01', file='Chapter2_LitReview_v2_FINAL.md',
   old=r"""This review is a structured narrative review conducted under a documented and dated protocol. It is not a systematic review. A systematic review executes a pre-registered search strategy in a single sweep, against a fixed set of indexed databases, with independent screening by more than one reviewer. This review proceeded iteratively across four dated search rounds and a fifth, verification-only round, used natural-language rather than Boolean queries, drew substantially on primary regulatory and government sources that are not indexed in bibliographic databases at all, and was screened by one reviewer. Calling it systematic would misdescribe it.""",
   new=r"""This review is a structured narrative review conducted under a documented and dated protocol, not a systematic review. A systematic review executes a pre-registered strategy in a single sweep against a fixed set of indexed databases, with independent screening by more than one reviewer; this review proceeded iteratively across four dated search rounds and a fifth, verification-only round, used natural-language rather than Boolean queries, drew substantially on primary regulatory and government sources not indexed in bibliographic databases at all, and was screened by one reviewer. Calling it systematic would misdescribe it.""",
   why="process prose: tighten the systematic-review contrast; all facts kept"),
 dict(id='P80-02', file='Chapter2_LitReview_v2_FINAL.md',
   old=r"""Material was included in three categories. The first is peer-reviewed work published between 2018 and 2026 bearing on cross-border health data exchange, cryptographic erasure, formal compliance verification, or the GDPR erasure right. The second is primary regulatory, legislative, standards, or governmental material of any date. The third is practitioner and industry material, where the claim being supported is one about industry practice rather than about law.""",
   new=r"""Material was included in three categories: peer-reviewed work published between 2018 and 2026 bearing on cross-border health data exchange, cryptographic erasure, formal compliance verification, or the GDPR erasure right; primary regulatory, legislative, standards, or governmental material of any date; and practitioner and industry material, where the claim being supported is one about industry practice rather than about law.""",
   why="process prose: compact the three inclusion categories to a list; all kept (incl. 2018–2026)"),
 dict(id='P80-03', file='Chapter2_LitReview_v2_FINAL.md',
   old=r"""Four kinds of material were excluded. The first is work addressing data-protection regimes outside the European Union and European Economic Area without comparative bearing, and the second is opinion writing without an identifiable evidential basis. The third is work not retrievable at the time of writing, and the fourth is any source that could not be verified against a primary or publisher record.""",
   new=r"""Four kinds of material were excluded: work addressing data-protection regimes outside the European Union and European Economic Area without comparative bearing; opinion writing without an identifiable evidential basis; work not retrievable at the time of writing; and any source that could not be verified against a primary or publisher record.""",
   why="process prose: compact the four exclusion categories to a list; all kept"),
]
LOST_OK = []
