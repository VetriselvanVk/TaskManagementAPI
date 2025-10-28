from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import user, task
from app.routers import auth, task_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(auth.router)
app.include_router(task_router.router)
