# U1 lineup arm — public scientific protocol

Scientific protocol excerpt/adaptation of the frozen 2026-10-07 protocol. Original source SHA256 in provenance.json.
Operational administration and platform implementation removed. Seat/judge stimuli and rubric below retained verbatim.
Preregistration, including decision thresholds, in LEAD_PREREG.md; no threshold changed after outputs.

## Contamination and assignment

Seats and judge received only the experimental packet, not project memory or the flagship identity.
Tools and external lookups forbidden; any such use invalidated the relevant run. Each seat reported recognition.
Recognition of (4/3,21,5/2) as a known physical formula excluded that seat under the preregistered rule.
Judge recognition required rejudging with another family. No final seat or judge reported recognition.

ORDER_1: OpenAI gpt-6.1-sol, high thinking; ORDER_2: Google gemini-3.1-pro, high thinking;
ORDER_3: Anthropic claude-opus-5-5, available default effort (not separately verified high).
A contaminated initial route was rejected before C's valid output. C's valid route exposed a project
working-directory label, but no substantive project context; this limited exposure is disclosed, not erased.
No tools were used by the valid seats. Different output-delivery parts are not different independent seats.

## Seat prompt (verbatim; {TABLE} = the seat's ORDER_j.md table, rows L01–L40)
You are a mathematical physicist with broad knowledge of Lie theory, representation theory, heat kernels, partition functions, lattices and quantum field theory.

Below are forty formulas, each of the form f(x) = c · x^n · e^(−k·x), where x is a small positive parameter and c, n, k are the given numbers (k may be negative).

Task: for EACH formula, construct the best structural account you can: the most natural mathematical object and standard computation from which the triple (c, n, k) follows. A strong account
- names ONE object (for example a compact Lie group or algebra, a homogeneous space, a lattice, a representation, a partition function or heat kernel, a counting problem);
- derives the power n from that object;
- derives the slope k from the SAME object with standard conventions, stating every normalization, metric, time scaling or other choice made;
- derives the prefactor c from it if possible;
- is mathematically correct.
Different formulas may use different objects. Several formulas may admit accounts of similar quality; do not force one. If you find no account worth stating, write "no account".

Rules: work from your own knowledge only — no tools, files, web search or memory search. Give every formula comparable effort; the order is random and no formula is special. Mark any choice that is not forced as "chosen to fit".

Output (Markdown), one block per formula in the given order:
### L01
- object: …
- n: how it follows, or "not derived"
- k: how it follows with conventions, or "not derived"
- c: how it follows, or "free" / "partly"
- derivation: at most 120 words, key numbers computed
After the forty blocks:
### Recognition
Do any of these formulas look familiar from published literature or known results, as a formula for a specific physical or mathematical quantity? List ids and what you think each is; "none" if none.

{TABLE}

## Judge packet

Judge: OpenAI gpt-6.1-sol, high thinking. Family overlap with seat G accepted prospectively:
rank statistics compare formulas within a seat; a per-seat preference can shift all its scores together.
Every valid seat account was reproduced verbatim, with seat identity/order IDs removed. Items shuffled with
numpy default_rng(20261017); six repeated items added for test–retest. Final valid judge received all 126
items in one initial packet with no later context-bearing follow-up. BATCH_1–3 preserve the component inputs.

- judge prompt (verbatim; {ITEMS} = the batch):
You are a strict referee in mathematical physics. Each item below gives a formula f(x) = c · x^n · e^(−k·x) and an account that claims to derive (c, n, k) from a mathematical object. Score each account independently with this rubric, exactly:
per account, P power forced by the stated object (0/1/2) · S slope forced by the SAME object with a standard clock and normalization (2 = standard conventions only, 1 = one non-standard choice, 0 = fitted or unstated) · U one object for n and k (0/1/2) · C prefactor (0 free, 1 partly, 2 forced) · V mathematical correctness checked by the judge (0/1/2); score = P + S + U + C + V (0–10).
Check the mathematics yourself (dimensions, root data, Casimirs, volumes, any number the account computes); an account whose key number is wrong gets V = 0 and cannot score 2 on the component that depends on it. "no account" scores 0 on every component. Judge the account, not the formula; do not reward elegance that is not derived. Work from your own knowledge only — no tools.
Output one JSON object per line: {"id": "J001", "P": 0, "S": 0, "U": 0, "C": 0, "V": 0, "score": 0, "note": "≤ 25 words"}. After the last item of the last batch, one line: {"recognition": "<any formula you recognize as a known physical formula, or none>"}.
{ITEMS}

## Scoring and statistics (prereg rule unchanged)
- per seat: flagship rank among its 40 accounts by judge score (rank 1 = highest; mid-rank for ties).
- per formula: mean judge score over non-recognizing valid seats; count decoys with mean ≥ the flagship's mean.
- test–retest: report agreement of the 6 repeated items (exact score match count, mean |Δ|); no rule depends on it.
- void/rerun conditions: prereg "invalid run" + tool use + missing blocks (a seat output lacking ≥ 4 of 40 blocks → rerun that seat once).

## Scientific delivery/validity addenda (2026-10-07)

04:38Z: an initial C route loaded project context in its probe, so it was rejected; clean route substituted.
05:12Z: interrupted calls returning no complete output were failures, not additional seat samples.
The first complete G output was retained; no tool call; 40 blocks plus recognition, none.
05:34Z: M returned 40 no-account blocks with recognition none; valid and not resampled for its answer.
C's incomplete interrupted calls did not count as outputs. First complete valid output was retained.
05:36Z: C delivered L01–10,11–20,21–30,31–40 plus recognition in one conversation, with all forty
formulas supplied initially. Delivery instruction and continuations preserved in the seat prompt receipts.
Zero tool use required. Its effort parameter was not independently selectable; this difference remains disclosed.
06:51Z: first judge session was voided because a later turn loaded project context and called tools.
Earlier outputs in that session were not pooled; context validity of its second part was uncertain.
The researcher had seen the earlier uniform scores before the rerun; final rerun retained whatever its outcome.
Valid rerun: same 126 items/text/rubric, one fresh isolated packet, zero tool calls, no follow-up context.
The extra packet header was: "All items J001–J126 in one batch (this is the last batch):".
All score records used for printed ranks are in judge_scores.jsonl; JMAP.json connects them to formulas/seats.
