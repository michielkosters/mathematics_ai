"""Derive an exact exponential-polynomial formula via the acyclic flip graph."""
import sympy as s
from pathlib import Path
from verify import dest,EDGES,g,weights,denominator
z,t=s.symbols('z t', positive=True)
energy=lambda state:sum(((state>>a)^(state>>b))&1 for a,b in EDGES)
u={}
for state in sorted(range(64),key=energy):
    changes=[d for d in dest[state] if d!=state]
    assert all(energy(d)<energy(state) for d in changes)
    u[state]=s.cancel((g[state]+sum(u[d] for d in changes))/(z+len(changes)))
laplace=s.factor(sum(weights[state]*u[state] for state in range(64))/denominator)
apart=s.apart(laplace,z)
expression=s.expand(s.inverse_laplace_transform(apart,z,t))
assert s.simplify(expression.subs(t,0))==s.Rational(-3,32)
assert abs(float(expression.subs(t,8))-1.4523612852898648e-5)<1e-15
Path(__file__).with_name('closed_form.txt').write_text('Laplace transform of derivative:\n'+str(apart)+'\n\nDerivative:\n'+str(expression)+'\n')
print(expression)
