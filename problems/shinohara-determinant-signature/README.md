# Knots of determinant 4k+1 and signature four

**Result:** a complete affirmative deduction for Shinohara's question from classical quadratic Gauss sums, Nikulin's existence theorem for even lattices, and Seifert-matrix realization. The argument even gives genus-two knots. Novelty is unconfirmed; this proof has not been independently reviewed or formally verified.

**Problem source:** Y. Shinohara's question, [Ohtsuki, Problems on invariants of knots and 3-manifolds, Problem 12.21](https://msp.org/gtm/2002/04/gtm-2002-04-024s.pdf#page=168). It asks whether every integer n=4k+1, k>0, occurs as the determinant of a knot of signature 4. Also [Stoimenow, A dozen of knot theoretical problems, Problem 9](https://stoimenov.net/stoimeno/homepage/papers/12pb.pdf). UnsolvedMath identifiers: `10400226`, `AMR-103-0226`, from [the upstream dataset](https://huggingface.co/datasets/ulamai/UnsolvedMath).

## Theorem

For every integer n>1 with n congruent to 1 modulo 4, there is a classical knot K in S^3 with

$$\det K=n,\qquad \sigma(K)=4,\qquad g(K)=2.$$

We use the convention sigma(K)=signature(V+V^T). Mirroring handles the opposite sign convention.

The idea is to construct a positive definite, even, integral four-by-four matrix of determinant n, and then turn it into a Seifert matrix.

## 1. A finite quadratic form of order n and Brown invariant four

For odd m and gcd(a,m)=1, put

$$q_{m,a}(x)=\frac{2ax^2}{m}\pmod{2\mathbb Z},\qquad x\in\mathbb Z/m\mathbb Z.$$

This is well-defined and nondegenerate: its associated bilinear pairing is 2axy/m modulo Z, and 2a is a unit modulo m. Its normalized Gauss sum is

$$G(m,a)=\frac1{\sqrt m}\sum_{x=0}^{m-1}\exp(2\pi i ax^2/m).$$

The classical quadratic Gauss-sum formula gives

$$G(m,a)=\varepsilon_m\left(\frac a m\right),\qquad
\varepsilon_m=\begin{cases}1&m\equiv1\pmod4,\\i&m\equiv3\pmod4,\end{cases}$$

where the parentheses denote the Jacobi symbol. Gauss sums multiply under orthogonal direct sums. The Brown invariant is the residue beta modulo 8 whose phase is exp(2 pi i beta/8). Thus a normalized sum of -1 means beta=4.

**If n is not a square:** the Jacobi character modulo n is nontrivial. Indeed, choose a prime appearing to an odd exponent in n, choose a to be a quadratic nonresidue there and a residue at the other primes, and apply the Chinese remainder theorem. Then gcd(a,n)=1 and (a/n)=-1. Since n is 1 modulo 4, q_{n,a} has Gauss sum -1. Its group is cyclic.

**If n is a square:** write n=p^e m with p prime, e positive and even, gcd(p,m)=1, and m a square. On

$$A=(\mathbb Z/p^{e-1}\mathbb Z)\oplus(\mathbb Z/p\mathbb Z)\oplus(\mathbb Z/m\mathbb Z)$$

take the form q_{p^{e-1},1} orthogonally summed with q_{p,a} and q_{m,1}; omit the last factor if m=1. Choose a with

$$\left(\frac a p\right)=-\left(\frac{-1}p\right).$$

Both Legendre signs are available. The first two factors have Gauss-sum product

$$\varepsilon_p^2\left(\frac a p\right)=-1,$$

and the last factor has sum 1 because m is an odd square. Again the total sum is -1. The group has order n and needs at most two generators: combine the coprime-order factors of orders p^(e-1) and m.

We have therefore constructed, for every required n, a nondegenerate finite quadratic form (A,q) with |A|=n, length at most two, and Brown invariant four.

## 2. Realize it by a positive definite even lattice

We use this sufficient case of Nikulin's even-lattice existence theorem: a finite nondegenerate quadratic form of length l and Brown invariant beta is the discriminant form of an even lattice of signature (r_+,r_-) if

$$r_++r_-\ge l+2,\qquad r_+-r_-\equiv\beta\pmod8.$$

The remaining local conditions in the full theorem occur only when a local discriminant group has length equal to the lattice rank, which is excluded here. Positive definiteness is allowed in the existence theorem; it is not a uniqueness assertion about indefinite lattices.

For a readable statement with all local conditions, see [Theorem 12.4.4 and Corollary 12.4.6 in this author-hosted quadratic-forms text](https://www-fourier.univ-grenoble-alpes.fr/~peters/Books/QuadraticForms/QuadForms.pdf#page=236), citing Nikulin, Theorem 1.10.1.

Apply it with (r_+,r_-)=(4,0), l<=2 and beta=4. Let S be a Gram matrix of the resulting lattice. Then S is integral, symmetric, positive definite, has even diagonal, and det S=|A|=n.

## 3. Turn the lattice into a knot

Because det S is odd, reduction modulo 2 gives a nondegenerate alternating bilinear form. Hence it has a symplectic basis. Lift the corresponding basis change to a unimodular integer matrix U: elementary swaps and column additions generating GL_4(F_2) lift to such integer operations. Set B=U^T S U. Then

$$B\equiv J\pmod2,\qquad
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\oplus
\begin{pmatrix}0&1\\-1&0\end{pmatrix}.$$

Define the integral matrix V=(B+J)/2. Direct calculation gives

$$V-V^T=J,\qquad V+V^T=B.$$

The classical Seifert realization theorem says that an integral matrix whose skew part is unimodular is a Seifert matrix of a classical knot. In this standard symplectic basis the realization uses a disk with four bands, hence a genus-two surface. See [J. Levine, The role of the Seifert matrix in knot theory, ICM 1970, vol. 2, pp. 95–98](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1970.2/ICM1970.2.ocr.pdf): the dimension-three exception mentioned there concerns three-dimensional knots, not classical one-dimensional knots in S^3.

For the resulting knot,

$$\det K=|\det(V+V^T)|=n,\qquad
\sigma(K)=\operatorname{signature}(V+V^T)=4.$$

The surface has genus two, and the signature bound |sigma(K)|<=2g(K) forces the knot genus to be exactly two. This proves the theorem for every n in the question.

## A small exact certificate

For n=2857, Sage produces the Seifert matrix

$$V=\begin{pmatrix}
2&0&0&-1\\
-1&33&0&1\\
0&0&2&0\\
-1&1&-1&2
\end{pmatrix}.$$

Its skew part is J, and its symmetric part is positive definite with determinant 2857. Thus the knot realization follows without computing a knot diagram. This example alone is not the general proof.

Run `sage -python problems/shinohara-determinant-signature/verify_sage.py`. The script checks 29 finite quadratic forms with exact cyclotomic/algebraic arithmetic, and exact lattice-to-Seifert conversions for determinants 17 and 2857. `verification.json` records the matrices. It uses no floating-point approximation. These are supporting checks; the all-n conclusion depends on the theorem applications above.

## Priority and scope

The original problem statement was checked, as was its later appearance as Question 5.1 in Stoimenow, *Determinants of knots and Diophantine equations*, Acta Arithmetica 129 (2007), 363–387, [DOI 10.4064/aa129-4-6](https://doi.org/10.4064/aa129-4-6). Targeted searches on 2026-09-13 did not settle whether this lattice deduction is already known. No novelty is claimed. This is an existence proof from established theorems, not a claim to have found a new lattice-existence theorem, and not a claim that all these knots are alternating, prime, or fibered.
