# AX: DOMAIN | SUM: frozen exact story-layer sets and witnesses | SIG: u1a1
from lie import H,Q
import itertools,json,subprocess

def clocks(a):return {Q(1),Q(1,2),Q(2),Q(1,a['dmin']),Q(1,2*a['dmin']),Q(1,a['d2']),Q(1,a['hv']),Q(1,2*a['hv']),Q(1,a['dim'])}
def metrics(a):
 r=Q(a['rho']);return {'long2':r,'long1':r/2,'Killing':Q(a['dim'],24)}|{f'C2=1({c})':r/Q(c) for c in a['c2']}
def build():
 data=json.loads((H/'receipts/lie_data.json').read_text());out={z:{} for z in ['narrow','medium','wide']}
 def add(layer,n,k,w):
  if n.denominator==1 and 0<n<=300:out[layer].setdefault(f'{n}:{k}',w)
 for a in data:
  n=Q(a['dim']);r=Q(a['rho']);w=dict(g=a['name'],clock=str(Q(1,a['dmin'])),metric='long2',mapping='Z^-2')
  add('narrow',n,2*r/a['dmin'],w)
  for m,rho in metrics(a).items():
   for c in sorted(clocks(a)):
    w=dict(g=a['name'],clock=str(c),metric=m,mapping='Z^-2')
    add('medium',n,2*rho*c,w);add('wide',n,2*rho*c,w)
    add('wide',n/2,rho*c,w|{'mapping':'Z^-1'})
 small=[a for a in data if a['dim']<=57]
 for nf in (2,3):
  for aa in itertools.combinations_with_replacement(small,nf):
   n=Q(sum(a['dim'] for a in aa))
   if n>60:continue
   cc={Q(1),Q(1,2),Q(2),1/n}
   for a in aa:cc|={Q(1,a['dmin']),Q(1,2*a['dmin']),Q(1,a['d2']),Q(1,a['hv']),Q(1,2*a['hv'])}
   rr={'long2':sum(Q(a['rho']) for a in aa),'long1':sum(Q(a['rho'])/2 for a in aa),'Killing':n/24}
   for c2 in itertools.product(*(a['c2'] for a in aa)):
    rr['C2=1('+','.join(c2)+')']=sum(Q(a['rho'])/Q(c) for a,c in zip(aa,c2))
   for m,rho in rr.items():
    for c in sorted(cc):
     w=dict(g='+'.join(a['name'] for a in aa),clock=str(c),metric=m,mapping='Z^-2')
     add('wide',n,2*rho*c,w);add('wide',n/2,rho*c,w|{'mapping':'Z^-1'})
 (H/'receipts/full_story_sets.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 out={layer:{key:w for key,w in ss.items() if int(key.split(':')[0])<=40} for layer,ss in out.items()}
 (H/'receipts/story_sets.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 table=['# U1a mechanical story calibration','','## n = 21 passing k and one exact witness','Each cell entry: k ⇒ algebra; clock; metric; mapping. Entries grouped only for line budget.','| layer | exact k and witness |','|---|---|']
 for layer,ss in out.items():
  entries=[]
  for key,w in sorted(ss.items(),key=lambda z:Q(z[0].split(':')[1])):
   n,k=key.split(':')
   if n=='21':entries.append(f"{k} ⇒ {w['g']}; {w['clock']}; {w['metric']}; {w['mapping']}")
  for i in range(0,len(entries),10):table.append('| '+layer+' | '+' <br> '.join(entries[i:i+10])+' |')
 (H/'RESULT.md').write_text('\n'.join(table)+'\n')
 stamp=subprocess.check_output(['date','-u','+%Y-%m-%dT%H:%M:%SZ'],text=True).strip()
 with (H/'LOG.md').open('a') as f:f.write(f'{stamp} S2 PASS: exact layers with witnesses; counts '+str({k:len(v) for k,v in out.items()})+'; n=21 full table written.\n')
 print('S2', {k:len(v) for k,v in out.items()})
if __name__=='__main__':build()
