# Compressed dyadic center

## 1. Eliminate one point register, preserving dyadic arithmetic

The original complex invocation gathers h point sums and a total sum:

```
g_j = sum_(T contains j) x_T
g_* = sum_T x_T.
```

Every T has size three, hence `sum_j g_j = 3g_*`.

Retain the total register and only point registers 1,...,h−1. Define G'
using those h gather outputs. For arbitrary scratch c, define the scatter
R' on a target triple S by

```
if h not in S:
    (R'c)_S = (sum_(j in S) c_j − c_*)/2
if h in S:
    (R'c)_S = c_* − (sum_(j<h, j not in S) c_j)/2.
```

These coefficients lie in `{0, ±1, ±1/2}`. In particular this construction
does **not** divide a coefficient by three or change the dyadic encoding.
The earlier idea of dropping the total register and dividing the sum of
point registers by three is unnecessary.

For an input basis vector x_T, if h is absent from S then twice its R'G'
coefficient is `|S∩T|−1`. If h is present, the coefficient is

`2 − |T∩({1,...,h−1}\S)| = 2 − (3−|S∩T|) = |S∩T|−1`.

Thus `R'G' = RG` exactly. Retain the original ordered side-wire correction
J,V; then `R'G'+JV=I`. The same eight scalar rows, with G,R replaced by
G',R', add x to y and restore every auxiliary value for arbitrary initial
scratch. Inverse rows give the inverse shear. The three stages still give
the signed exchange `(-Y,X)`.

Do not enforce `sum_j c_j=3c_*` on arbitrary scratch: that identity is used
only on the gathered increment G'x. Restoration follows algebraically
because the invocation subtracts and readds the identical R'c terms.


Keep the common frames on all surviving center wires and remove only the
omitted center wire. This changes the center-loss count to L=3v^2 h^2 and
Delta=2v^3-2L=2v^2(v-3h^2). The side DAG proof and bank sharing are in the
separate proof.md and stage-joins.md. No twelve-touch precision hypothesis
is asserted for the new DAG here; its complete guard integration remains open.
