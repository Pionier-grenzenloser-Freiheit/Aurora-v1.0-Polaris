# polaris-mvp-event-pack v1.0.0

## Kurzbefund

- Das MVP-Event-Pack enthält valide Seed-Instanzen für alle sieben freigegebenen MVP-Eventtypen.
- Polaris-Kern, freigegebenes Schema-Pack, Beispielinstanzen, `polaris-taxonomy-pack v1.0.0 baseline-ready`, `polaris-mvp-module-registry-pack v1.0.0 baseline-ready` und `polaris-mvp-policy-decision-pack v1.0.0 baseline-ready` wurden nicht verändert.

## Umfang

- `aurora.context.enriched`
- `aurora.task.planned`
- `aurora.agent.result`
- `aurora.policy.blocked`
- `aurora.feedback.received`
- `aurora.drift.detected`
- `aurora.model.promoted`

## Ableitungsregeln

- Jede Instanz folgt `mvp-event.schema.json`.
- `module_id` referenziert nur Module aus dem Module-Registry-Pack.
- `decision_ref` referenziert nur Decisions aus dem Policy-Decision-Pack.
- `actor` bleibt baseline-kompatibel als offener String.
- `risk_score` bleibt konservativ auf `open`.
- `integrity_marker` bleibt ein nicht-leerer baseline-kompatibler String.
- `input_ref` und `output_ref` sind nur Referenzen, keine Rohdaten.
- `aurora.policy.blocked` nutzt `output_ref: null` und nicht-leere `triggered_rules`.

## Validierungsstand

- Alle MVP-Event-Dateien sind RFC-8259-konformes JSON.
- Alle MVP-Event-Dateien validieren gegen `mvp-event.schema.json`.

## Freigabesatz

Der Stand ist als polaris-mvp-event-pack v1.0.0 baseline-ready abschließbar.
