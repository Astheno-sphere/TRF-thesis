# P03 — §2.2 EHDS dates (M5d). The sentence sourced to an Ernst & Young law alert gave
# "by June 2025" for digital health authorities and "by January 2026" for EHR certification,
# which contradicts the Article 105 schedule stated two sentences earlier.
# Verified 3 Oct against the Regulation (streamlex mirror of OJ L 2025/327):
#   Art 19(1): Member States designate one or more digital health authorities and inform the
#              Commission by 26 March 2027.
#   Art 105(1)(a): Arts 3-15, 23(2)-(6), 25-27, 47-49 apply from 26 March 2029 to the first
#              priority categories and the corresponding EHR systems; (b) 26 March 2031 for the rest.
# The law-firm source is dropped; nothing else in the thesis cites it (Appendix B keeps its
# round-5 locator record, which is history, not a citation).

EDITS = [
    dict(id="P03-01", file="Chapter2_LitReview_v2_FINAL.md",
         old="Each Member State must designate a National Digital Health Authority by June 2025, and healthcare providers and electronic health record vendors must certify their systems for interoperability and security compliance by January 2026 (Ernst & Young, 2025).",
         new="Each Member State must designate one or more digital health authorities and inform the Commission of them by 26 March 2027 (Article 19(1)), and the requirements on electronic health record systems follow the same Article 105 schedule, applying from 26 March 2029 to the systems that process the first priority categories (European Parliament and Council of the European Union, 2025).",
         why="M5d: dates verified against Arts 19(1) and 105(1)(a); EY law alert dropped as a source"),
    dict(id="P03-02", file="Chapter2_LitReview_v2_FINAL.md",
         old="Ernst & Young. (2025). *Regulation (EU) 2025/327: Establishing the European Health Data Space (EHDS)* [Law alert]. EY Greece. https://www.ey.com/en_gr/technical/tax/tax-alerts/regulation-2025-327-establishing-ehds\n\n",
         new="",
         why="M5d: reference entry removed with its only citation"),
]

LOST_OK = ["citation Ernst & Young, 2025", "number 2025", "number 2026"]  # "January 2026" was the wrong date being removed
