from app.core import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.mixins import IdPkMixin


class CountryOfOrigin(IdPkMixin, Base):
    __tablename__ = "country_of_origin"
    name: Mapped[str]

    phones = relationship(
            "Phone",
            back_populates="country_of_origin"
            )
