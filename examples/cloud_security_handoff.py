from agent_handoff.models import (
    A2AHandoff,
    HandoffContext,
    HandoffEnvironment,
    HandoffIntent,
    HandoffKnowledge,
    HandoffTask,
)


handoff = A2AHandoff(
    id="handoff-001",
    source_agent="cloud-architect-agent",
    target_agent="security-agent",
    workflow_id="workflow-001",
    run_id="run-001",
    intent=HandoffIntent(
        type="security_validation",
        summary="Validate k8smicro deployment security posture",
    ),
    task=HandoffTask(
        id="task-001",
        title="Validate security hardening",
        objective="Ensure the OVH/Kimsufi node is hardened before deployment",
        expected_output={
            "security_status": "pass|fail",
        },
    ),
    context=HandoffContext(
        memory_refs=["memory://deployment-plan"],
        trace_refs=["trace://bootstrap-run"],
        artifacts=["artifact://k3s-manifest"],
        payload={
            "provider": "ovh",
        },
    ),
    environment=HandoffEnvironment(
        environment_id="prod-eu-1",
        runtime_profile="k8smicro",
        target={
            "host": "kimsufi-node-01",
        },
    ),
    knowledge=HandoffKnowledge(
        knowledge_refs=["kb://security/k3s-hardening"],
        rag_query="k3s production hardening checklist",
    ),
)

print(handoff.model_dump_json(indent=2))
