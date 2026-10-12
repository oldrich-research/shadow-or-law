## J043
formula: c = 5, n = 21, k = -3
- object: Energy-bounded classical 22-mode isotropic oscillator canonical energy weight.
- n: \(22-1=21\); mode count **chosen to fit**.
- k: \(\beta=-3\), **chosen to fit**.
- c: \(\omega^{22}=1/(5\cdot21!)\), **chosen to fit**, gives \(c=5\).
- derivation: \(\rho(x)=5x^{21}\). Weighting by \(e^{3x}\) gives \(5x^{21}e^{3x}\) below the chosen cutoff.

## J044
formula: c = 5/2, n = 21, k = 1
- **object:** the one-sided Weyl denominator of SU(7) along exp(xH).
- **n:** derived: 21 = |Φ⁺(A₆)|.
- **k:** not derived. ρ(H) = 1 needs a tuned H (chosen to fit).
- **c:** not derived. ∏α(H) = 5/2 needs a tuned H (chosen to fit).
- **derivation:** For a dominant H, AM–GM requires c ≤ (2/21)²¹ ≈ 3.6·10⁻²². Here c/k²¹ = 2.5, which is 22 orders of magnitude too large, so no time scaling helps and H must be non-dominant and tuned. The cleanest standard match for k is the classical exact heat kernel on H³ at curvature −1, (4πt)^{−3/2}e^{−t}. It still has n = −3/2. **Verdict:** n only.

## J045
formula: c = 3, n = 21, k = -2
no account

## J046
formula: c = 2/5, n = 21, k = 3
- **object:** the one-sided Weyl denominator of SU(7) along exp(xH).
- **n:** derived: 21 = |Φ⁺(A₆)|.
- **k:** not derived. ρ(H) = 3 needs a tuned H (chosen to fit).
- **c:** not derived. ∏α(H) = 2/5 needs a tuned H (chosen to fit).
- **derivation:** For a dominant H, AM–GM requires c ≤ (2/7)²¹ ≈ 3.8·10⁻¹², and c = 2/5 breaks this. Here c/k²¹ = 3.8·10⁻¹¹, and rescaling x cannot change that ratio. So H is non-dominant and tuned. The k-only match is (H³)³ at curvature −1, (4πt)^{−9/2}e^{−3t}, with n = −9/2. L19 has the same k as L02 and differs only in c. **Verdict:** n only.

## J047
formula: c = 4, n = 21, k = 2
no account

## J048
formula: c = 2/3, n = 21, k = 1/2
- object: Classical 22-mode isotropic oscillator canonical energy weight.
- n: The action simplex gives exponent 21; mode count **chosen to fit**.
- k: \(\beta=1/2\), **chosen to fit**.
- c: \(\omega^{22}=3/(2\cdot21!)\), **chosen to fit**, gives \(c=2/3\).
- derivation: The density coefficient is \(2/3\), so canonical weighting gives \((2/3)x^{21}e^{-x/2}\).

## J049
formula: c = 4/5, n = 21, k = 1/2
no account

## J050
formula: c = 4/5, n = 21, k = 3/2
no account

## J051
formula: c = 4, n = 21, k = 2
- object: Classical 22-mode isotropic oscillator canonical energy weight.
- n: \(22-1=21\); mode count **chosen to fit**.
- k: \(\beta=2\), **chosen to fit**.
- c: \(\omega^{22}=1/(4\cdot21!)\), **chosen to fit**, gives \(c=4\).
- derivation: The density-of-states coefficient is \(4\); the canonical factor is \(e^{-2x}\). Together they give \(4x^{21}e^{-2x}\).

## J052
formula: c = 1/4, n = 21, k = 1
- **object:** the one-sided Weyl denominator of SU(7) along exp(xH).
- **n:** derived: 21 = |Φ⁺(A₆)|.
- **k:** not derived. ρ(H) = 1 needs a tuned H (chosen to fit).
- **c:** not derived. ∏α(H) = 1/4 needs a tuned H (chosen to fit).
- **derivation:** For a dominant H, AM–GM requires c ≤ (2/21)²¹ ≈ 3.6·10⁻²², and c = 1/4 breaks this, so H is non-dominant and tuned. The k-only match is the classical exact heat kernel on H³ at curvature −1, (4πt)^{−3/2}e^{−t}, with n = −3/2. Another account fits just as well and is just as arbitrary: 1/H_R for R = ℂ[x₁..x₂₂,y]/(q₂, y²−g₃₆) with deg y = 18. Here H_R ≈ 4x⁻²¹e^{+x}, so a = −2, c = 1/4 and k = 1 (chosen to fit). L33 has the same k as L06. **Verdict:** n only.

