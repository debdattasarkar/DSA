# Max Sum Increasing Subsequence

**Difficulty:** Medium
**Accuracy:** 40.02%
**Submissions:** 211K+
**Points:** 4
**Average Time:** 25m

---

Given an array of positive integers `arr`. Find the **maximum sum subsequence** of the given array such that the integers in the subsequence are sorted in **strictly increasing** order i.e. a **strictly increasing subsequence**.

---

## Examples

### Example 1

**Input:** `arr[] = [1, 101, 2, 3, 100]`
**Output:** `106`
**Explanation:** The maximum sum of a increasing sequence is obtained from `[1, 2, 3, 100]`.

### Example 2

**Input:** `arr[] = [4, 1, 2, 3]`
**Output:** `6`
**Explanation:** The maximum sum of a increasing sequence is obtained from `[1, 2, 3]`.

### Example 3

**Input:** `arr[] = [4, 1, 2, 4]`
**Output:** `7`
**Explanation:** The maximum sum of a increasing sequence is obtained from `[1, 2, 4]`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^3`
* `1 ≤ arr[i] ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n^2)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* Morgan Stanley
* Amazon
* Microsoft

---

## Topic Tags

* Dynamic Programming
* Algorithms

---

## Related Articles

* Maximum Sum Increasing Subsequence Dp 14

---

---

awesome—let’s make this interview-ready.

# 2) Problem explanation + step-by-step dry run

**Goal.** Given positive integers `arr[0..n-1]`, find the **maximum sum** of a subsequence whose elements are in **strictly increasing** order.

**Classic DP idea (most expected in interviews).**

* Let `dp[i]` = **maximum sum of an increasing subsequence that ends at index `i`** (i.e., it must include `arr[i]`).
* Initialize: `dp[i] = arr[i]` (the subsequence of just that element).
* Transition: for every `j < i` with `arr[j] < arr[i]`, we can append `arr[i]` after the best sequence ending at `j`:

  ```
  dp[i] = max(dp[i], dp[j] + arr[i])
  ```
* Answer: `max(dp)`.

**Why this works.** Any optimal increasing subsequence has a **last** element at some `i`. Everything before is an optimal subsequence that ends at some `j < i` with `arr[j] < arr[i]`. We try all such `j`.

**Complexity.** Two nested loops → **O(n²)** time, **O(n)** space.

---

## Dry run on the examples

### Example 1

`arr = [1, 101, 2, 3, 100]`

We’ll compute `dp` left → right.

* `i=0` (`1`): `dp[0]=1`
* `i=1` (`101`):

  * check `j=0` (`1 < 101`): `dp[1]=max(101, dp[0]+101)=max(101, 1+101)=102`
* `i=2` (`2`):

  * `j=0` (`1 < 2`): `dp[2]=max(2, 1+2)=3`
  * `j=1` (`101 < 2`? no)
* `i=3` (`3`):

  * `j=0` (`1 < 3`): `dp[3]=max(3, 1+3)=4`
  * `j=1` (`101 < 3`? no)
  * `j=2` (`2 < 3`): `dp[3]=max(4, 3+3)=6`
* `i=4` (`100`):

  * `j=0` (`1 < 100`): `dp[4]=max(100, 1+100)=101`
  * `j=1` (`101 < 100`? no)
  * `j=2` (`2 < 100`): `dp[4]=max(101, 3+100)=103`
  * `j=3` (`3 < 100`): `dp[4]=max(103, 6+100)=106`

Final `dp = [1, 102, 3, 6, 106]`, so **answer = 106** from subsequence `[1, 2, 3, 100]`.

### Example 2

`arr = [4, 1, 2, 3]`

* `dp = [4, 1, 3, 6]` → answer **6** from `[1, 2, 3]`.

### Example 3

`arr = [4, 1, 2, 4]`

* `dp = [4, 1, 3, 5]` → answer **7** from `[1, 2, 4]` (sum 7).

