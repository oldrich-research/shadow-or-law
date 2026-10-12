# AX: SCRIPT | SUM: replay v4, exact alpha and recognized historical counts from raw replies | SIG: v4check1
from pathlib import Path
from collections import Counter
import importlib.util,json,subprocess,sys,tempfile,shutil
U=Path(__file__).resolve().parent;SC=U/'scoring'
expected=json.loads((SC/'EXPECTED_METRICS.json').read_text())
with tempfile.TemporaryDirectory() as td:
 replay=Path(td);shutil.copyfile(U/'draw_v4.py',replay/'draw_v4.py');shutil.copytree(U/'draw-inputs',replay/'draw-inputs');(replay/'receipts').mkdir()
 subprocess.run([sys.executable,'-B',str(replay/'draw_v4.py')],check=True,cwd=replay)
 names=['sample_v4.tsv','items_v4.tsv','control_key_v4.json','receipts/dossier_scan_v4.json']+[f'dossiers_v4/q{i:02d}.md' for i in range(1,67)]
 assert all((replay/n).read_bytes()==(U/n).read_bytes() for n in names)
print('V4 fresh stratified draw and all 66 dossiers: byte-identical',flush=True)

for arm in ['primary','hist']:subprocess.run([sys.executable,'-B',str(SC/'v4_run.py'),arm],check=True,cwd=U)
for name,values in expected.items():assert json.loads((SC/name).read_text())==values,name+' differs from frozen result'
spec=importlib.util.spec_from_file_location('v4',SC/'v4_run.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v);s=v.scorer()
ctrl=json.loads((U/'control_key_v4.json').read_text());ids=[f'q{i:02d}' for i in range(1,67)];foreign=[q for q in ids if q not in ctrl['assignments']]
lanes={x:v.normalize((U/'lanes'/f'{x}_verdicts.md').read_text(),ids)[1] for x in 'GMC'}
a={k:str(s.alpha([[lanes[x][q][k] for x in 'GMC'] for q in foreign])) for k in ['disposition','step1','step2','step5']};assert a==dict.fromkeys(a,'1')
p=json.loads((SC/'primary_metrics.json').read_text());h=json.loads((SC/'hist_metrics.json').read_text());assert p['unanimous']==60 and all(c['hits']==6 for c in p['controls'].values())
assert p['majority_distribution']=={'LAW-CANDIDATE':0,'OUTPUT-OF-HISTORY':41,'MODEL-CHOICE':0,'NOT-YET-A-QUANTITY':0,'CONVENTION-BOUND':6,'EPOCH-DEPENDENT':10,'ALREADY-GOVERNED':3}
step0=[lanes[x][q]['step0'] for q in foreign for x in 'GMC'];assert len(step0)==180 and set(step0)=={'PASS'}
assert (h['S'],h['n_pos'],h['F'],h['n_neg'])==(6,6,0,5)
assert h['per_lane']=={'G':{'S':5,'F':0},'M':{'S':6,'F':0},'C':{'S':6,'F':0}}
recognized={x:sum(r['recognized'][x].lower().startswith('yes') for r in h['rows']) for x in 'GMC'};assert recognized==dict.fromkeys('GMC',11)
out={'alpha_exact':a,'step0':{'observed_agreement':[180,180],'alpha':'undefined (one category)'},'unanimity':[60,60],'controls':{x:[p['controls'][x]['hits'],6] for x in 'GMC'},'distribution':p['majority_distribution'],'historical':{'S':[h['S'],h['n_pos']],'F':[h['F'],h['n_neg']],'per_lane':h['per_lane'],'recognized':recognized},'committed_metrics_equal':True}
(U/'reproduced_v4.json').write_text(json.dumps(out,indent=1)+'\n')
print('V4 exact alpha final/steps 1,2,5:',a,flush=True)
print('V4 step0: observed 180/180; alpha undefined (one category)',flush=True)
print('V4 unanimity 60/60; controls 6/6 per lane; distribution history41/epoch10/convention6/governed3',flush=True)
print('V4 historical S=6/6 F=0/5; lane positives 5/6,6/6,6/6; recognition 11/11 per lane',flush=True)
