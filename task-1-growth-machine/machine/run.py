from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

from . import config
from .enrich import enrich
from .personalize import personalize
from .prospects import load_prospects


SAFE_RUN_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$")


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _portable_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(config.ROOT))
    except ValueError:
        return str(path)


def run_batch(
    batch_path: Path,
    run_id: str,
    use_llm: bool = True,
) -> dict:
    if config.SEND_MODE:
        raise RuntimeError("SEND_MODE is true — refusing to run. This machine must never send.")
    if not SAFE_RUN_ID.fullmatch(run_id):
        raise ValueError(f"Unsafe run_id: {run_id!r}")

    prospects = load_prospects(batch_path)
    run_dir = config.RUNS_DIR / run_id
    out_dir = config.OUTBOX_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Fresh outbox for this run id
    for old in out_dir.glob("*"):
        if old.is_file():
            old.unlink()

    results = []
    claim_failures = 0
    thin_flags = 0

    for p in prospects:
        enriched = enrich(p)
        if enriched.risk_flags:
            thin_flags += 1
        draft = personalize(enriched, use_llm=use_llm)
        if not draft.claim_check_passed:
            claim_failures += 1

        company_slug = re.sub(r"[^a-z0-9]+", "-", p.company.lower()).strip("-")[:40]
        slug = f"{p.prospect_id}__{company_slug or 'company'}"
        mail_path = out_dir / f"{slug}.md"
        mail_path.write_text(
            f"---\n"
            f"prospect_id: {draft.prospect_id}\n"
            f"company: {draft.company}\n"
            f"role: {draft.role}\n"
            f"subject: {draft.subject}\n"
            f"generator: {draft.generator}\n"
            f"send_mode: false\n"
            f"status: DRAFT_ONLY_NOT_SENT\n"
            f"---\n\n"
            f"# Subject\n{draft.subject}\n\n"
            f"# Body\n{draft.body}\n",
            encoding="utf-8",
        )

        results.append(
            {
                "prospect_id": p.prospect_id,
                "company": p.company,
                "role": p.role,
                "doc_pain": p.doc_pain,
                "generator": draft.generator,
                "claim_check_passed": draft.claim_check_passed,
                "claim_check_notes": draft.claim_check_notes,
                "risk_flags": enriched.risk_flags,
                "outbox_file": str(mail_path.relative_to(config.ROOT)),
                "subject": draft.subject,
                "body_chars": len(draft.body),
            }
        )

    metrics = {
        "run_id": run_id,
        "started_at": _utc_now(),
        "batch_file": _portable_path(batch_path),
        "batch_size": len(prospects),
        "drafts_written": len(results),
        "send_mode": False,
        "emails_sent": 0,
        "claim_check_failures": claim_failures,
        "rows_with_risk_flags": thin_flags,
        "generators": _count_by(results, "generator"),
        "doc_pains": _count_by(
            [{"doc_pain": r["doc_pain"]} for r in results], "doc_pain"
        ),
        "llm_env_present": bool(config.OPENAI_API_KEY),
        "product_url": config.PRODUCT_URL,
    }

    (run_dir / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    (run_dir / "results.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")

    # Snapshot the batch used for reproducibility
    shutil.copy(batch_path, run_dir / "batch.snapshot.csv")

    summary_lines = [
        f"# Run {run_id}",
        "",
        f"- Time (UTC): {metrics['started_at']}",
        f"- Batch: `{batch_path.name}` ({metrics['batch_size']} prospects)",
        f"- Drafts written: **{metrics['drafts_written']}**",
        f"- Emails sent: **0** (SEND_MODE hard-off)",
        f"- Claim-check failures: {metrics['claim_check_failures']}",
        f"- Rows with risk flags: {metrics['rows_with_risk_flags']}",
        f"- Generators: {metrics['generators']}",
        "",
        "## Drafts",
        "",
    ]
    for r in results:
        summary_lines.append(
            f"- `{r['prospect_id']}` · {r['company']} · {r['role']} → `{r['outbox_file']}`"
        )
    summary_lines.append("")
    (run_dir / "SUMMARY.md").write_text("\n".join(summary_lines), encoding="utf-8")

    return metrics


def _count_by(rows: list[dict], key: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for r in rows:
        k = str(r.get(key, ""))
        out[k] = out.get(k, 0) + 1
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Founder Doc Signal outbound machine — drafts only, never sends."
    )
    parser.add_argument(
        "--batch",
        required=True,
        help="Path to prospects CSV (relative to task-1-growth-machine or absolute)",
    )
    parser.add_argument("--run-id", required=True, help="e.g. run-1 or run-2")
    parser.add_argument(
        "--no-llm",
        action="store_true",
        help="Force deterministic personalizer even if API keys exist",
    )
    args = parser.parse_args(argv)

    batch_path = Path(args.batch)
    if not batch_path.is_absolute():
        batch_path = (config.ROOT / batch_path).resolve()

    metrics = run_batch(batch_path, args.run_id, use_llm=not args.no_llm)
    print(json.dumps(metrics, indent=2))
    print(
        f"\nOK — {metrics['drafts_written']} drafts in outbox/{args.run_id}/ "
        f"(sent: {metrics['emails_sent']})",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
