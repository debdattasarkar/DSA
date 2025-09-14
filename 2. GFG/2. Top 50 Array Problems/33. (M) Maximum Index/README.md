# Maximum Index

**Difficulty:** Medium
**Accuracy:** 24.5%
**Submissions:** 287K+
**Points:** 4

---

## Problem Statement

Given an array `arr` of positive integers. You have to return the maximum of `j - i` such that `arr[i] ≤ arr[j]` and `i ≤ j`.

---

## Examples

### Example 1

**Input:** `arr[] = [1, 10]`
**Output:** `1`
**Explanation:** `arr[0] ≤ arr[1]` so `(j - i)` is `1 - 0 = 1`.

### Example 2

**Input:** `arr[] = [5, 4, 3]`
**Output:** `0`
**Explanation:** There is no pair that satisfies the given condition.

### Example 3

**Input:** `arr[] = [34, 8, 10, 3, 2, 80, 30, 33, 1]`
**Output:** `6`
**Explanation:** In the given array `arr[1] < arr[7]` satisfying the required condition (`arr[i] ≤ arr[j]`) thus giving the maximum difference of `j - i` which is `6 (7 - 1)`.

---

## Constraints

* `1 ≤ arr.size ≤ 10^5`
* `0 ≤ arr[i] ≤ 10^9`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

VMWare, Amazon, Microsoft, MakeMyTrip

---

## Topic Tags

Arrays, Data Structures, two-pointer-algorithm

---

## Related Interview Experiences

* Vmware Interview Set 1 For Mts 2 Position
* Amazon Interview Experience Set 416 Campus Internship
* Makemytrip Interview Experience For Software Engineer

---

## Related Articles

* [Given An Array Arr Find The Maximum J I Such That Arrj Arri](https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/)

---

---

here’s a clean, interview-ready breakdown for **Maximum Index** (maximize `j - i` s.t. `arr[i] ≤ arr[j]` and `i ≤ j`).

---

# 2) Explanation + step-by-step dry run

## Intuition

We want the farthest apart indices where the **left value isn’t bigger than the right value**.
Brute force checks every pair `i ≤ j` → `O(n²)`.
A classic linear approach uses two helper arrays:

* `LMin[i]` = minimum of `arr[0..i]` (best value you could place on/left of `i`)
* `RMax[j]` = maximum of `arr[j..n-1]` (best value you could place on/right of `j`)

Now walk with two pointers:

* If `LMin[i] ≤ RMax[j]`, then **some** valid pair exists with left ≤ `i` and right ≥ `j`. Record `j - i`, push `j` right to try for a wider gap.
* Else move `i` right to try to reduce the left value.

This yields `O(n)` time and `O(n)` space.

## Dry run (array from the prompt)

`arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]`

1. Build `LMin` (prefix minima)

```
i:    0   1   2   3  4  5  6  7  8
arr: 34   8  10   3  2 80 30 33  1
LMin:34   8   8   3  2  2  2  2  1
```

2. Build `RMax` (suffix maxima)

```
j:     0   1   2   3   4   5  6  7  8
RMax: 80  80  80  80  80  80 33 33  1
```

3. Two-pointer sweep

```
i=0, j=0: LMin[0]=34 ≤ RMax[0]=80 → ans=max(0, 0-0)=0; j→1
i=0, j=1: 34 ≤ 80 → ans=1; j→2
i=0, j=2: 34 ≤ 80 → ans=2; j→3
i=0, j=3: 34 ≤ 80 → ans=3; j→4
i=0, j=4: 34 ≤ 80 → ans=4; j→5
i=0, j=5: 34 ≤ 80 → ans=5; j→6
i=0, j=6: 34 ≤ 33 ? no  → i→1
i=1, j=6:  8 ≤ 33 → ans=max(5, 6-1)=5; j→7
i=1, j=7:  8 ≤ 33 → ans=max(5, 7-1)=6; j→8
i=1, j=8:  8 ≤  1 ? no  → i→2→3→4→5→6 (keep moving while  LMin[i] > RMax[8]=1)
j hits end at 9; stop. Final ans = 6.
```

Result matches the example.

---

# 3) Python solutions (with inline comments)

### A) Optimized `O(n)` (prefix-min + suffix-max + two pointers) — **use this in interviews**

