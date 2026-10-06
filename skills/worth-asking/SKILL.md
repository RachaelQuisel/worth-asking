---
name: worth-asking
description: >-
  Surface high-leverage questions missed in a client meeting transcript or across recent client transcripts. Use when the user asks for worth asking, dissonance radar, an EOD review, or an evening wrap-up of client transcripts; asks what they are missing in a client transcript, what they did not ask a client, what shifted in today's client meetings, what to be curious about after a client call, or to review today's transcripts; or when operating or debugging the scheduled Codex Worth Asking automation. Not for code, stack traces, or general questions that are not about a client conversation.
---

# Worth Asking

## Why this exists

The operator's default is radical agency: any friction looks like theirs to fix, so they take on blame that is only partly theirs and skip the question that would surface the actual dynamic. The classic miss is a stakeholder who drops out of meetings and is never asked why. The skill is the pause that catches that miss. **It produces questions, not statements.** Inward questions ("what should I be noticing?") and outward questions ("what should I ask this stakeholder?") only. Never drafts of outbound communication. The point is to spark dialogue, not to send a message.

## Private config

At the start of every run, load settings:

```bash
python3 skills/worth-asking/scripts/load_config.py
```

Run that from the plugin root, or pass the config path as the first argument. The loader also checks `WORTH_ASKING_CONFIG`, `./config.local.yaml`, the plugin root, the skill directory, and `~/.config/worth-asking/config.local.yaml`.

- **`mode` is `generic`.** The private file is missing. Follow `behavior` from the loader. Review only a transcript pasted in the conversation or a file path the user names. Do not invent clients, accounts, channels, or home paths. Do not search Drive, post to Slack, write a brief to a home directory, or run the scheduled automation. Return the questions in the conversation. An empty radar is still valid.
- **`mode` is `configured`.** Use only the lists, accounts, channels, and paths in that JSON. `config.example.yaml` is a template of fake placeholders. Never treat it as the client list.
- **The loader exits non-zero, or `mode` is `error`.** Stop. Say the private config could not be read. Do not guess clients or accounts.

`manual_clients` is who a local no-input run may discover. `scheduled_clients` is who the automation may post for. The manual list may be longer. That difference is intentional: a client can be reviewed by hand and still be excluded from scheduled posting. Do not auto-post a manual-only client.

`pattern_notes`, when present, are private calibration. Use them to recognize a pattern. Do not repeat a note verbatim unless the user asked to see it. If the list is empty, or the mode is generic, use only the generic lenses and do not invent personal history.

Address the operator by `operator_name` when it is set. Otherwise say "you".

## When to run

- **Manually:** a check on one conversation ("run the radar on this transcript") or a sweep of the day's client transcripts ("EOD review").
- **Scheduled:** only when mode is `configured` and the user is operating or debugging the automation. Read [automation ops](references/automation-ops.md) then, not for an ordinary transcript review. The schedule, ledger, and delivery rules live there. The automation file at `paths.automation_toml` is the source of truth when it exists.

## Input modes

Use whichever of these the loaded config actually allows:

1. **Pasted transcript text.** Always available.
2. **File path(s) the user names in this conversation.** Always available. Do not browse the home directory looking for more.
3. **Auto-discover recent (manual/local).** Only in configured mode, and only when `paths.prepare_sources` exists. The script is not bundled. If it is missing, skip discovery and ask for a pasted transcript or a path. Discovery is limited to `manual_clients`.
4. **Google Drive.** Only in configured mode, and only when `work_email` and `drive_folder_id` are set. Read [Drive transcript recovery](references/google-drive-transcripts.md) first. If those fields are empty, do not search Drive.
5. **Date-specific.** When the prepare script exists, pass the requested date as both `--cutoff` and `--through`.

If several of today's client transcripts are in scope, process them as one batch so a pattern that shows up in two clients can surface.

**Scheduled source scope** applies only in configured mode. Details, including the recovery window, the ledger, and what to do when a script is missing, are in [automation ops](references/automation-ops.md). Calendar metadata never generates findings. An unresolved source failure is a failed client result, not an empty radar. Continue unaffected clients. A malformed ledger blocks all posting.

**Meta-conversations are valid input too.** A coaching session, retro, or solo note can feed the radar. When the source is a conversation about other conversations, lean toward inward questions. Both shapes are fine.

## The lenses

The catalog is in [lenses](references/lenses.md). Load it when a signal is borderline. Brief version:

### GRPI — conflict traces to one of four roots

