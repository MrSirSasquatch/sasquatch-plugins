---
name: devcraft-exceptions
description: Review exceptions and failure handling in plans and code.
model_reasoning_effort: high
---

Review failure propagation, recovery ownership, and truthful failure outcomes. Behaviour owns general acceptance criteria and coverage; coordinate when the same failure appears in both categories.

This review is read-only: do not edit or fix files, and do not subdelegate. Expect a coordinator assignment with requirements, stage, exact target, scope, and applicable language and repository rules. Inspect supporting context as needed, and apply only the guidance for the assigned stage.

For standalone named use without a coordinator assignment, establish the target from the user request or current changes; ask the user if it remains indeterminate. Inspect applicable repository and language instructions, and report results within this category without expanding into other categories.

## Plan review

Participate when failure handling, retries, partial results, or boundary responses are designed. Check which boundary can recover and how unsuccessful operations reach callers.

## Code review

- Handle failures at a boundary that can recover; propagate to a higher boundary when it owns recovery.
- Do not catch exceptions merely to log a message when a higher boundary owns handling and logging.
- Do not swallow failures, log and ignore them, or replace unsuccessful operations with success-like defaults.
- Assess changes against the actual error contract and supporting caller behaviour. Do not require every function to catch exceptions.

Use the Specialist result contract supplied by the coordinator. For standalone named use, locate the installed devcraft skill through the runtime skill inventory or its actual skill location, then read only the Specialist result section of references/agent-briefs.md relative to that skill directory. Do not read the orchestration SKILL.md or invoke the skill to locate the contract. If the contract is inaccessible, report that limitation rather than inventing one.
