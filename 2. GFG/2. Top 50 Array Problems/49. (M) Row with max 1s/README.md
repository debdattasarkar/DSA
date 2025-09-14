# Row with max 1s

**Difficulty:** Medium
**Accuracy:** 33.09%
**Submissions:** 360K+
**Points:** 4

---

## Problem Statement

You are given a 2D binary array `arr[][]` consisting of only `1`s and `0`s. **Each row of the array is sorted in non-decreasing order.** Your task is to find and return the **index of the first row that contains the maximum number of 1s**. If no such row exists, return `-1`.

### Note

* The array follows **0-based indexing**.
* The number of rows and columns in the array are denoted by `n` and `m` respectively.

---

## Examples

### Example 1

**Input:** `arr = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]`
**Output:** `2`
**Explanation:** Row `2` contains the most number of 1s (**4** 1s). Hence, the output is `2`.

### Example 2

**Input:** `arr = [[0,0], [1,1]]`
**Output:** `1`
**Explanation:** Row `1` contains the most number of 1s (**2** 1s). Hence, the output is `1`.

### Example 3

**Input:** `arr = [[0,0], [0,0]]`
**Output:** `-1`
**Explanation:** No row contains any 1s, so the output is `-1`.

---

## Constraints

* `1 ≤ arr.size(), arr[i].size() ≤ 10^3`
* `0 ≤ arr[i][j] ≤ 1`

---

## Expected Complexities

* **Time Complexity:** `O(n + m)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Amazon, Microsoft, Snapdeal

---

## Topic Tags

Arrays, Matrix, Data Structures

---

## Related Articles

* [Find The Row With Maximum Number 1s](https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/)


---

---

here’s a clean, interview-ready bundle for **“Row with max 1s”** (rows are sorted 0→1).

---

## 2) Explanation + step-by-step dry run

### Core observation

Each row is sorted non-decreasing (`000…0111…1`).
Start at the **top-right** cell and do a **staircase walk**:

* If you see a **1**, move **left** (this row has at least as many 1s as any previous best). Record this row index.
* If you see a **0**, move **down** (this row can’t beat current best at this column or further right).
* Stop when you fall off the left edge (j < 0) or bottom (i == n).

This visits at most **n + m** cells → `O(n + m)` time, `O(1)` space.
Return the **first** row with the maximum number of 1s (the algorithm only updates when it finds **strictly more** 1s, so ties keep the earlier row).

### Dry run

`arr = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]` (n=4, m=4)
Start `i=0, j=3, best=-1`.

* (0,3)=1 → move left; `best=0`, `j=2`
* (0,2)=1 → left; `best=0`, `j=1`
* (0,1)=1 → left; `best=0`, `j=0`
* (0,0)=0 → down; `i=1`
* (1,0)=0 → down; `i=2`
* (2,0)=1 → left; `best=2`, `j=-1`  ⇒ off the left edge → **stop**.

Answer `best = 2`. (Row 2 has 4 ones, which is maximal.)

Edge cases:

* Empty matrix or no `1` in any row → return `-1`.
* If multiple rows tie, we keep the first we discovered (lowest index).

---

## 3) Python solutions (optimized + alternatives)

### A) Staircase method — **O(n + m)** (most expected)

```python
"""
class Solution:
    def rowWithMax1s(self, arr):
        # code here
"""
class Solution:
    def rowWithMax1s(self, arr):
        """
        Staircase walk from top-right.
        Time : O(n + m)   (each step moves either left or down)
        Space: O(1)
        Returns: index of first row having the maximum number of 1s, else -1.
        """
        if not arr or not arr[0]:
            return -1

        n, m = len(arr), len(arr[0])
        i, j = 0, m - 1
        best_row = -1

        while i < n and j >= 0:
            if arr[i][j] == 1:
                # Found a 1: this row beats all rows seen so far at column j..m-1.
                best_row = i
                j -= 1                  # move left to try to find even more 1s here
            else:
                # Found a 0: this row has 0s up to j, can't improve here -> go down.
                i += 1

        return best_row
