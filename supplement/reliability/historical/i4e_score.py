# AX: ANALYZE | SUM: P1.5 I4e scorer — Krippendorff nominal alpha, controls gate, majority-vs-reference validity | SIG: i4e1
"""Mechanical scorer for PROTOCOL.md §Metrics (frozen 2026-09-07). Stdlib only; exact Fractions.
Usage: python i4e_score.py  → writes I4E_SCORING.md + i4e_metrics.json in this directory."""
import json, re, sys
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).parent
LANES = {'fable': 'annotation_pack/i4b_verdicts.md', 'astra': 'annotation_pack/i4c_verdicts.md', 'sol': 'annotation_pack/i4d_verdicts.md'}
REF = 'reference_verdicts_LEAD.md'
CLASSES = ['LAW-CANDIDATE', 'OUTPUT-OF-HISTORY', 'MODEL-CHOICE', 'NOT-YET-A-QUANTITY', 'CONVENTION-BOUND', 'EPOCH-DEPENDENT', 'ALREADY-GOVERNED']
STEPS = ['step0', 'step1', 'step2', 'step5']
FIELD = re.compile(r'^(item|step0|step1|step2|step5|disposition|confidence): *(.+?)\s*$')


def parse(path):
    out, cur = {}, None
    for line in Path(path).read_text().splitlines():
        m = FIELD.match(line)
        if not m: continue
        k, v = m.groups()
        if k == 'item': cur = v; out[cur] = {}
        elif cur: out[cur][k] = v
    return out


def alpha(units):
    """Krippendorff nominal alpha; units = list of value-lists (one per unit, any length >= 2)."""
    o = {}
    for vals in units:
        m = len(vals)
        if m < 2: continue
        for i in range(m):
            for j in range(m):
                if i != j: o[(vals[i], vals[j])] = o.get((vals[i], vals[j]), Q(0)) + Q(1, m - 1)
    cats = sorted({c for pair in o for c in pair})
    n_c = {c: sum(v for (a, _), v in o.items() if a == c) for c in cats}
    n = sum(n_c.values())
    d_o = sum(v for (a, b), v in o.items() if a != b)
    d_e = sum(n_c[a] * n_c[b] for a in cats for b in cats if a != b)
    if d_e == 0: return Q(1)
    return 1 - (n - 1) * d_o / d_e


def majority(vals):
    for v in set(vals):
        if vals.count(v) >= 2: return v
    return None


def score():
    key = json.loads((ROOT / 'control_key.json').read_text())
    ctrl = {item: next(c['disposition'] for c in key['controls'] if c['control_id'] == cid) for item, cid in key['assignments'].items()}
    lanes = {k: parse(ROOT / p) for k, p in LANES.items()}
    ref = parse(ROOT / REF)
    items = sorted(ref)
    foreign = [q for q in items if q not in ctrl]
    assert len(items) == 66 and len(foreign) == 60 and all(len(v) == 66 for v in lanes.values())
    names = list(LANES)
    m = {'n_items': len(items), 'n_foreign': len(foreign), 'n_controls': len(ctrl), 'lanes': names}
    m['controls'] = {k: {'hits': sum(lanes[k][q]['disposition'] == d for q, d in ctrl.items()), 'misses': [q for q, d in ctrl.items() if lanes[k][q]['disposition'] != d]} for k in names}
    for k in names: m['controls'][k]['valid'] = len(m['controls'][k]['misses']) <= 2
    valid = [k for k in names if m['controls'][k]['valid']]
    a = alpha([[lanes[k][q]['disposition'] for k in valid] for q in foreign])
    m['alpha_disposition'] = float(a); m['alpha_disposition_exact'] = str(a)
    m['alpha_steps'] = {s: float(alpha([[lanes[k][q][s] for k in valid] for q in foreign])) for s in STEPS}
    m['alpha_pairwise'] = {f'{x}|{y}': float(alpha([[lanes[x][q]['disposition'], lanes[y][q]['disposition']] for q in foreign])) for x, y in combinations(valid, 2)}
    m['verdict'] = 'STRONG' if a >= Q(4, 5) else 'PASS-RELIABLE' if a >= Q(667, 1000) else 'INCONCLUSIVE' if a >= Q(2, 5) else 'FAIL'
    maj = {q: majority([lanes[k][q]['disposition'] for k in valid]) for q in foreign}
    m['majority_none'] = [q for q in foreign if maj[q] is None]
    m['validity_accuracy'] = sum(maj[q] == ref[q]['disposition'] for q in foreign) / 60
    m['lane_vs_reference'] = {k: sum(lanes[k][q]['disposition'] == ref[q]['disposition'] for q in foreign) / 60 for k in names}
    conf = {r: {c: 0 for c in CLASSES + ['NONE']} for r in CLASSES}
    for q in foreign: conf[ref[q]['disposition']][maj[q] or 'NONE'] += 1
    m['confusion_ref_rows_majority_cols'] = conf
    m['disagreements'] = [{'item': q, 'reference': ref[q]['disposition'], 'majority': maj[q], **{k: lanes[k][q]['disposition'] for k in names}} for q in foreign if maj[q] != ref[q]['disposition']]
    m['distribution'] = {**{k: {c: sum(lanes[k][q]['disposition'] == c for q in foreign) for c in CLASSES} for k in names}, 'reference': {c: sum(ref[q]['disposition'] == c for q in foreign) for c in CLASSES}}
    return m, ref, lanes


