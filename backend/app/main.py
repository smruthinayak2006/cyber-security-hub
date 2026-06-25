from fastapi import FastAPI


app = FastAPI(
    title="Cyber Security Engineering Hub API",
    description="Backend API for security tools and resources",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Cyber Security Hub API running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
