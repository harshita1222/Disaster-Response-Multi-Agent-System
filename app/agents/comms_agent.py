# app/agents/comms_agent.py
from app.llm_client import call_openai

def generate_team_message(incident, asset):
    """Generate a message for the rescue team assigned to an incident."""
    prompt = f"""
You are a rescue operation assistant.
Incident: {incident['description']} at {incident['location']}
Assigned team: {asset['type']} unit {asset['id']}
Write a short clear action message (max 2 sentences).
"""
    return call_openai(prompt, model="gpt-3.5-turbo", max_tokens=80)

def generate_public_alert(incident):
    """Generate a safety message for the public near the incident."""
    prompt = f"""
Incident reported: {incident['description']} at {incident['location']}.
Write a short alert for the public with safety precautions.
"""
    return call_openai(prompt, model="gpt-3.5-turbo", max_tokens=80)
