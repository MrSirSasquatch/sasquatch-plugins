# Clean Code Review Standards

Use this reference to review names, functions, classes, comments, formatting, exceptions, and unit tests. Apply the standards to new and changed code, including existing code whose behavior the change affects.

## Review Decisions

- **Reject** when a change violates a standard and creates a concrete correctness, reliability, or maintenance problem. Require a fix before approval.
- **Flag** when there is a credible concern but its impact or remedy needs context. Explain the concern and request clarification or a focused improvement. A flag is not automatically a blocker.
- **Accept** when the implementation meets the intent of the standard, including when an established language idiom or repository convention achieves it differently.

For each finding, identify the location, the violated standard, the consequence, and the smallest useful correction. Describe the problem precisely enough that another reviewer can verify it. Avoid speculative findings and duplicate findings for the same underlying issue.

Judge readability and responsibility in context. Line counts, argument counts, and class sizes are investigation signals, not automatic rejection thresholds. Do not block on personal taste, demand abstractions for hypothetical requirements, or require unrelated cleanup. If a tradeoff is justified, record why it is acceptable and which risk remains.

## Meaningful Names

Names must reveal intent, distinguish concepts, and agree with behavior.

**Reject when:**

- A name misrepresents a value, unit, condition, or effect, such as `timeoutSeconds` holding milliseconds or `isValid()` mutating the object.
- Different concepts use indistinguishable names, or the same domain concept changes names across a boundary without a clear mapping, making incorrect use likely.
- A public API or shared domain concept has an ambiguous name that forces callers to inspect implementation details to use it correctly.

**Flag when:**

- Names such as `data`, `temp`, `manager`, or `process` conceal the entity or operation in a context where a specific name would clarify it. Prefer `invoiceLines` and `calculateInvoiceTotal` when those describe the actual purpose.
- Abbreviations, numeric suffixes, type encodings, or redundant prefixes require readers to decode names. Allow established domain terms and conventional names in small scopes.
- Similar operations use inconsistent vocabulary, or unrelated operations share a name that suggests equivalence.
- Boolean names obscure the condition, especially through double negatives, or functions use nouns where a verb would reveal the action.

Prefer names that communicate domain meaning and relevant units. Do not require long names when a short, conventional name is unambiguous in its scope.

## Functions

A function should perform one coherent operation at a consistent level of abstraction. Its inputs, outputs, and side effects must be understandable from its contract.

**Reject when:**

- A function hides consequential side effects behind a query-like name, silently changes caller-owned inputs, or depends on undocumented call order that can produce incorrect behavior.
- Unrelated operations are coupled so that a caller cannot safely perform one without triggering the others.
- An interface permits invalid argument combinations that the implementation mishandles, or interchangeable positional arguments create a demonstrated misuse risk.
- Duplicated business rules can produce inconsistent results across paths affected by the change. Consolidate the rule or make the necessary variation explicit.

**Flag when:**

- A function mixes orchestration with low-level details, contains several independently meaningful responsibilities, or needs section comments to explain separate phases.
- Deep nesting, tangled conditions, or repeated branching obscures normal and exceptional paths. Prefer guard clauses or cohesive extraction where they clarify flow.
- Boolean mode arguments or long parameter lists make calls difficult to interpret. Consider named arguments, distinct operations, or a cohesive domain object; avoid a parameter bag of unrelated values.
- A function both answers a question and changes state without making that combined operation explicit. Legitimate operations such as `tryDequeue` should expose both effects in their contract.
- Extraction would give an important concept a name, or existing helper layers make readers jump between functions without adding meaning.

Do not demand a function per statement or eliminate all repeated syntax. Extract cohesive behavior and shared knowledge, not merely text that happens to look alike.

## Classes

Classes should have a cohesive responsibility, protect their invariants, and expose a small interface suited to their callers.

**Reject when:**

- Public mutable state or an incomplete construction path lets callers violate an invariant that the class relies on.
- Unrelated responsibilities are entangled so that changing one can break another, or callers must understand internal representation to use the class safely.
- A subtype violates its base type's promised behavior, such as rejecting inputs the base contract accepts or unexpectedly changing observable effects.
- Shared mutable or global state introduces hidden coupling that causes incorrect behavior or prevents callers from safely using otherwise independent instances.

**Flag when:**

