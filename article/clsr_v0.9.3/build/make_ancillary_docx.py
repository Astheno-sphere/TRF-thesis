"""Title page, cover letter and declaration of competing interest (non-anonymised files).
Every [TO CONFIRM ...] and [TO FILL] marker must be settled and removed before submission."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.oxml.ns import qn

TITLE = "Auditing After Erasure in the European Health Data Space: Audit Logs, the Right to Erasure and Permit-Based Deletion"
JF = " [TO CONFIRM by J. Ferreira]"         # items the second author must approve
FILL = " [TO FILL]"                          # factual details still missing
EACH = " [TO CONFIRM by J. Ferreira]"
CONCEPT_DOI = "https://doi.org/10.5281/zenodo.23819274"   # all versions, resolves to the latest
VERSION_DOI = "https://doi.org/10.5281/zenodo.24587633"   # release 1.3.4 (includes sensitivity_secondary.py)

def new():
    d = Document()
    st = d.styles["Normal"]
    st.font.name, st.font.size = "Times New Roman", Pt(12)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    st.paragraph_format.space_after = Pt(6)
    st.paragraph_format.line_spacing = 1.15
    for s in d.sections:
        s.page_width, s.page_height = Cm(21.0), Cm(29.7)
        s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Cm(2.5)
    cp = d.core_properties
    cp.author = ""; cp.last_modified_by = ""; cp.comments = ""; cp.title = ""
    return d

def h(d, text, size=12):
    p = d.add_paragraph(); r = p.add_run(text); r.bold = True; r.font.size = Pt(size)
    p.paragraph_format.space_before = Pt(10)
    return p

def para(d, *parts):
    p = d.add_paragraph()
    for t in parts:
        if isinstance(t, tuple):
            r = p.add_run(t[0]); r.bold = "b" in t[1]; r.italic = "i" in t[1]
            if "s" in t[1]: r.font.superscript = True
        else:
            p.add_run(t)
    return p

# ---------------- Title page
d = new()
h(d, TITLE, 16)
para(d, "Arshad Akhtar Abbasia", ("a,*", "s"), ", João Ferreira", ("a", "s"),
     JF[:-1] + ": name form]")
para(d, ("a", "s"), " Molde University College (Høgskolen i Molde), P.O. Box 2110, 6402 Molde, Norway" + JF[:-1] +
     ": affiliation]")
para(d, ("*", "s"), " Corresponding author: Arshad Akhtar Abbasia. Email: arshad.a.abbasia@himolde.no. "
     "Postal address: Molde University College, P.O. Box 2110, 6402 Molde, Norway")
para(d, "ORCID: Arshad Akhtar Abbasia, https://orcid.org/0000-0001-9461-9442. João Ferreira:" + JF[:-1] +
     ": ORCID, if any]")
h(d, "Acknowledgments")
para(d, "The authors thank the Norwegian Directorate of Health (Helsedirektoratet), operator of the Norwegian "
        "National Contact Point for eHealth, for its written answer of 19 October 2026 on the retention of "
        "contact-point audit logs.")
h(d, "CRediT authorship contribution statement")
para(d, ("Arshad Akhtar Abbasia: ", "b"), "Conceptualization, Methodology, Software, Formal analysis, "
     "Investigation, Data curation, Visualization, Writing original draft.")
para(d, ("João Ferreira: ", "b"), "Supervision, Conceptualization, Validation, Writing review and editing." + JF)
h(d, "Funding")
para(d, "This research did not receive any specific grant from funding agencies in the public, commercial, "
        "or not-for-profit sectors." + EACH)
h(d, "Declaration of competing interest")
para(d, "The authors declare that they have no known competing financial interests or personal relationships "
        "that could have appeared to influence the work reported in this paper." + EACH)
h(d, "Data availability")
para(d, "The synthetic data and code are archived on Zenodo. Version 1.3.4, used for this article (includes "
        "sensitivity.py, which reproduces Table 3, and sensitivity_secondary.py, which reproduces the secondary-use, "
        "five-year and endpoint results in Section 5.2): " + VERSION_DOI + ". All versions (concept DOI, resolves "
        "to the latest version): " + CONCEPT_DOI + ". An anonymised copy of the code and synthetic data is "
        "supplied as supplementary material for review. No real patient data were used.")
d.save("Title_page.docx")

# ---------------- Cover letter
d = new()
para(d, "To the Editor,"); para(d, "Computer Law & Security Review")
para(d, "Date:" + FILL[:-1] + " on submission]")
para(d, ("Submission of a research article: ", "b"), ("\u201c" + TITLE + "\u201d", "i"))
para(d, "Dear Editor,")
para(d, "We submit the enclosed manuscript for consideration as a research article in Computer Law & Security "
        "Review. A health data access body investigating a research permit may need to establish which patients a "
        "query selected and which result left the secure processing environment. Those are different findings. The "
        "article examines the evidence each requires under Articles 68 and 73 of the European Health Data Space "
        "Regulation, and the circumstances in which Article 17 GDPR also requires a field to be erased.")
para(d, "Its contribution is a field-level test for a later dispute. Two queries can return the same aggregate even "
        "though one omitted a condition in the permit. A record of approval shows who approved the operation; "
        "establishing which filter ran needs evidence tied to its execution. In a fixed simulation of 100 "
        "secondary-use access events, 53 had conflicting requirements for readable data when the permit deadline "
        "covered logged health data and nine when audit fields fell outside its scope. The counts show the practical "
        "consequence of a disputed reading for the same events; they are not prevalence estimates.")
para(d, "The manuscript is original, has not been published elsewhere and is not under consideration by another "
        "journal. All authors have approved the submission.")
para(d, "For the editor only: the article derives from the first author's MSc thesis at Molde University College "
        "(Høgskolen i Molde). The public thesis repository also contains an earlier draft of this manuscript; we "
        "disclose both for editorial assessment. To preserve double anonymised review, the manuscript does not cite "
        "the thesis, its repository or the code DOI; the archived code is identified on the title page.")
para(d, "In line with the journal's double anonymised review, we supply the title page (with author details, "
        "acknowledgments and declarations) separately from the anonymised manuscript. Figures are supplied as "
        "separate files, tables are editable, and the code archive supplied as supplementary material is "
        "anonymised for review.")
para(d, "The manuscript contains the section \u201cDeclaration of generative AI and AI-assisted technologies in the "
        "manuscript preparation process\u201d before the references." + JF[:-1] + ": sign-off of that section]")
para(d, "The second author, as the first author's supervisor, has seen the manuscript and recommends it for "
        "publication." + JF)
para(d, "Yours sincerely,")
para(d, "Arshad Akhtar Abbasia (corresponding author), arshad.a.abbasia@himolde.no")
para(d, "João Ferreira" + JF[:-1] + ": name form]")
para(d, "Molde University College (Høgskolen i Molde), P.O. Box 2110, 6402 Molde, Norway" + JF[:-1] + ": affiliation]")
d.save("Cover_letter.docx")

# ---------------- Declaration of competing interest
d = new()
h(d, "Declaration of competing interest", 14)
para(d, ("Manuscript title: ", "b"), TITLE)
para(d, "The authors declare that they have no known competing financial interests or personal relationships "
        "that could have appeared to influence the work reported in this paper." + EACH)
para(d, "[Nothing to declare. In Editorial Manager select: \u201cI have nothing to declare.\u201d]")
para(d, "Authors: Arshad Akhtar Abbasia, João Ferreira")
d.save("Declaration_of_competing_interest.docx")
print("ancillary docx written")
