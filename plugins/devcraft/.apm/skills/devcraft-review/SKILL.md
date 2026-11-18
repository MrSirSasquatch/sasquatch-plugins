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

Unless instructed otherwise by the user, dispatch at least one of the following specialists as a subagent. Provide the agent with a prompt asking for a review of the scope of change they should look at and nothing else. It is important not to give the subagent any other context, as it may bias the review. 

For large changes, and with the exception of the codebase design specialist, reviews may be broken into multiple subagents for the same specialist type, each with a different subset of the changed files. The coordinator should ensure that all changed files are covered by at least one subagent.

| Specialist | Owns | Named agent |
| --- | --- | --- |
| Codebase Design | Code architecture, application layering, code cohesion, single responsibility | `devcraft-codebase-design` |
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

| Criticality | Category | Finding | Recommended Fix |
| --- | --- | --- | --- |

## Delegation and cost

Unless the user specifies otherwise, prefer a supported lightweight model such as the latest version of Luna or Haiku for specialist agents, using the runtime guidance for actual model and effort controls. Keep assignments bounded; reduce each assignment's size when the diff is too large for reliable coverage.

As coordinator, manage assignments, coverage, and consolidation; do not perform the specialist reviews yourself. Keep your context focused on review evidence and coverage rather than loading the entire codebase.
