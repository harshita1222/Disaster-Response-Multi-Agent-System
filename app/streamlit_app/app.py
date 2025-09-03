# streamlit_app/app.py
import streamlit as st
import requests
import json

API_BASE = st.secrets.get("api_base", "http://localhost:8000")

st.title("Disaster Response — Demo Dashboard")

with st.form("new_incident"):
    id = st.text_input("Incident ID")
    desc = st.text_area("Description")
    casualties = st.number_input("Casualties", min_value=0, step=1)
    submit = st.form_submit_button("Send")
    if submit:
        payload = {"id": id or "inc1", "description": desc, "location": {"lat":0,"lon":0}, "casualties": casualties}
        r = requests.post(f"{API_BASE}/triage", json=payload)
        st.write(r.json())
