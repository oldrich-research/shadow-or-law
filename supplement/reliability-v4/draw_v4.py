# AX: SCRIPT | SUM: v4 stratified lowest-hash draw, v3 controls reused, blinded interleave, v3 dossier template | SIG: p15draw04
"""Usage: python3 -I draw_v4.py  → sample_v4.tsv, items_v4.tsv, control_key_v4.json, dossiers_v4/q01..q66.md, receipts/dossier_scan_v4.json"""
import csv, hashlib, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent; V3 = HERE / 'draw-inputs'
SEED = '20261008-p15-v4'
QUOTA = {'CODATA-2022': 10, 'PDG-2024': 12, 'Planck-2018': 3, 'materials': 9, 'atomic-molecular-chemical': 8, 'nuclear': 8, 'astronomy-geo-planetary': 10}
BANNED = re.compile(r'LAW-CANDIDATE|OUTPUT-OF-HISTORY|MODEL-CHOICE|NOT-YET-A-QUANTITY|CONVENTION-BOUND|EPOCH-DEPENDENT|ALREADY-GOVERNED|\bfundamental\b|\brelic\b|\bhistory\b|\bhistorical\b|\bconvention\b|\bconventional\b|\bparameter choice\b|\bderived from\b|\bgoverned\b', re.I)
T = '# {qid} — {name}\n\n```text\nname: {name}\ndefinition: {definition}\ndimensions_units: {units}\nvalue: {value}\nsigma: {sigma}\nsource: {source}\nvalue_confidence: {confidence}\n```\n\n## Context\n\n{context}\n'


def rows(p):
    with p.open(newline='') as f: return list(csv.DictReader(f, delimiter='\t'))


def key(name, tag=''): return hashlib.sha256((SEED + '|' + tag + name).encode()).hexdigest()


def run():
    fam = {r['name']: r['source-list'] for r in rows(V3 / 'pool_v3.tsv')}
    excl = {r['pool_name'] for r in rows(V3 / 'exclusions_v3.tsv') if r['pool_name']}
    v3drawn = {r['name'] for r in rows(V3 / 'sample_v3.tsv')}
    ck3 = json.loads((V3 / 'control_key_v3.json').read_text()); ctrl = {c['name']: c for c in ck3['controls']}
    elig = sorted(n for n in fam if n not in excl and n not in v3drawn and n not in ctrl)
    assert len(elig) == 249, len(elig)
    sel = []
    for f, k in QUOTA.items():
        cand = sorted((key(n), n) for n in elig if fam[n] == f); assert len(cand) >= k, (f, len(cand)); sel += [(f, kk, n) for kk, n in cand[:k]]
    assert len(sel) == 60 and len({n for _, _, n in sel}) == 60
    names = [n for _, _, n in sel] + list(ctrl)
    order = sorted(names, key=lambda n: (key(n, 'order|'), n)); assert len(order) == 66
    with (HERE / 'sample_v4.tsv').open('w', newline='') as fh:
        w = csv.writer(fh, delimiter='\t'); w.writerow(['family', 'name', 'selection_key']); w.writerows([(f, n, kk) for f, kk, n in sel])
    ids = {n: f'q{i:02d}' for i, n in enumerate(order, 1)}
    with (HERE / 'items_v4.tsv').open('w', newline='') as fh:
        w = csv.writer(fh, delimiter='\t'); w.writerow(['id', 'name']); w.writerows([(ids[n], n) for n in order])
    ck = {'seed': SEED, 'source': 'v3 controls reused unchanged (control_key_v3.json)', 'controls': ck3['controls'],
          'assignments': {ids[n]: ctrl[n]['control_id'] for n in order if n in ctrl}}
    (HERE / 'control_key_v4.json').write_text(json.dumps(ck, ensure_ascii=False, indent=2) + '\n')
    data = {r['name']: r for r in json.loads((V3 / 'quantity_data_v3.json').read_text())}
    for n, d in json.loads((V3 / 'dossier_definitions_v3.json').read_text()).items(): data[n].update(d)
    for n, c in ctrl.items(): data[n] = c
    out = HERE / 'dossiers_v4'; out.mkdir(exist_ok=True); hits = []
    for n in order:
        d = data[n]; s = T.format(qid=ids[n], **{k: d[k] for k in ['name', 'definition', 'units', 'value', 'sigma', 'source', 'context']}, confidence='med')
        hits += [dict(item=ids[n], token=m.group()) for m in BANNED.finditer(s)]
        (out / (ids[n] + '.md')).write_text(s)
    (HERE / 'receipts' / 'dossier_scan_v4.json').write_text(json.dumps(dict(dossiers=66, banned_hits=hits), indent=2) + '\n')
    assert not hits, hits
    return dict(eligible=len(elig), drawn=60, controls=len(ctrl), items=66, families={f: sum(1 for x in sel if x[0] == f) for f in QUOTA})


if __name__ == '__main__': print(json.dumps(run()))
