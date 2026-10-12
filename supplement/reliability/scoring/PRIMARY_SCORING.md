# P1.5 v3 — primary arm scoring (UNCHANGED i4e_score.py; PROTOCOL_V3 §Metrics)

items 66 = 60 foreign + 6 controls; lanes L-C, L-M, L-G; valid lanes for α: ['L-C', 'L-M', 'L-G']

## Controls gate (lane invalid if misses > 2 of 6)

| lane | hits/6 | misses | valid |
|---|---:|---|---|
| L-C | 6 | — | True |
| L-M | 6 | — | True |
| L-G | 6 | — | True |

## Reliability (primary)

Krippendorff α (nominal), final disposition, 60 foreign items: **0.0955** (exact 189/1979) → **FAIL**
(thresholds: STRONG ≥ 0.8; PASS-RELIABLE ≥ 0.667; INCONCLUSIVE 0.4–0.667; FAIL < 0.4)

| step | α |
|---|---:|
| step0 | 1.0000 |
| step1 | 0.0955 |
| step2 | 0.0213 |
| step5 | 1.0000 |

pairwise α (disposition): L-C|L-M -0.2106, L-C|L-G 0.9270, L-M|L-G -0.1746

## Validity (secondary, no threshold)

majority-vote vs reference accuracy: **0.9833** (59/60); no-majority items: none
per-lane vs reference: L-C 1.0000, L-M 0.3333, L-G 0.9833

### Confusion matrix (rows = reference, cols = majority)

| ref \ maj | LAW-CANDIDATE | OUTPUT-OF-HISTORY | MODEL-CHOICE | NOT-YET-A-QUANTITY | CONVENTION-BOUND | EPOCH-DEPENDENT | ALREADY-GOVERNED | NONE |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| LAW-CANDIDATE | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| OUTPUT-OF-HISTORY | 0 | 52 | 0 | 0 | 1 | 0 | 0 | 0 |
| MODEL-CHOICE | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| NOT-YET-A-QUANTITY | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| CONVENTION-BOUND | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| EPOCH-DEPENDENT | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 |
| ALREADY-GOVERNED | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Disposition distribution (60 foreign)

| lane | LAW-CANDIDATE | OUTPUT-OF-HISTORY | MODEL-CHOICE | NOT-YET-A-QUANTITY | CONVENTION-BOUND | EPOCH-DEPENDENT | ALREADY-GOVERNED |
|---|---:|---:|---:|---:|---:|---:|---:|
| L-C | 0 | 53 | 0 | 0 | 3 | 4 | 0 |
| L-M | 0 | 13 | 0 | 0 | 43 | 4 | 0 |
| L-G | 0 | 52 | 0 | 0 | 4 | 4 | 0 |
| reference | 0 | 53 | 0 | 0 | 3 | 4 | 0 |

### Majority-vs-reference disagreements (1) — each requires written adjudication (protocol)

| item | reference | majority | L-C | L-M | L-G |
|---|---|---|---|---|---|
| q20 | OUTPUT-OF-HISTORY | CONVENTION-BOUND | OUTPUT-OF-HISTORY | CONVENTION-BOUND | CONVENTION-BOUND |

scorer sha256 66a2c7580c30fd58116017fd278a38243e4b928fb498979de4ee3ea9824cc4a5; lane slots fable=L-C astra=L-M sol=L-G; portable package inputs
