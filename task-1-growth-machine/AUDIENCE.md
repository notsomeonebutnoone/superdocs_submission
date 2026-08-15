# Audience: who, why, first ten

## Who (one group, not an industry)

**Seed-stage technical founders and founding engineers at B2B product companies with roughly 2–25 people**, who already use a coding agent daily (Cursor, Claude Code, or similar), and who still personally own:

- Investor / board updates  
- Customer proposals and SOWs  
- Security / vendor questionnaires  
- Launch posts that must also become polished one-pagers or PDFs  

They are not “people in SaaS.” They are the specific humans who ship code with an agent in the morning and re-format a proposal in Google Docs at night.

## What they do today instead of SuperDocs

| Step | Tool | Failure mode |
|------|------|--------------|
| Draft | ChatGPT / Claude chat | Great prose, no durable document |
| Transfer | Copy-paste | Tables, headings, brand styles break |
| Polish | Google Docs / Word by hand | Hours on formatting that AI already “knew” |
| Revise | New chat or scroll-back | No section-level revert; history is chat archaeology |
| Export | “Download as…” hope | Client opens a file that looks different |
| Agent loop | Coding agent stops at Markdown | Customer-facing deliverable still manual |

Chat solved *words*. It did not close the loop into the *document they already have*.

## What would genuinely make them switch

1. **Edits land in the file** — not a sidebar of text to ferry by hand.  
2. **Section precision** — “tighten risk section only” does not rewrite pricing.  
3. **Style survival** — branded tables, headers, fonts survive edit and `.docx`/PDF export.  
4. **Review gate** — proposals do not ship because an agent was confident.  
5. **Same agent surface** — optional MCP so Cursor/Claude Code can finish the doc the way it finishes the PR.  
6. **Per-message revert** — one bad instruction does not torch the afternoon.

We do **not** promise: SuperDocs browsing the live web, native e-sign, spreadsheet editing as the product, or compliance certifications not yet held.

## Why this audience (defended, falsifiable)

- **Specific enough to be wrong:** If most seed technical founders already have a chief of staff owning docs, this wedge dies. Evidence against that: public build-in-public posts still show founders writing their own updates and proposals.  
- **Reachable this week:** Public launch surfaces (Product Hunt, Show HN, Indie Hackers, company blogs) name companies and roles without needing private contact databases.  
- **Pain is adjacent to behavior they already paid for:** They already trust agents for code. Document loop is the unfinished twin.  
- **Aligned with SuperDocs’ actual wedge:** “Claude Code for documents” — not another chat window.

## How we find the first ten (find ≠ contact)

Finding is the task. Contacting is **out of scope for this round** and for this machine.

1. Pull last 30 days of public B2B launches (PH, Show HN).  
2. Filter: technical founder voice, headcount signal ≤25, sells to other businesses, document-heavy motion (sales, security, compliance, agencies).  
3. Read one public artifact (launch post, docs site, careers page).  
4. Score document-pain hypothesis (proposal-led sales, SOC2 journey, weekly investor note).  
5. Store **company + role + public URL + hypothesis** — never a private individual’s contact record for outreach execution in this round.

### Illustrative first-ten *company* shortlist shape

(Real rows used in machine batches are synthetic roles + real public companies where noted; no personal names.)

| # | Company type | Why the doc loop bites | Where they gather |
|---|--------------|------------------------|-------------------|
| 1 | Devtools seed | Security questionnaires + enterprise proposals | Show HN, Twitter/X |
| 2 | Vertical SaaS (health/fintech) | Branded proposals + policy packs | PH, LinkedIn company |
| 3 | AI agent startup | Irony: agents for customers, docs still manual | HN, Discord |
| 4 | Compliance-adjacent SaaS | Policy docs + audit packs | G2, PH |
| 5 | Boutique productized consultancy | Proposals weekly | Indie Hackers |
| 6 | Infra / observability seed | RFP responses | Show HN |
| 7 | HR / people-ops SaaS | Offer letters + policy acknowledgements | PH |
| 8 | Legaltech early | Clause work + exports to Word | LinkedIn company |
| 9 | Climate / industrial SaaS | Long SOWs | Industry newsletters |
| 10 | Education B2B | Grant narratives + decks-as-docs | IH, PH |

## What we cut

- Broad “SMBs” or “all founders”  
- Enterprise IT buyers (different motion, longer cycle)  
- Pure consumer creators  

## Machine implication

One outbound personalization system aimed at this group: public signal → enrichment fields → email a stranger would mistake for hand research → **outbox only**.
