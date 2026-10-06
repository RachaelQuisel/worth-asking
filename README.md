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
it is not a client transcript or a recorded plugin result. The full skill includes modes for the
author's connected sources and scheduled workflow. Those paths, accounts, schedules, and delivery
destinations are specific to that environment, so review and adapt them before any other use.

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

## Reuse terms

The author's original material is **all rights reserved**; see [LICENSE](LICENSE). Public access
to the source does not grant general reuse or redistribution rights. GitHub's public-repository
terms and applicable law still apply. Third-party references keep their own terms.
