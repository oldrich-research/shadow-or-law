# AX: SCRIPT | SUM: exact circular Farey count and endpoint null integration | SIG: r1
from fractions import Fraction as F
from math import gcd, floor, ceil, pi
from collections import defaultdict
from pathlib import Path
import json, datetime
OUT=Path(__file__).parent
ROWS=[('theta','1.0411','0.0003'),('ns','0.9649','0.0042'),('H0t0','0.95103824655253','0.00723111905553476'),('Om','0.315','0.007')]
def population(Q): return [F(p,q) for q in range(1,Q+1) for p in range(q) if gcd(p,q)==1]
def inside(p,c,s):
 d=abs(p-c); return min(d,1-d)<=s
def integrate(ps,s):
 e=defaultdict(int)
 for p in ps:
  e[(p-s)%1]+=1; e[(p+s)%1]-=1
 ks=sorted(set(e)|{F(0),F(1)}); hist=defaultdict(F)
 c=sum(inside(p,(ks[0]+ks[1])/2,s) for p in ps)
 for a,b in zip(ks,ks[1:]):
  hist[c]+=b-a
  c+=e[b]
 assert sum(hist.values())==1
 assert sum(k*v for k,v in hist.items())==2*s*len(ps)
 return hist
def brute(ps,s):
 ks=sorted({F(0),F(1)}|{(p+d)%1 for p in ps for d in [-s,s]}); h=defaultdict(F)
 for a,b in zip(ks,ks[1:]): h[sum(inside(p,(a+b)/2,s) for p in ps)]+=b-a
 return h
checks=[]
for Q in [1,2,5,12]:
 for s in [F(3,10000),F(42,10000),F(7,1000),F(1,3)]:
  assert integrate(population(Q),s)==brute(population(Q),s); checks.append([Q,str(s),'PASS'])
(OUT/'rational_lowQ.json').write_text(json.dumps(checks,indent=2)+'\n')
ps=population(500); result=[]
for name,x,s in ROWS:
 x=F(x); s=F(s)
 original=[]
 for q in range(1,501):
  for p in range(ceil((x-s)*q),floor((x+s)*q)+1):
   if gcd(p,q)==1: original.append((p,q))
 circular=sum(inside(p,x%1,s) for p in ps); assert circular==len(original)
 h=integrate(ps,s); tail=sum(v for k,v in h.items() if k>=circular)
 r={'name':name,'x':str(x),'sigma':str(s),'Q':500,'population':len(ps),'observed_gcd':len(original),'observed_circle':circular,'tail_exact':str(tail),'tail_decimal':float(tail),'mean_exact':str(2*s*len(ps)),'mean_decimal':float(2*s*len(ps)),'farey_approx':float(6*s*500**2)/pi**2,'count_range':[min(h),max(h)],'histogram':{str(k):str(v) for k,v in sorted(h.items())},'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 (OUT/f'rational_{name}.json').write_text(json.dumps(r,indent=2)+'\n'); result.append(r)
 print(name,circular,float(tail),flush=True)
(OUT/'rational_summary.json').write_text(json.dumps(result,indent=2)+'\n')
