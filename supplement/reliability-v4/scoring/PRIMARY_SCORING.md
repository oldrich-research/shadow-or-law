# P1.5 v4 — primary arm scoring (α and majority from the UNCHANGED i4e_score.py; PROTOCOL_V4 §Metrics)

items 66 = 60 foreign + 6 controls; lanes L-G (OpenAI gpt-6.1-sol), L-M (Google gemini-3.1-pro), L-C (Anthropic claude-opus-5-5); valid lanes for α: ['G', 'M', 'C']

## Controls gate (lane invalid if misses > 2 of 6)

| lane | hits/6 | misses | valid |
|---|---:|---|---|
| L-G (OpenAI gpt-6.1-sol) | 6 | — | True |
| L-M (Google gemini-3.1-pro) | 6 | — | True |
| L-C (Anthropic claude-opus-5-5) | 6 | — | True |

## Reliability (primary)

Krippendorff α (nominal), final disposition, 60 foreign items: **1.0000** (exact 1) → **STRONG**
(thresholds: STRONG ≥ 0.8; PASS-RELIABLE ≥ 0.667; INCONCLUSIVE 0.4–0.667; FAIL < 0.4)

| step | α |
|---|---:|
| step0 | 1.0000 |
| step1 | 1.0000 |
| step2 | 1.0000 |
| step5 | 1.0000 |

pairwise α (disposition): G|M 1.0000, G|C 1.0000, M|C 1.0000
unanimous items: 60/60; no-majority items: none

### Disposition distribution (60 foreign)

| lane | LAW-CANDIDATE | OUTPUT-OF-HISTORY | MODEL-CHOICE | NOT-YET-A-QUANTITY | CONVENTION-BOUND | EPOCH-DEPENDENT | ALREADY-GOVERNED |
|---|---:|---:|---:|---:|---:|---:|---:|
| L-G (OpenAI gpt-6.1-sol) | 0 | 41 | 0 | 0 | 6 | 10 | 3 |
| L-M (Google gemini-3.1-pro) | 0 | 41 | 0 | 0 | 6 | 10 | 3 |
| L-C (Anthropic claude-opus-5-5) | 0 | 41 | 0 | 0 | 6 | 10 | 3 |
| majority | 0 | 41 | 0 | 0 | 6 | 10 | 3 |

### Items without a 3/3 agreement (0) — each adjudicated in writing (protocol)

| item | name | L-G | L-M | L-C | majority |
|---|---|---|---|---|---|

### Natural-form provision (descriptive; 43 unit-bearing foreign items)

| lane | ratio named | none — reason | FAIL-UNIT without a none line |
|---|---:|---:|---|
| L-G (OpenAI gpt-6.1-sol) | 32 | 6 | — |
| L-M (Google gemini-3.1-pro) | 33 | 6 | — |
| L-C (Anthropic claude-opus-5-5) | 33 | 6 | — |

scorer functions from i4e_score.py sha256 66a2c7580c30fd58116017fd278a38243e4b928fb498979de4ee3ea9824cc4a5 (unchanged)
