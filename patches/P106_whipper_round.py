# P106 — independent whipper review of P102-P105 (2 Nov). Verified before applying. The six years is
# Helsedirektoratet's pilot decision as controller, not a statute; "besluttet" is "decided", not provisional;
# the reply finds no period in the documents it names (no wider claim); stale "eHDSI baseline" wording;
# Appendix D headings matched to the GDPR-side scope of the Datatilsynet enquiry; abstract/Sammendrag name the
# four subsidiary premises as the SoC does; Ch7 letter settles the two principal steps, not all six.
LOST_OK = []
EDITS = [
 dict(id='P106-01', file='Chapter4_TRF_Model_v1.md',
  old=r"""the period national law sets: 72 months in the Norwegian pilot""",
  new=r"""the period left to national law: 72 months in the Norwegian pilot, as set by Helsedirektoratet as controller""", why="whipper 1"),
 dict(id='P106-02', file='Chapter7_Conclusion_v1.md',
  old=r"""a period national law sets, six years in the Norwegian pilot""",
  new=r"""a period left to national law, six years in the Norwegian pilot as set by Helsedirektoratet""", why="whipper 1"),
 dict(id='P106-03', file='Chapter2_LitReview_v2_FINAL.md',
  old=r"""for the pilot it has provisionally set a six-year retention""",
  new=r"""for the pilot it has decided on a six-year retention""", why="whipper 2: 'besluttet' = decided"),
 dict(id='P106-04', file='Chapter4_TRF_Model_v1.md',
  old=r"""this being the ten-year minimum reported as the eHDSI deployment baseline""",
  new=r"""this being the ten-year figure reported in the secondary literature as the eHDSI deployment baseline""", why="whipper 10"),
 dict(id='P106-05', file='Front_Matter_v1.md',
  old=r"""correspondence with Helsedirektoratet, held by the author.""",
  new=r"""correspondence with Helsedirektoratet, reproduced in Appendix D.""", why="whipper 10"),
 dict(id='P106-06', file='Front_Matter_v1.md',
  old=r"""two principal interpretive steps without regulatory authority""",
  new=r"""two principal interpretive steps and four subsidiary premises without regulatory authority""", why="whipper 7: abstract matches SoC"),
 dict(id='P106-07', file='Front_Matter_v1.md',
  old=r"""to sentrale tolkningssteg uten støtte i rettskilder""",
  new=r"""to sentrale tolkningssteg og fire underordnede premisser uten støtte i rettskilder""", why="whipper 7"),
 dict(id='P106-08', file='Front_Matter_v1.md',
  old=r"""- D.2 Datatilsynet, on the two principal interpretive questions""",
  new=r"""- D.2 Datatilsynet, on the GDPR-side questions""", why="whipper 6"),
 dict(id='P106-09', file='Chapter7_Conclusion_v1.md',
  old=r"""and the means of settling them is a letter""",
  new=r"""and the means of settling the two principal ones is a letter""", why="whipper 5"),
 dict(id='P106-10', file='Appendix_D_Correspondence.md',
  old=r"""No eHDSI specification fixes a retention period for the cross-border audit repository; the period is left to national law; the Norwegian pilot uses six years,""",
  new=r"""The directorate finds no retention period in the eHDSI requirements catalogue or the specifications it names; they refer the matter to national law; for the Norwegian pilot the directorate, as controller, has decided on six years,""", why="whipper 3"),
 dict(id='P106-11', file='Appendix_D_Correspondence.md',
  old=r"""## D.2 Datatilsynet, on the two principal interpretive questions""",
  new=r"""## D.2 Datatilsynet, on the GDPR-side questions""", why="whipper 6"),
 dict(id='P106-12', file='Appendix_D_Correspondence.md',
  old=r"""No reply had been received at the time of writing. Its text is held by the author and will be added here, with the reply, if one is received before the defence.""",
  new=r"""No reply had been received at the time of submission.""", why="whipper 10: a submitted appendix cannot promise later content"),
]
