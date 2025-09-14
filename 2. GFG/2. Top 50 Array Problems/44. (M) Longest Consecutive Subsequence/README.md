# Longest Consecutive Subsequence

**Difficulty:** Medium
**Accuracy:** 33.0%
**Submissions:** 377K+
**Points:** 4
**Average Time:** 25m

---

## Problem Statement

Given an array `arr[]` of non-negative integers. Find the **length** of the longest sub-sequence such that elements in the subsequence are **consecutive integers**; the consecutive numbers can be in **any order**.

---

## Examples

### Example 1

**Input:** `arr[] = [2, 6, 1, 9, 4, 5, 3]`
**Output:** `6`
**Explanation:** The consecutive numbers here are `1, 2, 3, 4, 5, 6`. These `6` numbers form the longest consecutive subsequence.

### Example 2

**Input:** `arr[] = [1, 9, 3, 10, 4, 20, 2]`
**Output:** `4`
**Explanation:** `1, 2, 3, 4` is the longest consecutive subsequence.

### Example 3

**Input:** `arr[] = [15, 13, 12, 14, 11, 10, 9]`
**Output:** `7`
**Explanation:** The longest consecutive subsequence is `9, 10, 11, 12, 13, 14, 15`, which has a length of `7`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `0 ≤ arr[i] ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

Amazon, Microsoft, Walmart

---

## Topic Tags

Hash, Data Structures

---

## Related Interview Experiences

* Walmart Labs Interview Experience Set 2 On Campus

---

## Related Articles

* [Longest Consecutive Subsequence](https://www.geeksforgeeks.org/longest-consecutive-subsequence/)

---

---

here’s an interview-ready breakdown for **Longest Consecutive Subsequence (length only)**.

---

# 2) Explanation + step-by-step dry run

## Core idea (hash set, O(n))

Put all numbers into a **set** for O(1) average membership tests.
A number `x` can be the **start** of a consecutive run **iff** `(x-1)` is **not** in the set.
When you find such a start, count upward: `x, x+1, x+2, ...` while each is in the set, and keep the best length.

Why it works: every consecutive run has exactly **one** start (its smallest member). We only scan forward from starts, so each element contributes to at most one run count → **O(n)** overall.

### Dry run on `arr = [2, 6, 1, 9, 4, 5, 3]`

Set = `{1,2,3,4,5,6,9}`

* `2`: `1` **is** in set ⇒ not a start → skip
* `6`: `5` in set ⇒ skip
* `1`: `0` not in set ⇒ **start**. Count: `1,2,3,4,5,6` → length = 6 → best = 6
* `9`: `8` not in set ⇒ start. Count `9` only → length = 1 → best stays 6
* `4`: `3` in set ⇒ skip
* `5`: `4` in set ⇒ skip
* `3`: `2` in set ⇒ skip
  Answer = **6**.

Works with duplicates (set removes them) and with negatives (even though problem says non-negative).

---

# 3) Python solutions (optimized + alternatives)

```python
# User function Template for python3

class Solution:
    
    # arr[] : the input array
    # Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self, arr):
        """
        Hash-set start-detection.
        Time:  O(n) average (each element considered as start once; counting
               across the array happens at most n times total)
        Space: O(n) for the set
        """
        if not arr:
            return 0
        
        s = set(arr)          # O(n)
        best = 0
        
        for x in s:           # iterate unique values
            if x - 1 not in s:        # x is a potential start  → O(1) avg
                # count forward from x
                y = x
                while y in s:         # each y across all runs visited once
                    y += 1
                best = max(best, y - x)
        
        return best
```

### Variant A: Sorting (simple, interview-friendly too)

```python
class SolutionSort:
    def longestConsecutive(self, arr):
        """
        Sort + single pass while skipping duplicates.
        Time:  O(n log n) for sort
        Space: O(1) or O(n) depending on sorting implementation
        """
        if not arr:
            return 0
        
        arr.sort()                     # O(n log n)
        best = 1
        cur = 1
        
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                continue               # skip duplicates
            if arr[i] == arr[i-1] + 1:
                cur += 1               # extend run
                best = max(best, cur)
            else:
                cur = 1                # reset run
        
        return best
```

### Variant B: Brute force (educational; avoid in production)

```python
class SolutionBrute:
    def longestConsecutive(self, arr):
        """
        For each value x, try to grow x+1, x+2,... using a set *without* start check.
        This is worst-case O(n^2) when the array is mostly consecutive.
        """
        if not arr:
            return 0
        
        s = set(arr)
        best = 0
        for x in s:
            length = 1
            y = x + 1
            while y in s:
                length += 1
                y += 1
            best = max(best, length)
        return best
