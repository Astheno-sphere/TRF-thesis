"""Build the submission supplement PDF: python3 build_supplement.py  ->  TRF_Submission_Supplement.pdf"""
import base64, html, pathlib, subprocess, sys
import supplement_content as C

HERE = pathlib.Path(__file__).resolve().parent
F = HERE / "fonts"
e = html.escape


def face(name, file, style="normal", weight="100 900"):
    b = base64.b64encode((F / file).read_bytes()).decode()
    return (f"@font-face{{font-family:'{name}';font-style:{style};font-weight:{weight};"
            f"src:url(data:font/ttf;base64,{b}) format('truetype');}}")


FACES = "".join([face("Montserrat", "Montserrat.ttf"), face("Source Serif 4", "SourceSerif4.ttf"),
                 face("Source Serif 4", "SourceSerif4-Italic.ttf", "italic"),
                 face("Plex Mono", "PlexMono.ttf", weight="400")])

CSS = """
:root{--char:#1E1F23;--char2:#2B2C31;--ox:#6E1F26;--gold:#C9A23A;--orange:#C8662B;--cream:#E8DCC4;
--ink:#1E1F23;--mute:#5E5F66;--rule:#DCD3C2;--paper:#FFFFFF;--tint:#F6F2EA}
@page{size:A4;margin:20mm 18mm 18mm 20mm}
@page cover{margin:0}
*{box-sizing:border-box;margin:0;padding:0}
html{font-family:'Source Serif 4',serif;font-size:10.4pt;line-height:1.5;color:var(--ink);
     font-variant-numeric:oldstyle-nums proportional-nums;-webkit-print-color-adjust:exact;print-color-adjust:exact}
h1,h2,h3,.sans{font-family:'Montserrat',sans-serif;font-variant-numeric:lining-nums}
h2{font-size:19pt;font-weight:700;line-height:1.15;color:var(--ox);margin:0 0 3mm}
h3{font-size:10.5pt;font-weight:700;margin:5mm 0 1.5mm}
p{margin:0 0 2.6mm;max-width:158mm}
.lede{font-size:11.2pt;line-height:1.48;color:var(--char2);margin-bottom:6mm;max-width:150mm}
.part{break-before:page}
.cover + .part,body > .part:first-child{break-before:auto}
.kicker{font-family:'Montserrat';font-size:8.5pt;font-weight:600;color:var(--mute);margin-bottom:1.5mm}
.rule{height:2px;background:var(--gold);width:22mm;margin:0 0 6mm}
table{border-collapse:collapse;width:100%;font-size:9.4pt;line-height:1.42}
th{font-family:'Montserrat';font-size:8pt;font-weight:600;text-align:left;color:var(--mute);
   border-bottom:1.2px solid var(--char);padding:0 3mm 1.6mm 0}
td{border-bottom:.6px solid var(--rule);padding:2mm 3mm 2mm 0;vertical-align:top}
td.num{font-family:'Montserrat';font-weight:600;font-variant-numeric:lining-nums tabular-nums;white-space:nowrap}
td.where{font-family:'Montserrat';font-size:8.2pt;color:var(--mute);white-space:nowrap}
code,.mono{font-family:'Plex Mono',monospace;font-size:8.6pt}
/* cover */
.cover{page:cover;height:297mm;width:210mm;background:var(--char);color:var(--cream);position:relative;
       padding:30mm 22mm 24mm 26mm;display:flex;flex-direction:column}
.cover .band{position:absolute;left:0;top:0;bottom:0;width:9mm;background:var(--ox)}
.cover .what{font-family:'Montserrat';font-weight:600;font-size:10pt;color:var(--gold);margin-bottom:9mm}
.cover h1{font-size:25pt;font-weight:700;line-height:1.14;color:#F4EEE2;max-width:150mm;margin-bottom:9mm}
.cover .gold{height:2px;width:30mm;background:var(--gold);margin:0 0 9mm}
.cover .who{font-size:11pt;line-height:1.6;color:var(--cream)}
.cover .who b{font-family:'Montserrat';font-weight:600;color:#F4EEE2}
.cover .contents{margin-top:auto;border-top:.6px solid #4A4B52;padding-top:6mm}
.cover .contents div{display:grid;grid-template-columns:9mm 1fr;font-size:9.6pt;line-height:1.45;margin-bottom:2.6mm;color:#CFC6B4}
.cover .contents span{font-family:'Montserrat';font-weight:600;color:var(--gold)}
.cover .contents b{font-family:'Montserrat';font-weight:600;color:#F4EEE2;font-size:9.4pt}
/* index */
.idx td:first-child{font-family:'Montserrat';font-weight:600;width:32mm}
.idx td:nth-child(2){width:62mm;color:var(--ox);font-family:'Montserrat';font-size:8.8pt;font-weight:500}
/* reproduce */
.steps{counter-reset:s;margin:0 0 4mm}
.step{display:grid;grid-template-columns:9mm 1fr;border-bottom:.6px solid var(--rule);padding:1.8mm 0}
.step:before{counter-increment:s;content:counter(s);font-family:'Montserrat';font-weight:700;color:var(--ox);font-size:12pt}
.step .t{font-family:'Montserrat';font-weight:600;font-size:9.4pt}
.step code{display:block;background:var(--tint);padding:1.2mm 2.4mm;margin:.9mm 0 .5mm;border-left:2px solid var(--char)}
.step .n{font-size:8.8pt;color:var(--mute)}
.exp td{padding:1.5mm 3mm 1.5mm 0}
.finger{margin:1mm 0 2mm;background:var(--char);color:var(--cream);padding:5mm 6mm;display:grid;grid-template-columns:1fr auto;align-items:center;gap:6mm}
.finger .k{font-size:9.6pt;line-height:1.45}
.finger .v{font-family:'Plex Mono';font-size:13pt;color:var(--gold);letter-spacing:.02em}
/* dossier */
.rounds{font-size:9pt;line-height:1.38}.rounds td{padding:1.6mm 3mm 1.6mm 0}
.rounds td:first-child{font-family:'Montserrat';font-weight:600;width:34mm}
.rounds td:first-child small{display:block;font-weight:500;color:var(--mute);font-size:7.8pt;margin-top:.6mm}
.find{display:grid;grid-template-columns:21mm 1fr;border-top:.6px solid var(--rule);padding:3.2mm 0;break-inside:avoid}
.find .id{font-family:'Montserrat';font-weight:700;font-size:9pt}
.find .sev{display:block;font-family:'Montserrat';font-size:7.6pt;font-weight:600;margin-top:.8mm}
.sev.Critical{color:var(--ox)}.sev.Major{color:var(--orange)}.sev.open{color:#fff;background:var(--orange);display:inline-block;padding:.2mm 1.6mm;margin-top:1mm;border-radius:1px}
.find .f{font-weight:600;margin-bottom:1.2mm}
.find dl{display:grid;grid-template-columns:20mm 1fr;gap:.6mm 3mm;font-size:9.1pt;line-height:1.42}
.find dt{font-family:'Montserrat';font-size:7.8pt;font-weight:600;color:var(--mute);padding-top:.5mm}
.held{margin:5mm 0 0;padding:4mm 5mm;border-left:3px solid var(--gold);background:var(--tint);font-size:9.8pt}
/* evidence */
.ev{font-size:8.9pt;line-height:1.36}.ev td{padding:1.5mm 2.6mm 1.5mm 0}
.ev td:first-child{font-family:'Montserrat';font-weight:700;width:28mm;font-size:8.6pt}
.ev td:nth-child(4){font-family:'Plex Mono';font-size:7.6pt;width:40mm}
.ev td:nth-child(5){font-size:8.6pt;color:var(--char2);width:36mm}
/* brief */
.brief .to{font-family:'Montserrat';font-size:8.6pt;color:var(--mute);margin-bottom:5mm}
.brief h2{font-size:17pt}
.brief{font-size:9.9pt;line-height:1.46}.brief .lede{font-size:10.6pt;margin-bottom:4mm}
.brief .fd{display:grid;grid-template-columns:9mm 1fr;margin:2.6mm 0}
.brief .fd span{font-family:'Montserrat';font-weight:700;color:var(--ox);font-size:13pt;line-height:1.2}
.brief .fd b{font-family:'Montserrat';font-weight:700;display:block;margin-bottom:1.2mm;font-size:10pt}
.brief .ask{border-top:1.2px solid var(--char);margin-top:3.5mm;padding-top:2mm}
.brief .ask li{margin:0 0 1.6mm 4.5mm;padding-left:1mm}
.brief .ask li::marker{color:var(--gold);content:"■  "}
.brief .lim{margin-top:3mm;font-size:8.8pt;color:var(--mute);border-top:.6px solid var(--rule);padding-top:2.6mm}
.sig{margin-top:3mm;font-size:9pt;color:var(--char2)}
"""


