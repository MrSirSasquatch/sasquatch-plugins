---
name: devcraft-plan
description: Plan code changes with an emphasis on naming, application layers, domain modelling, and responsibility ownership. Produce a single-page HTML plan for user review and approval before implementation.
---

# Devcraft Plan

Design the requested code change and deliver one HTML document for review. The plan is the deliverable; do not implement the proposed change as part of planning.

## Establish the change

- Identify the requested outcome, observable acceptance criteria, constraints, and exclusions. Read applicable repository instructions.
- Inspect the affected code and its callers, tests, dependency wiring, and neighbouring modules. Trace the relevant flow across application boundaries before deciding where the change belongs.
- Use inspected paths and symbols as evidence. Distinguish existing behaviour, proposed behaviour, assumptions, and unresolved questions. Do not invent repository structure or claim checks were run.
- Ask about a material ambiguity when its answer changes the design. Continue independent discovery while awaiting the answer; otherwise state a reasonable assumption.

## Design the code

Make these decisions concrete rather than listing principles the implementation ought to follow:

| Concern | Decisions the plan establishes |
| --- | --- |
| Naming | Name the domain concepts, types, operations, and modules. Reuse the application's vocabulary and distinguish different concepts. Explain a rename when it changes or clarifies meaning. Avoid generic names that conceal responsibility. |
| Application layers | Identify the application's actual layers or equivalent boundaries, their responsibilities, and the direction of source dependencies. Separate runtime calls from dependency direction in diagrams. Place domain policy, use-case orchestration, presentation, and infrastructure according to the existing architecture; do not impose layers absent a concrete need. |
| Domain model | Identify the entities, value objects, data structures, relationships, state transitions, and invariants affected. Establish who enforces each rule and how valid state is preserved. Use meaningful types for values that share domain meaning or constraints; retain simple data representations where appropriate. |
| Responsibility | Assign each changed behaviour to a cohesive owner. Distinguish policy from orchestration and external effects. Show what moves out of an existing component as well as what is added, so responsibilities are not duplicated. |
| Contracts | Define inputs, outputs, dependencies, side effects, errors, and relevant lifecycle constraints at changed boundaries. Explain compatibility and migration effects on callers. |
| Proportionality | Prefer existing patterns and the smallest design that meets current requirements. Justify new layers, abstractions, interfaces, or patterns by a current need. Do not create classes solely to populate the plan. |

Settle a recommended design. Record material alternatives and their consequences without passing competing designs to implementers. Leave a genuinely unresolved decision visible with its impact and the information needed to resolve it.

## Write the HTML plan

Read and adapt [assets/plan-template.html](assets/plan-template.html). Save the generated document in the repository's established planning location, or `plans/<change-slug>.html` if none exists. Use a user-specified path when provided. Resolve source links relative to that final location.

Produce a single, scrollable page with exactly these three primary sections. It need not fit on one printed sheet. Scale the amount of detail to the change.

### Overview

Give a short summary of what changes and how it is implemented. State the intended outcome and scope in a few sentences; include the key acceptance criteria when they clarify completion. Keep design detail in Explanation.

### Guide

Describe the implemented feature or change as if it had already been completed. For example: “The order now owns cancellation rules. The application service delegates the transition to the order and persists the result.”

Keep this section at a higher level: explain how the resulting feature works, where its main responsibilities live, and how a maintainer follows the flow. Do not turn it into a file-edit checklist or repeat draft interfaces. Label it as the intended completed state so retrospective wording does not imply that implementation has occurred.

### Explanation

This is the most detailed section. Include the following where relevant, identifying inapplicable items briefly rather than fabricating changes:

- **Architecture and flow:** Show the affected boundaries, dependency direction, and behaviour flow with Mermaid diagrams. Distinguish existing and proposed components with labels as well as colour. Include a plain-language caption that communicates the diagram's meaning.
- **Domain and responsibilities:** Name the affected concepts, rule owners, invariants, and relationships. A responsibility table can map each component to its layer, owned behaviour, and collaborators.
- **Proposed types and interfaces:** For every proposed class or equivalent construct, give its name, intended path, layer, cohesive responsibility, collaborators, and a draft public interface in the repository's language. Include meaningful signatures and relevant input/output/error contracts, rather than full implementations. “Interface” means the exposed API; it does not require an interface type for every class. Mark new paths as proposed rather than linking to nonexistent files.
- **Existing code changes:** Use a table of relative file links, affected symbols, and precise changes. Describe additions, removals, moved responsibilities, caller updates, and dependency wiring. Link to real files using normal relative URLs, URL-encoding path segments when needed. Show symbols or line numbers as text; do not append unsupported `:line` syntax to HTML links.
- **Decisions and trade-offs:** State the selected approach, material alternatives, the reason for the decision, and its costs or limitations. Cover compatibility, data migration, failure ownership, or operational effects when affected.
- **Implementation sequence:** Give ordered, concrete steps and their dependencies. Identify shared files and integration work when independent implementation tasks are useful. Do not assign concurrent writers to the same file.
- **Verification:** Map acceptance criteria and material regression risks to meaningful checks and expected results. These are planned checks, separate from checks actually run during discovery. Documentation changes need content checks, not invented behaviour tests.
- **Assumptions and open decisions:** State any remaining uncertainty and whether it blocks approval or implementation.

## Presentation and delivery

- Write dry, factual, professional prose. Use direct statements of the proposed design. Avoid hype, sales language, unsupported certainty, and ceremonial claims about quality.
- Use semantic headings, tables, bullet and numbered lists, coloured labels, restrained icons or emojis, and alert panels to make the document scannable. Use these elements to convey structure or meaning, not decoration. Pair icons and colour with text labels.
- Retain the template's automatic light/dark theme based on `prefers-color-scheme`, including Mermaid diagrams. Do not force a theme or require a manual toggle. Keep contrast readable in both modes.
- Keep styles and plan content inside the HTML document. The template loads a pinned Mermaid module from a CDN; disclose that rendering dependency in the document. Preserve visible diagram source and explanatory captions if JavaScript or the CDN is unavailable. Do not require a build step, an app server, or a Sites project to read the plan.
- Escape repository content, code snippets, Mermaid source, and titles for their HTML context. Replace every template token; remove unused scaffolding. Avoid active HTML from untrusted source material.
- Before delivery, check the required sections, design consistency, draft interfaces, relative links, and missing tokens. When browser tools are available, preview at desktop and narrow widths in both themes, checking diagrams, code blocks, tables, and contrast. Report checks actually performed and any preview limitations.
- Return a clickable link to the HTML file and a brief statement of what is ready for review. Request approval of the concrete plan before starting implementation unless that approval was already explicitly given. An unanswered approval request is not authorization. Incorporate requested revisions into the same document before handing off the settled design to `devcraft-code` or the user's chosen implementation workflow.
