from __future__ import annotations

import json
import re
import urllib.error
import urllib.request
from dataclasses import dataclass

from . import config
from .enrich import EnrichedProspect


@dataclass
class DraftEmail:
    prospect_id: str
    company: str
    role: str
    subject: str
    body: str
    generator: str  # "deterministic" | "openai" | "anthropic"
    claim_check_passed: bool
    claim_check_notes: list[str]


def _claim_check(text: str) -> tuple[bool, list[str]]:
    lower = text.lower()
    notes: list[str] = []
    product_index = lower.find("superdocs")
    product_text = lower[product_index:] if product_index >= 0 else lower
    subject = lower.partition("\n")[0]
    forbidden_text = subject + "\n" + product_text
    for frag in config.FORBIDDEN_CLAIM_FRAGMENTS:
        if frag in forbidden_text:
            notes.append(f"forbidden claim fragment: {frag!r}")
    capability_markers = (
        "section",
        "style-preserving",
        "word/pdf",
        "review",
        "revert",
        "mcp",
        "api",
        "edit lands in the document",
        "edits documents in-place",
    )
    if product_index >= 0:
        if not any(marker in product_text for marker in capability_markers):
            notes.append("mentions product but no concrete capability")
    return (len(notes) == 0, notes)


def _deterministic_draft(e: EnrichedProspect) -> DraftEmail:
    p = e.prospect
    subject = f"{p.company} + the document loop after the agent draft"

    body = f"""Hi — writing to the {p.role} seat at {p.company} (no personal name on file; company + role only).

Saw the public signal: {p.public_signal}.
{p.recent_public_detail}

Hypothesis I'm testing (could be wrong): {p.hypothesis}
That usually shows up as {e.pain_label} — specifically {e.hook_angle}.

{config.PRODUCT_NAME} is {config.PRODUCT_ONE_LINER}
For teams in your shape, the useful part is usually: {e.proof_point}.
Not a chat window that hands you text to paste — the edit lands in the document, with review before anything final, and export that keeps structure for Word/PDF.

{e.cta}
Product: {config.PRODUCT_URL}

If the hypothesis is off, say so and I'll close the loop. If it's close, happy to show a 5-minute path on a synthetic proposal (no need to touch real customer files).

— Growth candidate build (draft only; this message is not sent to anyone)
"""
    ok, notes = _claim_check(subject + "\n" + body)
    return DraftEmail(
        prospect_id=p.prospect_id,
        company=p.company,
        role=p.role,
        subject=subject.strip(),
        body=body.strip() + "\n",
        generator="deterministic",
        claim_check_passed=ok,
        claim_check_notes=notes,
    )


def _openai_polish(base: DraftEmail, e: EnrichedProspect) -> DraftEmail | None:
    if not config.OPENAI_API_KEY:
        return None
    prompt = {
        "model": config.LLM_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You write short cold emails for a growth experiment. "
                    "Rules: max 140 words in the body; no fake personal names; "
                    "address role at company; no hype; no competitor bashing; "
                    "do not claim SOC2, e-sign, web browsing, or guaranteed redaction; "
                    "SuperDocs edits documents in-place with review and style-preserving export. "
                    "Return JSON with keys subject, body only."
                ),
            },
            {
                "role": "user",
                "content": json.dumps(
                    {
                        "company": e.prospect.company,
                        "role": e.prospect.role,
                        "signal": e.prospect.public_signal,
                        "detail": e.prospect.recent_public_detail,
                        "hypothesis": e.prospect.hypothesis,
                        "pain": e.pain_label,
                        "draft_subject": base.subject,
                        "draft_body": base.body,
                    }
                ),
            },
        ],
        "temperature": 0.4,
    }
    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(prompt).encode(),
        headers={
            "Authorization": f"Bearer {config.OPENAI_API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            raw = json.loads(resp.read().decode())
        content = raw["choices"][0]["message"]["content"]
        # Allow fenced JSON
        content = content.strip()
        if content.startswith("```"):
            content = re.sub(r"^```(?:json)?\n?", "", content)
            content = re.sub(r"\n?```$", "", content)
        parsed = json.loads(content)
        subject = str(parsed.get("subject") or base.subject).strip()
        body = str(parsed.get("body") or base.body).strip() + "\n"
        ok, notes = _claim_check(subject + "\n" + body)
        if len(body.split()) > 140:
            ok = False
            notes.append("body exceeds 140 words")
        if not ok:
            # Fall back to deterministic if model drifted.
            return None
        return DraftEmail(
            prospect_id=base.prospect_id,
            company=base.company,
            role=base.role,
            subject=subject,
            body=body,
            generator="openai",
            claim_check_passed=True,
            claim_check_notes=[],
        )
    except (urllib.error.URLError, KeyError, json.JSONDecodeError, TimeoutError, OSError):
        return None


def personalize(e: EnrichedProspect, use_llm: bool = True) -> DraftEmail:
    base = _deterministic_draft(e)
    if use_llm and config.OPENAI_API_KEY:
        polished = _openai_polish(base, e)
        if polished:
            return polished
    return base
