---
name: devcraft
description: Software craftsmanship and development best practices. Use on all coding tasks and code reviews to ensure high-quality, maintainable, and readable code. Do not use for non-coding tasks or changes to configuration, documentation, or other non-code related activities.
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

Ask two independent subagents to review the changes and provide structured feedback. The agents should not communicate with each other and should provide their assessments based solely on the changes made and the established coding standards. The agents should use competing models from two separate providers. Anthropic's Sonnet 5.5 and OpenAI GPT-6.1 Sol should be used for this purpose. Where two different model providers are not available. Use the same model for both subagents.

Prompt for the subagent review
```text
Review the uncomitted changes and provide structured feedback according to the guidelines and practices described in the /devcraft skill. 

The scope of your review applies to both the code changes and their impact on the overall codebase. Consider how the changes fit within the broader architecture of the codebase. Don't limit your review to just code within files. Also consider file naming, directory naming and structure as well as project artifacts and organisation as well.

You are to review the changes on their own and MUST NOT build, run or execute the code. You MUST NOT run tests or rely on any external tools to validate the changes. Your review should be based solely on the code and the established coding standards.

Return your findings in the following structured format

File: <path/to/changed/file:lineNumber>
Criticality: <level of criticality, e.g., High, Medium, Low>
Issue: <description of the issue>
Consequence: <description of the potential impact or outcome if the issue is not addressed>

More than one of the above templates can be provided where more than one issue exists.
```



## Standing Orders

These are the standing orders that should be followed for all development tasks:

 - You MUST prioritise your changes for human readability and consider the next developer who will read and maintain the code.
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
