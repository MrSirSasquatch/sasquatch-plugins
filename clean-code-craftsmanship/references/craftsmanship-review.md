# Craftsmanship Review

Use this reference when reviewing a change or preparing a self-review. Review the behavior and design, not the author's intelligence or the amount of code produced.

## Review order

1. **Intent:** Does the diff implement the stated behavior and avoid unrelated scope?
2. **Correctness:** Check normal, boundary, invalid, failure, retry, concurrency, and compatibility paths relevant to the change.
3. **Tests:** Do tests prove the contract at a useful boundary? Are they deterministic, focused, and capable of failing for a plausible regression?
4. **Design:** Are responsibilities, names, coupling, cohesion, dependency direction, and error ownership clear?
5. **Maintainability:** Does the next change have an obvious home? Is duplication either removed or intentionally tolerated?
6. **Operational impact:** Consider performance, observability, security, data migration, rollout, and rollback when relevant.

## Findings

Only report an issue when you can explain the consequence and point to evidence. Use severity proportionately:

- **Blocking:** likely correctness, security, data-loss, compatibility, or operability defect; or missing verification for a high-risk path.
- **Should fix:** meaningful design or test weakness that will make the next change harder or regression likely.
- **Nit:** optional clarity or style improvement with no material risk. Keep these scarce.

For each finding include:

- location or symbol;
- observed behavior or code fact;
- why it matters;
- a focused remedy or question.

Do not hide blockers among a long list of nits. If there are no findings, say what was checked and what remains unverified.

## Reviewer's restraint

Do not demand a pattern, abstraction, coverage percentage, or test style solely as a matter of taste. Do not rewrite the change while reviewing it unless the user asks for implementation. Distinguish a real defect from a preference, and preserve local conventions when they do not create risk.

End with a clear verdict such as **Ready to ship**, **Address blockers then ship**, or **Needs another pass**, plus the verification evidence.
