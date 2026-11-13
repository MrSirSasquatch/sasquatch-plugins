# Comments

Use comments to preserve reasoning, constraints, and contracts that the code alone cannot communicate clearly.

**DO:**

- Explain non-obvious ownership, side effects, units, ordering constraints, algorithms, and protocol requirements where callers or maintainers need them.
- Document the rationale, external constraint, and removal condition for a workaround when relevant.
- Keep comments and API documentation consistent with behavior; update adjacent comments when behavior changes.
- Follow language and repository conventions for documentation comments.

**DO NOT:**

- Paraphrase obvious statements, explain a misleading name instead of fixing it, or repeat facts already clear from names and types.
- Use comments to excuse a known correctness defect instead of fixing it or explicitly defining the unsupported behavior.
- Leave commented-out code, change histories, or stale TODOs in active code. Use version control and actionable tracking.
- Treat documentation comments as subject to a blanket ban on describing behavior.

| DO NOT | DO |
|---|---|
| `retryCount++; // Increment retry count` | Let the statement speak for itself. |
| `// Wait before retrying` when the reason for the delay matters. | `// The provider requires at least one second between retry attempts.` when that is the actual constraint. |
