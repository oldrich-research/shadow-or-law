# Annotation task — measurements at past states of knowledge

You are an independent annotator. This single message contains exactly two inputs:
the complete card v4 (the decision procedure — read it fully first) and dossiers h01..h11.

Each dossier describes a measurement as it stood at a past state of knowledge, given in its section
"Knowledge state". Run the card AS OF that state: treat the physics described there, and only that, as
"current theory", as "established" and as "everything you already know"; treat every later development as
unknown, even if you recognize the case. Names, places and dates are withheld on purpose.

Rules (binding): use ONLY this message, subject to the card's permission (step 1, rule 3) to recall physics
for a natural dimensionless form — recall only physics that belongs to the stated knowledge state. Do not read
files on any machine, do not browse the web, do not consult tools, memory, other documents or programme
context. If a dossier lacks a fact you need, say so in the justification and decide on what it contains.

Task: run the card's procedure on every dossier h01..h11 in order. Reply with one block per item, exactly in
the card's "Recording your verdict" format (item: hNN), with one extra last field in every block:
recognized: no | yes — <what you recognize>
Every item gets exactly one disposition; no blank fields; no skipped items.
After all 11 blocks, print the single line
ANNOTATION-COMPLETE

No file output or commits. No extra first turn or follow-up discussion. If output stops early, the only
allowed follow-up is an output-continuation sentence naming the first missing item.

# Procedure card — what can a measured quantity tell you?

```text
version: card v4 (P1.5 external-test; frozen protocol 2026-10-08; seal date set by the builder)
what this is: a fixed, self-contained decision procedure for sorting a measured physical quantity into
              one of seven dispositions. Extracted from a longer methods document; nothing outside this
              card is needed to run it.
what you receive: this card + a set of dossiers, one per quantity (name, definition, units, a
              representative value with uncertainty and public source, one paragraph of standard context).
what you return: for every dossier, the record described in "Recording your verdict" at the end.
rules of engagement: use only the dossier and this card. Do not look anything up. If a dossier lacks a
              fact you need, say so in the justification and decide on what it contains. Give every item
              exactly one disposition. Do not skip items. If a dossier's target bundles two or more
              quantities, judge the first-named one and name the others in the justification.
```

## What the procedure is for

A precision measurement can be one of several quite different things, and the difference is usually not
visible from inside the experiment. The quantity may be one that the structure of the world could force to
its value. It may be a real, well-defined, worth-measuring number that is nonetheless the endpoint of some
process, so that no amount of extra digits will ever explain *why* it has that value. It may be a number
that varies freely across the versions of current theory that fit everything known, so measuring it only
tells you which version you are in. It may be an expression that cannot be measured at all yet. Or the
question may belong somewhere else entirely: the value may encode a human choice, may depend on when you
ask, or may already be fixed by an established theorem.

The procedure below separates these cases by a fixed sequence of questions. It is meant to be run
*before* deciding what a measurement would establish, not after.

**One thing a refusal does not mean.** Sorting a quantity away from the "could be forced" disposition never
says the quantity is unimportant, incalculable or not worth measuring. Most of the quantities that fail are
fully computable in their own terms and are among the best-measured numbers in physics. What a refusal
withholds is only the *reason* the value is that value; it is a statement about what further precision can
and cannot deliver.

## The seven dispositions (closed set — every item gets exactly one)

**LAW-CANDIDATE.** The quantity has a carrier and a readout, is dimensionless and frame-independent, is
static rather than the endpoint of a dynamical process, and — within the family of admissible completions of
current theory — is either constant across that family or singled out by a principle established
independently and before the data. It could, in principle, be forced by the structure of the world by a
relation that is *not yet* established. A measurement of it can establish that a forced relation holds or
fails, to the precision reached. If the selecting principle is already an established theorem of existing
theory, the disposition is ALREADY-GOVERNED instead.

**OUTPUT-OF-HISTORY.** A dimensionless, frame-independent, well-measured number that is nonetheless the
endpoint of dynamics: a process that had to be run (recombination, freeze-out, growth, accretion, a
transition) or a dynamical computation that had to be solved (confinement, symmetry breaking, a bound state,
a phase). It is a dynamics observable: real physics, worth measuring precisely, and not a candidate for a
forced value. No static structural expression should be sought for it, and no further precision on it will
supply the reason it came out at this value rather than another.

**MODEL-CHOICE.** A number that varies freely across the admissible completions of current theory, with
nothing established selecting a point. Measuring it tells you which member of your admissible family you are
in, not anything about nature independent of that family. A genuinely different mainstream theory class
predicts a genuinely different value, and nothing pre-committed picks one.

**NOT-YET-A-QUANTITY.** An expression with no carrier (no physical system that bears it) or no readout (no
operation that measures it), or one whose claimed structure demonstrably does not exist on its carrier. It
cannot be measured until the missing half is built; no measurement of it can succeed or fail. Pure
mathematical constants belong here as well: there is no empirical degree of freedom for them to be a
measurement *of*, and matching digits is not evidence of anything.

