from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
wb=Workbook(); wb.remove(wb.active)
HF=PatternFill("solid",fgColor="4A148C"); HFont=Font(name="Arial",bold=True,color="FFFFFF",size=10)
CF=Font(name="Arial",size=10); WR=Alignment(wrap_text=True,vertical="top")
def tab(n,h,rows,w=None):
    ws=wb.create_sheet(n[:31]); ws.append(h)
    for c in range(1,len(h)+1):
        x=ws.cell(1,c); x.fill=HF; x.font=HFont; x.alignment=WR
    for r in rows: ws.append(list(r)+[""]*(len(h)-len(r)))
    for row in ws.iter_rows(min_row=2):
        for cell in row: cell.font=CF; cell.alignment=WR
    for i,width in enumerate((w or [16,46]+[26]*(len(h)-2))[:len(h)],1):
        ws.column_dimensions[get_column_letter(i)].width=width
    ws.freeze_panes="A2"

tab("00_READ_ME",["Item","Detail"],[
["Status","FINAL PATCH — 16 Sept 2026. Supersedes PATCH1/2/3 and MASTER. Copy each tab as one block."],
["Thesis state","All 7 chapters + front matter + Appendix A complete. Assembled full document produced."],
["Measured words","Front 2,057 | Ch1 4,744 | Ch2 11,107 | Ch3 4,449 | Ch4 6,958 | Ch5 3,270 | Ch6 4,209 | Ch7 2,083 | AppA 1,412 | TOTAL ~40,300 (~89pp)"],
["Page issue","89pp vs Joao's 80pp ceiling. Ch2 is the overrun. See tab 05."],
["Deliverables added","Consolidated_Bibliography.Rmd (67 entries, chapter-tagged); repro_package/ (self-verifying, byte-identity PASS)"],
])

tab("01_THIS_ROUND",["ID","Item","Resolution","Where"],[
["CORR-028","Ch5 had NO reference section while citing Synthea and basisprofiler","Reference section added (Walonoski 2018; HL7 Norway 2025); in-text citations inserted at first mention","Ch5 §5.2, §5.7, refs"],
["CORR-029","Ch1 cited '(NIST, 2025)' but reference entry is 'National Institute of Standards and Technology'","In-text harmonised to full name. Found by programmatic citation audit, not by eye","Ch1 §1.3"],
["CORR-030","F-06 unresolved (TEHDAS2 deliverable number)","RESOLVED: D7.4 'Technical specification for health data access bodies on the implementation of secure processing environments'. Also confirmed D7.2 (minimisation/pseudonymisation/anonymisation/synthetic data) and D6.3","Ch2, Ch3, Ch4, Ch6"],
["CORR-031","Theorem 2 vulnerable to 'you defined your way out' objection","Candour passage added: concedes the mathematical content is modest and the proof is verification not discovery; states Theorem 1 carries the load; Semantics II defensibility argued in §4.2, authority confronted in §6.2","Ch4 §4.7"],
["CORR-032","Art 68(12) broad reading asserted as fact (SELF-CAUGHT FALLACY)","Proposal Art 46(9) text reads 'The data within the secure processing environment shall be deleted within 6 months' — broad by location but sits in the data-permit article. Now stated as contestable, with a map of what depends on it: Cor 1.2 only; Thm 1, Cor 1.1, Thm 2, mechanism, residue all unaffected","Ch1, Ch2, Ch4 §4.6, Ch5 §5.4, Ch6 §6.2, Ch7 §7.4"],
["CORR-033","Front matter did not exist in rebuild; old draft's abstract/IRB claim still attached","Written fresh: abstract (520w, states limitations in the abstract), contribution statement with 'What is not claimed', ethics declaration WITHDRAWING the IRB claim by name, AI-assistance declaration, full nomenclature (model symbols + 27 abbreviations), TOC","Front_Matter_v1.md"],
])

tab("02_FETCH_REGISTER",["ID","Item","Status","Note"],[
["F-01","SPUHiN D5.2 full PDF","OPEN","Checklists verified; §6.6 absence claim already stated at reduced strength because of this"],
["F-02","EDPB CEF Art-17 full report","OPEN","Recurring-issue count deliberately removed rather than guessed"],
["F-03","EDPB Guidelines 02/2025 status","RESOLVED","v2.0 adopted 7 July 2026 after consultation — confirmed at edpb.europa.eu. Strengthens §4.9: metadata+content are in principle personal data, may extend to encrypted/hashed"],
["F-04","Aikebaier SoK","RESOLVED","Open problem #5 = our gap; #4 (ZKP selective disclosure) = our future work"],
["F-05","Haque et al. final venue","OPEN","arXiv cited; venue unconfirmed"],
["F-06","TEHDAS2 SPE deliverable number","RESOLVED","D7.4"],
["F-07","Albalwy full PDF","OPEN (optional)","Only if 113ms figure used; currently not"],
["F-08","EHDS implementing acts","RESOLVED","Art 73(5): due by 26 Mar 2027, not adopted"],
["F-09","Walonoski Synthea citation","RESOLVED","JAMIA 25(3):230-238 exact"],
["F-10","eHOMB '12 March' year","OPEN","Source has no year; chapters state date without asserting year"],
["F-11","EUR-Lex verbatim Art 73(1)(e)","SUBSTANTIALLY CORROBORATED","Full Art 73(1)(a)-(f) retrieved from two independent reproductions; official EUR-Lex text fetch returns page chrome"],
["F-12","EHDS in-force vs applies-from","RESOLVED","In force 26 Mar 2025; applies 26 Mar 2027; secondary use (Ch IV incl. Arts 68, 73) 26 Mar 2029"],
])

