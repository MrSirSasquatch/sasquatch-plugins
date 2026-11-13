# Applying the Code Smell Prevention Practices

Apply these practices when writing, changing, and reviewing code to prevent long functions, god classes, unclear parameter lists, data clumps, and primitive obsession. Apply them to new and changed code, including existing code whose behavior the change affects.

Write code that follows these practices. When reviewing code, flag anything that does not adhere to them. For each finding, identify the location, the practice not followed, the consequence, and the smallest useful correction. Make findings specific and verifiable. Avoid speculation and duplicate findings for the same underlying issue.

Apply the practices strictly, but in context, including the qualifications in each topic. Established language idioms and repository conventions can meet their intent without matching an example literally. If a necessary tradeoff departs from a practice, explain the reason and remaining risk rather than silently treating it as compliant.

Treat size, repetition, and primitive types as investigation signals, not automatic violations. A structure that resembles a named smell can still be clear and cohesive. Do not require unrelated refactoring, introduce abstractions for hypothetical reuse, or prescribe arbitrary line, field, or argument-count thresholds.

## Topics

- [Long Functions](long-functions.md)
- [Large Classes (God Classes)](large-classes.md)
- [Long Parameter Lists](long-parameter-lists.md)
- [Data Clumps](data-clumps.md)
- [Primitive Obsession](primitive-obsession.md)
