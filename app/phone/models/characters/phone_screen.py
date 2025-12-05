from app.core import Base
from app.mixins import IdPkMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import String


class PhoneScreen(Base, IdPkMixin):
    __tablename__ = "phone_screen"

    display_name: Mapped[str]
    
    display_size: Mapped[float]

    refresh_rate: Mapped[int]

    phones = relationship(
        "Phone",
        back_populates="screen"
    )