---

# 3) Python solutions (multiple styles)

## A) Standard O(n²) DP (most expected)

```python
#User function Template for python3
class Solution:
    def maxSumIS(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        # dp[i] = max sum of an increasing subsequence that ends at i (must include arr[i])
        dp = arr[:]  # start with the single-element subsequence at each i

        # O(n^2) time: for each i, scan all j < i
        for i in range(n):
            for j in range(i):
                if arr[j] < arr[i]:
                    # if we can append arr[i] after arr[j], try to improve dp[i]
                    dp[i] = max(dp[i], dp[j] + arr[i])

        # overall max is the answer
        return max(dp)
```

**Time:** `O(n²)`
**Space:** `O(n)`

---

## B) Top-down recursion + memo (same DP, interview-friendly derivation)

```python
# Brute-force style recursion upgraded with memoization (becomes O(n^2))
# Use when interviewer asks you to "start recursively" and then optimize.

#User function Template for python3
class Solution:
    def maxSumIS(self, arr):
        from functools import lru_cache
        n = len(arr)

        @lru_cache(maxsize=None)
        def best_end_at(i):
            # best sum of an increasing subsequence ending at index i
            best = arr[i]  # at least take arr[i] alone
            for j in range(i):
                if arr[j] < arr[i]:
                    best = max(best, best_end_at(j) + arr[i])
            return best

        return max(best_end_at(i) for i in range(n)) if n else 0
```

**Time:** `O(n²)` (each `(i,j)` pair considered once thanks to memo)
**Space:** `O(n)` recursion + memo

---

## C) Optimized with Fenwick Tree / Segment Tree (⚡ `O(n log U)`)

When values are bounded (here `arr[i] ≤ 1e5`) or after **coordinate compression**, we can do:

* Let `dp_val[x]` = best sum of an increasing subsequence whose last value is exactly `x`.
* For each `v = arr[i]`, we need `best prefix max` over values `< v`, then set
  `candidate = prefix_max + v`, and update at index `v` with this `candidate`.
* A **Fenwick Tree** (Binary Indexed Tree) stores prefix maxima.

```python
# Fenwick tree (BIT) solution: O(n log U), where U = number of distinct values
# Works because arr[i] are positive integers (strictly increasing by value).
# If values aren't small, do coordinate compression first.

#User function Template for python3
class Solution:
    def maxSumIS(self, arr):
        if not arr:
            return 0

        # Coordinate compression to keep tree small and generic
        vals = sorted(set(arr))
        idx = {v: i+1 for i, v in enumerate(vals)}  # 1-based Fenwick

        m = len(vals)
        bit = [0]*(m+1)  # Fenwick tree storing prefix MAX (not sum!)

        def bit_query(i):
            # max over [1..i]
            res = 0
            while i > 0:
                res = max(res, bit[i])
                i -= i & -i
            return res

        def bit_update(i, val):
            # bit[i] = max(bit[i], val) for all relevant indices
            while i <= m:
                if val > bit[i]:
                    bit[i] = val
                i += i & -i

        best = 0
        for v in arr:
            pos = idx[v]
            # best subsequence sum ending with a value < v
            prefix = bit_query(pos - 1)
            cand = prefix + v
            bit_update(pos, cand)
            if cand > best:
                best = cand

        return best
```

**Time:** `O(n log n)` due to compression + Fenwick ops
**Space:** `O(n)` for tree + compression tables

> In many interviews the **O(n²)** DP is the intended solution. The Fenwick variant shows depth if asked to “optimize further.”

---

# 4) Likely interviewer Q&A

**Q1. Define your DP state and transition. Why is it correct?**
`dp[i]` = max sum of an increasing subsequence ending at `i`.
Transition: `dp[i] = arr[i] + max(dp[j])` over `j<i` with `arr[j]<arr[i]`.
Any optimal subsequence ending at `i` must come from some earlier `j` with a smaller value; we try all such `j`, hence optimal.

