# P28 — PRES-4 (part 1): the Norwegian NCPeH pilot details said once, in §2.2, then cross-referred.
# §1.1 keeps a short account for the reader's first encounter; §1.4, §2.6, §4.11, §6.8 point to §2.2.
# The one fact only §1.1 carried (legal basis, privacy notices and DPIA completed by 31 March 2025)
# moves into §2.2 so nothing is lost.
C1, C2, C4, C6 = "Chapter1_Introduction_v2.md", "Chapter2_LitReview_v2_FINAL.md", "Chapter4_TRF_Model_v1.md", "Chapter6_Discussion_v1.md"
EDITS = [
    dict(id="P28-01", file=C1,
         old="Norway's integration with MyHealth@EU is no longer prospective but operational, though its scope remains deliberately narrow. The Norwegian connection project has been coordinated jointly by the Norwegian Directorate of Health (Helsedirektoratet) and the Norwegian Health Network (Norsk Helsenett SF) since January 2023, with a planned duration of 41 months. It has taken its pilot live at the emergency clinics (legevakter) in Bodø and Stjørdal, connected to Portugal, Czechia, and Finland for the receipt of patient summaries concerning citizens of those states who require care in Norway. The Bodø and Stjørdal clinics are in production with Czechia and Portugal, and emergency clinics in Trondheim and Ålesund operating on Helseplattformen have requested the service for the next stage of expansion (Helsedirektoratet, 2026). In 2026 the project began its next stage, establishing NCP-A, the contact point through which Norwegian health data will be shared with other participating states (Helsedirektoratet, 2026). Two qualifications are material and are recorded rather than elided. The pilot is live in the sense that the infrastructure is in production, and the legal basis, privacy notices, and data protection impact assessment were completed by 31 March 2025. But the Directorate's own portfolio reporting notes that no relevant patients had yet presented for the solution to be used in practice, so the volume of genuine cross-border audit records generated in Norway to date is minimal.",
         new="Norway's integration with MyHealth@EU is no longer prospective but operational, though its scope remains deliberately narrow. The pilot run by the Norwegian Directorate of Health (Helsedirektoratet) and the Norwegian Health Network (Norsk Helsenett SF) is in production at the emergency clinics (legevakter) in Bodø and Stjørdal, receiving patient summaries for citizens of other participating states, and in 2026 the project began establishing NCP-A, the contact point through which Norwegian health data will be shared abroad (Helsedirektoratet, 2026). No relevant patients had yet presented when the Directorate last reported, so the volume of genuine cross-border audit records generated in Norway is still minimal. Chapter 2, Section 2.2 gives the details.",
         why="PRES-4: short first account; details in §2.2"),
    dict(id="P28-02", file=C1,
         old="Norway's NCPeH is in live pilot operation, exchanging records with Portugal, Czechia, and Finland, with its outbound capability under construction during 2026 (Helsedirektoratet, 2026).",
         new="Norway's NCPeH is in live pilot operation, with its outbound capability under construction during 2026 (Helsedirektoratet, 2026), as Section 1.1 describes.",
         why="PRES-4: cross-reference"),
    dict(id="P28-03", file=C2,
         old="The Directorate's portfolio reporting records that no relevant patients had yet presented",
         new="The legal basis, privacy notices and data protection impact assessment were completed by 31 March 2025. The Directorate's portfolio reporting records that no relevant patients had yet presented",
         why="PRES-4: the one fact only §1.1 carried moves here"),
    dict(id="P28-04", file=C2,
         old="On the primary-use side, the national infrastructure has moved from preparation into operation during the review period. The Norwegian NCPeH pilot is live at the Bodø and Stjørdal emergency clinics, receiving patient summaries from Portugal, Czechia, and Finland (Helsedirektoratet, 2026). The cross-border audit records this thesis concerns are therefore beginning to be generated in Norwegian production, at presently small volume.",
         new="On the primary-use side, the national infrastructure has moved from preparation into operation during the review period: with the NCPeH pilot of Section 2.2 in production (Helsedirektoratet, 2026), the cross-border audit records this thesis concerns are beginning to be generated in Norway, at presently small volume.",
         why="PRES-4: cross-reference"),
    dict(id="P28-05", file=C4,
         old="Norway's NCPeH is in live pilot operation at the Bodø and Stjørdal emergency clinics, receiving patient summaries from Portugal, Czechia, and Finland, with expansion to further emergency clinics requested (Helsedirektoratet, 2026).",
         new="Norway's NCPeH is in live pilot operation (Helsedirektoratet, 2026), as Chapter 2, Section 2.2 describes.",
         why="PRES-4: cross-reference"),
    dict(id="P28-06", file=C6,
         old="Norway's National Contact Point is in live pilot operation at the Bodø and Stjørdal emergency clinics, connected to Portugal, Czechia, and Finland, with the Directorate's own portfolio reporting noting that no relevant patients had yet presented for the solution to be used in practice (Helsedirektoratet, 2026).",
         new="Norway's National Contact Point is in live pilot operation, but no relevant patients had yet presented when the Directorate last reported (Helsedirektoratet, 2026), as Chapter 2, Section 2.2 sets out.",
         why="PRES-4: cross-reference"),
]
LOST_OK = ["number 41", "number 2023", "number 31", "number 2025", "number 2026", "citation Helsedirektoratet, 2026"]  # the citation: §1.1 cited the same source twice in one paragraph; once now   # project dates and DPIA date: still in §2.2 (31 March 2025 moved there by P28-03)
