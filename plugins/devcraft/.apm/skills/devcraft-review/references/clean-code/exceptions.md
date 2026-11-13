# Exceptions

Preserve useful failure context, respect the API contract, and leave resources and state in a defined condition. Apply the same principles to explicit error values in languages that use them.

**DO:**

- Handle failures at a boundary that can recover, translate them for a caller, or report them usefully. Let failures propagate when a higher boundary owns that responsibility.
- Preserve the original cause, stack information, failed operation, and safe identifying context when translating or rethrowing errors.
- Follow language idioms for cleanup and cancellation. Use transactions or explicit recovery where partial updates would violate invariants.
- Make intentional fallbacks satisfy the contract and preserve required failure visibility.
- Use result types or ordinary control flow for routine expected outcomes when the API provides them.

**DO NOT:**

- Swallow a failure, log and ignore it, or replace an unsuccessful operation with a success-like default.
- Use overly broad handlers to turn unexpected defects into routine outcomes or hide cancellation.
- Retry without respecting the failure's retry semantics and the operation's side effects.
- Expose secrets or sensitive data in error messages or logs. Keep diagnostic detail separate from safe user-facing messages.
- Catch exceptions at every layer, duplicate logs without distinct operational value, or obscure the normal path with repeated handling code.

| DO NOT | DO |
|---|---|
| Return an empty invoice collection when retrieval failed. | Propagate or explicitly represent the retrieval failure; reserve an empty collection for a successful query with no invoices. |
| In C#, use `throw exception;` to rethrow a caught exception. | Use `throw;` to preserve the original stack when rethrowing from the catch block. |
