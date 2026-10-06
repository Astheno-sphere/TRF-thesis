# P59b — João 6 Oct: the tracked changes that could not be located word by word, adapted where P58 has
# since implemented what he marked "not yet implemented", and his comments: proactive invalidation in the
# notation and Proposition 2 (C5/C6); D6.3 cited at v2.0 with the two unsupported claims removed (C12);
# Helsedataservice corrected against helsedata.no (C3); Rak's sentence limited to what the abstract supports
# (C4); §6.11 merged into §6.12 (C16); Datatilsynet enquiry sent (C11); Table 5.7 and its notes on the re-run
# with the final code and the pinned Synthea jar (C9, C10); Appendix B queries restored and removed items
# noted (C13, C14); Appendix C R1 limitation (C15).
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from frozen import freeze
EDITS = freeze("P59b_jf_manual", lambda: None)   # computed once from the drafting script; see the .edits.json
LOST_OK = ["citation Helsedataservice, n.d.", "citation Rak, 2024", "citation TEHDAS2, 2025", "citation TEHDAS2, 2025, 2026", "citation TEHDAS2, 2025; European Parliament and Council of the European Union, 2025", "citation TEHDAS2, 2026", "hedge not yet", "number 1,006", "number 2025", "number 2026", "number 21", "number 28", "number 35", "number 4", "number 5.7", "number 6.12"]   # D6.3 now 2026a and D7.4 2026b; Rak pinpointed; Helsedataservice n.d.-a/-b; Table 5.7 on one code version (1,006 -> 1,002); §6.11 merged; 'do not yet carry' implemented
