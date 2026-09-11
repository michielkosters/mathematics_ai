# Kida's conjecture: a semiabelian group that is not monomial

**Result:** a complete counterexample of order **2592**, with an irreducible
complex character of degree eight that cannot be induced from a linear character.

| Original problem | Link |
|---|---|
| Masanari Kida, *On semiabelian groups*, Conjecture 1.3, Journal of Group Theory 28 (2025), 697–712 | [DOI: 10.1515/jgth-2024-0010](https://doi.org/10.1515/jgth-2024-0010) |
| Kourovka Notebook, 21st edition (2026), problem 21.68 | [Original notebook, printed p. 171](https://alglog.org/21tkt.pdf) |
| UnsolvedMath record 2577 (a dataset key) | [Source Git repository](https://huggingface.co/datasets/ulamai/UnsolvedMath) |

The conjecture says that every finite semiabelian group is monomial.
Our group is built by adjoining abelian normal factors of orders 3, 4, 8,
and 27. That makes semiabelianity immediate. A carefully chosen subgroup
then gives a degree-eight character: if it were monomial, a group with
abelianization C3 would have a subgroup of index two, an impossibility.

- [Complete proof](proof.md): construction and the character argument.
- [Self-contained Sage verifier](verify.py): reconstructs the group and checks it exactly.
- [Recorded certificate](certificate.json): outputs and permutation generators.
- [Prior-art check](prior-art.md): no earlier resolution found; priority unconfirmed.

From the repository root, with SageMath installed:

~~~sh
sage -python problems/kida-semiabelian/verify.py
~~~

Expected final line:

~~~text
PASS: semiabelian construction, order 2592; IsMonomial = false.
~~~

No API access, network connection, or input certificate is needed for the
verification. The script writes a fresh certificate next to itself.
This is a mathematical proof with exact computational corroboration,
not a Lean formalization or a claim of minimal group order.
