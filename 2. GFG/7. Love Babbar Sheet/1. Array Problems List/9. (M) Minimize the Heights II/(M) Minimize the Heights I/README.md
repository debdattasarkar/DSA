
---

# 🏗️ Minimize the Heights I

**Difficulty:** Medium
**Accuracy:** 26.16%
**Submissions:** 120K+
**Points:** 4
**Average Time:** 25m

---

## 📘 Problem Statement

Given an array `arr[]` and a positive integer `k` denoting the heights of towers, you have to **modify the height of each tower** by **either increasing or decreasing** them by `k` — but **only once**.

Find out the **minimum possible difference** between the height of the **shortest** and **tallest** towers after modification.

> **Note:** The modified height of the tower can be negative.

---

## 🧩 Examples

### Example 1

**Input:**

```
arr[] = [1, 5, 8, 10], k = 2
```

**Output:**

```
5
```

**Explanation:**
The array can be modified as:
`[3, 3, 6, 8]`
The difference between the largest and the smallest is `8 - 3 = 5`.

---

### Example 2

**Input:**

```
arr[] = [3, 9, 12, 16, 20], k = 3
```

**Output:**

```
11
```

**Explanation:**
The array can be modified as:
`[6, 12, 9, 13, 17]`
The difference between the largest and the smallest is `17 - 6 = 11`.

---

## ⚙️ Constraints

```
1 ≤ k ≤ 10⁴
1 ≤ number of towers ≤ 10⁵
0 ≤ arr[i] ≤ 10⁵
```

---

## ⏱️ Expected Complexities

| Type                | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(n log n) |
| **Auxiliary Space** | O(1)       |

---

## 🏢 Company Tags

`Adobe`

---

## 🧵 Topic Tags

`two-pointer-algorithm` • `Arrays` • `Greedy` • `Data Structures` • `Algorithms`

---

---

# 2) Intuition + step-by-step dry run

## Problem (one line)

Given tower heights `arr[]` and an integer `k`, you may change **each** height **exactly once** by either `+k` or `-k`. Minimize `(max_height - min_height)` after all changes. (In this “I” version, heights may go **negative** — that’s fine.)

## Key idea (greedy that’s expected)

1. **Sort** the array.
2. If you add `k` to some prefix and subtract `k` from the rest, the extreme values after changes must be among:

   * left extreme: `min(arr[0] + k, arr[i] - k)`
   * right extreme: `max(arr[i-1] + k, arr[-1] - k)`
     for some split index `i` (1…n-1).
3. Try every split; keep the best (smallest) difference.

Why this works: after sorting, pushing the small values **up** (`+k`) and large values **down** (`-k`) is the only way to shrink the span. Any optimal assignment can be represented by one cut index between the two groups.

### Dry run 1

`arr = [1, 5, 8, 10], k = 2` → sorted already
Initial (no changes): `10 - 1 = 9`

Try splits:

* `i=1`:
  `small = min(1+2, 5-2) = min(3, 3) = 3`
  `big   = max(1+2, 10-2) = max(3, 8) = 8`
  diff = `8 - 3 = 5`  ← best so far

* `i=2`:
  `small = min(3, 8-2=6) = 3`
  `big   = max(5+2=7, 8) = 8`
  diff = `5` (same)

* `i=3`:
  `small = min(3, 10-2=8) = 3`
  `big   = max(8+2=10, 8) = 10`
  diff = `7`

Answer = **5**.

### Dry run 2

`arr = [3, 9, 12, 16, 20], k = 3`
Initial = `20 - 3 = 17`

Try `i=1..4` → best diff becomes **11** (e.g., at `i=2`: `small=min(3+3, 12-3=9)=6`, `big=max(9+3=12, 20-3=17)=17`, diff `11`).

---

# 3) Python — brute (for understanding) and optimized (expected)

Required signature:

```python
# User function Template for python3
class Solution:
    def getMinDiff(self, arr, k):
        # code here
```

### A) Optimized Greedy (expected) — `O(n log n)` time, `O(1)` extra

