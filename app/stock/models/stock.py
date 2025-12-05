from sqlalchemy import ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core import Base
from app.mixins import IdPkMixin, TimestampMixin


class Stock(Base, IdPkMixin, TimestampMixin):
    __tablename__ = "stock"

    phone_id: Mapped[int] = mapped_column(
        ForeignKey("phone.id"),
        nullable=False)

    color_id: Mapped[int] = mapped_column(
        ForeignKey("color.id"),
        nullable=False)

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0)

    phone = relationship(
        "Phone",
        back_populates="stocks")

    color = relationship(
        "Color",
        back_populates="stocks")


    __table_args__ = (
        UniqueConstraint("phone_id", "color_id", name="uix_phone_color"),)

