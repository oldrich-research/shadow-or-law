# PUB-2 rational-density arithmetic null · frozen before pass 2 · 2026-10-07

Question: for four measured, dimensionless centers x and stated absolute uncertainty σ, how many reduced rationals with denominator ≤500 lie in [x−σ,x+σ], and how frequent is a count at least this large when an interval of the same width is translated uniformly modulo 1?

Inputs, decimal strings interpreted exactly: 100θ* x=1.0411 σ=0.0003; n_s x=0.9649 σ=0.0042; H0·t0 x=0.95103824655253 σ=0.00723111905553476; Ω_m0 x=0.315 σ=0.007. The age quantity is H0·t0, never t0/t_P. Q=500. Inclusive endpoints for observed count. Rational population: one member per reduced fraction p/q mod 1, 1≤q≤Q, 0≤p<q, gcd(p,q)=1 (including 0/1). For observed x, compare on the unit circle at x mod 1, shortest circular distance ≤σ. Translation by an integer leaves the original unbounded fraction count invariant. All σ<1/2.

Primary statistic per row: observed count C_obs; null tail probability = Lebesgue measure of c∈[0,1) for which C(c)≥C_obs, with C(c) the circular ±σ reduced-rational count. Compute by exact rational sweep over arc endpoints, not a random sample; point endpoints have measure zero. Report fraction or enough digits to round to six decimals; numerical uncertainty = zero for exact arithmetic (input measurement uncertainties remain fixed, not propagated). Report Farey density comparison separately. No seed, draws, fitted range, or multiplicity adjustment. Four rows are descriptive examples; no claim that null probabilities are physical p-values, evidence for a law, or independent tests of the shadow ontology.

Independent gate: recompute C_obs by gcd enumeration in the original real interval and by circular Farey-point count; require equality. Validate sweep by brute-force interval integration on a small Q with exact rational partition; optional Monte Carlo spot check only. Preserve all source/sham historical claims as historical with provenance caveat; do not substitute this newly specified null for their lost protocols.

State: frozen before computing results. Change requires dated addendum and separate output identity.
