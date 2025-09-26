# The Painter’s Partition Problem–II

**Difficulty:** Hard
**Accuracy:** 27.52%
**Submissions:** 156K+
**Points:** 8

---

## Problem Statement

Given an array `arr[]` where each element denotes the length of a board, and an integer `k` representing the number of painters available. Each painter takes **1 unit of time** to paint **1 unit length** of a board.

Determine the **minimum** amount of time required to paint all the boards, under the constraint that each painter can paint **only a contiguous sequence of boards** (no skipping or splitting allowed).

---

## Examples

### Example 1

**Input:** `arr[] = [5, 10, 30, 20, 15],  k = 3`
**Output:** `35`
**Explanation:**
The optimal allocation of boards among 3 painters is –

* Painter 1 → `[5, 10]` → time = `15`
* Painter 2 → `[30]` → time = `30`
* Painter 3 → `[20, 15]` → time = `35`
  Job will be done when all painters finish i.e. at time = `max(15, 30, 35) = 35`.

---

### Example 2

**Input:** `arr[] = [10, 20, 30, 40],  k = 2`
**Output:** `60`
**Explanation:**
A valid optimal partition is –

* Painter 1 → `[10, 20, 30]` → time = `60`
* Painter 2 → `[40]` → time = `40`
  Job will be complete at time = `max(60, 40) = 60`.

---

### Example 3

**Input:** `arr[] = [100, 200, 300, 400],  k = 1`
**Output:** `1000`
**Explanation:**
There is only one painter, so the painter must paint all boards sequentially. The total time taken will be the sum of all board lengths, i.e., `100 + 200 + 300 + 400 = 1000`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^4`
* `1 ≤ k ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n * log(sum(arr)))`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* Microsoft
* Google
* Codentation

---

## Topic Tags

* Searching
* Dynamic Programming
* Divide and Conquer
* Binary Search
* Algorithms

---

## Related Articles

* [Painters Partition Problem](https://www.geeksforgeeks.org/painters-partition-problem/)

---

---

awesome—let’s make **Painter’s Partition Problem–II** rock-solid for interviews.

---

# 2) Explanation + step-by-step dry run

## Goal

Given board lengths `arr` and `k` painters (each paints **contiguous** boards, 1 unit length per unit time), find the **minimum possible finishing time** (i.e., the minimum achievable **maximum load** among painters).

This is a classic **minimize the maximum subarray sum** with exactly/at-most `k` partitions.

## Key observation (monotonicity)

If we can finish within time `T`, then we can definitely finish within any time `T' ≥ T`.
So the predicate **“is it possible in ≤ T?”** is **monotone** → perfect for **binary search on the answer**.

### Feasibility check (greedy is optimal)

Given a candidate limit `T`, pack boards greedily to minimize painters used:

```
painters = 1
curr = 0
for each length L in arr:
    if L > T:  # impossible: a single board exceeds limit
        return False
    if curr + L <= T:
        curr += L                 # keep assigning to current painter
    else:
        painters += 1             # start a new painter
        curr = L
return painters <= k
```

This greedy packing minimizes painters for a fixed `T` (tightest packing).

### Bounds for binary search

* Lower bound `lo = max(arr)`  (no painter can do less than the largest single board)
* Upper bound `hi = sum(arr)`  (one painter does everything)

Binary search on `[lo, hi]`, tightening with the predicate above.

---

## Dry run (arr = [5,10,30,20,15], k = 3)

* `lo = 30`, `hi = 80`.
* `mid = 55`: greedy ⇒ painters used = 2 ⇒ feasible → `hi = 55`.
* `mid = (30+55)//2 = 42`: painters = 3 ⇒ feasible → `hi = 42`.
* `mid = 36`: painters = 3 ⇒ feasible → `hi = 36`.
* `mid = 33`: painters = 4 ⇒ not feasible → `lo = 34`.
* `mid = 35`: painters = 3 ⇒ feasible → `hi = 35`.
* `mid = 34`: painters = 4 ⇒ not feasible → `lo = 35`.

End: `lo == hi == 35` → **answer = 35**.

---

# 3) Python solutions (three ways, with inline interview notes)

Required signature:

```python
class Solution:
    def minTime (self, arr, k):
        # code here
```

## A) Binary search on answer + greedy check (most expected) — **O(n log S)**

