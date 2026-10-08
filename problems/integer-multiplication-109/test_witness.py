import unittest
from fractions import Fraction as F
from types import SimpleNamespace
from itertools import combinations
from hypergraph_complex import Circuit,subsets
from aligned_bit_circuit import AlignedCircuit
from paired_exclusion_circuit import PairedExclusionCircuit
from exclusion_circuit import ExclusionCircuit


class HypergraphTests(unittest.TestCase):
    def test_complete_disjoint_matrix_and_frames(self):
        for anchors in (1,2,3,4):
            c=Circuit(8).build(anchors)
            self.assertTrue(c.verify()['all_disjoint_coefficients_exact'])
            for n in c.active:
                if c.args[n]:
                    for child in c.args[n]:
                        if c.args[child] is None:
                            self.assertTrue(c.union[n]&~c.union[child])

    def test_lazy_partition_matches_full_matrix(self):
        c=Circuit(8).build_lazy(2)
        self.assertTrue(c.verify()['coordinate_frame_residuals_nonalternating'])

    def test_weighted_lower_rank_edges(self):
        c=Circuit(8);weights={}
        for t,n in c.variables.items():
            key=frozenset(p%5 for p in t)
            weights[key]=c.add(weights.get(key,0),n)
        answer=c.exclusions(list(range(5)),weights,3)
        for e in subsets(list(range(5)),3):
            expected=0
            for edge,n in weights.items():
                if not edge&e:expected|=c.support[n]
            self.assertEqual(c.support[answer[e]],expected)

    def test_compiled_disjoint_circuit_restores_dirty_values(self):
        c=Circuit(8).build(2)
        outputs={(a,t):n for a,(n,t) in enumerate(c.outputs)}
        adapter=SimpleNamespace(active=c.active,args=c.args,inputs=c.triples,
                                outputs=outputs,additions=c.additions)
        code=ExclusionCircuit.compile(adapter)
        z=[F((i*17)%29-14,16) for i in range(code['roles'])];initial=z[:]
        values={t:F(i-19,8) for i,t in enumerate(c.triples)}
        y={t:F(0) for t in c.triples}
        def mixer(inverse=False):
            for _,ins,outs in reversed(code['gates']) if inverse else code['gates']:
                if inverse:
                    for role in outs[1:]:z[role]-=z[ins[0]]
                    for role in ins[1:]:z[ins[0]]-=z[role]
                else:
                    for role in ins[1:]:z[ins[0]]+=z[role]
                    for role in outs[1:]:z[role]+=z[ins[0]]
        mixer()
        for (_,t),role in code['outputs'].items():y[t]-=z[role]/2
        mixer(True)
        for t,role in code['sources'].items():z[role]+=values[t]
        mixer()
        for (_,t),role in code['outputs'].items():y[t]+=z[role]/2
        mixer(True)
        for t,role in code['sources'].items():z[role]-=values[t]
        self.assertEqual(z,initial)
        for t in c.triples:
            self.assertEqual(y[t],sum((v/2 for s,v in values.items() if not set(s)&set(t)),F(0)))

    def test_aligned_bit_exact(self):
        for h in (8,12):
            c=AlignedCircuit(h,PairedExclusionCircuit(h-1))
            self.assertTrue(c.verify()['all_partial_outputs_exact'])
            self.assertTrue(c.verify_frames()['forward_frames_nested'])


if __name__=='__main__':unittest.main()
