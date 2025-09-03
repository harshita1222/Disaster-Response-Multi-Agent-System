# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.agents.triage_agent import score_incident

app = FastAPI()

# Allow Streamlit/HF frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (narrow down later if needed)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"msg": "Disaster Response System API running"}

@app.post("/triage")
def triage(incident: dict):
    return {
        "incident_id": incident.get("id", "unknown"),
        **score_incident(incident)
    }

