"""Cancellation-free weighted hypergraph exclusions for the complex side.

All nonleaf frames are coordinate spans. Designated sums covering all
coordinates outside their target are partitioned to avoid alternating
residuals. Builds a scalar DAG, not a certified multiplication machine.
"""
from itertools import combinations,product
from math import comb
from pathlib import Path
import json
from optimize_fourier import Network,saving_interval,decimal


def subsets(points,r):
    for k in range(min(len(points),r)+1):
        yield from (frozenset(t) for t in combinations(points,k))


class Circuit:
    def __init__(self,h):
        self.h=h;self.triples=list(combinations(range(h),3))
        self.variables={t:i+1 for i,t in enumerate(self.triples)}
        self.args=[None]*(len(self.triples)+1)
        self.support=[0]+[1<<i for i in range(len(self.triples))]
        self.union=[0]+[sum(1<<k for k in t) for t in self.triples]
        self.lookup={s:i for i,s in enumerate(self.support)}
        self.outputs=[];self.calls=0;self.split=0

    def add(self,a,b):
        if not a:return b
        if not b:return a
        assert not self.support[a]&self.support[b]
        s=self.support[a]|self.support[b]
        if s in self.lookup:return self.lookup[s]
        n=len(self.args);self.lookup[s]=n
        self.args.append((a,b));self.support.append(s);self.union.append(self.union[a]|self.union[b])
        return n

    def total(self,values):
        values=[v for v in values if v]
        if not values:return 0
        if len(values)==1:return values[0]
        m=len(values)//2
        return self.add(self.total(values[:m]),self.total(values[m:]))

    def exclusions(self,points,weights,r):
        self.calls+=1
        if r==0 or len(points)<=4:
            return {e:self.total([n for key,n in weights.items() if not key&e])
                    for e in subsets(points,r)}
        groups=[points[i:i+2] for i in range(0,len(points),2)]
        block={p:i for i,g in enumerate(groups) for p in g}
        def aggregate(fixed=()):
            fixed=frozenset(fixed);fb={block[p] for p in fixed};out={}
            for edge,n in weights.items():
                if not fixed<=edge:continue
                if any(block[p] in fb for p in edge-fixed):continue
                key=frozenset(block[p] for p in edge-fixed)
                out[key]=self.add(out.get(key,0),n)
            return out
        coarse=list(range(len(groups)))
        main=self.exclusions(coarse,aggregate(),r)
        boundary={};answer={}
        degree=max(map(len,weights),default=0)
        for e in subsets(points,r):
            deleted=frozenset(block[p] for p in e)
            survivors={b:[p for p in groups[b] if p not in e] for b in deleted}
            partial=[b for b in deleted if survivors[b]]
            parts=[main[deleted]]
            for size in range(1,min(len(partial),degree)+1):
                for bs in combinations(partial,size):
                    for fixed in product(*(survivors[b] for b in bs)):
                        fixed=tuple(sorted(fixed))
                        if fixed not in boundary:
                            remaining=[b for b in coarse if b not in bs]
                            boundary[fixed]=self.exclusions(remaining,aggregate(fixed),r-size)
                        parts.append(boundary[fixed][deleted-frozenset(bs)])
            answer[e]=self.total(parts)
        return answer

    def output(self,node,target):
        if not node:return
        tmask=sum(1<<k for k in target);allones=(1<<self.h)-1
        assert not self.union[node]&tmask
        if self.args[node] is None or (self.union[node]|tmask)!=allones:
            self.outputs.append((node,target));return
        self.split+=1
        # Any triple omits at least one of four selected non-target points.
        anchors=[k for k in range(self.h) if k not in target][:4]
        buckets=[[] for _ in anchors];s=self.support[node]
        while s:
            bit=s&-s;s-=bit;i=bit.bit_length()-1;triple=self.triples[i]
            first=next(a for a,k in enumerate(anchors) if k not in triple)
            buckets[first].append(i+1)
        for bucket in buckets:
            z=self.total(bucket)
            if z:self.outputs.append((z,target))

    def lazy_exclusions(self,points,weights):
        """Only construct exclusions actually requested by final outputs."""
        memo={};degree=max(map(len,weights),default=0)
        if len(points)<=4 or degree==0:
            def resolve(e):
                e=frozenset(e)
                if e not in memo:memo[e]=self.total([n for key,n in weights.items() if not key&e])
                return memo[e]
            return resolve
        groups=[points[i:i+2] for i in range(0,len(points),2)]
        block={p:i for i,g in enumerate(groups) for p in g};coarse=list(range(len(groups)))
        def aggregate(fixed=()):
            fixed=frozenset(fixed);fb={block[p] for p in fixed};out={}
            for edge,n in weights.items():
                if not fixed<=edge or any(block[p] in fb for p in edge-fixed):continue
                key=frozenset(block[p] for p in edge-fixed)
                out[key]=self.add(out.get(key,0),n)
            return out
        main=self.lazy_exclusions(coarse,aggregate());boundary={}
        def resolve(e):
            e=frozenset(e)
            if e in memo:return memo[e]
            deleted=frozenset(block[p] for p in e)
            survivors={b:[p for p in groups[b] if p not in e] for b in deleted}
            partial=[b for b in deleted if survivors[b]];parts=[main(deleted)]
            for size in range(1,min(len(partial),degree)+1):
                for bs in combinations(partial,size):
                    for fixed in product(*(survivors[b] for b in bs)):
                        fixed=tuple(sorted(fixed))
                        if fixed not in boundary:
                            boundary[fixed]=self.lazy_exclusions([b for b in coarse if b not in bs],aggregate(fixed))
                        parts.append(boundary[fixed](deleted-frozenset(bs)))
            memo[e]=self.total(parts);return memo[e]
        return resolve

    def build_lazy(self,anchors=2):
        a=list(range(anchors));b=list(range(anchors,self.h));allones=(1<<self.h)-1
        for fixed in subsets(a,3):
            degree=3-len(fixed)
            def helper(extra,omit=()):
                extra=frozenset(extra);omit=frozenset(omit);key=(extra,omit)
                if key not in solvers:
                    points=[p for p in b if p not in extra|omit]
                    weights={frozenset(t):self.variables[tuple(sorted(fixed|extra|frozenset(t)))]
                             for t in combinations(points,degree-len(extra))}
                    solvers[key]=self.lazy_exclusions(points,weights)
                return solvers[key]
            solvers={};base=helper(())
            for target in self.triples:
                if fixed&frozenset(target):continue
                excluded=frozenset(target)&frozenset(b);node=base(excluded)
                if not node:continue
                tmask=sum(1<<k for k in target)
                if self.args[node] is None or (self.union[node]|tmask)!=allones:
                    self.outputs.append((node,target));continue
                self.split+=1
                extra_anchors=[p for p in b if p not in target][:degree+1]
                prefix=[]
                for p in extra_anchors:
                    part=helper(prefix,(p,))(excluded)
                    if part:self.outputs.append((part,target))
                    prefix.append(p)
        self.active=set();stack=[n for n,_ in self.outputs]
        while stack:
            n=stack.pop()
            if n in self.active:continue
            self.active.add(n)
            if self.args[n]:stack.extend(self.args[n])
        self.additions=sum(self.args[n] is not None for n in self.active)
        return self

    def build(self,anchors=3):
        a=list(range(anchors));b=list(range(anchors,self.h))
        for fixed in subsets(a,3):
            degree=3-len(fixed)
            weights={frozenset(t):self.variables[tuple(sorted(fixed|frozenset(t)))]
                     for t in combinations(b,degree)}
            excluded=self.exclusions(b,weights,3)
            for target in self.triples:
                if not fixed&frozenset(target):self.output(excluded[frozenset(target)&frozenset(b)],target)
        self.active=set();stack=[n for n,_ in self.outputs]
        while stack:
            n=stack.pop()
            if n in self.active:continue
            self.active.add(n)
            if self.args[n]:stack.extend(self.args[n])
        self.additions=sum(self.args[n] is not None for n in self.active)
        return self

    def verify(self):
        allones=(1<<self.h)-1;acc={t:0 for t in self.triples}
        for n in self.active:
            if self.args[n]:
                a,b=self.args[n]
                assert not self.support[a]&self.support[b]
                assert self.support[n]==self.support[a]|self.support[b]
                assert self.union[n].bit_count()>=4
                assert not self.union[a]&~self.union[n] and not self.union[b]&~self.union[n]
        for n,t in self.outputs:
            mask=sum(1<<k for k in t)
            assert not self.union[n]&mask
            assert self.args[n] is None or (self.union[n]|mask)!=allones
            assert not acc[t]&self.support[n]
            acc[t]|=self.support[n]
        for t in self.triples:
            expected=sum(1<<i for i,s in enumerate(self.triples) if not set(s)&set(t))
            assert acc[t]==expected
        return dict(all_disjoint_coefficients_exact=True,coordinate_frame_residuals_nonalternating=True)


def counts(c):
    h=c.h;v=len(c.triples)
    # Separate fixed-pair leave-one-out circuit for intersection-two terms:
    # prefix/suffix: 3n-6 additions, n outputs for n=h-2>=3.
    intersection_roles=comb(h,2)*(4*(h-2)-6)
    r=c.additions+len(c.outputs)+intersection_roles
    w=2*v**3+2*v*v*(r+h);d=2*v*v*(v-3*h*h)
    n=Network(h,v,0,h**3,w,d);lo,hi=saving_interval(n,False)
    return dict(h=h,disjoint_additions=c.additions,disjoint_outputs=len(c.outputs),
        split_outputs=c.split,intersection_two_roles=intersection_roles,roles=r,
        wires=w,saving=d,complex_saving_lower=decimal(lo),complex_saving_upper=decimal(hi),
        status='local circuit/frame checks; full transfer and precision integration pending')

