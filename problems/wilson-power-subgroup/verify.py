"""Exact standard-library verification of D8 wr C2; no GAP data needed."""
from itertools import product
from pathlib import Path
import json

# D8 = <r,s | r^4=s^2=1, s*r*s=r^-1>; (a,b) means r^a s^b.
def dm(x,y):
    return ((x[0]+(-1)**x[1]*y[0])%4, x[1]^y[1])

# (x,y,t) means (x,y)*swap^t in (D8 x D8) semidirect C2.
def mul(g,h):
    x,y,t=g
    a,b,u=h
    if t:a,b=b,a
    return (dm(x,a),dm(y,b),t^u)

e=(0,0); r=(1,0); s=(0,1); z=(2,0)
identity=(e,e,0)
D=list(product(range(4),range(2)))
G=list(product(D,D,range(2)))
def square(g):return mul(g,g)
assert len(G)==128
assert all(square(square(square(g)))==identity for g in G)
x=(r,e,1); y=(s,e,1)
assert square(square(x))!=identity # x has order 8
squares={square(g) for g in G}
expected={(g,dm(g,c),0) for g in D for c in (e,z)}
assert squares==expected and len(squares)==16
assert all(mul(a,b) in squares for a in squares for b in squares)
assert all(square(square(a))==identity for a in squares)
a,b=square(x),square(y)
assert a==(r,r,0) and b==(s,s,0)
assert mul(a,b)!=mul(b,a)
result={"construction":"D8 wr C2, where |D8|=8","group_order":128,
        "exponent":8,"square_count":16,"squares_form_subgroup":True,
        "square_subgroup_exponent":4,"square_subgroup_abelian":False,
        "noncommuting_square_roots":[x,y],"square_products":[mul(a,b),mul(b,a)],
        "scope":"Refutes the general powerful-subgroup assertion and its p=2 case; odd-prime question not settled."}
Path(__file__).with_name("verification.json").write_text(json.dumps(result,indent=2)+"\n")
print("PASS: order 128, exponent 8; 16 squares form a nonabelian subgroup of exponent 4.")
