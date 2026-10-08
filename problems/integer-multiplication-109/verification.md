# Verification boundary

The executable is an exact finite witness checker, not a multiplication machine.
It validates the counted scalar DAGs, all relevant local binary residual
witnesses, rational frame inclusions, and every proposed assembly inequality.
The complete disjointness matrix at h=26 is checked, not merely sampled.

The written coordinate-frame and shared-stage arguments establish local
candidate interfaces. The precision growth argument and their integration
with the upstream tape/error/CRT/resampling machinery have not been completed
or independently reviewed. A passing run must not be cited as verification of
those remaining hypotheses or global novelty.

The exact minimum assembly margin is 761619/1250000000000000; it exceeds
609/1000000000000 by 369/1250000000000000.

Arithmetic routines are adapted from the pinned community checker, with the
compact-control packed-overhead constraint replacing its earlier full-window
constraint. The numerical scope is the compact-control/tight-Gaussian assembly.
