"""
Bounded SMT check of Propositions 1-3 (optional module)
========================================================
An independent check of the TRF Model's propositions in a different formalism from the
checker. trf_checker.py evaluates 200 generated records; this module asks the Z3 SMT solver
whether ANY record, with ANY parameter values inside the stated bounds, contradicts a
proposition. Every check is posed as "find a counterexample"; the expected answer is
"unsat" (no counterexample exists within the bounds).

Model (Chapter 4, Sections 4.3-4.6), one record, months t = 0..H:
  alpha_t        payload accessible at month t (free Boolean per month)
  C1 floor       alpha_t for t in [t_a, t_a + F]                       (Semantics I: V = alpha)
  C2 right       not alpha_t for t >= t_r + delta, if a request arrives
  C3 ceiling     not alpha_t for t >= e + L, if a ceiling applies (e: its anchor event)
Semantics II (Proposition 2) adds the accountability state: the accessor fields and the
commitment are kept, and an invalidation entry exists from the invalidation month on.

Bounds: t_a in [0, 12], F in [1, 24], delta in [1, 3], request month and anchor event in
[t_a, H], L in [1, 24], H = 64 (large enough that every window and deadline fits).
This is a bounded check: it covers every combination within the bounds, not all integers.
It checks that the propositions follow from the constraints as encoded here; like the
checker, it does not check that the constraints translate the law (Section 4.2 does that).

Run:  pip install z3-solver   then   python3 z3_check.py
"""

from z3 import And, Bool, If, Implies, Int, Not, Or, Solver, sat, unsat

H = 64
T = range(H + 1)


def record():
    """Symbolic parameters and constraints common to every check."""
    ta, F, d = Int("t_a"), Int("F"), Int("delta")
    tr, e, L = Int("t_r"), Int("e"), Int("L")
    req, ceil = Bool("request"), Bool("ceiling")
    alpha = [Bool(f"alpha_{t}") for t in T]
    bounds = And(ta >= 0, ta <= 12, F >= 1, F <= 24, d >= 1, d <= 3,
                 tr >= ta, tr <= H, e >= ta, e <= H, L >= 1, L <= 24)
    return ta, F, d, tr, e, L, req, ceil, alpha, bounds


def C1(alpha, ta, F):
    return And([Implies(And(ta <= t, t <= ta + F), alpha[t]) for t in T])


def C2(alpha, req, tr, d):
    return And([Implies(And(req, t >= tr + d), Not(alpha[t])) for t in T])


def C3(alpha, ceil, e, L):
    return And([Implies(And(ceil, t >= e + L), Not(alpha[t])) for t in T])


def check(name, formula):
    s = Solver()
    s.add(formula)
    r = s.check()
    print(f"{name:<74} {'unsat (no counterexample)' if r == unsat else 'SAT: ' + str(s.model())}")
    return r == unsat


