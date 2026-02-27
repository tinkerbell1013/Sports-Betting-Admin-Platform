from pydantic import BaseModel

class BetBase(BaseModel):
    customer_id: int
    event_id: int
    stake: float
    odds: float

class BetCreate(BetBase):
    pass

class BetRead(BetBase):
    id: int

    class Config:
        from_attributes = True
