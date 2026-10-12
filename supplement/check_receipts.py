# AX: SCRIPT | SUM: recount census, lineup and route index from their files; compare every recomputed number with the paper | SIG: pub2-rc2
"""Last step of reproduce.py. Recounts the census dispositions, the blind-lineup ranks and the scoped route index from
their files, reads the outputs the earlier steps have just recomputed, asserts each against the value printed in the
paper, and writes receipt_checks.json."""
from pathlib import Path
from collections import Counter
import csv,json,re
S=Path(__file__).resolve().parent
def read(n):return json.loads((S/n).read_text())
def tsv(n):return list(csv.DictReader((S/n).open(),delimiter='\t'))
# Census dispositions: adjudicated table, the shipped census CSV, historical exposition counts, adjudication outcomes.
rows=tsv('census/CENSUS_TABLE_74.tsv');print('census fields',list(rows[0]),flush=True)
assert len(rows)==74
counts_c=Counter(x['adjudicated'] for x in rows)
assert counts_c=={'OUTPUT-OF-HISTORY':40,'ALREADY-GOVERNED':11,'EPOCH-DEPENDENT':10,'NOT-YET-A-QUANTITY':8,'MODEL-CHOICE':2,'CONVENTION-BOUND':2,'LAW-CANDIDATE':1}, counts_c
hist=list(csv.DictReader((S/'census/historical_census.csv').open()));by={x['id']:x for x in rows}
assert sorted(h['id'] for h in hist)==sorted(by)
assert all((h['lane_1'],h['lane_2'],h['lane_3'],h['v3_adjudication'])==(by[h['id']]['L-G'],by[h['id']]['L-M'],by[h['id']]['L-C'],by[h['id']]['adjudicated']) for h in hist)
counts_h=Counter(h['historical_disposition'] for h in hist)
assert counts_h=={'History':44,'Governed':6,'Epoch':2,'Unmapped':3,'Model':3,'Convention':3,'Retained':13}, counts_h
adjud=Counter(x['verdict'] for x in tsv('census/census_adjudication.tsv'))
assert adjud=={'CENSUS-FAULTED':21,'AMBIGUOUS':4,'DOSSIER-DEFECT':1}, adjud
projection=sum(counts_c[k] for k in ('OUTPUT-OF-HISTORY','EPOCH-DEPENDENT','CONVENTION-BOUND','MODEL-CHOICE'))
assert (74-counts_c['LAW-CANDIDATE'],projection,74-counts_h['Retained'])==(73,54,61)
# Census agreement (v3_run.py census).
c=read('reliability/scoring/census_metrics.json');h,a=c['headline_nonleak'],c['all_rows']
assert h['alpha_exact']=='4467/6847' and h['n']==47 and round(h['alpha_disposition'],2)==0.65 and round(a['alpha_disposition'],2)==0.68
assert [round(h['alpha_steps'][s],2) for s in ('step0','step1','step2','step5')]==[0.67,0.67,0.68,0.53]
assert round(h['majority_vs_reference']*47)==28 and round(a['majority_vs_reference']*74)==48 and len(h['majority_none'])==4
# v3 coefficients (v3_run.py primary) and round-2 coefficient (v3_run.py r2 reproduced the committed metrics file).
m=read('reliability/scoring/primary_metrics.json');assert m['alpha_disposition_exact']=='189/1979' and m['verdict']=='FAIL'
assert round(m['alpha_disposition'],4)==0.0955 and round(m['alpha_steps']['step2'],4)==0.0213 and round(m['alpha_pairwise']['L-C|L-G'],4)==0.9270
assert all(v['hits']==6 for v in m['controls'].values()) and round(m['validity_accuracy']*60)==59
assert (round(m['lane_vs_reference']['L-C']*60),round(m['lane_vs_reference']['L-G']*60))==(60,59)
r2=read('reliability/historical/i4i_metrics.json')
assert r2['alpha_disposition_exact']=='8781/22564' and round(r2['alpha_disposition'],3)==0.389 and round(r2['validity_accuracy']*60)==31
assert [round(r2['alpha_steps'][s],3) for s in ('step1','step2','step5')]==[0.492,0.518,0.469]
# Lineup ranks, recomputed from the judge scores.
st=read('story/judge/STATS.json');assert st['decoys_mean_ge_flagship']==39 and st['retest_exact']==6
assert all(x['flagship_rank_mid']==20.5 and x['n_items']==40 for x in st['per_seat'].values())
judge=[json.loads(l) for l in (S/'story/judge/judge_scores.jsonl').read_text().splitlines() if l.startswith('{')]
jmap=read('story/judge/JMAP.json'); scores={x['id']:x['score'] for x in judge if 'id' in x}
assert len(scores)==126
lineup={}
for seat in 'GMC':
 ids=[q for q,v in jmap.items() if v['seat']==seat and not v.get('duplicate_of')]
 # Primary 40 items identified by the first three lineup orders; retests carry duplicate_of.
 ids=ids[:40]; fs=[q for q in ids if jmap[q]['is_flagship']]
 assert len(fs)==1 and len(ids)==40
 score=scores[fs[0]]; rank=1+sum(scores[q]>score for q in ids)+(sum(scores[q]==score for q in ids)-1)/2
 assert rank==20.5 and score==st['per_seat'][seat]['flagship_score']
 lineup[seat]={'flagship_score':score,'mid_rank':rank,'decoys_tied':sum(scores[q]==score for q in ids)-1}
