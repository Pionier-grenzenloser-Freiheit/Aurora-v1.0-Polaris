# polaris-mvp-module-registry-pack v1.0.0

## Kurzbefund

- Das Registry-Pack enthält valide `module-manifest`-Instanzen für alle MVP-relevanten Module.
- Polaris-Kern, freigegebenes Schema-Pack, Beispielinstanzen und `polaris-taxonomy-pack v1.0.0 baseline-ready` wurden nicht verändert.

## Umfang

- `api-gateway`
- `polaris-core`
- `context-prompt-engine`
- `agent-registry`
- `policy-engine`
- `legal-compliance-assessor`
- `secure-model-releaser`
- `hitl-router`
- `audit-store`
- `knowledge-layer`
- `monitoring-hub`
- `governance-dashboard`

## Ableitungsregeln

- Jedes Manifest folgt `module-manifest.schema.json`.
- `module_type` ist baseline-kompatibel zum Taxonomy-Pack gewählt.
- `allowed_connectors` ist ohne operative Freigabebasis auf `[]` gesetzt.
- `policy_profile` ist konservativ auf `open` gesetzt.
- Review-Regeln decken Confidence-Schwelle und Policy-Verstoß ab.
- Outputs sind audit-referenzierbar und enthalten mindestens ein Pflichtfeld.

## Validierungsstand

- Alle Manifest-Dateien sind RFC-8259-konformes JSON.
- Alle Manifest-Dateien validieren gegen `module-manifest.schema.json`.

## Freigabesatz

Der Stand ist als polaris-mvp-module-registry-pack v1.0.0 baseline-ready abschließbar.
