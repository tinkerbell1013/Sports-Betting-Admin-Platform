from pydantic import BaseModel

class AuditRead(BaseModel):
    id: int
    field_name: str
    old_value: str | None
    new_value: str | None
    changed_at: str

    class Config:
        from_attributes = True
