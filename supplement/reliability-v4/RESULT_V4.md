# P1.5 v4 — result (lead adjudication, 2026-10-08)

state: DONE. Protocol `PROTOCOL_V4.md` sha256 99ff717a… frozen 07:53:53Z; seal `seal_v4.json` sha256 d957a3b3… 08:04:24Z
(89 artifacts; keys hashed separately); lanes 08:04–08:11Z; scoring `scoring/v4_run.py` (α and majority from the unchanged
`i4e_score.py`, sha256 66a2c758…).

## Primary arm — reliability
- Krippendorff α (nominal, final disposition, 3 lanes × 60 fresh items) = **1.0000** (exact 1) → **STRONG** (bar 0.8).
- per-step α: step0 1.0 · step1 1.0 · step2 1.0 · step5 1.0; pairwise G|M, G|C, M|C all 1.0; unanimous 60/60.
- controls 6/6 for every lane (v3 controls reused unchanged).
- distribution (identical in all lanes): OUTPUT-OF-HISTORY 41 · EPOCH-DEPENDENT 10 · CONVENTION-BOUND 6 ·
  ALREADY-GOVERNED 3 · LAW-CANDIDATE 0 · MODEL-CHOICE 0 · NOT-YET-A-QUANTITY 0.
- natural-form step (the v3 failure): 43 unit-bearing foreign items; ratio named G 32 · M 33 · C 33, `none — rule 1`
  6 per lane (atomic units, Loschmidt constant), FAIL-UNIT without a `none` line: 0 in every lane. The v3 failure mode
  (43 of 44 unit-bearing items refused on units) is gone.
- lane validity: L-G gpt-6.1-sol ([transport identity omitted], 6 exec reads of the sealed path only), L-M gemini-3.1-pro
  (provider client [execution id omitted] + [execution id omitted], isolated), L-C claude-opus-5-5 ([transport identity omitted], 2 Reads of the
  sealed path only); all 66 blocks + completion line; no fallback (receipts `receipts/lanes/*.json`).
- adjudication: no item without a 3/3 agreement → nothing to adjudicate. Spot check of raw replies (q03, q14, q16, q22,
  q31, q39, q49, q64): agreement with independently worded reasons (e.g. q22 Γ_W/m_W formed by all three lanes).

## Historical arm — does the test say "yes" to numbers a later law fixed?
- S = 6/6 positives with majority LAW-CANDIDATE; F = 0/5 negatives → **YES-BRANCH WORKS** (bar S ≥ 5, F ≤ 1).
- positives (all LAW-CANDIDATE by majority): combining gas volumes 2:1; period–orbit exponent 3/2; hydrogen line ratio
  27/20; atomic splitting factor 4/3; nuclear closed-shell counts (L-G: OUTPUT-OF-HISTORY via the card's bound-state rule
  — the risk forecast in the protocol); electron moment anomaly.
- negatives (all refused): planetary gap growth → OUTPUT-OF-HISTORY; Moon/Sun disc ratio → EPOCH-DEPENDENT; g/π² →
  CONVENTION-BOUND (L-G EPOCH-DEPENDENT); solar days per year → EPOCH-DEPENDENT; solar cycle / largest-planet period →
  OUTPUT-OF-HISTORY.
- per lane: L-G S 5/6 F 0/5 · L-M S 6/6 F 0/5 · L-C S 6/6 F 0/5.
- limit (disclosed in the protocol): every lane recognized all 11 cases (`recognized: yes`), so hindsight may have helped;
  the arm shows that the card's yes-branch is reachable and is applied correctly on the classic cases judged at their
  knowledge state — not a blind discrimination. A blind version needs cases the annotators cannot recognize.

## What it means (lead reading)
- the instrument is externally runnable: three model families from three companies, given only the card and the dossiers,
  sort 60 fresh precision quantities identically. The v3 FAIL was the instrument's under-specified natural-form step, now
  mandatory and checkable — repaired and confirmed on fresh data under a new preregistration.
- the yes-branch exists: the same card that refuses 41 history outputs, 10 epoch readings and 6 conventions says
  LAW-CANDIDATE to the historical law numbers and refuses the historical numerology. This answers the census-arm limit
  ("a 73/74 refusal rate cannot by itself separate the thesis from a test that rarely says yes") on the classic cases.
- still true: model families are not human physicists; agreement is consistency, not truth; the census adjudication stays
  programme-internal; the historical cases were recognized.
