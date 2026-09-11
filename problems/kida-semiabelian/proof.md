# A semiabelian group of order 2592 that is not monomial

We construct a counterexample to Masanari Kida's Conjecture 1.3 in
[On semiabelian groups](https://doi.org/10.1515/jgth-2024-0010),
Journal of Group Theory 28 (2025), 697–712, also catalogued as
Kourovka Notebook problem 21.68 and UnsolvedMath record 2577.
This is a complete counterexample. No prior resolution was found in our
literature check on 10 September 2026; priority remains unconfirmed.

A finite group is monomial if every irreducible complex character is induced
from a linear character of a subgroup. Here semiabelian means obtainable
from the trivial group by successively taking quotients of semidirect
products with abelian normal factors. Our example needs no quotients.

## Construction

Let $D\cong C_2^3$ be the diagonal sign changes on four coordinates with
an even number of minus signs. Let $T=A_4$ permute the coordinates, and put
$$
G=D\rtimes T,\qquad |G|=96.
$$
Label the coordinate basis $1,i,j,k$. The following signed permutations
belong to $G$:
$$
u:(1,i,j,k)\mapsto(i,-1,k,-j),\qquad
v:(1,i,j,k)\mapsto(j,-k,-1,i),
$$
and $c$ fixes $1$ and cycles $i,j,k$.
The first two are left multiplication by quaternion units.
Thus $Q=\langle u,v\rangle\cong Q_8$, while $c$ has order three and
cyclically permutes the three quaternion generators by conjugation.
Consequently
$$
H=\langle u,v,c\rangle=Q_8\rtimes C_3,\qquad |H|=24,\qquad [G:H]=4.
$$

We need two facts about $H$. First, $H'=Q_8$: the quotient by $Q_8$
is abelian, and commutators with $c$ generate $Q_8$. More explicitly,
their images span $Q_8/\{\pm1\}$, and two independent quaternion units
generate $Q_8$. Hence $H/H'\cong C_3$, so **$H$ has no subgroup of
index two**.

Second, $H$ has an irreducible complex representation $\psi$ of degree
two. To see this without a character table, take the unique degree-two
irreducible representation of $Q_8$. Its equivalence class is invariant
under the automorphism induced by $c$. An intertwining matrix implementing
this automorphism has scalar cube, by Schur's lemma. Rescale it to have cube
the identity. This extends the representation to $Q_8\rtimes C_3$, and
the extension remains irreducible on restriction to $Q_8$.

Let $\Omega$ be the four cosets of $H$ in $G$, with their natural
transitive permutation action. Put
$$
A=\{a\in(\mathbb F_3)^\Omega:\sum_{\xi\in\Omega}a_\xi=0\},\qquad L=A\rtimes G.
$$
This is a $G$-invariant abelian group of order $3^3$, so $|L|=3^3\cdot96=2592$.
The verifier uses right cosets and the corresponding right-action convention;
the resulting group is the same construction.

## Semiabelianity

There is an explicit chain of embedded groups
$$
1<C_3<A_4<G<L.
$$
The successive constructions are
$$
C_3,\quad V_4\rtimes C_3=A_4,\quad D\rtimes A_4=G,\quad A\rtimes G=L.
$$
Each added normal factor is abelian. This proves semiabelianity directly
from the definition; no closure under arbitrary extensions is assumed.

## An irreducible character of degree eight

Write $\omega=e^{2\pi i/3}$ and let
$\lambda(a)=\omega^{a_H}$, where $a_H$ is the coordinate at the coset $H$.
The four coordinate characters are distinct on $A$: its annihilator in
the dual of $(\mathbb F_3)^\Omega$ consists of constant coefficient
vectors, whereas the difference of two coordinate vectors is not constant.
Its stabilizer in $G$ is exactly $H$, so its inertia subgroup in $L$
is $I=A\rtimes H$.

Since $H$ fixes that coordinate, $\lambda$ extends to $I$ by
$\widetilde\lambda(a,h)=\lambda(a)$. Inflate $\psi$ from $H$ to $I$
and define
$$
\chi=\operatorname{Ind}_I^L(\widetilde\lambda\otimes\psi).
$$
This has degree $4\cdot2=8$ and is irreducible. Indeed, its restriction
to $A$ has four distinct character spaces, one for each conjugate of
$\lambda$, each of dimension two. An invariant subspace decomposes into
these character spaces. Its intersection with the $\lambda$-space is
either zero or the whole space, since $I$ acts there irreducibly through
the degree-two representation above. Transitivity on the four spaces
then forces the invariant subspace to be zero or the whole representation.
In particular,
$$
\chi|_A=2\sum_{\mu\in\lambda^G}\mu.
$$

## Why this character is not monomial

Suppose $\chi=\operatorname{Ind}_K^L\theta$ for a linear character
$\theta$ of a subgroup $K$. Degrees give $[L:K]=8$.
Since $A$ is a normal 3-subgroup and this index is prime to 3, $A\le K$.
For clarity: a Sylow 3-subgroup of $K$ is also Sylow in $L$, and every
Sylow 3-subgroup of $L$ contains its normal 3-subgroup $A$.

The restriction $\theta|_A$ must be one of the four constituents of
$\chi|_A$. Conjugating $K$ and $\theta$, we may assume
$\theta|_A=\lambda$. A linear character is invariant under conjugation
by elements of its own group, so every element of $K$ stabilizes
$\lambda$. Hence $K\le I$.

But now
$$
[H:K/A]=[I:K]=[L:K]/[L:I]=8/4=2,
$$
contrary to the absence of an index-two subgroup of $H$.
Therefore $\chi$ is not monomial, and $L$ is a semiabelian,
nonmonomial finite group. This refutes the full stated conjecture.

## Verification and attribution

[verify.py](verify.py) reconstructs the group from scratch with Sage/GAP.
It checks the abelian factors, the subgroup H, its character degrees,
and the independent exact test IsMonomial(L) = false.
[certificate.json](certificate.json) records the outputs and explicit generators.
The written proof above does not depend on GAP's monomiality algorithm.

Kida's Example 5.5 already identifies a semiabelian group of order 96
containing SL(2,3). We credit that ingredient to the source paper.
Our construction adds the three-dimensional abelian module and uses its
coordinate characters to obstruct monomiality. See
[prior-art.md](prior-art.md) for the dated literature check and its limits.

We do not claim that 2592 is the smallest possible counterexample.
