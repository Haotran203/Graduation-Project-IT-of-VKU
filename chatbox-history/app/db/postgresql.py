import logging
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import QueuePool
from sqlalchemy.engine import Engine

from app.config.settings import settings
from app.db.models import Base

logger = logging.getLogger(__name__)

engine = create_engine(
    settings.POSTGRESQL_URL,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True, 
    pool_recycle=3600,
    echo=settings.POSTGRESQL_ECHO,
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# SQLite compatibility (for testing)
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_conn, connection_record):
    """Enable foreign keys for SQLite."""
    if 'sqlite' in str(settings.POSTGRESQL_URL):
        cursor = dbapi_conn.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


def init_db():
    """
    Initialize database tables.
    Creates all tables defined in models.py
    """
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("[PostgreSQL] ✓ Database tables initialized successfully")
    except Exception as e:
        logger.error(f"[PostgreSQL] ✗ Error initializing database: {e}")
        raise


def drop_db():
    """
    Drop all database tables (use with caution!).
    """
    try:
        Base.metadata.drop_all(bind=engine)
        logger.warning("[PostgreSQL] ⚠ All database tables dropped")
    except Exception as e:
        logger.error(f"[PostgreSQL] ✗ Error dropping database: {e}")
        raise


@contextmanager
def get_db_session() -> Generator[Session, None, None]:
    """
    Context manager for database sessions.

    Usage:
        with get_db_session() as db:
            conversation = db.query(Conversation).first()
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"[PostgreSQL] Session error: {e}")
        raise
    finally:
        db.close()


def get_db() -> Generator[Session, None, None]:
    """
    Dependency for FastAPI routes.

    Usage:
        @app.get("/api/conversations")
        def get_conversations(db: Session = Depends(get_db)):
            return db.query(Conversation).all()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_connection() -> bool:
    """
    Check database connection health.

    Returns:
        bool: True if connection is healthy
    """
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        logger.info("[PostgreSQL] ✓ Connection healthy")
        return True
    except Exception as e:
        logger.error(f"[PostgreSQL] ✗ Connection failed: {e}")
        return False
