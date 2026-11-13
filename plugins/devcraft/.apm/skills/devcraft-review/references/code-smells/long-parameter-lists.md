# Long Parameter Lists

Make an operation's required inputs clear and safe to provide. Communicate intent at the call site and represent cohesive concepts explicitly where useful.

**DO:**

- Use named arguments or distinct domain types when similar positional values are easy to confuse by order, meaning, or unit.
- Prevent invalid argument combinations or handle them explicitly.
- Represent related inputs with a cohesive domain object or options type when it clarifies their shared meaning.
- Use separate operations when boolean or nullable mode parameters select substantially different contracts.
- Keep independent, genuinely required inputs explicit rather than hiding them in ambient state or inappropriate optional defaults.

**DO NOT:**

- Require readers to remember the meaning or order of ambiguous arguments.
- Bundle unrelated values into a parameter bag merely to shorten the signature.
- Replace clear, explicit parameters solely to meet an argument-count limit.

| DO NOT | DO |
|---|---|
| `transferFunds(firstAccountId, secondAccountId, amount)` when the direction is unclear. | `transferFunds(sourceAccountId: firstAccountId, destinationAccountId: secondAccountId, amount: amount)`. |
| Combine unrelated dependencies and request values in a generic `OperationParameters` object. | Keep independent inputs explicit; group only values that form a meaningful concept. |
