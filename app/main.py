from fastapi import FastAPI
from app.routers import auth

app = FastAPI(title="FastAPI MySQL Auth API")

app.include_router(auth.router)