def page_cover():
    parts = "".join(f"<div><span>{i}</span><p><b>{e(t)}</b><br>{e(d)}</p></div>"
                    for i, (t, d) in enumerate(C.PARTS, 1))
    return f"""<section class="cover"><div class="band"></div>
<div class="what">Submission supplement</div>
<h1>{e(C.TITLE)}</h1><div class="gold"></div>
<div class="who"><b>{e(C.AUTHOR)}</b><br>{e(C.PROGRAMME)}<br>Supervisor: {e(C.SUPERVISOR)}<br>{e(C.DATE)}</div>
<div class="contents">{parts}</div></section>"""


def page_index():
    rows = "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td><td>{e(c)}</td></tr>" for a, b, c in C.INDEX)
    return f"""<section class="part"><div class="kicker">What is submitted</div><h2>The submission at a glance</h2><div class="rule"></div>
<p class="lede">The thesis is the examined work. Everything else here lets a reader check it: run the code,
see what hostile reviewers found and how it was fixed, follow any claim to the code that tests it, and read
what the findings mean for the authorities who will act on them.</p>
<table class="idx"><tr><th>Item</th><th>Where</th><th>What it is for</th></tr>{rows}</table>
<div class="held">Nothing in this supplement adds a claim to the thesis. Where it summarises, the thesis section is named;
where it reports a check, the check can be rerun from the archived code.</div></section>"""


