# Weighted hypergraphs and aligned bit circuits

Current conditional multiplication candidate: `κ=6.09×10^-10`, about
`609/83 = 7.3373` times the supplied community witness. The complex exponent
saving improves by about 69 times over the community complex motif, but that
factor does **not** carry through to multiplication: the bit circuit limits
the assembly. Complete upstream integration and independent review remain open.

## What changed

The complex side correction separates disjoint triples (+1/2) from triples
intersecting in exactly two points (-1/2). The latter use a fixed-pair
leave-one-out circuit. The former use a recursively weighted hypergraph
exclusion circuit instead of one auxiliary per ordered pair of triples.

The source code is [hypergraph_complex.py](hypergraph_complex.py). A bounded
screen tested 16 combinations of h=24,26,28,30 and 1,2,3,4 fixed anchors.
The best screened instance is h=26 with two anchors, not a globally optimal
network. It has 71,530 retained disjoint-sum addition nodes, 12,424 designated
disjoint outputs, and 29,250 intersection-two roles: **113,204 side roles**.
The old individual-edge count at the same h is 4,784,000.

The complex network has W=1,566,021,600,000, m=17,576 and
Delta=7,733,440,000. Exact rational logarithm enclosures give saving
`2.8745494655860578×10^-8`, compared with approximately
`4.1847990372×10^-10` for the community h=25 complex motif.

## The weighted recurrence

Input weights belong to hyperedges of size at most p. Request every sum
remaining after deleting at most q points. Pair the points into blocks.
Aggregate each hyperedge by its set of touched blocks, retaining lower-rank
weights when several vertices collapse into one block.

For a deletion set E, first take the coarse sum excluding every block that
E touches. For each nonempty collection of partially deleted blocks, take
their surviving vertices as fixed points V. Add the boundary sum consisting
of hyperedges containing V, with all other vertices outside those blocks
and all other deleted blocks. The remaining weighted problem has degree
at most p-|V| and deletion count at most q-|V|. Every surviving hyperedge
belongs to exactly one part, according to the deleted blocks it touches.
Thus all additions have disjoint formal supports; no cancellation is used.

For fixed p=q=1, this gives a linear-size circuit. For p=q=2 it gives
`T22(n) <= T22(ceil(n/2)) + O(n*T11(n/2)+n^2) = O(n^2)`.
For p=q=3:

`T33(n) <= T33(ceil(n/2)) + O(n*T22(n/2)+n^2*T11(n/2)+n^3) = O(n^3)`.

Input aggregation costs O(n^3) in total: an input hyperedge can occur in
only a bounded number of fixed-vertex boundary groups. These are circuit
size bounds for fixed degrees; the Python builder scans dictionaries and
does not claim matching construction time or uniform constants for all p,q.

The coordinate-frame-compatible family with **three** fixed anchors retains
O(h^3) side roles, versus O(h^6) individual-edge roles. Its bad-output repair
also costs O(h^3): there is one degree-three bad query, O(h) degree-two bad
queries, and O(h^2) degree-one bad queries. The two-anchor direct-split script
has better measured finite counts; that observation alone does not prove
an O(h^3) bound for its splitting routine. The separately implemented lazy
variant pre-excludes a missing anchor in a bounded number of helper families
and supports an O(h^3) argument, but has worse finite counts at h=26.

## Why the binary frames can work

A leaf has the norm-one line of its weight-three source indicator. Every
nonleaf has the coordinate span of the union of its source supports. A
nonleaf contains at least four coordinates. Along an edge, coordinate
spans grow. A leaf-to-nonleaf residual is nonalternating because a coordinate
outside the leaf's triple supplies a norm-one vector. Differences between
coordinate spans have their ordinary orthonormal coordinate bases.

Every designated disjoint sum contains sources disjoint from its target T.
If its coordinate union covers all points outside T, the remaining two
dimensions inside the target's three coordinates form an alternating plane.
That transition cannot be counted as two ordinary C factors. Partition the
sum by the first missing point among four selected points outside T. Each
triple misses at least one; each resulting part omits a non-target coordinate.
That omitted unit vector certifies a nonalternating output residual. Singleton
parts use the original triple line, with a unit coordinate outside both
disjoint triples certifying the residual for h>=8. Reverse transitions use
orthogonal complements and the same residual witnesses.

Early and late dirty-scratch mixers use the old D0 and D1 frames. The middle
mixers use these nested node frames. Hence this local argument preserves
the central-loss budget and the stage-sharing endpoints. It still requires
a full audit in the tensor/tape transfer and precision induction.

## Bit pairing alignment

The community bit construction removes a common point and pairs the
remaining ordered points. This shifts many pairs. Instead, keep every pair
of a global matching that does not contain the removed point, and place its
unpaired mate last. Source-order changes preserve every output definition.

At h=50 this shares 55,200 additions, versus 40,256 previously. Side roles
fall from 509,194 to **494,250**, and the bit saving rises from
`2.964610171565×10^-9` to `3.050819813902×10^-9`. The full merged coefficient
and forward/reverse frame checks pass at h=50.

Blocks of sizes 3,4,5,6 were also implemented and verified, including the
extra contributions inside partially deleted blocks. Every tested larger
block worsened the bit role count. Cutoffs 2 through 8 gave no improvement
over the aligned paired construction. These screens establish no general
lower bound.

An XOR-ordered global dyadic tree was screened at h=48,50,52,56,64. It did
not improve on the aligned h=50 circuit in the completed screen.

## Assembly and verification

[certificate.json](certificate.json)
records exact positive margins using bit saving 3050/10^12, complex saving
2874/10^11, epsilon=1999/10000 and c=1. It supports the arithmetic candidate
`κ=609/10^12`. The scoped bit ceiling is approximately `6.1016396278×10^-10`.
The size hypothesis s<m^5 for the stopped-depth guard is also checked.

The disjointness matrix and coordinate-frame residual conditions were
checked completely at h=26. Tests also cover weighted lower-rank hyperedges,
both full and lazy constructions, and a compiled mixer restoring arbitrary
nonzero dyadic scratch. Passing these checks does not establish the complete
multiplication theorem or its precision guard.

## Attribution and novelty

The reversible DAG compiler, common-point sharing, scalar paired recursion,
and first/third-stage sharing come from
[CrocSwap's pinned paired construction](https://github.com/CrocSwap/integer-mult-bounds/blob/6e564879f51ae16f23d392e9e196c605f36d90df/notes/paired-construction.tex).
Monotone disjoint summation is an established problem:
[Kaski, Koivisto and Korhonen (2012)](https://arxiv.org/abs/1208.0554) give
an O((n^p+n^q)log n) bound with uniform constants. Their appendix discusses
a stronger general target. Our fixed-degree recurrence has degree-dependent
constants; it is not a solution of that uniform target. Further literature
review is needed before asserting that the scalar recurrence is new.

The proposed contribution is its explicit complex-motif implementation,
coordinate frame assignment, alternating-residual repair, and exact finite
counts, together with globally aligned bit pairing. None has worldwide
novelty clearance. A finite-field Walsh shortcut was also considered but
not credited: reducing arithmetic modulo three does not supply the missing
tape reordering bound and would risk a circular use of the bit primitive.

Run `python verify.py` from this directory to reproduce the certificate and local tests.
