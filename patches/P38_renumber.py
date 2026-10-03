# P38 — MIN-13: regular numbering. Sections §5.5a -> 5.6 (5.6 -> 5.7, 5.7 -> 5.8) and
# §6.9a -> 6.10 (6.10 -> 6.11, 6.11 -> 6.12); Chapter 5 tables numbered in order of appearance
# (5.0a, 5.0, 5.1, 5.2, 5.2a, 5.3, 5.4 -> 5.1 ... 5.7); Appendix A sections numbered in order of
# appearance (A.1b, A.2b, A.9b-e, A.11b removed). Every reference in the prose, the appendices,
# the code docstrings and the app's labels follows. D7.4's own tables ("TEHDAS2, 2026, Table 5.2",
# "D7.4, Table 5.1") are NOT renumbered. Generated, then frozen to P38_renumber.edits.json.
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from frozen import freeze

FILES = ["Front_Matter_v1.md", "Chapter1_Introduction_v2.md", "Chapter2_LitReview_v2_FINAL.md",
         "Chapter3_Methodology_v1.md", "Chapter4_TRF_Model_v1.md", "Chapter5_Demonstration_v1.md",
         "Chapter6_Discussion_v1.md", "Chapter7_Conclusion_v1.md", "code_artefacts/README_Appendix_A.md",
         "Appendix_B_Search_Log.md", "Appendix_C_Evaluation_Instrument.md",
         "demo_app/app.py", "demo_app/trf_checker.py", "repro_package/trf_checker.py",
         "code_artefacts/trf_checker.py", "demo_app/README_repo.md", "repro_package/run_all.sh"]

SEC = {"5.5a": "5.6", "5.6": "5.7", "5.7": "5.8", "6.9a": "6.10", "6.10": "6.11", "6.11": "6.12"}
TAB = {"5.0a": "5.1", "5.0": "5.2", "5.1": "5.3", "5.2": "5.4", "5.2a": "5.5", "5.3": "5.6", "5.4": "5.7"}
APP_ORDER = ["A.1", "A.1b", "A.2", "A.2b", "A.3", "A.4", "A.5", "A.6", "A.7", "A.8", "A.9", "A.9b",
             "A.9c", "A.9d", "A.9e", "A.10", "A.11", "A.12", "A.13", "A.14", "A.11b", "A.15"]
APP = {old: f"A.{i + 1}" for i, old in enumerate(APP_ORDER)}
EXTERNAL = re.compile(r"(TEHDAS2, 2026, |D7\.4, |TEHDAS2 D7\.4, )$")


def renumber(text):
    text = re.sub(r"(?<![\d.])(5\.5a|5\.6|5\.7|6\.9a|6\.10|6\.11)(?![\d\w])", lambda m: SEC[m.group(1)], text)

    def tables(m):
        if EXTERNAL.search(text[max(0, m.start() - 20):m.start()]):
            return m.group(0)
        return m.group(1) + re.sub(r"5\.\d+a?", lambda n: TAB[n.group(0)], m.group(2))
    text = re.sub(r"(Tables? )(5\.\d+a?(?:(?:, | and | to |–)5\.\d+a?)*)", tables, text)
    text = re.sub(r"(?<![\w.])(A\.\d+[a-z]?)(?![\w])", lambda m: APP.get(m.group(1), m.group(1)), text)
    return text


def compute():
    edits, k = [], 0
    for f in FILES:
        t = pathlib.Path(f).read_text(encoding="utf-8")
        seen = set()
        for line in t.split("\n"):
            new = renumber(line)
            if new != line and line not in seen:
                seen.add(line); k += 1
                edits.append(dict(id=f"P38-{k:03d}", file=f, old=line, new=new,
                                  count=t.split("\n").count(line), why="MIN-13 renumbering"))
    return edits


EDITS = freeze("P38_renumber", compute)
LOST_OK = ["number 10", "number 11", "number 14", "number 3", "number 4", "number 5.", "number 5.0", "number 5.1", "number 5.2", "number 5.3", "number 5.4", "number 5.6", "number 5.7", "number 6."]   # renumbering: section, table and appendix numbers change by design