```

### B) Binary search per row — **O(n log m)**

Find the first `1` in each row; `ones = m - first_one_index`. Track max and earliest row.

```python
class SolutionBinarySearch:
    def rowWithMax1s(self, arr):
        """
        For each row, binary search the first 1.
        Time : O(n log m)
        Space: O(1)
        """
        if not arr or not arr[0]:
            return -1
        n, m = len(arr), len(arr[0])

        def first_one(row):
            lo, hi = 0, m - 1
            ans = m  # default: no 1s
            while lo <= hi:
                mid = (lo + hi) // 2
                if row[mid] == 1:
                    ans = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            return ans  # m if no 1s

        best_row, best_ones = -1, 0
        for i in range(n):
            idx = first_one(arr[i])
            ones = m - idx
            if ones > best_ones:
                best_ones = ones
                best_row = i
        return -1 if best_ones == 0 else best_row
```

### C) Brute force count — **O(n·m)** (baseline)

Count `1`s in each row (e.g., `sum(row)` since entries are 0/1); keep the earliest row with the maximum.

```python
class SolutionBrute:
    def rowWithMax1s(self, arr):
        """
        Sum each row; keep earliest row with max sum.
        Time : O(n * m)
        Space: O(1)
        """
        if not arr or not arr[0]:
            return -1
        best_row, best_ones = -1, 0
        for i, row in enumerate(arr):
            ones = sum(row)          # O(m)
            if ones > best_ones:
                best_ones = ones
                best_row = i
        return -1 if best_ones == 0 else best_row
