from typing import TYPE_CHECKING
from app.core.models import Base
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'
    
    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
    