```python
class Solution:
    def minTime(self, arr, k):
        """
        Binary search the minimal feasible 'max load' (time).
        Predicate: can we partition arr into at most k contiguous groups
                    so that each group's sum <= T ?
        Time : O(n * log(sum(arr)))     -- predicate is O(n), ~log range checks
        Space: O(1)
        """
        n = len(arr)
        if n == 0:
            return 0
        # If painters >= boards, each painter can take at most one board
        # -> the time is the largest board.
        if k >= n:
            return max(arr)

        lo, hi = max(arr), sum(arr)

        def feasible(T: int) -> bool:
            painters = 1
            curr = 0
            for L in arr:
                if L > T:             # single board too large
                    return False
                if curr + L <= T:     # keep filling current painter
                    curr += L
                else:                 # need a new painter
                    painters += 1
                    curr = L
                    if painters > k:  # early exit
                        return False
            return True

        # standard lower-bound binary search
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

---

## B) DFS + memo (DP over split points, educational) — **O(k·n²)**

```python
from functools import lru_cache
from itertools import accumulate

class SolutionDFS:
    def minTime(self, arr, k):
        """
        Let sum(i,j) be total from arr[i..j] (prefix sums).
        dp(i, p) = minimal possible max-load to paint arr[i..] with p painters,
                   each painting a contiguous block.
        Transition:
            dp(i, 1) = sum(i, n-1)             # last painter gets all remaining
            dp(i, p) = min over j>=i:
                        max( sum(i, j), dp(j+1, p-1) )
        Time : O(k * n^2)   (n choices for j per state)
        Space: O(k * n)
        """
        n = len(arr)
        pref = [0] + list(accumulate(arr))

        def seg_sum(i, j):
            return pref[j + 1] - pref[i]

        @lru_cache(None)
        def dp(i, p):
            if p == 1:
                return seg_sum(i, n - 1)
            best = float('inf')
            # j can go until there are enough boards left for (p-1) painters
            # -> at least one board per remaining painter
            limit = n - (p - 1)
            for j in range(i, limit):
                first = seg_sum(i, j)
                rest  = dp(j + 1, p - 1)
                best = min(best, max(first, rest))
            return best

        return dp(0, k)
```

> Works well for small/medium `n`, but with `n` up to `1e5` the **binary search** approach is required.

---

## C) Plain brute-force backtracking (exponential) — for completeness

```python
class SolutionBrute:
    def minTime(self, arr, k):
        """
        Try all placements of k-1 partition bars between boards.
        Exponential in n; only for demonstration on tiny inputs.
        """
        n = len(arr)
        best = float('inf')

        def backtrack(i, painters_left, curr_max, running_sum):
            nonlocal best
            if i == n:
                # last painter gets 'running_sum'
                best = min(best, max(curr_max, running_sum))
                return
            # Option 1: continue current painter
            backtrack(i + 1, painters_left, curr_max, running_sum + arr[i])
            # Option 2: cut here (if we still can)
            if painters_left > 1:
                backtrack(i + 1, painters_left - 1,
                          max(curr_max, running_sum + arr[i]), 0)

        backtrack(0, k, 0, 0)
        return best
