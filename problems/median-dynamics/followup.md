# Regular-graph counterexample and convexity screening

The time-monotonicity refutation extends to simple cubic graphs. Take
vertices0..9 with edges

    01,06,02,15,13,25,28,34,39,49,47,56,68,79,78.

Every vertex has degree3, so ties never occur. With independent Bernoulli(2/5)
initial states, vertex1 has m'(10)>9/10000000>0. The rate at each vertex is1.
This refutes time-monotonicity even restricted to regular graphs; it is a
strengthening of the same conjecture's refutation, not a second solved problem.
No assertion of vertex transitivity or novelty is made.

`verify_regular.py` constructs all1024 states explicitly and checks the sign
using integer and Fraction arithmetic. For H counting all10 clock events,
Q=H-10I. The code sums exp(100)m'(10) through degree400 and bounds the whole
omitted exponential tail geometrically using |pi(H/10)^k Qf|<=1. It also checks
degree3 and m'(0)=-6/125. Runtime about0.4seconds excluding interpreter startup.
`regular_certificate.json` records the exact certified bound. Numerical
screening found it after14 connected draws, seed20260910, in0.57seconds.

