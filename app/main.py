from fastapi import FastAPI
from app.models import QueryRequest, QueryResponse
from app.prompt import build_prompt
from app.llm import query_llm

app = FastAPI(title="LLM API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest):
    prompt = build_prompt(req.query, req.context)
    result = query_llm(prompt)

    return QueryResponse(response=result)
