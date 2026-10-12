# Census arm — lead adjudication · 2026-10-07T17:26:29Z · lead g-decode

rubric: CENSUS_ADJUDICATION_PRECOMMIT.md (sha 3613556b, frozen 17:16:44Z before L-C output). Inputs: frozen scorer output
`units/pub2-reliability-v3/scoring/CENSUS_SCORING.md` + census_metrics.json; lanes G (sha 703b675c), M (d20bcd8a), C
(7e689fbd; claude-opus-5-5 ×7 entries, no fallback, 2 Reads = whole prompt lines 1–1607, prompt sha e97e084a); card v3;
sealed dossiers; reference_census.tsv. No label, card, dossier, reference, leak list or metric changed.

## Result (descriptive arm, no pass threshold)
- agreement: non-leak (n = 47) α = 4467/6847 = 0.6524; per-step α step0 0.672 · step1 0.672 · step2 0.681 · step5 0.528.
  All rows (n = 74) α = 10562/15645 = 0.6751.
- majority vs September census: non-leak 28/47 (0.596; per lane G 0.617 · M 0.638 · C 0.511); all rows 48/74 (0.649).
  No majority: c15, c17, c48, c62.
- adjudication of all 26 disagreement rows: CENSUS-FAULTED 21 · AMBIGUOUS 4 (c01, c15, c17, c62) · DOSSIER-DEFECT 1 (c23)
  · REFERENCE-STANDS 0. Table: `census_adjudication.tsv` (same dir).
- adjudicated census (printed in PUB-2; historical exposition count beside it): 73/74 not law candidates (historical
  61/74 refused); OUTPUT-OF-HISTORY 40 (historical 44) · ALREADY-GOVERNED 11 · EPOCH-DEPENDENT 10 · NOT-YET-A-QUANTITY 8
  · MODEL-CHOICE 2 · CONVENTION-BOUND 2 · LAW-CANDIDATE 1 = c56 δ_CP ∈ {0°,180°} / J_CP = 0, conditional on premise X —
  the card's own walked example (leak row). Non-leak rows: 0 law candidates.

## What moved, by class
1. own rows (9 of the 10 September LAW-CANDIDATE rows move; programme rows got no special pleading):
   free-parameter rule (step 2: masses, couplings, mixings of the current standard theory are HISTORY until a mechanism
   bridges them) → c44 α_G flagship, c09 m_e/M_Pl, c05 Σm_ν (d = 6), c65 m_ββ = OUTPUT-OF-HISTORY, reopen = a bridge
   deriving the input from static structure, then the α-expression's rational-density null; no carrier (step 0) → c45
   d7/d8, c73 ladder exponent, c63 d4 occupancy, c62 G–α slope (both drifts null), c48 method residuals =
   NOT-YET-A-QUANTITY; c69 R_T/R_J = ALREADY-GOVERNED (established large-N derivation). This is the inconsistency the
   lead found at reading (m_p/m_e refused on the same gates α_G needs): the September census exempted its own rows.
   Forward predictions stay registered and are decided by data; they are not evidence for a census disposition.
2. cosmology present-epoch rows → EPOCH-DEPENDENT (first stop at step 1): c07, c08 (Λ-mixed bundle), c10, c15, c22,
   c42, c54, c71. Fixed-event components (z_eq, r_drag, Ω_DM/Ω_b, η) stay HISTORY. Refusal unchanged.
3. lepton anomalies a_e (c28), a_τ (c55) → ALREADY-GOVERNED by the card's explicit worked boundary (flagged before the
   lanes ran); a_μ stays HISTORY (hadronic inputs value-setting at measured precision).
4. single rows: c38 M_Pl → CONVENTION-BOUND (step 1.1 named combination; the frozen mapping's SCALE → HISTORY assumption
   conflicted with step 1.1); c59 ρ_Λ^(1/4) → HISTORY (free parameter); c74 Bekenstein 2π → ALREADY-GOVERNED; c17 A_L →
   ALREADY-GOVERNED (ratio to the model's own lensing; GR fixes 1).
5. kept against the majority: c01 3D Ising (card text conflict, printed ALREADY-GOVERNED), c23 Feigenbaum (dossier omitted
   physical carriers, printed ALREADY-GOVERNED).

## Consequences for PUB-2 (binding for lead R1 / WRITE3)
- census table = adjudicated disposition per row + three lane verdicts + historical disposition where faulted.
- abstract/summary: "73 of 74 (historical 61)"; "40 outputs of history (historical 44)"; own flagship = output of the
  electroweak history under the test until a mechanism bridges it; the only law candidate is the card's conditional CP
  example; agreement α 0.65 on 47 non-leak rows (descriptive).
- limit (state plainly): the yes-branch has no positive control (v3 controls planted six refusing dispositions); a
  73/74 refusal rate alone cannot separate "most measured numbers are shadows" from "the test rarely says yes" → v4
  disguised historical positive-control arm (THESIS_SECTIONS L1).
- v4 card fixes named by this arm: split bundles; nominal-reference rule; fixed-point/universality data computed
  non-perturbatively = STATIC; present-epoch amplitudes = EPOCH, fixed-event outputs = HISTORY; free-parameter rule's
  reopen path stated in the card.
