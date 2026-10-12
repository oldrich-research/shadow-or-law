# AX: SCRIPT | SUM: run all portable PUB2 numeric checks | SIG: pub2-repro3
"""python -B supplement/reproduce.py  (any working directory; uses only the files of this release)
Recomputes from these files the v3 and round-2 reliability coefficients, the v4 primary and recognized historical arm, the census agreement and dispositions,
the arithmetic-null counts and tails, the story rates, the lineup ranks and the route-index counts printed in the paper:
  reliability/scoring/v3_run.py r2       round-2 coefficient (checksum-pinned scorer must reproduce its committed metrics)
  reliability/scoring/v3_run.py primary  v3 coefficients from the raw lane outputs
  reliability/scoring/v3_run.py census   census agreement from the census-arm lane outputs
  arithmetic/rational_exact.py           arithmetic-null counts and exact tails
  story/story_independent.py             story rates from the raw search population and the story grammar
  check_receipts.py                      census dispositions, lineup ranks and route-index counts recounted from their
                                         files; every recomputed number compared with the value printed in the paper
No network requests, no model sessions."""
from pathlib import Path
import subprocess,sys,json
S=Path(__file__).resolve().parent
commands=[('reliability/scoring/v3_run.py',['r2']),('reliability/scoring/v3_run.py',['primary']),('reliability/scoring/v3_run.py',['census']),('arithmetic/rational_exact.py',[]),('story/story_independent.py',[]),('check_receipts.py',[]),('reliability-v4/check_printed.py',[])]
for script,args in commands:
 print('RUN',script,*args,flush=True)
 subprocess.run([sys.executable,'-B',str(S/script),*args],cwd=S,check=True)
print('ALL NUMERIC CHECKS PASS: v3 and round-2 reliability coefficients, census agreement and dispositions, arithmetic-null counts and tails, story rates, lineup ranks, route-index counts; v4 exact alpha, controls, unanimity, distribution and recognized historical S/F',flush=True)
