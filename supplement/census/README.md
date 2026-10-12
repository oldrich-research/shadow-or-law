# census

Curated research artifacts; CC-BY-4.0. Source hashes and adaptations: root provenance.json.
Outputs reproduce a constructed programme sample, not a population estimate or proof of ontology.
See root README.md for runnable entry points.

## Files

- `historical_census.csv`: the census CSV (byte-identical to the paper's `census.csv`).
- `CENSUS_TABLE_74.tsv`: the adjudicated 74-row table (mapped historical reference, blind G/M/C verdicts, adjudicated disposition).
- `census_adjudication.tsv`, `ADJUDICATION_CENSUS.md`: the 26 adjudicated rows and their adjudication record.

## Column dictionary of `historical_census.csv` (the paper's `census.csv`)

Historical dispositions and domain memberships retain the original exposition grouping. The paper's census appendix
prints the frozen mapped reference, blind G/M/C verdicts and adjudicated disposition; these are distinct fields, not
replacements for the historical grouping.

| column | meaning |
|---|---|
| `id` | row identifier c01–c74, as in Appendix A of the paper |
| `name` | the programme-built row |
| `atlas_line` | the row's line number in the historical catalogue |
| `ii06_group` | the row's group label in the original historical exposition |
| `historical_disposition` | that group as a short historical label (History, Governed, Convention, Model, Unmapped, Epoch, Retained) |
| `domain` | the domain grouping used for Fig. 2 of the paper |
| `reason`, `reopen` | concise historical reason and reopening condition |
| `lane_1`, `lane_2`, `lane_3` | the blind first-stop verdicts of lanes G, M and C (OpenAI gpt-6.1-sol, Google gemini-3.1-pro, Anthropic claude-opus-5-5) |
| `v3_adjudication` | the adjudicated disposition |

The two historical column names `atlas_line` and `ii06_group` are kept unchanged so that every consumer of the file in
the reproducibility release stays valid.
