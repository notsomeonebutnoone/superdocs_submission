# Founder Doc Signal machine

An offline, draft-only outbound machine for seed-stage technical founders who use agents but still finish customer-facing documents by hand.

## Run

```bash
python3 -m machine.run --batch data/batch-1.csv --run-id run-1 --no-llm
python3 -m machine.run --batch data/batch-2.csv --run-id run-2 --no-llm
python3 -m unittest discover -s tests -v
```

Finding and public-research collection are the human input stage. The automated pipeline starts at the CSV: it validates researched rows, maps document pain to a message angle, checks product claims, and writes Markdown drafts to `outbox/`. It has no sending integration and refuses to run if `SEND_MODE` is enabled.

## Evidence

- `AUDIENCE.md`: audience and finding method
- `data/`: two fresh synthetic batches
- `runs/`: snapshots, results, summaries, and metrics
- `outbox/`: draft-only messages
- `piece/index.html`: audience landing page
- `MEASUREMENT.md`: honest two-run interpretation
