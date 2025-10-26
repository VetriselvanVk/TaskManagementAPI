from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255))
    priority = Column(String(10))
    due_date = Column(Date)
    status = Column(String(20))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")
