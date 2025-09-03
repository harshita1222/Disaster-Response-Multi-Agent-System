# app/agents/ingest_agent.py
import json
import random
import uuid
from datetime import datetime

def simulate_incident():
    """Generate a random simulated disaster incident."""
    incidents = [
        "Building collapse with trapped people",
        "Flooded street, stranded vehicles",
        "Massive fire in residential area",
        "Road accident with multiple casualties",
        "Earthquake damage to infrastructure",
    ]
    return {
        "id": str(uuid.uuid4())[:8],
        "description": random.choice(incidents),
        "location": {
            "lat": round(random.uniform(-90, 90), 4),
            "lon": round(random.uniform(-180, 180), 4),
        },
        "casualties": random.randint(0, 20),
        "time": datetime.utcnow().isoformat()
    }

def load_incidents_from_file(filepath="demo_data/sample_incidents.json"):
    """Load incidents from a JSON file."""
    with open(filepath, "r") as f:
        return json.load(f)