assert {k:v['flagship_score'] for k,v in lineup.items()}=={'G':5,'M':0,'C':6} and all(v['decoys_tied']==39 for v in lineup.values())
assert len(st['retest'])==6 and all(scores[x['dup']]==scores[x['orig']] for x in st['retest'])
# Route-index counts, recounted from the index table.
counts=read('routes/counts.json')
idx=[[x.strip() for x in l.strip().strip('|').split('|')] for l in (S/'routes/SCOPED_ROUTE_INDEX.md').read_text().splitlines() if re.match(r'^\|\s*\d+\s*\|',l)]
assert all(len(x)==4 for x in idx) and [int(x[0]) for x in idx]==list(range(1,len(idx)+1))
audits=[x for x in idx if 'circularity audit' in x[2]];routes=[x for x in idx if x not in audits];dates=sorted(x[1] for x in routes)
recount={'index':len(idx),'audits':len(audits),'routes':len(routes),'empty':sum(not x[3] for x in routes),'nonempty':sum(bool(x[3]) for x in routes),
 'raw_leader':sum(x[3]=='raw leader finding' for x in routes),'guardrail':sum(x[3]=='selector guardrail' for x in routes),'dates':[dates[0],dates[-1]]}
assert recount==counts and (recount['index'],recount['audits'],recount['routes'],recount['empty'],recount['nonempty'],recount['raw_leader'],recount['guardrail'])==(180,2,178,15,163,13,9), recount
assert (min(x[1] for x in idx),max(x[1] for x in idx))==('2026-04-27','2026-06-25') and recount['dates']==['2026-06-23','2026-06-25']
# Arithmetic-null counts and tails (rational_exact.py).
for name,count,farey,mean,tail in [('theta',45,45.59,45.6696,.755639),('ns',637,638.32,639.3744,.802831),('H0t0',1103,1099.00,1100.807716,.366083),('Om',1073,1063.87,1065.624,.096630)]:
 x=read('arithmetic/rational_'+name+'.json');assert x['population']==76116 and x['observed_circle']==count and round(x['tail_decimal'],6)==tail
 assert round(x['farey_approx'],2)==farey and round(x['mean_decimal'],6)==mean
# Story rates (story_independent.py).
x=read('story/story_replay.json');assert x['hits']==1614 and x['selected_counts']=={'narrow':13,'medium':87,'wide':140}
assert abs(x['R_sel_exact_float']['medium']-.049998525600919025)<1e-10 and x['targets']==100000 and round(x['window']*1e6,2)==22.47
sel=x['selected_counts'];empirical=[round(100*sel[k]/x['hits'],3) for k in ('narrow','medium','wide')];assert empirical==[0.805,5.390,8.674]
analytic=[round(100*x['R_sel_exact_float']['narrow'],3),round(100*x['R_sel_exact_float']['medium'],5),round(100*x['R_sel_exact_float']['wide'],5)];assert analytic==[1.007,4.99985,8.02194]
assert [round(100*v,2) for v in x['CP95_medium']]==[4.34,6.61] and round(1/x['R_sel_exact_float']['medium'])==20
out={'lineup_rank':20.5,'ties':39,'retest_hits':6,'routes':counts,'census_rows':len(rows),'v3_alpha':m['alpha_disposition_exact'],'census_alpha':c['headline_nonleak']['alpha_exact'],
 'reliability':{'v3_alpha':round(m['alpha_disposition'],4),'v3_pair_alpha_C_G':round(m['alpha_pairwise']['L-C|L-G'],4),'round2_alpha':r2['alpha_disposition_exact']},
 'census':{'adjudicated':dict(counts_c),'historical':dict(counts_h),'adjudication_outcomes':dict(adjud),'alpha_47':round(h['alpha_disposition'],4),'alpha_74':round(a['alpha_disposition'],4)},
 'lineup':lineup,'route_recount':recount,'story':{'empirical_percent':empirical,'analytic_percent':analytic,'cp95_medium_percent':[round(100*v,2) for v in x['CP95_medium']]}}
(S/'receipt_checks.json').write_text(json.dumps(out,indent=1)+'\n');print(out)