def main():
    print("=" * 100)
    print("BOUNDED SMT CHECK OF PROPOSITIONS 1-3 (Z3)".center(100))
    print("=" * 100)
    print(f"bounds: t_a 0..12, F 1..24, delta 1..3, t_r and e in [t_a, {H}], L 1..24, horizon {H}")
    ok = []
    ta, F, d, tr, e, L, req, ceil, alpha, B = record()

    # Proposition 1, infeasibility direction: if a deadline falls inside the window,
    # no accessibility trajectory satisfies C1, C2 and C3 under Semantics I.
    inside = Or(And(req, tr + d <= ta + F), And(ceil, e + L <= ta + F))
    ok.append(check("P1  deadline inside window => no trajectory satisfies C1-C3 (Sem I)",
                    And(B, inside, C1(alpha, ta, F), C2(alpha, req, tr, d), C3(alpha, ceil, e, L))))

    # Proposition 1, boundary: if no deadline falls inside the window, the trajectory
    # "accessible until the earliest deadline" satisfies all three. Counterexample = it fails.
    dl = If(req, If(ceil, If(tr + d < e + L, tr + d, e + L), tr + d), If(ceil, e + L, H + 1))
    witness = [t < dl for t in T]
    ok.append(check("P1  no deadline inside window => witness trajectory satisfies C1-C3",
                    And(B, Not(inside),
                        Not(And(C1(witness, ta, F), C2(witness, req, tr, d), C3(witness, ceil, e, L))))))

    # Proposition 2: under Semantics II the constructive trajectory (accessible until
    # t_I = earliest deadline, then an invalidation entry) satisfies C1, C2 and C3 for
    # every arrival pattern and floor. V_II(t) = kept(m_acc) and kept(c) and
    # (alpha_t or logged_t); the construction never removes m_acc or c.
    tI = dl
    traj = [t < tI for t in T]
    logged = [t >= tI for t in T]
    V2 = [And(True, True, Or(traj[t], logged[t])) for t in T]
    C1_II = And([Implies(And(ta <= t, t <= ta + F), V2[t]) for t in T])
    ok.append(check("P2  constructive trajectory satisfies C1 (Sem II), C2, C3 for all inputs",
                    And(B, Not(And(C1_II, C2(traj, req, tr, d), C3(traj, ceil, e, L))))))

    # Proposition 3: floor F from t_a, ceiling L from e >= t_a, Semantics I.
    # (a) collision whenever e + L <= t_a + F: no trajectory satisfies floor and ceiling.
    both = And(C1(alpha, ta, F), C3(alpha, True, e, L))
    ok.append(check("P3  e + L <= t_a + F => floor and ceiling not jointly satisfiable",
                    And(B, e + L <= ta + F, both)))
    # (b) no collision whenever e + L > t_a + F: accessible-until-(e+L) satisfies both.
    w3 = [t < e + L for t in T]
    ok.append(check("P3  e + L > t_a + F => witness satisfies floor and ceiling",
                    And(B, e + L > ta + F, Not(And(C1(w3, ta, F), C3(w3, True, e, L))))))
    # (i) same anchor (e = t_a): satisfiable for the record iff L > F.
    ok.append(check("P3(i)  e = t_a: jointly satisfiable only if L > F",
                    And(B, e == ta, L <= F, both)))
    ok.append(check("P3(i)  e = t_a and L > F: witness satisfies floor and ceiling",
                    And(B, e == ta, L > F, Not(And(C1(w3, ta, F), C3(w3, True, e, L))))))
    # (ii) external anchor with L <= F: collision exactly when e - t_a <= F - L.
    ok.append(check("P3(ii) L <= F, e - t_a <= F - L => collision",
                    And(B, L <= F, e - ta <= F - L, both)))
    ok.append(check("P3(ii) L <= F, e - t_a >  F - L => witness satisfies both",
                    And(B, L <= F, e - ta > F - L, Not(And(C1(w3, ta, F), C3(w3, True, e, L))))))

    # Sanity: the encoding can return sat, so unsat above is not an artefact of a broken model.
    s = Solver(); s.add(B, Not(req), Not(ceil), C1(alpha, ta, F))
    sanity = s.check() == sat
    print(f"{'sanity: no request, no ceiling => some trajectory satisfies C1':<74} {'sat (as expected)' if sanity else 'UNSAT: encoding broken'}")
    # Mutation checks: deliberately wrong versions of Proposition 3 must be refuted (sat),
    # showing the checks are sensitive to an off-by-one in the condition.
    m1 = Solver(); m1.add(B, e + L <= ta + F + 1, both)       # claims collision one month too late
    m2 = Solver(); m2.add(B, e + L > ta + F - 1, Not(And(C1(w3, ta, F), C3(w3, True, e, L))))
    mut = m1.check() == sat and m2.check() == sat
    print(f"{'mutation: Proposition 3 with an off-by-one condition is refuted':<74} {'sat, counterexample found (as expected)' if mut else 'UNSAT: checks insensitive'}")
    sanity = sanity and mut
    print("=" * 100)
    print(f"RESULT: {sum(ok)}/{len(ok)} checks found no counterexample; sanity and mutation checks {'passed' if sanity else 'FAILED'}")
    print("=" * 100)


if __name__ == "__main__":
    main()
