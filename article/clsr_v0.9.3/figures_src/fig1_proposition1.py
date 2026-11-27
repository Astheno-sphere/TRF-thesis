"""Figure 1 (single column, 90 mm): Proposition 1 on the monthly grid for the worked example
(record 100). Values are parsed from docs/expected_trf_output.txt, not retyped."""
import re
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from style import CHARCOAL, OXBLOOD, INK2, GREY, RULE, MM, SINGLE, export, read_archive

txt = read_archive("docs/expected_trf_output.txt")
F = int(re.search(r"floors: cross-border=\d+, SPE=(\d+)", txt).group(1))
L = int(re.search(r"ceiling=(\d+)", txt).group(1))
m = re.search(r"rid=100: t_a=(\d+) permit expires t_pi=(\d+) -> C3 from t=(\d+), C1 to t=(\d+)\s+\| collision at t=(\d+)", txt)
s, e, d, end, coll = map(int, m.groups())
assert d == e + L and end == s + F and coll == max(s, d) and d <= s + F

T = end + 4                      # months shown: 0 .. T
FS, FS_S = 7.5, 7                # body and small text (pt) at 90 mm
fig = plt.figure(figsize=(SINGLE, 64 * MM))
ax = fig.add_axes([0.035, 0.0, 0.93, 1.0])
ax.set_xlim(-0.7, T + 0.7)
ax.set_ylim(-3.35, 4.2)
ax.axis("off")

H = 0.46                          # cell height
def cells(y, months, **kw):
    for t in months:
        ax.add_patch(Rectangle((t - 0.42, y - H / 2), 0.84, H, lw=0.5, **kw))

def row_label(y, text, color=CHARCOAL, weight="normal"):
    ax.text(-0.42, y + H / 2 + 0.16, text, ha="left", va="bottom", fontsize=FS, color=color,
            fontweight=weight, zorder=4, bbox=dict(fc="white", ec="none", pad=0.6))

# guides at the four events: solid hairlines, behind everything
for t in (s, e, d, end):
    ax.plot([t, t], [-1.25, 3.05], color=RULE, lw=0.4, zorder=0)

# row 1: floor
y1 = 2.0
cells(y1, range(s, end + 1), facecolor=GREY, edgecolor=GREY)
row_label(y1, r"Floor: $V(t) = 1$, so $x(t) = 1$")
# retention window bracket above the floor row
yb = 3.55
ax.plot([s, s, end, end], [yb - 0.14, yb, yb, yb - 0.14], color=CHARCOAL, lw=0.5)
ax.text((s + end) / 2, yb + 0.12, r"$W = \{s, \ldots, s + F\}$,  $F = %d$ months" % F,
        ha="center", va="bottom", fontsize=FS_S)

# row 2: ceiling
y2 = 0.85
cells(y2, range(d, T + 1), facecolor="white", edgecolor=CHARCOAL, hatch="//////")
row_label(y2, r"Ceiling: $x(t) = 0$ for $t \geq d$")

# row 3: conflict (the accent)
y3 = -0.3
cells(y3, range(max(s, d), end + 1), facecolor=OXBLOOD, edgecolor=OXBLOOD)
row_label(y3, "Conflict", color=OXBLOOD, weight="semibold")
ax.text(end + 0.75, y3, r"$d \leq s + F$" + "\ninfeasible", ha="left", va="center",
        fontsize=FS_S, color=OXBLOOD, linespacing=1.15)

# month axis
ya = -1.25
ax.plot([-0.5, T + 0.5], [ya, ya], color=CHARCOAL, lw=0.5)
for t in range(0, T + 1):
    ax.plot([t, t], [ya, ya - (0.14 if t % 2 == 0 else 0.07)], color=CHARCOAL, lw=0.4)
for t in range(0, T - 3, 4):
    ax.text(t, ya - 0.22, str(t), ha="center", va="top", fontsize=FS_S, color=INK2)
ax.text(T + 0.5, ya - 0.22, "month $t$", ha="right", va="top", fontsize=FS_S, color=INK2)

# event labels below the axis
ye = -2.0
for t, lab in [(s, "$s$"), (e, "$e$"), (d, "$d$"), (end, "$s + F$")]:
    ax.plot([t], [ya], marker="o", ms=2.6, color=OXBLOOD if t == d else CHARCOAL, zorder=3)
    ax.text(t, ye, f"{lab} = {t}", ha="center", va="top", fontsize=FS_S,
            color=OXBLOOD if t == d else CHARCOAL)
# ceiling length L between e and d
yl = -2.75
ax.plot([e, e, d, d], [yl + 0.12, yl, yl, yl + 0.12], color=CHARCOAL, lw=0.5)
ax.text((e + d) / 2, yl - 0.08, r"$L = %d$" % L, ha="center", va="top", fontsize=FS_S)

export(fig, "Figure_1")
