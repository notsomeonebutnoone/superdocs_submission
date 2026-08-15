# Proposal AI build-in-public series

These are posting drafts, not claims that anything was published. Suggested cadence is days 1, 3, 5, 8, and 10. Screenshots must use synthetic proposal content and exclude API keys.

## Post 1: the plan

**Disclosure:** I am a candidate for a growth role at SuperDocs, and I am building this as part of the process.

Coding agents can produce a strong proposal draft. The awkward part starts one minute later: paste it into a branded document, repair the table and headings, route the changes for review, then do it again after feedback.

Over the next ten days I am testing a small Proposal AI workflow on SuperDocs:

`structured brief → existing template → targeted edits → review → Word/PDF export`

The constraint is the point: no proposal generator clone and no fake automation. The output has to be the file a customer can actually open.

I will share the first failure, the decision it changes, the measured run, and the finished workflow.

**Visual:** one synthetic brief beside its branded proposal template.

## Post 2: the first breakage

The first version failed before the AI did.

I treated the proposal as blank-page generation. That produced decent words and a bad artifact: the pricing table, section order, and brand styles became cleanup work again.

The fix was to invert the workflow. Start from the real template, then make narrow instructions against named sections. The template is not decoration at the end. It is part of the input.

New test: if scope changes, can I update scope without touching pricing or the cover page?

That is a much harder and more useful standard than “did the model write a proposal?”

**Visual:** synthetic before/after showing a whole-document rewrite versus a section-scoped edit.

## Post 3: the decision that changed

I removed “one-click proposal” from the concept.

The risky moment is not generation. It is the last confident change before a customer sees the file. So review is now a required stage, not an optional polish step.

The workflow is deliberately less magical:

1. Fill the known sections from a structured brief.
2. Ask for a targeted revision.
3. Review the proposed change in context.
4. Export only after approval.

The product decision: optimize for controlled edits, not maximum autonomy. A proposal workflow earns trust by making the boundary visible.

**Visual:** synthetic review state with one accepted and one rejected change.

## Post 4: the measured result

The surrounding growth machine has now completed two fresh offline runs: sixteen synthetic company-and-role rows became sixteen draft messages, with zero sends, zero risk flags, and zero product-claim failures in the final runs.

One useful failure came first. The claim checker mistook a prospect's public SOC2 context for a SuperDocs claim. I narrowed the check to the product section and added a regression test before rerunning both batches.

This does not prove demand. It proves the workflow is reproducible and the safety boundary is testable. Demand is the next permitted experiment, not a number to invent now.

**Visual:** `MEASUREMENT.md` and the two run summaries, with no contact data.

## Post 5: the finished workflow design

Finished in this repository: the prompt contract, acceptance test, and recording plan for a Proposal AI mini-workflow that starts from a real document shape instead of ending with a block of chat text. The authenticated product run remains the proof step before this draft can be published.

The path is:

`brief → template → section edit → human review → revert if needed → DOCX/PDF`

What survived the build:

- The template comes first.
- Instructions target named sections.
- Review stays in the critical path.
- Per-message revert is the recovery mechanism.
- Export is part of “done.”

What I cut: autonomous sending, live customer data, and the fiction that generated prose equals a finished proposal.

The build notes, prompt contract, and synthetic acceptance test are documented in the repository. I will call the product build finished only after the authenticated acceptance test passes.

**Visual:** a short synthetic screen recording of the complete workflow. Do not reuse the assigned product-feature clip publicly.

## Posting checklist

- Keep the candidate disclosure in post 1.
- Use only synthetic customer and proposal content.
- Verify every capability against the current product before posting.
- Do not imply the posts were published until they are.
- Record links and dates here only after a human publishes them.
