from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional
from decimal import Decimal


class InvoiceBase(BaseModel):
    order_id: UUID
    total_amount: Decimal
    status: str
    due_date: Optional[datetime] = None


class InvoiceCreate(InvoiceBase):
    pass


class InvoiceUpdate(BaseModel):
    total_amount: Optional[Decimal] = None
    status: Optional[str] = None
    due_date: Optional[datetime] = None


class InvoiceResponse(InvoiceBase):
    id: UUID
    invoice_date: datetime
    
    class Config:
        from_attributes = True
