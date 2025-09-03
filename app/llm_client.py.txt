# app/llm_client.py
import os
import openai

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def call_openai(prompt, model="gpt-3.5-turbo", max_tokens=200):
    if not OPENAI_API_KEY:
        raise Exception("Set OPENAI_API_KEY in env")
    resp = openai.ChatCompletion.create(
        model=model,
        messages=[{"role":"user","content":prompt}],
        max_tokens=max_tokens,
        temperature=0.2,
    )
    return resp['choices'][0]['message']['content'].strip()
