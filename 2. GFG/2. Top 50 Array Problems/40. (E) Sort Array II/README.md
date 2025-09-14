# Sort Array II

**Difficulty:** Easy
**Accuracy:** 41.02%
**Submissions:** 131K+
**Points:** 2

---

## Problem Statement

Given an unsorted array `arr[]` of numbers, sort the array in **ascending order**.

---

## Examples

### Example 1

**Input:** `arr[] = [1, 5, 3, 2]`
**Output:** `[-, 1, 2, 3, 5]` → final array: `[1, 2, 3, 5]`
**Explanation:** After sorting, array will be like `[1, 2, 3, 5]`.

### Example 2

**Input:** `arr[] = [3, 1]`
**Output:** `[1, 3]`
**Explanation:** After sorting, array will be like `[1, 3]`.

### Example 3

**Input:** `arr[] = [1, 2, 3]`
**Output:** `[1, 2, 3]`
**Explanation:** It's already sorted in ascending order.

---

## Constraints

* `1 ≤ arr.size ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Cisco

---

## Topic Tags

Sorting, Algorithms

---

## Related Articles

* Arrays Sort In Java With Examples
* Cpp Program To Sort The Elements Of An Array In Ascending Order
* Java Program To Sort The Elements Of An Array In Ascending Order
* Sort C Stl

---

---

here’s an interview-ready pack for **Sort Array II** (ascending order).

---

# 2) Explanation + step-by-step dry run

## What are we asked?

Given an unsorted array, return it in **ascending** order. Target complexity is typically **O(n log n)** time and (if the problem insists) **O(1)** auxiliary space.

### Options at a glance

* **Built-in sort (Timsort)** — cleanest for Python; `O(n log n)` time, stable; extra space is small but not strictly `O(1)` in the worst case.
* **Heapsort (in-place)** — `O(n log n)` time, **O(1)** extra, not stable.
* **Merge sort** — `O(n log n)` time, `O(n)` extra, stable.
* **Quadratic baselines** — Selection/Bubble/Insertion sort: `O(n²)`.

### Dry run (Heapsort) on `arr = [1, 5, 3, 2]`

**Goal:** build a **max-heap**, then repeatedly swap the max to the end.

1. **Build max-heap** (sift down from last parent `i = ⌊(n-2)/2⌋` to `0`)

* Start: `[1, 5, 3, 2]`, `n=4`
* `i=1` (node `5` with child `2`): already max w\.r.t child → unchanged `[1,5,3,2]`
* `i=0` (node `1` with children `5,3`): largest child `5` → swap → `[5,1,3,2]`

  * Sift `1` with its child `2` → swap → `[5,2,3,1]`
  * Heap built: `[5,2,3,1]`

2. **Extract max** (swap heap\[0] with heap\[end], shrink heap, sift down)

* Swap 0 & 3 → `[1,2,3,5]` (heap size=3). Sift `1` against `2,3` → swap with `3` → `[3,2,1,5]`.
* Swap 0 & 2 → `[1,2,3,5]` (heap size=2). Sift `1` vs `2` → swap → `[2,1,3,5]`.
* Swap 0 & 1 → `[1,2,3,5]` (heap size=1). Done.

Result: **`[1, 2, 3, 5]`**

---

# 3) Python solutions (brute + optimized, interview-friendly)

```python
class Solution:
    def sortArr(self, arr):
        """
        In-place HEAPSORT (meets O(1) auxiliary space target)
        Time:  O(n log n)  -- building heap O(n), then n-1 sift-downs O(log n) each
        Space: O(1)        -- in-place (ignoring recursion; we use iterative sift)
        Returns the sorted array (ascending).
        """
        n = len(arr)

        # ---- helper: sift-down the element at index i within heap of size n ----
        def sift_down(i, heap_size):
            # Time per call: O(log n)
            while True:
                left = 2 * i + 1
                right = left + 1
                largest = i
                if left < heap_size and arr[left] > arr[largest]:
                    largest = left
                if right < heap_size and arr[right] > arr[largest]:
                    largest = right
                if largest == i:
                    break
                arr[i], arr[largest] = arr[largest], arr[i]  # swap
                i = largest

        # 1) Build max-heap: sift down from last parent to root
        #    Time: O(n) total
        for i in range((n - 2) // 2, -1, -1):
            sift_down(i, n)

        # 2) Repeatedly extract max to the end; shrink heap; restore heap
        #    Time: O(n log n)
        for end in range(n - 1, 0, -1):
            arr[0], arr[end] = arr[end], arr[0]  # move current max to its final place
            sift_down(0, end)                    # restore heap on the reduced prefix

        return arr
```

### A) One-liner using Python’s built-in (Timsort) — simplest

```python
class SolutionBuiltin:
    def sortArr(self, arr):
        """
        Python's built-in .sort() (Timsort, stable).
        Time:  O(n log n) average/worst
        Space: O(n) worst-case (implementation-dependent, usually small)
        """
        arr.sort()          # sorts in place, ascending
        return arr
```

### B) Merge Sort (stable, educational)

```python
class SolutionMerge:
    def sortArr(self, arr):
        """
        Top-down merge sort (stable).
        Time:  O(n log n)
        Space: O(n) for temp arrays
        """
        def merge_sort(a):
            if len(a) <= 1:
                return a
            mid = len(a) // 2
            left = merge_sort(a[:mid])
            right = merge_sort(a[mid:])
            # merge two sorted lists
            i = j = 0
            out = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    out.append(left[i]); i += 1
                else:
                    out.append(right[j]); j += 1
            out.extend(left[i:]); out.extend(right[j:])
            return out

        res = merge_sort(arr)
        # copy back to keep the same "in-place" signature style
        arr[:] = res
        return arr
```

### C) Brute baseline — Selection Sort (`O(n²)`, in-place)

```python
class SolutionSelection:
    def sortArr(self, arr):
        """
        Selection sort baseline (for very small n or interview warm-up).
        Time:  O(n^2)
        Space: O(1)
        """
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
```

---

# 4) Interviewer-style Q\&A

**Q1. Why pick Heapsort here?**
Because some prompts specify **O(1) auxiliary space**. Heapsort is in-place `O(1)` extra and `O(n log n)` time. It’s not stable, but that’s usually fine unless stability is required.

**Q2. When would you choose Python’s built-in sort?**
Almost always in production Python: it’s **Timsort**, stable, optimized for partially sorted data, and `O(n log n)` time. If the judge allows built-ins and doesn’t demand `O(1)` space, use it.

**Q3. Stability—do we need it?**
If equal keys must preserve original order (e.g., sort by secondary key later), you need a **stable** sort (Timsort/Merge sort). Heapsort/QuickSort (in-place) are not stable by default.

**Q4. What’s the worst case for Heapsort vs Merge?**
Both are `O(n log n)` worst case. Merge sort usually has better constant factors on random data but costs `O(n)` extra memory; Heapsort uses `O(1)` extra but can have more swaps.

**Q5. How do you optimize for nearly sorted inputs?**
Timsort excels: it detects “runs” and can approach **O(n)**. In interviews, you can mention **Insertion sort** with sentinel for small/near-sorted arrays (`O(n + k)` where `k` is # inversions).

**Q6. What about negative numbers or duplicates?**
All provided algorithms handle them naturally. Stability only matters for duplicates.

**Q7. Can QuickSort be used?**
Yes; **randomized QuickSort** is expected `O(n log n)` but worst case `O(n²)`. In production, Python avoids this by using Timsort for `.sort()`.


---

---

You got it! Here’s a **full, runnable Python program** for **Sort Array II (ascending)** that:

* prints results for a few **input arrays** (input → output),
* adds **inline time/space complexity** comments for every step,
* and **benchmarks** the main solution with `timeit` right inside `main`.

```python
#!/usr/bin/env python3
"""
Sort Array II — Ascending Order

Primary approach in this script: **Heapsort** (in-place, O(1) auxiliary space).
Why: many judges hint at O(1) extra-space sorting; heapsort satisfies that while
keeping O(n log n) time. (Python's built-in Timsort is excellent too, but may
use more than O(1) auxiliary space in worst case.)

This file:
  1) Implements `class Solution.sortArr` using in-place HEAPSORT.
  2) Demonstrates outputs on sample inputs (prints input → output).
  3) Benchmarks the algorithm with `timeit` in `main`.

Author notes: Each step lists time/space complexity in comments.
"""

from __future__ import annotations
import random
import timeit
from typing import List


class Solution:
    def sortArr(self, arr: List[int]) -> List[int]:
        """
        In-place **HEAPSORT** (ascending).

        Steps:
          A) Build a max-heap in-place (bottom-up sift-down from last parent).
             Time:  O(n)        Space: O(1)
          B) Repeatedly extract the max:
               - swap arr[0] with arr[end]
               - reduce heap size by 1
               - sift-down from root to restore heap
             Time:  O(n log n)  Space: O(1)
          C) Return the array (now sorted ascending).
             Time:  O(1)        Space: O(1)
        Overall: **Time O(n log n), Space O(1)**.
        """
        n = len(arr)

        # ---- helper: iterative sift-down (O(log n) per call) ----
        def sift_down(i: int, heap_size: int) -> None:
            # Move element at i down until heap property satisfied.
            while True:
                left = 2 * i + 1
                right = left + 1
                largest = i
                if left < heap_size and arr[left] > arr[largest]:
                    largest = left
                if right < heap_size and arr[right] > arr[largest]:
                    largest = right
                if largest == i:
                    break
                arr[i], arr[largest] = arr[largest], arr[i]
                i = largest

        # A) Build max-heap: sift down from last parent to root — O(n)/O(1)
        for i in range((n - 2) // 2, -1, -1):
            sift_down(i, n)

        # B) Pop max n-1 times — O(n log n)/O(1)
        for end in range(n - 1, 0, -1):
            arr[0], arr[end] = arr[end], arr[0]  # move current max to its final position
            sift_down(0, end)                    # restore heap in the reduced prefix

        # C) Done — O(1)/O(1)
        return arr


# ---------- Optional reference implementations (not used in the benchmark) ----------

class SolutionBuiltin:
    def sortArr(self, arr: List[int]) -> List[int]:
        """
        Python built-in Timsort (stable).
        Time:  O(n log n) average/worst
        Space: not strictly O(1) in worst case
        """
        arr.sort()
        return arr


class SolutionMerge:
    def sortArr(self, arr: List[int]) -> List[int]:
        """
        Top-down Merge Sort (stable).
        Time:  O(n log n)
        Space: O(n) extra for temporary arrays
        """
        def merge_sort(a: List[int]) -> List[int]:
            if len(a) <= 1:
                return a
            mid = len(a) // 2
            left = merge_sort(a[:mid])
            right = merge_sort(a[mid:])
            i = j = 0
            out: List[int] = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    out.append(left[i]); i += 1
                else:
                    out.append(right[j]); j += 1
            out.extend(left[i:]); out.extend(right[j:])
            return out

        arr[:] = merge_sort(arr)
        return arr


# ------------------------------- Demo & Benchmark -------------------------------

def demo_on_samples() -> None:
    """
    Print results for several inputs (input → output) using the heapsort solution.
    Overall time: proportional to total input length * log(length).
    Extra space: O(1) ignoring the printing.
    """
    samples = [
        [1, 5, 3, 2],        # -> [1, 2, 3, 5]
        [3, 1],              # -> [1, 3]
        [1, 2, 3],           # -> [1, 2, 3] (already sorted)
        [5, 5, 2, -1, 0, 9], # includes negatives/dupes
    ]

    sol = Solution()
    print("=== Sample Runs (Input → Output) ===")
    for arr in samples:
        original = list(arr)
        out = sol.sortArr(arr)  # in-place heapsort, O(n log n)/O(1)
        print(f"Input : {original}")
        print(f"Output: {out}")
        print("-" * 60)


def _bench_once(base_arr: List[int]) -> None:
    """
    Helper for timeit: make a fresh copy (so each run sorts the same unsorted data),
    then run the O(n log n) heapsort.
    Copy cost is O(n) but is part of practical end-to-end timing commonly reported.
    """
    arr = list(base_arr)              # O(n) copy
    Solution().sortArr(arr)           # O(n log n) heapsort


def benchmark() -> None:
    """
    Benchmark the heapsort-based Solution using timeit.

    Prep (outside timed region): build a random unsorted array once — O(N) time/space.
    Timed region: each iteration copies the base array (O(N)) and sorts it (O(N log N)).
    """
    SIZE = 200_000
    rng = random.Random(42)
    base_arr = [rng.randrange(-10**6, 10**6) for _ in range(SIZE)]

    runs = 3
    total = timeit.timeit(lambda: _bench_once(base_arr), number=runs)

    print("=== Benchmark (Heapsort O(n log n), O(1) extra) ===")
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

## Real-World Use Cases (short & important)

1. **Batch data preparation / ETL**
   Sorting records by keys (timestamp, user ID, price) to enable **merge-joins**, duplicate collapsing, or range queries.

2. **Leaderboards / ranking**
   Periodically sort scores or metrics to produce **top-K** lists or percentile buckets. (Heapsort gives tight memory bounds when needed.)

3. **External sort building blocks**
   While external sorting uses runs and merging, each in-memory partition still needs an **O(n log n)** sort before spilling/merging.
