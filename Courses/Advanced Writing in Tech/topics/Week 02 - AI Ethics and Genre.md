---
tags:
  - lecture
  - writing
  - northeastern
  - ai-ethics-genre
type: lecture
course: "[[Advanced Writing in Tech]]"
module: 2
week: 2
date: 2026-09-09
status: notes
---

# Week 02 — AI Ethics and Genre

Lecture for [[Advanced Writing in Tech]].

## Meetings

- **Mon Sep 14** — AI discussion
- **Wed Sep 16** — Make AI policy
- **Thu Sep 17** — Lecture — Genre

## Assigned Material

- [x] "ChatGPT Isn't 'Hallucinating' — It's Bullshitting!" (Scientific American) → [[Reading - Slater et al., ChatGPT Isn't Hallucinating]]
- [x] Mariana Mazzucato, "The ugly truth behind ChatGPT" (The Guardian) → [[Reading - Mazzucato, The Ugly Truth Behind ChatGPT]]
- [x] "Ethics and AI" → [[Reading - Ethics and AI]]
- [x] "Are these AI prompts damaging your thinking skills?" → [[Reading - Are These AI Prompts Damaging Your Thinking Skills]]
- [ ] Optional: AI productivity in engineering study
- [ ] Optional: "Why AI Breaks Bad"

## Notes

### Four readings, four different objections

They are not four versions of the same complaint. Each locates the problem somewhere else, and
the disagreement between them is the actual content of Monday's discussion.

| Reading | Where the problem lives | Who is responsible | Genre |
| --- | --- | --- | --- |
| Slater, Humphries & Hicks | In the **mechanism** — no step tracks truth | Users and programmers | Opinion column (compressed philosophy paper) |
| Mazzucato | In the **infrastructure** — power, water, minerals, grid | Governments and funders, via procurement | Newspaper op-ed |
| "Ethics and AI" | In the **institution** — IP, equity, privacy, bias | Instructors, then the college | Teaching-resource briefing |
| "Are these AI prompts…" | In the **user** — reduced encoding, less critical effort | Left open; staged as a debate | News feature |

Stacked in that order they move outward from the chip to the planet and inward again to the
skull. Nothing in any of them is the objection most people actually voice ("it cheats"), which is
worth naming on Monday.

### The one claim they'd fight about: where responsibility sits

Slater et al. want blame pushed *onto* users and programmers — that's the whole reason they object
to "hallucination," which they say launders responsibility by granting the machine agency.
Mazzucato pushes blame the opposite direction, off individuals entirely and onto the states and
funders who could make disclosure a condition of support. The BBC piece won't adjudicate. The
ethics page explicitly refuses to.

**Position worth defending:** these aren't in conflict, because they're answering different
questions. Slater et al. are asking who's accountable for a *specific false output*. Mazzucato is
asking who's accountable for the *existence and scale* of the system. Individual responsibility is
the right frame for the first and useless for the second — you can't opt out of a datacentre.

### The bullshit argument is the sharpest thing in the week

Frankfurt's distinction is the tool: lying requires caring about truth enough to move away from
it; bullshitting is indifference to truth. The payoff line is that the model **is bullshitting
even when it says true things**, because the truth of an output is incidental to the process that
produced it. That reframes "is it accurate?" as the wrong evaluation question — accuracy is a
property of outputs, and the objection is about the process.

The Macbeth test is the part to bring to class. A hallucination presupposes a faculty that
normally succeeds at representing the world and failed this once. There is no such faculty here,
so the metaphor flatters the machine and misdescribes the failure mode.

### Where the readings quietly contradict each other

- **Equity vs. detection.** "Ethics and AI" argues AI editing tools could help English language
  learners — then reports that AI detectors falsely accuse non-native English writers at an
  alarming rate. Same students, helped and punished by the same technology stack.
- **Efficiency vs. learning.** The BBC's Carnegie Mellon finding (confidence in the tool → less
  critical effort) and Holmes's "outputs are better but their learning is worse" cut directly
  against the productivity case the optional engineering study presumably makes.
- **Genre vs. genre.** OpenAI's Devani gets roughly equal standing with peer-reviewed studies in
  the BBC piece, purely because balance is a news convention. Mazzucato asserts unsourced numbers
  because op-eds permit it. Neither is dishonest; both are the genre doing work on the argument —
  which is exactly Thursday's topic arriving early.

### For Wednesday — making the AI policy

The four-axis checklist from "Ethics and AI" (**IP · equity · privacy · bias**) is the most usable
artifact in the week, but a *course-level* policy has real leverage over maybe two of them. Privacy
terms are set by the vendor; bias is set by the training data; neither is negotiable from a
classroom. What a policy can actually govern:

1. **Disclosure** — what gets declared, at what granularity. The writer's memo this course already
   requires is the obvious place to put it, and it's a better instrument than a ban because it
   produces evidence instead of suspicion.
2. **Equity** — if the policy permits AI and good AI costs money, the policy has created a
   pay-to-win layer. Either the assignment stops rewarding the surface layer a subscription buys,
   or the course supplies access.
3. **What detectors are worth** — the false-positive finding should kill any policy clause that
   treats a detector report as evidence.
4. **What's being protected** — if the harm is reduced encoding rather than dishonesty, the fix is
   assessment design (can you quote your own essay?) rather than prohibition. That's Holmes's
   distinction between better outputs and worse learning, turned into policy.

Holmes's own stance is the model to argue for: not "don't use it," but "understand enough about it
to make an informed decision."

### For Thursday — genre

The week is secretly a genre unit already. Four texts making overlapping claims about the same
object, and the form determines what each is allowed to do:

- The **opinion column** can swear in its title and skip citations, and that's what lets a
  philosophy paper reach the people who write headlines. Same argument as *Ethics and Information
  Technology*, different uptake target.
- The **op-ed** gets one concrete image per claim (*Despacito* = 40,000 homes; 7,000 paused houses
  in Bicester) because 800 words can't carry a methods section. It also inherits a headline it
  didn't write — "planet-eating" is a stronger claim than the hedged body text makes.
- The **teaching-resource page** is organized as a briefing with "further reading" lists and takes
  no position by design. Its refusal to draw lines *is* its stance.
- The **news feature** sources every claim to an institution and balances a critic against a
  vendor. Balance is a convention, not a judgment — and it's how a commercially interested party
  gets equal standing with an EEG study.

Connects straight back to [[Reading - Shipka, Rethinking Composition|Shipka]]: what makes a piece
of writing good stops being mysterious once you ask what it accomplishes for whom under what
constraints. Genre is the name for those constraints.

## Key Takeaways

- **Bullshit, not hallucination.** Frankfurt's sense: indifference to truth, not falsehood. The
  model is bullshitting even when correct, because nothing in next-token prediction checks.
- Calling it "hallucination" anthropomorphizes (the ELIZA effect) and shifts blame off the humans
  — which matters most exactly where the stakes are highest, like health care.
- The cloud is a building. It out-emits commercial aviation, and where you site it decides whose
  water it drinks.
- Climate goals collide: getting off fossil fuels runs into water security, grid capacity, and
  human rights in lithium and cobalt supply chains. Mazzucato's lever is conditional public
  support — "pick the willing," not winners.
- **Confidence in the tool is inversely related to critical effort** (Carnegie Mellon/Microsoft,
  n=319). The measured harm in the MIT study wasn't wrong answers — participants couldn't quote
  essays they had just written.
- No independent evidence at scale for these tools' effectiveness, safety, or positive impact in
  education (Holmes, UCL). Cheapest defensible position in the week.
- Source concealment is described as a **design goal**, not a limitation — the tools hide
  provenance so output reads as original.
- AI detectors have a high false-positive rate on non-native English writers, which makes them
  unusable as evidence and lands the cost on the students the tools were supposed to help.

## Open Questions

- Does "it never tries to represent the world" survive retrieval and tool use, where the model is
  wired to sources? Or is grounding a verification layer over a process still indifferent
  underneath?
- What do I owe a reader when I ship model output under my name — in a PR description, a design
  doc, a paper? Disclosure at what granularity to be honest rather than performative?
- Both the aviation-emissions and 700,000-litre figures are asserted without sourcing in the
  op-ed. Chase them to primaries before reusing — Assignment 2 will need real citations.
- If reduced encoding is the real harm, is any tool policy the right instrument, or is it entirely
  an assessment-design problem?
- Two of the four readings arrived without byline or date. Get the Canvas URLs before Assignment 2
  — an uncitable reading is an unusable one.

## Related

- [[Reading - Slater et al., ChatGPT Isn't Hallucinating]]
- [[Reading - Mazzucato, The Ugly Truth Behind ChatGPT]]
- [[Reading - Ethics and AI]]
- [[Reading - Are These AI Prompts Damaging Your Thinking Skills]]
- [[Week 01 - Writing Process]]
- [[Advanced Writing in Tech]]
