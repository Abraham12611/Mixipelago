/** Mixipelago design reference only. Not shipped code. */
export interface VersionedEnvelope<T> {
  eventId: string; schemaVersion: 1; occurredAt: string;
  rulesHash: string; actorId?: string; payload: T;
}
export type UiFeatureGate='always'|'CAMPAIGN_MAP'|'TRUSTED_ECONOMY'|'PLAYER_SKILLS'|'REWARD_INVENTORY'|'RANKED_WEEKLY'|'FESTIVAL_HUB'|'FRIENDS'|'CREWS';
export interface ScreenDefinition {route:string;owner:string;gate:UiFeatureGate;minRelease:string;}
export function visibleScreen(screen:ScreenDefinition,enabled:ReadonlySet<string>):boolean {
  return screen.gate==='always'||enabled.has(screen.gate);
}
export interface GameHudProjection {status:'aiming'|'active'|'paused'|'won'|'lost';score:number;activeOrders:ReadonlyArray<{orderId:string;tier:number;remaining:number}>;previewCoins:number;}
