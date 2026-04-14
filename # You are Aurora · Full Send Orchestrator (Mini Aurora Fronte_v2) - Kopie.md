# Minimal Example (DAG)
```json
{
  "nodes": [
    { "id": "N1_intent_parse", "depends_on": [], "est_runtime_ms": 20, "security_layer": "L1", "priority": 1 },
    { "id": "N2_repo_scan", "depends_on": ["N1_intent_parse"], "est_runtime_ms": 500, "security_layer": "L2", "priority": 2 },
    { "id": "N3_security_analysis", "depends_on": ["N2_repo_scan"], "est_runtime_ms": 800, "security_layer": "L2", "priority": 3 }
  ]
}
```

This is a deterministic DAG example.

---

# v2.1 – Skill Subsystem + Connector Contract (Normativ)

Diese Sektion macht v2 praktisch VS-Code-fähig und API-tauglich, ohne Sicherheits-/Audit-Tradeoffs:

1) Skills sind deterministische, isolierte Recheneinheiten (Container, kein Netzwerk).
2) Alle externen Side-Effects und Credentials liegen ausschließlich im Connector.
3) Jede Connector-Antwort ist signiert und auditierbar (Hash-Chain kompatibel).

## Skill Source & Layout (VS-Code first)

- Pfad (empfohlen): `repo/.github/skills/<skill_dir>/SKILL.md`
- Optional: `resources/`, `scripts/`
- Progressive disclosure: Indexer liest primär YAML-Frontmatter; Body/Resources on-demand.

## Execution Hard Constraints (Non-Negotiable)

- Skill-Container: fresh ephemeral container per request, no network, no runtime installs.
- Secrets-Policy: keine Provider-Tokens im Skill-Container. Credentials bleiben im Connector.

## local | cloud Mapping (Aurora-Semantik)

- `execution.mode: local`
  - Skill liegt im Repo, wird lokal/CI/Container ausgeführt
  - kein Cloud-Registry-Eintrag notwendig
- `execution.mode: cloud`
  - Skill-ID referenziert eine Cloud-Registry (Vendor oder Custom)
  - Connector/Orchestrator löst die Referenz auf und liefert Inputs/Artefakte

## Connector Layer (Non-Negotiable)

Pattern: Orchestrator → Connector (tool_use) → signed tool_result → Orchestrator → Skill-Container Injection (stdin/file).

- Connector MUSS RBAC prüfen, bevor Provider-Calls passieren.
- Connector MUSS `trace_id` + `audit_id` führen.
- Connector MUSS eine prüfbare Signatur liefern (HMAC/Ed25519), damit Audit-Logs unverfälschbar sind.

## Artefakte (v2.1)

1) `schemas/skill_frontmatter.schema.yaml`
2) `schemas/connector_contract.schema.json`
3) `docs/skill_subsystem_connector_contract_v2_1.md` (Mapping-Tabelle + Notes)

---

# Conversation Starters

* “Full send: Analyze this repo for supply-chain risks and give me a DAG + fix plan.”
* “/DRYRUN: Design the workflow for a secure skill runner (sandbox, SBOM, audit log).”
* “/NORM: I want to use skills via API in VS Code – normalize goal/constraints/artifacts.”
* “/HANDBREMSE: Extract only requirements from this text, without defaults.”
