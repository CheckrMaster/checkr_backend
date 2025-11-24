import uuid
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Text, Numeric, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base


class Vehicle(Base):
    __tablename__ = "vehicles"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    regNo = Column(String, index=True)
    chassis = Column(String)
    engine = Column(String)
    vehicleManufacturerName = Column(String)
    model = Column(String)
    vehicleColour = Column(String)
    type = Column(String)
    normsType = Column(String)
    bodyType = Column(String)
    ownerCount = Column(Integer)
    owner = Column(String)
    ownerFatherName = Column(String)
    mobileNumber = Column(String)
    status = Column(String)
    statusAsOn = Column(DateTime)
    regAuthority = Column(String)
    regDate = Column(DateTime)
    vehicleManufacturingMonthYear = Column(String)
    rcExpiryDate = Column(DateTime)
    vehicleTaxUpto = Column(String)
    vehicleInsuranceCompanyName = Column(String)
    vehicleInsuranceUpto = Column(DateTime)
    vehicleInsurancePolicyNumber = Column(String)
    rcFinancer = Column(String)
    presentAddress = Column(Text)
    permanentAddress = Column(Text)
    vehicleCubicCapacity = Column(Numeric)
    grossVehicleWeight = Column(Integer)
    unladenWeight = Column(Integer)
    vehicleCategory = Column(String)
    rcStandardCap = Column(String)
    vehicleCylindersNo = Column(Integer)
    vehicleSeatCapacity = Column(Integer)
    vehicleSleeperCapacity = Column(Integer)
    vehicleStandingCapacity = Column(Integer)
    wheelbase = Column(Integer)
    vehicleNumber = Column(String)
    puccNumber = Column(String)
    puccUpto = Column(DateTime)
    blacklistStatus = Column(Boolean, default=False)
    blacklistDetails = Column(JSON)
    permitIssueDate = Column(DateTime)
    permitNumber = Column(String)
    permitType = Column(String)
    permitValidFrom = Column(DateTime)
    permitValidUpto = Column(DateTime)
    nonUseStatus = Column(String)
    nonUseFrom = Column(String)
    nonUseTo = Column(String)
    nationalPermitNumber = Column(String)
    nationalPermitUpto = Column(String)
    nationalPermitIssuedBy = Column(String)
    isCommercial = Column(Boolean, default=False)
    nocDetails = Column(String)
    financed = Column(Boolean, default=False)
    class_ = Column("class", String)
    
    # Relationships
    orders = relationship("Order", back_populates="vehicle", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Vehicle(id={self.id}, regNo={self.regNo}, model={self.model})>"
