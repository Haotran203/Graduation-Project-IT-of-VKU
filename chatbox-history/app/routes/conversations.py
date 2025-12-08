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
