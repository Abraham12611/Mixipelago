# 28 — Content Studio: Authoring, Review and Publication

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Internal workflow
Draft achievement/item/album/policy → schema lint → cross-reference test → economic-budget simulation → accessibility/localization review → security review → preview on test account → approve versioned release → staged feature gate → monitor → retain rollback path. No production client can create/approve its own reward definition.

## Roles
Game designer authors rules and copy; economy reviewer approves spendable budgets; security reviewer approves source trust and eligibility; artist approves visuals; release coordinator publishes; support may view receipts but may not mint arbitrary funds. Two-person approval for compensation and any reward whose source is an operator grant.

## Validation gates
Reject duplicate `achievementId`, unknown item references, unbounded numeric counters, source-event types not in the allowlist, malformed UTC windows, reward loops, reward budgets exceeding caps, invalid collection denominators and enabled programs depending on disabled upstream features.

## Preview tools
Show example player progress for fresh and long-term accounts, claimed/pending states, multiple reward tiers, and cross-device retry. Allow deterministic sample event sequences with a dry-run read-only resolver. Show catalog diff: added items, retired achievements, changed thresholds, changed payout lines and affected players.

## Release safety
Catalog assets are immutable by hash and published by signed manifest; game client fetches a CDN copy for display but reward settlement resolves server-pinned content. Gate by environment and cohort. Rollback disables new claims but preserves already-earned entitlements and history; never delete awards to 'undo' a bad deployment without explicit corrective process.
