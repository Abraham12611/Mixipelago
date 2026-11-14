#!/usr/bin/env python3
"""Batch 5 draft/staged campaign graph lint, sample-only; NOT a physics solution proof.
Usage: python tools/validate_batch5.py
"""
from pathlib import Path
import json, sys, collections
from jsonschema import Draft202012Validator
BASE=Path(__file__).resolve().parents[1]
EX=BASE/'examples'
SCHEMA=json.loads((EX/'schemas/campaign-graph.schema.json').read_text())

def err(message, bag): bag.append(message)
def eval_rule(rule, progress):
    op=rule['op']; stars=progress.get('stars',{}); flags=progress.get('flags',{}); claims=set(progress.get('claims',[]))
    if op=='always':return True
    if op=='missionCleared':return stars.get(rule['missionId'],0)>=rule.get('minStars',1)
    if op=='minStars':return sum(stars.get(m,0) for m in rule['missionIds'])>=rule['count']
    if op=='nodeClaimed':return rule['nodeId'] in claims
    if op=='flagEquals':return flags.get(rule['flagId'])==rule['value']
    if op=='allOf':return all(eval_rule(r,progress) for r in rule['rules'])
    if op=='anyOf':return any(eval_rule(r,progress) for r in rule['rules'])
    raise ValueError(f'Unsupported unlock expression: {op}')

def leaves(rule, depth=0):
    if depth>8:raise ValueError('rule depth exceeds 8')
    if rule['op'] in ('allOf','anyOf'):
        return sum(leaves(r,depth+1) for r in rule['rules'])
    return 1

def bad_star_bounds(rule):
    if rule['op']=='minStars' and rule['count'] > 3 * len(rule['missionIds']):
        return True
    if rule['op'] in ('allOf','anyOf'):
        return any(bad_star_bounds(r) for r in rule['rules'])
    return False

def references(rule):
    op=rule['op']
    if op=='missionCleared':return [('mission',rule['missionId'])]
    if op=='minStars':return [('mission',m) for m in rule['missionIds']]
    if op=='nodeClaimed':return [('node',rule['nodeId'])]
    if op in ('allOf','anyOf'):
        return [r for x in rule['rules'] for r in references(x)]
    return []

def cycle_check(edges):
    successors=collections.defaultdict(list)
    for u,v in edges: successors[u].append(v)
    color={}; cycle=[]
    def visit(u,stack):
        if color.get(u)==1:
            cycle.extend(stack[stack.index(u):]+[u]);return True
        if color.get(u)==2:return False
        color[u]=1
        for v in successors[u]:
            if visit(v,stack+[v]):return True
        color[u]=2
        return False
    for u in list(successors):
        if color.get(u)!=2 and visit(u,[u]):return cycle
    return None

