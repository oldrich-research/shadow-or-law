# U1 decoy story-calibration — lead adjudication (LEAD-ONLY; written 2026-10-07T07:00:43Z date -u)

inputs: prereg LEAD_PREREG.md (sha256 eade5ded…, 04:24Z, before the brief) · protocol LINEUP_PROTOCOL.md + addenda 1–5 (98824453…) · arm A = units/u1-story-cal/RESULT.md (U1a, gpt-6.1-sol high) + lead check lead_check.json (independent parser; same 87/1614) · arm B = seats/SEAT_{G,M,C}.md, judge rerun seats/judge/OUT_1.jsonl + OUT_3.jsonl ([operational identifier redacted], [operational identifier redacted], history: prompt + one reply, no tool call), statistics seats/judge/STATS.json (tools/adjudicate_lineup.py).

## Arm A — mechanical story rates (local range [α_G/10, 10α_G), 100,000 log-uniform targets)
| window | R_any | narrow, DL ≤ 8: R_sel | medium, DL ≤ 8: R_sel (decision) | wide, DL ≤ 8: R_sel |
|---|---|---|---|---|
| 22.47 ppm | 1614 (1.61 %) | 13/1614 = 0.81 % [CP95 0.43, 1.37]; exact 1.01 % | 87/1614 = 5.39 % [4.34, 6.61]; exact 5.00 % | 140/1614 = 8.67 %; exact 8.02 % |
| 1.85 ppm | 148 (0.15 %) | 1/148 = 0.68 %; exact 1.00 % | 6/148 = 4.05 % [1.50, 8.61]; exact 4.99 % | 10/148 = 6.76 %; exact 7.98 % |
- flagship (4/3, 21, 5/2) eligible in every layer; real-target selection at 22.47 ppm = the flagship (cost 28); at 1.85 ppm no hit.
- n = 21 story slopes: narrow {5/2 (B3), 7/3 (C3)}; medium 44 values (B3/C3 clocks × metrics).

## Arm B — blind lineup (40 rows, all n = 21; flagship + 39 decoys of the alpha_exp_family pool, cost ≤ 28)
- seat G (gpt-6.1-sol): one constructed account for every row (22-mode classical oscillator; n from mode count, k and c "chosen to fit"); recognition none.
- seat M (gemini-3.1-pro): "no account" × 40; recognition none ("arbitrarily generated combinations, n = 21 constant").
- seat C (claude-opus-5-5): one account for every row (one-sided Weyl denominator of SU(7): n = |Φ⁺(A₆)| = 21 derived, k and c tuned); flagship k matched only by a heat kernel with the wrong-sign power (Sp(2,C)/Sp(2), |ρ|² = 5/2); recognition none.
- judge (fresh one-message spawn): every account of a seat scored alike — G 5/10 × 40, C 6/10 × 40, M 0 × 40; flagship mid-rank 20.5/40 in every seat; per-formula mean 3.67 for all 40 → 39 decoys with mean ≥ flagship; test–retest 6/6 exact; judge recognition none.

## Predicted (prereg) → got
- R_cond (22.47 ppm, any c): narrow 3–15 % (point 6) → 1.05 % (exact 1.13) · medium 20–60 % (point 35) → 6.13 % (exact 5.63) · wide 40–90 % → 9.67 % (exact 9.01). Lead expectation too high by ≈ 6×: the slope stories are dense among simple fractions, but only 470 of 8,684 local-range expressions are exp·α forms, so few selected hits can carry a story.
- lineup: flagship among the best, not uniquely first (P(rank 1 in ≥ 2 seats) ≈ 0.15) → not distinguished at all (all ties) · ≥ 2 decoys ≥ flagship (P ≈ 0.6) → 39 · recognition (P ≈ 0.2) → none.
- outcome: weight 0.10 / no weight 0.55 / inconclusive 0.35 → NO WEIGHT.

## Decision rule (frozen) → verdict
- WEIGHT needs R_sel ≤ 2 % AND flagship rank 1–2 in ≥ 2 of 3 seats → no (5.39 %; 20.5, 20.5, 20.5).
- NO WEIGHT: R_sel ≥ 20 % OR ≥ 3 decoys with mean judge score ≥ the flagship's → yes (39 decoys).
- VERDICT: NO WEIGHT. The B3 slope reading (5/2 = 2|ρ|²/dim V, 21 = dim B3) carries no evidential weight beyond what the same search plus a story search yields for decoys. HS-2 closes as a documented coincidence at the story level; the flagship's evidence rests on the value layer (≈ 1–2σ) and external tests; a mechanism is not excluded as a category.

## Lead notes
- the lineup is degenerate (each seat wrote one template for all rows); it shows that blind experts see no distinguished account for the flagship; it cannot rank stories nobody proposed — which is the point: the B3 story is not what an unprimed expert reaches for.
- the narrow-layer rate (≈ 1 %) is the most favourable reading of the B3 story; that layer was defined after the flagship was known (κ = 1/d_min picked to fit), so it does not license weight either.
- for the paper's next version: story-layer chance probability = 5.0 % (medium, simplicity-matched, 22.47 ppm; 1.0 % narrow); blind three-family lineup: no distinction, no recognition.
- P(physical mechanism behind α²¹) ≈ 0.03 → ≈ 0.02.