def render(m):
    L = ['# P1.5 I4e — scoring (mechanical, PROTOCOL.md §Metrics frozen 2026-09-07)', '',
         f"items 66 = 60 foreign + 6 controls; lanes {', '.join(m['lanes'])}; valid lanes for α: {[k for k in m['lanes'] if m['controls'][k]['valid']]}", '',
         '## Controls gate (lane invalid if misses > 2 of 6)', '', '| lane | hits/6 | misses | valid |', '|---|---:|---|---|']
    L += [f"| {k} | {v['hits']} | {', '.join(v['misses']) or '—'} | {v['valid']} |" for k, v in m['controls'].items()]
    L += ['', '## Reliability (primary)', '', f"Krippendorff α (nominal), final disposition, 60 foreign items: **{m['alpha_disposition']:.4f}** (exact {m['alpha_disposition_exact']}) → **{m['verdict']}**",
          '(thresholds: STRONG ≥ 0.8; PASS-RELIABLE ≥ 0.667; INCONCLUSIVE 0.4–0.667; FAIL < 0.4)', '',
          '| step | α |', '|---|---:|'] + [f'| {s} | {v:.4f} |' for s, v in m['alpha_steps'].items()]
    L += ['', 'pairwise α (disposition): ' + ', '.join(f'{k} {v:.4f}' for k, v in m['alpha_pairwise'].items()), '',
          '## Validity (secondary, no threshold)', '', f"majority-vote vs reference accuracy: **{m['validity_accuracy']:.4f}** ({round(m['validity_accuracy']*60)}/60); no-majority items: {m['majority_none'] or 'none'}",
          'per-lane vs reference: ' + ', '.join(f'{k} {v:.4f}' for k, v in m['lane_vs_reference'].items()), '',
          '### Confusion matrix (rows = reference, cols = majority)', '', '| ref \\ maj | ' + ' | '.join(CLASSES + ['NONE']) + ' |', '|---|' + '---:|' * (len(CLASSES) + 1)]
    L += ['| ' + r + ' | ' + ' | '.join(str(m['confusion_ref_rows_majority_cols'][r][c]) for c in CLASSES + ['NONE']) + ' |' for r in CLASSES]
    L += ['', '### Disposition distribution (60 foreign)', '', '| lane | ' + ' | '.join(CLASSES) + ' |', '|---|' + '---:|' * len(CLASSES)]
    L += ['| ' + k + ' | ' + ' | '.join(str(m['distribution'][k][c]) for c in CLASSES) + ' |' for k in m['distribution']]
    L += ['', f"### Majority-vs-reference disagreements ({len(m['disagreements'])}) — each requires written adjudication (protocol)", '', '| item | reference | majority | ' + ' | '.join(m['lanes']) + ' |', '|---|---|---|' + '---|' * len(m['lanes'])]
    L += ['| ' + d['item'] + ' | ' + d['reference'] + ' | ' + str(d['majority']) + ' | ' + ' | '.join(d[k] for k in m['lanes']) + ' |' for d in m['disagreements']]
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    m, _, _ = score()
    (ROOT / 'i4e_metrics.json').write_text(json.dumps(m, indent=1))
    (ROOT / 'I4E_SCORING.md').write_text(render(m))
    ctrl_s = ', '.join(k + ':' + str(v['hits']) + '/6' for k, v in m['controls'].items())
    print(f"alpha_disposition={m['alpha_disposition']:.4f} verdict={m['verdict']} validity={m['validity_accuracy']:.4f} controls={{{ctrl_s}}} disagreements={len(m['disagreements'])}")
