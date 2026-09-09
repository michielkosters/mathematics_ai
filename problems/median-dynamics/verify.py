"""Pure Python exact certificate: positive marginal derivative at t=8.

No scipy, numerical exponentials, or symbolic library is used.
Uniformization Q=6(P-I), H=6P. Bound omitted exponential series geometrically.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

N=6; VERTEX=1; T=8; K=220
EDGES=[(0,1),(0,4),(0,5),(1,2),(2,3),(2,5),(3,4),(3,5),(4,5)]
neighbors=[[b if a==v else a for a,b in EDGES if v in (a,b)] for v in range(N)]
dest=[]
for s in range(1<<N):
    updates=[]
    for v,nb in enumerate(neighbors):
        ones=sum((s>>u)&1 for u in nb)
        old=(s>>v)&1
        new=1 if 2*ones>len(nb) else 0 if 2*ones<len(nb) else old
        updates.append(s^((old^new)<<v))
    dest.append(updates)
# H counts all six possible clock events, including null events.
assert all(len(d)==N for d in dest)
f=[(s>>VERTEX)&1 for s in range(1<<N)]
g=[sum(f[d]-f[s] for d in dest[s]) for s in range(1<<N)]
assert max(map(abs,g))<=1
weights=[3**(N-s.bit_count()) for s in range(1<<N)]
denominator=4**N
assert sum(weights)==denominator
assert F(sum(w*x for w,x in zip(weights,g)),denominator)==F(-3,32)
assert all(dest[63-s][v]==63-dest[s][v] for s in range(64) for v in range(N))

# e^48 m'(8) = sum_{k>=0} 8^k/k! pi H^k g.
vector=g[:]; partial=F(0); coefficient=F(1)
for k in range(K+1):
    partial+=coefficient*F(sum(w*x for w,x in zip(weights,vector)),denominator)
    vector=[sum(vector[d] for d in updates) for updates in dest]
    coefficient*=F(T,k+1)
# |pi P^k g|<=1 as P is stochastic. For k>=K+1 successive
# terms 48^k/k! have ratio <=48/(K+2)<1.
tail=F(48**(K+1),factorial(K+1))/(1-F(48,K+2))
assert partial>tail>0
# Since e^48 <= sum_{k=0}^K48^k/k!+tail, obtain a lower bound
# on the derivative itself (positive numerator / upper denominator).
exp_upper=sum((F(48**k,factorial(k)) for k in range(K+1)),F(0))+tail
lower=(partial-tail)/exp_upper
assert lower>F(1,100000) # explicit and readily readable bound
record=dict(verified=True,vertices=N,edges=EDGES,vertex=VERTEX,
            initial_p='1/4',time=T,series_degree=K,
            derivative_lower_bound='1/100000',
            exact_lower_numerator=str(lower.numerator),exact_lower_denominator=str(lower.denominator),
            statement='The marginal probability of opinion 1 has strictly positive derivative at t=8, contradicting Conjecture 3.2.',
            novelty='Not established; source and literature audit required.')
Path(__file__).with_name('certificate.json').write_text(json.dumps(record,indent=2))
print('VERIFIED EXACTLY: m_prime(8) > 1/100000 for p=1/4 on specified six-vertex graph.')
