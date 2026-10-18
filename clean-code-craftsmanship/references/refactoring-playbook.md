# Refactoring Playbook

Use this reference for structural changes that should preserve behavior.

## Safety rule

Refactoring changes the shape, not the externally observable behavior. Keep the test suite green between small transformations. If behavior must change too, separate the steps or state exactly why they cannot be separated.

## A practical sequence

1. Establish a focused safety net or characterization test.
2. Make one named transformation.
3. Run the focused test and relevant static checks.
4. Inspect the diff for accidental behavior or scope expansion.
5. Repeat, then run broader verification.

Commit or checkpoint at a boundary that makes rollback meaningful when the repository workflow permits it.

## Common transformations

| Signal | First transformation to consider | Proof to preserve |
| --- | --- | --- |
| A name requires explanation | Rename variable, method, or type | Behavior and public API, unless intentionally changed |
| A method mixes levels of detail | Extract method around one decision or side effect | Inputs, outputs, and error behavior |
| A class has unrelated reasons to change | Extract a cohesive collaborator | Collaboration and ownership of invariants |
| Several branches repeat the same operation | Extract the common operation or introduce a small value object | Branch-specific behavior |
| A flag changes the meaning of a call | Replace with a named operation or value type | Default and failure behavior |
| A parameter bundle travels together | Introduce a parameter object only if it has a coherent concept | Validation and serialization |
| Variation is real and repeated | Introduce a stable interface or strategy | Contract tests across implementations |
| A conditional is complex and stable | Move the decision next to the data or use a polymorphic value | All branches and fallback behavior |

## Refactoring under pressure

When the task is urgent, prioritize changes that reduce risk immediately: clarify a name, isolate an external effect, remove a duplicated bug-prone rule, or add a characterization test. Avoid broad architectural replacement, formatting churn, or framework migration disguised as a fix.

## Completion check

Before calling a refactor done, compare the before and after behavior, public surface, dependency direction, test readability, and diff size. If the design became more abstract but not easier to change or explain, revert the abstraction and keep the simpler shape.
