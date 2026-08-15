# From agent draft to finished document

## The bet

SuperDocs should begin with a behavior, not an industry: seed-stage technical founders and founding engineers who already use coding agents every day but still personally finish proposals, investor updates, security questionnaires, and launch one-pagers. Their agent can produce words. The workflow breaks when those words must become a reviewed, branded document that another company can open.

This audience is useful because it is specific, reachable through public launch signals, and falsifiable. The wedge fails if document work is already delegated or if Markdown is genuinely the final output. It wins when a technical founder recognizes the chat-to-document handoff as an unfinished version of a workflow they already automated for code.

## The machine

I built one channel deeply: a draft-only outbound personalization machine. It takes a researched CSV row, validates it, enriches the document-pain hypothesis, creates a company-and-role message, checks product claims, and writes a Markdown draft to `outbox/`. It has no transport or send integration. `SEND_MODE` is hard-coded off and the runner refuses to continue if that changes.

The system ran on two fresh synthetic batches. The recorded result is sixteen inputs, sixteen drafts, no overlap, no risk flags, no final claim-check failures, and zero messages sent. Those are machine metrics, not demand metrics. Because outreach is prohibited, reporting opens, replies, meetings, or pipeline would be fiction.

The first attempted recording also exposed a real quality bug. A prospect's public SOC2-journey signal triggered the forbidden-claim checker even though the copy did not claim SuperDocs was certified. I narrowed checking to the product-claim portion, added a regression test, and regenerated both runs. The correction is documented rather than erased from the narrative.

## The piece

The landing page is written for the same audience and sells one behavior change: do not paste the last mile. It contrasts the current loop of draft, paste, repair, and repeat with a document loop of open, target, review, and export. It uses only current product surfaces: in-document edits, review, version history with per-message revert, Word/PDF export, and optional API/MCP access.

## The builds

The build-in-public project is a Proposal AI mini-workflow on SuperDocs, not a proposal-generator clone. It starts from an existing branded template and a structured synthetic brief. Instructions may populate named sections, but they may not alter pricing, legal text, or brand styles. A human reviews changes, can revert the instruction that missed, and exports only the approved document. Five posting drafts tell the plan, first failure, decision change, measured result, and finished workflow; the opening post discloses candidate affiliation.

The ecosystem map prioritizes distribution where SuperDocs' remote MCP and existing plugin assets already fit: Claude Code, Cursor, VS Code, and direct Codex before heavier hosted directories or custom REST adapters. The real-company use cases use public workflow evidence, but label product fit and conversation openers as hypotheses. No individual is named and no company is contacted.

## What I would test next

Once outreach is explicitly permitted, I would manually review a small set against a fixed quality rubric and test one variable: broad “document loop” language versus workflow-specific language. Qualified replies would be the primary signal. Negative replies and claim accuracy would be guardrails. I would not add channels until this audience-message pair earns evidence.

The submission's central choice is restraint: one audience, one machine, two reproducible runs, one piece, honest measurement, and clear boundaries between what is built, what is researched, and what still requires a human recording or market test.
