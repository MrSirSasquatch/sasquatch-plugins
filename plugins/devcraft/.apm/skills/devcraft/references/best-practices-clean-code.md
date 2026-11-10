# Clean Code Practices

Apply these practices when writing, changing, and reviewing code. They cover names, functions, classes, comments, exceptions, and unit tests. Apply them to new and changed code, including existing code whose behavior the change affects.

## Applying the Practices

Write code that follows these practices. When reviewing code, flag anything that does not adhere to them. For each finding, identify the location, the practice not followed, the consequence, and the smallest useful correction. Make findings specific and verifiable. Avoid speculation and duplicate findings for the same underlying issue.

Apply the practices strictly, but in context, including the qualifications below. Established language idioms and repository conventions can meet their intent without matching an example literally. If a necessary tradeoff departs from a practice, explain the reason and remaining risk rather than silently treating it as compliant.

Line counts, argument counts, and class sizes are investigation signals, not automatic violations. Do not impose personal taste, introduce abstractions for hypothetical requirements, or require unrelated cleanup.

## Meaningful Names

Names must reveal intent, distinguish concepts, and reflect behavior. Apply this to variables, parameters, fields, functions, classes, namespaces, directories, projects, and solutions.

**DO:**

- Name the domain entity, purpose, or role, not merely its technical category. Preserve meaningful domain qualifiers through parameters, fields, and local aliases.
- Make the represented concept apparent at the point of use without requiring readers to navigate to a declaration or use IDE hover. A nearby type declaration alone does not justify discarding useful domain meaning.
- Distinguish different concepts and use consistent vocabulary for the same concept across boundaries. Make any necessary translation explicit.
- Include relevant units and make names agree with values, conditions, and effects.
- Use verbs for operations and clear conditions for booleans. Use established domain terms rather than inventing abbreviations.

**DO NOT:**

- Replace a specific concept with generic names such as `settings`, `options`, `data`, `temp`, `manager`, `process`, or `result` when that removes useful meaning.
- Misrepresent behavior, such as naming a mutating operation `isValid`, or store milliseconds in a value named `timeoutSeconds`.
- Make readers decode unexplained abbreviations, numeric suffixes, type encodings, redundant prefixes, or double negatives.
- Give public APIs or shared domain concepts names that require inspecting implementation details to understand their purpose.

Use the shortest name that preserves useful meaning, not the shortest possible name. Short conventional names are appropriate when their meaning is immediately apparent in a small scope, such as a simple lambda parameter. Do not mechanically repeat an enclosing type's name or add words that provide no useful distinction.

**DO NOT:**

```csharp
var settings = options.Value;
```

**DO:**

```csharp
var organisationApiSettings = organisationApiOptions.Value;
```

The improvement is preserving which configuration both identifiers represent, not replacing `var` or merely making names longer.

## Functions

A function should perform one coherent operation at a consistent level of abstraction. Make its inputs, outputs, and side effects understandable from its contract.

**DO:**

- Separate unrelated operations so callers can invoke one without triggering another.
- Make consequential side effects, mutation of caller-owned inputs, and required call order explicit.
- Design interfaces to prevent invalid argument combinations or handle them explicitly. Use named arguments, distinct operations, or a cohesive domain object when positional arguments or boolean modes make calls ambiguous.
- Consolidate shared business rules, or make necessary variations explicit so affected paths stay consistent.
- Use guard clauses or cohesive extraction to clarify tangled conditions and deeply nested paths.
- Extract behavior when it gives an important concept a name; keep orchestration and low-level details at clear abstraction boundaries.

**DO NOT:**

- Hide state changes behind query-like names. Operations such as `tryDequeue` can legitimately answer a question and change state when the contract exposes both.
- Combine independently meaningful responsibilities or use section comments as a substitute for cohesive operations.
- Bundle unrelated arguments into a parameter object merely to reduce the argument count.
- Add helper layers that force readers to jump between functions without adding meaning.
- Create a function per statement or eliminate all repeated syntax. Extract cohesive behavior and shared knowledge, not merely similar text.

| DO NOT | DO |
|---|---|
| `saveInvoice(invoice, true)` where `true` means send an email. | `saveInvoice(invoice, sendEmail: true)` when that mode belongs to the operation's contract. |
| A function named `calculateInvoiceTotal` also saves the invoice. | Keep calculation free of persistence; make saving an explicit operation. |

## Classes

Give each class a cohesive responsibility, protect its invariants, and expose a small interface suited to its callers.

**DO:**

- Establish valid state during construction and control mutations that could violate invariants.
- Keep responsibilities and dependencies aligned with the class's purpose. Separate unrelated reasons to change.
- Put domain rules with the object that owns them rather than making callers navigate object graphs and reconstruct those rules.
- Preserve the base type's promised behavior in subtypes, including accepted inputs and observable effects.
- Prefer composition when inheritance mainly shares implementation and creates an awkward behavioral relationship.
- Isolate volatile infrastructure behind meaningful boundaries when direct coupling obstructs testing or routine change.

