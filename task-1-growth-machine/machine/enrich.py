from __future__ import annotations

from dataclasses import dataclass

from .prospects import Prospect


@dataclass
class EnrichedProspect:
    prospect: Prospect
    pain_label: str
    hook_angle: str
    proof_point: str
    cta: str
    risk_flags: list[str]


PAIN_PLAYBOOK = {
    "investor_update": {
        "pain_label": "investor / board update still assembled by hand",
        "hook_angle": "weekly narrative + numbers table that must stay branded",
        "proof_point": "section edits + style-preserving export so the update stays one file",
        "cta": "worth a 10-minute look if updates still start in chat and end in Docs",
    },
    "customer_proposal": {
        "pain_label": "customer proposals reformatted after every AI draft",
        "hook_angle": "template stays intact while scope/pricing sections move",
        "proof_point": "review gate before anything client-facing lands",
        "cta": "if proposals are still paste-and-fix, this loop is built for that",
    },
    "security_questionnaire": {
        "pain_label": "security questionnaires eating founder time",
        "hook_angle": "long structured answers that must match prior language",
        "proof_point": "search + section edit across a living questionnaire file",
        "cta": "useful when the same answers get rewritten from scratch each vendor cycle",
    },
    "launch_one_pager": {
        "pain_label": "launch post never becomes a clean one-pager/PDF",
        "hook_angle": "public narrative → polished leave-behind without a redesign",
        "proof_point": "draft once, export Word/PDF with structure preserved",
        "cta": "if launch week still needs a separate design pass for a PDF, look here",
    },
    "policy_pack": {
        "pain_label": "policy / SOP packs drifting out of sync",
        "hook_angle": "one change must land in the right sections only",
        "proof_point": "section-precision editing with full change history",
        "cta": "when policy edits are still whole-document rewrites, this is the wedge",
    },
}


def _normalize_pain_key(doc_pain: str) -> str:
    key = (doc_pain or "").strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "proposal": "customer_proposal",
        "proposals": "customer_proposal",
        "sales_proposal": "customer_proposal",
        "investor": "investor_update",
        "board_update": "investor_update",
        "security": "security_questionnaire",
        "questionnaire": "security_questionnaire",
        "vendor_review": "security_questionnaire",
        "launch": "launch_one_pager",
        "one_pager": "launch_one_pager",
        "policy": "policy_pack",
        "sop": "policy_pack",
    }
    if key in PAIN_PLAYBOOK:
        return key
    return aliases.get(key, "customer_proposal")


def enrich(prospect: Prospect) -> EnrichedProspect:
    """Deterministic enrichment from structured research fields.

    No live web calls (SuperDocs itself does not browse; our machine stays
    offline-reproducible from the batch CSV).
    """
    play = PAIN_PLAYBOOK[_normalize_pain_key(prospect.doc_pain)]
    flags: list[str] = []

    if not prospect.recent_public_detail:
        flags.append("thin_public_detail")
    if not prospect.public_url:
        flags.append("missing_public_url")
    if prospect.is_synthetic.lower() not in {"yes", "true", "1"}:
        # Real company rows are fine; we still never store personal names.
        flags.append("non_synthetic_company_row")

    # Soft quality gate: very short product lines get a flag, still draftable.
    if len(prospect.product_one_liner) < 12:
        flags.append("thin_product_line")

    return EnrichedProspect(
        prospect=prospect,
        pain_label=play["pain_label"],
        hook_angle=play["hook_angle"],
        proof_point=play["proof_point"],
        cta=play["cta"],
        risk_flags=flags,
    )