## J053
formula: c = 3, n = 21, k = -4
- **object:** the one-sided Weyl denominator of SU(7) (type A₆), taken along exp(xH): D_H(x) = ∏_{α∈Φ⁺}(1−e^{−xα(H)}), with H regular. This is the best account I found. It accounts for n only.
- **n:** derived. D_H vanishes at x=0 to order |Φ⁺(A₆)| = 21, which is also dim_ℂ SU(7)/T.
- **k:** not derived. Here k = ρ(H). The value −4 needs a tuned H (chosen to fit). The canonical H = ρ^∨ gives k = 28.
- **c:** not derived. Here c = ∏α(H). The value 3 needs a tuned H (chosen to fit). The canonical value is 1!2!⋯6! = 24 883 200.
- **derivation:** D_H = e^{−xρ(H)}∏2sinh(xα(H)/2) = (∏α(H))·x²¹·e^{−xρ(H)}·(1+O(x²)). Rescaling x leaves c/|k|²¹ unchanged. For this row it is 6.8·10⁻¹³. The canonical H gives 1.0·10⁻²³, and AM–GM caps every dominant H at (2/21)²¹ ≈ 3.6·10⁻²². Since k<0, H cannot be dominant. Since c>0, H cannot be antidominant either (that would make c<0). So H must be tuned inside an intermediate chamber wC with det w = +1. The heat kernel of SU(3)×SU(3) with the basic metric, K_t(e) ≈ (4πt)⁻⁸e^{+4t}, matches k. But every heat kernel has n = −d/2 < 0. **Verdict:** n is explained; (c,k) is not.

## J054
formula: c = 3/5, n = 21, k = -1/2
- object: Energy-bounded classical 22-mode isotropic oscillator canonical energy weight.
- n: The action simplex gives exponent 21; mode count **chosen to fit**.
- k: \(\beta=-1/2\), **chosen to fit**.
- c: \(\omega^{22}=5/(3\cdot21!)\), **chosen to fit**, gives \(c=3/5\).
- derivation: The shell density is \((3/5)x^{21}\). Multiplication by \(e^{x/2}\) gives the formula for energies below the cutoff.

## J055
formula: c = 3, n = 21, k = -3
no account

## J056
formula: c = 1/3, n = 21, k = 3/2
no account

## J057
formula: c = 1/4, n = 21, k = -1/2
- **object:** the one-sided Weyl denominator of SU(7) along exp(xH).
- **n:** derived: 21 = |Φ⁺(A₆)|.
- **k:** not derived. ρ(H) = −1/2 needs a tuned H (chosen to fit).
- **c:** not derived. ∏α(H) = 1/4 needs a tuned H (chosen to fit).
- **derivation:** The scale-free ratio is c/|k|²¹ = 5.2·10⁵. Since k<0 and c>0, H must lie in a tuned intermediate chamber. The k-only match is SU(2) with the basic metric, (4πt)^{−3/2}e^{t/2}, with n = −3/2. Another account fits just as well and is just as arbitrary: 1/H_R for the complete intersection R = ℂ[x₁..x₂₂,y]/(q₂, y²−g₄₂) with deg y = 21. Here H_R ≈ 4x⁻²¹e^{−x/2}, so c = 1/4 and k = −1/2 (chosen to fit). L24 has the same k as L07 and L08. **Verdict:** n only.

## J058
formula: c = 4/5, n = 21, k = 2
- object: Classical 22-mode isotropic oscillator canonical energy weight.
- n: \(22-1=21\); mode count **chosen to fit**.
- k: \(\beta=2\), **chosen to fit**.
- c: \(\omega^{22}=5/(4\cdot21!)\), **chosen to fit**, gives \(c=4/5\).
- derivation: The density-of-states coefficient is \(4/5\), and canonical weighting supplies \(e^{-2x}\).