```

---

# 4) Interview Q&A (high-yield)

**Q1. Why is greedy packing correct in the feasibility check?**
Because for a fixed limit `T`, putting as many boards as possible on the current painter **minimizes the number of painters used**. Any earlier cut would only increase painters or keep them equal.

**Q2. Why are the binary-search bounds `max(arr)` and `sum(arr)`?**

* No painter can do less time than the largest single board → lower bound.
* One painter does all boards in `sum(arr)` time → upper bound.

**Q3. Complexity of the optimal approach?**
Predicate is `O(n)`. Range size is up to `sum(arr) − max(arr)`; binary search adds a factor `log(sum)`. Overall **`O(n log(sum(arr)))`** time, **`O(1)`** extra space.

**Q4. What about `k >= n` and `k == 1` edge cases?**

* `k >= n` ⇒ each painter can take ≤ 1 board → time is `max(arr)`.
* `k == 1` ⇒ one painter paints everything → time is `sum(arr)`.

**Q5. Why must segments be contiguous?**
It’s a constraint of the problem (realistic: a painter paints a continuous range of boards). The DP and greedy packing both enforce contiguity naturally.

**Q6. Can painters have different speeds?**
Common variant: painting time per unit is `t` (or per-painter speeds). If constant `t`, multiply the final time by `t`. With heterogeneous speeds, the problem changes and the greedy predicate needs adjustment.

**Q7. Relation to other problems?**
Exactly the same pattern as **Split Array Largest Sum** (LeetCode 410): minimize the largest partition sum with `k` splits.

---

---

you got it — here’s a **ready-to-run program** for **The Painter’s Partition Problem–II** that:

* reads the boards array and `k` from stdin,
* solves it with **three approaches**

  1. **Binary search + greedy feasibility** (optimal for large inputs),
  2. **DP O(k·n²)** (educational; enabled for small `n`),
  3. **Brute partition backtracking** (tiny inputs only),
* prints the **result of each** and **times** them using `timeit`.

I’ve put **tight time/space notes** inline right where the logic happens.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Painter's Partition Problem – II
# Each painter paints contiguous boards. 1 unit length takes 1 unit time.
# Goal: minimize the finishing time = minimize the maximum load among painters.
#
# Methods:
#   1) Binary search on answer + greedy feasibility  <-- Recommended
#        Time:  O(n * log(sum(arr)))     Space: O(1)
#   2) DP (k groups, prefix sums, split points)      <-- Educational
#        Time:  O(k * n^2)               Space: O(k * n)
#   3) Brute force backtracking over cuts            <-- Tiny inputs only
#        Time:  Exponential                 Space: O(n) recursion
#
# Input (stdin):
#   Line 1: board lengths, space/comma separated (brackets allowed)
#   Line 2: k (number of painters)
#
# Output:
#   - Echo of input summary
#   - Answer and timing for each method (skipping slow ones on big n)
# ------------------------------------------------------------

import sys
import timeit
from functools import lru_cache
from itertools import accumulate

# --------------------- Method 1: Binary search + greedy ---------------------
class Solution:
    def minTime(self, arr, k):
        """
        Binary-search the minimal feasible 'max load' (finishing time).
        Feasibility(T): greedily pack contiguous boards into the current painter
                        until adding next board would exceed T; then start a new
                        painter. If painters used <= k, T is feasible.

        Time : O(n * log(sum(arr)))  -- predicate is O(n); ~log range checks
        Space: O(1)
        """
        n = len(arr)
        if n == 0:
            return 0
        # If painters >= boards, each painter can take at most one board
        # -> finishing time is the largest single board.
        if k >= n:
            return max(arr)

        lo, hi = max(arr), sum(arr)  # tight bounds

        def feasible(T: int) -> bool:
            painters = 1
            curr = 0
            for L in arr:
                if L > T:                 # a single board is too large -> impossible
                    return False
                if curr + L <= T:         # extend current painter's load
                    curr += L
                else:                     # start a new painter
                    painters += 1
                    curr = L
                    if painters > k:      # early stop
                        return False
            return True

        # Lower-bound binary search
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


# --------------------- Method 2: DP (k * n^2) with prefix sums ---------------------
class SolutionDP:
    def minTime(self, arr, k):
        """
        dp[p][i] = minimal possible max-load to paint first i boards with p painters.
        Transition:
            dp[1][i] = prefix_sum(i)                  -- one painter takes all
            dp[p][i] = min_{0<=j<i} max(dp[p-1][j], prefix_sum(i)-prefix_sum(j))
                        (j = split point; last painter gets j..i-1)
        Time : O(k * n^2)  -- each state scans j in [0..i-1]
        Space: O(k * n)
        """
        n = len(arr)
        if n == 0:
            return 0
        # Cap painters at n (more painters than boards doesn't help)
        k = min(k, n)

        pref = [0] + list(accumulate(arr))  # prefix sums, O(n)
        def seg_sum(i, j):  # sum of arr[i..j], inclusive
            return pref[j + 1] - pref[i]

        # dp table (k+1) x (n+1); dp[p][0] = 0 for all p
        INF = 10**18
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        for p in range(1, k + 1):
            dp[p][0] = 0
        # Base: one painter
        for i in range(1, n + 1):
            dp[1][i] = pref[i]

        # Fill for p >= 2
        for p in range(2, k + 1):
            for i in range(1, n + 1):
                # j must leave at least (p-1) boards for earlier painters?
                # Not required for correctness, but we can prune upper bound.
                best = INF
                # Try all splits j in [0..i-1]
                for j in range(0, i):
                    first = dp[p - 1][j]
                    last  = seg_sum(j, i - 1)
                    best = min(best, max(first, last))
                dp[p][i] = best

        return dp[k][n]


# --------------------- Method 3: Brute backtracking (tiny n) ---------------------
class SolutionBrute:
    def minTime(self, arr, k):
        """
        Place k-1 cuts between boards; evaluate maximum segment sum.
        Exponential; OK for very small n (e.g., n <= 20).
        """
        n = len(arr)
        best = float('inf')

        def backtrack(i, painters_left, curr_max, running_sum):
            nonlocal best
            if i == n:
                best = min(best, max(curr_max, running_sum))
                return
            # 1) continue current segment
            backtrack(i + 1, painters_left, curr_max, running_sum + arr[i])
            # 2) cut here if we still have painters to start a new segment
            if painters_left > 1:
                backtrack(i + 1, painters_left - 1,
                          max(curr_max, running_sum + arr[i]), 0)

        backtrack(0, k, 0, 0)
        return best


# ------------------------------- I/O helpers -------------------------------
def _parse():
    """
    Reads:
      line1: array e.g. "5 10 30 20 15" or "[5,10,30,20,15]"
      line2: k
    """
    lines = [ln.strip() for ln in sys.stdin.read().splitlines() if ln.strip()]
    if len(lines) < 2:
        print("Please provide two lines:\n<boards>\n<k>")
        sys.exit(0)
    arr_line = lines[0].replace("[", " ").replace("]", " ").replace(",", " ")
    arr = [int(x) for x in arr_line.split()]
    k = int(lines[1])
    return arr, k

def _preview(arr, limit=80):
    s = " ".join(map(str, arr))
    if len(s) <= limit:
        return f"arr (n={len(arr)}): [{s}]"
    return f"arr (n={len(arr)}): [{s[:limit]}...]"

# ---------------------------------- main -----------------------------------
def main():
    arr, k = _parse()
    print(_preview(arr))
    print(f"k = {k}\n")

    sol_opt = Solution()
    t_opt = timeit.timeit(lambda: sol_opt.minTime(arr, k), number=1)
    ans_opt = sol_opt.minTime(arr, k)

    print("Binary search + greedy (O(n log sum), O(1) space):", ans_opt)
    print("Time (ms): {:.3f}\n".format(t_opt * 1000.0))

    # DP: run only for reasonably small n to avoid long runtimes
    n = len(arr)
    dp_enabled = n <= 1200 and k <= 1200  # conservative guard
    if dp_enabled:
        sol_dp = SolutionDP()
        t_dp = timeit.timeit(lambda: sol_dp.minTime(arr, k), number=1)
        ans_dp = sol_dp.minTime(arr, k)
        print("DP k*n^2 (educational)                        :", ans_dp)
        print("Time (ms): {:.3f}\n".format(t_dp * 1000.0))
    else:
        ans_dp = None
        print("DP k*n^2 (educational)                        : (skipped for large n)")

    # Brute: only for very tiny n
    brute_enabled = n <= 20
    if brute_enabled:
        sol_bt = SolutionBrute()
        t_bt = timeit.timeit(lambda: sol_bt.minTime(arr, k), number=1)
        ans_bt = sol_bt.minTime(arr, k)
        print("Brute backtracking (tiny n)                   :", ans_bt)
        print("Time (ms): {:.3f}".format(t_bt * 1000.0))
    else:
        ans_bt = None
        print("Brute backtracking (tiny n)                   : (skipped)")

    # Consistency check when possible
    agrees = True
    for val in (ans_dp, ans_bt):
        if val is not None and val != ans_opt:
            agrees = False
    print("\nAll methods agree ✔" if agrees else "\nWARNING: methods disagree!")

if __name__ == "__main__":
    main()
```

