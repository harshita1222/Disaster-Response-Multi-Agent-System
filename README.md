# Disaster Response — Multi-Agent System

## Problem statement
Coordinate emergency response during disasters by triaging incidents, recommending routing, and allocating limited resources automatically.

## Architecture
- Streamlit dashboard (UI)
- FastAPI orchestrator
- Agents: ingest | triage | routing | optimizer | comms
- LLMs for reasoning (triage & plans)

## Run locally (dev)
1. Clone repo
2. `python -m venv venv && source venv/bin/activate`
3. `pip install -r requirements.txt`
4. Start API: `uvicorn app.main:app --reload --port 8000`
5. Start UI: `streamlit run streamlit_app/app.py`

## LLM configuration
Set `OPENAI_API_KEY` in environment (or configure HF wrapper in `app/llm_client.py`).

## Submission
- Link to this GitHub repo
- Streamlit demo link (if deployed)
- README includes architecture and run steps
