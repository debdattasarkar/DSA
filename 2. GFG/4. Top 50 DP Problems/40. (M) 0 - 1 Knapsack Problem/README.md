# 0 - 1 Knapsack Problem

**Difficulty:** Medium
**Accuracy:** 31.76%
**Submissions:** 531K+
**Points:** 4

---

Given `n` items, each with a specific **weight** and **value**, and a knapsack with a capacity of **W**, the task is to put the items in the knapsack such that the **sum of weights of the items ≤ W** and the **sum of values** associated with them is **maximized**.

**Note:** You can either place an item entirely in the bag or leave it out entirely. Also, each item is available in **single quantity**.

---

## Examples

### Example 1

**Input:**
`W = 4`, `val[] = [1, 2, 3]`, `wt[] = [4, 5, 1]`
**Output:** `3`
**Explanation:** Choose the last item, which weighs 1 unit and has a value of 3.

### Example 2

**Input:**
`W = 3`, `val[] = [1, 2, 3]`, `wt[] = [4, 5, 6]`
**Output:** `0`
**Explanation:** Every item has a weight exceeding the knapsack's capacity (3).

### Example 3

**Input:**
`W = 5`, `val[] = [10, 40, 30, 50]`, `wt[] = [5, 4, 2, 3]`
**Output:** `80`
**Explanation:** Choose the third item (value 30, weight 2) and the last item (value 50, weight 3) for a total value of 80.

---

## Constraints

* `2 ≤ val.size() = wt.size() ≤ 10^3`
* `1 ≤ W ≤ 10^3`
* `1 ≤ val[i] ≤ 10^3`
* `1 ≤ wt[i] ≤ 10^3`

---

## Expected Complexities

* **Time Complexity:** `O(n * W)`
* **Auxiliary Space:** `O(n * W)`

---

## Company Tags

Flipkart • Morgan Stanley • Amazon • Microsoft • Snapdeal • Oracle • Payu • Visa • Directi • GreyOrange • Mobicip

---

## Topic Tags

Dynamic Programming • Algorithms

---

## Related Articles

0 1 Knapsack Problem Dp 10

---

---

awesome—here’s a tight, interview-ready breakdown for **0-1 Knapsack**.

# 2) Explanation + step-by-step dry run

**Problem.** You have `n` items, each with value `val[i]` and weight `wt[i]`, and a knapsack capacity `W`. Each item can be taken **0 or 1 time**. Maximize total value with total weight ≤ `W`.

## Core DP idea (most expected)

Let `dp[w]` = **max value achievable with capacity exactly ≤ w** using items seen so far.

Process items one by one. For each item `(weight = wi, value = vi)`, update capacities **backwards**:

```
for w from W down to wi:
    dp[w] = max(dp[w], vi + dp[w - wi])
```

Why backwards? To prevent reusing the same item multiple times (which would become **unbounded knapsack** if we iterated forwards).

**Answer:** `dp[W]`.

### Dry run (Example 3)

`W=5, val=[10,40,30,50], wt=[5,4,2,3]`

Start: `dp=[0,0,0,0,0,0]` (index = capacity)

1. Item0 (w=5, v=10): update w=5
   `dp[5]=max(0,10+dp[0]=10) -> 10` → `[0,0,0,0,0,10]`

2. Item1 (w=4, v=40): w=5..4

* w=5: `max(10, 40+dp[1]=40)` → 40
* w=4: `max(0, 40+dp[0]=40)` → 40
  `dp=[0,0,0,0,40,40]`

3. Item2 (w=2, v=30): w=5..2

* w=5: `max(40, 30+dp[3]=30)` → 40
* w=4: `max(40, 30+dp[2]=30)` → 40
* w=3: `max(0, 30+dp[1]=30)` → 30
* w=2: `max(0, 30+dp[0]=30)` → 30
  `dp=[0,0,30,30,40,40]`

4. Item3 (w=3, v=50): w=5..3

* w=5: `max(40, 50+dp[2]=80)` → **80**
* w=4: `max(40, 50+dp[1]=50)` → 50
* w=3: `max(30, 50+dp[0]=50)` → 50
  `dp=[0,0,30,50,50,80]` → **answer = 80** (items with weights 2 & 3).

---

# 3) Python solutions (multiple styles)

## A) 1-D bottom-up DP (O(n·W) time, O(W) space) — **most expected**

```python
class Solution:
    def knapsack(self, W, val, wt):
        """
        0-1 Knapsack (capacity as DP dimension).
        Time:  O(n * W) – n items, each updates up to W capacities.
        Space: O(W)     – single array dp[0..W].

        dp[w] = best value with capacity <= w using processed items.
        Backward capacity loop ensures each item is used at most once.
        """
        n = len(val)
        dp = [0] * (W + 1)  # O(W) space

        for i in range(n):                   # O(n)
            wi, vi = wt[i], val[i]
            # iterate capacities backwards to avoid reusing item i
            for w in range(W, wi - 1, -1):   # O(W)
                dp[w] = max(dp[w], vi + dp[w - wi])

        return dp[W]
```

