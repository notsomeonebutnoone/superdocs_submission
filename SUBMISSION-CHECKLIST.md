# SuperDocs submission checklist

This checklist is derived from the original growth-task brief. The deadline is in the task email, not in this repository.

## Immediate critical path

- [ ] Confirm the exact Open Task List build card being documented. The current notes say “Proposal AI mini-workflow,” but do not name an exact catalog card. Do not publish the series until the card and the finished artifact clearly match.
- [ ] Use SuperDocs in an authenticated browser session on synthetic or personally owned material.
- [ ] Run the selected build end to end and retain real evidence: plan, first failure, changed decision, measured result, and finished artifact.
- [ ] Verify every product capability shown against the current app and documentation.
- [ ] Publish post 1 with candidate affiliation disclosed.
- [ ] Publish the remaining four posts across a total span of ten days. Record dates and links only after publication.

| Post | Required content | Planned date | Published URL |
|---|---|---|---|
| 1 | Plan + candidate disclosure |  |  |
| 2 | First real breakage |  |  |
| 3 | Decision changed after evidence |  |  |
| 4 | Measured result |  |  |
| 5 | Finished, reproducible build |  |  |

## Product evidence

- [ ] Use synthetic data only. Do not expose account details, keys, bookmarks, notifications, or private documents.
- [ ] Capture screenshots of the real failure and the corrected workflow.
- [ ] Complete the Proposal workflow acceptance checks in `task-2-builds/build-in-public/BUILD.md` if that remains the selected build.
- [ ] Ensure the final artifact follows the selected card’s `WHERE THE FINISHED WORK GOES` route. A SuperDocs build generally requires a PR to `github.com/superdocsapp/superdocs-builds`; the five public posts go on the candidate’s own channel.

## Required videos

- [ ] Record the private per-message-revert clip using `clip-task/README.md`.
  - 15–30 seconds.
  - Candidate’s real voice.
  - Demonstrate one-message revert while earlier accepted work remains.
  - No numbers or counts in the clip.
  - Never publish publicly. Upload only through the submission form, plus an unlisted link if available.
- [ ] Record the Task 4 demo using `task-4-demo-and-writeup/DEMO-SCRIPT.md`.
  - Aim for about three minutes, five minutes maximum.
  - Show both machine runs and the assigned builds.
  - Keep the separate feature clip out of the demo sequence except as a referenced deliverable.
  - Use the candidate’s real voice and reveal no credentials or private material.
- [ ] Review and personalize `task-4-demo-and-writeup/ONE-PAGE.md` so it accurately reflects the final authenticated build and published-post status.

## Form package

- [ ] Finalize the five answers in `FORM-ANSWERS-DRAFT.md`.
- [ ] Add every real SuperDocs bug or rough edge observed. Do not present the machine’s own claim-check bug as a SuperDocs product bug.
- [ ] State the approximate AI-built percentage and how the candidate directed the work.
- [ ] State honestly what works and what remains incomplete.
- [ ] Include the Task 3 use-case list.
- [ ] Include the one-page write-up.
- [ ] Include repository, PR, post, video, and unlisted-video links.

## Repository packaging

- [x] Machine tests pass locally.
- [x] Two fresh validation batches each produced eight drafts, zero sends, zero claim-check failures, and zero risk-flagged rows on 2026-08-15.
- [ ] Review the staged file list and confirm no `hrms/`, task PDFs, duplicate `*-2.*` files, secrets, or temporary validation runs are included.
- [ ] Create a private repository with a neutral name such as `doctask-<name>`.
- [ ] Push Task 1 and supporting research to the private repository.
- [ ] Invite GitHub user `o-kadam` as collaborator.
- [ ] Open any required public SuperDocs build PR in the destination specified by the chosen card.

## Final submission

- [ ] Wait for the Google Form if it has not arrived.
- [ ] Submit every file and link through the form. Email is for questions and bug reports, not submission attachments.
- [ ] Confirm the form accepted the submission before the deadline stated in the original email.