**CONVENTION-BOUND.** The value encodes a human choice — a unit system, a defining constant, a reference
level, a normalisation, a display convention — so there is nothing for a law to fix. Exact values fixed by
definition and identities that are tautologies by construction live here. This refuses the practice of
counting a convention as a discovery; it does not refuse the physics the convention is used to describe.

**EPOCH-DEPENDENT.** Well defined, but its value depends on when — or from where — you ask: a reading of a
running clock, an odometer that is larger tomorrow than today, a number that changes with cosmic epoch,
observer frame or chosen time-slice. Any simple number it matches is one it happened to transit.

**ALREADY-GOVERNED.** Real and derived, but by a different, established piece of theory: a theorem bound, a
universality-class constant, a fixed-point property, a symmetry consequence, a textbook derivation from
quantities already in hand. A second derivation would be redundant rather than confirmatory. The distinction
from LAW-CANDIDATE is that here the reason is already known; eligibility relative to OUTPUT-OF-HISTORY is decided
exclusively by the boundary stated in step 2.

Where each disposition is reached:

| Step | Question | Disposition if the quantity stops here |
|---|---|---|
| 0 | carrier and readout? | NOT-YET-A-QUANTITY |
| 1 | dimensionless and frame-independent? | CONVENTION-BOUND or EPOCH-DEPENDENT |
| 2 | static, or the output of a history? | OUTPUT-OF-HISTORY |
| 3 | (omitted in this test) | — |
| 4 | is a rational-density null required, vacuous, or not applicable? | (a judgment, not a stop) |
| 5 | constant, selected, or free on the fiber? | LAW-CANDIDATE, ALREADY-GOVERNED or MODEL-CHOICE |
| 6 | if it survives: pre-register before looking | — |
| 7 | if it fails: the refusal is a result | — |

The steps are run in order. The disposition is decided by the first step at which the quantity stops;
record later steps as NOT-REACHED. Where a step has more than one way to stop, record which.

## Step 0 — Does the quantity have a carrier and a readout?

Name the physical system that carries the quantity and the operation that reads it out. If either is
missing, the expression is not yet a quantity, and no measurement of it can succeed or fail. Build the
missing half first.

This is placed first because it is the cheapest test and it disposes of a surprising amount. The programme
that wrote this procedure applied it to itself: several internally attractive invariants turned out to have
no physical carrier, and were therefore not predictions being ignored by experimentalists — they were not
yet quantities. A subtler failure is a carrier that exists while the specific structure claimed to live on it
does not (an exact finite computation can show the claimed symmetry is absent); that also stops here.

Verdict tokens: `PASS` (carrier and readout both named) · `FAIL` (either missing, or claimed structure
absent).

## Step 1 — Is it dimensionless, and is it frame-independent?

A quantity carrying units is referred to a convention: a unit system, a defining constant, a display
normalisation. The *number* on the dossier is then partly a human choice. Ask first whether the physics
itself supplies a natural dimensionless form of the same quantity — a ratio to a reference of the same kind
that the theory, not the metrologist, provides (a mass ratio, a coupling, a pure number, a ratio of two
scales the physics relates). If it does, run the remaining steps on that form and say which form you used.
Decide step 1 in this order:

1. A defined unit, a nominal reference value, or an identity that is a tautology by construction stops here as
   CONVENTION-BOUND (`FAIL-UNIT`). A named combination of constants fixed by a defining identity
   (Bohr radius, classical electron radius, Compton wavelength and the like) also stops here:
   its ratio to its building blocks holds by definition; the physics lives in the building blocks.
   A value that is exact by definition relative to a nominal reference stops here. A measured ratio to a
   physical object that a convention chose as the reference (a mass relative to the mass of a defined atom, a
   frequency relative to a defined transition) does NOT stop here for that reason: the convention fixes the
   unit, not the ratio. A stop under this rule records `natural_form: none — rule 1: <defined unit, nominal
   reference, tautology or named combination>`.
2. Otherwise, a documented change of the target with epoch, observer frame or time-slice stops here as
   EPOCH-DEPENDENT (`FAIL-EPOCH`); coordinate corrections used to infer a fixed relational target are part of its
   readout, not a change of the target. A present-epoch amplitude — today's value of a quantity that evolves
   (a present density fraction, a present temperature, a present expansion or orbital rate) — stops here. A value
   frozen at a past event (the redshift of an event, a ratio fixed at a decoupling) is not epoch-dependent: it
   passes step 1 and is decided at step 2.
3. Otherwise, a target that is dimensionless as stated passes (`natural_form: as stated`). For a target that
   carries units you MUST attempt its standard natural dimensionless form from general physics knowledge, even
   when the dossier does not state it (this permission to recall physics overrides the dossier-only rule for this
   purpose), and record it in the field `natural_form:` as the ratio, the reference quantity, and the physical
   relation that makes that reference natural. The reference must be a different physical quantity related to the
   target by physics, not by the dossier wording; it may itself be measured. Sharing units is not, by itself, a
   relation. The reference must not be the same quantity under another name or projection (two spacings of one
   crystal lattice, one length in two units). Then run the remaining steps on that form. Only if no such form
   exists do you record `natural_form: none — <the physical reason no relation exists>` and stop as
   CONVENTION-BOUND (`FAIL-UNIT`). That a number carries units, or that its numerical value depends on the unit
   system, is NOT such a reason: every unit-bearing quantity has that property, and this rule exists to remove it.

