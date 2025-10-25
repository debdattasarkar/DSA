# Chocolate Distribution Problem

**Difficulty:** Easy
**Accuracy:** 49.91%
**Submissions:** 261K+
**Points:** 2
**Average Time:** 15m

---

## Problem Statement

Given an array `arr[]` of positive integers, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are `m` students; the task is to distribute chocolate packets among `m` students such that:

1. Each student gets **exactly one** packet.
2. The difference between the **maximum** number of chocolates given to a student and the **minimum** number of chocolates given to a student is **minimum**—return that minimum possible difference.

---

## Examples

### Example 1

**Input:** `arr = [3, 4, 1, 9, 56, 7, 9, 12], m = 5`
**Output:** `6`
**Explanation:** The minimum difference between maximum chocolates and minimum chocolates is `9 - 3 = 6` by choosing the following `m` packets: `[3, 4, 9, 7, 9]`.

### Example 2

**Input:** `arr = [7, 3, 2, 4, 9, 12, 56], m = 3`
**Output:** `2`
**Explanation:** The minimum difference between maximum chocolates and minimum chocolates is `4 - 2 = 2` by choosing the packets: `[3, 2, 4]`.

### Example 3

**Input:** `arr = [3, 4, 1, 9, 56], m = 5`
**Output:** `55`
**Explanation:** With 5 packets for 5 students, each student will receive one packet, so the difference is `56 - 1 = 55`.

---

## Constraints

* `1 ≤ m ≤ arr.size ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^9`

---

## Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Flipkart

---

## Topic Tags

Sorting, Algorithms

---

## Related Interview Experiences

* Flipkart Interview Experience Set 24

---

## Related Articles

