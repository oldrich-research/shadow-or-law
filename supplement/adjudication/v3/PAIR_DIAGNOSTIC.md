# PUB-2 v3 · two-lane diagnostic · 2026-10-07

Status: exploratory, post-seal, pre-third-lane; not primary v3 score. Frozen card/prompt/reference untouched. Third valid lane required by `PROTOCOL_V3.md` §§ Metrics, Order.

## Inputs

- `units/pub2-reliability-v3/lanes/G_verdicts.md` SHA-256 `e98f1aab34c8a4e712c63709221c5112d58060ce77b0a5542ef1b12e00d869db` (OpenAI lane; 66 complete).
- `units/pub2-reliability-v3/lanes/M_verdicts.md` SHA-256 `fee3a6b613893f9c7f631d0805293b9d2d60f798fe64441a03b3bfe69a000863` (Gemini lane; 66 complete).
- `units/pub2-reliability-v3/control_key_v3.json` SHA-256 `42bb40ab93312990fe67b3f5a0972b2286dea49744420a998e19ee81f03c0182` (lead only).
- `units/pub2-reliability-v3/items_v3.tsv` SHA-256 `0c353aca1a32de9a29524ff00aa09069d8a2cda69f55a73f5802c0b4a9256e5e` (item identities).
- Frozen scorer `i4e_score.py` SHA-256 `66a2c7580c30fd58116017fd278a38243e4b928fb498979de4ee3ea9824cc4a5`; exact `alpha()` reused for pair calculation.

## Measured

- 66/66 final labels in each lane; six controls: G 6/6, M 6/6; both valid under control gate.
- 60 foreign items: 21 same final label, 39 different; all 39 G `OUTPUT-OF-HISTORY` vs M `CONVENTION-BOUND`.
- Two-lane nominal Krippendorff α = `-230/1317` (≈ -0.1746), diagnostic only; not protocol primary result.
- Split items: q01,q02,q03,q04,q05,q10,q12,q13,q14,q16,q18,q19,q23,q24,q26,q27,q28,q29,q32,q36,q38,q40,q41,q45,q46,q47,q49,q50,q51,q52,q53,q54,q55,q58,q59,q61,q63,q64,q66.

## Decisive upper bound

For each G/M split item, any third category choice yields ≥2 of 3 coder-pair disagreements. Across 39 split items, ≥78 disagreements among 60×3=180 coder pairs; observed nominal disagreement `Do ≥ 78/180 = 13/30`. Chance disagreement `De ≤ 1` for the frozen nominal α formula. Therefore any three-valid-lane result has `α = 1 − Do/De ≤ 17/30 ≈ 0.5667`, below preregistered PASS-RELIABLE threshold 0.667. If the third lane fails controls, protocol requires same-family rerun; G/M splits persist and the bound applies to any valid replacement third lane. This does **not** determine whether final α is FAIL (<0.4) or INCONCLUSIVE (0.4–<0.667), nor validity vs sealed reference.

## Located split; no causal verdict yet

- Every split turns on step 1 (`PASS` vs `FAIL-UNIT`), before G reaches step 2 HISTORY; M gives generic unit-dependence reasons. Examples: q02 shielded helion gyromagnetic ratio (G nuclear-magneton ratio, M unit-bound), q05 Earth mass (G Earth/Sun ratio, M unit-bound), q14 meson mass (G meson/proton ratio, M unit-bound), q01 lanthanum density (G atomic-density ratio, M unit-bound).
- All 39 split items are dimensional. By name family: 14 elemental mean excitation energies, 11 elemental mass densities, 5 meson masses, 3 planetary masses, 3 bound neutron scattering lengths, 2 planetary diameters, 1 shielded gyromagnetic ratio. The first two NIST elemental families alone supply 25/39 splits; the pool/draw is clustered, not a balanced cross-domain sample. Generalize neither the observed split rate nor one family-specific remedy to all quantities.
- Card v3 § Step 1 explicitly permits recalled general physics and says `MAY` does not permit refusing a known standard natural form. M's generic unit-dependence reasons omit a proposed comparator even for q02's conventional nuclear magneton. G's choices are not automatically valid: q01's Bohr-volume/atomic-mass normalizer and some meson/planetary references may be plausible but nonunique. The tested unit of analysis can change when a grader replaces a dimensional target by a ratio; this choice itself needs a pre-fixed readout/comparator to become reproducible.
- Candidate causes: card rule A unclear about what qualifies as a standard natural ratio; or M insufficiently applied rule A; or both. Sealed reference itself marks some ratio cases as open-rule. No annotation or protocol rewrite before scoring/adjudication.
- Result limits the **claim of external repeatability of the written test**; does not independently validate/refute shadow ontology, numerical G formula, or the sealed reference labels.

## Next

1. Obtain independent valid third family under recorded route addendum, preserve exact sealed materials; compute full primary score.
2. Lead adjudicate every majority/reference disagreement and step-1 splits. Report v3 outcome without moving threshold.
3. For protocol-permitted INCONCLUSIVE branch only: locate ambiguity, reword as allowed, one fresh draw/re-run. For FAIL: publish as failed written procedure; any new construction is a separately preregistered experiment.
4. Paper and web: remove any claim that v3 established external runnability; report actual completed evidence and limitation.
