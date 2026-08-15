from __future__ import annotations

import csv
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class Prospect:
    """One outreach target. Roles and companies only — no private personal names."""

    prospect_id: str
    company: str
    role: str  # e.g. "Founding engineer", never a personal name
    segment: str
    public_signal: str
    public_url: str
    product_one_liner: str
    doc_pain: str
    recent_public_detail: str
    hypothesis: str
    is_synthetic: str = "yes"
    notes: str = ""
    extra: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        extra = d.pop("extra", {}) or {}
        d.update(extra)
        return d


REQUIRED_COLUMNS = [
    "prospect_id",
    "company",
    "role",
    "segment",
    "public_signal",
    "public_url",
    "product_one_liner",
    "doc_pain",
    "recent_public_detail",
    "hypothesis",
]

SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$")


def load_prospects(path: Path) -> list[Prospect]:
    if not path.exists():
        raise FileNotFoundError(f"Batch file not found: {path}")

    prospects: list[Prospect] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = [c for c in REQUIRED_COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"Batch CSV missing columns: {missing}")

        seen_ids: set[str] = set()
        for row in reader:
            if not row.get("prospect_id", "").strip():
                continue
            base = {k: (row.get(k) or "").strip() for k in REQUIRED_COLUMNS}
            prospect_id = base["prospect_id"]
            if not SAFE_ID.fullmatch(prospect_id):
                raise ValueError(f"Unsafe prospect_id: {prospect_id!r}")
            if prospect_id in seen_ids:
                raise ValueError(f"Duplicate prospect_id: {prospect_id!r}")
            seen_ids.add(prospect_id)
            base["is_synthetic"] = (row.get("is_synthetic") or "yes").strip()
            base["notes"] = (row.get("notes") or "").strip()
            known = set(REQUIRED_COLUMNS) | {"is_synthetic", "notes"}
            extra = {k: v for k, v in row.items() if k not in known and v}
            prospects.append(Prospect(**base, extra=extra))

    return prospects
