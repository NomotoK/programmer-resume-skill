# Codex Git Marketplace Plugin Implementation Plan

**Goal:** Publish the resume skill suite as a Git-backed Codex marketplace plugin while preserving Claude Code marketplace compatibility and shipping all export resources in one package.

**Architecture:** The repository root is a marketplace. Its single plugin lives at `plugins/programmer-resume-skill/`, which owns the manifests, skills, templates, scripts, examples, research, and tests. Codex and Claude marketplace manifests both point to that package.

**Status:** Implemented on `feat/codex-marketplace-plugin`.

## Decisions

- Codex marketplace: `programmer-resume`; plugin: `programmer-resume-skill`.
- Package source: `./plugins/programmer-resume-skill`.
- Codex policy: `AVAILABLE` / `ON_INSTALL`; category: `Developer Tools`.
- Codex manifest version: `0.2.0`; no MCP, App, or Hook declaration.
- Claude marketplace remains supported through the same packaged source tree.

## Tasks

- [x] Move the single plugin source tree under `plugins/programmer-resume-skill/`.
- [x] Add Codex and Claude marketplace manifests at the repository root.
- [x] Complete the Codex manifest interface metadata and synchronize the Claude version and agent prompt.
- [x] Extend structural validation to check marketplace names, source paths, policy, and category.
- [x] Update English and Chinese installation guidance, resource links, and update instructions.
- [x] Run plugin-manifest, marketplace, pytest, project-validator, Claude, and XeLaTeX verification gates.
- [x] Perform a local Codex marketplace install smoke test and verify the installed package resources.
