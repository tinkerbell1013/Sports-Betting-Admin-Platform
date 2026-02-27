from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

class Bet(Base):
    __tablename__ = "bets"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
    stake: Mapped[float] = mapped_column(Numeric)
    odds: Mapped[float]
