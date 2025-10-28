from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from typing import List
from app.core.auth import get_current_user
from app.models.user import User
from app.utils.response import success_response, error_response

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=None)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User | dict = Depends(get_current_user)):
    if isinstance(current_user, dict) and current_user.get("status") == -1:
        return current_user  
    db_task = Task(**task.dict(), user_id=current_user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return success_response("Task Created Successfull")


@router.get("/", response_model=None)
def list_tasks(db: Session = Depends(get_db), current_user: User | dict = Depends(get_current_user)):
    if isinstance(current_user, dict) and current_user.get("status") == -1:
        return current_user 
    return success_response("Task Fetched Successfull", db.query(Task).filter(Task.user_id == current_user.id).order_by(Task.due_date).all())


@router.put("/{task_id}", response_model=None)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db), current_user: User | dict = Depends(get_current_user)):
    if isinstance(current_user, dict) and current_user.get("status") == -1:
        return current_user 
    db_task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not db_task:
        return error_response("Task not found")
    for key, value in task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return success_response("Task Updated Successfull")


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User | dict = Depends(get_current_user)):
    if isinstance(current_user, dict) and current_user.get("status") == -1:
        return current_user 
    db_task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not db_task:
        return error_response("Task not found")
    db.delete(db_task)
    db.commit()
    return success_response("Task deleted successfully")
