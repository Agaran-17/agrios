from fastapi import FastAPI
from app.routers import farmers

app = FastAPI(title="AgriOS API")

app.include_router(farmers.router)


@app.get("/health")
def health():
    return {"status": "ok"}