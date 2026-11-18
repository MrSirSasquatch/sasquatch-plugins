---
name: devcraft-review
description: Perform a code review using small specialist subagents focused on devcraft principles
---

# Devcraft Review

A code review focused on devcraft principles.

## Procedure

### 1. Determine the scope

If the user hasn't provided a review scope, pick the first applicable scope:

- Uncommitted changes in the working directory
- Changes in the current branch, not yet merged into the main branch where there is no PR
- Changes in an open pull request for the current branch

Where the user specifies the scope explicitly, use that scope. Record the baseline and target, enumerate the changed files, and identify generated files or other proposed exclusions before dispatch. Keep findings limited to the chosen changes; reviewers may inspect supporting context as needed.

### 2. Dispatch to specialists

Dispatch at least one of each specialist below. Read [agent runtime guidance](references/agent-runtime.md) before dispatching, and use the [specialist brief and result contract](references/agent-briefs.md). Supply the scope, applicable repository rules, accessible craftsmanship references, and any relevant PR context. The agent definition supplies specialty guidance; the brief supplies the concrete assignment.

| Specialist | Owns | Named agent |
| --- | --- | --- |
| Architecture | System boundaries, dependency direction, placement, wider consistency | `devcraft-architecture` |
| Behaviour | Acceptance criteria, regressions, edge cases, verification quality | `devcraft-behaviour` |
| Classes | Cohesive responsibilities, encapsulation, invariants, public interfaces, data clumps, primitive obsession | `devcraft-classes` |
| Comments | Reasoning, contracts, accurate comments, required API documentation | `devcraft-comments` |
| Exceptions | Failure propagation, recovery boundaries, swallowed failures | `devcraft-exceptions` |
| Functions | Coherent operations, abstraction levels, decomposition, signatures | `devcraft-functions` |
| Naming | Names of locals, parameters, members, types, namespaces, and artifacts, including embedded code | `devcraft-naming` |



### 3. Review the review

After all specialist reviews are complete. Consolidate and output the findings. 

As the review coordinator you may remove deplicates or consolidate overlapping findings, reprioritise findings in either direction and dismiss irrelevant or resolved findings.

Output a report in the following tabular format. Order items but criticality and then by category.

| Criticality | Category | Finding | Smallest possible fix |
| --- | --- | --- | --- |

## Delegation and cost

Unless the user specifies otherwise, prefer a supported lightweight model such as the latest version of Luna or Haiku for specialist agents, using the runtime guidance for actual model and effort controls. Keep assignments bounded; reduce each assignment's size when the diff is too large for reliable coverage.

As coordinator, manage assignments, coverage, and consolidation; do not perform the specialist reviews yourself. Keep your context focused on review evidence and coverage rather than loading the entire codebase.
