/** Mixipelago Batch 9: pure reference functions; not production backend code. */
export type WeightedGuest = { customerId: string; weight: number };
export type CustomerPool = { poolId: string; entries: WeightedGuest[]; vipBaseBps: number; vipCapBps: number };
export type ObservedService = { verified: boolean; missionWon: boolean; fulfilled: boolean; extraBonus: number; penalty: number };
export const clamp = (min: number, max: number, value: number): number => Math.max(min, Math.min(max, value));

/** Percentage points in basis points (10000 = 100%). No percentage-of-percentage stacking. */
export function vipChanceBps(baseBps: number, modifiersBps: readonly number[], capBps = 2000): number {
  if (![baseBps, capBps, ...modifiersBps].every(Number.isSafeInteger)) throw new TypeError('integer basis points only');
  return clamp(0, clamp(0, 10000, capBps), baseBps + modifiersBps.reduce((a,b) => a+b, 0));
}

/** Sample within a pinned, published class with a versioned PRNG draw. */
export function selectWeightedGuest(entries: readonly WeightedGuest[], draw: number): string {
  const ordered = [...entries].filter(e => e.weight > 0).sort((a,b) => a.customerId.localeCompare(b.customerId,'en'));
  if (!ordered.length || ordered.some(e => !Number.isSafeInteger(e.weight))) throw new Error('invalid pool');
  const total = ordered.reduce((sum,e) => sum + e.weight, 0);
  if (!Number.isSafeInteger(total) || !Number.isSafeInteger(draw) || draw < 0 || draw >= total) throw new Error('draw out of range');
  let cumulative = 0;
  for (const e of ordered) { cumulative += e.weight; if (draw < cumulative) return e.customerId; }
  throw new Error('unreachable');
}

/** Candidates only. Do not call on local preview sessions. */
export function satisfactionIfEligible(e: ObservedService): number | null {
  if (!e.verified || !e.missionWon) return null;
  if (!Number.isSafeInteger(e.extraBonus) || !Number.isSafeInteger(e.penalty)) throw new TypeError('integer policy components only');
  const bonus = clamp(0,400,e.extraBonus);
  const penalty = clamp(0,1500,e.penalty);
  return clamp(0,10000,5000 + (e.fulfilled ? 2200 : 0) + 600 + bonus - penalty);
}

/** Reputation on a score already derived from a verified run. */
export function boundedReputationDelta(satisfaction: number, runAccum: number): number {
  if (![satisfaction,runAccum].every(Number.isSafeInteger)) throw new TypeError('integers only');
  const perEncounter = clamp(-30,30,Math.floor((clamp(0,10000,satisfaction)-5000)/100));
  return clamp(-60,60,runAccum+perEncounter) - runAccum;
}

export function loyaltyVisitPoints(firstVisit: boolean, favoriteMatched: boolean, eligible: boolean): number {
  if (!eligible) return 0;
  return Math.min(220,(firstVisit ? 100:180) + (favoriteMatched ? 40:0));
}
export function loyaltyTier(total: number): string {
  if (!Number.isSafeInteger(total) || total < 0) throw new Error('invalid total');
  return total>=1300 ? 'island_legend' : total>=700 ? 'friend_of_shop' : total>=300 ? 'regular' : total>=100 ? 'acquaintance' : 'stranger';
}

/** Consumer idempotency belongs in DB, not this sample. Canonical identity: */
export function customerSourceKey(playerId: string, shopId: string, sourceEncounterId: string): string {
  return JSON.stringify([playerId, shopId, sourceEncounterId]);
}
