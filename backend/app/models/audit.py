from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

class AuditLog(Base):
    __tablename__ = "audit_log"

    id: Mapped[int] = mapped_column(primary_key=True)
    table_name: Mapped[str] = mapped_column(String)
    record_id: Mapped[int] = mapped_column(Integer)
    field_name: Mapped[str] = mapped_column(String)
    old_value: Mapped[str | None]
    new_value: Mapped[str | None]
    changed_at: Mapped[str] = mapped_column(DateTime)
