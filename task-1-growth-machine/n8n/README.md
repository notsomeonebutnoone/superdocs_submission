# n8n workflow for Task 1

`task-1-growth-machine.workflow.json` is an importable n8n control plane for the existing Python growth machine. It deliberately wraps the current implementation instead of recreating it, so the Python code remains the single source of truth and all original Task 1 contents remain unchanged.

## What the workflow does

1. Starts only from a **Manual Trigger**.
2. Defines the project path, CSV batch, run ID, and whether LLM polishing is allowed.
3. Validates paths and IDs before building a shell command.
4. Runs `python3 -m machine.run` through n8n's **Execute Command** node.
5. Parses the machine's JSON metrics.
6. Fails the workflow unless all safety gates hold:
   - `send_mode` is `false`
   - `emails_sent` is `0`
   - every accepted batch row produced a draft
   - claim-check failures are `0`
7. Returns a compact run summary and the output locations.

```text
Manual Trigger
    -> Workflow Configuration
    -> Validate and Build Command
    -> Run Existing Python Machine
    -> Safety Gate and Run Summary
```

## Requirements

- Self-hosted n8n. The Execute Command node is not available in n8n Cloud and may be disabled by an administrator.
- Python 3 available in the n8n runtime.
- This `task-1-growth-machine` folder mounted into the n8n container or host.
- No credentials are needed for the default deterministic run.

## Import and run

1. In n8n, choose **Import from File** and select `task-1-growth-machine.workflow.json`.
2. Open **Workflow Configuration**.
3. Set `projectDirectory` to the absolute path as seen by n8n. The default is `/files/task-1-growth-machine`.
4. Leave `batchFile` as `data/batch-1.csv`, or switch to `data/batch-2.csv`.
5. Give the run a safe unique ID such as `n8n-run-1`.
6. Keep `useLlm` set to `false` for the same deterministic behavior used by the submitted runs.
7. Select **Execute Workflow**.

The generated files appear inside the mounted Task 1 directory:

- `outbox/<runId>/`: draft-only Markdown messages
- `runs/<runId>/metrics.json`: machine metrics
- `runs/<runId>/results.json`: per-prospect results
- `runs/<runId>/batch.snapshot.csv`: exact input snapshot
- `runs/<runId>/SUMMARY.md`: human-readable summary

## Docker example

If n8n runs in Docker, mount the repository folder read-write because the machine creates run evidence and drafts:

```bash
docker run --rm -it \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  -v /absolute/path/to/task-1-growth-machine:/files/task-1-growth-machine \
  docker.n8n.io/n8nio/n8n
```

The exact deployment command may differ for an existing n8n installation. The important part is that the directory configured in the workflow matches the in-container mount path.

## Optional LLM polishing

Setting `useLlm=true` removes the `--no-llm` flag. The existing Python code then uses OpenAI only if `OPENAI_API_KEY` is present in the n8n runtime. It still falls back to the deterministic draft if the API is unavailable, malformed, too verbose, or fails the claim checker.

For reviewing or reproducing Task 1, `useLlm=false` is recommended.

## Safety properties

This workflow cannot turn the project into a sender. The underlying `machine/config.py` hard-codes `SEND_MODE = False`, and `machine/run.py` refuses to execute if that value ever becomes true. There is no email, CRM, or outreach node in this n8n workflow.
