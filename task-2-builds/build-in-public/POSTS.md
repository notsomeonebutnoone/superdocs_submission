# Weakest-section critique engine — five-post build log

Exact Open Task List card: **Weakest-section critique engine** (page 417).

Card requirement: rank document sections against a stated goal, explain the ranking, and rewrite the weakest section on request. The strong bar is a defensible ranking that remains stable across repeated runs and a rewrite that measurably addresses the stated weakness.

These are publication-ready drafts, not claims that they have been published. Planned cadence: August 17, 19, 21, 24, and 26, 2026. Add a genuine URL and actual publication time only after posting.

## Post 1 — plan and disclosure

**Planned:** August 17, 2026

**Published:** August 17, 2026 at 1:53:28 PM IST

**URL:** https://x.com/chimisogood1/status/2089266850190553524

**Disclosure:** I am a candidate for a growth role at SuperDocs, and I am building this as part of the process.

I’m testing a narrow document-AI workflow: find the weakest section in an existing proposal, explain why it is weakest, then improve only that section.

The test document is a synthetic 1,910-word operations proposal. The evaluation goal is fixed before the run: rank five named sections by how concise, credible, and easy they are for an operations buyer to approve.

Success means:

- all five sections are ranked with reasons grounded in their current wording;
- the same weakest section survives repeated runs;
- no text changes during analysis;
- the rewrite changes only the selected section;
- a human reviews the proposed change before acceptance.

I already have an initial failure worth examining. Over the next ten days I’ll publish the failure, the prompt decision it changed, the measured replication, and the finished workflow—including the limitation if the ranking does not remain stable.

**Visual:** `post-1-plan-visual-v2.png`. It presents the experiment setup without revealing later results.

## Post 2 — first breakage

**Planned:** August 19, 2026

**Published:** August 17, 2026 at 2:03:09 PM IST

**URL:** https://x.com/chimisogood1/status/2089269287840260184

My first weakest-section prompt failed without editing the document.

I asked for every proposal section to be ranked from weakest to strongest, with a grounded reason for each. The first response asked me to rephrase. The retry displayed progress messages but never returned the ordered analysis.

The more revealing failure came next: when I asked what had changed, the response described several revisions even though a full-text comparison showed that the 1,910-word document was unchanged. Pricing and Terms were unchanged too.

That made the real problem clearer. “Analyze this whole document” was too broad to evaluate reliably, and a confident summary was not proof that anything had happened.

The next version would need a smaller input boundary, an explicit output contract, and an independent check against the actual document state.

**Visual:** `Screenshot 2026-08-15 152045.png` for the incomplete ranking. If space permits, pair it with `Screenshot 2026-08-15 152102.png` and label the claimed-change summary separately. Keep the failure visible; do not crop it into an apparent success.

## Post 3 — decision changed after evidence

**Planned:** August 21, 2026

**Published:** August 17, 2026 at 2:08:31 PM IST

**URL:** https://x.com/chimisogood1/status/2089270637374455995

I stopped asking document AI to “review everything.”

After the first failure, I changed the task from an open-ended whole-document critique to a bounded contract:

1. Analyze exactly five named sections.
2. Make no edits and propose no edits during ranking.
3. Rank them from weakest to strongest against one stated goal.
4. Give one reason grounded in each section’s current wording.
5. End by naming only the weakest section.

That version returned the complete ranking and selected Timeline as weakest.

The ranking was useful but not unquestionable: its explanation said exact dates and milestones were unresolved, while the source already contained weekly milestones and intentionally left calendar dates for discovery. So the workflow keeps human judgment between ranking and rewriting.

My changed decision: the product is not “press a button and trust the critique.” It is a constrained analysis step whose output must be inspectable before it is allowed to change the document.

**Visual:** `Screenshot 2026-08-15 152255.png`, showing the complete five-section ranking and named weakest section.

## Post 4 — measured replication

**Planned:** August 24, 2026

**Published:** August 19, 2026 at 8:51:43 PM IST

**URL:** https://x.com/chimisogood1/status/2090096881536037131

I reran the constrained weakest-section prompt twice against fresh copies of the same baseline proposal.

