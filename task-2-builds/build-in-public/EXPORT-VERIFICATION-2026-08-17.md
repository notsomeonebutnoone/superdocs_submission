# Final proposal export verification — 2026-08-17

## Files compared

- Baseline: `atlas-field-systems-detailed-proposal.docx`
- Final SuperDocs export: `../atlas-field-systems-final.docx`

The baseline is the 1,910-word pre-edit proposal identified in the Task 1–2 evidence report. The final export is the 1,930-word accepted result. Both files contain 159 paragraphs, no tables, one document section, and seven rendered pages in Microsoft Word.

## Verdict

**Partial pass; one formatting correction is required before Task 2 can be called complete.**

The intended Timeline edit is bounded correctly, and all protected and non-Timeline text is unchanged. However, the cover title changed from the Word `Title` style to `Heading 1`. This alters the heading hierarchy and contributes to pagination reflow. Correct the cover-title style, export again, and repeat this check.

| Check | Result | Evidence |
|---|---|---|
| Pricing unchanged | PASS | Both two-paragraph Pricing sections are text-identical. SHA-256 of normalized section text in both files: `17beee8a90e356228d8534c01930b55faf2a18676accde6eeb2ab7f9bb410386`. |
| Terms unchanged | PASS | Both two-paragraph Terms sections are text-identical. SHA-256 of normalized section text in both files: `c60fed9edd0177da732ea5f3b7f31e10db9d301b358e2c16a1983e40fecb2565`. |
| Non-Timeline text unchanged | PASS | Paragraph-by-paragraph comparison found no text difference outside the Timeline heading and its introductory paragraph. The document retained 159 paragraphs. |
| Revised Timeline inspected | PASS | `Timeline` became `Project Timeline`; only its introductory paragraph changed. All five week headings and all week-level activity/output/approval text are identical to the baseline. The required control sentence remains: “The six-week duration will not change without written agreement from both parties.” |
| Lists preserved | PASS | Both files contain 76 `List Bullet` paragraphs. Their ordered style-and-text digest is identical: `78a5ab24aa297e855414c410a2904764af0b62ffb3789266a752c67340a6f811`. |
| Page setup preserved | PASS | Page size, margins, header distance, and footer distance are identical. Word opens and repaginates both files successfully. |
| Page count | PASS | Microsoft Word renders both files as seven pages. |
| Heading hierarchy | FAIL | The cover title `Workflow Modernization Proposal` changed from `Title` to `Heading 1`. The baseline has 17 Heading 1 paragraphs plus one Title; the final has 18 Heading 1 paragraphs and no Title. Other heading levels are preserved, apart from the intended Timeline rename. |
| Pagination stability | REVIEW REQUIRED | Page count remains seven, but page boundaries reflow. For example, baseline page 1 ends with the first Current State paragraph, while final page 1 ends at the Current State heading. The longer Timeline introduction also shifts later content. There is no extra page, but a final visual review is required after restoring the title style. |
| Overall formatting | FAIL | The unchanged page setup, list structure, and page count pass, but the cover-title style regression prevents an overall formatting pass. |

## Exact document differences

Only these paragraph-level differences were found:

1. Cover title style: `Title` → `Heading 1` (unintended).
2. Timeline heading text: `Timeline` → `Project Timeline` (intended).
3. Timeline introduction: revised to describe stages, deliverables, approval points, and the preserved six-week control sentence (intended).

No other paragraph text or paragraph style differs.

## Required corrective action

1. Change only the cover paragraph `Workflow Modernization Proposal` back to the Word `Title` style.
2. Export the corrected document again without changing the accepted Timeline.
3. Re-run the protected-section, non-Timeline, heading, list, and Word pagination checks.
4. Mark the build complete only when the heading hierarchy and final visual review pass.

## Method

- Parsed both DOCX packages with `python-docx` and compared paragraph text, paragraph styles, list order, document sections, and page settings.
- Hashed normalized Pricing, Terms, and ordered list content with SHA-256.
- Opened both files read-only in Microsoft Word 16, forced repagination, recorded page/paragraph/word counts, and exported verification PDFs.
- Compared Word-reported page boundaries to identify reflow.

Generated verification renders:

- `verification-baseline.pdf`
- `verification-final.pdf`

