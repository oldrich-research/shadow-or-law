# Shadow or law? Reproducibility release

Reproducibility release of the paper *Shadow or law? Measured numbers as projections of an invariant whole, and a test
of which of them could be fixed by structure* (Oldřich Dvořák, 2026), doi:10.5281/zenodo.23221015.
The registered three-family reliability test (v3) remains a **FAIL** (alpha = 0.0955), with its cause located.
The separately preregistered v4 repeat gave exact alpha = 1 on 60 fresh quantities; the historical arm gave S = 6/6 and F = 0/5 on recognized cases. Agreement measures consistency, not truth; the historical arm is not blind discrimination.
This release preserves both tested instruments and their outputs. The census is programme-built and adjudicated by the author's programme. The shadow principle's universal
form and the source argument are argued in the paper, not computed here.

## Contents

- `census/`: the census CSV and the adjudicated census tables (column dictionary in `census/README.md`).
- `reliability/`: the exact tested card, foreign and census-arm dossiers, sealed references, lane outputs and the
  checksum-pinned scorer with its driver.
- `reliability-v4/`: corrected card, fresh stratified draw, dossiers, sealed prompts, keys, reply texts, pretest, validity summaries, scorer and recognized historical yes-branch arm.
- `adjudication/`: frozen adjudication rubrics and adjudication tables.
- `story/`: the story grammar, search population, selected-hit data and blinded lineup receipts.
- `routes/`: the scoped route index.
- `arithmetic/`: the exact rational calculator with the uniform-circle arithmetic-null protocol.
- `figures/`: the standalone figure sources.
- `claims/`: the complete 160-claim register with grades and standing (Appendix F prints its 69 core cards).
- `SHA256SUMS` (per-file SHA-256 checksums), `provenance.json` (source hash and adaptation of each curated file),
  `requirements.txt`, `reproduce.py`, `check_receipts.py`.

## One command

From the directory that contains `supplement/`, with Python 3.13 and the versions in `requirements.txt`
(numpy 2.5.3, scipy 1.18.1, sympy 1.14.0):

```sh
python -B supplement/reproduce.py
```

It recomputes from these files the v3, v4 and round-2 reliability coefficients, the census agreement and dispositions,
the arithmetic-null counts and tails, the story rates, the lineup ranks and the route-index counts printed in the
paper. It makes no network requests and starts no model sessions; runtime is several minutes.

Historical missing sham receipts and absent per-route class assignments are disclosed, not replaced by synthetic data.

## Files over 10 MB

| path in `supplement.tar.gz` | bytes | SHA-256 |
|---|---:|---|
| `supplement/story/inputs/gfull_engine_exprs.csv.gz` | 48,344,619 | 5cf9069a396933967b6a4805ebecfbad8f0732f9b431d5ea21b4a41c289f89de |
| `supplement/story/receipts/population.npz` | 67,845,635 | 6662954abc6e42c02d43c452c54e1e97afcd453f6bf969ebf96dae788fcee0be |

The companion repository keeps these two files out of its git tree; they ship inside `supplement.tar.gz`, which the
Zenodo record holds and each major revision's GitHub release attaches as an asset. To rerun from a repository
checkout, take `supplement/` from that archive. The raw search population is stored gzip-compressed (lossless);
`story/story_independent.py` checks the SHA-256 of the decompressed bytes.

## Licence and citation

CC-BY-4.0. Cite the paper: doi:10.5281/zenodo.23221015.
