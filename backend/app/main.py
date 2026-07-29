from fastapi import FastAPI
app = FastAPI(title="AgriOS API")
@app.get("/health")
def health():
    return {"status": "ok"}