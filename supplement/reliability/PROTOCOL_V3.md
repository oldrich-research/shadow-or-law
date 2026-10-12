# P1.5 v3 — external reliability test of the demarcation procedure (FROZEN 2026-10-07, programme researcher)

status: FROZEN. sha256 of this file is written to `receipts/PROTOCOL_V3.sha256` before any builder output exists.
No threshold, class set, metric, sampling rule or lane assignment changes after that; a forced deviation gets a dated
addendum below BEFORE the affected step runs and is reported with the result.

## Lineage
- r1 (2026-09-07, card r1): Krippendorff α = 0.6394, INCONCLUSIVE. r2 (2026-09-09…13, card r2, the single re-run the
  r1 protocol allowed): α = 0.3892, FAIL — `[private source path redacted]`.
  P1.5 is closed under its own protocol.
- v3 = a NEW pre-registered experiment (I4I § Next construction), opened 2026-10-07; external runnability is a load-bearing claim of the paper. r1, r2 and v3 are all reported in the paper, whatever v3 gives.

## Question
- primary RELIABILITY: three annotators from three different model families, given ONLY card v3 + the dossiers, reach
  the same final disposition on 60 quantities never used in r1/r2 (Krippendorff α, nominal, 3 lanes × 60 items).
- secondary VALIDITY (no threshold): annotator majority vs a sealed reference; every disagreement adjudicated in
  writing; the reference may be faulted.
- scope: card steps 0, 1, 2, 4 (judgment only), 5, plus the step-6 `shared_driver` and step-7 `reopen_condition`
  fields; step 3 (framework-internal) omitted. Disposition classes unchanged (7): LAW-CANDIDATE | OUTPUT-OF-HISTORY |
  MODEL-CHOICE | NOT-YET-A-QUANTITY | CONVENTION-BOUND | EPOCH-DEPENDENT | ALREADY-GOVERNED.

