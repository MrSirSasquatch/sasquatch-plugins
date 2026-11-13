# Functions

A function should perform one coherent operation at a consistent level of abstraction. Make its inputs, outputs, and side effects understandable from its contract.

**DO:**

- Separate unrelated operations so callers can invoke one without triggering another.
- Make consequential side effects, mutation of caller-owned inputs, and required call order explicit.
- Design interfaces to prevent invalid argument combinations or handle them explicitly. Use named arguments, distinct operations, or a cohesive domain object when positional arguments or boolean modes make calls ambiguous.
- Consolidate shared business rules, or make necessary variations explicit so affected paths stay consistent.
- Use guard clauses or cohesive extraction to clarify tangled conditions and deeply nested paths.
- Extract behavior when it gives an important concept a name; keep orchestration and low-level details at clear abstraction boundaries.

**DO NOT:**

- Hide state changes behind query-like names. Operations such as `tryDequeue` can legitimately answer a question and change state when the contract exposes both.
- Combine independently meaningful responsibilities or use section comments as a substitute for cohesive operations.
- Bundle unrelated arguments into a parameter object merely to reduce the argument count.
- Add helper layers that force readers to jump between functions without adding meaning.
- Create a function per statement or eliminate all repeated syntax. Extract cohesive behavior and shared knowledge, not merely similar text.

| DO NOT | DO |
|---|---|
| `saveInvoice(invoice, true)` where `true` means send an email. | `saveInvoice(invoice, sendEmail: true)` when that mode belongs to the operation's contract. |
| A function named `calculateInvoiceTotal` also saves the invoice. | Keep calculation free of persistence; make saving an explicit operation. |
