# Kiro Multi-Agent Engineering System Architecture

## Overview

This repository defines a **multi-agent engineering system** designed to run inside **Kiro CLI**.

The system consists of a **coordinator agent** that orchestrates multiple specialized engineering agents.

The coordinator analyzes user requests, decomposes them into tasks, assigns tasks to specialized agents, and manages workflow execution.

This architecture enables complex engineering workflows such as:

* feature implementation
* debugging
* testing
* architecture analysis
* documentation generation

The system is designed to behave like a **structured engineering team coordinated by a technical lead**.

---

# System Components

The system is composed of five primary layers:

1. Agents
2. Schemas
3. Policies
4. Prompts
5. MCP Tooling

Each layer serves a distinct purpose.

---

# Agent Layer

Agents represent specialized engineering roles.

## Coordinator Agent

The **coordinator agent** orchestrates the entire workflow.

Responsibilities:

* analyze user requests
* create execution plans
* validate plans
* generate structured task context
* delegate tasks
* aggregate results
* perform failure recovery
* update workflow state

The coordinator behaves like a **technical lead managing an engineering team**.

---

## Worker Agents

Worker agents perform specialized tasks.

Current agents:

agent_code
agent_test
agent_debug
agent_review
agent_architecture
agent_document

Each agent is self-contained and defined in:

```
agents/<agent_name>/
```

Each agent directory contains:

prompt.md
capabilities.yaml
tools.yaml

---

# Workflow Execution Model

The system executes workflows using a structured lifecycle.

Workflow pipeline:

User Request
↓
Coordinator analyzes request
↓
Coordinator generates execution plan
↓
Plan validated via self-validation layer
↓
Task contexts generated
↓
Tasks delegated to specialized agents
↓
Agents execute tasks using tools
↓
Agents return structured results
↓
Coordinator updates workflow state
↓
Coordinator determines next task
↓
Workflow continues until completion

---

# Execution Plan

Execution plans define the tasks required to complete a request.

Each plan contains:

Task ID
Assigned Agent
Task Description
Dependencies

Plans are defined using:

```
schemas/execution_plan_schema.json
```

Execution plans should remain **minimal and focused**.

Typical plans contain 1–4 tasks.

---

# Task Context

Each agent receives tasks in a structured format.

Task context includes:

* task identifier
* assigned agent
* objective
* detailed description
* relevant context
* constraints
* allowed tools
* success criteria

Defined in:

```
schemas/task_context_template.md
```

---

# Agent Execution Contract

All worker agents must return results using a structured contract.

Agent responses include:

* task summary
* execution steps
* results
* artifacts
* observations
* completion status

Defined in:

```
schemas/agent_task_execution_contract.md
```

This ensures that the coordinator can reliably interpret agent outputs.

---

# Workflow State Tracking

The coordinator tracks workflow execution state.

Workflow state includes:

* completed tasks
* pending tasks
* failed tasks
* retry counts
* current task

Defined in:

```
schemas/workflow_state_schema.json
```

This allows the coordinator to function as a **workflow engine rather than a simple planner**.

---

# Failure Recovery

Failures are expected in real engineering workflows.

The coordinator follows a structured recovery process when failures occur.

Possible recovery strategies include:

* debugging the failure
* reassigning tasks
* revising implementation
* architecture analysis
* replanning workflow

Defined in:

```
policies/failure_recovery_and_replanning.md
```

---

# Policies

Policies define operational rules governing the system.

Policies enforce discipline in areas such as:

* task delegation
* tool usage
* task decomposition
* context management
* failure recovery

Policy files:

```
policies/
delegation.md
tool_usage.md
task_splitting.md
context_limits.md
failure_recovery_and_replanning.md
```

Policies ensure consistent system behavior.

---

# Planning Heuristics

Planning heuristics guide the coordinator when creating execution plans.

Heuristics help the coordinator:

* avoid unnecessary tasks
* choose correct agents
* maintain logical task ordering
* minimize workflow complexity

Defined in:

```
prompts/task_planning_heuristics.md
```

---

# Self-Validation Layer

Before executing any plan, the coordinator performs a validation step.

The validation process checks:

* correct agent assignments
* task necessity
* logical ordering
* domain coverage
* plan simplicity

Defined in:

```
prompts/coordinator_self_validation.md
```

Only validated plans are executed.

---

# Tooling (MCP Servers)

Agents interact with external systems using MCP tools.

Examples include:

filesystem
repo_search
context7
terminal
git
sequential_thinking

Tool access is restricted per agent and defined in:

```
agents/<agent>/tools.yaml
```

The coordinator agent has minimal tool access to maintain focus on orchestration.

---

# Context Management

To maintain efficient reasoning:

* agents receive only relevant context
* large datasets are avoided
* unnecessary repository exploration is discouraged

Context constraints are defined in:

```
policies/context_limits.md
```

---

# Design Principles

The system follows several architectural principles.

### Clear Role Separation

Coordinator handles orchestration.
Worker agents perform execution.

---

### Minimal Task Decomposition

Tasks are only split when expertise domains differ.

---

### Structured Agent Communication

All agent inputs and outputs follow defined schemas.

---

### Failure-Resilient Workflows

Failures trigger recovery strategies instead of terminating workflows.

---

### Controlled Tool Usage

Tools are used selectively to avoid unnecessary context expansion.

---

# Directory Structure

```
kiro-agents
│
├── agents/
│
├── schemas/
│
├── policies/
│
├── prompts/
│
├── mcp/
│
└── ARCHITECTURE.md
```

Each directory represents a distinct layer of the system.

---

# Future Extensions

The architecture supports future enhancements such as:

* additional specialized agents
* dynamic agent discovery
* workflow parallelization
* memory and knowledge storage
* advanced debugging agents
* deployment automation agents

The modular structure allows the system to scale as the engineering team grows.

---

# Summary

This system transforms Kiro CLI into a **structured multi-agent engineering team**.

The coordinator behaves as a technical lead coordinating specialized engineers while maintaining disciplined workflows, structured communication, and failure recovery mechanisms.

The architecture emphasizes:

* clarity
* modularity
* reliability
* scalability
