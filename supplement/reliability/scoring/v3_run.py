# AX: SCRIPT | SUM: P1.5 v3 scoring — normalize lane replies, run UNCHANGED i4e_score.py (sha-pinned), census arm | SIG: v3run1
"""Usage: python3 -I v3_run.py r2 | primary | census
r2 = regression: the r2 inputs through this driver must reproduce the committed i4i_metrics.json (all keys).
primary/census: raw lane replies (verbatim, parts concatenated in order) lanes/{G,M,C}_verdicts.md resp.
census/lanes/{G,M,C}_verdicts.md → scoring/<arm>_<X>_norm.md (format-only normalization, first block per item wins)
→ scoring/<arm>_validation.json + <arm>_metrics.json + <ARM>_SCORING.md. Scorer file is never edited."""
import hashlib, importlib.util, json, os, re, shutil, sys, tempfile
from pathlib import Path
SC = Path(__file__).resolve().parent; U = SC.parent
R2 = U / 'historical'
SCORER_SHA = '66a2c7580c30fd58116017fd278a38243e4b928fb498979de4ee3ea9824cc4a5'
SLOT = {'fable': ('C', 'annotation_pack/i4b_verdicts.md'), 'astra': ('M', 'annotation_pack/i4c_verdicts.md'), 'sol': ('G', 'annotation_pack/i4d_verdicts.md')}
TOK = {'step0': ['PASS', 'FAIL'], 'step1': ['PASS', 'FAIL-UNIT', 'FAIL-EPOCH', 'NOT-REACHED'], 'step2': ['STATIC', 'HISTORY', 'NOT-REACHED'],
       'step4': ['REQUIRED', 'VACUOUS', 'NOT-APPLICABLE'], 'step5': ['CONSTANT', 'SELECTED-NEW', 'SELECTED-ESTABLISHED', 'VARIES', 'NOT-REACHED'],
       'disposition': ['LAW-CANDIDATE', 'OUTPUT-OF-HISTORY', 'MODEL-CHOICE', 'NOT-YET-A-QUANTITY', 'CONVENTION-BOUND', 'EPOCH-DEPENDENT', 'ALREADY-GOVERNED'],
       'confidence': ['high', 'med', 'low']}
KEYS = ['item', 'step0', 'step1', 'step2', 'step4', 'step5', 'disposition', 'confidence', 'shared_driver', 'reopen_condition', 'justification']
LINE = re.compile(r'^[\s>*_`#-]*(' + '|'.join(KEYS) + r')[\s*_`]*:\s*(.*?)\s*$', re.I)
# WHY: card consistency rules (step outcome → forced disposition); violations are reported, the disposition stands as recorded
FORCED = [('step0', 'FAIL', 'NOT-YET-A-QUANTITY'), ('step1', 'FAIL-UNIT', 'CONVENTION-BOUND'), ('step1', 'FAIL-EPOCH', 'EPOCH-DEPENDENT'), ('step2', 'HISTORY', 'OUTPUT-OF-HISTORY'),
          ('step5', 'CONSTANT', 'LAW-CANDIDATE'), ('step5', 'SELECTED-NEW', 'LAW-CANDIDATE'), ('step5', 'SELECTED-ESTABLISHED', 'ALREADY-GOVERNED'), ('step5', 'VARIES', 'MODEL-CHOICE')]


def scorer(path):
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == SCORER_SHA, 'scorer sha mismatch'
    spec = importlib.util.spec_from_file_location('i4e_score', path); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S); return S


def token(k, v):
    if k not in TOK: return v
    found = {t for t in TOK[k] if re.search(r'(?<![A-Za-z-])' + re.escape(t) + r'(?![A-Za-z-])', v, 0 if k == 'confidence' else re.I)}
    return found.pop() if len(found) == 1 else v  # ambiguous/none → raw, flagged by validate


