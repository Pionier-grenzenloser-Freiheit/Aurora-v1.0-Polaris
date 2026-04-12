# Aurora v1.0 Polaris

**Status:** `v1.0.0 baseline-ready`

Aurora v1.0 Polaris is a baseline specification repository for the Polaris MVP core. It collects the frozen baseline artifacts, schemas, controlled taxonomies, seed instances, and release notes needed to review and reuse the current Aurora Polaris baseline as a public v1 reference.

The repository is intentionally conservative. It publishes the existing baseline structure and supporting artifacts without adding runtime behavior, deployment claims, connector implementations, OpenAPI or gRPC derivations, new policy-pack content, a numeric risk scale, or a cryptographic integrity-marker method.

## What This Repository Contains

- Baseline documentation for the Polaris MVP core in [`docs/baseline/`](docs/baseline/).
- JSON Schemas for audit events, module manifests, MVP events, and policy decisions in [`schemas/`](schemas/).
- Controlled taxonomy and modeling notes in [`taxonomies/`](taxonomies/).
- MVP module manifests for 12 baseline modules in [`module-registry/`](module-registry/).
- Seed policy-decision instances for the controlled decision values in [`policy-decisions/`](policy-decisions/).
- Seed MVP event instances for the released MVP event types in [`mvp-events/`](mvp-events/).
- Valid and invalid example payloads in [`examples/`](examples/).
- Baseline bundle release notes, index, dependency map, validation report, and artifact manifest in [`releases/`](releases/).

## What This Repository Is Not

- It is not a deployed Aurora runtime.
- It is not an implementation of agents, connectors, dashboards, or services.
- It is not an API contract beyond the included baseline schemas and seed artifacts.
- It does not introduce policy-pack contents beyond the existing baseline decisions.
- It does not define a numeric risk scoring scale.
- It does not define a cryptographic method for integrity markers.

## Baseline-Ready Artifact Groups

The current baseline bundle marks these packs as `baseline-ready`:

| Artifact group | Location | Purpose |
|---|---|---|
| Polaris core baseline documents | [`docs/baseline/`](docs/baseline/) | Source documentation for the current Polaris MVP baseline. |
| Schema pack | [`schemas/`](schemas/) | Machine-readable validation surfaces for the baseline artifact types. |
| Taxonomy pack | [`taxonomies/`](taxonomies/) | Controlled enums and modeling notes for module types, severity levels, policy-pack IDs, actors, risk score, and integrity markers. |
| MVP module registry pack | [`module-registry/`](module-registry/) | Baseline module manifests for the MVP module set. |
| MVP policy-decision pack | [`policy-decisions/`](policy-decisions/) | Seed policy-decision instances for the controlled decision values. |
| MVP event pack | [`mvp-events/`](mvp-events/) | Seed MVP events for the released event types. |
| Baseline bundle metadata | [`releases/`](releases/) | Release notes, index, dependency map, validation report, and artifact manifest for `v1.0.0`. |

## Practical Use

This repository is suitable for:

- reviewing the Aurora v1.0 Polaris baseline scope;
- validating example payloads against the included schemas;
- using the module registry, policy-decision seeds, and MVP event seeds as reference fixtures;
- preparing downstream implementation work while keeping the baseline constraints visible;
- auditing which areas are intentionally left open for later specification.

## Intentionally Open Areas

The baseline bundle keeps the following areas open by design:

- concrete policy-pack contents;
- numeric risk scale definition;
- integrity-marker method;
- operational connector approvals;
- OpenAPI or gRPC derivations;
- runtime deployment and production-readiness claims.

## Repository Layout

```text
.
|-- README.md
|-- LICENSE
|-- .gitignore
|-- docs/
|   `-- baseline/
|-- schemas/
|-- taxonomies/
|-- module-registry/
|-- policy-decisions/
|-- mvp-events/
|-- examples/
`-- releases/
```

## Release Reference

The canonical release metadata for this baseline is in:

- [`releases/polaris-baseline-index__v1.0.0.md`](releases/polaris-baseline-index__v1.0.0.md)
- [`releases/polaris-baseline-dependency-map__v1.0.0.md`](releases/polaris-baseline-dependency-map__v1.0.0.md)
- [`releases/polaris-baseline-validation-report__v1.0.0.md`](releases/polaris-baseline-validation-report__v1.0.0.md)
- [`releases/polaris-baseline-artifact-manifest__v1.0.0.json`](releases/polaris-baseline-artifact-manifest__v1.0.0.json)
- [`releases/polaris-baseline-bundle__release-note__v1.0.0.md`](releases/polaris-baseline-bundle__release-note__v1.0.0.md)

## License

This repository is published under the MIT License. See [`LICENSE`](LICENSE).
