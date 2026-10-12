# AX: DOMAIN | SUM: exact Cartan roots and Weyl dimensions for compact simple algebras | SIG: u1a1
from fractions import Fraction as Q
from pathlib import Path
import json,subprocess
import sympy as s
H=Path(__file__).resolve().parent

def cartan(t,r):
 C=s.zeros(r)
 for i in range(r):C[i,i]=2
 edges=[(i,i+1) for i in range(r-1)] if t!='E' else [(i,i+1) for i in range(r-2)]+[(2,r-1)]
 for i,j in edges:C[i,j]=C[j,i]=-1
 if t=='B':C[r-1,r-2]=-2
 if t=='C':C[r-2,r-1]=-2
 if t=='D':
  C[r-2,r-1]=C[r-1,r-2]=0;C[r-3,r-1]=C[r-1,r-3]=-1
 if t=='F':C[2,1]=-2
 if t=='G':C[1,0]=-3
 return C

def datum(t,r):
 C=cartan(t,r);d=[None]*r;d[0]=Q(1)
 while None in d:
  for i in range(r):
   for j in range(r):
    if d[i] is not None and C[i,j] and i!=j:d[j]=d[i]*Q(int(C[i,j]),int(C[j,i]))
 d=[x/max(d) for x in d];D=s.diag(*d);W=D*(D*C).inv()*D
 roots={tuple(int(i==j) for i in range(r)) for j in range(r)};todo=list(roots)
 while todo:
  v=todo.pop()
  for i in range(r):
   z=list(v);z[i]-=sum(int(C[i,j])*v[j] for j in range(r));z=tuple(z)
   if z not in roots:roots.add(z);todo.append(z)
 pos=[v for v in roots if min(v)>=0];dim=r+2*len(pos);one=s.ones(r,1);rho=(one.T*W*one)[0]
 cor=[tuple(d[i]*v[i] for i in range(r)) for v in pos]
 def wd(a):
  out=Q(1)
  for v in cor:out*=sum((a[i]+1)*v[i] for i in range(r))/sum(v)
  assert out.denominator==1
  return int(out)
 def cas(a):
  av=s.Matrix(a);return (av.T*W*(av+2*one))[0]
 unit=[tuple(int(i==j) for i in range(r)) for j in range(r)]
 ceiling=sorted(set(wd(a) for a in unit+[tuple(2*x for x in a) for a in unit]))[1]
 seen=set();todo=[(0,)*r];found=[]
 while todo:
  a=todo.pop()
  if a in seen:continue
  seen.add(a);v=wd(a)
  if v>ceiling:continue
  if v>1:found.append((v,a))
  for i in range(r):b=list(a);b[i]+=1;todo.append(tuple(b))
 dims=sorted({v for v,a in found});dm,d2=dims[:2];ir=[a for v,a in found if v==dm]
 long=[v for v in pos if (s.Matrix(v).T*(D*C)*s.Matrix(v))[0]==2]
 theta=max(long,key=sum);hv=1+sum(d[i]*theta[i] for i in range(r));assert hv.denominator==1
 return dict(name=f'{t}{r}',rank=r,dim=dim,rho=str(rho),hv=int(hv),dmin=dm,d2=d2,c2=sorted({str(cas(a)) for a in ir}),min_labels=ir,positive_roots=len(pos))

def build():
 specs=[('A',r) for r in range(1,17)]+[('B',r) for r in range(2,13)]+[('C',r) for r in range(3,13)]+[('D',r) for r in range(4,13)]+[('G',2),('F',4),('E',6),('E',7),('E',8)]
 data=[datum(t,r) for t,r in specs];assert all(x['dim']<=300 for x in data)
 (H/'receipts').mkdir(exist_ok=True);(H/'receipts/lie_data.json').write_text(json.dumps(data,separators=(',',':'))+'\n')
 return data
if __name__=='__main__':build()
