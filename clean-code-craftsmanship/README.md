# Clean Code Craftsmanship

An opinionated, vendor-neutral Agent Skill for agents that work like a careful XP/OO craftsman: behavior first, tests as clients, small refactorings, clear responsibilities, and evidence-based review.

The package is deliberately pragmatic. It favors Beck/Fowler/Uncle Bob-style habits without turning any slogan, design pattern, coverage number, or formatting preference into a universal law.

## What is included

- `SKILL.md` — the concise, auto-discoverable workflow and reference router.
- `references/` — focused playbooks for TDD, object design, refactoring, review, AI-slop controls, and package conformance.
- `scripts/validate_package.py` — dependency-free structural validation.
- `apm.yml` — optional current APM metadata for package managers that support it.

## Use with a compatible agent

Treat `clean-code-craftsmanship/` as one skill directory and place it in the agent's documented skills location. The portable contract is the directory and its `SKILL.md`; the other files are supporting resources loaded when relevant.

This package does not require a particular model, IDE, shell, language, test framework, MCP server, or vendor plugin. Agents should follow the repository's local instructions and the user's request when they conflict with a general preference in this skill.

## Use with APM

`apm.yml` is optional. If using Microsoft's Agent Package Manager, run its documented install or pack command from this directory and select the target explicitly when auto-detection is not available. The manifest intentionally does not restrict targets, so the consumer can choose the runtime.

The APM manifest is not needed by a runtime that accepts a portable Agent Skills directory directly.

## Validate

From the package directory:

```text
python3 scripts/validate_package.py .
```

To validate the package and a ZIP archive:

```text
python3 scripts/validate_package.py . clean-code-craftsmanship-0.1.0.zip
```

See `references/packaging-and-conformance.md` for the standards checked and the rationale for the optional APM metadata.

## License

MIT. See `LICENSE`.
