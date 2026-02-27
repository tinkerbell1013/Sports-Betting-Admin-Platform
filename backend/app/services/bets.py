from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.bet import Bet
from app.schemas.bet import BetCreate

async def list_bets(session: AsyncSession) -> list[Bet]:
    result = await session.execute(select(Bet))
    return list(result.scalars().all())

async def create_bet(session: AsyncSession, data: BetCreate) -> Bet:
    bet = Bet(**data.model_dump())
    session.add(bet)
    await session.commit()
    await session.refresh(bet)
    return bet
