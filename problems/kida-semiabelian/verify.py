"""Run: sage -python problems/kida-semiabelian/verify.py. No input files needed."""
from sage.all import libgap as gap
from pathlib import Path
import json

# Signed coordinate permutations act on +1,+i,+j,+k,-1,-i,-j,-k.
def signed(p,signs):
    return [p[i]+(4 if signs[i]<0 else 0)+1 for i in range(4)]+[p[i]+(0 if signs[i]<0 else 4)+1 for i in range(4)]
def perm(p,signs=(1,1,1,1)):
    return gap.PermList(signed(p,signs))
one=[0,1,2,3]
dgens=[perm(one,tuple(-1 if i in [0,j] else 1 for i in range(4))) for j in [1,2,3]]
c=perm([0,2,3,1]); v=perm([1,0,3,2])
D=gap.Group(dgens); T=gap.Group([c,v]); G=gap.Group(dgens+[c,v])
i=perm([1,0,3,2],(1,-1,1,-1))
j=perm([2,3,0,1],(1,-1,-1,1))
Q=gap.Group([i,j]); H=gap.Group([i,j,c])
assert int(D.Size())==8 and bool(D.IsAbelian())
assert int(T.Size())==12 and int(G.Size())==96
assert bool(gap.IsNormal(G,D)) and int(gap.Intersection(D,T).Size())==1
C=gap.Group([c]); V=T.DerivedSubgroup()
assert int(C.Size())==3 and int(V.Size())==4 and bool(V.IsAbelian())
assert bool(gap.IsNormal(T,V)) and int(gap.Intersection(C,V).Size())==1
assert int(Q.Size())==8 and int(H.Size())==24
assert bool(gap.IsSubgroup(G,H))
assert int(H.DerivedSubgroup().Size())==8
degrees=[int(x[0]) for x in gap.Irr(H)]
assert 2 in degrees
cosets=gap.RightCosets(G,H)
assert len(cosets)==4
gens=list(G.GeneratorsOfGroup())
action=gap.ActionHomomorphism(G,cosets,gap.OnRight)

# Retain the original faithful degree8 action and append4 blocks of3.
# Each base generator cycles one block; G permutes blocks by its coset action.
lifted=[]
for g in gens:
    a=gap.Image(action,g)
    arr=[int(gap.OnPoints(k,g)) for k in range(1,9)]
    arr += [8+3*(int(gap.OnPoints(b+1,a))-1)+t+1 for b in range(4) for t in range(3)]
    lifted.append(gap.PermList(arr))
base=[]
for b in range(4):
    arr=list(range(1,21))
    for t in range(3):arr[8+3*b+t]=8+3*b+(t+1)%3+1
    base.append(gap.PermList(arr))
# Three differences generate the sum-zero submodule of F3^4.
augmentation=[base[k]*base[0]**-1 for k in range(1,4)]
A=gap.Group(augmentation); complement=gap.Group(lifted)
L=gap.Group(augmentation+lifted)
assert int(A.Size())==27 and bool(A.IsAbelian())
assert bool(gap.IsNormal(L,A)) and int(L.Size())==2592
assert int(complement.Size())==96 and int(gap.Intersection(A,complement).Size())==1
assert bool(gap.IsNormal(H,Q))
assert int(gap.Intersection(Q,C).Size())==1
result={
    "group_order":int(L.Size()),
    "semiabelian_chain_orders":[1,int(C.Size()),int(T.Size()),int(G.Size()),int(L.Size())],
    "abelian_factor_orders":[3,int(V.Size()),int(D.Size()),int(A.Size())],
    "H_order":int(H.Size()),
    "H_derived_order":int(H.DerivedSubgroup().Size()),
    "H_character_degrees":sorted(degrees),
    "coset_count":len(cosets),
    "sage_version":__import__("sage.env",fromlist=["SAGE_VERSION"]).SAGE_VERSION,
    "gap_version":str(gap.eval("GAPInfo.Version")),
    "generators":[list(map(int,gap.ListPerm(x,20))) for x in augmentation+lifted],
}
print("Structural checks passed; testing monomiality...",flush=True)
result["is_monomial"]=bool(gap.IsMonomial(L))
assert result["is_monomial"] is False
Path(__file__).with_name("certificate.json").write_text(json.dumps(result,indent=2)+"\n")
print("PASS: semiabelian construction, order 2592; IsMonomial = false.",flush=True)
