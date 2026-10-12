# P1.5 v4 — external reliability test of the demarcation procedure + historical yes-branch arm (FROZEN 2026-10-08, lead g-decode)

status: FROZEN. sha256 of this file is written to `receipts/PROTOCOL_V4.sha256` before any draw, dossier, card v4 or
lane output exists. No threshold, class set, metric, sampling rule or lane assignment changes after that; a forced
deviation gets a dated addendum below BEFORE the affected step runs and is reported with the result.

## Lineage and why v4 exists
- r1 α = 0.6394 INCONCLUSIVE (2026-09-07); r2 α = 0.3892 FAIL (2026-09-13); v3 α = 0.0955 FAIL (2026-10-07,
  `../reliability/`, lead adjudication `../adjudication/ADJUDICATION_V3.md`).
- v3 cause (lead-verified): one lane (Google gemini-3.1-pro) refused 43 of 44 unit-bearing foreign items as
  CONVENTION-BOUND without forming the natural dimensionless form that card step 1.3 permits and, for a known standard
  form, asks for; the ambiguity pretest had flagged that step as not operationalized. The other two lanes agreed
  (pair α 0.927). Sampling concentration amplified the failure (53/60 reference OUTPUT-OF-HISTORY; 25/39 splits from two
  NIST table families).
