# AX: SCRIPT | SUM: P1.5 v4 scoring — normalize lane replies, α/majority from UNCHANGED i4e_score.py functions, controls gate, natural-form provision, historical arm S/F | SIG: v4run1
"""Usage: python3 -I v4_run.py primary | hist
primary: lanes/{G,M,C}_verdicts.md → scoring/primary_<X>_norm.md, primary_validation.json, primary_metrics.json, PRIMARY_SCORING.md
hist:    hist/{G,M,C}_hist_verdicts.md → scoring/hist_<X>_norm.md, hist_validation.json, hist_metrics.json, HIST_SCORING.md
Thresholds, classes and α are PROTOCOL_V4 §Metrics; the scorer file is sha-pinned and never edited."""
import csv, hashlib, importlib.util, json, re, sys
from itertools import combinations
from pathlib import Path
SC = Path(__file__).resolve().parent; U = SC.parent
SCORER = U.parent / 'reliability' / 'historical' / 'i4e_score.py'
SCORER_SHA = '66a2c7580c30fd58116017fd278a38243e4b928fb498979de4ee3ea9824cc4a5'
FAM = {'G': 'L-G (OpenAI gpt-6.1-sol)', 'M': 'L-M (Google gemini-3.1-pro)', 'C': 'L-C (Anthropic claude-opus-5-5)'}
TOK = {'step0': ['PASS', 'FAIL'], 'step1': ['PASS', 'FAIL-UNIT', 'FAIL-EPOCH', 'NOT-REACHED'], 'step2': ['STATIC', 'HISTORY', 'NOT-REACHED'],
       'step4': ['REQUIRED', 'VACUOUS', 'NOT-APPLICABLE'], 'step5': ['CONSTANT', 'SELECTED-NEW', 'SELECTED-ESTABLISHED', 'VARIES', 'NOT-REACHED'],
       'disposition': ['LAW-CANDIDATE', 'OUTPUT-OF-HISTORY', 'MODEL-CHOICE', 'NOT-YET-A-QUANTITY', 'CONVENTION-BOUND', 'EPOCH-DEPENDENT', 'ALREADY-GOVERNED'],
       'confidence': ['high', 'med', 'low']}
KEYS = ['item', 'step0', 'step1', 'natural_form', 'step2', 'step4', 'step5', 'disposition', 'confidence', 'shared_driver', 'reopen_condition', 'justification', 'recognized']
LINE = re.compile(r'^[\s>*_`#-]*(' + '|'.join(KEYS) + r')[\s*_`]*:\s*(.*?)\s*$', re.I)
FORCED = [('step0', 'FAIL', 'NOT-YET-A-QUANTITY'), ('step1', 'FAIL-UNIT', 'CONVENTION-BOUND'), ('step1', 'FAIL-EPOCH', 'EPOCH-DEPENDENT'), ('step2', 'HISTORY', 'OUTPUT-OF-HISTORY'),
          ('step5', 'CONSTANT', 'LAW-CANDIDATE'), ('step5', 'SELECTED-NEW', 'LAW-CANDIDATE'), ('step5', 'SELECTED-ESTABLISHED', 'ALREADY-GOVERNED'), ('step5', 'VARIES', 'MODEL-CHOICE')]


def scorer():
    assert hashlib.sha256(SCORER.read_bytes()).hexdigest() == SCORER_SHA, 'scorer sha mismatch'
    spec = importlib.util.spec_from_file_location('i4e_score', SCORER); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S); return S


def token(k, v):
    if k not in TOK: return v
    found = {t for t in TOK[k] if re.search(r'(?<![A-Za-z-])' + re.escape(t) + r'(?![A-Za-z-])', v, 0 if k == 'confidence' else re.I)}
    return found.pop() if len(found) == 1 else v


def normalize(raw, ids):
    blocks, cur, dups = {}, None, []
    for line in raw.splitlines():
        m = LINE.match(line)
        if not m: continue
        k, v = m.group(1).lower(), m.group(2)
        v = re.sub(r'^[*_`]+|[*_`]+$', '', v).strip() if k in TOK or k == 'item' else v
        if k == 'item': v = v.lower()
        v = token(k, v.upper() if k in TOK and k != 'confidence' else v.lower() if k == 'confidence' else v)
        if k == 'item':
            cur = v if v not in blocks else None
            if cur is None: dups.append(v)
            else: blocks[cur] = {}
        elif cur and k not in blocks[cur]: blocks[cur][k] = v
    text = '\n\n'.join('\n'.join([f'item: {q}'] + [f'{k}: {b[k]}' for k in KEYS[1:] if k in b]) for q, b in blocks.items() if q in ids) + '\n'
    return text, blocks, {'duplicate_items_ignored': dups, 'unknown_items': sorted(set(blocks) - set(ids))}


