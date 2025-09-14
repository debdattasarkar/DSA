# Stock buy and sell

**Difficulty:** Medium
**Accuracy:** 29.18%
**Submissions:** 287K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given an array `arr[]` denoting the cost of stock on each day, the task is to find the maximum total profit if we can buy and sell the stocks any number of times.

**Note:** We can only sell a stock which we have bought earlier and we cannot hold multiple stocks on any day.

---

## Examples

### Example 1

**Input:** `arr[] = [100, 180, 260, 310, 40, 535, 695]`
**Output:** `865`
**Explanation:** Buy the stock on day 0 and sell it on day 3 ⇒ `310 - 100 = 210`. Buy the stock on day 4 and sell it on day 6 ⇒ `695 - 40 = 655`. Maximum Profit = `210 + 655 = 865`.

### Example 2

**Input:** `arr[] = [4, 2, 2, 2, 4]`
**Output:** `2`
**Explanation:** Buy the stock on day 3 and sell it on day 4 ⇒ `4 - 2 = 2`.

### Example 3

**Input:** `arr[] = [4, 2]`
**Output:** `0`
**Explanation:** Don't buy the stock.

---

## Constraints

* `2 ≤ arr.size() ≤ 10^6`
* `0 ≤ arr[i] ≤ 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

Paytm, Flipkart, Accolite, Amazon, Microsoft, D-E-Shaw, MakeMyTrip, Ola Cabs, Oracle, Walmart, Goldman Sachs, Directi, Intuit, Google, Quikr, Salesforce, Pubmatic, Sapient, Swiggy, Media.net

---

## Topic Tags

Arrays, Dynamic Programming, Greedy, Data Structures, Algorithms

---

## Related Interview Experiences

* Ola Interview Experience Set 7 For SDE 1
* Accolite Interview Experience Set 4 On Campus
* Directi Interview Set 1
* Intuit Interview Set 4 SSE
* One97Paytm Interview Experience
* Paytm Interview Experience Set 4 Walk In Drive
* Walmart Lab Interview Experience Set 8 Off Campus 3 Years Experience
* Makemytrip Interview Experience Set 7 On Campus
* Directi Interview Experience Set 22 Pool Campus

---

## Related Articles

* [Stock Buy Sell](https://www.geeksforgeeks.org/stock-buy-sell/)

---

---

Awesome — let’s lock in the **“total profit”** version (the judge in your screenshot expects a single number, e.g., `865`). I’ll still show multiple approaches so you can pick what an interviewer wants.

---

# 2) Explanation + step-by-step dry run

## Problem recap

You’re given daily prices `arr[0..n-1]`. You may make **any number of buy→sell transactions**, but you **cannot hold more than one share at a time** (must sell before buying again). Return the **maximum total profit**.

## Greedy insight (sum of positives)

Whenever price goes up from one day to the next, you could have bought yesterday and sold today. Summing **all positive day-to-day increases** gives the same profit as buying at each **valley** and selling at the next **peak**.

Formally, for any increasing chain `p[a] < p[a+1] < … < p[b]`:

```
(p[b] - p[a]) == Σ_{i=a}^{b-1} max(0, p[i+1] - p[i]).
```

So adding every positive `p[i+1]-p[i]` is optimal.

## Dry run (the big example)

`arr = [100, 180, 260, 310, 40, 535, 695]`

Day-to-day deltas:

* `180-100 = +80`  → add 80 (profit = 80)
* `260-180 = +80`  → add 80 (profit = 160)
* `310-260 = +50`  → add 50 (profit = 210)
* `40-310  = -270` → add 0  (profit = 210)
* `535-40  = +495` → add 495 (profit = 705)
* `695-535 = +160` → add 160 (profit = 865)

**Answer = 865** — same as buying on day 0, selling day 3; buying day 4, selling day 6.

Quick checks:

* `arr = [4, 2, 2, 2, 4]` → deltas: `-2, 0, 0, +2` → profit `2`.
* `arr = [4, 2]` → delta: `-2` → profit `0`.

---

# 3) Python solutions (interview-ready, with inline comments)

### A) Greedy “sum of positives” — **most expected** (O(n) / O(1))

```python
class Solution:
    # Function to find the maximum total profit (unlimited transactions).
    def stockBuySell(self, arr):
        """
        Greedy: sum all positive day-to-day increases.
        Time:  O(n)   - single pass over the array
        Space: O(1)   - constant extra space
        Returns: total profit as an int
        """
        profit = 0
        for i in range(len(arr) - 1):
            # If tomorrow is higher than today, take that increment
            if arr[i + 1] > arr[i]:
                profit += arr[i + 1] - arr[i]
        return profit
