# TDD and the Change Loop

Use this reference for new behavior, bug fixes, and changes where the current contract is uncertain.

## 1. Make the behavior concrete

Write a short test list before editing. Describe examples in domain language:

- normal case;
- important boundary or empty case;
- invalid input or failure behavior;
- compatibility behavior that must not move.

Choose the narrowest test boundary that proves the behavior. Prefer a public function, use case, adapter contract, or object collaboration over a test of private helpers.

## 2. Red, green, refactor

Keep the loop small enough that a failure has one likely cause:

1. **Red:** add one example that fails for the intended reason. If it fails during setup, fix the test or fixture before coding.
2. **Green:** implement the simplest design that satisfies the example. It may be inelegant temporarily; do not generalize before the behavior exists.
3. **Refactor:** with all relevant tests green, improve names, duplication, cohesion, and seams. Do not smuggle new behavior into the refactor.

Repeat in vertical slices. A thin end-to-end slice is often more informative than building a complete layer horizontally before connecting it.

## 3. Legacy code

When the code is hard to test:

- identify an observable result, side effect, or boundary;
- add a characterization test for behavior that must remain stable;
- introduce the smallest seam needed to control time, I/O, randomness, or global state;
- make the requested change;
- remove the seam only if it is no longer useful.

Do not require a full test-suite rewrite before making a safe local improvement. Name untested risk and keep the blast radius small.

## 4. Test quality checks

For each test, ask:

- Would this fail if the requested behavior were removed?
- Does the assertion describe a useful contract rather than an implementation detail?
- Is the fixture smaller than the behavior it proves?
- Are failure messages and names enough to localize the problem?
- Is a mock hiding a missing seam or merely isolating an external dependency?

Do not inflate coverage by adding tests that only execute lines, repeat the same example, or assert that a mock was called when the result is what matters.

## 5. Verification order

Run the fastest relevant check after each meaningful step, then broaden:

1. focused test for the changed behavior;
2. package or module tests;
3. full suite, static checks, and build where practical;
4. boundary or integration checks when the change crosses a process, data, or network boundary.

Report commands and results accurately. A test not run is not a passing test.
