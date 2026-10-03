# P11 — M7a, M7b. The supervisor asked for one or two concrete logistics anchors, suggested Union
# Customs Code record-keeping against destruction of goods, tested against the anchoring result of
# §6.9a, and said §1.4 overreaches. Verified 3 Oct (legislation.gov.uk, text "as adopted"):
#   UCC Art 51(1): keep documents and information "for at least three years", from the end of the
#   year the declaration is accepted / the procedure discharged; 51(2): extended for corrections,
#   appeals and court proceedings.
#   UCC Art 197: customs authorities "may require goods which have been presented to customs to be
#   destroyed".
# Finding: destruction reaches the goods, record-keeping reaches the documents; they do not collide.
# The record outlives the thing recorded: Semantics II in physical form. The analogy's limit is stated.

UCC = "European Parliament and Council of the European Union. (2013). Regulation (EU) No 952/2013 of 9 October 2013 laying down the Union Customs Code. *Official Journal of the European Union*, L 269, 1–101. https://eur-lex.europa.eu/eli/reg/2013/952/oj"

EDITS = [
    dict(id="P11-01", file="Chapter1_Introduction_v2.md",
         old="This situates the contribution within the disciplinary identity of Sustainable Energy Logistics at HiMolde and imports a solution structure that logistics has operated for decades into a domain that has not yet recognised the equivalence.",
         new="This situates the contribution within the disciplinary identity of Sustainable Energy Logistics at HiMolde. The borrowing is specific rather than wholesale: customs law already keeps the record of goods after the goods themselves have been destroyed (Chapter 2, Section 2.7), and that separation of the record from the thing recorded is the move Chapter 4 makes for the audit trail.",
         why="M7a: §1.4 overreach replaced by the specific, verified correspondence"),
    dict(id="P11-02", file="Chapter1_Introduction_v2.md",
         old="Fourth, it does not measure hardware energy consumption, and no sustainability metrics are claimed beyond conceptual framing.",
         new="Fourth, it does not measure hardware energy consumption, and no sustainability metrics are claimed beyond conceptual framing. Its place in a programme in Sustainable Energy Logistics is therefore in the logistics of information rather than of energy: it treats a regulated cross-border record as a consignment whose custody, retention and destruction are governed by the regimes it crosses.",
         why="M7b: one honest sentence on programme fit"),
    dict(id="P11-03", file="Chapter2_LitReview_v2_FINAL.md",
         old="The ten-year retention floor for that audit log under the eHDSI security framework is the digital equivalent of mandatory customs record-keeping obligations under physical trade law. The right to erasure under General Data Protection Regulation Article 17 is the digital equivalent of the destruction-of-records requirements that apply to perishable or sensitive physical goods. The conflict between these regimes is the same kind of conflict that physical logistics has long managed through ledger-based reconciliation systems, certified destruction protocols, and chain-of-custody documentation.",
         new="The retention floor on that audit log is the digital equivalent of customs record-keeping. The Union Customs Code requires the person concerned to keep the documents and information on which a customs declaration rests \"for at least three years\", the period running from the end of the year in which the declaration is accepted or the procedure discharged, and extended while a correction, an appeal or court proceedings are pending (European Parliament and Council of the European Union, 2013, Article 51). The erasure obligation of Article 17 GDPR has its physical counterpart in destruction: customs authorities \"may require goods which have been presented to customs to be destroyed\" (Article 197). The two do not collide, because destruction reaches the goods and record-keeping reaches the documents, so the record of a destroyed consignment, including the fact of its destruction, is kept for the full period. That separation of the record from the thing recorded is what Semantics II does for the audit trail, where accountability attaches to the record of the access and of its payload's invalidation rather than to the payload's continued existence (Chapter 4, Section 4.5). Checked against the anchoring result of Chapter 6, Section 6.9a, the customs case confirms it from the other side: the destruction power is anchored to an external event, a customs decision, and would cross the record-keeping floor if it reached the documents; it does not, because it is confined to the goods. The analogy also marks where it stops. In customs the floor and the destruction act on different objects by design, whereas in an audit trail the personal data and the record of their processing begin in the same record, and the mechanism has to separate them.",
         why="M7a: verified UCC anchor; unsourced 'destruction-of-records requirements' claim removed; tested against §6.9a; limit stated"),
    dict(id="P11-04", file="Chapter2_LitReview_v2_FINAL.md",
         old="\nEuropean Parliament and Council of the European Union. (2016)",
         new="\n" + UCC + "\n\nEuropean Parliament and Council of the European Union. (2016)",
         why="M7a: new reference"),
]

# "not yet" was in "a domain that has not yet recognised the equivalence", the overreach the
# supervisor flagged; removing it removes a claim, it does not weaken a hedge.
LOST_OK = ["hedge not yet"]
