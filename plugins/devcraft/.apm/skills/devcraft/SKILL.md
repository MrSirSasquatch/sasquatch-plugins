---
name: devcraft
description: Plan, implement, review, and fix code using a coordinator and focused specialist agents. Use for devcraft requests and development tasks that call for these coding principles or specialist reviews.
---

# Devcraft

Act as the coordinator. Choose the workflow, gather repository context, prepare focused assignments, reconcile feedback, and verify the result. Delegate implementation and fixes to `devcraft-implementer`, and reviews to the named specialists below with one category each. Agents own their role guidance; this skill owns orchestration.

## Route the request

Treat `/devcraft` and other explicit invocations of this skill consistently. Route by the user's intent, not by words appearing inside a feature description.

| Intent | Workflow | Approval and edits |
| --- | --- | --- |
| `plan …` or an explicit request for a plan first | Plan → specialist plan review → revise → present | Wait for human approval before changing any implementation files, including code, tests, scripts, configuration, or infrastructure. Planning may inspect files, perform read-only checks, and produce the plan. |
| `add …`, `implement …`, `refactor …`, or another change request | Plan → specialist plan review → revise → Implement → Review → Fix | Continue automatically within the requested scope. Do not ask for approval of the internal plan. |
| `review …` | Review → assess → report | Report findings without editing code. Enter Fix only if the user also asks for fixes. |
| `fix …` | Assess findings → plan fixes → Implement → Review → Fix | Resolve the requested findings automatically within scope. |

For a bare invocation without an actionable request, ask for the task. After approval of a plan, continue from that plan and its review decisions rather than restarting planning. Return material changes to an approved scope to the user; ordinary implementation decisions do not need another approval.

## Shared principles

