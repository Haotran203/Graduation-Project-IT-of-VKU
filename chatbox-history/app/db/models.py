from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Conversation(Base):
    """
    Conversation table for long-term storage.
    Stores conversation metadata and relationships to messages.
    """
    __tablename__ = "conversations"

    # UUID from frontend (String, not UUID type)
    id = Column(String(36), primary_key=True)
    title = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    meta_data = Column(JSONB, default={}, nullable=False)  # ← CHANGED from 'metadata'

    # Relationship to messages
    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan",
        lazy="dynamic",
        order_by="Message.created_at"
    )

    # Indexes
    __table_args__ = (
        Index('idx_conversations_updated_at', 'updated_at'),
        Index('idx_conversations_created_at', 'created_at'),
    )

    def to_dict(self):
        """Convert to dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "metadata": self.meta_data,  # ← Return as 'metadata' for API compatibility
            "message_count": self.messages.count() if self.messages else 0
        }

    def __repr__(self):
        return f"<Conversation(id={self.id}, title={self.title})>"


class Message(Base):
    """
    Message table for storing individual messages.
    Each message belongs to a conversation.
    """
    __tablename__ = "messages"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    conversation_id = Column(
        String(36),
        ForeignKey("conversations.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    role = Column(String(50), nullable=False, index=True)  # 'user' or 'assistant'
    content = Column(Text, nullable=False)
    sources = Column(JSONB, default=[], nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    meta_data = Column(JSONB, default={}, nullable=False)  # ← CHANGED from 'metadata'

    # Relationship back to conversation
    conversation = relationship("Conversation", back_populates="messages")

    # Indexes
    __table_args__ = (
        Index('idx_messages_conversation_id', 'conversation_id'),
        Index('idx_messages_conversation_created', 'conversation_id', 'created_at'),
        Index('idx_messages_role', 'role'),
    )

    def to_dict(self):
        """Convert to dictionary."""
        return {
            "id": str(self.id),
            "conversation_id": self.conversation_id,
            "role": self.role,
            "content": self.content,
            "sources": self.sources,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "metadata": self.meta_data  # ← Return as 'metadata' for API compatibility
        }

    def __repr__(self):
        return f"<Message(id={self.id}, role={self.role}, conversation_id={self.conversation_id})>"
