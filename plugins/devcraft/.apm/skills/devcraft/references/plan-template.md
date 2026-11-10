# Devcraft plan template

Use this structure for a new change plan. Keep small plans compact; expand sections only where decisions or coordination require detail. For fixes, adapt it around accepted findings rather than repeating completed discovery.

## Outcome and acceptance criteria

- State the requested outcome and observable completion criteria.
- Include failure behaviour and compatibility requirements relevant to the task.
- Identify assumptions and questions that materially affect the design.

## Current context

- Identify relevant existing code, callers, conventions, and repository instructions.
- Describe constraints that affect the solution, including existing behaviour to preserve.
- Distinguish inspected facts from assumptions.

## Proposed design

- Describe responsibilities, boundaries, contracts, and data or control flow.
- Explain important choices and tradeoffs, using existing patterns where appropriate.
- Resolve applicable devcraft concerns here: ownership of domain rules, invariants, function boundaries, naming of new public concepts, or failure recovery.
- Avoid abstractions justified only by hypothetical future work.

## Scope

- Identify intended changes and explicit exclusions.
- Note affected interfaces, migrations, configuration, or documentation when relevant.
- For a human-approved plan, identify changes that would require revisiting that approval.

## Implementation tasks

| Task | Deliverable and acceptance criteria | Files or ownership boundary | Dependencies | Parallel group |
| --- | --- | --- | --- | --- |
| Task identifier | Concrete result | One writer per shared file | Required earlier results | Independent tasks, or sequential |

Assign `devcraft-implementer` instances as task owners at dispatch time. Identify shared files and integration work before starting concurrent writers. Tasks should be implementable from their brief without rediscovering the whole plan.

## Devcraft considerations

- Record specific principles that affect this implementation and the decisions taken to satisfy them.
- Include relevant language requirements.
- Capture accepted plan-review feedback so coding agents receive the revised decision, not competing proposals.

## Verification

| Acceptance criterion or regression risk | Check or test | Expected result |
| --- | --- | --- |
| Observable requirement | Relevant automated check or explicit inspection | Evidence of completion |

Include integration checks beyond individual task checks where necessary. Record unavailable infrastructure and the resulting verification gap. Documentation-only tasks need content and structural checks rather than artificial behaviour tests.

## Review assignments and decisions

| Stage | Specialist and named agent | Scope and concrete question | Selection rationale |
| --- | --- | --- | --- |
| Plan or code | One category and catalogue agent name | Decisions or changes to assess | Why this reviewer is useful |

- State which other categories were omitted and why; categories without relevant evidence should not generate ceremonial reviews.
- Record plan findings as accepted, rejected, deferred, or duplicate, with reasons and resulting revisions.
- Record unresolved material questions and, for plan-first mode, that implementation awaits human approval.

After review, present a coherent revised plan. Include important decisions and unresolved issues without requiring the user to reconstruct agent transcripts.
