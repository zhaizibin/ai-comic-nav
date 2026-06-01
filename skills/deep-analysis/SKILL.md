---
name: deep-analysis
description: Structured deep analysis workflow for complex events, decisions, narratives, strategies, and forecasts. Use when the user asks for deep analysis, structural analysis, root-cause analysis, incentive mapping, game-theory reasoning, probability estimates, narrative/fact separation, anomaly analysis, cross-domain comparison, counterargument testing, or consistency auditing. The skill helps Codex separate evidence from inference, choose the right method path, and produce falsifiable, uncertainty-aware conclusions.
---

# Deep Analysis

Use this skill to analyze complex questions with explicit structure instead of free-form opinion. Treat the workflow as a reasoning scaffold, not as a source of facts.

## Operating Rules

1. Separate verified facts, reported claims, interpretations, and hypotheses.
2. Mark uncertainty and evidence gaps instead of filling them with invented detail.
3. Prefer structural incentives, causal mechanisms, and observable behavior over claims about hidden intent.
4. Use probability ranges only when the question involves prediction or uncertain judgment, and name the drivers behind the range.
5. Test the strongest counterargument before finalizing the conclusion.
6. If current or high-stakes facts matter, verify them with appropriate sources before analysis.

## Method Router

| Need | Method |
| --- | --- |
| Sources conflict or narrative is messy | `methods/00-layered-information.md` |
| Something feels inconsistent or unusual | `methods/01-anomaly-first.md` |
| Incentives, beneficiaries, or power structure matter | `methods/02-interest-structure.md` |
| The user asks why or how a result happened | `methods/03-causal-mechanism.md` |
| A pattern may transfer across domains | `methods/04-cross-domain.md` |
| Multiple actors make interdependent choices | `methods/05-game-theory.md` |
| The answer involves prediction or likelihood | `methods/06-probability-anchoring.md` |
| A conclusion needs stress testing | `methods/07-devil-advocate.md` |
| The analysis may contain contradictions or drift | `methods/08-consistency-audit.md` |

## Default Workflow

For broad "deep analysis" requests:

1. Load `00-layered-information.md` if the input has multiple claims, sources, or narratives.
2. Load `01-anomaly-first.md` to identify the highest-leverage anomaly or tension.
3. Load `03-causal-mechanism.md` to trace mechanisms and structural constraints.
4. Load `02-interest-structure.md` or `05-game-theory.md` when actors and incentives drive the outcome.
5. Load `04-cross-domain.md` when analogies can test or refine the mechanism.
6. Load `07-devil-advocate.md` to attack the strongest assumption.
7. Load `06-probability-anchoring.md` for any forecast.
8. Load `08-consistency-audit.md` before final output.

## Output Shape

Prefer this compact structure unless the user asks for another format:

```text
Bottom line
Evidence map
Key anomaly or tension
Causal / incentive structure
Competing hypotheses
Counterargument and failure mode
Probability or confidence, when relevant
What would change the conclusion
```
