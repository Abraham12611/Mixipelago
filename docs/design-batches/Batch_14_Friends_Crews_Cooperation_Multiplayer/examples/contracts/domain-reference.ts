/** Mixipelago design reference only. Not shipped code. */
export interface VersionedEnvelope<T> {
  eventId: string; schemaVersion: 1; occurredAt: string;
  rulesHash: string; actorId?: string; payload: T;
}
export interface FriendPair {leftId:string;rightId:string;}
export function canonicalPair(a:string,b:string):FriendPair {
  if(a===b)throw new Error('SELF_FRIEND_REQUEST');
  return a<b?{leftId:a,rightId:b}:{leftId:b,rightId:a};
}
export type FriendState='none'|'requested'|'accepted'|'declined'|'canceled'|'blocked';
export function effectiveState(current:FriendState,isBlocked:boolean):FriendState {
  return isBlocked?'blocked':current;
}
