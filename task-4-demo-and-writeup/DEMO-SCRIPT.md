# Three-minute demo script

Target length: about three minutes. Use the candidate's real voice. Record locally with no keys, personal data, or real-company contacts visible.

## 0:00–0:20 — thesis

“I chose one audience: seed-stage technical founders who already trust coding agents but still move customer-facing work from chat into Word by hand. The machine tests a narrow idea: the unfinished agent workflow is the document, not the draft.”

Show `AUDIENCE.md` and the repository map.

## 0:20–1:15 — run the machine twice

Run:

```bash
python3 -m machine.run --batch data/batch-1.csv --run-id demo-run-1 --no-llm
python3 -m machine.run --batch data/batch-2.csv --run-id demo-run-2 --no-llm
```

“Each CSV contains synthetic company-and-role research, never personal contacts. The runner validates identifiers, maps the document pain to a message angle, checks SuperDocs claims, and writes drafts to an outbox. There is no sending integration, and SEND_MODE is hard-off.”

Open one draft, then both generated `metrics.json` files. Point out completion, claim failures, risk flags, and emails sent. Do not imply synthetic output validates market demand.

## 1:15–1:40 — the piece and measurement

Open `piece/index.html` at desktop width, then briefly resize to mobile.

“The piece sells one change in behavior: stop pasting the last mile. The measurement page reports only what an offline run can prove. It explicitly refuses to invent opens, replies, or meetings.”

Show `MEASUREMENT.md`.

## 1:40–2:15 — assigned builds

Open `task-2-builds/build-in-public/BUILD.md` and `POSTS.md`.

“The public build is a proposal workflow on SuperDocs: structured brief, existing template, targeted section edit, review, revert, and export. The five-post arc includes the affiliation disclosure, first breakage, changed product decision, measured result, and finished work.”

Open the ecosystem map.

“The extension map prioritizes channels that already accept remote MCP before proposing new adapters. Every marketplace path is labeled as a possibility, not a shipped listing.”

## 2:15–2:40 — use cases and clip

Open `task-3-use-cases/README.md`.

“The ten use cases begin with verified public document workflows at real companies. The proposed fit and opener are clearly labeled hypotheses. No one was contacted.”

Show the private per-message-revert clip or, until recorded, the clip plan. Explain that the actual clip uses the candidate's voice and a synthetic document.

## 2:40–3:00 — close

“What I optimized for was a small system that runs twice, leaves evidence, and respects product and outreach boundaries. What I cut was multi-channel breadth, automated sending, and metrics the task cannot honestly produce. The next permitted test is human review of a small draft set, followed by one controlled messaging experiment.”

End on the top-level README.

## Recording checklist

- Delete `demo-run-1` and `demo-run-2` after recording; the canonical evidence is `run-1` and `run-2`.
- Keep terminal text at a readable size.
- Use the candidate's voice and keep the final take near three minutes.
- Do not reveal environment variables, browser account details, or unpublished contact information.
- Do not claim the clip or posts are complete until their actual files/links exist.
