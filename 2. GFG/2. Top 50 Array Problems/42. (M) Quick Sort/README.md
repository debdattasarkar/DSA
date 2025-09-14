# Quick Sort

**Difficulty:** Medium
**Accuracy:** 55.23%
**Submissions:** 288K+
**Points:** 4
**Average Time:** 15m

---

## Problem Statement

**Implement Quick Sort**, a Divide and Conquer algorithm, to sort an array, `arr[]` in **ascending** order.
Given an array `arr[]`, with starting index `low` and ending index `high`, complete the functions **`partition()`** and **`quickSort()`**.

Use the **last element as the pivot**, so that all elements **less than or equal to** the pivot come before it, and elements **greater than** the pivot follow it.

**Note:** `low` and `high` are inclusive.

---

## Examples

### Example 1

**Input:** `arr[] = [4, 1, 3, 9, 7]`
**Output:** `[1, 3, 4, 7, 9]`
**Explanation:** After sorting, all elements are arranged in ascending order.

### Example 2

**Input:** `arr[] = [2, 1, 6, 10, 4, 1, 3, 9, 7]`
**Output:** `[1, 1, 2, 3, 4, 6, 7, 9, 10]`
**Explanation:** Duplicate elements (1) are retained in sorted order.

### Example 3

**Input:** `arr[] = [5, 5, 5, 5]`
**Output:** `[5, 5, 5, 5]`
**Explanation:** All elements are identical, so the array remains unchanged.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(n)`  *(due to recursion stack in the worst/average case depending on implementation and pivot selection).*

---

## Company Tags

VMWare, Amazon, Microsoft, Samsung, Hike, Ola Cabs, Goldman Sachs, Adobe, SAP Labs, Qualcomm, HSBC, Grofers, Target Corporation

---

## Topic Tags

Divide and Conquer, Sorting, Algorithms

---

## Related Interview Experiences

* Qualcomm Interview Experience Set 9 Experienced Linkedin Invite

---

## Related Articles

* Iterative Quick Sort
* Quick Sort Algorithm

---

---

Here’s a tight, interview-ready package for **Quick Sort** with the required method names and several useful variants.

---

## 2) Explanation + step-by-step dry run

### Core idea (Lomuto partition, pivot = last element)

* Choose `pivot = arr[high]`.
* Maintain `i = low-1` = “end of ≤ pivot region”.
* Scan `j` from `low` to `high-1`:

  * If `arr[j] ≤ pivot`, grow the region: `i += 1; swap(arr[i], arr[j])`.
* Finally put the pivot in its correct place: `swap(arr[i+1], arr[high])` and return `i+1`.
* Recurse on the two halves: `[low … p-1]` and `[p+1 … high]`.

**Complexities**

* Average: `O(n log n)` time, `O(log n)` stack space (recursion).
* Worst (already sorted, all equal & bad pivot): `O(n^2)` time, `O(n)` stack.
* Not **stable**.

### Dry run on `arr = [4, 1, 3, 9, 7]`

1. `quickSort(arr,0,4)`
   `partition(0,4)`, pivot `7`

   * `i=-1`
   * `j=0: 4 ≤ 7` → `i=0`, swap(0,0) → `[4,1,3,9,7]`
   * `j=1: 1 ≤ 7` → `i=1`, swap(1,1) → `[4,1,3,9,7]`
   * `j=2: 3 ≤ 7` → `i=2`, swap(2,2) → `[4,1,3,9,7]`
   * `j=3: 9 ≤ 7`? no
   * Final: swap(i+1=3, high=4) → `[4,1,3,7,9]` ; return `p=3`
     Recurse on `[0..2]` and `[4..4]` (right is size 1 → base case).

2. `quickSort(arr,0,2)`
   `partition(0,2)`, pivot `3`

   * `i=-1`
   * `j=0: 4 ≤ 3`? no
   * `j=1: 1 ≤ 3` → `i=0`, swap(0,1) → `[1,4,3,7,9]`
   * Final: swap(i+1=1, high=2) → `[1,3,4,7,9]`; return `p=1`
     Recurse on `[0..0]` and `[2..2]` (both base cases).

Array is now **`[1, 3, 4, 7, 9]`**.

---

## 3) Python solutions (multiple ways, interview-friendly)

### A) Standard recursive QuickSort (Lomuto, pivot = last) — **most expected**

```python
class Solution:
    def quickSort(self, arr, low, high):
        """
        Recursive QuickSort using Lomuto partition (pivot = arr[high]).
        Time (avg): O(n log n); Worst: O(n^2)
        Space: recursion stack O(log n) avg, O(n) worst
        """
        if low < high:
            p = self.partition(arr, low, high)  # pivot index in correct place
            self.quickSort(arr, low, p - 1)     # sort left side
            self.quickSort(arr, p + 1, high)    # sort right side

    def partition(self, arr, low, high):
        """
        Lomuto partition:
          - arr[high] is pivot
          - i separates (≤ pivot) and (> pivot)
        Returns: final pivot index
        Time: O(high - low + 1), Space: O(1)
        """
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):         # scan all but the pivot
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        # place pivot after the last element ≤ pivot
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
```

### B) Tail-recursion optimized QuickSort (recurse on smaller half first)

* Same partitioning, but **loop** on the larger side to cap stack depth to `O(log n)`.

```python
class SolutionTailOptimized:
    def quickSort(self, arr, low, high):
        """
        Tail recursion elimination: always recurse on the smaller partition,
        then iterate (adjust low/high) on the larger. Stack depth: O(log n) worst.
        """
        while low < high:
            p = self.partition(arr, low, high)
            # Recurse on smaller side; iterate on the bigger side
            if p - low < high - p:
                self.quickSort(arr, low, p - 1)
                low = p + 1                # tail-call elimination
            else:
                self.quickSort(arr, p + 1, high)
                high = p - 1

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
```

### C) Iterative QuickSort using an explicit stack (no recursion)

```python
class SolutionIterative:
    def quickSort(self, arr, low, high):
        """
        Explicit stack simulates recursion.
        Time: O(n log n) avg, Space: O(log n) for the stack
        """
        stack = [(low, high)]
        while stack:
            l, h = stack.pop()
            if l < h:
                p = self.partition(arr, l, h)
                # push larger side first to keep stack shallow
                if p - 1 - l > h - (p + 1):
                    stack.append((l, p - 1))
                    stack.append((p + 1, h))
                else:
                    stack.append((p + 1, h))
                    stack.append((l, p - 1))

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
```

### D) Bonus: 3-way QuickSort (Dutch National Flag) — great with many duplicates

```python
class SolutionThreeWay:
    def quickSort(self, arr, low, high):
        """
        3-way partitioning:
          < pivot | == pivot | > pivot
        Reduces to ~O(n) on arrays with many equal keys.
        """
        if low >= high: return
        lt, i, gt = low, low, high
        pivot = arr[high]  # could randomize
        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]; lt += 1; i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]; gt -= 1
            else:  # equal
                i += 1
        self.quickSort(arr, low, lt - 1)
        self.quickSort(arr, gt + 1, high)

    # Not used; the partitioning is embedded above to keep <,==,> regions.
    def partition(self, arr, low, high):
        raise NotImplementedError("Not used in 3-way version")
```

> In most interviews, implement **A** (clean Lomuto). Mention **B** (tail recursion) and/or **D** (3-way) to show depth, especially if duplicates or worst-case behavior come up.

---

## 4) Interviewer-style Q\&A

**Q1. Why does Lomuto work with `≤ pivot`?**
Using `≤` ensures all values equal to the pivot go to the left partition, which is fine (and often preferable for stability of recursion). The final swap places the pivot after the last `≤` element, so everything left is `≤`, everything right is `>`.

**Q2. What are QuickSort’s time and space complexities?**
Average time **`O(n log n)`**, worst **`O(n^2)`** (e.g., already sorted with last-element pivot). Space is recursion stack: **`O(log n)`** average, **`O(n)`** worst.

**Q3. How to avoid the worst case?**
Randomize the pivot or use **median-of-three** (pick median of `low`, `mid`, `high`). Also apply **tail recursion optimization** (recurse on smaller half first) to cap stack depth.

**Q4. Lomuto vs Hoare?**

* **Lomuto** (this problem): simple, scans once, swaps more, pivot ends at returned index.
* **Hoare**: two pointers moving inward; fewer swaps; pivot not guaranteed to be at its final index; returns a split point. Both are `O(n)` per partition.

**Q5. Is QuickSort stable? In-place?**
Not stable by default. It **is** in-place (O(1) extra) aside from stack.

**Q6. What about many duplicate keys?**
Standard two-way partition degrades (lots of unnecessary work). Use **3-way partitioning** (Dutch National Flag) to group `== pivot` elements in the middle; performance improves to near linear on equal-key runs.

**Q7. When would you prefer Merge Sort over QuickSort?**
When you need **stability**, guaranteed `O(n log n)` time, or are sorting linked lists. Merge sort costs `O(n)` extra memory on arrays.

**Q8. Can you implement QuickSort iteratively?**
Yes—use an explicit stack (see variant **C**). Push the larger side first to keep the stack shallow.

---

---

Here’s a **full, runnable Python program** for **Quick Sort** (pivot = last element, Lomuto partition) that:

* prints outputs for a few **input arrays** (input → output),
* contains **inline time & space complexity comments for each step**, and
* **benchmarks** the full quicksort run using `timeit` in `main`.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quick Sort (ascending) — Lomuto partition with last element as pivot.

We implement the exact interface:

class Solution:
    def quickSort(self, arr, low, high): ...
    def partition(self, arr, low, high): ...

Complexities:
  Partition (per call):  Time O(high-low+1), Space O(1)
  QuickSort (overall):   Average Time O(n log n), Worst Time O(n^2)
                         Recursion stack Space O(log n) avg, O(n) worst

This script:
  1) Demonstrates sorting on small sample arrays (prints input → output).
  2) Benchmarks the algorithm with timeit on a larger random array.
"""

from __future__ import annotations
import random
import timeit
from typing import List


class Solution:
    def quickSort(self, arr: List[int], low: int, high: int) -> None:
        """
        Recursive QuickSort using **Lomuto** partition with last element as pivot.

        Steps per recursive call:
          A) Base-case check: if low >= high, subarray has 0/1 element -> already sorted.
             Time:  O(1)  | Space: O(1)
          B) Partition subarray arr[low..high] around pivot arr[high]; pivot lands at index p.
             Time:  O(high-low+1) | Space: O(1)
          C) Recurse on left [low..p-1] and right [p+1..high].
             Average depth O(log n) -> average extra space O(log n)
        """
        if low < high:  # A) O(1)
            p = self.partition(arr, low, high)  # B) O(size of subarray)
            self.quickSort(arr, low, p - 1)     # C) sort left
            self.quickSort(arr, p + 1, high)    # C) sort right

    def partition(self, arr: List[int], low: int, high: int) -> int:
        """
        Lomuto partition (pivot = arr[high]).

        Invariant:
          - arr[low..i]   <= pivot     (i starts at low-1; grows rightward)
          - arr[i+1..j-1] >  pivot
          - arr[j..high-1] are unprocessed
        After the loop, swap arr[i+1] with the pivot at arr[high] and return i+1.

        Time:  O(high - low + 1)  (single linear scan)
        Space: O(1)               (in-place swaps)
        """
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):          # visit each element once -> O(n_sub)
            if arr[j] <= pivot:             # keep ≤ pivot to the left part
                i += 1
                if i != j:                  # swap only when needed
                    arr[i], arr[j] = arr[j], arr[i]
        # put pivot after last ≤ element; now left ≤ pivot < right
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


# ------------------------------- Demo & Benchmark -------------------------------

def demo_on_samples() -> None:
    """
    Demonstrate sorting on a few arrays.
    Total time proportional to sum(n_i log n_i) for the examples.
    Extra space: recursion stack only (O(log n_i) per example on average).
    """
    samples = [
        [4, 1, 3, 9, 7],                # basic case
        [2, 1, 6, 10, 4, 1, 3, 9, 7],    # with duplicates
        [5, 5, 5, 5],                    # all equal
        [10, -3, 0, 8, -1, 7, 7, 2],     # negatives & duplicates
    ]

    sorter = Solution()
    print("=== Sample Runs (Input → Output) ===")
    for arr in samples:
        data = list(arr)
        sorter.quickSort(data, 0, len(data) - 1)
        print(f"Input : {arr}")
        print(f"Output: {data}")
        print("-" * 60)


def _bench_once(base: List[int]) -> None:
    """
    Helper for timeit:
      - Copy the base array so each run sorts the same unsorted data -> O(n) copy.
      - Run QuickSort on the copy -> O(n log n) average.
    """
    arr = list(base)                                # O(n) copy
    Solution().quickSort(arr, 0, len(arr) - 1)      # O(n log n) average


def benchmark() -> None:
    """
    Measure end-to-end sort time using `timeit`.
    Prep outside timing:
      - Build a random array of size SIZE -> O(SIZE) time/space.

    Timed region:
      - For each run: copy + quickSort -> O(n) + O(n log n).
    """
    SIZE = 50_000                 # choose size that runs comfortably with recursion
    rng = random.Random(123)
    base = [rng.randrange(-10**6, 10**6) for _ in range(SIZE)]  # O(SIZE)

    runs = 3
    total = timeit.timeit(lambda: _bench_once(base), number=runs)

    print("=== Benchmark (QuickSort with Lomuto) ===")
    print(f"Array size : {SIZE}")
    print(f"Runs       : {runs}")
    print(f"Total time : {total:.6f} s")
    print(f"Avg / run  : {total / runs:.6f} s")
    print("-" * 60)


def main() -> None:
    # 1) Show outputs for concrete inputs (includes inputs & outputs)
    demo_on_samples()

    # 2) Benchmark the optimized implementation with timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## Real-World Use Cases (short & important)

1. **Databases / Query Engines (in-memory sorts)**
   QuickSort’s in-place behavior and strong average performance make it a standard choice for sorting small/medium in-memory partitions before merges/joins.

2. **Systems / Embedded Sorting**
   When memory is tight and stability isn’t required, QuickSort’s **O(1) extra space** (beyond recursion) and good cache behavior are ideal.

3. **Graphics / Computational Geometry**
   Sorting primitives (e.g., edges, events) by key (x/y/time). QuickSort is simple, fast in practice, and widely used in preprocessing steps.

4. **Compiler / Toolchains**
   Sorting symbol tables or intermediate structures in-memory where speed and low memory overhead matter more than stability.
