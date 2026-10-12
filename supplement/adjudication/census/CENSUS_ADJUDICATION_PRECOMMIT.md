# Census arm lead adjudication rubric · 2026-10-07T17:16:44Z · before L-C output

status: frozen before the L-C census reply exists. Lead saw L-G and L-M census verdicts (exploratory two-lane count only:
G=M 59/74, G=ref 49/74, M=ref 50/74); no label, card, dossier, reference, leak list or metric changes.

scoring: frozen scorer via `scoring/v3_run.py census`, three valid lanes; headline alpha = non-leak rows (CENSUS_ARM.md);
leak rows reported separately; per-step alpha 0,1,2,5. Descriptive arm: no pass threshold.

per row where majority != reference (and every row with no majority):
- read sealed dossier cNN + card v3 + reference basis (atlas line, II_06 group); record: carrier/readout; natural
  dimensionless form; frame/epoch; static vs history; card step reached; disputed sentence.
- verdict, one of: REFERENCE-STANDS (lanes misapply a named card step) · CENSUS-FAULTED (card applied as written gives
  the majority disposition; paper prints adjudicated disposition, old one beside it) · DOSSIER-DEFECT (dossier omits or
  distorts what decides the row; report, no forced verdict) · AMBIGUOUS (card admits both; name the missing rule for v4).
- own rows (the 13 non-refused: flagship, m_e/M_Pl, d6/d7/d8, delta_CP, R_T/R_J, P2-Chem, G-alpha, ladder, m_bb, alpha,
  M_Pl): same rule, no special pleading. Card-consistent disposition of a programme relation whose inputs are free
  parameters of current theory with no mechanism = OUTPUT-OF-HISTORY + reopen condition (mechanism); the programme's
  forward predictions stay registered separately and are not evidence for a census disposition.
- refused/non-refused headline: paper prints adjudicated counts as primary, historical exposition counts (61/74, 44
  history) beside them; never merge the two.

reporting: majority vs reference accuracy + 7x7 confusion; adjudication table; lane verdicts beside each adjudicated row;
Operational notification instruction removed from release copy; scientific rubric above unchanged.
