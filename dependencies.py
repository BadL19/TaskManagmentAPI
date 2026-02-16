from database import get_db
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends

db_dependency = Annotated[Session, Depends(get_db)]