Standard natural references (use the one that belongs to the physics that sets the quantity; another admissible
one is fine if you name the relation):

| Domain | Natural references |
|---|---|
| atomic, molecular, chemical, materials | atomic units (electron mass, Bohr radius, Hartree energy, Bohr magneton); the atomic mass unit or the atom's own mass for masses and densities |
| nuclear | nucleon mass, nuclear magneton, the nucleon size scale (nucleon Compton wavelength), binding energy per nucleon |
| particle physics | another mass, width or coupling of the same theory (a hadron mass over the proton mass; a width over its particle's mass) |
| gravitating bodies, planets, stars | a mass, size or period of the same system (planet over star mass, radius over orbit radius), or the number of nucleons it contains |
| cosmology | density fractions; ratios to the Hubble scale or to the radiation temperature — then apply rule 2 |
| temperatures | the energy scale that sets them (thermal energy over a binding, radiative or orbital energy of the same system) |

A quantity that changes with the observer's frame, epoch, or chosen time-slice is a projection by
construction — that is what a projection is. If the quantity (or its natural dimensionless form) drifts with
cosmic time, with the observer's motion, or with the choice of reference moment, it stops here as
EPOCH-DEPENDENT.

Worked failures from the originating programme's catalogue (none of these appears in your dossier set):

- the present cosmic-microwave-background temperature in kelvin — unit-laden; its dimensionless anchored
  ratios then drift with epoch;
- the Hubble rate times the Planck time — an epoch-defined reading of the Hubble clock, not a constant;
- the age of the universe in Planck times — an odometer, larger tomorrow than today;
- the Hubble rate times the cosmic age — passes through 2/3 in matter domination, ≈0.95 now, and exceeds 1
  later. Any rational you match it to is a number it happened to transit.

This step alone removes a large fraction of the numbers that get called fundamental in popular accounts.

Verdict tokens: `PASS` (dimensionless and frame-independent, either as stated or after forming the natural
dimensionless version — name it in `natural_form`) · `FAIL-UNIT` (nothing beyond the reference choice; on a
unit-bearing target only with `natural_form: none — <reason>`) · `FAIL-EPOCH` (drifts with epoch, frame or
time-slice).

## Step 2 — Is it static, or is it the output of a history?

A dimensionless, frame-independent number can still be the endpoint of a dynamical history: recombination,
baryogenesis, structure growth, reionization. Such a number is a dynamics observable. It is real physics and
worth measuring precisely; it is not a candidate law value, and no static structural expression should be
sought for it.

The test: is the value set by a static structural fact (a symmetry, a count, an exact theorem), or does it
emerge only once dynamics have been run — a process with initial conditions and a path, or a computation
that solves for a bound state, a broken phase, a transition, a confined spectrum? STATIC includes an established
closed-form or perturbative prediction from independently available inputs, with no contingent initial condition
and no fitting of the target value; an analytic atomic spectrum with perturbative corrections is STATIC. This rule
takes priority over the general dynamical-computation examples above. HISTORY requires a contingent process
outcome, or a separate variational or non-perturbative solution for a bound state, a confined spectrum, a broken
phase or a transition. The absence of a known derivation does not by itself make a quantity HISTORY.
Fixed-point and universality data — critical exponents, universal amplitude ratios — are STATIC even when they are
computed non-perturbatively: they are properties of a fixed point, not outcomes of a contingent process; step 5
decides whether an established universality class accounts for them.

A value computed by an established formula whose inputs include a history-class quantity (hadronic
matrix element, decay constant, bag parameter, form factor, confinement scale, a material's electron
density or band structure) inherits HISTORY when that input sets the target value; an input that
cancels exactly from the target is not value-setting. Free parameters of the current standard theory — masses,
couplings and mixing parameters that enter as inputs — are HISTORY: their values are set by dynamics
not yet bridged. They stay HISTORY until a structure or dynamics that derives them is proposed with a forward map;
name that bridge in `reopen_condition`. These two rules take priority over the STATIC closed-form/perturbative rule
above.

Worked failures from the originating programme's catalogue (cosmological): the baryon-to-photon ratio
(baryogenesis plus nucleosynthesis dynamics); the acoustic scale, which is a ratio of a sound horizon to an
angular distance and therefore an output of recombination plus background geometry; the equality redshift;
the optical depth; the damping scale; the growth amplitude; the sound horizon. The same catalogue applied the
same reason to particle and nuclear quantities that emerge from confinement, electroweak breaking or flavour
dynamics: the proton-to-electron mass ratio, nuclear binding energies
and moments, the quark mass ratios, the mixing angles. None of these appears in your dossier set.

Worked boundary: a lepton anomalous magnetic moment predicted by an established perturbative derivation from
independently available inputs is STATIC at step 2 and SELECTED-ESTABLISHED → ALREADY-GOVERNED at step 5;
evaluating that derivation is not a contingent history.

Verdict tokens: `STATIC` · `HISTORY`.

## Step 3

Framework-internal step omitted from this test.

## Step 4 — The rational-density null: required, vacuous, or not applicable?

Any sufficiently precise number is close to some simple rational and to some power of a small constant.
Before a near-match is allowed to mean anything, the originating programme requires a null test:

1. Count how many rationals with denominator up to a declared bound fall within one standard deviation of
   the measured value.
2. Compare that count with the Farey expectation for that interval and bound.
3. If the observed count matches the expectation, the match is noise, and no amount of aesthetic appeal
   changes that.
4. Run the same search against a deliberately wrong target — a sham — and check that it does not also
   succeed.

**In this test you do not run the computation.** You record a judgment about whether it is needed:

- `REQUIRED` — the case for this quantity being structurally fixed rests, or would rest, on its numerical
  closeness to a simple expression (a rational, a power of a small constant, a combination of a few such).
  A near-match may count only after the null above has been run and passed.
- `VACUOUS` — the claim on the table is that the value is *exactly* a specific discrete value (an exact
  zero, an exact integer or rational fixed by a counting or symmetry argument). A discretely forced value
  has no near-match to explain away, so the null has nothing to test. When step 4 is vacuous the quantity
  is in better shape than when it passes, and a procedure reporting "passed step 4" for both would be
  hiding the difference.
- `NOT-APPLICABLE` — the quantity already stopped at step 0, 1 or 2, or no candidate simple expression is
  on the table at all.

For calibration, the programme published four of its own nulls, all on quantities excluded from your set.
Observed one-sigma rational hits with denominator ≤ 500, against the Farey expectation:

| Quantity | Observed hits | Farey expectation | Sham control |
|---|---|---|---|
| acoustic scale (×100) | 45 | ~45.6 | p(count ≥ obs) = 0.72 |
| scalar spectral index | 637 | ~638 | best hit 2/57 = the ordinary slow-roll form |
| cosmic age in Planck times | 1103 | ~1099.0 | sham mean 1100.9, p = 0.38 |
| matter density fraction | 1073 | ~1063.9 | sham mean 1065.8, p = 0.078 |

All four are noise. The fourth is the instructive one: it sits at p = 0.078, close enough to conventional
significance to be tempting, and it was still refused — a candidate that nearly clears its own null is not a
hit, and refusing it is what a pre-registered threshold is for. This step is the difference between a
programme and numerology.

## Step 5 — The Fiber Gate

Fix three things explicitly: the postulates you are assuming, the carrier-and-readout dictionary, and the
class of admissible channels. Let **F** be the family of admissible completions consistent with everything
you already know — the fiber over the known invariants. Then for the quantity X:

- if X is **constant across F**, X is a prediction → `CONSTANT` → LAW-CANDIDATE;
- if X is **singled out within F by a principle established independently and before the data**, X is a
  derived prediction — declare it and freeze it:
  - if that principle is a *new* or not-yet-established one → `SELECTED-NEW` → LAW-CANDIDATE;
  - if that principle is an *already established* theorem or theory that fully accounts for the value (a
    bound, a universality class, a symmetry consequence, a standard derivation from quantities in hand) →
    `SELECTED-ESTABLISHED` → ALREADY-GOVERNED;
- if X **varies across F and nothing selects a point**, X is a model choice → `VARIES` → MODEL-CHOICE.
  Measuring it constrains your model, not nature.

Here "established" means established in physics, whether or not the dossier reproduces the derivation.
If an established theorem fully accounts for the value, SELECTED-ESTABLISHED takes precedence
over CONSTANT; constancy alone does not turn an already explained value into a new prediction.

What CONSTANT means when no theory addresses the value: a static, dimensionless, frame-free value that no
admissible completion of current theory treats as an adjustable input, and that none accounts for, is CONSTANT
across F — nothing in F moves it. VARIES requires that the admissible family actually contains completions with
different values of X.

Dependence on a named postulate is an orthogonal axis. Any of these verdicts may additionally be
conditional on a postulate, and must say which.

The gate puts the carrier/readout test (step 0) first and lifts postulate-dependence onto its own axis for a
reason: an earlier form of the same test could classify a quantity that was never well defined to begin
with.

**Ten moves that look like a derivation and are not** — the worked-failure list for this step, ruled out in
advance. A proposed selection of X that rests on any of them is not a selection, and X does not pass:

1. a representation "predicted" because it appears in a decomposition;
2. a decomposable invariant realised as one connected word;
3. absolute depths read off dimensions or Casimirs;
4. exact laws inferred from parts-per-million proximity in scheme-dependent quantities;
5. amplitude/probability/record level-mixing without a full instrument;
6. first-order tangents promoted to finite laws without composition;
7. global charges copied onto local carriers;
8. gauge generators treated as direct observables;
9. picking a point in a cone because the ontology likes it;
10. fitting a determinant and calling its spectrum derived.

Several of these are mistakes made routinely well outside the programme that listed them — treating a global
charge as observable on a local carrier, promoting a gauge generator to an observable, reading a number as
predicted off a decomposition it merely appears in — which makes the list the most directly transferable
part of this card.

Verdict tokens: `CONSTANT` · `SELECTED-NEW` · `SELECTED-ESTABLISHED` · `VARIES` · `NOT-REACHED`.

## The anti-narrative clause — travels with the gate, not optional

A failed forward-built map must be *rejected*, never re-described as evidence of lossiness, emergence,
actualization or projection — otherwise the ontology becomes an empty renaming scheme. Failures are
consistent with a lossy projection; they become *evidence* for one only through a forward-built map that
predicts structure transverse to the fiber which is then confirmed.

In practice: if you propose that X is fixed by principle P and the map from P to X fails, reject the
proposal. Do not re-describe the failure as a discovery about the deeper nature of X. A refusal at any step
is a refusal, not a finding about what X "really is". Any framework whose central image is that the measured
world is an image of something else has a standing temptation to read every one of its own failures as
further proof of that image; the clause forbids it, and any reader adopting this procedure should write the
same clause into their own version.

The practical force of this is unpleasant and useful in equal measure: it converts a large class of
"predictions" into disclosures about the predictor.

## Step 6 — If it survives, pre-register before looking

Freeze the value, the comparison threshold, and the condition that would kill it, before the data are
inspected. Declare independence honestly: an algebraic restatement of a quantity you have already used is
not a second confirmation. Record the look-elsewhere effect at the time of freezing, not afterwards.

**The worked independence failure.** The originating programme carried two inflationary quantities, the
scalar spectral index `n_s = 1 − 2/N` and the tensor-to-scalar ratio `r = 12/N²`, on separate rows with
separate experiments and separate decision dates, which made them look like two chances to be right. They
are functions of the same free parameter `N`. There is one quantity there, not two. The failure is
invisible from inside either measurement — the two experiments are genuinely different, in different bands,
with unrelated systematics — because the dependence lives in the theory, not the apparatus. Before listing
two quantities as independent tests, write down what they are functions of; if the parameter sets overlap,
say so on both entries.

For this test: in the `shared_driver` field, name any other dossier in your set that is a function of the
same underlying quantity as this one (or `none`).

## Step 7 — If it fails, the refusal is still a result

A quantity that cannot carry a law, with the reason it cannot and the condition under which the question
could reopen, is a publishable finding. The accumulated set of them is a map of where not to dig. For this
test: where you can, state in one clause the condition under which the question could reopen
(`reopen_condition`); otherwise write `none stated`.

## Two quantities walked all the way through (from the originating programme; both excluded from your set)

**A quantity that passes: the leptonic CP-violating phase.**

| Step | Question | Verdict |
|---|---|---|
| 0 | carrier and readout? | PASS — the leptonic mixing matrix; read out as a CP asymmetry in long-baseline oscillation |
| 1 | dimensionless, frame-independent? | PASS — a phase, and the rephasing-invariant built from it is by construction frame-free |
| 2 | static, or output of a history? | STATIC — the proposed exact CP-real constraint under premise X below, not a claim to fix a free measured mixing input |
| 3 | — | omitted from this test |
| 4 | density null? | VACUOUS — under premise X the invariant is *exactly* zero by CP symmetry; there is no near-match to explain away |
| 5 | Fiber Gate | CONSTANT, conditional on premise X: one common antiunitary symmetry on all lepton operators, spurions/vacuum, light-mode reduction, charged-current overlap and matching, with invariant vacuum. J = 0 and δ_CP ∈ {0°,180°} follow only under that CP-real structure; no unconditional J = 0 claim |
| 6 | pre-register | conditional target registered; CP violation established in the same lepton data rejects premise X as implemented, not the unconditional framework |
| 7 | — | not reached; it survived → LAW-CANDIDATE |

**A quantity that fails at step 5: a normalisation factor inside the programme's own flagship formula.**
The formula factorises into powers and a normalisation. The powers pass. The normalisation — a rational
times an exponential of the fine-structure constant — walks to step 5 and stops.

| Step | Verdict |
|---|---|
| 0 | PASS — same carrier and readout as the formula itself |
| 1 | PASS — dimensionless, frame-independent |
| 2 | STATIC — not a history |
| 3 | omitted from this test |
| 4 | NOT-APPLICABLE as a near-match question — the constants are computed invariants, not fitted rationals |
| **5** | **VARIES — MODEL-CHOICE.** No single object produces the assembled form: the two pieces are opposite limits of different objects, and two independent derivation attempts failed. The constants are real and separately motivated; the functional form that assembles them is a choice. |

Why this example is here rather than a tidier one: a near-miss at step 5 looks, from outside, exactly like a
success — real constants, right answer, parts-per-million agreement. The only thing separating it from a
prediction is a question about whether anything selects the form, which is invisible unless you ask it.

## The output, in the form an experimentalist can use

| Disposition | What the measurement can establish | What it cannot |
|---|---|---|
| LAW-CANDIDATE | that a forced relation holds or fails, to the precision reached | — |
| OUTPUT-OF-HISTORY | the value of a real derived quantity; consistency of a history | a fundamental constant, at any precision |
| MODEL-CHOICE | which member of your admissible family you are in | anything about nature independent of that family |
| NOT-YET-A-QUANTITY | nothing | anything, until a carrier and readout exist |
| CONVENTION-BOUND | that the convention is being applied consistently | anything a law could fix |
| EPOCH-DEPENDENT | the present reading of a running quantity | a constant |
| ALREADY-GOVERNED | that an established theorem continues to hold | a new law; a second derivation adds nothing |

## Why this procedure stands on its own

Steps 0, 1, 2, 4, 5, 6 and 7 require no particular physical framework. The Fiber Gate is a statement about
any theory that compresses many degrees of freedom into a few invariants and then wants to make claims about
the pre-image. Any underdetermined theory — string constructions, effective field theories with unfixed
coefficients, cosmological parameterisations, machine-learned models — has a fiber, and the same verdicts
apply to it. A reader may reject every physical claim of the programme that wrote this card and still be
left with a criterion that does work in their own field.

## Recording your verdict

One block per dossier, in dossier order, using exactly these keys and tokens:

```text
item: qNN
step0: PASS | FAIL
step1: PASS | FAIL-UNIT | FAIL-EPOCH | NOT-REACHED
natural_form: as stated | <ratio; reference quantity; physical relation> | none — <physical reason> | none — rule 1: <which> | NOT-REACHED
step2: STATIC | HISTORY | NOT-REACHED
step4: REQUIRED | VACUOUS | NOT-APPLICABLE
step5: CONSTANT | SELECTED-NEW | SELECTED-ESTABLISHED | VARIES | NOT-REACHED
disposition: LAW-CANDIDATE | OUTPUT-OF-HISTORY | MODEL-CHOICE | NOT-YET-A-QUANTITY | CONVENTION-BOUND | EPOCH-DEPENDENT | ALREADY-GOVERNED
confidence: high | med | low
shared_driver: <other item id(s) or none>
reopen_condition: <one clause or "none stated">
justification: <one sentence>
```

Consistency rules: a `FAIL` at step 0 → disposition NOT-YET-A-QUANTITY and later steps NOT-REACHED (step 4
NOT-APPLICABLE). `FAIL-UNIT` → CONVENTION-BOUND; `FAIL-EPOCH` → EPOCH-DEPENDENT. `HISTORY` →
OUTPUT-OF-HISTORY. `CONSTANT` or `SELECTED-NEW` → LAW-CANDIDATE; `SELECTED-ESTABLISHED` →
ALREADY-GOVERNED; `VARIES` → MODEL-CHOICE. `natural_form`: `as stated` for a dimensionless target; for a
unit-bearing target the ratio + reference + relation you used, or `none — <physical reason>` / `none — rule 1:
<which>` (the only ways a unit-bearing target may get `FAIL-UNIT`); `NOT-REACHED` after a step-0 `FAIL`, and
after a `FAIL-EPOCH` stop unless you formed a natural form. Do not leave any field blank.

# h01 — volume ratio in which the lightest gas and the gas that supports burning combine

```text
name: volume ratio in which the lightest gas and the gas that supports burning combine
definition: Volume of the lightest known gas divided by the volume of the gas that supports combustion when the two combine completely into water vapour, both measured at the same temperature and pressure.
carrier_readout: the two gases reacting in a closed graduated tube ignited by a spark; readout = the gas volumes consumed, read on the tube scale
dimensions_units: dimensionless
value: 1.9989
sigma: about 0.003 (tube readings; not stated precisely)
source: measurement as published at the knowledge state described below (names and dates withheld)
value_confidence: med
```

## Knowledge state (judge as of this state)

Chemists have recently established that elements combine in fixed proportions by weight. A hypothesis that each element consists of identical indivisible particles is new and contested; particle weights are estimated from combining weights by assuming the simplest formulas, and nobody knows how many particles a given volume of gas contains. All gases are known to expand alike with temperature and to compress alike with pressure. Other pairs of gases are observed to combine in volume ratios that also look like ratios of small whole numbers, and gaseous products occupy volumes in similar ratios; no theory explains why gas volumes should combine in simple ratios at all.

# h02 — ratio of the apparent angular diameters of the Moon and the Sun seen from the Earth

```text
name: ratio of the apparent angular diameters of the Moon and the Sun seen from the Earth
definition: Mean apparent angular diameter of the Moon divided by the mean apparent angular diameter of the Sun, both as seen from the Earth.
carrier_readout: the Earth–Moon–Sun system; readout = angular diameters measured with a telescope micrometer; the occurrence of total and annular eclipses
dimensions_units: dimensionless
value: 0.97 (mean); 0.90–1.08 over the orbits
sigma: 0.01 for the mean
source: measurement as published at the knowledge state described below (names and dates withheld)
value_confidence: med
```

## Knowledge state (judge as of this state)

Gravitation and celestial mechanics are established; the orbits of the Moon around the Earth and of the Earth around the Sun are ellipses, so both distances vary over each orbit. Tidal friction is known to transfer angular momentum from the Earth's rotation to the Moon's orbit: the Moon recedes slowly and the day lengthens. The near-equality of the two discs is what makes total solar eclipses possible.

# h03 — fractional excess of the electron's intrinsic magnetic moment over its relativistic wave-equation value

```text
name: fractional excess of the electron's intrinsic magnetic moment over its relativistic wave-equation value
definition: a = (μ − μ_D)/μ_D, where μ_D is the intrinsic magnetic moment that the relativistic wave equation of the electron predicts (one magneton) and μ is the measured intrinsic moment.
carrier_readout: electrons bound in free atoms; readout = ratio of the magnetic resonance frequencies of two atomic states in the same magnetic field, which gives the ratio of the electron's intrinsic and orbital magnetic factors
dimensions_units: dimensionless
value: 0.00119
sigma: 0.00005
source: measurement as published at the knowledge state described below (names and dates withheld)
value_confidence: med
```

## Knowledge state (judge as of this state)

The relativistic wave equation of the electron is established: it predicts the intrinsic magnetic moment exactly (a = 0) and the fine structure of hydrogen. A quantum theory of the electromagnetic field exists, but its corrections to the electron's properties come out infinite, and no finite prediction of any correction is available. A small shift between two hydrogen levels that the wave equation makes equal has just been measured as well. No theory accounts for the excess.

# h04 — ratio of the mean length of the solar activity cycle to the orbital period of the largest planet

```text
name: ratio of the mean length of the solar activity cycle to the orbital period of the largest planet
definition: Mean period of the sunspot-number cycle divided by the sidereal orbital period of the largest planet.
carrier_readout: the Sun's surface activity and the planetary system; readout = daily sunspot counts over about two centuries; planetary timing
dimensions_units: dimensionless
value: 0.94 (about 11.1 years over 11.86 years)
sigma: 0.08 (individual cycles last 9 to 14 years)
source: measurement as published at the knowledge state described below (names and dates withheld)
value_confidence: med
```

## Knowledge state (judge as of this state)

Sunspots come and go in a cycle of about eleven years whose individual lengths vary from about nine to fourteen years; the Sun's magnetic polarity reverses each cycle, so the full magnetic cycle is twice as long. The Sun is a rotating, convecting ball of ionized gas with a magnetic field. The largest planet raises tides on the Sun about a millimetre high. A proposal says the planets, chiefly the largest, set the cycle.

# h05 — number of solar days in one orbit of the planet around its star

```text
name: number of solar days in one orbit of the planet around its star
definition: Length of the tropical year divided by the length of the mean solar day.
carrier_readout: the Earth's rotation and orbit; readout = astronomical timing of solstices and of the Sun's daily transits
dimensions_units: dimensionless
value: 365.2422
sigma: 0.0001
source: measurement as published at the knowledge state described below (names and dates withheld)
value_confidence: med
```

## Knowledge state (judge as of this state)

Celestial mechanics is established: the year is set by the Earth's orbital distance and the Sun's mass, the day by the Earth's rotation rate, which dates from the Earth's formation and which tidal friction slowly reduces. Ancient eclipse records and daily growth bands in fossil corals indicate that the day was shorter, and the year held more days, in the distant past.

# h06 — nucleon numbers at which nuclei show closed-group stability

```text
name: nucleon numbers at which nuclei show closed-group stability
definition: The proton numbers and neutron numbers at which nuclei are exceptionally stable (many stable isotopes or isotones, high natural abundance, a jump in separation energy, small neutron-capture probability).
carrier_readout: atomic nuclei; readout = separation energies from precise mass measurements, natural abundances, neutron-capture cross sections, counts of stable nuclei per proton or neutron number
dimensions_units: dimensionless (counts)
value: 2, 8, 20, 28, 50, 82, 126 — the same set for protons and for neutrons
sigma: none (exact counts; the evidence is strong for each number)
source: measurement as published at the knowledge state described below (names and dates withheld)
value_confidence: med
```

## Knowledge state (judge as of this state)

Nuclei are bound systems of protons and neutrons held by a short-range nuclear force of unknown form. The dominant picture treats the nucleus as a charged liquid drop; it reproduces nuclear masses smoothly but predicts no special numbers. Independent-particle orbits in a common potential — the picture that explains the closed electron shells of atoms — give the first three numbers (2, 8, 20) but not 28, 50, 82 and 126, and are widely thought implausible for a dense nucleus. No accepted theory accounts for the full set.

# h07 — magnetic splitting factor of the upper level of the shorter-wavelength yellow line of the element whose vapour colours flames yellow

```text
name: magnetic splitting factor of the upper level of the shorter-wavelength yellow line of the element whose vapour colours flames yellow
definition: Spacing of the sublevels into which this atomic energy level splits in a weak magnetic field, in units of the spacing the classical theory of an orbiting electron predicts.
carrier_readout: the element's vapour in a magnetic field; readout = the pattern of the split spectral line, measured with a high-resolution spectrograph
dimensions_units: dimensionless
value: 1.333
sigma: 0.005
source: measurement as published at the knowledge state described below (names and dates withheld)
value_confidence: med
```

## Knowledge state (judge as of this state)

Atoms are known to consist of a small heavy nucleus and electrons in discrete stationary states labelled by whole quantum numbers (and, empirically, by half-integers for some levels); level energies are known from spectra. In a weak magnetic field each level splits into equally spaced sublevels. The classical theory of an orbiting electron predicts a splitting factor of exactly 1 for every level, but most levels show other factors. Factors measured for many levels come out close to simple fractions such as 2/3, 4/3, 6/5 and 2. No accepted theory accounts for them; nothing is known of an intrinsic rotation of the electron.

# h08 — free-fall acceleration at the Earth's surface in metres per second squared, divided by π²

```text
name: free-fall acceleration at the Earth's surface in metres per second squared, divided by π²
definition: The number obtained by dividing the standard free-fall acceleration at the Earth's surface, expressed in metres per second squared (9.81), by π² (9.8696).
carrier_readout: the Earth's gravitational field; readout = pendulum periods and free-fall timing with the metre and the second as units
dimensions_units: the quotient of a value in m s^-2 by the pure number π²
value: 0.994
sigma: 0.003 (g varies with latitude and altitude)
source: measurement as published at the knowledge state described below (names and dates withheld)
value_confidence: med
```

## Knowledge state (judge as of this state)

Gravitation, the pendulum law (the period of a simple pendulum is 2π times the square root of its length over the free-fall acceleration) and the definitions of the metre and the second are established. The free-fall acceleration follows from the Earth's mass and radius by the law of gravitation, corrected for the Earth's rotation and shape.

# h09 — growth factor of the gaps between successive planetary orbits

```text
name: growth factor of the gaps between successive planetary orbits
definition: The factor by which the gap between the mean orbital distances of successive planets grows from one planet to the next, as summarized by the rule distance = 0.4 + 0.3 × 2^n (in units of the third planet's distance).
carrier_readout: the planetary system; readout = relative mean orbital distances from positional astronomy
dimensions_units: dimensionless
value: 2 (the rule); individual successive gap ratios 1.79–2.23 when one gap between the fourth and fifth planets is assumed to hold an undiscovered planet
sigma: individual gap ratios scatter by about ±0.2 about 2
source: measurement as published at the knowledge state described below (names and dates withheld)
value_confidence: med
```

## Knowledge state (judge as of this state)

The law of universal gravitation and its mechanics are established; they explain the shapes of orbits and the period–distance relation, but the sizes of the orbits enter only as initial conditions: gravitation allows a planet at any distance. A hypothesis that the planets formed out of a rotating, flattened cloud of matter around the young star exists. A planet beyond the six classical ones has recently been found at a distance close to the rule, and astronomers are searching the gap between the fourth and fifth planets for the body the rule requires there.

# h10 — ratio of the wavelengths of the two strongest visible emission lines of the lightest gas

```text
name: ratio of the wavelengths of the two strongest visible emission lines of the lightest gas
definition: Wavelength of the red emission line divided by the wavelength of the blue-green emission line of the lightest gas excited in an electric discharge.
carrier_readout: the dilute lightest gas glowing in a discharge tube; readout = wavelengths measured with a diffraction grating against a standard length scale
dimensions_units: dimensionless
value: 1.35002
sigma: 0.00004
source: measurement as published at the knowledge state described below (names and dates withheld)
value_confidence: med
```

## Knowledge state (judge as of this state)

Each chemical element emits and absorbs light only at its own sharp set of wavelengths, reproducible in every laboratory and also seen in the light of the stars; spectra identify elements. Light is understood as an electromagnetic wave. Nothing is known about the internal structure of the emitting particles, and no theory predicts where the lines of any element should lie. For the lightest gas four visible lines are measured; their wavelength ratios lie close to ratios of small whole numbers, but whether this means anything is unknown.

# h11 — exponent relating the orbital period to the orbit size of the bodies circling the central star

```text
name: exponent relating the orbital period to the orbit size of the bodies circling the central star
definition: The power k in T proportional to a^k fitted across the six known planets, with T the sidereal orbital period and a the mean distance (semi-major axis) from the central star.
carrier_readout: the planetary system; readout = periods from the timing of returns to the same place among the fixed stars, relative distances from the geometry of long series of naked-eye positional records
dimensions_units: dimensionless
value: 1.500
sigma: about 0.003 (scatter of the six planets about one power law)
source: measurement as published at the knowledge state described below (names and dates withheld)
value_confidence: med
```

## Knowledge state (judge as of this state)

Planetary orbits have recently been shown to be ellipses with the central star at one focus, each planet sweeping out equal areas in equal times. There is no physical theory of what moves the planets: no law of force, no mechanics that applies to the heavens, and the masses of the bodies are unknown. Distances are known only relative to the Earth's distance. The period–distance relation was found by fitting the six planets' records; no principle predicts its exponent.
