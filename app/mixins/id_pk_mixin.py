from sqlalchemy.orm import Mapped, mapped_column


class IdPkMixin:
    """Mixin for id primary key"""
    id: Mapped[int] = mapped_column(primary_key=True)
