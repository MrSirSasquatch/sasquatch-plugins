---
name: devcraft
description: Software craftsmanship and development best practices. Use on all development tasks to ensure high-quality, maintainable, and readable code.
---


## Workflow

### 1. Plan

 - Understand the ask from the user in the context of the codebase you'll be working withand the requirements for achieving it. At a high level, formulate a plan or opinion on how to approach the task.
 - Do you see any challenges in being able to implement the task according to these guidelines? Confirm with the user before proceeding. Provide options or alternative approaches if necessary.
 - Where the changes modify important aspects of the codebase such as adding new domain models, implementing a major architectural changes to how components interact, create a written implementation plan and get it reviewed by the user before proceeding. For minor changes, you may proceed with an in-memory plan without confirming with the user. 


### 2. Red/Green/Refactor

Start by writing tests using the Red/Green/Refactor cycle. This means you should first write a failing test (Red), then implement the minimum code necessary to make the test pass (Green), and finally refactor the code while keeping the tests passing (Refactor).

### 3. Review

Review the changes that have been made. Ensure that they align with the initial plan, follow best practices, and maintain code quality. 

Perform an automated review using subagents in a fresh context to ensure that the changes adhere to the established coding standards and best practices.

## Standing Orders

These are the standing orders that should be followed for all development tasks:

 - You MUST use the Red/Green/Refactor cycle for all code changes.
 - You SHOULD implement code using the tell, don't ask principle, meaning you should tell objects what to do rather than asking them for data and making decisions outside of them.
 - You SHOULD use the gang of four design patterns where applicable to promote code reuse and maintainability. GoF patterns MUST be used to solve demonstrated design and architectural problems, not to decorate code unnecessarily.
 - You MUST plan, consider and review XYZ in your approach to all development tasks.



## Craftsmanship Reference

Refer to these best-practices on every development task and code review.

|Reference file|Description|
|---|---|
|references/best-practices-clean-code.md|The most important topics and practices for writing clean, maintainable, and readable code.|

Refer to these best-practices when the implementation calls for it.

### Clean Code

#### When Writing Code

##### Naming
Prefer descriptive and intention-revealing names for variables, methods, and classes to make the code self-documenting. 

Examples:
 -  `var shoppingCart = new ShoppingCart();` over `var sc = new ShoppingCart();`
 -  `CalculateTotalPrice()` over `CalcTP()`

Avoid using ambiguous or names which don't clearly describe the thing they are naming. 

Examples:
 - `orderDetails` over `orderData`
 - `var fileData = file.Data;` over `var data = file.Data;`

When a variable holds an instance of a type, include the specific entity it serves in the variable name instead of using a generic name.

Examples:
 - `var userResolver = new UserResolver();` over `var resolver = new UserResolver();`



##### When Reviewing Code

Review the names of variables, methods, and classes to ensure they are descriptive and intention-revealing. Reject or flag names that do not meet the guidelines set forth above.



---
### Comments

#### When Writing Code
Add comments to explain why the code is doing something, not what it is doing. Through proper conventions such as intention revealing names, methods and properly named variables, the code should be self-documenting on what it does. Write comments explaining a "why" when this reasoning is not immediately apparent from the code itself.

#### When Reviewing Code

Note: This rule does not apply to documentation comments such as XML comments or Javadoc etc.

 - Large comment blocks explaining what code does indicate poorly written code. They MUST be avoided in favour of writing clear and self-documenting code.
 - Comments should provide meaningful context and explain the reasoning behind the code, rather than stating the obvious.
 - Comments should be concise and to the point, avoiding unnecessary verbosity.
 - Comments should be kept up-to-date and reflect the current state of the code. Outdated comments can be misleading and should be corrected or removed. Review unchanged comments adjacent to modified code to ensure consistency.

Reject or flag comments that do not meet these standards.


---
