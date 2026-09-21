---
tags:
  - lecture
  - distributed-systems
  - northeastern
  - cs4730
  - introduction-networking
type: lecture
course: "[[Distributed Systems]]"
module: 1
week: 1
date: 2026-09-10
status: raw
---

# Week 01 — Introduction and Networking

Lecture for [[Distributed Systems]].

> [!info] Introduction, class policy, project infrastructure; Networking. Meeting dates are derived — the course site's schedule is week-based with no calendar dates. Tue/Thu pattern anchored on the first class, Thu 2026-09-10.

## Meetings

- **Thu Sep 10**

## Assigned Material

- [ ] [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/html/)
- [ ] ["Why are Distributed Systems so Hard?"](https://www.usenix.org/conference/srecon19americas/presentation/yu) — Yu, SREcon19 Americas
- [ ] Slides: [Intro](https://4730.network/slides/cs4730_intro_awj.pptx) (pptx)
- [ ] [[Docker Tutorial]] — [starter](https://github.khoury.northeastern.edu/cs4730/docker-tutorial/), complete by 9/15

## Due This Session

- [[Docker Tutorial]] — due 2026-09-15

## Notes

### What is a distributed system
- A set of computer programs executing on one or more computers and coordinating actions by exchanging messages
- A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable
- comprised of hosts or nodes where
	- Each node has it's own local CPU, memory
	- Hosts connected via a network

#### Why do we need them
- **Distribute** load
- **Faster response** by placing replicas closer to clients
- **Increased resources**, computation and storage
- **Resilience** to failures and attacks

#### What is expected from distributed services
- **Reliability:** provide continuous service
- **Availability**: ready to use
- **Safety**: systems do what they are supposed to do, avoiding catastrophic consequences
- **Security**: withstand passive / active attacks from outsiders or insiders

> this is not easy to achieve because

- **Computers and networks fail** in many (often unpredictable) ways
- Computers get **compromised**
- Real-time **constraints**
- **Performance** requirements
- **Complexity**

#### How do systems fail
- **Halting failures:** noticed through timeout failures
- **Fail-stop failures:** accurately detectable halting failures
- **Send-omission failures**
- **Receive-omission failures**
- **Network failures**
- **Network partitioning failures**
- **Timing failures:** temporal property of the system is violated
- **Byzantine failures:** arbitrary failures, including both benign and malicious failures

### Challenges with Systems
#### Global Knowledge:
- No host has global knowledge
- Need to use network to exchange state information
	- Network capacity is limited, can't send everything
- Information may be incorrect, out of date, etc.
	- New information takes time to propagate
	- Other changes may happen in the meantime
- Key issue:
	- How can you detect and address inconsistencies?

#### Time:
- Cannot be measured perfectly
	- Hosts have delay/duplicate messages
- How to determine what happened first?
	- In a game, which player shot first?
	- In a GDS like Sabre, who bought the last seat on the plane
- Need to have a more nuanced abstraction to represent time

#### Failures:
- the common case
	- As systems get more complex, failure becomes more likely
	- Must design systems to tolerate failure
- In Web systems, what if server fails?
	- Systems need to detect failure, recover
#### Scalability
- Systems tend to grow over time
	- How to handle increases in users, hosts, networks, etc
- In a multiplayer game, each user needs to send location to all other users
	- O(n^2) message complexity
	- Quickly overwhelms real networks
	- Can reduce frequency of updates
	- Or choose nodes who should update each other
#### Concurrency
- To scale, distributed systems must leverage concurrency
	- A cluster of replicated web servers
	- A swarm of downloaders in BitTorrent
- Often will have concurrent operations on a single object
	- How do we ensure object is in consistent state?
	- E.g. bank account: How to ensure I can't overdraw?
- Solutions fall into a few ideas:
	- Serialization: Operations happen in a defined order
	- Transactions: Detect conflicts, abort
	- Append-only structures: Deal with conflicts later

#### Security
- Distributed systems often have many different entities
	- May not be mutually trusting
	- May not be under centralized control
- Economic Incentives for abuse
- Systems often need to provide
	- Confidentiality (only intended parties can read)
	- Integrity (messages are authentic)
	- Availability (system cannot be brought down)

#### Openness
- Can system be extended / re-implemented?
	- Can anyone develop a new client?
- Requires specification of system / protocol published
	- Often requires standard body (IETF, etc) to agree
	- Cumbersome process, takes years
		- MAny corporations simply publish own APIs
- IETF uses RFCs (Request For Comment)
	- Anyonhe can publish, propse new protocol
	- Rough consensus and running code

### Architecture
Two primary hoices:
- **Client-server**: System divided into clients (often limited in power, scope, etc) and servers (more powerful, more system visibility). Clients are sending requests to servers.
- **Peer-to-peer**: All hosts are "equal", or, hosts act as both clients and servers. Peers send requests to each other. More complicated in design, but potentially higher resilience.

### Transport Protocol
At a minimum, two choices for transport
- UDP
	- Good: lower overhead (no retries or order preservation), fast (no congestion control)
	- Bad: no reliability, may increase network congestions
- TCP:
	- Good: highly reliable, fair usage of bandwidth
	- Bad: high overhead (handshake), slow (slow start, ACK clocking, retransmissions)
- However, you can always roll your own protocol on top of UDP
	- Microtransport Protocol (uTP) - used by BitTorrent
	- QUIC - invented by Google, used in Chrome to speed up HTTP
- Making your own transport protocol is very difficult

### Messaging Interface
- Messaging is fundamentally asynchronous
	- Client asks network to deliver message
	- Waits for a response
- What should the programmer see?
	- Synchronous interface: Thread or "blocked" until a message comes back. Easier to reason about
	- Asynchronous interface: Control returns immediately, response may come later. Programmer has to remember all outstanding requests. Potentially higher performance

### Serialization / Marshalling
- All hosts must be able to exchange data, thus data format is crucial
	- Web: form encoded, URL encoded, XML, JSON, ...
	- "Hard" systems - MPI, Protocol Buffers, Thrift
- Considerations
	- Openness: the format human readable or binary? Proprietary?
	- Efficiency: text is bloated compared to binary, but easy to debug
	- Versioning: can you upgrade your protocol to v2 without breaking v1 clients
	- Language support: do your formats and types work across multiple languages
### Naming
- Able to refer to hosts/processes
- Naming decisions should reflect system organization
	- Different entities, a hierarchal system may be appropriate (entities name their own hosts)
- Naming must also consider
	- Mobility: hosts may change locations
	- Authenticity: how do hosts prove who they are?
	- Scalability: how many hosts can a naming system support?
	- Convergence: how quickly do new names propagate?

### Debugging distributed protocols
- They are known to be difficult to debug
- Write proactively - print all info sent / received over the network
- Finite state machine design before implementation, and understand what your state machine is supposed to do before you implement your code
- Have message detailed description in design before implementation
- Focus on test cases to understand specific behavior
	- Delay, interleave, drop messages
	- Crash processes
#### Fundamental Topics:
- Ordering events and distributed snapshots
	- Time in distributed systems. Clock synchronization. Global states and distributed snapshots. Detecting failures.
- Consensus
	- Synchronous systems, asynchronous systems, byzantine failures (including randomized solutions)
- Distributed commit and consistency models
	- 2PC and 3PC. Weak and strong consistency in partitioned database systems. Linearizability. CAP Theorem.
- Process Groups
	- Leader election, membership, reliable multicast, virtual synchrony. Gossip protocols.
- Quorums
	- Paxos, Viewstamped replication, BFT
- Peer-to-peer systems
	- File sharing, lookup services, streaming, publish-subscribe
- Files systems
	- GFS, HDFS
- Databases
	- BigTable, HBase, Spanner, DynamoDB, Cassandra
- Lock services
	- Chubby, Zookeeper, Zab
- Computational Services
	- MapReduce, Spark


### Containers and Docker

> [!info] Slides 85–102 — "Containers / basic docker commands: review with tutorial by next class." Worked through in [[Docker Tutorial]]; the wiki version lives at [[Docker]].

#### Why containerize applications
- *Build once, run anywhere*
- A container packs together an application and **all of its dependencies**, and isolates the application from the rest of the machine it runs on
- **Running multiple instances**: because the dependencies are isolated from each other, you can run multiple containers on the same machine without them interfering with each other
- **Automated installation on clusters**: orchestrators (such as Kubernetes) automatically distribute containerized applications across a cluster of servers, so you do not have to manually install applications

#### Linux features that make containers work
- **Control groups (cgroups)**: limit the resources — memory, CPU, network input/output — that a group of Linux processes can use
	- By limiting the resources a process can use, containers provide protection against attacks that consume excessive resources
- **Linux namespaces**: restrict the visibility of resources to a process
	- By putting a process in a namespace, you can restrict which resources are visible to that process
- **Changing the root directory**: limits the set of files and directories a process can see
	- By changing the root directory when the container is created, a container cannot see the host's entire filesystem

#### Containers vs VMs
- **Hypervisor** — pure virtual machine environment: a dedicated kernel-level VMM program runs *instead of* the OS kernel
- **Hosted VM** — VMs are hosted by the host OS: a VMM runs on the host OS and the guest OS runs on the VMM, e.g. VirtualBox on your laptop
- **Container** — shares the kernel with the OS on the machine it is running on
- Tradeoffs
	- A VM has fixed resources and the overhead of running a whole kernel
	- Faster to start a container than a kernel
	- VMs offer better isolation

#### What is Docker
- An application that allows you to create and build containers
	- A set of commands to manipulate images and containers
- **Image**: complete and executable version of an application
- **Container**: the instantiation of an image
- Docker maintains a **repository** of images

### Docker basic commands

#### push / pull
- Pull an image from a repo, or push one up; **you need a Docker account to push**

```bash
docker push [OPTIONS] NAME[:TAG]
docker pull [OPTIONS] NAME[:TAG|@DIGEST]

docker push registry-host:5000/myadmin/rhel-httpd
docker pull debian
```

#### run / stop
- `run` runs a command in a **new** container

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
docker stop [OPTIONS] CONTAINER [CONTAINER...]

docker run mydockerhello
docker stop mydockerhello
```

#### ps
- Shows containers running or finished — **finished containers are saved on disk**, `-a` reveals them

```bash
docker ps [OPTIONS]

docker ps       # running only
docker ps -a    # including exited
```

#### images
- Lists all images

```bash
docker images [OPTIONS] [REPOSITORY[:TAG]]

docker images java
```

#### rm / rmi
- Remove containers / images
- **You cannot remove an image before removing all containers that use it**

```bash
docker rm [OPTIONS] CONTAINER [CONTAINER...]
docker rmi [OPTIONS] IMAGE [IMAGE...]

docker rm redis
docker rmi test:latest
```

#### Volume mapping
- When the container ends, **data is not persistent — it is lost**
- To keep data after the container ends, mount a volume (file, directory) from the host into the container

```bash
docker run -v /opt/data:/var/lib/mysql mysql
```

- `/var/lib/mysql` inside the container is mapped to `/opt/data` on the host

#### Port mapping
- Containers are **not accessible via networking from outside the host by default**
- Port mapping exposes them through host ports
- You can run multiple instances, but **each host port can be mapped only once**

```bash
docker run -p 8001:5000 mycontainer1
docker run -p 8002:5000 mycontainer2
```

- Accessing host port 8001 reaches `mycontainer1`

#### stdin / stdout / stderr
- Containers are **not mapped to stdin, stdout, stderr by default** — `-i` on `run` attaches stdin

```bash
docker run -i mycontainer
```

- Running `mycontainer`, if it reads from stdin, you will be prompted to input from the keyboard

#### attach / detach
- `-d` runs the container in the **background** (detached)
- `-a` attaches `stdout`, `stdin`, `stderr` for a container

```bash
docker run -d mycontainer
docker run -a mycontainer
docker run -i -a STDERR mycontainer
```

#### exec
- Runs a command in an **already running** container

```bash
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]

docker run --name ubuntu_bash --rm -i -t ubuntu bash
docker exec -d ubuntu_bash touch /tmp/execWorks
```

- Result: creates a new file `/tmp/execWorks` inside the running container `ubuntu_bash`, in the background

#### Networking
- Installing Docker creates **three networks**: `bridge`, `host`, and `none`
- `bridge` is an internal private network — all containers get an IP address on it (172.17.x.x)
- Containers can talk to each other using this IP
- To reach them from outside there are several solutions; one is **port mapping**
- You can also create your own private network with `docker network create`

#### Dockerfile
- Tells Docker **how to build a container**

```docker
FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y gcc
ADD hello.c /app/
WORKDIR /app/
RUN gcc hello.c -o hello
ENTRYPOINT /app/hello
```

#### Passing args
- Arguments can be baked into the `ENTRYPOINT`, or supplied at `run` time after the image name

```docker
FROM ubuntu:24.04
RUN apt-get update
RUN apt-get install -y gcc
ADD hello.c /app/
WORKDIR /app/
RUN gcc hello.c -o hello
ENTRYPOINT /app/hello classnumber
```

```bash
docker run hello 4730
```


## Key Takeaways

- 

## Open Questions

- 

## Related

- [[Distributed Systems]]
- [[Docker Tutorial]] — the hands-on version of the container slides
- [[Docker]] — the same material as a reference wiki in `Code/Docker`
