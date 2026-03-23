from fastapi import FastAPI
from pydantic import BaseModel

class AddRequest(BaseModel):
    a: int
    b: int


def register_routes(app: FastAPI):
    @app.get("/api/health")
    def health():
        return {"status": "ok"}
    
    @app.post("/api/add")
    def add(request: AddRequest):
        result = request.a + request.b
        return {"result": result}