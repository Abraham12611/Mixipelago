# 24 — Content Authoring and Validation Fixtures

The examples in this directory are **planning fixtures**, not a running game or a real published content catalog.

## Example files

- [contest-plan.draft.json](examples/contest-plan.draft.json) — 12 proposed mission IDs, all **draft/unpublished**, disabled higher-risk features, no public Base44 URL or project creation claimed.
- [qa-checks.draft.json](examples/qa-checks.draft.json) — evidence checklist, all pending; assign actual human/automated outcome after tests.
- [rights-inventory.template.json](examples/rights-inventory.template.json) — blank asset rights and proof register; entries added only when files have actually been authored/cleared.
- [validate_contest_plan.py](tools/validate_contest_plan.py) — pure structural validator. It **does not** verify Base44 eligibility, playable physics, real rights, legal residence, owner manual QA or submission.

## Publishing data

To declare a mission published, set the flag only after actual gameplay code and assets exist, a seed-based legal winning replay has been recorded, static checks passed and **owner manual gameplay acceptance** is documented. The example manifest must not be used to turn a draft concept into playable stage.

When a real Base44 project exists, capture its actual URL and project timestamp **in secure build evidence**, then update a deployed config separate from this draft. Do not commit credentials or personally identifying details. Preserve the original draft for planning history.

## Validation command

From directory docs/contest/base44-nitro-2026:

~~~bash
python3 tools/validate_contest_plan.py
~~~

The validator uses Python standard library only. Do not claim game implementation or owner QA passes simply because JSON parses.
