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
    summary: str


class HandoffTask(BaseModel):
    id: str
    title: str
    objective: str
    expected_output: dict[str, Any]
    constraints: list[str] = Field(default_factory=list)


class HandoffContext(BaseModel):
    memory_refs: list[str]
    trace_refs: list[str]
    artifacts: list[str]
    payload: dict[str, Any]


class HandoffEnvironment(BaseModel):
    environment_id: str
    runtime_profile: str
    target: dict[str, Any]
    variables: dict[str, Any] = Field(default_factory=dict)


class HandoffKnowledge(BaseModel):
    knowledge_refs: list[str]
    rag_query: str | None = None
    facts: dict[str, Any] = Field(default_factory=dict)


class HandoffCapabilities(BaseModel):
    required_skills: list[str]
    required_tools: list[str]
    missing_skills: list[str] = Field(default_factory=list)
    missing_tools: list[str] = Field(default_factory=list)


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
    task: HandoffTask
    context: HandoffContext
    environment: HandoffEnvironment
    knowledge: HandoffKnowledge
    capabilities: HandoffCapabilities
    permissions: HandoffPermissions = Field(default_factory=HandoffPermissions)
    mode: HandoffMode = HandoffMode.DELEGATE
    status: HandoffStatus = HandoffStatus.REQUESTED
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    result: dict[str, Any] | None = None
    error: str | None = None
