# Counterexample to time monotonicity in majority dynamics and the median process

**Complete refutation of Conjectures 3.1 and 3.2 (equivalent time-monotonicity formulations). Novelty unestablished.**

Original source: Gideon Amir, Rangel Baldasso and Nissan Beilin, *Majority dynamics and the median process: connections, convergence and some new conjectures*, [arXiv:1911.08613v2, §3](https://arxiv.org/html/1911.08613v2#S3), [PDF](https://arxiv.org/pdf/1911.08613v2).

For iid Bernoulli(p) initial bits with p <= 1/2, the conjecture asserts that each vertex's probability of bit 1 is non-increasing in time. Each vertex updates at rate one to its neighbours' majority, retaining its bit in a tie. The thresholded median process has this law.

Our six-vertex example has a strictly positive marginal derivative at time 8 for p=1/4. The [complete proof](proof.md) gives the graph and exact formula. A [cubic ten-vertex strengthening](followup.md) removes ties entirely. It is a second witness to the same failed conjecture, not another solved problem. Other conjectures in the paper remain outside this result.

From the repository root:

```sh
python problems/median-dynamics/verify.py
python problems/median-dynamics/verify_regular.py
python problems/median-dynamics/closed_form.py
```

The first two scripts use exact integer and rational arithmetic and rigorous tail bounds, with no third-party dependencies. The third uses SymPy to independently derive the six-vertex exponential formula. Outputs are `certificate.json`, `regular_certificate.json` and `closed_form.txt`.

Dataset provenance: [Ulam AI / UnsolvedMath](https://huggingface.co/datasets/ulamai/UnsolvedMath), internal record ID `30004591`. This ID is an import key, not a number assigned by the paper. See the repository README for snapshot attribution.

Upstream identifiers: `OWR-4990373-005`, UnsolvedMath `30004591`, [Oberwolfach Reports 2021/4](https://doi.org/10.4171/OWR/2021/4). The precise claim is matched to arXiv:1911.08613v2 Conjectures 3.1/3.2 above. [Project GitHub](https://github.com/michielkosters/mathematics_ai).
