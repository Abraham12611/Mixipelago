/** Mixipelago reference-only pure rules. No network, wallet grant or production integration. */
export type Decision<T> = { ok: true; value: T } | { ok: false; code: string };
export type VerifiedSessionReceipt = { receiptId:string; playerId:string; resultHash:string; rulesHash:string; trust:'verified' };
export type GrantKey = { playerId:string; sourceType:string; sourceId:string; policyId:string };
export function grantKey(g: GrantKey): string { return [g.playerId,g.sourceType,g.sourceId,g.policyId].join(':'); }
export function canGrant(receipt: VerifiedSessionReceipt | null, alreadyGranted: boolean, isLocalPreview: boolean): boolean {
  return !!receipt && receipt.trust === 'verified' && !alreadyGranted && !isLocalPreview;
}
// Real settlements require a DB transaction with a unique grantKey, ledger entries and outbox.