### How to run

```bash
python3 painters_partition.py
5 10 30 20 15
3
```

**Sample output (timings vary):**

```
arr (n=5): [5 10 30 20 15]
k = 3

Binary search + greedy (O(n log sum), O(1) space): 35
Time (ms): 0.090

DP k*n^2 (educational)                        : 35
Time (ms): 0.520

Brute backtracking (tiny n)                   : 35
Time (ms): 0.180

All methods agree ✔
```

Another sample:

```
python3 painters_partition.py
10 20 30 40
2
```

Output:

```
arr (n=4): [10 20 30 40]
k = 2

Binary search + greedy (O(n log sum), O(1) space): 60
Time (ms): 0.060

DP k*n^2 (educational)                        : 60
Time (ms): 0.180

Brute backtracking (tiny n)                   : 60
Time (ms): 0.070

All methods agree ✔
```

---

## 6) Real-World Use Cases (high-impact)

1. **Manufacturing/painting lines:** Assign contiguous batches of boards/panels to workers or machines so the **slowest finisher** is minimized → shorter makespan.

2. **Disk/backup chunking:** Split a large, ordered list of files/blocks (must stay in order) among `k` storage nodes/workers to balance ingestion time.

3. **Video rendering / media encoding:** Divide a timeline (contiguous segments) across render nodes; goal is to finish the whole render ASAP.

4. **ETL/data pipeline shards:** Partition a time-ordered stream into contiguous shards for `k` executors to minimize wall-clock completion.

5. **Logistics pick paths:** Assign contiguous shelf ranges in a warehouse to pickers to reduce the completion time of a wave.