## J059
formula: c = 1/5, n = 21, k = -2
- **object:** the one-sided Weyl denominator of SU(7) along exp(xH).
- **n:** derived: 21 = |Φ⁺(A₆)|.
- **k:** not derived. ρ(H) = −2 needs a tuned H (chosen to fit).
- **c:** not derived. ∏α(H) = 1/5 needs a tuned H (chosen to fit).
- **derivation:** The scale-free ratio is c/|k|²¹ = 9.5·10⁻⁸. Since k<0 and c>0, H must lie in a tuned intermediate chamber. The k-only match is SU(3) with the basic metric, (4πt)⁻⁴e^{2t}, with n = −4. Another account fits just as well and is just as arbitrary: 1/H_R for R = ℂ[x₁..x₂₂,y]/(q₂,F₄₀), with deg y = 16 and (q₂,F₄₀) a regular sequence. Here H_R ≈ 5x⁻²¹e^{−2x}, so a = 4, c = 1/5 and k = −2 (chosen to fit). L37 has the same k as L20, L22 and L25. **Verdict:** n only.

## J060
formula: c = 5, n = 21, k = -3
- **object:** the one-sided Weyl denominator of SU(7) along exp(xH).
- **n:** derived: 21 = |Φ⁺(A₆)|.
- **k:** not derived. ρ(H) = −3 needs a tuned H (chosen to fit).
- **c:** not derived. ∏α(H) = 5 needs a tuned H (chosen to fit).
- **derivation:** The expansion is the same as in L01. The scale-free ratio is c/|k|²¹ = 4.8·10⁻¹⁰, against 1.0·10⁻²³ for the canonical H and at most 3.6·10⁻²² for any dominant H. Since k<0, H is not dominant; since c>0, it is not antidominant. So H sits in a tuned intermediate chamber. Unit (S³)³ matches k: K_t ≈ (4πt)^{−9/2}e^{3t}, up to e^{−a/t} terms. But n = −9/2. **Verdict:** n only.

## J061
formula: c = 4/3, n = 21, k = -2
- **object:** the one-sided Weyl denominator of SU(7) along exp(xH).
- **n:** derived: 21 = |Φ⁺(A₆)|.
- **k:** not derived. ρ(H) = −2 needs a tuned H (chosen to fit).
- **c:** not derived. ∏α(H) = 4/3 needs a tuned H (chosen to fit).
- **derivation:** D_H = (∏α(H))x²¹e^{−xρ(H)}(1+O(x²)). The scale-free ratio is c/|k|²¹ = 6.4·10⁻⁷, against 1.0·10⁻²³ for the canonical H. Since k<0 and c>0, H must be tuned in an intermediate chamber with det w = +1. SU(3) with the basic metric (|ρ|² = 2) matches k with standard conventions: K_t(e) ≈ (4πt)⁻⁴e^{2t}. But n = −4. **Verdict:** n only.

## J062
formula: c = 3, n = 21, k = 2
- **object:** the one-sided Weyl denominator of SU(7) along exp(xH).
- **n:** derived: 21 = |Φ⁺(A₆)|.
- **k:** not derived. ρ(H) = 2 needs a tuned H (chosen to fit).
- **c:** not derived. ∏α(H) = 3 needs a tuned H (chosen to fit).
- **derivation:** For a dominant H, AM–GM requires c ≤ (4/21)²¹ ≈ 7.5·10⁻¹⁶, and c = 3 breaks this. Here c/k²¹ = 1.4·10⁻⁶, which no rescaling of x can reduce, so H is non-dominant and tuned. The k-only match is SL(3,C)/SU(3) with the basic metric, (4πt)⁻⁴e^{−2t} exactly, with n = −4. L29 has the same k as L11 and differs only in c. **Verdict:** n only.

## J063
formula: c = 4/3, n = 21, k = 5/2
no account

## J064
formula: c = 2/5, n = 21, k = -3
- object: Energy-bounded classical 22-mode isotropic oscillator canonical energy weight.
- n: The 22-action simplex gives exponent 21; mode count **chosen to fit**.
- k: \(\beta=-3\), **chosen to fit**.
- c: \(\omega^{22}=5/(2\cdot21!)\), **chosen to fit**, gives \(c=2/5\).
- derivation: \(\rho(x)=(2/5)x^{21}\). The factor \(e^{3x}\) is the canonical weight at the chosen negative inverse temperature.

## J065
formula: c = 3, n = 21, k = -4
no account

## J066
formula: c = 4/5, n = 21, k = 4
- object: Classical 22-mode isotropic oscillator canonical energy weight.
- n: The simplex density gives exponent 21; mode count **chosen to fit**.
- k: \(\beta=4\), **chosen to fit**.
- c: \(\omega^{22}=5/(4\cdot21!)\), **chosen to fit**, gives \(c=4/5\).
- derivation: \(\rho(x)=(4/5)x^{21}\). At inverse temperature 4, the energy weight is \((4/5)x^{21}e^{-4x}\).

