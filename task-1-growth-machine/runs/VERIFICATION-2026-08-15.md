# Local verification — 2026-08-15

This verification reran the public workflow without changing the canonical evidence in `run-1/` and `run-2/`.

## Commands

```text
python -m unittest discover -s tests -v
python -m machine.run --batch data/batch-1.csv --run-id verification-run-1 --no-llm
python -m machine.run --batch data/batch-2.csv --run-id verification-run-2 --no-llm
```

The temporary `verification-run-*` output directories are excluded from Git after their metrics were inspected.

## Observed result

| Check | Verification run 1 | Verification run 2 |
|---|---:|---:|
| Batch size | 8 | 8 |
| Drafts written | 8 | 8 |
| Send mode | off | off |
| Emails sent | 0 | 0 |
| Claim-check failures | 0 | 0 |
| Rows with risk flags | 0 | 0 |
| Generator | deterministic | deterministic |

All unit tests completed successfully before both fresh batches ran. The temporary metrics reported start times `2026-08-15T07:56:40Z` and `2026-08-15T07:56:41Z` respectively.

This is reproducibility evidence only. It does not measure demand, opens, replies, meetings, or revenue.
