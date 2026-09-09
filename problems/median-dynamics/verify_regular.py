"""Exact rational uniformization certificate for a cubic counterexample."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
N=10; T=10; K=400; V=1; L=N*T
EDGES=[(0,1),(0,6),(0,2),(1,5),(1,3),(2,5),(2,8),(3,4),(3,9),(4,9),(4,7),(5,6),(6,8),(7,9),(7,8)]
nb=[[b if a==v else a for a,b in EDGES if v in (a,b)] for v in range(N)]
assert all(len(ns)==3 for ns in nb)
dest=[]
for state in range(1<<N):
 dest.append([state^((((state>>v)&1)^int(sum((state>>u)&1 for u in nb[v])>=2))<<v) for v in range(N)])
f=[(s>>V)&1 for s in range(1<<N)]
g=[sum(f[d]-f[s] for d in dest[s]) for s in range(1<<N)]
assert max(map(abs,g))<=1
weights=[2**s.bit_count()*3**(N-s.bit_count()) for s in range(1<<N)]
den=5**N
assert sum(weights)==den
assert F(sum(w*x for w,x in zip(weights,g)),den)==F(-6,125)
# Q=H-NI; H counts the N possible clock events. Thus
# exp(NT)m'(T)=sum T^k/k! pi H^k g. Bound |pi(H/N)^k g|<=1.
vector=g; partial=F(0); coefficient=F(1)
for k in range(K+1):
 partial+=coefficient*F(sum(w*x for w,x in zip(weights,vector)),den)
 vector=[sum(vector[d] for d in ds) for ds in dest]
 coefficient*=F(T,k+1)
tail=F(L**(K+1),factorial(K+1))/(1-F(L,K+2))
assert partial>tail>0
upper=sum((F(L**k,factorial(k)) for k in range(K+1)),F(0))+tail
lower=(partial-tail)/upper
assert lower>F(9,10**7)
result=dict(verified=True,n=N,degree=3,edges=EDGES,vertex=V,p='2/5',time=T,
            derivative_lower_bound='9/10000000',series_degree=K,
            novelty='Unestablished; strengthens existing time-monotonicity refutation, not a separate conjecture.')
Path(__file__).with_name('regular_certificate.json').write_text(json.dumps(result,indent=2))
print('EXACTLY VERIFIED: cubic graph, p=2/5, vertex1, m_prime(10)>9/10000000.')
