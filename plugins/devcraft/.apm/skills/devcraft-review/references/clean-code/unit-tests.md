# Unit Tests

Write fast, repeatable tests of observable behavior that protect the changed contract against regressions.

**DO:**

- Cover material success, boundary, failure, and cleanup cases affected by the change.
- Assert the required outcome so a test fails when the behavior it claims to verify is broken.
- Make test names, setup, and assertions communicate the behavior and expected result. Keep arrange, act, and assert discernible without requiring labels on trivial tests.
- Control time, randomness, and shared state. Keep tests independent of execution order and live services.
- Mock at meaningful boundaries and ensure test doubles honor the real dependency's relevant contract. Use integration tests when the contract depends on real components interacting.
- Use meaningful test values and assertions that identify what went wrong. Multiple assertions are appropriate for one coherent behavior.
- Use Arrange, Act and Assert comments to help readers identify the structure of a test
- Keep arrange code of tests simple and readable. Extract complicated test setups out into helper methods. An arrange that changes a property on a mock or fake shows intent that this precondition is part of the test but this is only easily visible without complicated arrange code cluttering the test method.

**DO NOT:**

- Remove or weaken assertions to accommodate a defect rather than an intentional contract change.
- Check only that a mock was called when the returned result is the requirement.
- Over-mock so the test bypasses the behavior it should verify, or bind tests to private methods and incidental call sequences.
- Cover unrelated behaviors in one test or add irrelevant setup to shared fixtures.
- Rely on arbitrary sleeps or equate a coverage percentage with useful regression protection.
- Require unit tests for documentation-only or purely mechanical edits.

| DO NOT | DO |
|---|---|
| Verify only that the repository was called in a test of an invoice total. | Assert the expected total returned by the operation under test. |
| Wait for a real deadline with a sleep. | Advance a controlled clock to exercise the deadline deterministically. |