**Q2. Complexity of the standard DP?**
Two nested loops → `O(n²)` time; `O(n)` extra space.

**Q3. How do duplicates affect the logic?**
We require **strictly increasing**, so we only extend when `arr[j] < arr[i]` (not `<=`). Duplicates cannot be in the same subsequence unless separated by strictly larger numbers in between.

**Q4. Can we reconstruct the subsequence, not just the sum?**
Yes. Keep a `parent[i]` that stores the `j` used when updating `dp[i]`. After finishing, pick `i = argmax dp[i]` and walk parents backward to get the sequence (reverse at the end).

**Q5. Can we do better than O(n²)?**
For **LIS length**, there’s a classic `O(n log n)` method. For **maximum sum**, we can also do `O(n log n)` using a Fenwick/segment tree over value ranks to query “best sum for values < v”. This needs coordinate compression when values are large or arbitrary.

**Q6. Edge cases you considered?**

* Single element → answer is that element.
* All decreasing → answer is the max single element (since we can’t extend).
* Large values but small `n` → DP is fine; for very large `n`, prefer Fenwick.

**Q7. Why does the Fenwick approach work?**
Because the only condition to append `v` is that prior value `< v`. So we maintain, for every value rank, the **best sum achievable**. Querying a prefix `< v` gives the best we can extend; updating at `v` records the new best sum ending with value `v`.

---

---

perfect—here’s a compact, runnable package with timing and clear complexity notes.

---

## Full program (with timing + inline complexity comments)

