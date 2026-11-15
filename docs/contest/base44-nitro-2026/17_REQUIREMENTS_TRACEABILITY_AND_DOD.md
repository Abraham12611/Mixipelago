# 17 — Requirements Traceability, Acceptance Gates and Definition of Done

## Traceability table

| Requirement ID | Source | Evidence | Acceptance |
|---|---|---|---|
| CE-R01 | Terms 6.1(b/c) | New Base44 project creation/edit history | Owner/organizer confidence recorded |
| CE-R02 | Terms 6.1(a/d) | Anonymous browser walkthrough | No download, login or purchase |
| CE-R03 | Terms 6.1(e) | Published Base44 URL + uptime plan | Public through required period |
| CE-R04 | Terms 6.1(f) | Asset/contributor licence register | Every asset rights-cleared |
| CE-R05 | Terms 5 | Manual confirmation receipt | Submitted before hard UTC deadline |
| CE-R06 | Terms 8.4 | Outreach policy | No manipulated votes |
| CE-G01 | Batch 2 | Pure merge tests | No double-claimed inputs |
| CE-G02 | Batch 3 | Ordered serve tests | Newly merged matching output serves oldest |
| CE-G03 | Batch 4 | Cove 001 replay | Two-order win and terminal priority |
| CE-G04 | Batch 5 | Campaign graph validator | Every selectable mission published/proven |
| CE-U01 | UX specification | Owner device screenshots | Responsive/no obscured controls |
| CE-U02 | Accessibility | Automated checks + owner run | Labels, motion/sound settings, touch alternatives |
| CE-S01 | Save contract | Save migration/corruption tests | Playable when storage unavailable |
| CE-Q01 | QA matrix | Test logs and owner approval | No P0/P1 at submission |

## Definition of Done — document level

- Each feature has a named owner, release gate, test evidence, user-visible states and rollback.
- Published-only content separation proven.
- No invented server-backed scores, grants, virtual-currency purchases or login requirement.
- All rights provenance and Base44 build evidence indexed.
- Owners approve any unresolved compliance ambiguity **before public submission**.

## Definition of Done — release level

- [ ] New Base44 project really built in contest period.
- [ ] Public, no-login Base44 URL tested by owner on mobile and desktop.
- [ ] At least 8 actual playable original missions, 12 targeted only if fully proven.
- [ ] Eight-tier physics loop and deterministic serving pass automated tests.
- [ ] All published missions solvable and their exits/retry paths functional.
- [ ] Original art/music and attributions cleared.
- [ ] Guest saves, corruption fallback, and pause/restart behavior verified.
- [ ] No broken or deceptive buttons.
- [ ] No purchase/ads/account requirements.
- [ ] No P0 or P1 issues; documented owner manual test signoff.
- [ ] Submission form completed before deadline and confirmation archived.
- [ ] Frozen release reproducible and uptime owner assigned.

## Evidence filename pattern

CE-R03_guest_access_YYYYMMDD_browser.png; CE-G03_cove001_replay.json; CE-U01_owner_manual_report.md; CE-IP_assets_manifest.json. Do not generate fake evidence or check a test that was not run. Store private account identifiers outside repository.