def validate(blocks, ids, need):
    v = {'n_items': sum(q in blocks for q in ids), 'missing': [q for q in ids if q not in blocks],
         'missing_fields': {q: [k for k in need if k not in b] for q, b in blocks.items() if any(k not in b for k in need)},
         'invalid_tokens': {q: {k: b[k] for k in TOK if k in b and b[k] not in TOK[k]} for q, b in blocks.items() if any(k in b and b[k] not in TOK[k] for k in TOK)},
         'consistency_violations': {q: x for q, b in blocks.items() if (x := [f'{s}={o} but disposition={b.get("disposition")}' for s, o, d in FORCED if b.get(s) == o and b.get('disposition') != d])}}
    v['scorable'] = not v['missing'] and not any('disposition' in x for x in v['invalid_tokens'].values())
    return v


def load(arm, ids, need):
    src = {'primary': lambda X: U / 'lanes' / f'{X}_verdicts.md', 'hist': lambda X: U / 'hist' / f'{X}_hist_verdicts.md'}[arm]
    L, val = {}, {}
    for X in 'GMC':
        text, blocks, info = normalize(src(X).read_text(), ids)
        (SC / f'{arm}_{X}_norm.md').write_text(text); L[X] = blocks; val[X] = {**info, **validate(blocks, ids, need)}
    (SC / f'{arm}_validation.json').write_text(json.dumps(val, indent=1, ensure_ascii=False))
    if not all(v['scorable'] for v in val.values()): sys.exit(f'NOT SCORABLE: see scoring/{arm}_validation.json')
    return L, val


