# Annotation task

You are an independent annotator. This single message contains exactly two inputs:
the complete card v4 (the decision procedure — read it fully first) and dossiers q01..q66.

Rules (binding): use ONLY this message, subject to the card's explicit permission (step 1, rule 3) to recall
physics for a natural dimensionless form. Do not read files on any machine, do not browse the web, do not
consult tools, memory, other documents or programme context.
If a dossier lacks a fact you need, say so in the justification and decide on what it contains.

Task: run the card's procedure on every dossier q01..q66 in order. Reply with your verdicts —
one block per item, exactly in the card's "Recording your verdict" format, including the natural_form field.
Every item gets exactly one disposition; no blank fields; no skipped items.
After all 66 blocks, print the single line
ANNOTATION-COMPLETE

No file output or commits. No extra first turn or follow-up discussion. If output stops early,
the only allowed follow-up is an output-continuation sentence naming the first missing item;
continue the same annotation in the same conversation without revising earlier blocks.
