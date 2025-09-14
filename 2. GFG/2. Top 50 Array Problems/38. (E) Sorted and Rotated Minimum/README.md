# Sorted and Rotated Minimum

**Difficulty:** Easy
**Accuracy:** 40.57%
**Submissions:** 162K+
**Points:** 2

---

## Problem Statement

A sorted array of distinct elements `arr[]` is rotated at some unknown point; the task is to find the **minimum element** in it.

---

## Examples

### Example 1

**Input:** `arr[] = [5, 6, 1, 2, 3, 4]`
**Output:** `1`
**Explanation:** `1` is the minimum element in the array.

### Example 2

**Input:** `arr[] = [3, 1, 2]`
**Output:** `1`
**Explanation:** Here `1` is the minimum element.

### Example 3

**Input:** `arr[] = [4, 2, 3]`
**Output:** `2`
**Explanation:** Here `2` is the minimum element.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^6`
* `1 ≤ arr[i] ≤ 10^9`

---

## Expected Complexities

* **Time Complexity:** `O(log n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Morgan Stanley, Amazon, Microsoft, Samsung, Snapdeal, Adobe, Times Internet

---

## Topic Tags

Searching, Algorithms

---

## Related Articles

* [Find Minimum Element In A Sorted And Rotated Array](https://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/)

---

---

here’s a crisp, interview-ready pack for **“Find minimum in a sorted, rotated array (distinct elements)”**.

---

# 2) Explanation + step-by-step dry run

## Key idea

Let `arr` be strictly increasing then rotated. The array consists of two sorted parts, and the **minimum** is the **pivot** where the rotation happens.
Binary search works by comparing the middle element with the **rightmost** element:

* If `arr[mid] > arr[r]`, the minimum lies **to the right** of `mid` (because the right half contains the “wrapped” smaller values). So set `l = mid + 1`.
* Else (`arr[mid] < arr[r]` since elements are distinct), the minimum lies **at mid or to the left**. So set `r = mid`.

Stop when `l == r`; that index is the minimum.

### Dry run (arr = `[5, 6, 1, 2, 3, 4]`)

* `l=0, r=5` → `mid=2`, `arr[mid]=1`, `arr[r]=4`. Since `1 < 4` ⇒ min in `[l..mid]`. Set `r=2`.
* `l=0, r=2` → `mid=1`, `arr[mid]=6`, `arr[r]=1`. Since `6 > 1` ⇒ min in `(mid..r]`. Set `l=2`.
* `l=2, r=2` ⇒ stop. `arr[2]=1` is the minimum.

### Another quick check (arr = `[4, 2, 3]`)

* `l=0, r=2` → `mid=1`, `arr[mid]=2`, `arr[r]=3`. `2 < 3` ⇒ `r=1`.
* `l=0, r=1` → `mid=0`, `arr[mid]=4`, `arr[r]=2`. `4 > 2` ⇒ `l=1`.
* `l=1, r=1` ⇒ stop. `arr[1]=2` is the minimum.

Why it works: at any time, one side is fully sorted. If the **rightmost** is ≥ `arr[mid]`, the right half is sorted and `mid` could be the pivot; otherwise the pivot is strictly to the right.

---

# 3) Python solutions (brute + optimized, interview-friendly)

All functions return the **minimum value**.

```python
# User function Template for python3

class Solution:
    def findMin(self, arr):
        """
        Optimized binary search: compare with right end.
        Distinct elements guaranteed.
        Time:  O(log n)
        Space: O(1)
        """
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            # If mid element is greater than rightmost,
            # the minimum is strictly to the right of mid.
            if arr[mid] > arr[r]:
                l = mid + 1
            else:
                # Minimum is at mid or in left part (including mid)
                r = mid
        return arr[l]
```

### Variant A (same idea, with early “already sorted” check and tracking answer)

```python
class SolutionEarlyExit:
    def findMin(self, arr):
        """
        Binary search with early exit when current window is sorted.
        Time:  O(log n)
        Space: O(1)
        """
        l, r = 0, len(arr) - 1
        ans = arr[0]
        while l <= r:
            # If subarray [l..r] is already sorted, arr[l] is the min here.
            if arr[l] < arr[r]:
                ans = min(ans, arr[l])
                break
            mid = (l + r) // 2
            ans = min(ans, arr[mid])
            # Left side sorted? then minimum must be on the right side.
            if arr[l] <= arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return ans
```

### Brute force (baseline)

```python
class SolutionBrute:
    def findMin(self, arr):
        """
        Linear scan for the minimum.
        Time:  O(n)
        Space: O(1)
        """
        m = arr[0]
        for x in arr[1:]:
            if x < m:
                m = x
        return m
```

> In interviews, use the **first** method (compare `mid` with `r`). It’s the cleanest and easy to reason about.

---

# 4) Interviewer-style Q\&A

**Q1. Why compare `arr[mid]` with `arr[right]`?**
**A.** Because the right portion helps us detect whether the pivot is to the right. If `arr[mid] > arr[right]`, the smallest element must be in `(mid, right]`; otherwise the right half is sorted and the pivot is at `mid` or to the left.

**Q2. What’s the complexity?**
**A.** `O(log n)` time, `O(1)` space.

**Q3. What if the array is not rotated?**
**A.** The binary search handles it: first check will move `r` left toward `l` (or the early-exit variant returns `arr[l]`). The answer will be `arr[0]`.

**Q4. What about **duplicates**?**
**A.** The classic logic needs tweaks for duplicates (when `arr[mid] == arr[right]`, you can’t decide; do `right -= 1` and continue). For this problem, elements are **distinct**, so we don’t need that.

**Q5. How to return the **index** of the minimum (rotation count)?**
**A.** The same binary search returns index `l` at the end. Rotation count = `l`.

**Q6. Common pitfalls?**

* Using `while l <= r` with the first approach but not updating correctly can loop. Prefer `while l < r` with `r = mid` (not `mid - 1`) on the “left” move.
* Forgetting the distinct-elements assumption and mishandling equality cases.
* Not handling tiny arrays (`n == 1`)—these implementations do.

---

---

Awesome — here’s a **full, runnable Python program** for **“Find the minimum in a sorted & rotated array (distinct elements)”**. It:

* prints results for **sample inputs** (input → output),
* contains **inline time & space complexity comments for each step**,
* and **benchmarks** the optimized `O(log n)` solution using `timeit` in `main`.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Find the minimum element in a sorted array that has been rotated at an unknown pivot.
Assumption: all elements are DISTINCT (as per problem statement).

Core idea (binary search with right-end comparison):
  - Keep pointers l, r. While l < r:
      mid = (l + r) // 2
      if arr[mid] > arr[r]:  # min strictly on the right half
          l = mid + 1
      else:                  # min is at mid or in the left half
          r = mid
  - When the loop ends, l == r is the index of the minimum.

Complexities:
  - Time:  O(log n)  (binary search halves the interval each step)
  - Space: O(1)      (constant extra memory)

This script:
  1) Implements the requested class/func signature.
  2) Prints outputs for several example inputs (includes the inputs).
  3) Benchmarks the algorithm using timeit (building the rotated array outside the timed section).