```python
#!/usr/bin/env python3
"""
Max Sum Increasing Subsequence (MSIS)

Includes:
  * Standard O(n^2) DP solution (most expected in interviews)
  * Fenwick/BIT + coordinate compression O(n log n) variant
  * Small driver with sample inputs/outputs
  * Timing using timeit.default_timer (same clock used by timeit)
"""

from timeit import default_timer as timer


# ------------------------------------------------------------
# User function Template for python3 — O(n^2) DP (expected)
# ------------------------------------------------------------
class Solution:
    def maxSumIS(self, arr):
        """
        dp[i] = maximum sum of a strictly increasing subsequence that ENDS at i.

        Initialization:
          dp[i] = arr[i]  (the subsequence consisting of arr[i] alone)

        Transition:
          for all j < i with arr[j] < arr[i]:
              dp[i] = max(dp[i], dp[j] + arr[i])

        Answer:
          max(dp)

        Time Complexity:
          - Build dp: O(n) to init
          - Double loop: sum over i of i comparisons -> O(n^2)
          => Total O(n^2)

        Space Complexity:
          - dp array of size n -> O(n)
        """
        n = len(arr)
        if n == 0:
            return 0

        # O(n) time & O(n) space: initialize dp with each element alone
        dp = arr[:]   # dp[i] starts as arr[i]

        # O(n^2) time: nested loops over (i, j)
        for i in range(n):
            # For each i, we try all j < i (at most n-1 comparisons)
            for j in range(i):
                # Only extend if strictly increasing
                if arr[j] < arr[i]:
                    # O(1) update
                    dp[i] = max(dp[i], dp[j] + arr[i])

        # O(n) time: take max over dp
        return max(dp)


# ------------------------------------------------------------
# Optional: Fenwick (BIT) + coordinate compression — O(n log n)
# ------------------------------------------------------------
class SolutionFenwick:
    def maxSumIS(self, arr):
        """
        Coordinate-compress values, then use a Fenwick Tree (BIT) to maintain
        prefix maxima of "best sum ending with value <= x".

        For each v in arr:
          best_prefix = query(max value strictly less than v)
          cand = best_prefix + v
          update(position of v, cand)

        Time Complexity:
          - Coordinate compression: O(n log n)
          - For each element: BIT query + update: O(log n)
          => Total O(n log n)

        Space Complexity:
          - O(n) for compression maps + BIT array
        """
        if not arr:
            return 0

        # O(n log n): coordinate compression
        vals = sorted(set(arr))
        # 1-based indexing for Fenwick
        pos = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)

        # Fenwick tree for prefix MAX (not sum)
        bit = [0] * (m + 1)  # O(n) space

        def bit_query(i):
            # O(log n): max over [1..i]
            best = 0
            while i > 0:
                best = max(best, bit[i])
                i -= i & -i
            return best

        def bit_update(i, val):
            # O(log n): bit[i] = max(bit[i], val)
            while i <= m:
                if val > bit[i]:
                    bit[i] = val
                i += i & -i

        best_overall = 0

        # O(n log n): each step does two BIT ops
        for v in arr:
            p = pos[v]
            # strictly less than v -> query up to p-1
            prefix = bit_query(p - 1)
            cand = prefix + v
            bit_update(p, cand)
            if cand > best_overall:
                best_overall = cand

        return best_overall


# ------------------------------------------------------------
# Main / demo with timing
# ------------------------------------------------------------
def run_once():
    """Run a small suite once; return results for printing."""
    tests = [
        [1, 101, 2, 3, 100],  # expected 106 (1,2,3,100)
        [4, 1, 2, 3],         # expected 6   (1,2,3)
        [4, 1, 2, 4],         # expected 7   (1,2,4)
        [10],                 # expected 10
        [5, 4, 3, 2, 1],      # expected 5   (take best single)
        [1, 2, 3, 4, 5],      # expected 15  (whole array)
        [8, 12, 2, 3, 15, 5, 7],  # expected 35 (8,12,15) or (2,3,15,? ... but 35 best)
    ]

    sol = Solution()
    sol_fast = SolutionFenwick()

    outputs = []
    for arr in tests:
        ans_dp = sol.maxSumIS(arr)
        ans_fast = sol_fast.maxSumIS(arr)
        outputs.append((arr, ans_dp, ans_fast))
    return outputs


def main():
    # Time the WHOLE program run (the suite) using timeit’s default timer.
    t0 = timer()
    results = run_once()
    t1 = timer()
    elapsed_ms = (t1 - t0) * 1000.0

    # Pretty-print inputs and outputs
    print("Max Sum Increasing Subsequence — Results\n")
    for arr, ans_dp, ans_fast in results:
        print(f"Input:  {arr}")
        print(f"O(n^2) DP Output      : {ans_dp}")
        print(f"O(n log n) Fenwick Out: {ans_fast}")
        print("-" * 48)

    print(f"\nTotal time for run_once(): {elapsed_ms:.3f} ms")


if __name__ == "__main__":
    main()
```

### What you’ll see (example)

```
Max Sum Increasing Subsequence — Results

Input:  [1, 101, 2, 3, 100]
O(n^2) DP Output      : 106
O(n log n) Fenwick Out: 106
------------------------------------------------
Input:  [4, 1, 2, 3]
O(n^2) DP Output      : 6
O(n log n) Fenwick Out: 6
------------------------------------------------
...
Total time for run_once(): 1.2 ms
```

---

## 6) Real-World Use Cases (high-value)

* **Portfolio growth planning:** Choose strictly increasing “risk tiers” or “capital allocations” where each step increases risk/return and the objective is to **maximize cumulative return** under monotone constraints.

* **Career/skills roadmaps:** Select a strictly increasing sequence of skill levels/certifications with **max utility score** while respecting prerequisite ordering (strict increase captures increasing mastery).

* **Supply chain/quality ladders:** Pick components with strictly increasing quality ratings across stages to **maximize total quality** or margin in a product pipeline.

* **Energy efficiency upgrades:** Sequence upgrades with strictly increasing efficiency ratings to **maximize total savings** while respecting that each step must improve on the previous.
