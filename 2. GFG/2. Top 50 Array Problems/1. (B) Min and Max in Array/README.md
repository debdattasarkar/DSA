
---

# Min and Max in Array

**Difficulty:** Basic
**Accuracy:** 68.55%
**Submissions:** 358K+
**Points:** 1
**Average Time:** 10m

---

## 🧾 Problem Statement

Given an array `arr`, your task is to find the **minimum** and **maximum** elements in the array.

> **Note:** Return a pair that contains two elements — the first one will be the minimum element and the second will be the maximum.

---

## 📘 Examples

### Example 1:

```
Input: arr[] = [3, 2, 1, 56, 10000, 167]
Output: 1 10000
Explanation: Minimum and maximum elements of array are 1 and 10000.
```

### Example 2:

```
Input: arr[] = [1, 345, 234, 21, 56789]
Output: 1 56789
Explanation: Minimum and maximum elements of array are 1 and 56789.
```

### Example 3:

```
Input: arr[] = [56789]
Output: 56789 56789
Explanation: Since the array contains only one element, both min & max are the same.
```

---

## 📌 Constraints

* `1 <= arr.size() <= 10^5`
* `1 <= arr[i] <= 10^9`

---

## ✅ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷️ Topic Tags

* Arrays
* Data Structures

---

## 📚 Related Articles

* Cpp Program To Find The Minimum And Maximum Element Of An Array
* Maximum And Minimum In An Array
* Min And Max In A List In Java

---

---

great pick—this is a classic you’ll see a lot. here’s the full interview-ready pack.

---

# 2) Explanation + step-by-step dry run

## Problem recap

Given an array `arr`, return **both** the minimum and maximum.
Constraints are large, so we should aim for **O(n) time** and **O(1) extra space**.

### Approaches you should know

1. **Brute (scan twice):**

   * `min(arr)` then `max(arr)` in two passes — simple but **2n − 2** comparisons.

2. **Single scan (most common in interviews):**

   * Track `min_val` and `max_val` in one pass — **2(n − 1)** comparisons.

3. **Pairwise / Tournament method (optimized comparisons):**

   * Compare elements **in pairs** to reduce total comparisons to about **3n/2** (precisely `3⌊n/2⌋` if n even, else `3⌊n/2⌋ + 2`).
   * Idea: first compare the two in a pair to decide local min/max, then compare those against global `min_val`/`max_val`.

All are linear; approach (3) minimizes comparisons (useful if comparisons are expensive).

---

## Dry run (Pairwise / Tournament)

Input: `arr = [3, 2, 1, 56, 10000, 167]`

* `n = 6` (even)
* Initialize by comparing the first pair `(3, 2)` → local min=2, max=3
  `min_val=2, max_val=3`
* Process remaining pairs:

1. Pair `(1, 56)` → local min=1, max=56

   * `min_val = min(2, 1) = 1`
   * `max_val = max(3, 56) = 56`

2. Pair `(10000, 167)` → local min=167, max=10000

   * `min_val = min(1, 167) = 1`
   * `max_val = max(56, 10000) = 10000`

**Result:** `(1, 10000)`

Comparisons count:

* 1 per pair to decide local order → 3 pairs → 3
* 2 per pair to update globals → 3 pairs × 2 = 6
* Total = **9 comparisons** vs single scan **10 comparisons** (2(n−1)=10) and two scans **10 comparisons**. For larger n the savings trend to ~25%.

---

# 3) Python solutions (with inline comments)

Return format: I’ll return a tuple `(min_val, max_val)` which is Pythonic and easy to unpack.
If your platform expects a list, just wrap: `[min_val, max_val]`.

### A) Two passes (brute, simplest)

```python
class Solution:
    def getMinMax(self, arr):
        """
        Two full scans.
        Time  : O(n) + O(n) = O(n)
        Space : O(1)
        """
        # Guard: array has at least one element per constraints
        min_val = arr[0]  # O(1)
        for x in arr[1:]:        # O(n)
            if x < min_val:
                min_val = x
        max_val = arr[0]
        for x in arr[1:]:        # O(n)
            if x > max_val:
                max_val = x
        return (min_val, max_val)
```

---

### B) One pass (most expected in interviews)

```python
class SolutionOnePass:
    def getMinMax(self, arr):
        """
        Single linear scan with two trackers.
        Time  : O(n)   (n-1 comparisons for min + n-1 for max interleaved; 2(n-1) total)
        Space : O(1)
        """
        min_val = max_val = arr[0]             # O(1)
        for x in arr[1:]:            # O(n-1)
            # One comparison to decide direction, then one update.
            if x < min_val:
                min_val = x
            elif x > max_val:
                max_val = x
        return (min_val, max_val)
```

---

### C) Pairwise / Tournament (optimized comparisons ≈ 1.5n)

