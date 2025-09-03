# app/agents/triage_agent.py
from app.llm_client import call_openai

def score_incident(incident):
    """
    incident: dict with fields: id, description, casualties, location, time
    returns: priority score (1-100) and reason
    """
    prompt = f"""
You are an emergency triage assistant. Given incident details in JSON, produce:
- a priority score 1-100 (100 highest)
- a short reason (1-2 sentences)
JSON: {incident}
Respond as: SCORE: <int>\\nREASON: <text>
"""
    out = call_openai(prompt, model="gpt-3.5-turbo")
    # naive parse:
    score = 50
    reason = out
    for line in out.splitlines():
        if line.upper().startswith("SCORE:"):
            try:
                score = int(line.split(":",1)[1].strip())
            except:
                pass
        if line.upper().startswith("REASON:"):
            reason = line.split(":",1)[1].strip()
    return {"score": score, "reason": reason}
