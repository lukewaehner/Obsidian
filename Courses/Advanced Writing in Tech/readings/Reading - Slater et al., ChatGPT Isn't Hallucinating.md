---
tags:
  - reading
  - writing
  - northeastern
  - ai-ethics-genre
type: reading
course: "[[Advanced Writing in Tech]]"
week: 2
author: Joe Slater, James Humphries, Michael Townsen Hicks
year: 2024
status: raw
---

# Reading — Slater, Humphries & Hicks, "ChatGPT Isn't 'Hallucinating' — It's Bullshitting!"

Reading for [[Week 02 - AI Ethics and Genre]] · [[Advanced Writing in Tech]]

> [!cite] Citation
> Slater, Joe, James Humphries, and Michael Townsen Hicks. "ChatGPT Isn't 'Hallucinating' —
> It's Bullshitting!" *Scientific American*, 17 July 2024,
> www.scientificamerican.com/article/chatgpt-isnt-hallucinating-its-bullshitting/.
> Opinion column condensing their peer-reviewed article in *Ethics and Information Technology*
> (June 2024). All three authors are lecturers at the University of Glasgow.

## Thesis

"Hallucination" is the wrong word for what LLMs do when they produce falsehoods, and the wrong
word does real damage. The right word — in Harry Frankfurt's technical philosophical sense — is
**bullshit**: speech produced with no regard whatsoever for whether it is true. This is not a
rhetorical insult. It is a claim about the architecture: nothing in next-token prediction ever
attempts to represent the world, so the model cannot be failing at representation. It was never
trying.

## The Argument in Sequence

1. **The familiar complaint.** Everyone who has used ChatGPT knows it makes things up — the
   lawyer who filed a brief full of case citations to cases that do not exist. This is not an
   anomaly; it falls out of the design.
2. **How the machine actually works.** ChatGPT, Gemini, and Llama are structurally alike: an LLM
   trained on billions of pages predicts the next linguistic token from a ranked list of
   candidates, with a "temperature" parameter controlling how often it declines the most likely
   one (that deviation is what makes the output sound creative and human). Human trainers then
   refine outputs for sensible speech, and guardrails get bolted on. Token-by-token prediction is
   the whole idea underneath.
3. **The inference from the mechanism.** "Nothing about the modeling ensures that the outputs
   accurately depict anything in the world." There is little reason to think the outputs connect
   to any internal representation at all. A well-trained chatbot produces humanlike text; no step
   in that process checks whether the text is true.
4. **Why "hallucination" fails — the Macbeth test.** Macbeth's floating dagger is a hallucination
   because his perception is *normally* reliable and world-connected, and this time it went
   wrong. The metaphor presupposes a faculty that usually succeeds at representing. ChatGPT has
   no such faculty. "When it goes wrong, it isn't because it hasn't succeeded in representing the
   world this time; it never tries to represent the world!"
5. **Why "bullshit" fits.** Frankfurt's bullshitter isn't lying — lying requires caring about the
   truth enough to move away from it. The bullshitter is indifferent. So is the model. **And the
   crucial move: it is bullshitting even when it says true things.** The truth of an output is
   incidental to the process that produced it.
6. **Three reasons the terminology matters** (below).

## Why the Word Choice Matters — the three reasons

| # | Reason | Mechanism of harm |
| --- | --- | --- |
| 1 | **Public understanding** | Misleading terms make people misconstrue how the technology works. Bad in itself. |
| 2 | **Our relationship to the tool** | "Hallucinating" is a human-psychology word, so it anthropomorphizes — the **ELIZA effect**. Precedent: people lulled into false security by "self-driving" cars; the Google engineer who concluded a chatbot was sentient. |
| 3 | **Blame and responsibility** | Attributing agency to the program shifts blame off the users and the programmers. As this moves into health care, "it is crucial that we know who is responsible when things go wrong." |

## Quotes Worth Keeping

> "What characterizes the bullshitter, Frankfurt said, is that they just don't care whether what
> they say is true. ChatGPT and its peers cannot care, and they are instead, in a technical
> sense, bullshit machines."

> "When it goes wrong, it isn't because it hasn't succeeded in representing the world this time;
> it never tries to represent the world!"

> "And crucially, it's bullshitting even when it says true things!"

## Why This Is a Genre Reading, Not Just an Ethics Reading

Worth noticing for Thursday: this is an **opinion column in a science magazine**, explicitly
flagged as such by the standing disclaimer at the bottom, and it is a compression of a
peer-reviewed philosophy paper. The genre move is the whole point of the piece — the argument
only does its work if it escapes *Ethics and Information Technology* and reaches the people who
write the headlines. Hence the profanity in the title (attention), the Macbeth example (shared
cultural reference, no philosophy background required), the five-minute read time, and the
imperative closing line. The scholarly claim is identical; the uptake target is not.

## Key Takeaways

- The error is not occasional malfunction — it is the normal operation of a system with no
  truth-tracking step in it.
- "Hallucination" smuggles in a working perceptual faculty that isn't there. The metaphor
  flatters the machine.
- Naming is an ethical act. Which word you pick determines who gets blamed when the output is
  wrong.
- Truth-indifference, not falsehood, is the defining property. A true answer from a bullshit
  machine is still bullshit.

## Open Questions

- Does the argument survive retrieval-augmented systems and tool use, where the model *is* wired
  to external sources? Or does grounding just add a verification layer on top of a process that
  is still indifferent underneath?
- If the model is a bullshit machine, what exactly is my responsibility as a user who ships its
  output under my name — in a PR description, a design doc, a paper?
- The authors want blame to land on users and programmers. Is that distribution stable when the
  user cannot inspect the training data or the weights?

## Related

- [[Week 02 - AI Ethics and Genre]]
- [[Reading - Mazzucato, The Ugly Truth Behind ChatGPT]]
- [[Reading - Ethics and AI]]
- [[Reading - Are These AI Prompts Damaging Your Thinking Skills]]
- [[Advanced Writing in Tech]]
