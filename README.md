# AI-assisted mathematics

We use AI to find proofs and counterexamples to unsolved mathematical conjectures. Our aim is to solve as many worthwhile problems as possible with efficient reasoning, modest computation, and results that other mathematicians can easily check.

We screen problems for precise statements and feasible approaches, check the existing literature, and then look for short arguments or explicit constructions. We use Python, SageMath, or Lean when they help verify a result. Each solution comes with its source, proof, and reproducible verification where applicable.

## Where the problems come from

Our starting collection is [Ulam AI's UnsolvedMath](https://www.unsolvedmath.com/), available as a [Git repository on Hugging Face](https://huggingface.co/datasets/ulamai/UnsolvedMath/tree/main), with records in [problems.json](https://huggingface.co/datasets/ulamai/UnsolvedMath/blob/main/problems.json). It collects questions from research papers, Oberwolfach Reports, Open Problem Garden, and other mathematical sources. We return to the original sources to check the statements and their status before attempting a solution.

Our imported snapshot is version 1.6.0, revision `b9437975f3c873f635a13c48f8b022f5ba80898a`. Credit for the dataset belongs to Ulam AI / UnsolvedMath contributors, under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); original mathematical sources retain their own attribution and terms. The problem data came from Hugging Face, not a GitHub mirror. Our work is collected at [michielkosters/mathematics_ai on GitHub](https://github.com/michielkosters/mathematics_ai).

## Solutions

This table grows as we complete and verify solutions. It includes complete resolutions of the stated conjectures, rather than partial progress or transcription corrections. Complete answers deduced from existing theorems are explicitly credited as such. Novelty assessments are separate from mathematical verification.

| Problem | Original source | Result | Proof and verification |
|---|---|---|---|
| Time monotonicity in majority dynamics / the median process | Amir, Baldasso and Beilin, *Majority dynamics and the median process: connections, convergence and some new conjectures*, [arXiv:1911.08613v2, Conjectures 3.1 and 3.2](https://arxiv.org/html/1911.08613v2#S3) | Complete counterexample, with a cubic-graph strengthening. Novelty unestablished. | [Solution folder](problems/median-dynamics/README.md) |
| Kida's semiabelian-group conjecture | Masanari Kida, [*On semiabelian groups*, Conjecture 1.3](https://doi.org/10.1515/jgth-2024-0010); [Kourovka Notebook 21.68](https://alglog.org/21tkt.pdf) | Complete counterexample of order 2592. No prior resolution found; priority unconfirmed. | [Proof and Sage verification](problems/kida-semiabelian/README.md) |
| Wilson's power-subgroup question | L. Wilson, [Kourovka Notebook 21.137, p. 181](https://alglog.org/21tkt.pdf) | Main universal claim refuted by an order-128 group. Separate odd-prime question unresolved; novelty unconfirmed. | [Short proof and Python verification](problems/wilson-power-subgroup/README.md) |
| Three-generated torsion-free nilpotent groups of class three: self-similarity | A. Dantas and S. Sidki, [Kourovka Notebook 21.42](https://alglog.org/21tkt.pdf); Berlatto–Gentil, [arXiv:2509.16947v1, Problem 1](https://arxiv.org/html/2509.16947v1) | Every such group is self-similar. Complete consequence of established theorems; no novelty claimed. | [Short proof](problems/three-generator-self-similarity/README.md) and [verification](problems/three-generator-self-similarity/verification.md) |
| Golod construction with a nontrivial finite centre | A. V. Timofeenko, [Kourovka Notebook 21.132, p. 180](https://alglog.org/21tkt.pdf) | For every prime p, an infinite residually finite torsion p-group with at most four generators and centre C_p. Built from classical results; novelty unestablished. | [Complete proof](problems/golod-finite-centre/README.md) and [verification](problems/golod-finite-centre/verification.md) |

The two conjecture numbers for median dynamics are equivalent formulations of the same time-monotonicity claim. The result does not address the paper's separate convexity or convergence questions.

## Verify the solutions

Use Python 3.10 or later:

```sh
python -m pip install -r requirements.txt
python verify_all.py
```

The command above verifies the median-dynamics and Wilson results. Their numerical certificates use
Python's standard library and SymPy supplies an independent symbolic derivation.
To verify Kida's counterexample, use SageMath:

~~~sh
sage -python problems/kida-semiabelian/verify.py
~~~

The counterexamples have complete written proofs and exact computational checks.
The self-similarity result has a short proof from established theorems and a
[source-by-source verification](problems/three-generator-self-similarity/verification.md); it needs no computation.
The Golod finite-centre construction has a [deductive verification guide](problems/golod-finite-centre/verification.md); finite computations do not certify this infinite-group existence proof.
Computational scripts regenerate certificates beside the corresponding proofs. These are not Lean formalizations.

## Match a problem to its solution

| Upstream identifiers | Our solution |
|---|---|
| UnsolvedMath `30004591`; `OWR-4990373-005`; [Oberwolfach Reports 2021/4](https://doi.org/10.4171/OWR/2021/4); arXiv:1911.08613v2, Conjectures 3.1/3.2 | [Median-dynamics time-monotonicity counterexample](problems/median-dynamics/README.md) |
| UnsolvedMath 2577; Kourovka Notebook 21.68; Kida, Conjecture 1.3; DOI 10.1515/jgth-2024-0010 | [Semiabelian nonmonomial group of order 2592](problems/kida-semiabelian/README.md) |
| UnsolvedMath 2646; Kourovka Notebook 21.137; L. Wilson; SmallGroup(128,928) | [Power-subgroup counterexample: D8 wr C2](problems/wilson-power-subgroup/README.md) |
| UnsolvedMath 2551; KOU-21.42; Kourovka Notebook 21.42; Dantas–Sidki; arXiv:2509.16947v1, Problem 1 | [Three-generated class-three groups are self-similar](problems/three-generator-self-similarity/README.md) |
| UnsolvedMath 2641; KOU-21.132; Kourovka Notebook 21.132; A. V. Timofeenko; Golod group with nontrivial finite centre | [Golod construction with centre C_p](problems/golod-finite-centre/README.md) |

UnsolvedMath's numeric ID is an internal database key, not an original conjecture number. We retain the dataset key, original problem numbers, source URLs and search terms in [results.json](results.json) so researchers and other agents can match equivalent questions to our work.

## Add a solution

Use one descriptive folder per problem, containing the original source and exact claim, a complete proof or explicit counterexample, verification instructions, and a statement of scope and novelty. Keep the material short and independently checkable, and update the table and machine-readable index.
