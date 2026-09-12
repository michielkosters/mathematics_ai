# Three generators, class three: self-similarity

**Answer: no. Every three-generated torsion-free nilpotent group of class three is self-similar.**

This answers the whole question in Kourovka Notebook 21.42 (A. Dantas and S. Sidki), also Problem 1 of Berlatto–Gentil, *On self-similarity of finitely generated torsion-free nilpotent groups*.

The answer follows by combining established theorems. **We do not claim a new theorem or priority for this implication.** The catalogue still labels the question open; that label is not evidence of novelty.

## Short complete proof

Let $G$ be such a group and let $L$ be its rational Malcev Lie algebra. The logarithms of a generating triple of $G$ generate $L$ as a Lie algebra: the Baker–Campbell–Hausdorff formula puts the logarithm of every group word in the Lie algebra they generate, and these logarithms span $L$. Malcev correspondence preserves nilpotency class.

The positive-grading theorem of **Dekimpe–Igodt–Pouseele (2003)** applies to three-generated, three-step nilpotent Lie algebras. It gives a decomposition

$$
L=\bigoplus_{j>0}L_j,\qquad [L_i,L_j]\subseteq L_{i+j}.
$$

Its applicability is explicitly recorded in **Dekimpe–Deré (2016), p. 365**, in the discussion following Theorem 6.1. If fewer generators suffice, the two-generator case is covered by the same cited result; class at most two also has its usual positive grading.

After extending scalars to $\mathbb C$, the grading still has zero degree-zero part. This is precisely a *very special grading* in **Mathieu (2021), Theorem 3**. That theorem says $G$ admits a free self-similar action with dense orbits on the boundary of a regular rooted tree. In particular the action is faithful and self-similar, as required. Thus no group asked for in Problem 21.42 exists. $\square$

Verification: see [the short source check](verification.md).

## What makes the proof work?

A positive grading assigns positive integer weights to coordinates, with weights adding under brackets. Scaling a coordinate of weight $j$ by $m^j$ preserves brackets. This supplies expanding copies of the group; their inverse maps supply the recursive tree action. Mathieu's theorem handles this passage for the original group, so the conclusion is not restricted to a finite-index subgroup or to a particular lattice.

This is a proof for every group in the question, not a finite computation. No search bounds, probabilistic tests, or computer certification are used.

## Sources and attribution

- [Original Kourovka question, 21.42](https://alglog.org/21tkt.pdf).
- [Berlatto–Gentil, arXiv:2509.16947v1, Problem 1](https://arxiv.org/html/2509.16947v1). This 2025 paper poses the same question.
- Karel Dekimpe, Paul Igodt, Hannes Pouseele, [*Expanding Automorphisms and Affine Structures on Nilpotent Lie Algebras with Few Generators*](https://doi.org/10.1081/AGB-120024857), Communications in Algebra **31** (2003), 5847–5874.
- Karel Dekimpe, Jonas Deré, [*Expanding Maps and Non-Trivial Self-Covers on Infra-Nilmanifolds*](https://www.tmna.ncu.pl/static/published/2016/v47n1-18.pdf), Topological Methods in Nonlinear Analysis **47** (2016), 347–368. See p. 365 for the precise grading result above; Theorem 4.1 explains its relation to expanding maps.
- Olivier Mathieu, [*Which Nilpotent Groups are Self-Similar?*, arXiv:2101.11291v1, Theorem 3](https://arxiv.org/html/2101.11291v1). See the introduction and §3.1 for the definition of a very special grading.
- [UnsolvedMath record 2551](https://www.unsolvedmath.com/problems/2551). This integer is an internal catalogue key; **Kourovka 21.42** is the original problem identifier.

Checked 2026-09-12. The 2003 publisher abstract and the explicit 2016 statement were checked; the complete 2003 article was not obtained. No claim is made that we are first to notice the implication. The underlying grading theorem and the self-similarity criterion belong to the authors above.