def page_repro():
    steps = "".join(f'<div class="step"><div><div class="t">{e(t)}</div><code>{e(c)}</code><div class="n">{e(n)}</div></div></div>'
                    for t, c, n in C.REPRO_STEPS)
    rows = "".join(f'<tr><td>{e(a)}</td><td class="num">{e(b)}</td><td class="where">{e(c)}</td></tr>'
                   for a, b, c in C.REPRO_EXPECT)
    return f"""<section class="part"><div class="kicker">Part 1</div><h2>Reproduce in five minutes</h2><div class="rule"></div>
<p class="lede">Python 3.11 to 3.13; the checker needs only the standard library. The run is deterministic under seed
20260915, so your output matches the thesis byte for byte.</p>
<div class="steps">{steps}</div>
<div class="finger"><div class="k"><b class="sans">The fastest single check.</b> The auditor view of record 100 prints its
commitment. If it matches, you are running the reported code and seed; the seven diffs of step 4 check the rest.</div><div class="v">{C.REPRO_FINGERPRINT}…</div></div>
<h3>What you should see</h3>
<table class="exp"><tr><th>Result</th><th>Value</th><th>Thesis</th></tr>{rows}</table></section>"""


def page_dossier():
    rounds = "".join(f"<tr><td>{e(a)}<small>{e(b)}</small></td><td>{e(c)}</td><td>{e(d)}</td></tr>"
                     for a, b, c, d in C.DOSSIER_ROUNDS)
    finds = "".join(f"""<div class="find"><div><span class="id">{e(i)}</span><span class="sev {s}">{s}</span>{'<span class="sev open">Open</span>' if v == "Open" else ""}</div>
<div><div class="f">{e(f)}</div><dl><dt>Evidence</dt><dd>{e(ev)}</dd><dt>Fix</dt><dd>{e(fx)}</dd><dt>Verified</dt><dd>{e(v)}</dd></dl></div></div>"""
                    for i, s, f, ev, fx, v in C.AUDIT)
    return f"""<section class="part"><div class="kicker">Part 2</div><h2>Verification dossier</h2><div class="rule"></div>
<p class="lede">Six reviews between 28 October and 6 November 2026: three by AI agents set to attack the thesis, one by the
supervisor, one search of the literature and law, and an AI audit of the code in two passes. Every finding was
checked against its source before anything changed, and every change went through a gated patch recorded in the
thesis repository's change trail.</p>
<table class="rounds"><tr><th>Review</th><th>What it attacked</th><th>What changed</th></tr>{rounds}</table>
<div class="held">What held throughout: the four propositions, every result figure in Chapter 5, and the novelty of modelling
the retention floor, the right to erasure and the deletion ceiling together.</div>
<section class="part"><div class="kicker">Part 2, continued</div><h2>The code audit, finding by finding</h2><div class="rule"></div>
<p class="lede">The critical and major findings of both passes, in the order fault, evidence, fix, and how the fix was verified;
the one left open is marked.
The full report, with every minor finding, is CODE_REVIEW.md in the thesis repository.</p>
{finds}<p class="held">{e(C.AUDIT_MINOR)}</p></section></section>"""


