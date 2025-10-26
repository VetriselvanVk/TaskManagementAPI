from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import user, task
from app.routers import auth, task_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")

app.include_router(auth.router)
app.include_router(task_router.router)
