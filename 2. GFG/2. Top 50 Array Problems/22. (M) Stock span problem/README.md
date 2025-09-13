# Stock Span Problem

**Difficulty:** Medium
**Accuracy:** 43.56%
**Submissions:** 241K+
**Points:** 4

---

## Problem Statement

The stock span problem is a classic financial puzzle where we are given a series of daily price quotes for a stock and we need to calculate the **span** of the stock price for **all** days.

You are given an array `arr[]` representing daily stock prices. The **stock span** for the `i`-th day is the **number of consecutive days** up to day `i` (**including day i itself**) for which the price of the stock is **less than or equal to** the price on day `i`.

Return the span of stock prices for each day in the given sequence.

---

## Examples

### Example 1

**Input:** `arr[] = [100, 80, 90, 120]`
**Output:** `[1, 1, 2, 4]`
**Explanation:**

* For 100, there are no previous days with price ≤ 100 → span = 1
* For 80, no previous price ≤ 80 → span = 1
* For 90, previous day 80 ≤ 90 → span = 2
* For 120, previous days 100, 80, 90 ≤ 120 → span = 4

---

### Example 2

**Input:** `arr[] = [10, 4, 5, 90, 120, 80]`
**Output:** `[1, 1, 2, 4, 5, 1]`
**Explanation:**

* 10 → span 1
* 4 → span 1 (less than 10)
* 5 → previous 4 ≤ 5 → span 2
* 90 → previous 5, 4, 10 ≤ 90 → span 4
* 120 → previous 90, 5, 4, 10 ≤ 120 → span 5
* 80 → previous is 120 (>80) → span 1

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

Flipkart • Accolite • Amazon • Microsoft • Samsung • Adobe

---

## Topic Tags

Arrays • Stack • Data Structures

---

## Related Interview Experiences

* Flipkart Interview Experience Set 24

---

## Related Articles

