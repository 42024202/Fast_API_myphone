from app.core import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.mixins.id_pk_mixin import IdPkMixin


class Storage(Base, IdPkMixin):
    __tablename__ = "storage"
    size:Mapped[int]

    phones = relationship(
        "Phone",
        back_populates="storage"
    )
