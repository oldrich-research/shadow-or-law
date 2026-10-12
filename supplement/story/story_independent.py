# AX: SCRIPT | SUM: independently replay raw story population, selection and exact window partition | SIG: s1
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations_with_replacement,product
import csv,json,math,hashlib,gzip
import numpy as np
import sympy as sy
from scipy.stats import beta
O=Path(__file__).parent; P=O; I=O/'inputs'
AG=6.67430e-11*(9.1093837139e-31)**2/(1.054571817e-34*299792458); w=0.00015/6.67430; lo,hi=AG/10,AG*10
source=I/'gfull_engine_exprs.csv.gz'; expected='7d997675a8579b26a72416bf333c2db07efa9e0c924048f5bac14b449dd6f907'
h=hashlib.sha256()
with gzip.open(source,'rb') as f:
 for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
assert h.hexdigest()==expected
rows=[]; count=0; alpha=None
for ix,r in enumerate(csv.DictReader(gzip.open(source,'rt'))):
 if r['pool']!='cumulative':continue
 v=float(r['value'])
 if not(v>0 and math.isfinite(v)):continue
 count+=1
 if r['expr']=='alpha':alpha=v
 if lo*(1-w)<=v<=hi*(1+w): rows.append(dict(r,ix=ix,v=v,cost=int(r['cost'])))
print('population',count,'local',len(rows),flush=True)
# Lie data primary table; regenerate all grammar combinations, rather than import supplied eligibility sets.
lie=json.loads((P/'receipts/lie_data.json').read_text()); sets={k:set() for k in ['narrow','medium','wide']}
for g in lie:
 d=g['dim']; rho=F(g['rho']); clocks={F(1),F(1,2),F(2),F(1,g['dmin']),F(1,2*g['dmin']),F(1,g['d2']),F(1,g['hv']),F(1,2*g['hv']),F(1,d)}
 metrics={rho,rho/2,F(d,24)}|{rho/F(c) for c in g['c2']}
 sets['narrow'].add((d,2*rho/g['dmin']))
 for r,k in product(metrics,clocks):sets['medium'].add((d,2*r*k))
 for r,k in product(metrics,clocks):
  sets['wide'].add((d,2*r*k))
  if d%2==0:sets['wide'].add((d//2,r*k))
small=[g for g in lie if g['dim']<=60]
for nf in [2,3]:
 for gs in combinations_with_replacement(small,nf):
  d=sum(g['dim'] for g in gs)
  if d>60:continue
  clocks={F(1),F(1,2),F(2),F(1,d)}
  for g in gs: clocks|={F(1,g['dmin']),F(1,2*g['dmin']),F(1,g['d2']),F(1,g['hv']),F(1,2*g['hv'])}
  metrics={sum(F(g['rho']) for g in gs),sum(F(g['rho'])/2 for g in gs),F(d,24)}
  metrics|={sum(F(g['rho'])/c for g,c in zip(gs,cs)) for cs in product(*[[F(x) for x in g['c2']] for g in gs])}
  for r,k in product(metrics,clocks):
   sets['wide'].add((d,2*r*k))
   if d%2==0:sets['wide'].add((d//2,r*k))
x=sy.Symbol('alpha',positive=True); parsed={}; locals={'alpha':x,'e':sy.E,'pi':sy.pi,'exp':sy.exp,'log':sy.log,'me':sy.Symbol('me'),'mp':sy.Symbol('mp'),'mmu':sy.Symbol('mmu'),'mtau':sy.Symbol('mtau')}
forms=0
for r in rows:
 expr=r['expr']; form=None
 if 'alpha' in expr and ('exp' in expr or 'e' in expr):
  f=sy.sympify(expr.replace('^','**'),locals=locals); z=sy.simplify(x*sy.diff(f,x)/f)
  n=sy.simplify(z.subs(x,0)); k=sy.simplify(-sy.diff(z,x))
  if n.is_Integer and k.is_Rational and k>0 and sy.simplify(z-(n-k*x))==0:
   c=sy.simplify(f*x**-n*sy.exp(k*x)); form=(c,int(n),F(str(k))); forms+=1
 flags={}
 for layer,ss in sets.items():
  eligible=bool(form and (form[1],form[2]) in ss and form[0].is_Rational and form[0]>0)
  if eligible:
   c=F(str(form[0])); dl=2*(c.numerator.bit_length()-1)+1+2*(c.denominator.bit_length()-1)+1; eligible=dl<=8
  flags[layer]=eligible
 r['eligibility']=flags
values=np.array([r['v'] for r in rows]); costs=np.array([r['cost'] for r in rows]); ix=np.array([r['ix'] for r in rows]); flags={k:np.array([r['eligibility'][k] for r in rows]) for k in sets}
tg=np.array([float(r['sham_value']) for r in csv.DictReader((I/'sham_targets.csv').open())]); hits=0; selected={k:0 for k in sets}
for t in tg:
 ids=np.flatnonzero(np.abs(values-t)/t<=w)
 if not len(ids):continue
 hits+=1; chosen=min(ids,key=lambda j:(costs[j],abs(values[j]-t)/t,ix[j]))
 for k in sets:selected[k]+=int(flags[k][chosen])
print('selected',hits,selected,flush=True)
left=np.maximum(lo,values/(1+w)); right=np.minimum(hi,values/(1-w)); endpoints={lo,hi}|set(left)|set(right)
# At fixed active minimum cost, residual order changes only at pairwise arithmetic midpoints.
order=np.argsort(left)
for z,j in enumerate(order):
 for k in order[z+1:]:
  if left[k]>right[j]:break
  if costs[j]==costs[k]:
   mid=(values[j]+values[k])/2
   if max(left[j],left[k])<mid<min(right[j],right[k]):endpoints.add(mid)
pts=sorted(endpoints); total=0.; selected_measure={k:0. for k in sets}
for a,b in zip(pts,pts[1:]):
 t=(a+b)/2; ids=np.flatnonzero((left<t)&(t<right))
 if not len(ids):continue
 weight=math.log(b/a); total+=weight; chosen=min(ids,key=lambda j:(costs[j],abs(values[j]-t),ix[j]))
 for k in sets:
  if flags[k][chosen]:selected_measure[k]+=weight
result={'method':'raw CSV local clipping, symbolic log derivative, grammar regeneration from Lie data; independent breakpoint integration','population':count,'local_rows':len(rows),'alpha_population':alpha,'AG':AG,'window':w,'targets':len(tg),'hits':hits,'selected_counts':selected,'R_any_exact_float':total/math.log(100),'R_sel_exact_float':{k:v/total for k,v in selected_measure.items()},'CP95_medium':[beta.ppf(.025,selected['medium'],hits-selected['medium']+1),beta.ppf(.975,selected['medium']+1,hits-selected['medium'])],'n21_slopes':{k:sorted(str(s) for n,s in ss if n==21) for k,ss in sets.items()},'local_story_form_rows':forms,'primary_hash':expected,'partition_segments':len(pts)-1}
(O/'story_replay.json').write_text(json.dumps(result,indent=2)+'\n');print(result,flush=True)
