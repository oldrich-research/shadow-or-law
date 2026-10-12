# AX: DOMAIN | SUM: event sweep exact selected-expression log measure | SIG: u1a1
import heapq,collections
import numpy as np

def selected_measure(p,lo,hi,w):
 v=p['values'];use=(v>=lo*(1-w))&(v<=hi*(1+w));v=v[use];c=p['costs'][use];rows=p['rows'][use];m=p['members'][use]
 if not len(v):return np.zeros(6)
 order=np.lexsort((rows,c,v));v,c,m=v[order],c[order],m[order];keep=np.r_[True,v[1:]!=v[:-1]];v,c,m=v[keep],c[keep],m[keep]
 left=np.maximum(lo,v/(1+w));right=np.minimum(hi,v/(1-w));events=[]
 for i,(l,r) in enumerate(zip(left,right)):
  if l<r:events.extend([(l,1,i),(r,-1,i)])
 events.sort();active=collections.defaultdict(set);heap=[];total=np.zeros(6);j=0
 while j<len(events):
  a=events[j][0]
  while j<len(events) and events[j][0]==a:
   _,kind,i=events[j];cost=int(c[i])
   if kind==1:
    if not active[cost]:heapq.heappush(heap,cost)
    active[cost].add(i)
   else:active[cost].remove(i)
   j+=1
  if j==len(events):break
  b=events[j][0]
  while heap and not active[heap[0]]:heapq.heappop(heap)
  if not heap:continue
  ix=np.array(sorted(active[heap[0]]));vv=v[ix];mid=(vv[:-1]+vv[1:])/2
  start=np.searchsorted(mid,a,side='right');end=np.searchsorted(mid,b,side='left');bounds=np.r_[a,mid[start:end],b]
  for z,(l,r) in enumerate(zip(bounds[:-1],bounds[1:])):total+=m[ix[start+z]]*(np.log(r)-np.log(l))
 return total/(np.log(hi)-np.log(lo))
