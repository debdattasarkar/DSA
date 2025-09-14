# Common in 3 Sorted Arrays

**Difficulty:** Easy
**Accuracy:** 22.16%
**Submissions:** 431K+
**Points:** 2

---

## Problem Statement

Given three sorted arrays in **non-decreasing** order, print **all common elements** in **non-decreasing** order across these arrays. If there are no such elements, return an empty array. In this case, the output will be `-1`.

**Note:** Can you handle the duplicates without using any additional Data Structure?

---

## Examples

### Example 1

**Input:**
`arr1 = [1, 5, 10, 20, 40, 80]` , `arr2 = [6, 7, 20, 80, 100]` , `arr3 = [3, 4, 15, 20, 30, 70, 80, 120]`
**Output:** `[20, 80]`
**Explanation:** `20` and `80` are the only common elements in `arr`, `brr` and `crr`.

### Example 2

**Input:**
`arr1 = [1, 2, 3, 4, 5]` , `arr2 = [6, 7]` , `arr3 = [8, 9, 10]`
**Output:** `[-1]`
**Explanation:** There are no common elements in `arr`, `brr` and `crr`.

### Example 3

**Input:**
`arr1 = [1, 1, 1, 2, 2, 2]` , `arr2 = [1, 1, 2, 2, 2]` , `arr3 = [1, 1, 1, 2, 2, 2, 2]`
**Output:** `[1, 2]`
**Explanation:** We do not need to consider duplicates.

---

## Constraints

* `1 ≤ arr1.size(), arr2.size(), arr3.size() ≤ 10^5`
* `-10^5 ≤ arr1_i, arr2_i, arr3_i ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

VMWare, Microsoft, MAQ Software

---

## Topic Tags

Searching, Algorithms

---

## Related Interview Experiences

* Microsoft Interview Experience Set 58 For Software Engineer

---

## Related Articles

* [Find Common Elements Three Sorted Arrays](https://www.geeksforgeeks.org/find-common-elements-three-sorted-arrays/)

---

---

here’s an interview-ready pack for **Common Elements in 3 Sorted Arrays**.

---

# 2) Explanation + step-by-step dry run

## Core idea (3 pointers, skip duplicates)

Because all three arrays are **sorted non-decreasing**, walk them simultaneously:

* Let `i, j, k` be indices in `arr1, arr2, arr3`.
* If `arr1[i] == arr2[j] == arr3[k]`, append it to `ans`, then **advance all three** and **skip further duplicates** of that value.
* Otherwise, **advance the pointer(s) with the smallest value** (again skipping duplicates) until values may match.

This works in **O(n1 + n2 + n3)** time and **O(1)** extra space (besides output), while naturally handling duplicates.

### Dry run (Example 1)

```
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
i=j=k=0, ans=[]