def normalize(raw, ids):
    blocks, cur, changed, dups = {}, None, 0, []
    for line in raw.splitlines():
        m = LINE.match(line)
        if not m: continue
        k, v = m.group(1).lower(), m.group(2)
        v = re.sub(r'^[*_`]+|[*_`]+$', '', v).strip() if k in TOK or k == 'item' else v
        v = v.lower() if k == 'item' else v
        v = token(k, v.upper() if k in TOK and k != 'confidence' else v.lower() if k == 'confidence' else v)
        if k == 'item':
            cur = v if v not in blocks else None
            if cur is None: dups.append(v)
            else: blocks[cur] = {}
        elif cur and k not in blocks[cur]: blocks[cur][k] = v
        changed += f'{k}: {v}' != line
    text = '\n\n'.join('\n'.join([f'item: {q}'] + [f'{k}: {b[k]}' for k in KEYS[1:] if k in b]) for q, b in blocks.items() if q in ids) + '\n'
    return text, blocks, {'lines_reformatted': changed, 'duplicate_items_ignored': dups, 'unknown_items': sorted(set(blocks) - set(ids))}


def validate(blocks, ids):
    v = {'n_items': sum(q in blocks for q in ids), 'missing': [q for q in ids if q not in blocks],
         'missing_fields': {q: [k for k in KEYS[1:] if k not in b] for q, b in blocks.items() if any(k not in b for k in KEYS[1:])},
         'invalid_tokens': {q: {k: b[k] for k in TOK if k in b and b[k] not in TOK[k]} for q, b in blocks.items() if any(k in b and b[k] not in TOK[k] for k in TOK)},
         'consistency_violations': {q: [f'{s}={o} but disposition={b.get("disposition")}' for s, o, d in FORCED if b.get(s) == o and b.get('disposition') != d] for q, b in blocks.items()}}
    v['consistency_violations'] = {q: x for q, x in v['consistency_violations'].items() if x}
    v['scorable'] = not v['missing'] and not any('disposition' in x for x in v['invalid_tokens'].values())
    return v


def lanes_in(arm, ids):
    src = (U / 'lanes') if arm == 'primary' else (U / 'census' / 'lanes')
    out, val = {}, {}
    for X in 'GMC':
        text, blocks, info = normalize((src / f'{X}_verdicts.md').read_text(), ids)
        (SC / f'{arm}_{X}_norm.md').write_text(text); out[X] = blocks; val[X] = {**info, **validate(blocks, ids)}
    (SC / f'{arm}_validation.json').write_text(json.dumps(val, indent=1, ensure_ascii=False))
    return out, val


def run_scorer(layout):
    with tempfile.TemporaryDirectory() as td:
        td = Path(td); (td / 'annotation_pack').mkdir(); shutil.copy(R2 / 'i4e_score.py', td / 'i4e_score.py')
        for dst, src in layout.items(): os.symlink(Path(src).resolve(), td / dst)
        S = scorer(td / 'i4e_score.py'); m, ref, lanes = S.score(); return S, json.loads(json.dumps(m)), ref, lanes


def relabel(m):
    s = json.dumps(m)
    for slot, (X, _) in SLOT.items(): s = s.replace(f'"{slot}', f'"L-{X}').replace(f'|{slot}"', f'|L-{X}"')
    return json.loads(s)