```python
class SolutionTournament:
    def getMinMax(self, arr):
        """
        Pairwise comparisons to reduce total comparisons.
        Time  : O(n)  (≈ 1.5n comparisons)
        Space : O(1)
        """
        n = len(arr)
        # Handle first one or two elements to seed min_val/max_val and set start index
        if n % 2 == 0:
            # Even length: initialize by comparing first pair
            a, b = arr[0], arr[1]
            if a < b:
                min_val, max_val = a, b
            else:
                min_val, max_val = b, a
            i = 2
        else:
            # Odd length: start with first element as both min_val and max_val
            min_val = max_val = arr[0]
            i = 1

        # Process remaining elements in pairs
        while i < n:
            a, b = arr[i], arr[i + 1]
            # First compare within pair (1 comparison)
            if a < b:
                # Compare local min and max to globals (2 comparisons)
                if a < min_val:
                    min_val = a
                if b > max_val:
                    max_val = b
            else:
                if b < min_val:
                    min_val = b
                if a > max_val:
                    max_val = a
            i += 2

        return (min_val, max_val)
```

---

### D) Python built-ins (be honest about trade-off)

```python
class SolutionBuiltins:
    def getMinMax(self, arr):
        """
        Uses Python's built-ins.
        Time  : O(n) twice if done separately; or O(n) once with a single pass via reduce,
                but most readable is two calls. In CP setting, prefer explicit one-pass.
        Space : O(1)
        """
        return (min(arr), max(arr))
```

> In interviews, mention built-ins but implement **B** or **C**.

---

### Edge cases to test

* Single element: `[56789]` → `(56789, 56789)`
* All equal: `[5,5,5]` → `(5,5)`
* Monotonic increasing / decreasing
* Large values near limits

---

# 4) Interviewer-style Q&A

**Q1. What’s the optimal time and space complexity?**
**A.** Time **O(n)** (you must inspect every element); space **O(1)** auxiliary.

**Q2. How many comparisons does each method do?**
**A.**

* Two passes: `2n − 2` comparisons.
* One pass (track min_val/max_val): also `2n − 2` in worst case.
* Pairwise/tournament: about `1.5n` (exactly `3⌊n/2⌋` if even, else `3⌊n/2⌋ + 2`).

**Q3. Why does the pairwise method save comparisons?**
**A.** By first comparing the two elements in each pair, we avoid comparing both against both globals. We only compare the **smaller** of the pair to `min_val` and the **larger** to `max_val`, cutting one comparison per pair.

**Q4. When do you prefer the one-pass vs tournament method?**
**A.** If comparisons are cheap and clarity matters, one-pass is perfect. If comparisons are expensive (e.g., custom comparators on big objects), the tournament method’s reduced comparisons can help.

**Q5. Can we do better than O(n)?**
**A.** Not in the worst case. Decision-tree lower bounds require inspecting every element at least once to be certain of min and max.

**Q6. What about streaming data?**
**A.** Maintain running `min_val`/`max_val` as new items arrive—same one-pass logic; always O(1) update per item.

**Q7. Any pitfalls?**
**A.** Forgetting to initialize properly for odd/even lengths in the pairwise method; not handling single-element arrays; mixing up comparisons when updating globals.

---

---

awesome — here’s a **complete runnable Python program** that:

* reads an integer array from stdin (space-separated),
* computes **min & max** using three approaches (One-Pass, Tournament/Pairwise, Built-ins),
* prints the results,
* and **times** each with both a single wall-clock run and a `timeit` average.

Every major step includes **inline comments** describing **time/space complexity**.

---

## Full Program

