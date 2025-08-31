from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.database import create_tables
from app.routers import profile, query, health, auth

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("krittika_api")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up Krittika API")
    create_tables()
    yield
    logger.info("Shutting down Krittika API")

app = FastAPI(
    title="Candidate Profile Playground",
    description="A FastAPI playground for managing candidate profiles",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(profile.router, prefix="/api/v1", tags=["profile"])
app.include_router(query.router, prefix="/api/v1", tags=["query"])
app.include_router(health.router, prefix="/api/v1", tags=["health"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)