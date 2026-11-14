# 36 — Versioning, Migration, Rollback and Integrity Preservation

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Version dimensions
`achievementDefinitionEpoch`, `collectionEdition`, `rewardPolicyVersion`, `itemAssetRevision`, `sourceReceiptRulesVersion`, and `competitiveProfileVersion` are distinct. A content rename should not reset a player's acquisition history. Breaking threshold changes should publish a new achievement epoch or explicit migration mapping.

## Safe migration examples
- Raise an achievement threshold 10→20: preserve prior earned tier, new epoch for future rules.
- Add items to album: publish a new `edition2`, retain previously completed `edition1` badge.
- Remove shop decoration from new sales: keep already owned inventory accessible; fall back visual if rights require asset withdrawal.
- Change payout amount: new policy version only for future claims; previously created entitlement payload remains pinned to published promise when applicable.

## Rollback
Disable new grants via gate and retain read access/claim history. Re-run reconciliation. Revert client presentation independently. Never drop wallet ledger, delete claim receipts, or quietly confiscate cosmetics to repair a content publishing mistake.

## Operational playbook
1. Freeze affected program.
2. Query outstanding entitlements/claims and source versions.
3. Identify affected players using source proofs.
4. Write repair migration or audited compensation, with owner approval.
5. Verify settlement and communicate changes in release notes.

## Compatibility with alpha
Do not migrate client-local preview coins, badges or unlocked trophies into server-authoritative rewards. If transitioning old tutorial UI, preserve their local display but label as unverified legacy preview.