"""

from __future__ import annotations
import random
import timeit
from typing import List


# ---------------------------------------------------------------------------
# User function Template for python3
# ---------------------------------------------------------------------------
class Solution:
    def findMin(self, arr: List[int]) -> int:
        """
        Optimized binary search (compare with right end).
        Distinct elements guaranteed.

        Steps with per-step complexities:
          A) Init l, r pointers               -> Time O(1), Space O(1)
          B) While l < r:                     -> ~O(log n) iterations
               mid = (l + r) // 2             -> O(1)/O(1)
               if arr[mid] > arr[r]:
                   l = mid + 1                 -> discard left incl mid   (O(1))
               else:
                   r = mid                     -> keep left incl mid       (O(1))
          C) Return arr[l]                     -> O(1)/O(1)

        Overall: Time O(log n), Space O(1).
        """
        l, r = 0, len(arr) - 1  # A) O(1)/O(1)

        # B) Binary search loop — O(log n) time, O(1) space
        while l < r:
            mid = (l + r) // 2
            # If middle is greater than the rightmost, minimum lies strictly to the right
            if arr[mid] > arr[r]:
                l = mid + 1
            else:
                # Minimum is at mid or to its left
                r = mid

        # C) l == r is the index of the minimum
        return arr[l]


# --------- Extra references (not used in the benchmark, but handy to study) ---------

class SolutionEarlyExit:
    """Binary search variant with an early 'already sorted' check."""
    def findMin(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        ans = arr[0]
        while l <= r:
            # If window [l..r] is already sorted, arr[l] is the minimum here
            if arr[l] < arr[r]:
                return min(ans, arr[l])
            mid = (l + r) // 2
            ans = min(ans, arr[mid])
            if arr[l] <= arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return ans


class SolutionBrute:
    """Linear scan baseline — O(n) time, O(1) space."""
    def findMin(self, arr: List[int]) -> int:
        m = arr[0]
        for x in arr[1:]:
            if x < m:
                m = x
        return m


# --------------------------- Demo & Benchmark utilities ---------------------------

def demo_on_samples() -> None:
    """
    Print results for several inputs (input → output) using the optimized solution.
    Time here is proportional to total data size; extra space is O(1).
    """
    samples = [
        [5, 6, 1, 2, 3, 4],   # -> 1
        [3, 1, 2],            # -> 1
        [4, 2, 3],            # -> 2
        [1, 2, 3, 4, 5],      # not rotated -> 1
        [10],                 # single element -> 10
    ]

    sol = Solution()
    print("=== Sample Runs (Input → Output) ===")
    for arr in samples:
        result = sol.findMin(arr)  # O(log n)
        print(f"Input : {arr}")
        print(f"Output: {result}")
        print("-" * 60)


def _bench_once(arr: List[int]) -> None:
    """
    Helper for timeit: only the O(log n) findMin is timed.
    The array is read-only during the search.
    """
    Solution().findMin(arr)


def make_rotated_sorted_unique(n: int, rng: random.Random) -> List[int]:
    """
    Build a strictly increasing array of size n, then rotate it at a random pivot.
    Done OUTSIDE the timed region.

    Time:  O(n) to build + O(n) to rotate (via slicing)
    Space: O(n)
    """
    base = list(range(1, n + 1))        # strictly increasing
    pivot = rng.randrange(0, n)          # rotation amount
    # Slicing rotation is O(n) but it's done before timing
    return base[pivot:] + base[:pivot]


def benchmark() -> None:
    """
    Benchmark the optimized binary search with timeit.

    Prep (outside timing):
      - Build a rotated sorted array of size SIZE: O(n) time/space.

    Timed:
      - Each run executes the O(log n) search on the same array.
    """
    SIZE = 1_000_000
    rng = random.Random(2025)

    # Build input once outside timing — O(n)
    arr = make_rotated_sorted_unique(SIZE, rng)

    runs = 10
    total = timeit.timeit(lambda: _bench_once(arr), number=runs)

    print("=== Benchmark (Binary Search O(log n) / O(1)) ===")
    print(f"Array size : {SIZE}")
    print(f"Runs       : {runs}")
    print(f"Total time : {total:.6f} s")
    print(f"Avg / run  : {total / runs:.6f} s")
    print("-" * 60)


def main() -> None:
    # 1) Show outputs for specific inputs (includes inputs and outputs)
    demo_on_samples()

    # 2) Benchmark the optimized method (timeit)
    benchmark()


if __name__ == "__main__":
    main()
```

---

## Real-World Use Cases (short & important)

1. **Rotating logs / circular buffers**
   Systems often store items in a ring (wrap-around). Finding the **oldest** (minimum timestamp/ID) via this binary-search pattern recovers the head pointer in `O(log n)`.

2. **Versioned data after rollover**
   When version numbers or sequence IDs are **monotonically increasing** but **roll over** (e.g., at deployment), the data looks like a rotated sorted list. Quickly locate the **lowest version** to anchor diffs or migrations.

3. **Clock-handled / cyclic schedules**
   Time slots sorted by minutes since midnight but starting at an arbitrary offset (rotation). To pick the **earliest slot** (minimum) after importing, use this search instead of linear scans.
