# Submission-ready form answers

These answers reflect the completed repository evidence and five published build-in-public posts. Paste them into the corresponding form fields, shortening only if the form imposes a character limit.

## 1. What broke?

### SuperDocs product and documentation

The authenticated weakest-section experiment exposed four firsthand product issues:

- **Broad ranking instruction did not complete.** Action: requested a weakest-to-strongest ranking grounded in the document without edits. Expected: an ordered analysis. Observed: a rephrase response followed by progress statements with no ranking. Impact: slowed the build; resolved by narrowing the task to five named sections and an explicit output contract. Evidence: `Screenshot 2026-08-15 152045.png`.
- **Change summary was not grounded in document state.** Action: asked for a breakdown after the stalled ranking. Expected: a statement that no changes existed. Observed: the response acknowledged no diff, then described revisions that a normalized full-text comparison proved had not occurred. Impact: material trust issue; required independent document comparison. Evidence: `Screenshot 2026-08-15 152102.png` and `Screenshot 2026-08-15 152111.png`.
- **Repeated rankings were unstable.** Action: ran the same constrained five-section ranking prompt twice in fresh sessions against the unchanged proposal. Expected: a defensible and stable weakest-section result. Observed: replication A selected Next Steps, replication B selected Current State, and the earlier constrained run selected Timeline. Replication B also displayed the numbered list strongest-to-weakest despite the prompt defining 1 as weakest. Impact: prevents automatic weakest-section rewriting; a human must choose among the critiques. Evidence: two 2026-08-17 replication captures.
- **DOCX export changed an unrelated title style.** Action: exported the reviewed proposal and compared it with the baseline. Expected: protected wording, list structure, and unrelated styles to remain unchanged. Observed: Pricing, Terms, all non-Timeline text, and all 76 list items were preserved, but the cover title changed from Word's `Title` style to `Heading 1`. Impact: partial formatting failure that requires a manual export check. Evidence: `EXPORT-VERIFICATION-2026-08-17.md` and the baseline/final comparison files.

### My own machine

My first recorded machine attempt produced a false positive: a prospect’s public SOC2 context was interpreted as a SuperDocs certification claim. I scoped the checker to the product-claim section, added a regression test, and reran both batches. This was a bug in my submission system, not in SuperDocs.

## 2. What one number would you watch every morning, and why?

**Proposed number: new workspaces that reach a verified finished-document event within 24 hours of signup.**

A finished-document event means the workspace completes an AI edit, reviews or accepts the result, and exports or successfully reopens the edited document. Signup volume alone can hide failure to reach value, while raw edit counts can reward experimentation without completion. This number joins acquisition, activation, trust, and the product’s core promise: the work lands in a usable document. I would segment it by web app, REST API, MCP, and agent self-signup, then inspect the largest drop-off daily.

## 3. Five features to build next, in order, and one thing to drop

1. **First-edit reliability and recovery.** Make the first instruction consistently fast and successful, with clear retry state and actionable errors.
2. **Export-fidelity regression coverage and a visible fidelity report.** Test representative DOCX structures and show users what was preserved or degraded before download.
3. **Review and change provenance.** Make section-level diffs, source references, accept/reject, and per-message revert unmistakable for high-stakes documents.
4. **Workflow-sized MCP experiences.** Ship curated tool subsets, tested recipes, and safer approval boundaries for Claude Code, Cursor, VS Code, and Codex rather than exposing every tool equally.
5. **Reusable organization templates and policy context.** Make a team’s approved document shapes, terminology, and reusable source material easy to govern and apply.

**Drop or defer:** broad document-management/archive positioning. SuperDocs is strongest as the editing and execution layer. Competing as a general DMS would blur the wedge and add permissions, retention, and governance complexity before the core edit-review-export loop is undeniable.

**Frictions and bugs to fix immediately:** Ground change summaries in the actual document diff; make stalled or incomplete requests fail clearly; enforce requested ranking direction; and prevent unrelated DOCX styles from changing during export.

## 4. How would you make the entire GTM operation run itself?

I would build one observable system with four loops, not a collection of disconnected content agents.

