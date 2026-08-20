# SuperDocs submission checklist

This checklist is derived from the original growth-task brief. The deadline is in the task email, not in this repository.

## Immediate critical path

- [x] Confirmed the exact Open Task List card: **Weakest-section critique engine** (page 417).
- [x] Used SuperDocs in an authenticated browser session with the synthetic Atlas Field Systems proposal.
- [x] Retained genuine evidence of the broad-prompt failure, changed prompt decision, successful constrained ranking, targeted rewrite, human review, and exported result.
- [x] Ran two constrained-ranking replications on 2026-08-17. Results were not stable: Next Steps and Current State, versus Timeline in the original constrained run.
- [ ] Verify every product capability shown against the current app and documentation.
- [ ] Before each public post, enforce the publication rails: candidate disclosure where applicable, no competitor ranking, no confidential material, no unsupported product claim, and at most one SuperDocs-related number drawn from SuperDocs’ own published material. When unsure, use no number.
- [x] Publish post 1 with candidate affiliation disclosed.
- [x] Published all five posts and recorded their dates and links. Posts 1 through 3 were published on August 17, 2026; Posts 4 and 5 were published on August 19, 2026.

| Post | Required content | Planned date | Published URL |
|---|---|---|---|
| 1 | Plan + candidate disclosure | August 17, 2026 | https://x.com/chimisogood1/status/2089266850190553524 |
| 2 | First real breakage | August 17, 2026 | https://x.com/chimisogood1/status/2089269287840260184 |
| 3 | Decision changed after evidence | August 17, 2026 | https://x.com/chimisogood1/status/2089270637374455995 |
| 4 | Measured result | August 19, 2026 | https://x.com/chimisogood1/status/2090096881536037131 |
| 5 | Finished, reproducible build | August 19, 2026 | https://x.com/chimisogood1/status/2090098189022237054 |

## Product evidence

- [ ] Use synthetic data only. Do not expose account details, keys, bookmarks, notifications, or private documents.
- [x] Captured screenshots of the real failure, constrained ranking, tracked rewrite, and accepted review.
- [ ] Complete the Proposal workflow acceptance checks in `task-2-builds/build-in-public/BUILD.md` if that remains the selected build.
- [ ] Follow the selected card’s `WHERE THE FINISHED WORK GOES` route exactly. Depending on the card, that may be a public-repository PR, the submission form/Drive, or the candidate’s own channel. The assigned five-post series itself goes on the candidate’s own channel.

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
  - Use the candidate’s real voice. Show only sanitized run output needed for the demonstration, with no shell history, environment values, credentials, or private material.
  - Upload the video file through the form and add an unlisted link if available.
- [ ] Review and personalize `task-4-demo-and-writeup/ONE-PAGE.md` so it accurately reflects the final authenticated build and published-post status.

## Form package

- [ ] Finalize the five answers in `FORM-ANSWERS-DRAFT.md`.
- [ ] Add every real SuperDocs bug or rough edge observed. Do not present the machine’s own claim-check bug as a SuperDocs product bug.
- [ ] State the approximate AI-built percentage and how the candidate directed the work.
- [ ] State honestly what works and what remains incomplete.
- [ ] Include the Task 3 use-case list.
- [ ] Include the agent-ecosystem map through the submission form/Drive route.
- [ ] Include the one-page write-up.
- [ ] Include repository, PR, post, video, and unlisted-video links.
- [ ] Include the GitHub handle and complete the clip/work-feature consent choices.
- [ ] Include extra-credit work and the optional naming/brand suggestion only if applicable.

## Repository packaging

- [x] Machine tests pass locally.
- [x] A fresh local re-run on 2026-08-15 reproduced eight drafts per batch, zero sends, zero claim-check failures, and zero risk-flagged rows. The commands and observed metrics are recorded in `task-1-growth-machine/runs/VERIFICATION-2026-08-15.md`; canonical run artifacts remain `run-1/` and `run-2/`.
- [x] Reviewed the tracked tree during the readiness pass: no `hrms/`, original task PDFs, duplicate `*-2.*` files, secrets, or temporary validation runs are tracked.
- [ ] Create a private repository with a neutral name such as `doctask-<name>`.
- [ ] Push Task 1 and supporting research to the private repository.
- [ ] Invite GitHub user `o-kadam` as collaborator.
- [ ] Open any required public SuperDocs build PR in the destination specified by the chosen card.

## Final submission

- [ ] Wait for the Google Form if it has not arrived.
- [ ] Submit every file and link through the form. Email is for questions and bug reports, not submission attachments.
- [ ] Confirm the form accepted the submission before the deadline stated in the original email.
