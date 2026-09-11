# Wilson's power-subgroup question: a counterexample

**The main universal claim is false.** A finite p-group can have its set of
p-th powers form a subgroup that is not powerful.

Source: L. Wilson, [Kourovka Notebook, 21st edition (2026), problem 21.137,
printed p. 181](https://alglog.org/21tkt.pdf).
Dataset: [UnsolvedMath](https://huggingface.co/datasets/ulamai/UnsolvedMath),
record 2646 (an internal dataset key).

Take G = D8 wr C2, where D8 is the dihedral group of order eight.
Then G has order 128 and exponent eight. Its 16 squares form a subgroup
isomorphic to D8 x C2. This subgroup has exponent four and is nonabelian,
so it is not powerful.

The [complete proof](proof.md) identifies every square by a short formula.
The [independent verifier](verify.py) checks all 128 elements using only
Python's standard library. From the repository root:

~~~sh
python problems/wilson-power-subgroup/verify.py
~~~

Expected output:

~~~text
PASS: order 128, exponent 8; 16 squares form a nonabelian subgroup of exponent 4.
~~~

The script regenerates [verification.json](verification.json). It requires
no Sage installation, API access, network, or input certificate.

**Scope:** this completely refutes the main assertion and answers its
explicit 2-group case negatively. The separate odd-prime question remains
unresolved here.

**Novelty:** no earlier resolution found, but priority is unconfirmed.
Two relevant older papers remain unchecked in full; see the
[dated prior-art check](prior-art.md). The group itself is classical.
