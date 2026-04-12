# polaris-baseline-dependency-map v1.0.0

## Zweck

Diese Dependency-Map beschreibt die Abhängigkeiten zwischen den eingefrorenen Polaris-Baseline-Packs.

## Abhängigkeitsübersicht

| Artefakt / Pack | Baut auf | Zweck der Abhängigkeit |
|---|---|---|
| `polaris-taxonomy-pack v1.0.0` | Polaris-Kern, Kontrollvertrag, Schema-Pack | Standardisiert kontrollierte Taxonomien, ohne bestehende Schemas zu ändern. |
| `polaris-mvp-module-registry-pack v1.0.0` | `module-manifest.schema.json`, Kontrollvertrag, Taxonomy-Pack | Materialisiert 12 MVP-Module als valide Module-Manifeste. |
| `polaris-mvp-policy-decision-pack v1.0.0` | `policy-decision.schema.json`, Kontrollvertrag, Taxonomy-Pack, Module-Registry-Pack | Materialisiert die 6 kontrollierten Decision-Werte als valide Policy Decisions. |
| `polaris-mvp-event-pack v1.0.0` | `mvp-event.schema.json`, Kontrollvertrag, Taxonomy-Pack, Module-Registry-Pack, Policy-Decision-Pack | Materialisiert die 7 MVP-Eventtypen und referenziert Module sowie Decisions. |

## Referenzregeln

- `module_id`-Referenzen im MVP-Event-Pack kommen aus dem Module-Registry-Pack.
- `decision_ref`-Referenzen im MVP-Event-Pack kommen aus dem Policy-Decision-Pack.
- Das MVP-Event-Pack bildet den Event-Schnitt des aktuellen Baseline-Kerns ab.
- `actor` bleibt im Schema baseline-kompatibel als offener String.
- `risk_score` bleibt baseline-kompatibel dual modelliert; im Seed-Stand wird konservativ `open` verwendet.
- `integrity_marker` bleibt ein nicht-leerer String; kein verbindliches kryptografisches Format wird behauptet.

## Abhängigkeitskette

```text
Polaris-Kern + Kontrollvertrag + Schema-Pack
  -> polaris-taxonomy-pack v1.0.0
  -> polaris-mvp-module-registry-pack v1.0.0
  -> polaris-mvp-policy-decision-pack v1.0.0
  -> polaris-mvp-event-pack v1.0.0
  -> polaris-baseline-bundle v1.0.0
```
