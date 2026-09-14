# No uniform reverse Wasserstein bound for the spherical Radon transform

**Status:** complete negative answer to the stated inequality, with a stronger
negative answer on smooth even densities on the two-dimensional sphere.
Novelty is **not established**; this is a short deduction from classical facts,
not a claim of a new inversion theorem. Independent review remains pending.

**Source:** Benjamin K. Stephens, *Measuring the Geodesic Radon Transform with
Mass Transport*, Oberwolfach Reports 5 (2008), 1762–1764, especially the final
question on p. 1763, [original report](https://ems.press/content/serial-article-files/46174#page=57),
DOI [10.4171/OWR/2008/31](https://doi.org/10.4171/OWR/2008/31).
Dataset: UnsolvedMath ID **30000999**, OWR-2042-008,
[catalog entry](https://www.unsolvedmath.com/problems/30000999).
The original report, not just the catalog paraphrase, was checked.

## Question and immediate answer

On the unit sphere with geodesic distance, let R send a point mass at u to
normalized uniform measure on its perpendicular equator. Extend R linearly to
probability measures. For fixed 1 <= p < infinity, can a finite constant C satisfy

    W_p(mu,nu) <= C W_p(R mu,R nu)

for every pair of probability measures?

No. For any unit vector u, take mu=delta_u and nu=delta_{-u}. Their Wasserstein
distance is pi, but their equators are identical, so their transformed distance
is zero. This answers the unrestricted question on every S^(n-1), n>=2.

The antipodal obstruction is classical and should not be advertised as a new
discovery. The following argument also removes that obstruction entirely.

## Stronger theorem: smooth, positive, even densities still fail on S^2

For every finite p>=1 and every C, the inequality fails for some smooth
antipodally symmetric probability density on S^2 and the uniform probability
measure sigma. The density can be chosen arbitrarily close to 1 in uniform norm.

### 1. Explicit attenuated densities

Let P_l be the Legendre polynomial normalized by P_l(1)=1, and take l=2k>0.
Set h(x)=P_(2k)(x_3). Its mean is zero, it is even, and |h|<=1. Thus

    mu_t = (1+t h) sigma,       |t|<1/2,

has all the claimed regularity and positivity properties. Normalized equatorial
averaging satisfies the classical spherical-harmonic identity

    R h = lambda_k h,
    lambda_k = P_(2k)(0) = (-1)^k binomial(2k,k)/4^k.

Here the same identity applies to measure densities: uniform incidence measure
on perpendicular pairs is symmetric, so the averaging operator is self-adjoint
relative to sigma. Consequently R sigma=sigma and R mu_t=mu_(lambda_k t).

One way to see the eigenfunction identity is to average a zonal spherical
harmonic over the equator. Rotation invariance preserves its harmonic degree
and axial symmetry, hence gives a multiple of the same zonal harmonic.
Evaluating at the north pole gives the multiple P_(2k)(0).
The standard identity is also stated in the
[author-hosted Funk–Radon paper](https://www.csc.univie.ac.at/paper/ThoSch12.pdf).

Write b_k=|lambda_k|. Since

    b_k = product_(j=1)^k (1-1/(2j)),
    log b_k <= -(1/2) sum_(j=1)^k 1/j,

we have b_k -> 0. No asymptotic formula is needed.

### 2. Wasserstein distance reduces exactly to an interval

Use colatitude theta in [0,pi]. The colatitude law of sigma has density
a(theta)=sin(theta)/2, and that of mu_t has density
a(theta)(1+t P_(2k)(cos(theta))).

Projection to colatitude is 1-Lipschitz, so interval transport gives a lower
bound on spherical transport cost. Conversely, couple colatitudes optimally
and give both points the same independent uniform longitude. Their spherical
distance is exactly the difference of their colatitudes. This coupling attains
the interval cost. Thus the two Wasserstein distances are equal.

Put h(theta)=P_(2k)(cos(theta)),

    F_t(theta) = integral_0^theta a(s)(1+t h(s)) ds,
    H(theta) = integral_0^theta a(s)h(s) ds.

The increasing optimal interval transport from the uniform spherical law is
T_t(theta)=F_t^(-1)(F_0(theta)). Hence

    W_p(mu_t,sigma)^p
      = integral_0^pi |T_t(theta)-theta|^p a(theta) dtheta.

This uses the usual monotone optimal coupling on the real line for cost |x-y|^p.

### 3. The infinitesimal transport cost scales linearly

For interior theta, differentiate F_t(T_t(theta))=F_0(theta):

    partial_t T_t(theta)
      = -H(T_t(theta)) / [a(T_t(theta))(1+t h(T_t(theta)))].

The function H/a extends continuously to both endpoints with value zero.
Indeed H(theta)=O(theta^2) near zero, and H(pi)=0 makes
H(theta)=O((pi-theta)^2) near pi, whereas a vanishes linearly.
It is not identically zero because h is not zero. For |t|<1/2 the derivative
above is bounded in absolute value by 2 max|H/a|, uniformly in theta and t.
Dominated convergence therefore gives

    lim_(t->0) W_p(mu_t,sigma)/|t| = B_(p,k),
    B_(p,k)^p = integral_0^pi |H(theta)/a(theta)|^p a(theta) dtheta,
    0 < B_(p,k) < infinity.

Since R mu_t=mu_(lambda_k t), it follows that

    lim_(t->0) W_p(R mu_t,R sigma)/W_p(mu_t,sigma) = b_k.

Given C>0, first choose k with C b_k<1, then choose sufficiently small nonzero
t. The proposed reverse bound fails. This proves the stronger theorem for
every finite p. No assertion about other inverse moduli of continuity is made.

### Particularly simple exact version for p=1

On an interval W_1 is the integral of the absolute difference of cumulative
distribution functions. Thus, without taking any limit,

    W_1(mu_t,sigma) = |t| integral_0^pi |H(theta)| dtheta,
    W_1(R mu_t,sigma) = b_k W_1(mu_t,sigma).

For example k=100 makes the ratio binomial(200,100)/4^100 < 1/17.

## Verification and limits

Run `sage -python problems/spherical-radon-reverse-wasserstein/verify_sage.py`. The script checks the equator-average
polynomial identity exactly over QQ for degrees 2 through 24, mean zero,
parity, and the exact multiplier formula. It also checks the displayed k=100
bound. These checks support the formulas; the proof for all k and all finite p
is the argument above, not a finite experiment or a formalized proof.

The immediate obstruction and harmonic attenuation are classical. Targeted
searches for the talk title and reverse Wasserstein estimates did not establish
priority for this particular formulation. Do not label this a verified new
research discovery or add it to a novelty-confirmed list without further review.
