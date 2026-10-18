# Object Design and Patterns

Use this reference when deciding where behavior belongs or whether an abstraction is justified.

## Start with responsibilities and messages

Describe the collaboration in plain language before naming a pattern:

- Who owns this decision?
- Which object has the information needed to make it?
- What message would let that object do the work without exposing its internals?
- What should remain invariant if an implementation is replaced?

Prefer objects with one coherent reason to change. A class can have several methods; the test is whether those methods serve one clear responsibility and use a related set of data and collaborators.

## Useful design heuristics

- Keep policies separate from mechanisms and I/O.
- Keep volatile details behind a boundary when that makes tests and replacement easier.
- Prefer immutable values for concepts that have identity by content.
- Prefer composition when inheritance would expose or couple more than the subtype needs.
- Use polymorphism when multiple implementations genuinely honor one stable contract; do not create an interface for a single class merely to look decoupled.
- Tell collaborators what to do when that preserves their invariants; avoid reaching through several objects to assemble their state.
- Make invalid states difficult to construct when the added constraint is local and understandable.

These are heuristics, not a mandate to split every method or class. A small, explicit conditional can be clearer than a hierarchy.

## Pattern decision rule

Name the forces before naming the pattern:

1. What variation or coupling is causing pain now?
2. What must remain stable?
3. Which simpler design was considered?
4. What new indirection, lifecycle, or configuration cost will the pattern add?
5. How will a test demonstrate the intended benefit?

Use a pattern when it reduces a real, repeated design force. Do not add factories, strategies, visitors, repositories, event buses, or dependency-injection layers solely because they are familiar.

## Smells worth investigating

Treat these as clues, not automatic defects:

- a method knows too much about another object's representation;
- a change requires editing many unrelated conditionals;
- a class mixes policy with persistence, transport, formatting, or process control;
- names such as `Manager`, `Helper`, or `Utils` hide several responsibilities;
- a parameter list or boolean flag grows as variation accumulates;
- inheritance is used only to reuse implementation;
- a test needs a large object graph to prove one rule.

First improve the smallest boundary that makes the responsibility visible. Recheck the design after the next real use case; do not finish an abstraction speculatively.