Compare 1,6,3 -> min=1  -> move i past all 1s -> i=1
Compare 5,6,3 -> min=3  -> move k past all 3s -> k=1
Compare 5,6,4 -> min=4  -> move k past all 4s -> k=2
Compare 5,6,15-> min=5  -> i++ -> i=2
Compare 10,6,15-> min=6 -> j++ -> j=1 (7)
Compare 10,7,15-> min=7 -> j++ -> j=2 (20)
Compare 10,20,15-> min=10-> i++ -> i=3 (20)
Compare 20,20,15-> min=15-> k++ -> k=3 (20)
Compare 20,20,20 -> equal -> ans=[20]; i=4,j=3,k=4
Compare 40,80,30-> min=30-> k++ -> k=5 (70)
Compare 40,80,70-> min=40-> i++ -> i=5 (80)
Compare 80,80,70-> min=70-> k++ -> k=6 (80)
Compare 80,80,80 -> equal -> ans=[20,80]; i=6,j=4,k=7
Stop (i out).  Result = [20, 80]
```

---

# 3) Python solutions (optimized + alternatives)

```python
# User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        """
        Three-pointer sweep with duplicate skipping.
        Time:  O(n1 + n2 + n3)
        Space: O(1) extra (besides the result list)
        Returns: list of common elements in non-decreasing order,
                 or [-1] if none.
        """
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        i = j = k = 0
        ans = []

        while i < n1 and j < n2 and k < n3:
            a, b, c = arr1[i], arr2[j], arr3[k]

            # If all equal, record once and skip duplicates in all arrays
            if a == b == c:
                ans.append(a)
                val = a
                # advance i/j/k past all occurrences of 'val'
                while i < n1 and arr1[i] == val: i += 1
                while j < n2 and arr2[j] == val: j += 1
                while k < n3 and arr3[k] == val: k += 1
            else:
                # find current minimum value
                m = min(a, b, c)
                # advance any pointer(s) equal to the minimum, skipping duplicates
                if a == m:
                    va = a
                    while i < n1 and arr1[i] == va: i += 1
                if b == m:
                    vb = b
                    while j < n2 and arr2[j] == vb: j += 1
                if c == m:
                    vc = c
                    while k < n3 and arr3[k] == vc: k += 1

        return ans if ans else [-1]
```

### Alternative A — Hashing (simple, but uses extra space)

* Build `set2 = set(arr2)` and `set3 = set(arr3)` (which also dedupes).
* Walk `arr1`, append `x` if `x in set2 and x in set3`, while skipping duplicates in `arr1`.

```python
class SolutionHash:
    def commonElements(self, arr1, arr2, arr3):
        """
        Hash-set membership.
        Time:  O(n1 + n2 + n3) average
        Space: O(n2 + n3)
        """
        set2, set3 = set(arr2), set(arr3)
        ans = []
        prev = None
        for x in arr1:
            if x == prev:          # skip duplicate in arr1
                continue
            if x in set2 and x in set3:
                ans.append(x)
            prev = x
        return ans if ans else [-1]
```

### Alternative B — Binary search the other two arrays for each distinct element of the smallest array

* Choose the shortest array (say `A`), and `bisect` search `x` in `B` and `C`.
* Skip duplicates while scanning `A`.

```python
import bisect

class SolutionBinarySearch:
    def commonElements(self, arr1, arr2, arr3):
        """
        For each distinct element in the smallest array,
        binary-search in the other two arrays.
        Time:  O(n_small * (log n_mid + log n_large))
        Space: O(1)
        """
        A, B, C = arr1, arr2, arr3
        # reorder so A is the smallest to minimize work
        if len(B) < len(A): A, B = B, A
        if len(C) < len(A): A, C = C, A
        if len(C) < len(B): B, C = C, B

        ans = []
        prev = None
        for x in A:
            if x == prev:          # skip duplicates in A
                continue
            # check presence via binary search
            i = bisect.bisect_left(B, x)
            if i == len(B) or B[i] != x:
                prev = x
                continue
            j = bisect.bisect_left(C, x)
            if j == len(C) or C[j] != x:
                prev = x
                continue
            ans.append(x)
            prev = x

        return ans if ans else [-1]
```

---

# 4) Interviewer-style Q\&A

**Q1. Why does the 3-pointer approach run in O(n1+n2+n3)?**
Because each pointer only **moves forward** and never backtracks. Every increment discards at least one element forever; therefore we do at most `n1+n2+n3` advances.

**Q2. How do you avoid duplicates without extra space?**
Whenever you consume a value (either on match or when advancing the minimum side), **skip all its consecutive duplicates** by advancing that pointer until the value changes.

**Q3. What if arrays aren’t sorted?**
Sorting first gives `O(n log n)` per array and then the same pointer sweep. Or use hash sets for `O(n)` average time with extra space.

**Q4. If there are no common elements, what do we return?**
Per the prompt style, return `[-1]`. (If your judge expects an empty list, just return `[]` instead.)

**Q5. Can you generalize to *k* sorted arrays?**
Yes. Maintain `k` pointers; at each step find the **min** and **max** of current values. If all equal → record & advance all; else advance **all pointers at the min value**, skipping duplicates. This is still linear in the total length.

**Q6. Space–time trade-offs?**

* **Pointers (no DS):** `O(total)` time, `O(1)` extra space.
* **Hashing:** simpler code, average `O(total)` time, but `O(n2+n3)` space.
* **Binary search variant:** `O(n_small log n_mid + n_small log n_large)` time, `O(1)` space.

**Q7. Edge cases?**
Empty array (then answer is `[-1]`), all elements identical, negative numbers, very large ranges. The pointer method handles all as long as arrays are sorted.

---

---

Here’s a **full, runnable Python program** for **Common Elements in 3 Sorted Arrays** that:

* prints outputs for several **input arrays** (input → output),
* includes **inline time & space complexity notes for every step**, and
* **benchmarks** the optimized solution using `timeit` right inside `main`.

```python
#!/usr/bin/env python3
"""
Common in 3 Sorted Arrays
Return all values that appear in arr1, arr2, and arr3 (each sorted non-decreasing),
with duplicates removed and results in non-decreasing order. If none, return [-1].

Core solution: 3-pointer sweep + duplicate skipping (no extra DS).
Why it works: arrays are sorted; advancing the pointer(s) with the smallest
current value discards values that cannot match later. Skipping duplicates
prevents repeated work and repeated outputs.

Complexities:
  - Time:  O(n1 + n2 + n3)     (each pointer advances at most its array length)
  - Space: O(1) extra          (besides the output list)
