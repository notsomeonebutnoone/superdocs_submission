# doctask — SuperDocs growth round

Private working repository for the SuperDocs GTM / Growth Engineer task (Round 2).

> **Bright line:** nothing in this repo is sent to any real person or company. Outreach drafts are synthetic-run artifacts only. SuperDocs does all real outreach themselves.

## Map

| Path | What |
|------|------|
| [`TASK.md`](./TASK.md) | How to work this round |
| [`PROGRESS.md`](./PROGRESS.md) | Running log of assumptions, cuts, status |
| [`notes/DECISIONS.md`](./notes/DECISIONS.md) | Strategic calls |
| [`task-1-growth-machine/`](./task-1-growth-machine/) | Audience, runnable outbound machine, piece, measurement, two runs |
| [`task-2-builds/build-in-public/`](./task-2-builds/build-in-public/) | Five-post series (content + posting checklist) |
| [`task-2-builds/agent-ecosystem-map/`](./task-2-builds/agent-ecosystem-map/) | Agent products → extension mechanics → SuperDocs fit |
| [`task-3-use-cases/`](./task-3-use-cases/) | ~10 buyable use cases with real companies |
| [`clip-task/`](./clip-task/) | Per-message revert clip brief + script |
| [`task-4-demo-and-writeup/`](./task-4-demo-and-writeup/) | Demo script + one-page write-up |

## Task 1 in one line

**Audience:** seed-stage technical founders who already use coding agents but still paste docs out of chat.  
**Machine:** load researched rows → validate/enrich → personalize cold email → write `outbox/` (never send).  
**Piece:** landing page for that audience.  
**Numbers:** measurement page + metrics JSON from both runs.

### Run the machine

```bash
cd task-1-growth-machine
python3 -m machine.run --batch data/batch-1.csv --run-id run-1 --no-llm
python3 -m machine.run --batch data/batch-2.csv --run-id run-2 --no-llm
```

Optional: set `OPENAI_API_KEY` for LLM-polished copy. Without a key, the deterministic personalizer still produces full drafts from research fields (demo-safe, free).

## Credit

Built for the SuperDocs growth task. Product claims limited to what SuperDocs ships today.
