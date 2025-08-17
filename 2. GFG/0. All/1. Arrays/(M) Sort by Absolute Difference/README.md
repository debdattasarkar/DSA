
---

# Sort by Absolute Difference

**Difficulty:** Medium
**Accuracy:** 27.77%
**Submissions:** 51K+
**Points:** 4
**Average Time:** 5m

---

## Problem Statement

You are given a number **x** and an array **arr\[]**. Your task is to rearrange the elements of the array according to the **absolute difference** with **x**, i.e., an element having minimum difference comes first, and so on.

**Note:** If two or more elements are at equal distances, arrange them in the same sequence as in the given array.

---

## Examples

**Input:**
x = 7, arr\[] = \[10, 5, 3, 9, 2]
**Output:**
\[5, 9, 10, 3, 2]
**Explanation:**
Sorting the numbers according to the absolute difference with 7, we have array elements as 5, 9, 10, 3, 2.

---

**Input:**
x = 6, arr\[] = \[1, 2, 3, 4, 5]
**Output:**
\[5, 4, 3, 2, 1]
**Explanation:**
Sorting the numbers according to the absolute difference with 6, we have array elements as 5, 4, 3, 2, 1.

---

## Constraints

* 1 ≤ x ≤ 10⁵
* 1 ≤ arr.size() ≤ 10⁵
* 1 ≤ arr\[i] ≤ 10⁵

---

## Expected Complexities

* **Time Complexity:** O(n log n)
* **Auxiliary Space:** O(1)

---

## Topic Tags

* Arrays
* Sorting
* Data Structures
* Algorithms

---

## Related Articles

