# Agent invocation and model controls

Read this once before dispatching workers. The coordinator owns selection, scheduling, collection, adjudication, and integration. Named agents supply focused role instructions; APM deploys their definitions rather than executing the workflow.

## Invoke a named agent

Use the runtime's agent inventory and delegation API to select the exact catalogue name, such as `devcraft-naming` or `devcraft-implementer`. Supply the relevant [assignment brief](agent-briefs.md). A task label containing an agent name does not load a custom definition.

APM sources live in `.apm/agents/*.agent.md` and are included alongside the devcraft skill in the package manifest. For the configured project targets, APM deploys them as follows:

| Target | Agent definition |
| --- | --- |
| Codex | `.codex/agents/devcraft-<role>.toml` |
| Claude | `.claude/agents/devcraft-<role>.md` |
| Copilot | `.github/agents/devcraft-<role>.agent.md` |

User-scope installation locations can differ. Discover the actual installed inventory rather than assuming the project directory. See [APM's agent format and target transforms](https://microsoft.github.io/apm/producer/author-primitives/instructions-and-agents/#agents).

If the runtime can spawn agents but cannot select named definitions, locate the definition through the installed agent inventory or an accessible source package's `.apm/agents/` directory. Supply its role body, the common contract, and the focused assignment to a fresh agent. For a Codex TOML definition, the body is `developer_instructions`; YAML frontmatter or TOML keys are configuration, not prompt instructions. Reapply supported settings through actual launch controls. Report this as an agent using the role instructions, not as native named invocation. Workers must not load the orchestration skill and restart its workflow.

If a required definition or contract cannot be accessed, report the missing role or coverage instead of substituting an unfocused review. If delegation itself is unavailable, the coordinator uses sequential implementation and read-only category passes as described in the entry point, without claiming independent agents.

## Select models and effort

Prefer a supported lightweight model at high effort for implementation, fixes, and specialist review: use Terra or Luna when the runtime offers them, otherwise a supported lightweight alternative. Resolve the actual runtime identifiers and honor explicit user choices and cost limits.

The shared definitions contain `name`, `description`, and `model_reasoning_effort: high`. They deliberately omit `model`: APM passes model identifiers through without translating them between providers. A model available in Codex is not thereby available in Claude or Copilot.

For Codex, APM exports the effort field as a native top-level agent TOML setting. For other targets, its presence in copied frontmatter does not establish effort support; use that runtime's supported controls. Set model and effort overrides when launching the selected role if available, and record settings actually used. See [APM's frontmatter translation contract](https://microsoft.github.io/apm/producer/author-primitives/instructions-and-agents/#frontmatter-1).

If named invocation prevents selecting the preferred model but fresh-agent launch allows it, use the role-body fallback above with the supported model controls. Otherwise disclose the inherited or available model and unsupported effort preference. Do not silently exceed a user budget, claim settings merely mentioned in a prompt were applied, or edit source/global agent configuration just to change one task's model.

## Review permissions and references

Review agents are instructed to be read-only. Apply runtime-enforced read-only tools or sandbox controls when available. Shared definitions omit a `tools` whitelist because APM does not preserve those restrictions in its Codex export; do not treat a role prompt as an enforced permission boundary.

Agent bodies use the contract and craftsmanship sections supplied in the assignment or read the applicable sections in the installed devcraft skill. Resolve paths such as `references/agent-briefs.md` from the skill's actual directory rather than the agent file. This avoids relying on relative links inside generated Codex agent instructions, which APM 0.35.0 does not rewrite. Supply excerpts if the worker cannot access the installed skill files. Keep the detailed guidance and schemas in the shared references.

The coordinator catalogue identifies agents by name rather than linking to source filenames: bundle installation changes their locations and extensions. Keep skill references inside the skill bundle so they remain valid after deployment. Verify deployed agents and skill references after changing packaging. See [APM package-relative links](https://microsoft.github.io/apm/producer/package-relative-links/).

With APM 0.35.0, for all three targets declare the source package in the consumer's `dependencies.apm`, then run `apm install --target claude,codex,copilot`. Checkout deployment also works by running that command from the source package directory. Passing a source directory with a root `plugin.json` as a positional install argument can misclassify it as a bundle and bypass agent transforms.

APM 0.35.0's `agent-plugin` pack format rejects agents. Its `claude-plugin` bundle preserves agents and installs Claude and Copilot Markdown, but bundle installation copies YAML/Markdown into Codex `.toml` files without conversion. Do not treat that bundle as a complete three-target installation. Parse the actual Codex output as TOML and validate each receiving runtime's native agent inventory; a successful copy does not establish valid agents or native model execution.
