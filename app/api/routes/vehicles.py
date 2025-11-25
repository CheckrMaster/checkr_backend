from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_, and_
from typing import List
from uuid import UUID

from app.db.session import get_db
from app.models.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate, VehicleUpdate, VehicleResponse


router = APIRouter(prefix="/vehicles", tags=["Vehicles"])


@router.post("/", response_model=VehicleResponse, status_code=status.HTTP_201_CREATED)
async def create_vehicle(
    vehicle_data: VehicleCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new vehicle"""
    vehicle = Vehicle(**vehicle_data.model_dump())
    db.add(vehicle)
    await db.commit()
    await db.refresh(vehicle)
    return vehicle


@router.get("/", response_model=List[VehicleResponse])
async def get_vehicles(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """Get all vehicles with pagination"""
    result = await db.execute(
        select(Vehicle).offset(skip).limit(limit)
    )
    vehicles = result.scalars().all()
    return vehicles


@router.get("/search", response_model=List[VehicleResponse])
async def search_vehicles(
    regNo: str | None = None,
    chassis: str | None = None,
    engine: str | None = None,
    db: AsyncSession = Depends(get_db)
):
    """Search vehicles by registration number, chassis, and/or engine number"""
    if not any([regNo, chassis, engine]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one search parameter (regNo, chassis, or engine) must be provided"
        )
    
    # Build query conditions
    conditions = []
    if regNo:
        conditions.append(Vehicle.regNo.ilike(f"%{regNo}%"))
    if chassis:
        conditions.append(Vehicle.chassis.ilike(f"%{chassis}%"))
    if engine:
        conditions.append(Vehicle.engine.ilike(f"%{engine}%"))
    
    # Use OR condition to match any of the provided parameters
    query = select(Vehicle).where(or_(*conditions))
    
    result = await db.execute(query)
    vehicles = result.scalars().all()
    
    if not vehicles:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No vehicles found matching the search criteria"
        )
    
    return vehicles


@router.get("/{regNo}", response_model=VehicleResponse)
async def get_vehicle(
    regNo: str,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific vehicle by registration number"""
    result = await db.execute(
        select(Vehicle).where(Vehicle.regNo == regNo)
    )
    vehicle = result.scalar_one_or_none()
    
    if not vehicle:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vehicle with regNo {regNo} not found"
        )
    
    return vehicle


@router.put("/{vehicle_id}", response_model=VehicleResponse)
async def update_vehicle(
    vehicle_id: UUID,
    vehicle_data: VehicleUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update a vehicle"""
    result = await db.execute(
        select(Vehicle).where(Vehicle.id == vehicle_id)
    )
    vehicle = result.scalar_one_or_none()
    
    if not vehicle:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vehicle with id {vehicle_id} not found"
        )
    
    # Update only provided fields
    update_data = vehicle_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(vehicle, field, value)
    
    await db.commit()
    await db.refresh(vehicle)
    return vehicle


@router.delete("/{vehicle_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_vehicle(
    vehicle_id: UUID,
    db: AsyncSession = Depends(get_db)
):
    """Delete a vehicle"""
    result = await db.execute(
        select(Vehicle).where(Vehicle.id == vehicle_id)
    )
    vehicle = result.scalar_one_or_none()
    
    if not vehicle:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vehicle with id {vehicle_id} not found"
        )
    
    await db.delete(vehicle)
    await db.commit()
    return None
