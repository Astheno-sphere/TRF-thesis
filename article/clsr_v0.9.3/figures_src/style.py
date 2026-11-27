"""Shared figure style (v0.9.1): editorial palette, Inter (pinned), sizes in millimetres at final print width.

Final widths: single column 90 mm, double column 190 mm. Minimum text size 7 pt at final width;
double-column figures use 8 pt or more so that a Word page (160 mm text width) still prints >= 6.7 pt.
Export: vector PDF (fonts embedded), 600 dpi PNG, 1000 dpi TIFF.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

# palette: charcoal ink, oxblood as the single accent, gold sparingly, greys for structure
CHARCOAL = "#1B1C20"
OXBLOOD = "#5E1A21"
GOLD = "#C9A23A"
INK2 = "#55565B"      # secondary text, 7.4:1 on white
GREY = "#8A8A8E"      # mid grey fills
RULE = "#BDBDC0"      # hairlines and gridlines
PALE = "#ECECEE"      # pale fill

MM = 1 / 25.4
SINGLE, DOUBLE = 90 * MM, 190 * MM

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "Figures")
ARCHIVE = os.environ.get("REVIEW_CODE", os.path.join(HERE, "..", "..", "review_code"))

# Pinned font: Inter (SIL OFL 1.1) converted from the OTF release to TrueType outlines with fontTools
# and renamed "InterFig" (figures_src/fonts). TrueType keeps the PDF embedding clean (Type 42);
# the CFF-based OTF produced font-type mismatch warnings. No fallback: a different face would change
# every label width that was checked by eye.
FONT_DIR = os.path.join(HERE, "fonts")
for _f in ("Inter-Regular.ttf", "Inter-Italic.ttf", "Inter-SemiBold.ttf"):
    font_manager.fontManager.addfont(os.path.join(FONT_DIR, _f))
FONT = "InterFig"
if FONT not in {f.name for f in font_manager.fontManager.ttflist}:
    raise SystemExit("figure font InterFig not found in figures_src/fonts")

plt.rcParams.update({
    "font.family": FONT, "font.size": 8,
    "mathtext.fontset": "custom", "mathtext.rm": FONT, "mathtext.it": FONT + ":italic",
    "mathtext.bf": FONT + ":bold", "mathtext.sf": FONT,
    "axes.edgecolor": CHARCOAL, "axes.labelcolor": CHARCOAL, "text.color": CHARCOAL,
    "xtick.color": INK2, "ytick.color": INK2, "axes.linewidth": 0.5,
    "xtick.major.width": 0.5, "ytick.major.width": 0.5,
    "pdf.fonttype": 42, "ps.fonttype": 42, "svg.fonttype": "none",
    "hatch.linewidth": 0.5, "hatch.color": CHARCOAL,
    "lines.solid_capstyle": "butt",
})


def export(fig, name):
    os.makedirs(OUT, exist_ok=True)
    base = os.path.join(OUT, name)
    meta_pdf = {"Creator": None, "Producer": None, "Author": None, "Title": name}
    fig.savefig(base + ".pdf", metadata=meta_pdf)
    fig.savefig(base + ".png", dpi=600, metadata={"Software": None})
    fig.savefig(base + ".tif", dpi=1000, pil_kwargs={"compression": "tiff_lzw"})
    plt.close(fig)
    print("wrote", base + ".{pdf,png,tif}")


def read_archive(rel):
    with open(os.path.join(ARCHIVE, rel), encoding="utf-8") as fh:
        return fh.read()