def page_evidence():
    rows = "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td><td class='where'>{e(c)}</td><td>{e(d)}</td><td>{e(g)}</td></tr>"
                   for a, b, c, d, g in C.EVIDENCE)
    return f"""<section class="part"><div class="kicker">Part 3</div><h2>Evidence map</h2><div class="rule"></div>
<p class="lede">Each load-bearing claim, the section that makes it, the code that checks it, and what fails if the code
stops agreeing with the thesis. Proposition 4 is argued, not executed, and is listed so that the gap is visible.</p>
<table class="ev"><tr><th>Claim</th><th>What it says</th><th>Thesis</th><th>Checked by</th><th>Guarded by</th></tr>{rows}</table>
<div class="held">The viewer's claim ledger recomputes every Chapter 5 figure each time it opens, and an automated test fails if
any of them, or any proposition the viewer quotes, departs from the thesis text.</div></section>"""


def page_brief(B, kicker, limits_label, asks_label):
    fds = "".join(f'<div class="fd"><span>{i}</span><div><b>{e(h)}</b><p>{e(t)}</p></div></div>'
                  for i, (h, t) in enumerate(B["findings"], 1))
    asks = "".join(f"<li>{e(a)}</li>" for a in B["asks"])
    return f"""<section class="part brief"><div class="kicker">{kicker}</div><h2>{e(B['title'])}</h2><div class="rule"></div>
<div class="to">{e(B['to'])}</div><p class="lede">{e(B['context'])}</p>{fds}
<div class="ask"><h3>{asks_label}</h3><ul>{asks}</ul></div>
<p class="lim"><b class="sans">{limits_label}</b> {e(B['limits'])}</p>
<p class="sig">{e(C.AUTHOR)}, Høgskolen i Molde, {'November 2026' if kicker.startswith('Part 4') else 'november 2026'}. {'Thesis' if kicker.startswith('Part 4') else 'Masteroppgave'}: <i>{e(C.TITLE)}</i>.</p></section>"""


def render(body, out, footer):
    doc = f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{FACES}{CSS}</style></head><body>{body}</body></html>"
    h = HERE / (out + ".html")
    h.write_text(doc, encoding="utf-8")
    foot = ('<div style="width:100%;font-size:7pt;font-family:sans-serif;color:#8a8a90;padding:0 18mm 0 20mm;'
            'display:flex;justify-content:space-between"><span>Submission supplement. ' + C.AUTHOR +
            ', H\u00f8gskolen i Molde, 2026</span><span class="pageNumber"></span></div>') if footer else '<span></span>'
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();"
          f"await p.goto('file://{h}');await p.waitForTimeout(800);"
          f"await p.pdf({{path:'{HERE}/{out}.pdf',format:'A4',printBackground:true,preferCSSPageSize:true,"
          f"displayHeaderFooter:{str(footer).lower()},headerTemplate:'<span></span>',footerTemplate:{foot!r}}});await b.close();}})();")
    env = {**__import__("os").environ,
           "NODE_PATH": subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()}
    r = subprocess.run(["node", "-e", js], capture_output=True, text=True, env=env)
    if r.returncode:
        sys.exit(r.stderr[-800:])
    h.unlink()
    return HERE / (out + ".pdf")


def build():
    from pypdf import PdfWriter
    cover = render(page_cover(), "_cover", False)
    rest = render(page_index() + page_repro() + page_dossier() + page_evidence()
                  + page_brief(C.POLICY_EN, "Part 4, policy brief", "Limits.", "Questions put to the authorities (Chapter 7, §7.4)")
                  + page_brief(C.POLICY_NO, "Del 5, notat", "Begrensninger.", "Spørsmål til myndighetene (kapittel 7, avsnitt 7.4)"),
                  "_rest", True)
    w = PdfWriter()
    for f in (cover, rest):
        w.append(str(f))
    w.add_metadata({"/Title": "Submission supplement: " + C.TITLE, "/Author": C.AUTHOR})
    out = HERE / "TRF_Submission_Supplement.pdf"
    with open(out, "wb") as fh:
        w.write(fh)
    cover.unlink(); rest.unlink()
    print("written", out)


if __name__ == "__main__":
    build()
