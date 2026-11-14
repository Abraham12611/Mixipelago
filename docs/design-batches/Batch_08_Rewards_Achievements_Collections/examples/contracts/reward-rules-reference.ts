/** Pure reference helpers; not authorization or settlement code. */
export function distinctCount(eventIds: readonly string[]): number {
  return new Set(eventIds).size;
}
export function crossedThresholds(before: number, after: number, thresholds: readonly number[]): number[] {
  if (!Number.isSafeInteger(before) || !Number.isSafeInteger(after) || after < before || before < 0) {
    throw new Error("Invalid monotonic counter");
  }
  return [...new Set(thresholds)].filter(t => t > before && t <= after).sort((a, b) => a - b);
}
export function albumProgress(eligible: readonly string[], owned: readonly string[]) {
  const allowed = new Set(eligible);
  if (!allowed.size) throw new Error("Album cannot be empty");
  const n = new Set(owned.filter(id => allowed.has(id))).size;
  return { owned: n, total: allowed.size, percent: Math.round(100 * n / allowed.size) };
}
export function isFirstClaim(sourceKey: string, grantedSourceKeys: ReadonlySet<string>): boolean {
  return !grantedSourceKeys.has(sourceKey);
}
// Server must validate claims and commit ownership/ledger changes atomically.
// These helpers intentionally do not grant XP, coins or inventory.