* [Chocolate Distribution Problem](https://www.geeksforgeeks.org/chocolate-distribution-problem/)

---

---

here’s an interview-ready bundle for the **Chocolate Distribution Problem** (minimize `max - min` over any `M` chosen packets; each student gets exactly one packet).

---

# 2) Explanation + step-by-step dry run

## Intuition

To minimize the unfairness `max − min` among `M` packets:

1. **Sort** the packets by chocolates.
2. In the sorted list, the best group of `M` packets must be a **contiguous window** of length `M`.

   * Any `M` chosen packets can be rearranged in non-decreasing order; their spread is the last minus the first — exactly what a contiguous window measures.
3. Slide a window of size `M` across the sorted array and keep the smallest difference `arr[i+M-1] - arr[i]`.

**Corner cases**

* If `M == 0` → nobody to serve → `0`.
* If `M == 1` → one packet to one student → difference `0`.
* If `M > n` → impossible → often return `-1` (GFG style).

### Dry run 1

`arr = [7, 3, 2, 4, 9, 12, 56]`, `M = 3`
Sort → `[2, 3, 4, 7, 9, 12, 56]`
Windows (size 3):

* `[2,3,4]` → `4-2 = 2` ← **best so far**
* `[3,4,7]` → `7-3 = 4`
* `[4,7,9]` → `9-4 = 5`
* `[7,9,12]` → `12-7 = 5`
* `[9,12,56]` → `56-9 = 47`
  Answer = **2**.

### Dry run 2

`arr = [3, 4, 1, 9, 56, 7, 9, 12]`, `M = 5`
Sort → `[1, 3, 4, 7, 9, 9, 12, 56]`
Windows:

* `[1..9]` → `9-1 = 8`
* `[3..9]` → `9-3 = 6` ← **best**
* `[4..12]` → `12-4 = 8`
* `[7..56]` → `56-7 = 49`
  Answer = **6**.

---

# 3) Python solutions (optimized + brute)

```python
# User function Template for python3
class Solution:
    def findMinDiff(self, arr, M):
        """
        Optimized: sort + sliding window
        Time:  O(n log n) for sorting + O(n) scan
        Space: O(1) auxiliary (sort in-place; ignore recursion)
        Returns the minimum possible difference (max-min) among any M packets;
        -1 if M > n. For M in {0,1}, result is 0.
        """
        n = len(arr)
        if M == 0 or M == 1:
            return 0
        if M > n:
            return -1

        # sort packets by chocolates — O(n log n)
        arr.sort()

        # slide a window of size M, track minimal spread — O(n)
        best = float('inf')
        for i in range(n - M + 1):
            spread = arr[i + M - 1] - arr[i]  # max - min in this window
            if spread < best:
                best = spread

        return best
```

### Brute force (educational, only for tiny n)

Try all `nC M` choices and compute `max - min` for each.

```python
from itertools import combinations

class SolutionBrute:
    def findMinDiff(self, arr, M):
        """
        Brute force: check every combination of M packets.
        Time:  O(C(n,M) * M)  (infeasible for large n)
        Space: O(M) for combination tuple
        """
        n = len(arr)
        if M == 0 or M == 1:
            return 0
        if M > n:
            return -1

        best = float('inf')
        for combo in combinations(arr, M):
            spread = max(combo) - min(combo)
            if spread < best:
                best = spread
        return best
```

---

# 4) Interviewer-style Q\&A

**Q1. Why does sorting + contiguous window give the optimum?**
Because for any chosen `M` packets, when you sort those `M` values, their spread is `last - first`. In the global sorted array, those `M` values lie between their smallest and largest positions, which is contained within some contiguous window of size `M`. Minimizing over all windows hence minimizes `max - min`.

**Q2. What’s the time and space complexity?**
`O(n log n)` time due to sorting; one linear pass after. Auxiliary space `O(1)` (in-place sort), ignoring the output itself.

**Q3. How do you handle `M == 0`, `M == 1`, or `M > n`?**

* `M == 0` or `M == 1` → difference `0`.
* `M > n` → impossible; return `-1` (typical GFG convention).

**Q4. Do duplicates or very large numbers matter?**
Duplicates are fine—windows may contain equal values which only help reduce the spread. The algorithm uses subtraction only; use 64-bit where needed (Python ints are unbounded).

**Q5. Can we do better than `O(n log n)`?**
Not in the comparison model for arbitrary large integers; you need to at least order values. For small bounded ranges you could use counting sort to get `O(n + K)` where `K` is the value range.

**Q6. How would you return the actual chosen packets?**
Keep track of the window index `best_i` that minimized `arr[i+M-1]-arr[i]`; the packets are `arr[best_i : best_i + M]` after sorting.

---

---

Here’s a **full, runnable Python program** for the **Chocolate Distribution Problem** that:

* prints results for several **input cases** (input → output),
* includes **inline time & space complexity** notes at each step, and
* **benchmarks** the optimized solution using `timeit` right inside `main`.

```python
#!/usr/bin/env python3
"""
Chocolate Distribution Problem
Given packet sizes (chocolates per packet) and M students, pick exactly M packets
so that the difference (max - min) among those M is minimum.

Core idea (interview-standard):
  1) Sort the array.                                  -> O(n log n) time, O(1) aux
  2) Slide a window of length M; minimize arr[i+M-1]-arr[i]  -> O(n) time
Overall complexity: O(n log n) time, O(1) auxiliary space.

This script:
  - Implements class Solution.findMinDiff (optimized).
  - Adds a tiny brute-force (for very small n) to sanity-check.
  - Prints outputs for sample inputs.
  - Benchmarks the optimized method with timeit.
"""

from __future__ import annotations
import random
import timeit
from typing import List
from itertools import combinations


# ------------------------- Optimized Solution -------------------------

class Solution:
    def findMinDiff(self, arr: List[int], M: int) -> int:
        """
        Sort + sliding window (contiguous in sorted order)
        Time:
          - sort: O(n log n)
          - single pass: O(n)
          => O(n log n) overall
        Space:
          - O(1) auxiliary (in-place sort + a few scalars)

        Returns:
          Minimum possible difference (max - min) among any M packets.
          Edge cases:
            - M == 0 or M == 1 -> 0
            - M > len(arr)     -> -1  (impossible)
        """
        n = len(arr)

        # Fast edge cases — O(1) time/space
        if M == 0 or M == 1:
            return 0
        if M > n:
            return -1

        # Step 1: sort packets — O(n log n) time / O(1) extra
        arr.sort()

        # Step 2: scan windows of size M — O(n) time / O(1) extra
        best = float('inf')
        for i in range(n - M + 1):
            # Spread of current window = last - first
            spread = arr[i + M - 1] - arr[i]   # O(1)
            if spread < best:
                best = spread

        # Step 3: answer — O(1)
        return best


# ------------------------- Brute Force (tiny n only) -------------------------

class SolutionBrute:
    def findMinDiff(self, arr: List[int], M: int) -> int:
        """
        Brute force over all combinations of size M (for educational checks).
        Time:  O(C(n, M) * M)   -> infeasible for large n
        Space: O(M)              -> to hold a combination
        """
        n = len(arr)
        if M == 0 or M == 1:
            return 0
        if M > n:
            return -1

        best = float('inf')
        for combo in combinations(arr, M):      # generates all M-combinations
            spread = max(combo) - min(combo)    # O(M)
            if spread < best:
                best = spread
        return best


# ------------------------------ Demo & Benchmark ------------------------------

def demo_on_samples() -> None:
    """
    Show correctness on sample inputs.
    Total time: sum over cases (dominated by sort O(n log n))
    Space: O(1) auxiliary beyond the arrays themselves.
    """
    samples = [
        # (arr, M, expected)
        ([3, 4, 1, 9, 56, 7, 9, 12], 5, 6),   # from prompt
        ([7, 3, 2, 4, 9, 12, 56],       3, 2),
        ([3, 4, 1, 9, 56],              5, 55),
        ([5, 5, 5, 5],                   2, 0),  # duplicates OK
        ([1, 2, 3],                      4, -1), # impossible (M>n)
        ([42],                           1, 0),  # one student
        (list(range(100, 111)),          1, 0),  # M==1 -> 0
    ]

    sol = Solution()
    print("=== Sample Runs (Input → Output) ===")
    for arr, m, expected in samples:
        arr_print = list(arr)
        out = sol.findMinDiff(arr, m)  # O(n log n)
        print(f"arr: {arr_print}\nM: {m}")
        print(f"Output  : {out}")
        print(f"Expected: {expected}")
        print("-" * 60)


def _bench_once(base_arr: List[int], M: int) -> None:
    """
    Helper for timeit:
    - We pass a COPY into findMinDiff because it sorts in-place.
    - Copy: O(n)
    - findMinDiff: O(n log n)
    """
    arr = list(base_arr)               # O(n) copy
    Solution().findMinDiff(arr, M)     # O(n log n)


def benchmark() -> None:
    """
    Benchmark the optimized solution using timeit.

    Prep (outside timed region):
      - Build a random array once (size SIZE, values up to 1e9) — O(n).

    Timed region:
      - Each run: copy + sort+scan — O(n) + O(n log n).
    """
    SIZE = 200_000
    M = 100
    rng = random.Random(2025)

    # Build base input once — O(SIZE) time/space
    base_arr = [rng.randrange(1, 10**9) for _ in range(SIZE)]

    runs = 3
    total = timeit.timeit(lambda: _bench_once(base_arr, M), number=runs)

    print("=== Benchmark (Sort+Window O(n log n) / O(1) aux) ===")
    print(f"Array size : {SIZE},  M : {M}")
    print(f"Runs       : {runs}")
    print(f"Total time : {total:.6f} s")
    print(f"Avg / run  : {total / runs:.6f} s")
    print("-" * 60)


def main() -> None:
    # 1) Demonstrate outputs for sample inputs (includes input values)
    demo_on_samples()

    # 2) Benchmark the optimized method
    benchmark()


if __name__ == "__main__":
    main()
```

---

## Real-World Use Cases (short & important)

1. **Fair kit/pack assignment**
   When packing kits (medical tests, snacks, swag) with varying counts per pack, choose `M` packs for a cohort so the **max–min** difference is minimal → consistent user experience.

2. **Server or VM selection with variability**
   From many nodes with fluctuating free capacity, pick `M` nodes whose **available-capacity spread** is minimal to ensure **balanced** and predictable performance across assigned jobs.

3. **Scholarship or grant brackets**
   Given proposed award amounts (packets), select `M` awards such that the **spread** within a specific program is minimal—helps enforce **equity** within a cohort.

4. **Manufacturing sample selection**
   Choose `M` items from a batch so that the **property range** (e.g., weight, thickness) is as tight as possible for calibration or validation runs.