tab("03_DELIVERABLES",["Artefact","Detail","Status"],[
["Front_Matter_v1.md","Title, abstract, contribution statement, declarations, nomenclature, TOC","COMPLETE"],
["Chapter1-7 (7 files)","Individually maintained, cross-referenced, anti-drift swept","COMPLETE"],
["VERA-SNARK_Thesis_FULL_16Sept2026.md","Assembled: front matter + 7 chapters + Appendix A","COMPLETE"],
["Consolidated_Bibliography.Rmd","67 unique entries, de-duplicated across 7 chapter lists, alphabetised, chapter-provenance tagged, APA 7. Source-type flags (preprint/patent/commentary/guidance) visible in the list itself","COMPLETE"],
["repro_package/","README + run_all.sh + src/ + data/synthea_sample/ + results/ + docs/Appendix_A.md. Executed end-to-end; rerun byte-identical to reported run (PASS)","COMPLETE & SELF-VERIFIED"],
["Citation audit","Programmatic: every in-text (Author, year) matched against reference entries. 2 defects found and fixed (CORR-028, CORR-029)","COMPLETE"],
])

tab("04_OUTSTANDING",["Item","Priority","Note"],[
["Send Joao the update email","HIGHEST","Drafted, unsent. He has seen none of this. Highest-risk item on the project and unrelated to the text"],
["Viva preparation notes","HIGH","Nothing exists. 5 questions: where's the logistics; are access logs 'data within the environment'; are 1-12mo permits realistic; Semantics II has no authority; why informal proofs"],
["Chapter 2 reduction","HIGH","89pp vs 80pp ceiling. Ch2 = 11,107w. Cut targets: §2.2 and §2.7 background that Ch4/Ch6 restate; also the absence-of-literature argument leans harder than it should given provisions apply 2029"],
["Remaining fetches F-01/F-05/F-10/F-11","MEDIUM","Half a day, one sitting, none load-bearing"],
["Two figures","MEDIUM","Timeline (2025 in force -> 2027 acts -> 2029 secondary use); record-state diagram (payload -> commitment + invalidation + auditor view)"],
["Formatting / Rmd / PDF","LAST","Only after content freeze"],
])

tab("05_CH2_OVERRUN",["Section","Words (approx)","Assessment"],[
["NOTE","","'Overrun' = Ch2 is ~11,100 words against a planned ~7,000-8,000, and the thesis total is 89pp against Joao's 80pp ceiling. Ch2 is where the excess sits."],
["2.1 Review Strategy","~600","Keep"],
["2.2 Cross-Border Landscape","~1,500","CUT CANDIDATE — Ch1 §1.1 and Ch4 §4.11 restate much of the MyHealth@EU/NCPeH detail"],
["2.3 Retention vs Erasure Tension","~2,400","KEEP — carries Art 17(3)(b) defence, Art 73(1)(e), legal corridor. Load-bearing"],
["2.4 Cryptographic Approaches","~2,600","TRIM — comparator paragraphs (Health-zkIDM, zkFL-Health, NewbornTime) could compress; prior-art and PoSE passages must stay"],
["2.5 Formal Approaches","~700","KEEP — anchors the method"],
["2.6 Norwegian Infrastructure","~1,200","KEEP — the substrate argument"],
["2.7 Information Logistics","~800","CUT CANDIDATE — the maritime example and OECD figures are colour; the customs-ledger analogy alone carries the framing and also appears in Ch1 §1.4"],
["2.8 Comparative Analysis","~700","KEEP"],
["2.9 Research Gaps","~900","KEEP — but soften the absence-of-literature reliance (nobody writes about provisions applying in 2029)"],
["2.10 Positioning","~500","KEEP"],
["TARGET","~2,000 cut","Brings Ch2 to ~9,100 and the thesis to ~80pp before figures"],
])
wb.save("/mnt/user-data/outputs/Substrate_FINAL_PATCH_16Sept2026.xlsx"); print("final patch:",len(wb.worksheets),"tabs")