```python
class Solution:
    def maxIndexDiff(self, arr):
        n = len(arr)
        if n <= 1:
            return 0

        # Build LMin: LMin[i] = min(arr[0..i])
        LMin = [0] * n
        LMin[0] = arr[0]
        for i in range(1, n):
            LMin[i] = min(LMin[i-1], arr[i])

        # Build RMax: RMax[j] = max(arr[j..n-1])
        RMax = [0] * n
        RMax[-1] = arr[-1]
        for j in range(n-2, -1, -1):
            RMax[j] = max(RMax[j+1], arr[j])

        # Two-pointer sweep to maximize (j - i)
        i = j = 0
        best = 0  # if no valid pair wider than 0 exists, answer is 0
        while i < n and j < n:
            if LMin[i] <= RMax[j]:
                # Valid i..j window exists; try to push j to the right (wider)
                best = max(best, j - i)
                j += 1
            else:
                # Need a smaller left value → move i to the right
                i += 1
        return best
```

### B) Monotonic stack `O(n)` (LeetCode “Maximum Width Ramp” style)

Build a strictly decreasing stack of indices from the left; then scan from the right and pop while you can form valid ramps.

```python
class SolutionStack:
    def maxIndexDiff(self, arr):
        n = len(arr)
        if n <= 1:
            return 0

        # Step 1: strictly decreasing stack of indices
        st = []
        for i, x in enumerate(arr):
            if not st or arr[st[-1]] > x:
                st.append(i)

        # Step 2: scan from right; widen while arr[st[-1]] <= arr[j]
        best = 0
        for j in range(n-1, -1, -1):
            while st and arr[st[-1]] <= arr[j]:
                i = st.pop()
                best = max(best, j - i)
        return best
```

### C) Sort by value `O(n log n)` (constant extra apart from the list of pairs)

Sort pairs `(value, index)` ascending; keep the smallest index seen so far as you sweep.

```python
class SolutionSort:
    def maxIndexDiff(self, arr):
        n = len(arr)
        if n <= 1:
            return 0

        pairs = sorted((val, idx) for idx, val in enumerate(arr))  # sort by value, then index
        best = 0
        min_idx = pairs[0][1]  # smallest index among values ≤ current

        for k in range(1, n):
            _, idx = pairs[k]
            # min_idx is among all earlier values (<= current value), so arr[min_idx] ≤ arr[idx]
            best = max(best, idx - min_idx)
            # update for future elements
            if idx < min_idx:
                min_idx = idx
        return best
```

### D) Brute force `O(n²)` (clear baseline)

```python
class SolutionBrute:
    def maxIndexDiff(self, arr):
        n = len(arr)
        best = 0
        # try every i, j (i ≤ j). Early break when remaining span can't beat best.
        for i in range(n):
            # If the farthest possible at this i can't beat best, break early.
            if n - 1 - i <= best:
                break
            for j in range(n-1, i-1, -1):
                if arr[i] <= arr[j]:
                    best = max(best, j - i)
                    # since we're moving j downward, the first hit is the farthest for this i
                    break
        return best
```

**Complexities**

* A) Two arrays + two pointers: `O(n)` time, `O(n)` space.
* B) Monotonic stack: `O(n)` time, `O(n)` space.
* C) Sort by value: `O(n log n)` time, `O(1)` auxiliary (besides the sortable list of pairs).
* D) Brute: `O(n²)` time, `O(1)` space.

---

# 4) Interviewer-style Q\&A

**Q1. Why does the two-pointer method work?**
**A.** `LMin[i]` guarantees a value ≤ any element to its left, and `RMax[j]` guarantees a value ≥ any element to its right.
If `LMin[i] ≤ RMax[j]`, there exists some `p ≤ i` and `q ≥ j` with `arr[p] ≤ arr[q]`. Pushing `j` right can only increase `(j - i)`. If it fails (`LMin[i] > RMax[j]`), increasing `i` may reduce the left value and restore feasibility. This monotonic movement ensures we never miss the optimal width and we finish in linear time.

**Q2. What happens in a strictly decreasing array?**
**A.** No pair with `arr[i] ≤ arr[j]` and `i < j` exists, so the answer is `0`. The code handles this naturally.

**Q3. How do duplicates affect the answer?**
**A.** Duplicates help: if `arr[i] == arr[j]`, the pair is valid and can produce a wide gap. Sorting approach must sort by `(value, index)` so earlier indices for the same value are seen first.

