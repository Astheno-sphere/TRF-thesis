# P21 — MIN-05 (frequency claims softened: §3.7 says no result is a frequency) and MIN-06 (the
# closed window [t(a), t(a)+F] spans F+1 monthly indices: justified, not changed, because changing
# it would change every recorded figure and the closed form is the conservative reading of
# "at least"). Also the Ch4 summary sentence made conditional on log granularity (D-16 residue).
C3, C4 = "Chapter3_Methodology_v1.md", "Chapter4_TRF_Model_v1.md"
EDITS = [
    dict(id="P21-01", file=C3,
         old="which, over a ten-year window, is the ordinary case rather than the exception.",
         new="which, over a ten-year window, covers a request arriving in almost any month; how often requests in fact arrive is not modelled (Section 3.7).",
         why="MIN-05: no frequency claim"),
    dict(id="P21-02", file=C4,
         old="Infeasibility is therefore not an edge case arising from unusual timing; it is the generic case, avoided only if no data subject exercises Article 17 in respect of any record for essentially the whole of its retention life.",
         new="The condition is therefore not one of unusual timing: it holds for a request arriving in any but the last month of the window. How often data subjects exercise Article 17 is an empirical question that the model does not answer (Chapter 3, Section 3.7).",
         why="MIN-05: 'the generic case' was a frequency claim"),
    dict(id="P21-03", file=C4,
         old="It proved that under the plaintext-verifiability semantics implicit in current practice the system is infeasible, generically so in the cross-border case and, critically, without any erasure request at all in the Secure Processing Environment case, where two retention provisions of a single regulation collide over a single environment.",
         new="It proved that under the plaintext-verifiability semantics implicit in current practice the system is infeasible for any cross-border record whose erasure request arrives inside its window and, for Secure Processing Environment logs kept at patient-record granularity on the broad reading, without any erasure request at all, where two retention provisions of a single regulation collide over a single environment.",
         why="MIN-05; D-16 conditional carried into the chapter summary"),
    dict(id="P21-04", file=C4,
         old="The record must count as verifiable throughout its retention window. Source:",
         new="The record must count as verifiable throughout its retention window. The window is closed at both ends and so spans $F + 1$ monthly indices. This is deliberate: the obligations are minimums (\"at least one year\"), and a record written during month $t(a)$ completes $F$ full months only during month $t(a) + F$, so requiring verifiability through that month is the conservative reading of \"at least\". A half-open window would shorten every obligation by up to a month. Source:",
         why="MIN-06: closed window justified"),
]
