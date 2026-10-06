---
name: worth-asking
description: Surface high-leverage questions Rachael missed asking in one conversation or across recent client transcripts. Use when Rachael says "worth asking," "dissonance radar," "EOD review," "evening wrap-up," "what am I missing," "what didn't I ask," "what shifted today," "what should I be curious about," "review today's transcripts," or "did anything change today"; or when operating or debugging the scheduled Codex Worth Asking.
---

# Worth Asking

## Why this exists

Rachael's default mode is "radical agency" — she assumes any friction is hers to fix, takes on blame that isn't only hers, and doesn't ask the questions that would surface the actual dynamic. The classic miss: a stakeholder dropped out of meetings for a month and she didn't ask why. Turned out the stakeholder was frustrated with the build. She found out two weeks later via NotebookLM mining the transcripts.

The skill is the pause button that catches what her default misses. **It produces questions, not statements.** Inward questions ("what should I be noticing?") and outward questions ("what should I ask the stakeholder?") — never drafts of outbound communication. The point is to spark dialogue, not to send messages.

## When to run

- **Manually:** any time Rachael wants a check on a conversation she just had ("run the radar on this transcript") or a sweep of the day ("EOD review")
- **Scheduled:** autonomously in the Codex automation at 2:00 AM and 10:00 AM Pacific (5:00 AM and 1:00 PM Eastern), using a 14-day discovery recovery window, a durable pending ledger, and seven days of comparison context. See "Codex automation" below.

## Input modes

The skill accepts any of:

1. **Pasted transcript text** — Rachael drops a transcript directly in the prompt
2. **File path(s)** — e.g. `~/Documents/Transcripts/ClientA-Transcript-2026-08-25-Weekly.md`
3. **Auto-discover recent (manual/local)** — when run with no input locally, run `~/Documents/Transcripts/prepare_sources.py`. It syncs Debrief first and returns files by meeting date for exactly the allowlisted clients (for example, Client A, Client B, and Client C).
4. **Google Drive** — autonomously discover and retrieve transcripts accessible through the connected `you@example.com` work account. Read [Drive transcript recovery](references/google-drive-transcripts.md) before using Drive.
5. **Date-specific** — pass the requested date as both `--cutoff` and `--through` to `prepare_sources.py`

If multiple transcripts exist for today, process them as ONE batch so cross-client patterns can surface (the same stakeholder vocabulary showing up across two clients, for example).

**Scheduled source scope.** Debrief in connected Airtable supplies meeting metadata and durable record IDs. Complete transcripts may come from Debrief or verified matching Google Drive files. When Debrief text is missing or incomplete, recover it from Drive before declaring a source failure. Connected Google Calendar is a coverage source only: the automation compares completed allowlisted calendar meetings with Debrief so an omitted transcript cannot disappear silently. Calendar metadata never generates Radar findings. The Codex automation inventories a 14-day recovery window by meeting date, inclusive from today minus 13 days through today, and records eligible Debrief IDs in `~/.codex/automations/dissonance-radar/state.json`. Unposted IDs remain pending until Slack confirms delivery, even after they leave the recovery window. Successfully posted meetings from the last seven days provide comparison context. Its allowlist is exactly Client A and Client B. Do not add other clients, glob local folders, use modified time as the conversation date, or treat Meeting Prep as a transcript source. An unresolved source failure is a failed client result, not an empty radar; continue unaffected clients. A malformed ledger blocks all posting. Read [Drive transcript recovery](references/google-drive-transcripts.md) for account checks, matching, completeness, and meetings absent from Debrief.

**Meta-conversations are a valid input mode too.** Rachael's coaching sessions, retros, or solo reflection notes can also feed the radar — when the source IS a conversation about other conversations, expect the output to lean toward inward questions ("what should I be noticing?") rather than outward ones ("what should I ask the stakeholder?"). Both shapes are fine.

## The lenses (apply each one to the transcript)

Full pattern catalog is in `references/lenses.md`. Load it when needed. Brief version:

### GRPI — every conflict traces to one of four roots

