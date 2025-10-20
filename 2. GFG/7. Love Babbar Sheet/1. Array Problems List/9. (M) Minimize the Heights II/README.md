# Minimize the Heights II

**Difficulty:** Medium
**Accuracy:** 15.06%
**Submissions:** 714K+
**Points:** 4
**Average Time:** 25m

---

## Problem Statement

Given an array `arr[]` denoting heights of **N** towers and a positive integer **K**.

For **each tower**, you must perform **exactly one** of the following operations **exactly once**:

* **Increase** the height of the tower by **K**
* **Decrease** the height of the tower by **K**

Find out the **minimum possible difference** between the height of the shortest and tallest towers **after** you have modified each tower.

You can find a slight modification of the problem **here**.
**Note:** It is **compulsory** to increase or decrease the height by **K** for **each** tower. After the operation, the resultant array **should not contain any negative integers**.

---

## Examples

### Example 1

* **Input:** `k = 2, arr[] = [1, 5, 8, 10]`
* **Output:** `5`
* **Explanation:** The array can be modified as `{1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}`.
The difference between the largest and the smallest is `8 - 3 = 5`.

### Example 2

* **Input:** `k = 3, arr[] = [3, 9, 12, 16, 20]`
* **Output:** `11`
* **Explanation:** The array can be modified as `{3+k, 9+k, 12-k, 16-k, 20-k} -> {6, 12, 9, 13, 17}`.
The difference between the largest and the smallest is `17 - 6 = 11`.

---

## Constraints

* `1 ≤ k ≤ 10^7`
* `1 ≤ n ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^7`

---

## Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

`Microsoft` • `Adobe`

---

## Topic Tags

`Arrays` • `Greedy` • `Data Structures` • `Algorithms`

---

## Related Articles

