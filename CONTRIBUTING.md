# Contributing

Contributions are welcome, especially examples, method refinements, validation checks, and translations.

## Good Contributions

- Add realistic examples that show the workflow on a bounded problem.
- Improve method wording so it is more evidence-aware and easier for an AI agent to follow.
- Add checks that catch broken skill metadata or stale method links.
- Propose new methods with a clear trigger, input, output, and failure mode.

## Method Design Rules

- Separate evidence from inference.
- Prefer falsifiable hypotheses over confident speculation.
- Include counterarguments and uncertainty when evidence is incomplete.
- Avoid claims about hidden intent unless the evidence and inference chain are explicit.

## Pull Request Checklist

- Run `python scripts/validate_skill.py`.
- Keep `skills/deep-analysis/SKILL.md` concise.
- Put detailed method instructions in `skills/deep-analysis/methods/`.
- Update examples when behavior changes.
