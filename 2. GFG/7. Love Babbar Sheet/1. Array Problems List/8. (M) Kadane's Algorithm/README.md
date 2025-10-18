# Kadane's Algorithm

**Difficulty:** Medium
**Accuracy:** 36.28%
**Submissions:** 1.1M
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given an integer array `arr[]`. You need to find the **maximum** sum of a subarray.

---

## Examples

### Example 1

**Input:** `arr[] = [2, 3, -8, 7, -1, 2, 3]`
**Output:** `11`
**Explanation:** The subarray `{7, -1, 2, 3}` has the largest sum `11`.

### Example 2

**Input:** `arr[] = [-2, -4]`
**Output:** `-2`
**Explanation:** The subarray `{-2}` has the largest sum `-2`.

### Example 3

**Input:** `arr[] = [5, 4, 1, 7, 8]`
**Output:** `25`
**Explanation:** The subarray `{5, 4, 1, 7, 8}` has the largest sum `25`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `-10^9 ≤ arr[i] ≤ 10^4`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Zoho, Flipkart, Morgan Stanley, Accolite, Amazon, Microsoft, Samsung, Snapdeal, 24\*7 Innovation Labs, Citrix, D-E-Shaw, FactSet, Hike, Housing.com, MetLife, Ola Cabs, Oracle, Payu, Teradata, Visa, Walmart, Adobe, Google, Arcesium

---

## Topic Tags

Arrays, Dynamic Programming, Data Structures, Algorithms

---

## Related Interview Experiences

* Oracle Interview Experience Set 45 For 3 Years Experienced
* Zoho Interview Experience Set 18 On Campus
* Hike Interview Experience Set 5
* Ola Interview Experience Set 10 Ds
* Accolite Interview Experience Set 3 On Campus
* Microsoft Interview Experience Set 151 Sde 2 3 5 Years Experience
* Microsoft Interview Experience For Internship 4
* Adobe Shecodes Product Interview Experience For Internship 2020

---

## Related Articles

* [Largest Sum Contiguous Subarray](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)

---

---

here’s a crisp, interview-ready package for **Kadane’s Algorithm** (Maximum Subarray Sum).

---

# 2) Explanation + step-by-step dry run

## Core idea (Kadane)

Maintain a running best subarray that **must end at the current index**.

* `cur` = best sum of a subarray that ends at the current element.
* `best` = best sum seen anywhere so far.

Transition at each element `x`:

* Either **extend** the previous subarray: `cur + x`
* Or **start fresh** at `x`: `x`

So:

```
cur  = max(x, cur + x)
best = max(best, cur)
```

Initialize with the first element to correctly handle **all-negative** arrays.

### Why this works

If the best subarray ending at `i-1` is negative, extending it only hurts. So we “drop” it and restart at `i`. This greedy decision is always safe and yields an `O(n)` solution.

---

## Dry runs

### Example A

`arr = [2, 3, -8, 7, -1, 2, 3]`

| i | x  | cur = max(x, cur+x)      | best   |
| - | -- | ------------------------ | ------ |
| 0 | 2  | max(2, 2) = **2**        | **2**  |
| 1 | 3  | max(3, 2+3=5) = **5**    | **5**  |
| 2 | -8 | max(-8, 5-8=-3) = **-3** | **5**  |
| 3 | 7  | max(7, -3+7=4) = **7**   | **7**  |
| 4 | -1 | max(-1, 7-1=6) = **6**   | **7**  |
| 5 | 2  | max(2, 6+2=8) = **8**    | **8**  |
| 6 | 3  | max(3, 8+3=11) = **11**  | **11** |

Answer = **11** (subarray `[7, -1, 2, 3]`).

### Example B (all negatives)

`arr = [-2, -4]`

| i | x  | cur                     | best   |
| - | -- | ----------------------- | ------ |
| 0 | -2 | max(-2, -2) = **-2**    | **-2** |
| 1 | -4 | max(-4, -2-4=-6)=**-4** | **-2** |

Answer = **-2** (pick the least-negative single element).

---

# 3) Python solutions (multiple ways, interview-friendly)

### A) Kadane — clean, `O(n)` time / `O(1)` space  ✅ (most expected)

```python
class Solution:
    def maxSubarraySum(self, arr):
        # Kadane's algorithm
        # Time:  O(n) — single pass
        # Space: O(1) — constant extra space
        cur = best = arr[0]             # init with first element to handle all-negatives
        for x in arr[1:]:
            cur = max(x, cur + x)       # either extend previous or start fresh at x
            best = max(best, cur)       # track the global best
        return best
```

### B) Kadane with indices (often requested)

Returns (max\_sum, start, end). Great to reconstruct the subarray.