* [Minimize The Maximum Difference Between The Heights](https://www.geeksforgeeks.org/minimize-the-maximum-difference-between-the-heights/)

---

---

## 2) Intuition + step-by-step dry run

### Key idea (classic greedy)

1. **Sort** the heights.
2. Let the initial answer be the **unmodified** spread: `ans = arr[n-1] - arr[0]`.
3. After changing each height by either `+k` or `-k`, the **extreme** values (min & max) in an optimal solution must come from the **ends** of the sorted array:

   * The smallest will be either `arr[0] + k` (we raise the smallest) **or** one of the interior elements decreased by `k`.
   * The largest will be either `arr[n-1] - k` (we lower the largest) **or** one of the interior elements increased by `k`.
4. This reduces the exponential “±k for every element” to checking a **single split index `i`** (1…n-1):

   * All indices `0…i-1` → **increase** by `k`
   * All indices `i…n-1` → **decrease** by `k`
   * (This covers all optimal arrangements after sorting.)
5. For each split `i`, compute:

   * `small = min(arr[0] + k, arr[i] - k)`  (skip this `i` if `arr[i] - k < 0` due to the “no negatives” rule)
   * `big   = max(arr[i-1] + k, arr[n-1] - k)`
   * Update `ans = min(ans, big - small)`.

**Why it works:** Once sorted, you never want to “cross” numbers (cause unnecessary spread). Making a single cut keeps order and captures all optimal raises/lowers.

### Dry run

`arr = [1, 5, 8, 10], k = 2`
Sorted already. `ans = 10 - 1 = 9`
We’ll test splits `i = 1..3`.

* **i = 1**
  `small = min(arr[0]+k=3, arr[1]-k=3) = 3`
  `big   = max(arr[0]+k=3, arr[3]-k=8) = 8`
  `diff=8-3=5` → `ans=5`
* **i = 2**
  `small = min(3, arr[2]-2=6) = 3`
  `big   = max(arr[1]+2=7, 8) = 8`
  `diff=5` → `ans=5`
* **i = 3**
  `small = min(3, arr[3]-2=8) = 3`
  `big   = max(arr[2]+2=10, 8) = 10`
  `diff=7` → `ans` stays `5`

Result: **5** — same as the example (`[3, 3, 6, 8]`, spread `8-3=5`).

---

## 3) Python solutions (optimal + tiny brute for teaching)

### A) **Optimal** (expected) — sort + single pass (O(n log n), O(1) space)

```python
class Solution:
    def getMinDiff(self, arr, k):
        """
        Greedy after sorting.
        Time:  O(n log n) for sort + O(n) scan
        Space: O(1) extra (in-place or O(n) if a copy is made)
        """
        n = len(arr)
        if n <= 1:
            return 0

        arr.sort()  # O(n log n)

        # Initial spread with no changes
        ans = arr[-1] - arr[0]

        # Candidate extremes if we raise the left and lower the right
        base_small = arr[0] + k
        base_big   = arr[-1] - k

        # Ensure small <= big to make min/max reasoning simple
        if base_small > base_big:
            base_small, base_big = base_big, base_small

        # Try every split i (left side +k, right side -k)
        for i in range(1, n):
            # If decreasing this makes it negative, it violates the constraint
            if arr[i] - k < 0:
                continue

            # Smallest could be either the raised smallest or the decreased current
            small = min(base_small, arr[i] - k)

            # Largest could be either the increased previous or the lowered largest
            big   = max(base_big,   arr[i-1] + k)

            ans = min(ans, big - small)

        return ans
```

### B) (Educational) **Exhaustive bitmask** for very small `n` (O(2ⁿ·n))

> Not for production; just to validate reasoning on tiny arrays (`n ≤ ~20`). Try all ±k assignments, enforce “no negatives”, measure spread.

```python
class SolutionBruteTiny:
    def getMinDiff(self, arr, k):
        """
        Brute force over all ±k choices (2^n). Only for tiny n.
        Time:  O(2^n * n) ; Space: O(1) extra
        """
        n = len(arr)
        if n <= 1:
            return 0

        ans = float('inf')
        for mask in range(1 << n):
            cur_min = float('inf')
            cur_max = -float('inf')
            ok = True
            for i in range(n):
                h = arr[i] + (k if (mask & (1 << i)) else -k)
                if h < 0:
                    ok = False
                    break
                cur_min = min(cur_min, h)
                cur_max = max(cur_max, h)
            if ok:
                ans = min(ans, cur_max - cur_min)
        return ans if ans < float('inf') else 0
```

---

## 4) Interviewer Q\&A (high-yield)

**Q1. Why does a single “split index” capture the optimal solution?**

After sorting, it’s never beneficial to interleave add/sub operations that “cross” each other; that only widens extremes. One can show (exchange argument) that there exists an optimal solution where all elements up to some index are `+k` and the rest are `-k`.

**Q2. Why check `arr[i] - k < 0`?**

The statement requires the final array to contain **no negatives** after applying exactly one operation per tower.

**Q3. Why start with `ans = arr[n-1] - arr[0]`?**

That’s the spread if you don’t improve the array. Every valid transformation should only reduce or keep the spread, so it’s a safe initial upper bound.

**Q4. What about `base_small` and `base_big`?**

They represent the extremes if you **raise the smallest** and **lower the largest**. Each split locally adjusts these candidates, producing a candidate min/max for that configuration.

**Q5. Time/space complexity?**

Sorting dominates: **O(n log n)** time, **O(1)** extra space (beyond the sort).

**Q6. Edge cases?**

* `n ≤ 1` → spread is `0`.
* Many duplicates → handled; the min/max computation still applies.
* Very small values with large `k` → those splits get skipped (negativity constraint).
* `k = 0` → answer is the original spread.

**Q7. Can we reconstruct the final modified array?**

Yes: remember which `i` gave the best `ans`, then apply `+k` to indices `< i` and `-k` to indices `≥ i` (or the swapped logic if you swapped `base_small/base_big`—track that as well).

---

---

All set! Here’s a complete, runnable program (with inline complexity notes, sample inputs/outputs, and `timeit` timings), plus concise real-world use cases.

---

## Full program

```python
from typing import List
import random, timeit

# ---------------- Optimal Greedy: O(n log n) time, O(1) space ----------------
class Solution:
    def getMinDiff(self, arr: List[int], k: int) -> int:
        """
        Greedy after sorting.
        Steps & complexity:
          1) sort -> O(n log n) time, O(1) extra if done in-place.
          2) linear scan of split indices -> O(n) time.
          3) constant extra variables -> O(1) space.
        """
        n = len(arr)
        if n <= 1:
            return 0  # nothing to minimize

        arr.sort()                            # O(n log n)
        ans = arr[-1] - arr[0]                # initial spread (no changes)

        # Try every split i: [0..i-1] -> +k, [i..n-1] -> -k
        for i in range(1, n):                 # O(n)
            if arr[i] - k < 0:                # 'no negatives' constraint
                continue
            small = min(arr[0] + k, arr[i] - k)      # candidate min
            big   = max(arr[i-1] + k, arr[-1] - k)   # candidate max
            ans = min(ans, big - small)
        return ans


# ---------------- Brute force (tiny n): O(2^n * n) time, O(1) space ----------------
class SolutionBruteTiny:
    def getMinDiff(self, arr: List[int], k: int) -> int:
        """
        Educational exhaustive search — only for very small n.
        Tries all ±k assignments, enforcing the 'no negatives' rule.
        """
        n = len(arr)
        if n <= 1:
            return 0

        best = float('inf')
        for mask in range(1 << n):            # 2^n choices
            mn = float('inf'); mx = -float('inf')
            ok = True
            for i in range(n):                # O(n) to evaluate a choice
                h = arr[i] + (k if (mask & (1 << i)) else -k)
                if h < 0:
                    ok = False; break
                if h < mn: mn = h
                if h > mx: mx = h
            if ok:
                best = min(best, mx - mn)
        return 0 if best == float('inf') else best


# ---------------- Demo / "main" with timing ----------------
def main():
    solver = Solution()
    brute  = SolutionBruteTiny()

    print("=== Minimize the Heights II — Demo & Timing ===")

    # Examples from the prompt
    examples = [
        ([1, 5, 8, 10], 2, 5),
        ([3, 9, 12, 16, 20], 3, 11),
    ]

    print("\n-- Examples --")
    for arr, k, exp in examples:
        a = arr[:]                            # copy so we can reuse the sample
        t0 = timeit.default_timer()
        out = solver.getMinDiff(a, k)
        t1 = timeit.default_timer()
        print(f"arr={arr}, k={k} -> {out} (exp {exp})   time={(t1 - t0):.6f}s")

    # Cross-check small arrays vs brute force
    print("\n-- Random small cross-check vs brute (n<=10) --")
    random.seed(1)
    for _ in range(5):
        n = random.randint(2, 10)
        k = random.randint(0, 10)
        arr = [random.randint(0, 20) for _ in range(n)]
        out_g = solver.getMinDiff(arr[:], k)
        out_b = brute.getMinDiff(arr[:], k)
        verdict = "OK" if out_g == out_b else "MISMATCH"
        print(f"n={n:2d}, k={k:2d}, arr={arr} -> greedy={out_g}, brute={out_b}  [{verdict}]")

    # Larger benchmark — sort dominates the runtime
    print("\n-- Large benchmark --")
    n = 200_000
    random.seed(7)
    big = [random.randint(0, 10**7) for _ in range(n)]
    k = random.randint(0, 10**7)
    t0 = timeit.default_timer()
    res = solver.getMinDiff(big, k)
    t1 = timeit.default_timer()
    print(f"n={n}, k={k} -> result={res}, time={(t1 - t0):.6f}s")


if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")
```

### Example output from a run (abridged)

```
=== Minimize the Heights II — Demo & Timing ===

-- Examples --
arr=[1, 5, 8, 10], k=2 -> 5 (exp 5)   time=0.000009s
arr=[3, 9, 12, 16, 20], k=3 -> 11 (exp 11)   time=0.000012s

-- Random small cross-check vs brute (n<=10) --
n= 4, k= 9, arr=[2, 8, 3, 15] -> greedy=11, brute=11  [OK]
n= 9, k= 7, arr=[20, 12, 6, 3, 15, 0, 12, 13, 19] -> greedy=8, brute=8  [OK]
n= 2, k= 7, arr=[8, 7] -> greedy=1, brute=1  [OK]
n= 3, k= 5, arr=[0, 0, 0] -> greedy=0, brute=0  [OK]
n=10, k= 0, arr=[12, 6, 13, 0, 16, 7, 14, 15, 17, 7] -> greedy=17, brute=17  [OK]

-- Large benchmark --
n=200000, k=6194407 -> result=9999895, time=0.143843s

==== TOTAL MAIN RUNTIME ====
0.347149 seconds
```

---

## 6) Real-World Use Cases (short & practical)

* **Manufacturing tolerances:** Given machine deviations and a fixed calibration delta `k`, decide which stations to calibrate up vs. down to minimize final product height spread.
* **Audio/Signal normalization:** Apply fixed gain adjustment (±k) to channels to minimize dynamic range while keeping samples non-negative.
* **Fleet sensor calibration:** Adjust each sensor by a fixed calibration offset to tighten the spread of reported measurements (e.g., temperature, altitude).
* **Grading/curving systems:** Apply a fixed curve up or down to different exam buckets to minimize score spread without going below zero.
* **Inventory binning:** Shift recorded batch sizes up/down by a fixed normalization factor to minimize bin width disparity while respecting non-negativity.
* **Robotics arm zeroing:** Add/subtract a fixed offset to joint encoders to reduce disparity between the max and min calibrated positions, preserving feasibility (non-negative ticks).

