"""Run all ordinary-Python checks; the Kida check requires Sage separately."""
from pathlib import Path
import subprocess
import sys
root=Path(__file__).resolve().parent
scripts=[root/'problems/median-dynamics'/name
         for name in ['verify.py','verify_regular.py','closed_form.py']]
scripts.append(root/'problems/wilson-power-subgroup/verify.py')
for script in scripts:
    name=str(script.relative_to(root))
    print('Checking',name,flush=True)
    r=subprocess.run([sys.executable,str(script)],cwd=root,capture_output=True,text=True,timeout=120)
    if r.returncode:
        print(r.stdout)
        print(r.stderr)
        raise SystemExit(r.returncode)
print('PASS: 4 Python scripts for the median-dynamics and Wilson results.')
print('Kida verification requires Sage: sage -python problems/kida-semiabelian/verify.py')
print('These checks do not establish novelty.')

print('Self-similarity: deductive verification in problems/three-generator-self-similarity/verification.md (not checked by this script).')

print('Golod finite centre: deductive verification in problems/golod-finite-centre/verification.md (not checked by this script).')
