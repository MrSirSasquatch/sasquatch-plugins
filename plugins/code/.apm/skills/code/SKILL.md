---
name: code
description: Apply personal coding preferences when writing, refactoring, or reviewing code.
---

# Code

How to write clean, readable, and maintainable code.

## Standing orders

- Write code that is easy to read and understand by a human
  - On naming, prefer verbose and descriptive names over short or abbreviated ones. Avoid generic or ambiguous names, prefer names like `customerData`, `configFileStream`, and `ProcessEvent()` over `data`, `stream`, and `Process()`.
  - Other than documentation comments, add code comments sparingly to explain non-obvious reasoning, constraints, or choices. **Don't explain what** the code does, well written code should be self-documenting. If needed, **explain why** the code is written in a particular way.
- Follow the SOLID principles for object-oriented design.
- Keep functions and classes focused on a single responsibility.
- Structure code for modularity and reusability. Prefer more files, each with a focused responsibility, over fewer large files. 
- Avoid god classes that accumulate unrelated responsibilities. Keep classes focused on a cohesive purpose.
- Avoid primitive obsession: when a method takes several related primitive parameters, group them into a meaningful domain or parameter object, such as `Address` instead of separate street, city, and postcode strings. Keep simple independent values as primitives.

#### Comments
- Add explanatory comments sparingly to document non-obvious reasoning, constraints, or choices.
- Prefer clearer code over comments that merely explain what the code does.
- Follow the language's documentation conventions. 

These standing orders MUST be followed on every code change unless any of the following criteria are met.

 - The user explicitly instructs otherwise.
 - Following any or all of the orders would have an overall negative impact on the codebase. 


## Workflow

### 1. Write tests

Write tests for your planned changes before implementing them. The tests should fail initially with the intention of them passing after the implementation is complete. 

For any new classes or methods etc that need to be introduced, it is acceptable to add them as stubs initially to allow the tests to compile and run.

### 2. Review

Perform a self-review of the tests that have been created.

The tests and any stubs give you an idea of how the implementation will be completed. At this point, you can review the code structure, organisation and planned additions/modifications against the standing orders before expensive implementation code has been written. 

Ask annother agent, using this skill to review the code in a fresh session for an additional unbiased perspective.

Make any necessary adjustments based on the feedback received and then move to the next step. 

### 3. Implement

Implement the planned changes to the codebase. Follow the standing orders and coding principles outlined above to ensure high-quality, maintainable, and readable code.

### 4. Review Implementation

After implementing the changes, review the code to ensure it adheres to the standing orders and coding principles. Check for readability, maintainability, and overall quality before considering the task complete.

Again, ask another agent, using this skill to review the implementation in a fresh session for an additional unbiased perspective.

Make any necessary adjustments based on the feedback received before considering the task complete.


## Code Style

- Prefer descriptive variable names over short or abbreviated names. Add words only when they improve clarity.
- Prefer `var shoppingCart = new ShoppingCart();` over `var sc = new ShoppingCart();`.
- Avoid generic variable and method names: prefer `customerData`, `configFileStream`, and `ProcessEvent()` over `data`, `stream`, and `Process()`.

## Design

- Unless explicitly instructed otherwise, follow established coding practices, including SOLID and clean code principles where applicable.
- Keep designs simple; introduce abstractions for current requirements rather than hypothetical future needs.


- Keep functions short and focused. Treat functions of 100 or more lines as a signal to review their responsibilities and extract cohesive operations where it improves clarity.

## Testing



## Comments



## Workflow

1. Follow the testing approach above, then implement the feature or change.
2. Run relevant tests, linting, and builds. Fix warnings introduced by your changes.
3. Review code touched by the task for readability, organisation, naming, and appropriate modularity. Refactor only where it provides a concrete benefit within scope.
3. Review your own code changes for potential improvements and adherence to this guidance. Below are some additional review points which should be considered.
  - f
4. After refactoring, rerun relevant tests, linting, and builds.
