# P09 — M5a: the ten-year floor rests on one secondary source (Simjanoska Misheva et al., 2025).
# Searched 3 Oct for a primary eHDSI/eHMSEG document (RESEARCH_LOG rows 22-25). The one primary
# document reached, the 2017 agreement on NCPeH participation in cross-border eHealth services,
# requires compliance "with the requirements for logs, audit trails, non-repudiation" (clause
# II.4.2) and states no period in its main text; its annexes were not reachable. Per the supervisor's
# fallback, F = 120 is presented as an illustrative parameter, sourced to what it rests on.
# M5e (part): Feng et al. — the arXiv preprint 2209.04052 is the extended version of a peer-reviewed
# paper, CAV 2023, LNCS 13966, pp. 374-396, doi 10.1007/978-3-031-37709-9_18 (Springer page, 3 Oct).

EHN = "eHealth Network. (2017). *Agreement between National Authorities or National Organisations responsible for National Contact Points for eHealth on the Criteria required for the participation in Cross-Border eHealth Information Services* (adopted 9 May 2017). European Commission. https://health.ec.europa.eu/system/files/2017-07/ev_20170509_co06_en_0.pdf\n\n"
OLD_FENG = "Feng, N., Marsso, L., Sabetzadeh, M., & Chechik, M. (2022). *Bounded satisfiability checking of metric first-order temporal logic*. arXiv. https://doi.org/10.48550/arXiv.2209.04052"
NEW_FENG = "Feng, N., Marsso, L., Sabetzadeh, M., & Chechik, M. (2023). Early verification of legal compliance via bounded satisfiability checking. In *Computer Aided Verification (CAV 2023)* (LNCS 13966, pp. 374–396). Springer. https://doi.org/10.1007/978-3-031-37709-9_18"

