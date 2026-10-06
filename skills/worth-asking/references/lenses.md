# Dissonance lenses

Load this when the brief lenses in SKILL.md are not enough: a signal is borderline, or you are deciding what to filter out.

These patterns are generic. If the loaded config includes `pattern_notes`, use those notes as extra calibration for this operator. Do not repeat a note verbatim unless they asked to see it. If `pattern_notes` is missing or empty, do not invent personal history, a coaching transcript, or a stakeholder who is not in the source.

## GRPI

Treat conflict as coming from one of four roots: goals, roles, process, or interpersonal friction. Interpersonal friction is often downstream of the other three.

### G — Goals misalignment

**The shape:** Two parties act aligned until effort has to be split. The friction sounds like "why isn't this faster" or "why are we spending time on that."

**Transcript tells:**

- One person pushes for speed, another for thoroughness, and both say they want a good product.
- They disagree about what to build next, and both cite what the user wants.
- One person measures shipped count. The other measures completeness.

**Candidate questions:**

- "What does success look like for you in 30 days?"
- "If we had to ship something this week, what is the one thing it should do?"
- "What are we optimizing for here: speed, accuracy, scope, or learning?"

### R — Roles misalignment

**The shape:** Two people both think a task is theirs, or neither does, or one is making decisions the other thinks are theirs. A typical case: one person holds the contract, and someone brought in as a liaison thinks their job is to manage the build. Two role models, no shared agreement.

**Transcript tells:**

- Two people approve or reject the same artifact differently.
- One person says they will handle something, and another says they already are.
- Someone changes priority or scope, and another person pushes back later.
- Long pauses when ownership is named.

**Candidate questions:**

- "Who is the final decision-maker on [X]?"
- "Whose job is it to [Y]?"
- "When [A] and [B] disagree, who breaks the tie?"

### P — Process misalignment

**The shape:** There is no shared method. Decisions get made and unmade because nothing captures them. Each meeting starts from scratch.

**Transcript tells:**

- "We talked about this last time," and nobody can say what was decided.
- The same topic returns for several meetings without a resolution.
- Action items are assigned and never followed up.
- New requirements arrive mid-build with no path to take them in.

**Candidate questions:**

- "How are we capturing decisions so we do not relitigate them?"
- "What is the path for changing scope mid-sprint?"
- "Can we open each meeting with a few minutes to confirm where we are?"

### I — Interpersonal friction

**The shape:** Two people do not get along. Often downstream of goals, roles, or process. Sometimes the root.

**Transcript tells:**

- Sniping ("as I've said before").
- One person routes around another.
- They talk past each other in the same meeting.
- One person stops showing up.

**Candidate questions:** Do not ask the interpersonal question directly. It is not the operator's job to mediate. Ask about the structure that surfaces the friction, usually roles or goals. Instead of "Are you two getting along?", ask "How should we structure decisions when you two disagree?"

## Default-mode patterns

These are tuned to a specific default: radical agency, plus speed, plus skipping the hard question. They are still generic. A private `pattern_notes` entry may sharpen them for one operator. It is not required.

### Disappearance

**The pattern:** A stakeholder who was in the last several meetings is absent, or present and silent.

**Why it gets missed:** Fewer voices feel like clearer instructions. The harder question does not get asked.

**Tells:**

- A named participant from prior transcripts is absent.
- A new person speaks for an absent person.
- The absent person is mentioned in the past tense, or by name only.

Ask only if they were expected to attend. A meeting that is one-to-one by design is not a disappearance. If an operational stakeholder was never invited, ask how they hear about the change.

**Candidate questions:**

- "Where is [X]? Are they still on the project?"
- "Is [X] all right with where this has gone?"
- "Who is representing [X]'s view when they are not here?"

### In-meeting disagreement

**The pattern:** Two stakeholders contradict each other in the same conversation, and it is not marked in the moment.

**Why it gets missed:** Absorbing both directives is easier than surfacing the disagreement.

**Tells:**

- "But the other person said..." followed by a contradiction.
- The room pivots about which direction to take.
- Speakers talk past each other.

**Candidate questions:**

- "I'm hearing [X] from [A] and [Y] from [B]. Which should I anchor to?"
- "Can we get aligned on [Z] before I keep building?"

### Sentiment shift

**The pattern:** The same person, a different tone, week over week. Enthusiasm becomes curt, or the reverse.

**Why it gets missed:** Delivery work does not track tone unless the change is dramatic.

**Tells:** You need at least one prior transcript. Small word swaps matter: "great", "concerned", "fine".

**Candidate questions:**

- "How are you feeling about the direction right now?"
- "Anything I should know that you have not said out loud?"

### Topic avoided

**The pattern:** Someone raises a subject, and the conversation moves past it. Or the operator raises it and lets it drop.

**Tells:**

- A question gets an unrelated answer, then the topic dies.
- A pivot lands immediately after a delicate subject.
- "Anyway" or "moving on" follows a real question.

**Candidate questions:**

- "I noticed we skipped [X] earlier. Want to come back to it?"
- "What is the right time to talk about [X]?"

### New vocabulary

**The pattern:** A term enters that was not there before. Sometimes it is a priority the speaker has not named. Example: "compliance" replaces "good enough."

**Why it gets missed:** New words blend in unless they are load-bearing.

**Tells:** Word frequency changes across recent transcripts. If "audit", "compliance", "deadline", or a stakeholder's name starts appearing, surface it.

**Candidate questions:**

- "You mentioned [new term] for the first time today. Has something shifted?"

### Commit drift

**The pattern:** A prior transcript records a commitment. Today's transcript shows it did not happen, and nobody mentions it.

**Why this matters:** Drift compounds. Several undone commitments erode trust faster than one.

**Candidate questions** (usually for the operator, not the stakeholder):

- "What did I commit to last week that I have not done? Should I do it, or say that I am not going to?"

### Radical-agency tell

**The pattern:** The operator says "I should have known", "that was on me", or "I'll handle it" when the responsibility is shared.

**Why this matters:** The default is to assume the friction is theirs to fix. That can be partly true and still be incomplete. The question is which part belongs to someone else.

**Candidate questions** (for the operator):

- "What part of this is actually mine, and what part is theirs?"
- "What question would surface the other side of this?"

### Pace mismatch

**The pattern:** The client expects faster delivery than the scope supports. The operator absorbs the gap by working unsustainably. The transcript shows the gap, for example a short deadline on a long scope, and nobody names it.

**Why this matters:** The overwork is a signal that the scope conversation did not happen.

**Candidate questions:**

- "What is the right pace given the actual scope?"
- "What gets cut if we stay on the original budget?"

## Calibration

- Cut signals that do not change a decision. Interesting-but-actionless is noise.
- Three commitments in a meeting is normal. Six is a smell. Use the volume of "I'll do X" as a proxy for taking on too much.
- An empty radar is a valid output. Some days are quiet. Say so.
- Cross-client signals are rare and high-leverage. The same new vocabulary at two clients in one week is often the operator's shift, not the client's.
