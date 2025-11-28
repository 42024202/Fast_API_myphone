from ...core.models import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "user"
    username:Mapped[str] = mapped_column(String(50), unique=True)