- **G — Goals.** Are people working toward the same outcome? "My goal is new customers, yours is keep existing customers" — looks aligned until effort allocation comes up.
- **R — Roles.** Does everyone know whose job is what? "I thought that was your job" / "She doesn't have the technical ability but is making technical calls."
- **P — Process.** Is there a shared method? "We don't have a way to capture decisions" / "Every meeting we start from scratch."
- **I — Interpersonal.** Is there friction between specific people that isn't about the work? Usually a downstream consequence of G/R/P breakdowns, but sometimes the root.

### Rachael-specific dissonance patterns (the things her default mode misses)

- **Disappearance.** Someone who was in the last N meetings isn't in this one. The skill asks: *"Where did [X] go? Are they OK with the current direction?"* — **but only if they were on the invite list to begin with.** Many of Rachael's client meetings are 1:1 by design (e.g. Rachael ↔ a stakeholder at Client A). If an operational stakeholder was never expected to attend, don't apply this lens; surface them as an *ask* instead ("how does [X] hear about this change?").
- **In-meeting disagreement.** Two stakeholders contradict each other in the same transcript — Rachael often doesn't register this in the moment.
- **Sentiment shift.** Someone who was enthusiastic last week is curt this week, or vice versa. Tone-change is information.
- **Topic avoided.** Something Rachael raised got deflected or buried. Was that on purpose?
- **New vocabulary.** A new term or framing enters the conversation that wasn't there before — sometimes signals a priority shift the speaker hasn't named yet.
- **Commit drift.** Rachael said she'd do something last week and the transcript shows it didn't happen. Why?
- **Radical-agency tell.** Rachael takes on blame in the transcript that isn't only hers ("I should have known," "that was on me"). Flag for self-review — is there a question she should have asked instead?
- **Pace mismatch.** Client expects faster delivery than the scope allows, but Rachael is absorbing the gap by working until 2am. The transcript shows the gap without the gap getting named.

## Workflow

1. **Load inputs** — pasted text, file paths, or auto-discovery (see Input modes).
2. **Read the full transcripts.** Don't skim. Sentiment + sequence matter.
3. **Apply each lens.** Walk GRPI, then walk Rachael-specific patterns. For each potential signal, capture: the excerpt that triggered it, which lens, and the candidate question.
4. **Filter aggressively.** **Strategic curiosity, not all curiosity.** A signal is worth surfacing only if asking the question could change the next decision Rachael makes. Cut anything that's interesting-but-actionless. Target output: 3-7 questions, not 15.
5. **Rank.** Lead with the question that, if Rachael asked it tomorrow, would move the most. Bury the lower-stakes ones at the bottom.
6. **Format.** For a manual/local run, see "Manual/local output format" below. Scheduled reports use the repository contract named under "Codex automation."
7. **Deliver.** For a manual/local run, save to `~/Documents/Transcripts/briefs/<YYYY-MM-DD>.md` and print the path. In scheduled mode, let the Codex automation post each successful report through the connected Slack tool and record only successfully posted meetings in automation memory.

## Manual/local output format

```markdown
# Worth Asking — <YYYY-MM-DD>
**Sources:** <list of transcripts read, with file paths or "pasted">
**Mode:** <manual | scheduled-EOD>

## 1. <The question, as a question>
**Lens:** <G | R | P | I | disappearance | sentiment-shift | etc.>
**Trigger:**
> [<speaker>] "<one-sentence excerpt>"
> — <source, e.g. "Client A 2026-06-04 strategy">

<2-3 sentence read on why this is worth asking. What changes if Rachael asks it. What changes if she doesn't.>

**Next move:** <ONE sentence, exactly one of: "ask [stakeholder] directly in next 1:1" / "raise in next meeting opener" / "ask yourself before [trigger]" / "just notice for now". No multi-step paragraphs, no nested inward-then-outward chains.>

## 2. ...

(repeat for 3-7 questions, ranked by leverage)

---
## What I did NOT flag (and why)

<Optional. 1-3 bullets on signals you considered but cut because they wouldn't change a decision. Helps Rachael calibrate the filter over time.>
```

## Voice

Strategically curious, not anxious. Warm, not alarmist. "Worth asking, not urgent" is the tone. The skill's job is to help Rachael notice — not to overwhelm her. If the day was actually quiet, say so. **An empty radar is a valid output.** Don't manufacture dissonance.

