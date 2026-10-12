# U1 decoy story-calibration — lead preregistration (LEAD-ONLY; written 2026-10-07 04:24Z date -u, before the unit brief and before any U1 number exists)

[operational identifier redacted] (board research). Design source: units/forge-hs2/DISPOSITION.md rows 11–18 (council 2026-10-07). Executor never opens this file.
Information the lead had when writing: the published look-elsewhere audit (any-hit rate 1.614 % at 22.47 ppm over [α_G/10, 10α_G)); counts only from the population CSV: 8,684 expressions in the local range, 470 contain both exp and alpha, flagship = root `alpha_exp_family`, cost 28 (no k values, no story checks looked at).

## Question
Does the group reading of the flagship's slope (5/2 = 2|ρ|²/dim V for B3, with exponent 21 = dim B3) carry evidential weight beyond what the same formula search plus a story search yields for decoy targets? Pre-registered as the evidential weight of the slope layer; never a verdict on mechanism or coincidence as categories (council rows 18).

## Definitions (fixed now; the brief carries the same text)
- population: published G-FULL CSV (sha256 7d997675…), positive finite cumulative values; local range [α_G/10, 10α_G) log-uniform; windows w = 22.47 ppm (primary) and 1.85 ppm (secondary), relative.
- story-eligible expression: parses exactly as c·α^n·exp(−kα), c > 0 independent of α, n integer, k rational > 0; story layer passes (n, k).
- story layers (α_G = Z⁻² mapping: n = dim g, k = 2|ρ|²κ; long roots² = 2 unless stated):
  - narrow: g compact simple; κ = 1/d_min(g) only; metric long roots² = 2.
  - medium: g compact simple; κ ∈ {1, 1/2, 2, 1/d_min, 1/(2 d_min), 1/d_2, 1/h∨, 1/(2h∨), 1/dim g} (d_2 = second-smallest nontrivial irrep dimension); metrics: long roots² ∈ {2, 1}, Killing form (|ρ|² = dim g/24), C₂(d_min irrep) = 1.
  - wide: medium ∪ semisimple g with ≤ 3 simple factors (dim ≤ 60; |ρ|² additive, clocks from the factor set) ∪ the Z⁻¹ mapping (n = dim g/2, k = |ρ|²κ).
- equal surface simplicity: c rational p/q reduced with DL(c) = ℓ(p) + ℓ(q) ≤ DL(4/3) = 8, ℓ(m) = 2⌊log₂ m⌋ + 1; "any c" = no restriction.
- rates over the local range: R_any = any-hit coverage (published 1.614 % at 22.47 ppm); R_cov(width, c-class) = coverage of story-eligible windows; R_cond = R_cov/R_any; R_sel = fraction of hit-bearing targets whose selected expression (reporting rule: min cost, then min |residual|) is story-eligible.
- lineup: pool = `alpha_exp_family` expressions in the local range with cost ≤ 28, deduplicated by (c, n, k), flagship excluded; 39 drawn with seed 20261007 (all if fewer); flagship added; three random orders; formulas shown as f(x) = c·x^n·e^{−kx}, x a small positive parameter, nothing else.
- judge rubric (frozen, given to the judge verbatim): per account, P power forced by the stated object (0/1/2) · S slope forced by the SAME object with a standard clock and normalization (2 = standard conventions only, 1 = one non-standard choice, 0 = fitted or unstated) · U one object for n and k (0/1/2) · C prefactor (0 free, 1 partly, 2 forced) · V mathematical correctness checked by the judge (0/1/2); score = P + S + U + C + V (0–10). Flagship rank per seat by judge score (mid-rank for ties).

## Lead expectations (before any number)
- analytic note written now: with n = 21 both B3 and C3 give natural narrow-width slopes (B3: 2·(35/4)/7 = 5/2; C3 = sp(6): |ρ|² = 7, vector 6 ⇒ 7/3), and h∨ clocks give 7/2 for both; Killing metric gives |ρ|² = 7/8 for both ⇒ the medium story set at n = 21 contains many simple fractions (≈ 1/4, 2/3, 5/6, 7/8, 1, 7/6, 5/4, 7/4, 2, 7/3, 5/2, 35/12, 7/2, 14/3, …). The slope layer is therefore expected to be common at medium width.
- R_cond (22.47 ppm, any c): narrow 3–15 % (point 6 %), medium 20–60 % (point 35 %), wide 40–90 % (point 60 %); DL-matched: ×0.3–0.7 of each. R_sel lower than R_cond by ×0.3–1 (cheaper non-exp expressions win selection). Secondary window: same R_cond order (both numerator and denominator scale with w).
- lineup: flagship judged among the best but not uniquely first; P(flagship rank 1 for ≥ 2 of 3 seats) ≈ 0.15; expected ≥ 2 decoys with mean score ≥ the flagship's if the pool contains (c, 21, 7/3) or (c, 21, 7/2) with simple c (P ≈ 0.6 that it does).
- recognition: P(some seat recognizes the flagship as a published G relation) ≈ 0.2.
- outcome probabilities under the decision rule below: weight ≈ 0.10, no weight ≈ 0.55, inconclusive ≈ 0.35.

## Decision rule (frozen)
- WEIGHT: R_sel(medium, DL-matched, 22.47 ppm) ≤ 2 % AND the flagship ranks 1st or 2nd for ≥ 2 of 3 lineup seats (recognizing seats excluded; if fewer than 2 non-recognizing seats remain, the lineup arm is void and the rule uses arm A alone with threshold ≤ 1 %). → slope layer carries weight (LR ≈ 1/R_sel under the stated null); a new forge round with the calibrated story layer; the paper's next version states the measured probability.
- NO WEIGHT: R_sel(medium, DL-matched, 22.47 ppm) ≥ 20 % OR ≥ 3 decoys with mean judge score ≥ the flagship's (non-recognizing seats). → HS-2 closed as a documented coincidence at the story level; the flagship's evidence rests on the value layer (≈ 1–2σ) and external tests; mechanism not excluded as a category.
- otherwise INCONCLUSIVE: report R_sel per width, the lineup ranks and the implied LR range; no change of programme direction.
- invalid run: parser verification fails (re-evaluated value ≠ CSV value beyond 1e-12 relative for any parsed expression), population hash mismatch, or a seat with access to project files/memory/web (tool logs) → that part void, rerun.
