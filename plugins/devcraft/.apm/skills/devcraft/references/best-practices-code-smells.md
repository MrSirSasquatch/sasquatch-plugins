# Code Smell Review Standards

Use this reference as guidance for both preventing code smells in your generated code as well as reviewing code where these smells should be avoided. 

## Review Decisions

- **Reject** when a smell contributes to a concrete correctness, reliability, or maintenance problem. Explain the consequence and require the smallest useful correction.
- **Flag** when the structure makes change or correct use meaningfully harder, but impact or remedy depends on context. Explain the concern and request clarification or a focused improvement.
- **Accept** when the structure is clear and cohesive in context, even if it resembles a named smell.

Treat size, repetition, and primitive types as investigation signals, not automatic violations. A review finding should identify the location, explain the risk, and suggest a proportionate improvement. Do not demand refactoring unrelated to the change, introduce abstractions for hypothetical reuse, or prescribe arbitrary line, field, or argument-count thresholds.

## Long Functions

A function should express one coherent operation at a consistent level of abstraction. Review whether its length hides meaningful decisions, distinct responsibilities, or important paths.

**Reject when:**

- The function's unrelated operations are coupled so a caller cannot use or change one safely without affecting another.
- Complex control flow or mixed responsibilities cause an observable defect, conceal an important failure path, or make a required behavior impractical to verify.
- Duplicated decision logic in the function can produce inconsistent results on paths affected by the change.

**Flag when:**

- Several independently meaningful steps, nested branches, or multiple abstraction levels make the main flow difficult to follow.
- A cohesive section lacks a useful name, or the function's inputs, outputs, and side effects are difficult to understand as one contract.
- The function combines orchestration with detailed work that could be isolated to clarify responsibility or enable focused testing.

Prefer extracting cohesive operations with meaningful names, simplifying control flow, or separating responsibilities. Do not split a straightforward sequence into tiny helpers merely to reduce line count; keep closely related steps together when extraction would obscure the behavior.

## Large Classes (God Classes)

A class should have a cohesive responsibility, protect the invariants it owns, and expose an interface suited to its callers. Judge its responsibilities and coupling, not its raw size.

**Reject when:**

- Unrelated responsibilities are entangled so that changing one can break another or callers must understand internal representation to use the class safely.
- One class coordinates or owns state in a way that creates a concrete correctness defect, hidden coupling, or a change that cannot be isolated safely.
- A responsibility split is necessary to correct a demonstrated invariant, lifecycle, or ownership problem.

**Flag when:**

- Groups of methods operate on largely separate subsets of fields or change for distinct reasons.
- The class accumulates broad dependencies, branching by unrelated concerns, or many public operations that make its contract difficult to understand.
- Callers repeatedly navigate its internals or duplicate rules that belong with a cohesive collaborator.

Consider extracting a responsibility or collaborator when it establishes a useful boundary and can own related behavior and state. Do not split a cohesive class just to reduce its field or method count, or create a service for every operation.

## Long Parameter Lists

Parameters should make an operation's required inputs clear and safe to provide. Review whether the call site communicates intent and whether the inputs represent a cohesive concept.

**Reject when:**

- The signature permits invalid combinations that the implementation mishandles.
- Similar or interchangeable positional parameters create a demonstrated risk of passing values in the wrong order or unit.
- Required information is hidden in ambient state or optional defaults, causing incorrect behavior for callers affected by the change.

**Flag when:**

- Calls require readers to remember the meaning or order of many arguments, especially repeated values of the same type.
- Several parameters always travel together or describe one domain concept, suggesting a cohesive value object or options type.
- A boolean or nullable parameter selects substantially different behavior, obscuring the operation's contract.

Prefer named arguments, a domain type, or separate operations when they make valid usage clearer. Keep independent, genuinely required inputs explicit; do not bundle unrelated values into a parameter bag just to shorten the signature.

## Data Clumps

Repeated groups of values may represent one concept with shared meaning, validation, or behavior. Confirm that the values belong together before recommending a new type.

**Reject when:**

- A duplicated group represents one domain rule or invariant, but independent handling lets affected paths accept inconsistent or invalid values.
- The group is repeatedly passed or stored in a way that causes a concrete misuse, synchronization defect, or inconsistent change.

**Flag when:**

- The same related values repeatedly appear together in function signatures, return values, or fields, and callers must keep them aligned.
- The values share validation, lifecycle, units, or behavior that is duplicated across the changed paths.
- A cohesive type would name the concept and make its valid state easier to represent.

Prefer introducing a value object when it captures real domain meaning or protects a shared invariant. Do not create a type solely because values appear together once, or combine values whose relationship is incidental.

## Primitive Obsession

Primitive values are appropriate for simple data and boundaries. Consider a domain type when a primitive conceals meaningful constraints, units, identity, or behavior that callers must repeatedly reconstruct.

**Reject when:**

- A primitive permits invalid states that lead to a concrete defect, such as confusing distinct identifiers, mixing units, or accepting malformed domain values.
- Callers duplicate validation or conversion rules inconsistently for the same concept on paths affected by the change.
- The representation fails to protect an invariant the code relies on.

**Flag when:**

- A primitive repeatedly crosses boundaries with domain meaning that is unclear from its name or use.
- Callers perform repeated parsing, formatting, validation, or unit conversion for the same concept.
- Several related values and operations would be clearer and safer when represented by a cohesive domain type.

Prefer a small type that expresses a meaningful invariant or operation, and validate at the appropriate boundary. Do not wrap every string, number, or boolean; keep primitives when their meaning is obvious, constraints are trivial, and a type would add indirection without improving safety or clarity.