**When the signal is about Rachael's own pattern (radical-agency tells, pace mismatch, commit drift), stay observational, not diagnostic.** Surface the pattern with a question; don't interpret her psychology. "What if the non-answer wasn't yours to absorb?" beats "you have a tendency to absorb." She's the one diagnosing — the radar just notices.

**Lead next-move suggestions with inquiry, not prescription, when the transcript shows emotion.** If someone is processing, nervous, grieving, distressed, or making a statement that could be grief OR a scope ask, open the next move with an inquiry-style question that lets Rachael ask before solving — *"I'm hearing this is a lot — can you walk me through what's in your head right now?"* / *"Where is this coming from for you?"* / *"Tell me more about that."* Then layer the tactical follow-up. The point of the radar is to spark dialogue, so the next move should model the dialogue, not jump past it.

No "ensure / utilize / facilitate." No "needs fixing" — "needs to be fixed." Match Rachael's voice rules in `~/Documents/my-voice.md`.

## Codex automation

The active scheduled Radar is `~/.codex/automations/dissonance-radar/automation.toml`. Its generated prompt points to the versioned operating contract at `prompts/codex-automation.md`. It runs at 2:00 AM and 10:00 AM Pacific and uses connected Google Calendar, Airtable, Google Drive, and Slack tools. Scheduled Drive searches and reads are authorized to run without user participation; missing access must produce an actionable failure rather than an unattended question. Local execution still requires the host and Codex scheduler to be available. The Codex app currently records it with `execution_environment = "local"`; do not describe it as a Codex cloud execution target.

`prompts/report-instructions.md` in the `your-org/dissonance-radar` repository is the canonical contract for scheduled output. Do not duplicate or override its source labels, evidence rules, voice rules, empty-radar form, or next-move constraints here. The manual/local format above remains the contract for skill runs outside the scheduled automation.

**How the fire works, end to end:**

1. Codex fires at 2:00 AM and 10:00 AM Pacific.
2. The automation compares 14 days of approved client calendar events with Debrief. A missing transcript triggers Drive recovery; only unresolved gaps produce deduplicated source-gap notices. A prior source-exception report suppresses duplicate delivery.
3. It inventories 14 days of approved Debrief metadata and adds eligible IDs to the durable pending ledger.
4. It searches each approved Slack channel for pending Airtable record IDs and marks confirmed existing posts as processed.
5. Pending records absent from Slack trigger one client report; successful meetings from the last seven days remain comparison context.
6. It fetches transcripts by exact record ID and recovers missing or truncated text from verified matching Drive files. It reads complete files before analysis; an unresolved client does not block other clients.
7. Codex posts through the connected Slack tool to the client's exact approved huddle.
8. Only record IDs from successful sends move from pending to processed; failed clients remain pending without an age cutoff.

**Operate cheatsheet.** Use the Codex automation as the source of truth:

| Action | Command |
|---|---|
| Inspect the active contract | `sed -n '1,260p' ~/.codex/automations/dissonance-radar/automation.toml` |
| Inspect pending and processed IDs | `python3 ~/Documents/Transcripts/scripts/codex_state.py show` |
| Run one non-posting diagnostic | `python3 scripts/run_one_transcript.py --record-id <rec...> --client <client-a\|client-b\|client-c>` |
| Trigger the GitHub fallback manually | `gh workflow run dissonance-radar.yml --repo your-org/dissonance-radar` |

For a Slack failure, verify that the connected installation lists your Slack workspace (for example, `T00000000`), that the exact destination is one of the two allowlisted huddle channels, and that `slack_send_message` returned a message link or identifier. The scheduled Codex path does not use `SLACK_BOT_TOKEN`. A generated report without a successful connected-tool response is failed delivery and remains retryable.

## Related skills

- `meeting-prep` — pre-meeting brief (BEFORE conversations). Complement, not overlap.
- `gem-miner` — daily scheduled mining for funny/sweet quotes. Same scheduling shape, different lens.
- `humanizing` — apply if Rachael decides to actually send one of the questions as a message (turns the question into her voice for delivery)
- `~/Documents/my-voice.md` — voice rules
- `references/lenses.md` — full pattern catalog with worked examples