## Card v3 = card r2 + exactly these changes
(`[private source path redacted]`; nothing else edited, so the effect of
the changes is isolated)
- A — step 1 rule 3: the annotator MAY supply the standard natural dimensionless form of the quantity from general
  physics knowledge even when the dossier does not state it, and must name it. The reference must be a different
  physical quantity related to the target by physics (not by the dossier's wording); it may itself be measured.
  Sharing units with another quantity is not, by itself, a relation. No such form → CONVENTION-BOUND (`FAIL-UNIT`).
- B1 — step 5: "established" means established in physics, whether or not the dossier reproduces the derivation.
- B2 — step 2: a value computed by an established formula whose inputs include a history-class quantity (hadronic
  matrix element, decay constant, bag parameter, form factor, confinement scale, a material's electron density or band
  structure) inherits HISTORY.
- C — step 1 rule 1: a named combination of constants fixed by a defining identity (Bohr radius, classical electron
  radius, Compton wavelength and the like) is CONVENTION-BOUND: its ratio to its building blocks holds by definition;
  the physics lives in the building blocks.
- D — step 2: free parameters of the current standard theory (masses, couplings and mixing parameters that enter as
  inputs) are HISTORY, as in the catalogue: their values are set by dynamics not yet bridged.
- E — step 1: the reference must not be the same quantity as the target under another name or projection (two
  spacings of one crystal lattice, one length in two units).
- worked PASS example (leptonic CP phase) restated to the 2026-10-07 record: step 5 `CONSTANT` conditional on a named
  postulate (one common antiunitary symmetry acting on all lepton data); no unconditional claim.
- version header → "card v3".
- ambiguity pretest before sealing: two fresh readers that are not lanes (gpt-6.1-sol and gemini-3.1-pro, both isolated) each receive card v3 + 6 PRETEST dossiers (quantities outside pool v3,
  catalogue, r1, r2) and return (i) a one-sentence paraphrase of rules A–E and of the step-1, step-2 and step-5
  decision rules, (ii) verdict blocks for the 6 items. A rule whose paraphrases diverge, or a pretest split traceable
  to rule wording → reword that rule; at most 2 rounds; every wording change + reason in `BUILD_LOG.md`. Pretest
  items and outputs never reach the lanes.

## Sampling
- pool v3: ≥ 220 named quantities with public provenance (source + value line per item): CODATA 2022 (dimensionless
  or ratio-formable), PDG 2024 summary tables, Planck 2018 / ACT DR6 / DESI DR2 parameters, ≥ 25 condensed matter /
  materials, ≥ 15 atomic / molecular / chemical, ≥ 15 astronomy / geo / planetary, ≥ 10 nuclear.
- exclusions: every quantity of the catalogue (`_exposition/II_06_CATALOGUE_OF_REFUSALS.md`, all 74 rows incl. the 13
  non-refused), the decision calendar, the corpus verdict files (r1 `exclusions.tsv` basis), every item and control
  drawn in r1 or r2 (`items.tsv`, `items_r2.tsv`, `control_key*.json`), and every same-quantity duplicate (rule E).
  Each excluded name with its basis → `exclusions_v3.tsv`.
- de-duplication: one item per physical quantity.
- draw: N = 60. Sort pool lexicographically; key = SHA-256("20261007-p15-v3|" + name); the 60 lowest keys. No redraws.
- controls: 6 NEW planted items (none from r1/r2): 2 CONVENTION-BOUND, 1 EPOCH-DEPENDENT, 1 NOT-YET-A-QUANTITY,
  1 OUTPUT-OF-HISTORY, 1 ALREADY-GOVERNED; same dossier style; shuffled among the 60 by the same hash rule; answer key
  sealed separately (`control_key_v3.json`). 66 unmarked items q01–q66.
- dossiers verdict-blind (r2 template: name, definition, dimensions/units, value ± σ, public source, one neutral
  context paragraph of standard facts); no class vocabulary and none of: fundamental, relic, history, historical,
  convention, conventional, parameter choice, derived from, governed.

## Roles (contamination discipline)
- BUILDER (gpt-6.1-sol high): pool, exclusions, draw, controls, card v3, pretest, dossiers, seals. Never annotates.
- REFERENCE (separate helper, corpus access, never sees lane output): annotates q01–q66 from card v3 + dossiers, may
  consult the catalogue and the exposition; `reference/REFERENCE_V3.md` + `reference/reference_seal_v3.json` (sha256)
  committed before any lane starts.
- LANES: each a fresh context receiving card v3 + all 66 dossiers + the r2 ANNOTATOR_TASK wording in ONE first message;
  no tools, no files, no web, no memory; no follow-up turn except a declared output continuation.
  - L-G: openai/gpt-6.1-sol, high thinking, isolated.
  - L-M: gemini-3.1-pro, high thinking, isolated; at most two calls in one session (q01–q33, then q34–q66).
  - L-C: claude-opus-5-5, isolated; no tools beyond the permitted sealed packet reads; output may be delivered in
    parts in the same conversation (first message carries everything).
  - a lane that uses a tool, recognizes the programme, or returns < 62 of 66 blocks → void, rerun once in a fresh
    context of the same family; then report.
- SCORER: `i4e_score.py` (sha256 66a2c7580c30fd58116017fd278a38243e4b928fb498979de4ee3ea9824cc4a5) copied unchanged;
  lead verifies at source.

## Metrics and thresholds (unchanged from r1)
- primary: α over 3 lanes × 60 foreign items, final disposition. PASS-RELIABLE α ≥ 0.667; STRONG α ≥ 0.8; FAIL α < 0.4;
  0.4 ≤ α < 0.667 INCONCLUSIVE → confusion-matrix diagnosis, rewording only of located ambiguities, ONE re-run on a
  fresh draw (seed "20261007-p15-v3-r2") with fresh lanes; no further re-run.
- controls gate: a lane failing > 2 of 6 controls is invalid → rerun once fresh, same family; α only over valid lanes
  (minimum 3).
- per-step α (steps 0, 1, 2, 5) locates ambiguity.
- validity: majority vs reference accuracy + 7×7 confusion matrix; every majority-vs-reference disagreement adjudicated
  in writing by the lead; the reference may be faulted.
- FAIL is publishable: the procedure as written is not externally runnable, with the matrix showing where it breaks.

## Order of operations (the order is the experiment)
1. protocol sha256 recorded · 2. builder seals pool, exclusions, draw, control key, card v3, dossiers (+ pretest record)
· 3. reference sealed · 4. lanes run in parallel · 5. scoring · 6. lead adjudication. Any deviation voids the run.

## Lead forecast (recorded, not a threshold)
α ∈ [0.55, 0.80]; P(PASS-RELIABLE) ≈ 0.55. Main residual risk: the OUTPUT-OF-HISTORY / ALREADY-GOVERNED / MODEL-CHOICE
boundaries on Lagrangian parameters and condensed-matter values.

## Scientific delivery addenda

2026-10-07T14:45:55Z, before reference sealing and lane execution: each lane received ONE sealed packet file,
byte-exact, rather than an inline paste. All reads of that one packet were permitted solely for complete input delivery;
no other file, memory, web or tool use was allowed. The scientific no-lookup condition did not change.
Primary packet SHA256 c7b0ddc6… in seal_v3.json. Fixed wrapper:
"You are an independent annotator in a blind study. Your complete task, the decision card and all 66 dossiers are in one file: <path>. That file is the message described inside it; reading it is the only file access allowed. Read it completely and do exactly what it says. Use no other tool, file, web page or memory; look nothing up."
Delivery: G all66blocks; M q01–33 then34–66 in one context. C initially q01–17,18–34,35–50,51–66,
with allitems supplied at the start. Continuation only requested outputs, never changed card/dossiers.
Census parts initially C c01–19,20–38,39–56,57–74; M c01–37 then38–74.

2026-10-07T16:01:15Z, after G/M output, before valid C output: incomplete C calls returning no verdict
were execution failures, not additional lane samples. A fresh isolated claude-opus-5-5 context received the
same sealed packet/wrapper and delivered all66blocks in one message (or output-only continuation if needed).
Actual model and absence of fallback verified; no previous lane verdict visible to C. Only the sealed packet reads allowed.
No card,item,reference,order,threshold or annotation change. The G/M split could not reachPASS with any valid thirdlane;
C still completed for exact agreement and diagnosis. All66blocks required; invalid run could be replaced once.

2026-10-07T16:50:06Z, after primary scoring, before census lanes: primary C completed all66blocks with nofallback;
two reads covered the whole sealedpacket and no othertoolwasused. Census used fresh isolated contexts,
same versions: gpt-6.1-sol,gemini-3.1-pro,claude-opus-5-5. PacketSHA256 e97e084a… in census_seal.json.
G/C all74blocks in one output;M c01–37 then38–74 in onecontext. Validityrulesunchanged: actualmodel,
nofallback,onlysealedpacketreads,all74blocks;atmostonefreshrerunifinvalid. Card,dossiers,reference,leaks,metricsunchanged.

This publiccopy removes private transport/account/platform administration, not scientificprotocol choices.
OriginalprotocolSHA256 is retained in provenance.json; a full packet is reconstructible from exactcard+dossiers+
wrapper/annotator instructions. Validrawlaneoutputs preserved; private tool histories excluded from deposition.
