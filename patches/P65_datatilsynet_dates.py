# P65 — Round 5 legal (quick, inputs now in hand):
#  P65-01  Jo R5[16]: Datatilsynet enquiry — give the send date (23 Sept 2026, from Tiger) and state no
#          response received (Helsedirektoratet and Datatilsynet both silent). Letter-as-appendix left to Tiger.
#  P65-02  Jo R5[6]: demote the "Healthy Europe" news site off the Article 105 legal dates; the dates are
#          already anchored on Article 105 in the surrounding prose and on European Commission (2025a).
#          Healthy Europe stays as a commentary source at its other use (Ch2 TEHDAS2 duration).
EDITS = [
 dict(id='P65-01', file='Chapter7_Conclusion_v1.md',
   old=r"""The enquiry to Datatilsynet on the GDPR-side questions has been sent, and its response is pending at the time of submission.""",
   new=r"""The enquiry to Datatilsynet on the GDPR-side questions was sent on 23 September 2026; no response had been received at the time of submission, and the parallel enquiry to Helsedirektoratet on the ten-year floor was likewise unanswered.""",
   why="Jo R5[16]: send date supplied (23 Sep 2026); both enquiries unanswered at submission"),
 dict(id='P65-02', file='Chapter2_LitReview_v2_FINAL.md',
   old=r"""follow by 26 March 2031 (Healthy Europe, 2026; European Commission, 2025a).""",
   new=r"""follow by 26 March 2031 (Article 105 EHDS; European Commission, 2025a).""",
   why="Jo R5[6]: anchor the staggered dates on Article 105 directly, not the news site"),
]
LOST_OK = ["citation Healthy Europe, 2026; European Commission, 2025a", "number 2026"]  # news site demoted off the legal dates (still cited for commentary at its other use)
