from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings
from app.db.session import engine
from app.db.base import Base
from app.api.routes import users, vehicles, orders, payments, invoices


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events"""
    try:
        # Create tables on startup with timeout handling
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("Database tables created successfully")
    except Exception as e:
        print(f"Warning: Database setup failed: {e}")
        # Continue without failing - tables might already exist
    
    yield
    
    # Cleanup on shutdown
    try:
        await engine.dispose()
        print("Database connections closed")
    except Exception as e:
        print(f"Warning: Database cleanup failed: {e}")


# Initialize FastAPI app with optimizations
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to FastAPI Async Application",
        "version": settings.APP_VERSION
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


# Include routers
app.include_router(users.router, prefix="/api")
app.include_router(vehicles.router, prefix="/api")
app.include_router(orders.router, prefix="/api")
app.include_router(payments.router, prefix="/api")
app.include_router(invoices.router, prefix="/api")


if __name__ == "__main__":
    import uvicorn
    import os
    
    port = int(os.environ.get("PORT", 8000))
    debug = os.environ.get("DEBUG", "True").lower() == "true"
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=debug,
        workers=1 if debug else 4,
        access_log=not debug,
        log_level="info" if not debug else "debug"
    )
