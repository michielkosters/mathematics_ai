# AI-assisted mathematics

We use AI to find proofs and counterexamples to unsolved mathematical conjectures. Our aim is to solve as many worthwhile problems as possible with efficient reasoning, modest computation, and results that other mathematicians can easily check.

We screen problems for precise statements and feasible approaches, check the existing literature, and then look for short arguments or explicit constructions. We use Python, SageMath, or Lean when they help verify a result. Each solution comes with its source, proof, and reproducible verification where applicable.

## Where the problems come from

Our starting collection is [Ulam AI's UnsolvedMath](https://www.unsolvedmath.com/), available as a [Git repository on Hugging Face](https://huggingface.co/datasets/ulamai/UnsolvedMath/tree/main), with records in [problems.json](https://huggingface.co/datasets/ulamai/UnsolvedMath/blob/main/problems.json). It collects questions from research papers, Oberwolfach Reports, Open Problem Garden, and other mathematical sources. We return to the original sources to check the statements and their status before attempting a solution.

Our imported snapshot is version 1.6.0, revision `b9437975f3c873f635a13c48f8b022f5ba80898a`. Credit for the dataset belongs to Ulam AI / UnsolvedMath contributors, under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); original mathematical sources retain their own attribution and terms. The problem data came from Hugging Face, not a GitHub mirror. Our work is collected at [michielkosters/mathematics_ai on GitHub](https://github.com/michielkosters/mathematics_ai).

## Solutions

This table grows as we complete and verify solutions. It includes complete resolutions of the stated conjectures, rather than partial progress, transcription corrections, or reproductions of published solutions. Novelty assessments are separate from mathematical verification.

| Problem | Original source | Result | Proof and verification |
|---|---|---|---|
| Time monotonicity in majority dynamics / the median process | Amir, Baldasso and Beilin, *Majority dynamics and the median process: connections, convergence and some new conjectures*, [arXiv:1911.08613v2, Conjectures 3.1 and 3.2](https://arxiv.org/html/1911.08613v2#S3) | Complete counterexample, with a cubic-graph strengthening. Novelty unestablished. | [Solution folder](problems/median-dynamics/README.md) |

The two conjecture numbers above are equivalent formulations of the same time-monotonicity claim. The result does not address the paper's separate convexity or convergence questions.

## Verify the solutions

Use Python 3.10 or later:

```sh
python -m pip install -r requirements.txt
python verify_all.py
```

The current counterexample certificates use only Python's standard library; SymPy supplies an independent symbolic derivation. Scripts regenerate small certificate files beside the proofs. The current collection contains written proofs and exact Python checks, not Lean formalizations.

## Match a problem to its solution

| Upstream identifiers | Our solution |
|---|---|
| UnsolvedMath `30004591`; `OWR-4990373-005`; [Oberwolfach Reports 2021/4](https://doi.org/10.4171/OWR/2021/4); arXiv:1911.08613v2, Conjectures 3.1/3.2 | [Median-dynamics time-monotonicity counterexample](problems/median-dynamics/README.md) |

UnsolvedMath's numeric ID is an internal database key, not an original conjecture number. We retain the dataset key, original problem numbers, source URLs and search terms in [results.json](results.json) so researchers and other agents can match equivalent questions to our work.

## Add a solution

Use one descriptive folder per problem, containing the original source and exact claim, a complete proof or explicit counterexample, verification instructions, and a statement of scope and novelty. Keep the material short and independently checkable, and update the table and machine-readable index.
