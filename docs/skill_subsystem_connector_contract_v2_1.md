# v2.1 – Skill Subsystem + Connector Contract

Diese Sektion regelt Beschreibung, Ausführung, Abbildung, Auditierbarkeit der Skills und garantiert Kompatibilität zu:
- VS Code Skill Loader / Indexer
- deterministischer Container-Execution
- Cloud-Skill-Registries (Vendor/Custom)
- Aurora-interner Orchestrierung

Leitsatz:
Skills sind deterministische, isolierte Recheneinheiten. Alle Nebenwirkungen und Credentials verbleiben im Connector; Verstöße sind auditierbar.

## Mapping-Tabelle: local | cloud ↔ VS Code ↔ Cloud Registry

| Execution Mode | VS Code Location | Cloud Registry Entry | Notizen |
|---|---|---|---|
| local | .github/skills/<skill_dir>/SKILL.md | none | nur lokal, CI-validierbar |
| cloud (custom) | n/a | type=custom, skill_id, version | Mapping via Connector |
| cloud (vendor) | n/a | type=vendor, skill_id, version | Vendor-Skill (vorab geprüft) |

## Hard Constraints (Non-Negotiable)

- Skill-Container: kein Netzwerk, keine Runtime-Installationen, frischer Container je Request.
- Secrets-Policy: keine Tokens/Secrets im Skill-Container; Connector hält Credentials.
- Audit-Kette: jede Skill-Exec + jeder Tool-Call bekommt trace_id + audit_id + Signatur.
