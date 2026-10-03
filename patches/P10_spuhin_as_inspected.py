# P10 — M5b: SPUHiN "finalised" claims aligned with what was inspected.
# Helsedirektoratet's SPUHiN project page (fetched 3 Oct): the SPE criteria "were on hearing
# July–October 2025" and are "included in SPUHiN-rapport D5.2", reached through the EU Funding &
# Tenders portal; "adaptation to the final implementing act will depend on decisions from the EU
# Commission". The reference entry SPUHiN (2025) is the hearing version, and §6.8 already conceded
# the absence was observed in the published checklists rather than in the full deliverable.
# Every claim now says what was inspected: the hearing version.

EDITS = [
    dict(id="P10-01", file="Front_Matter_v1.md",
         old="requires of the substrate nothing that the finalised national criteria do not already demand.",
         new="requires of the substrate nothing that the national criteria put to public hearing in 2025 do not already demand.", why="M5b"),
    dict(id="P10-02", file="Chapter1_Introduction_v2.md",
         old="the recommendations have since been consolidated into final form, including separate compliance checklists for SPE providers and SPE user organisations, positioned as a national reference basis pending the EU implementing act (SPUHiN, 2025). The finalised criteria contain governance and functional requirements but no mechanism reconciling the retention and erasure regimes: the gap addressed here therefore survives against the final national document, not merely a draft.",
         new="the Directorate states that the criteria are included in deliverable D5.2, with separate compliance checklists for SPE providers and SPE user organisations, positioned as a national reference basis pending the EU implementing act (SPUHiN, 2025). The version this thesis inspected, the one put to hearing, contains governance and functional requirements but no mechanism reconciling the retention and erasure regimes. The absence is observed in that version and has not been checked against the deliverable as submitted.",
         why="M5b: claim limited to the version inspected"),
    dict(id="P10-03", file="Chapter1_Introduction_v2.md",
         old="It also includes finalised national SPE criteria from the SPUHiN process, whose published checklists do not address",
         new="It also includes national SPE criteria from the SPUHiN process, whose checklists in the hearing version do not address", why="M5b"),
    dict(id="P10-04", file="Chapter2_LitReview_v2_FINAL.md",
         old="the recommendations were consolidated into final form as SPUHiN deliverable D5.2,",
         new="the criteria were, by the Directorate's account, included in SPUHiN deliverable D5.2,", why="M5b"),
    dict(id="P10-05", file="Chapter2_LitReview_v2_FINAL.md",
         old="Inspection of the finalised checklists shows", new="Inspection of the checklists in the hearing version shows", why="M5b"),
    dict(id="P10-06", file="Chapter2_LitReview_v2_FINAL.md",
         old="What the finalised criteria do not contain", new="What those criteria do not contain", why="M5b"),
    dict(id="P10-07", file="Chapter2_LitReview_v2_FINAL.md",
         old="The gap identified by this thesis therefore survives contact with the final national document, not merely its draft: Norway now possesses finalised SPE criteria that govern",
         new="The gap identified by this thesis therefore survives the hearing version, not only the 2024 draft: Norway now has national SPE criteria that govern", why="M5b"),
    dict(id="P10-08", file="Chapter2_LitReview_v2_FINAL.md",
         old="requiring of the substrate nothing that the finalised criteria do not already demand", new="requiring of the substrate nothing that the national criteria do not already demand", why="M5b"),
    dict(id="P10-09", file="Chapter2_LitReview_v2_FINAL.md",
         old="The finalised Norwegian SPE criteria (SPUHiN, 2025) govern", new="The Norwegian SPE criteria in their hearing version (SPUHiN, 2025) govern", why="M5b"),
    dict(id="P10-10", file="Chapter2_LitReview_v2_FINAL.md",
         old="nothing beyond what the finalised national criteria already require", new="nothing beyond what the national criteria already require", why="M5b"),
    dict(id="P10-11", file="Chapter3_Methodology_v1.md",
         old="the finalised Norwegian Secure Processing Environment criteria,", new="the Norwegian Secure Processing Environment criteria in their hearing version,", why="M5b"),
    dict(id="P10-12", file="Chapter4_TRF_Model_v1.md",
         old="The finalised Norwegian criteria for Secure Processing Environments require", new="The Norwegian criteria for Secure Processing Environments, in the version put to hearing, require", why="M5b"),
    dict(id="P10-13", file="Chapter4_TRF_Model_v1.md",
         old="requiring nothing of the substrate that the finalised national criteria do not already require.", new="requiring nothing of the substrate that the national criteria do not already require.", why="M5b"),
    dict(id="P10-14", file="Chapter6_Discussion_v1.md",
         old="the national criteria for Secure Processing Environments were finalised through the SPUHiN process after a public hearing running from July to October 2025, and are positioned",
         new="the national criteria for Secure Processing Environments went through a public hearing in the SPUHiN process from July to October 2025, and are positioned", why="M5b"),
    dict(id="P10-15", file="Chapter6_Discussion_v1.md",
         old="The finalised compliance checklists, as inspected, address", new="The compliance checklists, in the hearing version inspected, address", why="M5b"),
    dict(id="P10-16", file="Chapter7_Conclusion_v1.md",
         old="It requires of the substrate nothing that the finalised national criteria do not already demand.", new="It requires of the substrate nothing that the national criteria do not already demand.", why="M5b"),
    dict(id="P10-17", file="Chapter7_Conclusion_v1.md",
         old="The Norwegian national criteria, finalised after public hearing, govern", new="The Norwegian national criteria, put to public hearing in 2025, govern", why="M5b"),
]
