
CLI:
HTTP requests to the exchane service
Terminal interface to submit orderfs, check market status, view depth, cancel, etc

reqwest for HTTP requests (async)
Operations are stateless -> multiple CLIs can connect to one exchange (can be rewritten in other langs)

Status codes get mapped to easy debug / error messages
serde to serialize json

tokio for async runtime -> all http requests are await'ed

[[Rest API]]

---

Exchange Service:

the engine that manages order books concurrently
Exposes APIs for order management and websocket streams

[[WebSockets]]


DashMap -> lock free concurrent hashmap for symbol mapping
RwLock<OrderBook> locking per symbol

DashMap -> allows symbols to be read without causing global locks
RwLock -> many can read, queue to write the orders in (whoever is first, is first)

---

OrderBook:
Two sided book for bids and asks. Orders are match by price first, then by time

BTreeMap: sorted order on both sides with O(logn) look up (prices)
	Keeps price levels
	Insert, find, remove O(logn)
	Best prices always at the end -> Buyers low to high, sellers high to low
VecDeque: O(1) FIFO operation for time priority (time)

Match:
Does order cross the spread?

Lazy cancel for O(1) cancellation



1. BTreeMap: Sorted price levels for O(log n) best price lookup

2. VecDeque: FIFO queues for time priority within price levels

3. HashMap: O(1) order lookup for fast cancellation

The synergy:

- BTreeMap provides sorted price access

- VecDeque maintains time priority at each price

- HashMap enables fast order location for cancellation

This design achieves:

- O(log n) price operations: BTreeMap for price level management

- O(1) time operations: VecDeque for FIFO order processing

- O(1) cancellation: HashMap for order lookup

- Price-time priority: BTreeMap + VecDeque combination"