**Q4. Can we do it in `O(n)` time and `O(1)` extra space?**
**A.** Not with the standard deterministic methods. Known linear-time solutions (prefix/suffix arrays or monotonic stack) use `O(n)` extra memory. There’s no widely known `O(n)` / `O(1)` exact algorithm for the general case.

**Q5. Alternative approaches besides the two-pointer trick?**
**A.**

* **Monotonic stack** (as shown) — popularized by LeetCode 962 “Maximum Width Ramp”.
* **Binary search variant (`O(n log n)`)**: Build `RMax`, and for each `i` binary-search the farthest `j` with `RMax[j] ≥ arr[i]`.

**Q6. Off-by-one pitfalls to watch for?**
**A.**

* Initialize `best = 0` (not `-inf`) because `(i == j)` is allowed and gives width 0.
* Pointers must be kept within bounds: `while i < n and j < n`.
* Build `LMin` forward and `RMax` backward correctly (prefix **min**, suffix **max**).

**Q7. How would you test quickly?**
**A.**

* Single element: `[7] → 0`
* All equal: `[5,5,5] → 2`
* Strictly decreasing: `[5,4,3] → 0`
* Mixed with a large tail max: `[1,2,3,4,0,0,100] → 6`
* The given sample: `[34,8,10,3,2,80,30,33,1] → 6`

---

---

Awesome—here’s a **full, runnable program** that:

* prints results for sample inputs,
* includes **inline time & space complexity notes for every step**,
* and measures runtime using **`timeit`** right inside `main`.

It also includes multiple approaches (Optimized `O(n)`, Monotonic-Stack `O(n)`, Sort-based `O(n log n)`, and Brute `O(n²)`), but the “official” one is the first `Solution` class.

