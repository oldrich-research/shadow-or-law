## Part 1

R1. A measured ratio to a conventionally chosen physical reference is not rejected merely because the reference defines a unit, while a rule-1 rejection must identify the defining convention, tautology or named combination in `natural_form`; unclear: whether a named expression involving a specified temperature, rather than constants alone, counts as a named combination under this rule.

R2. Reject a present value of an evolving quantity as epoch-dependent, but send a value frozen at a past event onward to step 2; unclear: none.

R3. For a unit-bearing target, attempt a physically related, different reference quantity using general physics knowledge, record the resulting dimensionless ratio and its relation, and allow FAIL-UNIT only when no such form exists or rule 1 applies; unclear: none.

R4. Treat fixed-point properties and universal data as STATIC even when their calculation is non-perturbative, leaving their established theoretical explanation to step 5; unclear: none.

R5. Treat standard-theory free inputs as HISTORY until a proposed structure or dynamics supplies a forward derivation, naming that bridge as the reopening condition; unclear: none.

R6. When a target bundles quantities, classify only the first-named quantity and identify the others in the justification; unclear: none.

R7. An otherwise eligible value unexplained and unadjustable in current admissible completions counts as CONSTANT, whereas VARIES requires actual admissible completions assigning different values; unclear: none.

R8. Apply step 1 in order by rejecting defining conventions first, rejecting documented epoch or frame dependence second, and otherwise accepting an existing or physically justified natural dimensionless form; unclear: the rule-1 boundary for named expressions involving state variables.

R9. Step 2 distinguishes static structural or established analytic predictions from contingent outcomes, separate bound-state or phase solutions, value-setting history inputs and unbridged free parameters, with the stated exceptions taking priority; unclear: none.

R10. Step 5 fixes the assumptions, measurement dictionary and admissible family, then classifies an unexplained invariant value as CONSTANT, an independently selected value according to whether its selecting theory is established, and an unselected varying value as VARIES; unclear: none.

## Part 2

```text
item: p01
step0: PASS
step1: FAIL-UNIT
natural_form: none — rule 1: named combination fixed by the defining identity λ = h/sqrt(2π m k_B T)
step2: NOT-REACHED
step4: NOT-APPLICABLE
step5: NOT-REACHED
disposition: CONVENTION-BOUND
confidence: med
shared_driver: none
reopen_condition: a separately specified physical observable replaces the definition-fixed combination
justification: The gas supplies the carrier and measurements of mass and temperature supply the inferred readout, but I interpret this named wavelength as a definition-fixed combination whose ratio to its defining expression is tautological, although rule 1 is less explicit about combinations involving temperature.
```

```text
item: p02
step0: PASS
step1: PASS
natural_form: E_gap/E_h; Hartree energy E_h; the electronic band gap arises from atomic-scale Coulomb interactions whose natural energy unit is the Hartree
step2: HISTORY
step4: NOT-APPLICABLE
step5: NOT-REACHED
disposition: OUTPUT-OF-HISTORY
confidence: high
shared_driver: none
reopen_condition: a static structural relation fixes the dimensionless gap without a value-setting band-structure solution
justification: Bulk germanium carries the gap and absorption or transport reads it out, but the gap at the specified temperature depends on the material's electronic band structure rather than a static structural value.
```

```text
item: p03
step0: PASS
step1: PASS
natural_form: as stated
step2: HISTORY
step4: NOT-APPLICABLE
step5: NOT-REACHED
disposition: OUTPUT-OF-HISTORY
confidence: high
shared_driver: none
reopen_condition: a forward derivation bridges the value-setting B decay constant and flavour inputs
justification: Charged B mesons carry the branching fraction and tagged decay counts read it out, while its predicted value inherits HISTORY from the B decay constant and free mixing input.
```

```text
item: p04
step0: PASS
step1: PASS
natural_form: m_c(3 GeV)/v; electroweak vacuum energy scale v; the charm Yukawa relation connects the quark mass to that scale
step2: HISTORY
step4: NOT-APPLICABLE
step5: NOT-REACHED
disposition: OUTPUT-OF-HISTORY
confidence: high
shared_driver: none
reopen_condition: a proposed flavour or symmetry-breaking dynamics derives the charm Yukawa parameter through a forward map
justification: Charm-sector correlators and lattice calculations read out the mass in its fixed scheme and scale, so subtraction-scale running is not epoch dependence, but the mass remains an unbridged free input.
```

```text
item: p05
step0: PASS
step1: PASS
natural_form: as stated
step2: STATIC
step4: VACUOUS
step5: SELECTED-ESTABLISHED
disposition: ALREADY-GOVERNED
confidence: high
shared_driver: none
reopen_condition: none stated
justification: Hydrogen supplies the transition carrier and spectroscopy supplies its readout with the specified limiting extrapolation, while the established Coulomb spectrum fixes the exact ratio 1 − 1/4 = 3/4 under the stated nonrelativistic infinite-nuclear-mass assumptions.
```

```text
item: p06
step0: PASS
step1: PASS
natural_form: a/a_0; Bohr radius a_0; electronic Coulomb bonding sets the crystal's equilibrium length on the atomic length scale
step2: HISTORY
step4: NOT-APPLICABLE
step5: NOT-REACHED
disposition: OUTPUT-OF-HISTORY
confidence: high
shared_driver: none
reopen_condition: a static structural relation fixes a/a_0 without a separate equilibrium material-state solution
justification: The crystal carries the lattice length and diffraction reads it out, but its equilibrium spacing requires a material-state solution, and d_100 is merely another projection of the same lattice size rather than an admissible independent reference.
```

PRETEST-COMPLETE