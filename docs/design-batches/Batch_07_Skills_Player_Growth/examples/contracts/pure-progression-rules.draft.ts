/** Batch 7 reference-only pure TypeScript rules. No I/O, auth, DB or actual skill publishing. */
export type ErrorCode = 'LEVEL_REQUIRED'|'PREREQUISITE_MISSING'|'INSUFFICIENT_POINTS'|'SKILL_RANK_SEQUENCE'|'SKILL_ALREADY_MAXED'|'NODE_UNPUBLISHED'|'MODE_DISABLED';
export const MAX_LEVEL = 20;
export function xpToNext(level: number): bigint {
  if (!Number.isSafeInteger(level) || level < 1 || level >= MAX_LEVEL) throw new RangeError('level out of bounds');
  const x = BigInt(level - 1);
  return 100n + 35n*x + 5n*x*x;
}
export function cumulativeXp(level: number): bigint {
  if (!Number.isSafeInteger(level) || level < 1 || level > MAX_LEVEL) throw new RangeError('invalid level');
  let total = 0n;
  for (let l=1; l<level; l++) total += xpToNext(l);
  return total;
}
export function levelForTotalXp(totalXp: bigint): number {
  if (totalXp < 0n) throw new RangeError('negative XP');
  let level = 1;
  while (level < MAX_LEVEL && totalXp >= cumulativeXp(level+1)) level++;
  return level;
}
export function earnedPointsFromLevel(level: number): number {
  return Math.max(0, Math.min(MAX_LEVEL, level)-1);
}
export function vipProbability(base: number, seating: number, guestlistRank: number, reputation: number, cap=0.20): number {
  const parts=[base,seating,guestlistRank,reputation,cap];
  if (parts.some(x => !Number.isFinite(x)) || !Number.isInteger(guestlistRank) || guestlistRank < 0) throw new RangeError('bad value');
  return Math.min(cap, Math.max(0, base + seating + 0.01 * guestlistRank + reputation));
}
export function discountedCoinPrice(basePrice: number, discount: number): number {
  if (!Number.isSafeInteger(basePrice) || basePrice < 0 || !Number.isFinite(discount) || discount < 0 || discount > 0.15) throw new RangeError('bad price or discount');
  // For production server wallet, use integer basis points or an exact decimal library.
  const basisPoints = Math.round(discount * 10000);
  return basePrice - Math.floor(basePrice * basisPoints / 10000);
}
