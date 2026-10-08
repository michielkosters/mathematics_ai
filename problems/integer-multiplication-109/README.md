# Integer multiplication #109: conditional witness

The proposed witness is **kappa = 609/10^12 = 6.09e-10**, giving the conditional
bound `T(n)=O(n(log n)^(1-kappa))` in the upstream fixed multitape model.
It is about 7.34 times the supplied community witness. It is a conditional
research record, not a verified new world record or a complete proof of that
multiplication bound. The full motif-to-tape transfer and precision guard
integration remain unverified. Independent review and global novelty clearance
are also outstanding.

* [Proof and scope](proof.md)
* [Center identity](center.md)
* [Shared-stage frame joins](stage-joins.md)
* [Exact witness](certificate.json)
* [Verification](verification.md)
* [Sources and attribution](SOURCES.md)

Run from any working directory, with Python 3.10 or later:

```sh
python /path/to/this/folder/verify.py
```

No dependencies, network access, original workspace, or downloaded manuscripts
are required. The verifier checks all h=26 disjoint coefficients, h=50 bit
coefficients and frame nesting, exact rational logarithm bounds, all assembly
slacks, the stored certificate, local dirty-scratch restoration, and source
integrity. These checks do not certify the full upstream multiplication theorem.
