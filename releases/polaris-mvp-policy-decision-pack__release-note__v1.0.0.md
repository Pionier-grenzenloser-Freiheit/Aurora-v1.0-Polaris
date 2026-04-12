# polaris-mvp-policy-decision-pack v1.0.0

## Kurzbefund

- Das Policy-Decision-Pack enthält valide Seed-Instanzen für alle sechs kontrollierten Decision-Werte.
- Polaris-Kern, freigegebenes Schema-Pack, Beispielinstanzen, `polaris-taxonomy-pack v1.0.0 baseline-ready` und `polaris-mvp-module-registry-pack v1.0.0 baseline-ready` wurden nicht verändert.

## Umfang

- `allow`
- `block`
- `require_human_review`
- `escalate`
- `promote`
- `rollback_candidate`

## Ableitungsregeln

- Jede Instanz folgt `policy-decision.schema.json`.
- `policy_pack` bleibt konservativ auf `open`.
- `severity` nutzt baseline-kompatible Werte aus dem Taxonomy-Pack.
- `triggered_rules` ist nie leer.
- `requires_human_review` ist je Decision-Fall konservativ gesetzt.
- Subjects beziehen sich auf ableitbare Modulaktionen oder Release-Schritte aus Registry und Kontrollvertrag.

## Validierungsstand

- Alle Policy-Decision-Dateien sind RFC-8259-konformes JSON.
- Alle Policy-Decision-Dateien validieren gegen `policy-decision.schema.json`.

## Freigabesatz

Der Stand ist als polaris-mvp-policy-decision-pack v1.0.0 baseline-ready abschließbar.
