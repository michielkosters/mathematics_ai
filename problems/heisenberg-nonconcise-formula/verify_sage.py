"""Exact supporting checks. The universal proof is in README.md."""
from sage.all import *
import json
from pathlib import Path

R = PolynomialRing(ZZ, names="r,s,t,u,v,w")
r,s,t,u,v,w = R.gens()

def mul(a,b):
    x,y,z = a
    X,Y,Z = b
    return (x+X,y+Y,z+Z+x*Y)

def inv(a):
    x,y,z = a
    return (-x,-y,x*y-z)

def comm(a,b):
    return mul(mul(mul(inv(a),inv(b)),a),b)

assert comm((r,s,t),(u,v,w)) == (0,0,r*v-s*u)
assert mul((r,0,t-r*s),(0,s,0)) == (r,s,t)
assert mul((0,s,t),(r,0,0)) == (r,s,t)
assert comm((r,0,t-r*s),(1,0,0)) == (0,0,0)
assert comm((0,s,0),(0,1,0)) == (0,0,0)
assert comm((1,0,0),(0,1,0)) == (0,0,1)
assert comm((0,1,0),(1,0,0)) == (0,0,-1)

checked = 0
for x in range(-5,6):
    for y in range(-5,6):
        if gcd(x,y) != 1:
            continue
        g,A,B = xgcd(ZZ(x),ZZ(y))
        assert g == 1 and x*A+y*B == 1
        assert comm((x,y,0),(-B,A,0)) == (0,0,1)
        for X in range(-5,6):
            for Y in range(-5,6):
                if x*Y-y*X == 0:
                    k=A*X+B*Y
                    assert (X,Y) == (k*x,k*y)
                checked += 1

result = {"symbolic_commutator": True, "both_factorizations": True,
          "both_central_generator_values": True,
          "primitive_kernel_sample_checks": checked,
          "full_result_basis": "Deductive proof in README.md; not finite enumeration"}
Path(__file__).with_name("verification.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps(result))
