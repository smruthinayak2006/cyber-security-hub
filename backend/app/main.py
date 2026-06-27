from fastapi import FastAPI

from app.routers.hash import router as hash_router

app = FastAPI(
    title="Cyber Security Engineering Hub API",
    description="Backend API for cybersecurity tools",
    version="0.1.0",
)

app.include_router(hash_router)


@app.get("/")
def root():
    return {
        "message": "Cyber Security Engineering Hub API is running."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }