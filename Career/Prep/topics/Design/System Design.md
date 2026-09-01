---
type: topic
group: Design
tier: core
confidence:
---

# System Design

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

System design interviews test a different skill than algorithm interviews:
feature sets, interfaces, class hierarchies, and designing under constraints
— simplicity, robustness, and tradeoffs matter more than a single correct
answer. Expect these questions with 4+ years of experience.

## How it works

A repeatable flow for working through a design in an interview:

1. **Understand the problem and scope** — define use cases with the
   interviewer, suggest additional features, cut what's out of scope, and
   assume high availability is a use case by default.
2. **Think about constraints** — requests per month/second, read vs. write
   ratio (keep the 80/20 rule in mind), data written and read per second,
   total storage over 5 years.
3. **Abstract design** — layers (service, data, caching), infrastructure
   (load balancing, messaging), a rough sketch of any key algorithm driving
   the service, and where the bottlenecks are.

## Implementation

## Complexity

Back-of-envelope capacity estimates (requests/sec, storage growth) are the
concrete deliverable of the constraints step above — see Resources for
reference numbers.

## When to use it

Practicing the process — work these through on paper against the flow
above, then compare to how they were handled in the real world:

- [Design a random unique ID generation system](https://blog.twitter.com/2010/announcing-snowflake)
- [Design a key-value database](http://www.slideshare.net/dvirsky/introduction-to-redis)
- [Design a picture sharing system](http://highscalability.com/blog/2011/12/6/instagram-architecture-14-million-users-terabytes-of-photos.html)
- [Design a recommendation system](http://ijcai13.org/files/tutorial_slides/td3.pdf)
- [Design a URL-shortener system](http://www.hiredintech.com/system-design/the-system-design-process/)
- [Design a cache system](https://web.archive.org/web/20220217064329/https://adayinthelifeof.nl/2011/02/06/memcache-internals/)

## Gotchas

Skipping straight to a design without pinning down scope and constraints
first is the most common failure mode — the constraints (read/write ratio,
scale) should drive the design, not the other way around.

## Resources

- [System Design from HiredInTech](http://www.hiredintech.com/system-design/)
- [How Do I Prepare To Answer Design Questions In A Technical Interview? (Quora)](https://www.quora.com/How-do-I-prepare-to-answer-design-questions-in-a-technical-interview?redirected_qid=1500023)
- [8 steps guide to ace your system design interview](https://javascript.plainenglish.io/8-steps-guide-to-ace-a-system-design-interview-7a5a797f4d7d)
- [System Design Interview (curated resource list)](https://github.com/checkcheckzz/system-design-interview)
- [How to ace a systems design interview](https://web.archive.org/web/20120716060051/http://www.palantir.com/2011/10/how-to-rock-a-systems-design-interview/)
- [System design cheat sheet (PDF)](https://github.com/jwasham/coding-interview-university/blob/main/extras/cheat%20sheets/system-design.pdf)
- [Numbers Everyone Should Know](http://everythingisdata.wordpress.com/2009/10/17/numbers-everyone-should-know/)
- [How long does it take to make a context switch?](http://blog.tsunanet.net/2010/11/how-long-does-it-take-to-make-context.html)

## Problems

_None yet._
