# Agent-Handoff

Agent-Handoff owns A2A agent-to-agent handoff protocols for AGenNext.

## Decision

A2A handoff belongs in `Agent-Handoff`.

This repo defines how one agent delegates, transfers, escalates, or hands context to another agent.

## Scope

Agent-Handoff owns:

- A2A handoff contracts
- delegation envelopes
- context transfer models
- ownership transfer semantics
- escalation rules
- handoff acceptance/rejection
- handoff trace events
- handoff retry policies
- handoff authorization requirements

Agent-Handoff does not own:

- runtime execution
- graph execution
- identity verification
- memory storage
- agent team composition
- UI

## Boundary

| Component | Responsibility |
|---|---|
| Agent-Handoff | A2A handoff and delegation contracts |
| Agent-Team | Defines composed agent teams |
| Agent-Runtime | Executes workflows and invokes handoffs |
| Agent-Identity | Verifies agent identities and trust |
| Agent-IGA | Governs access/entitlements for handoff actions |
| Agent-Traces | Records handoff timeline events |
| Agent-Memory | Stores durable handoff context if needed |

## Cloud agent example

```txt
Cloud Architect Agent
  ↓ hands off security validation to
Security Agent
  ↓ hands result back to
Cloud Architect Agent
  ↓ hands deployment to
Deploy Agent
```

## A2A flow

```txt
source_agent prepares handoff envelope
  ↓
Agent-Identity verifies source/target agent identities
  ↓
Agent-IGA checks delegation permission
  ↓
target_agent accepts or rejects handoff
  ↓
Agent-Traces records handoff event
  ↓
Agent-Runtime continues workflow
```
