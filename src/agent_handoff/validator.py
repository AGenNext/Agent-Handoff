from agent_handoff.models import A2AHandoff


class HandoffValidationError(ValueError):
    pass


class HandoffValidator:
    REQUIRED_SECTIONS = ("task", "context", "environment", "knowledge")

    @classmethod
    def validate_complete(cls, handoff: A2AHandoff) -> None:
        missing = []

        for section in cls.REQUIRED_SECTIONS:
            if getattr(handoff, section, None) is None:
                missing.append(section)

        if missing:
            raise HandoffValidationError(
                f"Incomplete A2A handoff. Missing required sections: {', '.join(missing)}"
            )

        if not handoff.task.objective:
            raise HandoffValidationError("A2A handoff task.objective is required")

        if not handoff.task.expected_output:
            raise HandoffValidationError("A2A handoff task.expected_output is required")

        if not handoff.context.memory_refs and not handoff.context.payload:
            raise HandoffValidationError(
                "A2A handoff must include context.memory_refs or context.payload"
            )

        if not handoff.environment.runtime_profile:
            raise HandoffValidationError("A2A handoff environment.runtime_profile is required")

        if not handoff.environment.target:
            raise HandoffValidationError("A2A handoff environment.target is required")

        if not handoff.knowledge.knowledge_refs and not handoff.knowledge.rag_query:
            raise HandoffValidationError(
                "A2A handoff must include knowledge.knowledge_refs or knowledge.rag_query"
            )
