# app/agents/optimizer_agent.py
def allocate_resources(incidents, assets):
    """
    incidents: list of dicts with 'score', 'location'
    assets: list of available units {'id','type','capacity','location'}
    returns: allocations list of (asset_id, incident_id)
    """
    # sort incidents by score descending
    incidents_sorted = sorted(incidents, key=lambda x: x['score'], reverse=True)
    allocations = []
    used_assets = set()
    for inc in incidents_sorted:
        for a in assets:
            if a['id'] in used_assets:
                continue
            # simple nearest heuristic (placeholder)
            allocations.append({"asset_id": a['id'], "incident_id": inc['id']})
            used_assets.add(a['id'])
            break
    return allocations
