# Proposal AI mini-workflow

## Job

Turn a structured customer brief into a reviewable proposal based on an existing branded template. This is a workflow design for SuperDocs, not a separate proposal product.

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

- All facts come from the synthetic brief.
- Pricing and legal terms are byte-for-byte unchanged in the text layer.
- No section outside the allowed list changes.
- A reviewer can identify and reject a proposed change.
- The last instruction can be reverted without discarding earlier accepted work.
- Export opens with the template hierarchy intact.

## Evidence status

The workflow, prompt contract, and acceptance test are complete. Product screenshots and an end-to-end SuperDocs recording still require a human-operated authenticated session; do not claim those assets exist until recorded.
