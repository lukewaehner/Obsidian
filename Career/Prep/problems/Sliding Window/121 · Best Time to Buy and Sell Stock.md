---
type: problem
source: neetcode
number: 121
url: https://neetcode.io/problems/buy-and-sell-crypto
difficulty: Easy
pattern: Sliding Window
patterns: ["Sliding Window", "Greedy"]
topics: ["[[Career/Prep/topics/Data Structures/Arrays|Arrays]]", "[[Career/Prep/topics/Algorithm Design/Greedy Algorithms|Greedy Algorithms]]"]
solved_on: 2026-09-08
attempts: 3
aid: unaided
revisit: false
time: O(n)
space: O(1)
language: python
---

# 121 · Best Time to Buy and Sell Stock

> [!question]- Problem
> Given daily prices, choose one day to buy and a later day to sell to maximise profit. Return the maximum profit, or 0 if none is possible.

## Idea

Selling on day `i` is only ever worth doing against the cheapest day seen before
it, so one pass carrying that minimum answers every sell day in O(1).

## Naive

Every ordered pair, explicitly:

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for l in range(len(prices) - 1):
            r = l + 1
            while r < len(prices):
                theorized = prices[r] - prices[l]
                profit = max(theorized, profit)
                r += 1

        return profit
```

> [!warning] Defect
> Correct, but O(n²) against a standard O(n) — at the problem's limit of
> 10⁵ prices that is ~5 × 10⁹ comparisons, a guaranteed timeout. The fix is not a
> micro-optimisation of the inner loop but its deletion: the inner loop recomputes
> `min(prices[:r])` from scratch on every `r`, and that minimum can be carried
> forward in a single variable instead.

## Optimal

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for sell in prices:
            profit = max(profit, sell - buy)
            buy = min(buy, sell)
        return profit
```

## Why it works

The brute force asks "for each buy day, what is the best sell day?" — n choices
downstream of each of n days. Flipping the question is what collapses it: **for
each sell day, what is the best buy day?** There is exactly one answer, the
minimum price strictly before it, and minima extend incrementally.

The two lines encode that:

```python
profit = max(profit, sell - buy)   # best trade ending today
buy    = min(buy, sell)            # cheapest day for tomorrow onwards
```

Order matters, though not in the way it first appears. `profit` is computed
*before* `buy` is updated, so on the day the new minimum arrives it is compared
against the older, higher `buy` — but that day's own `sell - buy` is at best
`0`, and `profit` starts at `0`, so nothing is lost. Updating `buy` first would
also be correct here, for the same reason: buying and selling on the same day
yields `0`, which the initial `profit = 0` already covers. That initial value is
also what encodes "no transaction" for a strictly decreasing price series.

Read as a sliding window: `buy` is the left edge, `sell` the right, and the
window jumps its left edge to the right edge whenever a cheaper price appears —
the left never moves backwards, which is what makes the sweep linear.

> [!tip] `prices[0]` on an empty list
> `buy = prices[0]` raises `IndexError` on `[]`. This problem guarantees at least
> one price, so it is fine as written; `buy = float("inf")` with the loop
> unchanged removes the assumption at no cost.

## Template

One pass carrying the best-so-far prefix statistic:

```python
best_prefix = arr[0]
answer = 0
for x in arr:
    answer = max(answer, x - best_prefix)
    best_prefix = min(best_prefix, x)
```

## Mistakes I made

Reached for the pair enumeration first and only then looked for structure. The
generalisable move is the one that fixed it: when a brute force is a nested loop
over `(i, j)` with `i < j`, ask what the inner loop is actually *computing* about
the prefix — here a running minimum — and whether it can be maintained instead of
recomputed. That is the same reduction that turns the O(n²) subarray-sum scan
into a prefix-sum sweep.

## Related

- [[Career/Prep/problems/Two Pointers/11 · Container With Most Water|11 · Container With Most Water]] — the other problem where a maximum over pairs collapses to a single sweep
- [[Career/Prep/topics/Algorithm Design/Greedy Algorithms|Greedy Algorithms]]
