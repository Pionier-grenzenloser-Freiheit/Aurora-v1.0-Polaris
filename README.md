# Aurora v1.0 Polaris

Aurora v1.0 Polaris is a governance-first baseline bundle for a regulated multi-agent MVP. It provides a structured reference set of contracts, schemas, taxonomies, module manifests, policy decisions, and MVP event seeds.

## What this repository is

This repository is a baseline-ready specification and governance bundle for a controlled multi-agent MVP. It is designed to make architectural intent, policy surfaces, validation structure, and cross-artifact dependencies explicit and versionable.

## What this repository is not

This repository is not a production runtime, not a deployed service, and not a finalized policy implementation.

It does not include:
- live external connectors
- operational policy packs
- a finalized numerical risk scale
- a finalized integrity-marker method
- generated OpenAPI or gRPC contracts

## Repository contents

### Contracts and architecture
Core governance and MVP architecture materials that define the control model and system boundaries.

### Schemas
JSON Schemas for:
- module manifests
- policy decisions
- audit events
- MVP events

### Taxonomies
Controlled vocabularies and supporting notes for:
- module types
- severity levels
- policy-pack ID conventions
- actor classes
- risk score modeling
- integrity-marker format guidance

### Materialized baseline packs
- `polaris-taxonomy-pack v1.0.0 baseline-ready`
- `polaris-mvp-module-registry-pack v1.0.0 baseline-ready`
- `polaris-mvp-policy-decision-pack v1.0.0 baseline-ready`
- `polaris-mvp-event-pack v1.0.0 baseline-ready`

### Baseline bundle
A frozen baseline bundle that indexes, validates, and cross-checks the current MVP baseline state.

## Current status

**Status:** `v1.0.0 baseline-ready`

The current repository state documents a frozen baseline slice with:
- controlled taxonomies
- 12 MVP module manifests
- 6 controlled policy-decision seed instances
- 7 MVP event seed instances
- cross-pack dependency and validation documentation

## Practical use cases

This repository can be used as:

1. A reference architecture for governance-first AI system design
2. A baseline contract bundle for future implementation work
3. A specification source for validators, generators, or interface derivation
4. A portfolio-grade architecture artifact for regulated AI and MVP design discussions

## Suggested reading order

1. `docs/mvp-control-contract.md`
2. `docs/mvp-architecture.md`
3. `schemas/`
4. `taxonomies/`
5. `module-registry/`
6. `policy-decisions/`
7. `mvp-events/`
8. `docs/baseline/validation-report.md`

## Deliberately open areas

The following areas remain intentionally open in `v1.0.0`:
- concrete policy-pack contents
- numerical risk-scale definition
- integrity-marker method
- operational connector approvals
- OpenAPI/gRPC derivations

## Design stance

Aurora v1.0 Polaris follows a governance-first and fail-closed design stance:
- explicit contracts before implementation
- auditable artifacts before operational claims
- conservative assumptions where specifications remain open
- versioned baseline slices instead of implicit drift

## Repository layout

```text
.
├─ docs/
├─ schemas/
├─ taxonomies/
├─ module-registry/
├─ policy-decisions/
├─ mvp-events/
├─ examples/
└─ releases/
```

## License

Apache-2.0