def primary():
    S = scorer(); ids = [f'q{i:02d}' for i in range(1, 67)]; L, val = load('primary', ids, KEYS[1:12])
    ck = json.loads((U / 'control_key_v4.json').read_text())
    ctrl = {q: next(c['disposition'] for c in ck['controls'] if c['control_id'] == cid) for q, cid in ck['assignments'].items()}
    foreign = [q for q in ids if q not in ctrl]; assert len(foreign) == 60
    m = {'protocol': 'PROTOCOL_V4.md sha256 99ff717a…', 'n_items': 66, 'n_foreign': 60, 'lanes': [FAM[X] for X in 'GMC']}
    m['controls'] = {X: {'hits': sum(L[X][q]['disposition'] == d for q, d in ctrl.items()), 'misses': [q for q, d in ctrl.items() if L[X][q]['disposition'] != d]} for X in 'GMC'}
    for X in 'GMC': m['controls'][X]['valid'] = len(m['controls'][X]['misses']) <= 2
    valid = [X for X in 'GMC' if m['controls'][X]['valid']]; m['valid_lanes'] = valid
    a = S.alpha([[L[X][q]['disposition'] for X in valid] for q in foreign])
    m['alpha_disposition'] = float(a); m['alpha_disposition_exact'] = str(a)
    m['verdict'] = 'STRONG' if a >= S.Q(4, 5) else 'PASS-RELIABLE' if a >= S.Q(667, 1000) else 'INCONCLUSIVE' if a >= S.Q(2, 5) else 'FAIL'
    m['alpha_steps'] = {s: float(S.alpha([[L[X][q][s] for X in valid] for q in foreign])) for s in S.STEPS}
    m['alpha_pairwise'] = {f'{x}|{y}': float(S.alpha([[L[x][q]['disposition'], L[y][q]['disposition']] for q in foreign])) for x, y in combinations(valid, 2)}
    maj = {q: S.majority([L[X][q]['disposition'] for X in valid]) for q in foreign}
    m['unanimous'] = sum(len({L[X][q]['disposition'] for X in valid}) == 1 for q in foreign)
    m['majority_none'] = [q for q in foreign if maj[q] is None]
    m['majority_distribution'] = {c: sum(maj[q] == c for q in foreign) for c in S.CLASSES}
    m['distribution'] = {X: {c: sum(L[X][q]['disposition'] == c for q in foreign) for c in S.CLASSES} for X in 'GMC'}
    items = {r['id']: r['name'] for r in csv.DictReader((U / 'items_v4.tsv').open(newline=''), delimiter='\t')}
    m['not_unanimous'] = [{'item': q, 'name': items[q], **{X: L[X][q]['disposition'] for X in 'GMC'}, 'majority': maj[q]} for q in foreign if len({L[X][q]['disposition'] for X in valid}) > 1]
    units = {}
    for q in foreign:
        u = re.search(r'^dimensions_units: (.*)$', (U / 'dossiers_v4' / f'{q}.md').read_text(), re.M).group(1).strip()
        units[q] = u
    ub = [q for q in foreign if units[q].lower() not in ('dimensionless', '1', '')]
    def named(nf): return bool(nf) and not nf.lower().startswith(('as stated', 'none', 'not-reached'))
    m['natural_form'] = {'unit_bearing_items': len(ub), 'unit_bearing_list': {q: units[q] for q in ub},
                         **{X: {'ratio_named': sum(named(L[X][q].get('natural_form', '')) for q in ub),
                                'none_with_reason': sum(L[X][q].get('natural_form', '').lower().startswith('none') for q in ub),
                                'fail_unit_without_none': [q for q in ub if L[X][q]['step1'] == 'FAIL-UNIT' and not L[X][q].get('natural_form', '').lower().startswith('none')]} for X in 'GMC'}}
    m['scorer_sha256'] = SCORER_SHA
    (SC / 'primary_metrics.json').write_text(json.dumps(m, indent=1, ensure_ascii=False))
    md = ['# P1.5 v4 — primary arm scoring (α and majority from the UNCHANGED i4e_score.py; PROTOCOL_V4 §Metrics)', '',
          f"items 66 = 60 foreign + 6 controls; lanes {', '.join(FAM[X] for X in 'GMC')}; valid lanes for α: {valid}", '',
          '## Controls gate (lane invalid if misses > 2 of 6)', '', '| lane | hits/6 | misses | valid |', '|---|---:|---|---|']
    md += [f"| {FAM[X]} | {m['controls'][X]['hits']} | {', '.join(m['controls'][X]['misses']) or '—'} | {m['controls'][X]['valid']} |" for X in 'GMC']
    md += ['', '## Reliability (primary)', '', f"Krippendorff α (nominal), final disposition, 60 foreign items: **{m['alpha_disposition']:.4f}** (exact {m['alpha_disposition_exact']}) → **{m['verdict']}**",
           '(thresholds: STRONG ≥ 0.8; PASS-RELIABLE ≥ 0.667; INCONCLUSIVE 0.4–0.667; FAIL < 0.4)', '', '| step | α |', '|---|---:|']
    md += [f'| {s} | {v:.4f} |' for s, v in m['alpha_steps'].items()]
    md += ['', 'pairwise α (disposition): ' + ', '.join(f'{k} {v:.4f}' for k, v in m['alpha_pairwise'].items()), f"unanimous items: {m['unanimous']}/60; no-majority items: {m['majority_none'] or 'none'}", '',
           '### Disposition distribution (60 foreign)', '', '| lane | ' + ' | '.join(S.CLASSES) + ' |', '|---|' + '---:|' * len(S.CLASSES)]
    md += ['| ' + FAM[X] + ' | ' + ' | '.join(str(m['distribution'][X][c]) for c in S.CLASSES) + ' |' for X in 'GMC']
    md += ['| majority | ' + ' | '.join(str(m['majority_distribution'][c]) for c in S.CLASSES) + ' |', '',
           f"### Items without a 3/3 agreement ({len(m['not_unanimous'])}) — each adjudicated in writing (protocol)", '', '| item | name | L-G | L-M | L-C | majority |', '|---|---|---|---|---|---|']
    md += [f"| {d['item']} | {d['name']} | {d['G']} | {d['M']} | {d['C']} | {d['majority']} |" for d in m['not_unanimous']]
    nf = m['natural_form']
    md += ['', f"### Natural-form provision (descriptive; {nf['unit_bearing_items']} unit-bearing foreign items)", '', '| lane | ratio named | none — reason | FAIL-UNIT without a none line |', '|---|---:|---:|---|']
    md += [f"| {FAM[X]} | {nf[X]['ratio_named']} | {nf[X]['none_with_reason']} | {', '.join(nf[X]['fail_unit_without_none']) or '—'} |" for X in 'GMC']
    md += ['', f'scorer functions from i4e_score.py sha256 {SCORER_SHA} (unchanged)']
    (SC / 'PRIMARY_SCORING.md').write_text('\n'.join(md) + '\n')
    print(f"alpha={m['alpha_disposition']:.4f} verdict={m['verdict']} controls={ {X: m['controls'][X]['hits'] for X in 'GMC'} } unanimous={m['unanimous']}/60 pairwise={m['alpha_pairwise']}")