```python
# User function Template for python3
class Solution:
    def getMinDiff(self, arr, k):
        """
        Greedy (expected in interviews):
          1) Sort.
          2) Start with baseline answer (max - min).
          3) For each split i (1..n-1):
                left side gets +k, right side gets -k
             Compute min & max formed by borders and update best.
        Time  : O(n log n) for sort + O(n) scan
        Space : O(1) extra (in-place)
        """
        n = len(arr)
        if n <= 1:
            return 0
        arr.sort()  # O(n log n)

        # Baseline with no modifications
        best_diff = arr[-1] - arr[0]

        # If k == 0, nothing changes
        if k == 0:
            return best_diff

        # Scan all cut positions
        smallest_after_raise = arr[0] + k       # candidate when left side is raised
        largest_after_lower  = arr[-1] - k      # candidate when right side is lowered

        for i in range(1, n):
            # Left segment [0..i-1] uses +k, Right segment [i..n-1] uses -k
            min_height = min(smallest_after_raise, arr[i] - k)
            max_height = max(arr[i-1] + k,       largest_after_lower)
            best_diff = min(best_diff, max_height - min_height)

        return best_diff
```

> Note: Unlike “Heights II”, **we don’t skip** cases where `arr[i] - k < 0` because the problem allows negative heights.

---

### B) Brute force (educational) — `O(2^n * n)` time, `O(1)` extra

Try all `±k` assignments using bitmasks. Only for very small `n` (teaching/demo).

```python
class SolutionBrute:
    def getMinDiff(self, arr, k):
        """
        Brute force: try every ±k assignment.
        Time  : O(2^n * n)  -> infeasible for large n, only educational
        Space : O(1) extra
        """
        n = len(arr)
        if n <= 1:
            return 0
        best = float('inf')

        # Bitmask from 0..(2^n - 1): bit j=1 means +k, 0 means -k
        for mask in range(1 << n):
            mn = float('inf'); mx = -float('inf')
            for j in range(n):
                val = arr[j] + (k if (mask >> j) & 1 else -k)
                if val < mn: mn = val
                if val > mx: mx = val
            best = min(best, mx - mn)
        return best
```

---

# 4) Interview quick-recall + Q&A

## 30-second mnemonic — **“Sort → Split → Shrink”**

* **Sort** the heights.
* Move **left group up** (`+k`), **right group down** (`-k`).
* For every **Split** `i`, compute
  `min = min(arr[0]+k, arr[i]-k)` and `max = max(arr[i-1]+k, arr[-1]-k)`
  and **Shrink** the answer with `max - min`.

Say this out loud while coding:

> “Sort, baseline, scan cut i=1..n-1, min from (first+K or arr[i]-K), max from (arr[i-1]+K or last-K). Keep best.”

## High-yield Q&A

**Q1. Why does the single split cover all possibilities?**
Because after sorting, to reduce the span we’ll always **raise some prefix** and **lower the suffix**. Any interleaving assignment can be reordered without worsening extremes, so a single cut is sufficient.

**Q2. Complexity?**
`O(n log n)` for sorting; `O(n)` for scanning; `O(1)` extra space.

**Q3. What about negative heights?**
In **Heights I**, negative is **allowed** → no need to skip `arr[i]-k < 0`.
In **Heights II**, negative is disallowed, so you **skip** those splits.

**Q4. Edge cases?**

* `n <= 1`: answer `0`.
* `k == 0`: answer `max - min` (no change).
* Duplicate heights: algorithm still valid.

**Q5. How is “I” different from “II”?**
Heights **II** requires **every** tower to be modified and **no negatives**, so you add a guard `if arr[i] - k < 0: continue`. Logic otherwise is the same.

---

---

Perfect—here are (5) crisp, interview-friendly use cases, then a complete runnable Python program (with your requested signature, inline complexity notes, sample inputs/outputs, and timing via `perf_counter` + `timeit`).

---

## 5) Real-World Use Cases (easy to relate)

1. **Manufacturing tolerances:** Parts come in varying heights; you can machine each by ±k once. Choose directions to minimize tallest–shortest spread so parts fit together.

2. **Audio/Video normalization:** Per-track loudness/brightness can be raised or lowered by the same fixed gain k. Pick ±k per track to minimize perceived dynamic range variation.

3. **Network latencies normalization:** Each service’s latency can be optimized up/down by a fixed budget k (cache, QoS). Choose directions to minimize worst-case spread.

4. **Exam score moderation:** Apply ±k curve to each student once (policy constraint) to tighten score spread while preserving relative order as much as possible.

5. **Warehouse shelf leveling:** Every shelf can be shimmed up/down by k once; minimize max difference so robots handle fewer extreme lifts.

---

## 6) Full Program (optimized + brute, I/O + timings)