```python
#!/usr/bin/env python3
"""
Problem: Maximum Index
Return the maximum (j - i) such that arr[i] <= arr[j] and i <= j.

This file prints outputs for sample inputs and benchmarks the optimized solution
using Python's timeit inside main.

Author note: Inline comments include time/space complexity for each step.
"""

from __future__ import annotations
import random
import timeit
from typing import List


class Solution:
    """
    Optimized prefix-min + suffix-max + two-pointers.
    Time:  O(n)   — single forward pass to build LMin, single backward pass to build RMax,
                     and one linear two-pointer sweep (pointers move monotonically).
    Space: O(n)   — LMin and RMax arrays of size n.
    """

    def maxIndexDiff(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        # Build LMin: LMin[i] = min(arr[0..i])
        # Time:  O(n)
        # Space: O(n)
        LMin = [0] * n
        LMin[0] = arr[0]
        for i in range(1, n):
            # Maintain prefix minimum up to i
            LMin[i] = LMin[i - 1] if LMin[i - 1] <= arr[i] else arr[i]

        # Build RMax: RMax[j] = max(arr[j..n-1])
        # Time:  O(n)
        # Space: O(n)
        RMax = [0] * n
        RMax[-1] = arr[-1]
        for j in range(n - 2, -1, -1):
            # Maintain suffix maximum from j to end
            RMax[j] = RMax[j + 1] if RMax[j + 1] >= arr[j] else arr[j]

        # Two-pointer sweep to maximize (j - i)
        # Time:  O(n)   — both pointers traverse at most n steps total
        # Space: O(1)   — aside from pre-built arrays
        i = 0
        j = 0
        best = 0
        while i < n and j < n:
            if LMin[i] <= RMax[j]:
                # Feasible window exists with some p<=i and q>=j; try to widen by moving j
                # Update the best distance
                gap = j - i
                if gap > best:
                    best = gap
                j += 1
            else:
                # Need a smaller left value; move i right
                i += 1

        return best


class SolutionStack:
    """
    Monotonic stack (Maximum Width Ramp style).
    Time:  O(n)   — each index pushed & popped at most once.
    Space: O(n)   — stack stores a subset of indices.
    """
    def maxIndexDiff(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        # Build strictly decreasing stack of indices from the left
        st = []
        for i, x in enumerate(arr):
            if not st or arr[st[-1]] > x:
                st.append(i)

        # Scan from the right and pop while arr[st[-1]] <= arr[j]
        best = 0
        for j in range(n - 1, -1, -1):
            while st and arr[st[-1]] <= arr[j]:
                i = st.pop()
                if j - i > best:
                    best = j - i
        return best


class SolutionSort:
    """
    Sort by (value, index) and sweep while tracking minimum index seen so far.
    Time:  O(n log n) — sorting dominates.
    Space: O(n)       — list of pairs.
    """
    def maxIndexDiff(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        pairs = sorted((val, idx) for idx, val in enumerate(arr))  # O(n log n)
        best = 0
        min_idx = pairs[0][1]
        for k in range(1, n):
            idx = pairs[k][1]
            # All earlier pairs have value <= current value, so constraint holds.
            if idx - min_idx > best:
                best = idx - min_idx
            if idx < min_idx:
                min_idx = idx
        return best


class SolutionBrute:
    """
    Brute force (baseline for correctness).
    Time:  O(n^2)     — checks pairs (i, j).
    Space: O(1)       — constant extra space.
    """
    def maxIndexDiff(self, arr: List[int]) -> int:
        n = len(arr)
        best = 0
        for i in range(n):
            # Early exit: if remaining farthest j can't beat best, break.
            if n - 1 - i <= best:
                break
            for j in range(n - 1, i - 1, -1):
                if arr[i] <= arr[j]:
                    if j - i > best:
                        best = j - i
                    # First valid j from the right is the farthest; break inner loop.
                    break
        return best


def demo_on_samples():
    """Run all methods on sample inputs and show outputs."""
    samples = [
        [1, 10],
        [5, 4, 3],
        [34, 8, 10, 3, 2, 80, 30, 33, 1],
        [5],                        # edge: single element
        [5, 5, 5, 5],               # all duplicates
        [1, 2, 3, 4, 0, 0, 100],    # mixed, large tail max
    ]

    sol_opt = Solution()
    sol_stack = SolutionStack()
    sol_sort = SolutionSort()
    sol_brut = SolutionBrute()

    print("=== Sample Runs ===")
    for arr in samples:
        ans_opt   = sol_opt.maxIndexDiff(arr)
        ans_stack = sol_stack.maxIndexDiff(arr)
        ans_sort  = sol_sort.maxIndexDiff(arr)
        ans_brut  = sol_brut.maxIndexDiff(arr) if len(arr) <= 1000 else "(skipped brute)"
        print(f"Input: {arr}")
        print(f" Optimized (O(n))      -> {ans_opt}")
        print(f" Monotonic Stack (O(n))-> {ans_stack}")
        print(f" Sort-based (O(n log n))-> {ans_sort}")
        print(f" Brute (O(n^2))        -> {ans_brut}")
        print("-" * 60)


def _bench_opt_once(arr_large):
    """Helper for timeit: run the optimized method once on a pre-built array."""
    Solution().maxIndexDiff(arr_large)


def benchmark():
    """
    Benchmark the optimized O(n) solution using timeit.
    We generate the large input OUTSIDE the timed call so we only time the algorithm.

    Adjust N and SIZE to taste if you run locally.
    """
    SIZE = 200_000  # choose a large N to see linear performance
    rng = random.Random(42)
    arr_large = [rng.randrange(0, 10**9) for _ in range(SIZE)]

    # timeit setup: pass arr_large via closure using default argument
    t = timeit.timeit(lambda: _bench_opt_once(arr_large), number=3)
    print("=== Benchmark (Optimized O(n)) ===")
    print(f" Array size: {SIZE}")
    print(f" Runs: 3")
    print(f" Total time (s): {t:.6f}")
    print(f" Avg per run (s): {t/3:.6f}")
    print("-" * 60)


def main():
    # Show outputs for explicit example inputs
    demo_on_samples()

    # Benchmark the optimized solution with timeit
    benchmark()


if __name__ == "__main__":
    main()
```

### What you’ll see when you run it

* For each **input array**, the program prints:

  * the **optimized** result,
  * **monotonic stack** result,
  * **sort-based** result,
  * and **brute-force** result (skipped for very large arrays).
* Then it prints a **timeit benchmark** for the optimized method on a large random array (size = 200,000, three runs), with total and average times.

---

## Real-World Use Cases (short & important)

1. **Finance / Trading (no-loss span):**
   Find the longest holding period where your exit price isn’t below your entry price (`close[j] ≥ close[i]`). This reveals **maximal “non-negative return” windows** irrespective of profit magnitude.

2. **SLA / Monitoring (stability window):**
   For a time series metric (e.g., availability, throughput), find the longest interval where the **ending value is at least the starting value**—a simple way to capture **non-degradation windows**.

3. **Manufacturing / Quality Control:**
   Over sequential quality scores, find the longest interval that **does not deteriorate** from start to end, useful for tracking **process robustness** windows.
