"""
Database initialization script
Run this to create all tables in the database
"""
import asyncio
from app.db.session import engine
from app.db.base import Base
from app.models import User, Vehicle, ServiceHistory, Order, Payment, Invoice


async def init_db():
    """Initialize database tables"""
    async with engine.begin() as conn:
        # Drop all tables (use with caution in production)
        # await conn.run_sync(Base.metadata.drop_all)
        
        # Create all tables
        await conn.run_sync(Base.metadata.create_all)
    
    print("Database tables created successfully!")


if __name__ == "__main__":
    asyncio.run(init_db())
