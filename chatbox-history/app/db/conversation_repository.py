import logging
from typing import List, Optional, Dict
from datetime import datetime

from sqlalchemy import desc, func, or_
from sqlalchemy.orm import Session

from app.db.models import Conversation, Message
from app.db.postgresql import get_db_session

logger = logging.getLogger(__name__)


class ConversationRepository:
    """
    Repository pattern for conversation persistence in PostgreSQL.
    Handles CRUD operations for conversations and messages.
    """

    def create_conversation(
            self,
            conversation_id: str,
            title: Optional[str] = None,
            metadata: Optional[Dict] = None
    ) -> Dict:
        """Create a new conversation in PostgreSQL."""
        with get_db_session() as db:
            conversation = Conversation(
                id=conversation_id,
                title=title or "New Conversation",
                meta_data=metadata or {}  # ← Gán vào 'meta_data'
            )
            db.add(conversation)
            db.flush()

            logger.info(f"[REPO] ✓ Created conversation: {conversation_id}")
            return conversation.to_dict()

    def get_or_create_conversation(
            self,
            conversation_id: str,
            title: Optional[str] = None,
            metadata: Optional[Dict] = None
    ) -> Dict:
        """Get existing conversation or create if not exists."""
        with get_db_session() as db:
            conversation = db.query(Conversation).filter(
                Conversation.id == conversation_id
            ).first()

            if conversation:
                logger.info(f"[REPO] Found existing conversation: {conversation_id}")
                return conversation.to_dict()

            # Create new conversation
            conversation = Conversation(
                id=conversation_id,
                title=title or "New Conversation",
                meta_data=metadata or {}  # ← Gán vào 'meta_data'
            )
            db.add(conversation)
            db.flush()

            logger.info(f"[REPO] ✓ Created conversation: {conversation_id}")
            return conversation.to_dict()

    def save_message(
            self,
            conversation_id: str,
            role: str,
            content: str,
            sources: Optional[List[Dict]] = None,
            metadata: Optional[Dict] = None
    ) -> Dict:
        """Save a single message to PostgreSQL."""
        with get_db_session() as db:
            # Ensure conversation exists
            conversation = db.query(Conversation).filter(
                Conversation.id == conversation_id
            ).first()

            if not conversation:
                # Auto-create conversation if not exists
                conversation = Conversation(
                    id=conversation_id,
                    title=content[:100] + ("..." if len(content) > 100 else "")
                )
                db.add(conversation)
                logger.info(f"[REPO] Auto-created conversation: {conversation_id}")

            # Create message
            message = Message(
                conversation_id=conversation_id,
                role=role,
                content=content,
                sources=sources or [],
                meta_data=metadata or {}  # ← Gán vào 'meta_data'
            )
            db.add(message)

            # Update conversation timestamp
            conversation.updated_at = datetime.utcnow()

            db.flush()

            logger.info(f"[REPO] ✓ Saved message ({role}) to conversation: {conversation_id}")
            return message.to_dict()

    def save_turn(
            self,
            conversation_id: str,
            user_query: str,
            assistant_answer: str,
            sources: Optional[List[Dict]] = None
    ):
        """
        Save a complete conversation turn (user + assistant messages).

        Args:
            conversation_id: UUID of conversation
            user_query: User's message
            assistant_answer: AI's response
            sources: RAG sources (optional)
        """
        with get_db_session() as db:
            # Ensure conversation exists
            conversation = db.query(Conversation).filter(
                Conversation.id == conversation_id
            ).first()

            if not conversation:
                conversation = Conversation(
                    id=conversation_id,
                    title=user_query[:100] + ("..." if len(user_query) > 100 else "")
                )
                db.add(conversation)
                logger.info(f"[REPO] Auto-created conversation: {conversation_id}")

            # Save user message
            user_message = Message(
                conversation_id=conversation_id,
                role="user",
                content=user_query,
                sources=[]
            )
            db.add(user_message)

            # Save assistant message
            assistant_message = Message(
                conversation_id=conversation_id,
                role="assistant",
                content=assistant_answer,
                sources=sources or []
            )
            db.add(assistant_message)

            # Update conversation
            conversation.updated_at = datetime.utcnow()
            if conversation.title == "New Conversation":
                conversation.title = user_query[:100] + ("..." if len(user_query) > 100 else "")

            db.flush()

            logger.info(f"[REPO] ✓ Saved turn to conversation: {conversation_id}")


# Singleton instance
conversation_repo = ConversationRepository()
