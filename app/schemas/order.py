from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional
from decimal import Decimal


class OrderBase(BaseModel):
    user_id: UUID
    vehicle_id: Optional[UUID] = None
    order_type: str
    status: str
    total_amount: Decimal


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    order_type: Optional[str] = None
    status: Optional[str] = None
    total_amount: Optional[Decimal] = None


class OrderResponse(OrderBase):
    id: UUID
    order_date: datetime
    
    class Config:
        from_attributes = True
