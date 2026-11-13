# Meaningful Names

Names must reveal intent, distinguish concepts, and reflect behavior. Apply this to variables, parameters, fields, functions, classes, namespaces, directories, projects, and solutions.

**DO:**

- Name the domain entity, purpose, or role, not merely its technical category. Preserve meaningful domain qualifiers through parameters, fields, and local aliases.
- Make the represented concept apparent at the point of use without requiring readers to navigate to a declaration or use IDE hover. A nearby type declaration alone does not justify discarding useful domain meaning.
- Distinguish different concepts and use consistent vocabulary for the same concept across boundaries. Make any necessary translation explicit.
- Include relevant units and make names agree with values, conditions, and effects.
- Use verbs for operations and clear conditions for booleans. Use established domain terms rather than inventing abbreviations.

**DO NOT:**

- Replace a specific concept with generic names such as `settings`, `options`, `data`, `temp`, `manager`, `process`, or `result` when that removes useful meaning.
- Misrepresent behavior, such as naming a mutating operation `isValid`, or store milliseconds in a value named `timeoutSeconds`.
- Make readers decode unexplained abbreviations, numeric suffixes, type encodings, redundant prefixes, or double negatives.
- Give public APIs or shared domain concepts names that require inspecting implementation details to understand their purpose.

Use the shortest name that preserves useful meaning, not the shortest possible name. Short conventional names are appropriate when their meaning is immediately apparent in a small scope, such as a simple lambda parameter. Do not mechanically repeat an enclosing type's name or add words that provide no useful distinction.

**DO NOT:**

```csharp
var settings = options.Value;
```

**DO:**

```csharp
var organisationApiSettings = organisationApiOptions.Value;
```

The improvement is preserving which configuration both identifiers represent, not replacing `var` or merely making names longer.
