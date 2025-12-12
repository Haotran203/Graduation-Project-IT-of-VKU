# app/routes/health.py

from fastapi import APIRouter, HTTPException
from app.db.qdrant_client import get_client
from app.config.settings import settings
from app.schedulers.crawler_scheduler import get_scheduled_jobs
from datetime import datetime

router = APIRouter()


@router.get("/")
async def health_check():
    """Health check endpoint."""
    try:
        qdrant = get_client()
        count = qdrant.count(collection_name=settings.COLLECTION_NAME)
        jobs = get_scheduled_jobs()

        return {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "database": {
                "status": "connected",
                "documents": count.count,
                "collection": settings.COLLECTION_NAME
            },
            "scheduler": {
                "status": "active",
                "jobs": jobs
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
