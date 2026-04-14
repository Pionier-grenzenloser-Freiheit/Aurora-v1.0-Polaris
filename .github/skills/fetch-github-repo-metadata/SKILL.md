---
id: skill.example.fetch_repo
name: fetch-github-repo-metadata
description: Collects GitHub repository metadata via connector (read-only).
version: 0.1.0
execution:
  mode: local
allowed_tools:
  - tool.github_fetch_repo
rbac:
  scope: repo:read
inputs:
  - name: repo
    type: string
    required: true
outputs:
  - name: repo_summary
    type: json
x-aurora:
  connector_required: true
---

# Fetch GitHub Repo Metadata

This skill is deterministic and must not perform network access.

Inputs:
- repo: "owner/name"

Behavior:
1) Request connector tool `tool.github_fetch_repo` with RBAC `repo:read`.
2) Receive signed result and write sanitized summary to output.

Output:
- repo_summary (json)
