# Worth Asking

This repository preserves the local Codex plugin named Worth Asking. It reviews meeting transcripts
and identifies useful questions that were missed, with a short excerpt explaining each one. It
includes the plugin manifest, skill instructions, and reference material.

This is a separate Codex package from the Claude plugin
[Questions Worth Asking](https://github.com/RachaelQuisel/questions-worth-asking). The source here
matches the author's local Worth Asking package. This repository does not contain transcript
records or credentials.

## Try the review format

With this skill available in your Codex session, paste a fictional or authorized transcript and
ask for an in-chat review. For example:

```text
Use $worth-asking on only the fictional conversation below. Do not search connected accounts,
read other files, or send a message. Return the questions in this chat.

Alex: We can launch the intake form next week, right?
Morgan: I can finish the form, but I thought Finance was approving the wording.
Alex: I thought you already had that approval.
```

A useful question would clarify who owns approval and when it is due. The excerpt is invented;
it is not a client transcript or a recorded plugin result. Without a private config file, this
in-chat review is the whole skill: no connected accounts and no scheduled send.

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

Claude Code can validate this checkout and install it from the Claude marketplace file:

```bash
claude plugin validate .
claude plugin marketplace add ./
claude plugin install worth-asking@worth-asking
```

## Private config

Client names, account identifiers, channels, and local paths are not part of this repository.
They load at runtime from a gitignored file.

```bash
cp config.example.yaml config.local.yaml
```

Edit `config.local.yaml` with your own values. Every value in `config.example.yaml` is a fake
placeholder. The skill reads the local file through:

```bash
python3 skills/worth-asking/scripts/load_config.py
```

The loader also checks `WORTH_ASKING_CONFIG` and `~/.config/worth-asking/config.local.yaml`.
A copy installed from git does not include the private file, because that file is gitignored.
Point `WORTH_ASKING_CONFIG` at your copy, or keep `config.local.yaml` in a local checkout.

If `config.local.yaml` is missing, the skill still runs. It reviews a transcript you paste or
a file path you name, and it does not assume clients, accounts, channels, or a scheduled
automation.

`manual_clients` and `scheduled_clients` are separate on purpose. The manual list can include
a client the scheduled automation should not post for.

## Files

- `.agents/plugins/marketplace.json` is the Codex marketplace catalog.
- `.claude-plugin/marketplace.json` is the Claude Code marketplace catalog.
- `.codex-plugin/plugin.json` describes the plugin.
- `config.example.yaml` is the fake template for the private runtime config.
- `skills/worth-asking/SKILL.md` contains the instructions.
- `skills/worth-asking/scripts/load_config.py` loads the private config or reports generic mode.
- `skills/worth-asking/references/` contains the review lenses, Drive recovery, and automation ops.

The plugin uses the connections available in the user's session. Pushing this source does not install the plugin or connect an account.

## Reuse terms

The author's original material is **all rights reserved**; see [LICENSE](LICENSE). Public access
to the source does not grant general reuse or redistribution rights. GitHub's public-repository
terms and applicable law still apply. Third-party references keep their own terms.
