from app.core.models import Base
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'
    pass
    
    