1. **Signal loop:** collect public company events, product launches, job posts, technology signals, and document-heavy workflow evidence. Normalize each item into a company, role, source, date, confidence, and hypothesized document pain. Never store scraped private-person contact details.
2. **Audience and message loop:** score signals against explicit audience definitions, draft channel-appropriate assets, and run claim, privacy, duplication, and tone checks. A human approves audience changes, product claims, public posts, and any outbound experiment. Sending remains disabled unless SuperDocs explicitly authorizes a controlled campaign.
3. **Distribution loop:** publish approved owned-channel material, maintain integration assets for agent ecosystems, and create workflow pages from evidence-backed use cases. Each asset has one audience, one intended behavior, a source trail, and an expiry/revalidation date.
4. **Learning loop:** join source, asset, activation, retained usage, and qualified-conversation data. Agents summarize leaks and propose one-variable experiments. Humans choose the experiment, review sensitive output, and stop loops when quality, safety, or marginal return crosses a threshold.

The practical stack can start with scheduled Python or n8n workflows, a small relational store, product analytics, a content/research queue, and evaluation jobs. Every run should be resumable and idempotent. The first failures at scale will be stale research, overconfident personalization, duplicated work, claim drift, and review overload, so source freshness, deterministic IDs, claim allowlists, sample-based quality scoring, and queue limits belong in version one.

## 5. What would you change on superdocs.app and docs.superdocs.app?

Research basis: the public pages at `https://superdocs.app` and `https://docs.superdocs.app` were re-checked on 2026-08-20.

### Website

- Keep the opening “edit inside the document” contrast, then show one complete interactive workflow from upload/template through targeted edit, review, revert, and export before expanding into platform breadth.
- Consolidate the overlapping audience and integration sections into three persistent journeys: edit my documents, add document AI to my product, and connect my agent. Keep the same labels from the first decision point through the final call to action.
- Add an availability and evidence table for major capabilities and quantitative claims. Link measured claims to methodology and label available, request-only, coming-soon, and roadmap features consistently—especially where white-label embedding and deployment options are described.
- Replace some feature inventory with three concrete outcome pages, such as proposals, contract review, and policy/report updates, each showing inputs, approval boundary, exported output, and limitations.
- Use one unit consistently when describing the free allowance: the homepage alternates between “edits” and “AI operations,” while the pricing explanation applies the allowance across the web editor, API, and MCP.

### Documentation

- Keep the useful persona routing table, but give every route one copy-paste golden path with sample input, expected response, review step, export step, and cleanup.
- Add a prominent “production checklist” covering idempotency, asynchronous jobs, retries, rate limits, secret handling, human approval, and destructive/revert operations.
- Publish a capability-status reference that maps web app, REST, and MCP parity and identifies preview or request-only features.
- Put a minimal workflow-oriented MCP tool set before the full tool catalog so agents select tools reliably.
- Add one curated, tested example for the complete document lifecycle alongside the existing quickstarts: create or upload, edit, review, revert, export, and reopen.

## Final form-only fields

- **Demo video:** https://drive.google.com/file/d/1LSYa400C1j5kwrwHbQSgWn_HPv9AMvAs/view?usp=sharing
- **Approximate AI-built percentage:** Approximately 85%. AI produced most of the initial research synthesis, implementation, tests, copy variants, and documentation. I directed the audience choice, constraints, evidence standard, authenticated product experiments, publishing decisions, review judgments, recordings, and final claims.
- **How I directed AI:** I set the audience, constraints, product-claim ceiling, channel choice, acceptance criteria, and cuts; used AI for research synthesis, implementation, tests, copy variants, and verification; and retained human responsibility for authenticated product use, publishing, voice recordings, and final claims.
- **What works:** The offline machine and its reproducible two-batch runs; deterministic safety and claim checks; the responsive audience landing page; honest measurement plan; agent-ecosystem map; ten real-company use-case hypotheses; authenticated weakest-section experiment; review and export verification; and all five published build-in-public posts. The assigned card is **Weakest-section critique engine**.
- **What remains incomplete:** Final submission packaging: add the separate per-message-revert clip link, invite `o-kadam` to the private repository, and submit the completed Google Form. No real-company outreach was performed, so demand metrics remain intentionally unproven.
