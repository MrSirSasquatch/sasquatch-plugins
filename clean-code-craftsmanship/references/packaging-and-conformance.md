# Packaging and Conformance

This file is maintainer documentation, not part of the normal coding workflow. Read it when publishing or adapting the package.

## Portable Agent Skills contract

The package follows the current Agent Skills specification at <https://agentskills.io/specification>:

- the package is a directory with exactly one required `SKILL.md` entrypoint;
- the frontmatter contains `name` and `description` and uses a lowercase hyphenated name matching the directory;
- `references/` contains focused material loaded on demand;
- the body links references with relative paths one level below `SKILL.md`;
- no client-specific tool permissions are required by the core skill.

The main entrypoint is intentionally concise. The detailed methods are separate so a compatible agent can discover the skill cheaply, activate the short workflow, and load only the route it needs.

## Optional APM layer

`apm.yml` is optional metadata for Microsoft's Agent Package Manager. It is not required by the portable Agent Skills format. It declares the package as a `skill`, uses `includes: auto`, and leaves targets unspecified so a consumer can select a runtime explicitly or let APM detect one.

The manifest deliberately omits a `$schema` URL. APM's current documentation distinguishes its working-draft manifest from an explicit OpenAPM v0.1.41 schema opt-in; omitting `$schema` avoids falsely pinning this package to a schema revision while retaining the required `name` and `version` fields. If a publishing pipeline requires a pinned schema, validate against the current APM schema and update this note with the chosen revision.

The portable skill remains usable without APM. Do not copy `apm.yml` into a runtime that expects only a skill directory unless that runtime documents support for it.

## Packaging choices

- `README.md` documents installation and scope for humans.
- `scripts/validate_package.py` performs dependency-free structural validation and can inspect a ZIP archive.
- `LICENSE` makes the distribution terms explicit.
- There is no `plugin.json` or vendor-specific `agents/openai.yaml` in the core package. Those are adapter formats, not part of the cross-agent skill contract.

Verified against the Agent Skills specification and APM references on 2026-10-19. Standards and tooling can change; rerun the validator and recheck the linked sources before publishing a new release.