```python
#!/usr/bin/env python3
"""
Min and Max in Array — Full Program with Timing and Inline Complexity Notes

Input format (single line):
  space-separated integers
Example:
  3 2 1 56 10000 167

Output:
  (min, max) for three approaches + timing
"""

from time import perf_counter
import timeit
import sys


# ------------------------------------------------------------
# Approach A: One-Pass scan (most expected in interviews)
# ------------------------------------------------------------
def get_min_max_one_pass(arr):
    """
    Single linear scan with two trackers.
    Time  : O(n)  -- touch each element once
    Space : O(1)  -- only two variables
    """
    min_val = max_val = arr[0]              # O(1)
    for x in arr[1:]:             # O(n-1)
        # 1 comparison to check if it's a new min;
        # if not, 1 comparison to check if it's a new max.
        if x < min_val:
            min_val = x
        elif x > max_val:
            max_val = x
    return min_val, max_val


# ------------------------------------------------------------
# Approach B: Tournament / Pairwise (fewer comparisons ≈ 1.5n)
# ------------------------------------------------------------
def get_min_max_tournament(arr):
    """
    Compare elements in pairs:
      - First compare within the pair (1 cmp),
      - Compare smaller to global min_val, larger to global max_val (2 cmps).
    Time  : O(n)     -- still linear work
    Space : O(1)
    """
    n = len(arr)
    if n % 2 == 0:
        a, b = arr[0], arr[1]
        if a < b: min_val, max_val = a, b
        else:     min_val, max_val = b, a
        i = 2
    else:
        min_val = max_val = arr[0]
        i = 1

    while i < n:                     # O(n/2) iterations
        a, b = arr[i], arr[i + 1]
        if a < b:                    # 1 comparison inside the pair
            if a < min_val: min_val = a        # compare local min to global min_val
            if b > max_val: max_val = b        # compare local max to global max_val
        else:
            if b < min_val: min_val = b
            if a > max_val: max_val = a
        i += 2
    return min_val, max_val


# ------------------------------------------------------------
# Approach C: Python built-ins (readable baseline)
# ------------------------------------------------------------
def get_min_max_builtins(arr):
    """
    Uses Python's built-ins.
    Time  : O(n) + O(n) if called separately (min + max), still linear.
    Space : O(1)   (ignoring Python iterator overhead)
    """
    return min(arr), max(arr)


# ------------------------------------------------------------
# Timing helpers
# ------------------------------------------------------------
def time_single_run(func, *args, **kwargs):
    """
    Single wall-clock timing using perf_counter.
    """
    t0 = perf_counter()
    result = func(*args, **kwargs)
    t1 = perf_counter()
    return result, (t1 - t0)


def time_with_timeit(stmt_callable, number=5):
    """
    Average runtime over `number` runs using timeit.
    """
    total = timeit.timeit(stmt_callable, number=number)
    return total / number


# ------------------------------------------------------------
# Main driver
# ------------------------------------------------------------
def main():
    # ---------- Input ----------
    # Read one line of integers; per constraints n >= 1
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        print("No input provided. Example: 3 2 1 56 10000 167")
        return
    arr = list(map(int, tokens))  # O(n) time, O(n) space for parsed ints

    print("Input array:", arr)

    # ---------- A: One-Pass ----------
    (min_val_a, max_val_a), t_a = time_single_run(get_min_max_one_pass, arr)
    avg_a = time_with_timeit(lambda: get_min_max_one_pass(arr), number=5)
    print("\n[One-Pass]        ->", (min_val_a, max_val_a))
    print(f"  Single-run time : {t_a:.8f} s")
    print(f"  Avg over 5 runs : {avg_a:.8f} s")

    # ---------- B: Tournament / Pairwise ----------
    (min_val_b, max_val_b), t_b = time_single_run(get_min_max_tournament, arr)
    avg_b = time_with_timeit(lambda: get_min_max_tournament(arr), number=5)
    print("\n[Tournament/Pair] ->", (min_val_b, max_val_b))
    print(f"  Single-run time : {t_b:.8f} s")
    print(f"  Avg over 5 runs : {avg_b:.8f} s")

    # ---------- C: Built-ins ----------
    (min_val_c, max_val_c), t_c = time_single_run(get_min_max_builtins, arr)
    avg_c = time_with_timeit(lambda: get_min_max_builtins(arr), number=5)
    print("\n[Built-ins]       ->", (min_val_c, max_val_c))
    print(f"  Single-run time : {t_c:.8f} s")
    print(f"  Avg over 5 runs : {avg_c:.8f} s")

    # ---------- Complexity Summary ----------
    print("\nComplexity Summary:")
    print("  One-Pass       : Time O(n), Space O(1)")
    print("  Tournament     : Time O(n), Space O(1), ~1.5n comparisons")
    print("  Built-ins      : Time O(n), Space O(1) (but two passes)")

if __name__ == "__main__":
    """
    Example:
      echo "3 2 1 56 10000 167" | python3 minmax.py
      -> (1, 10000)
    """
    main()
```

### Example run

Input:

```
3 2 1 56 10000 167
```

Output (your times will vary):

```
Input array: [3, 2, 1, 56, 10000, 167]

[One-Pass]        -> (1, 10000)
  Single-run time : 0.00000310 s
  Avg over 5 runs : 0.00000301 s

[Tournament/Pair] -> (1, 10000)
  Single-run time : 0.00000305 s
  Avg over 5 runs : 0.00000296 s

[Built-ins]       -> (1, 10000)
  Single-run time : 0.00000290 s
  Avg over 5 runs : 0.00000285 s

Complexity Summary:
  One-Pass       : Time O(n), Space O(1)
  Tournament     : Time O(n), Space O(1), ~1.5n comparisons
  Built-ins      : Time O(n), Space O(1) (but two passes)
```

---

## 6) Real-World Use Cases (high-value)

* **Streaming analytics / monitoring:** Maintain running min and max of telemetry (latency, CPU, stock ticks) in O(1) per update.
* **Graphics & geometry:** Compute **axis-aligned bounding boxes** (AABB) by tracking min/max x/y/z as vertices stream in.
* **Data quality & validation:** Quick sanity checks (e.g., min ≥ 0, max ≤ threshold) before expensive processing.
* **Compression & normalization:** Normalize values to `[0,1]` using `(x - min) / (max - min)`; min/max are first-pass stats.

> For interviews, implement **One-Pass** confidently, mention **Tournament** for reduced comparisons, and acknowledge built-ins for readability.
