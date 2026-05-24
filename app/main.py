from fastapi import FastAPI
from app.routes import auth
from app.database import engine, text

app = FastAPI(title="Internship Tracker API")
app.include_router(auth.router, prefix="/auth")
@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

@app.get("/health")
def health():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "ok", "db": "connected"}
    
    except Exception as e:
        return {
            "status": "error",
            "db": "disconnected",
            "detail": str(e)
        }