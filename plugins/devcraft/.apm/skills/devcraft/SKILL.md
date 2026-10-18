---
name: devcraft
description: Software craftsmanship and development best practices. Use on all development tasks to ensure high-quality, maintainable, and readable code.
---


## Workflow

The following workflow SHOULD be followed for all development tasks unless explicitly instructed otherwise by the user.

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
 - You MUST plan, consider and review all must-have best-practices noted in the Craftsmanship Reference section below on every development task and code review.



## Craftsmanship Reference


### Must-have best-practices
Refer to these best-practices on every development task and code review.

|Reference file|Description|
|---|---|
|references/best-practices-clean-code.md|The most important topics and practices for writing clean, maintainable, and readable code.|
|references/best-practices-code-smells.md|Code smells that should be avoided or resolved.|

---
