# Sum Except First and Last

**Difficulty:** Basic
**Accuracy:** 34.83%
**Submissions:** 125K+
**Points:** 1

---

You are given an array `arr` of numbers. Return the sum of all the elements except the first and last elements.

---

## Examples

### Example 1

**Input:** `arr[] = [5, 24, 39, 60, 15, 28, 27, 40, 50, 90]`
**Output:** `283`
**Explanation:** The sum of all the elements except the first and last element is 283.

### Example 2

**Input:** `arr[] = [5, 10, 1, 11]`
**Output:** `11`
**Explanation:** The sum of all the elements except the first and last element is 11.

### Example 3

**Input:** `arr[] = [5, 10]`
**Output:** `0`
**Explanation:** The sum of all the elements except the first and last element is 0.

---

## Constraints

* `2 <= arr.size() <= 10^5`
* `2 <= arr[i] <= 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Amazon • Microsoft

---

## Topic Tags

Dynamic Programming • Greedy • Algorithms

---

---

# Sum Except First and Last — Explanation, Dry Run & Python Solutions

## 2) Idea & Dry Run

**Goal:** return the sum of all elements **except** the first and the last.

* If `n == 2` → nothing to sum → return `0`.
* Otherwise, we can:

  * sum the whole array once and subtract the ends: `sum(arr) - arr[0] - arr[-1]`, or
  * iterate from index `1` to `n-2` and add up.

**Dry run (Example 1)**
`arr = [5, 24, 39, 60, 15, 28, 27, 40, 50, 90]`
Total = 5+24+39+60+15+28+27+40+50+90 = 378
Answer = `378 - 5 - 90 = 283` ✅

**Dry run (Example 2)**
`arr = [5, 10, 1, 11]` → total=27 → `27 - 5 - 11 = 11` ✅

**Dry run (Example 3)**
`arr = [5, 10]` → return `0`.

> Optimal complexity is **O(n)** time and **O(1)** extra space.

---

## 3) Python solutions (interview-ready, with inline comments)

### A) One-pass, subtract ends (clean & fastest in Python)

```python
class Solution:
    def sumExceptFirstLast(self, arr):
        # Parr:  list of pair
        n = len(arr)                      # O(1)
        if n <= 2:                        # O(1) — edge case
            return 0
        # Use built-in sum once; Python sums in O(n).
        # Extra space: O(1).
        return sum(arr) - arr[0] - arr[-1]
```

### B) Manual loop without summing the ends (no reliance on whole-array sum)

```python
class Solution:
    def sumExceptFirstLast(self, arr):
        # Parr:  list of pair
        n = len(arr)
        if n <= 2:
            return 0
        total = 0                         # O(1)
        # Single pass over middle elements: O(n)
        for i in range(1, n - 1):
            total += arr[i]
        # Time: O(n); Space: O(1)
        return total
```

### C) Readable slice + sum (note: creates a slice)

```python
class Solution:
    def sumExceptFirstLast(self, arr):
        # Parr:  list of pair
        n = len(arr)
        if n <= 2:
            return 0
        # sum over a slice; slice creation is O(n) time and O(n) extra memory
        # (copies the middle section). Still fine for many interview settings,
        # but less memory-efficient than A/B.
        return sum(arr[1:-1])
```

---

## 4) Interview Q&A

**Q1. What’s the optimal time and space complexity?**
**A.** `O(n)` time, `O(1)` extra space (e.g., `sum(arr) - arr[0] - arr[-1]` or a single pass over indices `1..n-2`).

**Q2. Is the problem asking to exclude the *smallest* and *largest* values?**
**A.** No. It explicitly says exclude the **first** and **last** elements in the array order. Sorting would change the meaning.

**Q3. Any edge cases?**
**A.** `n <= 2` → return `0`. Works with negative numbers as well; logic is unchanged.

**Q4. Why not use `sum(arr[1:-1])` always?**
**A.** It’s concise, but it creates a new list slice (extra **O(n)** memory). `sum(arr) - arr[0] - arr[-1]` avoids the copy.

**Q5. Will Python overflow for large sums?**
**A.** No—Python integers are arbitrary-precision.

---

---

Done — the full program just ran and printed inputs, outputs, and `timeit` timings for three approaches.

### What you’ve got

* **Approach A (Subtract-Ends)**: `sum(arr) - arr[0] - arr[-1]` — cleanest, O(n) time, O(1) extra space.
* **Approach B (Manual Loop)**: iterate indices `1..n-2` — also O(n) time, O(1) space.
* **Approach C (Slice + Sum)**: `sum(arr[1:-1])` — O(n) time but uses O(n) extra memory due to slicing.

```python

