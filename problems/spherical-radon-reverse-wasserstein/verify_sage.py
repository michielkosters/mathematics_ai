"""Exact supporting checks, not a formal proof of the transport theorem."""
from sage.all import QQ, PolynomialRing, legendre_P, binomial
from pathlib import Path
import json

R = PolynomialRing(QQ, 'z')
z = R.gen()
checks = []
for k in range(1, 13):
    P = R(legendre_P(2*k, z))
    lam = QQ((-1)**k * binomial(2*k, k)) / 4**k
    assert P(0) == lam and P(-z) == P
    primitive = P.integral()
    assert primitive(1) == primitive(-1)
    # On the equator perpendicular to a vector of height z, the height
    # coordinate is sqrt(1-z^2)*cos(phi). Its even moments are exact.
    average = sum(P[2*j] * (1-z*z)**j * QQ(binomial(2*j,j))/4**j
                  for j in range(k+1))
    assert average == lam*P
    checks.append({'degree':2*k, 'eigenvalue':str(lam), 'passed':True})
b100 = QQ(binomial(200,100))/4**100
assert b100 < QQ(1)/17
result = {'status':'PASS', 'exact_polynomial_checks':checks,
          'k100_ratio':str(b100), 'k100_ratio_less_than_1_over_17':True,
          'scope':'Supporting identities only; universal proof is in README.md.'}
Path(__file__).with_name('verification.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: 12 exact equator identities, parity and mean checks; k=100 bound.')