```

---

## 4) Interviewer-style Q\&A

**Q1. Why does the staircase method run in O(n + m)?**
You start at (0, m−1). Each step moves **left** (j−−) or **down** (i++). You can move left at most `m` times and down at most `n` times → total ≤ `n + m`.

**Q2. Why do we update the answer only when we move left from a 1?**
Moving left past a 1 means we just proved this row has **strictly more** 1s than any row that hasn’t moved this far left yet. That’s when we can safely record a better row.

**Q3. How do we ensure we return the *first* row in case of ties?**
We update the row **only** when we find strictly more 1s (move left). If a later row ties, it won’t move left beyond the current boundary, so we keep the earlier row.

**Q4. What if all rows are zeros?**
The staircase never moves left; `best_row` remains `-1` and we return `-1`.

**Q5. When would you choose binary search per row instead?**
If you dislike pointer logic or want a straightforward proof using sorted rows, `O(n log m)` is simple and robust.

**Q6. Can this be extended if rows aren’t sorted?**
Without sorted rows, these optimizations don’t apply. You’d need `O(n·m)` counting or precomputation (e.g., prefix sums) after sorting rows individually (which changes the problem).

**Q7. Memory usage?**
All approaches above are **O(1)** auxiliary space (besides input), since we only keep a few scalars.

---

---

Here’s a **full, runnable Python program** for **Row with max 1s** that:

* implements the classic **O(n + m)** “staircase” solution,
* shows **inputs → outputs** for sample matrices,
* and **benchmarks** the implementation with `timeit` inside `main`.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Row with max 1s (rows are sorted 0…0 1…1)

Algorithm used below (interview-standard):
  • Start at top-right and walk like a staircase:
      - If arr[i][j] == 1: update answer to row i, move LEFT (j -= 1)
      - Else (0)         : move DOWN (i += 1)
  • Each step moves left or down → at most n + m steps total.

Big-O summary:
  • Time  : O(n + m)         (staircase walk touches ≤ n+m cells)
  • Space : O(1) auxiliary   (few scalars only)

This script:
  1) Implements class Solution.rowWithMax1s (staircase).
  2) Also includes a Binary-Search-per-row variant for reference.
  3) Prints results for sample inputs (input → output).
  4) Benchmarks the staircase method with timeit on a large random matrix
     (with each row sorted as required).
"""

from __future__ import annotations
import random
import timeit
from typing import List


# -------------------------------------------------------------------
# Primary solution: O(n + m) staircase walk
# -------------------------------------------------------------------
class Solution:
    def rowWithMax1s(self, arr: List[List[int]]) -> int:
        """
        Return index of the FIRST row containing the maximum number of 1s;
        return -1 if no 1 exists.

        Steps (with local complexity):
          A) Guard for empty input                     -> O(1)
          B) Start at (i=0, j=m-1) (top-right)         -> O(1)
          C) While in-bounds:
               - if 1: best_row = i; j -= 1            -> move LEFT (≤ m times)
               - else: i += 1                          -> move DOWN (≤ n times)
             Total steps ≤ n + m → O(n + m)
          D) Return best_row                           -> O(1)
        Space: O(1) (only a few integers)
        """
        if not arr or not arr[0]:   # A)
            return -1

        n, m = len(arr), len(arr[0])
        i, j = 0, m - 1             # B)
        best_row = -1

        # C) Staircase walk
        while i < n and j >= 0:
            if arr[i][j] == 1:
                best_row = i
                j -= 1              # move LEFT to see if this row has more 1s
            else:
                i += 1              # move DOWN; this row can’t beat at this column

        return best_row             # D)


# -------------------------------------------------------------------
# Optional: Binary-search-per-row (O(n log m)) for reference
# -------------------------------------------------------------------
class SolutionBinarySearch:
    def rowWithMax1s(self, arr: List[List[int]]) -> int:
        if not arr or not arr[0]:
            return -1
        n, m = len(arr), len(arr[0])

        def first_one(row: List[int]) -> int:
            lo, hi, ans = 0, m - 1, m  # default m means "no 1s"
            while lo <= hi:
                mid = (lo + hi) // 2
                if row[mid] == 1:
                    ans = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            return ans

        best_row, best_ones = -1, 0
        for i, row in enumerate(arr):           # n rows
            idx = first_one(row)                # O(log m)
            ones = m - idx
            if ones > best_ones:
                best_ones, best_row = ones, i
        return -1 if best_ones == 0 else best_row


# --------------------------- Demo & Benchmark ---------------------------

def demo_on_samples() -> None:
    """
    Demonstrate correctness on the three examples.
    Time per case: O(n + m), Space: O(1).
    """
    samples = [
        ([[0,1,1,1],
          [0,0,1,1],
          [1,1,1,1],
          [0,0,0,0]], 2),

        ([[0,0],
          [1,1]], 1),

        ([[0,0],
          [0,0]], -1),
    ]

    sol = Solution()
    print("=== Sample Runs (Input → Output) ===")
    for mat, expected in samples:
        out = sol.rowWithMax1s(mat)
        print("Matrix:")
        for row in mat:
            print(row)
        print(f"Output  : {out}")
        print(f"Expected: {expected}")
        print("-" * 60)


def make_sorted_binary_matrix(n: int, m: int, rng: random.Random) -> List[List[int]]:
    """
    Build an n x m binary matrix where each row is sorted non-decreasing:
      row = [0]*(m-k) + [1]*k with random k in [0..m].
    Time:  O(n*m).  Space: O(n*m).
    """
    mat = []
    for _ in range(n):
        k = rng.randrange(0, m + 1)
        row = [0] * (m - k) + [1] * k
        mat.append(row)
    return mat


def _bench_once(mat: List[List[int]]) -> None:
    """Single timed call to the O(n + m) algorithm."""
    Solution().rowWithMax1s(mat)


def benchmark() -> None:
    """
    Benchmark the staircase method using timeit.

    We generate one large matrix (outside timing), then call the solver
    multiple times on the same matrix to measure algorithmic time.
    """
    rng = random.Random(2025)
    n, m = 800, 800                                  # 640k cells (~tens of MB)
    mat = make_sorted_binary_matrix(n, m, rng)       # O(n*m) (not timed below)

    runs = 1000
    total = timeit.timeit(lambda: _bench_once(mat), number=runs)

    print("=== Benchmark (Staircase O(n + m)) ===")
    print(f"Matrix size : {n} x {m}")
    print(f"Runs        : {runs}")
    print(f"Total time  : {total:.6f} s")
    print(f"Avg / run   : {total / runs:.6f} s")
    print("-" * 60)


def main() -> None:
    # 1) Show outputs for explicit inputs (includes the inputs and outputs)
    demo_on_samples()

    # 2) Benchmark the optimized method with timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (short & important)

1. **Threshold tables (best performer detection)**
   Rows are items (sensors, candidates) and columns are **increasing thresholds**. Cell is `1` if the item’s value ≥ threshold. Each row is monotone (`0…01…1`). The row with the most `1`s corresponds to the **largest value**.

2. **Image / silhouette analysis**
   In a binary silhouette where each row transitions from background (`0`) to object (`1`) and stays `1`, the row with maximum `1`s is the **widest cross-section**—useful for sizing, defect detection, or alignment.

3. **Quality control across specs**
   For products tested against progressively stricter specs (columns), a `1` marks “passes spec”. The row with the most `1`s identifies the unit with **highest quality margin**.

4. **Feature gating by rank cutoffs**
   Users sorted by rank; columns are monotone gates (e.g., access at ≥ certain rank). The row with max `1`s signals users with **widest feature access**.