def hist():
    S = scorer(); ids = [f'h{i:02d}' for i in range(1, 12)]; L, val = load('hist', ids, KEYS[1:13])
    key = json.loads((U / 'hist' / 'hist_key_v4.json').read_text())['items']
    pos = [h for h in ids if key[h]['truth'] == 'POSITIVE']; neg = [h for h in ids if key[h]['truth'] == 'NEGATIVE']
    maj = {h: S.majority([L[X][h]['disposition'] for X in 'GMC']) for h in ids}
    rec = {h: {X: not L[X][h].get('recognized', '').lower().startswith('no') for X in 'GMC'} for h in ids}
    Sv = sum(maj[h] == 'LAW-CANDIDATE' for h in pos); Fv = sum(maj[h] == 'LAW-CANDIDATE' for h in neg)
    verdict = 'YES-BRANCH WORKS' if Sv >= 5 and Fv <= 1 else 'PARTIAL' if Sv in (3, 4) and Fv <= 1 else 'FAILS'
    unrec = [h for h in ids if not any(rec[h].values())]
    m = {'S': Sv, 'F': Fv, 'n_pos': len(pos), 'n_neg': len(neg), 'verdict': verdict,
         'per_lane': {X: {'S': sum(L[X][h]['disposition'] == 'LAW-CANDIDATE' for h in pos), 'F': sum(L[X][h]['disposition'] == 'LAW-CANDIDATE' for h in neg)} for X in 'GMC'},
         'recognized_by_any_lane': len(ids) - len(unrec), 'unrecognized_items': unrec,
         'S_unrecognized': sum(maj[h] == 'LAW-CANDIDATE' for h in pos if h in unrec), 'F_unrecognized': sum(maj[h] == 'LAW-CANDIDATE' for h in neg if h in unrec),
         'rows': [{'item': h, 'case': key[h]['slug'], 'truth': key[h]['truth'], 'best_class': key[h]['best_class'], **{X: L[X][h]['disposition'] for X in 'GMC'}, 'majority': maj[h],
                   'recognized': {X: L[X][h].get('recognized', '') for X in 'GMC'}} for h in ids],
         'alpha_disposition_11': float(S.alpha([[L[X][h]['disposition'] for X in 'GMC'] for h in ids])), 'scorer_sha256': SCORER_SHA}
    (SC / 'hist_metrics.json').write_text(json.dumps(m, indent=1, ensure_ascii=False))
    md = ['# P1.5 v4 — historical yes-branch arm (PROTOCOL_V4 §Historical arm)', '', f"S = {Sv}/{len(pos)} positives with majority LAW-CANDIDATE · F = {Fv}/{len(neg)} negatives with majority LAW-CANDIDATE → **{verdict}**",
          '(YES-BRANCH WORKS: S ≥ 5 and F ≤ 1 · PARTIAL: S ∈ {3, 4} and F ≤ 1 · FAILS otherwise)', '',
          'per lane: ' + ', '.join(f"{FAM[X]} S {m['per_lane'][X]['S']}/6 F {m['per_lane'][X]['F']}/5" for X in 'GMC'),
          f"recognized by at least one lane: {m['recognized_by_any_lane']}/11; S, F over items no lane recognized: {m['S_unrecognized']}, {m['F_unrecognized']} (items: {unrec or 'none'})", '',
          '| item | case | truth | L-G | L-M | L-C | majority |', '|---|---|---|---|---|---|---|']
    md += [f"| {r['item']} | {r['case']} | {r['truth']} | {r['G']} | {r['M']} | {r['C']} | {r['majority']} |" for r in m['rows']]
    (SC / 'HIST_SCORING.md').write_text('\n'.join(md) + '\n')
    print(f"S={Sv}/6 F={Fv}/5 verdict={verdict} per_lane={m['per_lane']} recognized={m['recognized_by_any_lane']}/11")


if __name__ == '__main__': {'primary': primary, 'hist': hist}[sys.argv[1]]()
