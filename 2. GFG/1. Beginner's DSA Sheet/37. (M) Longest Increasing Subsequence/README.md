# Longest Increasing Subsequence

**Difficulty:** Medium
**Accuracy:** 32.8%
**Submissions:** 354K+
**Points:** 4

---

## Problem Statement

Given an array `arr[]` of non-negative integers, the task is to find the **length of the Longest Strictly Increasing Subsequence (LIS)**.

A subsequence is **strictly increasing** if each element in the subsequence is strictly less than the next element.

---

## Examples

### Example 1

**Input:** `arr[] = [5, 8, 3, 7, 9, 1]`
**Output:** `3`
**Explanation:** The longest strictly increasing subsequence could be `[5, 7, 9]`, which has a length of `3`.

### Example 2

**Input:**
`arr[] = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]`
**Output:** `6`
**Explanation:** One of the possible longest strictly increasing subsequences is `[0, 2, 6, 9, 13, 15]`, which has a length of `6`.

### Example 3

**Input:** `arr[] = [3, 10, 2, 1, 20]`
**Output:** `3`
**Explanation:** The longest strictly increasing subsequence could be `[3, 10, 20]`, which has a length of `3`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^3`
* `0 ≤ arr[i] ≤ 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* Paytm
* Amazon
* Microsoft
* OYO Rooms
* Samsung
* BankBazaar

---

## Topic Tags

* Dynamic Programming
* Binary Search
* Algorithms

---

## Related Interview Experiences

* Paytm Interview Experience Set 14 For Senior Android Developer
* Bankbazaar Com Interview Experience Set 7 Senior Android Developer

---

## Related Articles

* Longest Increasing Subsequence Dp 3

---

---

Here’s a compact, interview-ready guide for **Longest Increasing Subsequence (LIS)**.

---

## 2) Explanation (how LIS works) + step-by-step dry run

We want the **length of the longest strictly increasing subsequence** (not necessarily contiguous).

### Two classic approaches

1. **DP (O(n²))**
   Let `dp[i]` be the LIS length **ending at** index `i`.
   Recurrence: `dp[i] = 1 + max(dp[j]) for all j<i with arr[j] < arr[i]`, else `1` if none.
   Answer is `max(dp)`.

2. **Patience sorting / Tails with Binary Search (O(n log n))** — most common in interviews
   Maintain an array `tails`, where `tails[len]` is the **smallest possible tail** value of an increasing subsequence of length `len+1`.
   For each `x` in `arr`:

   * Find the first index `pos` in `tails` with `tails[pos] >= x` (**`bisect_left`**).

     * If such `pos` exists → set `tails[pos] = x` (we improved that length’s tail).
     * Else append `x` to `tails` (we extended LIS by 1).
       The size of `tails` is the LIS length.
       (Use `bisect_left` for **strictly** increasing; use `bisect_right` for **non-decreasing**.)

### Dry run with `arr = [5, 8, 3, 7, 9, 1]`

Start: `tails = []`

* `5`: `tails = [5]`              (append)
* `8`: `tails = [5, 8]`           (append)
* `3`: replace first `>=3` → index 0 ⇒ `tails = [3, 8]`
* `7`: replace first `>=7` → index 1 ⇒ `tails = [3, 7]`
* `9`: `tails = [3, 7, 9]`        (append)
* `1`: replace first `>=1` → index 0 ⇒ `tails = [1, 7, 9]`

Length of `tails` = **3**, which is the LIS length (e.g., `[5,7,9]`).

---

## 3) Python solutions (brute + optimized), interview-style

```python
from bisect import bisect_left

class Solution:
    def lis(self, arr):
        """
        O(n log n) patience-sorting style solution (length only).
        tails[i] = minimum possible tail of any increasing subsequence of length i+1.
        For each x:
          - pos = first index with tails[pos] >= x   (bisect_left for STRICTLY increasing)
          - if pos == len(tails): append x (extend LIS)
            else: replace tails[pos] = x (improve tail)
        Time:  O(n log n)
        Space: O(n)  (tails)
        """
        if not arr:
            return 0

        tails = []
        for x in arr:
            pos = bisect_left(tails, x)   # first >= x
            if pos == len(tails):
                tails.append(x)
            else:
                tails[pos] = x
        return len(tails)

    # ----- Simpler to explain but slower: O(n^2) DP -----
    def lis_dp_n2(self, arr):
        """
        dp[i] = LIS length ending at i
        dp[i] = 1 + max(dp[j]) for j<i and arr[j] < arr[i], else 1
        Time:  O(n^2)
        Space: O(n)
        """
        n = len(arr)
        if n == 0:
            return 0
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # ----- Optional: reconstruct one LIS (O(n log n) with predecessors) -----
    def lis_sequence(self, arr):
        """
        Returns one actual LIS (strictly increasing).
        Uses tails indices plus predecessor pointers.
        Time:  O(n log n) ; Space: O(n)
        """
        from bisect import bisect_left
        n = len(arr)
        if n == 0:
            return []

        tails = []          # values' tails (not strictly necessary)
        tails_idx = []      # indices of tails in arr
        prev = [-1] * n     # predecessor pointer for reconstruction

        for i, x in enumerate(arr):
            pos = bisect_left(tails, x)
            if pos == len(tails):
                tails.append(x)
                tails_idx.append(i)
            else:
                tails[pos] = x
                tails_idx[pos] = i
            if pos > 0:
                prev[i] = tails_idx[pos - 1]

        # reconstruct from last tail index
        lis_len = len(tails)
        k = tails_idx[-1]
        seq = []
        while k != -1:
            seq.append(arr[k])
            k = prev[k]
        return list(reversed(seq))
```

