"""Offline exact verification of this conditional research witness."""
from pathlib import Path
import json,sys,unittest,hashlib
if sys.flags.optimize:
    raise SystemExit("Run without -O: the exact circuit checks require assertions.")
root=Path(__file__).resolve().parent
for name,digest in json.loads((root/'manifest.json').read_text(encoding='utf-8'))['sha256'].items():
    if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest:
        raise SystemExit("Integrity mismatch: "+name)
tests=unittest.defaultTestLoader.discover(str(root),pattern='test_witness.py')
result=unittest.TextTestRunner(verbosity=2).run(tests)
if not result.wasSuccessful():raise SystemExit(1)
from witness import certificate
actual=certificate()
expected=json.loads((root/'certificate.json').read_text(encoding='utf-8'))
if actual!=expected:raise SystemExit("FAIL: regenerated certificate differs from stored witness")
print("PASS: exact certificate reproduces; kappa = 609/10^12 = 6.09e-10")
print("Conditional on complete motif/tape/precision integration; not a certified multiplication theorem.")
