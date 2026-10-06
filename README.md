# Worth Asking

This repository preserves the local Codex plugin named Worth Asking. It reviews meeting transcripts and identifies useful questions that were missed. It includes the plugin manifest, skill instructions, and reference material.

This is a separate Codex package from the Claude plugin named Questions Worth Asking. The source here matches the local Worth Asking package. This repository does not contain transcript records or credentials.

## Install

Codex installs this plugin by name from `.agents/plugins/marketplace.json`. The plugin root is this repository, which already contains `.codex-plugin/plugin.json`.

Add the marketplace, then install the plugin:

```bash
codex plugin marketplace add RachaelQuisel/worth-asking
codex plugin add worth-asking@worth-asking
```

From a local checkout of this repository, point the marketplace command at that directory:

```bash
codex plugin marketplace add .
codex plugin add worth-asking@worth-asking
```

Start a new Codex session after installing so the skill is available.

## Files

- `.agents/plugins/marketplace.json` is the Codex marketplace catalog.
- `.codex-plugin/plugin.json` describes the plugin.
- `skills/worth-asking/SKILL.md` contains the instructions.
- `skills/worth-asking/references/` contains the review lenses and transcript-source guidance.

The plugin uses the connections available in the user's session. Pushing this source does not install the plugin or connect an account.