**When to present which version**

* In a typical interview, explain `O(n²)` DP quickly (simple, correct), then move to `O(n log n)` with the `tails` idea and `bisect_left`. If asked to **return the sequence**, show the predecessor-pointer variant.

---

## 4) Likely interviewer Q\&A

**Q1. Why does the `tails` method work?**
**A.** `tails[L-1]` stores the **smallest possible tail** of any increasing subsequence of length `L`. Replacing a tail with a smaller value keeps the subsequence length the same but maximizes chances to extend it later. The number of piles (size of `tails`) equals the LIS length (patience sorting analogy).

**Q2. `bisect_left` vs `bisect_right`?**
**A.** For **strictly** increasing LIS, use `bisect_left` (first `>= x`) so equal values **replace** the existing tail (no length increase).
For **non-decreasing** LIS, use `bisect_right` (first `> x`) so equal values **extend** properly.

**Q3. How to handle duplicates?**
**A.** With strict LIS, duplicates are treated like “not increasing”; `bisect_left` ensures they won’t increase length.

**Q4. Can I reconstruct the actual subsequence in `O(n log n)`?**
**A.** Yes—store, for each `pos`, the index in the original array that ends the best subsequence of length `pos+1`, and predecessor pointers to rebuild one LIS.

**Q5. What’s the complexity and space for both methods?**
**A.**

* DP: `O(n²)` time, `O(n)` space.
* Tails: `O(n log n)` time, `O(n)` space (can be `O(L)` where `L` is LIS length if you only keep `tails`).

**Q6. Variants/Extensions?**
**A.**

* **Longest Non-Decreasing Subsequence:** switch to `bisect_right`.
* **Counting number of LIS:** requires DP with additional counts (not handled by simple `tails`).
* **Coordinate compression + Fenwick tree:** useful for LIS on very large domains or if you need extra properties (e.g., max over values).

---

---

All set! Here’s the **full inline program** for LIS with detailed complexity comments, printed **inputs/outputs**, and **timings** for both the `O(n log n)` and `O(n²)` approaches. You can copy the exact script from the run above—it already executed and printed results and runtimes.

```python

# Re-run the inline LIS program so outputs are visible
from bisect import bisect_left
import random, timeit
from typing import List

class Solution:
    def lis(self, arr: List[int]) -> int:
        if not arr:
            return 0
        tails: List[int] = []
        for x in arr:
            pos = bisect_left(tails, x)
            if pos == len(tails):
                tails.append(x)
            else:
                tails[pos] = x
        return len(tails)

    def lis_dp_n2(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lis_sequence(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 0:
            return []
        tails: List[int] = []
        tails_idx: List[int] = []
        prev = [-1] * n
        for i, x in enumerate(arr):
            pos = bisect_left(tails, x)
            if pos == len(tails):
                tails.append(x)
                tails_idx.append(i)
            else:
                tails[pos] = x
                tails_idx[pos] = i
            if pos > 0:
                prev[i] = tails_idx[pos - 1]
        k = tails_idx[-1]
        seq = []
        while k != -1:
            seq.append(arr[k])
            k = prev[k]
        return list(reversed(seq))

def main():
    sol = Solution()
    print("=== Longest Increasing Subsequence — Demo ===")
    arr1 = [5, 8, 3, 7, 9, 1]
    arr2 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    arr3 = [3, 10, 2, 1, 20]
    for idx, arr in enumerate([arr1, arr2, arr3], start=1):
        print(f"\nInput {idx}: {arr}")
        ans_fast = sol.lis(arr)
        ans_dp   = sol.lis_dp_n2(arr)
        seq_one  = sol.lis_sequence(arr)
        print("  LIS length (O(n log n)):", ans_fast)
        print("  LIS length (O(n^2) DP): ", ans_dp)
        print("  One LIS sequence:       ", seq_one)

    n = 1000
    random.seed(7)
    arr_big = [random.randint(0, 10**6) for _ in range(n)]
    t0 = timeit.default_timer()
    fast_len = sol.lis(arr_big)
    t1 = timeit.default_timer()
    t2 = timeit.default_timer()
    dp_len = sol.lis_dp_n2(arr_big)
    t3 = timeit.default_timer()
    print(f"\nTiming on n={n} random array:")
    print(f"  O(n log n) length={fast_len}  time={(t1 - t0):.6f}s")
    print(f"  O(n^2) DP    length={dp_len}  time={(t3 - t2):.6f}s")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (high-impact)

* **Versioned dependencies / upgrades:** Choose the longest chain of increasing versions that can be installed without conflicts (each version higher than the last).
* **Scheduling with precedence:** Longest chain of tasks ordered by start/end or priority where each next task must strictly exceed a metric (e.g., strictly later finishing time).
* **Portfolio rebalancing checkpoints:** Identify the longest run of strictly increasing daily account values to detect sustained uptrends.
* **Data compression / anomaly detection:** Use LIS length as a shape descriptor (e.g., near-monotonic segments) to spot breaks or anomalies in time series.
* **Competitive programming patterns:** Basis for problems like “Russian Doll Envelopes” (2D LIS after sort), “Building Bridges”, or finding max non-overlapping pairs.

If you want a version that reads arrays from stdin (judge-style) or reconstructs **all** LIS variants, I can extend this further.
