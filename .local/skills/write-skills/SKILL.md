---
name: write-skills
description: Create, edit, or review agent skills when defining their scope, writing instructions, or improving clarity and concision.
---

# Write Skills

## Scope and Discovery

- Give each skill one clear purpose. Preserve the user's requested scope.
- Use a short, descriptive, lowercase hyphenated name matching its directory.
- Include `name` and `description` in YAML frontmatter.
- Make the description state what the skill does and when to use it. Add exclusions only to prevent likely confusion.

## Keep Instructions Concise

- Assume the agent already knows how to code and use ordinary tools. Include guidance that changes its decisions.
- Use descriptive headings and short, actionable bullets instead of large paragraphs.
- State each rule once. Remove filler, repeated advice, and speculative edge cases.
- Explain the desired outcome and essential constraints; prescribe exact steps only when correctness requires them.
- Prefer the smallest useful skill over an exhaustive manual. Avoid arbitrary word counts and mandatory sections.

## Organize Detail

- Keep the purpose, core workflow, and essential constraints in `SKILL.md`.
- Move lengthy examples, schemas, and specialized procedures into focused `references/` files.
- Link each reference where relevant and say when to read it. Load only what the task needs.
- Add `scripts/` for useful repeatable automation and `assets/` for output resources, only when needed.
- Keep simple skills self-contained; do not create empty folders or duplicate documentation.

## Review Before Finishing

- Check that the description distinguishes relevant requests from unrelated work.
- Cut anything that does not help the agent make a better decision.
- Verify frontmatter, relative links, and any scripts or commands introduced by the skill.
- Check a realistic use case and a nearby out-of-scope request against the instructions.
- Keep this repository's local authoring skills out of the APM publish list.
