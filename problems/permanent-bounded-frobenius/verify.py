"""Exact rational enumeration; high-precision numerical sanity checks, not formal proof."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json
import random
import mpmath as mp

mp.mp.dps = 60
rng = random.Random(30001073)
tol = mp.mpf('1e-50')

def real(x):
    return mp.mpf(x.numerator) / x.denominator

def g(x):
    if x == 0: return mp.mpf(0)
    if x == 1: return mp.mpf(1)
    return -x*x*mp.log(x)/(1-x)

def d(q, a):
    return q*mp.log(q/a)-q+a if q else a

count = 0
for n in range(1, 8):
    perms = list(permutations(range(n)))
    matrices = [
        [[F(i == j) for j in range(n)] for i in range(n)],
        [[F(1, n) for j in range(n)] for i in range(n)],
    ]
    for _ in range(6):
        a = [[F(0) for j in range(n)] for i in range(n)]
        weights = [rng.randint(1, 50) for _ in range(2*n)]
        for weight in weights:
            p = rng.choice(perms)
            for i, j in enumerate(p): a[i][j] += F(weight, sum(weights))
        matrices.append(a)
    for a in matrices:
        assert all(sum(row) == 1 for row in a)
        assert all(sum(a[i][j] for i in range(n)) == 1 for j in range(n))
        weighted = []
        for p in perms:
            w = F(1)
            for i, j in enumerate(p): w *= a[i][j]
            if w: weighted.append((p, w))
        permanent = sum(w for p, w in weighted)
        q = [[F(0) for j in range(n)] for i in range(n)]
        entropy = mp.mpf(0)
        for p, w in weighted:
            prob = w/permanent
            entropy -= real(prob)*mp.log(real(prob))
            for i, j in enumerate(p): q[i][j] += prob
        marginal_entropy = mp.mpf(0)
        correction = mp.mpf(0)
        energy = mp.mpf(0)
        divergence = mp.mpf(0)
        smooth = mp.mpf(0)
        for i in range(n):
            for j in range(n):
                x, y = real(q[i][j]), real(a[i][j])
                correction += g(x)
                if x:
                    marginal_entropy -= x*mp.log(x)
                    energy += x*mp.log(y)
                if y:
                    divergence += d(x,y)
                    smooth += y*y*mp.log(mp.e/y)
                    assert g(x) <= d(x,y)+64*y*y*mp.log(mp.e/y)+tol
        lp = mp.log(real(permanent))
        s = real(sum(x*x for row in a for x in row))
        assert abs(lp-entropy-energy) < tol
        assert entropy <= marginal_entropy-n+correction+tol
        assert lp <= -n+correction-divergence+tol
        assert lp <= -n+64*smooth+tol
        assert smooth <= s*(1+mp.log(n))+tol
        assert lp >= -n-tol
        count += 1

grid = [mp.mpf(0), mp.mpf(1)] + [mp.mpf(k)/100 for k in range(1,100)]
aa = [mp.mpf(10)**(-k) for k in range(1,31)] + grid[1:]
scalar_checks = 0
for a in aa:
    for q in grid:
        assert g(q) <= d(q,a)+64*a*a*mp.log(mp.e/a)+tol
        scalar_checks += 1

result = {'status':'PASS', 'matrices':count, 'sizes':'1..7',
          'scalar_checks':scalar_checks, 'decimal_precision':mp.mp.dps,
          'exact':'rational permanents and permutation marginals',
          'limitation':'logarithmic checks are numerical; universal proof is README.md'}
Path(__file__).with_name('verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
