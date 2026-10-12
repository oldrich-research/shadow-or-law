# AX: SCRIPT | SUM: assemble v4 lane prompts (task + card + dossiers, one file each) and seal every artifact | SIG: p15seal04
"""Usage: python3 -I seal_v4.py → lanes/LANE_PROMPT_V4.md, lanes/LANE_PROMPT_HIST_V4.md, seal_v4.json (keys hashed separately, never inline)."""
import csv, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
HERE = Path(__file__).resolve().parent


def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def run():
    card = (HERE / 'card_v4.md').read_text()
    ids = [r['id'] for r in csv.DictReader((HERE / 'items_v4.tsv').open(newline=''), delimiter='\t')]
    assert ids == [f'q{i:02d}' for i in range(1, 67)]
    prim = (HERE / 'lanes' / 'ANNOTATOR_TASK_V4.md').read_text() + '\n' + card + '\n' + '\n'.join((HERE / 'dossiers_v4' / f'{q}.md').read_text() for q in ids)
    hist = (HERE / 'hist' / 'HIST_TASK_V4.md').read_text() + '\n' + card + '\n' + '\n'.join((HERE / 'hist' / f'h{i:02d}.md').read_text() for i in range(1, 12))
    for text in (prim, hist):  # no key, slug, truth or pretest material may reach a lane
        for bad in ('POSITIVE', 'NEGATIVE', 'truth', 'slug', 'control_id', 'hist_key', 'pretest', 'PRETEST', 'later_explanation'):
            assert bad not in text, bad
    (HERE / 'lanes' / 'LANE_PROMPT_V4.md').write_text(prim); (HERE / 'lanes' / 'LANE_PROMPT_HIST_V4.md').write_text(hist)
    files = ['PROTOCOL_V4.md', 'card_v4.md', 'card_v4.diff', 'draw_v4.py', 'sample_v4.tsv', 'items_v4.tsv', 'lanes/ANNOTATOR_TASK_V4.md', 'lanes/LANE_PROMPT_V4.md',
             'hist/HIST_TASK_V4.md', 'hist/make_hist_v4.py', 'lanes/LANE_PROMPT_HIST_V4.md', 'receipts/dossier_scan_v4.json'] + \
            [f'dossiers_v4/{q}.md' for q in ids] + [f'hist/h{i:02d}.md' for i in range(1, 12)]
    seal = {'sealed_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'artifacts': {f: sha(HERE / f) for f in files},
            'keys_hashed_separately': {'control_key_v4.json': sha(HERE / 'control_key_v4.json'), 'hist/hist_key_v4.json': sha(HERE / 'hist' / 'hist_key_v4.json')}}
    (HERE / 'seal_v4.json').write_text(json.dumps(seal, indent=1) + '\n')
    for f, h in seal['artifacts'].items(): assert sha(HERE / f) == h
    print(json.dumps({'sealed_at': seal['sealed_at'], 'n': len(files), 'LANE_PROMPT_V4': seal['artifacts']['lanes/LANE_PROMPT_V4.md'][:12],
                      'LANE_PROMPT_HIST_V4': seal['artifacts']['lanes/LANE_PROMPT_HIST_V4.md'][:12], 'seal_sha': sha(HERE / 'seal_v4.json')[:12]}))


if __name__ == '__main__': run()
