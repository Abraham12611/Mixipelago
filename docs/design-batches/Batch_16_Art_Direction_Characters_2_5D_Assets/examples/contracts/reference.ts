/** Mixipelago reference-only pure rules. No network, wallet grant or production integration. */
export type Decision<T> = { ok: true; value: T } | { ok: false; code: string };
export const DRINKS = ['citrus-shot','sunny-lemon','sunset-splash','blossom-fizz','coral-martini','mint-lagoon','ocean-cloud','crown-of-isles'] as const;
export function drinkIdForTier(tier: number): string | null { return Number.isInteger(tier) && tier >= 1 && tier <= 8 ? DRINKS[tier - 1] : null; }
export type VisualAsset = { id: string; available: boolean; rightsApproved: boolean; kind: 'sprite' | 'icon'; digest?: string };
export function chooseAsset(asset?: VisualAsset): string { return asset?.available && asset.rightsApproved && asset.digest ? asset.id : 'ui.drink.labeled-placeholder'; }
export function visualSkinHasCompetitiveEffect(): false { return false; }
