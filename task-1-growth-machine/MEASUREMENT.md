# Measurement: two reproducible runs

## What was measured

The machine was evaluated as an offline production system, not as a sent campaign. The round explicitly forbids outreach, so open, reply, meeting, and revenue metrics would be fabricated. The useful leading indicators are input validity, completion, claim safety, research depth, and reproducibility.

## Recorded result

| Metric | Run 1 | Run 2 | Combined |
|---|---:|---:|---:|
| Fresh prospects | 8 | 8 | 16 |
| Drafts written | 8 | 8 | 16 |
| Completion rate | 100% | 100% | 100% |
| Claim-check failures | 0 | 0 | 0 |
| Rows with risk flags | 0 | 0 | 0 |
| Emails sent | 0 | 0 | 0 |
| Batch overlap | n/a | 0 | 0 |

Evidence lives in `runs/run-1/`, `runs/run-2/`, and `outbox/`. Both runs used the deterministic generator with `--no-llm`.

## What changed after run 1

The first attempted recording caught one false positive: a prospect's public SOC2-journey context was treated as a SuperDocs claim. The checker was narrowed to the product-claim portion of the message, a regression test was added, and both runs were regenerated. This is a machine-quality correction, not a hidden campaign result.

## Quality rubric

Before any future human-approved send, score each draft from 0 to 2 on signal specificity, pain plausibility, product fit, and CTA restraint. A draft needs at least 7/8 and zero claim failures. Any non-synthetic row requires a source check by a human.

## Next experiment

If outreach becomes permitted, manually review five drafts and test one variable only: document-loop framing versus workflow-specific framing. Primary outcome: qualified replies. Guardrails: unsubscribe/negative-response rate, claim accuracy, and zero automated sends.