```python
class SolutionWithIndices:
    def maxSubarraySum(self, arr):
        # Time: O(n), Space: O(1)
        best = cur = arr[0]
        best_l = best_r = 0
        l = 0                           # tentative start for current subarray

        for r in range(1, len(arr)):
            x = arr[r]
            if x > cur + x:             # better to start new subarray at r
                cur = x
                l = r
            else:                       # extend
                cur += x

            if cur > best:              # found better global answer
                best = cur
                best_l, best_r = l, r

        return best  # or (best, best_l, best_r)
```

### C) Prefix-sum + min-prefix trick — also `O(n)` / `O(1)`

`max subarray sum` = `max_i (prefix[i] - min_prefix_before_i)`

```python
class SolutionPrefixMin:
    def maxSubarraySum(self, arr):
        # Time: O(n), Space: O(1) extra (prefix carried in one variable)
        prefix = 0
        min_prefix = 0     # best (smallest) prefix seen before current index
        best = arr[0]      # handles all-negatives

        for x in arr:
            prefix += x
            best = max(best, prefix - min_prefix)
            min_prefix = min(min_prefix, prefix)
        return best
```

### D) Divide & Conquer — `O(n log n)` (nice to mention)

```python
class SolutionDivideConquer:
    def maxSubarraySum(self, arr):
        # Time: O(n log n), Space: O(log n) recursion
        def solve(lo, hi):
            if lo == hi:
                x = arr[lo]
                return (x, x, x, x)  
                # (total_sum, best_prefix, best_suffix, best_subarray)

            mid = (lo + hi) // 2
            lt = solve(lo, mid)
            rt = solve(mid + 1, hi)

            total = lt[0] + rt[0]
            best_pref = max(lt[1], lt[0] + rt[1])
            best_suff = max(rt[2], rt[0] + lt[2])
            best_sub = max(lt[3], rt[3], lt[2] + rt[1])
            return (total, best_pref, best_suff, best_sub)

        return solve(0, len(arr) - 1)[3]
```

### E) Brute force (with prefix sums) — `O(n²)` baseline

```python
class SolutionBrute:
    def maxSubarraySum(self, arr):
        # Time: O(n^2), Space: O(n) for prefix
        n = len(arr)
        pref = [0] * (n + 1)
        for i in range(n):                  # build prefix sums
            pref[i + 1] = pref[i] + arr[i]

        best = arr[0]
        for i in range(n):
            for j in range(i, n):
                # sum(i..j) = pref[j+1] - pref[i]
                s = pref[j + 1] - pref[i]
                if s > best:
                    best = s
        return best
```

---

# 4) Interviewer-style Q\&A

**Q1. Why initialize Kadane with the first element instead of 0?**
**A.** If all numbers are negative, initializing `cur=best=0` would wrongly return `0`. Using the first element ensures we pick the least-negative element and remain correct for all cases.

**Q2. What’s the time and space complexity of Kadane?**
**A.** `O(n)` time, `O(1)` extra space.

**Q3. How do you recover the actual subarray (indices)?**
**A.** Track a tentative start index `l`. When you restart at `r`, set `l=r`. Update `(best_l, best_r)` whenever a better `best` is found. (See code B.)

**Q4. How does the prefix-min method relate to Kadane?**
**A.** Let `P[i]` be prefix sums. The best subarray ending at `i` is `P[i] - min_{k<i} P[k]`. Updating `min_prefix` while scanning is equivalent to Kadane’s decisions.

**Q5. What if the problem asks for the **minimum** subarray sum?**
**A.** Flip the signs (or symmetrically track `cur = min(x, cur + x)` and `best = min(best, cur)`).

**Q6. How to handle **circular** maximum subarray?**
**A.** Answer is `max( kadane(arr), total_sum - min_subarray_sum )`, unless all numbers are negative (then use plain Kadane). This is the standard trick for circular arrays.

**Q7. Subarray vs subsequence difference here?**
**A.** Subarray = contiguous block; subsequence = order-preserving but not necessarily contiguous. Kadane solves the **contiguous** version.

**Q8. Common pitfalls?**
**A.**

* Returning `0` for all-negatives (bad init).
* Using 32-bit types in languages with overflow (use 64-bit).
* Forgetting that empty subarray is **not** allowed in standard Kadane.

---

---

Awesome—here’s a **full, runnable Python program** for **Kadane’s Algorithm** that:

* prints outputs for several **input arrays**,
* includes **inline time & space complexity comments for each step**,
* and **benchmarks** the optimized solution using `timeit` right inside `main`.

It uses the exact interview-style signature:

```python
class Solution:
    def maxSubarraySum(self, arr):
        # Code here
```

---

