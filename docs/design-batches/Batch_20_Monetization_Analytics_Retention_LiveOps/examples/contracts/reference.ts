/** Mixipelago reference-only pure rules. No network, wallet grant or production integration. */
export type Decision<T> = { ok: true; value: T } | { ok: false; code: string };
export type Offer = { id:string; published:boolean; enabled:boolean; category:'cosmetic'|'bundle'|'pass' };
export function maySettlePurchase(offer:Offer, providerVerified:boolean, commerceOn:boolean):boolean {return commerceOn && offer.published && offer.enabled && providerVerified;}
export function paidEffectInRanked():false { return false; }
export function adsRequiredForMainline():false { return false; }
// Platform receipts must be validated server-side before entitlements are granted.
