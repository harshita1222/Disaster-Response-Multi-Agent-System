# app/db.py
import json
from pathlib import Path

DB_FILE = Path("demo_data/incidents_log.json")

def save_incident(incident):
    """Append incident to DB file."""
    data = []
    if DB_FILE.exists():
        data = json.loads(DB_FILE.read_text())
    data.append(incident)
    DB_FILE.write_text(json.dumps(data, indent=2))

def load_all_incidents():
    """Load all incidents from DB file."""
    if DB_FILE.exists():
        return json.loads(DB_FILE.read_text())
    return []
