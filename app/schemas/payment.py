from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional
from decimal import Decimal


class PaymentBase(BaseModel):
    order_id: UUID
    amount: Decimal
    payment_method: str
    status: str


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    amount: Optional[Decimal] = None
    payment_method: Optional[str] = None
    status: Optional[str] = None


class PaymentResponse(PaymentBase):
    id: UUID
    payment_date: datetime
    
    class Config:
        from_attributes = True
