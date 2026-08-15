from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from machine.personalize import _claim_check
from machine.prospects import REQUIRED_COLUMNS, load_prospects
from machine.run import run_batch


class ClaimCheckTests(unittest.TestCase):
    def test_accepts_documented_capability(self) -> None:
        passed, notes = _claim_check("SuperDocs supports review before document edits land.")
        self.assertTrue(passed)
        self.assertEqual(notes, [])

    def test_rejects_forbidden_claim_variant(self) -> None:
        passed, notes = _claim_check("SuperDocs is SOC2 compliant and supports review.")
        self.assertFalse(passed)
        self.assertTrue(any("soc2" in note for note in notes))

    def test_requires_concrete_capability(self) -> None:
        passed, notes = _claim_check("SuperDocs is a revolutionary product.")
        self.assertFalse(passed)
        self.assertIn("mentions product but no concrete capability", notes)

    def test_ignores_prospect_compliance_context(self) -> None:
        text = (
            "A note about your policy workflow\n"
            "Your public SOC2 journey suggests policy work is painful. "
            + ("Background context. " * 10)
            + "SuperDocs supports review before document edits land."
        )
        passed, notes = _claim_check(text)
        self.assertTrue(passed)
        self.assertEqual(notes, [])

    def test_prospect_marker_does_not_validate_product_claim(self) -> None:
        passed, notes = _claim_check(
            "A note about your document loop\n"
            "API-first prospect. SuperDocs is revolutionary."
        )
        self.assertFalse(passed)
        self.assertIn("mentions product but no concrete capability", notes)

    def test_ignores_nearby_prospect_compliance_context(self) -> None:
        passed, notes = _claim_check(
            "A note about your policy workflow\n"
            "Your work mentions SOC2. SuperDocs supports review before edits land."
        )
        self.assertTrue(passed)
        self.assertEqual(notes, [])

    def test_rejects_forbidden_claim_in_subject(self) -> None:
        passed, notes = _claim_check(
            "SOC2-certified document editing\nSuperDocs supports review."
        )
        self.assertFalse(passed)
        self.assertTrue(any("soc2" in note for note in notes))


class InputSafetyTests(unittest.TestCase):
    def _write_batch(self, path: Path, prospect_id: str) -> None:
        row = {column: "value" for column in REQUIRED_COLUMNS}
        row.update(
            prospect_id=prospect_id,
            company="Example Company",
            role="Technical founder",
            public_url="https://example.com",
            product_one_liner="A sufficiently descriptive product line",
            doc_pain="proposal",
        )
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=REQUIRED_COLUMNS)
            writer.writeheader()
            writer.writerow(row)

    def test_rejects_unsafe_prospect_id(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            batch = Path(directory) / "batch.csv"
            self._write_batch(batch, "../escape")
            with self.assertRaisesRegex(ValueError, "Unsafe prospect_id"):
                load_prospects(batch)

    def test_rejects_unsafe_run_id(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            batch = Path(directory) / "batch.csv"
            self._write_batch(batch, "safe-id")
            with self.assertRaisesRegex(ValueError, "Unsafe run_id"):
                run_batch(batch, "../escape", use_llm=False)


if __name__ == "__main__":
    unittest.main()
