# Review, adjudication, and fixes

## Establish the target

For change workflows, record the starting baseline before implementation and review the complete task diff, including changes from every coding agent. Do not replace the baseline with an intermediate implementation or fix commit.

For standalone review, use the user's named diff, branch, commit, files, or audit scope. Otherwise inspect current staged, unstaged, and untracked changes. If there are no changes and no discernible target, ask for the target rather than silently reviewing the entire repository or an arbitrary commit.

Freeze a common target before dispatching reviewers: base/head identifiers when applicable, the working-tree patch and relevant untracked contents, and a version or snapshot identifier. HEAD alone does not identify uncommitted code. Keep writers stopped during the review, or give reviewers an immutable snapshot. If the target changes externally, reassess affected coverage and rerun invalidated reviews against the new common target.

For plan review, freeze a plan revision instead of a code diff. Resolve feedback after collecting the assigned reviewers, then obtain a targeted follow-up when material decisions change.

## Select and collect specialists

For plan review, choose categories based on evidence in the plan. For code review, ALL specialists in the catalogue are required; never omit a category, and record any that could not run as a coverage gap. Keep the individual remits narrow; do not combine categories into one general review to reduce the agent count. Reduce cost by bounding scope, not by dropping specialists.

Invoke the catalogue's named specialist for each selected category with its focused brief. Run independent reviews concurrently up to runtime capacity. Schedule remaining categories in later waves against the same frozen target. Review agents are read-only and do not recruit other reviewers or implement repairs.

**Collection barrier:** Wait for every assigned reviewer, including queued waves, before adjudicating the set or dispatching fixes. A timeout, failure, or missing response is not a clean review. Retry within budget, replace the assignment, or explicitly mark the category incomplete and report the coverage gap. Do not silently drop it.

## Adjudicate the complete set

Maintain a findings ledger with stable IDs, source category, priority, location, evidence, decision, rationale, owner, and verification status.

| Decision | Meaning |
| --- | --- |
| Accepted | Supported, within scope, and appropriate to resolve in this run |
| Rejected | Unsupported, incorrect, or an inappropriate tradeoff; explain why |
| Deferred | Valid but outside the current scope or budget; report the remaining issue |
| Duplicate | Same underlying problem as another finding; link the retained ID |

Validate feedback against the actual code, requirements, and principles. Do not accept it just because a specialist produced it, or reject it just because tests pass. Distinguish substantive design concerns from personal preferences. Resolve contradictory recommendations before assigning work; use focused investigation when evidence is insufficient.

Route out-of-category leads to their primary owner when they warrant review. Complete that investigation before dispatching fixes. Each underlying problem should have one accepted finding and a coherent repair direction.

For standalone Review mode, report assessed findings by priority with locations and rationale, rejected/deferred decisions when material, and coverage limitations. Stop without editing code unless fixes were requested.

## Dispatch fixes

After collection and adjudication, group accepted findings into cohesive tasks based on overlapping files and dependencies, rather than one agent per finding or reviewer. Dispatch `devcraft-implementer` instances using the generalist fix brief.

- Assign non-overlapping files to concurrent agents.
- Serialize shared-file changes, dependent repairs, and integration work.
- Include accepted IDs, a consistent repair direction, and verification expectations.
- Require coordinator resolution of scope changes or new design conflicts.

## Verify and stop

Inspect the integrated repairs, run appropriate checks, and send affected code to the relevant specialists for targeted follow-up (a full code review, if re-run, again uses all specialists). Evaluate repairs against the original task baseline and acceptance criteria. Include newly introduced regressions, not just whether the original lines disappeared.

Expand review coverage when repairs change boundaries, public contracts, failure behaviour, or previously unreviewed areas. Use the same collection barrier for each follow-up wave before another fix dispatch. Update each accepted finding to verified fixed or still open with supporting evidence.

Default to two fix rounds after the initial review. A round comprises a batch of accepted repairs, integration checks, and follow-up review. Honor a lower user budget and do not silently exceed an explicit cost cap. This limit does not mean that two rounds are required when the first succeeds.

Stop when accepted findings are verified resolved and relevant checks pass, or when a limit, material unresolved decision, or unavailable dependency prevents completion. In the latter case, report the task as incomplete with open finding IDs, failed or unrun checks, coverage gaps, and the next needed action. Preserve rejected and deferred decisions; do not reintroduce them in later rounds without new evidence.
