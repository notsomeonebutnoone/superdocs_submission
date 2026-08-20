# Progress log

## 2026-08-06 — kickoff

### Decisions locked

- **Audience:** Solo technical founders / founding engineers at seed-stage B2B product companies (roughly 2–25 people) who already use Cursor, Claude Code, or similar coding agents daily, and who still personally write investor updates, customer proposals, security questionnaires, and launch docs by ChatGPT → paste into Google Docs/Word.
- **Why this audience (and why it can be wrong):** Specific enough to name ten this week via public launch signals. Wrong if they already have an ops hire doing docs, or if their docs never leave Markdown. Defended because the agent→document gap is visible in how they already work.
- **Channel:** One outbound personalization machine (human research → validate/enrich → draft). Not multi-channel. Depth over sketches.
- **Piece:** Audience landing page that sells the *document loop* pain (not a feature laundry list), plus the machine’s cold-email drafts as the running artifact.
- **Build-in-public card:** Document the exact Open Task List card **Weakest-section critique engine** live in five posts. The synthetic proposal supplies the test document; the workflow ranks five sections, rewrites the weakest after human review, and verifies document integrity.
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

- [x] Ran the initial weakest-section critique experiment in authenticated SuperDocs and captured synthetic failure, success, rewrite, and review evidence.
- [x] Ran two fresh constrained-ranking replications. The result was unstable: original = Timeline, replication A = Next Steps, replication B = Current State. Run B also inverted the requested display order.
- [x] Published the five-post series and recorded all links.
- [ ] Record the private per-message-revert clip with the candidate's real voice.
- [x] Recorded the approximately three-minute demo with the candidate's real voice: https://drive.google.com/file/d/1LSYa400C1j5kwrwHbQSgWn_HPv9AMvAs/view?usp=sharing
- [ ] Private GitHub repository is created, committed, and pushed; invite `o-kadam` and submit the repository link.

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

- [x] Exact Open Task List card confirmed: **Weakest-section critique engine** (page 417). The five-section ranking, targeted Timeline rewrite, review evidence, and integrity check map directly to the card.
- [x] Ran the constrained ranking twice in fresh authenticated sessions. The weakest-section result was not stable; the limitation is recorded in Post 4.

### Remaining human-only work

- [x] Completed the authenticated build and captured genuine failure, constrained-ranking, targeted-rewrite, and review evidence.
- [x] Published all five posts and recorded their dates and links. Posts 1 through 3 were published on August 17, 2026; Posts 4 and 5 were published on August 19, 2026.
- [ ] Record the private 15–30 second per-message-revert clip with the candidate’s real voice.
- [x] Recorded the Task 4 demo with the candidate’s real voice and added the share link to the final package.
- [x] Finalized firsthand bug notes, form answers, AI-use estimate, and honest completion report.
- [ ] Private remote is created and pushed; invite `o-kadam`, open any build PR required by the selected card, and submit every destination through the Google Form.
