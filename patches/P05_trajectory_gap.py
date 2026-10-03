# P05 — gap in P04's proof extension, found on re-reading before commit.
# P04-13 said that when an erasure request fixes t^I before the ceiling, the subject fields are
# removed at t_pi + 6 "by the same rule", but step 2 only removes them when the ground at t^I is
# Art 68(12). The trajectory now has an explicit step for that case, and the C3 argument cites it.

EDITS = [
    dict(id="P05-01", file="Chapter4_TRF_Model_v1.md",
         old="3. For $t > t^{I}(a)$: set $\\alpha(a,t) = 0$, and $\\beta(a,t) = 0$ where step 2 removed the subject fields. Retain $m_{acc}(a), c(a)$, and $\\iota(a)$.",
         new="3. For $t > t^{I}(a)$: set $\\alpha(a,t) = 0$, and $\\beta(a,t) = 0$ where step 2 removed the subject fields. Retain $m_{acc}(a), c(a)$, and $\\iota(a)$.\n4. If C3 reaches the subject fields and $t^{I}(a) < t_\\pi(a) + 6$, so that an erasure request fixed the invalidation month, remove $m_{subj}(a)$ at $t_\\pi(a) + 6$, set $\\beta(a,t) = 0$ from that month, and append a second entry to $\\iota(a)$ recording it.",
         why="P04 gap: explicit step for the subject link when Art 17 fixed t^I earlier"),
    dict(id="P05-02", file="Chapter4_TRF_Model_v1.md",
         old="If $t^{I}(a)$ was set by an earlier erasure request, the subject fields are removed at $t_\\pi(a) + 6$ by the same rule.",
         new="If $t^{I}(a)$ was set by an earlier erasure request, step 4 removes the subject fields at $t_\\pi(a) + 6$.",
         why="P04 gap: the C3 argument now cites the step that does the work"),
]