def check_graph(path):
    g=json.loads(path.read_text()); errors=[];warnings=[]
    failures=list(Draft202012Validator(SCHEMA).iter_errors(g))
    for v in failures:errors.append('schema: '+'/'.join(map(str,v.absolute_path))+': '+v.message)
    if failures:return errors,warnings
    nodes={}; islands={}; chapters={}; edges={}; missions={}
    for i in g['islands']:
        if i['islandId'] in islands:err('duplicate island '+i['islandId'],errors)
        islands[i['islandId']]=i
    for c in g['chapters']:
        if c['chapterId'] in chapters:err('duplicate chapter '+c['chapterId'],errors)
        chapters[c['chapterId']]=c
        if c['islandId'] not in islands:err('chapter missing island '+c['chapterId'],errors)
    for n in g['nodes']:
        nid=n['nodeId']
        if nid in nodes:err('duplicate node '+nid,errors)
        nodes[nid]=n
        if n['islandId'] not in islands:err('node missing island '+nid,errors)
        if n['chapterId'] not in chapters:err('node missing chapter '+nid,errors)
        elif chapters[n['chapterId']]['islandId']!=n['islandId']:err('node chapter wrong island '+nid,errors)
        if n['critical'] and n['visibility']=='hidden' and n['status']!='draft':err('hidden critical node '+nid,errors)
        if n['type']=='mission':
            if n['status'] in ('published','staged') and not n.get('mission'):
                err('non-draft mission node lacks real mission ref '+nid,errors)
            ref=n.get('mission')
            mid=(ref or {}).get('missionId') or n.get('futureMissionId')
            if not mid:err('mission node has no mission or futureMissionId '+nid,errors)
            if mid in missions:err('duplicate mission mapped to nodes '+mid,errors)
            else:missions[mid]=nid
            if ref:
                p=EX/'missions'/f'{mid}.json'
                if p.exists():
                    data=json.loads(p.read_text())
                    if data.get('missionId')!=mid or data.get('missionVersion')!=ref['missionVersion']:
                        err('pinned mission identity/version mismatch '+nid,errors)
                elif n['status']!='draft':err('missing authored mission '+mid,errors)
                else:warnings.append('draft missing mission '+mid)
            elif n['status']=='draft': warnings.append('draft placeholder '+nid)
        try:
            if bad_star_bounds(n['unlock']):err('impossible theoretical star sum '+nid,errors)
            if leaves(n['unlock'])>64:err('unlock leaves exceed 64 '+nid,errors)
            if n.get('discoveryRule') and leaves(n['discoveryRule'])>64:err('discovery leaves exceed 64 '+nid,errors)
        except ValueError as e:err(str(e)+' '+nid,errors)
    for i in g['islands']:
        if i['entryNodeId'] not in nodes:err('island missing entry node '+i['islandId'],errors)
        elif nodes[i['entryNodeId']]['islandId']!=i['islandId']:
            err('island entry wrong island '+i['islandId'],errors)
    for e in g['edges']:
        key=e['edgeId']
        if key in edges:err('duplicate edge '+key,errors)
        edges[key]=e
        if e['from'] not in nodes or e['to'] not in nodes:err('dangling edge '+key,errors)
        if e['from']==e['to']:err('self edge '+key,errors)
        if e['from'] in nodes and e['to'] in nodes:
            if nodes[e['from']]['islandId']!=nodes[e['to']]['islandId'] and e['kind']!='gateway':err('cross-island edge needs gateway '+key,errors)
    # Visual graph connectivity: every currently active critical node must be connected
    # from its island entry, independently of unlock rule satisfiability.
    routes=collections.defaultdict(list)
    for e in g['edges']:
        if e['from'] in nodes and e['to'] in nodes:
            routes[e['from']].append(e['to'])
    for island in g['islands']:
        start=island['entryNodeId']; seen={start}; todo=[start]
        while todo:
            u=todo.pop()
            for v in routes.get(u,[]):
                if v not in seen:seen.add(v);todo.append(v)
        for n in nodes.values():
            if n['islandId']!=island['islandId'] or not n['critical'] or n['status']=='retired':continue
            if g['publicationStatus']=='draft' and n['status']=='draft': continue
            if n['nodeId'] not in seen:err('disconnected critical node '+n['nodeId'],errors)
    depend=[]
    for n in nodes.values():
        for name,expr in [('unlock',n['unlock']),('discovery',n.get('discoveryRule'))]:
            if expr is None:continue
            for kind,target in references(expr):
                if kind=='node':
                    if target not in nodes:err('missing referenced node '+target+' on '+n['nodeId'],errors)
                    else:depend.append((target,n['nodeId']))
                else:
                    if target not in missions:
                        if g['publicationStatus']=='draft':warnings.append('unresolved draft mission gate '+target+' on '+n['nodeId'])
                        else:err('unknown mission gate '+target+' on '+n['nodeId'],errors)
                    else:depend.append((missions[target],n['nodeId']))
    cycle=cycle_check(depend)
    if cycle:err('dependency cycle '+' -> '.join(cycle),errors)
    for n in nodes.values():
        if n['type']=='gateway' and n.get('destinationIslandId') not in islands:
            if g['publicationStatus']=='draft':warnings.append('external draft island gateway '+n['nodeId'])
            else:err('gateway destination missing '+n['nodeId'],errors)
    if g['publicationStatus']=='published':
        if g.get('exampleNotDeployed'):err('exampleNotDeployed cannot be production published',errors)
        for n in nodes.values():
            if n['status']=='staged' and n['critical']:err('published critical route has staged node '+n['nodeId'],errors)
    if g['publicationStatus'] in ('staged','published'):
        warnings.append('STATIC ONLY: no physical winning replay or manual UX proof provided')
    return errors,warnings

def main():
    import hashlib
    ok=True
    for path in sorted((EX/'worlds').glob('*.json')):
        errors,warnings=check_graph(path)
        print(f'{path.name}: {"PASS" if not errors else "FAIL"} ({len(errors)} errors, {len(warnings)} warnings)')
        for issue in errors:print('  ERROR:',issue)
        for issue in warnings[:5]:print('  note:',issue)
        ok &= not bool(errors)
    tests=json.loads((EX/'tests/unlock-rule-vectors.json').read_text())
    for case in tests:
        actual=eval_rule(case['rule'],case.get('progress',{}))
        if actual != case['expected']:
            print('UNLOCK TEST FAILURE',case['name'],actual,case['expected']);ok=False
    print(f'Pure unlock rule vectors: {len(tests)} cases')
    negatives=['dangling-edge.json','dependency-cycle.json','missing-mission.json','invalid-unlock-rule.json','disconnected-critical.json','hidden-critical.json','impossible-star-threshold.json']
    for name in negatives:
        errors,_=check_graph(EX/'tests'/name)
        if not errors:
            print('INVALID FIXTURE WAS ACCEPTED:',name);ok=False
        else:print('Expected rejection:',name,'->',errors[0])
    # Exact bytes check: source mission examples copied without edit, no rewriting Batch4 definitions.
    prior=Path('/mnt/data/Mixipelago_Batch_04_Gameplay_Modes_Level_Design/examples/missions')
    if prior.exists():
        for name in ('coconut-cove-001.json','coconut-cove-002.json'):
            a=(EX/'missions'/name).read_bytes(); b=(prior/name).read_bytes()
            if a!=b:print('BYTE DRIFT:',name);ok=False
            else:print('Unchanged mission:',name,hashlib.sha256(a).hexdigest()[:12])
    print('RESULT:', 'PASS' if ok else 'FAIL')
    return 0 if ok else 1
if __name__=='__main__':sys.exit(main())