# Re-run after kernel reset: include all code again and execute.
from typing import List
import timeit
import random

class SolutionSumSubtract:
    def sumExceptFirstLast(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 2:
            return 0
        return sum(arr) - arr[0] - arr[-1]

class SolutionManualLoop:
    def sumExceptFirstLast(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 2:
            return 0
        total = 0
        for i in range(1, n - 1):
            total += arr[i]
        return total

class SolutionSliceSum:
    def sumExceptFirstLast(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 2:
            return 0
        return sum(arr[1:-1])

def time_call(fn, *args, repeat=5, number=1):
    result = fn(*args)
    timer = timeit.Timer(lambda: fn(*args))
    best = min(timer.repeat(repeat=repeat, number=number))
    return result, best

tests = [
    {"arr": [5, 24, 39, 60, 15, 28, 27, 40, 50, 90], "expected": 283},
    {"arr": [5, 10, 1, 11], "expected": 11},
    {"arr": [5, 10], "expected": 0},
    {"arr": [1, 2, 3], "expected": 2},
]

random.seed(0)
big_arr = [random.randint(2, 10**5) for _ in range(100_000)]
tests.append({"arr": big_arr, "expected": sum(big_arr) - big_arr[0] - big_arr[-1]})

def run_and_report():
    print("=== Sum Except First and Last — Full Program ===\n")
    s1 = SolutionSumSubtract()
    s2 = SolutionManualLoop()
    s3 = SolutionSliceSum()

    for idx, t in enumerate(tests, 1):
        arr, exp = t["arr"], t["expected"]
        n = len(arr)
        show = arr if n <= 12 else f"[{arr[0]}, {arr[1]}, ..., {arr[-2]}, {arr[-1]}] (n={n})"
        print(f"Test #{idx}: arr={show}")

        r1, t1 = time_call(lambda a: s1.sumExceptFirstLast(a), arr)
        print(f"  Subtract-Ends : result={r1}, expected={exp}, best={t1:.6f}s")

        r2, t2 = time_call(lambda a: s2.sumExceptFirstLast(a), arr)
        print(f"  Manual-Loop   : result={r2}, expected={exp}, best={t2:.6f}s")

        r3, t3 = time_call(lambda a: s3.sumExceptFirstLast(a), arr)
        print(f"  Slice+Sum     : result={r3}, expected={exp}, best={t3:.6f}s")

        print(f"  All agree? {r1 == r2 == r3 == exp}\n")

run_and_report()

```

All three agree on results. For the big test (`n=100000`), subtract-ends was the fastest in Python.

If you need a minimal interview-ready class with the requested signature:

```python
class Solution:
    def sumExceptFirstLast(self, arr):
        # Parr:  list of pair
        n = len(arr)                  # O(1)
        if n <= 2:                    # O(1) edge
            return 0
        # One pass sum + constant-time subtractions
        # Time:  O(n)
        # Space: O(1)
        return sum(arr) - arr[0] - arr[-1]
```

---

## Real-World Use Cases (important ones)

* **Analytics windows:** compute totals excluding known sentinel/boundary records (e.g., first/last timestamps in a session that are incomplete).
* **Data cleaning:** ignore header/footer markers embedded in numeric logs while aggregating.
* **Finance:** sum of intra-day transactions excluding the opening/closing auction prints.
* **Sensor streams:** aggregate mid-sample readings excluding potentially noisy warm-up/cool-down readings at the boundaries.
