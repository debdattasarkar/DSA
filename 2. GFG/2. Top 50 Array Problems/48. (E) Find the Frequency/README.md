# Find the Frequency

**Difficulty:** Easy
**Accuracy:** 77.19%
**Submissions:** 89K+
**Points:** 2

---

## Problem Statement

Given an array `arr` of positive integers and an integer `x`. Return the **frequency** of `x` in the array.

---

## Examples

### Example 1

**Input:** `arr = [1, 1, 1, 1, 1], x = 1`
**Output:** `5`
**Explanation:** Frequency of `1` is `5`.

### Example 2

**Input:** `arr = [1, 2, 3, 3, 2, 1], x = 2`
**Output:** `2`
**Explanation:** Frequency of `2` is `2`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^5`
* `1 ≤ x ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Google

---

## Topic Tags

STL

---

## Related Articles

* [Find Frequency Number Array](https://www.geeksforgeeks.org/find-frequency-number-array/)

---

---

here’s an interview-ready bundle for **Find the Frequency**.

---

# 2) Explanation + step-by-step dry run

## What to do

You’re given an array `arr` and a value `x`. Count how many elements equal `x`.

### Straightforward idea (most general)

Scan the array once, increment a counter whenever you see `x`.

* **Time:** `O(n)` (look at each element once)
* **Aux space:** `O(1)` (just a counter)

### When the array is **sorted** (bonus)

If `arr` is sorted, you can use binary search (`bisect_left/right`) to get the first and last position of `x`, and subtract.

* **Time:** `O(log n)`
* **Space:** `O(1)`

### When there are **many queries** on the same array (x changes)

Precompute a frequency table (hash map) once: `O(n)` build, then each query answers in `O(1)`.

---

## Dry run (linear scan) on `arr = [1, 2, 3, 3, 2, 1], x = 2`

* `count = 0`
* Look at `1` → not `2` → `count = 0`
* Look at `2` → match → `count = 1`
* Look at `3` → no → `count = 1`
* Look at `3` → no → `count = 1`
* Look at `2` → match → `count = 2`
* Look at `1` → no → `count = 2`

Return **2**.

---

# 3) Python solutions (brute + optimized variants)

```python
"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        """
        Single-pass linear scan (works for any array).
        Time:  O(n)
        Space: O(1)
        """
        cnt = 0
        for v in arr:           # visit each element once
            if v == x:          # O(1) comparison
                cnt += 1
        return cnt
```

### Variant A: Pythonic one-liner (same complexity)

```python
class SolutionPythonic:
    def findFrequency(self, arr, x):
        # Time: O(n), Space: O(1) extra (ignoring Python internals)
        return sum(1 for v in arr if v == x)
```

### Variant B: Many queries on the same array → precompute with a dict

```python
from collections import Counter

class SolutionManyQueries:
    def __init__(self, arr):
        # Precompute once: O(n) time, O(k) space where k unique values
        self.freq = Counter(arr)

    def findFrequency(self, _, x):
        # O(1) per query
        return self.freq.get(x, 0)
```

### Variant C: Array is **sorted** → use binary search

```python
import bisect

class SolutionSorted:
    def findFrequency(self, arr, x):
        """
        Requires 'arr' to be sorted in non-decreasing order.
        Time:  O(log n)
        Space: O(1)
        """
        left  = bisect.bisect_left(arr, x)      # first index >= x
        right = bisect.bisect_right(arr, x)     # first index >  x
        return right - left                     # number of x's
```

### Variant D (Brute baseline): Nested loops (educational only)

Not really necessary here; counting is already O(n). The “brute” is essentially the linear scan above. A *bad* brute would be `arr.count(x)` in a loop for multiple queries, giving `O(qn)`; instead use the Counter for multiple queries.

---

# 4) Interviewer-style Q\&A

**Q1. What are the time and space complexities of your primary approach?**
Linear scan is **O(n)** time, **O(1)** extra space.

**Q2. How would you optimize if the array is sorted?**
Use binary search to find the first and last position of `x` (`bisect_left/right`) and subtract: **O(log n)** time, **O(1)** space.

**Q3. What if there are many frequency queries on the same array?**
Precompute a **Counter** (hash map) in **O(n)** time; then each query is **O(1)**.

**Q4. Any edge cases?**

* `x` not present → return `0`.
* `arr` length 1 → return `1` if `arr[0]==x` else `0`.
* Large `n` (up to `1e5`) → linear scan is perfectly fine.

**Q5. Does using `arr.count(x)` differ from manual counting?**
Both are `O(n)`. In interviews, it’s fine to mention `arr.count(x)`; but showing the explicit loop demonstrates understanding and portability across languages.

**Q6. Can negative numbers or zeros appear?**
The prompt says “positive integers”, but the methods above work for any hashable comparable values (including 0/negatives).

---

---


Absolutely—here’s a **full, runnable Python program** for **Find the Frequency** that:

* implements the standard **O(n)** linear scan (interview-favorite),
* shows **inputs → outputs** for sample cases,
* and **benchmarks** with `timeit` (including a “many queries” comparison).

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Find the Frequency of x in an array.

Primary approach: single-pass linear scan.
Big-O:
  • Time  : O(n) — touch each element once
  • Space : O(1) — only a counter (output not counted)

Also included:
  • Many-queries optimization using Counter (precompute once → O(1)/query)
  • Sorted-array optimization using binary search (O(log n))
"""

from __future__ import annotations
import random
import timeit
import bisect
from collections import Counter
from typing import List


# -----------------------------------------------------------------------------
# Required interface
# -----------------------------------------------------------------------------
class Solution:
    def findFrequency(self, arr: List[int], x: int) -> int:
        """
        Linear scan — works for any array (sorted or not).
        Steps:
          A) Initialize counter -> O(1) time/space
          B) For each value v in arr:
               if v == x: increment counter -> each comparison O(1)
             Overall -> O(n) time, O(1) extra space
          C) Return counter -> O(1)
        """
        cnt = 0                   # A) O(1)
        for v in arr:             # B) loop runs n times -> O(n)
            if v == x:            #    O(1) comparison
                cnt += 1
        return cnt                # C) O(1)


# -----------------------------------------------------------------------------
# Optional reference variants
# -----------------------------------------------------------------------------
class SolutionSorted:
    """Use when arr is sorted: O(log n) using binary search."""
    def findFrequency(self, arr: List[int], x: int) -> int:
        # First index >= x
        left = bisect.bisect_left(arr, x)     # O(log n)
        # First index > x
        right = bisect.bisect_right(arr, x)   # O(log n)
        return right - left                   # O(1)


class SolutionManyQueries:
    """
    Optimize for many queries on the same array:
    Build frequency map once: O(n) time, O(k) space (k = #unique values).
    Each query becomes O(1).
    """
    def __init__(self, arr: List[int]):
        self.freq = Counter(arr)              # O(n) build

    def findFrequency(self, _arr_ignored: List[int], x: int) -> int:
        return self.freq.get(x, 0)            # O(1) per query


# -----------------------------------------------------------------------------
# Demo & Benchmark
# -----------------------------------------------------------------------------
def demo_on_samples() -> None:
    """
    Show correctness on a few inputs.
    Time: sum O(n) over the small samples; Space: O(1) extra.
    """
    samples = [
        ([1, 1, 1, 1, 1], 1, 5),
        ([1, 2, 3, 3, 2, 1], 2, 2),
        ([42], 7, 0),
        ([5, 4, 5, 6, 5, 8], 5, 3),
    ]
    sol = Solution()
    print("=== Sample Runs (Input → Output) ===")
    for arr, x, expected in samples:
        out = sol.findFrequency(arr, x)       # O(n)
        print(f"arr = {arr}, x = {x}")
        print(f"Output  : {out}")
        print(f"Expected: {expected}")
        print("-" * 60)


def _bench_linear(arr: List[int], x: int) -> None:
    """Timeit target for the O(n) linear scan."""
    Solution().findFrequency(arr, x)


def _bench_many_queries(arr: List[int], queries: List[int]) -> None:
    """
    Timeit target for many queries:
      - Build Counter once (O(n))
      - Answer q queries (O(q))
    """
    mq = SolutionManyQueries(arr)
    for x in queries:
        _ = mq.findFrequency(arr, x)


def benchmark() -> None:
    """
    Benchmark the linear scan and the many-queries optimization.

    Input generation (outside timing):
      - n up to 1e5 (problem constraint), values up to 1e5
      - We choose a random x that likely appears multiple times.

    Timed regions:
      - Linear: one O(n) pass per run.
      - Many-queries: O(n) build + O(q) queries per run.
    """
    rng = random.Random(2025)
    n = 100_000
    MAXV = 100_000
    arr = [rng.randrange(1, MAXV + 1) for _ in range(n)]  # O(n) build

    # Choose a value from arr to avoid worst-case (zero hits)
    x = rng.choice(arr)

    runs = 5
    t_linear = timeit.timeit(lambda: _bench_linear(arr, x), number=runs)

    # Many-queries scenario: q = 5000 different x's
    q = 5_000
    queries = [rng.randrange(1, MAXV + 1) for _ in range(q)]  # O(q)
    t_many = timeit.timeit(lambda: _bench_many_queries(arr, queries), number=runs)

    print("=== Benchmark ===")
    print(f"n (array size) : {n}, MAXV: {MAXV}")
    print(f"Runs           : {runs}")
    print(f"Linear scan    : total {t_linear:.6f}s | avg/run {t_linear/runs:.6f}s")
    print(f"Many-queries   : total {t_many:.6f}s | avg/run {t_many/runs:.6f}s "
          f"(includes O(n) Counter build each run)")
    print("-" * 60)


def main() -> None:
    # 1) Demonstrate with explicit inputs (prints input values and outputs)
    demo_on_samples()

    # 2) Benchmark solutions using timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (short & important)

1. **Analytics & telemetry** – Count occurrences of a specific event code/ID in logs or streams (e.g., how many times status `200` appears).

2. **Inventory lookups** – Determine how many items of a given SKU are present in a list/inventory snapshot.

3. **Search query monitoring** – Frequency of a particular keyword/hashtag in a batch of messages/tweets.

4. **Spam/abuse detection** – Count appearances of a suspicious token in message batches before deeper analysis.
