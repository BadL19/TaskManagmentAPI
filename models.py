from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    full_name = Column(String)
    email = Column(String, index = True, unique = True, nullable = False)
    password = Column(String, nullable = False)
    is_active = Column(Boolean, default=True) 
    created_at = Column(DateTime, server_default=func.now())
    tasks = relationship("Task", back_populates = "owner")

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key = True, index = True)
    task_name = Column(String, index = True, nullable = False)
    task_description = Column(String)
    is_completed = Column(Boolean, default = False)
    created_at = Column(DateTime, server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"), nullable = False) 
    owner = relationship("User", back_populates = "tasks")