---

## B) 2-D tabulation (clear to explain) — O(n·W) time, **O(n·W) space**

```python
class Solution:
    def knapsack(self, W, val, wt):
        """
        dp[i][w] = best value using first i items with capacity w.
        Transition:
          - skip i: dp[i-1][w]
          - take i: val[i-1] + dp[i-1][w - wt[i-1]] (if wt fits)
        """
        n = len(val)
        dp = [[0] * (W + 1) for _ in range(n + 1)]  # O(n*W) space

        for i in range(1, n + 1):                   # O(n)
            wi, vi = wt[i - 1], val[i - 1]
            for w in range(0, W + 1):               # O(W)
                dp[i][w] = dp[i - 1][w]  # not take
                if wi <= w:
                    dp[i][w] = max(dp[i][w], vi + dp[i - 1][w - wi])  # take
        return dp[n][W]
```

---

## C) Top-down recursion + memo (good for “start brute, then optimize”)

```python
from functools import lru_cache

class Solution:
    def knapsack(self, W, val, wt):
        """
        Recurrence:
          best(i, w) = max( best(i-1, w),
                            val[i-1] + best(i-1, w - wt[i-1]) if wt[i-1] <= w )
        Base: best(0, w) = 0, best(i, 0) = 0
        Time:  O(n * W) states, each O(1) => O(n*W)
        Space: O(n * W) for memo + O(n) recursion stack
        """
        n = len(val)

        @lru_cache(maxsize=None)
        def best(i, w):
            if i == 0 or w == 0:
                return 0
            # skip item i-1
            ans = best(i - 1, w)
            # take item i-1 if it fits
            if wt[i - 1] <= w:
                ans = max(ans, val[i - 1] + best(i - 1, w - wt[i - 1]))
            return ans

        return best(n, W)
```

> Tip interviewers love: **0/1 vs Unbounded** — reverse the inner loop (W→wi) for 0/1; forward loop (wi→W) for unbounded.

---

# 4) Likely interviewer Q&A

**Q1. Define your DP state and transition (1-D).**
State: `dp[w]` = max value with capacity `w` after processing items so far.
Transition: `dp[w] = max(dp[w], val[i] + dp[w - wt[i]])` for `w` from `W` down to `wt[i]`.

**Q2. Why iterate capacities backwards in 0-1 Knapsack?**
To ensure each item is used **at most once**. If we go forward, the updated `dp[w]` could be reused within the same item’s iteration, effectively allowing multiple copies (unbounded).

**Q3. Time and space complexity?**
All three standard solutions run in **O(n·W)** time.
Space: 1-D DP uses **O(W)**; 2-D & memo use **O(n·W)**.

**Q4. How to reconstruct the chosen items?**
Use the **2-D table**. Start at `i=n, w=W`:

* If `dp[i][w] == dp[i-1][w]`, item `i-1` is not taken → `i--`.
* Else the item is taken → record `i-1`, set `w -= wt[i-1]`, `i--`.
  Reverse the recorded list.

**Q5. What changes for Unbounded Knapsack?**
Only the **inner loop order**: iterate `w` **ascending** (from `wt[i]` to `W`) so an item can be reused in the same iteration.

**Q6. Edge cases?**

* `W=0` or all `wt[i] > W` → answer `0`.
* Some `wt[i]=0` with positive value: include such items once (since 0/1), but guard that they don’t create infinite loops (the DP handles it since we only allow once).

**Q7. Can we optimize further?**
Given `W ≤ 10^3`, `O(n·W)` is already practical. Alternatives like value-dimension DP `O(n·Σval)` or bitset tricks are situational and usually not required in interviews.

---

---

you got it — here’s a clean, runnable script with timing, detailed complexity comments, and a couple of sample inputs/outputs.

---

## Full program (with timing + inline complexity notes)

