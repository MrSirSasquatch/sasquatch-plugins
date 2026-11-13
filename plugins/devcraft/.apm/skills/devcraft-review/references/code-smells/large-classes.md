# Large Classes (God Classes)

A class should have a cohesive responsibility, protect the invariants it owns, and expose an interface suited to its callers. Organize it around responsibilities and coupling, not raw size.

**DO:**

- Keep related behavior and state together with clear ownership, lifecycle, and invariant protection.
- Separate unrelated responsibilities when changing one could break another or their state and dependencies can be isolated meaningfully.
- Use groups of methods that operate on separate fields or change for distinct reasons as signals to examine responsibility boundaries.
- Keep dependencies and public operations aligned with the class's purpose.
- Put rules with a cohesive collaborator that owns them instead of making callers navigate internals or duplicate those rules.

**DO NOT:**

- Accumulate unrelated concerns and dependencies in one class or leave state ownership ambiguous.
- Require callers to understand internal representation to use the class safely.
- Split a cohesive class solely to reduce its field or method count, or create a service for every operation.

| DO NOT | DO |
|---|---|
| Make one class own invoice rules, SMTP connections, and PDF layout details. | Keep invoice rules cohesive and delegate email transport and document rendering to collaborators with clear responsibilities. |
| Move fields into a helper while leaving all their rules in the original class. | Move related state and behavior together so the new boundary has meaningful ownership. |
