# Code Smell Prevention Practices

Apply these practices when writing, changing, and reviewing code to prevent long functions, god classes, unclear parameter lists, data clumps, and primitive obsession. Apply them to new and changed code, including existing code whose behavior the change affects.

## Applying the Practices

Write code that follows these practices. When reviewing code, flag anything that does not adhere to them. For each finding, identify the location, the practice not followed, the consequence, and the smallest useful correction. Make findings specific and verifiable. Avoid speculation and duplicate findings for the same underlying issue.

Apply the practices strictly, but in context, including the qualifications below. Established language idioms and repository conventions can meet their intent without matching an example literally. If a necessary tradeoff departs from a practice, explain the reason and remaining risk rather than silently treating it as compliant.

Treat size, repetition, and primitive types as investigation signals, not automatic violations. A structure that resembles a named smell can still be clear and cohesive. Do not require unrelated refactoring, introduce abstractions for hypothetical reuse, or prescribe arbitrary line, field, or argument-count thresholds.

## Long Functions

A function should express one coherent operation at a consistent level of abstraction. Keep meaningful decisions, responsibilities, and important paths visible.

**DO:**

- Extract cohesive operations with meaningful names when distinct steps or mixed abstraction levels obscure the main flow.
- Separate unrelated responsibilities so callers can use or change one without unintentionally affecting another.
- Simplify nested branches and tangled control flow so normal and failure paths are understandable and verifiable.
- Consolidate shared decision logic so affected paths apply the same rules consistently.
- Make inputs, outputs, and side effects understandable as one contract. Separate orchestration from detailed work when it clarifies responsibility or enables focused testing.

**DO NOT:**

- Hide important failure paths or independently meaningful responsibilities inside a long sequence of implementation details.
- Split a straightforward sequence into tiny helpers merely to reduce line count. Keep closely related steps together when extraction would obscure behavior.

| DO NOT | DO |
|---|---|
| Bury invoice validation, total calculation, and persistence details in one deeply nested function. | Keep the main flow readable through cohesive operations such as `validateInvoice`, `calculateInvoiceTotal`, and `saveInvoice`. |
| Extract each assignment into a helper to meet a line-count limit. | Keep a clear, cohesive sequence together regardless of its line count. |

## Large Classes (God Classes)

A class should have a cohesive responsibility, protect the invariants it owns, and expose an interface suited to its callers. Organize it around responsibilities and coupling, not raw size.

**DO:**

- Keep related behavior and state together with clear ownership, lifecycle, and invariant protection.
- Separate unrelated responsibilities when changing one could break another or their state and dependencies can be isolated meaningfully.
- Use groups of methods that operate on separate fields or change for distinct reasons as signals to examine responsibility boundaries.
- Keep dependencies and public operations aligned with the class's purpose.
- Put rules with a cohesive collaborator that owns them instead of making callers navigate internals or duplicate those rules.

**DO NOT:**

- Accumulate unrelated concerns and dependencies in one class or leave state ownership ambiguous.
- Require callers to understand internal representation to use the class safely.
- Split a cohesive class solely to reduce its field or method count, or create a service for every operation.

| DO NOT | DO |
|---|---|
| Make one class own invoice rules, SMTP connections, and PDF layout details. | Keep invoice rules cohesive and delegate email transport and document rendering to collaborators with clear responsibilities. |
| Move fields into a helper while leaving all their rules in the original class. | Move related state and behavior together so the new boundary has meaningful ownership. |

## Long Parameter Lists

Make an operation's required inputs clear and safe to provide. Communicate intent at the call site and represent cohesive concepts explicitly where useful.

**DO:**

- Use named arguments or distinct domain types when similar positional values are easy to confuse by order, meaning, or unit.
- Prevent invalid argument combinations or handle them explicitly.
- Represent related inputs with a cohesive domain object or options type when it clarifies their shared meaning.
- Use separate operations when boolean or nullable mode parameters select substantially different contracts.
- Keep independent, genuinely required inputs explicit rather than hiding them in ambient state or inappropriate optional defaults.

**DO NOT:**

- Require readers to remember the meaning or order of ambiguous arguments.
- Bundle unrelated values into a parameter bag merely to shorten the signature.
- Replace clear, explicit parameters solely to meet an argument-count limit.

| DO NOT | DO |
|---|---|
| `transferFunds(firstAccountId, secondAccountId, amount)` when the direction is unclear. | `transferFunds(sourceAccountId: firstAccountId, destinationAccountId: secondAccountId, amount: amount)`. |
| Combine unrelated dependencies and request values in a generic `OperationParameters` object. | Keep independent inputs explicit; group only values that form a meaningful concept. |

## Data Clumps

Repeated groups of values may represent one concept with shared meaning, validation, or behavior. Establish that relationship before introducing a new type.

**DO:**

- Identify related values that repeatedly travel together through signatures, return values, or fields and require callers to keep them aligned.
- Introduce a cohesive value object when it names a real domain concept or protects a shared invariant.
- Centralize shared validation and behavior so affected paths cannot apply inconsistent rules.
- Keep values with a shared lifecycle consistent when passing, storing, or updating them.

**DO NOT:**

- Make callers repeatedly reconstruct a domain concept from separately handled values and duplicated rules.
- Create a type solely because values appear together once, or combine values whose relationship is incidental.

| DO NOT | DO |
|---|---|
| Pass `startDate` and `endDate` separately through many operations, each implementing its own date-order validation. | Use a `DateRange` value object that enforces the shared ordering rule. |
| Group `customerId` and `retryCount` because they appear in the same call. | Keep them independent when they have no shared meaning, lifecycle, or invariant. |

## Primitive Obsession

Primitive values are appropriate for simple data and boundaries. Use a domain type when a primitive conceals meaningful constraints, units, identity, or behavior that callers must repeatedly reconstruct.

**DO:**

- Represent meaningful invariants or operations with a small domain type when it improves safety or clarity.
- Distinguish identifiers and units when using interchangeable primitives would permit incorrect use.
- Validate at the appropriate boundary and preserve the valid state the code relies on.
- Centralize repeated parsing, formatting, validation, and conversion for the same concept.
- Make domain meaning explicit when values cross boundaries.

**DO NOT:**

- Rely on callers to reconstruct hidden constraints or apply duplicated validation and conversion rules consistently.
- Allow a representation to admit invalid states that the code assumes cannot occur.
- Wrap every string, number, or boolean. Keep primitives when their meaning is obvious, constraints are trivial, and a type would add indirection without improving safety or clarity.

| DO NOT | DO |
|---|---|
| Pass a timeout as an unqualified integer while callers repeatedly convert between seconds and milliseconds. | Use a duration type such as `TimeSpan`, converting to the required unit at the external boundary. |
| Wrap a simple display label in a domain type solely because it is a string. | Keep the string when a meaningful name already communicates its purpose and no additional invariant needs protection. |
