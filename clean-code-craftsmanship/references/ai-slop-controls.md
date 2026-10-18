# AI-Slop Controls

Use this reference when generated code is broad, generic, over-engineered, or difficult to trust. The remedy is observable engineering discipline, not distrust of every generated line.

## High-signal warning signs

- code was added without a failing example or an explicit behavior contract;
- a small request changed many files, introduced a framework, or created several layers;
- interfaces, factories, adapters, or configuration were added before a second implementation existed;
- tests assert private calls, mirror the implementation, or pass for the wrong reason;
- comments explain confusing code instead of improving the code;
- names are vague, repeated boilerplate is everywhere, or error handling is generic;
- dead branches, unused parameters, speculative options, and duplicate utilities remain;
- the diff is formatted or regenerated so heavily that the behavioral change is hard to inspect;
- verification is reported as "should pass" rather than backed by executed checks.

## Controls

1. Restate the behavior and non-goals in one or two sentences.
2. Set a change budget: smallest relevant files, one behavior at a time, no unrelated cleanup.
3. Ask for a test that would fail before the implementation. In legacy code, add characterization coverage first.
4. Search for an existing concept before introducing a type, helper, or dependency.
5. Prefer the simplest design that supports the current evidence. Defer extension points until a second real use case or a clear boundary justifies them.
6. Read every changed line. Remove generated boilerplate, unused options, duplicate validation, and comments that no longer add information.
7. Run the focused and broader checks; inspect warnings and failures instead of weakening assertions.
8. Explain any remaining uncertainty, untested path, or intentional compromise.

## A useful challenge

For each new abstraction, answer: “What concrete problem does this solve today, what code becomes simpler because of it, and what test proves the benefit?” If the answer is vague, keep the code local and explicit.
