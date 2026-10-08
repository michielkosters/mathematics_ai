"""Audit global pairing alignment in the community's existing bit DAG.

The DAG merger and reversible frame proof are community prior art. This
changes local point orders to retain one common global block partition.
"""
import sys
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
import json
sys.path.insert(0,str(Path(__file__).resolve().parent/'vendor'))
from shared_point_circuit import SharedPointCircuit
from paired_exclusion_circuit import PairedExclusionCircuit
from optimize_fourier import Network,saving_interval,decimal


class AlignedCircuit(SharedPointCircuit):
    def __init__(self,h,local=None,order='aligned'):
        self.h=h;self.local=local or PairedExclusionCircuit(h-1)
        assert h%2==0 and self.local.n==h-1
        self.inputs=list(combinations(range(h),3))
        self.variables={t:i+1 for i,t in enumerate(self.inputs)}
        self.args=[None]*(len(self.inputs)+1)
        self.core=[0]+[sum(1<<i for i in t) for t in self.inputs]
        self.union=self.core[:];self.provenance=[None]*len(self.args)
        self.points=[]
        for common in range(h):
            if order=='original': points=[j for j in range(h) if j!=common]
            elif order=='xor_tree': points=sorted((j for j in range(h) if j!=common),key=lambda j:j^common,reverse=True)
            else:
                mate=common^1
                points=[j for j in range(h) if j not in (common,mate)]+[mate]
                if order=='aligned_front': points=[mate]+points[:-1]
            self.points.append(points)
        self.pair_ids=[{tuple(sorted(points[k] for k in pair)):i+1
                       for i,pair in enumerate(self.local.inputs)} for points in self.points]
        lookup={};self.outputs={};self.merged=0
        for common in range(h):
            mapping={}
            for node in sorted(self.local.active):
                if self.local.args[node] is None:
                    a,b=self.local.inputs[node-1]
                    t=tuple(sorted((common,self.points[common][a],self.points[common][b])))
                    mapping[node]=self.variables[t];continue
                a,b=(mapping[x] for x in self.local.args[node])
                core=self.core[a]&self.core[b];union=self.union[a]|self.union[b]
                key=(core,union)
                if core.bit_count()>=2 and key in lookup:
                    mapping[node]=lookup[key];self.merged+=1;continue
                new=len(self.args);mapping[node]=new
                self.args.append((a,b));self.core.append(core);self.union.append(union)
                self.provenance.append((common,node))
                if core.bit_count()>=2: lookup[key]=new
            for pair,node in sorted(self.local.outputs.items()):
                t=tuple(sorted((common,*(self.points[common][x] for x in pair))))
                self.outputs[common,t]=mapping[node]
        self.active=set();stack=list(self.outputs.values())
        while stack:
            n=stack.pop()
            if n in self.active: continue
            self.active.add(n)
            if self.args[n]:stack.extend(self.args[n])
        self.additions=sum(self.args[n] is not None for n in self.active)

    def verify(self):
        self.local.verify()
        for node in sorted(self.active):
            if self.args[node]:
                a,b=self.args[node];common,local=self.provenance[node]
                assert a<node and b<node
                sa=self.support_in(a,common);sb=self.support_in(b,common)
                assert not sa&sb
                assert sa|sb==self.local.support[local]
                assert self.core[node]==self.core[a]&self.core[b]
                assert self.union[node]==self.union[a]|self.union[b]
            assert self.core[node]
        for (common,target),node in self.outputs.items():
            excluded=tuple(sorted(self.points[common].index(x) for x in target if x!=common))
            assert self.support_in(node,common)==self.local.support[self.local.outputs[excluded]]
        return dict(h=self.h,all_additions_disjoint=True,all_partial_outputs_exact=True,
                    roles=self.additions+len(self.outputs))


def counts(c):
    h=c.h;v=len(c.inputs);r=c.additions+len(c.outputs)
    w=2*v**3+2*v*v*(r+h);d=v*v*(v-6*h*h)
    n=Network(h,v,0,h**3,w,d)
    if d<=0:return dict(h=h,roles=r,positive=False)
    lo,hi=saving_interval(n,False)
    return dict(h=h,roles=r,additions=c.additions,merged=c.merged,
                wires=w,saving=d,bit_saving_lower=decimal(lo),bit_saving_upper=decimal(hi))

