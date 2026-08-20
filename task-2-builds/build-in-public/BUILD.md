# Weakest-section critique engine

Exact Open Task List card: **Weakest-section critique engine** (page 417).

## Job

Rank five sections of an existing proposal against a fixed approval goal, explain the ranking from the document’s wording, and rewrite only the weakest section after human review.

## Synthetic input contract

```yaml
company: Atlas Field Systems
buyer: Operations team
problem: Manual inspection reports delay handoff
scope:
  - discovery workshop
  - reporting workflow configuration
  - team enablement
timeline: Six weeks
commercial_note: Pricing remains unchanged from the approved template
```

## Instruction sequence

1. Open the approved proposal template.
2. Populate only `Executive summary`, `Current state`, `Proposed scope`, and `Timeline` from the brief.
3. Do not edit `Pricing`, legal terms, headers, footers, or brand styles.
4. Review each proposed change before accepting it.
5. Ask: “Shorten the Current state section to two paragraphs. Do not change any other section.”
6. Demonstrate per-message revert if the revision is not acceptable.
7. Export the approved result to DOCX or PDF.

## Acceptance test

- Two fresh constrained runs return complete five-section rankings.
- The selected weakest section is stable across those repeated runs, or instability is reported honestly.
- All facts come from the synthetic brief.
- Pricing and legal terms are byte-for-byte unchanged in the text layer.
- No section outside the allowed list changes.
- A reviewer can identify and reject a proposed change.
- The last instruction can be reverted without discarding earlier accepted work.
- Export opens with the template hierarchy intact.

## Evidence status

The workflow, prompt contract, authenticated SuperDocs run, failure trail, accepted Timeline edit, screenshots, and final DOCX export exist. See `TASK-1-2-COMPLETE-EVIDENCE-REPORT.pdf` for the run evidence and `EXPORT-VERIFICATION-2026-08-17.md` for the export comparison.

The export verification is a partial formatting pass. Pricing, Terms, all non-Timeline text, all 76 list items, page setup, and the seven-page count are preserved. The intended Timeline change is correctly bounded. The cover title style changed from `Title` to `Heading 1`; this limitation must remain disclosed.

Two fresh constrained-ranking replications were completed on 2026-08-17. The result did not meet the card’s stability bar: the original constrained run selected Timeline, replication A selected Next Steps, and replication B selected Current State. Replication B also displayed its numbered list strongest-to-weakest despite the requested weakest-to-strongest contract. This limitation is recorded in Post 4 and makes human selection mandatory before rewriting. Confirm that neither replication changed the document, attach both screenshots, and then the evidence package is complete. Publishing the five posts remains a candidate-owned action.