- census arm (2026-10-07) named five further card fixes and one missing piece of evidence: the yes-branch has never
  been tested on numbers known to be law-fixed (a 73/74 refusal rate cannot by itself separate "most measured numbers
  are shadows" from "the test rarely says yes").
- founder 2026-10-08 07:4xZ: the corrected test runs now, before the PUB-2 release, and its result enters the paper.
- v4 = a NEW pre-registered experiment. r1, r2, v3 and v4 are all reported, whatever v4 gives.

## Questions
- primary RELIABILITY: three annotators from three model families, given ONLY card v4 + dossiers, reach the same final
  disposition on 60 quantities never used in r1/r2/v3 (Krippendorff α, nominal, 3 lanes × 60 items).
- secondary YES-BRANCH VALIDITY (historical arm, ground truth from the history of physics, not from any model): judged
  at the knowledge state of their time, do numbers that a later law fixed get LAW-CANDIDATE, and do numerical patterns
  whose non-law nature was visible at the time (formation history, epoch, unit convention) get refused?
- no reference annotation in v4: the v3 validity arm used a reference written by the builder's model family; v4 replaces
  it by the historical arm, whose key is history.

## Card v4 = card v3 + exactly these changes (`card_v4.md`, diff `card_v4.diff`)
- N (step 1, rule 3 → mandatory and checkable): for every target that carries units the annotator MUST attempt the
  standard natural dimensionless form and record it in a new field `natural_form:` (the ratio, the reference quantity,
  the physical relation that makes the reference natural) or `none — <the physical reason no relation exists>`;
  `FAIL-UNIT` on a unit-bearing target is valid only with such a `none — …` line; "it has units" is not a reason. A
  short table of standard natural references by domain is added (atomic, nuclear, particle, gravitating bodies,
  cosmology, materials). Dimensionless targets record `natural_form: as stated`.
- R (step 1, rule 1, nominal-reference rule): a value fixed by definition relative to a nominal reference is
  CONVENTION-BOUND; a measured ratio to a physical object chosen as reference by convention (a mass relative to a
  defined atom's mass) is not convention-bound for that reason: the convention fixes the unit, not the ratio.
- P (step 1, rule 2): a present-epoch amplitude (the current value of an evolving quantity) is EPOCH-DEPENDENT; a value
  frozen at a past event (an event redshift, a ratio frozen at decoupling) passes step 1 and is decided at step 2.
- U (step 2): fixed-point and universality data (critical exponents, universal amplitude ratios), even when computed
  non-perturbatively, are STATIC (properties of a fixed point, not outcomes of a contingent process); step 5 decides.
- D' (step 2, free-parameter rule): reopen path stated — the free inputs stay HISTORY until a structure or dynamics
  that derives them is proposed with a forward map; `reopen_condition` names that bridge.
- B (bundles): a dossier whose target bundles two or more quantities is judged on the first-named quantity; the
  others are named in the justification.
- F (step 5, CONSTANT operationalized; the yes-branch was never operationalized): a static, dimensionless, frame-free
  value that no admissible completion of current theory treats as an adjustable input and none accounts for is
  CONSTANT across F (nothing in F moves it); VARIES requires that the admissible family actually contains completions
  with different values.
- recording: field `natural_form` added after `step1`; consistency rule added for it; version header → card v4.
- nothing else edited.

## Sampling (primary arm)
- pool = pool v3 (381 named quantities with public provenance, `../reliability/pool_v3.tsv`,
  `quantity_data_v3.json`); exclusions = v3 exclusions + the 60 v3 draws + the 6 v3 controls → 249 eligible.
- stratified draw capping each source family (fixed quotas, total 60): CODATA-2022 10 · PDG-2024 12 · Planck-2018 3
  (all eligible) · materials 9 · atomic-molecular-chemical 8 · nuclear 8 · astronomy-geo-planetary 10.
- within a family: key = SHA-256("20261008-p15-v4|" + name); the lowest keys. No redraws.
- controls: the 6 v3 planted controls (dossiers and key unchanged; attention/validity gate as in v3: a lane missing > 2
  of 6 is invalid → one fresh rerun of the same family). Interleave the 66 by SHA-256("20261008-p15-v4|order|" + name);
  ids q01–q66.
- dossiers: the v3 template and generator unchanged (`make_dossiers_v3.py` logic, same vocabulary scan); confidence
  `med` as in v3.

## Historical arm (secondary)
- 11 dossiers h01–h11, written by the lead before any lane runs, sealed with a separate key `hist_key_v4.json`:
  6 positives (a dimensionless number measured before the law that later fixed it: combining gas volumes, the
  period–orbit-size exponent, a hydrogen line-wavelength ratio, an atomic magnetic splitting factor, the nucleon
  closed-shell counts, the electron magnetic-moment anomaly) and 5 negatives (a number whose non-law nature was visible
  at the time: planetary spacing growth factor, Moon/Sun apparent-diameter ratio, free-fall acceleration in metric units
  vs π², solar days per year, solar-cycle length vs the largest planet's period).
- each dossier: neutral name (no eponyms, no dates), carrier and readout, value ± uncertainty as measured then, and a
  `knowledge_state` paragraph (what physics knew then). Annotators judge AS OF that knowledge state and add a field
  `recognized: no | yes — <what they recognize>`.
- expected: positives → LAW-CANDIDATE; negatives → any disposition other than LAW-CANDIDATE (the key also names the
  lead's best class; not scored).
- metric: S = number of the 6 positives whose lane-majority disposition is LAW-CANDIDATE; F = number of the 5 negatives
  whose lane-majority disposition is LAW-CANDIDATE. YES-BRANCH WORKS: S ≥ 5 and F ≤ 1 · PARTIAL: S ∈ {3, 4} and F ≤ 1
  · FAILS: otherwise. Per-lane S and F, and S and F over items no lane recognized, reported beside it.
- disclosed limit: the cases are famous; annotators may recognize them and judge with hindsight. The `recognized`
  field measures that; it does not remove it.

## Roles
- BUILDER = lead (Anthropic claude-opus-5-5): protocol, card v4, draw (mechanical), dossiers (mechanical template;
  historical dossiers hand-written), keys, seal. Never annotates. Overlap disclosed: lane L-C is the builder's family;
  the card was written inside the programme (OpenAI and Anthropic models).
- PRETEST (wording only, before the final seal): one fresh isolated reader per family that failed or flagged step 1 in
  v3 — gemini-3.1-pro (provider client, isolated) and gpt-6.1-sol (fresh isolated context) — on the six v3 pretest dossiers
  p01–p06 (outside every pool): a one-sentence paraphrase of rules N, R, P, U, D', B, F and the step-1/2/5 decision
  rules + verdict blocks with `natural_form`. At most ONE rewording round of a rule whose paraphrases diverge or whose
  `natural_form` use fails; every change + reason in `BUILD_LOG.md`. Pretest material never reaches the lanes.
- LANES (each a fresh context, ONE first message, one sealed file read-only, no tools beyond reading that file, no
  web, no memory; output-continuation only):
  - L-G: openai/gpt-6.1-sol, thinking high, fresh isolated context.
  - L-M: gemini-3.1-pro, thinking high, provider client isolated, context_files = the sealed prompt; primary arm in two calls of one
    session (q01–q33, then q34–q66 + completion line).
  - L-C: anthropic/claude-opus-5-5 through the Gateway subscription pool (v3 Addendum 2 route), fresh isolated context.
  - each family runs the primary arm and, in a separate fresh context, the historical arm (6 lane runs).
  - validity per lane run (v3 Addenda 1–2): actual model and no fallback; tool history = reads of the one sealed path
    only; all blocks present; else void → one fresh rerun of the same family, reported.
- SCORER: Krippendorff α and majority from the unchanged `i4e_score.py` functions (sha256 66a2c758…); driver
  `scoring/v4_run.py` (format normalization as v3, plus `natural_form` and `recognized`).
- ADJUDICATOR = lead; every primary-arm item without a 3/3 agreement is read and classed (lane error · card ambiguity ·
  dossier defect) in writing; nothing re-labels a lane.

## Metrics and thresholds
- primary (unchanged from r1/v3): α over the valid lanes × 60 foreign items, final disposition. STRONG α ≥ 0.8;
  PASS-RELIABLE α ≥ 0.667; INCONCLUSIVE 0.4 ≤ α < 0.667 → confusion diagnosis, rewording only of located ambiguities,
  ONE re-run on a fresh stratified draw (seed "20261008-p15-v4-r2") with fresh lanes; FAIL α < 0.4.
- per-step α (steps 0, 1, 2, 5); pairwise α; per-lane disposition distribution.
- natural-form provision (descriptive): per lane, the share of unit-bearing foreign items with a `natural_form` that
  names a ratio, and the share of FAIL-UNIT on unit-bearing items without a `none — <reason>` line.
- historical arm: S, F, verdict as above.
- every result is publishable; a FAIL is reported first, cause second.

## Order of operations (the order is the experiment)
1. protocol sha256 recorded · 2. draw, primary dossiers, controls, historical dossiers + key sealed · 3. pretest on the
card wording (≤ 1 rewording round) · 4. card v4 + lane prompts sealed · 5. six lane runs in parallel · 6. scoring ·
7. lead adjudication. Any deviation without an addendum voids the run.

## Lead forecast (recorded, not a threshold)
- primary α ∈ [0.55, 0.85]; P(PASS-RELIABLE) ≈ 0.6. Main risks: the atomic-unit CODATA rows (CONVENTION-BOUND by
  rule C vs a natural ratio), electroweak asymmetries and couplings (inherit HISTORY from a free mixing angle vs
  ALREADY-GOVERNED), planetary temperatures and Planck rows (EPOCH vs HISTORY).
- historical arm: S ∈ [4, 6], F ∈ [0, 1]; most at risk: the closed-shell counts (card's bound-state HISTORY rule) and
  the moment anomaly (hindsight ALREADY-GOVERNED).

## Addenda
(none at freeze)
