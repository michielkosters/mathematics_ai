# A non-concise first-order formula in the integer Heisenberg group

**Result.** Not every parameter-free first-order group formula is concise in residually finite groups. The formula below has exactly two values in \(H=\mathrm{UT}_3(\mathbb Z)\), and those values generate its infinite cyclic centre.

This answers the entire question in **Kourovka Notebook 21.106** (local catalog ID 2615), also Question 1 of Martina Conte and Jan Moritz Petschick, *Conciseness of first-order formulae*, DOI [10.1007/s00605-025-02127-5](https://doi.org/10.1007/s00605-025-02127-5).

Sources: [original paper, Question 1](https://d-nb.info/1387927140/34), [Kourovka Notebook](https://alglog.org/21tkt.pdf), [problem dataset](https://huggingface.co/datasets/ulamai/UnsolvedMath).

## The formula

Use the convention \([a,b]=a^{-1}b^{-1}ab\). The following are merely abbreviations for first-order formulas:
\[
\begin{aligned}
Z(t)&:\quad \forall h\;[t,h]=1,\\
P(a)&:\quad \forall t\;\bigl(Z(t)\Rightarrow\exists u\;[a,u]=t\bigr),\\
B(a,b)&:\quad \forall g\;\exists c\,\exists d\;
 (g=cd\ \land\ [c,a]=1\ \land\ [d,b]=1).
\end{aligned}
\]
Define
\[
\boxed{\ \phi(x):\quad x\ne1\ \land\
\exists a\,\exists b\;
\bigl(x=[a,b]\land P(a)\land P(b)\land B(a,b)\bigr).\ }
\]
All symbols other than \(x\) are bound group variables. Expanding the abbreviations gives a finite, parameter-free formula with exactly one free variable. In particular, the central generator used in the proof is **not** a parameter of the formula.

Informally, \(P(a)\) says that commutation with \(a\) reaches every central element; \(B(a,b)\) says that the two centralizers multiply to the whole group.

## Coordinate proof

Write the elements of \(H\) as triples
\[
(r,s,t)=\begin{pmatrix}1&r&t\\0&1&s\\0&0&1\end{pmatrix},
\qquad
(r,s,t)(u,v,w)=(r+u,s+v,t+w+rv).
\]
Then
\[
[(r,s,t),(u,v,w)]=(0,0,rv-su).
\]
Consequently the centre is \(Z(H)=\{(0,0,t):t\in\mathbb Z\}\). Put \(z=(0,0,1)\).

Let \(\pi:H\to\mathbb Z^2\) send \((r,s,t)\) to \((r,s)\).

**1. The surjectivity condition means primitivity.**
For \(a=(r,s,t)\), the commutators \([a,u]\), as \(u\) varies, form exactly
\[
\{z^{rv-sw}:v,w\in\mathbb Z\}
=\{z^{k\gcd(r,s)}:k\in\mathbb Z\}.
\]
By Bézout's identity, \(P(a)\) therefore holds exactly when \(\gcd(r,s)=1\). In particular \(\pi(a)\ne0\).

**2. Centralizers recover the two lattice directions.**
If \(\pi(a)=(r,s)\) is primitive, the equation \(rv-su=0\) for \((u,v)\in\mathbb Z^2\) has precisely the solutions \((u,v)=k(r,s)\). Thus
\[
\pi(C_H(a))=\mathbb Z\pi(a).
\]

**3. Every value of the formula is \(z\) or \(z^{-1}\).**
Suppose \(\phi(x)\) holds with witnesses \(a,b\). By step 1 both projected vectors are primitive. Applying \(\pi\) to \(H=C_H(a)C_H(b)\) gives
\[
\mathbb Z^2=\mathbb Z\pi(a)+\mathbb Z\pi(b).
\]
The two vectors therefore form an integral basis, so their determinant is \(1\) or \(-1\). The commutator formula now gives \(x=[a,b]=z^{\pm1}\).

**4. Both values occur.**
Take \(a=(1,0,0)\), \(b=(0,1,0)\). Both satisfy \(P\), and every element factors as
\[
(r,s,t)=(r,0,t-rs)(0,s,0).
\]
The first factor centralizes \(a\), the second centralizes \(b\). The witnesses satisfy \([a,b]=z\).
For \(z^{-1}\), interchange \(a,b\) and use
\[
(r,s,t)=(0,s,t)(r,0,0).
\]
Thus \(H_\phi=\{z,z^{-1}\}\), and \(\langle H_\phi\rangle=\langle z\rangle\cong\mathbb Z\).

Finally, \(H\) is residually finite: reducing all three coordinates modulo any integer \(m\ge2\) is a homomorphism to the finite group \(\mathrm{UT}_3(\mathbb Z/m\mathbb Z)\). Given a nonidentity triple, choose \(m\) larger than the absolute value of a nonzero coordinate; that coordinate remains nonzero modulo \(m\).

This proves that \(\phi\) is not concise in the class of residually finite groups, already within finitely generated torsion-free nilpotent groups of class two.

## Verification, scope, and novelty

The proof above establishes the infinite statement; finite checks cannot replace it. The Sage script verifies the coordinate commutator and both witness factorizations symbolically, and checks the primitive-kernel lemma on a small integer sample.

The paper explicitly permits arbitrary parameter-free formulas and asks this question. Its positive result for **existential** formulas does not apply: our formula contains universal quantifiers.

Source and targeted literature searches on 2026-09-13 did not locate an earlier resolution. **Novelty is unconfirmed.** Definability of arithmetic in nilpotent groups is an older subject; no claim is made that this definability mechanism itself is new.

The proof has been checked during preparation, but has not received independent review or formal proof-assistant verification.

Run the supporting checks with:

```sh
sage -python problems/heisenberg-nonconcise-formula/verify_sage.py
```

This regenerates `verification.json` beside the proof.
