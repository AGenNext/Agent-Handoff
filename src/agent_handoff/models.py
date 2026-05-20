from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field


class HandoffMode(StrEnum):
    DELEGATE = "delegate"
    TRANSFER = "transfer"
    ESCALATE = "escalate"


class HandoffStatus(StrEnum):
    REQUESTED = "requested"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    COMPLETED = "completed"
    FAILED = "failed"
    EXPIRED = "expired"


class HandoffIntent(BaseModel):
    type: str
    priority: str = "normal"
    summary: str | None = None


class HandoffContext(BaseModel):
    memory_refs: list[str] = Field(default_factory=list)
    trace_refs: list[str] = Field(default_factory=list)
    artifacts: list[str] = Field(default_factory=list)
    payload: dict[str, Any] = Field(default_factory=dict)


class HandoffPermissions(BaseModel):
    approval_required: bool = False
    required_roles: list[str] = Field(default_factory=list)


class A2AHandoff(BaseModel):
    id: str
    source_agent: str
    target_agent: str
    workflow_id: str
    run_id: str
    intent: HandoffIntent
    context: HandoffContext = Field(default_factory=HandoffContext)
    permissions: HandoffPermissions = Field(default_factory=HandoffPermissions)
    mode: HandoffMode = HandoffMode.DELEGATE
    status: HandoffStatus = HandoffStatus.REQUESTED
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    result: dict[str, Any] | None = None
    error: str | None = None
