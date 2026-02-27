from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.schemas.bet import BetCreate, BetRead
from app.schemas.audit import AuditRead
from app.services.bets import list_bets, create_bet
from app.services.audits import get_audit_for_record

router = APIRouter(prefix="/bets", tags=["bets"])


@router.get("/", response_model=list[BetRead])
async def get_all_bets(
    session: AsyncSession = Depends(get_session),
) -> list[BetRead]:
    return await list_bets(session)


@router.post("/", response_model=BetRead, status_code=201)
async def add_bet(
    bet: BetCreate,
    session: AsyncSession = Depends(get_session),
) -> BetRead:
    return await create_bet(session, bet)


@router.get("/{bet_id}/audit", response_model=list[AuditRead])
async def bet_audit(
    bet_id: int,
    session: AsyncSession = Depends(get_session),
) -> list[AuditRead]:
    return await get_audit_for_record(session, "bets", bet_id)
