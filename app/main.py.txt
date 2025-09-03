# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.agents.triage_agent import score_incident
from app.agents.optimizer_agent import allocate_resources

app = FastAPI()

class Incident(BaseModel):
    id: str
    description: str
    location: dict
    casualties: int = 0

@app.post("/triage")
def triage(inc: Incident):
    s = score_incident(inc.dict())
    return {"incident_id": inc.id, "score": s['score'], "reason": s['reason']}

@app.post("/allocate")
def allocate(payload: dict):
    incidents = payload.get("incidents", [])
    assets = payload.get("assets", [])
    alloc = allocate_resources(incidents, assets)
    return {"allocations": alloc}
