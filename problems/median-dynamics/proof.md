# A six-vertex counterexample to time-monotonicity in median dynamics

## Statement and source

Amir, Baldasso and Beilin, *Majority dynamics and the median process:
connections, convergence and some new conjectures*, arXiv:1911.08613v2,
Conjectures 3.1 and 3.2:
https://arxiv.org/html/1911.08613v2#S3

For any graph and iid Bernoulli(p) initial bits with p<=1/2, the probability
of bit 1 at each vertex is conjectured to be non-increasing in time.
Every vertex has a rate-one Poisson clock and takes its neighbors' majority;
ties retain its own bit. This is precisely the thresholded median process.
The imported database statement omitted evaluation of its marginal measure
at alpha. We use the full primary statement, not that transcription defect.

## Counterexample

Take vertices 0,1,2,3,4,5 and edges

    01, 04, 05, 12, 23, 25, 34, 35, 45.

Start with iid Bernoulli(1/4) bits. Let m(t) be the probability that vertex 1
has bit 1 at time t. Exact finite-state computation gives

    m'(t) = (18t^2 - 93t - 275)e^(-t)/3072
          + 27(t+1)e^(-3t)/3072 - 40e^(-4t)/3072.

Consequently

    m'(8) = [133e^(-8) + 243e^(-24) - 40e^(-32)]/3072 > 0,

since 133e^(-8) > 40e^(-32). The conjectured non-increasing marginal
therefore fails. Initially m'(0)=-3/32, so it actually changes direction.
By complement symmetry, the p=3/4 marginal decreases at time8, contradicting
the non-decreasing version in database ID30004591.

## Reproducible derivation and independent certificate

There are only 64 bit configurations s. For a configuration let r(s) be the
number of vertices that would change their bit if updated, and let s^v be
the result of such a change. Let f(s) be the bit at vertex1 and
g(s)=sum_v(f(s^v)-f(s)), summing only changing updates.

Every change strictly decreases the number of disagreeing edges: a vertex
changes only when strictly more than half its neighbors disagree. Thus the
following exact rational recurrence is evaluated in increasing order of
disagreeing-edge count, without solving a large symbolic linear system:

    u_s(z) = [g(s) + sum_{changing v} u_{s^v}(z)] / [z+r(s)].

For stable s the numerator is zero. This is the resolvent equation
(zI-Q)u=g, hence u_s is the Laplace transform of E_s[g(X_t)]. Average with
weights 3^(6-popcount(s))/4096 to obtain the Laplace transform of m'(t).
Partial fractions give the displayed formula. `closed_form.py` implements
this recurrence with exact SymPy rational arithmetic and saves its result
in `closed_form.txt`.

Separately, `verify.py` uses only Python integers and Fraction. It expands
the uniformized chain to degree220 and bounds the entire omitted tail by
a geometric series. It proves the explicit inequality m'(8)>1/100000,
without floating-point arithmetic or the closed-form derivation.

Run from the project root:

    python problems/median-dynamics/verify.py
    python problems/median-dynamics/closed_form.py

Both passed. A Luna subagent independently reconstructed the generator and
numerical derivative, then audited and ran the rational tail certificate.
Numerical derivative: approximately 0.0000145236128529.

## Scope and provenance

This is a full counterexample to the cited time-monotonicity statement,
not a proof concerning all other median-dynamics conjectures. The graph
is simple and connected, but not regular or vertex-transitive.
We do not claim minimality: atlas screening stopped after its first hit,
and absence of earlier numerical hits is not an exact exclusion.

The witness was found locally by `atlas_search.py` after 106 connected
graphs (3.16 seconds). Earlier complete-bipartite screening tested48 graphs
at three biases and49 times, without a hit (4.57 seconds).

Novelty is unestablished. Initial targeted web searches did not identify an
existing refutation, but they are not a comprehensive literature audit.
No author contact or publication has been made.
