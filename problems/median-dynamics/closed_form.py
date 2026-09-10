"""Exact derivation from an independently specified neighbour table.

Run as closed_form.py in the published folder. No imports from verify.py.
"""
from pathlib import Path
import sympy as sp

NEIGHBOURS = ((1,4,5),(0,2),(1,3,5),(2,4,5),(0,3,5),(0,2,3,4))
STATES = range(64)
bit = lambda state, vertex: (state >> vertex) & 1
edges = [(v,w) for v,ns in enumerate(NEIGHBOURS) for w in ns if v<w]
assert len(edges)==9
assert all(v in NEIGHBOURS[w] for v,ns in enumerate(NEIGHBOURS) for w in ns)

flips={}
for state in STATES:
    flips[state]=[]
    for v,ns in enumerate(NEIGHBOURS):
        disagree=sum(bit(state,v)!=bit(state,w) for w in ns)
        if 2*disagree>len(ns):
            flips[state].append(state^(1<<v))
g={state:sum(bit(nxt,1)-bit(state,1) for nxt in flips[state]) for state in STATES}
energy=lambda state:sum(bit(state,v)!=bit(state,w) for v,w in edges)
z,t=sp.symbols('z t',positive=True)
u={}
for state in sorted(STATES,key=energy):
    assert all(energy(nxt)<energy(state) for nxt in flips[state])
    u[state]=sp.cancel((g[state]+sum(u[nxt] for nxt in flips[state]))/(z+len(flips[state])))
for state in STATES:
    residual=(z+len(flips[state]))*u[state]-sum(u[nxt] for nxt in flips[state])-g[state]
    assert sp.cancel(residual)==0

transform=sp.cancel(sum(3**(6-state.bit_count())*u[state] for state in STATES)/4096)
expected_transform=(36/(z+1)**3-93/(z+1)**2-275/(z+1)+27/(z+3)**2+27/(z+3)-40/(z+4))/3072
assert sp.cancel(transform-expected_transform)==0
expected=((18*t**2-93*t-275)*sp.exp(-t)+27*(t+1)*sp.exp(-3*t)-40*sp.exp(-4*t))/3072
derived=sp.inverse_laplace_transform(sp.apart(transform,z),z,t)
assert sp.simplify(derived-expected)==0
assert sp.simplify(expected.subs(t,0))==sp.Rational(-3,32)
at_eight=(133*sp.exp(-8)+243*sp.exp(-24)-40*sp.exp(-32))/3072
assert sp.simplify(expected.subs(t,8)-at_eight)==0
# Sign is elementary: 133 exp(-8)>40 exp(-32), and 243 exp(-24)>0.
Path(__file__).with_name('closed_form.txt').write_text(
    'Laplace transform of derivative:\n'+str(sp.apart(transform,z))+
    '\n\nDerivative:\n'+str(sp.expand(expected))+'\n',encoding='utf-8')
print('PASS: all 64 resolvent equations, the displayed rational identity, inverse transform and t=8 identity (exact).')