- **G — Goals.** Are people working toward the same outcome? Two goals can look aligned until effort has to be split.
- **R — Roles.** Does everyone know whose job is what?
- **P — Process.** Is there a shared method for decisions, or does every meeting start over?
- **I — Interpersonal.** Is there friction between specific people that is not about the work? Often downstream of G, R, or P. Sometimes the root.

### Default-mode patterns

These are the misses radical agency tends to skip. They are generic. Do not add a personal history that is not in the transcript or in `pattern_notes`.

- **Disappearance.** Someone from the last few meetings is absent. Ask where they went only if they were expected to attend. Many meetings are one-to-one by design. If an operational stakeholder was never on the invite, do not call it disappearance. Ask how they hear about the change.
- **In-meeting disagreement.** Two stakeholders contradict each other and it goes unmarked.
- **Sentiment shift.** The same person is enthusiastic one week and curt the next. Tone change is information.
- **Topic avoided.** Something raised was deflected or buried.
- **New vocabulary.** A new term shows up and may be an unnamed priority shift.
- **Commit drift.** A commitment from last week is undone, and nobody mentions it.
- **Radical-agency tell.** The operator takes blame that is only partly theirs ("I should have known", "that was on me"). Flag it for a question, not a diagnosis.
- **Pace mismatch.** The client wants more speed than the scope supports, and the operator absorbs the gap. The transcript shows the gap and nobody names it.

## Workflow

1. **Load config** with `scripts/load_config.py`, then load the transcript inputs the mode allows.
2. **Read the full transcripts.** Sentiment and sequence matter.
3. **Apply each lens.** For every candidate signal, keep the excerpt, the lens, and the question.
4. **Filter.** A signal is worth surfacing only if asking could change the next decision. Cut interesting-but-actionless notes. Target 3–7 questions, not 15.
5. **Rank.** Lead with the question that would move the most if asked next.
6. **Format.** Manual runs use the format below. Scheduled runs use the report contract named in automation ops, when that file exists.
7. **Deliver.** In generic mode, return the questions in the conversation. In configured mode, a manual run may also save `paths.briefs_dir/<YYYY-MM-DD>.md` when that directory's parent exists, and should print the path. Scheduled delivery is defined in automation ops. Do not post to Slack from a manual run unless the user asked you to operate the automation.

## Manual output format

```markdown
# Worth Asking — <YYYY-MM-DD>
**Sources:** <transcripts read, with paths or "pasted">
**Mode:** <manual | scheduled-EOD>

## 1. <The question, as a question>
**Lens:** <G | R | P | I | disappearance | sentiment-shift | etc.>
**Trigger:**
> [<speaker>] "<one-sentence excerpt>"
> — <source, e.g. "Northwind Example 2026-06-04 strategy">

<2-3 sentences on why this is worth asking. What changes if it is asked. What changes if it is not.>

**Next move:** <ONE sentence, exactly one of: "ask [stakeholder] directly in next 1:1" / "raise in next meeting opener" / "ask yourself before [trigger]" / "just notice for now". No multi-step paragraphs.>

## 2. ...

(repeat for 3-7 questions, ranked by leverage)

---
## What I did NOT flag (and why)

<Optional. 1-3 bullets on signals cut because they would not change a decision.>
```

## Voice

Strategically curious, not anxious. Warm, not alarmist. "Worth asking, not urgent" is the tone. If the day was quiet, say so. **An empty radar is a valid output.** Do not manufacture dissonance.

When the signal is the operator's own pattern (radical-agency tells, pace mismatch, commit drift), stay observational. Surface it as a question. "What if the non-answer was not yours to absorb?" rather than a verdict about their psychology.

When the transcript shows emotion, lead the next move with inquiry, then a tactical follow-up. Someone processing, nervous, grieving, or distressed may be naming a feeling or a scope change. Ask before solving.

No "ensure / utilize / facilitate." Prefer "needs to be fixed" over "needs fixing." When `paths.voice_file` exists, match that file. If it does not, keep this voice and do not invent a style guide.

## Related context

These are optional. They are not part of this package. If a skill is not installed, or a path from config is missing, skip it and continue. A pasted transcript is enough for a manual review.

- `meeting-prep` — a pre-meeting brief. Complement, not overlap. Use only if it is installed.
- `gem-miner` — a different daily pass, for lines worth keeping rather than questions worth asking. Use only if it is installed.
- `humanizing` — only if the user decides to send one of these questions and that skill is installed.
- [lenses](references/lenses.md) — full pattern catalog.
- [Drive transcript recovery](references/google-drive-transcripts.md) — only when configured Drive recovery is in use.
- [automation ops](references/automation-ops.md) — only when operating or debugging the scheduled automation.