## J067
formula: c = 2/5, n = 21, k = 1/2
- **object:** the one-sided Weyl denominator of SU(7) along exp(xH).
- **n:** derived: 21 = |Φ⁺(A₆)|.
- **k:** not derived. ρ(H) = 1/2 needs a tuned H (chosen to fit).
- **c:** not derived. ∏α(H) = 2/5 needs a tuned H (chosen to fit).
- **derivation:** For a dominant H, AM–GM requires c ≤ (1/21)²¹ ≈ 1.7·10⁻²⁸, and c = 2/5 breaks this. Here c/k²¹ = 8.4·10⁵, whatever the scale of x, so H is non-dominant and tuned. The k-only match is H³ at curvature −1/2, which is SL(2,C)/SU(2) with the basic metric: (4πt)^{−3/2}e^{−t/2} exactly, with n = −3/2. L26 has the same k as L14 and L18 and differs only in c. **Verdict:** n only.

## J068
formula: c = 5/3, n = 21, k = 1/2
no account

## J069
formula: c = 2/5, n = 21, k = 1/2
- object: Classical 22-mode isotropic oscillator canonical energy weight.
- n: The 22-action simplex gives \(x^{21}\); mode count **chosen to fit**.
- k: \(\beta=1/2\), **chosen to fit**.
- c: \(\omega^{22}=5/(2\cdot21!)\), **chosen to fit**, gives \(c=2/5\).
- derivation: \(1/(21!\omega^{22})=2/5\). Hence the canonical energy weight is \((2/5)x^{21}e^{-x/2}\).

## J070
formula: c = 3, n = 21, k = -2
- **object:** the one-sided Weyl denominator of SU(7) along exp(xH).
- **n:** derived: 21 = |Φ⁺(A₆)|.
- **k:** not derived. ρ(H) = −2 needs a tuned H (chosen to fit).
- **c:** not derived. ∏α(H) = 3 needs a tuned H (chosen to fit).
- **derivation:** The scale-free ratio is c/|k|²¹ = 1.4·10⁻⁶; the canonical H gives 1.0·10⁻²³. Since k<0, H cannot be dominant. Since c>0, H cannot be antidominant (that would make c<0). So H must be tuned in an intermediate chamber with det w = +1. SU(3) with the basic metric matches k with standard conventions: K_t(e) ≈ (4πt)⁻⁴e^{2t}, up to e^{−a/t} terms. But n = −4. L22 has the same k as L20 and differs only in c. **Verdict:** n only.

## J071
formula: c = 1/5, n = 21, k = -4
no account

## J072
formula: c = 5/3, n = 21, k = 1/2
- object: Classical 22-mode isotropic oscillator canonical energy weight.
- n: The 22-action simplex gives exponent 21; mode count **chosen to fit**.
- k: \(\beta=1/2\), **chosen to fit**.
- c: \(\omega^{22}=3/(5\cdot21!)\), **chosen to fit**, gives \(c=5/3\).
- derivation: \(\rho(x)=(5/3)x^{21}\). Canonical weighting gives \((5/3)x^{21}e^{-x/2}\).

## J073
formula: c = 1/5, n = 21, k = -4
- **object:** the one-sided Weyl denominator of SU(7) along exp(xH).
- **n:** derived: 21 = |Φ⁺(A₆)|.
- **k:** not derived. ρ(H) = −4 needs a tuned H (chosen to fit).
- **c:** not derived. ∏α(H) = 1/5 needs a tuned H (chosen to fit).
- **derivation:** The scale-free ratio is c/|k|²¹ = 4.5·10⁻¹⁴. Since k<0 and c>0, H must lie in a tuned intermediate chamber with det w = +1. The k-only match is SU(3)×SU(3) with the basic metric, (4πt)⁻⁸e^{4t}, with n = −8. Another account fits just as well and is just as arbitrary: 1/H_R for R = ℂ[x₁..x₂₁,y,z]/(f₃,F₄₀) with deg y = 2 and deg z = 12. Here H_R ≈ 5x⁻²¹e^{−4x}, so a = 8, c = 1/5 and k = −4 (chosen to fit). L39 has the same k as L01. **Verdict:** n only.