The result was not stable. Run A returned all five sections in the requested weakest-to-strongest order and named Next Steps weakest. Run B covered all five sections but presented its numbered list strongest-to-weakest despite the prompt defining 1 as weakest; it named Current State weakest. The two runs therefore disagreed with each other and with the original constrained run, which had named Timeline weakest.

The disagreement was substantive, not just formatting. Run A criticized Next Steps as vague. Run B called Current State overly defensive. The original run selected Timeline because dates remained subject to discovery. Each explanation points to real wording, but the workflow did not produce a stable weakest-section decision across repeated runs.

The original experiment provides the baseline:

- the broad prompt did not produce the requested ranking;
- the constrained prompt returned all five ranked sections;
- normalized pre-edit text remained 1,910 words and matched the source exactly;
- Pricing and Terms remained exact matches.

Across three constrained results, three different sections were selected as weakest: Timeline, Next Steps, and Current State. This is a small reproducibility check, not a general reliability percentage. It shows that the prompt can produce a complete, grounded critique, but the ranking is not stable enough to act as an automatic edit decision. A human must choose which critique is useful before any rewrite begins.

**Visual:** a side-by-side capture of the two new constrained results. Show the prompt and final ranking in each; hide account details. Do not reuse the old single-run screenshot as evidence of replication.

## Post 5 — finished workflow

**Planned:** August 26, 2026

**Published:** August 19, 2026 at 8:56:55 PM IST

**URL:** https://x.com/chimisogood1/status/2090098189022237054

The finished workflow is deliberately small:

`fixed goal → five-section ranking → human check → weakest-section rewrite → review → integrity check`

In the proposal test, the constrained ranking identified Timeline. The rewrite preserved the six-week duration and every existing week-level activity, added clearer purpose and approval framing, and proposed only two visible changes: the section heading and its introduction.

Human review still mattered. The first revision weakened an important control sentence, so I restored the original wording before accepting it: “The six-week duration will not change without written agreement from both parties.”

The final comparison passed on protected content: Pricing, Terms, all non-Timeline text, and all 76 list items were unchanged. It also exposed a real export limitation: the cover title’s Word style changed from `Title` to `Heading 1`, so I am reporting the export as a partial formatting pass rather than hiding the defect.

What survived the build:

- narrow prompts are easier to evaluate than broad critique requests;
- analysis and editing need separate turns;
- the document, not the assistant’s summary, is the source of truth;
- review catches changes that satisfy the prompt but weaken the document;
- “finished” includes an integrity check and an honest limitation.

**Visual:** `Screenshot 2026-08-15 152702.png` beside `Screenshot 2026-08-15 152711.png`, followed by the verdict table in `EXPORT-VERIFICATION-2026-08-17.md`.

## Replication prompt for Post 4

Run this twice in separate fresh sessions against the unchanged baseline file. Do not accept or apply any changes.

> Do not edit, rewrite, summarize, or propose changes to the document. Perform analysis only. Review exactly these five sections: Executive Summary, Current State, Proposed Approach, Timeline, and Next Steps. Rank them from 1, weakest, to 5, strongest against this goal: concise, credible, and easy for an operations buyer to approve. For each section, provide one reason grounded in its current wording. End by naming only the weakest section. Do not modify the document.

Record for each run:

| Run | Date/time | Complete 1–5 ranking? | Weakest section | Document changed? | Screenshot |
|---|---|---|---|---|---|
| A | 2026-08-17; time not recorded | Yes | Next Steps | Confirmation pending | Not yet saved in repository |
| B | 2026-08-17; time not recorded | Partial: all five covered, but displayed strongest-to-weakest | Current State | Confirmation pending | Not yet saved in repository |

## Publication rails

- Keep the candidate disclosure in Post 1.
- Use only the synthetic Atlas Field Systems proposal.
- Publish on an account you own; do not DM or contact any person or company.
- Preserve failures and limitations instead of polishing them away.
- Use no unsupported SuperDocs capability or performance claim.
- Show no credentials, account details, private documents, or reversible blur/pixelation.
- Add dates and URLs only after publication.
- Put all five links in the submission form.