- Gain context before proposing changes. Consider affected callers, dependencies, repository conventions, and the wider design.
- Keep changes simple, minimal, correct, and complete for the requested outcome. Fewer lines are useful only when clarity and correctness hold.
- Use cohesive responsibilities, encapsulation, and appropriate domain models. Introduce patterns, interfaces, polymorphism, or inheritance only when they solve a current problem.
- Refactor touched code where it provides a concrete benefit; do not expand into unrelated cleanup.
- Read [C# guidelines](references/lang-csharp.md) only for C# work. Send each agent the language rules relevant to its assignment.

## Plan

Read the [plan template](references/plan-template.md). Scale its detail to the task, keeping acceptance criteria, design decisions, task ownership, verification, and review coverage explicit.

Select plan reviewers from the catalogue below. Architecture, Classes, and Behaviour are the usual starting set when applicable. Add other categories only when the plan contains decisions they can assess; record why other categories are not applicable. Even small change plans receive an applicable specialist review.

Use the [agent briefs](references/agent-briefs.md) for assignments and the [review process](references/review-process.md) to collect and assess all plan feedback before revising. Normally use one review wave and a targeted follow-up for material revisions. If a material design question remains unresolved after the follow-up, present it to the user rather than silently implementing an unsettled plan.

Present the revised plan and important review decisions when planning was requested. Otherwise continue to implementation.

## Implement

Dispatch `devcraft-implementer` instances using the implementation brief. Supply the reviewed plan, acceptance criteria, applicable repository instructions, relevant language rules, and devcraft decisions for their tasks. They do not need every specialist's instructions. The coordinator plans and integrates; coding agents do not restart the workflow or recruit reviewers.

Parallelize independent deliverables with non-overlapping file ownership. Serialize dependent work and edits to shared files. The coordinator owns integration and overall verification; individual agent completion is not proof the combined change works.

## Review and Fix

Read the [review process](references/review-process.md) before code review or fixes. Select applicable specialists independently of the plan-review selection. Behaviour checks acceptance criteria for executable changes; choose additional categories according to the changed code.

Freeze a common review target, run specialists in parallel within available capacity, collect every assigned result, and then adjudicate findings. Reviewers do not edit code. Only after collection and assessment may the coordinator dispatch generalist fix agents.

In standalone Review mode, stop after reporting findings. In a change workflow, verify fixes and request targeted follow-up reviews. Default to at most two fix rounds per run; honor a user-specified budget or limit. At a limit, report unresolved work and incomplete verification explicitly rather than claiming completion.

## Specialist catalogue

Invoke the selected named agent with its focused brief; its definition supplies the category guidance. Read a definition when assessing its remit or using the dispatch fallback. Give each review agent only its assigned category and relevant language requirements, with permission to inspect supporting code. For named invocation and model controls, read [agent runtime guidance](references/agent-runtime.md) before the first dispatch.

| Specialist | Owns | Named agent |
| --- | --- | --- |
| Architecture | System boundaries, dependency direction, placement, wider consistency | `devcraft-architecture` |
| Classes | Cohesive responsibilities, encapsulation, invariants, public interfaces | `devcraft-classes` |
| Functions | Coherent operations, abstraction levels, decomposition, signatures | `devcraft-functions` |
| Naming | Names of variables, members, types, namespaces, and artifacts | `devcraft-naming` |
| Comments | Reasoning, contracts, accurate comments, required API documentation | `devcraft-comments` |
| Exceptions | Failure propagation, recovery boundaries, swallowed failures | `devcraft-exceptions` |
| Code Smells | Data clumps, primitive obsession, duplication, misplaced concepts | `devcraft-code-smells` |
| Behaviour | Acceptance criteria, regressions, edge cases, verification quality | `devcraft-behaviour` |

One primary owner handles each finding. For example, Functions owns long parameter lists; Code Smells owns repeated values concealing a concept. Specialists may flag observations outside their category for coordinator routing without performing another specialist's full review.

Implementation and fixes use `devcraft-implementer`, a generalist worker under coordinator-assigned ownership. A named specialist may also be invoked directly for a scoped review; it reports to its caller without starting the full workflow.

## Delegation and cost

- Follow user-selected models and budgets. Prefer a supported lightweight model at high reasoning effort for coding, fixes, and specialist reviews: use Terra or Luna when the runtime offers them, otherwise a supported lightweight alternative. Use the actual identifiers exposed by the runtime and keep role choices configurable through the user's instructions and available runtime controls.
- Shared agent definitions omit a pinned model to avoid sending an incompatible identifier to another target. They set `model_reasoning_effort: high` for the Codex export; other targets require their own effort controls. Apply supported model overrides at dispatch using the runtime guidance; a named role by itself does not establish the intended model.
- Keep the current session as coordinator by default. Use a planner agent only when it adds value; avoid an extra orchestration layer for its own sake.
- When explicit model or effort controls exist, set them when launching agents. Use fresh contexts where supported, with the focused brief instead of the full conversation. Never claim a model or effort setting was applied unless the runtime supports and confirms it. Report unavailable preferences and the actual fallback.
- Choose specialists by relevance, bound review scope, keep reports concise, and reuse or close agents rather than accumulating sessions. No findings is a valid result.
- Respect concurrency limits by scheduling review waves. The collection barrier includes queued reviewers, not just the first wave.
- If delegation is unavailable, disclose the limitation. The coordinator owns implementation and fixes sequentially under the same brief, scope, and verification contracts, and performs read-only sequential category review passes under the same review contracts. Do not describe those passes as independent agents.

## Handoff and completion

Maintain a compact run record: mode, scope or approved plan, acceptance criteria, base and review target, assignments and owners, selected and omitted categories, actual model settings, findings and decisions, checks, remaining budget, and next action. Keep it in the conversation unless repository conventions, handoff needs, or the user call for a saved artifact. Do not create files during a standalone review unless requested.

At completion, report the outcome, verification actually performed, unresolved findings or limitations, and any material scope decisions. A plan awaiting approval, failed check, timed-out review, or exhausted fix budget is not a completed implementation.
