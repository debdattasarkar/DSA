# Subarray with 0 sum

**Difficulty:** Medium
**Accuracy:** 39.79%
**Submissions:** 306K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given an array of integers, `arr[]`. Find if there is a **subarray** (of size at least one) with **0 sum**. Return true/false depending upon whether there is a subarray present with 0-sum or not.

---

## Examples

### Example 1

**Input:** `arr[] = [4, 2, -3, 1, 6]`
**Output:** `true`
**Explanation:** `2, -3, 1` is the subarray with a sum of `0`.

### Example 2

**Input:** `arr = [4, 2, 0, 1, 6]`
**Output:** `true`
**Explanation:** `0` is one of the elements in the array so there exists a subarray with sum `0`.

### Example 3

**Input:** `arr = [1, 2, -1]`
**Output:** `false`

---

## Constraints

* `1 <= arr.size <= 10^4`
* `-10^5 <= arr[i] <= 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

Paytm, Adobe

---

## Topic Tags

sliding-window, Hash, Map, STL, Data Structures, Algorithms

---

## Related Interview Experiences

* One97 Interview Experience Set 3 Backendnode Js Developer
* Adobe Interview Experience For Member Of Technical Staff 2

---

## Related Articles

* [Find If There Is A Subarray With 0 Sum](https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/)

---

---

here’s an interview-ready bundle for **“Subarray with 0 sum”**.

---

# 2) Explanation + step-by-step dry run

## Key idea (prefix sums + hash set)

Let `pref[i] = arr[0] + ... + arr[i]`.
A subarray `arr[l..r]` has sum `0` iff:

* `pref[r] == pref[l-1]` (same prefix seen before), or
* `pref[r] == 0` (the subarray starts at 0), or
* any element itself is `0`.

So, while scanning left→right, keep a **set of prefix sums seen**.
If the **current prefix sum** is already in the set (or is `0`) ⇒ there exists a zero-sum subarray.

**Why it works:** If `pref[r]` repeats (`pref[r] == pref[k]`), then the sum of elements from `k+1` to `r` is `pref[r] - pref[k] = 0`.

### Dry run on `[4, 2, -3, 1, 6]`

* `seen = ∅`, `sum = 0`
* `4`: `sum=4` (≠0, not in seen). Add 4 → `seen={4}`
* `2`: `sum=6` (≠0, not in seen). Add 6 → `seen={4,6}`
* `-3`: `sum=3` (≠0, not in seen). Add 3 → `seen={3,4,6}`
* `1`: `sum=4` → **4 is in seen** ⇒ subarray from index after previous 4 (i.e., indices 2..3) sums to 0. Return **True**.
  (Indeed `2 + (-3) + 1 = 0`.)

### Dry run on `[4, 2, 0, 1, 6]`

* Hit element `0` → a 1-length subarray with sum 0 exists → **True**.

### Dry run on `[1, 2, -1]`

* `sum=1` (add)
* `sum=3` (add)
* `sum=2` (new, not zero, not seen) → end, return **False**.

---

# 3) Python solutions (optimized + alternatives)

```python
# User function Template for python3

class Solution:
    
    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self, arr):
        """
        Optimized: prefix-sum + hash set
        Time:  O(n)     – single pass
        Space: O(n)     – set of seen prefix sums
        Return: True if any zero-sum subarray exists, else False
        """
        seen = set()      # stores prefix sums we've seen so far
        s = 0             # running prefix sum
        for x in arr:
            s += x
            # zero-sum exists if: current element is 0, or prefix sum is 0,
            # or this prefix sum has been seen before
            if x == 0 or s == 0 or s in seen:
                return True
            seen.add(s)
        return False
```

### A) Also return the subarray indices (handy in interviews)

```python
class SolutionWithIndices:
    def subArrayExists(self, arr):
        """
        Returns (True, (l, r)) for one zero-sum subarray if found,
        else (False, None). Uses prefix->firstIndex map.
        """
        first = {0: -1}    # prefix sum -> earliest index; 0 at -1 handles prefix=0 case
        s = 0
        for i, x in enumerate(arr):
            s += x
            if s in first:
                return True, (first[s] + 1, i)  # subarray (l..i) sums to 0
            first[s] = i
        return False, None
```

### B) Brute force (for completeness / tiny n only)

```python
class SolutionBrute:
    def subArrayExists(self, arr):
        """
        Check all O(n^2) subarrays by prefix-in-loop (no extra set).
        Time:  O(n^2)   – sum ranges in nested loops
        Space: O(1)
        """
        n = len(arr)
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += arr[j]
                if s == 0:
                    return True
        return False
```

> Note: A sliding-window (two pointers) approach **does not** work with negative numbers because the window sum is not monotonic. That’s why we use prefix sums with hashing.

---

# 4) Interviewer-style Q\&A

**Q1. Why does repeating a prefix sum imply a zero-sum subarray?**
Because `sum(i..j) = pref[j] - pref[i-1]`. If `pref[j] == pref[i-1]`, their difference is `0`, so the subarray between them sums to zero.

**Q2. Why do we check `x == 0` or `s == 0`?**

* `x == 0` → the single element forms a zero-sum subarray.
* `s == 0` → the subarray from index `0` to current index sums to zero.

**Q3. Complexity of the optimized method?**
`O(n)` time (each element processed once; set ops are average O(1)), `O(n)` space for the set/map.

**Q4. Will this work with large values or duplicates?**
Yes. Prefix sums can be any integers; Python ints are arbitrary precision. Duplicates are naturally handled by the set.

**Q5. Can you return the actual subarray, not just True/False?**
Yes—store a map `prefix_sum → first_index`. When you see the same prefix again at `j`, the zero-sum subarray is `(first_index + 1 .. j)` (see “WithIndices” variant).

**Q6. Why not a sliding window?**
Sliding windows rely on positivity to shrink/grow while maintaining order. With negatives present, growing or shrinking does not monotonically change the sum; you may skip valid subarrays.

**Q7. Edge cases to test?**

* Contains `0` (e.g., `[0]`, `[5,0,1]`)
* Starts with zero-sum prefix (e.g., `[1, -1, 2]`)
* All positives (usually False unless there’s a `0`)
* Large n near the upper bound

---

---

Absolutely! Here’s a **full, runnable Python program** for **“Subarray with 0 sum”** that:

* prints results for several **input arrays** (input → output),
* contains **inline time & space complexity comments at each step**, and
* **benchmarks** the optimized solution using `timeit` right inside `main`.

```python
#!/usr/bin/env python3
"""
Subarray with 0 Sum
-------------------
Goal: Given an integer array, return True if there exists a (non-empty) subarray
whose sum is 0; otherwise return False.

Approach (interview-standard):
  • Use a running prefix sum `s`.
  • Keep a set of seen prefix sums.
  • If `s` repeats (or `s == 0` or current element is 0), a zero-sum subarray exists.

Why it works:
  If prefix sums at positions r and k are equal, then sum(k+1..r) = pref[r] - pref[k] = 0.

Complexities:
  • Time:  O(n)  — single pass, average O(1) set operations
  • Space: O(n)  — stores at most n prefix sums in a set

This script:
  1) Implements `class Solution.subArrayExists`.
  2) (Optional) Implements `class SolutionWithIndices` to also return one subarray.
  3) Prints outputs for sample inputs (input → output).
  4) Benchmarks the algorithm using `timeit` (pure O(n) scan).
"""

from __future__ import annotations
import random
import timeit
from typing import List, Optional, Tuple


# -------------------------------------------------------------------
# User function Template for python3
# -------------------------------------------------------------------
class Solution:
    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self, arr: List[int]) -> bool:
        """
        Prefix-sum + hash set.

        Steps (with per-step complexity):
          A) Initialize empty set and running sum          -> O(1) time, O(1) space
          B) For each element x in arr (single pass):
               - s += x                                    -> O(1)
               - if x == 0 or s == 0 or s in seen: True    -> O(1) avg lookup
               - else add s to `seen`                      -> O(1) avg insert
             Overall loop                                  -> O(n) time, O(n) space (worst)
          C) If loop completes, return False               -> O(1)
        """
        seen = set()   # O(1) space now; grows up to O(n)
        s = 0          # running prefix sum

        for x in arr:                      # B) O(n) iterations
            s += x                         #    O(1)
            if x == 0 or s == 0 or s in seen:  # O(1) average checks
                return True
            seen.add(s)                    # O(1) average insert

        return False                       # C) O(1)


# Optional helper that also returns one zero-sum subarray's indices
class SolutionWithIndices:
    def subArrayExists(self, arr: List[int]) -> Tuple[bool, Optional[Tuple[int, int]]]:
        """
        Returns (True, (l, r)) if a zero-sum subarray exists, else (False, None).
        Time:  O(n)  Space: O(n)
        """
        first_index = {0: -1}  # prefix sum 0 occurs before the array starts
        s = 0
        for i, x in enumerate(arr):
            s += x
            if s in first_index:
                return True, (first_index[s] + 1, i)
            first_index[s] = i
        return False, None


# ------------------------------- Demo & Benchmark -------------------------------

def demo_on_samples() -> None:
    """
    Demonstrate correctness on several inputs (each printed as input → output).
    Time:  proportional to total input length (O(sum n_i))
    Space: O(1) extra besides the sets used during checks.
    """
    samples = [
        ([4, 2, -3, 1, 6], True),        # 2, -3, 1 -> 0
        ([4, 2, 0, 1, 6], True),         # single 0 element
        ([1, 2, -1], False),             # no zero-sum subarray
        ([1, -1], True),                 # whole array sums to 0
        ([3, -1, -2, 5, -5, 1, -1], True),
        ([5, 5, 5], False),              # all positive, no zero
        ([0], True),                     # single zero
    ]

    sol = Solution()
    print("=== Sample Runs (Input → Output) ===")
    for arr, expected in samples:
        out = sol.subArrayExists(arr)  # O(n)
        print(f"Input : {arr}")
        print(f"Output: {out}    (Expected: {expected})")
        print("-" * 60)

    # Show indices for one case
    print("One example with indices:")
    ok, seg = SolutionWithIndices().subArrayExists([4, 2, -3, 1, 6])
    print(f"Exists: {ok}, Subarray indices (l, r): {seg}")
    print("-" * 60)


def _bench_once(arr: List[int]) -> None:
    """
    Helper for timeit: run only the O(n) algorithm.
    The function is read-only on `arr`, so we can reuse the same list each run.
    """
    Solution().subArrayExists(arr)


def benchmark() -> None:
    """
    Benchmark the O(n) solution using timeit.

    Prep (outside timing):
      - Generate a random array once (size SIZE) with values in [-MAXV, MAXV]
        Time:  O(SIZE), Space: O(SIZE).

    Timed region:
      - Each run: single O(n) scan over the same list.
    """
    SIZE = 250_000
    MAXV = 10**5
    rng = random.Random(2025)

    # Build input once — O(SIZE) time/space
    arr = [rng.randrange(-MAXV, MAXV + 1) for _ in range(SIZE)]

    runs = 5
    total = timeit.timeit(lambda: _bench_once(arr), number=runs)

    print("=== Benchmark (Prefix-sum + Hash Set, O(n) time / O(n) space) ===")
    print(f"Array size : {SIZE}")
    print(f"Runs       : {runs}")
    print(f"Total time : {total:.6f} s")
    print(f"Avg / run  : {total / runs:.6f} s")
    print("-" * 60)


def main() -> None:
    # 1) Show outputs for specific inputs (includes inputs and outputs)
    demo_on_samples()

    # 2) Benchmark the optimized method with timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (short & important)

1. **Financial reconciliation / ledger sanity checks**
   Detect if any contiguous segment of transactions nets to zero (e.g., charge immediately offset by a refund + fees), useful for audits and anomaly detection.

2. **Streaming telemetry sanity**
   In counters that allow positive/negative adjustments, finding a zero-sum subarray reveals bursts that fully cancel out—helpful when debugging spikes that “disappear” in aggregates.

3. **Balancing operations in systems**
   When applying a sequence of resource allocations and releases, a zero-sum interval indicates a window with **no net effect**—useful for rolling-back or compressing logs/ops.

4. **Signal processing / time-series**
   In detrended series with positive/negative deviations, a zero-sum subarray exposes intervals where the error integrates to zero—handy for segmentation and regime analysis.

