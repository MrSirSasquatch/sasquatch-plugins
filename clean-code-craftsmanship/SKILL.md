---
name: clean-code-craftsmanship
description: Apply an opinionated XP and object-oriented craftsmanship workflow to software changes and code reviews. Use when implementing behavior, writing or repairing tests, refactoring, designing object collaborations, reviewing a diff, or reducing AI-generated code slop. Favor small verified steps, TDD where practical, clear names, cohesive objects, explicit trade-offs, and evidence over ceremony.
license: MIT
metadata:
  version: "0.1.0"
  standard: agentskills.io
  focus: xp-tdd-refactoring-object-design-review
---

# Clean Code Craftsmanship

Use this skill to keep a change small, behavior-led, test-backed, and easy to explain. The goal is not to make code look clever or to apply patterns by reflex; it is to leave the design simpler and the behavior more trustworthy than it was.

## Operating stance

- Start with the user's observable outcome and the existing code's current behavior. Do not redesign a system merely because a cleaner design is imaginable.
- Prefer a short red–green–refactor loop. Add the smallest meaningful failing test, make it pass, then improve names, boundaries, and duplication while the tests are green.
- Treat tests as clients of the code. Test behavior and collaborations that matter; avoid tests coupled to private implementation details.
- Let abstractions emerge from a demonstrated variation or responsibility. Prefer a few clear objects and messages over speculative layers, factories, frameworks, or pattern-shaped code.
- Keep each change reviewable. Separate behavior changes, structural refactoring, formatting, and dependency upgrades when practical.
- Preserve compatibility deliberately. If an API, persisted format, error contract, or timing assumption changes, call it out and test the boundary.

## Route only the detail you need

Read the relevant reference before acting; do not load every reference by default.

- New behavior, a bug fix, or weak test coverage: [TDD and change loop](references/tdd-and-change-loop.md)
- Object boundaries, polymorphism, or a design pattern decision: [Object design and patterns](references/object-design-and-patterns.md)
- Safe restructuring of existing code: [Refactoring playbook](references/refactoring-playbook.md)
- Reviewing a diff or preparing a craftsmanship verdict: [Craftsmanship review](references/craftsmanship-review.md)
- Suspected generated-code bloat, shallow tests, or unnecessary abstraction: [AI-slop controls](references/ai-slop-controls.md)

## Default workflow

1. State the behavior that must change or be protected, including important non-goals.
2. Inspect the smallest relevant slice: entry point, collaborators, tests, configuration, and public boundary.
3. Write or identify a test that would fail for the missing behavior. For legacy code, use a characterization test before changing an unclear seam.
4. Make the smallest implementation change that passes the focused test. Avoid unrelated cleanup in the same step.
5. Refactor only with a green safety net: improve names, cohesion, duplication, coupling, and error paths without changing behavior.
6. Run focused checks, then the broader relevant suite. Investigate failures rather than weakening tests or hiding warnings.
7. Review the diff as a maintainer: explain the design, remaining risk, compatibility impact, and why each abstraction exists.

## Review and completion standard

A change is not complete merely because it compiles or the happy path works. Before handing it back, establish:

- the requested behavior is covered at the right boundary;
- tests are meaningful and would catch a plausible regression;
- names and object responsibilities make the code readable without narration;
- duplication and coupling were addressed proportionately, not cosmetically;
- error, empty, timeout, retry, and compatibility paths were considered where relevant;
- verification results and any unverified assumptions are explicit.

When the repository's conventions conflict with these preferences, follow the repository and user first, then record the trade-off rather than forcing a doctrine.
