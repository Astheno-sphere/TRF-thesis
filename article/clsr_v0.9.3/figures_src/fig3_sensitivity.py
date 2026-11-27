"""Figure 3 (double column, 190 mm): the six sensitivity scenarios as four dumbbell panels on one
shared scale. Every value is parsed from docs/expected_sensitivity_output.txt (no number typed in)."""
import re
import matplotlib.pyplot as plt
from style import CHARCOAL, OXBLOOD, INK2, RULE, MM, DOUBLE, export, read_archive

txt = read_archive("docs/expected_sensitivity_output.txt")
rows = [tuple(m.groups()) for m in re.finditer(
    r"^\s*(\d+)\s+(applies|excluded)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*$", txt, re.M)]
assert len(rows) == 6, rows
seed = re.search(r"seed=(\d+)", txt).group(1)
floors = sorted({int(r[0]) for r in rows}, reverse=True)
data = {(int(f), c): tuple(map(int, rest)) for f, c, *rest in rows}

FS_H, FS = 8.5, 8
panels = ["Plaintext records\nwith a violation", "Plaintext violations",
          "Accountability-preserving\nviolations", "Scheduled payload\ninvalidations"]
vmax = max(v for vals in data.values() for v in vals)
xmax = 25 * (int(vmax / 25) + 1)                      # shared scale, rounded up

fig = plt.figure(figsize=(DOUBLE, 64 * MM))
left, right, gap = 0.105, 0.985, 0.022
pw = (right - left - 3 * gap) / 4
axes = [fig.add_axes([left + k * (pw + gap), 0.17, pw, 0.58]) for k in range(4)]
for k, ax in enumerate(axes):
    for i, f in enumerate(floors):
        a, x = data[(f, "applies")][k], data[(f, "excluded")][k]
        ax.plot([x, a], [i, i], color=RULE, lw=1.4, zorder=1)
        sq = 6.4 if a == x else 4.0          # coincident values: hollow square drawn around the dot
        ax.plot([x], [i], "s", ms=sq, mfc="white", mec=CHARCOAL, mew=0.9, zorder=3)
        ax.plot([a], [i], "o", ms=3.4 if a == x else 4.6, color=OXBLOOD, zorder=4)
        if a == x:   # coincident: one label for both
            ax.text(a + xmax * 0.085, i, str(a), va="center", ha="left", fontsize=FS, color=CHARCOAL)
        else:
            ax.text(a + xmax * 0.045, i, str(a), va="center", ha="left", fontsize=FS, color=OXBLOOD)
            ax.text(x - xmax * 0.045, i, str(x), va="center", ha="right", fontsize=FS, color=CHARCOAL)
    ax.set_xlim(-xmax * 0.17, xmax * 1.2)
    ax.set_ylim(len(floors) - 0.5, -1.1)
    ax.set_xticks(range(0, xmax + 1, 50))
    ax.tick_params(axis="x", length=2, labelsize=FS, colors=INK2, pad=2)
    ax.set_yticks(range(len(floors)))
    ax.set_yticklabels([f"{f} months" for f in floors] if k == 0 else [])
    ax.tick_params(axis="y", length=0, labelsize=FS, colors=CHARCOAL, pad=4)
    ax.grid(axis="x", color=RULE, lw=0.4)
    ax.set_axisbelow(True)
    for sp in ("left", "right", "top"):
        ax.spines[sp].set_visible(False)
    ax.spines["bottom"].set_color(INK2)
    ax.text(0, 1.3, panels[k], transform=ax.transAxes, ha="left", va="top",
            fontsize=FS_H, fontweight="semibold", linespacing=1.15)

# direct labels for the two marks, in the last panel (widest separation) above its top row
ax3 = axes[3]
a0, x0_ = data[(floors[0], "applies")][3], data[(floors[0], "excluded")][3]
ax3.text(a0, -0.5, "ceiling\napplies", ha="center", va="bottom", fontsize=FS, color=OXBLOOD, linespacing=1.1)
ax3.text(x0_, -0.5, "ceiling\nexcluded", ha="center", va="bottom", fontsize=FS, color=CHARCOAL, linespacing=1.1)
axes[0].text(-0.03, 0.97, "Primary-use\nfloor", transform=axes[0].transAxes, ha="right", va="bottom", fontsize=FS, color=INK2, linespacing=1.1)
fig.text(right, 0.02, f"Synthetic cohort, seed {seed}", ha="right", va="bottom",
         fontsize=FS, color=INK2)
export(fig, "Figure_3")
