# Classes

Give each class a cohesive single responsibility, protect its invariants, and expose a small interface suited to its callers.

**DO:**

- Establish valid state during construction and control mutations that could violate invariants.
- Keep responsibilities and dependencies aligned with the class's purpose. Separate unrelated reasons to change.
- Put domain rules with the object that owns them rather than making callers navigate object graphs and reconstruct those rules.
- Preserve the base type's promised behavior in subtypes, including accepted inputs and observable effects.
- Prefer composition when inheritance mainly shares implementation and creates an awkward behavioral relationship.
- Isolate volatile infrastructure behind meaningful boundaries when direct coupling obstructs testing or routine change.

**DO NOT:**

- Expose mutable state that lets callers break invariants or require callers to understand internal representation to use a class safely.
- Introduce shared mutable or global state that creates hidden coupling between otherwise independent instances.
- Add abstractions, interfaces, or design patterns without a current problem they solve.
- Mechanically wrap every dependency or primitive, or require behavior on every data structure. Records, DTOs, and boundary representations can legitimately expose data.

| DO NOT | DO |
|---|---|
| Let callers set an order's status to shipped without satisfying its shipping rules. | Expose an operation such as `order.ship()` that enforces those rules. |
| Add `IInvoiceFormatter` solely because every class is expected to have an interface. | Introduce an interface when it protects a real boundary or supports required implementations. |
