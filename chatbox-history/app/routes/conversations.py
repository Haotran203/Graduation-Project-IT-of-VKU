# app/api/routes/conversations.py

from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel, Field

from app.db.conversation_repository import conversation_repo

router = APIRouter()

# Pydantic Models

class ConversationCreate(BaseModel):
    conversation_id: str = Field(..., description="Conversation UUID from frontend")
    title: Optional[str] = Field(None, description="Conversation title")
    metadata: dict = Field(default_factory=dict, description="Additional metadata")


class ConversationUpdate(BaseModel):
    title: Optional[str] = Field(None, description="New title")
    metadata: Optional[dict] = Field(None, description="New metadata")


class MessageCreate(BaseModel):
    conversation_id: str = Field(..., description="Conversation UUID")
    role: str = Field(..., description="'user' or 'assistant'")
    content: str = Field(..., description="Message content")
    sources: List[dict] = Field(default_factory=list, description="RAG sources")


class MessageTurn(BaseModel):
    conversation_id: str = Field(..., description="Conversation UUID")
    user_query: str = Field(..., description="User's message")
    assistant_answer: str = Field(..., description="AI's response")
    sources: List[dict] = Field(default_factory=list, description="RAG sources")


# Endpoints
@router.post("/create", summary="Create new conversation")
def create_conversation(data: ConversationCreate):
    """
    Create a new conversation in PostgreSQL.
    Frontend generates conversation_id (UUID).
    """
    try:
        conversation = conversation_repo.get_or_create_conversation(
            conversation_id=data.conversation_id,
            title=data.title,
            metadata=data.metadata
        )
        return {
            "status": "success",
            "conversation": conversation
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create conversation: {str(e)}")


@router.get("/list", summary="List all conversations")
def list_conversations(
        limit: int = Query(50, ge=1, le=100, description="Max results"),
        offset: int = Query(0, ge=0, description="Pagination offset"),
        order_by: str = Query("updated_at", description="Sort by: updated_at or created_at")
):
    """
    Get list of all conversations from PostgreSQL.
    Sorted by most recent (updated_at DESC).
    """
    try:
        conversations = conversation_repo.list_conversations(
            limit=limit,
            offset=offset,
            order_by=order_by
        )

        total = conversation_repo.get_conversation_count()

        return {
            "status": "success",
            "conversations": conversations,
            "count": len(conversations),
            "total": total,
            "offset": offset,
            "limit": limit
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list conversations: {str(e)}")


@router.get("/{conversation_id}", summary="Get conversation details")
def get_conversation(conversation_id: str):
    """
    Get conversation metadata by ID.
    """
    try:
        conversation = conversation_repo.get_conversation(conversation_id)

        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")

        return {
            "status": "success",
            "conversation": conversation
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get conversation: {str(e)}")


@router.get("/{conversation_id}/messages", summary="Get conversation messages")
def get_messages(
        conversation_id: str,
        limit: Optional[int] = Query(None, ge=1, le=1000, description="Max messages"),
        offset: int = Query(0, ge=0, description="Pagination offset")
):
    """
    Get all messages in a conversation from PostgreSQL.
    Returns in chronological order (oldest first).
    """
    try:
        messages = conversation_repo.get_messages(
            conversation_id=conversation_id,
            limit=limit,
            offset=offset
        )

        total = conversation_repo.get_message_count(conversation_id)

        return {
            "status": "success",
            "messages": messages,
            "count": len(messages),
            "total": total
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get messages: {str(e)}")


@router.post("/message", summary="Save single message")
def save_message(data: MessageCreate):
    """
    Save a single message to PostgreSQL.
    Auto-creates conversation if not exists.
    """
    try:
        message = conversation_repo.save_message(
            conversation_id=data.conversation_id,
            role=data.role,
            content=data.content,
            sources=data.sources
        )

        return {
            "status": "success",
            "message": message
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save message: {str(e)}")


@router.post("/turn", summary="Save conversation turn")
def save_turn(data: MessageTurn):
    """
    Save a complete turn (user + assistant messages) to PostgreSQL.
    Auto-creates conversation if not exists.
    """
    try:
        conversation_repo.save_turn(
            conversation_id=data.conversation_id,
            user_query=data.user_query,
            assistant_answer=data.assistant_answer,
            sources=data.sources
        )

        return {
            "status": "success",
            "message": "Turn saved"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save turn: {str(e)}")


@router.patch("/{conversation_id}", summary="Update conversation")
def update_conversation(conversation_id: str, data: ConversationUpdate):
    """
    Update conversation title or metadata.
    """
    try:
        success = conversation_repo.update_conversation(
            conversation_id=conversation_id,
            title=data.title,
            metadata=data.metadata
        )

        if not success:
            raise HTTPException(status_code=404, detail="Conversation not found")

        return {
            "status": "success",
            "message": "Conversation updated"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update conversation: {str(e)}")


@router.delete("/{conversation_id}", summary="Delete conversation")
def delete_conversation(conversation_id: str):
    """
    Delete conversation and all messages (cascade delete).
    """
    try:
        success = conversation_repo.delete_conversation(conversation_id)

        if not success:
            raise HTTPException(status_code=404, detail="Conversation not found")

        return {
            "status": "success",
            "message": "Conversation deleted"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete conversation: {str(e)}")


@router.delete("/{conversation_id}/messages", summary="Clear messages")
def clear_messages(conversation_id: str):
    """
    Delete all messages in a conversation (keep conversation metadata).
    """
    try:
        count = conversation_repo.delete_messages(conversation_id)

        return {
            "status": "success",
            "message": f"Deleted {count} messages"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to clear messages: {str(e)}")


@router.get("/search", summary="Search conversations")
def search_conversations(
        q: str = Query(..., min_length=1, description="Search query"),
        limit: int = Query(20, ge=1, le=100, description="Max results")
):
    """
    Search conversations by title or message content.
    """
    try:
        results = conversation_repo.search_conversations(
            query=q,
            limit=limit
        )

        return {
            "status": "success",
            "results": results,
            "count": len(results),
            "query": q
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")
