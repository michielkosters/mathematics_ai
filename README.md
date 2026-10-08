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
| Conciseness of parameter-free first-order group formulas | M. Petschick, [Kourovka Notebook 21.106](https://alglog.org/21tkt.pdf); Conte–Petschick, [*Conciseness of first-order formulae*, Question 1](https://doi.org/10.1007/s00605-025-02127-5) | Complete counterexample in the integer Heisenberg group: two formula values generate an infinite cyclic subgroup. Novelty unconfirmed. | [Simple proof and Sage verification](problems/heisenberg-nonconcise-formula/README.md) |
| Permanents of doubly stochastic matrices with bounded Frobenius norm | Alexander Barvinok and Alex Samorodnitsky, [OWR 44/2008, Problem 9, pp. 2549–2550](https://ems.press/content/serial-article-files/46191?nt=1#page=73); [DOI](https://doi.org/10.4171/OWR/2008/44) | Complete affirmative answer: per(A) ≤ exp(−n)(en)^(64γ) when sum a_ij² ≤ γ. Novelty unconfirmed. | [Complete entropy proof and verification](problems/permanent-bounded-frobenius/README.md) |
| Shinohara’s determinant and signature question | Y. Shinohara, [Ohtsuki Problem 12.21](https://msp.org/gtm/2002/04/gtm-2002-04-024s.pdf#page=168); Stoimenow, [Question 5.1](https://doi.org/10.4064/aa129-4-6) | Complete affirmative deduction: every n = 4k+1 > 1 occurs for a genus-two knot of signature 4. Uses classical lattice and Seifert realization theorems; novelty unconfirmed, independent review pending. | [Proof and exact Sage verification](problems/shinohara-determinant-signature/README.md) |
| Reverse Wasserstein bound for the spherical Radon transform | Benjamin K. Stephens, [*Measuring the Geodesic Radon Transform with Mass Transport*, OWR 31/2008, p. 1763](https://ems.press/content/serial-article-files/46174#page=57); [DOI](https://doi.org/10.4171/OWR/2008/31) | Complete negative answer; failure persists for smooth positive even densities on S^2 for every finite p >= 1. Classical ingredients; novelty unconfirmed, independent review pending. | [Proof and exact Sage checks](problems/spherical-radon-reverse-wasserstein/README.md) |

The two conjecture numbers for median dynamics are equivalent formulations of the same time-monotonicity claim. The result does not address the paper's separate convexity or convergence questions.

## Conditional research witnesses

These records contain reproducible finite checks and proposed proofs with
explicit outstanding hypotheses. They are separate from the completed solutions.

| Problem | Witness | Scope | Proof and verification |
|---|---|---|---|
| OpenAI math #109: integer multiplication | Proposed kappa = 609/10^12 = 6.09e-10 | Conditional; full motif-to-tape transfer and precision integration unverified. Novelty unestablished. | [Witness and proof](problems/integer-multiplication-109/README.md); `python problems/integer-multiplication-109/verify.py` |

## Verify the solutions

Use Python 3.10 or later:

```sh
python -m pip install -r requirements.txt
python verify_all.py
```

The command above verifies the median-dynamics and Wilson results and runs supporting checks for the permanent bound. Their numerical certificates use
Python's standard library and SymPy supplies an independent symbolic derivation.
To verify Kida's counterexample, use SageMath:

~~~sh
sage -python problems/kida-semiabelian/verify.py
~~~

The counterexamples have complete written proofs and exact computational checks.
The self-similarity result has a short proof from established theorems and a
[source-by-source verification](problems/three-generator-self-similarity/verification.md); it needs no computation.
The Golod finite-centre construction has a [deductive verification guide](problems/golod-finite-centre/verification.md); finite computations do not certify this infinite-group existence proof.
For the Heisenberg formula, run `sage -python problems/heisenberg-nonconcise-formula/verify_sage.py` for supporting symbolic checks; the written proof establishes the infinite-group conclusion.
For the permanent bound, `python problems/permanent-bounded-frobenius/verify.py` enumerates exact rational examples and checks logarithmic inequalities at 60-digit precision. The written proof establishes the universal statement; the numerical checks do not.
For Shinohara’s question, run `sage -python problems/shinohara-determinant-signature/verify_sage.py` for exact Gauss-sum and Seifert-matrix checks. The written proof supplies the universal existence argument.
For the spherical Radon transform, run `sage -python problems/spherical-radon-reverse-wasserstein/verify_sage.py` for exact polynomial identity checks. The written transport argument proves the failure of a uniform reverse bound.
Computational scripts regenerate certificates beside the corresponding proofs. These are not Lean formalizations.

## Match a problem to its solution

| Upstream identifiers | Our solution |
|---|---|
| UnsolvedMath `30004591`; `OWR-4990373-005`; [Oberwolfach Reports 2021/4](https://doi.org/10.4171/OWR/2021/4); arXiv:1911.08613v2, Conjectures 3.1/3.2 | [Median-dynamics time-monotonicity counterexample](problems/median-dynamics/README.md) |
| UnsolvedMath 2577; Kourovka Notebook 21.68; Kida, Conjecture 1.3; DOI 10.1515/jgth-2024-0010 | [Semiabelian nonmonomial group of order 2592](problems/kida-semiabelian/README.md) |
| UnsolvedMath 2646; Kourovka Notebook 21.137; L. Wilson; SmallGroup(128,928) | [Power-subgroup counterexample: D8 wr C2](problems/wilson-power-subgroup/README.md) |
| UnsolvedMath 2551; KOU-21.42; Kourovka Notebook 21.42; Dantas–Sidki; arXiv:2509.16947v1, Problem 1 | [Three-generated class-three groups are self-similar](problems/three-generator-self-similarity/README.md) |
| UnsolvedMath 2641; KOU-21.132; Kourovka Notebook 21.132; A. V. Timofeenko; Golod group with nontrivial finite centre | [Golod construction with centre C_p](problems/golod-finite-centre/README.md) |
| UnsolvedMath 2615; KOU-21.106; Kourovka Notebook 21.106; Conte–Petschick Question 1; DOI 10.1007/s00605-025-02127-5; arXiv:2505.01411 | [Non-concise formula in UT3(Z)](problems/heisenberg-nonconcise-formula/README.md) |
| UnsolvedMath 30001073; OWR 44/2008 Problem 9; DOI 10.4171/OWR/2008/44; Barvinok–Samorodnitsky; permanent with bounded Frobenius norm | [Polynomial-factor permanent bound](problems/permanent-bounded-frobenius/README.md) |
| UnsolvedMath 10400226; AMR-103-0226; Shinohara; Ohtsuki Problem 12.21; Stoimenow Question 5.1; DOI 10.4064/aa129-4-6; determinant 4k+1 and signature four | [Genus-two knots with prescribed determinant](problems/shinohara-determinant-signature/README.md) |
| UnsolvedMath 30000999; OWR-2042-008; Benjamin K. Stephens; OWR 31/2008 p. 1763; DOI 10.4171/OWR/2008/31; inverse Funk transform Wasserstein stability | [No uniform reverse Wasserstein bound](problems/spherical-radon-reverse-wasserstein/README.md) |

UnsolvedMath's numeric ID is an internal database key, not an original conjecture number. We retain the dataset key, original problem numbers, source URLs and search terms in [results.json](results.json) so researchers and other agents can match equivalent questions to our work.

## Add a solution

Use one descriptive folder per problem, containing the original source and exact claim, a complete proof or explicit counterexample, verification instructions, and a statement of scope and novelty. Keep the material short and independently checkable, and update the table and machine-readable index.
