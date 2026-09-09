"""Check both counterexamples and the independent symbolic derivation."""
from pathlib import Path
import subprocess
import sys
root=Path(__file__).resolve().parent
for name in ['verify.py','verify_regular.py','closed_form.py']:
    script=root/'problems/median-dynamics'/name
    print('Checking',name,flush=True)
    r=subprocess.run([sys.executable,str(script)],cwd=root,capture_output=True,text=True,timeout=120)
    if r.returncode:
        print(r.stdout)
        print(r.stderr)
        raise SystemExit(r.returncode)
print('PASS: 3 scripts for one conjecture; novelty is not established by these checks.')
