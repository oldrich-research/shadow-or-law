# P1.5 v4 — historical yes-branch arm (PROTOCOL_V4 §Historical arm)

S = 6/6 positives with majority LAW-CANDIDATE · F = 0/5 negatives with majority LAW-CANDIDATE → **YES-BRANCH WORKS**
(YES-BRANCH WORKS: S ≥ 5 and F ≤ 1 · PARTIAL: S ∈ {3, 4} and F ≤ 1 · FAILS otherwise)

per lane: L-G (OpenAI gpt-6.1-sol) S 5/6 F 0/5, L-M (Google gemini-3.1-pro) S 6/6 F 0/5, L-C (Anthropic claude-opus-5-5) S 6/6 F 0/5
recognized by at least one lane: 11/11; S, F over items no lane recognized: 0, 0 (items: none)

| item | case | truth | L-G | L-M | L-C | majority |
|---|---|---|---|---|---|---|
| h01 | P1-combining-volumes | POSITIVE | LAW-CANDIDATE | LAW-CANDIDATE | LAW-CANDIDATE | LAW-CANDIDATE |
| h02 | N2-disc-ratio | NEGATIVE | EPOCH-DEPENDENT | EPOCH-DEPENDENT | EPOCH-DEPENDENT | EPOCH-DEPENDENT |
| h03 | P6-moment-anomaly | POSITIVE | LAW-CANDIDATE | LAW-CANDIDATE | LAW-CANDIDATE | LAW-CANDIDATE |
| h04 | N5-cycle-over-orbit | NEGATIVE | OUTPUT-OF-HISTORY | OUTPUT-OF-HISTORY | OUTPUT-OF-HISTORY | OUTPUT-OF-HISTORY |
| h05 | N4-days-per-year | NEGATIVE | EPOCH-DEPENDENT | EPOCH-DEPENDENT | EPOCH-DEPENDENT | EPOCH-DEPENDENT |
| h06 | P5-closed-counts | POSITIVE | OUTPUT-OF-HISTORY | LAW-CANDIDATE | LAW-CANDIDATE | LAW-CANDIDATE |
| h07 | P4-splitting-factor | POSITIVE | LAW-CANDIDATE | LAW-CANDIDATE | LAW-CANDIDATE | LAW-CANDIDATE |
| h08 | N3-g-over-pi2 | NEGATIVE | EPOCH-DEPENDENT | CONVENTION-BOUND | CONVENTION-BOUND | CONVENTION-BOUND |
| h09 | N1-orbit-gap-growth | NEGATIVE | OUTPUT-OF-HISTORY | OUTPUT-OF-HISTORY | OUTPUT-OF-HISTORY | OUTPUT-OF-HISTORY |
| h10 | P3-line-ratio | POSITIVE | LAW-CANDIDATE | LAW-CANDIDATE | LAW-CANDIDATE | LAW-CANDIDATE |
| h11 | P2-period-size-exponent | POSITIVE | LAW-CANDIDATE | LAW-CANDIDATE | LAW-CANDIDATE | LAW-CANDIDATE |
