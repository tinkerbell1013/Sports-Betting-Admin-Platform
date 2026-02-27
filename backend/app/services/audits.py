from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.audit import AuditLog

async def get_audit_for_record(
    session: AsyncSession,
    table_name: str,
    record_id: int,
) -> list[AuditLog]:
    stmt = select(AuditLog).where(
        AuditLog.table_name == table_name,
        AuditLog.record_id == record_id,
    )
    result = await session.execute(stmt)
    return list(result.scalars().all())