## J074
formula: c = 4/5, n = 21, k = -1/2
- **object:** the one-sided Weyl denominator of SU(7) along exp(xH).
- **n:** derived: 21 = |Φ⁺(A₆)|.
- **k:** not derived. ρ(H) = −1/2 needs a tuned H (chosen to fit).
- **c:** not derived. ∏α(H) = 4/5 needs a tuned H (chosen to fit).
- **derivation:** The scale-free ratio is c/|k|²¹ = 1.7·10⁶, against at most 3.6·10⁻²² for a dominant H. Since k<0 and c>0, H must be in an intermediate chamber and tuned. The k-only match is the same as in L07: SU(2) with the basic metric, (4πt)^{−3/2}e^{t/2}, with n = −3/2. L07 and L08 differ only in c, and none of the candidate objects distinguishes 3/5 from 4/5. **Verdict:** n only.

## J075
formula: c = 2/5, n = 21, k = 3
no account

## J076
formula: c = 1/5, n = 21, k = -2
no account

## J077
formula: c = 2/5, n = 21, k = -3
no account

## J078
formula: c = 2, n = 21, k = 3
- object: Classical 22-mode isotropic oscillator canonical energy weight.
- n: \(22-1=21\); mode count **chosen to fit**.
- k: \(\beta=3\), **chosen to fit**.
- c: \(\omega^{22}=1/(2\cdot21!)\), **chosen to fit**, gives \(c=2\).
- derivation: \(\rho(x)=2x^{21}\). The canonical factor \(e^{-3x}\) gives the requested energy weight.

## J079
formula: c = 1/2, n = 21, k = -3
- **object:** the one-sided Weyl denominator of SU(7) along exp(xH).
- **n:** derived: 21 = |Φ⁺(A₆)|.
- **k:** not derived. ρ(H) = −3 needs a tuned H (chosen to fit).
- **c:** not derived. ∏α(H) = 1/2 needs a tuned H (chosen to fit).
- **derivation:** The scale-free ratio is c/|k|²¹ = 4.8·10⁻¹¹. Since k<0 and c>0, H must lie in a tuned intermediate chamber. The k-only match is unit (S³)³, (4πt)^{−9/2}e^{3t}, with n = −9/2. Another account fits just as well and is just as arbitrary: 1/H_R for R = ℂ[x₁..x₂₁,y]/(y²−g) with deg y = 27 and deg g = 54. That gives c = 1/deg = 1/2 and a = 54−27−21 = 6, so k = −a/2 = −3 (chosen to fit). L16 has the same k as L04 and differs only in c. **Verdict:** n only.

## J080
formula: c = 2, n = 21, k = 3
no account

## J081
formula: c = 4/3, n = 21, k = 5
no account

## J082
formula: c = 2, n = 21, k = -3
- object: Energy-bounded classical 22-mode isotropic oscillator canonical energy weight.
- n: \(22-1=21\); mode count **chosen to fit**.
- k: \(\beta=-3\), **chosen to fit**.
- c: \(\omega^{22}=1/(2\cdot21!)\), **chosen to fit**, gives \(c=2\).
- derivation: The shell density is \(2x^{21}\). On \(0<x<1\), its negative-temperature canonical weight is \(2x^{21}e^{3x}\).

## J083
formula: c = 2/5, n = 21, k = 3
- object: Classical 22-mode isotropic oscillator canonical energy weight.
- n: \(22-1=21\); mode count **chosen to fit**.
- k: \(\beta=3\), **chosen to fit**.
- c: \(\omega^{22}=5/(2\cdot21!)\), **chosen to fit**, gives \(c=2/5\).
- derivation: \(1/(21!\omega^{22})=2/5\). Canonical weighting gives \((2/5)x^{21}e^{-3x}\).

## J084
formula: c = 4/3, n = 21, k = 5/2
- **object:** the one-sided Weyl denominator of SU(7) along exp(xH).
- **n:** derived: 21 = |Φ⁺(A₆)|.
- **k:** not derived. ρ(H) = 5/2 needs a tuned H (chosen to fit).
- **c:** not derived. ∏α(H) = 4/3 needs a tuned H (chosen to fit).
- **derivation:** For a dominant H, AM–GM requires c ≤ (5/21)²¹ ≈ 8.2·10⁻¹⁴, and c = 4/3 breaks this. Here c/k²¹ = 5.9·10⁻⁹, against 1.0·10⁻²³ for the canonical H, whatever the scale of x. So H is non-dominant and tuned. The exact heat kernel of Sp(2,C)/Sp(2) with the basic metric (|ρ|² = 5/2), (4πt)⁻⁵e^{−5t/2}, matches k. But n = −5. **Verdict:** n only.
