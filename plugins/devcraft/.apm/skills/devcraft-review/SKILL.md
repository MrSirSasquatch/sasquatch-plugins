---
name: devcraft-review
description: Perform a code review using small specialist subagents focused on devcraft principles
---

# Devcraft Review

A code review focused on devcraft principles. 

## Procedure

### 1. Determine the scope

If the user hasn't provided a review scope, assume they want you to review changes in one of the following scopes. Pick the first one that applies, perform the review and make a note of the scope that you applied. 
 - Uncommitted changes in the working directory
 - Changes in the current branch, not yet merged into the main branch where there is no PR
 - Changes in an open pull request for the current branch

Where the user specifies the scope of the review explicitly, use that scope for the review.

Keep the scope of the review limited to only the changes within the determined scope. Reviews may read any supporting context as needed where the review dictates understanding of broader code and structure.


### 2. Dispatch to specialists

Dispatch at least one each of the following specialist review agents to gather and report findings within their area of speciality. Give each agent a brief that defines the scope of the review. You don't need to instruct the specialsts on how to do their reviews since they are already specialists in that area. Keep the agent brief focused and meaningful. For PR reviews, you may include context from the pull request such as the description to give context about the changes made.

| Specialist | Owns | Named agent |
| --- | --- | --- |
| Architecture | System boundaries, dependency direction, placement, wider consistency | `devcraft-architecture` |
| Behaviour | Acceptance criteria, regressions, edge cases, verification quality | `devcraft-behaviour` |
| Classes | Cohesive responsibilities, encapsulation, invariants, public interfaces, data clumps, primitive obsession | `devcraft-classes` |
| Comments | Reasoning, contracts, accurate comments, required API documentation | `devcraft-comments` |
| Exceptions | Failure propagation, recovery boundaries, swallowed failures | `devcraft-exceptions` |
| Functions | Coherent operations, abstraction levels, decomposition, signatures | `devcraft-functions` |
| Naming | Names of variables, members, types, namespaces, and artifacts | `devcraft-naming` |

### 3. Review the review

After all specialist reviews are complete. Consolidate and output the findings. 

As the review coordinator you may remove deplicates or consolidate overlapping findings, reprioritise findings in either direction and dismiss irrelevant or resolved findings.

Output a report in the following tabular format. Order items but criticality and then by category.

| Criticality | Category | Finding | Smallest possible fix |
| --- | --- | --- | --- |

## Delegation and cost

Dispatching many specialist agents can increase the thoroughness of the review but also incurs higher coordination and computational costs. Unless the user has specified otherwise, use a lightweight model such as GPT-6 Luna or Haiku for the specialist agents. Small models can perform will where they have limited scope and clear instructions.

For larger reviews like extensive codebases or complex feature additions, consider keeping lightweight models but dispatching additional agents to review limited sections of the codebase in parallel.

As the review coordinator, you coordinate a review and must never perform the review yourself. Your role is to manage the process, assign tasks, and consolidate findings from the specialist agents. Your context should be kept as clean as possible to avoid bias and ensure objective assessment of the review findings.