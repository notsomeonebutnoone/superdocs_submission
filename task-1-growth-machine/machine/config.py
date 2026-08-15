from __future__ import annotations

import os
from pathlib import Path

# Absolute bright line: this machine never sends.
SEND_MODE = False

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUTBOX_DIR = ROOT / "outbox"
RUNS_DIR = ROOT / "runs"

PRODUCT_NAME = "SuperDocs"
PRODUCT_ONE_LINER = (
    "AI that edits the document you already have — inside it, not beside it."
)
PRODUCT_URL = "https://use.superdocs.app"
DOCS_URL = "https://docs.superdocs.app"

# Claims ceiling: only ship-today capabilities.
ALLOWED_CLAIMS = [
    "section-precision edits that leave the rest of the document alone",
    "style-preserving export to Word (.docx) and PDF",
    "review before changes land",
    "version history with per-message revert",
    "MCP / API so a coding agent can drive the same loop",
]

FORBIDDEN_CLAIM_FRAGMENTS = [
    "soc 2",
    "soc2",
    "guaranteed redaction",
    "browses the web",
    "browse the web",
    "replaces google docs",
    "multiplayer cursors",
    "native e-signature",
    "native esignature",
    "native e-sign",
]

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "").strip()
LLM_MODEL = os.environ.get("GROWTH_LLM_MODEL", "gpt-4o-mini")
