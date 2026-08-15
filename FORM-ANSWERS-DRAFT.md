# Submission form answer worksheet

These are working drafts. Replace bracketed prompts with firsthand observations before submission.

## 1. What broke?

### SuperDocs product and documentation

The authenticated product run is still required before this answer can be finalized. During that run, record each issue in this format:

- **Action:** [what I did]
- **Expected:** [what I expected]
- **Observed:** [what happened]
- **Impact:** [cosmetic / slowed me down / blocked the build]
- **Evidence:** [screenshot, file, or reproducible steps]
- **Reported through:** [in-app bug button or task email]

Fresh-eyes issues visible on the public surfaces, to confirm against the live product:

- The marketing page mixes a clear user promise (“AI edits inside the document”) with a very broad developer/platform story. A first-time visitor must choose among web app, API, MCP, white-label, autonomous agents, memory, images, and many document capabilities before seeing one complete end-to-end workflow.
- The site contains several precise speed, usage, endpoint, developer-hour, and token-saving claims. These need prominent methodology or links to evidence so the strongest claims are independently understandable.
- Deployment language mixes “now,” “soon,” and “on request” on the same path. A compact availability matrix would make shipped versus planned capabilities easier to distinguish.
- The docs overview is strong at routing four user types, but the first screen could link one runnable end-to-end example for each path, including expected output, error handling, review, and export.

### My own machine

My first recorded machine attempt produced a false positive: a prospect’s public SOC2 context was interpreted as a SuperDocs certification claim. I scoped the checker to the product-claim section, added a regression test, and reran both batches. This was a bug in my submission system, not in SuperDocs.

## 2. What one number would you watch every morning, and why?

**Proposed number: new workspaces that reach a verified finished-document event within 24 hours of signup.**

A finished-document event means the workspace completes an AI edit, reviews or accepts the result, and exports or successfully reopens the edited document. Signup volume alone can hide failure to reach value, while raw edit counts can reward experimentation without completion. This number joins acquisition, activation, trust, and the product’s core promise: the work lands in a usable document. I would segment it by web app, REST API, MCP, and agent self-signup, then inspect the largest drop-off daily.

## 3. Five features to build next, in order, and one thing to drop

1. **First-edit reliability and recovery.** Make the first instruction consistently fast and successful, with clear retry state and actionable errors.
2. **Export-fidelity regression coverage and visible guarantees.** Test representative DOCX structures and show users what was preserved or degraded before download.
3. **Review and change provenance.** Make section-level diffs, source references, accept/reject, and per-message revert unmistakable for high-stakes documents.
4. **Workflow-sized MCP experiences.** Ship curated tool subsets, tested recipes, and safer approval boundaries for Claude Code, Cursor, VS Code, and Codex rather than exposing every tool equally.
5. **Reusable organization templates and policy context.** Make a team’s approved document shapes, terminology, and reusable source material easy to govern and apply.

**Drop or defer:** broad document-management/archive positioning. SuperDocs is strongest as the editing and execution layer. Competing as a general DMS would blur the wedge and add permissions, retention, and governance complexity before the core edit-review-export loop is undeniable.

## 4. How would you make the entire GTM operation run itself?

I would build one observable system with four loops, not a collection of disconnected content agents.

1. **Signal loop:** collect public company events, product launches, job posts, technology signals, and document-heavy workflow evidence. Normalize each item into a company, role, source, date, confidence, and hypothesized document pain. Never store scraped private-person contact details.
2. **Audience and message loop:** score signals against explicit audience definitions, draft channel-appropriate assets, and run claim, privacy, duplication, and tone checks. A human approves audience changes, product claims, public posts, and any outbound experiment. Sending remains disabled unless SuperDocs explicitly authorizes a controlled campaign.
3. **Distribution loop:** publish approved owned-channel material, maintain integration assets for agent ecosystems, and create workflow pages from evidence-backed use cases. Each asset has one audience, one intended behavior, a source trail, and an expiry/revalidation date.
4. **Learning loop:** join source, asset, activation, retained usage, and qualified-conversation data. Agents summarize leaks and propose one-variable experiments. Humans choose the experiment, review sensitive output, and stop loops when quality, safety, or marginal return crosses a threshold.

The practical stack can start with scheduled Python or n8n workflows, a small relational store, product analytics, a content/research queue, and evaluation jobs. Every run should be resumable and idempotent. The first failures at scale will be stale research, overconfident personalization, duplicated work, claim drift, and review overload, so source freshness, deterministic IDs, claim allowlists, sample-based quality scoring, and queue limits belong in version one.

## 5. What would you change on superdocs.app and docs.superdocs.app?

### Website

- Keep the opening “edit inside the document” contrast, then show one complete interactive workflow from upload/template through targeted edit, review, revert, and export before expanding into platform breadth.
- Split the page earlier into two explicit journeys: “edit my documents” and “add document AI to my product.” Preserve a third, smaller route for agent/MCP users.
- Add an availability and evidence table for major capabilities and quantitative claims. Link each measured claim to methodology and label preview, request-only, and planned features consistently.
- Replace some feature inventory with three concrete outcome pages, such as proposals, contract review, and policy/report updates, each showing inputs, approval boundary, exported output, and limitations.
- Clarify the relationship between the free web-app allowance and API usage/pricing at the decision point rather than making visitors infer it across sections.

### Documentation

- Keep the useful persona routing table, but give every route one copy-paste golden path with sample input, expected response, review step, export step, and cleanup.
- Add a prominent “production checklist” covering idempotency, asynchronous jobs, retries, rate limits, secret handling, human approval, and destructive/revert operations.
- Publish a capability-status reference that maps web app, REST, and MCP parity and identifies preview or request-only features.
- Put a minimal workflow-oriented MCP tool set before the full tool catalog so agents select tools reliably.
- Add tested examples for a complete document lifecycle rather than focusing only on the first edit.

## Final form-only fields

- **Approximate AI-built percentage:** [enter an honest estimate]
- **How I directed AI:** I set the audience, constraints, product-claim ceiling, channel choice, acceptance criteria, and cuts; used AI for research synthesis, implementation, tests, copy variants, and verification; and retained human responsibility for authenticated product use, publishing, voice recordings, and final claims.
- **What works:** The offline machine, two-batch reproducibility, safety checks, landing page, measurement, ecosystem map, use-case research, posting drafts, clip plan, demo script, and one-page draft.
- **What remains incomplete:** Authenticated build evidence, actual publication links, both human-voice recordings, selected-card/destination confirmation, repository remote/collaborator setup, and final form submission.