```

### B) Valley→Peak scan (compute intervals, then sum) — O(n) / O(1)

Useful when an interviewer asks you to **explain trades**. We still **return total profit** to match the judge.

```python
class SolutionValleyPeak:
    # Same signature, returns total profit but internally identifies intervals.
    def stockBuySell(self, arr):
        """
        Find each local valley (buy) and next peak (sell), sum their differences.
        Time:  O(n)
        Space: O(1)   (ignoring the optional intervals list)
        """
        n = len(arr)
        i = 0
        profit = 0

        while i < n - 1:
            # 1) Find next valley (first day where price stops falling)
            while i < n - 1 and arr[i + 1] <= arr[i]:
                i += 1
            if i == n - 1:       # no buy possible at the very end
                break
            buy = i

            # 2) Find next peak (last day of non-decreasing run)
            i += 1
            while i < n and arr[i] >= arr[i - 1]:
                i += 1
            sell = i - 1

            # 3) Add that trade's profit
            profit += arr[sell] - arr[buy]

        return profit
```

### C) DP “state machine” (cash/hold) — O(n) / O(1)

Shows you understand how to extend to **fees/cooldowns** later.

```python
class SolutionDP:
    # Return total profit using a 2-state DP (not holding vs holding).
    def stockBuySell(self, arr):
        """
        State transitions:
          hold = max(hold, cash - price)   # buy or keep holding
          cash = max(cash, hold + price)   # sell or keep cash
        Time:  O(n)
        Space: O(1)
        """
        if not arr:
            return 0

        cash = 0         # max profit when NOT holding a stock up to today
        hold = -arr[0]   # max profit when HOLDING a stock up to today

        for price in arr[1:]:
            hold = max(hold, cash - price)   # buy today or keep holding
            cash = max(cash, hold + price)   # sell today or keep cash

        return cash
```

### D) Baseline “brute” (recursive choices) — exponential (for learning only)

Not for production; included to show the decision space.

```python
class SolutionBrute:
    # Exponential recursion exploring buy/sell/skip decisions.
    def stockBuySell(self, arr):
        """
        Time:  O(2^n) worst-case (each day: buy/sell/skip)
        Space: O(n) recursion stack
        """
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, holding, last_buy_price):
            # i: day index; holding: 0/1; last_buy_price: price when we bought (if holding)
            if i == len(arr):
                return 0

            # Option 1: skip
            best = dfs(i + 1, holding, last_buy_price)

            if holding:
                # Option 2: sell today
                best = max(best, arr[i] - last_buy_price + dfs(i + 1, 0, 0))
            else:
                # Option 3: buy today
                best = max(best, dfs(i + 1, 1, arr[i]))

            return best

        return dfs(0, 0, 0)
```

---

# 4) Interviewer-style Q\&A

**Q1. Why does “sum of positives” give the optimal total profit?**
**A.** Any profit comes from increasing segments. For an increasing chain `p[a] < … < p[b]`, doing one trade `p[b]-p[a]` equals the sum of all daily positive increments inside that chain. Taking **every positive increment** realizes the full gain of every increasing chain; you can’t do better without violating the “one share at a time” rule.

**Q2. What’s the time/space complexity of your main solution?**
**A.** `O(n)` time (single pass), `O(1)` extra space.

**Q3. What if the array is non-increasing (always falling or flat)?**
**A.** All day-to-day differences are `≤ 0`, so the algorithm returns `0` (never buy).

**Q4. How would you print the actual buy/sell days?**
**A.** Use the **valley→peak** method to collect intervals `[buy, sell]`. Profit is the sum of `arr[sell] - arr[buy]`. (See Solution B; tweak to return the intervals if the judge wants them.)

**Q5. How do things change with a **transaction fee**?**
**A.** Modify the DP:

```
hold = max(hold, cash - price)
cash = max(cash, hold + price - fee)
```

This subtracts the fee at sell time.

**Q6. How about a **cooldown** (cannot buy the day after you sell)?**
**A.** Add a `cool` state or delay the transition from `sell` to `buy` by one day:

```
new_hold = max(hold, cash - price)
new_cash = max(cash, hold + price)  # sell today
cooldown handling: use an extra state or keep prev cash to enforce the gap
```

**Q7. What if only **one transaction** were allowed?**
**A.** Track the running minimum price and the best profit `price - min_price` (or run Kadane on day-to-day deltas). That’s a different classic problem.

**Q8. Can we hold multiple shares?**
**A.** If there’s no cap or cost, the profit becomes unbounded (you’d buy infinite quantity at each rise). Real problems add capital constraints or per-trade costs; then you’d need position sizing or more complex DP/optimization.

**Q9. Any common pitfalls?**
**A.**

* Returning intervals when the judge expects **a number** (your screenshot case).
* Forgetting to treat equal prices correctly (they neither add nor subtract profit).
* Mixing this unlimited-transaction solution with the **single-transaction** constraints.

---

---

Perfect—here’s a **full, runnable Python program** for **Stock Buy & Sell (unlimited transactions, 1 share max at a time)** that:

* prints outputs for several **input arrays** (input → output),
* includes **inline time & space complexity** notes for every step,
* and **benchmarks** the optimized solution using `timeit` right inside `main`.

It keeps the exact interview-style signature you asked for.

```python
#!/usr/bin/env python3
"""
Stock Buy & Sell (unlimited transactions, cannot hold multiple stocks)
Return the **maximum total profit**.

This script:
  1) Implements the optimized O(n) greedy (sum of positives) in class Solution.
  2) Also shows a valley->peak variant that returns the same profit.
  3) Prints results for sample inputs (input values + output).
  4) Benchmarks the optimized method using timeit inside main.

All major steps include inline time/space complexity comments.
"""

