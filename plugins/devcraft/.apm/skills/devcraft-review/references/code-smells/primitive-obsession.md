# Primitive Obsession

Primitive values are appropriate for simple data and boundaries. Use a domain type when a primitive conceals meaningful constraints, units, identity, or behavior that callers must repeatedly reconstruct.

**DO:**

- Represent meaningful invariants or operations with a small domain type when it improves safety or clarity.
- Distinguish identifiers and units when using interchangeable primitives would permit incorrect use.
- Validate at the appropriate boundary and preserve the valid state the code relies on.
- Centralize repeated parsing, formatting, validation, and conversion for the same concept.
- Make domain meaning explicit when values cross boundaries.

**DO NOT:**

- Rely on callers to reconstruct hidden constraints or apply duplicated validation and conversion rules consistently.
- Allow a representation to admit invalid states that the code assumes cannot occur.
- Wrap every string, number, or boolean. Keep primitives when their meaning is obvious, constraints are trivial, and a type would add indirection without improving safety or clarity.

| DO NOT | DO |
|---|---|
| Pass a timeout as an unqualified integer while callers repeatedly convert between seconds and milliseconds. | Use a duration type such as `TimeSpan`, converting to the required unit at the external boundary. |
| Wrap a simple display label in a domain type solely because it is a string. | Keep the string when a meaningful name already communicates its purpose and no additional invariant needs protection. |
