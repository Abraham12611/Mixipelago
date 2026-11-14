/** Mixipelago reference-only pure rules. No network, wallet grant or production integration. */
export type Decision<T> = { ok: true; value: T } | { ok: false; code: string };
export type Actor = { playerId:string; roles:ReadonlySet<string> };
export function canAccessOwned(actor: Actor | null, ownerId: string): boolean { return !!actor && (actor.playerId === ownerId || actor.roles.has('admin')); }
export type Proof = { signed:boolean; catalogPinned:boolean; normalizedRankedProfile:boolean };
export function eligibleRankedProof(p: Proof): boolean { return p.signed && p.catalogPinned && p.normalizedRankedProfile; }
// Actual JWT verification, RLS and Rapier replay verification run server-side.