def primary():
    ids = [f'q{i:02d}' for i in range(1, 67)]; _, val = lanes_in('primary', ids)
    if not all(v['scorable'] for v in val.values()): sys.exit('NOT SCORABLE: see scoring/primary_validation.json')
    layout = {'control_key.json': U / 'control_key_v3.json', 'reference_verdicts_LEAD.md': U / 'reference' / 'REFERENCE_V3.md',
              **{p: SC / f'primary_{X}_norm.md' for X, p in SLOT.values()}}
    S, m, _, _ = run_scorer(layout); m = relabel(m); m['scorer_sha256'] = SCORER_SHA; m['layout'] = {k: str(v) for k, v in layout.items()}
    (SC / 'primary_metrics.json').write_text(json.dumps(m, indent=1))
    (SC / 'PRIMARY_SCORING.md').write_text(S.render(m).replace('# P1.5 I4e — scoring (mechanical, PROTOCOL.md §Metrics frozen 2026-09-07)', '# P1.5 v3 — primary arm scoring (UNCHANGED i4e_score.py; PROTOCOL_V3 §Metrics)', 1)
                                          + f"\nscorer sha256 {SCORER_SHA}; lane slots fable=L-C astra=L-M sol=L-G; inputs {json.dumps(m['layout'])}\n")
    print(f"alpha={m['alpha_disposition']:.4f} verdict={m['verdict']} validity={m['validity_accuracy']:.4f} controls={ {k: v['hits'] for k, v in m['controls'].items()} } disagreements={len(m['disagreements'])}")


def census():
    import csv
    S = scorer(R2 / 'i4e_score.py'); ids = [f'c{i:02d}' for i in range(1, 75)]; L, val = lanes_in('census', ids)
    if not all(v['scorable'] for v in val.values()): sys.exit('NOT SCORABLE: see scoring/census_validation.json')
    ref = {r['id']: r['reference_disposition'] for r in csv.DictReader(open(U / 'census' / 'reference_census.tsv'), delimiter='\t')}
    leak = sorted({r['id'] for r in csv.DictReader(open(U / 'census' / 'leak_rows.tsv'), delimiter='\t')})
    assert len(ref) == 74 and set(ref) == set(ids)
    m = {'n_rows': 74, 'leak_rows': leak, 'lanes': ['L-G', 'L-M', 'L-C']}
    for tag, rows in (('headline_nonleak', [q for q in ids if q not in leak]), ('all_rows', ids)):
        maj = {q: S.majority([L[X][q]['disposition'] for X in 'GMC']) for q in rows}
        conf = {r: {c: 0 for c in S.CLASSES + ['NONE']} for r in S.CLASSES}
        for q in rows: conf[ref[q]][maj[q] or 'NONE'] += 1
        a = S.alpha([[L[X][q]['disposition'] for X in 'GMC'] for q in rows])
        m[tag] = {'n': len(rows), 'alpha_disposition': float(a), 'alpha_exact': str(a),
                  'alpha_steps': {s: float(S.alpha([[L[X][q][s] for X in 'GMC'] for q in rows])) for s in S.STEPS},
                  'majority_vs_reference': sum(maj[q] == ref[q] for q in rows) / len(rows), 'majority_none': [q for q in rows if maj[q] is None],
                  'lane_vs_reference': {f'L-{X}': sum(L[X][q]['disposition'] == ref[q] for q in rows) / len(rows) for X in 'GMC'},
                  'confusion_ref_rows_majority_cols': conf,
                  'disagreements': [{'item': q, 'reference': ref[q], 'majority': maj[q], **{f'L-{X}': L[X][q]['disposition'] for X in 'GMC'}} for q in rows if maj[q] != ref[q]]}
    (SC / 'census_metrics.json').write_text(json.dumps(m, indent=1))
    h = m['headline_nonleak']; md = ['# P1.5 v3 — census arm scoring (descriptive; CENSUS_ARM.md §Metrics)', '', f"leak rows excluded from headline ({len(leak)}): {', '.join(leak)}", '']
    for tag in ('headline_nonleak', 'all_rows'):
        x = m[tag]; md += [f"## {tag} (n={x['n']})", '', f"α (nominal, disposition): **{x['alpha_disposition']:.4f}** (exact {x['alpha_exact']}); per-step " + ', '.join(f'{s} {v:.4f}' for s, v in x['alpha_steps'].items()),
                          f"majority vs reference: **{x['majority_vs_reference']:.4f}**; no majority: {x['majority_none'] or 'none'}; per lane " + ', '.join(f'{k} {v:.4f}' for k, v in x['lane_vs_reference'].items()), '',
                          '| ref \\ maj | ' + ' | '.join(S.CLASSES + ['NONE']) + ' |', '|---|' + '---:|' * (len(S.CLASSES) + 1)]
        md += ['| ' + r + ' | ' + ' | '.join(str(x['confusion_ref_rows_majority_cols'][r][c]) for c in S.CLASSES + ['NONE']) + ' |' for r in S.CLASSES]
        md += ['', f"disagreements ({len(x['disagreements'])}):", '', '| item | reference | majority | L-G | L-M | L-C |', '|---|---|---|---|---|---|']
        md += [f"| {d['item']} | {d['reference']} | {d['majority']} | {d['L-G']} | {d['L-M']} | {d['L-C']} |" for d in x['disagreements']] + ['']
    (SC / 'CENSUS_SCORING.md').write_text('\n'.join(md) + f'\nscorer functions from i4e_score.py sha256 {SCORER_SHA} (unchanged)\n')
    print(f"census headline alpha={h['alpha_disposition']:.4f} n={h['n']} majority_vs_ref={h['majority_vs_reference']:.4f} disagreements={len(h['disagreements'])}")


