---
name: devcraft-code
description: Write, change, or fix code by dispatching devcraft-implementer agents that apply devcraft principles. Use for implementing features, refactors, and accepted review fixes.
---

# Devcraft Code

Implement a requested change by coordinating `devcraft-implementer` agents. The coordinator scopes, briefs, dispatches, verifies, and integrates. The implementers write the code.

## Procedure

### 1. Establish the task

- Identify the requested outcome, acceptance criteria, and exclusions. If the user supplied accepted review findings, treat those as the scope; rejected or deferred findings are not instructions.
- Inspect only enough of the repository to understand affected code, conventions, repository instructions, and the checks available (build, tests, linters).
- Ask the user only when a material ambiguity would change the design. Otherwise state your assumptions and continue.

### 2. Plan the work

Split the work into tasks only where the split is natural. Use one implementer for small or tightly coupled changes. Use several implementers in parallel only when their file ownership is disjoint and dependencies are satisfied; otherwise run them sequentially.

For each task decide the deliverable, the files the agent may edit, files it must not touch, dependencies on other tasks, and the checks that prove it is done. Settle design decisions here so implementers receive one decision, not competing options.

### 3. Dispatch implementers

Invoke the named agent `devcraft-implementer` for each task with a focused brief. Do not paste the whole conversation. A task label containing the agent name does not load the agent definition, so use the runtime's named-agent invocation. If it is unavailable, supply the body of the agent definition plus the brief to a fresh agent and report that fallback.

Each brief contains:

- **Task and ownership:** The concrete deliverable, files the agent may edit, and exclusions. Do not allow overwriting another agent's work.
- **Outcome:** Acceptance criteria and relevant settled design decisions.
- **Rules:** Applicable repository instructions and language guidelines. Point to the relevant files under the `devcraft-review` skill's `references/` directory (`clean-code/`, `code-smells/`, and the `lang-*.md` file for the language, for example `lang-csharp.md`) or include excerpts if the agent cannot read them. Always name `clean-code/unit-tests.md` when tests are written or changed.
- **Dependencies:** Earlier results or contracts the task relies on.
- **Verification:** The build, test, and lint commands to run and the expected results. Meaningful tests are added or updated for changed behaviour; documentation-only changes need content checks instead.
- **Return:** Changed files, acceptance criteria satisfied, checks actually run with results, deviations from the brief, and unresolved issues. An unrun check must not be reported as passing.

Use a lightweight model at high reasoning effort unless the user chose otherwise, and set it through the runtime's launch controls when supported. Never claim a model or effort setting was applied unless the runtime confirms it.

### 4. Verify and integrate

- Read each result and confirm it matches the brief. Resolve ownership conflicts and material deviations by deciding, then re-dispatching the same agent with a narrow follow-up if needed.
- Run the relevant build, tests, and linters yourself after integration. Fix failures by dispatching an implementer rather than editing the code directly.
- Check that all acceptance criteria are met and that nothing outside the scope changed.

### 5. Report

Summarise what changed, the checks you ran and their results, any deviations, and open issues. Suggest `devcraft-review` for an independent review when the change is substantial; do not start it unless asked.

## Coordinator rules

- Do not write the production code yourself; your job is to coordinate. Trivial edits to integrate results, such as fixing an import conflict between tasks, are acceptable.
- Keep your own context clean: pass implementers briefs and excerpts, not transcripts.
- Do not launch reviewers from this skill. Review belongs to `devcraft-review`.
