# Decision log

## Audience

**Chosen:** Solo technical founders and founding engineers at seed-stage B2B product companies (2–25 people) who already run coding agents (Cursor, Claude Code, Copilot Workspace-class tools) and still own investor updates, customer proposals, security questionnaires, and launch narratives themselves.

**What they do today instead of SuperDocs**

1. Draft in ChatGPT / Claude chat.
2. Paste into Google Docs or Word.
3. Fix formatting by hand.
4. Re-copy when the next revision is needed.
5. Lose section-level history; “undo” means hoping the chat still has the right turn.

**What would make them switch**

- Edits land *in* the document (not beside it).
- Section-scoped changes without reformatting the whole file.
- Export that keeps tables, headers, and branding (`.docx` / PDF).
- Review gate so nothing ships unapproved.
- Optional: coding agent talks to SuperDocs over MCP so the same agent that writes code can finish the customer-facing doc.

**How to find the first ten (find only — never contact in this round)**

| Source | Signal | How we’d shortlist |
|--------|--------|--------------------|
| Product Hunt / Show HN launches this month | Solo or tiny team, B2B, technical founder posting | Public launch post + company site |
| Indie Hackers “launched” / revenue milestones | Founder writes their own updates | Public post text |
| GitHub READMEs of young B2B tools | “Built with Cursor” / agent mentions in about | Public repo |
| Public LinkedIn company pages | Headcount 2–25, recent “we’re hiring founding…” | Company only, no personal scrape for outreach storage |

**Ten example companies (public, illustrative — not a contact list)**

1. Linear-adjacent tooling startups on PH
2. Early developer-tools on Show HN
3. Vertical SaaS seeds in fintech/compliance
4. Security startups mid-questionnaire hell
5. Agency-product hybrids shipping proposals weekly  
*(Concrete researched rows live in Task 3 and machine batch CSVs.)*

## Channel

**Outbound personalization machine** — one channel, built to run twice on fresh batches without patching.

Why not content/SEO first: this audience already lives in agent tools; a sharp, researched note that names their *document* pain beats ranking for generic “AI document editor” keywords they will never type. Content can come later as extra credit; it is not the floor machine.

## Restraint

All machine outputs write to `outbox/` only. `SEND_MODE` is hard-coded off. README states the bright line. Demo video shows drafts, never a real send.

## Product claim ceiling

Only promise what SuperDocs does today per product surfaces we verified:

- In-document AI editing with section precision
- Style-preserving export (docx, PDF, HTML, MD, text)
- Review / proposed changes before landing
- Multi-document workspace, search, summarize
- Version history and **per-message revert**
- REST API + MCP for agents
- Not: live web browse inside SuperDocs, native e-sign, spreadsheet product, DMS, guaranteed PII wipe without human review, SOC2-as-current-fact (roadmap language only if we mention security)

## Build-in-public subject

Five posts documenting the exact Open Task List card **Weakest-section critique engine** (page 417): fixed evaluation goal → ranked sections with reasons → human check → weakest-section rewrite → review → integrity check. The Atlas Field Systems proposal is the synthetic test document. The earlier “Proposal AI workflow” label was too broad and has been retired.