def r2():
    layout = {'control_key.json': R2 / 'control_key_r2.json', 'reference_verdicts_LEAD.md': R2 / 'reference_verdicts_r2_LEAD.md',
              'annotation_pack/i4b_verdicts.md': R2 / 'annotation_pack_r2/i4hb_verdicts.md', 'annotation_pack/i4c_verdicts.md': R2 / 'annotation_pack_r2/i4hc_verdicts.md',
              'annotation_pack/i4d_verdicts.md': R2 / 'annotation_pack_r2/i4hd_verdicts.md'}
    S, m, _, _ = run_scorer(layout); ref = json.loads((R2 / 'i4i_metrics.json').read_text())
    bad = [k for k in ref if k not in ('scorer_sha256', 'layout') and m.get(k) != ref[k]]
    ids = [f'q{i:02d}' for i in range(1, 67)]; seen = ('step0', 'step1', 'step2', 'step5', 'disposition', 'confidence')
    with tempfile.TemporaryDirectory() as td:  # normalizer must change nothing the scorer sees on the clean r2 files
        for x in 'bcd':
            f = R2 / f'annotation_pack_r2/i4h{x}_verdicts.md'; n = Path(td) / f'{x}.md'; n.write_text(normalize(f.read_text(), ids)[0])
            a, b = S.parse(f), S.parse(n)
            if a.keys() != b.keys() or any(a[q].get(k) != b[q].get(k) for q in a for k in seen): bad.append(f'normalizer:{x}')
    messy = 'item: q01\n**step0:** PASS\n- step1: `PASS`\nstep2: History\nstep4: NOT-APPLICABLE\nstep5: NOT-REACHED\n**disposition:** OUTPUT-OF-HISTORY (dynamics)\nconfidence: Med\n' \
            'shared_driver: none\nreopen_condition: none stated\njustification: x_\n\nitem: q02\ndisposition: MODEL-CHOICE or OUTPUT-OF-HISTORY\n\nitem: q01\ndisposition: LAW-CANDIDATE\n'
    _, bl, info = normalize(messy, ['q01', 'q02']); v = validate(bl, ['q01', 'q02'])
    if not (bl['q01']['disposition'] == 'OUTPUT-OF-HISTORY' and bl['q01']['step2'] == 'HISTORY' and bl['q01']['step1'] == 'PASS' and bl['q01']['confidence'] == 'med'
            and bl['q01']['justification'] == 'x_' and info['duplicate_items_ignored'] == ['q01'] and 'q02' in v['invalid_tokens'] and not v['scorable']): bad.append('normalizer:synthetic')
    print(f"r2 alpha={m['alpha_disposition']:.4f} verdict={m['verdict']} REGRESSION {'OK' if not bad else 'MISMATCH ' + str(bad)}")
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    {'r2': r2, 'primary': primary, 'census': census}[sys.argv[1]]()
