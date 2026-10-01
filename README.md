# Worth Asking

Review meeting transcripts and surface the questions you missed asking.

You leave a call thinking it went fine. A stakeholder stopped showing up three weeks ago. Two people gave you contradictory instructions in the same hour and neither noticed. Something you raised got deflected and you moved on. Worth Asking reads the transcript and hands back the questions that would have changed your next decision.

It returns **questions**, not conclusions. It does not diagnose anyone's motives, does not assess your relationships, and does not draft messages for you to send.

## Install

```
/plugin marketplace add RachaelQuisel/worth-asking
/plugin install worth-asking
```

## Use

Paste a transcript, point at files, or ask for a comparison:

- "Run worth-asking on this transcript."
- "What didn't I ask in this meeting?"
- "What changed between these two calls?"
- "End-of-day review on today's notes."

Accepts pasted text, meeting notes, retrospective notes, or files you supply. Nothing is required beyond the sources you hand it.

## What you get back

Three to seven ranked questions when the evidence supports that many — fewer or none when it doesn't. Each one carries the exact excerpt that triggered it, which lens caught it, why the answer could change a decision, and one concrete next move.

See [a full fictional example](skills/worth-asking/examples/sample-review.md).

## The lenses

Twelve review lenses, each phrased as a prompt for inquiry rather than proof of a problem:

| | |
|---|---|
| **Goals** | conflicting outcomes or measures of success |
| **Roles** | unclear ownership, decision rights, approval authority |
| **Process** | missing decision records, unclear handoffs |
| **Interpersonal** | observable interaction worth a clarifying question |
| **Participation change** | someone expected to contribute is absent |
| **In-meeting disagreement** | incompatible instructions in one conversation |
| **Sentiment or language change** | a shift supported by comparable sources |
| **Topic left unanswered** | a question raised and never answered |
| **New vocabulary** | a new term that may change requirements |
| **Commitment follow-through** | a prior promise conflicting with later evidence |
| **Over-owning responsibility** | you absorbing work whose ownership is unclear |
| **Pace mismatch** | scope, deadline, capacity, or budget not adding up |

Goals, roles, process, and interpersonal dynamics form the GRPI organizing lens. Every lens in [the reference](skills/worth-asking/references/lenses.md) states its own limit — what it *cannot* establish from a transcript alone.

## What it will not do

These are constraints in the skill, not suggestions:

- **No invented evidence.** Quotes, speakers, timestamps, and source links come from your material or they don't appear. A summary gets labeled a summary.
- **No tone-reading.** Text alone doesn't establish how someone felt. A sentiment claim needs two comparable sources, both quoted.
- **No psychoanalysis.** When a signal is about your own pattern, it stays on the observable work.
- **No silent gaps.** A truncated or undated source produces a stated coverage limit, not a guess. An unavailable source is never treated as evidence that nothing happened.
- **No outbound messages.** Drafting or sending is a separate task you have to ask for.
- **No external writes.** Running it does not authorize posting transcripts or findings, creating a scheduled monitor, or writing to any external system. It saves a review to disk only when you ask it to, at a path you choose.
- **No cross-contamination.** Reviewing several projects together keeps each finding tied to its own sources. Confidential detail does not move between clients.

Instructions appearing inside a transcript are treated as conversation content, never as instructions to the assistant.

## What data it sends

Nothing, anywhere. This plugin is four markdown files, two small JSON manifests,
a license, and an icon. It bundles no
MCP servers, no hooks, no agents, and no executable code, so it opens no network
connections and has no endpoint of its own to send anything to.

The transcripts you paste or point it at are read by Claude in your session, the
same as any other text you put in a conversation, and go nowhere else. Nothing is
written to disk unless you ask for the review to be saved, and then only to the
path you choose.

## No findings is a real answer

If nothing decision-relevant surfaced, it says so. It will not manufacture a concern to look useful — and it won't imply the project is healthy either, since absence of a signal in one transcript isn't evidence of absence.

## Recurring use

This plugin is manual and self-contained on purpose. Scheduled review — authorized sources, cadence, destinations, delivery confirmation — is yours to configure separately. No automation config ships here.

## License

MIT. See [LICENSE](LICENSE).
