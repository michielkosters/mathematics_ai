"""Exact supporting checks for the Shinohara lattice argument; not a formal proof."""
from sage.all import *
from pathlib import Path
import json

def blocks(n):
    if not ZZ(n).is_square():
        a=next(a for a in range(1,n) if kronecker(a,n)==-1)
        return [(n,a)]
    fac=list(factor(n)); p,e=fac[0]
    # For p-primary odd exponents the product of the two epsilon factors
    # is (-1/p). Choose the second coefficient to make the Gauss phase -1.
    target=-kronecker(-1,p)
    a=next(a for a in range(1,p) if kronecker(a,p)==target)
    return [(p**(e-1),1),(p,a)]+[(q**f,1) for q,f in fac[1:]]

tested=[]
for n in list(range(5,102,4))+[121,169,225,289]:
    bs=blocks(n)
    assert prod(m for m,a in bs)==n
    total=QQbar(1)
    for m,a in bs:
        assert gcd(m,a)==1
        z=CyclotomicField(m).gen()
        total*=QQbar(sum(z**((a*x*x)%m) for x in range(m)))
    assert total == -QQbar(n).sqrt()
    tested.append(n)

def seifert_from_even(S):
    n=S.nrows(); U=identity_matrix(ZZ,n)
    # Integer elementary column operations implement symplectic reduction mod 2.
    for k in range(0,n,2):
        B=U.transpose()*S*U
        pair=next((i,j) for i in range(k,n) for j in range(i+1,n) if B[i,j]%2)
        U.swap_columns(k,pair[0]); U.swap_columns(k+1,pair[1])
        for j in range(k+2,n):
            B=U.transpose()*S*U
            alpha=B[k+1,j]%2; beta=B[k,j]%2
            U.set_column(j,U.column(j)+alpha*U.column(k)+beta*U.column(k+1))
    J=block_diagonal_matrix([matrix(ZZ,[[0,1],[-1,0]]) for _ in range(n//2)])
    B=U.transpose()*S*U
    assert abs(U.det())==1
    assert matrix(GF(2),B)==matrix(GF(2),J)
    V=matrix(ZZ,(B+J)/2)
    assert V-V.transpose()==J
    assert V+V.transpose()==B
    assert (V-V.transpose()).det()==1
    return V,U

examples=[]
matrices=[
    matrix(ZZ,[[2,-1,0,-1],[-1,2,0,0],[0,0,2,-1],[-1,0,-1,4]]),
    matrix(ZZ,[[4,-2,0,-1],[-2,4,-1,2],[0,-1,4,0],[-1,2,0,66]])]
for S in matrices:
    assert all(S[i,i]%2==0 for i in range(4))
    assert all(S[:i,:i].det()>0 for i in range(1,5))
    V,U=seifert_from_even(S)
    examples.append({'determinant':int(S.det()),'signature':4,
      'S':[[int(x) for x in row] for row in S.rows()],
      'U':[[int(x) for x in row] for row in U.rows()],
      'V':[[int(x) for x in row] for row in V.rows()]})

result={'status':'PASS','gauss_sum_orders':tested,'exact_arithmetic':'cyclotomic fields and QQbar; integer matrices',
        'examples':examples,'limitation':'Finite supporting checks; the universal existence proof uses Nikulin and Seifert realization.'}
Path(__file__).with_name('verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
