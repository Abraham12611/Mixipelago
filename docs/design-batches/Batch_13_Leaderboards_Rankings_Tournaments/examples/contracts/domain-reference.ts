/** Mixipelago design reference only. Not shipped code. */
export interface VersionedEnvelope<T> {
  eventId: string; schemaVersion: 1; occurredAt: string;
  rulesHash: string; actorId?: string; payload: T;
}
export type OfficialState='pending'|'verified'|'rejected';
export interface RankRow {playerId:string;score:number;shots:number;activeTicks:number;verifiedAt:string;trustStatus:OfficialState;}
/** Negative return => a ranks ahead of b. Verified rows ONLY. */
export function compareRank(a:RankRow,b:RankRow):number {
  if(a.score!==b.score)return b.score-a.score;
  if(a.shots!==b.shots)return a.shots-b.shots;
  if(a.activeTicks!==b.activeTicks)return a.activeTicks-b.activeTicks;
  if(a.verifiedAt!==b.verifiedAt)return a.verifiedAt.localeCompare(b.verifiedAt);
  return a.playerId.localeCompare(b.playerId);
}