```

---

# 4) Interviewer-style Q\&A

**Q1. Why check `x-1 not in set` before counting?**
This guarantees `x` is the **smallest** element of its run. Each run is counted exactly once, so total counting across all runs is O(n).

**Q2. What’s the complexity of the hash-set method?**
Average **O(n) time**, **O(n) space**. Each element is inserted once and looked up O(1) average times. Counting forward visits each element at most once overall.

**Q3. How do duplicates affect the answer?**
They don’t—using a set removes duplicates. With sorting, you must explicitly `continue` on equal neighbors to avoid inflating the streak.

**Q4. Does it work for negative numbers?**
Yes; consecutiveness is arithmetic (`k, k+1, ...`) regardless of sign. The set approach works unchanged.

**Q5. Why not sliding window or two pointers?**
Because the array is not ordered by value. Sliding windows rely on monotonic structure, which we don’t have.

**Q6. Can we also return the actual subsequence?**
You can reconstruct it easily: once you find a start `x` giving `best`, return `[x, x+1, ..., x+best-1]`. The problem asks only for length.

**Q7. Memory concerns with very large ranges?**
Set size is O(n). If memory is tight and `n` fits, the **sorting** variant uses less auxiliary memory (beyond the sort’s needs) and is often acceptable.

---

---

Here’s a **full, runnable Python program** for **Longest Consecutive Subsequence (length only)** that:

* prints outputs for several **input arrays** (input → output),
* includes **inline time/space complexity notes for every step**, and
* **benchmarks** the optimized solution using `timeit` inside `main`.

```python
#!/usr/bin/env python3
"""
Longest Consecutive Subsequence (length)

Goal:
  Given an integer array (any order), return the length of the longest set of
  consecutive integers that appear in the array (order in the array is irrelevant).

Interview-standard approach:
  Put all values in a set. A number x is a START of a streak iff (x-1) not in set.
  From each start, count x, x+1, ... while present; keep the best length.

Complexities:
  • Time:  O(n) average    (each element participates in counting at most once)
  • Space: O(n)            (the hash set of values)

This script:
  1) Implements class Solution.longestConsecutive using the O(n) set method.
  2) Also provides a simple sorting variant for reference.
  3) Prints results for sample inputs (input → output).
  4) Benchmarks the optimized method with timeit.
"""

from __future__ import annotations
import random
import timeit
from typing import List


# -------------------------------------------------------------------
# User function Template for python3
# -------------------------------------------------------------------
class Solution:
    # arr[] : the input array
    # Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self, arr: List[int]) -> int:
        """
        Hash-set start-detection.

        Steps:
          A) Build a set of all values                  -> Time O(n), Space O(n)
          B) For each unique value x in the set:        -> Time O(n) overall
               - If (x-1) not in set, x is a start:     -> O(1) avg lookup
                   count y = x, x+1, ... while in set   -> each y counted once total
               - Update best length                     -> O(1)
          C) Return best                                -> O(1)

        Overall:
          Time  O(n) average, Space O(n).
        """
        if not arr:
            return 0

        s = set(arr)              # A) O(n)/O(n)
        best = 0

        # B) Only extend from starts; each element extended at most once → O(n)
        for x in s:
            if x - 1 not in s:    # x is the smallest in its run
                y = x
                while y in s:     # walk the run forward (across all runs: O(n))
                    y += 1
                best = max(best, y - x)

        return best


# -------- Optional reference variant (sorting) -------- #
class SolutionSort:
    def longestConsecutive(self, arr: List[int]) -> int:
        """
        Sort + scan (simple, but O(n log n) time).
        Space: O(1) aux (ignoring sort's internal needs).
        """
        if not arr:
            return 0
        arr.sort()                # O(n log n)
        best = 1
        cur = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                continue          # skip duplicates
            if arr[i] == arr[i - 1] + 1:
                cur += 1
                best = max(best, cur)
            else:
                cur = 1
        return best


# ------------------------------- Demo & Benchmark -------------------------------

def demo_on_samples() -> None:
    """
    Show correctness on a few inputs.
    Total time here ≈ sum O(n) for each case; space is O(n) for the set per case.
    """
    samples = [
        ([2, 6, 1, 9, 4, 5, 3], 6),        # 1..6 -> length 6
        ([1, 9, 3, 10, 4, 20, 2], 4),      # 1..4 -> 4
        ([15, 13, 12, 14, 11, 10, 9], 7),  # 9..15 -> 7
        ([], 0),
        ([100], 1),
        ([1, 2, 2, 3], 3),                 # duplicates present
    ]

    sol = Solution()
    print("=== Sample Runs (Input → Output) ===")
    for arr, expected in samples:
        out = sol.longestConsecutive(arr)   # O(n) avg
        print(f"Input : {arr}")
        print(f"Output: {out}   (Expected: {expected})")
        print("-" * 60)


def _bench_once(arr: List[int]) -> None:
    """
    Helper for timeit: run the O(n) algorithm.
    Note: method does not mutate arr, so we can reuse the same list.
    """
    Solution().longestConsecutive(arr)


def benchmark() -> None:
    """
    Benchmark the O(n) set-based solution using timeit.

    Prep (outside timing): build one large random array -> O(N) time/space.
    Timed region          : each run does a single O(N) scan (plus set building).
    """
    SIZE = 300_000
    MAXV = 1_000_000
    rng = random.Random(2025)

    # Build the input once (not timed): O(SIZE)
    arr = [rng.randrange(0, MAXV + 1) for _ in range(SIZE)]

    runs = 3
    total = timeit.timeit(lambda: _bench_once(arr), number=runs)

    print("=== Benchmark (Hash-set method: O(n) time / O(n) space) ===")
    print(f"Array size : {SIZE}")
    print(f"Runs       : {runs}")
    print(f"Total time : {total:.6f} s")
    print(f"Avg / run  : {total / runs:.6f} s")
    print("-" * 60)


def main() -> None:
    # 1) Demonstrate on concrete inputs (prints input and output)
    demo_on_samples()
    # 2) Benchmark the optimized solution
    benchmark()


if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (short & important)

1. **Streak analytics**
   Find a user’s **longest login/commit/workout streak** when days are recorded as integers (e.g., YYYYMMDD or day numbers), regardless of order in the database dump.

2. **Monitoring gaps**
   In event or log IDs, compute the longest span of **consecutive IDs** observed to verify ingestion completeness and detect missing intervals.

3. **Inventory / serial validation**
   Determine the longest **continuous range of serial numbers** scanned/produced to assess production consistency or to plan batch processing.

4. **Time-series quality checks**
   Given a set of timestamps quantized to minutes/seconds, measure the longest run of **back-to-back intervals** present (useful in IoT data to flag dropouts).