* [The Stock Span Problem](https://www.geeksforgeeks.org/the-stock-span-problem/)

---

---

Here’s an interview-ready guide to the **Stock Span** problem.

---

## 2) Intuition + Step-by-step dry run

### What is the span?

For each day `i`, the span is the number of **consecutive** days ending at `i` (including day `i`) whose price is \*\*≤ price\[i]`.  
Equivalently: distance from `i`back to the last day **strictly greater** than`price\[i]\`.

### Key idea

If we knew the index of the **previous greater element** (PGE) for day `i`, say `p`, then:

```
span[i] = i - p            # where p = index of last day with price > price[i]
                           # if none exists, p = -1, span = i - (-1) = i + 1
```

A **monotonic decreasing stack of indices** (prices strictly decreasing from bottom → top) helps us find the PGE in **O(1) amortized** per day by popping all smaller or equal prices.

#### Dry run on arr = \[10, 4, 5, 90, 120, 80]

We maintain a stack `st` of indices with **strictly decreasing** prices; for day `i`, we pop while `arr[st[-1]] <= arr[i]`.

* i=0, price=10
  st=\[], pop none → previous greater index = -1 → span = 0 - (-1) = 1
  push 0 → st=\[0]
* i=1, price=4
  st=\[0], arr\[0]=10 > 4 → previous greater = 0 → span=1-0=1
  push 1 → st=\[0,1]
* i=2, price=5
  st=\[0,1], arr\[1]=4 <= 5 → pop 1; now st=\[0], arr\[0]=10>5 → previous greater=0
  span=2-0=2
  push 2 → st=\[0,2]
* i=3, price=90
  st=\[0,2], arr\[2]=5<=90 → pop; arr\[0]=10<=90 → pop; st=\[] → previous greater=-1
  span=3-(-1)=4
  push 3 → st=\[3]
* i=4, price=120
  st=\[3], arr\[3]=90<=120 → pop; st=\[] → previous greater=-1
  span=4-(-1)=5
  push 4 → st=\[4]
* i=5, price=80
  st=\[4], arr\[4]=120>80 → previous greater=4
  span=5-4=1
  push 5 → st=\[4,5]

**Spans:** `[1, 1, 2, 4, 5, 1]` ✅

---

## 3) Python solutions (brute & optimal) with interview-style comments

### A) Brute force — scan backwards for each day (O(n²))

```python
class Solution:
    def calculateSpan(self, arr):
        """
        Brute force: for each day i, walk left while prices are <= arr[i].
        Time:  O(n^2) worst-case (strictly increasing prices)
        Space: O(1) extra
        """
        n = len(arr)
        span = [0] * n
        for i in range(n):                     # O(n)
            j = i
            # Count consecutive days ending at i with price <= arr[i]
            while j >= 0 and arr[j] <= arr[i]: # worst-case O(n) per i
                j -= 1
            span[i] = i - j                    # i - previous_greater_index
        return span
```

### B) Optimal — Monotonic decreasing stack of indices (O(n))

```python
class Solution:
    def calculateSpan(self, arr):
        """
        Monotonic stack of indices storing a strictly decreasing sequence of prices.
        For day i: pop indices with price <= arr[i] so the new top (if any) is the
        previous greater element (PGE). Span = i - PGE_index (or i - (-1) if none).
        
        Time:  O(n) total — each index is pushed once and popped at most once
        Space: O(n) for the stack + O(n) for the output
        """
        n = len(arr)
        span = [0] * n
        st = []  # stack of indices, prices strictly decreasing along the stack

        for i in range(n):
            # Pop while current price dominates (<= because equal prices also extend span)
            while st and arr[st[-1]] <= arr[i]:
                st.pop()

            prev_greater_idx = st[-1] if st else -1
            span[i] = i - prev_greater_idx

            st.append(i)   # push current index to serve as PGE for future days

        return span
```

### C) Optimal (variant) — Stack of (price, cumulative\_span)

This accumulates span while popping, sometimes seen in interviews:

```python
class SolutionVariant:
    def calculateSpan(self, arr):
        """
        Keep stack of pairs (price, accumulated_span). For each new price,
        pop and accumulate spans while stack top price <= current price.
        The resulting span is 1 + accumulated pops.
        
        Time:  O(n)
        Space: O(n)
        """
        st = []              # each element: (price, span_of_that_price)
        out = []
        for p in arr:
            s = 1            # at least today itself
            # absorb consecutive previous prices <= p
            while st and st[-1][0] <= p:
                s += st.pop()[1]
            st.append((p, s))
            out.append(s)
        return out
```

---

## 4) Common Interview Q\&A

**Q1. Why do we pop while `<=` (not just `<`)?**
Because the span includes **equal** prices: “less than or equal to today’s price.”
Using `<=` merges equal days into a single continuous block.

**Q2. Proof of O(n) time for the stack approach?**
Each index is **pushed once** and **popped at most once**. All loop iterations across the whole run sum to O(n).

**Q3. What does the stack store—prices or indices?**
Either works.

* **Indices** let you compute `span = i - prev_greater_index` directly.
* **(price, span)** pairs let you accumulate spans as you pop.

**Q4. Edge cases?**

* Strictly increasing sequence → spans `[1,2,3,...,n]`.
* Strictly decreasing sequence → spans all `1`.
* Repeated equal prices are handled by the `<=` popping rule.

**Q5. Can we do it in O(1) extra space?**
Not while keeping O(n) time in standard Python; you need some structure to remember previous greater elements. You could reuse the output array as an auxiliary stack in lower-level languages, but clarity usually wins in interviews.

**Q6. Relation to “Previous Greater Element (PGE)”?**
Identical. Once you know PGE for each index, `span[i] = i - PGE[i]`.

**Q7. Why not binary search on prior days?**
Previous days are not sorted by value; we need a structure (stack) that compresses monotonic runs and gives amortized O(1) updates.

---

---

Below is a **complete, runnable Python program** that solves the **Stock Span** problem using the optimal **monotonic stack** approach, prints results for sample inputs, and **times** the run with `timeit`. I’ve added **inline comments** that clearly state the **time and space complexity** at each step.

```python
from typing import List
import timeit
import random

# ============================================================
# Stock Span — Monotonic Stack (Optimal O(n))
# ============================================================

class Solution:
    def calculateSpan(self, arr: List[int]) -> List[int]:
        """
        Compute the stock span for each day.

        Core idea:
        - Maintain a stack of indices whose prices form a strictly decreasing sequence.
        - For day i, pop all indices with price <= arr[i] so the new top is the
          previous GREATER element index. Then span[i] = i - prev_greater_index.
          If none exists, prev_greater_index = -1, span[i] = i - (-1) = i + 1.

        Time complexity:
          - Each index is pushed once and popped at most once -> O(n) total.
        Space complexity:
          - O(n) for the stack + O(n) for the output array.
        """
        n = len(arr)                 # O(1)
        span = [0] * n               # O(n) output
        st: List[int] = []           # O(n) worst-case stack of indices

        # Single pass over the array: O(n)
        for i in range(n):
            # Pop while current price "dominates" (<= to include equal prices)
            # Amortized O(1) per index, O(n) over full loop.
            while st and arr[st[-1]] <= arr[i]:
                st.pop()

            prev_greater_idx = st[-1] if st else -1  # O(1)
            span[i] = i - prev_greater_idx           # O(1)

            st.append(i)                              # O(1) push

        return span


# (Optional) Brute force for comparison & validation
class SolutionBrute:
    def calculateSpan(self, arr: List[int]) -> List[int]:
        """
        Brute force: For each i, scan left while arr[j] <= arr[i].
        Time complexity:  O(n^2) worst-case (strictly increasing prices).
        Space complexity: O(1) extra (besides output).
        """
        n = len(arr)             # O(1)
        span = [0] * n           # O(n)
        for i in range(n):       # O(n)
            j = i                # O(1)
            # Worst-case inner loop O(n) per i -> O(n^2)
            while j >= 0 and arr[j] <= arr[i]:
                j -= 1
            span[i] = i - j
        return span


# ---------------------- Demo / Timing Harness ---------------------- #

def run_case(name: str, arr: List[int], solver) -> None:
    """
    Run one case, print input, output and timing.

    Time per call (optimal): O(n)
    Space per call (optimal): O(n)
    """
    arr_copy = arr[:]                           # O(n) copy to keep inputs intact
    t0 = timeit.default_timer()
    ans = solver.calculateSpan(arr_copy)
    t1 = timeit.default_timer()
    print(f"{name}:")
    print("  Input :", arr)
    print("  Span  :", ans)
    print(f"  Time  : {(t1 - t0):.6f}s\n")


def main():
    print("=== Stock Span — Examples, Validation, and Timing ===\n")

    # Instantiate solvers
    fast = Solution()
    slow = SolutionBrute()

    # Example 1 (expected [1, 1, 2, 4])
    arr1 = [100, 80, 90, 120]
    run_case("Example 1 (optimal)", arr1, fast)
    run_case("Example 1 (brute)",   arr1, slow)

    # Example 2 (expected [1, 1, 2, 4, 5, 1])
    arr2 = [10, 4, 5, 90, 120, 80]
    run_case("Example 2 (optimal)", arr2, fast)
    run_case("Example 2 (brute)",   arr2, slow)

    # Quick correctness check that optimal == brute on random data (small n to keep it quick)
    rng_arr = [random.randint(1, 1000) for _ in range(25)]
    span_fast = fast.calculateSpan(rng_arr[:])
    span_slow = slow.calculateSpan(rng_arr[:])
    print("Random check equal? ->", span_fast == span_slow, "\n")

    # Performance demo (larger input) — optimal should be much faster than brute
    n = 100_000
    big = [random.randint(1, 100_000) for _ in range(n)]

    # Time optimal on big input: O(n)
    t0 = timeit.default_timer()
    _ = fast.calculateSpan(big[:])
    t1 = timeit.default_timer()
    print(f"Large input n={n} (optimal) elapsed: {(t1 - t0):.6f}s")

    # (Optional) Skip brute on large input to keep runtime reasonable.
    # Uncomment to observe O(n^2) behavior (will be very slow):
    # t2 = timeit.default_timer()
    # _ = slow.calculateSpan(big[:n//50])  # Try a much smaller slice instead
    # t3 = timeit.default_timer()
    # print(f"Brute on n={n//50} elapsed: {(t3 - t2):.6f}s")


if __name__ == "__main__":
    total_start = timeit.default_timer()
    main()
    total_end = timeit.default_timer()
    print("\n==== TOTAL PROGRAM TIME ====")
    print(f"{(total_end - total_start):.6f}s")
```

---

## 6) Real-World Use Cases (just the big ones)

* **Portfolio analytics / streaks:** Quickly compute run-lengths of days a stock did not break a certain price level (support), or days up to a new high—used in backtesting and momentum indicators.
* **E-commerce price tracking:** For each day, how many previous days did an item's price stay below (or equal to) today’s price—helps detect sustained promotions vs. one-off discounts.
* **Sensor thresholds / SLA streaks:** For a time series (CPU utilization, error rates), find for each timestamp how long a metric has been at or under a threshold—useful for alerting and capacity planning.
* **Gaming leaderboards:** For each score submission, determine the consecutive previous submissions that were ≤ current—useful for streaks and reward logic.
