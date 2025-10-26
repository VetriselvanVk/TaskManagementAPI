from pydantic import BaseModel
from datetime import date
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str
    due_date: date
    status: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    priority: Optional[str]
    due_date: Optional[date]
    status: Optional[str]

class TaskResponse(TaskBase):
    id: int
    class Config:
        from_attributes = True
