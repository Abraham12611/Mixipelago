/** Mixipelago design reference only. Not shipped code. */
export interface VersionedEnvelope<T> {
  eventId: string; schemaVersion: 1; occurredAt: string;
  rulesHash: string; actorId?: string; payload: T;
}
export type QuestState='locked'|'available'|'active'|'completed'|'archived';
export type StoryCondition={type:'mission_cleared';missionId:string}|{type:'flag_eq';key:string;value:string}|{type:'all';items:StoryCondition[]};
export interface StoryChoice {sceneId:string;choiceId:string;expectedRevision:number;requestId:string;}
export function eligible(c:StoryCondition,missions:ReadonlySet<string>,flags:Readonly<Record<string,string>>):boolean {
  if(c.type==='mission_cleared') return missions.has(c.missionId);
  if(c.type==='flag_eq') return flags[c.key]===c.value;
  return c.items.every(x=>eligible(x,missions,flags));
}
