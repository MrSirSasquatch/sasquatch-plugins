# Data Clumps

Repeated groups of values may represent one concept with shared meaning, validation, or behavior. Establish that relationship before introducing a new type.

**DO:**

- Identify related values that repeatedly travel together through signatures, return values, or fields and require callers to keep them aligned.
- Introduce a cohesive value object when it names a real domain concept or protects a shared invariant.
- Centralize shared validation and behavior so affected paths cannot apply inconsistent rules.
- Keep values with a shared lifecycle consistent when passing, storing, or updating them.

**DO NOT:**

- Make callers repeatedly reconstruct a domain concept from separately handled values and duplicated rules.
- Create a type solely because values appear together once, or combine values whose relationship is incidental.

| DO NOT | DO |
|---|---|
| Pass `startDate` and `endDate` separately through many operations, each implementing its own date-order validation. | Use a `DateRange` value object that enforces the shared ordering rule. |
| Group `customerId` and `retryCount` because they appear in the same call. | Keep them independent when they have no shared meaning, lifecycle, or invariant. |
