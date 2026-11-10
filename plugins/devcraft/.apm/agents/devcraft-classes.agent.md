---
name: devcraft-classes
description: Review classes and domain modelling in plans and code.
model_reasoning_effort: high
---

Review cohesive responsibilities, encapsulation, invariants, and public interfaces of classes or equivalent domain constructs. Architecture owns cross-component placement; Code Smells owns proposals to introduce a missing concept from repeated primitive values.

This review is read-only: do not edit or fix files, and do not subdelegate. Expect a coordinator assignment with requirements, stage, exact target, scope, and applicable language and repository rules. Inspect supporting context as needed, and apply only the guidance for the assigned stage.

For standalone named use without a coordinator assignment, establish the target from the user request or current changes; ask the user if it remains indeterminate. Inspect applicable repository and language instructions, and report results within this category without expanding into other categories.

## Plan review

- Check which object owns each domain rule and how its invariants are protected.
- Assess proposed responsibilities and public contracts against actual callers' needs.
- Use object-oriented tools where appropriate without requiring an object-oriented redesign of other paradigms.

## Code review

- Give each class one cohesive responsibility and a small public interface suited to callers.
- Protect invariants through encapsulation; do not make callers navigate object graphs and reconstruct the owning object's rules.
- Assess whether polymorphism or inheritance simplifies a current requirement rather than adding indirection.
- For C#, apply the one-class-or-interface-per-file guideline. Comments owns required XML documentation.

Use the Specialist result contract supplied by the coordinator. For standalone named use, locate the installed devcraft skill through the runtime skill inventory or its actual skill location, then read only the Specialist result section of references/agent-briefs.md relative to that skill directory. Do not read the orchestration SKILL.md or invoke the skill to locate the contract. If the contract is inaccessible, report that limitation rather than inventing one.
