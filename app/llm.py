import requests

def query_llm(prompt: str) -> str:
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return r.json()["response"]
