from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional
from decimal import Decimal


class VehicleBase(BaseModel):
    regNo: Optional[str] = None
    chassis: Optional[str] = None
    engine: Optional[str] = None
    vehicleManufacturerName: Optional[str] = None
    model: Optional[str] = None
    vehicleColour: Optional[str] = None
    type: Optional[str] = None
    normsType: Optional[str] = None
    bodyType: Optional[str] = None
    ownerCount: Optional[int] = None
    owner: Optional[str] = None
    ownerFatherName: Optional[str] = None
    mobileNumber: Optional[str] = None
    status: Optional[str] = None
    statusAsOn: Optional[datetime] = None
    regAuthority: Optional[str] = None
    regDate: Optional[datetime] = None
    vehicleManufacturingMonthYear: Optional[str] = None
    rcExpiryDate: Optional[datetime] = None
    vehicleTaxUpto: Optional[str] = None
    vehicleInsuranceCompanyName: Optional[str] = None
    vehicleInsuranceUpto: Optional[datetime] = None
    vehicleInsurancePolicyNumber: Optional[str] = None
    rcFinancer: Optional[str] = None
    presentAddress: Optional[str] = None
    permanentAddress: Optional[str] = None
    vehicleCubicCapacity: Optional[Decimal] = None
    grossVehicleWeight: Optional[int] = None
    unladenWeight: Optional[int] = None
    vehicleCategory: Optional[str] = None
    rcStandardCap: Optional[str] = None
    vehicleCylindersNo: Optional[int] = None
    vehicleSeatCapacity: Optional[int] = None
    vehicleSleeperCapacity: Optional[int] = None
    vehicleStandingCapacity: Optional[int] = None
    wheelbase: Optional[int] = None
    vehicleNumber: Optional[str] = None
    puccNumber: Optional[str] = None
    puccUpto: Optional[datetime] = None
    blacklistStatus: bool = False
    blacklistDetails: Optional[dict] = None
    permitIssueDate: Optional[datetime] = None
    permitNumber: Optional[str] = None
    permitType: Optional[str] = None
    permitValidFrom: Optional[datetime] = None
    permitValidUpto: Optional[datetime] = None
    nonUseStatus: Optional[str] = None
    nonUseFrom: Optional[str] = None
    nonUseTo: Optional[str] = None
    nationalPermitNumber: Optional[str] = None
    nationalPermitUpto: Optional[str] = None
    nationalPermitIssuedBy: Optional[str] = None
    isCommercial: bool = False
    nocDetails: Optional[str] = None
    financed: bool = False
    class_: Optional[str] = None


class VehicleCreate(VehicleBase):
    pass


class VehicleUpdate(VehicleBase):
    pass


class VehicleResponse(VehicleBase):
    id: UUID
    
    class Config:
        from_attributes = True
