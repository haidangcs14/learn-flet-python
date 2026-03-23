from fastapi import FastAPI

def register_routes(app: FastAPI):
    @app.get("/api/health")
    def health():
        return {"status": "ok"}