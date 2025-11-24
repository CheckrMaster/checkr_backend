import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.db.base import Base


class ServiceHistory(Base):
    __tablename__ = "service_history"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vin = Column(String, index=True)
    file_path = Column(String)
    status_on = Column(DateTime)
    
    def __repr__(self):
        return f"<ServiceHistory(id={self.id}, vin={self.vin})>"
