# Permanents with bounded Frobenius norm

**Result:** an affirmative answer to Problem 9 of the 2008 Oberwolfach Discrete Geometry report, posed by Alexander Barvinok and Alex Samorodnitsky. A complete argument is below. Novelty has not been established; this is not independently refereed or formally verified.

**Original source:** [OWR 44/2008, pp. 2549–2550, Problem 9](https://ems.press/content/serial-article-files/46191?nt=1#page=73), [DOI 10.4171/OWR/2008/44](https://doi.org/10.4171/OWR/2008/44). Catalog ID `30001073` is an internal identifier from [UnsolvedMath](https://huggingface.co/datasets/ulamai/UnsolvedMath), not the original problem number. That catalog entry also contains the unrelated spanning-tree question (Problem 10), which this note does not resolve.

## Theorem

Let A=(a_ij) be an n by n doubly stochastic matrix, and put s=sum_ij a_ij^2. Then

$$
 e^{-n}\le \frac{n!}{n^n}\le \operatorname{per}(A)
 \le e^{-n}(en)^{64s}.
$$

Consequently, for every fixed gamma >= 1, the condition s <= gamma implies per(A) = e^{-n} n^{O_gamma(1)} as n tends to infinity. The constant 64 is chosen for an easy proof, not sharpness.

All logarithms are natural. Terms of the form 0 log 0 are zero.

## 1. An entropy bound for random permutations

Let sigma be any random permutation, with marginal probabilities q_ij = P(sigma(i)=j). Define

$$
 g(q)=\frac{-q^2\log q}{1-q}\quad(0<q<1),\qquad g(0)=0,\quad g(1)=1.
$$

We claim

$$
 H(\sigma)\le -\sum_{ij}q_{ij}\log q_{ij}-n+\sum_{ij}g(q_{ij}). \tag{1}
$$

Here H is Shannon entropy with natural logarithms. To prove this, independently give every row a uniform random priority U_i in [0,1], and reveal sigma(i) in increasing priority order. For each fixed ordering, apply the entropy chain rule.

When row i is revealed, let C be the unused columns and S_i=sum_{j in C} q_ij. Its conditional distribution p is supported on C. Nonnegativity of relative entropy against the distribution q_ij/S_i on C gives

$$
 H(p)\le \mathbb E[-\log q_{i,\sigma(i)}\mid\text{history}]+\log S_i.
$$

Zero marginal entries cannot occur as realized assignments; also S_i>0 on every history of positive probability. Averaging this inequality over histories and orderings bounds H(sigma) by the sum of the corresponding expectations.

Conditional on the full permutation sigma and on U_i=t, its assigned column is certainly unused. Every other column is unused precisely when its assigned row has priority greater than t, an event of probability 1-t. Therefore, writing q=q_{i,sigma(i)},

$$
 \mathbb E[S_i\mid\sigma,U_i=t]=q+(1-t)(1-q).
$$

Jensen's inequality and integration over t yield

$$
 \mathbb E[\log S_i\mid\sigma]
 \le\int_0^1\log(q+(1-t)(1-q))\,dt
 =-1-\frac{q\log q}{1-q}.
$$

At q=1 the expression means its limit, zero. Averaging over sigma contributes -1+sum_j g(q_ij) for row i. Summing proves (1). Independence among the unused-column indicators is not needed.

## 2. Apply the bound to weighted permutations

The van der Waerden permanent theorem gives per(A)>=n!/n^n>0. Give each permutation probability

$$
 \mathbb P(\sigma)=\frac{\prod_i a_{i,\sigma(i)}}{\operatorname{per}(A)}.
$$

Its marginal matrix Q=(q_ij) is doubly stochastic, and q_ij=0 whenever a_ij=0. Directly from this probability formula,

$$
 \log\operatorname{per}(A)=H(\sigma)+\sum_{ij}q_{ij}\log a_{ij}.
$$

Using (1), we obtain

$$
 \log\operatorname{per}(A)\le -n+\sum_{ij}\bigl(g(q_{ij})-d(q_{ij},a_{ij})\bigr), \tag{2}
$$

where d(q,a)=q log(q/a)-q+a. Indeed sum q_ij=sum a_ij=n, so the linear terms cancel. We set d(0,a)=a and d(0,0)=0; no term with q>0,a=0 occurs. The elementary inequality x log x-x+1>=0 shows d>=0.

## 3. The elementary scalar estimate

For 0<a<=1 and 0<=q<=1,

$$
 g(q)\le d(q,a)+64a^2\log(e/a). \tag{3}
$$

First, -q log q<=1-q implies both g(q)<=q and
g(q)<=q^2 log(e/q), with endpoints interpreted continuously. For the second inequality, writing L=-log q, the required inequality L/(1-q)<=1+L is exactly qL<=1-q.

If q>=8a, then
d(q,a)>=q(log 8-1)+a>=q>=g(q), since log 8>2.

Suppose q<8a. The function f(x)=x^2 log(e/x) is increasing on [0,1], since f'(x)=x(1-2 log x)>0 on (0,1]. If 8a<=1, then

$$
 g(q)\le f(q)\le f(8a)\le64a^2\log(e/a).
$$

If 8a>1, use instead g(q)<=1<=64a^2 log(e/a). Since d>=0, this proves (3) in all cases. Entries with a=q=0 contribute zero.

Combining (2) and (3) proves the stronger intermediate estimate

$$
 \log\operatorname{per}(A)\le -n+64\sum_{ij}a_{ij}^2\log(e/a_{ij}). \tag{4}
$$

## 4. Finish with the Frobenius hypothesis

Cauchy–Schwarz in each row gives s>=1. The n^2 numbers b_ij=a_ij^2/s form a probability distribution, whose entropy is at most log(n^2). Hence

$$
 \sum_{ij}a_{ij}^2\log(1/a_{ij})
 =\frac{s}{2}\bigl(H(b)-\log s\bigr)\le s\log n.
$$

Thus (4) gives log per(A)<=-n+64s(1+log n), the desired upper bound. For the lower bound, use van der Waerden and
log(n!)>=integral_1^n log x dx>=n log n-n. This completes the proof.

## Verification and priority

`verify.py` enumerates permutations of small rational doubly stochastic matrices. Permanents and marginals are exact rational numbers; logarithmic inequalities are checked numerically with 60 decimal digits. It checks the entropy bound, the Gibbs identity, the scalar bound, and the final bound, including zero entries and deterministic permutations. These are regression checks, not a proof for all matrices; the argument above supplies that proof. Run `python problems/permanent-bounded-frobenius/verify.py` (requires mpmath).

The proof uses the classical random-exposure entropy method for permanent bounds, rather than a claim of a new entropy technique. Related literature includes [Entropy inequalities for random walks and permutations](https://arxiv.org/abs/2109.06009). Targeted searches on 2026-09-13 found the original question but did not establish whether its exact conclusion has already been published. No priority claim is made. Independent mathematical review remains desirable.
