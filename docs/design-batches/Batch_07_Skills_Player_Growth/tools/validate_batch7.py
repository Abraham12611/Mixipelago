#!/usr/bin/env python3
"""Batch 7 static catalog and pure rule validation. Run from batch root; no dependencies."""
from pathlib import Path
import json, copy, math

BASE=Path(__file__).resolve().parents[1]
def load(path): return json.loads((BASE/path).read_text(encoding='utf-8'))
catalog=load('examples/catalog/skills-catalog.draft.json')
curve=load('examples/catalog/entrepreneur-xp-policy.draft.json')
xpv=load('examples/tests/xp-rule-vectors.json')
rulev=load('examples/tests/allocation-modifier-rule-vectors.json')

assert catalog['publicationState']=='DRAFT_NOT_SHIPPED'
branch_ids=[x['branchId'] for x in catalog['branches']]
assert len(branch_ids)==6 and len(set(branch_ids))==6
nodes=catalog['nodes']; by_id={x['skillId']:x for x in nodes}
assert len(nodes)==30 and len(by_id)==len(nodes)
assert sum(n['status']=='pilot' for n in nodes)==6
assert all(n['branchId'] in branch_ids for n in nodes)
assert all(n['maxRank']>=1 and n['minPlayerLevel']>=1 and n['pointCostPerRank']>=1 for n in nodes)
assert all(len(n['effects'])>=1 for n in nodes)
assert all(e['operation'] in {'flat_add','percentage_point_add','multiplier_add','bool_unlock','capacity_add'} for n in nodes for e in n['effects'])
# Validate DAG and no pilot->draft dependency.
state={}
def visit(node_id):
 s=state.get(node_id,0)
 if s==1: raise AssertionError('Cycle in graph '+node_id)
 if s==2:return
 state[node_id]=1
 n=by_id[node_id]
 for required in n['requiredSkillRanks']:
  ref=required['skillId']; assert ref in by_id, (node_id,ref)
  parent=by_id[ref]
  assert required['rank']<=parent['maxRank']
  if n['status']=='pilot': assert parent['status']=='pilot',(node_id,ref)
  visit(ref)
 state[node_id]=2
for id in by_id:visit(id)
# Every enabled node is reachable in cap and available point budget (conservative chain cost).
def cost_to(node_id,visited=None):
 visited=set() if visited is None else visited
 if node_id in visited:return 0
 visited.add(node_id)
 n=by_id[node_id]
 return n['pointCostPerRank']+sum(cost_to(p['skillId'],visited) for p in n['requiredSkillRanks'])
for n in nodes:
 if n['status']=='pilot':
  assert n['minPlayerLevel']<=20
  assert cost_to(n['skillId'])<=19
# XP threshold curve exactness and monotonicity.
assert curve['maxLevel']==20
cum=0
for level in range(1,21):
 assert curve['cumulativeXpForLevel'][level-1]=={'level':level,'threshold':cum}
 if level<20:
  needed=100+35*(level-1)+5*(level-1)**2
  assert curve['xpToNextByCurrentLevel'][level-1]=={'level':level,'xpRequired':needed}
  cum+=needed
assert curve['pointMilestones']==list(range(2,21))
def level_from_xp(xp):
 if xp<0:raise ValueError('negative xp')
 return max(x['level'] for x in curve['cumulativeXpForLevel'] if x['threshold']<=xp)
def purchase(v):
 n=by_id[v['skillId']]
 if n['status']!='pilot':return 'NODE_UNPUBLISHED'
 if v['level']<n['minPlayerLevel']:return 'LEVEL_REQUIRED'
 cur=v['ranks'].get(v['skillId'],0)
 if v['rank']>n['maxRank']:return 'SKILL_ALREADY_MAXED'
 if v['rank']!=cur+1:return 'SKILL_RANK_SEQUENCE'
 if n.get('requiredFeatureFlag') and n['requiredFeatureFlag'] not in v.get('enabledFlags',[]):return 'MODE_DISABLED'
 if any(v['ranks'].get(p['skillId'],0)<p['rank'] for p in n['requiredSkillRanks']):return 'PREREQUISITE_MISSING'
 if v['balance']<n['pointCostPerRank']:return 'INSUFFICIENT_POINTS'
 return 'ALLOW'
for v in xpv:
 if v['kind']=='level_from_xp':
  assert level_from_xp(v['xp'])==v['expectedLevel'],v
  assert min(level_from_xp(v['xp'])-1,19)==v['expectedEarnedPoints'],v
 elif v['kind']=='xp_to_next':
  assert 100+35*(v['level']-1)+5*(v['level']-1)**2==v['expectedXpRequired'],v
 else:raise AssertionError(v)
for v in rulev:
 kind=v['kind']
 if kind=='valid_purchase': assert purchase(v)==v['expected'],(v,purchase(v))
 elif kind=='modifier_vip':
  got=min(v['cap'],max(0,v['base']+v['seating']+v['guestlistRank']*.01+v['reputation']))
  assert math.isclose(got,v['expected'],abs_tol=1e-12),(v,got)
 elif kind=='discount':
  val=v['price']-math.floor(v['price']*round(v['discount']*10000)/10000)
  assert val==v['expectedPrice'],v
 elif kind=='competitive_normalization':
  assert v['expectedMode']=='STANDARDIZED' and v['expectedVipBonus']==0
 elif kind=='respec':
  assert v['expectedAllocated']==0 and v['expectedAvailable']==v['earned']
 else: raise AssertionError(kind)
# Optional syntax validation if jsonschema installed.
try:
 import jsonschema
 jsonschema.Draft202012Validator(load('examples/schemas/skill-catalog.schema.json')).validate(catalog)
 print('JSON Schema: passed')
except ModuleNotFoundError:
 print('JSON Schema: skipped (install jsonschema to enable syntax schema validation)')
print(f'Batch 7 validated: {len(nodes)} nodes, {len(branch_ids)} branches, {len(xpv)} XP vectors, {len(rulev)} allocation/effect vectors, DAG and cap checks passed')
