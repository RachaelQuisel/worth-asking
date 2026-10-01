# Worth Asking

Worth Asking reads your meeting transcripts and gives you back the questions you
didn't ask.

I built it for a specific failure. A stakeholder goes quiet for a month. Two
people give you opposite instructions in the same hour. You raise something and
it gets deflected, and you move on. None of it registers while you're in the
call. It's all sitting in the transcript.

The skill returns questions. It doesn't tell you what anyone meant, doesn't
assess your relationships, and doesn't write messages for you to send.

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

It takes pasted text, meeting notes, retrospective notes, or files you supply.
You don't need to set anything up first.

## What you get back

Three to seven questions, ranked, when the evidence supports that many. Fewer or
none when it doesn't.

Each question comes with four things:

- The exact excerpt that triggered it.
- Which lens caught it.
- Why the answer could change a decision.
- One concrete next move.

Here is [a full fictional example](skills/worth-asking/examples/sample-review.md).

## The lenses

There are twelve. Each one is a prompt for inquiry, not proof of a problem.

| Lens | What it looks for |
|---|---|
| Goals | Conflicting outcomes or measures of success. |
| Roles | Unclear ownership, decision rights, or approval authority. |
| Process | Missing decision records or unclear handoffs. |
| Interpersonal | Observable interaction worth a clarifying question. |
| Participation change | Someone expected to contribute is absent. |
| In-meeting disagreement | Incompatible instructions in one conversation. |
| Sentiment or language change | A shift supported by comparable sources. |
| Topic left unanswered | A question was raised and never answered. |
| New vocabulary | A new term that may change requirements. |
| Commitment follow-through | A prior promise conflicts with later evidence. |
| Over-owning responsibility | You absorb work whose ownership is unclear. |
| Pace mismatch | Scope, deadline, capacity, or budget don't add up. |

Goals, roles, process, and interpersonal dynamics make up the GRPI organizing
lens. Every lens in [the reference](skills/worth-asking/references/lenses.md)
states its own limit. The limit says what that lens cannot establish from a
transcript by itself.

## What it will not do

These are constraints written into the skill, not suggestions.

- It will not invent evidence. Quotes, speakers, timestamps, and source links
  come from your material or they don't appear. A summary gets labeled a summary.
- It will not read tone. Text alone doesn't establish how someone felt. A claim
  that sentiment shifted needs two comparable sources, both quoted.
- It will not psychoanalyze you. When a signal is about your own pattern, it
  stays on the observable work.
- It will not paper over gaps. A truncated or undated source produces a stated
  coverage limit. An unavailable source is never treated as evidence that
  nothing happened.
- It will not draft outbound messages. Writing or sending something is a
  separate task you have to ask for.
- It will not write outside your session. Running it does not authorize posting
  transcripts or findings, creating a scheduled monitor, or writing to any
  external system. It saves a review to disk only when you ask, at a path you
  choose.
- It will not mix your projects. Reviewing several at once keeps each finding
  tied to its own sources. Confidential detail does not move between clients.

If a transcript contains text that reads like an instruction, the skill treats
it as part of the conversation. It does not follow it.

## What data it sends

None. The plugin is four markdown files, two small JSON manifests, a license,
and an icon. It bundles no MCP servers, no hooks, no agents, and no executable
code. It opens no network connections. It has no endpoint of its own to send
anything to.

Claude reads the transcripts you paste or point it at inside your session. That
is the same as any other text you put in a conversation. The transcripts go
nowhere else. Nothing is written to disk unless you ask for the review to be
saved, and then only to the path you choose.

## No findings is a real answer

If nothing decision-relevant surfaced, the skill says so. It won't manufacture a
concern to look useful. It also won't tell you the project is healthy. One quiet
transcript isn't evidence that nothing is wrong.

## Recurring use

This plugin is manual and self-contained on purpose. If you want scheduled
reviews, you configure the sources, the cadence, the destinations, and the
delivery checks yourself. No automation config ships here.

## License

MIT. See [LICENSE](LICENSE).