- A class accumulates unrelated reasons to change, broad dependency lists, or groups of methods that work on separate subsets of its fields.
- Callers repeatedly navigate object graphs and implement rules that belong with the object responsible for them. Prefer telling that object to perform a domain operation when it owns the rule.
- Inheritance exists mainly to reuse implementation and creates an awkward behavioral relationship. Consider composition where it makes the contract clearer.
- A class depends directly on volatile infrastructure in a way that obstructs meaningful testing or routine change.
- An abstraction, interface, or design pattern adds indirection without solving a current problem.

Do not require behavior on every data structure. Records, DTOs, and boundary representations can legitimately expose data. Introduce interfaces or domain types where they protect a real boundary or invariant, rather than mechanically wrapping every dependency or primitive.

## Comments

Comments should preserve reasoning, constraints, and contracts that the code alone cannot communicate clearly.

**Reject when:**

- A comment or API documentation contradicts the implementation in a way that can cause incorrect use or maintenance.
- A required contract is missing or inaccurate, including non-obvious ownership, side effects, units, or ordering constraints that callers need to use an API safely.
- A comment excuses a known correctness defect instead of addressing it or making the unsupported behavior explicit in the contract.

**Flag when:**

- A comment paraphrases statements, explains a misleading name, or describes phases that would be clearer as cohesive operations.
- Commented-out code, change histories, or stale TODOs obscure the active implementation. Use version control for history and actionable tracking for deferred work.
- Comments repeat facts already expressed by names, types, or nearby documentation, creating multiple places to maintain the same information.
- A workaround or surprising choice lacks the rationale, external constraint, or removal condition needed to maintain it safely.

Keep useful explanations of algorithms, protocol requirements, and deliberate tradeoffs. Documentation comments follow the language and repository conventions; they are not subject to a blanket ban on describing behavior. Review adjacent comments when changing the behavior they explain.

## Exceptions

Failure paths must preserve useful context, respect the API contract, and leave resources and state in a defined condition. Apply the same principles to explicit error values in languages that use them.

**Reject when:**

- An exception is swallowed, logged and ignored, or replaced with a success-like default while the operation remains unsuccessful. An intentional fallback must meet the contract and preserve any required failure visibility.
- An overly broad handler turns unexpected defects into routine outcomes, hides cancellation, or retries failures without respecting the operation's retry and side-effect semantics.
- Error conversion or rethrowing destroys the original cause, stack information, or context needed to diagnose the failure when the language supports preserving it.
- Failure leaks resources or leaves partially updated state that violates an invariant. Require appropriate cleanup, transactions, or explicit recovery behavior.
- An error message or log exposes secrets or sensitive data.

**Flag when:**

- Handlers are far from the boundary that can actually recover, translate the failure for a caller, or report it usefully.
- Generic exceptions or vague messages omit the failed operation and safe identifying context.
- Routine expected outcomes use exceptions where the language or API provides a clearer result type or ordinary control flow.
- Multiple layers log the same failure without distinct operational value, or repeated handling code obscures the normal path.

Do not require every layer to catch exceptions. Let failures propagate when a higher boundary owns recovery or reporting. Follow the language's cleanup and cancellation idioms, and keep diagnostic detail separate from safe user-facing messages.

## Unit Tests

Tests should provide fast, repeatable evidence of observable behavior and protect the changed contract against regressions.

**Reject when:**

- Changed behavior lacks coverage for a material success, boundary, or failure case, leaving a concrete regression risk unexplained.
- A test can pass when the behavior it claims to verify is broken, such as checking only that a mock was called when the returned result is the requirement.
- Assertions are removed, weakened, or rewritten merely to accommodate a defect rather than an intentional contract change.
- Tests depend on execution order, uncontrolled time or randomness, shared mutable state, live services, or arbitrary sleeps in ways that make outcomes unreliable.
- Over-mocking bypasses the very logic under test, or a test double implements a materially different contract from the real dependency and hides a defect.

**Flag when:**

- Test names, setup, or assertions obscure the behavior and expected outcome. Prefer visible arrange, act, and assert phases without requiring labels on trivial tests.
- Tests bind to private methods, incidental call sequences, or internal structure, making behavior-preserving refactoring needlessly expensive.
- A test covers unrelated behaviors, or a shared fixture contains irrelevant setup that makes failures difficult to understand.
- Boundary values, failure handling, or cleanup paths affected by the change are missing and their importance needs investigation.
- A test relies on unexplained literals or produces failures that do not identify what went wrong.

Allow multiple assertions for one coherent behavior. Mock at meaningful boundaries; use integration tests when the contract depends on real components interacting. Do not demand unit tests for documentation-only or purely mechanical edits, or equate a coverage percentage with useful regression protection.
