---
type: topic
group: Design
tier: core
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# Messaging, Serialization, and Queues

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Once a system is more than one process, it needs a wire format
(serialization) and a way to move messages between services (queues,
pub-sub) — these are the technologies that glue [[Scalability]]'s
asynchronism story together.

## How it works

- Serialization formats trade off human-readability, size, and schema
  strictness: Protocol Buffers and Thrift are compact, schema'd binary
  formats built for RPC; MessagePack and Avro are similar in spirit.
- gRPC builds RPC on top of Protocol Buffers and HTTP/2.
- Queues (Amazon SQS, RabbitMQ, ActiveMQ, Celery) decouple producers from
  consumers and absorb bursts; pub-sub (Amazon SNS) fans a message out to
  multiple subscribers instead of one consumer; Kafka is a durable,
  ordered log that supports both patterns at high throughput.
- Redis serves as both a fast key-value store and a lightweight message
  broker (pub-sub, simple queues).

## Implementation

## Complexity

## When to use it

Queue when producers and consumers run at different rates or need to be
decoupled for reliability; pub-sub when multiple independent consumers need
the same event; a durable log (Kafka) when consumers need to replay history
or process at very high throughput.

## Gotchas

## Resources

- [Thrift](https://thrift.apache.org/) — [tutorial](http://thrift-tutorial.readthedocs.io/en/latest/intro.html)
- [Protocol Buffers](https://developers.google.com/protocol-buffers/) — [tutorials](https://developers.google.com/protocol-buffers/docs/tutorials)
- [gRPC](http://www.grpc.io/) — [gRPC 101 for Java Developers (video)](https://www.youtube.com/watch?v=5tmPvSe7xXQ&list=PLcTqM9n_dieN0k1nSeN36Z_ppKnvMJoly&index=1)
- [Redis](http://redis.io/) — [tutorial](http://try.redis.io/)
- [Amazon SQS (queue)](https://aws.amazon.com/sqs/)
- [Amazon SNS (pub-sub)](https://aws.amazon.com/sns/)
- [RabbitMQ](https://www.rabbitmq.com/) — [Get Started](https://www.rabbitmq.com/getstarted.html)
- [Celery](http://www.celeryproject.org/) — [First Steps With Celery](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html)
- [ZeroMQ](http://zeromq.org/) — [Intro - Read The Manual](http://zeromq.org/intro:read-the-manual)
- [ActiveMQ](http://activemq.apache.org/)
- [Kafka](http://kafka.apache.org/documentation.html#introduction)
- [MessagePack](http://msgpack.org/index.html)
- [Avro](https://avro.apache.org/)

## Problems

_None yet._
