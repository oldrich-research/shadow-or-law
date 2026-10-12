# AX: SCRIPT | SUM: v4 historical yes-branch arm — 11 knowledge-state dossiers, hash-ordered ids, sealed key | SIG: p15hist04
"""Usage: python3 -I make_hist_v4.py → hist/h01..h11.md, hist/hist_key_v4.json. Written by the lead (builder) before any lane runs."""
import hashlib, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SEED = '20261008-p15-v4-hist'
T = ('# {hid} — {name}\n\n```text\nname: {name}\ndefinition: {definition}\ncarrier_readout: {carrier}\n'
     'dimensions_units: {units}\nvalue: {value}\nsigma: {sigma}\nsource: {source}\nvalue_confidence: med\n```\n\n'
     '## Knowledge state (judge as of this state)\n\n{ks}\n')
SRC = 'measurement as published at the knowledge state described below (names and dates withheld)'
ITEMS = [
 dict(slug='P1-combining-volumes', truth='POSITIVE', later='equal volumes of gases hold equal numbers of molecules; water = two light atoms per heavy one → exactly 2 in the ideal-gas limit',
      best='LAW-CANDIDATE',
      name='volume ratio in which the lightest gas and the gas that supports burning combine',
      definition='Volume of the lightest known gas divided by the volume of the gas that supports combustion when the two combine completely into water vapour, both measured at the same temperature and pressure.',
      carrier='the two gases reacting in a closed graduated tube ignited by a spark; readout = the gas volumes consumed, read on the tube scale',
      units='dimensionless', value='1.9989', sigma='about 0.003 (tube readings; not stated precisely)', source=SRC,
      ks='Chemists have recently established that elements combine in fixed proportions by weight. A hypothesis that each element consists of identical indivisible particles is new and contested; particle weights are estimated from combining weights by assuming the simplest formulas, and nobody knows how many particles a given volume of gas contains. All gases are known to expand alike with temperature and to compress alike with pressure. Other pairs of gases are observed to combine in volume ratios that also look like ratios of small whole numbers, and gaseous products occupy volumes in similar ratios; no theory explains why gas volumes should combine in simple ratios at all.'),
 dict(slug='P2-period-size-exponent', truth='POSITIVE', later='inverse-square gravitation → exactly 3/2 (tiny planet-mass corrections)', best='LAW-CANDIDATE',
      name='exponent relating the orbital period to the orbit size of the bodies circling the central star',
      definition='The power k in T proportional to a^k fitted across the six known planets, with T the sidereal orbital period and a the mean distance (semi-major axis) from the central star.',
      carrier='the planetary system; readout = periods from the timing of returns to the same place among the fixed stars, relative distances from the geometry of long series of naked-eye positional records',
      units='dimensionless', value='1.500', sigma='about 0.003 (scatter of the six planets about one power law)', source=SRC,
      ks='Planetary orbits have recently been shown to be ellipses with the central star at one focus, each planet sweeping out equal areas in equal times. There is no physical theory of what moves the planets: no law of force, no mechanics that applies to the heavens, and the masses of the bodies are unknown. Distances are known only relative to the Earth\'s distance. The period–distance relation was found by fitting the six planets\' records; no principle predicts its exponent.'),
 dict(slug='P3-line-ratio', truth='POSITIVE', later='quantized bound electron in hydrogen → (1/4−1/9)^{-1}/(1/4−1/16)^{-1} = 27/20 exactly at leading order', best='LAW-CANDIDATE',
      name='ratio of the wavelengths of the two strongest visible emission lines of the lightest gas',
      definition='Wavelength of the red emission line divided by the wavelength of the blue-green emission line of the lightest gas excited in an electric discharge.',
      carrier='the dilute lightest gas glowing in a discharge tube; readout = wavelengths measured with a diffraction grating against a standard length scale',
      units='dimensionless', value='1.35002', sigma='0.00004', source=SRC,
      ks='Each chemical element emits and absorbs light only at its own sharp set of wavelengths, reproducible in every laboratory and also seen in the light of the stars; spectra identify elements. Light is understood as an electromagnetic wave. Nothing is known about the internal structure of the emitting particles, and no theory predicts where the lines of any element should lie. For the lightest gas four visible lines are measured; their wavelength ratios lie close to ratios of small whole numbers, but whether this means anything is unknown.'),
 dict(slug='P4-splitting-factor', truth='POSITIVE', later='electron spin + angular-momentum coupling → g = 4/3 exactly for this level', best='LAW-CANDIDATE',
      name='magnetic splitting factor of the upper level of the shorter-wavelength yellow line of the element whose vapour colours flames yellow',
      definition='Spacing of the sublevels into which this atomic energy level splits in a weak magnetic field, in units of the spacing the classical theory of an orbiting electron predicts.',
      carrier='the element\'s vapour in a magnetic field; readout = the pattern of the split spectral line, measured with a high-resolution spectrograph',
      units='dimensionless', value='1.333', sigma='0.005', source=SRC,
      ks='Atoms are known to consist of a small heavy nucleus and electrons in discrete stationary states labelled by whole quantum numbers (and, empirically, by half-integers for some levels); level energies are known from spectra. In a weak magnetic field each level splits into equally spaced sublevels. The classical theory of an orbiting electron predicts a splitting factor of exactly 1 for every level, but most levels show other factors. Factors measured for many levels come out close to simple fractions such as 2/3, 4/3, 6/5 and 2. No accepted theory accounts for them; nothing is known of an intrinsic rotation of the electron.'),
 dict(slug='P5-closed-counts', truth='POSITIVE', later='independent-nucleon shells with strong spin–orbit coupling → exactly these counts', best='LAW-CANDIDATE',
      name='nucleon numbers at which nuclei show closed-group stability',
      definition='The proton numbers and neutron numbers at which nuclei are exceptionally stable (many stable isotopes or isotones, high natural abundance, a jump in separation energy, small neutron-capture probability).',
      carrier='atomic nuclei; readout = separation energies from precise mass measurements, natural abundances, neutron-capture cross sections, counts of stable nuclei per proton or neutron number',
      units='dimensionless (counts)', value='2, 8, 20, 28, 50, 82, 126 — the same set for protons and for neutrons', sigma='none (exact counts; the evidence is strong for each number)', source=SRC,
      ks='Nuclei are bound systems of protons and neutrons held by a short-range nuclear force of unknown form. The dominant picture treats the nucleus as a charged liquid drop; it reproduces nuclear masses smoothly but predicts no special numbers. Independent-particle orbits in a common potential — the picture that explains the closed electron shells of atoms — give the first three numbers (2, 8, 20) but not 28, 50, 82 and 126, and are widely thought implausible for a dense nucleus. No accepted theory accounts for the full set.'),
 dict(slug='P6-moment-anomaly', truth='POSITIVE', later='quantum electrodynamics, renormalized: a = α/2π at first order', best='LAW-CANDIDATE',
      name='fractional excess of the electron\'s intrinsic magnetic moment over its relativistic wave-equation value',
      definition='a = (μ − μ_D)/μ_D, where μ_D is the intrinsic magnetic moment that the relativistic wave equation of the electron predicts (one magneton) and μ is the measured intrinsic moment.',
      carrier='electrons bound in free atoms; readout = ratio of the magnetic resonance frequencies of two atomic states in the same magnetic field, which gives the ratio of the electron\'s intrinsic and orbital magnetic factors',
      units='dimensionless', value='0.00119', sigma='0.00005', source=SRC,
      ks='The relativistic wave equation of the electron is established: it predicts the intrinsic magnetic moment exactly (a = 0) and the fine structure of hydrogen. A quantum theory of the electromagnetic field exists, but its corrections to the electron\'s properties come out infinite, and no finite prediction of any correction is available. A small shift between two hydrogen levels that the wave equation makes equal has just been measured as well. No theory accounts for the excess.'),
 dict(slug='N1-orbit-gap-growth', truth='NEGATIVE', later='orbit sizes = outcome of planet formation; the rule failed for the eighth planet', best='OUTPUT-OF-HISTORY',
      name='growth factor of the gaps between successive planetary orbits',
      definition='The factor by which the gap between the mean orbital distances of successive planets grows from one planet to the next, as summarized by the rule distance = 0.4 + 0.3 × 2^n (in units of the third planet\'s distance).',
      carrier='the planetary system; readout = relative mean orbital distances from positional astronomy',
      units='dimensionless', value='2 (the rule); individual successive gap ratios 1.79–2.23 when one gap between the fourth and fifth planets is assumed to hold an undiscovered planet',
      sigma='individual gap ratios scatter by about ±0.2 about 2', source=SRC,
      ks='The law of universal gravitation and its mechanics are established; they explain the shapes of orbits and the period–distance relation, but the sizes of the orbits enter only as initial conditions: gravitation allows a planet at any distance. A hypothesis that the planets formed out of a rotating, flattened cloud of matter around the young star exists. A planet beyond the six classical ones has recently been found at a distance close to the rule, and astronomers are searching the gap between the fourth and fifth planets for the body the rule requires there.'),
 dict(slug='N2-disc-ratio', truth='NEGATIVE', later='orbital eccentricities + tidal recession of the Moon: a passing value', best='EPOCH-DEPENDENT',
      name='ratio of the apparent angular diameters of the Moon and the Sun seen from the Earth',
      definition='Mean apparent angular diameter of the Moon divided by the mean apparent angular diameter of the Sun, both as seen from the Earth.',
      carrier='the Earth–Moon–Sun system; readout = angular diameters measured with a telescope micrometer; the occurrence of total and annular eclipses',
      units='dimensionless', value='0.97 (mean); 0.90–1.08 over the orbits', sigma='0.01 for the mean', source=SRC,
      ks='Gravitation and celestial mechanics are established; the orbits of the Moon around the Earth and of the Earth around the Sun are ellipses, so both distances vary over each orbit. Tidal friction is known to transfer angular momentum from the Earth\'s rotation to the Moon\'s orbit: the Moon recedes slowly and the day lengthens. The near-equality of the two discs is what makes total solar eclipses possible.'),
 dict(slug='N3-g-over-pi2', truth='NEGATIVE', later='unit coincidence: the metre was once proposed as the length of the pendulum that beats seconds, which makes g ≈ π² m/s²', best='CONVENTION-BOUND',
      name='free-fall acceleration at the Earth\'s surface in metres per second squared, divided by π²',
      definition='The number obtained by dividing the standard free-fall acceleration at the Earth\'s surface, expressed in metres per second squared (9.81), by π² (9.8696).',
      carrier='the Earth\'s gravitational field; readout = pendulum periods and free-fall timing with the metre and the second as units',
      units='the quotient of a value in m s^-2 by the pure number π²', value='0.994', sigma='0.003 (g varies with latitude and altitude)', source=SRC,
      ks='Gravitation, the pendulum law (the period of a simple pendulum is 2π times the square root of its length over the free-fall acceleration) and the definitions of the metre and the second are established. The free-fall acceleration follows from the Earth\'s mass and radius by the law of gravitation, corrected for the Earth\'s rotation and shape.'),
 dict(slug='N4-days-per-year', truth='NEGATIVE', later='rotation set at formation and slowed by tides; ≈ 400 days per year 400 million years ago', best='EPOCH-DEPENDENT',
      name='number of solar days in one orbit of the planet around its star',
      definition='Length of the tropical year divided by the length of the mean solar day.',
      carrier='the Earth\'s rotation and orbit; readout = astronomical timing of solstices and of the Sun\'s daily transits',
      units='dimensionless', value='365.2422', sigma='0.0001', source=SRC,
      ks='Celestial mechanics is established: the year is set by the Earth\'s orbital distance and the Sun\'s mass, the day by the Earth\'s rotation rate, which dates from the Earth\'s formation and which tidal friction slowly reduces. Ancient eclipse records and daily growth bands in fossil corals indicate that the day was shorter, and the year held more days, in the distant past.'),
 dict(slug='N5-cycle-over-orbit', truth='NEGATIVE', later='solar magnetic dynamo output; no planetary forcing established', best='OUTPUT-OF-HISTORY',
      name='ratio of the mean length of the solar activity cycle to the orbital period of the largest planet',
      definition='Mean period of the sunspot-number cycle divided by the sidereal orbital period of the largest planet.',
      carrier='the Sun\'s surface activity and the planetary system; readout = daily sunspot counts over about two centuries; planetary timing',
      units='dimensionless', value='0.94 (about 11.1 years over 11.86 years)', sigma='0.08 (individual cycles last 9 to 14 years)', source=SRC,
      ks='Sunspots come and go in a cycle of about eleven years whose individual lengths vary from about nine to fourteen years; the Sun\'s magnetic polarity reverses each cycle, so the full magnetic cycle is twice as long. The Sun is a rotating, convecting ball of ionized gas with a magnetic field. The largest planet raises tides on the Sun about a millimetre high. A proposal says the planets, chiefly the largest, set the cycle.'),
]


def run():
    order = sorted(ITEMS, key=lambda d: hashlib.sha256((SEED + '|' + d['slug']).encode()).hexdigest())
    key = {'seed': SEED, 'rule': 'POSITIVE → expected LAW-CANDIDATE; NEGATIVE → expected any disposition except LAW-CANDIDATE (best class noted, not scored)', 'items': {}}
    for i, d in enumerate(order, 1):
        hid = f'h{i:02d}'
        (HERE / f'{hid}.md').write_text(T.format(hid=hid, name=d['name'], definition=d['definition'], carrier=d['carrier'], units=d['units'], value=d['value'], sigma=d['sigma'], source=d['source'], ks=d['ks']))
        key['items'][hid] = {'slug': d['slug'], 'truth': d['truth'], 'best_class': d['best'], 'later_explanation': d['later']}
    (HERE / 'hist_key_v4.json').write_text(json.dumps(key, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({h: v['slug'] for h, v in key['items'].items()}))


if __name__ == '__main__': run()