* [Sort An Array According To Absolute Difference With Given Value](https://www.geeksforgeeks.org/sort-an-array-according-to-absolute-difference-with-given-value/)

---

---

Here’s everything you need, tidy and interview‑ready 👇

---

## 2) Explanation + Step‑by‑step dry run

### Problem recap

Given an array `arr` and a number `x`, rearrange `arr` so that elements appear in **increasing order of their absolute difference** to `x`. If two elements are **equally close**, keep them in the **same relative order** as in the original array (stable).

### Key ideas

* Sort by key = `abs(a - x)`.
* Stability matters for ties. Python’s `list.sort()` / `sorted()` is **stable**, so equal keys preserve original order automatically. (If using a language without stable sort, pair each value with its original index and use that as a tie‑breaker.)

### Dry run

Input: `x = 7`, `arr = [10, 5, 3, 9, 2]`

Compute diffs:

* 10 → |10–7| = 3
* 5  → |5–7|  = 2
* 3  → |3–7|  = 4
* 9  → |9–7|  = 2
* 2  → |2–7|  = 5

Sort by diff (stable for ties):

* diff 2: 5, 9   (order kept: 5 before 9)
* diff 3: 10
* diff 4: 3
* diff 5: 2

Result: **\[5, 9, 10, 3, 2]**

Another: `x = 6`, `arr = [1, 2, 3, 4, 5]`
Diffs: 5,4,3,2,1 → result **\[5, 4, 3, 2, 1]**.

---

## 3) Optimized Python solutions (brute & interview‑expected)

### A) Interview‑expected (stable sort by key) — O(n log n) time, O(1) extra\*

\*O(1) extra if sorting the array in-place; otherwise O(n) to build a new list.

```python
class Solution:
    def rearrange(self, arr, x):
        # Time: O(n log n) due to sort
        # Space: O(1) extra if sorting in place (Python's Timsort is in-place); otherwise O(n).
        # Python's sort is stable, so ties keep original order automatically.
        arr.sort(key=lambda a: abs(a - x))
        return arr
```

### B) Brute force (stable selection by minimal diff) — O(n²) time, O(1) space

```python
class Solution:
    def rearrange(self, arr, x):
        # Time: O(n^2) - selection-like process
        # Space: O(1)
        n = len(arr)
        for i in range(n):
            # find index of minimal |arr[j]-x| in [i..n-1];
            # first minimal keeps stability relative to earlier elements
            best = i
            best_diff = abs(arr[i] - x)
            for j in range(i + 1, n):
                d = abs(arr[j] - x)
                if d < best_diff:              # strictly smaller diff wins
                    best = j
                    best_diff = d
            # stable place by extracting best and inserting at i
            val = arr.pop(best)
            arr.insert(i, val)
        return arr
```

### C) Bucket (counting‑style, explicitly stable) — O(n + D) time, O(n + D) space

Where `D = max(|arr[i]-x|)`. Useful if `D` is small compared to `n log n`.

```python
from collections import defaultdict, deque

class Solution:
    def rearrange(self, arr, x):
        # Time: O(n + D) where D = max absolute difference
        # Space: O(n + D)
        if not arr:
            return arr
        diffs = [abs(a - x) for a in arr]
        D = max(diffs)
        buckets = [deque() for _ in range(D + 1)]  # index = diff
        for a in arr:                               # fill buckets in original order -> stability
            buckets[abs(a - x)].append(a)
        out = []
        for d in range(D + 1):
            out.extend(buckets[d])
        return out
```

---

## 4) Interviewer Q\&A (quick hits)

**Q1. How do you guarantee stability for equal absolute differences?**

* In Python, `sort` is stable; sorting with key `abs(a - x)` preserves input order for ties.
* In non‑stable sorts/languages, pair `(abs(a-x), original_index, value)` or perform a stable algorithm (e.g., stable mergesort).

**Q2. Time and space complexity of your main solution?**

* Sorting by key is `O(n log n)` time and `O(1)` extra memory in-place (Python’s Timsort). Returning a new list costs `O(n)` extra.

**Q3. Can we do better than `O(n log n)`?**

* If values are integers and `D = max(|a-x|)` is small, a bucket (counting)-style solution runs in `O(n + D)`. Otherwise, comparison sort lower bound applies.

**Q4. What edge cases do you consider?**

* Empty array; single element; all elements equal; all elements at same distance from `x` (must remain unchanged); very large `x` or values causing large diffs.

**Q5. Why not use a custom comparator comparing concatenations (like “largest number” problem)?**

* That’s a different problem. Here the ordering is solely `abs(a - x)` with stability on ties.

---

---

Here’s a ready-to-run script that:

* Implements the three approaches (Stable Sort, Bucket when range is small, and Brute/Selection).
* Annotates time & space at each step right in the code.
* Runs a small main with sample inputs and measures runtime via `timeit`.

---

```python
"""
Problem: Sort array by absolute difference from x (stable for ties)

We provide 3 approaches:

A) Stable Sort by Key (Interview-standard)
   Time:  O(n log n)
   Space: O(1) extra (in-place Timsort; returning a copy would be O(n))

B) Bucket (Counting-style, explicitly stable) when the max absolute diff D is small
   Time:  O(n + D)
   Space: O(n + D)

C) Brute / Stable-Selection (for pedagogy/testing)
   Time:  O(n^2)
   Space: O(1)
"""

from collections import deque
from timeit import timeit
import copy


class Solution:
    # -------------------------------
    # A) Stable sort by absolute diff
    # -------------------------------
    def rearrange_sort(self, arr, x):
        """
        Steps:
        1) Compute sort key on-the-fly: abs(a - x).  # Time per compare: O(1)
        2) Python's sort is stable, so ties keep original order automatically.
        Complexity:
            - Time: O(n log n) due to sorting.
            - Space: O(1) extra (Timsort is in-place aside from a small constant buffer).
        """
        arr.sort(key=lambda a: abs(a - x))  # stable
        return arr

    # -------------------------------------------------------
    # B) Bucket (Counting-like) when D = max(|a-x|) is small
    # -------------------------------------------------------
    def rearrange_bucket(self, arr, x):
        """
        Steps:
        1) Compute D = max |a - x|.                           # O(n)
        2) Allocate D+1 buckets (deque each) for stability.   # O(D)
        3) One pass: push each a into bucket[|a-x|].          # O(n)
        4) Concatenate buckets from diff 0..D.                # O(n + D)
        Complexity:
            - Time: O(n + D)
            - Space: O(n + D)
        """
        if not arr:
            return arr
        # Step 1: compute max diff — O(n)
        D = 0
        for a in arr:
            # |a - x| is O(1)
            diff = a - x if a >= x else x - a
            if diff > D:
                D = diff

        # Step 2: buckets — O(D)
        buckets = [deque() for _ in range(D + 1)]

        # Step 3: fill buckets preserving input order — O(n)
        for a in arr:
            buckets[abs(a - x)].append(a)

        # Step 4: flatten — O(n + D)
        out = []
        for d in range(D + 1):
            out.extend(buckets[d])

        # Write back to original list (optional, to keep signature similar)
        arr[:] = out
        return arr

    # --------------------------------------------
    # C) Brute / Stable Selection (pedagogical)
    # --------------------------------------------
    def rearrange_brutish(self, arr, x):
        """
        Idea: For position i, find first minimal |a-x| in arr[i:], then
              extract and insert at i (preserves stability).
        Complexity:
            - Time: O(n^2)
            - Space: O(1) (mutating list)
        """
        n = len(arr)
        for i in range(n):
            best = i
            best_diff = abs(arr[i] - x)
            # Find first minimal diff in [i..n-1] — O(n-i)
            for j in range(i + 1, n):
                d = abs(arr[j] - x)
                if d < best_diff:
                    best = j
                    best_diff = d
            # Extract + insert preserves earlier tie-order — amortized O(n)
            val = arr.pop(best)
            arr.insert(i, val)
        return arr


# ----------------------
# Demonstration + timeit
# ----------------------
def demo_once(method, arr, x, label):
    s = Solution()
    data = copy.deepcopy(arr)  # keep original intact across runs

    # One execution
    result = method(data, x)

    # Time multiple runs for a more stable measurement
    t = timeit(lambda: method(copy.deepcopy(arr), x), number=1000)

    print(f"{label}:")
    print(f"  Input arr = {arr}, x = {x}")
    print(f"  Output    = {result}")
    print(f"  Time (1000 runs) ≈ {t:.6f} s\n")


if __name__ == "__main__":
    # Sample inputs (you can change or add more)
    x1, arr1 = 7, [10, 5, 3, 9, 2]
    x2, arr2 = 6, [1, 2, 3, 4, 5]
    x3, arr3 = 10, [10, 9, 11, 8, 12, 10]

    # Methods to test
    s = Solution()
    tests = [
        (s.rearrange_sort, "Stable sort (O(n log n))"),
        (s.rearrange_bucket, "Bucket (O(n + D))"),
        (s.rearrange_brutish, "Brute selection (O(n^2))"),
    ]

    # Run on multiple inputs
    for method, label in tests:
        demo_once(method, arr1, x1, label)
        demo_once(method, arr2, x2, label)
        demo_once(method, arr3, x3, label)
```

### Example Output (will vary by machine)

```
Stable sort (O(n log n)):
  Input arr = [10, 5, 3, 9, 2], x = 7
  Output    = [5, 9, 10, 3, 2]
  Time (1000 runs) ≈ 0.004321 s

Stable sort (O(n log n)):
  Input arr = [1, 2, 3, 4, 5], x = 6
  Output    = [5, 4, 3, 2, 1]
  Time (1000 runs) ≈ 0.003980 s
...
```

---

## 6) Real-World Use Cases (high-impact)

1. **Recommendations by Similarity**
   Show products/users/documents ordered by distance to a target embedding/score, while preserving original ranking for ties. Stable ordering avoids jitter when equal scores occur.

2. **Nearest-Neighbor UI Lists**
   In geo apps (e.g., restaurants near me), sort by distance from the user’s location. If multiple places are at the same distance (e.g., same mall), keep their catalog ordering.

3. **Alert Prioritization**
   Security/ops dashboards often sort events by deviation from a threshold. Equal deviations preserve ingestion order so operators don’t see alerts “flip-flopping” on refresh.

4. **Cache Prefetching / Memory Heuristics**
   Rank pages/blocks by distance from a current pointer/offset and preserve trace order for equal distances to maintain predictable prefetch patterns.
