from app.core import Base
from sqlalchemy.orm import Mapped, mapped_column,relationship


class Brand(Base):
    __tablename__ = "brand"
    name: Mapped[str] = mapped_column(
            unique=True,
            nullable=False
            )

    models = relationship(
            "Model",
            back_populates="brand"
            )

    phones = relationship(
            "Phone",
            back_populates="brand"
            )
