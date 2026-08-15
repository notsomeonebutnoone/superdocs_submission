# Progress log

## 2026-08-06 — kickoff

### Decisions locked

- **Audience:** Solo technical founders / founding engineers at seed-stage B2B product companies (roughly 2–25 people) who already use Cursor, Claude Code, or similar coding agents daily, and who still personally write investor updates, customer proposals, security questionnaires, and launch docs by ChatGPT → paste into Google Docs/Word.
- **Why this audience (and why it can be wrong):** Specific enough to name ten this week via public launch signals. Wrong if they already have an ops hire doing docs, or if their docs never leave Markdown. Defended because the agent→document gap is visible in how they already work.
- **Channel:** One outbound personalization machine (human research → validate/enrich → draft). Not multi-channel. Depth over sketches.
- **Piece:** Audience landing page that sells the *document loop* pain (not a feature laundry list), plus the machine’s cold-email drafts as the running artifact.
- **Build-in-public card:** Document building a **Proposal AI mini-workflow on SuperDocs** (catalog-aligned vertical: personalized proposals from a brief + template) live in five posts. Ties T1 audience, T2a, and product surfaces (chat, templates, review, export).
- **Clip feature:** Per-message revert (assigned).
- **Repo layout:** Folders by task; machine is plain Python, no paid tooling required.

### Done this session

- [x] Read growth brief + open task list structure
- [x] Product surface research (marketing features page, use cases; docs fetch flaky)
- [x] Repo scaffold, TASK.md, PROGRESS.md
- [x] Growth machine code + two deterministic recorded runs
- [x] Audience / measurement / responsive landing-page piece
- [x] Agent ecosystem map with extension mechanics and sources
- [x] Ten real-company use-case hypotheses, buyer roles, channels, and openers
- [x] Build-in-public post drafts (posting remains human/channel work)
- [x] Task 4 one-pager + timed demo script
- [x] Clip recording plan and voice script

### Verification completed

- Eight standard-library tests pass, including unsafe path inputs and claim-check regressions.
- Both canonical batches produce eight drafts, no risk flags, no final claim-check failures, and zero sends.
- Canonical runs use `--no-llm` for reproducibility.
- Public-signal research is separated from hypotheses; no private individuals are named.

### Human-only blockers before submission

- [ ] Run the Proposal AI acceptance test in an authenticated SuperDocs session and capture synthetic evidence.
- [ ] Publish the five-post series over the required cadence, recording links only after publication.
- [ ] Record the private per-message-revert clip with the candidate's real voice.
- [ ] Record the approximately three-minute demo with the candidate's real voice.
- [ ] Create the private GitHub remote, commit the work, invite `o-kadam`, and submit the repository link.

### Open assumptions

1. Free-tier / local generation is enough for personalization quality; optional LLM env vars if present.
2. Synthetic prospects + public company facts only in machine I/O.
3. User will create private GitHub remote + invite o-kadam at submit time.
4. Submission form not yet available — hold final packaging until form email.

### Cuts (so far)

- Skipped multi-channel (content SEO + community + outbound). One channel only.
- Skipped paid Clay/Apollo; use public signals + hand research fields in CSV.
- Skipped building a real Word add-in for the public series; document a SuperDocs-native proposal workflow instead (fits S1 surfaces, no backend required).

## 2026-08-15 — submission readiness pass

### Verified locally

- [x] Re-read the original growth brief and open-list submission mechanics.
- [x] Ran all standard-library tests successfully.
- [x] Ran two fresh deterministic verification batches: eight drafts each, zero sends, zero claim-check failures, and zero risk-flagged rows.
- [x] Added `SUBMISSION-CHECKLIST.md` with repository, post, video, form, and destination requirements.
- [x] Added `FORM-ANSWERS-DRAFT.md` with source-backed drafts and explicit firsthand-evidence placeholders.
- [x] Excluded the unrelated `hrms/` checkout, local task PDFs, identical `*-2.*` sync copies, and temporary validation runs from the submission package.

### Critical clarification before publishing

- [ ] Name the exact Open Task List card used by the five-post build and ensure the finished artifact meets that card. “Proposal AI mini-workflow” currently describes a catalog family, not an exact card title.

### Remaining human-only work

- [ ] Complete the authenticated build and capture genuine failure/result evidence.
- [ ] Publish five posts over ten days and record their dates/links.
- [ ] Record the private 15–30 second per-message-revert clip with the candidate’s real voice.
- [ ] Record the Task 4 demo with the candidate’s real voice and update the one-page write-up to final status.
- [ ] Finalize firsthand bug notes, form answers, AI-use estimate, and honest completion report.
- [ ] Create the private remote, invite `o-kadam`, open any build PR required by the selected card, and submit every destination through the Google Form.
