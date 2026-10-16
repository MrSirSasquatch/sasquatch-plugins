---
name: code
description: Apply personal coding preferences when writing, refactoring, or reviewing code.
---

# Code

## Code Style

- Prefer descriptive variable names over short or abbreviated names. Add words only when they improve clarity.
- Prefer `var shoppingCart = new ShoppingCart();` over `var sc = new ShoppingCart();`.
- Avoid generic variable and method names: prefer `customerData`, `configFileStream`, and `ProcessEvent()` over `data`, `stream`, and `Process()`.

## Design

- Unless explicitly instructed otherwise, follow established coding practices, including SOLID and clean code principles where applicable.
- Keep designs simple; introduce abstractions for current requirements rather than hypothetical future needs.
- Avoid god classes that accumulate unrelated responsibilities. Keep classes focused on a cohesive purpose.
- Avoid primitive obsession: when a method takes several related primitive parameters, group them into a meaningful domain or parameter object, such as `Address` instead of separate street, city, and postcode strings. Keep simple independent values as primitives.
- Keep functions short and focused. Treat functions of 100 or more lines as a signal to review their responsibilities and extract cohesive operations where it improves clarity.

## Testing

- Use test-driven development for changes to code behavior: add or extend a test for the intended behavior, observe it fail for the expected reason, then implement the change.
- Preserve existing regression coverage. Update an existing expectation only when the intended behavior changes.
- Add stub classes or methods only when needed to run the failing test.
- For documentation-only changes, review the content without adding behavior tests.
- If test infrastructure is unavailable, report the limitation and use appropriate available checks. Do not claim unrun tests passed.

## Comments

- Add explanatory comments sparingly to document non-obvious reasoning, constraints, or choices.
- Prefer clearer code over comments that merely explain what the code does.
- Follow the language's documentation conventions. In C#, document every public class and member.

## Workflow

1. Follow the testing approach above, then implement the feature or change.
2. Run relevant tests, linting, and builds. Fix warnings introduced by your changes.
3. Review code touched by the task for readability, organisation, naming, and appropriate modularity. Refactor only where it provides a concrete benefit within scope.
4. After refactoring, rerun relevant tests, linting, and builds.