**DO NOT:**

- Expose mutable state that lets callers break invariants or require callers to understand internal representation to use a class safely.
- Introduce shared mutable or global state that creates hidden coupling between otherwise independent instances.
- Add abstractions, interfaces, or design patterns without a current problem they solve.
- Mechanically wrap every dependency or primitive, or require behavior on every data structure. Records, DTOs, and boundary representations can legitimately expose data.

| DO NOT | DO |
|---|---|
| Let callers set an order's status to shipped without satisfying its shipping rules. | Expose an operation such as `order.ship()` that enforces those rules. |
| Add `IInvoiceFormatter` solely because every class is expected to have an interface. | Introduce an interface when it protects a real boundary or supports required implementations. |

## Comments

Use comments to preserve reasoning, constraints, and contracts that the code alone cannot communicate clearly.

**DO:**

- Explain non-obvious ownership, side effects, units, ordering constraints, algorithms, and protocol requirements where callers or maintainers need them.
- Document the rationale, external constraint, and removal condition for a workaround when relevant.
- Keep comments and API documentation consistent with behavior; update adjacent comments when behavior changes.
- Follow language and repository conventions for documentation comments.

**DO NOT:**

- Paraphrase obvious statements, explain a misleading name instead of fixing it, or repeat facts already clear from names and types.
- Use comments to excuse a known correctness defect instead of fixing it or explicitly defining the unsupported behavior.
- Leave commented-out code, change histories, or stale TODOs in active code. Use version control and actionable tracking.
- Treat documentation comments as subject to a blanket ban on describing behavior.

| DO NOT | DO |
|---|---|
| `retryCount++; // Increment retry count` | Let the statement speak for itself. |
| `// Wait before retrying` when the reason for the delay matters. | `// The provider requires at least one second between retry attempts.` when that is the actual constraint. |

## Exceptions

Preserve useful failure context, respect the API contract, and leave resources and state in a defined condition. Apply the same principles to explicit error values in languages that use them.

**DO:**

- Handle failures at a boundary that can recover, translate them for a caller, or report them usefully. Let failures propagate when a higher boundary owns that responsibility.
- Preserve the original cause, stack information, failed operation, and safe identifying context when translating or rethrowing errors.
- Follow language idioms for cleanup and cancellation. Use transactions or explicit recovery where partial updates would violate invariants.
- Make intentional fallbacks satisfy the contract and preserve required failure visibility.
- Use result types or ordinary control flow for routine expected outcomes when the API provides them.

**DO NOT:**

- Swallow a failure, log and ignore it, or replace an unsuccessful operation with a success-like default.
- Use overly broad handlers to turn unexpected defects into routine outcomes or hide cancellation.
- Retry without respecting the failure's retry semantics and the operation's side effects.
- Expose secrets or sensitive data in error messages or logs. Keep diagnostic detail separate from safe user-facing messages.
- Catch exceptions at every layer, duplicate logs without distinct operational value, or obscure the normal path with repeated handling code.

| DO NOT | DO |
|---|---|
| Return an empty invoice collection when retrieval failed. | Propagate or explicitly represent the retrieval failure; reserve an empty collection for a successful query with no invoices. |
| In C#, use `throw exception;` to rethrow a caught exception. | Use `throw;` to preserve the original stack when rethrowing from the catch block. |

## Unit Tests

Write fast, repeatable tests of observable behavior that protect the changed contract against regressions.

**DO:**

- Cover material success, boundary, failure, and cleanup cases affected by the change.
- Assert the required outcome so a test fails when the behavior it claims to verify is broken.
- Make test names, setup, and assertions communicate the behavior and expected result. Keep arrange, act, and assert discernible without requiring labels on trivial tests.
- Control time, randomness, and shared state. Keep tests independent of execution order and live services.
- Mock at meaningful boundaries and ensure test doubles honor the real dependency's relevant contract. Use integration tests when the contract depends on real components interacting.
- Use meaningful test values and assertions that identify what went wrong. Multiple assertions are appropriate for one coherent behavior.
- Use Arrange, Act and Assert comments to help readers identify the structure of a test
- Keep arrange code of tests simple and readable. Extract complicated test setups out into helper methods. An arrange that changes a property on a mock or fake shows intent that this precondition is part of the test but this is only easily visible without complicated arrange code cluttering the test method.

**DO NOT:**

- Remove or weaken assertions to accommodate a defect rather than an intentional contract change.
- Check only that a mock was called when the returned result is the requirement.
- Over-mock so the test bypasses the behavior it should verify, or bind tests to private methods and incidental call sequences.
- Cover unrelated behaviors in one test or add irrelevant setup to shared fixtures.
- Rely on arbitrary sleeps or equate a coverage percentage with useful regression protection.
- Require unit tests for documentation-only or purely mechanical edits.

| DO NOT | DO |
|---|---|
| Verify only that the repository was called in a test of an invoice total. | Assert the expected total returned by the operation under test. |
| Wait for a real deadline with a sleep. | Advance a controlled clock to exercise the deadline deterministically. |
