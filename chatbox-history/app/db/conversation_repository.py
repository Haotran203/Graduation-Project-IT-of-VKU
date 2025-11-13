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

    def get_conversation(self, conversation_id: str) -> Optional[Dict]:
        """
        Get conversation by ID.

        Args:
            conversation_id: UUID of conversation

        Returns:
            Conversation dict or None
        """
        with get_db_session() as db:
            conversation = db.query(Conversation).filter(
                Conversation.id == conversation_id
            ).first()

            if conversation:
                return conversation.to_dict()

            return None

    def get_messages(
            self,
            conversation_id: str,
            limit: Optional[int] = None,
            offset: int = 0
    ) -> List[Dict]:
        """
        Get messages for a conversation.

        Args:
            conversation_id: UUID of conversation
            limit: Maximum number of messages (optional)
            offset: Pagination offset

        Returns:
            List of message dicts (oldest first)
        """
        with get_db_session() as db:
            query = db.query(Message).filter(
                Message.conversation_id == conversation_id
            ).order_by(Message.created_at.asc())

            if offset:
                query = query.offset(offset)

            if limit:
                query = query.limit(limit)

            messages = query.all()

            logger.info(f"[REPO] Retrieved {len(messages)} messages for: {conversation_id}")
            return [msg.to_dict() for msg in messages]

    def get_recent_messages(
            self,
            conversation_id: str,
            limit: int = 10
    ) -> List[Dict]:
        """
        Get recent messages (last N messages).

        Args:
            conversation_id: UUID of conversation
            limit: Number of recent messages

        Returns:
            List of message dicts (oldest first)
        """
        with get_db_session() as db:
            # Get total count
            total_count = db.query(func.count(Message.id)).filter(
                Message.conversation_id == conversation_id
            ).scalar()

            # Calculate offset to get last N messages
            offset = max(0, total_count - limit)

            messages = db.query(Message).filter(
                Message.conversation_id == conversation_id
            ).order_by(Message.created_at.asc()).offset(offset).limit(limit).all()

            return [msg.to_dict() for msg in messages]

    def list_conversations(
            self,
            limit: int = 50,
            offset: int = 0,
            order_by: str = "updated_at"
    ) -> List[Dict]:
        """
        List all conversations.

        Args:
            limit: Maximum number of conversations
            offset: Pagination offset
            order_by: Sort field ('updated_at' or 'created_at')

        Returns:
            List of conversation dicts with preview
        """
        with get_db_session() as db:
            # Query conversations
            order_column = Conversation.updated_at if order_by == "updated_at" else Conversation.created_at
            conversations = db.query(Conversation).order_by(
                desc(order_column)
            ).limit(limit).offset(offset).all()

            # Build result with preview
            result = []
            for conv in conversations:
                conv_dict = conv.to_dict()

                # Get first user message as preview
                first_message = db.query(Message).filter(
                    Message.conversation_id == conv.id,
                    Message.role == "user"
                ).order_by(Message.created_at.asc()).first()

                if first_message:
                    preview = first_message.content[:100]
                    conv_dict["preview"] = preview + ("..." if len(first_message.content) > 100 else "")
                else:
                    conv_dict["preview"] = ""

                result.append(conv_dict)

            logger.info(f"[REPO] Listed {len(result)} conversations")
            return result

    def update_conversation(
            self,
            conversation_id: str,
            title: Optional[str] = None,
            metadata: Optional[Dict] = None
    ) -> bool:
        """Update conversation metadata."""
        with get_db_session() as db:
            conversation = db.query(Conversation).filter(
                Conversation.id == conversation_id
            ).first()

            if not conversation:
                return False

            if title is not None:
                conversation.title = title

            if metadata is not None:
                conversation.meta_data = metadata  # ← Gán vào 'meta_data'

            conversation.updated_at = datetime.utcnow()

            db.flush()

            logger.info(f"[REPO] ✓ Updated conversation: {conversation_id}")
            return True

    def delete_conversation(self, conversation_id: str) -> bool:
        """
        Delete conversation and all messages (cascade).

        Args:
            conversation_id: UUID of conversation

        Returns:
            True if deleted, False if not found
        """
        with get_db_session() as db:
            conversation = db.query(Conversation).filter(
                Conversation.id == conversation_id
            ).first()

            if not conversation:
                return False

            db.delete(conversation)
            db.flush()

            logger.info(f"[REPO] ✓ Deleted conversation: {conversation_id}")
            return True

    def delete_messages(self, conversation_id: str) -> int:
        """
        Delete all messages in a conversation (keep conversation).

        Args:
            conversation_id: UUID of conversation

        Returns:
            Number of messages deleted
        """
        with get_db_session() as db:
            count = db.query(Message).filter(
                Message.conversation_id == conversation_id
            ).delete()

            db.flush()

            logger.info(f"[REPO] ✓ Deleted {count} messages from: {conversation_id}")
            return count

    def search_conversations(
            self,
            query: str,
            limit: int = 20
    ) -> List[Dict]:
        """
        Search conversations by title or message content.

        Args:
            query: Search text
            limit: Maximum results

        Returns:
            List of matching conversations
        """
        with get_db_session() as db:
            conversations = db.query(Conversation).join(Message).filter(
                or_(
                    Conversation.title.ilike(f"%{query}%"),
                    Message.content.ilike(f"%{query}%")
                )
            ).group_by(Conversation.id).order_by(
                desc(Conversation.updated_at)
            ).limit(limit).all()

            result = [conv.to_dict() for conv in conversations]

            logger.info(f"[REPO] Search '{query}' found {len(result)} results")
            return result

    def get_conversation_count(self) -> int:
        """
        Get total number of conversations.

        Returns:
            Total count
        """
        with get_db_session() as db:
            count = db.query(func.count(Conversation.id)).scalar()
            return count or 0

    def get_message_count(self, conversation_id: str) -> int:
        """
        Get number of messages in a conversation.

        Args:
            conversation_id: UUID of conversation

        Returns:
            Message count
        """
        with get_db_session() as db:
            count = db.query(func.count(Message.id)).filter(
                Message.conversation_id == conversation_id
            ).scalar()
            return count or 0


# Singleton instance
conversation_repo = ConversationRepository()