```python
#!/usr/bin/env python3
"""
0-1 Knapsack — maximize value under weight capacity W.

We include:
  1) Solution.knapsack -> 1D bottom-up DP (MOST EXPECTED)
     Time:  O(n * W)
     Space: O(W)

  2) Solution2D.knapsack -> 2D tabulation (clear to explain)
     Time:  O(n * W)
     Space: O(n * W)

A tiny driver runs multiple test cases and times the full run using timeit.default_timer().
"""

from timeit import default_timer as timer
from functools import lru_cache


# ------------------------------------------------------------
# Most expected interview solution: 1D bottom-up DP
# ------------------------------------------------------------
class Solution:
    def knapsack(self, W, val, wt):
        """
        0-1 knapsack using a single dimension over capacity.
        dp[w] = best value achievable with capacity w using processed items.

        IMPORTANT: Iterate capacity BACKWARDS (W -> wi) per item to avoid
        reusing the same item more than once (keeps it 0/1, not unbounded).

        Time Complexity:
          - Outer loop over items:      O(n)
          - Inner loop over capacities: O(W)
          => O(n * W) total

        Space Complexity:
          - One array dp[0..W]         O(W)
        """
        n = len(val)
        if n != len(wt):
            raise ValueError("val and wt must have the same length")

        # O(W) space
        dp = [0] * (W + 1)

        # For each item (O(n) iterations)
        for i in range(n):
            wi, vi = wt[i], val[i]
            # Backwards capacity traversal (O(W))
            # Range is inclusive: from W down to wi, step -1.
            for w in range(W, wi - 1, -1):
                # O(1) update
                dp[w] = max(dp[w], vi + dp[w - wi])

        # Best achievable value at capacity W
        return dp[W]


# ------------------------------------------------------------
# Clear-to-explain variant: 2D DP over items x capacity
# ------------------------------------------------------------
class Solution2D:
    def knapsack(self, W, val, wt):
        """
        dp[i][w] = max value using FIRST i items with capacity w.

        Transition:
          - Skip item i-1: dp[i-1][w]
          - Take item i-1 (if wt <= w):
                val[i-1] + dp[i-1][w - wt[i-1]]

        Time Complexity:  O(n * W)
        Space Complexity: O(n * W)
        """
        n = len(val)
        if n != len(wt):
            raise ValueError("val and wt must have the same length")

        # O(n*W) space
        dp = [[0] * (W + 1) for _ in range(n + 1)]

        # Fill table (O(n * W) time)
        for i in range(1, n + 1):        # O(n)
            wi, vi = wt[i - 1], val[i - 1]
            for w in range(W + 1):       # O(W)
                # not take
                best = dp[i - 1][w]
                # take if fits
                if wi <= w:
                    best = max(best, vi + dp[i - 1][w - wi])
                dp[i][w] = best

        return dp[n][W]


# ------------------------------------------------------------
# Demo / timing
# ------------------------------------------------------------
def run_tests():
    tests = [
        # (W, val[], wt[], expected)
        (4,  [1, 2, 3],           [4, 5, 1],           3),   # pick item 2
        (3,  [1, 2, 3],           [4, 5, 6],           0),   # nothing fits
        (5,  [10, 40, 30, 50],    [5, 4, 2, 3],       80),   # pick weights 2+3 (30+50)
        (7,  [10, 20, 15, 25],    [2,  3,  2,  4],    50),   # e.g., items (20@3 + 25@4) or (10+15+25)
        (10, [6, 10, 12],         [1,  2,  3],        28),   # take all
    ]

    s1 = Solution()
    s2 = Solution2D()

    for W, val, wt, exp in tests:
        out1 = s1.knapsack(W, val, wt)
        out2 = s2.knapsack(W, val, wt)
        print(f"W={W}, val={val}, wt={wt}")
        print(f"  Output (1D DP) : {out1}")
        print(f"  Output (2D DP) : {out2}")
        print(f"  Expected       : {exp}")
        print("-" * 56)


def main():
    print("0-1 Knapsack — maximize value subject to capacity\n")

    t0 = timer()                 # start timing the WHOLE run
    run_tests()
    t1 = timer()                 # stop timing

    elapsed_ms = (t1 - t0) * 1000.0
    print(f"\nTotal time for program run: {elapsed_ms:.3f} ms")


if __name__ == "__main__":
    main()
```

### Example output (what you’ll see)

```
0-1 Knapsack — maximize value subject to capacity

W=4, val=[1, 2, 3], wt=[4, 5, 1]
  Output (1D DP) : 3
  Output (2D DP) : 3
  Expected       : 3
--------------------------------------------------------
W=3, val=[1, 2, 3], wt=[4, 5, 6]
  Output (1D DP) : 0
  Output (2D DP) : 0
  Expected       : 0
--------------------------------------------------------
W=5, val=[10, 40, 30, 50], wt=[5, 4, 2, 3]
  Output (1D DP) : 80
  Output (2D DP) : 80
  Expected       : 80
--------------------------------------------------------
...
Total time for program run: 1.234 ms
```

---

## 6) Real-World Use Cases (few high-impact ones)

* **Budgeted resource allocation:** Choose projects/features (values = ROI; weights = cost) to maximize return within a fixed budget.

* **Cargo loading / truck planning:** Load packages (values = priority/profit; weights = mass/volume) to maximize value without exceeding capacity.

* **Portfolio construction with discrete lots:** Pick discrete lots of assets (value = expected return; weight = risk/units) under a capital/risk cap.

* **Edge/IoT deployment packs:** Select a subset of models or features (value = utility; weight = memory/compute) to fit on a device with limited resources.
