# Partition Equal Subset Sum

**Difficulty:** Medium
**Accuracy:** 30.24%
**Submissions:** 276K+
**Points:** 4

---

## Problem Statement

Given an array `arr[]`, determine if it can be partitioned into two subsets such that the **sum of elements in both parts is the same**.

**Note:** Each element must be in exactly one subset.

---

## Examples

### Example 1

**Input:** `arr = [1, 5, 11, 5]`
**Output:** `true`
**Explanation:** The two parts are `[1, 5, 5]` and `[11]`.

### Example 2

**Input:** `arr = [1, 3, 5]`
**Output:** `false`
**Explanation:** This array can never be partitioned into two such parts.

---

## Constraints

* `1 ≤ arr.size ≤ 100`
* `1 ≤ arr[i] ≤ 200`

---

## Expected Complexities

* **Time Complexity:** `O(sum(arr) * n)`
* **Auxiliary Space:** `O(sum(arr))`

---

## Company Tags

* `Accolite`, `Amazon`, `Microsoft`, `OYO Rooms`, `Adobe`, `Drishti-Soft`

---

## Topic Tags

* `Dynamic Programming`, `subset`, `Algorithms`

---

## Related Articles

* [Partition Problem Dp 18](https://www.geeksforgeeks.org/partition-problem-dp-18/)

---

---

Here’s an interview-ready guide to **Partition Equal Subset Sum**.

---

## 2) Explanation (what to do & why) + step-by-step dry run

### Key idea

Let `S = sum(arr)`. If `S` is **odd**, you can’t split it into two equal parts → **False**.
If `S` is even, the problem becomes: **is there a subset that sums to `target = S/2`?**

Because all numbers are **positive** (per constraints), the classic **subset-sum DP** works:

* 1-D DP: `dp[t]` = can we make sum `t` using some prefix of the array?
* Initialize `dp[0] = True`, others False.
* For each value `x`, update `dp[t] |= dp[t - x]` for `t` from `target` down to `x`.

If `dp[target]` becomes True, we can partition.

### Dry run on `arr = [1, 5, 11, 5]`

* `S = 22` (even) → `target = 11`
* Start: `dp = [True, False, …, False]` (length 12)

Process `1`:

* Update from 11→1: `dp[1] |= dp[0]` → `dp[1] = True`.

Process `5`:

* Update 11→5:

  * `dp[6] |= dp[1]` → `dp[6] = True`
  * `dp[5] |= dp[0]` → `dp[5] = True`.

Process `11`:

* Update only `t=11`: `dp[11] |= dp[0]` → **`dp[11] = True`** → early success.
  Answer: **True** (subsets `[11]` and `[1,5,5]`).

Dry run on `arr = [1, 3, 5]`

* `S = 9` (odd) → **False** immediately.

---

## 3) Python solutions (optimized + alternatives)

### A) 1-D DP (most expected in interviews)

```python
class Solution:
    def equalPartition(self, arr):
        """
        1-D subset-sum DP to reach total/2.
        Time:  O(n * target)   where target = sum(arr)//2
        Space: O(target)
        """
        total = sum(arr)
        # odd total can't be split equally
        if total & 1:
            return False
        target = total // 2

        # dp[t] == True if some subset makes sum t
        dp = [False] * (target + 1)
        dp[0] = True  # empty subset makes 0

        for x in arr:
            # iterate backwards so each number is used at most once
            for t in range(target, x - 1, -1):
                if dp[t - x]:
                    dp[t] = True
            if dp[target]:               # early exit optimization
                return True

        return dp[target]
```

### B) Bitset trick (super compact & fast in Python)

Use a single integer as a bitset; shift by `x` and OR.

```python
class SolutionBitset:
    def equalPartition(self, arr):
        """
        Bitset subset-sum: maintain reachable sums in bits of an integer.
        Time:  O(n * target/word) (very fast in Python due to C bigints)
        Space: O(target/word)
        """
        total = sum(arr)
        if total & 1:
            return False
        target = total // 2

        bits = 1  # bit 0 set => sum 0 reachable
        for x in arr:
            bits |= (bits << x)          # add x to all existing sums
            if (bits >> target) & 1:     # early exit: target reachable
                return True
        return ((bits >> target) & 1) == 1
```

### C) Top-down recursion with memo (clear logic, exponential without memo)

```python
from functools import lru_cache

class SolutionMemo:
    def equalPartition(self, arr):
        """
        DFS + memo on (i, t): can we reach sum t using items from i..end?
        Time:  O(n * target) states
        Space: O(n * target) memo + recursion depth O(n)
        """
        total = sum(arr)
        if total & 1:
            return False
        target = total // 2

        @lru_cache(None)
        def dfs(i, t):
            if t == 0:          # reached target
                return True
            if i == len(arr) or t < 0:
                return False
            # choose or skip current element
            return dfs(i + 1, t - arr[i]) or dfs(i + 1, t)

        return dfs(0, target)
```

---

## 4) Interviewer-style Q\&A

**Q1. Why is `sum(arr)` being odd a hard “no”?**
Because two equal integers must sum to an **even** number. If total is odd, it’s impossible to split into two equal integer sums.

**Q2. Why do we iterate the DP array **backwards** for the 1-D approach?**
To ensure each number is used **at most once**. Forward iteration would allow reusing the same element multiple times (unbounded knapsack behavior).

**Q3. Complexity?**

* 1-D DP: `O(n * target)` time and `O(target)` space; with `target = sum/2`.
* Bitset: very fast in practice; still conceptually `O(n * target/word)`.

**Q4. Are negatives allowed?**
No (per constraints). With negatives, subset-sum needs different handling; these methods assume **nonnegative** integers.

**Q5. What about zeros in the array?**
Zeros don’t change the target but can multiply the number of subsets; DP still works (backward pass preserves correctness).

**Q6. Can we reconstruct the actual subsets?**
Yes—augment DP to track choices or reconstruct by walking back from `dp[target]`. For interviews, returning **True/False** is enough unless asked.

**Q7. When would you choose the bitset method?**
When `target` is up to a few tens of thousands and you want a concise, fast solution in Python; big-int bit operations are implemented in C and are very efficient.

---

---

Here’s a **full, runnable Python program** for **Partition Equal Subset Sum** that:

* implements the classic **1-D DP** solution (plus a fast **bitset** variant),
* prints **inputs & outputs** for sample cases,
* and **benchmarks** the algorithm with `timeit` directly in `main`.

```python
#!/usr/bin/env python3
"""
Partition Equal Subset Sum
--------------------------
Given arr[] of positive ints, decide if it can be split into two subsets
with equal sum. Equivalent to: is there a subset that sums to total//2?

Primary solution below: 1-D subset-sum DP.

Big-O overview:
  n  := len(arr)
  S  := sum(arr)
  T  := S // 2 (target)

  DP time   : O(n * T)
  DP space  : O(T)

We also include a very fast bitset implementation using Python bigints.
"""

from __future__ import annotations
import random
import timeit
from typing import List


# -----------------------------------------------------------------------------
# Main interview solution: 1-D subset-sum DP (backward iteration)
# -----------------------------------------------------------------------------
class Solution:
    def equalPartition(self, arr: List[int]) -> bool:
        """
        Decide if arr can be partitioned into two subsets with equal sum.

        Steps:
          A) total = sum(arr)                                  -> Time O(n), Space O(1)
             If total is odd: impossible, return False         -> O(1)
             target = total // 2                               -> O(1)

          B) dp array of size target+1, dp[0] = True           -> Time O(target), Space O(target)
             Meaning: dp[t] == True if a subset sums to t.

          C) For each x in arr:
               For t from target down to x:                    -> Total Time O(n * target)
                 if dp[t - x] is True: set dp[t] = True        -> O(1) per state
               Early exit: if dp[target] becomes True          -> best-case early stop

          D) return dp[target]                                  -> O(1)

        Overall:
          Time  : O(n * target)  (target = sum(arr)//2)
          Space : O(target)
        """
        total = sum(arr)                          # A) O(n)
        if total & 1:                             # odd total cannot be split
            return False
        target = total // 2

        # B) initialize DP bitset as boolean list
        dp = [False] * (target + 1)
        dp[0] = True

        # C) process each value exactly once (0/1 knapsack)
        for x in arr:
            # iterate backwards to avoid reusing the same element
            for t in range(target, x - 1, -1):
                if dp[t - x]:
                    dp[t] = True
            if dp[target]:                        # early success
                return True

        # D)
        return dp[target]


# -----------------------------------------------------------------------------
# Fast variant: bitset subset-sum using Python bigints (one-liner core)
# -----------------------------------------------------------------------------
class SolutionBitset:
    def equalPartition(self, arr: List[int]) -> bool:
        """
        Maintain reachable sums in bits of an integer:
          bits has bit k set <=> sum k is reachable.

        Steps:
          - bits starts with 1 (only sum 0 reachable).
          - For each x: bits |= (bits << x)  (add x to all reachable sums)
          - Check if bit 'target' becomes 1.

        Time  : roughly O(n * target / word_size) but *very fast* in Python
        Space : O(target / word_size) inside big-int
        """
        total = sum(arr)
        if total & 1:
            return False
        target = total // 2

        bits = 1                                   # bit 0 set (sum 0)
        for x in arr:
            bits |= (bits << x)
            if (bits >> target) & 1:               # early exit
                return True
        return ((bits >> target) & 1) == 1


# -----------------------------------------------------------------------------
# Demo & Benchmark helpers
# -----------------------------------------------------------------------------
def demo_on_samples() -> None:
    """
    Print inputs and outputs for a few sample arrays.
    Time: small; each call bounded by O(n * target) for that case.
    """
    cases = [
        [1, 5, 11, 5],        # True  -> [1,5,5] vs [11]
        [1, 3, 5],            # False -> total odd
        [2, 2, 3, 5],         # True  -> [2,3] vs [2,5]
        [1, 2, 3, 5],         # False -> target 5 not reachable
        [100, 100],           # True  -> [100] vs [100]
        [2] * 10 + [3] * 10,  # True  -> many solutions
    ]
    sol = Solution()
    print("=== Sample Runs (Input → Output) ===")
    for arr in cases:
        ans = sol.equalPartition(arr)              # O(n * target)
        print(f"Input : {arr}")
        print(f"Output: {ans}")
        print("-" * 60)


def _bench_dp(arr: List[int]) -> None:
    """Timeit target: run DP solution once on provided arr (O(n * target))."""
    Solution().equalPartition(arr)


def _bench_bitset(arr: List[int]) -> None:
    """Timeit target: run bitset solution once."""
    SolutionBitset().equalPartition(arr)


def _make_even_sum_case(n: int, low: int, high: int, rng: random.Random) -> List[int]:
    """
    Make a random test case with even total (to avoid trivial early False).
    Time: O(n)
    """
    while True:
        arr = [rng.randint(low, high) for _ in range(n)]
        if sum(arr) % 2 == 0:
            return arr


def benchmark() -> None:
    """
    Benchmark both implementations using timeit.

    We generate a random case within constraints:
      1 <= n <= 100,  1 <= arr[i] <= 200
    Pick n=100, values up to 200 -> target up to 10,000 (typical).
    """
    rng = random.Random(2025)
    n, low, high = 100, 1, 200
    arr = _make_even_sum_case(n, low, high, rng)   # O(n)

    # Warm-up correctness check (not timed)
    assert Solution().equalPartition(arr) == SolutionBitset().equalPartition(arr)

    runs = 3
    t_dp = timeit.timeit(lambda: _bench_dp(arr), number=runs)
    t_bs = timeit.timeit(lambda: _bench_bitset(arr), number=runs)

    print("=== Benchmark ===")
    print(f"Array size n : {n} (values in [{low}, {high}], even total)")
    print(f"Runs         : {runs}")
    print(f"DP     total : {t_dp:.6f} s   | avg/run: {t_dp / runs:.6f} s")
    print(f"Bitset total : {t_bs:.6f} s   | avg/run: {t_bs / runs:.6f} s")
    print("-" * 60)


def main() -> None:
    # 1) Show outputs for sample inputs (includes input values and outputs)
    demo_on_samples()

    # 2) Benchmark the implementations using timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (short & important)

1. **Load/Resource Balancing**
   Split jobs, files, or users into two buckets with **equal total weight** (e.g., sharding, dual server assignment). The feasibility check is exactly subset-sum to half of the total.

2. **Finance / Portfolio Split**
   Partition a set of positions (positive notionals) into two books with **equal exposure** to simplify migration, A/B testing, or risk parity experiments.

3. **Manufacturing / Logistics**
   Divide items (with weights or volumes) into two shipments with equal total load to satisfy **truck capacity** or **counterweight** requirements.

4. **Team Formation / Fairness**
   Assign participants with skill ratings into two teams of *as equal strength as possible*. The exact equality check is this partition problem; (near-equality uses knapsack variants).
