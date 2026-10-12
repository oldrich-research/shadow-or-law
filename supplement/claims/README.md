# claims

Curated research artifact; CC-BY-4.0. Source hash and adaptation: root provenance.json.

`CLAIM_REGISTER.tsv` is the complete 158-claim register of the paper with grades; Appendix F of the paper prints its 67
core cards. The register has one card per core claim (`C01`–`C67`), operational role (`ROLE-1`–`ROLE-7`), methodological
guard (`MOVE-1`–`MOVE-10`) and historical census row (`ROW-c01`–`ROW-c74`, rows c01–c74 of Appendix A), each with its
grade and standing.

| column | meaning |
|---|---|
| `id` | card identifier |
| `claim` | the claim as the register words it |
| `grade` | the grade defined in Appendix F; census-row cards carry `adjudicated` |
| `standing` | the claim's standing, as in the Standing column of Appendix F |

Tab-separated UTF-8 text with one header row; no field contains a tab, a line break or a double quote. Curated from the
paper's machine register: the cards' source references and receipt identifiers are not included. As Appendix F states,
neither measured nor recomputed upgrades a claim into a physical mechanism.