from __future__ import annotations
import random
import timeit
from typing import List


class Solution:
    # Function to find the days of buying and selling stock for max profit.
    def stockBuySell(self, arr: List[int]) -> int:
        """
        Greedy: Sum all positive day-to-day increases.
        Proof idea: For any increasing run p[a] < ... < p[b],
                    (p[b] - p[a]) = sum(max(0, p[i+1]-p[i])) over that run.

        Time:  O(n)   - single pass over the array
        Space: O(1)   - constant extra space
        Returns: total profit as an int
        """
        # O(1) time/space
        profit = 0

        # Single pass: O(n) time, O(1) space
        for i in range(len(arr) - 1):
            # O(1) compare and (optional) add
            if arr[i + 1] > arr[i]:
                profit += arr[i + 1] - arr[i]

        # O(1) return
        return profit


class SolutionValleyPeak:
    """
    Alternative: valley->peak scan (same profit, gives the intervals internally).
    Time:  O(n)
    Space: O(1) aside from optional interval storage (not returned here).
    """
    def stockBuySell(self, arr: List[int]) -> int:
        n = len(arr)
        i = 0
        profit = 0

        # Outer loop advances i monotonically => O(n) time
        while i < n - 1:
            # 1) Find next valley (local minimum) — may skip flats/declines
            #    O(k) for a maximal non-increasing stretch, amortized O(n) overall
            while i < n - 1 and arr[i + 1] <= arr[i]:
                i += 1
            if i == n - 1:  # end => no more buys
                break
            buy = i

            # 2) Find next peak (local maximum) — stretch of non-decreasing days
            i += 1
            while i < n and arr[i] >= arr[i - 1]:
                i += 1
            sell = i - 1

            # 3) Add trade's profit — O(1)
            profit += arr[sell] - arr[buy]

        return profit


def demo_on_samples() -> None:
    """
    Show correctness on a handful of inputs.
    Each print includes input and the output from both implementations.

    Overall:
      Time:  O(total length of samples)
      Space: O(1), ignoring the sample data themselves.
    """
    samples = [
        [100, 180, 260, 310, 40, 535, 695],  # expected 865
        [4, 2, 2, 2, 4],                     # expected 2
        [4, 2],                               # expected 0
        [5, 5, 5, 5],                         # flat => 0
        [1, 3, 2, 4, 6, 1, 7],               # mixed
    ]

    greedy = Solution()
    vp     = SolutionValleyPeak()

    print("=== Sample Runs (Input → Output) ===")
    for arr in samples:
        out_greedy = greedy.stockBuySell(arr)       # O(n)
        out_vp     = vp.stockBuySell(arr)           # O(n)
        print(f"Input : {arr}")
        print(f"Profit (Greedy sum-of-positives): {out_greedy}")
        print(f"Profit (Valley→Peak)            : {out_vp}")
        print("-" * 60)


# Helper used by timeit; isolates only the algorithm inside the timed region
def _bench_once(arr_large: List[int]) -> None:
    Solution().stockBuySell(arr_large)


def benchmark() -> None:
    """
    Benchmark the optimized O(n) solution using timeit.

    Prep:
      - Build a random array outside the timed call so we only time the algorithm.
      - Building input: O(N) time, O(N) space.

    Timed:
      - Each run: Kadane-like greedy loop O(N) time, O(1) space.
    """
    SIZE = 200_000  # adjust to your machine if desired
    rng = random.Random(42)

    # O(N) time, O(N) space to build input
    arr_large = [rng.randrange(0, 10**6) for _ in range(SIZE)]

    runs = 3
    # Time only the algorithm — the lambda closes over the same list (no copy)
    total = timeit.timeit(lambda: _bench_once(arr_large), number=runs)

    print("=== Benchmark (Optimized Greedy O(n)) ===")
    print(f"Array size : {SIZE}")
    print(f"Runs       : {runs}")
    print(f"Total time : {total:.6f} s")
    print(f"Avg / run  : {total / runs:.6f} s")
    print("-" * 60)


def main() -> None:
    # 1) Show outputs for specific inputs (includes inputs and outputs in print)
    demo_on_samples()

    # 2) Benchmark the optimized method with timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## Real-World Use Cases (short, high-value)

1. **Trading backtests (upper bound without frictions)**
   Compute the theoretical **maximum attainable P\&L** with unlimited entries/exits and no costs—useful as a sanity bound to evaluate whether a strategy has any hope once fees/slippage are added.

2. **Inventory / commodity roll decisions (1-unit carry)**
   If you can hold at most one unit of a commodity, this gives the best profit obtainable by repeatedly buying on local lows and selling on local highs in a price series.

3. **KPI trend harvesting**
   For monotone segments in a business metric (e.g., daily active users or sales index), this pattern identifies **all positive stretches**; the total “gain harvested” equates to the sum of positive day-to-day deltas—handy for reporting improvement windows.

---

---
