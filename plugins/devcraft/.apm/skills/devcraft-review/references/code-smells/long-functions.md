# Long Functions

A function should express one coherent operation at a consistent level of abstraction. Keep meaningful decisions, responsibilities, and important paths visible.

**DO:**

- Extract cohesive operations with meaningful names when distinct steps or mixed abstraction levels obscure the main flow.
- Separate unrelated responsibilities so callers can use or change one without unintentionally affecting another.
- Simplify nested branches and tangled control flow so normal and failure paths are understandable and verifiable.
- Consolidate shared decision logic so affected paths apply the same rules consistently.
- Make inputs, outputs, and side effects understandable as one contract. Separate orchestration from detailed work when it clarifies responsibility or enables focused testing.

**DO NOT:**

- Hide important failure paths or independently meaningful responsibilities inside a long sequence of implementation details.
- Split a straightforward sequence into tiny helpers merely to reduce line count. Keep closely related steps together when extraction would obscure behavior.

| DO NOT | DO |
|---|---|
| Bury invoice validation, total calculation, and persistence details in one deeply nested function. | Keep the main flow readable through cohesive operations such as `validateInvoice`, `calculateInvoiceTotal`, and `saveInvoice`. |
| Extract each assignment into a helper to meet a line-count limit. | Keep a clear, cohesive sequence together regardless of its line count. |
