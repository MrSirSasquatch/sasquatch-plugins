# Focused agent briefs

The coordinator fills these briefs with concrete context before dispatching the named APM agent. Its definition supplies role guidance; the brief supplies the task. Send relevant excerpts and paths rather than the full conversation. Include applicable repository instructions; a narrow brief does not override them. Agents may inspect supporting files needed to establish evidence. Workers do not restart the orchestration skill or delegate further.

## Specialist review brief

- **Role:** One specialist category and its named agent from the coordinator's catalogue. For a fresh-agent fallback, load that agent's canonical definition as described in [runtime guidance](agent-runtime.md).
- **Stage and mode:** Plan review or code review; state that the assignment is read-only.
- **Request:** Original requested outcome and relevant acceptance criteria.
- **Target:** Plan version and section references, or the exact code baseline and frozen target including uncommitted and untracked content when applicable.
- **Scope:** Decisions, files, symbols, or diff to assess, and relevant supporting context. For code review, include the settled design contracts needed to judge behaviour without the implementer's persuasive explanation.
- **Rules:** Relevant language requirements and repository constraints.
- **Question:** What this specialist should assess, including category boundaries and exclusions.
- **Output:** Supply the Specialist result contract below as an excerpt or an accessible path resolved from the installed devcraft skill. Include coverage and any limitations. No quota and no edits. Flag out-of-category observations for coordinator routing.

Give reviewers requirements and evidence, not another reviewer's conclusions, the coordinator's preferred findings, or implementation-agent reasoning. For targeted follow-up, include the accepted finding and repair scope because that is what is being verified.

### Specialist result

- **Coverage:** Category, target reviewed, and files or plan sections inspected.
- **Findings:** For each, supply a local ID, category, priority, precise location, relevant principle or acceptance criterion, evidence, concrete consequence, and suggested direction. Identify uncertainty or the check needed to resolve it.
- **Priority:** High for serious correctness, compatibility, or structural risk; medium for a concrete maintainability or behavioural problem; low for a local clarity or documentation improvement. Explain the impact rather than assigning severity from a rule's name or a line-count threshold.
- **Location:** File and line or symbol for code, or section/task identifier for a plan. Reference the frozen target, not a later edit.
- **Other observations:** Out-of-category leads for routing, separately from findings.
- **Limitations:** Missing context, unavailable checks, or incomplete coverage. Explicitly return no findings when none are supported.

Do not demand unrelated refactoring or report hypothetical problems without evidence. In code review, focus on problems introduced or compounded by the changes; discuss pre-existing code only to establish their impact. In an explicitly requested broader audit, use the user's selected scope instead.

## Generalist implementation or fix brief

- **Agent:** `devcraft-implementer`. Multiple instances may own independent tasks; the coordinator remains responsible for scheduling and integration.
- **Task and owner:** Concrete deliverable, files the agent may edit, and ownership exclusions.
- **Outcome:** Acceptance criteria and the reviewed plan sections relevant to this task.
- **Decisions:** Settled design, applicable devcraft considerations, language rules, and repository instructions.
- **Dependencies:** Required earlier results, integration contracts, and other agents' ownership. Do not overwrite another agent's changes.
- **Verification:** Relevant checks and expected results. Add or update meaningful tests for changed behaviour when warranted; documentation-only changes need appropriate content checks.
- **For fixes:** Accepted finding IDs, coordinator decisions, intended repair scope, and regression checks. Rejected or deferred suggestions are not instructions to implement.
- **Return:** Supply this common generalist contract as an excerpt or an accessible path resolved from the installed devcraft skill. Report changed files, acceptance criteria satisfied, checks actually run and results, deviations, and unresolved issues. Do not claim an unrun check passed.

Keep code simple, minimal, correct, and complete. Ask the coordinator to resolve ownership conflicts or material design deviations before expanding scope. Agents implement the reviewed decisions rather than independently redesigning the whole task.

## Coordinator dispatch checks

Before starting concurrent writers, confirm that file ownership is disjoint and dependencies are satisfied. Read-only reviewers can share files. If ownership changes, update assignments before another writer starts.

Use [runtime guidance](agent-runtime.md) to invoke the named definition and configure the preferred lightweight model and high effort with supported controls. A model mentioned inside a prompt is not proof of model selection. Record actual settings and any unsupported preference in the run record. Apply read-only tool or sandbox restrictions for reviewers when the runtime supports them; role instructions alone are not an enforced permission boundary.