EDITS = [
    dict(id="P09-01", file="Front_Matter_v1.md",
         old="audit-retention floors (ten years for MyHealth@EU audit repositories under the eHDSI deployment baseline,",
         new="audit-retention floors (ten years as reported for MyHealth@EU audit repositories under the eHDSI deployment baseline,",
         why="M5a: abstract no longer states the floor as established"),
    dict(id="P09-02", file="Front_Matter_v1.md",
         old="(ti år for MyHealth@EU under eHDSI-baselinen",
         new="(ti år slik det er rapportert for MyHealth@EU under eHDSI-baselinen",
         why="M5a: Sammendrag aligned with the abstract"),
    dict(id="P09-03", file="Chapter1_Introduction_v2.md",
         old="ATNA-compliant audit repositories must retain their logs for a minimum of ten years (Simjanoska Misheva et al., 2025; IHE International, 2023).",
         new="ATNA-compliant audit repositories are reported to retain their logs for a minimum of ten years (Simjanoska Misheva et al., 2025; IHE International, 2023), a figure this thesis could not confirm in a primary document and treats as illustrative (Chapter 2, Section 2.3).",
         why="M5a"),
    dict(id="P09-04", file="Chapter1_Introduction_v2.md",
         old="instantiated as the ten-year floor imposed on cross-border audit repositories by the eHDSI deployment baseline",
         new="instantiated as the ten-year floor reported for cross-border audit repositories under the eHDSI deployment baseline",
         why="M5a"),
    dict(id="P09-05", file="Chapter1_Introduction_v2.md",
         old="namely the ten-year minimum imposed on IHE ATNA audit repositories by the eHDSI deployment baseline",
         new="namely the ten-year minimum reported for IHE ATNA audit repositories under the eHDSI deployment baseline",
         why="M5a"),
    dict(id="P09-06", file="Chapter2_LitReview_v2_FINAL.md",
         old="The eHDSI security framework that operationalises ATNA within the MyHealth@EU infrastructure does specify retention in concrete terms. The framework adopted by the eHMSEG governance body for cross-border NCPeH operations requires audit repositories to retain records for a minimum of ten years, characterised by Simjanoska Misheva et al. (2025) as the binding deployment baseline.",
         new="The eHDSI security framework that operationalises ATNA within the MyHealth@EU infrastructure is reported to specify retention in concrete terms: Simjanoska Misheva et al. (2025) characterise a minimum of ten years for audit repositories as the binding deployment baseline for cross-border NCPeH operations. The primary document this thesis could inspect, the agreement under which National Contact Points join the cross-border services, requires each party to ensure its contact point's compliance \"with the requirements for logs, audit trails, non-repudiation\" and states no period in its main text (eHealth Network, 2017, clause II.4.2); the annexes that would fix one were not available. The thesis therefore treats ten years as an illustrative value of the floor parameter rather than as an established requirement, and Chapter 4, Corollary 2.2 shows that no result depends on it.",
         why="M5a: secondary source named as such; primary document cited for what it says; F=120 illustrative"),
    dict(id="P09-07", file="Chapter2_LitReview_v2_FINAL.md",
         old="\nEuropean Commission. (2025a).",
         new="\n" + EHN.rstrip("\n") + "\n\nEuropean Commission. (2025a).",
         why="M5a: new primary reference"),
    dict(id="P09-08", file="Chapter4_TRF_Model_v1.md",
         old="this being the ten-year minimum imposed by the eHDSI deployment baseline for MyHealth@EU operations (Simjanoska Misheva et al., 2025).",
         new="this being the ten-year minimum reported as the eHDSI deployment baseline for MyHealth@EU operations (Simjanoska Misheva et al., 2025). The value is illustrative: the primary agreement inspected requires audit trails without stating a period (eHealth Network, 2017, clause II.4.2), and by Corollary 2.2 no result depends on it.",
         why="M5a"),
    dict(id="P09-09", file="Chapter4_TRF_Model_v1.md",
         old="\nFinck, M. (2018)",
         new="\n" + EHN.rstrip("\n") + "\n\nFinck, M. (2018)",
         why="M5a: reference in Ch4 list"),
]
for f in ["Chapter1_Introduction_v2.md", "Chapter2_LitReview_v2_FINAL.md", "Chapter3_Methodology_v1.md", "Chapter6_Discussion_v1.md", "Chapter7_Conclusion_v1.md"]:
    EDITS.append(dict(id=f"P09-F{len(EDITS):02d}", file=f, old=OLD_FENG, new=NEW_FENG,
                      why="M5e: peer-reviewed version (CAV 2023) replaces the arXiv preprint"))
for f, n1, n2, n3 in [("Chapter1_Introduction_v2.md", 1, 1, 1), ("Chapter2_LitReview_v2_FINAL.md", 2, 0, 1),
                      ("Chapter3_Methodology_v1.md", 1, 1, 1), ("Chapter6_Discussion_v1.md", 0, 0, 1),
                      ("Chapter7_Conclusion_v1.md", 0, 0, 1)]:
    if n1: EDITS.append(dict(id=f"P09-F{len(EDITS):02d}", file=f, old="Feng et al., 2022)", new="Feng et al., 2023)", count=n1, why="M5e: year"))
    if n2: EDITS.append(dict(id=f"P09-F{len(EDITS):02d}", file=f, old="Feng et al. (2022)", new="Feng et al. (2023)", count=n2, why="M5e: year"))
    EDITS.append(dict(id=f"P09-F{len(EDITS):02d}", file=f, old="Chechik, 2022)" if f in ("Chapter1_Introduction_v2.md", "Chapter6_Discussion_v1.md", "Chapter7_Conclusion_v1.md") else "Chechik (2022)",
                      new="Chechik, 2023)" if f in ("Chapter1_Introduction_v2.md", "Chapter6_Discussion_v1.md", "Chapter7_Conclusion_v1.md") else "Chechik (2023)", count=n3, why="M5e: year"))

LOST_OK = ["citation Feng et al., 2022", "citation Feng, Marsso, Sabetzadeh, & Chechik, 2022", "number 2022", "citation Feng et al. (2022)", "citation Chechik (2022)",
           "number 2209.04052", "number 10.48550", "citation Sabetzadeh, and Chechik (2022)"]  # every 2022 Feng citation becomes 2023; each gain is shown
