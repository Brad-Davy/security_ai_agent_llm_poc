from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str
    context: str | None = None

class QueryResponse(BaseModel):
    response: str
