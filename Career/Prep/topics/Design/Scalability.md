---
type: topic
group: Design
tier: core
confidence:
---

# Scalability

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Scaling a system means handling more — more requests, more data, more
users — without a proportional increase in cost or latency. It shows up as
three distinct problems: distilling large data sets to single values,
transforming one data set into another, and simply handling obscenely large
amounts of data.

## How it works

The short-series framing (see Resources) breaks scaling up into four moves,
roughly in the order a growing system adopts them: **clone** the
application server (horizontal scaling behind a load balancer), scale the
**database** (read replicas, sharding), add a **cache** in front of
expensive reads, and introduce **asynchronism** (queues, background
workers) to stop making users wait on slow work synchronously. See
[[Messaging, Serialization, and Queues]] for the technologies that glue
services together once you're past a single machine.

## Implementation

## Complexity

## When to use it

## Gotchas

The "fallacies of distributed computing" (the network is reliable, latency
is zero, bandwidth is infinite, the network is secure, topology doesn't
change, there's one administrator, transport cost is zero, the network is
homogeneous) are the assumptions that silently break once a system is no
longer a single process — see Resources.

## Resources

- [Great overview (video)](https://www.youtube.com/watch?v=-W9F__D3oY4)
- [Scalability for Dummies, Part 1: Clones](http://www.lecloud.net/post/7295452622/scalability-for-dummies-part-1-clones)
- [Scalability for Dummies, Part 2: Database](http://www.lecloud.net/post/7994751381/scalability-for-dummies-part-2-database)
- [Scalability for Dummies, Part 3: Cache](http://www.lecloud.net/post/9246290032/scalability-for-dummies-part-3-cache)
- [Scalability for Dummies, Part 4: Asynchronism](http://www.lecloud.net/post/9699762917/scalability-for-dummies-part-4-asynchronism)
- [Scalable Web Architecture and Distributed Systems](http://www.aosabook.org/en/distsys.html)
- [Fallacies of Distributed Computing Explained (PDF)](https://pages.cs.wisc.edu/~zuyu/files/fallacies.pdf)
- [Jeff Dean - Building Software Systems At Google and Lessons Learned (video)](https://www.youtube.com/watch?v=modXC5IWTJI)
- [Introduction to Architecting Systems for Scale](http://lethain.com/introduction-to-architecting-systems-for-scale/)
- [Scaling mobile games to a global audience using App Engine and Cloud Datastore (video)](https://www.youtube.com/watch?v=9nWyWwY2Onc)
- [How Google Does Planet-Scale Engineering for Planet-Scale Infra (video)](https://www.youtube.com/watch?v=H4vMcD7zKM0)
- [The Importance of Algorithms](https://www.topcoder.com/thrive/articles/The%20Importance%20of%20Algorithms)
- [Sharding: An Unorthodox Approach to Database Design](http://highscalability.com/blog/2009/8/6/an-unorthodox-approach-to-database-design-the-coming-of-the.html)
- [Engineering for the Long Game - Astrid Atkinson Keynote (video)](https://www.youtube.com/watch?v=p0jGmgIrf_M&list=PLRXxvay_m8gqVlExPC5DG3TGWJTaBgqSA&index=4)
- [7 Years Of YouTube Scalability Lessons In 30 Minutes](http://highscalability.com/blog/2012/3/26/7-years-of-youtube-scalability-lessons-in-30-minutes.html) — [video](https://www.youtube.com/watch?v=G-lGCC4KKok)
- [How PayPal Scaled To Billions Of Transactions Daily Using Just 8VMs](http://highscalability.com/blog/2016/8/15/how-paypal-scaled-to-billions-of-transactions-daily-using-ju.html)
- [How to Remove Duplicates in Large Datasets](https://blog.clevertap.com/how-to-remove-duplicates-in-large-datasets/)
- [A look inside Etsy's scale and engineering culture with Jon Cowie (video)](https://www.youtube.com/watch?v=3vV4YiqKm1o)
- [What Led Amazon to its Own Microservices Architecture](http://thenewstack.io/led-amazon-microservices-architecture/)
- [To Compress Or Not To Compress, That Was Uber's Question](https://eng.uber.com/trip-data-squeeze/)
- [When Should Approximate Query Processing Be Used?](http://highscalability.com/blog/2016/2/25/when-should-approximate-query-processing-be-used.html)
- [Google's Transition From Single Datacenter To Failover, To A Native Multihomed Architecture](http://highscalability.com/blog/2016/2/23/googles-transition-from-single-datacenter-to-failover-to-a-n.html)
- [The Image Optimization Technology That Serves Millions Of Requests Per Day](http://highscalability.com/blog/2016/6/15/the-image-optimization-technology-that-serves-millions-of-re.html)
- [A Patreon Architecture Short](http://highscalability.com/blog/2016/2/1/a-patreon-architecture-short.html)
- [Tinder: How Does One Of The Largest Recommendation Engines Decide Who You'll See Next?](http://highscalability.com/blog/2016/1/27/tinder-how-does-one-of-the-largest-recommendation-engines-de.html)
- [Design Of A Modern Cache](http://highscalability.com/blog/2016/1/25/design-of-a-modern-cache.html)
- [Live Video Streaming At Facebook Scale](http://highscalability.com/blog/2016/1/13/live-video-streaming-at-facebook-scale.html)
- [A Beginner's Guide To Scaling To 11 Million+ Users On Amazon's AWS](http://highscalability.com/blog/2016/1/11/a-beginners-guide-to-scaling-to-11-million-users-on-amazons.html)
- [A 360 Degree View Of The Entire Netflix Stack](http://highscalability.com/blog/2015/11/9/a-360-degree-view-of-the-entire-netflix-stack.html)
- [Latency Is Everywhere And It Costs You Sales - How To Crush It](http://highscalability.com/latency-everywhere-and-it-costs-you-sales-how-crush-it)
- [What Powers Instagram: Hundreds of Instances, Dozens of Technologies](http://instagram-engineering.tumblr.com/post/13649370142/what-powers-instagram-hundreds-of-instances)
- [Salesforce Architecture - How They Handle 1.3 Billion Transactions A Day](http://highscalability.com/blog/2013/9/23/salesforce-architecture-how-they-handle-13-billion-transacti.html)
- [ESPN's Architecture At Scale - Operating At 100,000 Duh Nuh Nuhs Per Second](http://highscalability.com/blog/2013/11/4/espns-architecture-at-scale-operating-at-100000-duh-nuh-nuhs.html)
- [O'Reilly MySQL CE 2011: Jeremy Cole, "Big and Small Data at @Twitter" (video)](https://www.youtube.com/watch?v=5cKTP36HVgI)
- [Twitter: Timelines at Scale](https://www.infoq.com/presentations/Twitter-Timeline-Scalability)

## Problems

_None yet._
