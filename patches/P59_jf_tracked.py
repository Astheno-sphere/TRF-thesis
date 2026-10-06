# P59 — João's review of 6 Oct (supervisor_review/review4_JF_2026-10-06.docx): his tracked changes, applied
# verbatim where they still fit the current text, located word by word (supervisor_review/review4_changes.txt
# lists all 77 marked paragraphs). Manual items and his comments follow in P59b.
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from frozen import freeze
EDITS = freeze("P59_jf_tracked", lambda: None)
LOST_OK = ["number 2023", "hedge may ", "number 2"]   # "dissolved in May 2023" corrected to the 1 Jan 2024 merger; "listed in A.2" now "in docs/"
