"""Figure 2 (double column, 190 mm): crypto-erasure by invalidation for one audit record.
Labels follow Sections 3.3 and 4.1 and the code archive (trf_checker.apply_invalidation, V_II).
Drawn in millimetre coordinates: four stages on a time rule, the append-only log below,
and the two state lines x(t) and V(t) at the foot."""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from style import CHARCOAL, OXBLOOD, GOLD, INK2, GREY, RULE, PALE, MM, DOUBLE, export

FS_H, FS, FS_S = 8.5, 8, 8       # heading, body, small (pt) at 190 mm
Wfig, Hfig = 190, 84
fig = plt.figure(figsize=(DOUBLE, Hfig * MM))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, Wfig); ax.set_ylim(0, Hfig); ax.axis("off")

def arrow(p0, p1, color=CHARCOAL):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=6, color=color,
                                 lw=0.6, shrinkA=0, shrinkB=0))

# ---- stages: columns on a shared time rule --------------------------------------------
x0, colw = 4, 45.5
cols = [x0 + i * colw for i in range(4)]
ytop = 80
stages = [
    ("Creation, month $s$", CHARCOAL,
     ["authenticate access event", "log accessor evidence $A$", "commit to payload $P$",
      "commit to patient link $J$", "encrypt $P$ under data key"]),
    ("Retained evidence", CHARCOAL,
     ["$A$ readable to auditors", "commitments $c(P)$, $c(J)$", "inclusion proofs",
      "against the log root", "$x(t) = 1$ before $d$"]),
    ("Binding deadline $d$", OXBLOOD,
     ["destroy key and opening", "delete ciphertext of $P$", "remove $J$ at its own deadline",
      "append invalidation entry"]),
    ("Audit within $W$", CHARCOAL,
     ["verify $A$ and event entry", "verify commitment inclusion", "verify invalidation entry",
      "payload not recoverable", "$V(t) = 1$ across $W$"]),
]
for i, (title, col, lines) in enumerate(stages):
    x = cols[i]
    ax.text(x, ytop, str(i + 1), ha="left", va="top", fontsize=FS_H, color=col, fontweight="semibold")
    ax.text(x + 4, ytop, title, ha="left", va="top", fontsize=FS_H, color=col, fontweight="semibold")
    ax.plot([x, x + colw - 5], [ytop - 5.2, ytop - 5.2], color=col if col == OXBLOOD else CHARCOAL,
            lw=0.9 if col == OXBLOOD else 0.5)
    for k, ln in enumerate(lines):
        ax.text(x, ytop - 8.2 - k * 4.1, ln, ha="left", va="top", fontsize=FS, color=CHARCOAL)
    if i < 3:   # sequence marker between stages, on the heading line
        arrow((x + colw - 4.2, ytop - 5.2), (x + colw - 1.0, ytop - 5.2), color=GREY)

# ---- append-only log --------------------------------------------------------------------
ly, lh = 30, 7.5
ax.text(x0, ly - 2.0, "Append-only Merkle log (RFC 6962 hashing)", ha="left", va="top",
        fontsize=FS_H, fontweight="semibold")
leaves = [("event entry", 26, CHARCOAL, "white", CHARCOAL),
          ("...", 9, "white", INK2, RULE),
          ("other records", 30, "white", INK2, RULE),
          ("...", 9, "white", INK2, RULE),
          ("invalidation entry", 31, OXBLOOD, "white", OXBLOOD)]
lx, centres = x0, []
for lab, w, fc, tc, ec in leaves:
    ax.add_patch(Rectangle((lx, ly), w, lh, fc=fc, ec=ec, lw=0.6))
    ax.text(lx + w / 2, ly + lh / 2, lab, ha="center", va="center", fontsize=FS, color=tc)
    centres.append(lx + w / 2)
    lx += w + 1.5
log_end = lx - 1.5
# links from stages to their log entries
yfoot = ytop - 8.2 - 4 * 4.1 - 4.5
arrow((centres[0], yfoot), (centres[0], ly + lh + 0.4))
arrow((centres[4], yfoot + 4.1), (centres[4], ly + lh + 0.4), color=OXBLOOD)
# auditor checks the root
xa = cols[3] + 10
ax.plot([log_end + 1.0, xa], [ly + lh / 2, ly + lh / 2], color=CHARCOAL, lw=0.6)
arrow((xa, ly + lh / 2), (xa, yfoot))
ax.text(xa + 2.0, (ly + lh / 2 + yfoot) / 2, "root checked\nby the auditor", ha="left", va="center",
        fontsize=FS, color=CHARCOAL, linespacing=1.2)

# ---- state lines at the foot ------------------------------------------------------------
xd = cols[2]                                  # deadline d
xW0, xW1 = cols[0], cols[3] + colw - 5        # retention window W, schematic
ys1, ys2 = 14, 6.5
def state(y, label):
    ax.text(x0, y + 2.2, label, ha="left", va="bottom", fontsize=FS, color=CHARCOAL)
state(ys1, r"Payload $x(t)$: readable until $d$, unavailable from $d$")
ax.add_patch(Rectangle((xW0, ys1), xd - xW0, 1.6, fc=GREY, ec="none"))
ax.add_patch(Rectangle((xd, ys1), xW1 - xd, 1.6, fc="white", ec=GREY, lw=0.5))
state(ys2, r"Verification $V(t)$: retained evidence and invalidation entries, throughout $W$")
ax.add_patch(Rectangle((xW0, ys2), xW1 - xW0, 1.6, fc=CHARCOAL, ec="none"))
# deadline mark through both lines
for yy in (ys1, ys2):
    ax.plot([xd, xd], [yy - 1.0, yy + 2.6], color=OXBLOOD, lw=0.9)
ax.text(xd, ys2 - 2.0, "$d$", ha="center", va="top", fontsize=FS, color=OXBLOOD)
ax.text(xW1, ys2 - 2.0, "end of $W$", ha="right", va="top", fontsize=FS, color=INK2)

export(fig, "Figure_2")
