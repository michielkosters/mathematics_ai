# A six-vertex counterexample to time monotonicity in majority dynamics

**Result.** On the graph below, rate-one majority dynamics started from independent Bernoulli(1/4) opinions has a vertex whose probability of opinion 1 initially decreases but is strictly increasing at time 8.

This refutes Conjectures 3.1 and 3.2 of Amir, Baldasso and Beilin, *Majority dynamics and the median process: connections, convergence and some new conjectures*, [arXiv:1911.08613v2, §3](https://arxiv.org/html/1911.08613v2#S3). They are equivalent formulations of one time-monotonicity claim. The construction was obtained in this project; **novelty is unestablished**.

## 1. The process and the conjecture

Each vertex has an independent Poisson clock of rate one. When its clock rings, it adopts its neighbours' majority opinion; in a tie, it keeps its current opinion. The clocks are independent of the initial opinions.

Write $X_t(v)\in\{0,1\}$ for the opinion of vertex $v$. Initially these bits are independent, each equal to 1 with probability $p$. Conjecture 3.2 asserts that, for $p\leq1/2$, every marginal

$$m_v(t)=\mathbb P(X_t(v)=1)$$

is non-increasing in time, on every graph.

The probability averages over **both the initial opinions and the random clocks**. A specially chosen deterministic update schedule would not refute this conjecture. We calculate the full continuous-time process.

## 2. The counterexample

Take vertices $0,1,2,3,4,5$ and the nine undirected edges

$$E=\{01,04,05,12,23,25,34,35,45\},$$

where $ij$ denotes the edge joining $i$ to $j$. Equivalently:

| Vertex | Neighbours |
|---|---|
| 0 | 1, 4, 5 |
| **1** | **0, 2** |
| 2 | 1, 3, 5 |
| 3 | 2, 4, 5 |
| 4 | 0, 3, 5 |
| 5 | 0, 2, 3, 4 |

Set $p=1/4$, observe vertex 1, and write $m(t)=\mathbb P(X_t(1)=1)$.

**Exact identity.** For all $t\geq0$,

$$
\boxed{\displaystyle
m'(t)=\frac{(18t^2-93t-275)e^{-t}+27(t+1)e^{-3t}-40e^{-4t}}{3072}.}
\tag{1}
$$

Section 3 derives this identity. Once established, the contradiction is immediate:

$$m'(8)=\frac{133e^{-8}+243e^{-24}-40e^{-32}}{3072}>0.$$

Indeed, $133e^{-8}>40e^{-32}$, and the remaining term is positive. Since $m'$ is continuous, $m$ increases on an interval around 8. It is therefore not non-increasing.

Initially $m'(0)=-3/32<0$, so the marginal actually changes direction. For scale only, $m'(8)\approx1.45236\times10^{-5}$. No numerical approximation is needed to establish its sign.

## 3. The finite calculation behind the identity

There are only 64 states. A decreasing integer statistic lets us compute the answer by rational recurrence, without simulation or numerical eigenvalues.

### Generator and initial distribution

A state is a bit vector $s=(s_0,\ldots,s_5)$. Let $A(s)$ be the vertices whose opinion would **change** if updated, let $s^v$ denote the state with bit $v$ flipped, and put $r(s)=|A(s)|$. The generator acts on functions of states by

$$ (Qh)(s)=\sum_{v\in A(s)}[h(s^v)-h(s)]. $$

For $f(s)=s_1$, only updating vertex 1 changes $f$. Thus $g=Qf$ is

$$
g(s)=\begin{cases}
1,&s_1=0,\ s_0=s_2=1,\\
-1,&s_1=1,\ s_0=s_2=0,\\
0,&\text{otherwise}.
\end{cases}
$$

With $|s|=\sum_vs_v$, the initial probability of state $s$ is

$$\pi(s)=3^{6-|s|}/4096.$$

Differentiating the finite Markov-chain semigroup gives $m'(t)=\pi e^{tQ}g$. As a quick check,

$$m'(0)=(1-p)p^2-p(1-p)^2=p(1-p)(2p-1)=-3/32.$$

### Why the recurrence terminates

Let $D(s)$ be the number of edges whose endpoints disagree. A vertex of degree $d$ flips only when $a>d/2$ of its neighbours disagree with it. Its flip changes $D$ by $d-2a<0$.

Every actual transition therefore decreases $D$. Null clock events are absent from $Q$. We may calculate quantities for states in increasing order of $D$, beginning with stable states.

### Exact rational identity

For $z>0$, define

$$u_s(z)=\int_0^\infty e^{-zt}\mathbb E_s[g(X_t)]\,dt.$$

The resolvent equation $(zI-Q)u=g$ gives

$$
\boxed{\displaystyle
u_s(z)=\frac{g(s)+\sum_{v\in A(s)}u_{s^v}(z)}{z+r(s)}.}
\tag{2}
$$

In a stable state $g(s)=0$, so $u_s=0$. Otherwise every function in the numerator has already been calculated at lower $D$.

Applying (2) to the 64 states, weighting by their initial probabilities, and collecting fractions gives

$$
\begin{aligned}
\widehat{m'}(z)
&=\frac1{4096}\sum_{s\in\{0,1\}^6}3^{6-|s|}u_s(z)\\
&=\frac1{3072}\left[
\frac{36}{(z+1)^3}-\frac{93}{(z+1)^2}-\frac{275}{z+1}
+\frac{27}{(z+3)^2}+\frac{27}{z+3}-\frac{40}{z+4}
\right].
\end{aligned}
\tag{3}
$$

Equations (2) and (3) are the finite algebraic part of the proof. The short script [closed_form.py](closed_form.py) constructs all states directly from the neighbour table, applies (2), and checks (3) as an **exact symbolic identity**. It also checks all 64 resolvent equations after construction. The result is derived from the graph, not assumed from a saved output file.

Finally,

$$
\mathcal L[e^{-at}](z)=\frac1{z+a},\qquad
\mathcal L[te^{-at}](z)=\frac1{(z+a)^2},\qquad
\mathcal L[t^2e^{-at}](z)=\frac2{(z+a)^3}.
$$

Applying these elementary identities to (3) proves (1).

## 4. A separate exact certificate of the sign

The standard-library script [verify.py](verify.py) does not use (1), Laplace transforms, or SymPy. It certifies $m'(8)>1/100000$ directly with rational arithmetic.

Let $Hh(s)$ be the sum of $h$ over the six possible clock updates, including updates that leave the state unchanged. Then $Q=H-6I$, and $P=H/6$ is stochastic. Hence

$$e^{48}m'(8)=\sum_{k=0}^\infty\frac{8^k}{k!}\pi H^kg.$$

Since $|g|\leq1$ and $P$ is stochastic, the absolute value of the $k$-th term is at most $48^k/k!$. After degree 220, the entire remaining tail is bounded by

$$R=\frac{48^{221}}{221!}\frac1{1-48/222}.$$

Writing $S$ for the exact partial sum, the script checks $S>R$ and then checks

$$
m'(8)\geq
\frac{S-R}{\sum_{k=0}^{220}48^k/k!+R}
>\frac1{100000}.
$$

The denominator bounds $e^{48}$ from above. This is a second way to establish the sign, with an explicit lower bound. The calculation is finite; its tail estimate covers every omitted term.

## 5. Median-process interpretation and scope

In the median process, initial opinions are independent uniforms on $[0,1]$. Thresholding by $1_{\{\eta_t(v)<p\}}$ gives the majority dynamics under the same clocks, as in the paper's Proposition 2.2. For even degree, the median rule includes the vertex's own opinion; this produces the keep-current-bit rule in a binary tie.

Therefore $\mathbb P(\eta_t(1)<1/4)=m(t)$. Its positive derivative also refutes Conjecture 3.1, the median-process version.

The graph is finite, simple and connected. Since the conjecture covers arbitrary graphs, this suffices. No minimality is claimed. A [ten-vertex cubic example](followup.md) additionally shows that failure does not depend on ties or unequal degrees. It strengthens the same result.

We do not assert $m(t)>p$, so there is no contradiction with a bound $m(t)\leq p$. The failure is monotonicity in time. The separate convexity and convergence questions are outside this result.

## 6. Reproduction

From the repository root:

~~~sh
python problems/median-dynamics/verify.py
python problems/median-dynamics/closed_form.py
python problems/median-dynamics/verify_regular.py
~~~

The first and third commands use only Python's standard library; the second needs SymPy. The files certificate.json, closed_form.txt and regular_certificate.json are regenerated. All three checks passed.

These are exact computational checks, not Lean formalizations or a certification of novelty. The finite algebra is transparent and reproducible, but has not been replaced by a short computation-free derivation.
