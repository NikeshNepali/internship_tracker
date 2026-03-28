from fastapi import FastAPI
from app.routes import applications

app = FastAPI(title="Internship Tracker API")
app.include_router(applications.router, prefix="/applications")
@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}
