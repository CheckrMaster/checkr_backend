#!/usr/bin/env python3
"""
Startup script for production deployment
Handles graceful startup with better error handling
"""
import os
import sys
import asyncio
import logging
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def check_database_connection():
    """Check if database is reachable before starting workers"""
    try:
        from app.db.session import engine
        from sqlalchemy import text
        
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        logger.info("Database connection successful")
        return True
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        return False

def get_worker_count() -> int:
    """Determine optimal worker count based on environment"""
    # Get from environment or default to 1 for memory-constrained environments
    workers = os.getenv("WORKERS", "1")
    try:
        return max(1, int(workers))
    except (ValueError, TypeError):
        return 1

def get_gunicorn_config() -> list:
    """Build Gunicorn configuration"""
    workers = get_worker_count()
    port = os.getenv("PORT", "8000")
    
    config = [
        "gunicorn",
        "main:app",
        "-w", str(workers),
        "-k", "uvicorn.workers.UvicornWorker",
        "-b", f"0.0.0.0:{port}",
        "--timeout", "120",
        "--worker-connections", "1000",
        "--max-requests", "1000",
        "--max-requests-jitter", "100",
        "--access-logfile", "-",
        "--error-logfile", "-",
        "--log-level", "info"
    ]
    
    # Add preload for production if we have multiple workers
    if workers > 1:
        config.append("--preload")
    
    return config

async def main():
    """Main startup function"""
    logger.info("Starting FastAPI application...")
    
    # Check database connection with retries
    max_retries = 3
    for attempt in range(max_retries):
        if await check_database_connection():
            break
        if attempt < max_retries - 1:
            logger.warning(f"Database check attempt {attempt + 1} failed, retrying in 5 seconds...")
            await asyncio.sleep(5)
        else:
            logger.error("Database connection failed after all retries")
            # Continue anyway - the app might still work or DB might come up later
    
    # Build and execute Gunicorn command
    config = get_gunicorn_config()
    logger.info(f"Starting with config: {' '.join(config)}")
    
    try:
        os.execvp(config[0], config)
    except Exception as e:
        logger.error(f"Failed to start Gunicorn: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())