import uuid
from sqlalchemy import Column, String, DateTime, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base


class Invoice(Base):
    __tablename__ = "invoices"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id"), nullable=False)
    invoice_date = Column(DateTime, default=datetime.utcnow)
    total_amount = Column(Numeric)
    status = Column(String)
    due_date = Column(DateTime, nullable=True)
    
    # Relationships
    order = relationship("Order", back_populates="invoices")
    
    def __repr__(self):
        return f"<Invoice(id={self.id}, order_id={self.order_id}, status={self.status})>"
