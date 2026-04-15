# Aurora Briefing & Variant Canvas System

This document defines the two-stage workflow, data formats, and export rules for a structured, editable canvas that initiates interactive web-app projects.

## 1) Workflow Overview

### 1.1 Klärungsphase (Clarification)
* **Initial prompt:** “Stopp – was möchten Sie erreichen?”
* **Orchestration:** Ask focused follow-up questions about:
  * Goals and outcomes
  * UX/UI requirements
  * Devices
  * Accessibility
  * Performance
  * Compliance
  * Security & privacy
  * Integrations
  * Monetization
  * Expected users
  * KPIs & analytics
  * Timeline & budget
  * Team capabilities
* **Persistence:** Store responses as:
  * Free text summary
  * Structured `BriefingRecord` JSON
* **Versioning:** Every edit updates `meta.version` and `meta.lastUpdatedAt`.
* **Assets:** Optionally capture brand guidelines, APIs, sample screens, analytics goals, competitor links in an assets list and reference them in the canvas sidebar.

### 1.2 Vorschlagsphase (Variants)
* Generate **five** editable canvas cards (variants).
* Each card contains a short structured profile:
  * Zielgruppe, Ziel/Outcome (success criteria)
  * Core features (Must/Should/Could/Out of Scope)
  * Tech stack
  * Effort estimate
  * Elevator pitch
  * Advantages & risks
  * Example user stories with acceptance criteria
  * Security & privacy requirements
  * Integrations
  * Roles/agents and required skills
  * KPIs
  * Relevant constraints
  * **Rationale:** why this variant fits the briefing

### 1.3 Post-Selection Handover
After selecting a variant, orchestrate a multi-agent team (Frontend, Backend, DevOps, Security, QA, Data) and create a full delivery package:
* Prioritized user stories & acceptance criteria
* UI artifacts
* API specification
* Data model
* Tests
* Security/performance checks
* CI/CD requirements
* Repo structure
* Timeline

## 2) Data Contracts

### 2.1 BriefingRecord
See `schemas/briefingRecord.schema.json`.

### 2.2 Card
See `schemas/card.schema.json`.

### 2.3 Error
See `schemas/error.schema.json`.

### 2.4 Compare View
See `schemas/compare.schema.json`.

## 3) Validation & Error Handling

### 3.1 Missing/Invalid Fields
Return an error object with:
* `type`: `ValidationError`
* `fields`: list of missing/invalid fields
* `expected`: example or schema snippet

### 3.2 Incomplete or Draft
When incomplete fields are allowed:
* Set `meta.status` to `draft` or `incomplete`.
* Return an error object with:
  * `type`: `PartialCompletion`
  * `status`: `draft` or `incomplete`
  * `fields`: list of missing fields
  * `message`: recommended next step

### 3.3 Version Conflicts
If a conflict exists:
* Return error object with:
  * `type`: `VersionConflict`
  * `expected`: `{ recordId, version }`
  * `message`: conflict origin

### 3.4 Parallel Edits
Use `lastUpdatedAt` + `owner` as the conflict key. Provide one of:
* `MergeConflict` error with “last write wins” note, or
* `MergeConflict` + `mergeProposal`

## 4) Compare/Diff Rules

* Compare view displays variants side-by-side.
* Differences are structured as JSON Patch-like entries for:
  * `scope.must`
  * `tech`
  * `effort.estimate`
  * `risks`
  * `constraints`

## 5) Export Mapping

### 5.1 CSV
* Columns mirror the JSON schema field order.
* Headers in English.
* Empty fields are `''`.

### 5.2 Markdown
* Section per core field.
* Tables for arrays.
* Lists for KPIs.
* Errors in code blocks.

### 5.3 Notion Page
* Mirrors JSON structure.
* Sections for Meta/Details.
* Tables for User Stories and Integrations.

### 5.4 Figma Starter
* Properties in the start frame: `recordId`, `title`, core UX requirements, outcomes.
* User stories as links.
* Integrations as annotations.