```python
#!/usr/bin/env python3
"""
Minimize the Heights I
----------------------
We may add or subtract 'k' from EACH height exactly once (negatives allowed).
Goal: minimize (max - min) after all changes.

Approaches:
  - Optimized Greedy (expected): O(n log n) time, O(1) space
  - Brute force (educational):   O(2^n * n) time, O(1) space  -> only for tiny n

The script:
  * Implements class Solution with getMinDiff(arr, k)  [greedy]
  * Implements class SolutionBrute for correctness demo on tiny arrays
  * Runs sample inputs and prints outputs
  * Times with perf_counter (single run) and timeit (averaged)
"""

from time import perf_counter
import timeit
from typing import List


# -------------------------------------------------------------------
# User function Template for python3 (OPTIMIZED / EXPECTED)
# -------------------------------------------------------------------
class Solution:
    def getMinDiff(self, arr: List[int], k: int) -> int:
        """
        Greedy (expected in interviews).
        Steps:
          1) Sort the array.                               -> O(n log n)
          2) Baseline answer = arr[-1] - arr[0].          -> O(1)
          3) For each split i in [1..n-1],                 -> O(n)
             left segment [0..i-1] uses +k,
             right segment [i..n-1] uses -k.
             New min = min(arr[0]+k, arr[i]-k)
             New max = max(arr[i-1]+k, arr[-1]-k)
             Update best difference.
        Time  : O(n log n)  (sort dominates)
        Space : O(1) extra  (in-place)
        """
        n = len(arr)
        if n <= 1:
            return 0

        arr.sort()  # O(n log n)
        best_diff = arr[-1] - arr[0]

        if k == 0:
            return best_diff

        smallest_after_raise = arr[0] + k
        largest_after_lower  = arr[-1] - k

        # Try every cut position once -> O(n)
        for i in range(1, n):
            # Note: In "Heights I", negatives are ALLOWED.
            min_height = min(smallest_after_raise, arr[i] - k)
            max_height = max(arr[i - 1] + k,   largest_after_lower)
            current = max_height - min_height
            if current < best_diff:
                best_diff = current

        return best_diff


# -------------------------------------------------------------------
# Brute force (educational / correctness for tiny n)
# -------------------------------------------------------------------
class SolutionBrute:
    def getMinDiff(self, arr: List[int], k: int) -> int:
        """
        Try every ±k assignment via bitmask.
        Time  : O(2^n * n) -- infeasible for large n
        Space : O(1) extra
        """
        n = len(arr)
        if n <= 1:
            return 0
        best = float('inf')
        for mask in range(1 << n):             # 0..2^n-1
            mn, mx = float('inf'), -float('inf')
            for i in range(n):
                val = arr[i] + (k if (mask >> i) & 1 else -k)
                if val < mn: mn = val
                if val > mx: mx = val
            if mx - mn < best:
                best = mx - mn
        return best


# --------------------------- Utilities -----------------------------
def run_case(name: str, arr: List[int], k: int, expected: int = None):
    print(f"\n-- {name} --")
    print("Input:", arr, "k =", k)

    # Single-run timings using perf_counter
    opt = Solution()
    t0 = perf_counter()
    out_opt = opt.getMinDiff(arr[:], k)      # use a copy to preserve input
    t1 = perf_counter()

    print("Optimized Output:", out_opt)
    if expected is not None:
        print("Expected        :", expected)
    print(f"Single-run time  : {(t1 - t0)*1e6:.2f} µs")

    # For tiny arrays we can compare against brute
    if len(arr) <= 18:  # guard to keep brute feasible
        brute = SolutionBrute()
        t2 = perf_counter()
        out_brute = brute.getMinDiff(arr[:], k)
        t3 = perf_counter()
        print("Brute Output    :", out_brute,
              f"(time {(t3 - t2)*1e6:.2f} µs)")
        print("Match?          :", out_opt == out_brute)

    # Averaged timings via timeit (more stable)
    def call_opt():
        opt.getMinDiff(arr[:], k)

    avg = timeit.timeit(call_opt, number=2000) / 2000
    print(f"Avg over 2000 runs: {avg*1e6:.2f} µs/run")


# ----------------------------- Main -------------------------------
def main():
    # Examples from prompt
    run_case("Example 1", [1, 5, 8, 10], k=2, expected=5)
    run_case("Example 2", [3, 9, 12, 16, 20], k=3, expected=11)

    # Extra tiny case (to show brute match)
    run_case("Tiny sanity", [7, 7], k=5, expected=0)
    run_case("Small random", [2, 6, 3], k=4)

if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"\n==== TOTAL PROGRAM RUNTIME: {(end - start):.6f} s ====")
```

**What you’ll see when you run it**

* For each case: input, optimized output (and expected when known).
* Brute output (for tiny arrays) to validate the greedy result.
* **Single-run microseconds** and **average µs/run** via `timeit`.