```python
#!/usr/bin/env python3
"""
Kadane's Algorithm — Maximum Subarray Sum
Goal: Given an integer array arr, find the maximum sum over all CONTIGUOUS subarrays.

This script:
  1) Implements the optimized O(n) Kadane solution in class Solution (interview-friendly).
  2) Demonstrates results on sample inputs (prints both inputs and outputs).
  3) Benchmarks the algorithm using timeit on a large random array.

All major steps include inline time/space complexity notes.
"""

from __future__ import annotations
import random
import timeit
from typing import List, Tuple


class Solution:
    def maxSubarraySum(self, arr: List[int]) -> int:
        """
        Kadane's Algorithm — O(n) time, O(1) extra space

        Steps & complexities:
        - Initialize current and best sums with arr[0] (O(1) time, O(1) space).
        - Single pass over the rest of the array (O(n) time, O(1) space):
          For each x: cur = max(x, cur + x); best = max(best, cur).
          Greedy restart when the previous sum is negative.
        - Return best (O(1) time, O(1) space).
        """
        # Edge cases are guaranteed by constraints (len(arr) >= 1). If needed, guard here.

        # O(1) time / O(1) space
        cur = best = arr[0]

        # O(n) time total / O(1) extra space
        for x in arr[1:]:
            # Decide to extend or restart — O(1)
            cur = max(x, cur + x)
            # Track global best — O(1)
            best = max(best, cur)

        # O(1) time / O(1) space
        return best


class SolutionWithIndices:
    """
    Same as Kadane but also tracks (start, end) indices of the best subarray.
    Time:  O(n)
    Space: O(1)
    """
    def maxSubarraySum(self, arr: List[int]) -> Tuple[int, int, int]:
        best = cur = arr[0]
        best_l = best_r = 0
        l = 0  # tentative start of current window

        for r in range(1, len(arr)):
            x = arr[r]
            # If starting fresh at r is better than extending, restart here.
            if x > cur + x:
                cur = x
                l = r
            else:
                cur += x

            # Update global best and its indices
            if cur > best:
                best = cur
                best_l, best_r = l, r

        return best, best_l, best_r


def demo_on_samples() -> None:
    """
    Show correctness on a handful of inputs.
    Each print includes the input values and the output from both versions.
    """
    samples = [
        [2, 3, -8, 7, -1, 2, 3],  # expected 11
        [-2, -4],                 # expected -2 (least negative element)
        [5, 4, 1, 7, 8],          # expected 25
        [-5],                     # single negative
        [0, 0, 0, 0],             # all zeros => 0
        [1, -2, 3, 10, -4, 7, 2, -5],  # classic => 18 (3 + 10 - 4 + 7 + 2)
    ]

    kadane = Solution()
    kadane_idx = SolutionWithIndices()

    print("=== Sample Runs ===")
    for arr in samples:
        # Optimized O(n) Kadane — O(n) time, O(1) space
        ans = kadane.maxSubarraySum(arr)

        # Optional: show indices and actual subarray
        best, L, R = kadane_idx.maxSubarraySum(arr)
        subarr = arr[L:R+1]
        print(f"Input:  {arr}")
        print(f"Output (Kadane sum): {ans}")
        print(f"Output (sum, L, R):  ({best}, {L}, {R})  Subarray: {subarr}")
        print("-" * 60)


# Helper used by timeit; keeps only the O(n) algorithm in the timed section
def _bench_once(arr_large: List[int]) -> None:
    Solution().maxSubarraySum(arr_large)


def benchmark() -> None:
    """
    Benchmark the optimized solution using timeit.

    Complexity of prep below:
      - Building the random array: O(N) time, O(N) space.
    The timed part (_bench_once) does:
      - Kadane O(N) time, O(1) extra space.
    """
    SIZE = 200_000  # adjust if running locally on limited hardware
    rng = random.Random(12345)

    # Build input outside the timed function so we only measure algorithm time.
    # O(N) time, O(N) space
    arr_large = [rng.randrange(-10**6, 10**6) for _ in range(SIZE)]

    # Time only the algorithm; run it a few times to average out noise.
    # The lambda closes over arr_large (no copying).
    runs = 3
    total = timeit.timeit(lambda: _bench_once(arr_large), number=runs)

    print("=== Benchmark (Optimized Kadane O(n)) ===")
    print(f"Array size : {SIZE}")
    print(f"Runs       : {runs}")
    print(f"Total time : {total:.6f} s")
    print(f"Avg / run  : {total / runs:.6f} s")
    print("-" * 60)


def main() -> None:
    # 1) Show outputs for several inputs (prints both input values and outputs)
    demo_on_samples()

    # 2) Benchmark the optimized solution using timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## Real-World Use Cases (few, but important)

1. **Trading / Portfolio Analytics**
   Model daily **returns** as an array. Kadane finds the **best contiguous run** of days (max cumulative return), i.e., the most profitable continuous holding period.

2. **Performance Monitoring / Telemetry**
   Given per-interval **delta improvements** (positive/negative), Kadane pinpoints the longest/highest **net positive streak**, useful for detecting periods of strong recovery or growth.

3. **Signal Processing / Sensor Data**
   Over noise-like readings converted to **signed deviations**, Kadane extracts the strongest continuous **positive energy** segment—handy for event detection or burst identification.
