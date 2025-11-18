# app/main.py

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import settings
from app.db.qdrant_client import init_collection
from app.routes import ask, health, conversations
from app.schedulers.crawler_scheduler import start_scheduler, stop_scheduler, get_scheduled_jobs
from app.services.factory import get_embedder

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager.
    - Startup: Init DB + start scheduler
    - Shutdown: Stop scheduler
    """

    logger.info("=" * 80)
    logger.info("[APP] STARTING APPLICATION")
    logger.info("=" * 80)

    # ✅ STARTUP
    try:
        logger.info("[STARTUP] Initializing Qdrant collection...")
        init_collection()
        logger.info("[STARTUP] ✅ Qdrant initialized")

        # ✅ START SCHEDULER
        logger.info("[STARTUP] Starting background crawler scheduler...")
        start_scheduler(
            enable_daily_crawl=True,
            crawl_hour=2  # 2 AM daily
        )
        logger.info("[STARTUP] ✅ Scheduler started")

        logger.info("[STARTUP] Starting initiate embedder...")
        embedder = get_embedder()
        logger.info("[STARTUP] ✅ initiated embedder")

    except Exception as e:
        logger.error(f"[STARTUP] ❌ Error: {e}")
        raise

    logger.info("=" * 80)
    logger.info("[APP] APPLICATION READY")
    logger.info("=" * 80)

    # ✅ SHUTDOWN
    yield

    logger.info("=" * 80)
    logger.info("[SHUTDOWN] GRACEFUL SHUTDOWN")
    logger.info("=" * 80)

    try:
        stop_scheduler()
        logger.info("[SHUTDOWN] ✅ All resources cleaned up")
    except Exception as e:
        logger.error(f"[SHUTDOWN] ❌ Error: {e}")

    logger.info("=" * 80)


# Create app
app = FastAPI(
    title=settings.APP_NAME,
    description="RAG System for History & Tourism",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(ask.router, prefix="/ask", tags=["Ask"])
app.include_router(conversations.router, prefix="/conversations", tags=["Ask"])
app.include_router(health.router, prefix="/health", tags=["Health"])


# ✅ NEW: Endpoint để check scheduler
@app.get("/api/scheduler/jobs", tags=["Scheduler"])
async def get_jobs():
    """Get list of scheduled jobs."""
    jobs = get_scheduled_jobs()
    return {
        "status": "ok",
        "jobs": jobs,
        "total": len(jobs)
    }


@app.post("/api/scheduler/run-crawl", tags=["Scheduler"])
async def trigger_crawl_now():
    """Trigger daily crawl immediately (for testing)."""
    from app.schedulers.crawler_scheduler import run_daily_crawl
    import threading

    logger.info("[MANUAL] User triggered daily crawl")

    # Run in background thread
    thread = threading.Thread(target=run_daily_crawl, daemon=True)
    thread.start()

    return {
        "status": "ok",
        "message": "Daily crawl triggered",
        "note": "Running in background"
    }


@app.get("/", tags=["Root"])
async def root():
    return {
        "app": settings.APP_NAME,
        "version": "1.0.0",
        "status": "running",
        "scheduler": "active"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
