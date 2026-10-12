# P79 — length cut, Ch3 §3.8 (Option-2, low-value completeness). The instrument is "specified in
# full in Appendix C" (line 123 says so); §3.8's own job is to summarise and point there. Condense the
# full instrument enumeration to a summary that keeps the panel structure, the four perspectives, the
# questionnaire dimensions and the thematic-analysis→revisions link; the per-session mechanics
# (45 min, demonstration script, 13-question count, 16 five-point items) live in Appendix C. Lines 123,
# 127, 129 (the Q7/Cor 1.2 point and the not-executed Sikt caveat) untouched.
EDITS = [
 dict(id='P79-01', file='Chapter3_Methodology_v1.md',
   old=r"""The instrument comprises an eight-person expert panel drawn from four perspectives, two participants each: data protection, health IT architecture, Secure Processing Environment operation, and information logistics. Sessions last forty-five minutes, and participants describe current practice before being shown the proposed mechanism. A demonstration script runs the artefact live and states its limitations before participants are asked to find them. The instrument also includes a thirteen-question semi-structured interview guide, and a closed-response questionnaire of sixteen five-point Likert items across four dimensions: perceived utility, regulatory alignment, operational viability, and audit integrity. A thematic analysis plan sets out an explicit route by which findings would revise the trust model, the residue analysis, and the direction of the next design iteration.""",
   new=r"""The instrument comprises an eight-person expert panel drawn from four perspectives, two participants each: data protection, health IT architecture, Secure Processing Environment operation, and information logistics. It pairs a semi-structured interview guide with a closed-response Likert questionnaire across four dimensions — perceived utility, regulatory alignment, operational viability, and audit integrity — and a thematic analysis plan routing findings into revisions of the trust model, the residue analysis, and the next design iteration. Appendix C specifies the session protocol, the questions and the items in full.""",
   why="low-value completeness: §3.8 defers to Appendix C (line 123); condense instrument enumeration to a summary + pointer, keep panel/perspectives/dimensions/analysis-plan"),
]
LOST_OK = []
