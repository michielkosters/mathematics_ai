"""Exact conditional assembly arithmetic for the screened hypergraph motif."""
from fractions import Fraction as F
from pathlib import Path
import json
from hypergraph_complex import Circuit,counts
from aligned_bit_circuit import AlignedCircuit,counts as bit_counts
import vendor.certify as arithmetic
from optimize_fourier import decimal


def certificate():
    complex_circuit=Circuit(26).build(2)
    complex_result=counts(complex_circuit)
    complex_result['verification']=complex_circuit.verify()
    bit=AlignedCircuit(50)
    bit_result=bit_counts(bit)
    bit_result['verification']=bit.verify()
    bit_result['frames']=bit.verify_frames()
    a=arithmetic
    p=a.Parameters(tau=1-F(3050,10**12),sigma=1-F(2874,10**11),
        epsilon=F(1999,10000),c=F(1),lam=1-F(3049,10**12),
        lamp=1-F(3048,10**12),kappa=F(609,10**12),beta=F(1,1000),
        delta=F(1,10**6),C1=F(49961,10000))
    slacks=a.constraints(p,layout_model='nonadjacent',assembly_model='tight-gaussian')
    slacks['packed_overhead']=p.lam-(p.tau+(1-p.beta)*max(p.sigma-p.tau,F(0)))
    slacks['reserved_axes']=p.lamp-max(F(0),1-p.c)
    margins=a.margins(p,layout_model='nonadjacent',assembly_model='tight-gaussian')
    assert all(x>0 for x in slacks.values()) and min(margins.values())>p.kappa
    assert F(complex_result['complex_saving_lower'])>1-p.sigma
    assert F(bit_result['bit_saving_lower'])>1-p.tau
    m=26**3;s=complex_result['wires']*m-complex_result['saving']
    assert 2<=s<m**5
    return dict(status='conditional research candidate; complete upstream integration unverified',
        kappa=str(p.kappa),kappa_decimal=decimal(p.kappa),ratio_to_community=str(p.kappa/F(83,10**12)),
        complex=complex_result,bit=bit_result,
        parameters={k:str(v) for k,v in vars(p).items()},
        slacks={k:str(v) for k,v in slacks.items()},
        margins={k:str(v) for k,v in margins.items()},
        scoped_bit_ceiling=str(F(bit_result['bit_saving_upper'])/5),
        guard_size_hypothesis_checked=True,
        unresolved=['Complete motif-to-tape transfer and precision guard integration',
                    'Independent mathematical review','Global novelty clearance'])

