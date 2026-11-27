"""One-off: derive the body of manuscript.md from the accepted base (pandoc --track-changes=accept).
Every edit beyond accepted changes is an explicit, asserted substitution, listed in CHANGES_vs_original.md."""
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
body = src.split("\n[^1]:")[0]
body = body.split("# 1 Introduction", 1)[1]
body = "# 1 Introduction" + body
# drop the base AI declaration and data statement: rewritten in manuscript.md by hand
body = body.split("# Data and code availability")[0]
# footnote markers -> numbered citations before the punctuation
body = re.sub(r"\.\s?\[\^(\d+)\]", r" [\1].", body)
body = re.sub(r"\[\^(\d+)\]", r" [\1]", body)
body = body.replace("record--constraint", "record-constraint")
def sub(old, new):
    global body
    assert body.count(old) == 1, old
    body = body.replace(old, new)
sub("(anonymised for review, entry R-47)", "supplied as supplementary material (anonymised for review)")
open(sys.argv[2], "w", encoding="utf-8").write(body)
print(len(body.split()))
