# Corrected reliability test v4

Separately preregistered repeat: final disposition and steps 1, 2, 5 alpha = 1 exactly; 60/60 unanimous. Historical S=6/6, F=0/5; every case recognized, not blind discrimination. v3 remains FAIL.

Run scoring/v4_run.py primary and hist through the top-level reproduce.py. Unchanged checksum-pinned scorer reused from ../reliability/historical/. Draw sources are the original v3 pool, exclusions, sample, controls, quantity data and dossier definitions in draw-inputs/. Exclusion-source paths made relative; names and rules unchanged. Checker rebuilds sample/items/keys and all66 dossiers byte-for-byte. Protocol and construction logs retain scientific choices; transport identities omitted. Original seal_v4.json hashes original artifacts; provenance.json records every original and packaged hash. PACKAGE_SEAL.json verifies curated artifacts; seal_v4.py rebuilds a new seal, never the historical timestamp. JSON transport envelopes replaced by verbatim .reply.txt response files; existing verdict markdown remains authoritative. Validity receipts retain models, completion and sealed-path-only facts, not raw tool histories.

Step 0 has one category and 180/180 observed agreement; nominal alpha is undefined. The historical scorer convention returns 1 for this case, not an exact-alpha result.