"""

from __future__ import annotations
import random
import timeit
from typing import List


# -------------------------------------------------------------------
# User function Template for python3
# -------------------------------------------------------------------
class Solution:
    def commonElements(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        """
        Three-pointer sweep with duplicate skipping.

        Steps (with per-step complexities):
          A) Init i, j, k = 0 (pointers into arr1/arr2/arr3)
             Time:  O(1)   Space: O(1)
          B) While all pointers are in range:
               - If arr1[i] == arr2[j] == arr3[k]:
                     append once, then advance each pointer past all duplicates of that value
                 Else:
                     let m = min(arr1[i], arr2[j], arr3[k]);
                     advance any pointer(s) whose current value equals m,
                     skipping duplicates (since those cannot match later)
             Time:  O(n1 + n2 + n3)   Space: O(1)
          C) If ans empty, return [-1], else ans
             Time:  O(1)   Space: O(1)
        """
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        i = j = k = 0
        ans: List[int] = []

        # B) Linear sweep over all three arrays — O(n1+n2+n3)
        while i < n1 and j < n2 and k < n3:
            a, b, c = arr1[i], arr2[j], arr3[k]

            if a == b == c:
                ans.append(a)
                # Skip all duplicates of this value in each array
                val = a
                while i < n1 and arr1[i] == val: i += 1
                while j < n2 and arr2[j] == val: j += 1
                while k < n3 and arr3[k] == val: k += 1
            else:
                m = min(a, b, c)
                # Advance every pointer at the minimum value, skipping duplicates
                if a == m:
                    va = a
                    while i < n1 and arr1[i] == va: i += 1
                if b == m:
                    vb = b
                    while j < n2 and arr2[j] == vb: j += 1
                if c == m:
                    vc = c
                    while k < n3 and arr3[k] == vc: k += 1

        # C) Return result or [-1] when empty — O(1)
        return ans if ans else [-1]


# ------------------------------- Demo & Benchmark -------------------------------

def demo_on_samples() -> None:
    """
    Show correctness on a few inputs.
    Overall time: proportional to total sizes of sample arrays (linear).
    Extra space: O(1) besides the outputs.
    """
    samples = [
        # (arr1, arr2, arr3, expected)
        ([1, 5, 10, 20, 40, 80],
         [6, 7, 20, 80, 100],
         [3, 4, 15, 20, 30, 70, 80, 120],
         [20, 80]),

        ([1, 2, 3, 4, 5],
         [6, 7],
         [8, 9, 10],
         [-1]),

        ([1, 1, 1, 2, 2, 2],
         [1, 1, 2, 2, 2],
         [1, 1, 1, 2, 2, 2, 2],
         [1, 2]),
    ]

    sol = Solution()
    print("=== Sample Runs (Input → Output) ===")
    for a1, a2, a3, expected in samples:
        out = sol.commonElements(a1, a2, a3)  # O(n1+n2+n3)
        print(f"arr1: {a1}\narr2: {a2}\narr3: {a3}")
        print(f"Output  : {out}")
        print(f"Expected: {expected}")
        print("-" * 60)


def _bench_once(arr1: List[int], arr2: List[int], arr3: List[int]) -> None:
    """
    Helper for timeit: run only the algorithm in the timed section.
    """
    Solution().commonElements(arr1, arr2, arr3)


def _make_sorted_array(size: int, rng: random.Random, low: int, high: int) -> List[int]:
    """
    Build a non-decreasing array of given size with values in [low, high].
    Done outside the timed region.
    Time:  O(size log size) for sorting
    Space: O(size)
    """
    arr = [rng.randrange(low, high + 1) for _ in range(size)]
    arr.sort()
    return arr


def benchmark() -> None:
    """
    Benchmark the O(n1+n2+n3) algorithm using timeit.

    Prep (outside timing):
      - Generate three sorted arrays (possibly with duplicates) of size SIZE.

    Timed region:
      - Run commonElements once per iteration on the same arrays.
    """
    SIZE = 100_000   # each array size; adjust if you want faster/slower runs
    rng = random.Random(123)

    # Build inputs once (not counted in timing)
    arr1 = _make_sorted_array(SIZE, rng, -100_000, 100_000)
    arr2 = _make_sorted_array(SIZE, rng, -100_000, 100_000)
    arr3 = _make_sorted_array(SIZE, rng, -100_000, 100_000)

    runs = 3
    total = timeit.timeit(lambda: _bench_once(arr1, arr2, arr3), number=runs)

    print("=== Benchmark (3-pointers O(n1+n2+n3), O(1) extra) ===")
    print(f"Sizes  : n1=n2=n3={SIZE}")
    print(f"Runs   : {runs}")
    print(f"Total  : {total:.6f} s")
    print(f"Avg/run: {total / runs:.6f} s")
    print("-" * 60)


def main() -> None:
    # 1) Demonstrate on sample inputs
    demo_on_samples()

    # 2) Benchmark the optimized solution with timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## Real-World Use Cases (short & important)

1. **Search/IR postings intersection**
   Intersect three sorted posting lists (e.g., users who searched term A, clicked B, and purchased C). The 3-pointer sweep is exactly how inverted-index engines intersect lists efficiently.

2. **Telemetry/log joins**
   Find IDs present in **all** of three sorted log streams (auth logs, API hits, billing events) to build reliable funnels without loading everything into hash tables.

3. **Bioinformatics / genomics**
   Identify genomic positions or variant IDs common to multiple sorted datasets (e.g., **SNPs** present in three different cohorts), where data often arrives pre-sorted by coordinate.
