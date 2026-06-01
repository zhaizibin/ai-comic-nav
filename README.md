# Deep Analysis

Deep Analysis is an open-source Codex skill for structured analysis of complex questions. It turns an ambiguous topic, event, decision, or narrative into a disciplined workflow: separate facts from narratives, identify anomalies, trace causal mechanisms, map incentives, test counterarguments, and attach confidence or probability estimates when prediction is involved.

The method is designed for analysts, maintainers, writers, researchers, and AI-agent users who need reusable reasoning scaffolds instead of one-off opinions.

## What It Does

- Separates facts, narratives, interpretations, and meta-interpretations.
- Finds high-leverage anomalies before applying a framework.
- Traces causal mechanisms from surface events to structural constraints.
- Maps incentives and multi-party strategic interactions.
- Uses cross-domain comparison to test whether a pattern generalizes.
- Requires counterarguments and failure modes before final conclusions.
- Uses probability ranges for forecasts and other uncertain judgments.

## Repository Layout

```text
skills/deep-analysis/
  SKILL.md
  methods/
    00-layered-information.md
    01-anomaly-first.md
    02-interest-structure.md
    03-causal-mechanism.md
    04-cross-domain.md
    05-game-theory.md
    06-probability-anchoring.md
    07-devil-advocate.md
    08-consistency-audit.md
  agents/openai.yaml
examples/
scripts/
```

## Install

### Codex CLI

Copy `skills/deep-analysis` into your Codex skills directory:

```powershell
# Windows (PowerShell)
Copy-Item -Recurse .\skills\deep-analysis $env:USERPROFILE\.codex\skills\
```

```bash
# macOS / Linux
cp -r skills/deep-analysis ~/.codex/skills/
```

Restart Codex so the skill metadata can be discovered.

### Other AI agents

The skill files are platform-agnostic Markdown + YAML. You can load `SKILL.md` and `methods/*.md` into any agent that supports structured instruction files (Cline, OpenAI Agents SDK, custom workflows).

### Validate installation

```bash
python scripts/validate_skill.py
```

Should print `Deep Analysis skill validation passed.`

## Example Prompts

```text
Use Deep Analysis to analyze why this product launch failed.
```

```text
Use Deep Analysis to separate facts from narrative in this announcement, then estimate the probability that the policy is implemented within 12 months.
```

```text
Apply the counterargument and consistency audit methods to this draft strategy memo.
```

## Method Boundary

Deep Analysis is a reasoning workflow, not an evidence source. It should not invent facts, hidden motives, or probabilities without support. When evidence is missing, the skill should label claims as assumptions, hypotheses, or unknowns.

## Maintenance Status

This is an early-stage open-source project. The first public release focuses on a compact 9-method version of the original framework. Additional methods from the extended version are tracked as future work.

## License

MIT
