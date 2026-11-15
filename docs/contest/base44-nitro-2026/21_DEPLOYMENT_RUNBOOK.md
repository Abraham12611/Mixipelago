# 21 — Base44 Deployment, Stability and Freeze Runbook

## Roles

**Build lead:** publishes tested new Base44 project and controls current deployed revision.  
**Release coordinator:** owns release checklist, rollback, monitoring and PR approvals.  
**Owner/entrant:** runs manual gameplay acceptance and official contest form.  
**Art/IP lead:** verifies included assets and licences.

## Pre-deploy

- Checkout approved contest source version and cross-check Base44 sync direction.
- Run unit, mission content and production build tests.
- Audit env/config: guest play on, payments/ads/required auth off.
- Verify draft missions and unfinished screens do not show as active.
- Confirm deployed assets only from approved rights inventory.
- Capture version IDs, deployment timestamp, sources and validation output.
- Avoid embedding private Base44 credentials in shipped JavaScript.

## Publish procedure

1. Publish using Base44-supported workflow from the *new* contest project.
2. Record public Base44 URL; do not substitute custom domain.
3. Open from private browsing, cold session and mobile network.
4. Follow guest Play → first merge → first mission win → results → map.
5. Check browser console, static assets, focus and mobile safe areas.
6. Run owner-directed manual test checklist.
7. If pass, mark release candidate. If fail, rollback or re-publish corrected version, re-test.

## After publish, before submission

- Generate at least one authentic screenshot, 15–45s demo clip.
- Export sanitized Base44 creation/edit history and pinned source commit.
- Verify the contact email/contest form fields without putting personal details into GitHub.
- Record time remaining in UTC; submit early enough to recover form issues.

## Freeze policy

Per terms, changes are allowed until Dec 3 23:59 UTC; after that, avoid **material changes** until winner announcement. Section 6.1 also expects stable public availability without material changes from submission through judging, so prefer early final acceptance and no unnecessary modifications. For severe technical fixes, record cause and consult organizer when a material change is possible.

## Availability

- Keep URL public and stable through judging and at least **90 days after actual winner announcement**; do not delete project, break deployment or enable login/paywall.
- Check availability from a public unauthenticated browser at a reasonable cadence. An external monitor may query the page but not emulate prohibited contest votes or submission.
- Monitor actual game route and asset success, not just HTTP 200 from Home.
- Retain build evidence, known-good assets, config and rollback reference.

## Incident handling

**P0:** game not loadable, no guest play, licensing incident. Notify owner, preserve evidence, restore approved build.  
**P1:** one critical mission broken or serious mobile input regression. Triage, choose rollback to a known-good build, owner retest.  
**P2:** cosmetic issue. Leave for after judging if change risks material alteration.

When rollback is used, check whether it counts as a material change under contest rules and seek clarification if needed.

## End of obligation

Track the **actual** winner announcement date, count 90 days, then have owner decide whether to keep the Base44 app live. Never rely solely on the provisional Dec 10 date.
